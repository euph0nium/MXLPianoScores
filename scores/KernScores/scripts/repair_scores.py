#!/usr/bin/env python3
"""
MusicXML Auto-Repair and High-Fidelity Sync
Validates all MusicXML files, and for any file with measure inconsistencies,
automatically fetches the official Stanford hum2xml MusicXML.
"""

import os
import sys
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Suppress urllib3 / requests warnings
import warnings
warnings.filterwarnings("ignore")

WORKSPACE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = WORKSPACE_DIR / "musicxml_scores"

# Import catalog from download_and_convert_kernscores
from download_and_convert_kernscores import COLLECTIONS_CATALOG

# Map (composer, collection) -> url_path
COLLECTION_PATH_MAP = {
    (composer, coll_name): url_path
    for (_, composer, coll_name, url_path) in COLLECTIONS_CATALOG
}


def validate_file(filepath: Path):
    """Check if MusicXML has proper structure and consistent measure counts."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        parts = root.findall("part")
        if not parts:
            return False, "No parts"

        if len(parts) > 1:
            part_measures = []
            for p in parts:
                m_nums = [m.get("number") for m in p.findall("measure")]
                part_measures.append(m_nums)

            counts = [len(m) for m in part_measures]
            if len(set(counts)) > 1:
                return False, f"Measure count mismatch: {counts}"

            first_m = part_measures[0]
            for idx, m_list in enumerate(part_measures[1:], 2):
                if m_list != first_m:
                    return False, f"Measure numbers mismatch with Part {idx}"

        return True, "OK"
    except Exception as e:
        return False, str(e)


def extract_raw_krn_name(musicxml_name: str) -> str:
    """Extract the original .krn file name from the generated MusicXML filename."""
    # MusicXML files start with original base name, e.g. sonata01-1_Piano_Sonata...
    match = re.match(r"^([^_]+(?:-[0-9]+)?)_", musicxml_name)
    if match:
        base = match.group(1)
        return f"{base}.krn"
    # fallback
    base = musicxml_name.split("_")[0]
    return f"{base}.krn"


def repair_single_file(task):
    filepath, url_path, krn_name = task
    try:
        url = f"http://kern.ccarh.org/cgi-bin/ksdata?l={url_path}&file={krn_name}&format=musicxml"
        headers = {"User-Agent": "Mozilla/5.0"}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()

        if len(data) > 500 and b"<score-partwise" in data:
            with open(filepath, "wb") as f:
                f.write(data)
            is_valid, reason = validate_file(filepath)
            return filepath, is_valid, reason
        else:
            return filepath, False, "Downloaded data invalid"
    except Exception as e:
        return filepath, False, str(e)


def main():
    print("=" * 65)
    print("  MusicXML 乐谱全量校验与自动化高精度修复 (Stanford hum2xml 引擎)")
    print("=" * 65)

    all_files = list(BASE_DIR.rglob("*.musicxml"))
    total = len(all_files)
    print(f"\n[1/3] 正在全量扫描 {total} 首乐谱...")

    needs_repair = []
    for f in all_files:
        is_valid, reason = validate_file(f)
        if not is_valid:
            comp = f.parent.parent.name
            coll = f.parent.name
            url_path = COLLECTION_PATH_MAP.get((comp, coll))
            krn_name = extract_raw_krn_name(f.name)
            needs_repair.append((f, url_path, krn_name, reason))

    print(f"\n[2/3] 扫描完成！发现 {len(needs_repair)} 首乐谱需要修复对齐。")
    if not needs_repair:
        print("  所有乐谱均 100% 正常，无需修复！")
        return

    print("  正在从斯坦福官方 hum2xml 引擎拉取原生高精度 MusicXML 修复中...")

    repair_tasks = [
        (f, url_path, krn_name)
        for (f, url_path, krn_name, _) in needs_repair
        if url_path
    ]

    fixed_count = 0
    failed_count = 0

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(repair_single_file, t): t for t in repair_tasks}
        for future in as_completed(futures):
            fpath, is_valid, reason = future.result()
            if is_valid:
                fixed_count += 1
            else:
                failed_count += 1

    print(f"\n[3/3] 修复完成！成功修复: {fixed_count} 首 | 失败: {failed_count} 首")

    # Final re-validation
    re_scan_valid = sum(1 for f in all_files if validate_file(f)[0])
    print("\n" + "=" * 65)
    print(f"  最终健康状态:")
    print(f"  - ✅ 100% 结构完整可用: {re_scan_valid} / {total} ({re_scan_valid/total*100:.2f}%)")
    print("=" * 65)


if __name__ == "__main__":
    main()
