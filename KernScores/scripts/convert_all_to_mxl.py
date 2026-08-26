#!/usr/bin/env python3
"""
MusicXML to Compressed MXL Batch Converter
Converts all .musicxml scores to standard W3C compressed .mxl archives.
"""

import os
import sys
import time
import json
import zipfile
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

WORKSPACE_DIR = Path(__file__).resolve().parent.parent
INPUT_BASE_DIR = WORKSPACE_DIR / "musicxml_scores"
OUTPUT_BASE_DIR = WORKSPACE_DIR / "mxl_scores"


def convert_single_file(task):
    xml_path, mxl_path = task
    try:
        xml_bytes = Path(xml_path).read_bytes()
        root_filename = Path(xml_path).name

        container_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="{root_filename}"/>
  </rootfiles>
</container>'''

        # Ensure parent directory exists
        Path(mxl_path).parent.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(mxl_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            zf.writestr("META-INF/container.xml", container_xml.encode("utf-8"))
            zf.writestr(root_filename, xml_bytes)

        orig_size = len(xml_bytes)
        mxl_size = os.path.getsize(mxl_path)
        return True, str(mxl_path), orig_size, mxl_size, None
    except Exception as e:
        return False, str(mxl_path), 0, 0, str(e)


def main():
    print("=" * 65)
    print("  MusicXML 全量压缩至标准 MXL (.mxl) 批处理转换")
    print(f"  源目录: {INPUT_BASE_DIR}")
    print(f"  输出目录: {OUTPUT_BASE_DIR}")
    print("=" * 65)

    all_xml_files = list(INPUT_BASE_DIR.rglob("*.musicxml"))
    total_files = len(all_xml_files)
    print(f"\n[1/3] 找到 {total_files} 首 MusicXML 乐谱，准备并行压缩转换...")

    tasks = []
    for xml_file in all_xml_files:
        rel_path = xml_file.relative_to(INPUT_BASE_DIR)
        mxl_rel_path = rel_path.with_suffix(".mxl")
        mxl_file = OUTPUT_BASE_DIR / mxl_rel_path
        tasks.append((str(xml_file), str(mxl_file)))

    start_time = time.time()
    num_workers = min(12, os.cpu_count() or 4)

    success_count = 0
    total_orig_bytes = 0
    total_mxl_bytes = 0
    errors = []

    print(f"[2/3] 启用 {num_workers} 核并行压缩转换中...")

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(convert_single_file, task): task for task in tasks}
        completed = 0
        for future in as_completed(futures):
            completed += 1
            success, mxl_p, orig_sz, mxl_sz, err = future.result()
            if success:
                success_count += 1
                total_orig_bytes += orig_sz
                total_mxl_bytes += mxl_sz
            else:
                errors.append((mxl_p, err))

            if completed % 100 == 0 or completed == total_files:
                pct = completed / total_files * 100
                sys.stdout.write(f"\r  转换进度: [{completed:04d}/{total_files:04d}] {pct:5.1f}% | 成功: {success_count}")
                sys.stdout.flush()

    elapsed = time.time() - start_time
    print(f"\n\n[3/3] 压缩转换完成！耗时: {elapsed:.2f} 秒")

    orig_mb = total_orig_bytes / (1024 * 1024)
    mxl_mb = total_mxl_bytes / (1024 * 1024)
    ratio = (mxl_mb / orig_mb * 100) if orig_mb > 0 else 0

    print("\n" + "=" * 65)
    print(f"  统计报表:")
    print(f"  - 成功转换 MXL 文件数: {success_count} 首")
    print(f"  - 原始 MusicXML 体积: {orig_mb:.2f} MB")
    print(f"  - 压缩后 MXL 总存储体积: {mxl_mb:.2f} MB (压缩至原体积的 {ratio:.1f}%)")
    print(f"  - 节省空间: {orig_mb - mxl_mb:.2f} MB (节省 {(100 - ratio):.1f}% 磁盘空间)")
    print(f"  - 输出目录: {OUTPUT_BASE_DIR}")
    print("=" * 65)


if __name__ == "__main__":
    main()
