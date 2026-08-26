# 🎹 MXLPianoScores (高品质古典与教学钢琴独奏乐谱库)

[![MusicXML](https://img.shields.io/badge/Format-MusicXML_%2F_MXL-blue.svg)](https://www.w3.org/2021/06/musicxml40/)
[![License: CC0 / Public Domain](https://img.shields.io/badge/License-Public_Domain_%2F_CC0-brightgreen.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Total Scores](https://img.shields.io/badge/Total_Scores-5%2C897_Scores-orange.svg)](#-收录作品集概览)
[![Piano Solo](https://img.shields.io/badge/Instrument-100%25_Grand_Staff_Piano_Solo-purple.svg)](#)

本开源库收录了经过规范化整理、100% 结构与节拍校验、声部清洗的**高品质古典与教学钢琴独奏 (Piano Solo)** 乐谱库。全库共收录 **5,897** 首乐谱，全部统一封装为标准压缩版 `.mxl` (MusicXML) 格式，各数据集独立分目录存放，并提供完整中英文双语索引与结构化机器元数据。

---

## 📊 收录作品集概览 (共 12 大独立数据集)

| 数据集目录 | 收录内容与代表作品 | 乐谱总数 | 谱表结构 | 版权与来源 |
| :--- | :--- | :--- | :--- | :--- |
| [**Czerny**](./Czerny) | 车尔尼练习曲全套 (Op.599 + Op.849 + Op.299 + Op.740 + Op.821) | **380** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**Hanon**](./Hanon) | 夏尔-路易·哈农《钢琴练指法》(The Virtuoso Pianist) 全集 (No.01~60) | **60** 首 | 钢琴双行大谱表 | Public Domain (完全免费商用) |
| [**Burgmuller**](./Burgmuller) | 布格缪勒《25首简易与进阶练习曲》(Op.100 全集) | **25** 首 | 钢琴双行大谱表 | Public Domain (Mutopia 历史版) |
| [**Beyer**](./Beyer) | 费迪南德·拜厄《钢琴初步教程》(Op.101 全集 No.001~106) | **106** 首 | 钢琴双行大谱表 | Public Domain (LilyPond 原典版) |
| [**Bach_Beginner**](./Bach_Beginner) | 巴赫初中级复调全集 (初级曲集28首 + 小前奏曲18首 + 二部创意曲15首) | **61** 首 | 钢琴双行大谱表 | Public Domain (Stanford CCARH) |
| [**Sonatinas**](./Sonatinas) | 小奏鸣曲与古典奏鸣曲 (克莱门蒂Op.36 + 库劳 + 迪亚贝利 + 莫扎特K.545 + 贝多芬Op.49) | **72** 乐章 | 钢琴双行大谱表 | Public Domain (Stanford CCARH) |
| [**Schumann_Album_for_the_Young**](./Schumann_Album_for_the_Young) | 罗伯特·舒曼《少年曲集》(Op.68 全套43首) | **43** 首 | 钢琴双行大谱表 | Public Domain (Rach3 ISMIR 原典) |
| [**Tchaikovsky_Childrens_Album**](./Tchaikovsky_Childrens_Album) | 柴可夫斯基《儿童钢琴曲集》(Op.39 全套24首) | **24** 首 | 钢琴双行大谱表 | Public Domain (标准双谱表) |
| [**Grieg_Lyric_Pieces**](./Grieg_Lyric_Pieces) | 爱德华·格里格《抒情小品集》(10卷全套66首) | **66** 首 | 钢琴双行大谱表 | Public Domain / CC0 (洛桑理工 DCMLab) |
| [**Technique_Studies**](./Technique_Studies) | 初中级技巧练习曲 (施密特Op.16 + 柯勒 + 贝伦斯Op.70 + 杜弗诺伊Op.120 + 海勒Op.45/46) | **160** 首 | 钢琴双行大谱表 | Public Domain (标准双谱表) |
| [**KernScores**](./KernScores) | 斯坦福大学经典名作库 (巴赫、贝多芬、肖邦、莫扎特、斯卡拉蒂等) | **3,480** 首 | 钢琴双行大谱表 | CC BY-NC-SA / Academic |
| [**OpenScore**](./OpenScore) | OpenScore 123 位大师艺术歌曲纯钢琴双谱表伴奏独奏版 (0空白小节) | **1,420** 首 | 钢琴双行大谱表 | **CC0 1.0 Universal (无限制商用)** |
| **全库合计** | **从启蒙、练习曲、小奏鸣曲到浪漫派名作的完整钢琴乐谱库** | **5,897** 首 | **100% 钢琴双行大谱表** | **均包含 manifest.json 清单** |

---

## 📁 目录结构说明

```text
MXLPianoScores/
├── Bach_Beginner/                      # 巴赫初中级复调 (初级曲集 / 小前奏曲 / 二部创意曲)
├── Beyer/                              # 拜厄《钢琴初步教程》Op. 101 全套 106 首
├── Burgmuller/                          # 布格缪勒《进阶练习曲25首》Op. 100 全套 25 首
├── Czerny/                              # 车尔尼练习曲全套 (Op.599 / 849 / 299 / 740 / 821)
├── Grieg_Lyric_Pieces/                 # 格里格《抒情小品集》10卷 66 首全集
├── Hanon/                               # 哈农《钢琴练指法》60 首全集
├── KernScores/                          # 斯坦福大学 CCARH 经典大师名作库 (3,480 首)
├── OpenScore/                           # 国际 OpenScore 艺术歌曲纯钢琴独奏库 (1,420 首)
├── Schumann_Album_for_the_Young/       # 舒曼《少年曲集》Op. 68 全套 43 首
├── Sonatinas/                          # 经典小奏鸣曲全集 (克莱门蒂 / 库劳 / 迪亚贝利 / 莫扎特 / 贝多芬)
├── Tchaikovsky_Childrens_Album/        # 柴可夫斯基《儿童钢琴曲集》Op. 39 全套 24 首
├── Technique_Studies/                  # 施密特 / 柯勒 / 贝伦斯 / 杜弗诺伊 / 海勒练习曲
├── scripts/                            # 自动化质检、目录构建与转换工具
├── APP_STORE_SUBMISSION_GUIDE.md    # 苹果 App Store 提审与版权合规实战指南
├── COPYRIGHT_AND_COMMERCIAL_LICENSE.md # 乐谱版权与免费商用许可合规说明书
├── GLOBAL_PIANO_SOLO_CATALOG.md        # 全量作品逐曲详细中英文索引与百科
├── Piano_Solo_MusicXML_Guide.md        # 开发者与乐谱格式集成指南
└── global_scores_index.json            # 机器可读的 5,897 条结构化元数据数据库
```

---

## ⚖️ 版权与免费商用许可

本曲库收录的古典音乐作品本身 **100% 处于公有领域 (Public Domain)**，数字化乐谱编码均遵循 **CC0 1.0 Universal / Public Domain** 协议，支持**无偿、免版税的商业化应用**（包括移动端 App 嵌入、SaaS 云服务、AI 算法训练、教材出版与教学等）。

* 👉 **完整版权法律剖析与商用合规指南**：[📄 COPYRIGHT_AND_COMMERCIAL_LICENSE.md](./COPYRIGHT_AND_COMMERCIAL_LICENSE.md)
* 🍎 **苹果 App Store 提审与审核备注模板**：[📄 APP_STORE_SUBMISSION_GUIDE.md](./APP_STORE_SUBMISSION_GUIDE.md)

---

## 🔍 程序化读取示例 (Python)

```python
import json

with open("global_scores_index.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

print(f"总收录曲目数: {catalog['total_scores']}")

# 查询肖邦的所有作品
chopin_scores = [s for s in catalog["scores"] if "Chopin" in s["composer"]]
print(f"肖邦作品数: {len(chopin_scores)}")
```

---

## 🛠️ 质量验证

您可以随时运行自动化质量审计脚本检验全库 5,897 首乐谱的 XML 容器有效性、大谱表结构与小节节拍完整性：

```bash
python3 scripts/validate_scores_quality.py
```

