#!/usr/bin/env python3
"""
MusicXML Fast Batch Validator
Checks XML syntax, structure, and measure synchronization across parts.
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor

WORKSPACE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = WORKSPACE_DIR / "musicxml_scores"


def validate_xml_file(filepath):
    try:
        # Fast XML parse
        tree = ET.parse(filepath)
        root = tree.getroot()

        parts = root.findall("part")
        if not parts:
            return str(filepath), False, "No <part> elements found"

        # Check measure consistency across multi-part scores (e.g. Piano grand staff)
        if len(parts) > 1:
            part_measures = []
            for p in parts:
                m_nums = [m.get("number") for m in p.findall("measure")]
                part_measures.append(m_nums)

            # Measure count mismatch
            counts = [len(m) for m in part_measures]
            if len(set(counts)) > 1:
                return str(filepath), False, f"Measure count mismatch across parts: {counts}"

            # Measure number alignment mismatch
            first_m = part_measures[0]
            for idx, m_list in enumerate(part_measures[1:], 2):
                if m_list != first_m:
                    return str(filepath), False, f"Measure numbers mismatch between Part 1 and Part {idx}"

        return str(filepath), True, "OK"
    except Exception as e:
        return str(filepath), False, f"XML Parse Error: {e}"


def main():
    all_files = list(BASE_DIR.rglob("*.musicxml"))
    total = len(all_files)
    print(f"正在快速校验 {total} 首 MusicXML 乐谱的完整性与小节同步性...")

    num_workers = min(12, os.cpu_count() or 4)
    with ProcessPoolExecutor(max_workers=num_workers) as ex:
        results = list(ex.map(validate_xml_file, all_files))

    valid = [r for r in results if r[1]]
    invalid = [r for r in results if not r[1]]

    print("\n" + "=" * 60)
    print(f"  校验完成！总计扫描: {total} 首")
    print(f"  - ✅ 100% 结构完整无错: {len(valid)} 首 ({len(valid)/total*100:.2f}%)")
    print(f"  - ⚠️ 存在小节错乱/异常: {len(invalid)} 首 ({len(invalid)/total*100:.2f}%)")
    print("=" * 60)

    if invalid:
        by_composer = defaultdict(list)
        for path, _, reason in invalid:
            p = Path(path)
            comp = p.parent.parent.name
            coll = p.parent.name
            fname = p.name
            by_composer[comp].append((coll, fname, reason))

        print("\n存在异常的乐谱明细：")
        for comp, items in sorted(by_composer.items()):
            print(f"\n【{comp}】 共 {len(items)} 首异常:")
            for coll, fname, reason in items[:10]:
                print(f"   * [{coll}] {fname}")
                print(f"     原因: {reason}")
            if len(items) > 10:
                print(f"     ... 其余 {len(items) - 10} 首省略")


if __name__ == "__main__":
    main()
