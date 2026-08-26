#!/usr/bin/env python3
"""
Title and Metadata Polisher for MusicXML & MXL scores
- Unescapes raw HTML entities (&auml;, &szlig;, &eacute;, &mdash;, etc.) to standard UTF-8.
- Cleans rhythmic notation tokens ([eighth-dot], [quarter], etc.) in titles.
- Fixes Webern and other multi-movement work titles for clean display in MuseScore.
- Updates both musicxml_scores/ and mxl_scores/.
"""

import os
import sys
import re
import html
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

WORKSPACE_DIR = Path(__file__).resolve().parent.parent
XML_BASE_DIR = WORKSPACE_DIR / "musicxml_scores"
MXL_BASE_DIR = WORKSPACE_DIR / "mxl_scores"

RHYTHM_MAP = {
    r"\[eighth-dot\]": "♪.",
    r"\[quarter-dot\]": "♩.",
    r"\[half-dot\]": "𝅗𝅥.",
    r"\[quarter\]": "♩",
    r"\[half\]": "𝅗𝅥",
    r"\[eighth\]": "♪",
    r"\[sixteenth\]": "𝅘𝅥𝅯",
    r"\[whole\]": "𝅝",
}

COMMON_ENTITIES = {
    "&amp;auml;": "ä", "&auml;": "ä",
    "&amp;Auml;": "Ä", "&Auml;": "Ä",
    "&amp;ouml;": "ö", "&ouml;": "ö",
    "&amp;Ouml;": "Ö", "&Ouml;": "Ö",
    "&amp;uuml;": "ü", "&uuml;": "ü",
    "&amp;Uuml;": "Ü", "&Uuml;": "Ü",
    "&amp;szlig;": "ß", "&szlig;": "ß",
    "&amp;eacute;": "é", "&eacute;": "é",
    "&amp;Eacute;": "É", "&Eacute;": "É",
    "&amp;egrave;": "è", "&egrave;": "è",
    "&amp;agrave;": "à", "&agrave;": "à",
    "&amp;aacute;": "á", "&aacute;": "á",
    "&amp;oacute;": "ó", "&oacute;": "ó",
    "&amp;uacute;": "ú", "&uacute;": "ú",
    "&amp;iacute;": "í", "&iacute;": "í",
    "&amp;ntilde;": "ñ", "&ntilde;": "ñ",
    "&amp;ccedil;": "ç", "&ccedil;": "ç",
    "&amp;mdash;": "—", "&mdash;": "—",
    "&amp;ndash;": "–", "&ndash;": "–",
    "&amp;copy;": "©", "&copy;": "©",
}


def clean_text(text: str) -> str:
    """Clean HTML entities and rhythmic tokens in title strings."""
    if not text:
        return text

    # Unescape common HTML entities
    for ent, char in COMMON_ENTITIES.items():
        text = text.replace(ent, char)

    # General HTML unescape (avoiding &lt;, &gt;, &amp;, &quot;, &apos;)
    text = html.unescape(text)

    # Replace rhythm tokens
    for pattern, rep in RHYTHM_MAP.items():
        text = re.sub(pattern, rep, text, flags=re.IGNORECASE)

    return text.strip()


def polish_single_xml_file(xml_path: Path):
    """Parse, polish titles and metadata, and save XML & MXL."""
    try:
        content = xml_path.read_text(encoding="utf-8", errors="ignore")

        # Global replace of entities in text
        for ent, char in COMMON_ENTITIES.items():
            content = content.replace(ent, char)

        for pattern, rep in RHYTHM_MAP.items():
            content = re.sub(pattern, rep, content, flags=re.IGNORECASE)

        # Parse XML tree for structural title polishing
        tree = ET.fromstring(content.encode("utf-8"))

        work = tree.find("work")
        work_title_elem = work.find("work-title") if work is not None else None
        mov_title_elem = tree.find("movement-title")
        mov_num_elem = tree.find("movement-number")

        # Check miscellaneous fields for metadata
        misc_fields = {}
        for misc_field in tree.findall(".//miscellaneous-field"):
            name = misc_field.get("name")
            val = misc_field.text
            if name and val:
                misc_fields[name] = val

        # Polishing Webern Op. 27
        if "webern-op27" in xml_path.name.lower():
            if work is None:
                work = ET.SubElement(tree, "work")
            if work_title_elem is None:
                work_title_elem = ET.SubElement(work, "work-title")

            work_title_elem.text = "Variations for Piano, Op. 27"

            mov_num = mov_num_elem.text if mov_num_elem is not None else ""
            if "n1" in xml_path.name.lower():
                if mov_title_elem is None:
                    mov_title_elem = ET.SubElement(tree, "movement-title")
                mov_title_elem.text = "I. Sehr mäßig (♪. = ca. 40)"
            elif "n2" in xml_path.name.lower():
                if mov_title_elem is None:
                    mov_title_elem = ET.SubElement(tree, "movement-title")
                mov_title_elem.text = "II. Sehr schnell (♩ = ca. 160)"
            elif "n3" in xml_path.name.lower():
                if mov_title_elem is None:
                    mov_title_elem = ET.SubElement(tree, "movement-title")
                mov_title_elem.text = "III. Ruhig fließend (♩ = ca. 80)"

            # Remove isolated movement-number tag so MuseScore doesn't print stray number in middle
            if mov_num_elem is not None:
                tree.remove(mov_num_elem)

        # Generic title cleaning
        if work_title_elem is not None and work_title_elem.text:
            work_title_elem.text = clean_text(work_title_elem.text)

        if mov_title_elem is not None and mov_title_elem.text:
            mov_title_elem.text = clean_text(mov_title_elem.text)

        # Write polished MusicXML
        polished_xml_bytes = ET.tostring(tree, encoding="utf-8", xml_declaration=True)
        xml_path.write_bytes(polished_xml_bytes)

        # Update corresponding MXL file
        rel_path = xml_path.relative_to(XML_BASE_DIR)
        mxl_path = MXL_BASE_DIR / rel_path.with_suffix(".mxl")
        mxl_path.parent.mkdir(parents=True, exist_ok=True)

        container_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="{xml_path.name}"/>
  </rootfiles>
</container>'''

        with zipfile.ZipFile(mxl_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            zf.writestr("META-INF/container.xml", container_xml.encode("utf-8"))
            zf.writestr(xml_path.name, polished_xml_bytes)

        return True, str(xml_path), None
    except Exception as e:
        return False, str(xml_path), str(e)


def main():
    print("=" * 65)
    print("  全库乐谱标题排版美化与字符实体（HTML Entities）清洗修复")
    print("=" * 65)

    all_xml_files = list(XML_BASE_DIR.rglob("*.musicxml"))
    total = len(all_xml_files)
    print(f"\n正在对全部 {total} 首乐谱进行标题与文本清洗...")

    num_workers = min(12, os.cpu_count() or 4)
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(polish_single_xml_file, all_xml_files))

    success = [r for r in results if r[0]]
    failed = [r for r in results if not r[0]]

    print(f"\n✅ 处理完成！成功美化与更新: {len(success)} 首 | 失败: {len(failed)} 首")


if __name__ == "__main__":
    main()
