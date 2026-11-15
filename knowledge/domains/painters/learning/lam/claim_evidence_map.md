<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-lam；原正文 SHA-256 `288f2932eda8cf307b4e5f010040cee4309ff6b2df961f228b979e5da4c509e8`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-lam — 论断→证据定位图（claim_evidence_map）

> 任务 `LEARN-lam` ｜ 仓库只读 @ `f008952365a77e140cbda3f3959d43ef000f9a22` ｜ 证据基线 `AUDIT-lam`（ACCEPTED，review verdict=accepted）。
> 覆盖对象：[learning_path.md](learning_path.md)（LP）、[how-to-think.md](how-to-think.md)（HT）、[mechanism_notes.md](mechanism_notes.md)（MN）、`RESULT.md`（RS）四份产物里的**每一条实质论断**。
> **复用 `AUDIT-lam` 的 locator 纪律，不重审、不新增史实考证、不改仓库。** 本 LEARN 新产物只有「操作序列/决策序/参数映射/失败条件」，不新增史实。
> 证据分级沿用档案 `:5`：`[史料]`/`[研究]`/`[归纳]`/`[推测]`/`[自述]`；§4/§8.2 阈值一律 `[归纳]` 未实测（`:203`、`:262`）。

<a id="db-source-line-8"></a>
## 0. 源文件缩写与 sha256（开工已 `sha256sum` 核对，全部匹配 ledger `artist-shards.json` / AUDIT-CM）

| 缩写 | 路径 | sha256 | 版本 |
|---|---|---|---|
| **DOSSIER** | [lam.md](../../dossiers/lam.md) | `76625f85a9be9aa5cb15d1db4c787f787705f0b30b860f1b18d538cebc198756` | `f008952…` |
| **CARD** | [lam.md](../../modules/lam.md) | `4be0af2680c8a5191ac621a0458dcac149513fe2d304e8c29ed50c0a0d713cf2` | 同上 |
| **CORPUS** | [lam.md](../../dossiers/_corpus/lam.md) | `450a59ed4820da0c53ceaea2bf22603fa0b311f264e0997f0093dbeee463df5a` | 同上 |
| **IMG-MANIFEST** | [manifest.md](../../dossiers/_images/manifest.md) | `5698124daf47c989fd26232a686ec54cda2658b623e1a302ddb5806ebf95b470` | 同上 |
| **CONFLICTS** | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | 同上 |
| **GOALS** | `ops/GOALS.md`（A-114 行 `:110`） | `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144` | 同上 |
| **AUDIT-CM** | 内部证据 7a0795fd9e7af97b（未公开；来源记录由维护者保留） | `b1e4ac207a3eefd62c014dbc3c466f03cede9734a4c45fb129aa89c58de1560e` | ACCEPTED |
| **AUDIT-CSV** | 内部证据 e6c421beaf054826（未公开；来源记录由维护者保留） | （71 行，LAM-S/S31/Q/X/G…） | ACCEPTED |
| **AUDIT-RESULT** | 内部证据 937b815f5d5b6b65（未公开；来源记录由维护者保留） | `6352c077694d83a64f329d24a8e0ed714935ddf26149f33ef7d94d500bf0383f` | ACCEPTED |
| **QUOTE-AUDIT** | 内部证据 52f041efc4d18805（未公开；来源记录由维护者保留） | `9ab31acb1e6a0b750f1a7397fb5e621bf40c0d5ad4bb26ca9c1ab070acb71137` | ACCEPTED |
| **RIGHTS** | 内部证据 c13f3f0ffc21b50e（未公开；来源记录由维护者保留） | `54aec17b5ffe8aeacd1a077458b45543e15ec0d779565a4ab85f7b1402a261de` | ACCEPTED |
| **COUNTEREX** | 内部证据 450e712d69b4f2bc（未公开；来源记录由维护者保留） | `8b460d9e17764c2b652697047b4d66dc76bd30b10032dff16c52e88f2139cf1b` | ACCEPTED |
| **DRIFT** | 内部证据 5662a5686ec83d00（未公开；来源记录由维护者保留） | `b6663275adee75529289698c67c7c125c65b50366fef761424da1b90604bd062` | ACCEPTED |
| **RISK** | 内部证据 e05ea8fbc8e0537c（未公开；来源记录由维护者保留） | `8969ba579de295eb9cb12bdd935b0141f7433e634cbc1d1f5756694b57064ab3` | ACCEPTED |
| **REVIEW-EV** | 内部证据 a9e8e5f38e15e8d6（未公开；来源记录由维护者保留） | `c3d0a387f38a5b4c13e10cbfbf68c59f244d0b27fa27e342627bbeb6da6916cf` | ACCEPTED |

> locator 写作 `文件:行号`，行号均为**冻结 head 实测值**（本轮 `grep -n` / `read` 核对）。
> **漂移注记（继承 AUDIT `DRIFT`，不修复）**：`CONFLICTS:16` 覆盖 11 位 wave3 画家、lam 不在其列；`DRIFT` 报告 12 项 conflicts.md 写死行号漂移（如对 caravaggio.md 的 +1、对 matisse/picasso 的 +5/+6）——本图引用 lam.md 一律用冻结实测行号，**不抄 conflicts.md 内旧 L 号**，也不把 lam 的 C 引用误读为 lam 专属行。

---

<a id="db-source-line-33"></a>
## 1. OVERTURNED / 馆藏错位（brief 强调 ②）— C1–C6

| # | 论断（出现在） | 证据级 | locator |
|---|---|---|---|
| C1 | 《La jungla》(The Jungle /《丛林》) 1942–43 **藏 MoMA 140.1945（Inter-American Fund）**，239.4×229.9 cm，油彩+炭笔/kraft 纸后裱画布 | `[史料]` | DOSSIER `:22` §0 关键作品表; AUDIT-CSV `LAM-S10-01`; AUDIT-RESULT §结论; RISK F2 |
| C2 | **MALBA 藏《La mañana verde》2003.35**（186.9×124 cm，Costantini 捐赠 2003）并展出《Omi Obini》；二者与《丛林》同为 1943「丛林期」姊妹作 | `[史料]` | DOSSIER `:23`, `:24`, `:253` §10-1; AUDIT-CSV `LAM-S10-01`; RISK F3 |
| C3 | 原 wave22 简报误记「MALBA《丛林》在藏」= **OVERTURNED、不可回退**；A-114 唯一 OVERTURNED | `[史料]`（AUDIT 已 supported） | DOSSIER `:253` §10-1; GOALS `:110` A-114; AUDIT-RESULT §结论; REVIEW-EV §(b) |
| C4 | 外部四源交叉：Wayback MoMA 对象页 `Inter-American Fund. 140.1945.` + `239.4 x 229.9 cm` + `© 2026 ARS/ADAGP`；MALBA 页 `2003.35`/`La mañana verde` 且 `La jungla(1942)` 仅作关联作品；Wikipedia infobox `The Jungle (1943), Museum of Modern Art collection`；MoMA 新闻稿 `decoloniz` | `[史料]` | RISK F2/F3/F4/F6; REVIEW-EV §(a)(b)(e) 6 个 raw sha; AUDIT-CM `external_fetches` / `overturned_claim` |
| C5 | MALBA 专文（Bernal）把《La mañana verde》读作甘蔗田 santería 仪式：带翼躯体＋马蹄＝被 orishá 骑乘、一颈两头 Elegguá/Ogún、供盘玉米水果、染红手持烟叶 | `[研究]` | DOSSIER `:153` §7-4; CARD（§0 来源）; AUDIT-CSV `LAM-S1-03` |
| C6 | 把《丛林》写成 MALBA / 把 `2003.35` 安到《丛林》= 事实层直接失败（练习/引用纪律） | LEARN 口径（继承 C1–C4） | LP §1.3/§6 失败 0/§8; HT 步 0; MN §3/§4; RS §4 |

---

<a id="db-source-line-46"></a>
## 2. 密度＋兽形机制（brief 强调 ①）— C7–C14

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C7 | 满幅丛林（无地平线）：甘蔗/竹/阔叶/果实构成密度极高单一空间，天与地平线被吃掉；主体从植被里「长出」 | `[研究]` | DOSSIER `:36` §1-2; CARD `:10`（浓缩第2条） |
| C8 | 密度量化：负空间 ≤15%、地平线=无、四边触边、秆 ≥8 根/画幅；§8.2-2 四边触边率 ≥90% | `[归纳]` 未实测 | DOSSIER `:36`, `:195` §8.2-2, `:99` P2 强档; CARD `:41`/`:56` |
| C9 | 竖向节律：秆/肢/颈构成多列竖线＋弧线对位，竖线族 ≥3 组、重心偏下，被读作「舞蹈/仪式进行时」 | `[研究]`+`[归纳]` | DOSSIER `:44` §1-10, `:201` §8.2-8; CARD `:10`, `:47` |
| C10 | 混种合体（人×动物×植物）：马首/鸟首、马蹄、爪形手、果实状乳房、植物茎干与人体无缝过渡（polymorphism）；每主体可拆 ≥2 类部件、拼贴接缝=0 | `[研究]` | DOSSIER `:35` §1-1; CARD `:9`; MoMA 对象页「handlike feet, elongated legs」DOSSIER `:150` §7-1 |
| C11 | 生长式而非拼贴式装配：部件取自人/马/鸟/蛇/植物/果实，以连续生长逻辑接合，禁字母/报纸/木纹类拼贴物 | `[自述]`+`[归纳]` | DOSSIER `:58` §2-7, `:69` §3-4, `:78` §3.1, `:194` §8.2-1; CORPUS `:25` #3 |
| C12 | 密度×兽形耦合 = 「场（甘蔗竖线载体）+ 场中物（从节律长出的混种主体）」；甘蔗＝奴隶制与榨取史符号、常作竖向节律载体 | `[归纳]` | DOSSIER `:40` §1-6, `:36` §1-2; MN §1 耦合段; LP §1.4 |
| C13 | P1 混种度默认 75% / P2 丛林密度默认 80%；P1/P2 ≥1 条 ≥ 中档 = 起步判据 | `[归纳]` | DOSSIER `:98`, `:99`, `:105`; CARD `:55`, `:56`, `:62` |
| C14 | 起步判据**必要非充分**：满幅密度强档＋解剖正常的人可满足起步，却在 §8.2 八条里 ≥4 条硬失败 | `[inference]`（AUDIT 纸面推演） | COUNTEREX 反例 1; DOSSIER `:105`; LP §3 起步注/§6 失败 1; HT 步 6; MN §1/§4 |

---

<a id="db-source-line-61"></a>
## 3. FR3 / ES3 / EN18 语料语言分层（brief 强调 ③）— C15–C20

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C15 | corpus 共 **24** 条逐字引文（`grep -c '^### '`），与 ledger `corpus_quotes:24`、dossier §0 一致；每条 = 原文（原语言保留）+ 来源 + 类型 + 中文意译（本项目意译，非逐字回译） | `[史料]` | CORPUS `:1-7` 卷首; QUOTE-AUDIT `:3-7`; AUDIT-CM `quote_count=24`; REVIEW-EV §(a) |
| C16 | 原语言分布 **FR 3（#1,#20,#21）/ ES 3（#5,#14,#15）/ EN 18（其余）**；3+3+18=24 | `[史料]` | QUOTE-AUDIT `:36-37`「语言/翻译统计」; REVIEW-EV §(a) 第 3 行; AUDIT-RESULT §验证 2 |
| C17 | 类型分布 `[self-spoken]` 19 / `[self-written]` 1 / `[contemporary record]` 3 / `[reception]` 2 = 24；#20–24 为转录/接受层、一手未回查 → partial | `[史料]` | QUOTE-AUDIT `:38-39`, `:30-34`, `:46-48`; AUDIT-RESULT §诚实边界 |
| C18 | 作者侧可用依据逐条标语言层：#1 木马 FR（Fouchet 1976 p.31）、#2 去殖民 EN（JSA p.3）、#3 回到自己的世界 EN 且点名 *In La Jungla*、#4 transculturación ES（Bernal 2006 p.185）、#8 剪刀/塞尚/合成 EN、#10 月亮 EN、#11 纸 EN、#17 方向 EN、#19 心理色 EN | `[自述]`（分层） | CORPUS `:10-11`, `:17-18`, `:24-25`, `:31-32`, `:68-69`, `:75-76`, `:82-83`, `:125-126`, `:139-140`; HT §0/步 1-5 |
| C19 | 未收清单（纪律）：Ocula「I am not interested in painting for painting's sake」原始文件未命中；Tate/官网转录层 3 条暂列未收；Breton 专文未直读一手 → **未采用** | `[史料]`（边界） | QUOTE-AUDIT `:41-44`; CORPUS `:185-189` 未收清单; DOSSIER `:258`, `:259`, `:263` §10-6/7/11 |
| C20 | 禁止把不同语言/年份/层的引语揉成无出处「他说」；#18（1980「不是种族而是阶级」）与去殖民轴并用时不得简化；Berger #23 为 `[reception]` 不作自述 | 项目口径 | CORPUS `:133-137` #18, `:169-174` #23; DOSSIER `:72` §3-7, `:125`; HT §0/§3 自查 2-3-6 |

---

<a id="db-source-line-74"></a>
## 4. 16 private images / 权利事实（brief 强调 ④）— C21–C24

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C21 | `images_public=0 / images_private=16`（作品图 8 + 照片/展厅图 6 + 同框图 2），**全部版权未清**、© SDO Estate / ADAGP / ARS；美国 life+70 → 2052 前受保护；公开侧零图是既定权利事实非缺陷 | `[史料]` | IMG-MANIFEST `:3229`, `:11`, `:3164`; DOSSIER `:9`, `:27`, `:261` §10-9; AUDIT-CM `images_public/images_private`; RIGHTS §结论 |
| C22 | 磁盘核对：`knowledge/domains/painters/dossiers/_images/lam/` 目录不存在；manifest 总表无 `| lam/` 公开图行；含 `Lamgods`/`gemaldegalerie` 字样者经核为 van_eyck/piero 的 Commons 文件名，非 lam | `[史料]` | RIGHTS §「逐公开图行」/§对照; AUDIT-RESULT §验证 6; REVIEW-EV §(c) |
| C23 | Wayback MoMA 对象页页脚 `© 2026 Artists Rights Society (ARS), New York / ADAGP, Paris` 外部旁证；16 张逐张 license/摄影者状态在公开 manifest 未披露 → **unknown 保持 unknown，不猜 PD/CC** | `[史料]`（边界） | RIGHTS §「unknown 保持 unknown」/§外部旁证; RISK F2; AUDIT-CM `external_fetches_detail` |
| C24 | 本 LEARN 因此**不使用任何图像文件、不引用 `_private/` 路径、不声称亲眼看原作、不做像素测量**；「看什么」只回读档案 §1/§7/§12 文字记录 | LEARN 口径 | LP 卷首权利事实/§8; HT §3 自查 7; MN §3/§6; RS §5 |

---

<a id="db-source-line-85"></a>
## 5. §4 参数 / §8.2 规则（LP §3/§5、MN §1/§2、HT 步 1-6）— C25–C40

| # | 论断 | locator |
|---|---|---|
| C25 | P1 混种度 弱/中/强 = 单一物种畸变 / 人+动物部件 / 人-动物-植物三元合体·多头·生长过渡；默认 75% | DOSSIER `:98`; CARD `:55` |
| C26 | P2 丛林密度 弱/中/强 = 留白天空地平线在场 / 植被围合局部天光 / 满幅无地平线负空间≤15%四边触边；默认 80% | DOSSIER `:99`; CARD `:56` |
| C27 | P3 暗域度 弱/中/强 = 亮色铺开(越界博斯/高更) / 暗绿-赭为主 / 黑-暗绿-棕+红橙闪点+月光夜色；默认 70% | DOSSIER `:100`; CARD `:57` |
| C28 | P4 仪式符号密度 弱/中/强 = 无 / ≥1 符号(月/供盘/烟叶/剪刀) / 神祇在场(orisha 可指名、被附体)；默认 50% | DOSSIER `:101`; CARD `:58` |
| C29 | P5 性征夸张 弱/中/强 = 自然比例 / 单部件夸张 / 多部件+雌雄同体(esteatopigia)；默认 45% | DOSSIER `:102`; CARD `:59` |
| C30 | P6 面具化 弱/中/强 = 具象脸 / 面具脸(类型化无个性) / 面具+非人首(马首/鸟首/无面)；默认 65% | DOSSIER `:103`; CARD `:60` |
| C31 | §4 用法：P1/P2 定身份起步、P3 氛围、P4 仪式档、P5/P6 身体-面部档；越界警报①–⑤（毕/博/高更·塔西拉/卢梭/里维拉） | DOSSIER `:105-106`; CARD `:62-63` |
| C32 | §8.2-1 混种：≥1 主体可拆 ≥2 类部件、拼贴接缝=0、马首/鸟首/爪形足模板命中 ≥1 | DOSSIER `:194`; CARD `:40` |
| C33 | §8.2-2 密度：负空间 ≤15%、地平线=无、四边触边 ≥90% | DOSSIER `:195`; CARD `:41` |
| C34 | §8.2-3 色域：主色相 ≤4、红橙 2–8%、S>0.6 ≤12%、平均明度 ≤0.45 | DOSSIER `:196`; CARD `:42` |
| C35 | §8.2-4 表面：露纸 5–20%、滴/溅连通域 ≥3、厚涂高光=0、显式「柔边薄涂/哑光」 | DOSSIER `:197`; CARD `:43` |
| C36 | §8.2-5 面具：面具脸 ≥1、P6 强档非人首 ≥1、面部类型化 | DOSSIER `:198`; CARD `:44` |
| C37 | §8.2-6 仪式符号：每帧 ≥1 符号、承担叙事、禁静物化陈列 | DOSSIER `:199`; CARD `:45` |
| C38 | §8.2-7 性征并置：≥1 夸张部件 ≥1.5×、雌雄可同体、「神圣而非色情」 | DOSSIER `:200`; CARD `:46` |
| C39 | §8.2-8 节律：竖线族 ≥3 组、弧竖交替、重心偏下 | DOSSIER `:201`; CARD `:47` |
| C40 | §8.2 阈值为 `[归纳]` 未实测、分母＝假想参考帧；1/2/3/4/6 条与 §3.1 分工判据同轴 | DOSSIER `:203` §8.2 末, `:262` §10-10; CARD `:49` |

---

<a id="db-source-line-108"></a>
## 6. 分工条款 / 组合预检 / 失败条件（LP §6、MN §3、HT「何时失效」）— C41–C50

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C41 | 第一写死条款 vs 毕加索：立体主义欧洲内部发明/原始主义为外部素材 vs 带回加勒比被神话充能；四判据（符号指向/形体构造/色彩/方向）、**≥2 轴联合尤其①④**、边界注（林 1938–39 毕式阶段、不得只看面具脸/几何感） | `[归纳]` 可推翻 | DOSSIER `:77-82`, `:81`, `:426` 自审 B1; CARD `:69` |
| C42 | 第二写死条款 vs 博斯：混种=道德编码讽喻机器 vs 仪式性在场；四判据（合体职能/场景组织/情绪距离/色与光）、**≥2 轴尤其①③**、「混种非独有、职能才是判据」 | `[归纳]` 可推翻 | DOSSIER `:83-88`, `:87`, `:427` 自审 B2; CARD `:70` |
| C43 | 组合纪律：选一个主导轴（70/30 起）、碎裂度轴不得双开、毕式拼贴物禁入林式画面、仪式符号不得降格静物；「怪诞」轴不得同帧折中 | `[归纳]` | DOSSIER `:82`, `:88` |
| C44 | 次级注记：不借高更塔希提装饰色/卡罗自传象征/里维拉壁画尺度/卢梭植物学细描（植物=符号非标本） | `[归纳]` | DOSSIER `:89`; CARD `:71` |
| C45 | 组合预检通用 C 轴：C-01 硬阴影（柔边薄涂/哑光）/C-05 笔触（薄涂渗化非厚涂）/C-06 饱和度（中低+小面积红橙）/C-12 色相面积（绿黑主导）/C-17 负空间（≤15%）/C-18（有机流动档） | `[归纳]` | DOSSIER `:89`, `:203`; CARD `:72` |
| C46 | **结构性漂移**：conflicts.md:16 扫描范围=11 位 wave3 画家、lam 不在其列；18 条 C + 11 条 near-miss 无 lam 行；lam 的 C 引用是通用轴指针非专属行（`LAM-S31-03` partial） | `[史料]`（AUDIT 报告） | DRIFT §「与 lam 直接相关的结构性漂移」; CONFLICTS `:16`, `:32-49`, `:347-357`; AUDIT-CM `conflicts_rows_checked=18` |
| C47 | 单轴假阳性反例：机械套「几何化/面具脸=越界毕加索」会把林 1938–39 自己也判越界；须把 §3.1「≥2 轴联合」回引 §4/§8.2 | `[inference]` | COUNTEREX 反例 2; DOSSIER `:81`, `:426` |
| C48 | 归纳阈值内部互斥反例：P3 弱档「亮色铺开」×§8.2-3「红橙 2–8%」字面不可同时满足；须声明豁免，非史实错误 | `[inference]` | COUNTEREX 反例 3; DOSSIER `:100`, `:196`, `:262` |
| C49 | Lane B 句式改写：「别做成：渐变」→「渐变仅限稀释油彩的渗化/擦痕，不得成平滑数码渐变」+ 显式「哑光/薄涂/纸底透出/无清漆」；「归还装置」= 两阶段状态机（取欧洲骨架→还符号入仪式语境） | `[归纳]` | DOSSIER `:190`, `:209-210` §8.3, `:145` §7-10; CARD `:72` |
| C50 | 12 项 conflicts.md 行号漂移只报告不修复；AUDIT 自身 71 条 locator 全部指向当前 HEAD 现场验证行，不受影响 | `[史料]`（AUDIT 报告） | DRIFT §逐条/§说明; AUDIT-RESULT §验证 3、§诚实边界; AUDIT-CM `conflicts_locator_drifts_recorded=12` |

---

<a id="db-source-line-125"></a>
## 7. 作品 / 练习来源（LP §2/§4、MN §1、HT 步 1-5）— C51–C60

| # | 论断 | locator |
|---|---|---|
| C51 | §0 关键作品表 5 件（含馆藏/URL：MoMA 34666 / MALBA 807 / MALBA 2756 / Rudman Trust / Capriles Cannizzaro） | DOSSIER `:22-26` |
| C52 | §7 深度分析 10 条逐条带 URL（MoMA 对象页/回顾展/语音导览/MALBA 专文/Reina Sofia/Gremels/Mosquera/Artsy） | DOSSIER `:148-159` |
| C53 | §12 临摹清单 10 件各含「看什么/学什么/怎么练」；组合练习建议 1/2/4 合体仪式、3/9/10 暗域母题、5 政治密度、6/7 线面、8 单部件替换 | DOSSIER `:357-411`, 组合建议 `:411` |
| C54 | 《La jungla》看/学/练：生长式合体、接缝不可见、满幅密度节律；3 版（写生→几何化→生长融合）、禁拼贴/禁地平线/禁亮色 | DOSSIER `:361-364` §12.1 |
| C55 | 《La mañana verde》一场仪式：1 主体+1 供物+≥2 符号、一处附体标记（马蹄/翼）、禁说明性手势 | DOSSIER `:366-369` §12.2 |
| C56 | 《Omi Obini》神祇名作题、暗调靠轮廓与微光；《Le Sombre Malembo》单主体纪念碑性、近方重心偏下 | DOSSIER `:371-379` §12.3/§12.4 |
| C57 | 《Horse-Headed Woman》只替换一个部位（马首）、≥3 遍稀释色、「是怪物还是存在」 | DOSSIER `:396-399` §12.8 |
| C58 | 《Grande Composition》4 张对开纸拼大画、3 母题循环 ≥2 次、稀薄透纸纹；《La Guerra Civil》无中心群像 ≥8 面具头/肢、土色+黑+白闪点 | DOSSIER `:401-404` §12.9, `:381-384` §12.5 |
| C59 | 《Fata Morgana》水墨自动书写 7 天连笔不断、每张只允许 2 处添加；《Mother and Child》去面部化、曲面/平面平衡 | DOSSIER `:391-394` §12.7, `:386-389` §12.6 |
| C60 | §2 技法：kraft 纸+稀释油彩+炭笔（`:57`）、马赛混种语汇成型（`:56`）、符号库学理 Ortiz/Cabrera/Carpentier/Eloísa（`:59`）、色法心理色（`:60`） | DOSSIER `:50-61` |

---

<a id="db-source-line-142"></a>
## 8. 口径 / 产物 / 验证类论断（RS、各卷首）— C61–C68

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C61 | 林飞龙无画论专著；`[自述]` 来自 24 条访谈/书信语料，两层声音（1940s 宣言 / 1950s–80s 回顾-校正）均非画论体系；prompt 从「作品可见机制+表述」反推 | `[史料]`/项目口径 | DOSSIER `:112`, `:125`, `:132`; AUDIT-RESULT §诚实边界 |
| C62 | §4/§8.2 量化阈值 `[归纳]` 未实测；练习为「建议练习」未经人评、不声称「已证实学习收益」 | 项目口径（A-30 §8.1） | DOSSIER `:203`, `:262`; 包 `01-AUDIT.md:269-273` §8.1; LP 卷首/§4/§8 |
| C63 | AUDIT-lam 状态 accepted、review verdict=accepted；71 条 claims（supported 50 / partial 12 / conflict 0 / unverified 9 = 71）；24 语料；6 次外部 fetch；3 个 `[inference]` counterexample | `[史料]`（收据） | AUDIT-CM `claims_total/per_status_counts/external_fetches/counterexample_attempts`; AUDIT-RESULT §验证 4-5; AUDIT `receipt.json` |
| C64 | 本 LEARN 无 repo 写入、无子代理（spawns_allowed=false）、无联网抓取、无凭据、无渲染/像素测量/视觉检查 | LEARN 口径 | RS §6/§7; 各文件「产物边界」 |
| C65 | 7-file 契约：RESULT.md / learning_path.md / how-to-think.md / mechanism_notes.md / claim_evidence_map.md / runner_receipt.json / receipt.json | 项目口径 | task-registry `LEARN-lam` 条目（`required_artifact_kinds`: result_summary/learning_path/mechanism_notes/claim_evidence_map）；wave-1 LEARN 实测 7 文件（LEARN-monet / LEARN-michelangelo） |
| C66 | 无 bound `LEARN-lam.contract.json`、无 `execution-inventory.json` → 收据 `status=submitted`、`execution_dedup_key=null`、`review=null`、`author_actor_id=null`（诚实，不伪造）；verify-receipt.py 对 submitted 仅做 schema 校验并返回 exit 0 | 项目口径 | 包 `tools/verify-receipt.py:20-21`; 内部工作区 内部证据 c33b8e9a20496b0c（未公开；来源记录由维护者保留）（仅 4 个 LEARN 契约，无 lam）; RS §7 |
| C67 | `profile_sha256` 与 `omp_version` 沿用 hy4free LEARN wave-1 约定（`147baa7b…` / `18.20.2`）；`observed_model`/`token_usage` 为 null（无工具输出暴露有效模型/可靠 usage） | 项目口径 | LEARN-caravaggio/cezanne/monet `receipt.json` model_route; RS §7 |
| C68 | 输入 8 哈希开工 `sha256sum` 逐一核对、全部等于 ledger `artist-shards.json` lam 条目与 AUDIT-CM `hashes` | `[史料]`（本轮核对） | RS §2; AUDIT-RESULT §验证 1; 本图 §0 表 |

---

<a id="db-source-line-157"></a>
## 9. 计数与一致性（可复算）

| 项 | 值 | 复算命令 / 来源 |
|---|---|---|
| 本图论断条数 | **68**（C1–C68） | 本文件表格行计数 |
| 覆盖产物 | 4（LP / HT / MN / RS） | 内部证据 d8eea759929c6889（未公开；来源记录由维护者保留） |
| brief 四项强调覆盖 | 4/4（§1 OVERTURNED / §2 密度+兽形 / §3 FR3·ES3·EN18 / §4 16 图） | 本图 §1–§4 + MN §5 落点表 + RS §4 |
| corpus 语料 / 语言分布 | 24 / FR3+ES3+EN18=24 | `grep -c '^### ' _corpus/lam.md`; QUOTE-AUDIT `:36-37` |
| §4 参数 / §8.2 规则 / §1 指纹 | 6 / 8 / 10 | DOSSIER `:98-103` / `:194-201` / `:35-44` |
| 输入 sha 全部匹配 | 8/8 | 本轮 `sha256sum` 开工核对；RS §2；AUDIT-RESULT §验证 1 |
| AUDIT claims / statuses | 71 / 50+12+0+9 | AUDIT-CM `claims_total` / `per_status_counts` |
| 公开图 / 私有图 | 0 / 16 | AUDIT-CM `images_public` / `images_private`; RIGHTS |
| 练习阶梯数 | 3（L1/L2/L3），每级 ≥4 步 | [learning_path.md](learning_path.md) §4 |
| AUDIT counterexample / drift / fetch | 3 `[inference]` / 12 报告 / 6 fetch | COUNTEREX / DRIFT / RISK / AUDIT-CM |

> **未在本图出现的仓库事实一律未写入四份产物**：例如生卒细节、拍卖纪录、陶艺批次、父亲生年两说、《La silla》现藏未核实、晚年细节——这些属 AUDIT 证据域，本 LEARN 不引用、不重审。
> **本图不主张**：不主张任何练习已验证、不主张组合已通过、不主张 §4/§8.2 阈值是原作实测、不主张 `[自述]` 超出 24 条分层语料、不主张亲眼看图、不主张 OVERTURNED 可回退。

---

<a id="db-source-line-177"></a>
## 10. 使用边界

- 本图是**定位索引**，不替代源文本；引用请回读对应 `文件:行号`。
- 证据级沿用档案 `:5`；AUDIT `DRIFT` 的 conflicts.md 旧 L 号与「lam 不在 11 位覆盖表」结论**只继承、只报告、不修复**。
- OVERTURNED 与 16 图权利事实为 AUDIT 已 supported 的继承值；处置权归集成/实验/权利 lane；本 LEARN 仅写 内部证据 c88e89d7660e4a36（未公开；来源记录由维护者保留），无 repo 写入、无子代理、无联网、无凭据。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
