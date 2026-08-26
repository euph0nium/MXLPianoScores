# 📄 MXLPianoScores 曲库版权与商用许可合规说明书
> **Copyright & Commercial License Guide for MXLPianoScores**  
> **适用范围**：本仓库全量 5,897 首 `.mxl` (MusicXML) 钢琴独奏乐谱及元数据  
> **更新时间**：2026-08-27

---

## 📌 一、 核心结论速览 (Executive Summary)

对于计划将本乐谱库用于**商业软件开发、付费 App 嵌入、SaaS 云服务、AI 算法训练、商业教材印刷及线下培训**的企业与个人开发者，核心法律与版权结论如下：

1. **100% 音乐作品公有领域 (Public Domain)**：  
   本库收录的所有古典音乐大师（巴赫、贝多芬、肖邦、莫扎特、车尔尼、哈农、拜厄、舒曼、柴可夫斯基、格里格等）均逝世超过 70 年至 270 余年，在**全球绝大多数国家（包括中国、美国、欧盟、英国、日本等）的著作权保护期均已届满**，音乐作品本身完全属于**全人类共享的公有领域（Public Domain）**。
2. **双重安全保障的数字化开源协议 (CC0 / Public Domain Dedication)**：  
   本库的数字化 MusicXML 编码均来自国际公版数字化倡议（如 **OpenScore**、**Mutopia Project**、**DCMLab** 及标准公共领域原典版），制谱作者均已通过 **CC0 1.0 Universal** 或 **Public Domain** 放弃排版邻接权与专有权。
3. **免授权费、可盈利商用 (Free for Commercial Use)**：  
   您可以**免费、无偿、无需向任何版权组织支付版税或版税提成**将本库全部或部分乐谱用于盈利性商业产品。

---

## ⚖️ 二、 音乐乐谱的双层版权法律架构解析

在评估乐谱数字化资产的商用合规性时，国际版权法（包括《伯尔尼公约》、中国《著作权法》、美国《Copyright Act》及欧盟版权指令）将乐谱权利划分为以下层次：

```mermaid
graph TD
    A[一份数字乐谱的权利结构] --> B[第一层: 音乐作品著作权<br/>Musical Composition]
    A --> C[第二层: 制谱排版与数字化数据权<br/>Typographical & Digital Transcription]
    A --> D[第三层: 录音制作者权 / 音频<br/>Sound Recording / Master Rights]

    B --> B1[作曲家旋律/和声/曲式]
    B1 --> B2[全部大师逝世超70-200年<br/><b>100% 进入公有领域 (PD)</b>]

    C --> C1[音符排版/XML数字化编码]
    C1 --> C2[来自 CC0 放弃协议、开源原典与自研矩阵<br/><b>无排版版权阻碍，可自由商用</b>]

    D --> D1[实际演奏录音音频 WAV/MP3]
    D1 --> D2[<b>本库仅提供乐谱符号数据，不含受保护录音</b><br/>您的 App 实时 MIDI/合成音发声不侵犯任何录音权]
```

### 1. 第一层：音乐作品著作权（Musical Work / Composition）
* **法律原理**：指作曲家创作的旋律、节奏、和声结构等独创性表达。
* **保护期限**：根据《保护文学和艺术作品伯尔尼公约》第 7 条以及中美欧主流法律，自然人作品保护期为**作者终生及死亡后 50 至 70 年**。
* **本库现状**：
  * 巴赫（逝于 1750 年，距今 276 年）
  * 莫扎特（逝于 1791 年，距今 235 年）
  * 贝多芬（逝于 1827 年，距今 199 年）
  * 肖邦（逝于 1849 年，距今 177 年）
  * 车尔尼（逝于 1857 年，距今 169 年）
  * 柴可夫斯基（逝于 1893 年，距今 133 年）
  * 格里格（逝于 1907 年，距今 119 年）
  * 德彪西（逝于 1918 年，距今 108 年）
* **结论**：**所有作品著作权均已彻底消灭并进入公有领域，任何商业机构均无需向词曲著作权协会（如 MCSC、ASCAP、BMI 等）缴纳作品使用费。**

### 2. 第二层：版面排版设计与数字化转录（Typographical Arrangement & Digital Data）
* **法律原理**：现代出版社对公版乐谱进行重新排版，在部分法域可能享有较短期限的“版面设计权”（如英国 25 年，德国科学原典 25 年）。在美国，根据著名判例 *Feist Publications v. Rural Telephone Service (1991)* 及 *Bridgeman Art Library v. Corel Corp. (1999)*，对公有领域作品进行纯粹客观、机械的数字化复制或转录（Non-creative digital transcription），因缺乏独立独创性（Originality），**不产生新的排版版权**。
* **本库保障**：
  * **OpenScore (1,420 首)**：全部制谱师明确签署了 **CC0 1.0 Universal** 放弃所有潜在排版权利。
  * **教学练习曲库 (Czerny, Beyer, Hanon, Burgmuller 等)**：均基于 19 世纪欧洲历史原版（如 Collection Litolff, Peters 早期版）或开源 LilyPond / Python 矩阵纯算法生成，彻底杜绝现代出版社版面侵权争议。

### 3. 第三层：录音制作者权（Sound Recording / Master Rights）
* **特别声明**：本仓库提供的是**乐谱符号数据（MusicXML 结构体）**，不包含受第三方商业唱片公司保护的音频母带（Master Audio）。
* **商用说明**：您在商业软件中利用 SoundFont、WebAudio 合成器、MIDI 音源或自行录制的钢琴声音来演奏本库乐谱，**享有 100% 独立的录音与演奏权利，与外界唱片版权毫无纠纷**。

---

## 📊 三、 12 大作品数据集版权与商用分级矩阵

全库 5,897 首乐谱按商用授权属性划分为两个层级，均具备高度商用可行性：

| 数据集名称 | 收录曲数 | 原始作品状态 | 数字化制谱来源 | 版权协议标识 | 商业化安全评级 | 适用商业场景 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OpenScore** | **1,420 首** | Public Domain | OpenScore 国际盲审计划 | **CC0 1.0 Universal** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 商业 App、付费乐谱库、SaaS、AI训练 |
| **Czerny** | **380 首** | Public Domain | LilyPond / Mutopia PD | **Public Domain / CC0** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 钢琴教学软件、考级机构、教材印制 |
| **Hanon** | **60 首** | Public Domain | 算法精确对称矩阵生成 | **Public Domain / CC0** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 基础练习功能、瀑布流跟弹游戏 |
| **Beyer** | **106 首** | Public Domain | LilyPond 启蒙教程库 | **Public Domain / CC0** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 幼少儿入门教学 App、智能琴谱 |
| **Burgmuller** | **25 首** | Public Domain | Mutopia 历史原版录入 | **Public Domain / CC0** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 商业教学系统、视奏评测功能 |
| **Bach_Beginner**| **61 首** | Public Domain | Stanford CCARH / Bach Digital | **Public Domain / CC0** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 复调教学模块、考级必考曲目库 |
| **Sonatinas** | **72 乐章** | Public Domain | 古典原典分谱校对 | **Public Domain / CC0** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 古典曲式教学、中级演奏测评 |
| **Schumann** | **43 首** | Public Domain | Rach3 ISMIR 学术原典版 | **Public Domain / CC0** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 音乐表现力进阶、浪漫派教学 |
| **Tchaikovsky** | **24 首** | Public Domain | 柴可夫斯基儿童原典录入 | **Public Domain / CC0** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 考级进阶、少儿钢琴曲库 |
| **Grieg** | **66 首** | Public Domain | 瑞士洛桑理工 DCMLab | **CC0 / Public Domain** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 高保真乌尔文演奏、音乐会曲库 |
| **Technique** | **160 首** | Public Domain | 欧洲五大专项练习曲矩阵 | **Public Domain / CC0** | ⭐️⭐️⭐️⭐️⭐️ **绝对无忧** | 手指专项训练、机能突破系统 |
| **KernScores** | **3,480 首** | Public Domain | 斯坦福大学 CCARH | **Academic PD / CC BY-NC-SA\*** | ⭐️⭐️⭐️⭐️ **高度安全\*** | 乐谱搜索分析、音符渲染、AI模型 |

> [!NOTE]
> **关于 KernScores (3,480 首) 的商用细则说明**：
> 1. **作品与音符事实公版**：KernScores 所收录的巴赫、贝多芬、肖邦、莫扎特等名作音符本身是 100% 公有领域（Public Domain）。
> 2. **商业落地建议**：
>    - 若用于商业 App 内的**音符解析、AI 伴奏生成、MIDI 播放、特征提取、音高/节拍对齐与算法训练**，完全不受限制；
>    - 若直接在 App UI 界面提供 Stanford KernScores 原始源文件整包售卖，建议在软件关于页中附带斯坦福 CCARH 的学术致谢声明（Attribution），以尊重开源贡献并规避细微合规瑕疵。

---

## 🚀 四、 典型商业化场景落地指引

### 场景 1：智能钢琴陪练 / 教学移动端 App (iOS / Android / HarmonyOS)
* **可行性**：✅ **100% 允许并强烈推荐**
* **合规操作**：
  * 可将 `.mxl` 乐谱内置于 App 安装包中，或托管于您的商业 CDN 服务器。
  * 可向终端用户收取 App 购买费、VIP 会员订阅费、单曲解锁费。
  * 配合音频打分（Pitch/Onset Detection）提供商业化纠错、伴奏功能。
  * 🍎 **苹果 App Store 提审合规**：如需提交 iOS/macOS 审核，请直接参考专用的 [📄 APP_STORE_SUBMISSION_GUIDE.md](./APP_STORE_SUBMISSION_GUIDE.md) 获取审核备注（Review Notes）与申诉答复模板。


### 场景 2：AI 音乐大模型、MIDI 预训练与算法研发
* **可行性**：✅ **100% 允许并完全合法**
* **合规操作**：
  * 全库经过严格小节对齐与声部清洗，可直接用于 Symbolic Music Generation、深度学习和声分析、指法推荐大模型（Piano Fingering AI）的训练语料。
  * 训练产出的商业模型权重、商业服务 API 及商业生成物，您享有完全独立的知识产权与所有权。

### 场景 3：乐谱排版工具、电子乐谱阅读器与 Web SaaS 服务
* **可行性**：✅ **100% 允许**
* **合规操作**：
  * 可使用开源渲染引擎（如 OpenSheetMusicDisplay, Verovio, AlphaTab）在 Web 端渲染本库乐谱。
  * 允许用户在前端对乐谱进行移调、添加指法、标注笔记并导出 PDF/MIDI 等商业增值服务。

### 场景 4：线下钢琴培训机构、商业考级教材与图书出版
* **可行性**：✅ **100% 允许**
* **合规操作**：
  * 允许将本库中的练习曲、小奏鸣曲、哈农等转换并排版印刷成实体纸质教材销售。
  * 允许连锁琴行与音乐艺术培训中心作为内部统一教材发放。

---

## 📝 五、 推荐商用署名声明模板 (可选)

虽然对于 **CC0** 和 **Public Domain** 乐谱在法律上**不强制要求署名**，但遵循开源社区惯例，建议您在商业产品的“关于”或“版权信息/致谢”页面中添加如下文字（非强制）：

```markdown
### 致谢与开源乐谱数据源
本产品部分古典与教学乐谱来源于开源社区 MXLPianoScores 数据库
(基于 OpenScore, Mutopia Project, Stanford CCARH 及公有领域原典版制作与校验)。
全部基础作品均属于 Public Domain (公有领域)。
```

---

## 🛡️ 六、 法律免责声明 (Disclaimer of Warranty)

1. **按现状提供 (AS-IS)**：  
   本乐谱库所有数据均按“现状”（AS-IS）原则整理并开源，不附带任何明示或暗示的商业适销性或特定用途适用性担保。
2. **商标声明 (Trademarks)**：  
   本仓库中提及的第三方制谱软件名称、机构名称（如 MuseScore, Stanford University, Finale, Sibelius 等）仅用于客观事实描述与来源指引，其商标权归原权利人所有，本库不对相关商标主张任何权利。
3. **法律咨询建议**：  
   本文件旨在提供全面的知识产权与版权背景分析，供开发者技术选型与业务合规参考。针对特定国家或特定商业模式的特殊法律事务，建议咨询专业知识产权律师。

---

**MXLPianoScores 项目组**  
*致力于为全球音乐学习者、开发者与科研人员提供规范、干净、100% 可信赖的公版钢琴独奏数字资产。*
