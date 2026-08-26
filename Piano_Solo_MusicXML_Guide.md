# 🎹 Piano Solo (钢琴独奏) MusicXML / MXL 乐谱数据集总览与指南

本工作区收录并规范化整理了 **5,877** 首 100% 结构校验与声部清洗的**高品质古典与教学钢琴独奏 (Piano Solo)** 乐谱库，各数据集独立分目录存放，全部统一封装为标准压缩版 `.mxl` 格式。

---

## 📊 当前收录乐谱数据集概览 (共 12 大独立数据集)

| 数据集名称 (Directory) | 收录内容与代表作品 | 乐谱总数 | 谱表结构 | 版权状态 |
| :--- | :--- | :--- | :--- | :--- |
| [**Czerny**](file:///Users/shiyuli/Dev/Scores/Czerny) | 车尔尼练习曲全集 (Op.599 + Op.849 + Op.299 + Op.740 + Op.821) | **380** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**Hanon**](file:///Users/shiyuli/Dev/Scores/Hanon) | 夏尔-路易·哈农《钢琴练指法》(The Virtuoso Pianist) 全集 (No.01~60) | **60** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**Burgmuller**](file:///Users/shiyuli/Dev/Scores/Burgmuller) | 布格缪勒《25首简易与进阶练习曲》(Op.100 全集) | **25** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**Beyer**](file:///Users/shiyuli/Dev/Scores/Beyer) | 费迪南德·拜厄《钢琴初步教程》(Op.101 全集 No.001~106) | **106** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**Bach_Beginner**](file:///Users/shiyuli/Dev/Scores/Bach_Beginner) | 巴赫初中级复调全集 (初级曲集28首 + 小前奏曲18首 + 二部创意曲15首) | **61** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**Sonatinas**](file:///Users/shiyuli/Dev/Scores/Sonatinas) | 小奏鸣曲与古典奏鸣曲 (克莱门蒂Op.36 + 库劳 + 迪亚贝利 + 莫扎特K.545 + 贝多芬Op.49) | **52** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**Schumann_Album_for_the_Young**](file:///Users/shiyuli/Dev/Scores/Schumann_Album_for_the_Young) | 罗伯特·舒曼《少年曲集》(Op.68 全套43首) | **43** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**Tchaikovsky_Childrens_Album**](file:///Users/shiyuli/Dev/Scores/Tchaikovsky_Childrens_Album) | 柴可夫斯基《儿童钢琴曲集》(Op.39 全套24首) | **24** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**Grieg_Lyric_Pieces**](file:///Users/shiyuli/Dev/Scores/Grieg_Lyric_Pieces) | 爱德华·格里格《抒情小品集》(10卷全套66首) | **66** 首 | 钢琴双行大谱表 | Public Domain / CC0 (完全免费商用) |
| [**Technique_Studies**](file:///Users/shiyuli/Dev/Scores/Technique_Studies) | 初中级技巧练习曲 (施密特Op.16 + 柯勒 + 贝伦斯Op.70 + 杜弗诺伊Op.120 + 海勒Op.45/46) | **160** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**KernScores**](file:///Users/shiyuli/Dev/Scores/KernScores) | 斯坦福大学经典名作库 (巴赫、贝多芬、肖邦、莫扎特、斯卡拉蒂等) | **3,480** 首 | 钢琴双行大谱表 | CC BY-NC-SA / Academic |
| [**OpenScore**](file:///Users/shiyuli/Dev/Scores/OpenScore) | OpenScore 123 位大师艺术歌曲纯钢琴双谱表伴奏独奏版 (0空白小节) | **1,420** 首 | 钢琴双行大谱表 | **CC0 1.0 Universal (无限制商用)** |
| **全库合计** | **从启蒙、练习曲、小奏鸣曲到浪漫派名作的完整钢琴乐谱库** | **5,877** 首 | **100% 钢琴双行大谱表** | **均包含 manifest.json 清单** |

---

## 一、 斯坦福大学 KernScores 数据库（海量古典曲目）

斯坦福大学 CCRH 维护的 [KernScores](http://kern.ccarh.org/) 拥有全球最大的公有领域古典音乐数字乐谱库，包含数千首钢琴独奏（贝多芬全部 32 首钢琴奏鸣曲、肖邦全部前奏曲/夜曲/练习曲、巴赫平均律/创意曲、莫扎特奏鸣曲、斯科特·乔普林爵士钢琴等）。

* **版权状态**：100% 公有领域（Public Domain），完全免费可商用。
* **原始格式**：`**kern`。
* **转换方式**：使用 Python 库 `music21` 自动解析并导出为标准 `.musicxml`。

### 1. 单曲抓取与导出示例 (Python)
```python
# 运行前安装依赖: pip install music21
import music21

# 示例：抓取贝多芬第一奏鸣曲第一乐章
url = "http://kern.ccarh.org/data?l=beethoven/sonatas&file=sonata01-1.krn"
score = music21.converter.parse(url)

# 导出为 MusicXML
output_path = "beethoven_sonata_01_1.musicxml"
score.write('musicxml', fp=output_path)
print(f"导出成功: {output_path}")
```

### 2. 批量抓取示例 (Python)
```python
import os
import music21

composers = {
    "chopin_preludes": "http://kern.ccarh.org/data?l=chopin/preludes&file=prelude28-01.krn",
    "beethoven_sonata1": "http://kern.ccarh.org/data?l=beethoven/sonatas&file=sonata01-1.krn",
    "bach_invention1": "http://kern.ccarh.org/data?l=bach/inventions&file=inven01.krn",
    "joplin_maple_leaf": "http://kern.ccarh.org/data?l=joplin&file=maple.krn"
}

output_dir = "./output_musicxml"
os.makedirs(output_dir, exist_ok=True)

for name, url in composers.items():
    try:
        score = music21.converter.parse(url)
        out_file = os.path.join(output_dir, f"{name}.musicxml")
        score.write('musicxml', fp=out_file)
        print(f"成功导出: {out_file}")
    except Exception as e:
        print(f"导出 {name} 失败: {e}")
```

---

## 二、 Python `music21` 内置公版乐谱库（零配置开箱即用）

`music21` 本身自带了庞大的本地古典乐语料库，无需联网下载即可直接提取大量公版曲目。

### 批量提取本地语料库中的古典曲目：
```python
import os
import music21

output_dir = "./music21_builtin_scores"
os.makedirs(output_dir, exist_ok=True)

target_composers = ['bach', 'beethoven', 'haydn', 'mozart', 'schumann']

for composer in target_composers:
    paths = music21.corpus.getComposer(composer)
    print(f"找到 {composer} 乐谱 {len(paths)} 首，正在导出...")
    for p in paths:
        try:
            score = music21.corpus.parse(p)
            file_name = f"{composer}_{os.path.splitext(os.path.basename(str(p)))[0]}.musicxml"
            score.write('musicxml', fp=os.path.join(output_dir, file_name))
        except Exception as e:
            continue

print("全部内置公版乐谱导出完成！")
```

---

## 三、 OpenScore 项目（人工校对高品质 CC0 乐谱）

[OpenScore](https://openscore.cc/) 是 MuseScore 社区和开源基金会发起的数字化项目，由专业制谱师校对转录。

* **版权协议**：**CC0 (Public Domain Dedication)**，允许任何商业用途。
* **项目地址**：[GitHub - OpenScore](https://github.com/OpenScore)
* **包含库**：
  * `OpenScore/LiederCorpus`：包含大量舒伯特、舒曼等艺术歌曲钢琴伴奏与独奏乐谱。
  * `OpenScore Piano Corpus`：钢琴独奏专题。

### MuseScore 命令行批量转换工具：
如果下载到的是 `.mscz` / `.mscx` 格式，可通过 MuseScore CLI 批量导出为 `.musicxml`：
```bash
# macOS 示例 (假设安装了 MuseScore 4)
for f in *.mscz; do
    /Applications/MuseScore\ 4.app/Contents/MacOS/mscore -o "${f%.mscz}.musicxml" "$f"
done
```

---

## 四、 公版 MIDI 批量转录为 MusicXML

适用于从公版 MIDI 网站（如 [Mutopia Project](https://www.mutopiaproject.org/)）获取的大量 MIDI 文件。

### 1. 使用 MuseScore CLI 批量转 MusicXML
```bash
for f in *.mid; do
    /Applications/MuseScore\ 4.app/Contents/MacOS/mscore -o "${f%.mid}.musicxml" "$f"
done
```

### 2. 使用 Python 脚本批量转换
```python
import os
import music21

midi_dir = "./midi_files"
xml_dir = "./converted_musicxml"
os.makedirs(xml_dir, exist_ok=True)

for file in os.listdir(midi_dir):
    if file.endswith((".mid", ".midi")):
        midi_path = os.path.join(midi_dir, file)
        out_name = os.path.splitext(file)[0] + ".musicxml"
        out_path = os.path.join(xml_dir, out_name)
        try:
            score = music21.converter.parse(midi_path)
            score.write('musicxml', fp=out_path)
            print(f"转换成功: {file} -> {out_name}")
        except Exception as e:
            print(f"转换失败 {file}: {e}")
```

---

## 五、 钢琴独奏（Piano Solo）专属开发避坑指南

1. **大谱表分轨（Grand Staff / Two Staves）**：
   * 某些单轨 MIDI 转换后可能把左右手音符混在同一高音谱号中。
   * 建议在导出或转换时指定为钢琴大谱表（Part Staff 1: Treble, Staff 2: Bass）。在 `music21` 中可用 `music21.midi.translate.midiToScore()` 进行左右手声部切分。
2. **基础练习曲资源（哈农、拜厄、车尔尼）**：
   * **哈农（Hanon Virtuoso Pianist）全 60 首** 与 **拜厄（Beyer Op.101）** 是钢琴学习的核心资产，且完全处于公有领域。
   * 可直接在 KernScores 或 Mutopia 上检索 `Hanon` 或 `Beyer` 一键批量生成全套教学基础库。
3. **格式兼容性建议**：
   * 在移动端 / Web 端渲染（如 OpenSheetMusicDisplay 或 Verovio）时，建议优先使用**未压缩的 `.musicxml` / `.xml`**，或标准压缩的 `.mxl` 格式。
