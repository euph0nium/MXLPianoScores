# 🎵 古典音乐家信息库 (Composers Database)

本目录为当前乐谱库（5,897+ 首 MusicXML 乐谱）收录的所有核心古典音乐作曲家提供完整的**艺术生平介绍**、**代表作目录**、**对应本地乐谱路径**以及**标准化视觉资产（1:1 满版淡雅水彩工笔插画 JPG）**。

---

## 🎨 视觉设计与技术规范

- **风格定位**：淡雅水彩工笔插画风（Subtle Pastel Watercolor & Fine Line Art）
- **格式规范**：**标准 JPG 格式（画质 95%）**，1:1 纯矩形满版画幅（无圆形边框限制，水彩背景无缝填满整个矩形）。
- **资产文件**：
  - `avatar.jpg`: 1:1 满版矩形胸像头像（适合列表、作者个人主页、支持 App 自由裁剪）
  - `illustration.jpg`: 1:1 钢琴/管风琴全景艺术情境插画（适合专栏封面、介绍背景）
  - `info.json`: 供 App / Web 客户端直接解析调用的结构化数据
  - `README.md`: Markdown 格式的中英文生平与权威导聆

---

## 📂 目录结构示例

```text
作家信息/
├── README.md                      # 目录索引与全局规范说明
├── 肖邦/                         # Frédéric Chopin
│   ├── avatar.jpg                 # 肖邦满版淡雅水彩头像 (1:1 JPG)
│   ├── illustration.jpg           # 肖邦全景演奏艺术插画 (1:1 JPG)
│   ├── README.md                  # Markdown 格式生平与代表作
│   └── info.json                  # App 结构化 JSON 元数据
├── 巴赫/                         # J.S. Bach
│   ├── avatar.jpg                 # 巴赫满版淡雅水彩头像 (1:1 JPG)
│   ├── illustration.jpg           # 巴赫管风琴全景演奏插画 (1:1 JPG)
│   ├── README.md                  # Markdown 格式生平与代表作
│   └── info.json                  # App 结构化 JSON 元数据
├── 贝多芬/                       # Ludwig van Beethoven
│   ├── README.md
│   └── info.json
├── 莫扎特/                       # Wolfgang Amadeus Mozart
│   ├── README.md
│   └── info.json
└── ...                            # 更多作曲家目录
```

---

## 🎼 全库作曲家名录索引 (共 17 位核心作曲家)

| 作曲家 | 外文全名 | 艺术时期 / 流派 | 代表性称号 | 本地乐谱库对应专集 | 目录链接 | 视觉状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **肖邦** | Frédéric Chopin | 浪漫主义 | “钢琴诗人” | `KernScores/chopin` | [进入详情](./肖邦/README.md) | ✅ 头像 + 插画就绪 |
| **巴赫** | J.S. Bach | 巴洛克 | “西方音乐之父” | `Bach_Beginner`, `KernScores/bach` | [进入详情](./巴赫/README.md) | ✅ 头像 + 插画就绪 |
| **贝多芬** | Ludwig van Beethoven | 古典 / 早期浪漫 | “乐圣” | `KernScores/beethoven`, `Sonatinas` | [进入详情](./贝多芬/README.md) | 📝 档案与数据就绪 |
| **莫扎特** | W.A. Mozart | 古典主义 | “音乐神童” | `KernScores/mozart`, `Sonatinas` | [进入详情](./莫扎特/README.md) | 📝 档案与数据就绪 |
| **海顿** | Franz Joseph Haydn | 古典主义 | “交响乐之父” | `KernScores/haydn` | [进入详情](./海顿/README.md) | 📝 档案与数据就绪 |
| **车尔尼** | Carl Czerny | 古典 / 浪漫过渡 | “现代钢琴教学之父” | `Czerny (Op.599/849/299/740)` | [进入详情](./车尔尼/README.md) | 📝 档案与数据就绪 |
| **布格缪勒** | Friedrich Burgmüller | 浪漫主义 | “叙事练习曲大师” | `Burgmuller (Op.100/105/109)` | [进入详情](./布格缪勒/README.md) | 📝 档案与数据就绪 |
| **拜厄** | Ferdinand Beyer | 浪漫主义 | “钢琴启蒙奠基人” | `Beyer (Op.101)` | [进入详情](./拜厄/README.md) | 📝 档案与数据就绪 |
| **哈农** | Charles-Louis Hanon | 技巧训练宗师 | “钢琴手指机能宗师” | `Hanon (60 Virtuoso Exercises)` | [进入详情](./哈农/README.md) | 📝 档案与数据就绪 |
| **舒曼** | Robert Schumann | 浪漫主义全盛期 | “浪漫主义音乐诗人” | `Schumann_Album_for_the_Young` | [进入详情](./舒曼/README.md) | 📝 档案与数据就绪 |
| **柴可夫斯基** | P.I. Tchaikovsky | 俄罗斯浪漫派 | “俄罗斯旋律之王” | `Tchaikovsky_Childrens_Album` | [进入详情](./柴可夫斯基/README.md) | 📝 档案与数据就绪 |
| **格里格** | Edvard Grieg | 民族乐派 / 浪漫 | “北欧肖邦” | `Grieg_Lyric_Pieces (全10卷)` | [进入详情](./格里格/README.md) | 📝 档案与数据就绪 |
| **克莱门蒂** | Muzio Clementi | 古典主义 | “现代钢琴演奏之父” | `Sonatinas (Op.36)` | [进入详情](./克莱门蒂/README.md) | 📝 档案与数据就绪 |
| **舒伯特** | Franz Schubert | 早期浪漫主义 | “歌曲之王” | `KernScores/schubert`, `OpenScore` | [进入详情](./舒伯特/README.md) | 📝 档案与数据就绪 |
| **勃拉姆斯** | Johannes Brahms | 浪漫主义全盛期 | “三B巨匠之一” | `KernScores/brahms`, `OpenScore` | [进入详情](./勃拉姆斯/README.md) | 📝 档案与数据就绪 |
| **乔普林** | Scott Joplin | 拉格泰姆 / 爵士 | “拉格泰姆之王” | `KernScores/joplin` | [进入详情](./乔普林/README.md) | 📝 档案与数据就绪 |
| **库劳** | Friedrich Kuhlau | 古典浪漫过渡 | “小奏鸣曲名家” | `Sonatinas/Kuhlau` | [进入详情](./库劳/README.md) | 📝 档案与数据就绪 |
