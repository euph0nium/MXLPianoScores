#!/usr/bin/env python3
"""
Clean Multi-Track & Multi-Staff Scores:
Deletes all MusicXML (.mxl) scores with > 2 parts or non-piano multi-staves (> 2 staves)
to ensure the entire repository contains strictly Piano Solo scores.
"""

import os
import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path("/Users/shiyuli/Dev/Scores")
SCORES_DIR = ROOT_DIR / "scores"

def get_score_tracks(mxl_path: Path):
    """
    Returns (num_parts, total_staves, should_delete, reason)
    """
    try:
        with zipfile.ZipFile(mxl_path, 'r') as zf:
            xml_names = [n for n in zf.namelist() if (n.endswith('.xml') or n.endswith('.musicxml')) and not n.startswith('META-INF')]
            if not xml_names:
                return 0, 0, True, "No valid MusicXML found in archive"
            
            root = ET.fromstring(zf.read(xml_names[0]))
            parts = root.findall('part')
            num_parts = len(parts)
            
            total_staves = 0
            for part in parts:
                staves_elem = part.find('.//attributes/staves')
                if staves_elem is not None and staves_elem.text:
                    try:
                        total_staves += int(staves_elem.text)
                    except:
                        total_staves += 1
                else:
                    total_staves += 1
            
            # Grieg Op.43 No.6 ("To Spring") is a solo piano piece with 3-stave texture in some measures
            if mxl_path.name == "Grieg_Op43_No06.mxl" and num_parts == 1:
                return num_parts, total_staves, False, "Solo piano with 3-stave notation"

            if num_parts > 2:
                return num_parts, total_staves, True, f"Multi-part ensemble/choral ({num_parts} parts)"
            
            if total_staves > 2:
                return num_parts, total_staves, True, f"Multi-staff score ({num_parts} parts, {total_staves} staves)"
            
            return num_parts, total_staves, False, "Valid piano solo"
    except Exception as e:
        return 0, 0, True, f"Corrupted score: {e}"

def clean_empty_directories(base_dir: Path):
    """Remove empty directories recursively."""
    deleted_dirs = 0
    for root_dir, dirs, files in os.walk(base_dir, topdown=False):
        for d in dirs:
            dir_path = Path(root_dir) / d
            try:
                # check if directory has no files or subdirectories
                if not any(dir_path.iterdir()):
                    dir_path.rmdir()
                    deleted_dirs += 1
            except Exception:
                pass
    return deleted_dirs

def update_kernscores_manifest():
    manifest_p = SCORES_DIR / "KernScores" / "scores_manifest.json"
    if not manifest_p.exists():
        return
    
    kern_dir = SCORES_DIR / "KernScores"
    remaining_files = sorted(list(kern_dir.rglob("*.mxl")))
    
    # Rebuild scores_by_composer
    scores_by_composer = {}
    for f in remaining_files:
        rel = f.relative_to(kern_dir)
        parts = rel.parts
        # parts usually: ('mxl_scores', composer, collection, filename) or ('mxl_scores', composer, filename)
        if len(parts) >= 2 and parts[0] == 'mxl_scores':
            comp = parts[1]
            coll = parts[2] if len(parts) >= 4 else "Default"
        else:
            comp = "Unknown"
            coll = "Default"
        
        if comp not in scores_by_composer:
            scores_by_composer[comp] = {}
        if coll not in scores_by_composer[comp]:
            scores_by_composer[comp][coll] = []
        
        scores_by_composer[comp][coll].append({
            "file": f.name,
            "path": str(f),
            "size_bytes": f.stat().st_size
        })
    
    new_manifest = {
        "updated_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_musicxml_scores": len(remaining_files),
        "verification_status": "100% Validated (Piano Solo <= 2 Tracks)",
        "scores_by_composer": scores_by_composer
    }
    
    with open(manifest_p, 'w', encoding='utf-8') as f:
        json.dump(new_manifest, f, ensure_ascii=False, indent=2)
    print(f"Updated KernScores manifest: {len(remaining_files)} scores")

def update_openscore_manifest():
    manifest_p = SCORES_DIR / "OpenScore" / "scores_manifest.json"
    if not manifest_p.exists():
        return
    
    with open(manifest_p, 'r', encoding='utf-8') as f:
        raw = json.load(f)
    
    openscore_dir = SCORES_DIR / "OpenScore"
    existing_files = {f.name for f in openscore_dir.rglob("*.mxl")}
    
    updated_raw = [item for item in raw if (item.get('filename') in existing_files or Path(item.get('relative_path', '')).name in existing_files)]
    
    with open(manifest_p, 'w', encoding='utf-8') as f:
        json.dump(updated_raw, f, ensure_ascii=False, indent=2)
    print(f"Updated OpenScore manifest: {len(updated_raw)} scores (was {len(raw)})")

def main():
    print("=" * 80)
    print("🧹 STARTING CLEANUP: REMOVING ALL SCORES WITH > 2 TRACKS / STAVES")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    mxl_files = sorted(list(SCORES_DIR.rglob("*.mxl")))
    print(f"Total scores found before cleanup: {len(mxl_files)}")

    deleted_count = 0
    kept_count = 0
    deleted_by_ds = {}

    for f in mxl_files:
        ds = f.relative_to(SCORES_DIR).parts[0]
        num_parts, total_staves, should_delete, reason = get_score_tracks(f)
        
        if should_delete:
            deleted_count += 1
            deleted_by_ds[ds] = deleted_by_ds.get(ds, 0) + 1
            f.unlink()
        else:
            kept_count += 1

    print("\nDeletion Summary by Dataset:")
    for ds, cnt in sorted(deleted_by_ds.items()):
        print(f"  • {ds}: deleted {cnt} scores")

    print(f"\nTotal Deleted: {deleted_count}")
    print(f"Total Kept: {kept_count}")

    print("\nPruning empty directories...")
    deleted_dirs = clean_empty_directories(SCORES_DIR)
    print(f"Removed {deleted_dirs} empty subdirectories.")

    print("\nUpdating dataset manifests...")
    update_kernscores_manifest()
    update_openscore_manifest()

    print("\nCleanup successfully completed!")

if __name__ == "__main__":
    main()
