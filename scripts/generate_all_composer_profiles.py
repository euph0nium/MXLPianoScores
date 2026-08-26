#!/usr/bin/env python3
"""
Generate comprehensive composer directories, README.md biographies, and info.json
structured metadata for all major composers represented in the piano score library.
All folders and identifiers are in English.
"""

import os
import json

BASE_DIR = "/Users/shiyuli/Dev/Scores/Composers"

COMPOSERS_DATA = [
    {
        "id": "chopin",
        "name": "弗雷德里克·肖邦",
        "original_name": "Frédéric François Chopin",
        "short_name": "肖邦",
        "folder_name": "Chopin",
        "birth_year": 1810,
        "death_year": 1849,
        "nationality": "波兰 / 法国",
        "period": "浪漫主义时期 (Romantic)",
        "title": "钢琴诗人 (The Poet of the Piano)",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/KernScores/chopin"],
        "bio_short": "19世纪浪漫主义时期最伟大的作曲家和钢琴演奏家之一，被誉为‘钢琴诗人’。其毕生创作专注于钢琴独奏，将旋律的诗意、细腻的织体与自由速度（Rubato）发挥到了极致。",
        "bio_full": "弗雷德里克·肖邦出生于波兰华沙附近的热拉佐瓦-沃拉。二十岁时前往巴黎并在欧洲音乐界赢得极高声誉。肖邦将波兰传统的民间音乐语汇（如玛祖卡、波兰舞曲）与典雅的法式沙龙文化相融合，创作出兼具深沉爱国情怀与诗意色彩的永恒杰作。他的音乐旋律优美动人、和声丰富，是浪漫主义钢琴音乐的最高典范。",
        "masterpieces": [
            {"title": "降E大调夜曲 Op.9 No.2", "genre": "Nocturne", "opus": "Op.9 No.2", "key": "E-flat major"},
            {"title": "升c小调夜曲 遗作", "genre": "Nocturne", "opus": "B.49", "key": "C-sharp minor"},
            {"title": "c小调练习曲「革命」", "genre": "Étude", "opus": "Op.10 No.12", "key": "C minor"},
            {"title": "E大调练习曲「离别」", "genre": "Étude", "opus": "Op.10 No.3", "key": "E major"},
            {"title": "降D大调「一分钟/小狗圆舞曲」", "genre": "Waltz", "opus": "Op.64 No.1", "key": "D-flat major"},
            {"title": "升c小调圆舞曲", "genre": "Waltz", "opus": "Op.64 No.2", "key": "C-sharp minor"},
            {"title": "降A大调「英雄波兰舞曲」", "genre": "Polonaise", "opus": "Op.53", "key": "A-flat major"},
            {"title": "24首前奏曲「雨滴」", "genre": "Prelude", "opus": "Op.28 No.15", "key": "D-flat major"},
            {"title": "g小调第一叙事曲", "genre": "Ballade", "opus": "Op.23", "key": "G minor"}
        ]
    },
    {
        "id": "bach",
        "name": "约翰·塞巴斯蒂安·巴赫",
        "original_name": "Johann Sebastian Bach",
        "short_name": "巴赫",
        "folder_name": "Bach",
        "birth_year": 1685,
        "death_year": 1750,
        "nationality": "德国",
        "period": "巴洛克时期 (Baroque)",
        "title": "西方现代音乐之父 (The Father of Western Music)",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/Bach_Beginner", "scores/KernScores/bach"],
        "bio_short": "巴洛克音乐集大成者，整部西方古典音乐史中最伟大的奠基人，被尊称为‘西方音乐之父’。其《平均律键盘曲集》被誉为键盘乐器的‘旧约圣经’。",
        "bio_full": "约翰·塞巴斯蒂安·巴赫精通管风琴、羽管键琴与小提琴，将复调对位法、赋格与和声体系推向不可逾越的艺术巅峰。其音乐兼具深邃的宗教神圣感与严密的数学逻辑结构，为近现代键盘音乐打下了坚实基石。",
        "masterpieces": [
            {"title": "C大调前奏曲 (平均律第一卷 BWV 846)", "genre": "Prelude", "opus": "BWV 846", "key": "C major"},
            {"title": "G大调小步舞曲 (安娜笔记本)", "genre": "Minuet", "opus": "BWV Anh. 114", "key": "G major"},
            {"title": "g小调小步舞曲 (安娜笔记本)", "genre": "Minuet", "opus": "BWV Anh. 115", "key": "G minor"},
            {"title": "C大调二部创意曲 No.1", "genre": "Invention", "opus": "BWV 772", "key": "C major"},
            {"title": "F大调二部创意曲 No.8", "genre": "Invention", "opus": "BWV 779", "key": "F major"},
            {"title": "哥德堡变奏曲「萨拉班德主题」", "genre": "Variation", "opus": "BWV 988", "key": "G major"},
            {"title": "d小调托卡塔与赋格", "genre": "Toccata & Fugue", "opus": "BWV 565", "key": "D minor"},
            {"title": "G弦上的咏叹调", "genre": "Air", "opus": "BWV 1068", "key": "D major"}
        ]
    },
    {
        "id": "beethoven",
        "name": "路德维希·凡·贝多芬",
        "original_name": "Ludwig van Beethoven",
        "short_name": "贝多芬",
        "folder_name": "Beethoven",
        "birth_year": 1770,
        "death_year": 1827,
        "nationality": "德国",
        "period": "维也纳古典乐派 / 早期浪漫主义",
        "title": "乐圣 (The Titan of Classical Music)",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/KernScores/beethoven", "scores/Sonatinas/Beethoven"],
        "bio_short": "维也纳古典乐派代表人物、西方音乐史上最伟大的作曲家之一，被后世尊称为‘乐圣’。其32首钢琴奏鸣曲被公认为钢琴音乐的‘新约圣经’。",
        "bio_full": "贝多芬出生于德国波恩，少年时期定居维也纳并师从海顿。青年时期以精湛绝伦的钢琴即兴演奏震撼维也纳乐坛，随后在中年时期遭遇严重的进行性耳聋打击。面对命运的重压，他以‘扼住命运的咽喉’的坚强意志创作出数量惊人的传世杰作。他的音乐突破了古典主义严谨的框框，开创了浪漫主义以个人情感、英雄主义与崇高意志为核心的音乐新纪元。其32首钢琴奏鸣曲集思想深度、结构交响化与演奏技巧于一体，与巴赫《平均律键盘曲集》并称为钢琴艺术史上不可逾越的双峰。",
        "masterpieces": [
            {"title": "升c小调第十四钢琴奏鸣曲「月光」", "genre": "Piano Sonata", "opus": "Op.27 No.2", "key": "C-sharp minor"},
            {"title": "c小调第八钢琴奏鸣曲「悲怆」", "genre": "Piano Sonata", "opus": "Op.13", "key": "C minor"},
            {"title": "f小调第二十三钢琴奏鸣曲「热情」", "genre": "Piano Sonata", "opus": "Op.57", "key": "F minor"},
            {"title": "C大调第二十一钢琴奏鸣曲「华尔斯坦/黎明」", "genre": "Piano Sonata", "opus": "Op.53", "key": "C major"},
            {"title": "降E大调第二十六钢琴奏鸣曲「告别」", "genre": "Piano Sonata", "opus": "Op.81a", "key": "E-flat major"},
            {"title": "致爱丽丝 (Für Elise)", "genre": "Bagatelle", "opus": "WoO 59", "key": "A minor"},
            {"title": "G大调小奏鸣曲", "genre": "Sonatina", "opus": "Anh.5 No.1", "key": "G major"},
            {"title": "F大调小奏鸣曲", "genre": "Sonatina", "opus": "Anh.5 No.2", "key": "F major"}
        ]
    },
    {
        "id": "mozart",
        "name": "沃尔夫冈·阿玛多伊斯·莫扎特",
        "original_name": "Wolfgang Amadeus Mozart",
        "short_name": "莫扎特",
        "folder_name": "Mozart",
        "birth_year": 1756,
        "death_year": 1791,
        "nationality": "奥地利",
        "period": "维也纳古典乐派 (Classical)",
        "title": "音乐神童 (The Musical Genius)",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/KernScores/mozart", "scores/Sonatinas/Mozart"],
        "bio_short": "欧洲古典主义音乐巅峰代表，人类历史上无与伦比的音乐天才。其音乐纯净典雅、旋律宛若天籁，在钢琴奏鸣曲、协奏曲与歌剧领域均达至臻之境。",
        "bio_full": "莫扎特出生于奥地利萨尔茨堡，4岁开始作曲，自幼随父亲巡演全欧，展现出震古烁今的音乐早慧。在短暂而辉煌的35年生命中，莫扎特留下了600多部涵盖所有体裁的旷世杰作。莫扎特的钢琴作品结构严谨对称、织体明澈透亮，看似清丽流畅、无拘无束，实则蕴含极高的歌唱性与细腻复杂的情感张力。他的音乐被后世誉为‘降临人间的纯净阳光’。",
        "masterpieces": [
            {"title": "A大调第十一钢琴奏鸣曲 (含「土耳其进行曲」)", "genre": "Piano Sonata", "opus": "K.331", "key": "A major"},
            {"title": "C大调第十六钢琴奏鸣曲 (易懂的奏鸣曲)", "genre": "Piano Sonata", "opus": "K.545", "key": "C major"},
            {"title": "F大调第十二钢琴奏鸣曲", "genre": "Piano Sonata", "opus": "K.332", "key": "F major"},
            {"title": "d小调幻想曲", "genre": "Fantasia", "opus": "K.397", "key": "D minor"},
            {"title": "c小调幻想曲", "genre": "Fantasia", "opus": "K.475", "key": "C minor"},
            {"title": "c小调第十四钢琴奏鸣曲", "genre": "Piano Sonata", "opus": "K.457", "key": "C minor"},
            {"title": "小星星变奏曲", "genre": "Variations", "opus": "K.265", "key": "C major"},
            {"title": "C大调小奏鸣曲", "genre": "Sonatina", "opus": "K.545", "key": "C major"}
        ]
    },
    {
        "id": "haydn",
        "name": "约瑟夫·海顿",
        "original_name": "Franz Joseph Haydn",
        "short_name": "海顿",
        "folder_name": "Haydn",
        "birth_year": 1732,
        "death_year": 1809,
        "nationality": "奥地利",
        "period": "维也纳古典乐派 (Classical)",
        "title": "交响乐之父 / 弦乐四重奏之父",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/KernScores/haydn"],
        "bio_short": "维也纳古典乐派奠基人，被尊称为‘交响乐之父’与‘海顿爸爸’。确立了古典主义奏鸣曲式结构，其键盘奏鸣曲洋溢着风趣、幽默与均衡之美。",
        "bio_full": "海顿在埃斯特哈齐家族担任乐长近三十年，在长期的乐团实践中探索并奠定了交响曲、弦乐四重奏以及古典钢琴奏鸣曲的标准曲式框架。海顿不仅启发并指导了年轻的莫扎特与贝多芬，更以其乐观豁达、生动风趣的音乐性格为世人所爱。他的60余首键盘奏鸣曲构思精巧、充满民间音乐的质朴欢快与机智巧思，是古典键盘艺术不可或缺的基石。",
        "masterpieces": [
            {"title": "D大调键盘奏鸣曲", "genre": "Keyboard Sonata", "opus": "Hob. XVI:37", "key": "D major"},
            {"title": "e小调键盘奏鸣曲", "genre": "Keyboard Sonata", "opus": "Hob. XVI:34", "key": "E minor"},
            {"title": "C大调键盘奏鸣曲", "genre": "Keyboard Sonata", "opus": "Hob. XVI:35", "key": "C major"},
            {"title": "降E大调第五十二键盘奏鸣曲", "genre": "Keyboard Sonata", "opus": "Hob. XVI:52", "key": "E-flat major"},
            {"title": "f小调行板与变奏曲", "genre": "Variations", "opus": "Hob. XVII:6", "key": "F minor"},
            {"title": "吉普赛回旋曲", "genre": "Rondo", "opus": "Hob. XV:25", "key": "G major"}
        ]
    },
    {
        "id": "czerny",
        "name": "卡尔·车尔尼",
        "original_name": "Carl Czerny",
        "short_name": "车尔尼",
        "folder_name": "Czerny",
        "birth_year": 1791,
        "death_year": 1857,
        "nationality": "奥地利",
        "period": "浪漫主义时期 / 维也纳古典传统",
        "title": "现代钢琴教学之父",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/Czerny/Op_599", "scores/Czerny/Op_849", "scores/Czerny/Op_299", "scores/Czerny/Op_740"],
        "bio_short": "贝多芬的得意门生、李斯特的恩师，钢琴练习曲发展史上的里程碑式宗师。其编写的系统性练习曲是全世界钢琴学子通往专业演奏的必由之路。",
        "bio_full": "车尔尼自幼随贝多芬学习钢琴，继承了维也纳古典乐派严谨规范的演奏法，随后培养出包括李斯特（Franz Liszt）、莱谢蒂茨基（Leschetizky）等一大批钢琴巨匠。车尔尼一生创作了超过千部作品，其中以循序渐进、体系完备的钢琴技巧练习曲最为举世瞩目。从《599 初级练习曲》、《849 流畅练习曲》到《299 快速练习曲》与《740 高级技巧练习曲》，构成了全球钢琴教育史上最具权威性、不可替代的技术教学大纲。",
        "masterpieces": [
            {"title": "钢琴初步教程 Op.599 (全100首)", "genre": "Études", "opus": "Op.599", "key": "Various"},
            {"title": "钢琴流畅练习曲 Op.849 (全30首)", "genre": "Études", "opus": "Op.849", "key": "Various"},
            {"title": "钢琴快速练习曲 Op.299 (全40首)", "genre": "Études", "opus": "Op.299", "key": "Various"},
            {"title": "钢琴手指灵活性练习曲 Op.740 (全50首)", "genre": "Études", "opus": "Op.740", "key": "Various"},
            {"title": "左手练习曲 Op.718", "genre": "Études", "opus": "Op.718", "key": "Various"},
            {"title": "小小钢琴家 Op.823", "genre": "Études", "opus": "Op.823", "key": "Various"}
        ]
    },
    {
        "id": "burgmuller",
        "name": "约瑟夫·弗里德里希·布格缪勒",
        "original_name": "Johann Friedrich Franz Burgmüller",
        "short_name": "布格缪勒",
        "folder_name": "Burgmuller",
        "birth_year": 1806,
        "death_year": 1874,
        "nationality": "德国 / 法国",
        "period": "浪漫主义时期 (Romantic)",
        "title": "钢琴叙事性进阶练习曲大师",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/Burgmuller/Op_100", "scores/Burgmuller/Op_105", "scores/Burgmuller/Op_109"],
        "bio_short": "浪漫主义时期著名的作曲家与钢琴教育家。其《25首简易与进阶练习曲 Op.100》将纯正的技术训练与生动诗意的标题音乐完美融为一体。",
        "bio_full": "布格缪勒出生于德国雷根斯堡的音乐名门，后定居巴黎成为炙手可热的沙龙钢琴家与作曲家。布格缪勒最深远的影响力在于他创造性地将枯燥的手指机能练习转化为充满诗情画意、极具感染力的音乐小品。其《进阶练习曲 25 首 Op.100》（如《贵妇人的骑马》、《牧歌》、《阿拉伯风格曲》、《清澈的小溪》）旋律优美生动、形象鲜明，被公认为全球钢琴入门过渡到中级阶段最受喜爱的教学经典。",
        "masterpieces": [
            {"title": "顺叙 / 坦率 (La Candeur)", "genre": "Étude", "opus": "Op.100 No.1", "key": "C major"},
            {"title": "阿拉伯风格曲 (Arabesque)", "genre": "Étude", "opus": "Op.100 No.2", "key": "A minor"},
            {"title": "牧歌 (Pastoral)", "genre": "Étude", "opus": "Op.100 No.3", "key": "G major"},
            {"title": "清澈的溪水 (Le Courant Limpide)", "genre": "Étude", "opus": "Op.100 No.7", "key": "G major"},
            {"title": "再会 (L'Adieu)", "genre": "Étude", "opus": "Op.100 No.12", "key": "A minor"},
            {"title": "安慰 (Consolation)", "genre": "Étude", "opus": "Op.100 No.13", "key": "C major"},
            {"title": "贵妇人的骑马 / 骑士 (La Chevaleresque)", "genre": "Étude", "opus": "Op.100 No.25", "key": "C major"},
            {"title": "18首风格练习曲 Op.109", "genre": "Études", "opus": "Op.109", "key": "Various"}
        ]
    },
    {
        "id": "beyer",
        "name": "斐迪南·拜厄",
        "original_name": "Ferdinand Beyer",
        "short_name": "拜厄",
        "folder_name": "Beyer",
        "birth_year": 1803,
        "death_year": 1863,
        "nationality": "德国",
        "period": "浪漫主义时期 (Romantic)",
        "title": "钢琴启蒙教育奠基人",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/Beyer/Op_101"],
        "bio_short": "德国钢琴家与著名音乐教育家。其《钢琴初级教程 Op.101》（通称‘拜厄’）是全球普及度最高、影响了几代琴童的经典钢琴启蒙教材。",
        "bio_full": "拜厄活跃于19世纪中叶的德国莱茵地区，致力于普及钢琴基础教育。他编订的《钢琴初级教程 Op.101》以极其平缓温和的坡度，系统讲解了五线谱识读、双手独立协调、简单调性转换、音阶与琶音练习，并穿插了大量优美易懂的四手联弹曲目。历经一个半世纪的教学检验，拜厄教程依然是全球非专业与少儿钢琴启蒙最具知名度的入门大纲之一。",
        "masterpieces": [
            {"title": "钢琴初级教程 Op.101 (全106条教程)", "genre": "Method", "opus": "Op.101", "key": "Various"},
            {"title": "单手与双手交替练习 (Op.101 No.1-12)", "genre": "Exercise", "opus": "Op.101 No.1-12", "key": "C major"},
            {"title": "双手并进练习与音阶练习", "genre": "Exercise", "opus": "Op.101 No.65-80", "key": "Various"},
            {"title": "流畅性与装饰音练习", "genre": "Exercise", "opus": "Op.101 No.81-106", "key": "Various"}
        ]
    },
    {
        "id": "hanon",
        "name": "夏尔-路易·哈农",
        "original_name": "Charles-Louis Hanon",
        "short_name": "哈农",
        "folder_name": "Hanon",
        "birth_year": 1819,
        "death_year": 1900,
        "nationality": "法国",
        "period": "浪漫主义时期 (Romantic)",
        "title": "钢琴手指机能训练宗师",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/Hanon"],
        "bio_short": "法国管风琴家、钢琴家与教育家。其著作《钢琴练指法 60 首名手练功曲》是全世界钢琴演奏者锻炼手指独立性、爆发力与敏捷度的核心圣经。",
        "bio_full": "哈农生于法国北部滨海布洛涅，毕生专注研究钢琴弹奏的生理学机能与手指独立运动规律。其传世代表作《钢琴练指法 60 首》(The Virtuoso Pianist) 针对钢琴演奏中每根手指（尤其是薄弱的 4、5 指）的力量均衡、手腕柔韧性、大指穿指、八度、震音及全调音阶琶音设计了高度精炼的模块化练习。无论是初学者打基础，还是职业钢琴大师日常开指热身，哈农练指法均是必不可少的‘手指体操’。",
        "masterpieces": [
            {"title": "钢琴名手练指法 第1-20条 (手指灵活、独立与力量)", "genre": "Technique", "opus": "Hanon No.1-20", "key": "C major"},
            {"title": "钢琴名手练指法 第21-43条 (大拇指穿指、全调音阶与琶音)", "genre": "Technique", "opus": "Hanon No.21-43", "key": "All Keys"},
            {"title": "钢琴名手练指法 第44-60条 (同音反复、八度、三度与震音特技)", "genre": "Technique", "opus": "Hanon No.44-60", "key": "Various"}
        ]
    },
    {
        "id": "schumann",
        "name": "罗伯特·舒曼",
        "original_name": "Robert Schumann",
        "short_name": "舒曼",
        "folder_name": "Schumann",
        "birth_year": 1810,
        "death_year": 1856,
        "nationality": "德国",
        "period": "浪漫主义全盛期 (Romantic)",
        "title": "浪漫主义音乐诗人 / 音乐评论宗师",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/Schumann_Album_for_the_Young", "scores/OpenScore/Schumann"],
        "bio_short": "德奥浪漫主义音乐巅峰代表，兼具深邃文学修养与梦幻音乐构思的天才。其《童年情景》与《少年钢琴曲集》以纯真诗意与细腻织体闻名遐迩。",
        "bio_full": "舒曼出生于德国茨维考的书商家庭，自幼兼具卓越的文学才华与音乐天赋。他创办《新音乐杂志》并极具前瞻性地发掘了肖邦与勃拉姆斯。舒曼的钢琴音乐充满双重性格（激昂热烈的弗洛雷斯坦与沉思内省的约瑟比乌斯），善于捕捉瞬息万变的情感微澜。其《少年钢琴曲集 Op.68》专为儿童与青少年的音乐想象力而作，而《童年情景 Op.15》（包含名作《梦幻曲》）更是以成人的温情目光回望童年时光的至臻杰作。",
        "masterpieces": [
            {"title": "梦幻曲 (Traumerei, 选自《童年情景》)", "genre": "Character Piece", "opus": "Op.15 No.7", "key": "F major"},
            {"title": "勇敢的骑士 (选自《少年曲集》)", "genre": "Character Piece", "opus": "Op.68 No.8", "key": "D minor"},
            {"title": "快乐的农夫 (选自《少年曲集》)", "genre": "Character Piece", "opus": "Op.68 No.10", "key": "F major"},
            {"title": "狂欢节 (Carnaval)", "genre": "Suite", "opus": "Op.9", "key": "Various"},
            {"title": "克莱斯勒偶记 (Kreisleriana)", "genre": "Suite", "opus": "Op.16", "key": "Various"},
            {"title": "蝴蝶 (Papillons)", "genre": "Suite", "opus": "Op.2", "key": "Various"}
        ]
    },
    {
        "id": "tchaikovsky",
        "name": "彼得·伊里奇·柴可夫斯基",
        "original_name": "Pyotr Ilyich Tchaikovsky",
        "short_name": "柴可夫斯基",
        "folder_name": "Tchaikovsky",
        "birth_year": 1840,
        "death_year": 1893,
        "nationality": "俄罗斯",
        "period": "浪漫主义时期 (Romantic)",
        "title": "俄罗斯旋律之王 / 芭蕾音乐巨擘",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/Tchaikovsky_Childrens_Album"],
        "bio_short": "俄罗斯浪漫主义音乐最伟大的代表，世所公认的‘旋律之王’。其音乐情感真挚浓郁、旋律极具歌唱性，其《儿童钢琴曲集》是世界少儿钢琴文献明珠。",
        "bio_full": "柴可夫斯基毕业于圣彼得堡音乐学院，将俄罗斯民族民间音乐的深沉忧郁、辽阔奔放与西欧古典管弦乐交响构思完美融为一体。柴可夫斯基拥有无与伦比的抒情旋律天赋。其创作的《儿童钢琴曲集 Op.39》（全24首）生动再现了俄罗斯儿童的日常生活、童话故事与异国风情（如《晨祷》、《玩具兵进行曲》、《甜美的梦》、《俄罗斯舞曲》等），曲调通俗优美、形象生动，深受全世界钢琴演奏者喜爱。",
        "masterpieces": [
            {"title": "四月·松雪草 (选自《四季》)", "genre": "Character Piece", "opus": "Op.37bis No.4", "key": "B-flat major"},
            {"title": "六月·船歌 (选自《四季》)", "genre": "Character Piece", "opus": "Op.37bis No.6", "key": "G minor"},
            {"title": "十一月·在三驾马车上 (选自《四季》)", "genre": "Character Piece", "opus": "Op.37bis No.11", "key": "E major"},
            {"title": "晨祷 (选自《儿童钢琴曲集》)", "genre": "Character Piece", "opus": "Op.39 No.1", "key": "G major"},
            {"title": "玩具兵进行曲 (选自《儿童曲集》)", "genre": "March", "opus": "Op.39 No.5", "key": "D major"},
            {"title": "甜美的梦 (选自《儿童曲集》)", "genre": "Character Piece", "opus": "Op.39 No.21", "key": "C major"},
            {"title": "俄罗斯舞曲 (选自《儿童曲集》)", "genre": "Dance", "opus": "Op.39 No.24", "key": "B-flat major"}
        ]
    },
    {
        "id": "grieg",
        "name": "爱德华·格里格",
        "original_name": "Edvard Hagerup Grieg",
        "short_name": "格里格",
        "folder_name": "Grieg",
        "birth_year": 1843,
        "death_year": 1907,
        "nationality": "挪威",
        "period": "民族乐派 / 浪漫主义时期",
        "title": "北欧肖邦 / 挪威民族音乐之魂",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/Grieg_Lyric_Pieces"],
        "bio_short": "挪威民族乐派奠基人，以清丽脱俗、散发着北欧峡湾与森林气息的旋律闻名，其10卷《抒情小品集》(Lyric Pieces) 是浪漫主义钢琴小品之瑰宝。",
        "bio_full": "格里格毕业于莱比锡音乐学院，随后致力于发掘挪威民间传说、民歌调式与峡湾壮丽自然风光中的艺术灵感。他的音乐清新纯净、和声大胆新颖，对后来的印象主义音乐产生了先导性启示。格里格一生共创作了 10 卷共 66 首《抒情小品集》(Lyric Pieces)，包括著名的《致春天》、《蝴蝶》、《特罗尔德豪根的婚礼日》、《挪威舞曲》等，将北欧大自然的纯净风情化作极度洗练优美的钢琴音诗。",
        "masterpieces": [
            {"title": "致春天 (To Spring, 选自抒情小品集)", "genre": "Lyric Piece", "opus": "Op.43 No.6", "key": "F-sharp major"},
            {"title": "蝴蝶 (Butterfly, 选自抒情小品集)", "genre": "Lyric Piece", "opus": "Op.43 No.1", "key": "A major"},
            {"title": "特罗尔德豪根的婚礼日", "genre": "Lyric Piece", "opus": "Op.65 No.6", "key": "D major"},
            {"title": "阿丽埃塔 (Arietta, 抒情小品开篇)", "genre": "Lyric Piece", "opus": "Op.12 No.1", "key": "E-flat major"},
            {"title": "小精灵 / 侏儒进行曲", "genre": "Lyric Piece", "opus": "Op.54 No.3", "key": "D minor"},
            {"title": "a小调钢琴协奏曲 第一乐章", "genre": "Concerto", "opus": "Op.16", "key": "A minor"}
        ]
    },
    {
        "id": "clementi",
        "name": "穆齐奥·克莱门蒂",
        "original_name": "Muzio Clementi",
        "short_name": "克莱门蒂",
        "folder_name": "Clementi",
        "birth_year": 1752,
        "death_year": 1832,
        "nationality": "意大利 / 英国",
        "period": "古典主义时期 (Classical)",
        "title": "现代钢琴演奏之父 / 小奏鸣曲宗师",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/Sonatinas/Clementi_Op36"],
        "bio_short": "古典主义时期作曲家、钢琴演奏大师与钢琴制造商，被誉为‘现代钢琴演奏之父’。其《小奏鸣曲集 Op.36》是全球钢琴教学黄金必弹经典。",
        "bio_full": "克莱门蒂出生于罗马，长期活跃于伦敦。他是最早完全针对现代击弦钢琴（而非羽管键琴）的机械性能与发音特质进行系统创作和演奏的先驱。曾与青年莫扎特在维也纳宫廷进行举世瞩目的钢琴演奏对决。他的《6首小奏鸣曲 Op.36》结构紧凑明快、乐句清晰匀称、指法规范严谨，是所有学习古典奏鸣曲结构与双手平衡控制最重要的必修阶梯。",
        "masterpieces": [
            {"title": "C大调小奏鸣曲 第一乐章快板", "genre": "Sonatina", "opus": "Op.36 No.1", "key": "C major"},
            {"title": "G大调小奏鸣曲", "genre": "Sonatina", "opus": "Op.36 No.2", "key": "G major"},
            {"title": "C大调小奏鸣曲", "genre": "Sonatina", "opus": "Op.36 No.3", "key": "C major"},
            {"title": "F大调小奏鸣曲", "genre": "Sonatina", "opus": "Op.36 No.4", "key": "F major"},
            {"title": "G大调小奏鸣曲", "genre": "Sonatina", "opus": "Op.36 No.5", "key": "G major"},
            {"title": "D大调小奏鸣曲", "genre": "Sonatina", "opus": "Op.36 No.6", "key": "D major"},
            {"title": "名手之道 (Gradus ad Parnassum, 练习曲100首)", "genre": "Études", "opus": "Op.44", "key": "Various"}
        ]
    },
    {
        "id": "schubert",
        "name": "弗朗茨·舒伯特",
        "original_name": "Franz Peter Schubert",
        "short_name": "舒伯特",
        "folder_name": "Schubert",
        "birth_year": 1797,
        "death_year": 1828,
        "nationality": "奥地利",
        "period": "早期浪漫主义 (Romantic)",
        "title": "歌曲之王 / 浪漫主义抒情天才",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/KernScores/schubert", "scores/OpenScore/Schubert"],
        "bio_short": "奥地利早期浪漫主义杰出代表，被公认为‘歌曲之王’。其钢琴即兴曲、音乐瞬间与奏鸣曲洋溢着天籁般的歌唱性旋律与多愁善感的和声色彩。",
        "bio_full": "舒伯特生于维也纳，在极其贫困与病痛的短暂31年岁月中，创作了600多首不朽的艺术歌曲及大量室内乐与钢琴曲。舒伯特将德奥艺术歌曲中深邃动人的歌唱性完美移植到了钢琴独奏领域。他的《即兴曲集》(Op.90, Op.142) 与《音乐瞬间》(Moments Musicaux, Op.94) 旋律纯净悠扬、转调如梦如幻，深深启发了后来的肖邦、李斯特与勃拉姆斯。",
        "masterpieces": [
            {"title": "f小调音乐瞬间 (Moments Musicaux No.3)", "genre": "Musical Moment", "opus": "Op.94 No.3", "key": "F minor"},
            {"title": "降G大调即兴曲", "genre": "Impromptu", "opus": "Op.90 No.3", "key": "G-flat major"},
            {"title": "降E大调即兴曲", "genre": "Impromptu", "opus": "Op.90 No.2", "key": "E-flat major"},
            {"title": "c小调即兴曲", "genre": "Impromptu", "opus": "Op.90 No.1", "key": "C minor"},
            {"title": "降B大调第二十一钢琴奏鸣曲", "genre": "Piano Sonata", "opus": "D.960", "key": "B-flat major"},
            {"title": "军队进行曲", "genre": "March", "opus": "D.733 No.1", "key": "D major"}
        ]
    },
    {
        "id": "brahms",
        "name": "约翰内斯·勃拉姆斯",
        "original_name": "Johannes Brahms",
        "short_name": "勃拉姆斯",
        "folder_name": "Brahms",
        "birth_year": 1833,
        "death_year": 1897,
        "nationality": "德国",
        "period": "浪漫主义全盛期 (Romantic)",
        "title": "古典传统的坚守者 / 三B巨匠之一",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/KernScores/brahms", "scores/OpenScore/Brahms"],
        "bio_short": "德国浪漫主义音乐大师，与巴赫、贝多芬并称为德国音乐史上的‘3B’巨匠。其晚期钢琴间奏曲与狂想曲沉郁内省、结构严密、情感深厚。",
        "bio_full": "勃拉姆斯出生于汉堡，青年时期受到舒曼夫妇的大力推介。在19世纪激进的新德意志乐派狂潮中，勃拉姆斯坚持严格继承巴赫的对位法与贝多芬的古典奏鸣曲严密架构，创造出宏大雄浑与深沉内敛并存的崇高艺术风格。他的晚期钢琴小品集（Op.116至119间奏曲、狂想曲、叙事曲）被誉为‘写给钢琴的暮年沉思诗篇’。",
        "masterpieces": [
            {"title": "b小调狂想曲", "genre": "Rhapsody", "opus": "Op.79 No.1", "key": "B minor"},
            {"title": "g小调狂想曲", "genre": "Rhapsody", "opus": "Op.79 No.2", "key": "G minor"},
            {"title": "A大调间奏曲", "genre": "Intermezzo", "opus": "Op.118 No.2", "key": "A major"},
            {"title": "降E大调圆舞曲", "genre": "Waltz", "opus": "Op.39 No.15", "key": "A-flat major"},
            {"title": "匈牙利舞曲第五号 (钢琴版)", "genre": "Dance", "opus": "WoO 1 No.5", "key": "F-sharp minor"},
            {"title": "帕格尼尼主题变奏曲", "genre": "Variations", "opus": "Op.35", "key": "A minor"}
        ]
    },
    {
        "id": "joplin",
        "name": "斯科特·乔普林",
        "original_name": "Scott Joplin",
        "short_name": "乔普林",
        "folder_name": "Joplin",
        "birth_year": 1868,
        "death_year": 1917,
        "nationality": "美国",
        "period": "拉格泰姆 / 早期爵士时代",
        "title": "拉格泰姆之王 (The King of Ragtime)",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/KernScores/joplin"],
        "bio_short": "美国非裔作曲家、钢琴家，被公认为‘拉格泰姆之王’。他将复杂的切分节奏与古典钢琴和声完美结合，开创了近现代流行与爵士音乐的先河。",
        "bio_full": "乔普林出生于美国德克萨斯州，在非裔民间切分音乐传统与欧洲古典钢琴技术的交汇中开创了风靡全球的‘拉格泰姆’（Ragtime）风格。乔普林的钢琴作品旋律欢快跳跃、节奏富于弹性与律动感，同时蕴含细腻典雅的古典结构美。代表作《枫叶拉格》与《演艺人》（电影《骗中骗》主题曲）是全世界家喻户晓的经典名作。",
        "masterpieces": [
            {"title": "枫叶拉格 (Maple Leaf Rag)", "genre": "Ragtime", "opus": "1899", "key": "A-flat major"},
            {"title": "演艺人 (The Entertainer)", "genre": "Ragtime", "opus": "1902", "key": "C major"},
            {"title": "精英切分曲 (Elite Syncopations)", "genre": "Ragtime", "opus": "1902", "key": "F major"},
            {"title": "惬意狂欢 (The Easy Winners)", "genre": "Ragtime", "opus": "1901", "key": "A-flat major"},
            {"title": "抹布小品 (Ragtime Dance)", "genre": "Ragtime", "opus": "1906", "key": "B-flat major"}
        ]
    },
    {
        "id": "kuhlau",
        "name": "弗里德里希·库劳",
        "original_name": "Friedrich Daniel Rudolf Kuhlau",
        "short_name": "库劳",
        "folder_name": "Kuhlau",
        "birth_year": 1786,
        "death_year": 1832,
        "nationality": "德国 / 丹麦",
        "period": "古典主义向早期浪漫主义过渡",
        "title": "小奏鸣曲名家 / 长笛贝多芬",
        "avatar": "avatar.jpg",
        "illustration": "illustration.jpg",
        "library_collections": ["scores/Sonatinas/Kuhlau"],
        "bio_short": "德裔丹麦古典浪漫主义作曲家。其《小奏鸣曲集》(Op.20, Op.55) 清新明朗、织体工整，是全球钢琴教育界与克莱门蒂齐名的小奏鸣曲大师。",
        "bio_full": "库劳早年在汉堡学习音乐，后定居哥本哈根并成为丹麦宫廷作曲家。他曾与贝多芬私交甚笃并深受其启发。库劳的小奏鸣曲（如 Op.20、Op.55、Op.59）旋律活泼纯净、技术难度适中、曲式严谨清晰，充满歌唱性的欢快主题，是钢琴学子从初级进阶到中高级古典奏鸣曲不可或缺的基石文献。",
        "masterpieces": [
            {"title": "C大调小奏鸣曲 第一乐章快板", "genre": "Sonatina", "opus": "Op.20 No.1", "key": "C major"},
            {"title": "G大调小奏鸣曲", "genre": "Sonatina", "opus": "Op.20 No.2", "key": "G major"},
            {"title": "F大调小奏鸣曲", "genre": "Sonatina", "opus": "Op.20 No.3", "key": "F major"},
            {"title": "C大调小奏鸣曲", "genre": "Sonatina", "opus": "Op.55 No.1", "key": "C major"},
            {"title": "G大调小奏鸣曲", "genre": "Sonatina", "opus": "Op.55 No.2", "key": "G major"},
            {"title": "C大调小奏鸣曲", "genre": "Sonatina", "opus": "Op.55 No.3", "key": "C major"}
        ]
    }
]

def generate_markdown(comp):
    lines = []
    lines.append(f"# {comp['name']} ({comp['original_name']})\n")
    lines.append(f"![{comp['short_name']}头像](./avatar.jpg)\n")
    lines.append("## 📌 基本信息\n")
    lines.append("| 字段 | 信息 |")
    lines.append("| :--- | :--- |")
    lines.append(f"| **中文名** | {comp['name']} |")
    lines.append(f"| **外文名** | {comp['original_name']} |")
    lines.append(f"| **目录名称** | `{comp['folder_name']}` |")
    lines.append(f"| **生卒年月** | {comp['birth_year']}年 － {comp['death_year']}年 |")
    lines.append(f"| **国籍** | {comp['nationality']} |")
    lines.append(f"| **时期流派** | {comp['period']} |")
    lines.append(f"| **称号** | “{comp['title']}” |")
    lines.append("\n---\n")
    lines.append("## 📖 作家介绍与艺术生平\n")
    lines.append(f"{comp['bio_full']}\n")
    lines.append("\n---\n")
    lines.append("## 🎹 代表体裁与经典作品\n")
    for i, piece in enumerate(comp['masterpieces'], 1):
        opus_str = f" ({piece['opus']})" if piece.get('opus') else ""
        lines.append(f"{i}. **{piece['title']}**{opus_str} — *{piece['genre']}*")
    lines.append("\n---\n")
    lines.append("## 🎼 本地乐谱库对应专集目录\n")
    for col in comp['library_collections']:
        lines.append(f"- `/{col}`")
    lines.append("\n---\n")
    lines.append("## 🎨 视觉资产规范\n")
    lines.append(f"- **标准矩形头像 (`avatar.jpg`)**: 1:1 纯矩形 JPG 格式，淡雅水彩工笔插画，水彩背景完整延展填满矩形。")
    lines.append(f"- **全景情境插画 (`illustration.jpg`)**: 1:1 音乐家艺术演奏/创作情境图。")
    return "\n".join(lines)

def generate_root_readme():
    lines = []
    lines.append("# 🎵 Composers Database (古典音乐家数据库)\n")
    lines.append("本目录为当前乐谱库（5,897+ 首 MusicXML 乐谱）收录的所有核心古典音乐作曲家提供完整的**艺术生平介绍**、**代表作目录**、**对应本地乐谱路径**以及**标准化视觉资产（1:1 满版淡雅水彩工笔插画 JPG）**。\n")
    lines.append("---\n")
    lines.append("## 🎨 视觉设计与技术规范\n")
    lines.append("- **风格定位**：淡雅水彩工笔插画风（Subtle Pastel Watercolor & Fine Line Art）")
    lines.append("- **格式规范**：**标准 JPG 格式（画质 95%）**，1:1 纯矩形满版画幅（无圆形边框限制，水彩背景无缝填满整个矩形）。")
    lines.append("- **命名规则**：根目录与作家子目录均采用**英文标准名称（PascalCase）**，便于代码库工程化维护与 API 路由对接。")
    lines.append("- **资产文件**：")
    lines.append("  - `avatar.jpg`: 1:1 满版矩形胸像头像（适合列表、作者主页，支持 App 自由裁剪）")
    lines.append("  - `illustration.jpg`: 1:1 钢琴/乐器全景艺术情境插画（适合专栏封面、介绍背景）")
    lines.append("  - `info.json`: 供 App / Web 客户端直接解析调用的结构化数据")
    lines.append("  - `README.md`: Markdown 格式的中英文生平与权威导聆\n")
    lines.append("---\n")
    lines.append("## 📂 目录结构 (Directory Structure)\n")
    lines.append("```text\nComposers/\n├── README.md                      # 全局作曲家总索引\n├── Chopin/                        # Frédéric Chopin\n│   ├── avatar.jpg                 # 满版淡雅水彩头像 (1:1 JPG)\n│   ├── illustration.jpg           # 全景演奏艺术插画 (1:1 JPG)\n│   ├── README.md                  # 生平与代表作导聆\n│   └── info.json                  # App 结构化 JSON 元数据\n├── Bach/                          # Johann Sebastian Bach\n│   ├── avatar.jpg\n│   ├── README.md\n│   └── info.json\n├── Beethoven/                     # Ludwig van Beethoven\n├── Mozart/                        # Wolfgang Amadeus Mozart\n└── ...                            # 更多作曲家目录\n```\n")
    lines.append("---\n")
    lines.append("## 🎼 全库作曲家名录索引 (Composers Catalog)\n")
    lines.append("| 目录 (Folder) | 中文名 | 外文全名 (Full Name) | 艺术流派 | 代表性称号 | 本地乐谱库专集 | 目录链接 |")
    lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")

    for comp in COMPOSERS_DATA:
        folder = comp["folder_name"]
        zh_name = comp["name"]
        en_name = comp["original_name"]
        period = comp["period"].split("/")[0].strip()
        title = comp["title"].split("(")[0].strip().replace("“", "").replace("”", "")
        cols = ", ".join([f"`{c}`" for c in comp["library_collections"][:2]])
        lines.append(f"| **`{folder}`** | {zh_name} | {en_name} | {period} | {title} | {cols} | [进入 `{folder}`](./{folder}/README.md) |")

    return "\n".join(lines)

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    generated_count = 0

    for comp in COMPOSERS_DATA:
        folder_path = os.path.join(BASE_DIR, comp['folder_name'])
        os.makedirs(folder_path, exist_ok=True)

        # Write info.json
        info_json_path = os.path.join(folder_path, "info.json")
        info_data = {
            "id": comp["id"],
            "name": comp["name"],
            "original_name": comp["original_name"],
            "short_name": comp["short_name"],
            "folder_name": comp["folder_name"],
            "birth_year": comp["birth_year"],
            "death_year": comp["death_year"],
            "nationality": comp["nationality"],
            "period": comp["period"],
            "title": comp["title"],
            "avatar": comp["avatar"],
            "illustration": comp["illustration"],
            "library_collections": comp["library_collections"],
            "bio_short": comp["bio_short"],
            "bio_full": comp["bio_full"],
            "masterpieces": comp["masterpieces"]
        }
        with open(info_json_path, "w", encoding="utf-8") as f:
            json.dump(info_data, f, ensure_ascii=False, indent=2)

        # Write README.md
        readme_path = os.path.join(folder_path, "README.md")
        readme_content = generate_markdown(comp)
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)

        generated_count += 1
        print(f"✅ Synced: Composers/{comp['folder_name']} (info.json + README.md)")

    # Write root README.md
    root_readme_path = os.path.join(BASE_DIR, "README.md")
    with open(root_readme_path, "w", encoding="utf-8") as f:
        f.write(generate_root_readme())
    print(f"✅ Synced: Composers/README.md")

    print(f"\n🎉 Successfully synced all {generated_count} composer profiles in English directory structure!")

if __name__ == '__main__':
    main()
