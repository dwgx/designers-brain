<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-hogarth；原正文 SHA-256 `3710fe6bc0a0c6757041f8e9f56ace81b29ca65f77b17b9fd0831158e302d65f`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-hogarth — claim / evidence 图（逐 claim 带定位）

> 给 `RESULT.md` / [learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md) 里**每一条实质 claim** 配 `文件 : 节 : 行号` 定位（dossier / corpus / 卡 / conflicts / goya / AUDIT 产物）。沿用 ACCEPTED 内部证据 4e85de3bb67b5cd9（未公开；来源记录由维护者保留）（77 行）的 locator 纪律，**不重审**。
> 基线 `f008952365a77e140cbda3f3959d43ef000f9a22`（repo READ-ONLY）。等级照录 [hogarth.md](../../dossiers/hogarth.md) L5：`[自述]/[史料]/[研究]/[归纳]/[推测]`。
> **support_status 只评「本机档案内自洽 / 定位可寻址 / 类型正确」**，不评外部原文真伪、不评学习成效（AUDIT 同口径）。外部语料真伪 / license truth 留 `unverified`（AUDIT RESULT §8）。
> 输入 hash（开工实测，见 `RESULT.md` §0）：card `b76354c1…25ea8`、dossier `b9509997…5ca3c`、corpus `dc513ae8…48ce`、conflicts `314a24da…abef`、goya `a50f0d27…ee73`、AUDIT RESULT `a514f000…5f760`、AUDIT counterexample `29ec7a4a…35c1`、AUDIT claim map `0f127bea…1194`、AUDIT coverage `9d29b0af…0d04c`、AUDIT rights `d86af208…b2369`。

---

<a id="db-source-line-10"></a>
## §A 证据分级 / 口径（how-to-think §0/§2、RESULT §3）

| claim_id | 内容 | 等级 | 定位 | 来源文件 |
|---|---|---|---|---|
| LH-GRADE-DEF | 证据级定义；`[归纳]`=本项目操作规则、不冒充艺术家内心 | 口径 | [hogarth.md](../../dossiers/hogarth.md) L5 | dossier |
| LH-THRESH-INDUCTION | 全部 §8.2 阈值 `[归纳]`、未对原作做像素测量（分母＝假想参考帧）；档位划分本身 `[归纳]` | 口径 | [hogarth.md](../../dossiers/hogarth.md) L243；[hogarth.md](../../modules/hogarth.md) L49；`conflicts.md` §5.D L420 | dossier + 卡 + conflicts |
| LH-NO-MIND | 禁止从画面外观反推作者心理、禁止把 `[归纳]` 写成「荷加斯主张」 | project rule | `00-GOAL.md` L9；[hogarth.md](../../dossiers/hogarth.md) L5/L243；AUDIT caveat | GOAL + dossier + AUDIT |
| LH-PRACTICE-SUGGESTED | 练习效果尚未由人完成或评价 → 全部为建议练习，不写「已证实学习收益」 | project rule | `01-AUDIT.md` §8.1 L273；本 shard `human_review.status=not_applicable` | 01-AUDIT + receipt |
| LH-A30 | A-30 = 76 位画家学习路径与总路线；本 shard 为 hogarth 一片 | `[史料]`（本机记录） | `01-AUDIT.md` L72；`03-RESEARCH-AGENDA.md` R1 L114–131 | 包文件 |

---

<a id="db-source-line-22"></a>
## §B S 曲线 / line-of-beauty（brief 强调点；learning_path §3-M0/阶梯1、how-to-think D0、mechanism §A）

| claim_id | 内容（含原文要点） | 等级 | 定位 | 来源文件 |
|---|---|---|---|---|
| **LH-LINE-22** | 「波状线 waving line…称它为『美的线』the line of beauty」——形式论主变量 | `[自述]` | [hogarth.md](../../dossiers/_corpus/hogarth.md) #22 L168–173（原文逐字 + `en->zh`）；AUDIT claim `HG-CORP-22` | corpus |
| **LH-LINE-23** | 「蛇形线 serpentine line 同时朝不同方向起伏缠绕，牵引眼睛…精确的蛇形线，或『优雅的线』line of grace」——细金属丝绕锥体 | `[自述]` | [hogarth.md](../../dossiers/_corpus/hogarth.md) #23 L175–180；AUDIT claim `HG-CORP-23` | corpus |
| LH-LINE-20-21 | 多样（Variety）为普遍快感之源 / 「有组织的多样」——S 曲线前置概念 | `[自述]` | [hogarth.md](../../dossiers/_corpus/hogarth.md) #20 L154、#21 L161 | corpus |
| LH-LINE-BOOK | 《美的分析》1753 出版（line of beauty 论）；底本 Gutenberg #51459 | `[史料]` | [hogarth.md](../../dossiers/hogarth.md) §11 L355、§9 R19 L277；`AUDIT-hogarth/RESULT.md` §4（联网复核 line of beauty×7 / line of grace×5）；claim `HG-R19-01` | dossier + AUDIT |
| LH-LINE-EX-7 | 图版 1 = 「S 形曲线的可视化教具」；学「形式分析工具（线条作为造型主变量）」；练「标 ≥5 处实例 + 3 件日常物各画最优 S 线」 | `[归纳]`（学习设计） | [hogarth.md](../../dossiers/hogarth.md) §12 #7 L411–414 | dossier |
| **LH-LINE-NOT-GATE** | S 曲线**不是**「是不是荷加斯」画面门：§8.2 八规则/§4 六参数无 S 曲线阈值；§8.1 负向排除 `idealised beauty / decorative abstraction` | `[归纳]`（观察判定） | [hogarth.md](../../modules/hogarth.md) §8.1 L32/L34；§8.2 全 L40–47；§4 全 L53–60；[hogarth.md](../../dossiers/hogarth.md) L114（P2/P3 定是不是荷加斯） | 卡 + dossier |
| LH-LINE-PRINT | print variant 同源线刻 `bold confident line, cross-hatching for shadow`（与 §C 相接） | `[归纳]` prompt | [hogarth.md](../../modules/hogarth.md) §8.1 正向 L28；[hogarth.md](../../dossiers/hogarth.md) L218 | 卡 + dossier |

---

<a id="db-source-line-36"></a>
## §C 连环画叙事序列机制（brief 强调点；learning_path §3-M1/阶梯2、how-to-think D1/D3、mechanism §B/§B.1）

| claim_id | 内容 | 等级 | 定位 | 来源文件 |
|---|---|---|---|---|
| **LH-SEQ-1** | 系列＝叙事单位（6/8/12 帧成套）；同一主角跨帧推进；完整道德弧必须按序读 | `[自述]` + `[研究]` | [hogarth.md](../../dossiers/hogarth.md) §1-1 L35（corpus #1 "field not broken up" + [R1]）；[hogarth.md](../../modules/hogarth.md) L9；AUDIT claim `HG-S1-01` | dossier + 卡 |
| LH-SEQ-STAGE | 「我的画就是我的舞台（dumb show）」；画＝舞台、人＝演员 | `[自述]` | [hogarth.md](../../dossiers/hogarth.md) §3-1 L69、§1-2 L36；corpus #2/#3；claim `HG-S3-01` | dossier + corpus |
| **LH-SEQ-CRITERION** | 判据＝**「帧间是否存在进度依赖」**；角色复用 ≠ 连续叙事（Willie Gillis 式各帧自足归单帧档） | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) §3.1 L91（复现角色测试）、L89–90（四轴） | dossier |
| LH-SEQ-STORYBOARD | 系列＝分镜板（8 帧＝8 场，每场「标题＋一行」）；Alan Parker「分镜祖先」经 Wikipedia 转引 Observer 2000（原刊未回查） | `[史料-转引]` | [hogarth.md](../../dossiers/hogarth.md) §3.1 L95；§10-5 降级；AUDIT claim `HG-STORYBOARD-01`（`partial`）；`AUDIT-hogarth/RESULT.md` §4 | dossier + AUDIT |
| LH-SEQ-3OPS | 可操作三条：系列骨架 / 帧间连续性进度表 / 顺序与放行（关键帧先行） | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) §3.1 L98；[hogarth.md](../../modules/hogarth.md) L72（Lane B 接口） | dossier + 卡 |
| LH-SEQ-RULE2 | §8.2-2：帧数 ≥6、可追踪元素每帧 100%、≥2 次状态变化（工作流） | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) L235；[hogarth.md](../../modules/hogarth.md) L41；AUDIT claim `HG-S4-01`（P1 `partial`） | dossier + 卡 |
| LH-SEQ-P1 | P1 系列化强度默认 **8**；弱档「小系列 3–6 帧（成对/三段）」；工作流参数不进画面重叠计算 | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) §4 L107、L114；[hogarth.md](../../modules/hogarth.md) L55、L62 | dossier + 卡 |
| LH-SEQ-P6 | P6 角色复用度默认「系列内复用（服装状态推进）」 | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) §4 L112；[hogarth.md](../../modules/hogarth.md) L60 | dossier + 卡 |
| LH-SEQ-PROMPT | `[series variant] a numbered progress: the same protagonist across frames, costume and props declining`；负向禁 `single-frame isolation when a series is requested` | `[归纳]` prompt | [hogarth.md](../../modules/hogarth.md) §8.1 正向 L27 / 负向 L35 | 卡 |
| LH-SEQ-EX-1 | 《浪子历程》8 帧：看服装/道具进度、Sarah Young 跨帧复现；练 8 行分镜表 + 抽帧复述测试 | `[归纳]`（学习设计） | [hogarth.md](../../dossiers/hogarth.md) §12 #1 L381–384 | dossier |
| LH-SEQ-EX-4 | 《浪女历程》1–3 帧：progress「相遇→沦落→毁灭」；练 6 格当代 progress 大纲 | `[归纳]`（学习设计） | [hogarth.md](../../dossiers/hogarth.md) §12 #4 L396–399 | dossier |

---

<a id="db-source-line-54"></a>
## §D 对位 / 单帧多线索 / 参数门（learning_path §3-M2/阶梯3、how-to-think D4、mechanism §B）

| claim_id | 内容 | 等级 | 定位 | 来源文件 |
|---|---|---|---|---|
| LH-PAIR-1-5 | 道德对位结构（pair / 双主角）：《啤酒街》×《琴酒巷》；《勤奋与懒散》12 帧双轨 | `[史料]` [R17] | [hogarth.md](../../dossiers/hogarth.md) §1-5 L39；§12 #3 L391–394；AUDIT claim `HG-S1-05`（`partial`） | dossier |
| LH-CLUE-1-3 | 单帧多线索「别的画我们看；他的画我们读」（Lamb） | `[研究]` 转引 | [hogarth.md](../../dossiers/hogarth.md) §1-3 L37；AUDIT claim `HG-S1-03`（`partial`） | dossier |
| LH-RULE5 | §8.2-5 对位规则：骨架相似度 ≥70%、语义相反标志物 ≥3 对 | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) L238；[hogarth.md](../../modules/hogarth.md) L44 | dossier + 卡 |
| LH-RULE1 | §8.2-1 线索 ≥5 / 可读文字 ≥1 | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) L234；[hogarth.md](../../modules/hogarth.md) L40 | dossier + 卡 |
| LH-RULE4 | §8.2-4 类型化面孔 ≥3 种、关键点偏差 ≤15% | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) L237；[hogarth.md](../../modules/hogarth.md) L43 | dossier + 卡 |
| LH-GATE-P2P3 | P2 剧场化 70% + P3 线索密度 65%，「两条同时 ≥中档才成立」= 是不是荷加斯起步门 | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) §4 L108–109、用法注 L114；§8.1 中文说明 L228；[hogarth.md](../../modules/hogarth.md) L62 | dossier + 卡 |
| LH-P4 | P4 讽刺/道德强度 50%（警示题材 85%） | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) §4 L110 | dossier |
| LH-P5-LIGHT | P5 光线戏剧度 30%；§8.2-3 画内单一硬光源=0 / 暗部 L<0.2 ≤35% / 近黑 L<0.08 ≤10% | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) §4 L111、§8.2 L236；[hogarth.md](../../modules/hogarth.md) L42 | dossier + 卡 |
| LH-LIGHT-OVER | P5 升「画外单光源＋亮部只落脸/手/道具」→ 卡拉瓦乔；「单光源连续衰减照单张脸」→ 伦勃朗 | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) §4 分工注 L115；[hogarth.md](../../modules/hogarth.md) L63 | dossier + 卡 |
| LH-RULE6 | §8.2-6 运动模糊=0 / 1 个动作极值；§8.2-7 题刻 ≤2 行 | `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) L239–240；[hogarth.md](../../modules/hogarth.md) L45–46 | dossier + 卡 |
| LH-3CHECK | 生成后三查（线索/面孔/光线） | `[归纳]` prompt 说明 | [hogarth.md](../../dossiers/hogarth.md) §8.1 中文说明 L229；[hogarth.md](../../modules/hogarth.md) 对应 | dossier |

---

<a id="db-source-line-72"></a>
## §E OVERTURNED（交叉排线允许——与戈雅相反）= 已决事实（brief 强调点；mechanism §C、how-to-think D5、learning_path 阶梯3）

| claim_id | 内容 | 等级 / 状态 | 定位 | 来源文件 |
|---|---|---|---|---|
| **LH-OVERTURN-01** | 自审B #4：初稿假设「荷加斯版画无交叉排线」经 contact sheet 目检（Gin Lane/Beer Street/Rake 面部暗部密布交叉排线）→ **OVERTURNED**，改为「交叉排线允许——与戈雅相反」 | fact / `supported`（档案内已决） | [hogarth.md](../../dossiers/hogarth.md) L444；AUDIT claim `HG-OVERTURN-01` | dossier |
| **LH-OVERTURN-02** | 对侧 `goya.md` L39/L52「无交叉排线原则：平行细线＋平飞尘块」= 互斥轴 | `[研究]` / `supported` | `goya.md` L39、L52；AUDIT claim `HG-OVERTURN-02` | goya |
| LH-OVERTURN-LAND | 定论落地三处：§1-9 / §2-3 / §8.2-8「排线族 ≥2 方向（交叉排线允许）」 | `[归纳]` 规则文本（方向性结论 fact） | [hogarth.md](../../dossiers/hogarth.md) L43、L54、L241；[hogarth.md](../../modules/hogarth.md) L47 | dossier + 卡 |
| LH-OVERTURN-BOLD | 「strong bold stroke」粗犷刀痕（作者自述）；BM「etching and engraving」工艺著录 | `[自述]` / `[史料]` [R9] | [hogarth.md](../../dossiers/_corpus/hogarth.md) #11 L84；[hogarth.md](../../dossiers/hogarth.md) §2-2 L53；AUDIT claim `HG-S1-09`/`HG-S2-03` | corpus + dossier |
| LH-OVERTURN-ACCT | GOALS A-103「1 条 OVERTURNED（交叉排线）」；AUDIT RESULT §4「1/1 accounted for」 | `[史料]`（本机记录） | `ops/GOALS.md` L99；`AUDIT-hogarth/RESULT.md` §4；claim `HG-GOALS-01` | GOALS + AUDIT |
| **LH-OVERTURN-BOUND** | 未升级为 web-supported（无 web 来源陈述）；档案内已决事实，不冒充外部佐证 / 像素实测 / 渲染验证 | 边界（诚实口径） | `AUDIT-hogarth/RESULT.md` §4、§8；`coverage_manifest.json` 4 fetches 只证 4 上下文事实 | AUDIT |
| LH-OVERTURN-COMBO | 与戈雅组合按 `conflicts.md` 预检 + N4 分区，两轴不得互抄 | `[归纳]` 组合纪律 | [hogarth.md](../../dossiers/hogarth.md) §3.1 L99、§8.2 组合注意 L230 | dossier |

---

<a id="db-source-line-86"></a>
## §F CE-1 PARTIAL REFUTATION → scoped carve-out（brief 强调点；mechanism §E、how-to-think D2、learning_path 阶梯2）

| claim_id | 内容 | 等级 / 状态 | 定位 | 来源文件 |
|---|---|---|---|---|
| **LH-CE1-RULE** | 被攻击规则：§8.2-2 帧数≥6 + 同一主角跨帧进度；§4 P1 默认 8 | `[归纳]` 规则 | [hogarth.md](../../dossiers/hogarth.md) L235、L107；`AUDIT-hogarth/counterexample.md` L9–11 | dossier + AUDIT |
| **LH-CE1-OBJ** | 反例对象：《琴酒巷》×《啤酒街》= 2 帧 pair、无同一主角，却是 dossier 自称 core 道德对位指纹 + §12 练习 | `[史料]` + `[归纳]` | [hogarth.md](../../dossiers/hogarth.md) §1-5 L39、§0 L24、§12 #3 L391–394；`AUDIT-hogarth/counterexample.md` L13–14 | dossier + AUDIT |
| **LH-CE1-VERDICT** | **CE-1 = PARTIAL REFUTATION**：规则对 8/6/12 帧 progress series 成立，但**不是荷加斯的必要条件**；需显式 applicability domain | `[inference]` / `partial` | `AUDIT-hogarth/counterexample.md` L16–23（判词 L23）；`AUDIT-hogarth/RESULT.md` §5 | AUDIT |
| **LH-CE1-CARVEOUT** | **scoped carve-out**：§8.2-2 / P1 默认 8 适用域 = **progress-series variant only**；pair 走 §8.2-5 对位规则 | `[归纳]`（本 shard 记录的适用域收窄）/ `partial` | 依据 [hogarth.md](../../dossiers/hogarth.md) §4 P1 弱档 L107「成对/三段」、L114 分工注；`AUDIT-hogarth/counterexample.md` L21；本 shard [mechanism_notes.md](mechanism_notes.md) §E.5、[learning_path.md](learning_path.md) 阶梯2、[how-to-think.md](how-to-think.md) D2 | AUDIT + 本 shard 产物 |
| LH-CE1-HONEST | 本 shard 未渲染帧、未跑 §8.2 八规则自查、未改 §8.2 文本 / 仓库（repo read-only） | 边界 | `AUDIT-hogarth/counterexample.md` L3/L21/L54；`RESULT.md` §4 | AUDIT + 本 shard |
| LH-CE2 | CE-2 UNDER-SPECIFICATION：「1 个动作极值」无测量协议（全局拐点 vs 姿态数）；非反驳 | `[inference]` | `AUDIT-hogarth/counterexample.md` L27–40 | AUDIT |
| LH-CE3 | CE-3 WEAKENED / hedge-dependent：§1-8 靠「灯烛作道具但不成光锥主角」非操作化例外存活 | `[inference]` | `AUDIT-hogarth/counterexample.md` L44–50；[hogarth.md](../../dossiers/hogarth.md) §1-8 L42 | AUDIT + dossier |

---

<a id="db-source-line-100"></a>
## §G 20 权利行 CC0×11 + PD×9（brief 强调点；mechanism §G、RESULT §2/§4）

| claim_id | 内容 | 等级 / 状态 | 定位 | 来源文件 |
|---|---|---|---|---|
| **LH-RIGHTS-COUNT** | `images_public = 20`；labels `{"CC0":11,"Public_domain":9,"unknown":0}`；private-layer `images_public=0` 例外不适用 | `[史料]`（本机声明）/ `supported`（本机自洽） | `AUDIT-hogarth/coverage_manifest.json` L32–33、L45；`AUDIT-hogarth/RESULT.md` §3；`rights_review.md` L3 | AUDIT |
| LH-RIGHTS-CC0 | CC0 = 11：Met Open Access 10（8 直取 + 2 Commons 捐赠件）+ Cleveland 1 | `[史料]`（本机声明） | `AUDIT-hogarth/rights_review.md` L9/L11（桶说明）、表 #1,2,3,4,5,6,7,13,14,15,17 | AUDIT |
| LH-RIGHTS-PD | Public domain = 9：Yorck / Google Art Project / PD-art 油画扫描（Commons） | `[史料]`（本机声明） | `AUDIT-hogarth/rights_review.md` L10（桶说明）、表 #8,9,10,11,12,16,18,19,20 | AUDIT |
| LH-RIGHTS-ROWS | 20/20 行有 license label + source URL + attribution；无 row 猜 PD | `[史料]`（本机声明） | `AUDIT-hogarth/rights_review.md` L13–37；全局 [manifest.md](../../dossiers/_images/manifest.md) L713–L732；AUDIT claim `HG-IMG-01` | AUDIT + repo |
| **LH-RIGHTS-BOUND** | 本机声明级：无逐行 license-page 回查、无 `image_seen`、PD 管辖有效性未裁定；本 shard 不升级、不复制像素 | 边界（诚实口径） | `AUDIT-hogarth/rights_review.md` L6、L38–40；`RESULT.md` §8 | AUDIT |
| LH-RIGHTS-LINK | `analysis_of_beauty_plate_1`(#2) = §12 #7 S 曲线图版；`beer_street`/`gin_lane`(#3/#6) = CE-1 pair；`a_harlots_progress`/`rakes_print_*` = progress 印本 | `[归纳]`（本 shard 关联） | `AUDIT-hogarth/rights_review.md` 表 + [hogarth.md](../../dossiers/hogarth.md) §12 #1/#3/#4/#7 | AUDIT + dossier |

---

<a id="db-source-line-113"></a>
## §H 冲突 / 漂移 / 口径（mechanism §D、RESULT §3/§4）

| claim_id | 内容 | 状态 | 定位 | 来源文件 |
|---|---|---|---|---|
| LH-CONF-ROWS | C-01（均匀舞台光同侧）/ C-07（排线分轴）/ C-08（模糊=0）/ C-16·C-17（N4 分区） | `supported` | `conflicts.md` C-01 L55、C-07 L136、C-08 L149、C-16 L258、C-17 L272；[hogarth.md](../../dossiers/hogarth.md) §8.2 组合注意 L230；[hogarth.md](../../modules/hogarth.md) L72 | conflicts + dossier + 卡 |
| LH-NEARMiss | near-miss「8 对 vs §4 表 11 编号行」口径差；512/513 行、§11 32/33、conflicts §5 415/421 | `partial`（口径漂移，不重设分母） | `AUDIT-hogarth/RESULT.md` §6；`locator_drift.md`；`conflicts.md` §5.C L404 | AUDIT + conflicts |
| LH-CANON-DRIFT | dossier §3.1 L86 / §10-8 L303「goya.md 无对侧条款 / 唯一写死正本」vs `goya.md` L88（A-109）已有「vs 荷加斯…为主正本」 | `conflict`（AUDIT 判，未修） | AUDIT claim `HG-ONLYCANON-01`/`-02`；`goya.md` L88；`AUDIT-hogarth/RESULT.md` §6 | AUDIT + goya |
| LH-LEDGER | card/dossier/corpus 三 hash 与 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） hogarth 条目一致（3/3）；quotes=29、images=20 | `supported`（本机） | `AUDIT-hogarth/RESULT.md` §2；`coverage_manifest.json` hashes | AUDIT + ledger |

---

<a id="db-source-line-124"></a>
## §I 支持状态汇总（本机档案内自洽，不评外部真伪）

- `supported`：§A 口径、§B S 曲线自述定位、§C 序列自述/判据定位、§D 规则定位、§E OVERTURNED 已决事实、§G 权利计数、§H ledger 一致 / C-rows。
- `partial`：CE-1 判定与 carve-out（`[inference]` 纸面，非渲染验证）、near-miss/计数口径漂移、AUDIT 原判 `partial` 项（storyboard 转引 / P1 / 5+线索 / 对位骨架 / Lamb 转引）。
- `conflict`：dossier「唯一正本」措辞 vs goya.md L88（AUDIT 已报未修，本 shard 不碰）。
- `unverified`（外部，诚实保留）：29 条语料原文/英译逐字回源、Observer 2000 原刊、BL Add MS 27991 原稿、BM curator's comments、London Evening Post 1751 原刊、20 行逐行 license truth、`image_seen`、§8.2 阈值像素实测、真人学习成效。

> 证据底本：内部证据 1569918a037bdd5e（未公开；来源记录由维护者保留）（ACCEPTED）——本图复用其 77 行 claim map / coverage / counterexample / rights / RESULT 判定与 locator，**未重新盘点、未改任何 AUDIT 产物**；本 shard 为 `submitted`，`review:null`，作者不自接受。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
