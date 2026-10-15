# 米开朗基罗·梅里西·达·卡拉瓦乔（Michelangelo Merisi da Caravaggio, 1571–1610）档案

> 标注清扫 2026-10-15（依据 _crosscheck.md）
> 模板：`templates/artist_module.md`｜写手：ArtistCaravaggio（wave2，GOALS A-15）｜日期：2026-10-15
> 证据分级：`[自述]`（本人写下/说出，带出处）· `[史料]`（当时记录/档案/法庭证词/馆藏信息）· `[研究]`（艺术史家/博物馆分析）· `[归纳]`（本项目从作品与资料归纳的操作规则，不冒充艺术家内心）· `[推测]`（低置信）
> 正文中文；引用保留原文；prompt 用英文。
> **本档案的特殊性（写在前面的口径）**：卡拉瓦乔几乎没有文字留世——无书信集、无论述、无笔记；现代传记作者 Graham-Dixon 的判断是「关于绘画，我们只有他的一句话」，且出自 1603 年诽谤罪的审讯记录 `[研究]`[R11]。因此本档案第 5 节以**法庭证词转录**与**同代传记（Baglione 1642 / Bellori 1672，两人都对他有敌意：前者是诉讼对手，后者属古典主义阵营且从未见过他）**为主，全部标 `[史料]` 并注明性质；不把同代转述包装成「他本人说的」。

---

## 0. 元信息

- **生卒 / 国别**：1571-09-29 生于米兰；1610-07-18 卒于 Porto Ercole（托斯卡纳 Grosseto 附近）。意大利。`[史料]`（[R1]；另见 [R14] 的死亡档案）**出生地注**：旧说生于 Caravaggio 镇，现代学界共识为生于米兰（"It was previously assumed that he had been born in Caravaggio"）`[史料]`[R1]。
- **主要流派**：无自建学派；被艺术史归为**巴洛克形成期的关键革命者**与「现实主义/自然主义」潮流的开创人物（梵蒂冈博物馆用语："the protagonist of a real artistic revolution… the most important personage of the 'realist' trend of seventeenth century painting"）`[研究]`[R8]。追随者统称 **Caravaggisti**（亦称 tenebrosi，"shadowists"）`[研究]`[R1]。
- **主要媒介**：油画（布面为主；《美杜莎》为木盾凸面圆画）`[史料]`[R1][R16]。
- **一句话能力定位**：**舞台式硬光 / 「光的开关」**——给系统补上「光可以是非自然的」这一档：单一硬光源、无反射、背景压到近黑，亮部只落在**脸、手与关键道具**三类对象上；与「人物贴住画面平面 + 定格瞬间」共同构成叙事语法。（缺口归属：`expansion.md` §2.2 **G1 戏剧性光影（舞台式硬光）**，本档案即该缺口的模块化落地；§1.2 已定能力标签：`戏剧布光(舞台式)` · `高反差明暗两级` · `瞬间定格叙事` · `非理想化人体` · `暗底静物`）
- **关键作品 5 件（带馆藏与 URL）**：
  1. *The Supper at Emmaus*《以马忤斯的晚餐》1601，141 × 196.2 cm，National Gallery London（NG172）— [R5]
  2. *David with the Head of Goliath*《大卫手提歌利亚的头》1606–07 或 1609–10，125 × 101 cm，Galleria Borghese（inv. 455）— [R10]
  3. *The Deposition (Entombment)*《基督下葬》1603–04，Musei Vaticani, Pinacoteca, Sala XII — [R8]
  4. *The Beheading of Saint John the Baptist*《施洗者圣约翰被斩首》1608，370 × 520 cm，St John's Co-Cathedral, Valletta（**唯一署名作品**，画幅最大）— [R1]（馆方页本轮未直读，见 §10）
  5. *Boy with a Basket of Fruit*《捧果篮的男孩》c. 1595，70 × 67 cm，Galleria Borghese（inv. 136）— [R9]

---

## 1. 视觉指纹（10 条）

| # | 特征 | 可观察量 | 证据级 |
|---|---|---|---|
| 1 | **单光源、无反射、背景近黑**：光来自画外高处（左或右上方），画内不出现光源；环境反光被取消 | 背景（墙/地）最亮像素 ≤ 全帧最亮的 ~10%；画面内可见光源数 = 0 | `[史料]` [R4]（Met 引同代批评家："a focused light source from high up, without reflections, as though in a room with a single window and the walls painted black"）；[R16]（Bellori：灯置高处、光直落） |
| 2 | **两级明暗（tenebrism）**：亮部极亮、暗部极暗，中间调被压缩；黑暗本身成为画面主体（"darkness becomes a dominating feature"） | 亮度直方图双峰；中间带 [0.35,0.65] 像素占比显著低于常规油画 | `[研究]` [R2][R1]（"the shift from light to dark with little intermediate value"） |
| 3 | **暗部不是死黑**：暗区保留可辨的中间调结构（深色底被有意留出当中间调用） | 暗区内部仍有明度层次；纯黑（=0）像素占比低 | `[研究]` [R6]（NG 论《莎乐美》："the dark ground left deliberately exposed in several areas to provide the mid-tone in the shadows"） |
| 4 | **人物贴住画面平面**：前景人物被推到最外层，越出/贴边，空间深度被压扁 | 主人物包围盒高度 ≥ 画幅高 ~80%；至少 1 个主体被画幅边缘裁切 | `[研究]` [R4]（"pushed the figures up against the picture plane"）；量化阈值为 `[归纳]`（对照 [R5][R6] 作品） |
| 5 | **手势是叙事主语**：指、伸、插、摊——关键信息由手传递，且手被光点亮 | 高光连通域与「手」相交 ≥1；手势延长线指向叙事对象 | `[归纳]`（依据 [R5] 的 Thomas 手指、[R5]《以马忤斯》前伸的手、[R13] 的"手臂朝向"分析） |
| 6 | **反理想化的人体与面孔**：脏指甲、破衣缝、粗糙市井面孔当圣徒 | 布料有磨损/撕裂细节；指甲、脚底、衣缝可见污痕 | `[史料]` [R1]（"dirt under his fingernails"）[R5]（"bearded, lined faces and ragged clothes"） |
| 7 | **当代服装 + 当代空间**：圣徒穿 17 世纪衣服，场景像当代罗马室内/酒馆/地下室 | 服装年代 = 17 世纪；背景为素墙/室内，无风景、无天空 | `[史料]` [R1]（"figures in contemporary dress inhabiting a religious scene"）[R16]（"a dingy modern tax collector's office somewhere in a basement of Rome"，Graham-Dixon 语） |
| 8 | **定格瞬间**：画面是一个被冻结的动作极值（认出的一瞬、刀落的一瞬） | 每帧只有一个"动作极值"；无运动模糊 | `[研究]` [R1]（"the passing of a crucial moment"）；[R5]（"captures the dramatic climax… the moment of revelation"） |
| 9 | **色域收窄**：土色系（赭、红棕、铅白、黑）为主；晚期进一步收窄、更少纯色 | 同屏色相数少；晚期作品（[R6][R10]）色彩范围明显窄于罗马期（[R5]） | `[研究]` [R6]（"restricted range of colour"）[R10]（Borghese：晚期"la riduzione della gamma cromatica"） |
| 10 | **深色底（dark ground）**：画布先铺深棕底，亮部在其上"塑出"，底色参与中间调 | 暗部可见底色透出；亮部从深底上叠加 | `[研究]` [R6]；配套技法见 §2 |

---

## 2. 技法规则（10 条）

1. **直接画法：不做纸上素描，直接在画布上工作**。NG 明说这是他"最有争议的技法之一"——"painting directly onto the canvas, rather than following the traditional method of working out a composition through numerous preparatory studies. Indeed, not a single drawing that can be firmly attributed to Caravaggio survives." `[研究]` [R5]
2. **但"直接画"≠"无准备"**：技术检查发现他会在画布上先用深棕色颜料以笔画轮廓（**abbozzo**）；《以马忤斯》桌上酒杯底部的最终轮廓上方就有这种笔绘痕迹 `[研究]` [R5]。Borghese 藏品页记载：2012 年的分析在《捧果篮的男孩》上发现了**直接画在画布上的底层草图**，恰好印证古代文献所说的"dal naturale"（从自然写生）的画法 `[研究]` [R9]。
3. **incisions（刻线定位）**：他常在尚软的底子（priming/undercoat）上用笔杆尾端**徒手刻出人物位置线**——"to mark out where figures were to be placed, and presumably to allow models to resume their poses" `[研究]` [R5]；《大卫》的诊断分析同样发现了 incisioni `[研究]` [R10]；Wikipedia 综述同此说（"scoring basic guides directly onto the canvas with the end of the brush handle"）`[研究]` [R1]。
4. **深色底 + 留底作中间调**：深色 ground 被有意暴露在若干区域充当暗部中间调（见 §1-3）`[研究]` [R6]。
5. **真人摆姿势、从真人写生**：Met："His practice of painting directly from posed models violated the idealizing premise of Renaissance theory" `[研究]` [R4]；模特可考者包括 Mario Minniti、Francesco Boneri，女性模特多为当时登记在册的妓女（Fillide Melandroni、Anna Bianchini、Maddalena Antognetti/Lena）`[史料]` [R1]。
6. **快速工作**：以极快的速度完成（"worked at great speed, from live models"）`[史料]` [R1]；1604 年印行的记述说他"干两周活、晃荡一两个月"（见 §5-5）。
7. **光＝画外单灯**：同代批评家与 Bellori 的记载一致（§5-3、§5-7）：高置单光源、无反射、暗室黑墙 `[史料]` [R4][R16]。
8. **笔触：亮部"概括性"厚笔 + 晚期放宽**：《以马忤斯》中"两条快速、高度厚涂（impastoed）的斜笔"被当作人物定位的概括手段 `[研究]` [R5]；晚期"broad application in place of finely modelled gradations" `[研究]` [R6]。
9. **少 pentimenti、高预谋**：NG 指出《以马忤斯》几乎没有重大改动，唯一的显著改动是把使徒的左膝移到地毯后，以增强手臂前伸的推力——说明构图经过高度准备 `[研究]` [R5]。
10. **覆盖重画**：有时放弃不满意的构图，直接在上面画新画 `[史料]` [R7]（NG 艺术家页："Sometimes he abandoned a disappointing composition and painted new work over the top."）。

---

## 3. 创作原则（8 条）

1. **从自然/真人写生优先于程式**：古代文献（Mancini 1617–21、Baglione、Bellori）一致记载其画法为"dal naturale"，Borghese 的 2012 年分析以画布上的底层草图佐证此说。`[史料]` [R9]（另见 [R1]）
2. **光的取舍先于色彩**：同代与后世的第一手描述都把机制落在光上——高置单灯、直落、只揭示"身体的主要部分"；颜色服务于光的分区。`[史料]` [R16]；据此归纳的操作序列（先定光位→再定亮部三对象→最后压暗背景）标 `[归纳]`。
3. **反理想化是立场，不是疏忽**：把圣徒画成普通劳动者（破衣、皱纹、脏指甲），宗教场景按"正在眼前发生"来处理——Met 称之为"a provocative insistence on the physical reality of the scene portrayed"。`[研究]` [R4][R5]
4. **叙事只取一瞬**：画面永远是决定性瞬间的动作极值，不画过程。`[研究]` [R1][R5]
5. **为对抗委托方的口味承担代价**：《圣母与蛇》（Madonna dei Palafrenieri）上墙两天即被撤下 `[史料]` [R1]；《圣母之死》被加尔默罗会拒收（Mancini 记因以名妓为圣母模特，Baglione 记因"露腿"失礼，Gash 认为可能还有神学原因）`[史料]/[研究]` [R1]。Graham-Dixon 的判断："他拒绝改变做法"。`[研究]` [R11]
6. **物理真实压倒象征程式**：圣像的象征符号（光环等）被压缩到最低，代之以可触摸的物证（伤口、面包、水杯折射）。`[研究]` [R5][R13]
7. **不做工作室、不立学派**：与 Carracci 相反，他没有建立工坊来传播技法，也没有留下理论（"Nor did he ever set out his underlying philosophical approach to art"）——这既是他死后声誉脆弱的原因，也是后世只能"从他的画里反推规则"的原因。`[研究]` [R1]
8. **把模特当材料，反复使用同一批脸**：Minniti、Boneri、Fillide 等反复出现在不同角色里（天使、圣约翰、大卫……），同一张脸可以同时是神与市井。`[史料]` [R1]

> 口径提醒（项目宪章）：以上 1–8 是**从作品与艺术史资料归纳的操作规则**，不冒充"他心里想的"；按行内标注：第 1/2/5/8 条有 `[史料]` 支撑（#2 另含 `[归纳]` 操作序列），第 3/4/6/7 条为 `[研究]`。

---

## 4. 控制参数（6 个，各带弱/中/强三档）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **光源聚焦度 / 硬度（Light Hardness）**`[归纳]` | 柔和环境光，多个光源或天光；有反射补光 | 单一方向光，允许少量反射；亮部边界略软 | 单一硬光（画外、高置 30°–60° 仰角），无反射、无补光，亮部边界硬 | **85%**（本模块强档即其身份） |
| P2 | **背景明度上限（Background Ceiling）**`[归纳]` | 背景可达全帧最亮的 40–50%（近自然室内） | ≤20% | ≤8–10%（近黑，墙/地几乎只剩轮廓暗示） | **10%** |
| P3 | **中间调压缩（Midtone Compression）**`[归纳]` | 全调域，中间调充足（学院式渐变） | 中间调 [0.35,0.65] 占比 25–40% | ≤25%，直方图双峰；暗带 [0,0.25) ≥40% | **30%**（比强档松一档，保可读性） |
| P4 | **贴平面度（Figure-to-Plane）**`[归纳]` | 人物在景深中，有明确地面/环境纵深 | 半身/大半身，背景压暗但仍有空间暗示 | 主人物高度 ≥ 画幅 80%、被边缘裁切、前景物越出画面 | **80%** |
| P5 | **色域收窄（Palette Restraint）**`[归纳]` | 色相多、含冷色与高纯色（晚期以后被弃） | 土色系为主，1–2 个饱和强调色（红/绿） | 近乎单色阶：赭/红棕/铅白/黑，饱和色仅出现在道具 | **60%**（罗马期）／晚期取 85% |
| P6 | **手势—光斑绑定（Gesture & Highlight Binding）**`[归纳]` | 光均匀落在全身；手部无特别强调 | 脸部优先受光，手部次之 | 光斑只落在**脸 / 手 / 关键道具**三类对象；高光连通域 ≤5 且都与三者相交 | **85%** |

> **分工口径（与伦勃朗，必须写死，来源 `expansion.md` §1.1/§1.2 与 §4.3 冲突规则）**：两人同属"从黑暗里打光"一族（视觉重叠 ~60%），本档案固定为——**卡拉瓦乔 = 光的开关 + 物理（硬光戏剧）**；**伦勃朗 = 光的连续衰减 + 心理（心理化光斑）**。落到参数上：P1 的强档（无反射硬光）与 P3 的强档（中间调双峰）**是本模块专属**；一旦把 P1 降到中档并允许"光在面部连续衰减"，产出就进入伦勃朗的地盘，组合实验里必须按此判分。本判据为 `[归纳]`，可被 wave3 实验推翻。
> **用法**：P1/P2 定"是不是卡拉瓦乔"；P4/P6 定叙事（贴平面 + 手势受光）；P3/P5 定时期（罗马期 vs 晚期）。三档描述可直接当判定标准写进自查表。

---

## 5. 自述与原话（8 条，逐条标性质；本档案"自述"以审讯记录与同代转述为主）

1. **1603 年诽谤案法庭证词（唯一被现代学者认定为"他关于绘画的话"的记录）**
   原文（英译）："I don't know any painter who thinks Giovanni Baglione is a good painter."；另一句：the Resurrection altarpiece was "clumsy [goffa]"，"it's the worst he's done, and I haven't heard a single painter praise the said painting."
   中译：我不认识任何一个认为乔瓦尼·巴利奥内画得好的画家。……（他的《复活》）笨拙，是他画得最差的一件，我没听到任何一个画家夸过那幅画。
   出处：[R3]（Wikipedia "Giovanni Baglione" 引 1603 年法庭文书；同一引文另见 [R15]）。
   性质：**法庭证词转录** `[史料]`——且据 [R11]（Graham-Dixon）："关于绘画，我们只有他的一句话——而这句话的真诚度本身就可疑，因为它是在他以诽谤罪（死罪）被审讯时挤出来的。" 使用注意：这是**贬损对手**的语境，不是画论。
2. **Baglione《Vite》1642（敌意传记作者；1603 年官司的原告）**
   原文（意）："fece alcuni quadretti da lui nello specchio ritratti. E il primo fu un Bacco con alcuni grappoli d'uve diverse, con gran diligenza fatte ma di maniera un poco secca"
   中译：他画了一些小画，是他照着镜子画的自己的肖像。第一幅是一个巴克斯，手里拿着几串不同的葡萄，画得极用心，但手法有点干。
   出处：[R12]（Galleria Borghese 藏品页引 Baglione 1642, p. 136）。
   性质：`[史料]`，**带贬抑的转述**（"maniera un poco secca"＝手法干涩）；也是"用镜子作画"这条记载的出处。
3. **Bellori《Le vite》1672（古典主义理论家；从未见过他本人）**
   原文（英译）："He went so far in this style that he never showed any of his figures in open daylight, but instead found a way to place them in the darkness of a closed room, placing a lamp high so that the light would fall straight down, revealing the principal part of the body and leaving the rest in shadow."
   中译：他在这条路上走得太远：从不让任何人物出现在天光下，而是设法把他们安置在暗室之中，把灯放在高处，让光直直落下，只揭示身体的主要部分，其余留在阴影里。
   出处：[R16]（The Art Story 所载英译，系 Bellori 1672 论《施洗者圣约翰被斩首》段落的转引）。**本条为二手转引，原书页码回查未做（见 §10）。**
   性质：`[史料]`（同代记录，敌意框架）。
4. **1604-04-26 侍者 Pietro Antonio de Fosaccia 的报案陈述（罗马国家档案馆文书）**
   原文（英译）："About 17 o'clock [lunchtime] the accused, together with two other people, was eating in the Moor's restaurant at La Maddalena, where I work as a waiter. I brought them eight cooked artichokes, four cooked in butter and four fried in oil. The accused asked me which were cooked in butter and which fried in oil, and I told him to smell them… He got angry and without saying anything more, grabbed an earthenware dish and hit me on the cheek…"
   中译：约 17 时（午餐时分），被告与另外两人在拉·马达莱纳的"摩尔人"餐馆吃饭，我在那里当侍者。我端上八个熟洋蓟，四个黄油煮的、四个油炸的。被告问我哪几个是黄油的、哪几个是油炸的，我让他闻一闻就能分出来……他就火了，二话不说抓起一个陶盘打在我脸颊上……
   出处：[R14]（BBC 公布的档案英译，2011-02-18）。
   性质：`[史料]`（档案文书，**不是**他本人的话；但这是与艺术家直接相关的原样证词）。
5. **1604 年印行的早期记述（时人对他的描述）**
   原文："after a fortnight's work he will swagger about for a month or two with a sword at his side and a servant following him, from one ball-court to the next, ever ready to engage in a fight or an argument, so that it is most awkward to get along with him."
   中译：干两周活，然后就佩着剑、带着仆人晃荡一两个月，从一个球场到另一个球场，随时准备吵架或打架，跟他相处极难。
   出处：[R7]（NG 艺术家页，注明"据他的一位传记作者"）；同文另见 [R1]（1604 年印行的早期记述）。
   性质：`[史料]`（当时出版物）。
6. **友人 Marzio Milesi 所撰墓志铭（1610）**
   原文："Michelangelo Merisi, son of Fermo di Caravaggio – in painting not equal to a painter, but to Nature itself – died in Port' Ercole… He lived thirty-six years nine months and twenty days."
   中译：米开朗基罗·梅里西，费尔莫·达·卡拉瓦乔之子——在绘画上不逊于任何画家，而堪比自然本身——卒于圣埃尔科港……他活了三十六年九个月零二十天。
   出处：[R1]。
   性质：`[史料]`（友人撰，带溢美；注意按此计算生卒与 1610-07-18 一致）。
7. **同代批评家对"该画派"的机制描述（Met 转引）**
   原文："a characteristic of this school [of painting] is to use a focused light source from high up, without reflections, as though in a room with a [single] window and the walls painted black. In this fashion the lit and shadowed areas are very light and very dark and give enormous three-dimensionality to the painting, but in an unnatural fashion neither done or even conceived before by such artists as Raphael, Titian, Correggio, or others."
   中译：这个（画）派的特点是用一个高处的聚焦光源、没有反射，就像在一间只有一扇窗、墙被涂成黑色的房间里。这样，受光与阴影的部分都极亮极暗，给画面巨大的立体感，但以**不自然**的方式——拉斐尔、提香、科雷焦等人既没做过、也没想到过。
   出处：[R4]（Met，Christiansen 2003 转引"一位同代批评家"；Met 未具名原文作者，回查待办）。
   性质：`[史料]`（**这是本项目 §1-1、P1、P2 参数的直接史料依据**）。
8. **Graham-Dixon 对其"文字留世"的判语（给本节定性的现代研究）**
   原文："He was one of the most original artists ever to have lived, yet we have only one solitary sentence from him on the subject of painting…"
   中译：他是史上最具原创性的艺术家之一，然而关于绘画，我们只有他孤零零的一句话……
   出处：[R11]。
   性质：`[研究]`（现代传记作者判断）。

> **本节用法**：第 1 条是"他嘴里出来的"（且敌意语境）；第 2/3/7 条是"同代/近同代说他怎么画"（2、3 带敌意）；第 4/5 条是档案与时人记述；第 6 条是友人。**没有任何一条可以当作画论引用**——这决定了本模块的 prompt 只能从"作品可见机制"反推（§8）。

---

## 6. 临摹与影响链

### 6.1 他学过谁（来源方向）

- **Simone Peterzano（1584–88 学徒）**：米兰画家，学徒合约注明他是**提香的学生**；伦巴第自然主义（更近德国式写实、远于罗马风格主义的程式）经他传入 `[史料]` [R1]；Borghese 藏品页进一步指出《病酒神》的姿势引用了 Peterzano 在 Garegnano 的《波斯女先知》草图，并引 Dürer 版画《Ecce Homo》 `[研究]` [R12]。
- **米兰的公共资源**：达·芬奇《最后的晚餐》与伦巴第地方传统；反宗教改革大主教 Carlo Borromeo 所推的"朴素而有力"的宗教图像口味（Graham-Dixon 认为这是他的一个影响来源） `[史料]/[研究]` [R1][R11]。
- **威尼斯（可能）**：据载他可能到过威尼斯、看过乔尔乔内与提香——这是 `[推测]` 级：Zuccari 后来指责他"模仿乔尔乔内" `[史料]` [R1]。
- **罗马初期**：初到罗马时佩服拉斐尔（Gombrich 语，经 [R16] 转引）；进入 Cavalier d'Arpino（Giuseppe Cesari）工坊画花卉果实 `[史料]` [R1][R9]。
- **古典与前辈的直接引用（可考）**：《下葬》的 Nicodemus 用**米开朗基罗的脸**（其佛罗伦萨《哀悼基督》的自画像）、《圣母》姿态关联米开朗基罗《圣殇》与拉斐尔《博尔盖塞下葬》 `[研究]` [R13]；《病酒神》引用 Dürer `[研究]` [R12]。
- **同代对手**：与 **Annibale Carracci** 的路线之争（在罗马与意大利，最终胜出的是 Carracci 一路） `[研究]` [R1]。

### 6.2 谁学过他（输出方向）

- **罗马第一代 Caravaggisti**：Orazio Gentileschi、Giovanni Baglione（短暂的 Caravaggesco 期）、Carlo Saraceni、Orazio Borgianni；**Bartolomeo Manfredi 被 Met 称为"关键意大利传播者"** `[史料]/[研究]` [R1][R4]；Artemisia Gentileschi 风格上靠近该运动 `[研究]` [R1]。
- **那不勒斯**：Battistello Caracciolo、Carlo Sellitto（该派随 1656 年瘟疫终结）；NG 补充晚期直接影响 Caracciolo、Mattia Preti、**Jusepe de Ribera** `[研究]` [R1][R6]。
- **荷兰（Utrecht Caravaggisti）**：Hendrick ter Brugghen、Gerrit van Honthorst、Dirck van Baburen 到罗马受其影响，回国后形成 Utrecht Caravaggism；**再下一代传到 Rembrandt 与 Vermeer——两人都没去过意大利** `[研究]` [R1][R4]。
- **法国**：Valentin de Boulogne、Nicolas Tournier、Simon Vouet，以及**Georges de La Tour**（远距离影响） `[研究]` [R1][R4]。
- **西班牙**：Ribera、Zurbarán、Juan Bautista Maino；Velázquez 可能通过复制品接触 `[研究]` [R4]。
- **佛兰德斯**：**Rubens** 1601 年在罗马即接触其作品，后来画过《下葬》的"演绎"版，并建议曼图亚公爵买下被拒收的《圣母之死》（后入路易十四收藏） `[史料]/[研究]` [R1][R13]。
- **19–20 世纪重估**：Roberto Longhi 在 1920 年代把他重新推入欧洲传统——"Ribera, Vermeer, La Tour and Rembrandt could never have existed without him. And the art of Delacroix, Courbet and Manet would have been utterly different."；Bernard Berenson："除米开朗基罗外，没有哪位意大利画家影响如此之大。"；Berne-Joffroy："现代绘画，就始于卡拉瓦乔的作品。"；1951 年米兰 Palazzo Reale《Mostra del Caravaggio》展（Borghese 藏品页的展览史亦记此次）；1986 年 Derek Jarman 电影《Caravaggio》 `[研究]` [R1][R9]。

### 6.3 一句话总结（给提示词模块的"来历"注脚）

这条链说明卡拉瓦乔的 prompt 不是"风格滤镜"，而是一套**操作序列**：**先决定光从哪里来（开关）→ 再让光只落在脸/手/关键道具 → 最后把背景压到近黑、把中间调抽掉**；上游是伦巴第写实与威尼斯色（Peterzano/达芬奇/Borromeo 的口味），下游是整条欧洲巴洛克的明暗谱系（Caravaggisti → Utrecht → Rembrandt/Vermeer → La Tour → Ribera），并在 20 世纪经 Longhi 一脉被重新追认为"现代绘画的起点"。

---

## 7. 深度分析（10 条，馆方/学者，逐条带 URL）

1. **The Met, Heilbrunn Timeline — Keith Christiansen, "Caravaggio (Michelangelo Merisi) (1571–1610) and His Followers"（2003-10）**：给出机制的最凝练表述——"把人物推向画面平面 + 用光增强戏剧冲击与即时性"，并转引同代批评家对"高处聚焦光源、无反射、黑墙"的描述；把 Manfredi 定为意大利关键传播者，列出 ter Brugghen/Honthorst/Valentin/Tournier/Maino/Ribera/Zurbarán，判定"Caravaggism 由此成为国际运动、巴洛克绘画的拱心石之一"。[R4]
2. **National Gallery London —《The Supper at Emmaus》in-depth**：技法证据链最完整的一篇：abbozzo 笔绘底线、"not a single drawing… survives"、incised freehand lines 刻在软底上以便模特复位、两条厚涂斜笔作概括指示、几乎无 pentimenti 说明高度预谋；光从左侧来，在基督身后墙上投下"近乎反向光环"的阴影。[R5]
3. **National Gallery London —《Salome receives the Head of John the Baptist》in-depth**：晚期风格的三条判据——色域收窄、宽笔触替代精细过渡、**深色底被有意留出作暗部中间调**；并给出影响链（Caracciolo、Preti、Ribera）。[R6]
4. **Musei Vaticani — Pinacoteca, Sala XII《Deposition》**：馆方把它定义为"卡拉瓦乔最伟大的杰作之一"，并给出构图重解——不是"下葬"而是把基督安放在**敷油石（Anointing Stone）**上；同时给出馆方对艺术史地位的定性："realist trend of seventeenth century painting 最重要的人物"。[R8]（房间页见 [R12b]）
5. **Galleria Borghese 藏品目录 —《David con la testa di Golia》(inv. 455)**：出处链（1613 已在 Scipione Borghese 收藏，Manilli 1650 首次指出巨人脸＝卡拉瓦乔自画像、大卫＝"他的 Caravaggino"）、剑刃铭文 "H.AS O S" 的奥古斯丁格言读法（'H[umilit]AS O[ccidit] S[uperbiam]'）、以及**诊断分析发现 incisioni** 与晚期色彩收窄的实证。[R10]
6. **Galleria Borghese 藏品目录 —《Giovane con canestra di frutta》(inv. 136)**：记录 **2012 年分析发现画布上的底层草图**，用于印证古代文献"他直接从自然写生"的说法；并梳理 1607 年 Cavalier d'Arpino 收藏被没收→Scipione Borghese 的流传链。[R9]
7. **Andrew Graham-Dixon, *Caravaggio: A Life Sacred and Profane*（Penguin, 2010）摘录**：作者自述花十年拼证据；"只有一句话"的判语；把《朱迪斯斩首荷罗孚尼》读作"亚述帐篷里的神圣处决变成了罗马妓院里的谋杀"；对 1606 决斗与 1610 死亡的叙述（热衰竭/心脏骤停的可能）。[R11]
8. **BBC News — "Caravaggio's crimes exposed in Rome's police files"（2011-02-18）**：罗马国家档案馆展览报道，给出**档案日期表**（1598 携剑、1600 打人、1604 洋蓟、1606 杀人等）与**1604 侍者报案英译全文**；并给出一个与旧传记冲突的说法：他"不是在沙滩上独自死去，而是在医院病床上"。[R14]
9. **Literary Review — Jonathan Keates 评 Helen Langdon, *Caravaggio: A Life*（Chatto & Windus, 1998）**：书评强调"现代人把卡拉瓦乔重塑成 20 世纪艺术家形象"的投射问题，主张 17 世纪的语境比传记神话更复杂；Langdon 的这部传记被 Met 列为延伸阅读。[R17]（该页付费墙，仅开头可读）
10. **The Art Story — Caravaggio 条目（转引 Bellori 1672 英译与 Gombrich 等）**：作为 §5-3 Bellori 引文的载体与作品细读的二手来源；注意其为通俗资源，引文必须回查原书（见 §10）。[R16]

---

## 8. 提示词模块

### 8.1 图像生成模块（英文 prompt + 中文说明）

**正向段（可直接粘贴）**
```
Caravaggio-style tenebrist oil painting:
one single hard directional light from high left, no fill light, no reflected light;
background walls and floor in near-black shadow (values under 10% of the lit highlights);
deep dark brown ground left visible inside the shadows as their mid-tone;
violent chiaroscuro: lit passages bright and warm, shadows crushed, midtones suppressed;
one frozen instant of a narrative action; faces and hands catch the light;
gestures point at the narrative object; figures pushed flat against the picture plane,
half-length or three-quarter figures cropped by the frame edge;
ordinary working people as saints — weathered faces, torn clothes, dirty fingernails,
contemporary 17th-century Roman clothing; plain dark interior, no landscape, no sky;
restrained earth palette — ochre, madder red, lead white, bitumen black,
one or two saturated accents on a prop; direct painting, broad final touches,
impasto highlights on the lit edges
```
**负向约束（`--no` 风格）**
```
--no soft diffuse lighting, ambient light, multiple light sources, rim light, backlight,
glow, bloom, lens flare, volumetric rays, evenly lit faces, bright background,
landscape, sky, daylight, symmetry, idealised anatomy, smooth airbrushed gradients,
pastel palette, neon colours, cartoon, 3D render, photographic realism, motion blur,
fog, haze, mirror, chandelier, candles visible in frame, halo disc, crowd
```
**中文使用说明与强度建议**
- 先跑 6 张关键帧（1920×1080 静止构图），核对三件事：① 背景最亮像素是否 ≤ 全帧最亮的 ~10%？② 高光是否只落在脸/手/道具（P6）？③ 直方图是否双峰（P3）？
- 强度旋钮：①「光的硬度」由 P1 控制（默认 85%；想试伦勃朗式心理光降到 50%，但此时已越界，见 §4 分工注）；②「背景暗度」由 P2 控制（默认 10%）；③「贴平面」由 P4 控制（默认 80%）。
- 若模型退化成"普通暗调照片"：追加 `single unseen lamp above and outside the frame, hard shadow edges, no ambient occlusion fill`；若退化成"死黑剪影"：追加 `shadow areas still readable, dark brown ground visible in the half-tones`（对应 §1-3、8.2 规则 7）。
- 与达·芬奇模块组合时：只借用其**人物结构的体感**，禁止其 sfumato 的柔边与全调域（两条规则的冲突点就是"光的硬度轴"两端）。

### 8.2 代码艺术模块（7 条可判定规则，逐帧可自查）

1. **光源单一性**：全帧可见光源数 = 0（光从画外来）；主光方向固定为左上或右上（方向向量取 (±0.7, −0.7) 一类）；环境光强度 ≤ 主光的 5%。
2. **背景明度上限**：背景区域（非人物/非道具像素）最大亮度 ≤ 0.10 × 全帧最大亮度；背景亮度标准差 ≤ 全帧 5%（禁光晕渐变）。
3. **中间调压缩（直方图双峰）**：亮度直方图中，中间带 [0.35, 0.65] 像素占比 ≤ 25%；暗带 [0, 0.25) 占比 ≥ 40%。（强档默认；中档放宽到 ≥25% / ≤40%）
4. **光斑三处法则**：高光连通域（亮度 ≥ 0.9 × max）数量 ∈ [2, 5]，且每个连通域必须与"脸 / 手 / 关键道具"之一相交；人物背部的高光连通域数 = 0。
5. **贴平面构图**：主人物包围盒高度 ≥ 画幅高 80%；至少 1 个主体被画幅边缘裁切；地平线（若出现）不得高于画幅下缘以上 15%。
6. **定格瞬间**：每帧只允许 1 个"动作极值"（最大手势位移向量的方向唯一）；运动模糊核 = 0；手势向量的延长线在 ±15° 内指向叙事对象中心。
7. **暗部保细节**：暗区（亮度 < 0.15）内部亮度标准差 ≥ 1.5/255（非死黑）；纯黑像素（=0）占比 ≤ 10%（对应 §1-3 的"底色作中间调"）。

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（见 §10）；3、5 两条与 `expansion.md` §1.2 的三条建议（光源仰角、背景明度上限 8%、贴平面）对齐。

### 8.3 野外样本（本机素材；未找到以卡拉瓦乔命名的卡）

- **来源**：`knowledge/domains/motion-graphics/origin/提示词全文.md`（15 张 10 秒 MG 卡语料，Claude Code · Opus 5.5 制作）。
- **检索结果**：以 `卡拉瓦乔|Caravaggio|伦勃朗|明暗|光|暗|影` 全目录 grep，**未命中任何以卡拉瓦乔（或明暗对照）命名的卡**；命中均为其他卡里的"光"字。
- **有价值的是"护栏冲突"**：该语料的**结构模板**把"硬阴影"列为默认退化行为，须在固定位置的「别做成」里封堵——第 40 行（模板说明：反向约束要封堵"默认塑料材质、**硬阴影**、运动模糊……"）与第 60 行（3D 卡："别做成：默认的塑料材质、**硬阴影**、全画面都清楚。"）。
  **点评**：这意味着 Lane B 的默认护栏**正好禁止**卡拉瓦乔模块的核心机制（硬光/硬阴影）。系统组合时必须在 prompt 里**显式覆盖**这条默认禁令（例如把"别做成：硬阴影"替换为"别做成：多光源、环境补光、背景发亮"），否则两个模块会互相抵消。`[史料]`（本机素材，行号已核）
- **状态**：`[史料]`（grep 于 2026-10-15；未找到外部"Caravaggio AI prompt"样本——web_search 全 provider 限流，见 §10）。

---

## 9. 参考资料（编号 ↔ 正文标注）

| # | 来源 | URL | 本机可达性（2026-10-15） |
|---|---|---|---|
| R1 | Wikipedia: Caravaggio（生平/年表/技法/影响链；三手来源，仅用于交叉核对与索引） | https://en.wikipedia.org/wiki/Caravaggio | ✅ read 200 |
| R2 | Wikipedia: Tenebrism（术语定义） | https://en.wikipedia.org/wiki/Tenebrism | ✅ read 200 |
| R3 | Wikipedia: Giovanni Baglione（1603 诽谤案证词引文、敌意传记背景） | https://en.wikipedia.org/wiki/Giovanni_Baglione | ✅ read 200 |
| R4 | The Met (Heilbrunn Timeline), Keith Christiansen, "Caravaggio (Michelangelo Merisi) (1571–1610) and His Followers", 2003-10 | https://www.metmuseum.org/essays/caravaggio-michelangelo-merisi-1571-1610-and-his-followers | ⚠️ 直读 429（限流）；**Wayback 快照 ✅**：https://web.archive.org/web/20250219231149/https://www.metmuseum.org/essays/caravaggio-michelangelo-merisi-1571-1610-and-his-followers |
| R5 | National Gallery London —《The Supper at Emmaus》NG172（in-depth 技法段） | https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-the-supper-at-emmaus | ✅ read 200 |
| R6 | National Gallery London —《Salome receives the Head of John the Baptist》NG6389（in-depth 晚期风格段） | https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-salome-receives-the-head-of-john-the-baptist | ✅ read 200 |
| R7 | National Gallery London — 艺术家页（生平叙事 + "painted straight onto the canvas"） | https://www.nationalgallery.org.uk/artists/michelangelo-merisi-da-caravaggio | ✅ read 200 |
| R8 | Musei Vaticani — Pinacoteca, Sala XII《Caravaggio, Deposition》 | https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/la-pinacoteca/sala-xii---secolo-xvii/caravaggio--deposizione-dalla-croce.html | ✅ read 200 |
| R9 | Galleria Borghese 藏品目录 —《Giovane con canestra di frutta》inv. 136（2012 底层草图发现） | https://www.collezionegalleriaborghese.it/opere/giovane-con-canestra-di-frutta | ✅ read 200 |
| R10 | Galleria Borghese 藏品目录 —《David con la testa di Golia》inv. 455（铭文/自画像/incisioni 诊断） | https://www.collezionegalleriaborghese.it/opere/david-con-la-testa-di-golia | ✅ read 200 |
| R11 | Andrew Graham-Dixon, *Caravaggio: A Life Sacred and Profane*（Penguin 2010）官方摘录页 | https://www.andrewgrahamdixon.com/extract/caravaggio-a-life-sacred-and-profane.html | ✅ read 200 |
| R12 | Galleria Borghese 藏品目录 —《Autoritratto in veste di Bacco (Bacchino malato)》inv. 534（Baglione 1642 引文"nello specchio"） | https://www.collezionegalleriaborghese.it/opere/autoritratto-in-veste-di-bacco-bacchino-malato | ✅ read 200 |
| R12b | Musei Vaticani — Pinacoteca, Sala XII 房间页（R8 的父页） | https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/la-pinacoteca/sala-xii---secolo-xvii.html | ✅ read 200 |
| R13 | Wikipedia: The Entombment of Christ (Caravaggio)（构图分析 + 被临摹史：Rubens/Fragonard/Géricault/Cézanne） | https://en.wikipedia.org/wiki/The_Entombment_of_Christ_(Caravaggio) | ✅ read 200 |
| R14 | BBC News — "Caravaggio's crimes exposed in Rome's police files"（2011-02-18；含 1604 侍者报案英译） | https://www.bbc.com/news/world-europe-12497978 | ✅ read 200 |
| R15 | Through Eternity Tours — "The Seven Crimes of Caravaggio"（1603 审讯引文、马耳他除籍用语 "putridum et foetidum membrum"） | https://www.througheternity.com/travel-guide/seven-crimes-caravaggio-rome | ✅ read 200 |
| R16 | The Art Story — Caravaggio（转引 Bellori 1672 英译与 Gombrich；二手，引文须回查） | https://www.theartstory.org/artist/caravaggio/ | ✅ read 200 |
| R17 | Literary Review — Jonathan Keates 评 Helen Langdon《Caravaggio: A Life》(1998) | https://literaryreview.co.uk/works-of-faith-hope-and-eroticism | ✅ 可读开头（付费墙） |
| R18 | Internet Archive — Helen Langdon, *Caravaggio: A Life*（全文借阅） | https://archive.org/details/caravaggiolife00lang | ⚠️ 未直读（检索命中，未打开） |
| R19 | Uffizi —《Bacchus》 | https://www.uffizi.it/opere/caravaggio-bacco | ⚠️ 未直读（由 [R12] 外链） |
| R20 | Met 藏品页 —《The Musicians》435844 /《The Denial of Saint Peter》437986 | https://www.metmuseum.org/en/art/collection/search/435844 | ⚠️ 未直读（由 [R4] 外链；Met 站直读限流） |
| R21 | 本机素材：`knowledge/domains/motion-graphics/origin/提示词全文.md`（L40、L60 护栏条目） | 本地路径 | ✅ grep 命中（见 §8.3） |

**交叉核对（≥2 条关键事实，两条独立来源）**

1. **"无纸上素描、直接在画布上画 + incisions 定位"**：NG《以马忤斯》in-depth（[R5]："not a single drawing… survives"、"incised freehand lines into the still malleable priming"、abbozzo 深棕笔绘）**×** Galleria Borghese《捧果篮的男孩》（[R9]：2012 年分析发现"直接画在画布上的底层草图"，印证 "dal naturale"）**×** Wikipedia（[R1]："scoring basic guides directly onto the canvas with the end of the brush handle"）。三条来源分属两家馆方著录与百科，独立。**结论：CONFIRMED（但需加精确化：不是"零准备"，而是"准备都发生在画布上"——笔绘底稿 abbozzo + 刻线 incisions + 高度预谋构图）。**
2. **"硬光机制＝画外高处单光源、无反射、背景近黑"**：Met 转引同代批评家（[R4]："focused light source from high up, without reflections… walls painted black"）**×** Bellori 1672（[R16]："placing a lamp high so that the light would fall straight down"）**×** NG（[R5]："A strong light from the left… casts a shadow on the blank wall behind Christ, almost like a reverse halo"）。**结论：CONFIRMED**（两条同代记录 + 一条馆方观察；注意 [R16] 为二手转引，见 §10）。
3. **1603 年诽谤案与证词**：Wikipedia "Giovanni Baglione"（[R3]：诉讼时间、当事人、Caravaggio 被判有罪并关押 Tor di Nona 两周、证词原文）**×** Through Eternity（[R15]：同段证词的英文表述与"Baglione 胜诉"叙述）。**结论：CONFIRMED（两条最终都源自 1603 年法庭文书，视为同源双引；已在 §5-1 注明）。**
4. **《大卫》自画像与铭文**：Galleria Borghese 藏品页（[R10]：Manilli 1650 记载、'H[umilit]AS O[ccidit] S[uperbiam]' 读法）**×** Wikipedia（[R1]："the severed head of the giant, which is again Caravaggio"）。**结论：CONFIRMED。**

---

## 10. 缺口与待验证

1. **原话几乎为零（结构性缺口，不是没查到）**：除 1603 年审讯那一句外，未找到任何书信/笔记/画论（已查：[R1][R11] 均称其文字留世极少；Graham-Dixon 明说"只有一句"）。§5 的其余条目均为同代转述或档案，**不可当画论使用**。
2. **Bellori 引文回查**：§5-3 用的是 [R16]（The Art Story）所载英译；**未回查 Bellori 1672 原书（Borea 编 1976 版）页码**。待办：找到 Bellori《Le vite》"Caravaggio" 节的原文页码。
3. **Met 馆方专文**：本机直读全程 429（curl 亦 429），仅经 Wayback 2025-02-19 快照读取 [R4]；引文作者（"同代批评家"）Met 未具名——**该段原始出处待考**（常见说法指向某 17 世纪评论，但本档案未证实，不写死）。
4. **死亡情形四说并存且互斥**：热病 [R1]／他杀（Tomassoni 家族或骑士团复仇）[R1]／铅中毒（2010 骨骼研究）[R1]／那不勒斯斗殴伤口引发的金黄色葡萄球菌败血症（2018 研究）[R1]；另有 [R14] 的"医院病床"说与传记的"海滩"说冲突。**结论：未决**——本档案不采信任一版本，只记录分歧。
5. **量化阈值为本项目归纳、未实测**：§4 的 P2/P3 百分比、§8.2 的 7 条规则阈值均未对原作做像素测量（分母＝假想参考帧），也未跑过渲染器；wave3 的 A-12 组合实验（建议主题"暴风雨中的海边灯塔"）可按 §8.2 逐帧自查后回改。
6. **未直读的 URL**：[R18]（Langdon 全文）、[R19]（Uffizi《Bacchus》）、[R20]（Met 藏品页）——均为检索/外链命中，未打开，标 `[UNVERIFIED]`。
7. **出生地分歧**：米兰（现代共识 [R1]）vs Caravaggio 镇（旧说；[R16] 仍写 Caravaggio）——已在 §0 双注。
8. **web_search 全 provider 限流**（2026-10-15）：外部"Caravaggio AI prompt"样本未能采集（§8.3 因此只有本机素材与护栏冲突分析）；替代通道用了 Brave HTML、Bing HTML、Wikipedia API、Wayback、Google Books API（429）。DuckDuckGo/Mojeek/Ecosia 均反爬拦截（实测）。
9. **画家页之外未核**：St John's Co-Cathedral（马耳他《斩首》）的馆方页未直读，§0 第 4 件作品的馆藏信息取自 [R1]。

---

## 11. 生平与年代轴（详细）

> wave14 加固增项（规格：`knowledge/domains/painters/program/README.md` §1）。任务重点三线：**① 档案文献（Mancini、Baglione 同时代记述、罗马档案诉讼记录）；② 1606 命案与逃亡（那不勒斯/马耳他/西西里/波尔托埃尔科莱）；③ 近年档案发现**。来源编号 `S1–S19` 为本节独立编号（§9 的 R 编号不动）；引文保留原文；证据分级沿用全文口径。
> **口径注（任务提示「2007 年书信」）**：经多通道检索，2007 年（2 月 14 日）的档案发现为**受洗记录**（非书信）；「书信」线的近年发现/再发现为——Wignacourt 1607-12-29（一对）与 1608-02-07、Pourbus 1607-09-25、Masetti 1607-05-26、de Rosis 1610-06-18（2022 年公布）、Gentile 1610–11 五封（1991 年刊布、2023–25 再检讨）。**未找到**（已查: DDG / Bing / Google Scholar / JSTOR / HathiTrust / Sogou / Baidu / AboutArt / Storia dell'Arte 等）字面意义的「2007 年发现的书信」；来源清单见 11.3。

### 11.1 叙述

**（1）米兰：出生、家庭与学徒（1571–1592）。** 米开朗基罗·梅里西 1571 年 9 月 29 日生于米兰，次日（9 月 30 日）在圣斯德望堂（Santo Stefano in Brolo）受洗。受洗记录原文：「Adi 30 ditto [Setembre 1571] fu Bap[tiza]to Michel Angelo f[iliol]o de D[omino] Firmo Merixio et D[omina] Lucia de Aratoribus / compar D[omino] Fran[cesc]o Sessa」；这条记录 2007 年 2 月 14 日由退休会计师维托里奥·皮拉米（Vittorio Pirami）在米兰教区档案馆偶然发现，为「生于米兰、而非卡拉瓦乔镇」的现代共识提供了直接证据 `[史料]`（S4、S5）。父亲费尔莫·梅里西（Fermo Merisi）是卡拉瓦乔侯爵家的管家兼建筑装饰师（"household administrator and architect-decorator to the marquess of Caravaggio"），母亲露琪亚·阿拉托里（Lucia Aratori）；两家均原籍卡拉瓦乔镇 `[史料]`（S1、S2）。1577 年为避瘟疫全家离米兰返乡，父亲途中染疫去世，祖父贝尔纳迪诺与叔父彼得罗相继去世 `[史料]`（S2）。1584 年 4 月 6 日，母亲代签学徒合同，13 岁的米开朗基罗进入米兰画家西蒙内·彼得扎诺（Simone Peterzano）画室四年，学费「四十余枚金盾」；彼得扎诺自称提香的学生（自画像题记可证），属伦巴第晚期风格主义一路 `[史料]`（S2）。母亲去世年份两说并存：Mancini 记为 1591 年 11 月 29 日（意维基采纳；遗产分割文献存世，画家约 1592 年年中离伦巴第），另有 1584 年说（英维基所据 Lambert 等）——本档案并记不裁 `[史料]`（S2、S1）。近年（2018/2022）Renato Di Tomasi 的档案研究证实：1591–92 年间画家继承约 1700 里拉帝国币遗产，并披露其与继兄、神父 Ludovico Merisi 的遗产冲突——「青年赤贫」的旧图景因此动摇 `[研究]`（S13）。

**（2）「消失的四年」与初到罗马（1592–1600）。** 1592 年 7 月 1 日是他最后一次在伦巴第被记录；此后至 1596 年间的行踪即所谓「消失的四年」。早期传记（Celio 1614、Mancini、Bellori）都说他在米兰犯下杀人案后逃亡（先威尼斯后罗马）；但档案复查（Berra 等）查无实据。2011 年罗马国家档案馆的新发现把他在罗马的最早记录定在 1596 年四旬斋（画家 Lorenzo Carli 画室一带；理发师 Pietropaolo Pellegrino 的证词），推翻旧说 1592；Di Tomasi 则主张抵罗马时间为 1594 年末–1595 年初 `[史料]/[研究]`（S2、S6、S13、S14）。初到罗马时「赤裸而极其贫困」（"naked and extremely needy… without fixed address and without provision… short of money"，三本源流一致）`[史料]`（S1）；先寄居有「Insalata 主教」绰号的 Pandolfo Pucci 家，后入 Cavalier d'Arpino（Giuseppe Cesari）工坊画花卉果实 `[史料]`（S1、S6）。约 1597 年（住院出院后，经画家朋友 Costantino Spata 引介）结识红衣主教弗朗切斯科·马里亚·德尔·蒙特（Francesco Maria del Monte）：主教购藏《老千》（I bari）等画，画家进入其府邸，人生转折由此完成 `[史料]`（S2）。1599–1600 年，孔塔雷利礼拜堂（Contarelli，圣路易吉·德·弗朗切西教堂）两幅马太像完成——「一年之内完成两件作品，成功就此打开」；随后瑟拉西礼拜堂（Cerasi）委托接踵而至 `[史料]`（S2、S13）。

**（3）罗马档案里的诉讼记录（1598–1606）。** 罗马国家档案馆（Archivio di Stato di Roma）的警察记录、法庭文书与公证档案构成他罗马生活最硬的一手材料。BBC 2011 年整理的核心时间线：1598-05-04 深夜无证携剑被捕（Piazza Navona 附近）；1600-11-19 凌晨用棍打人、以剑划破斗篷被诉；1601-10-02 被控与友人持剑袭击；1604-04-24 洋蓟事件（侍者 Pietro Antonio de Fosaccia 报案原文见 §5-4）；1604-10-19 向警察掷石被捕；1605-05-28 无证携剑与匕首被捕；1605-07-29 公证人 Mariano Pasqualone 指控其背后袭击（因模特「Lena」Maddalena Antognetti；他为此避走热那亚约三周）；1606-05-28 命案 `[史料]`（S3、S2）。1603 年另有诽谤案：画家 Giovanni Baglione 控告卡拉瓦乔、Orazio Gentileschi 与 Onorio Longhi 以诗诽谤；庭审证词里留下他关于绘画的唯一一句传世之语（§5-1）；他被判有罪、短暂关押 Tor di Nona 后经法国大使干预获释 `[史料]`（S3）。1605 年秋（10 月，一说 11 月）的受伤供词同样出自这些卷宗——面对刑事公证人他声称：「Io me so' ferito da me con la mia spada che so' cascato per queste strade et non so dove se sia suto, né c'è stato nesuno」（我是自己拿剑伤的自己；我在这些街上摔倒，不知在哪儿，也没有人在场）`[史料]`（S6、S2）。

**（4）1606 年命案与逃亡：罗马 → 科隆纳领地 → 那不勒斯。** 1606 年 5 月 28 日（星期日），坎波·马齐奥，紧邻 Scrofa 街：一场 pallacorda（早期网球）比赛的争执后爆发械斗，双方各四人——卡拉瓦乔方：Onorio Longhi、博洛尼亚上尉 Petronio Troppa 及一名未识别者；对方：Ranuccio Tomassoni 及其兄弟 Giovanni Francesco、姻亲 Ignazio 与 Federico Iugoli `[研究]`（S10）。卡拉瓦乔一记刺击致对手股动脉出血（对手已倒地），Ranuccio 旋即死亡；Giovanni Francesco 击中米开朗基罗头部并重伤 Troppa（后者被押入 Tor di Nona）。动机旧说纷纭：赌债、比赛争议（Baglione 记「一个判罚」）、与 Fillide Melandroni／Lavinia Iugoli 的情感纠纷，乃至政治背景（Tomassoni 家亲西班牙，米开朗基罗受亲法派保护）`[研究]`（S2、S10）。他当夜被抬入科隆纳宫，随后藏身科隆纳家族领地——Zagarolo、Palestrina、Paliano——受保护人 Costanza Sforza Colonna 照应；罗马法庭随后缺席宣判「bando capitale」（首都放逐令；未必等于死刑，可能仅约五年驱逐——Renzi 判断大概率属后者）`[研究]`（S10）。1606 年 6 月 28 日已「contumace」（缺席在逃）；1607 年 5 月 26 日摩德纳公爵代理 Fabio Masetti 信云：（款项）「…per un homicidio comesso dal detto [Caravaggio], per il quale è stato bandito, ma perché il detto homicidio fu casuale e restò anch'egli malamente ferito, si tratta della sua remissione et si spera la g[razia]」——案发约一年后双方已在谋求和解与赦免 `[史料]`（S9）。

**（5）那不勒斯 → 马耳他（1606–1608）。** 1606 年秋抵那不勒斯（受科隆纳家保护）：接下 Pio Monte della Misericordia《七件善事》（1607 年完成）与《玫瑰经圣母》等；1606 年 Banco di Sant'Eligio 的「copiapolizze」还记录了他为克罗地亚商人 Nicola Radulovich 所作祭坛画的付款条目（画本身「无人见过」，或未完成）`[史料]`（S15、S2）。1607 年 7 月渡海赴马耳他——由 Costanza 之子、骑士团舰队将领 Fabrizio Sforza Colonna 安排；目标是以骑士身份取得对教皇判决的免疫力 `[史料]/[研究]`（S1、S17）。马耳他国家图书馆（瓦莱塔）的 Wignacourt 大团长通信近年被系统整理（Macioce）：**1607 年 12 月 29 日**大团长致驻罗马教廷两位大使（Fornellini、Bosio）的一对信件，请求准许「不经常规资格证明」授予这位候选人骑士服——信中为一位「virtuosissimo」的无名人物求情，并请求「non li hobsti l'aver in rissa commesso un homicidio」（愿其「斗殴中杀人」一事不妨碍授予）；**1608 年 2 月 7 日**再致教皇请求特别豁免 `[史料]`（S17、S10）。1608 年 7 月 14 日获授「恩典骑士」（Cavaliere di Grazia Magistrale），期间完成《施洗者圣约翰被斩首》（唯一署名作品）等 `[史料]`（S17）。但 1608 年 8 月底被捕入狱（据 Sciberras 档案研究：与一名高等骑士冲突，房门被砸、骑士重伤），关押于 Birgu 圣安杰洛堡；1608 年 10 月 6 日越狱（或得科隆纳家之助）逃往西西里；同年 12 月被缺席褫夺骑士服（敕书用语「putridum et foetidum membrum」——「腐臭之肢」，属标准套语且可逆）`[史料]/[研究]`（S2、S10）。

**（6）西西里 → 再返那不勒斯（1608–1609）。** 西西里近一年：叙拉古（老友 Mario Minniti 接待；《圣露西亚下葬》）、墨西拿（《拉撒路复活》《牧人来拜》）、巴勒莫（《圣方济各与圣劳伦斯的圣诞》——近年研究（Cuppone）提出它或为 1600 年罗马为商人 Fabio Nuti 所作后寄往巴勒莫；1969 年被盗至今失踪）`[史料]/[研究]`（S2、S14）。1609 年夏末返那不勒斯，再受科隆纳家庇护；1609 年 10 月（大概率）在 Cerriglio 酒馆外遭数名男子袭击、面部毁伤，「死亡」消息开始流传（Avvisi 有「重伤未死」与「已死」两说）`[史料]/[研究]`（S2、S10）。

**（7）1610：最后旅程、死亡与身后。** 1610 年为 Marcantonio Doria 画《圣乌尔苏拉殉道》（被视为最后作品）；罗马方面 Scipione Borghese 正为其争取保罗五世的赦免（赦免是否实际签发寄达，无确证 `[史料]`S2）；他携三幅画（两幅《圣约翰》与一幅《抹大拉》，后为「赎金」）乘快帆（felucca）北上，途中在 Palo di Ladispoli 被拦、短暂拘押，船却带其行李继续北行；他随后（据 Gentile 信）「per terra e forse a piedi si ridusse fino a Port'Hercole」（或经陆路、可能步行抵达波尔托埃尔科莱）`[史料]`（S9、S11）。1610 年 7 月 18 日死于波尔托埃尔科莱；7 月 28 日罗马匿名 avviso 已报死讯、7 月 31 日续报「死于热病」；**7 月 29 日**驻那不勒斯教廷大使 Deodato Gentile 致 Scipione Borghese 的信写道：「Ritrovo che il povero Caravaggio non è morto in Procida, ma a Porthercole, perché essendo capitato con la felluca in quale andava a Palo, ivi da quel Capitano fu carcerato e la felluca in quel romore tiratasi in alto mare se ne ritornò a Napoli」（我查明可怜的卡拉瓦乔并非死于普罗奇达，而是波尔托埃尔科莱：他随快帆行至 Palo，被那里的船长拘押，船在混乱中驶回那不勒斯）——死讯最早的官方通信之一（Pacelli 1991 年刊布；2023–25 年 Carla Rossi 与 Francesca Curti 等就其细节展开新一轮论战）`[史料]`（S11、S12）。葬于波尔托埃尔科莱圣塞巴斯蒂亚诺墓地；1956 年修路时遗骨迁入现公墓（Sant'Erasmo 一带）；2010 年（2008 年起）跨学科研究宣称以高置信度识别其遗骨（DNA/碳十四/骨骼分析），并先后提出铅中毒（2010）、金黄色葡萄球菌败血症（2018）等死因假说——与「热病」「他杀」诸说并存，本档案不采信任一版本 `[研究]`（S1、S2）。友人 Marzio Milesi 墓志铭称其「活了三十六年九个月零二十天」，誉其「在绘画上不逊于任何画家，而堪比自然本身」（§5-6）`[史料]`（S1）。

**（8）身后与「近年档案发现」清单。** 身后：17 世纪起名声渐被遮蔽，20 世纪经 Roberto Longhi 一脉重估（1920 年代起）、1951 年米兰王宫大展，至 21 世纪成为「超级明星」 `[研究]`（S1）。**近年档案发现（本节重点，按时间）**：① **2007-02-14** 受洗记录（Pirami；米兰教区档案馆；确认米兰出生）`[史料]`（S4、S5）；② **2010–2011** 罗马国家档案馆修复与展览「Caravaggio a Roma. Una vita dal vero」——7 名青年研究者翻检 60 余公里档案、修复 30 余卷：新见 1597 年司法文书、1604 年租赁合同（Prudenzia Bruni）、1618 年 Faustina Juvarra 遗嘱、1605 年受伤供词等；展览宣称「颠覆性新见、重写传记」（BBC 同期报道警察卷宗）`[史料]`（S6、S7、S8、S3）；③ **2012** 博尔盖塞美术馆分析发现《捧果篮的男孩》画布底层草图（§2-2、§9 交叉核对 1）`[研究]`（R9）；④ **2014–2019** 图卢兹《朱迪斯》再现与 Louis Finson 文献（含 1607 年书信与 1617 年遗嘱；归属仍存争议）`[研究]`（S18）；⑤ **2018–2024** Di Tomasi 系列：遗产文件（2018）、Orsini 基金新见 1610-06-18 Marcello de Rosis 致 Virginio Orsini 书信（2022）、米兰「狱案」再考（2024）`[史料]/[研究]`（S13）；⑥ **2021–2022** Giulia Cocconi 发现 Tomassoni 家两份委托书（1609-11-20、1610-03-15；和平协议「Instrumentum pacis」）`[史料]`（S9）；⑦ **2021** 马德里《Ecce Homo》再归属（普拉多/文化部出口禁令）`[研究]`（S1）；⑧ **2023** Macioce《Documenti, fonti e inventari》第 3 版（+106 份文件）与 Zuccari 等《Cantiere Caravaggio》`[研究]`（S14、S16）；⑨ **2023–2025** 1610 年 Gentile 书信、Margotti 7 月 24 日信与「Procida 误传」的再检讨（Rossi/Curti 论战）`[研究]`（S11、S12）；⑩（备查）**2014** Vinceti 公布的 1610 年那不勒斯副王（Pedro Fernández de Castro）致 Stato dei Presidi 长官信（转述死讯并追索三幅画；主张性材料，标 `[推测]` 级备查）`[史料]/[推测]`（S19）。另：Celio《Vite》（1614）手稿「近年由 Riccardo Gandolfi 发现」，为早期传记增一新源 `[研究]`（S14）。

### 11.2 年份表（≥15 行）

| 年份 | 事件 | 证据级（来源） |
|---|---|---|
| 1571 | 9 月 29 日生于米兰；9 月 30 日在 Santo Stefano in Brolo 受洗（记录 2007 年发现） | `[史料]` S4/S5 |
| 1577 | 避疫返乡，父亲 Fermo 去世（祖父、叔父相继去世） | `[史料]` S2 |
| 1584 | 4 月 6 日与 Simone Peterzano 签四年学徒合同（母亲代签，四十余金盾） | `[史料]` S2 |
| 1591/1592 | 母亲去世（1591-11-29 说 / 1584 说并存）；约 1592 年中离伦巴第 | `[史料]` S2/S1 |
| 1592 | 7 月 1 日最后一次伦巴第记录；「消失的四年」开始 | `[史料]` S14 |
| 1592–1595/96 | 空白期（米兰狱案说 vs 威尼斯说；Di Tomasi：约 1594 末–1595 初抵罗马） | `[研究]` S13/S2 |
| 1596 | 罗马最早记录（四旬斋；Lorenzo Carli 画室；旧说 1592） | `[史料]` S6/S14 |
| 1597 | 结识德尔·蒙特主教并入其府邸；约此前后住院（Spata 引介）；7 月司法文书（新见） | `[史料]` S2/S14 |
| 1599–1600 | 孔塔雷利礼拜堂两作（1599 签约、1600 揭幕）；成名 | `[史料]` S2/S13 |
| 1600-11-19 | 被诉打人、剑划斗篷（档案） | `[史料]` S3 |
| 1601 | 瑟拉西礼拜堂两作；《以马忤斯的晚餐》 | `[史料]` S1 |
| 1603 | Baglione 诽谤案：作证、被判有罪、短暂关押后获释 | `[史料]` S3 |
| 1604-04-24 | 洋蓟事件（侍者报案） | `[史料]` S3 |
| 1605-07-29 | Pasqualone 袭击案；避走热那亚约三周 | `[史料]` S2/S3 |
| 1605 秋 | 受伤供词（「自己刺伤自己」）；房租纠纷与掷石（Prudenzia Bruni） | `[史料]` S6/S2 |
| 1606-05-28 | 杀 Ranuccio Tomassoni；当夜入科隆纳宫；藏身 Zagarolo/Palestrina/Paliano | `[史料]/[研究]` S10 |
| 1606-06-28 | 缺席（contumace）；其后 bando capitale | `[史料]` S9/S10 |
| 1606 秋 | 抵那不勒斯；受 Costanza Colonna 保护 | `[史料]` S2/S15 |
| 1606–1607 | 《七件善事》《玫瑰经圣母》；Radulovich 付款条目（1606 copiapolizze） | `[史料]` S15 |
| 1607-05-26 | Masetti 书信（「si spera la grazia」） | `[史料]` S9 |
| 1607-07 | 渡海抵马耳他 | `[史料]` S1/S17 |
| 1607-09-25 | Pourbus 致曼图亚公爵信（Finson 持有「Oloferno」与《玫瑰经圣母》） | `[史料]` S18 |
| 1607-12-29 | Wignacourt 致罗马两大使信（一对；「non li hobsti…」） | `[史料]` S17/S10 |
| 1608-02-07 | Wignacourt 致教皇信（特别豁免） | `[史料]` S17 |
| 1608-07-14 | 授予「恩典骑士」；《斩首》（唯一签名作） | `[史料]` S17 |
| 1608-08 末 | 与高等骑士冲突被捕，关押 Birgu 圣安杰洛堡 | `[史料]/[研究]` S2/S10 |
| 1608-10-06 | 越狱，逃往西西里 | `[史料]` S10 |
| 1608-12 | 缺席褫夺骑士服（「putridum et foetidum membrum」） | `[史料]` S10 |
| 1608–1609 | 西西里：叙拉古/墨西拿/巴勒莫；《圣露西亚下葬》《拉撒路复活》《牧人来拜》《圣诞》 | `[史料]` S2 |
| 1609-08/09 | 返那不勒斯 | `[史料]` S2 |
| 1609-10 | Cerriglio 遇袭毁容；死讯流传 | `[史料]` S2/S10 |
| 1610 | 《圣乌尔苏拉殉道》（最后作品）；6 月 18 日 de Rosis 致 Orsini 书信 | `[史料]/[研究]` S13 |
| 1610-07 | 快帆北上；Palo 被拦；抵波尔托埃尔科莱 | `[史料]` S9/S11 |
| 1610-07-18 | 卒于波尔托埃尔科莱 | `[史料]` S1 |
| 1610-07-28/31 | avviso 报死讯（31 日续报「热病」）；Gentile 致 Borghese 信（「非死于普罗奇达」） | `[史料]` S11/S12 |
| 1610 | Milesi 墓志铭；葬圣塞巴斯蒂亚诺墓地 | `[史料]` S1 |
| 1920s–1951 | Longhi 重估；1951 米兰大展 | `[研究]` S1 |
| 2007-02-14 | 受洗记录发现（Pirami） | `[史料]` S4/S5 |
| 2010–2011 | 罗马国档馆修复/展览；BBC 警察卷宗报道 | `[史料]` S3/S6/S7/S8 |
| 2012 | 博尔盖塞：《捧果篮的男孩》底层草图发现 | `[研究]` R9 |
| 2014–2019 | 图卢兹《朱迪斯》；Finson 文献 | `[研究]` S18 |
| 2018–2024 | Di Tomasi 系列；Cocconi 委托书；Ecce Homo 再归属 | `[史料]/[研究]` S13/S9/S1 |
| 2023 | Macioce 第 3 版（+106 文件）；《Cantiere Caravaggio》 | `[研究]` S14/S16 |
| 2025 | Gentile 信再检讨（Rossi/Curti）；「Caravaggio 2025」大展 | `[研究]` S11/S12 |

### 11.3 本节来源（S 编号，19 条）

1. **S1** — Wikipedia (EN), "Caravaggio" — https://en.wikipedia.org/wiki/Caravaggio（三手；年表/死亡/身后交叉核对）
2. **S2** — Wikipedia (IT), "Caravaggio" — https://it.wikipedia.org/wiki/Caravaggio（三手；家庭/学徒合同/马耳他/死亡辩论）
3. **S3** — BBC News (David Willey), "Caravaggio's crimes exposed in Rome's police files", 2011-02-18 — https://www.bbc.com/news/world-europe-12497978（罗马国档馆警察卷宗时间线；侍者报案英译；「医院病床」说）
4. **S4** — il Giornale (Maria Sorbi), "Il ragioniere della Standa che ha scoperto la verità sulla nascita di Caravaggio", 2018-02-28 — https://www.ilgiornale.it/news/ragioniere-standa-che-ha-scoperto-verit-sulla-nascita-1498933.html（2007-02-14 发现经过）
5. **S5** — Chiesa di Milano, "Caravaggio? E' nato a Milano. Un anno fa la scoperta all'Archivio Diocesano" — https://www.chiesadimilano.it/senza-categoria/caravaggio-e-nato-a-milano-un-anno-fa-la-scoperta-allarchivio-diocesano-33577.html
6. **S6** — Corriere della Sera (Lauretta Colonnelli), "Caravaggio, non solo quadri, ma documenti e manoscritti", 2011-02-10 — https://roma.corriere.it/notizie/arte_e_cultura/11_febbraio_10/mostra-passi-caravaggio-181438253952.shtml（展览与 7 名研究者名单；1605 供词引文）
7. **S7** — Archivio di Stato di Roma, "Caravaggio a Roma. Una vita dal vero"（2011 展览页）— https://archiviodistatoroma.cultura.gov.it/2011/02/11/caravaggio-a-roma-una-vita-dal-vero/
8. **S8** — Blitz Quotidiano, "Caravaggio, restaurati i documenti che chiariscono il suo arrivo a Roma", 2010-09-27 — https://archivio.blitzquotidiano.it/arte/caravaggio-documenti-restaurati-564084/
9. **S9** — Francesca Curti, "«Misesi in una feluca con alcune poche robe»: l'ultimo viaggio di Caravaggio", Storia dell'Arte in tempo reale, 2023-11-03 — https://www.storiadellarterivista.it/blog/2023/11/03/misesi-in-una-feluca-con-alcune-poche-robe-lultimo-viaggio-di-caravaggio/（Gentile 五封信；Cocconi 委托书；Masetti 1607-05-26 引文）
10. **S10** — Claudia Renzi, "«…non li hobsti l'aver in rissa commesso un homicidio». Caravaggio: dalla corruzione delle fonti alla leggenda del pittore maledetto", AboutArtOnline — https://www.aboutartonline.com/non-li-hobsti-laver-in-rissa-commesso-un-homicidio-caravaggio-dalla-corruzione-delle-fonti-alla-leggenda-del-pittore-maledetto/（1606 命案细节；Wignacourt 1607-12 信引文；越狱日期；Celio/Bellori 引文）
11. **S11** — News-Art, "Gli ultimi giorni di vita di Caravaggio", 2025-11-21 — https://news-art.it/news/gli-ultimi-giorni-di-vita-di-caravaggio.htm（Carla Rossi 两文转载；Gentile 信「per terra e forse a piedi」）
12. **S12** — AboutArtOnline, "«E' una questione di metodo». Precisazioni e chiarimenti di Francesca Curti sugli ultimi giorni di Caravaggio", 2025-08-24 — https://www.aboutartonline.com/e-una-questione-di-metodo-precisazioni-e-chiarimenti-di-francesca-curti-sugli-ultimi-giorni-di-caravaggio/
13. **S13** — News-Art, "Studi Archivistici su Caravaggio: Nuove Prospettive sulla Giovinezza e le vicende Milanesi" — https://news-art.it/news/studi-archivistici-su-caravaggio--nuove-prospettive-sulla-giovinezza-e-le-vicende-milanesi.htm（Di Tomasi 2018/2022/2024；1700 里拉遗产；de Rosis 书信）
14. **S14** — Rossella Vodret, "Caravaggio: la nuova edizione del monumentale volume di Stefania Macioce", Storia dell'Arte in tempo reale, 2023-10-21 — https://www.storiadellarterivista.it/blog/2023/10/21/recensione-del-volume-di-stefania-macioce-michelangelo-merisi-da-caravaggio-documenti-fonti-e-inventari/（第 3 版；1597 文书；Celio Vite 由 Gandolfi 发现）
15. **S15** — il Cartastorie（Banco di Napoli 历史档案馆博物馆）, "Caravaggio" — https://www.ilcartastorie.it/caravaggio/（1606 copiapolizze；Radulovich 条目）
16. **S16** — Avvenire (Maurizio Cecchetti), "Le verità ritrovate su Caravaggio", 2023-09-01 — https://www.avvenire.it/agora/cultura/le-verita-ritrovate-su-caravaggio_69272
17. **S17** — "Caravaggio a Malta e i suoi referenti: notizie d'archivio"（Macioce 文摘要页，Storia dell'Arte in tempo reale）— https://www.storiadellarterivista.it/caravaggio-a-malta-e-i-suoi-referenti-notizie-darchivio/（Wignacourt 1607-12-29 / 1608-02-07 书信；1608-07-14 授勋）
18. **S18** — Wikipedia (IT), "Giuditta che decapita Oloferne (Finson)" — https://it.wikipedia.org/wiki/Giuditta_che_decapita_Oloferne_(Finson)（Pourbus 1607-09-25 书信）
19. **S19** — ToscanaLibri, "Mistero sulla morte di Caravaggio, ritrovata lettera di un viceré che rafforza l'ipotesi sul decesso a Porto Ercole", 2014-06-17 — https://www.toscanalibri.it/notizia/mistero-sulla-morte-di-caravaggio-ritrovata-lettera-di-un-vicere-che-rafforza-l-ipotesi-sul-decesso-a-porto-ercole_6844/（副王信；Vinceti 主张，备查）

## 12. 临摹/学习清单

> wave14 加固增项（规格 §1）：9 件代表作，各写「看什么 / 学什么 / 怎么练（可执行练习）」。练习默认以纸笔/数字笔临摹或重演执行；涉及生成工具处沿用 §8.1 提示词与 §8.2 自查规则；作品图源见 `_images/caravaggio/` 与 §9。
> 建议顺序：12.1 → 12.3 → 12.2 → 12.4 → 12.7 → 12.6 → 12.8 → 12.5 → 12.9（由单光源静物，到叙事装置，到巨幅黑暗，到晚期极简）。

### 12.1 《捧果篮的男孩》Boy with a Basket of Fruit（c.1595，Galleria Borghese，inv. 136）
- **看什么**：早期「从自然写生」的极限样本——2012 年分析发现的画布底层草图（§2-2）；静物精度与人物同等；单光源下叶片投影、果皮高光、篮条编织密度。
- **学什么**：让「静物」当主角的构图（主体偏右下、深底、贴平面雏形）；同光源下「物—人」一致性（高光方向与阴影色温）。
- **怎么练**：① 摆一组真实水果 + 单一硬光（无补光）拍照；② 先只画水果与篮（明暗两大区起手，禁细化）；③ 加一只手入画；④ 用 §8.2-4 自查「高光连通域 ≤5 且落脸/手/道具」，用 §8.2-2 查背景最亮 ≤ 全帧 10%。

### 12.2 《圣马太蒙召》The Calling of Saint Matthew（1599–1600，San Luigi dei Francesi，Contarelli 礼拜堂）
- **看什么**：一束光「选中」一个人的叙事机制；基督的手与马太的手（与米开朗基罗《创造亚当》的互文）；五个税吏的视线链；当代服装 + 税吏房间（§1-7）。
- **学什么**：用光当叙事主语（光只落在被召唤者）；手势向量指向叙事对象；群体中「一瞬」的冻结。
- **怎么练**：① 写一张「光选人」分镜：标出谁被照亮、谁留在暗里、光源画外位置；② 画 5 人视线链与手势向量图（检查箭头是否汇聚）；③ 临摹为明暗大块（只画 3 个亮块），再逐步加深；④ 自查：高光只落脸/手/道具（§8.2-4）。

### 12.3 《以马忤斯的晚餐》The Supper at Emmaus（1601，National Gallery London，NG172）
- **看什么**：abbozzo 笔绘底稿与 incisions 刻线（§2-1/2/3）；两条厚涂斜笔的定位法；「认出的一瞬」——前伸的手、桌上静物（面包/水果/酒杯）、墙上「反向光环」阴影（§1-1）。
- **学什么**：决定性瞬间的构图（动作极值 + 手势延长线）；直接画法流程（深色笔线定形 → 刻线 → 铺色 → 亮部厚涂）。
- **怎么练**：① 不打草稿纸，直接在画布/厚纸上以深棕色笔线定形（限 30 分钟）；② 用笔杆尾端刻出两个人物位置线；③ 复现「手—面包—酒杯」的三角；④ 自查：中间调压缩（§8.2-3）与暗部保细节（§8.2-7）。

### 12.4 《基督下葬》The Entombment（1603–04，Musei Vaticani，Pinacoteca Sala XII）
- **看什么**：五人群像的「贴平面」压缩（§1-4）；四只手臂的合力方向（把视线推向画外墓穴）；尼哥底母用米开朗基罗的脸（§6.1）；大块明暗的简洁。
- **学什么**：群像压缩术（主人物包围盒 ≥80%、边缘裁切）；手势向量的合力与画外指向。
- **怎么练**：① 用箭头图标注所有手势/视线向量，检查是否汇聚到画外一点；② 只画五人的明暗大块（忽略细节），再做「谁被裁切」检查；③ 复现石材与布褶两种质感的两级对比。

### 12.5 《圣母之死》Death of the Virgin（1601–03，Louvre；1606 年被拒收撤下）
- **看什么**：被拒收的「失礼」细节——垂落的手、肿胀的躯体、极简的圣光；Mancini 1606-10-14 信与 Rubens 接手（§6.2、§11）。
- **学什么**：把宗教图像「去象征化」；悲剧性由物理细节（脚、腹、手）承担。
- **怎么练**：① 对照 §11 引文逐条找出「被指摘」的细节；② 做「删掉所有光环/象征物」的改写练习：只留人体与布；③ 用单光源重摆「垂手」姿态并写生。

### 12.6 《大卫手提歌利亚的头》David with the Head of Goliath（1606–07 或 1609–10，Galleria Borghese，inv. 455）
- **看什么**：晚期色域收窄与宽笔触（§1-9、§2-8）；巨人头 = 自画像（§6.2）；剑刃铭文 "H.AS O S"；光的双重心（持头的手 vs 垂下的头）。
- **学什么**：把自传性放进道具（头、剑铭）；晚期「少色阶、多黑」的收窄法。
- **怎么练**：① 临摹头部「半光半暗」处理（限三色：赭/黑/白）；② 做「只照亮两个物件」（手 + 头）的缩略图 6 张；③ 自查：色相数与高光数量（§4-P5 强档）。

### 12.7 《施洗者圣约翰被斩首》The Beheading of Saint John the Baptist（1608，St John's Co-Cathedral, Valletta）
- **看什么**：370 × 520 cm 巨幅里的「黑暗主导」；血泊中的签名（唯一）；冷漠的旁观者与空荡牢房——神圣处决被画成监狱谋杀。
- **学什么**：大面积黑暗 + 单一动作的巨幅控制；把「签名」当构图元素。
- **怎么练**：① 用「暗面 ≥60%」约束做同构草图（人物贴左、大墙留黑）；② 复现血泊签名位置（画面下部中线）；③ 检查：可见光源数 = 0、光斑落点 = 三个关键人物部位。

### 12.8 《七件善事》The Seven Works of Mercy（1606–07，Pio Monte della Misericordia, Napoli）
- **看什么**：七件事在一格街巷夜景里叠合；从高处垂下的光柱同时点亮两组善行；人群密度与「手」的可辨识性。
- **学什么**：多叙事合并（七个动作 → 一个画面）；垂直光柱的分配；密度下的可读性。
- **怎么练**：① 把七个动作写成七行分镜，再压进一格构图（限 10 人内）；② 标出每件善事对应的「手」；③ 自查：每件善事至少一只可辨的手 + 光斑覆盖。

### 12.9 《圣乌尔苏拉殉道》The Martyrdom of Saint Ursula（1610，Gallerie d'Italia, Napoli）
- **看什么**：最后作品；光只照亮三人（乌尔苏拉、箭、刽子手半身）；「瞬间之后」的沉默；晚期的极简。
- **学什么**：把「死亡瞬间」压缩到三人 + 一束光；晚期的克制。
- **怎么练**：① 临摹三人组的光斑分布图（标出 3 个高光连通域）；② 用「只 3 个高光」的约束做一张新构图练习。

## 自审四段

### A. 早产出
骨架（0–10 全节标题）在开工第 7 次工具调用时即落盘 `knowledge/domains/painters/dossiers/caravaggio.md`（write，1554 bytes）；随后按"来源到手即回填"的顺序逐节覆盖，最终版覆盖模板全部节（0–10 + 自审）。

### B. 反驳（挑最强结论逐条试推翻）

| # | 结论 | 反驳动作（跑过什么） | 判定 |
|---|---|---|---|
| 1 | "卡拉瓦乔不做任何准备、不打底稿直接画" | 逐篇复读馆方文本：[R5] 同时写了 "not a single drawing… survives" **和** abbozzo/incisions；[R9] 记 2012 年发现画布上的底层草图；[R1] 记"用笔杆尾端在画布上划定位线" | **WEAKENED → 改写**：正文（§2-1/2/3、§9 交叉核对 1）改为"**准备全部发生在画布上**（abbozzo 笔绘底稿 + incisions 刻线 + 高度预谋、少 pentimenti），不是纸上素描/卡通" |
| 2 | "他是'从自然写生'的纯粹现实主义者" | 查 [R12]：Bacchino 的姿势引用 Peterzano 草图与 Dürer 版画；[R13]：《下葬》引用米开朗基罗《圣殇》/自画像与拉斐尔构图；[R1]：钦佩拉斐尔 | **WEAKENED**：正文 §6.1 增列"古典与前人的直接引用（可考）"；§3 不写"拒绝传统"，只写"反理想化 + 物理真实优先" |
| 3 | "他死于 1610 年热病/铅中毒" | 交叉 [R1]（四说并存 + 2010 骨骼研究 + 2018 败血症研究）与 [R14]（档案展："死在医院病床，不是海滩"） | **OVERTURNED（作为单一结论不成立）**：正文不采信任一死因，§10-4 只记录分歧 |
| 4 | "Bellori 的'灯置于高处'引文可直接引用" | 追源：该英译见 [R16]（通俗艺术网站），未回查 Bellori 1672 原书 | **WEAKENED**：§5-3 与 §7-10 均标注"二手转引、原书页码回查未做"，并进 §10-2 缺口 |
| 5 | "1603 年那句'没有画家认为 Baglione 画得好'是他关于绘画的唯一一句话" | 核 [R11] 原文："only one solitary sentence from him on the subject of painting — … elicited when he was under interrogation for the capital crime of libel"；核 [R3] 证词两处引文 | **CONFIRMED（措辞收窄）**：正文写"唯一被现代学者认定为'他关于绘画的话'的记录"，不写"他一生只说过一句关于画的话" |

### C. 机械验证（原样粘贴；检查器：`read` 直读 3 条关键 URL，见下）

**① National Gallery London《The Supper at Emmaus》in-depth（R5）——`read` 返回头部逐字：**
```
URL: https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-the-supper-at-emmaus
Content-Type: text/html
Method: native

---
canonical: https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-the-supper-at-emmaus
meta-author: The National Gallery, London
meta-description: Michelangelo Merisi da Caravaggio, The Supper at Emmaus, 1601. Read about this painting, learn the key facts and zoom in to discover more.
meta-viewport: width=device-width, initial-scale=1, shrink-to-fit=no
title: Michelangelo Merisi da Caravaggio | The Supper at Emmaus | NG172 | National Gallery, London
```
正文命中（逐字）：`"In many of his works he also incised freehand lines into the still malleable priming (or undercoat) to mark out where figures were to be placed, and presumably to allow models to resume their poses."`；`"not a single drawing that can be firmly attributed to Caravaggio survives"`。

**② Galleria Borghese《Giovane con canestra di frutta》inv.136（R9）——`read` 返回头部逐字：**
```
URL: https://www.collezionegalleriaborghese.it/opere/giovane-con-canestra-di-frutta
Content-Type: text/html
Method: native

---
meta-author: Galleria Borghese
meta-og:site_name: collezionegalleriaborghese.it
meta-og:title: Merisi Michelangelo detto Caravaggio - Giovane con canestra di frutta
meta-og:type: website
meta-og:url: https://www.collezionegalleriaborghese.it/opere/giovane-con-canestra-di-frutta
title: Giovane con canestra di frutta - Merisi Michelangelo detto Caravaggio
```
正文命中（逐字）：`"In seguito ad alcune analisi effettuate sull'opera nel 2012, è stata evidenziata la presenza di un disegno preparatorio sottostante, uno schizzo fatto dall'artista direttamente sulla tela che conferma quanto testimoniato dalle fonti antiche a proposito del modo di Caravaggio di dipingere 'dal naturale'."`

**③ BBC News（R14）——`read` 返回头部逐字：**
```
URL: https://www.bbc.com/news/world-europe-12497978
Content-Type: text/html
Method: native

---
canonical: https://www.bbc.com/news/world-europe-12497978
meta-article:section: Europe
meta-description: An exhibition of documents at Rome's State Archives throws vivid light on Caravaggio's tumultuous life in the city, 400 years ago.
meta-og:title: Caravaggio's crimes exposed in Rome's police files
meta-og:url: https://www.bbc.com/news/world-europe-12497978
title: Caravaggio's crimes exposed in Rome's police files - BBC News
```
正文命中（逐字）：`"Statement to police by Pietro Antonio de Fosaccia, waiter, 26 April 1604:"`；`"He did not die alone on a beach after escaping from his creditors and the police, as some of his biographers say, but in a hospital bed."`

（三条 URL 的完整 `read` 返回体量较大，此处按"头部 meta 块 + 正文命中句"原样摘录，未改一字；完整输出见本会话工具回执。）

**④ 附加机械核对（Met 通道）**：`curl -A "Mozilla/5.0…" https://www.metmuseum.org/essays/caravaggio-michelangelo-merisi-1571-1610-and-his-followers` → `429 34224`（限流确认）；`read https://web.archive.org/web/2024/https://www.metmuseum.org/essays/caravaggio-michelangelo-merisi-1571-1610-and-his-followers` → 200，快照正文含 `"Caravaggio pushed the figures up against the picture plane and used light to enhance the dramatic impact and give the figures a quality of immediacy."`

### D. 小结（≤14 行）
- **已确立**：10 条视觉指纹、10 条技法规则、8 条创作原则、6 个控制参数（各三档 + 与伦勃朗的分工口径）、8 条"原话"（全部注明性质：审讯/敌意传记/档案/友人墓志）、10 条馆方与学者深度分析、21 条参考来源（其中 15 条本机 ✅ 直读）。
- **已确立（交叉核对 4 组）**：①"准备全在画布上"（NG × Borghese × Wikipedia）；②硬光机制（Met 引同代 × Bellori 转引 × NG）；③1603 审讯证词（Wikipedia Baglione × Through Eternity，同源双引）；④《大卫》自画像与铭文（Borghese × Wikipedia）。
- **已改写/被削弱**：①"零准备直接画"→"准备在画布上"；②"纯粹写生现实主义者"→补古典引用；③Bellori 引文降为二手转引；④"唯一一句话"措辞收窄。
- **被推翻**：单一死因（四说并存 + 医院床 vs 海滩冲突）——正文不采信任何版本。
- **未知**：Bellori 原书页码；Met 所引"同代批评家"是谁；Langdon/Uffizi/Met 藏品页未直读；外部 AI prompt 样本未采（搜索通道全限流）。
- **下一步**：wave3 A-12 用 §8.1 正/负向 prompt 跑同一主题对照（建议"暴风雨中的海边灯塔"），按 §8.2 的 7 条逐帧自查；组合实验时**必须**处理 §8.3 的护栏冲突（默认禁硬阴影）。
- **我仍赌错的是什么**：§4/§8.2 的量化阈值（背景 ≤10%、中间调 ≤25%、贴平面 ≥80%）是我从馆方文本与作品归纳的**未实测**参数——若对照实验显示原作分布更宽，以实测分布修正（分母＝该实验全部帧）。
