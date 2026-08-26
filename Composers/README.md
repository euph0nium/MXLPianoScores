# 🎵 Composers Database (古典音乐家数据库)

本目录为当前乐谱库（5,897+ 首 MusicXML 乐谱）收录的所有核心古典音乐作曲家提供完整的**艺术生平介绍**、**代表作目录**、**对应本地乐谱路径**以及**标准化视觉资产（1:1 满版淡雅水彩工笔插画 JPG）**。

---

## 🎨 视觉设计与技术规范

- **风格定位**：淡雅水彩工笔插画风（Subtle Pastel Watercolor & Fine Line Art）
- **格式规范**：**标准 JPG 格式（画质 95%）**，1:1 纯矩形满版画幅（无圆形边框限制，水彩背景无缝填满整个矩形）。
- **命名规则**：根目录与作家子目录均采用**英文标准名称（PascalCase）**，便于代码库工程化维护与 API 路由对接。
- **资产文件**：
  - `avatar.jpg`: 1:1 满版矩形胸像头像（适合列表、作者主页，支持 App 自由裁剪）
  - `illustration.jpg`: 1:1 钢琴/乐器全景艺术情境插画（适合专栏封面、介绍背景）
  - `info.json`: 供 App / Web 客户端直接解析调用的结构化数据
  - `README.md`: Markdown 格式的中英文生平与权威导聆

---

## 📂 目录结构 (Directory Structure)

```text
Composers/
├── README.md                      # 全局作曲家总索引
├── Chopin/                        # Frédéric Chopin
│   ├── avatar.jpg                 # 满版淡雅水彩头像 (1:1 JPG)
│   ├── illustration.jpg           # 全景演奏艺术插画 (1:1 JPG)
│   ├── README.md                  # 生平与代表作导聆
│   └── info.json                  # App 结构化 JSON 元数据
├── Bach/                          # Johann Sebastian Bach
│   ├── avatar.jpg
│   ├── README.md
│   └── info.json
├── Beethoven/                     # Ludwig van Beethoven
├── Mozart/                        # Wolfgang Amadeus Mozart
└── ...                            # 更多作曲家目录
```

---

## 🎼 全库作曲家名录索引 (Composers Catalog)

| 目录 (Folder) | 中文名 | 外文全名 (Full Name) | 艺术流派 | 代表性称号 | 本地乐谱库专集 | 目录链接 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`Chopin`** | 弗雷德里克·肖邦 | Frédéric François Chopin | 浪漫主义时期 (Romantic) | 钢琴诗人 | `KernScores/chopin` | [进入 `Chopin`](./Chopin/README.md) |
| **`Bach`** | 约翰·塞巴斯蒂安·巴赫 | Johann Sebastian Bach | 巴洛克时期 (Baroque) | 西方现代音乐之父 | `Bach_Beginner`, `KernScores/bach` | [进入 `Bach`](./Bach/README.md) |
| **`Beethoven`** | 路德维希·凡·贝多芬 | Ludwig van Beethoven | 维也纳古典乐派 | 乐圣 | `KernScores/beethoven`, `Sonatinas/Beethoven` | [进入 `Beethoven`](./Beethoven/README.md) |
| **`Mozart`** | 沃尔夫冈·阿玛多伊斯·莫扎特 | Wolfgang Amadeus Mozart | 维也纳古典乐派 (Classical) | 音乐神童 | `KernScores/mozart`, `Sonatinas/Mozart` | [进入 `Mozart`](./Mozart/README.md) |
| **`Haydn`** | 约瑟夫·海顿 | Franz Joseph Haydn | 维也纳古典乐派 (Classical) | 交响乐之父 / 弦乐四重奏之父 | `KernScores/haydn` | [进入 `Haydn`](./Haydn/README.md) |
| **`Czerny`** | 卡尔·车尔尼 | Carl Czerny | 浪漫主义时期 | 现代钢琴教学之父 | `Czerny/Op_599`, `Czerny/Op_849` | [进入 `Czerny`](./Czerny/README.md) |
| **`Burgmuller`** | 约瑟夫·弗里德里希·布格缪勒 | Johann Friedrich Franz Burgmüller | 浪漫主义时期 (Romantic) | 钢琴叙事性进阶练习曲大师 | `Burgmuller/Op_100`, `Burgmuller/Op_105` | [进入 `Burgmuller`](./Burgmuller/README.md) |
| **`Beyer`** | 斐迪南·拜厄 | Ferdinand Beyer | 浪漫主义时期 (Romantic) | 钢琴启蒙教育奠基人 | `Beyer/Op_101` | [进入 `Beyer`](./Beyer/README.md) |
| **`Hanon`** | 夏尔-路易·哈农 | Charles-Louis Hanon | 浪漫主义时期 (Romantic) | 钢琴手指机能训练宗师 | `Hanon` | [进入 `Hanon`](./Hanon/README.md) |
| **`Schumann`** | 罗伯特·舒曼 | Robert Schumann | 浪漫主义全盛期 (Romantic) | 浪漫主义音乐诗人 / 音乐评论宗师 | `Schumann_Album_for_the_Young`, `OpenScore/Schumann` | [进入 `Schumann`](./Schumann/README.md) |
| **`Tchaikovsky`** | 彼得·伊里奇·柴可夫斯基 | Pyotr Ilyich Tchaikovsky | 浪漫主义时期 (Romantic) | 俄罗斯旋律之王 / 芭蕾音乐巨擘 | `Tchaikovsky_Childrens_Album` | [进入 `Tchaikovsky`](./Tchaikovsky/README.md) |
| **`Grieg`** | 爱德华·格里格 | Edvard Hagerup Grieg | 民族乐派 | 北欧肖邦 / 挪威民族音乐之魂 | `Grieg_Lyric_Pieces` | [进入 `Grieg`](./Grieg/README.md) |
| **`Clementi`** | 穆齐奥·克莱门蒂 | Muzio Clementi | 古典主义时期 (Classical) | 现代钢琴演奏之父 / 小奏鸣曲宗师 | `Sonatinas/Clementi_Op36` | [进入 `Clementi`](./Clementi/README.md) |
| **`Schubert`** | 弗朗茨·舒伯特 | Franz Peter Schubert | 早期浪漫主义 (Romantic) | 歌曲之王 / 浪漫主义抒情天才 | `KernScores/schubert`, `OpenScore/Schubert` | [进入 `Schubert`](./Schubert/README.md) |
| **`Brahms`** | 约翰内斯·勃拉姆斯 | Johannes Brahms | 浪漫主义全盛期 (Romantic) | 古典传统的坚守者 / 三B巨匠之一 | `KernScores/brahms`, `OpenScore/Brahms` | [进入 `Brahms`](./Brahms/README.md) |
| **`Joplin`** | 斯科特·乔普林 | Scott Joplin | 拉格泰姆 | 拉格泰姆之王 | `KernScores/joplin` | [进入 `Joplin`](./Joplin/README.md) |
| **`Kuhlau`** | 弗里德里希·库劳 | Friedrich Daniel Rudolf Kuhlau | 古典主义向早期浪漫主义过渡 | 小奏鸣曲名家 / 长笛贝多芬 | `Sonatinas/Kuhlau` | [进入 `Kuhlau`](./Kuhlau/README.md) |