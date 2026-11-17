<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-qi_baishi；原正文 SHA-256 `388800478a65d71d6932f9ec23ccc88f5938d18ed27fe97c7195e6672baf28f9`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-qi_baishi — 论断→证据定位图（claim_evidence_map）

> 任务 `LEARN-qi_baishi` ｜ 仓库只读 @ `f008952365a77e140cbda3f3959d43ef000f9a22` ｜ 证据基线 `AUDIT-qi_baishi`（**ACCEPTED**，`receipt.json` status=accepted、`review-gate-receipt.json` verdict=accepted/blocking_defects=0）。
> 覆盖对象：[learning_path.md](learning_path.md)（LP）、[how-to-think.md](how-to-think.md)（HT）、[mechanism_notes.md](mechanism_notes.md)（MN）、`RESULT.md`（RS）四份产物里的**每一条实质论断**。
> **复用 AUDIT 的 locator 纪律，不重审、不新增史实考证、不改仓库。** 本 LEARN 新产物只有「操作序列/决策序/参数映射/失败条件/权利边界译法」，不新增史实。
> 证据分级沿用档案 `:4-5`：`[自述]`/`[史料]`/`[研究]`/`[归纳]`/`[推测]` + corpus `[self-written]`/`[reported speech]`/`[contemporary record]`；§4/§8.2/conflicts 阈值一律 `[归纳]` 未实测（`rights_review.md:51` `image_seen=false`）。**`[推测]`=0**。

<a id="db-source-line-8"></a>
## 0. 源文件缩写与 sha256（开工 `sha256sum` 实跑，全部匹配 ledger `artist-shards.json:681-691` / AUDIT `RESULT.md §2`）

| 缩写 | 路径 | sha256 | 版本 / 状态 |
|---|---|---|---|
| **CARD** | [qi_baishi.md](../../modules/qi_baishi.md) | `b7a96e25abdaa783637a202b16d4f4da44e16891ce3f77132b1de334d276dd71` | `f008952…`（只读） |
| **DOSSIER** | [qi_baishi.md](../../dossiers/qi_baishi.md) | `ff773626b7d6736e6e86e73dbfc0d8f2552b67e457f7088dd6dc2af6b54a9d25` | 同上 |
| **CORPUS** | [qi_baishi.md](../../dossiers/_corpus/qi_baishi.md) | `d39e19680aa953eba42b25eef803d1068e0c3e089e29e3252d3aeaf16b900aa5` | 同上（25 条） |
| **CONFLICTS** | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | 同上 |
| **IMG-MANIFEST** | [manifest.md](../../dossiers/_images/manifest.md) | `5698124daf47c989fd26232a686ec54cda2658b623e1a302ddb5806ebf95b470` | 同上（L99–L109 公开 11 行） |
| **PMANIFEST** | [MANIFEST.md](../../dossiers/_images/qi_baishi/MANIFEST.md) | `b20bd35c1f708f8f495fd739125af39bc3d68e2e5777006113a47e4f37dc514a` | 同上（头「15」/尾注「11」漂移） |
| **INDEX** | [INDEX.md](../../dossiers/_corpus/INDEX.md) | `b74bf44fe2e9523f6f14f7171bce00bbc1729143a0634e4b5c789595e33c65b4` | 同上（L35 qi_baishi 25 条） |
| **GOALS** | `ops/GOALS.md` | `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144` | 同上（L41 A-27 / L72 A-66） |
| **LEDGER** | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留）（内部工作区） | `e1ec2d11…58ce9`（AUDIT RESULT §2 登记值） | 冻结副本在 AUDIT `inputs/` |
| **AUDIT-CM** | 内部证据 a6a6f5e0952e2a84（未公开；来源记录由维护者保留） | `57b0b0494f850000bcd502d61dd8ba850faebe630ebc0be3a22cd0a7864064e1` | ACCEPTED（本 lane 第 4 项输入哈希） |
| **AUDIT-MAP** | 内部证据 7ee4991675a7039e（未公开；来源记录由维护者保留） | `68b432fcbb3552ed438b9aab61f0da6b3ac6c28fb125b14c68536c345d4d90a1` | ACCEPTED（83 行） |
| **AUDIT-RIGHTS** | 内部证据 63ac8acba3114752（未公开；来源记录由维护者保留） | `ac59972db36502002e7c14cb08041b396123014e03bceb45f28d0fbbcce19a63` | ACCEPTED |
| **AUDIT-RESULT** | 内部证据 ee194226f7758975（未公开；来源记录由维护者保留） | `b93c2ab25945f58622c5db0ff9b9ad9bd2806938236248260afe44ccc60a05bf` | ACCEPTED |
| **AUDIT-RG** | 内部证据 35de1e7c6becb7b2（未公开；来源记录由维护者保留） | `c853e54dba18c38c64b44a810f8d129933ab7822f3cdf9150e5bfd6e5e1b4b6d` | verdict=accepted |
| **AUDIT-RECEIPT** | 内部证据 f299fd2688b8fd4e（未公开；来源记录由维护者保留） | `1232f75ec38efa2eccdabf6ffe3b311c96343fe4f722c35d2d96c9c35865e42c` | status=accepted |
| **内部工作区-01** | 包 `01-AUDIT.md` | `738d6a5a7dde17e444a594c1116da7322f2b0b127cc000c43c835f7f4e65aacf` | §8.1 A-30 `:269-273` |
| **内部工作区-00** | 包 `00-GOAL.md` | `3799710118a32d6aeaf2f2fdc9524f779ba4d1132318e1a7422413df44fbfa81` | L9 How to Think 红线 |

> locator 写作 `文件:行号`，行号均为**冻结 head 实测值**（本轮 `grep -n` / `read` 核对）。漂移注记（继承 AUDIT，不修复）：per-artist MANIFEST「公开 15」vs 尾注/目录「11」、near-miss「8 对」vs 11 行、C-17 正文未点名齐白石/八大——三者见 AUDIT `RESULT.md §8`，本图用实测行号 + 子串，不抄旧行号、不把漂移当结论。

---

<a id="db-source-line-34"></a>
## 1. 锚点「似与不似之间」（brief 强调②）— C1–C6

| # | 论断（出现在） | 证据级 | locator |
|---|---|---|---|
| C1 | `「作画妙在似与不似之间，太似为媚俗，不似为欺世」` = 齐白石《题〈枇杷〉》**自写题跋**，写意造型最高判据；本卡全部取舍的最高锚点 | `[自述]`/Q1 `[self-written]` | DOSSIER `:70`(§3-1)、`:140`(§5-1)；CORPUS `:10-14`(Q1)；LP 卷首锚点/§1 K3/§3 观察纪律/§8 B3；HT S1；MN §4/§9；RS §1 |
| C2 | 该句流行异文「作画在似与不似之间为妙…」两版并存，本卡以**北京画院版为正引**；A-27 引文抽查 5/5 第①条 `[HIT]`（scratch gitignored，按落盘自审 + GOALS 双证登记，本 LEARN 未重跑） | `[自述]`/机械验证 | CORPUS `:14`(Q1 备注)；DOSSIER `:420`(自审 C 段 `[HIT]`)、`:391/L426`(scratch 说明)；GOALS `:41`(A-27 5/5)；AUDIT-RESULT `§3`；AUDIT-MAP `:51`(QB-QUOTE-SPOT-1) |
| C3 | 造型停在「似与不似之间」的操作落点 = 减笔（虾减腿、蛙取稚拙、人物漫画化）；「略似」不倒向「不似（欺世）」、「毕真」不倒向「太似（媚俗）」 | `[自述]`(判据)+`[归纳]`(操作化) | DOSSIER `:46`(§1-7)、`:70`(§3-1)；CORPUS `:11`(Q1)、`:75`(Q11 三变「初只略似，一变毕真」)；LP §3 观察纪律/§4 阶梯一；HT S1/S2；MN §4 |
| C4 | Q12「探得虾游之变动，不犹专似其形」、Q17「写生我懒求形似」与锚点同一立场；但 **Q17 拍卖图录转引、原件未核**、**Q4「学我者生」原始题词未核** → 保留待核标记，不升级为一手 | `[self-written]`(Q12)+partial(Q17/Q4) | CORPUS `:80-84`(Q12)、`:110-114`(Q17)、`:28-32`(Q4)；DOSSIER `:278`(§10 学我者生待核)、`:284`(9.315 亿待核)；AUDIT-MAP `:59,72`(Q4/Q17=partial)；LP §1 K3/§6 F10；MN §4 待核段 |
| C5 | Q25「画吾自画自合古，何必低首求同群？」是**陈师曾赠句、非齐白石自述**（A-27 自审 B-2 OVERTURNED）；本卡不写成自述 | `[contemporary record]`/OVERTURNED | CORPUS `:164-168`(Q25)；DOSSIER `:395`(自审 B-2)、`:165`(§6.1 归属)；AUDIT-RESULT `§6-2`(联网核 Q25 归属)；LP §1 K7；HT §0/§4 |
| C6 | 「似与不似」参数化译成减笔/墨阶/邻接率 = 研究者 `[归纳]` 动作，不是齐白石说过「墨阶 ≥5 级」；不从画面推作者心理（`[推测]`=0） | 项目口径（`00-GOAL.md:9`） | 内部工作区-00 `:9`；DOSSIER `:4-5`(五级词表)、`:285`(未用 [推测])；LP §8 B2；HT §0/§4/§5；MN §9；RS §5 |

---

<a id="db-source-line-47"></a>
## 2. 虾蟹写意笔墨机制（brief 强调①）— C7–C16

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C7 | 画虾「三变」自述：「余之画虾已经数变，初只略似，一变毕真，再变色分深浅，此三变也」；异文「色分深淡」两版并存 | `[self-written]`(Q11)/`[自述]` | CORPUS `:74-78`(Q11)；DOSSIER `:57`(§2-3)、`:143`(§5-4)、`:269`(CC-2 异文)；MN §4 |
| C8 | 画蟹变法自述：「余之画蟹七十岁以后一变，此又变也」；变法不限一题，虾/蟹/雏「三绝」同出一辙 | `[self-written]`(Q14)/`[研究]` | CORPUS `:92-96`(Q14)；DOSSIER `:58`(§2-4)、`:49`(§1-10 三绝)；MN §4；LP §1 K2/§4 阶梯一 |
| C9 | 写生观自述：「家园有池多大虾…探得虾游之变动，不犹专似其形」——案头水盂蓄养活虾实际观察压过临摹 | `[self-written]`(Q12)/`[研究]` | CORPUS `:80-84`(Q12)；DOSSIER `:61`(§2-7)；MN §4 |
| C10 | 三变后**七改**（央视 R2）：头戟甲片参差（压扁笔锋）/虾眼圆点→横点/短须 6 根左右/腹部小脚笔尖回钩/群虾近浓远淡/远虾躯干只画三节/小脚 8→6→5 | `[研究]` | DOSSIER `:57`(§2-3)、`:188`(§7-4 R2)；AUDIT-RESULT `§6-1`(wiki 命中画虾相关)；MN §4；LP §1 K2/§3 M2 |
| C11 | 用水法：水破墨得水痕、墨破水得渍、飞白表现粗糙质感；「笔根淡、笔尖浓，一笔之中有浓淡」；「用笔如书法写字一般，落笔笃定，不作修饰」 | `[归纳]`(操作口径)+`[研究]`(R2) | DOSSIER `:56`(§2-2)、`:59`(§2-5)、`:45`(§1-6)；MN §4 |
| C12 | 虾体透明感 = 淡墨多层 + 留白、**不勾轮廓线**；墨分五色（焦浓重淡清）+ 水痕/渍墨/飞白为「水的体系」 | `[归纳]`(依据 R2/R10 作品) | DOSSIER `:43`(§1-4)；CARD `:11`(浓缩第3条)、`:65-66`(P3 中/强档「虾体分层/透明感优先，如虾身」)；MN §4；LP §1 K2/§3 M2/§4 阶梯一 |
| C13 | P3 墨阶数（默认 5 级，弱 2–3 / 中 5 级虾体分层 / 强 ≥7 级+水痕渍墨透明感优先）；§8.2-1 墨阶 ≥5 级、焦墨 2–15%、纯黑 ≤8% | `[归纳]` | DOSSIER `:114-117`(P3)、`:230`(§8.2-1)；CARD `:64-66`,`:42`；MN §1/§2；LP §3 M2/§4 阶梯一 |
| C14 | §8.2-7 水痕规则：渗化过渡带 2–8 px、硬边剪裁 ≤10%、干笔飞白 ≥5 条/100×100px（若声明飞白档） | `[归纳]` | DOSSIER `:236`(§8.2-7)；CARD `:48`；MN §2；LP §3 M2 |
| C15 | 练习落点：单虾分解临摹 5 遍（头/身/须/钳）、「墨阶数 vs 虾体分段」表；3 笔 1 蛙 ×10 标注似/不似；蟹变法前后并置 | `[归纳]`(建议练习) | DOSSIER `:354-361`(§12-2/§12-3 怎么练)；CORPUS `:92-96`(Q14)；LP §4 阶梯一；MN §3 M2 |
| C16 | 变法姿态自述：88 岁「其画笔可稍去旧样否？」(Q16)、「即饿死京华…从此决定大变」(Q3)；虾蟹「变法」同一姿态 | `[self-written]`/`[自述]` | CORPUS `:104-108`(Q16)、`:22-26`(Q3)；DOSSIER `:64`(§2-10)、`:142`(§5-3)、`:146`(§5-6)；HT S2/S7；MN §4 |

---

<a id="db-source-line-64"></a>
## 3. URAA 4 从严 + 2 存疑权利边界 carried（brief 强调③）— C17–C24

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C17 | 齐白石卒 1957 → 中国及多数伯尔尼公约国 2008-01-01 起 PD；**美国 URAA 逐件可能不同**；公开图只收明确 PD/开放素材，存疑进 `_private/` | `[史料]`（版权专则） | DOSSIER `:7`(§0 版权口径)、`:398`(自审 B-5 推算)；AUDIT-RIGHTS `:4`；LP 卷首权利边界；MN §6 |
| C18 | **4 件 URAA 从严移入 `_private/`**：`ink_shrimp` / `pine_eagle_and_couplet_1946` / `daiyu_buries_flowers_1950` / `leaves_and_insects`；三处同向证据（global manifest L3175 + pmanifest L79 尾注 + INVENTORY L13）；公开侧不再分发 | `[史料]`（主脑处置 2026-10-15） | DOSSIER `:281`(§10)；GOALS `:41`(A-27「4 件 URAA 从严移入 _private」)；AUDIT-RESULT `§5`；AUDIT-RIGHTS `:26-37`(§2 逐件表)；AUDIT-MAP `:88`(QB-URAA-4)；LP 卷首/§2/§8 B4；MN §6；HT S0 |
| C19 | **2 件原存疑**：`cicada`（400×594 低分辨率 + iclub-china 来源弱）/ `portrait_1956_zheng_jingkang`（1978《中国摄影》翻拍、权利链不清）；INVENTORY L8–L9；私有目录实测 6 `.jpg` = 4+2 | `[史料]` | AUDIT-RIGHTS `:39-44`(§3)、`:49`(§4 计数)；AUDIT-MAP `:89`(QB-URAA-PRIV)；DOSSIER `:7`(存疑 2 件)；LP 卷首/§8 B4；MN §6 |
| C20 | 公开 **11 张**逐张许可/署名/来源见 AUDIT `rights_review.md §1`（本机 manifest 字段，global L99–L109）；目录实测 11 = ledger `images_public=11` = L3175 = pmanifest 尾注 | `[史料]`（本机 manifest 字段） | AUDIT-RIGHTS `:8-24`(§1 11 行表)、`:48`(§4 计数)；IMG-MANIFEST(global L99–L109)；LEDGER `:690`(images_public=11)；GOALS `:41`(A-27「图库 11 张公开」)；AUDIT-MAP `:91`(QB-RIGHTS-11=partial)；LP §2/§8 B4；MN §6 |
| C21 | 联网抽样 1 件（`pine_eagle` / `File:Qi_Baishi_Eagle.jpg`）确认 Commons `Not-PD-US-URAA` 模板真实（PD-China×40 / Not-PD-US-URAA×30 / Uruguay Round Agreements Act / Category:Works copyrighted in the U.S.） | `[史料]`（AUDIT 联网取证，本 LEARN 未重访） | AUDIT-RESULT `§6-3`；AUDIT-RIGHTS `:33`；AUDIT-MAP `:94`(QB-WEB-3)；LP 卷首/§2；MN §6 |
| C22 | **unknown 保留**：首次发表地/版权持有人未逐张给出、10 张未逐张 imageinfo、像素未目检（`image_seen=false`）；美国逐件版权状态仍 unknown，本 LEARN 不做法律判定；本画家**不是 private-layer 型**（`images_public=11`，不套「公开 0 是事实而非缺陷」） | `[史料]`（字段边界）+`[归纳]`（操作纪律） | AUDIT-RIGHTS `:5-6,24,37,51`；AUDIT-RESULT `§5/§10`；LP 卷首/§6 F7/§8 B4；MN §6/§9；HT S0 |
| C23 | per-artist MANIFEST 头/总表标题「公开 15」+ 表内 15 行 vs 尾注「公开侧现 11」/目录 11 张 = **文本口径漂移**（表未同步删 4 行）；以目录实测 11 为准，登记不改仓库，交权利/RECOVERY lane | `[史料]`（AUDIT 报告） | AUDIT-RIGHTS `:50`；AUDIT-RESULT `§8.3`；AUDIT-MAP `:90`(QB-PMANIFEST-DRIFT=conflict)；PMANIFEST `:3/:8/:79`；LP §2/§6 F8/§8 B4；MN §6/§7 |
| C24 | 本 LEARN 因此**不引用 `_private/` 路径、不打开 4 URAA/2 存疑图、不猜 PD/CC、不目检像素、不做像素测量**；「看什么」只回读 AUDIT rights §1 文字记录 + 档案 §12 描述 | LEARN 口径（继承 C17–C23） | LP 卷首/§2/§4 阶梯三/§8 B4；HT S0/§3 第7/§4；MN §6/§9；RS §5 |

---

<a id="db-source-line-79"></a>
## 4. §4 参数 / §8.2 规则（LP §3、MN §1/§2、HT 各步）— C25–C40

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C25 | P1 红墨对比：默认 60%，弱纯红 ≤5% 近纯水墨 / 中 5–15% / 强 ≥15% 大红大黑对撞 | `[归纳]` | DOSSIER `:104-107`; CARD `:53-56` |
| C26 | P2 工写落差：默认 70%，弱全写意单一精度 / 中局部 1–2 草虫细度 1/5 / 强极细草虫 ≤1px × 极粗花叶双分辨率 | `[归纳]` | DOSSIER `:109-112`; CARD `:58-61` |
| C27 | P3 墨阶数：默认 5 级（见 C13） | `[归纳]` | DOSSIER `:114-117`; CARD `:64-66` |
| C28 | P4 留白率：默认 40%，弱 <15% / 中 15–35% / 强 ≥35% 主体一角 | `[归纳]` | DOSSIER `:119-122`; CARD `:68-71` |
| C29 | P5 民间色占比：默认 15%，弱 ≤5% / 中 5–20% / 强 ≥20% 多色并置仍以墨压阵 | `[归纳]` | DOSSIER `:124-127`; CARD `:73-76` |
| C30 | P6 金石笔性：默认 60%，弱流畅尖利 / 中中锋圆劲 / 强迟涩圆厚飞白如篆如刻（《祀三公山碑》） | `[归纳]` | DOSSIER `:129-132`; CARD `:78-81` |
| C31 | §4 用法：「P1/P2 定『是不是红花墨叶+工写』；P3/P4 定水墨气息；P5 定民间色档；P6 定金石质感」——**P1 是题材开关非全画种硬阈**（§5 反例的档案防线） | `[归纳]` | DOSSIER `:134`; CARD `:83`; AUDIT-RESULT `§7` |
| C32 | §8.2-1 墨阶：≥5 级、焦墨 2–15%、纯黑 ≤8% | `[归纳]` | DOSSIER `:230`; CARD `:42` |
| C33 | §8.2-2 红墨对比：纯红 3–15%（强 ≥15%）、红区边缘邻接墨黑/纸白 ≥60% | `[归纳]` | DOSSIER `:231`; CARD `:43` |
| C34 | §8.2-3 工写落差：最细 5% ≤2px / 最粗 5% ≥20px / 双峰比 ≥8×，或（无虫帧）宽度变异系数 ≥0.35 | `[归纳]` | DOSSIER `:232`; CARD `:44` |
| C35 | §8.2-4 留白：未涂布 ≥30%、主体包围盒 ≤55%、空白无均匀噪点 | `[归纳]` | DOSSIER `:233`; CARD `:45` |
| C36 | §8.2-5 民间色：高饱和 ≤20%、色相簇 ≤6、无荧光色 | `[归纳]` | DOSSIER `:234`; CARD `:46` |
| C37 | §8.2-6 线条：线宽 CV ≥0.25、无排线（≤2 条/cm²）、端点圆润 | `[归纳]` | DOSSIER `:235`; CARD `:47` |
| C38 | §8.2-7 水痕：渗化带 2–8px、硬边 ≤10%、飞白 ≥5 条/100×100px（见 C14） | `[归纳]` | DOSSIER `:236`; CARD `:48` |
| C39 | §8.2-8 构图款印：视觉质量差 ≥15%、题款+印章 ≥1 处 ≤8%、竖排中文短题无拉丁字母 | `[归纳]` | DOSSIER `:237`; CARD `:49` |
| C40 | §8.2 阈值为 `[归纳]` 未实测、分母 = 假想参考帧；[qi_baishi.md](../../modules/qi_baishi.md) §4/§8.2 与 dossier 逐字一致（`_extract.py --check` `[qi_baishi] §8.1 ok(1289c) · §8.2 ok(801c) · §4 ok(909c)` EXIT=0） | `[归纳]`/机械验证 | DOSSIER `:228-237`; CARD `:40-49,51-83`; AUDIT-RESULT `§1/§2`; AUDIT-MAP `:82`(QB-META-02) |

---

<a id="db-source-line-102"></a>
## 5. AUDIT 反例 / 适用域缺口（LP §4 阶梯二、§6 F2/F3；MN §5；HT S3/S4）— C41–C44

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C41 | **反例 1**：纯水墨《墨虾图》《鸣蛙》纯红面积 = 0%、民间色 = 0%、无红区 → §8.2-2「红墨绑定 ≥60%」在空集上**分母为 0、不可计算**；若当全集必要判据会误判二者「非齐白石」（与 §0 首批 10 件/§12 代表作矛盾） | `[inference]`（AUDIT 纸面推演） | AUDIT-RESULT `§7`; DOSSIER `:25-26,134,224,354-361`; CORPUS `:75,81`; LP §4 阶梯二边界/§6 F2; MN §5 R1; HT S3 |
| C42 | 档案内防线：§4 用法把 P1 定为题材开关（C31）、§8.1 中文说明「纯水墨花鸟 → P1 弱、P5 弱」预留弱档、§8.2-3 无虫帧替代判据；**但 §8.2-2 未写「无红帧跳过」豁免** → 规则可判定性缺口，非事实错误 | `[归纳]`/`[inference]` | DOSSIER `:134,:224,:232`; AUDIT-RESULT `§7`; LP §4/§6 F2; MN §5; HT S3 |
| C43 | **反例 2**：§3 L83「红 = 永远与墨绑定」用「永远」全称量词；朱砂印章（多印并置、款印 ≥1 处）压在纸白/题款旁、不邻接墨叶 → 字面「一切红像素」不成立，判据应限定「花头红」 | `[inference]` | DOSSIER `:83,:48,:237`; AUDIT-RESULT `§7`; LP §6 F3; MN §5 R2; HT S4 |
| C44 | 两反例**只继承登记、不改仓库、不改 228/228 逐字契约**（改一处破坏 `_extract.py --check`），处置权归 RULE lane；本 LEARN 练习层显式声明「适用域=设色帧」+ 纯水墨帧以 P1/P5 弱档 + 墨阶/留白/工写落差接管 | 项目口径 | AUDIT-RESULT `§7/§10`; AUDIT-MAP（QB 元行）; LP §4/§7/§8 B5; MN §5/§9; HT S3/S4; RS §6 |

---

<a id="db-source-line-113"></a>
## 6. 分工条款 / 组合预检 / 冲突行（LP §1 K5、§6、MN §7、HT §3）— C45–C52

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C45 | vs 马蒂斯 **3 互斥轴**：①表面系统平涂色块 vs 水墨（N4 不可拆二选一）②红的使用大面平涂 vs 花头点缀永远与墨绑定（N3 红轴单主）③双分辨率工写并置齐独有、组合归齐 | `[归纳]`（写死 2026-10-15） | DOSSIER `:81-84`; CARD `:89-91`; AUDIT-MAP `:46-48`(QB-DIV-M1/M2/M3 supported); LP §1 K5/§4 阶梯三; MN §7; HT §3 第2 |
| C46 | vs 八大**两档互斥**：齐=热烈/生机/色彩 vs 八大=冷峻/极简；温度/繁简/色彩/情绪四判据；色彩轴归齐、极简减笔轴归八大（N3）；负空间 ≥30% 同侧 | `[归纳]` | DOSSIER `:87-92`; CARD `:91`; AUDIT-MAP `:49`; LP §6 F6; MN §7; HT §3 第3 |
| C47 | vs 徐渭**两档互斥**：齐=民间趣味/生机 vs 徐=文人狂态/泄愤，**历史影响链非风格同化**；色彩轴归齐、爆发/湿墨轴归徐、70/30 起；对侧 `xu_wei.md §3.1` 已对齐 | `[归纳]` | DOSSIER `:94-96`; GOALS `:98`(A-102 徐渭分工); AUDIT-MAP `:50`; MN §7; HT §3 第4 |
| C48 | **C-17 负空间**：齐 ≥30% 与八大 ≥60%/北斋 ≥35%/马蒂斯 ≥20% 同侧（取交集显式取值）；与米开朗基罗 ≤15% 按 N4 二选一；「空白背景」与「负空间」是否同量先统一口径 | `[归纳]` | CONFLICTS `:48`(总表)/`:272-283`(详条，含 `:279` 口径问题)/`:314`(N4); CARD `:92`; AUDIT-MAP `:86`; LP §1 K5/§3 M5/§6 F6; MN §7; HT §3 第5 |
| C49 | N 规则：N1 反约束一致性 / N3 轴所有权表 / N4 可拆判别 / N9 无双标准；组合前先判轴不先调强度，§8.2 是判分规则非强度旋钮，冲突轴辅模块规则整条移除 | `[归纳]` | CONFLICTS `:305,:311-313,:314-315,:332-333`; CARD `:87`; LP §4 阶梯三; MN §8; HT §3 第1/第6 |
| C50 | near-miss 计数漂移：module 卡「8 对」vs conflicts §4 现 11 编号行（#9–#11 2026-10-16 补）= **conflict 登记不改仓库**，交 CONFLICT/RULE lane | `[史料]`（AUDIT 报告） | CARD `:98`; CONFLICTS `:341-357`(:357 补行); AUDIT-RESULT `§8.1`; AUDIT-MAP `:87`(QB-NM-DRIFT=conflict); MN §7 |
| C51 | C-17 正文（`:272-283`）未点名齐白石/八大，但 §3 L92/模块卡纳入其同侧口径 = 范围漂移，交 CONFLICT-17 写手 | `[史料]`（AUDIT 报告） | CONFLICTS `:272-283`; DOSSIER `:92`; CARD `:92`; AUDIT-RESULT `§8.2`; AUDIT-MAP `:107`; MN §7 |
| C52 | 组合实验/规则层判定 ≠ 实验验证；分工条款=规则层 `[归纳]` 互斥，不写「已验证可组合」 | 项目口径 | AUDIT-RESULT `§5/§10`; CONFLICTS `:303`(采纳状态，待 A-12 验证); LP §8 B5; MN §9; HT §3 卷首 |

---

<a id="db-source-line-128"></a>
## 7. 作品 / 练习 / 来源（LP §2/§4、MN §3、HT 各步）— C53–C60

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C53 | §0 关键作品表 10 件（牵牛花 1950 赛努奇 / 墨虾图 c.1947 浙博 / 鸣蛙 ≤1955 中国美术馆 / 十二山水屏 1925 / 松柏高立 1946 / 工虫册页 1949 等，各带馆藏/URL） | `[史料]` | DOSSIER `:21-32`; LP §2 |
| C54 | §12 临摹清单 9 件各含「看什么/学什么/怎么练」；阶梯一取 §12-2/§12-3、阶梯二取 §12-1/§12-8、阶梯三取 §12-4/§12-6/§12-7 | `[史料]`+`[归纳]`(练习映射) | DOSSIER `:348-385`; LP §2/§4; MN §3 |
| C55 | 生成后自查四项：①红区是否与墨绑定（邻接率）②是否有双分辨率 ③空白 ≥30% ④有无渐变/3D 泄漏 | `[归纳]` | DOSSIER `:226`; CARD(§8.1 中文说明); MN §8; LP §5 |
| C56 | §8.1 负向段禁：油画厚涂/画布纹/西方线性透视/平滑数码渐变/喷枪/3D/HDR/平涂矢量色块/硬剪纸边/金箔/霓虹/明暗对照/硬投影/对称/等宽机械线/排线/辉光 | `[归纳]` | DOSSIER `:214-221`; CARD `:31-38`; HT S2 失效条件; LP §6 F1 |
| C57 | dossier §9 参考表 R1–R17（R2 央视画虾、R3 澎湃变法、R6 故宫、R9 Google Arts、R10 Commons、R15 archive.org 借阅制、R16 502、R17 未直读等）；可达性 = 2026-10-15 本机实测，**本 LEARN 未重访** | `[史料]`（沿用 AUDIT） | DOSSIER `:245-266`; AUDIT-RESULT `§6`(3 次 fetch 为上游行为); LP §2/§8 B6; MN §9 |
| C58 | corpus 25 条类型分布 `[self-written]` 21 / `[reported speech]` 2（Q4/Q9）/ `[contemporary record]` 2（Q24/Q25）；中文原文无英译；转录/转引/异文在 L5–L6 + 逐条备注标注 | `[史料]`（AUDIT 机械验证） | CORPUS `:1-6,8-168`; INDEX `:35`(qi_baishi 25 条); AUDIT-RESULT `§3`; AUDIT-MAP `:81,83`; LP §1 K7; HT §0 |
| C59 | A-27 自审 B 段 5 条反驳：①红花墨叶双源 CONFIRMED ②「画吾自画自合古」OVERTURNED ③「学我者生」WEAKENED ④「色分深淡」WEAKENED ⑤卒年/PD CONFIRMED | `[史料]`（落盘自审记录） | DOSSIER `:393-398`; AUDIT-RESULT `§3/§6-2`; HT §0/§4; LP §1 K7 |
| C60 | 9.315 亿成交价 / Q4 原始题词 / Q17 原件 / 1950 年代正式发言文本 = 档案已自标 `[待核]`/`未核到`，Wikipedia 为二手佐证不升级 | `[史料]`（待核） | DOSSIER `:278,:284`; CORPUS `:170-177`(缺口); AUDIT-RESULT `§10`; LP §6 F10; MN §4 |

---

<a id="db-source-line-143"></a>
## 8. 口径 / 产物 / 验证类论断（RS、各卷首）— C61–C68

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C61 | 本 LEARN 证据底座 = 4 项输入哈希（card/dossier/corpus/AUDIT-CM），开工 `sha256sum` 实跑全部匹配 ledger `:681-691` + AUDIT `RESULT.md §2`；[qi_baishi.md](../../modules/qi_baishi.md) §4/§8.2 逐字一致 | `[史料]`（本轮核对） | LEDGER `:681-691`; AUDIT-RESULT `§1/§2`; AUDIT-MAP `:81`; 本图 §0 表; RS §2 |
| C62 | AUDIT-qi_baishi = **ACCEPTED**（status=accepted / verdict=accepted / blocking_defects=0）；83 行 claim map（supported 78 / partial 3 / conflict 2 = 83）；25 语料；3 次联网 fetch；11 公开 / 6 私有 | `[史料]`（收据） | AUDIT-RECEIPT `:6`; AUDIT-RG `:64`(verdict); AUDIT-CM(claims_total/per_status_counts/images_public/external_fetches); AUDIT-RESULT `§2/§5/§6/§11`; RS §2/§3 |
| C63 | 7-file 契约：`RESULT.md` / [learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md) / [claim_evidence_map.md](claim_evidence_map.md) / `runner_receipt.json` / `receipt.json`；`required_artifact_kinds` = result_summary/learning_path/mechanism_notes/claim_evidence_map，how_to_think 为模板 #2 追加 | 项目口径 | task-registry `LEARN-qi_baishi`(`:3589-3611`); tasks-plan.json `:7449-7454`; wave-1 LEARN 实测（LEARN-monet / LEARN-hogarth 7 文件）; RS §3 |
| C64 | A-30 §8.1 形状 = 八节（前置知识/重点作品及来源/要观察的机制/具体练习/可观察结果/常见失败/下一步/使用边界）；练习须标**建议练习**、不写「已证实学习收益」（`01-AUDIT.md:273`）；本卡 3 阶梯全标建议练习 | 项目口径 | 内部工作区-01 `:269-273`; LP 卷首/§4/§8 B1; RS §1/§5 |
| C65 | How to Think 必须区分作者可核实的自述与研究者推断、不能编造作者心理（`00-GOAL.md:9`）；本卡严格分栏、`[推测]`=0、决策序 S0–S7 每步带等级 | 项目口径 | 内部工作区-00 `:9`; DOSSIER `:4-5,:285`; HT §0/§1/§5; RS §5 |
| C66 | 无 bound `LEARN-qi_baishi.contract.json`、无 `execution-inventory.json` → 收据 `status=submitted`、`execution_dedup_key=null`、`review=null`、`human_review=not_applicable`、`author_actor_id=LearnQiBaishi`（诚实，不伪造）；`verify-receipt.py` 对 submitted 仅做 schema 校验并返回 exit 0 | 项目口径 | 包 `tools/verify-receipt.py:20-21`; 内部工作区 内部证据 c33b8e9a20496b0c（未公开；来源记录由维护者保留）(仅 AUDIT 契约，无 LEARN-qi_baishi); RS §7 |
| C67 | `profile_sha256` / `omp_version` 沿用 hy4free LEARN wave-1 约定（`147baa7b…` / `18.20.2`）；`observed_model`/`token_usage` 为 null（无工具输出暴露有效模型/可靠 usage）；`requested_model=buddyfarm/hy4free` | 项目口径 | LEARN-monet/caravaggio `receipt.json` model_route; AUDIT-qi_baishi `receipt.json:60-61`; RS §7 |
| C68 | 本 LEARN 无 repo 写入、无子代理（spawns_allowed=false）、无联网抓取、无凭据、无渲染/像素测量/视觉检查；外部 URL 未重访、11 公开图未目检 | LEARN 口径 | RS §2/§6/§7; 各文件「产物边界」; `receipt.json` allowed_write_paths/spawns_allowed |

---

<a id="db-source-line-158"></a>
## 9. 计数与一致性（可复算）

| 项 | 值 | 复算命令 / 来源 |
|---|---|---|
| 本图论断条数 | **68**（C1–C68） | 本文件表格行计数 |
| 覆盖产物 | 4（LP / HT / MN / RS） | 内部证据 14f2ce0817760e5e（未公开；来源记录由维护者保留） |
| brief 四项强调覆盖 | 4/4（§1 锚点 / §2 虾蟹 / §3 权利 11 公开+4 从严+2 存疑 / §4 参数规则） | 本图 §1–§4 + LP 卷首/§3/§4/§8 + HT S0–S7 + MN §4/§5/§6 + RS §1 |
| corpus 语料 / 类型分布 | 25 / 21+2+2 | `grep -c '^### ' _corpus/qi_baishi.md`; AUDIT-RESULT `§3`; INDEX `:35` |
| §4 参数 / §8.2 规则 / §1 指纹 / §12 清单 | 6 / 8 / 10 / 9 | DOSSIER `:102-134` / `:228-237` / `:38-49` / `:348-385` |
| 输入 sha 匹配 | 4/4（+7 项次要 locator 全匹配） | 本轮 `sha256sum` 开工核对；RS §2；AUDIT-RESULT `§2`；本图 §0 表 |
| AUDIT claims / statuses | 83 / 78+3+2 | AUDIT-CM `claims_total` / `per_status_counts`; AUDIT-MAP `:96-101` |
| 公开图 / 私有图 / URAA 从严 / 存疑 | 11 / 6 / 4 / 2 | AUDIT-RIGHTS `:48-49`; LEDGER `:690`; GOALS `:41`; AUDIT-MAP `:88-89` |
| 权利 unknown / image_seen | 美国逐件=unknown / 像素目检=false | AUDIT-RIGHTS `:24,:37,:51`; AUDIT-RESULT `§10` |
| 练习阶梯数 / 决策步 | 3（L1 虾蟹 / L2 红墨+工写 / L3 留白金石+边界）/ 8（S0–S7） | LP §4; HT §1 |
| AUDIT 反例 / 漂移登记 / 联网 fetch | 2 `[inference]` / 3 项（near-miss / C-17 范围 / MANIFEST 15vs11）/ 3（上游） | AUDIT-RESULT `§7/§8/§6`; MN §5/§7; RS §6 |
| `[推测]` 计数 | **0** | HT §5 汇总表；DOSSIER `:285` |
| 7-file 契约 | 7（5 内容 + runner_receipt + receipt） | C63; 内部证据 e4b268c5d5b51fe7（未公开；来源记录由维护者保留） |

> **未在本图出现的仓库事实一律未写入四份产物**：例如生卒细节全表、五出五归逐站、胡适年谱、拍卖纪录、印章近三百方考、和平奖/人大代表年表——这些属 AUDIT/档案证据域，本 LEARN 不引用、不重审、不新增史实。
> **本图不主张**：不主张任何练习已验证、不主张组合已通过、不主张 §4/§8.2 阈值是原作实测、不主张 `[自述]` 超出 25 条分层语料、不主张亲眼看图、不主张 4 URAA/2 存疑可公开分发、不主张美国逐件版权状态已判定、不主张 `submitted=accepted`、不主张 OVERTURNED 可回退。

---

<a id="db-source-line-181"></a>
## 10. 使用边界

- 本图是**定位索引**，不替代源文本；引用请回读对应 `文件:行号`。
- 证据级沿用档案 `:4-5`；AUDIT 的 near-miss/MANIFEST/C-17 漂移、2 个反例、权利 unknown 结论**只继承、只报告、不修复**（处置权归 RULE/CONFLICT/权利/RECOVERY lane）。
- 4 项输入哈希与 AUDIT ACCEPTED 状态为继承值；本 LEARN 仅写 内部证据 6e7a62d2efb0b514（未公开；来源记录由维护者保留），无 repo 写入、无子代理、无联网、无凭据、`image_seen=false`。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
