#!/usr/bin/env python3
"""
KernScores to MusicXML Batch Downloader and Converter
Author: Antigravity
"""

import os
import sys
import re
import io
import time
import json
import zipfile
import urllib.request
import urllib.error
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

# Suppress urllib3 / requests warnings
import warnings
warnings.filterwarnings("ignore")

# Define base output directory
WORKSPACE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_BASE_DIR = WORKSPACE_DIR / "musicxml_scores"

# Curated and categorized collection mappings: (Category, Composer, Collection Name, URL path)
COLLECTIONS_CATALOG = [
    # --- Ludwig van Beethoven ---
    ("Classical_Solo_Piano", "Ludwig_van_Beethoven", "32_Piano_Sonatas", "/users/craig/classical/beethoven/piano/sonata"),
    ("Classical_Chamber", "Ludwig_van_Beethoven", "16_String_Quartets", "/users/craig/classical/beethoven/quartet"),
    ("Classical_Orchestral", "Ludwig_van_Beethoven", "Symphonies", "/musedata/beethoven/sym"),

    # --- Frédéric Chopin ---
    ("Classical_Solo_Piano", "Frederic_Chopin", "24_Preludes_Op28", "/users/craig/classical/chopin/prelude"),
    ("Classical_Solo_Piano", "Frederic_Chopin", "Etudes_Op10_Op25", "/users/craig/classical/chopin/etude"),
    ("Classical_Solo_Piano", "Frederic_Chopin", "Mazurkas", "/users/craig/classical/chopin/mazurka"),
    ("Classical_Solo_Piano", "Frederic_Chopin", "First_Editions", "/users/mkonik/nifc-digital-editions/chopin-first-editions"),

    # --- Johann Sebastian Bach ---
    ("Classical_Solo_Piano", "Johann_Sebastian_Bach", "Well_Tempered_Clavier_Book_1_Musedata", "/musedata/bach/keyboard/wtc-1"),
    ("Classical_Solo_Piano", "Johann_Sebastian_Bach", "Well_Tempered_Clavier_Book_2_Musedata", "/musedata/bach/keyboard/wtc-2"),
    ("Classical_Solo_Piano", "Johann_Sebastian_Bach", "Well_Tempered_Clavier_Book_1_OSU", "/osu/classical/bach/wtc-1"),
    ("Classical_Solo_Piano", "Johann_Sebastian_Bach", "Well_Tempered_Clavier_Book_2_OSU", "/osu/classical/bach/wtc-2"),
    ("Classical_Solo_Piano", "Johann_Sebastian_Bach", "WTC_Book_2_Preludes", "/users/craig/classical/bach/wtc2preludes"),
    ("Classical_Solo_Piano", "Johann_Sebastian_Bach", "Two_Part_Inventions", "/osu/classical/bach/inventions"),
    ("Classical_Solo_Piano", "Johann_Sebastian_Bach", "Art_of_Fugue", "/users/craig/classical/bach/artfugue"),
    ("Classical_Solo_Piano", "Johann_Sebastian_Bach", "Musical_Offering", "/users/craig/classical/bach/offering"),
    ("Classical_Choral", "Johann_Sebastian_Bach", "371_Chorales", "/users/craig/classical/bach/371chorales"),
    ("Classical_Choral", "Johann_Sebastian_Bach", "185_Cantata_Chorales", "/musedata/bach/chorales"),
    ("Classical_Choral", "Johann_Sebastian_Bach", "69_Analyzed_Chorales", "/users/craig/classical/bach/bhchorale"),
    ("Classical_Orchestral", "Johann_Sebastian_Bach", "Brandenburg_Concertos", "/musedata/bach/brandenburg"),

    # --- Wolfgang Amadeus Mozart ---
    ("Classical_Solo_Piano", "Wolfgang_Amadeus_Mozart", "Piano_Sonatas", "/users/craig/classical/mozart/piano/sonata"),
    ("Classical_Chamber", "Wolfgang_Amadeus_Mozart", "String_Quartets", "/musedata/mozart/quartet"),

    # --- Scott Joplin ---
    ("Classical_Solo_Piano", "Scott_Joplin", "Complete_Piano_Rags", "/users/craig/ragtime/joplin"),

    # --- Joseph Haydn ---
    ("Classical_Solo_Piano", "Joseph_Haydn", "Keyboard_Sonatas", "/users/craig/classical/haydn/keyboard/uesonatas"),
    ("Classical_Chamber", "Joseph_Haydn", "String_Quartets", "/musedata/haydn/quartet"),
    ("Classical_Orchestral", "Joseph_Haydn", "Musedata_Symphonies", "/musedata/haydn/sym"),
    ("Classical_Orchestral", "Joseph_Haydn", "London_Symphonies", "/osu/classical/haydn/london"),

    # --- Domenico Scarlatti ---
    ("Classical_Solo_Piano", "Domenico_Scarlatti", "Keyboard_Sonatas_Longo", "/users/craig/classical/scarlatti/longo"),

    # --- Other Keyboard Masters ---
    ("Classical_Solo_Piano", "Muzio_Clementi", "6_Progressive_Sonatinas_Op36", "/users/craig/classical/clementi/op36"),
    ("Classical_Solo_Piano", "Johann_Nepomuk_Hummel", "24_Preludes_Op67", "/users/craig/classical/hummel/op67"),
    ("Classical_Solo_Piano", "Edvard_Grieg", "Piano_Sonata_Op7", "/users/craig/classical/grieg/op07"),
    ("Classical_Solo_Piano", "Johannes_Brahms", "Piano_Sonata_No1_Op1", "/users/craig/classical/brahms/op01"),
    ("Classical_Chamber", "Johannes_Brahms", "String_Quartet_Op51", "/users/craig/classical/brahms/op51"),
    ("Classical_Chamber", "Edvard_Grieg", "Selected_Works", "/users/craig/classical/grieg"),
    ("Classical_Solo_Piano", "Mikalojus_Konstantinas_Ciurlionis", "Piano_and_Organ_Works", "/ktu/ciurlionis"),

    # --- Arcangelo Corelli ---
    ("Classical_Chamber", "Arcangelo_Corelli", "Trio_Sonatas_Op1", "/musedata/corelli/op1"),
    ("Classical_Chamber", "Arcangelo_Corelli", "Trio_Sonatas_Op2", "/musedata/corelli/op2"),
    ("Classical_Chamber", "Arcangelo_Corelli", "Trio_Sonatas_Op3", "/musedata/corelli/op3"),
    ("Classical_Chamber", "Arcangelo_Corelli", "Trio_Sonatas_Op4", "/musedata/corelli/op4"),
    ("Classical_Chamber", "Arcangelo_Corelli", "Violin_Sonatas_Op5", "/musedata/corelli/op5"),
    ("Classical_Chamber", "Arcangelo_Corelli", "Concerti_Grossi_Op6", "/musedata/corelli/op6"),

    # --- Antonio Vivaldi ---
    ("Classical_Orchestral", "Antonio_Vivaldi", "Concertos_Op01", "/musedata/vivaldi/op01"),
    ("Classical_Orchestral", "Antonio_Vivaldi", "Concertos_Op02", "/musedata/vivaldi/op02"),
    ("Classical_Orchestral", "Antonio_Vivaldi", "Concertos_Op03_LEstro_Armonico", "/musedata/vivaldi/op03"),
    ("Classical_Orchestral", "Antonio_Vivaldi", "Concertos_Op04_La_Stravaganza", "/musedata/vivaldi/op04"),
    ("Classical_Orchestral", "Antonio_Vivaldi", "Concertos_Op05", "/musedata/vivaldi/op05"),
    ("Classical_Orchestral", "Antonio_Vivaldi", "Concertos_Op06", "/musedata/vivaldi/op06"),
    ("Classical_Orchestral", "Antonio_Vivaldi", "Concertos_Op07", "/musedata/vivaldi/op07"),
    ("Classical_Orchestral", "Antonio_Vivaldi", "Concertos_Op08_Four_Seasons", "/musedata/vivaldi/op08"),
    ("Classical_Orchestral", "Antonio_Vivaldi", "Concertos_Op09_La_Cetra", "/musedata/vivaldi/op09"),
    ("Classical_Orchestral", "Antonio_Vivaldi", "Concertos_Op10", "/musedata/vivaldi/op00"),

    # --- 20th Century & Serialism ---
    ("Classical_20th_Century", "Anton_Webern", "Selected_Works", "/users/craig/classical/webern"),
    ("Classical_20th_Century", "Arnold_Schoenberg", "Tone_Rows", "/osu/tonerow/schoenberg"),
    ("Classical_20th_Century", "Alban_Berg", "Tone_Rows", "/osu/tonerow/berg"),
    ("Classical_20th_Century", "Anton_Webern", "Tone_Rows", "/osu/tonerow/webern"),

    # --- Historical & Polish Editions ---
    ("Historical_Editions", "Polish_Historical_1500_1599", "Renaissance_Scores", "/users/mkonik/nifc-digital-editions/polish-scores/1500-1599"),
    ("Historical_Editions", "Polish_Historical_1600_1699", "Baroque_Scores", "/users/mkonik/nifc-digital-editions/polish-scores/1600-1699"),
    ("Historical_Editions", "Polish_Historical_1700_1799", "Classical_Scores", "/users/mkonik/nifc-digital-editions/polish-scores/1700-1799"),
    ("Historical_Editions", "Polish_Historical_1800_1899", "Romantic_Scores", "/users/mkonik/nifc-digital-editions/polish-scores/1800-1899"),
    ("Historical_Editions", "Orlandus_Lassus", "Geistliche_Psalmen", "/users/wolfgang/lassus/geistliche-psalmen"),
    ("Historical_Editions", "Mikolaj_Gomolka", "Psalterz_Melodies", "/users/jacek/gomolka"),
    ("Historical_Editions", "Maddalena_Casulana", "First_Book_of_Madrigals", "/users/deutsch/casulana"),
    ("Historical_Editions", "Hugo_Distler", "Choral_Works", "/users/lucas/distler"),
    ("Historical_Editions", "Tasso_in_Music", "Aminta_Tam", "/tasso/Tam"),
    ("Historical_Editions", "Tasso_in_Music", "Eclogues_Tec", "/tasso/Tec"),
    ("Historical_Editions", "Tasso_in_Music", "Rime_Trm", "/tasso/Trm"),
    ("Historical_Editions", "Tasso_in_Music", "Gerusalemme_Tsg", "/tasso/Tsg"),

    # --- Folk & Vocal Collections ---
    ("Folk_and_Vocal", "Traditional_German", "Essen_Allerlei_Keyboard", "/essen/europa/deutschl/allerkbd"),
    ("Folk_and_Vocal", "Traditional_German", "Essen_Altdeutsche_Lieder_1", "/essen/europa/deutschl/altdeu1"),
    ("Folk_and_Vocal", "Traditional_German", "Essen_Altdeutsche_Lieder_2", "/essen/europa/deutschl/altdeu2"),
    ("Folk_and_Vocal", "Traditional_German", "Essen_Boehme_Collection", "/essen/europa/deutschl/boehme"),
    ("Folk_and_Vocal", "Traditional_German", "Essen_DVA_Ballads", "/essen/europa/deutschl/dva"),
    ("Folk_and_Vocal", "Traditional_German", "Essen_Erk_Lieder", "/essen/europa/deutschl/erk"),
    ("Folk_and_Vocal", "Traditional_German", "Essen_Fink_Collection", "/essen/europa/deutschl/fink"),
    ("Folk_and_Vocal", "Traditional_German", "Essen_Kinderlieder", "/essen/europa/deutschl/kinder"),
    ("Folk_and_Vocal", "Traditional_German", "Essen_Zuccalmaglio", "/essen/europa/deutschl/zuccal"),
    ("Folk_and_Vocal", "Traditional_German", "Deutscher_Liederschatz_Band1", "/users/craig/songs/erk/liederschatz/band1"),
    ("Folk_and_Vocal", "Traditional_German", "Deutscher_Liederschatz_Band2", "/users/craig/songs/erk/liederschatz/band2"),
    ("Folk_and_Vocal", "Traditional_German", "Deutscher_Liederschatz_Band3", "/users/craig/songs/erk/liederschatz/band3"),

    ("Folk_and_Vocal", "Traditional_Chinese", "Essen_China_Han", "/essen/asia/china/han"),
    ("Folk_and_Vocal", "Traditional_Chinese", "Essen_China_Natmin", "/essen/asia/china/natmin"),
    ("Folk_and_Vocal", "Traditional_Chinese", "Essen_China_Shanxi", "/essen/asia/china/shanxi"),
    ("Folk_and_Vocal", "Traditional_Chinese", "Essen_China_Xinhua", "/essen/asia/china/xinhua"),
    ("Folk_and_Vocal", "Traditional_Chinese", "OSU_Chinese_Folksongs", "/osu/monophony/chinese"),

    ("Folk_and_Vocal", "Traditional_European", "Essen_Austria", "/essen/europa/oesterrh"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Tirol", "/essen/europa/tirol"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_France", "/essen/europa/france"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Alsace", "/essen/europa/elsass"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Lorraine", "/essen/europa/lothring"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_England", "/essen/europa/england"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Czech", "/essen/europa/czech"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Poland", "/essen/europa/polska"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Hungary", "/essen/europa/magyar"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Romania", "/essen/europa/romania"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Russia", "/essen/europa/rossiya"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Ukraine", "/essen/europa/ukraina"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Yugoslavia", "/essen/europa/jugoslav"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Italy", "/essen/europa/italia"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Switzerland", "/essen/europa/schweiz"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Sweden", "/essen/europa/sverige"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Denmark", "/essen/europa/danmark"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Netherlands", "/essen/europa/nederlan"),
    ("Folk_and_Vocal", "Traditional_European", "Essen_Luxembourg", "/essen/europa/luxembrg"),
    ("Folk_and_Vocal", "Traditional_European", "Irish_Songs_Sagrillo", "/users/sagrillo/ireland"),
    ("Folk_and_Vocal", "Traditional_European", "Friuli_Folk_Songs", "/ccarh/songs/friuli"),
    ("Folk_and_Vocal", "Traditional_European", "Nova_Scotia_Creighton", "/users/craig/songs/creighton/nova"),

    ("Folk_and_Vocal", "Native_American_Densmore", "Sioux_Songs", "/users/craig/songs/densmore/sioux"),
    ("Folk_and_Vocal", "Native_American_Densmore", "Pawnee_Songs", "/osu/densmore/pawnee"),
    ("Folk_and_Vocal", "Native_American_Densmore", "Chippewa_Ojibway_Songs", "/osu/densmore/ojibway"),

    ("Folk_and_Vocal", "Stephen_Foster", "Vocal_Melodies", "/osu/monophony/foster"),
    ("Folk_and_Vocal", "George_Gershwin", "Monophonic_Songs", "/osu/monophony/gershwin"),
    ("Folk_and_Vocal", "Franz_Schubert", "Lieder_Melodies", "/osu/monophony/schubert"),
    ("Folk_and_Vocal", "Traditional_Barbershop", "Barbershop_Quartets", "/osu/barbershop"),
    ("Folk_and_Vocal", "Gregorian_Chant", "Liber_Usualis_OSU", "/osu/chant/liber"),
    ("Folk_and_Vocal", "Gregorian_Chant", "Liber_Usualis_McGill", "/mcgill/liber"),
]


def sanitize_filename(name: str) -> str:
    """Sanitize string to be safe for filenames."""
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    name = re.sub(r"\s+", "_", name.strip())
    name = re.sub(r"_+", "_", name)
    return name[:120]


def extract_metadata_from_krn(krn_text: str):
    """Extract standard Humdrum reference records."""
    meta = {}
    for line in krn_text.splitlines():
        if line.startswith("!!!"):
            match = re.match(r"^!!!([A-Za-z0-9]+):\s*(.*)$", line)
            if match:
                key, val = match.groups()
                meta[key] = val.strip()
    return meta


def generate_piece_name(raw_filename: str, krn_text: str) -> str:
    """Generate a clean descriptive piece name based on filename and metadata."""
    meta = extract_metadata_from_krn(krn_text)
    base_name = os.path.splitext(os.path.basename(raw_filename))[0]

    title = meta.get("OTL")
    opus = meta.get("OPS")
    num = meta.get("ONM")
    mov = meta.get("OMV")

    parts = []
    if title:
        parts.append(title)
    if opus and (f"op" not in title.lower() if title else True):
        parts.append(f"Op{opus}")
    if num and (f"no" not in title.lower() if title else True):
        parts.append(f"No{num}")
    if mov:
        parts.append(f"Mov{mov}")

    if parts:
        clean_title = sanitize_filename(" ".join(parts))
        return f"{base_name}_{clean_title}" if len(clean_title) < 80 else clean_title
    return base_name


def convert_single_krn_task(task_args):
    """Worker task to parse Humdrum krn and write MusicXML."""
    import music21

    category, composer, collection, raw_fname, krn_bytes, out_dir = task_args
    try:
        krn_text = krn_bytes.decode("utf-8", errors="ignore")
        piece_name = generate_piece_name(raw_fname, krn_text)
        out_filename = f"{piece_name}.musicxml"
        out_filepath = os.path.join(out_dir, out_filename)

        # Check if already exists and is non-empty
        if os.path.exists(out_filepath) and os.path.getsize(out_filepath) > 500:
            return {
                "status": "skipped",
                "composer": composer,
                "collection": collection,
                "file": out_filename,
                "path": out_filepath,
                "size": os.path.getsize(out_filepath),
            }

        # Parse with music21
        score = music21.converter.parseData(krn_text, format="humdrum")

        # Ensure metadata title and composer are preserved
        meta = extract_metadata_from_krn(krn_text)
        if score.metadata is None:
            score.metadata = music21.metadata.Metadata()
        if "COM" in meta and not score.metadata.composer:
            score.metadata.composer = meta["COM"]
        if "OTL" in meta and not score.metadata.title:
            score.metadata.title = meta["OTL"]

        # Export MusicXML
        score.write("musicxml", fp=out_filepath)

        return {
            "status": "success",
            "composer": composer,
            "collection": collection,
            "file": out_filename,
            "path": out_filepath,
            "size": os.path.getsize(out_filepath),
        }
    except Exception as e:
        return {
            "status": "error",
            "composer": composer,
            "collection": collection,
            "file": raw_fname,
            "error": str(e),
        }


def download_collection_zip(url_path: str, retries: int = 3) -> bytes:
    """Download ZIP archive from KernScores with retry logic."""
    url = f"http://kern.ccarh.org/cgi-bin/ksdata?l={url_path}&format=zip"
    headers = {"User-Agent": "Mozilla/5.0 (KernScores MusicXML Exporter)"}
    req = urllib.request.Request(url, headers=headers)

    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                data = resp.read()
                if len(data) > 0:
                    return data
        except Exception as e:
            if attempt == retries:
                raise e
            time.sleep(2 * attempt)
    return b""


def main():
    print("=" * 70)
    print("  Stanford CCRH KernScores 全量乐谱批量下载与 MusicXML 分类转换")
    print(f"  CPU 核心数: {os.cpu_count()} | 输出目录: {OUTPUT_BASE_DIR}")
    print("=" * 70)

    OUTPUT_BASE_DIR.mkdir(parents=True, exist_ok=True)

    total_collections = len(COLLECTIONS_CATALOG)
    print(f"\n[1/3] 正在加载并下载 {total_collections} 个作品集归档...")

    all_conversion_tasks = []
    download_stats = {
        "collections_success": 0,
        "collections_failed": 0,
        "total_krn_found": 0,
    }

    for idx, (category, composer, collection, path) in enumerate(COLLECTIONS_CATALOG, 1):
        coll_dir = OUTPUT_BASE_DIR / composer / collection
        coll_dir.mkdir(parents=True, exist_ok=True)

        sys.stdout.write(f"\r[{idx:02d}/{total_collections:02d}] 正在获取: {composer} / {collection} ...")
        sys.stdout.flush()

        try:
            zip_bytes = download_collection_zip(path)
            if not zip_bytes:
                download_stats["collections_failed"] += 1
                continue

            z = zipfile.ZipFile(io.BytesIO(zip_bytes))
            krn_files = [n for n in z.namelist() if n.endswith(".krn") and not n.startswith("__MACOSX")]

            if not krn_files:
                continue

            download_stats["collections_success"] += 1
            download_stats["total_krn_found"] += len(krn_files)

            for fname in krn_files:
                file_bytes = z.read(fname)
                all_conversion_tasks.append((category, composer, collection, fname, file_bytes, str(coll_dir)))

        except Exception as err:
            download_stats["collections_failed"] += 1
            print(f"\n  [警告] 下载失败 {composer}/{collection} ({path}): {err}")

    print(f"\n\n[2/3] 下载完成！已检索到 {len(all_conversion_tasks)} 首乐谱，启动多进程并行转换...")

    # Multi-process parallel conversion
    num_workers = min(12, os.cpu_count() or 4)
    results = {
        "success": [],
        "skipped": [],
        "error": [],
    }

    start_time = time.time()
    total_tasks = len(all_conversion_tasks)

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(convert_single_krn_task, task): task for task in all_conversion_tasks}
        completed = 0

        for future in as_completed(futures):
            completed += 1
            res = future.result()
            status = res["status"]
            results[status].append(res)

            if completed % 25 == 0 or completed == total_tasks:
                elapsed = time.time() - start_time
                rate = completed / elapsed if elapsed > 0 else 0
                pct = (completed / total_tasks) * 100
                sys.stdout.write(
                    f"\r  转换进度: [{completed:04d}/{total_tasks:04d}] {pct:5.1f}% | "
                    f"成功: {len(results['success'])} | 速率: {rate:.1f} 首/秒 | 耗时: {elapsed:.0f}s"
                )
                sys.stdout.flush()

    total_time = time.time() - start_time
    print(f"\n\n[3/3] 转换完成！总耗时: {total_time:.2f} 秒")

    # Generate Manifest & Summary Report
    manifest = {
        "generation_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_scores_discovered": total_tasks,
        "total_musicxml_converted": len(results["success"]) + len(results["skipped"]),
        "total_errors": len(results["error"]),
        "conversion_time_seconds": round(total_time, 2),
        "scores_by_composer": {},
    }

    # Group scores by composer & collection
    for r in results["success"] + results["skipped"]:
        comp = r["composer"]
        coll = r["collection"]
        if comp not in manifest["scores_by_composer"]:
            manifest["scores_by_composer"][comp] = {}
        if coll not in manifest["scores_by_composer"][comp]:
            manifest["scores_by_composer"][comp][coll] = []
        manifest["scores_by_composer"][comp][coll].append({
            "file": r["file"],
            "path": r["path"],
            "size_bytes": r["size"],
        })

    manifest_path = WORKSPACE_DIR / "scores_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    # Markdown Summary
    summary_path = WORKSPACE_DIR / "scores_summary.md"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("# Stanford KernScores 全量乐谱下载与 MusicXML 分类转换报告\n\n")
        f.write(f"- **生成时间**：{manifest['generation_time']}\n")
        f.write(f"- **检索总曲目数**：{manifest['total_scores_discovered']}\n")
        f.write(f"- **成功转换 MusicXML 总数**：{manifest['total_musicxml_converted']}\n")
        f.write(f"- **转换失败数**：{manifest['total_errors']}\n")
        f.write(f"- **总执行耗时**：{manifest['conversion_time_seconds']} 秒\n")
        f.write(f"- **输出主目录**：`musicxml_scores/`\n\n")

        f.write("## 乐谱分类统计明细\n\n")
        f.write("| 作曲家 / 归属类别 | 作品集 (Collection) | MusicXML 曲目数 |\n")
        f.write("| :--- | :--- | :--- |\n")

        for comp, collections in sorted(manifest["scores_by_composer"].items()):
            for coll, items in sorted(collections.items()):
                f.write(f"| **{comp.replace('_', ' ')}** | {coll.replace('_', ' ')} | {len(items)} 首 |\n")

        if results["error"]:
            f.write("\n## 异常与跳过记录\n\n")
            for err in results["error"][:50]:
                f.write(f"- `{err['composer']}/{err['collection']}/{err['file']}`: {err['error']}\n")

    print("=" * 70)
    print(f"  全部完成！")
    print(f"  - 成功转换: {manifest['total_musicxml_converted']} 首 MusicXML 乐谱")
    print(f"  - 详细索引清单: {manifest_path}")
    print(f"  - 分类统计报表: {summary_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
