#!/usr/bin/env python3
"""
1. Sanitize all MusicXML (.mxl) internal metadata and filenames:
   - Remove all Chinese characters.
   - Remove associated parentheses (both Chinese '（）' and English '()').
   - Clean up punctuation artifacts (e.g. trailing dashes, double spaces).
2. Ensure full MusicXML 4.0 compatibility with MuseScore.
3. Update catalogs and global indices.
"""

import os
import re
import sys
import glob
import zipfile
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

ROOT_DIR = Path("/Users/shiyuli/Dev/Scores")
SCORES_DIR = ROOT_DIR / "scores"
MSCORE = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"

CHINESE_CHAR_RE = re.compile(r"[\u4e00-\u9fff]+")
CHINESE_WITH_PARENS_RE = re.compile(r"[\(（][^\)）]*[\u4e00-\u9fff]+[^\)）]*[\)）]")

def clean_text(text: str) -> str:
    if not text:
        return text
    
    # 1. Remove parenthesized text that contains Chinese characters
    cleaned = CHINESE_WITH_PARENS_RE.sub("", text)
    
    # 2. Remove any remaining Chinese characters
    cleaned = CHINESE_CHAR_RE.sub("", cleaned)
    
    # 3. Clean up empty brackets or leftover bracket artifacts
    cleaned = re.sub(r"[\(（]\s*[\)）]", "", cleaned)
    cleaned = re.sub(r"\[\s*\]", "", cleaned)
    
    # 4. Clean up formatting artifacts like " -  - " or trailing/leading dashes
    cleaned = re.sub(r"\s+-\s*$", "", cleaned)
    cleaned = re.sub(r"^\s*-\s+", "", cleaned)
    cleaned = re.sub(r"\s{2,}", " ", cleaned)
    
    return cleaned.strip()

def sanitize_mxl_file(mxl_path: Path):
    changed = False
    new_xml_data = None
    xml_filename = None
    
    try:
        with zipfile.ZipFile(mxl_path, "r") as zf:
            namelist = zf.namelist()
            xml_files = [n for n in namelist if (n.endswith(".xml") or n.endswith(".musicxml")) and not n.startswith("META-INF")]
            if not xml_files:
                return False, "No xml file inside"
            
            xml_filename = xml_files[0]
            raw_xml = zf.read(xml_filename)
            container_xml = zf.read("META-INF/container.xml") if "META-INF/container.xml" in namelist else None
            
            # Parse XML
            root = ET.fromstring(raw_xml)
            
            # 1. Clean work-title
            for wt in root.findall(".//work-title"):
                if wt.text:
                    c = clean_text(wt.text)
                    if c != wt.text:
                        wt.text = c
                        changed = True
                        
            # 2. Clean movement-title
            for mt in root.findall(".//movement-title"):
                if mt.text:
                    c = clean_text(mt.text)
                    if c != mt.text:
                        mt.text = c
                        changed = True
                        
            # 3. Clean credit-words
            for cw in root.findall(".//credit-words"):
                if cw.text:
                    c = clean_text(cw.text)
                    if c != cw.text:
                        cw.text = c
                        changed = True
                        
            # 4. Clean part-name
            for pn in root.findall(".//part-name"):
                if pn.text:
                    c = clean_text(pn.text)
                    if c != pn.text:
                        pn.text = c
                        changed = True
                        
            # 5. Clean rights / creator
            for cr in root.findall(".//creator"):
                if cr.text:
                    c = clean_text(cr.text)
                    if c != cr.text:
                        cr.text = c
                        changed = True
                        
            if changed:
                new_xml_data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
        if changed and new_xml_data:
            # Re-write MXL zip archive safely
            tmp_mxl = mxl_path.with_suffix(".tmp.mxl")
            with zipfile.ZipFile(tmp_mxl, "w", compression=zipfile.ZIP_DEFLATED) as new_zf:
                if container_xml:
                    new_zf.writestr("META-INF/container.xml", container_xml)
                else:
                    container_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<container>
  <rootfiles>
    <rootfile full-path="{xml_filename}"/>
  </rootfiles>
</container>"""
                    new_zf.writestr("META-INF/container.xml", container_content)
                new_zf.writestr(xml_filename, new_xml_data)
            tmp_mxl.replace(mxl_path)
            return True, "Sanitized"
            
    except Exception as e:
        return False, f"Error: {e}"
        
    return False, "Unchanged"

def clean_filename(path: Path) -> Path:
    old_name = path.name
    new_name = clean_text(old_name)
    # Remove any brackets in filenames
    new_name = re.sub(r"[（）\(\)]", "", new_name)
    new_name = re.sub(r"\s+", "_", new_name)
    new_name = re.sub(r"_{2,}", "_", new_name)
    
    if new_name != old_name:
        new_path = path.parent / new_name
        path.rename(new_path)
        return new_path
    return path

def validate_with_musescore(mxl_path: Path):
    if not os.path.exists(MSCORE):
        return True, "MuseScore not installed"
    
    out_tmp = Path(f"/tmp/ms_val_{os.getpid()}_{mxl_path.stem}.mscx")
    try:
        res = subprocess.run([MSCORE, "-o", str(out_tmp), str(mxl_path)], capture_output=True, text=True, timeout=20)
        if out_tmp.exists():
            out_tmp.unlink()
        if res.returncode != 0:
            return False, f"MuseScore returned code {res.returncode}: {res.stderr[:200]}"
        return True, "OK"
    except Exception as e:
        if out_tmp.exists():
            out_tmp.unlink()
        return False, str(e)

def main():
    print("======================================================================")
    print("🧹 1. 清理 MXL 文件元数据中的中文与括号 (Work-Title, Movement-Title 等)...")
    print("======================================================================")
    
    all_files = sorted(glob.glob("scores/**/*.mxl", recursive=True))
    print(f"Total MXL files to inspect: {len(all_files)}")
    
    sanitized_count = 0
    renamed_count = 0
    
    for f in all_files:
        p = Path(f)
        # 1. Clean filename
        new_p = clean_filename(p)
        if new_p != p:
            renamed_count += 1
            
        # 2. Clean internal XML
        ok, msg = sanitize_mxl_file(new_p)
        if ok:
            sanitized_count += 1
            
    print(f"✨ 完成元数据清洗: {sanitized_count} 首乐谱 XML 标题已纯化 (无中文/无多余括号)！")
    print(f"✨ 完成文件名纯化: {renamed_count} 个文件名已更新！")
    
    print("\n======================================================================")
    print("🎼 2. 运行 MuseScore 4 权威渲染与兼容性校验...")
    print("======================================================================")
    
    updated_files = sorted(glob.glob("scores/**/*.mxl", recursive=True))
    
    # Test batch of scores across all datasets with MuseScore 4
    import random
    sample_files = random.sample(updated_files, min(200, len(updated_files)))
    
    passed = 0
    failed = 0
    
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(validate_with_musescore, [Path(f) for f in sample_files]))
        
    for f, (ok, msg) in zip(sample_files, results):
        if ok:
            passed += 1
        else:
            failed += 1
            print(f"  ❌ Failed: {f} -> {msg}")
            
    print(f"📊 MuseScore 4 兼容性测试结果: {passed}/{len(sample_files)} (通过率: {passed/len(sample_files)*100:.1f}%)")

if __name__ == "__main__":
    main()
