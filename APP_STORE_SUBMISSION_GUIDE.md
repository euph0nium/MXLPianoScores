# 🍎 苹果 App Store 乐谱应用上架与审核合规实战指南
> **App Store Submission & Copyright Compliance Guide for MXLPianoScores**  
> **适用场景**：将本曲库 `.mxl` 乐谱内置或集成到 iOS / iPadOS / macOS / visionOS 应用并提交 App Store 审核  
> **更新时间**：2026-08-27

---

## 📌 一、 核心要点概述

将公版古典乐谱与练习曲内置到 Apple 平台应用时，开发者最常面临的审核要点集中在 **App Store 审核指南 Guideline 5.2 (知识产权)** 与 **Guideline 4.2 (最低功能性)**。

只要做好以下两项准备，即可确保 100% 顺利过审：
1. **App 提交时主动填写审核备注 (App Review Notes)**：向审核员清晰声明曲目属于公有领域 (Public Domain) 与 CC0 开源数据，消除审核员对“是否具备分发资质”的疑虑。
2. **应用内提供规范的关于/致谢 (In-App Attribution)**：在设置或关于页面中保留简短的数据源说明。

---

## 📋 二、 App Store Connect 提审备注模板 (复制即用)

在 **App Store Connect** 提交新版本时，在 **「App 审核信息 -> 备注 (App Review Information -> Notes)」** 栏中直接粘贴以下内容：

### 📝 英文版（推荐，苹果全球审核团队通用）
```text
[Content Copyright & Licensing Declaration]
All sheet music assets bundled/available in this application are Classical Piano Solo works that reside 100% in the Public Domain worldwide (e.g., compositions by J.S. Bach, L.v. Beethoven, F. Chopin, C. Czerny, C.L. Hanon, F. Beyer, etc., all composers deceased 70–270+ years ago).

The digital MusicXML/MXL sheet music transcriptions are sourced from reputable open-source public domain initiatives, including the OpenScore Project (released under CC0 1.0 Universal / Public Domain Dedication: https://creativecommons.org/publicdomain/zero/1.0/), Mutopia Project, and standard historical Urtext editions. No copyrighted recordings or proprietary modern editorial publications are used.

Audio playback inside the app is synthesized in real-time using built-in software audio engines (MIDI/SoundFont) and contains no copyrighted third-party sound recordings.

The application fully complies with App Store Review Guideline 5.2 (Intellectual Property).
```

### 📝 中文版（适用于面向大中华区审核团队）
```text
【曲库版权与内容授权说明】
本应用内收录的所有乐谱内容均为古典钢琴与教学作品（包括巴赫、贝多芬、肖邦、车尔尼、哈农、拜厄等大师作品），所有原作者逝世均已超过 70~200 余年，音乐作品本身 100% 属于全球公有领域（Public Domain）。

本应用所采用的数字化 MusicXML 乐谱数据来源于国际开源公版数字化项目（如 OpenScore CC0 1.0 Universal、Mutopia Project 及历史乌尔文原典版），制谱数据完全开源且免版税，不包含任何第三方受保护的音频母带或现代出版社专有排版，应用内音频均为软件合成音源实时发声，完全符合 App Store 审核指南 5.2 知识产权条款。
```

---

## 📱 三、 应用内（In-App）文案展示规范

建议在 App 的 **「设置」->「关于我们」或「开源致谢与版权 (About & Open Source Licenses)」** 页面中加入如下说明：

### 中文文案示例：
```text
关于乐谱版权与数据源：
本软件收录的古典与教学钢琴乐谱均属于公有领域 (Public Domain)。
数字化乐谱数据基于 OpenScore (CC0 1.0 Universal)、Mutopia Project 
及历史原典版进行规范化编排与校验，支持自由学习、研究与演奏。
```

### 英文文案示例：
```text
Sheet Music Licensing:
All classical piano scores provided in this app are in the Public Domain.
Digital sheet music transcriptions are curated from OpenScore (CC0 1.0 Universal),
Mutopia Project, and historic Urtext editions for educational and performance use.
```

---

## ⚠️ 四、 苹果审核关键避坑与合规红线

| 审核条款 | 潜在风险点 | 开发者正确做法 / 避坑指南 |
| :--- | :--- | :--- |
| **Guideline 5.2.1**<br/>(知识产权与商标) | 使用了现代商业出版社的注册商标或专有专有名词，如标称“*Henle 原版*”、“*Alfred 独家编订版*”、“*人音考级版*”。 | **严禁使用任何现代商业出版社品牌名称**。统一标注为：“*乌尔文原典版 (Urtext)*”、“*标准公版*”、“*OpenScore 开源版*”或直接以作品编号（如 *Op. 599 No. 1*, *BWV 846*）命名。 |
| **Guideline 5.2.2**<br/>(音频/录音版权) | 误在 App 中内嵌了商业唱片公司发行的母带音频（如索尼、环球、DG 唱片出版的钢琴家录音 MP3/WAV）。 | **仅使用实时合成音频**。通过 iOS `AVFoundation`、`AudioKit`、`SoundFont / DLS` 或 `WebAudio` 实时解析 MusicXML 演奏，发声权利 100% 归开发者所有。 |
| **Guideline 4.2**<br/>(最低功能性) | 仅提供静态图片或纯 PDF 翻页浏览，被审核员判定为“电子书/功能简陋的搬运应用”。 | 确保 App 具备**交互式核心功能**，例如：五线谱动态排版渲染、节拍器调速、AB 段循环练琴、单手/双手分轨静音、麦克风跟弹音高识别打分、指法标注等。 |
| **Guideline 2.3.1**<br/>(隐藏功能与内购) | 若包含付费乐谱或 VIP 会员，未通过 Apple In-App Purchase (IAP) 结算。 | 所有针对内置乐谱的解锁、去广告、VIP 订阅均必须接入 **StoreKit (IAP)**，不可包含外部支付链接。 |

---

## 🛡️ 五、 应对审核质疑 / 被拒的申诉回复模板

若在极低概率下，审核员发出问询（如询问版权资质或补充授权文件证明），请直接在 **Resolution Center（解决方案中心）** 中提交以下英文申诉：

```text
Dear Apple App Review Team,

Thank you for your valuable feedback. In response to your inquiry regarding the sheet music content bundled in our application:

1. Worldwide Public Domain Status:
   All compositions included in our app are historical classical works created by composers (such as J.S. Bach, Ludwig van Beethoven, Frédéric Chopin, Carl Czerny, and C.L. Hanon) who passed away over 70 to 200+ years ago. Under international copyright treaties (the Berne Convention) and US Copyright Law (Title 17 of the United States Code), all these musical works reside entirely in the Public Domain.

2. Open Source CC0 Digital Transcriptions:
   The digital MusicXML sheet music files were created and transcribed from open-source public domain projects, primarily OpenScore (released under CC0 1.0 Universal - Public Domain Dedication: https://creativecommons.org/publicdomain/zero/1.0/) and the Mutopia Project. The contributors have explicitly dedicated these digital files to the public domain without reservation.

3. Proprietary Real-Time Audio Synthesis:
   Our application does not use or redistribute any copyrighted third-party sound recordings or commercially released master tracks. All audio playback is synthesized in real-time by our application's built-in MIDI synthesizer / SoundFont engine.

4. Proprietary Interactive Features:
   Our app provides comprehensive interactive features (including dynamic MusicXML score rendering, tempo customization, loop practice, and pitch detection) that go far beyond static document viewing, fully complying with Guidelines 4.2 and 5.2.

Please let us know if you require any further documentation or information. Thank you for your review and assistance!

Best regards,
The Development Team
```

---

## 🔗 相关参考文档

* [📄 COPYRIGHT_AND_COMMERCIAL_LICENSE.md (全库版权与免费商用许可说明)](./COPYRIGHT_AND_COMMERCIAL_LICENSE.md)
* [🎹 Piano_Solo_MusicXML_Guide.md (开发者集成与渲染指南)](./Piano_Solo_MusicXML_Guide.md)
* [📊 global_scores_index.json (5,897 首乐谱机器索引元数据)](./global_scores_index.json)
