# 🎹 MXLPianoScores (高品质原典与权威数字乐谱库)

[![MusicXML](https://img.shields.io/badge/Format-MusicXML_%2F_MXL-blue.svg)](https://www.w3.org/2021/06/musicxml40/)
[![License: CC0 / Public Domain](https://img.shields.io/badge/License-Public_Domain_%2F_CC0-brightgreen.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Total Scores](https://img.shields.io/badge/Total_Scores-5%2C077_Scores-orange.svg)](#-收录作品集概览)
[![Piano Solo](https://img.shields.io/badge/Instrument-100%25_Grand_Staff_Piano_Solo-purple.svg)](#)

本开源库收录了经过彻底质量审计、去重清洗与真伪核验的**高品质古典与专业数字乐谱库**。全库现存 **5,077** 首 100% 真实原典乐谱与权威数字化转录谱，全部统一封装为标准压缩版 `.mxl` (MusicXML) 格式，提供完整中英文双语索引与结构化机器元数据。

---

## 📊 收录作品集概览 (共 8 大核心真品数据集)

| 数据集目录 | 收录内容与代表作品 | 乐谱总数 | 谱表结构 | 版权与来源 |
| :--- | :--- | :---: | :--- | :--- |
| [**KernScores**](./scores/KernScores) | 斯坦福大学 CCARH 学术原典库（克莱门蒂 Op.36 小奏鸣曲全套、莫扎特奏鸣曲全套、巴赫、肖邦、贝多芬、海顿、斯卡拉蒂等） | **3,463** 首 | 钢琴双行大谱表 | CC BY-NC-SA / Academic Urtext |
| [**OpenScore**](./scores/OpenScore) | OpenScore 国际公共数字乐谱项目（艺术歌曲伴奏、古典四重奏与独奏名作） | **1,420** 首 | 钢琴双行大谱表 | **CC0 1.0 Universal (无限制商用)** |
| [**Bach_Beginner**](./scores/Bach_Beginner) | 约翰·塞巴斯蒂安·巴赫《二部创意曲全集》(15首)、《三部创意曲全集》(15首)、《安娜·玛格达莱娜笔记本》(20首)、《小前奏曲与小赋格》(17首) | **67** 首 | 钢琴双行大谱表 | Public Domain / CC0 (Mutopia & CCARH) |
| [**Grieg_Lyric_Pieces**](./scores/Grieg_Lyric_Pieces) | 爱德华·格里格《抒情小品集》(Op.12 ~ Op.71 全套 10 卷完整版，含第一卷 Op.12 初级名作) | **66** 首 | 钢琴双行大谱表 | Public Domain / CC0 (洛桑理工 DCMLab) |
| [**Schumann_Album_for_the_Young**](./scores/Schumann_Album_for_the_Young) | 罗伯特·舒曼《少年曲集》(Op.68 权威版，含士兵进行曲、快乐的农夫、猎歌、骑士等) | **32** 首 | 钢琴双行大谱表 | Public Domain / CC0 (ISMIR & Mutopia) |
| [**Burgmuller**](./scores/Burgmuller) | 约瑟夫·弗里德里希·布格缪勒《25首简易与进阶练习曲》(Op.100 真实原典版，含坦白、阿拉伯风格曲、牧歌、清澈的溪水等) | **18** 首 | 钢琴双行大谱表 | Public Domain / CC0 (Mutopia Project) |
| [**Sonatinas**](./scores/Sonatinas) | 贝多芬《致爱丽丝》(WoO 59)、贝多芬《简易奏鸣曲两首》(Op.49 No.1&2)、库劳《小奏鸣曲》(Op.20 No.1 全乐章) | **8** 首 | 钢琴双行大谱表 | Public Domain / CC0 (Mutopia Project) |
| [**Tchaikovsky_Childrens_Album**](./scores/Tchaikovsky_Childrens_Album) | 柴可夫斯基《儿童钢琴曲集》(Op.39 真谱，含早晨的祈祷、木兵进行曲、老法国之歌) | **3** 首 | 钢琴双行大谱表 | Public Domain / CC0 (Mutopia Project) |
| **全库合计** | **100% 真实原典与权威人工校对数字乐谱库** | **5,077** 首 | **100% 真实音符与结构** | **含 global_scores_index.json** |

---

## 📁 目录结构说明

```text
MXLPianoScores/
├── Composers/                          # 核心大师传记、肖像、代表作与元数据
├── scores/
│   ├── Bach_Beginner/                  # 巴赫初中级全集 (二部创意曲、三部创意曲、安娜笔记本、小前奏曲 67 首)
│   ├── Burgmuller/                     # 布格缪勒《25首进阶练习曲》Op. 100 真实原典 (18 首)
│   ├── Grieg_Lyric_Pieces/             # 格里格《抒情小品集》10卷 66 首全集 (EPFL DCMLab)
│   ├── KernScores/                     # 斯坦福 CCARH 原典库 (含克莱门蒂 Op.36、莫扎特、肖邦等 3,463 首)
│   ├── OpenScore/                      # 国际 OpenScore 艺术歌曲与器乐真谱库 (1,420 首 CC0)
│   ├── Schumann_Album_for_the_Young/   # 舒曼《少年曲集》Op. 68 真实版 (32 首)
│   ├── Sonatinas/                      # 小奏鸣曲与初级名曲 (贝多芬致爱丽丝、Op.49、库劳 Op.20 共 11 首)
│   └── Tchaikovsky_Childrens_Album/    # 柴可夫斯基《儿童曲集》Op. 39 (3 首)
├── scripts/                            # 自动化质检、目录构建与转换工具
├── APP_STORE_SUBMISSION_GUIDE.md       # 苹果 App Store 提审与版权合规实战指南
├── COPYRIGHT_AND_COMMERCIAL_LICENSE.md # 乐谱版权与免费商用许可合规说明书
├── GLOBAL_PIANO_SOLO_CATALOG.md        # 全量作品逐曲详细中英文索引与百科
├── Piano_Solo_MusicXML_Guide.md        # 开发者与乐谱格式集成指南
└── global_scores_index.json            # 机器可读的 5,080 条结构化元数据数据库
```

---

## ⚖️ 版权与免费商用许可

本曲库收录的古典音乐作品本身 **100% 处于公有领域 (Public Domain)**，数字化乐谱编码均遵循 **CC0 1.0 Universal / Public Domain / CC BY-NC-SA** 协议，支持**免版税的应用开发与教学**。

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

您可以随时运行自动化质量审计脚本检验全库 4,977 首乐谱的有效性：

```bash
python3 scripts/validate_scores_quality.py
```
