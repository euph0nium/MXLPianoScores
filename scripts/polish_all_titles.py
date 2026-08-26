#!/usr/bin/env python3
"""
Polish all MusicXML titles and remove any leftover Chinese, bracket artifacts, or duplicates.
Ensures pristine international titles across all datasets.
"""

import os
import re
import glob
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path("/Users/shiyuli/Dev/Scores")
SCORES_DIR = ROOT_DIR / "scores"

# Clean mappings for specific works
CUSTOM_TITLE_MAP = {
    # Burgmuller
    "Burgmuller_Op100_No_01_La_Candeur.mxl": "25 Études faciles, Op. 100 - No. 01 La Candeur",
    "Burgmuller_Op100_No_02_LArabesque.mxl": "25 Études faciles, Op. 100 - No. 02 L'Arabesque",
    "Burgmuller_Op100_No_03_Pastorale.mxl": "25 Études faciles, Op. 100 - No. 03 Pastorale",
    "Burgmuller_Op100_No_04_Petite_réunion.mxl": "25 Études faciles, Op. 100 - No. 04 Petite réunion",
    "Burgmuller_Op100_No_05_Innocence.mxl": "25 Études faciles, Op. 100 - No. 05 Innocence",
    "Burgmuller_Op100_No_06_Progrès.mxl": "25 Études faciles, Op. 100 - No. 06 Progrès",
    "Burgmuller_Op100_No_07_Le_courant_limpide.mxl": "25 Études faciles, Op. 100 - No. 07 Le courant limpide",
    "Burgmuller_Op100_No_08_La_gracieuse.mxl": "25 Études faciles, Op. 100 - No. 08 La gracieuse",
    "Burgmuller_Op100_No_09_La_chasse.mxl": "25 Études faciles, Op. 100 - No. 09 La chasse",
    "Burgmuller_Op100_No_10_Tendre_fleur.mxl": "25 Études faciles, Op. 100 - No. 10 Tendre fleur",
    "Burgmuller_Op100_No_11_La_bergeronnette.mxl": "25 Études faciles, Op. 100 - No. 11 La bergeronnette",
    "Burgmuller_Op100_No_12_Ladieu.mxl": "25 Études faciles, Op. 100 - No. 12 L'adieu",
    "Burgmuller_Op100_No_13_Consolation.mxl": "25 Études faciles, Op. 100 - No. 13 Consolation",
    "Burgmuller_Op100_No_14_La_styrienne.mxl": "25 Études faciles, Op. 100 - No. 14 La styrienne",
    "Burgmuller_Op100_No_15_Ballade.mxl": "25 Études faciles, Op. 100 - No. 15 Ballade",
    "Burgmuller_Op100_No_16_Douce_plainte.mxl": "25 Études faciles, Op. 100 - No. 16 Douce plainte",
    "Burgmuller_Op100_No_17_La_babillarde.mxl": "25 Études faciles, Op. 100 - No. 17 La babillarde",
    "Burgmuller_Op100_No_18_Inquiétude.mxl": "25 Études faciles, Op. 100 - No. 18 Inquiétude",
    
    # Beethoven Sonatas Op. 49 & Fur Elise
    "Beethoven_Fur_Elise_WoO59.mxl": "Für Elise - Bagatelle in A minor, WoO 59",
    "Beethoven_LVB_Sonate_49no1_1.mxl": "Piano Sonata No. 19 in G minor, Op. 49 No. 1 - 1. Andante",
    "Beethoven_LVB_Sonate_49no1_2.mxl": "Piano Sonata No. 19 in G minor, Op. 49 No. 1 - 2. Rondo. Allegro",
    "Beethoven_LVB_Sonate_49no2_1.mxl": "Piano Sonata No. 20 in G major, Op. 49 No. 2 - 1. Allegro, ma non troppo",
    "Beethoven_LVB_Sonate_49no2_2.mxl": "Piano Sonata No. 20 in G major, Op. 49 No. 2 - 2. Tempo di Menuetto",
    
    # Kuhlau Op. 20 No. 1
    "Kuhlau_Op20_No1_sonatine-1-allegro.mxl": "Sonatina in C major, Op. 20 No. 1 - 1. Allegro",
    "Kuhlau_Op20_No1_sonatine-1-andante.mxl": "Sonatina in C major, Op. 20 No. 1 - 2. Andante",
    "Kuhlau_Op20_No1_sonatine-1-rondo.mxl": "Sonatina in C major, Op. 20 No. 1 - 3. Rondo. Allegro",
}

def clean_general_text(text: str) -> str:
    if not text:
        return ""
    # Remove Chinese inside/with parens
    text = re.sub(r"\s*[\(（][^\)）]*?[\u4e00-\u9fff]+[^\)）]*?[\)）]\s*", " ", text)
    # Remove any remaining Chinese characters
    text = re.sub(r"[\u4e00-\u9fff]+", "", text)
    # Remove empty brackets
    text = re.sub(r"[\(（]\s*[\)）]", "", text)
    text = re.sub(r"\[\s*\]", "", text)
    # Remove trailing/leading dashes and spaces
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\s*-\s*$", "", text)
    text = re.sub(r"^\s*-\s*", "", text)
    return text.strip()

def polish_all_scores():
    all_files = sorted(glob.glob("scores/**/*.mxl", recursive=True))
    print(f"Polishing {len(all_files)} scores...")
    
    modified = 0
    for f in all_files:
        p = Path(f)
        fn = p.name
        
        with zipfile.ZipFile(p, "r") as zf:
            xml_names = [n for n in zf.namelist() if (n.endswith('.xml') or n.endswith('.musicxml')) and not n.startswith('META-INF')]
            if not xml_names:
                continue
            xml_fn = xml_names[0]
            root = ET.fromstring(zf.read(xml_fn))
            
        changed = False
        
        # 1. Custom exact titles if mapped
        if fn in CUSTOM_TITLE_MAP:
            target_title = CUSTOM_TITLE_MAP[fn]
            
            wt = root.find(".//work-title")
            if wt is not None:
                wt.text = target_title
            else:
                work_elem = root.find(".//work")
                if work_elem is None:
                    work_elem = ET.Element("work")
                    root.insert(0, work_elem)
                wt = ET.SubElement(work_elem, "work-title")
                wt.text = target_title
                
            mt = root.find(".//movement-title")
            if mt is not None:
                mt.text = target_title
                
            changed = True
        else:
            # General cleaning
            for wt in root.findall(".//work-title"):
                if wt.text:
                    ct = clean_general_text(wt.text)
                    if ct != wt.text:
                        wt.text = ct
                        changed = True
                        
            for mt in root.findall(".//movement-title"):
                if mt.text:
                    ct = clean_general_text(mt.text)
                    if ct != mt.text:
                        mt.text = ct
                        changed = True
                        
            for cw in root.findall(".//credit-words"):
                if cw.text:
                    ct = clean_general_text(cw.text)
                    if ct != cw.text:
                        cw.text = ct
                        changed = True
                        
        if changed:
            clean_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            tmp_mxl = p.with_suffix(".tmp.mxl")
            with zipfile.ZipFile(tmp_mxl, "w", compression=zipfile.ZIP_DEFLATED) as new_zf:
                container_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<container>
  <rootfiles>
    <rootfile full-path="{xml_fn}"/>
  </rootfiles>
</container>"""
                new_zf.writestr("META-INF/container.xml", container_content)
                new_zf.writestr(xml_fn, clean_xml)
            tmp_mxl.replace(p)
            modified += 1
            
    print(f"✨ Polished {modified} score files!")

if __name__ == "__main__":
    polish_all_scores()
