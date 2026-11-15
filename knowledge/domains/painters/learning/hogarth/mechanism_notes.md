<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-hogarth；原正文 SHA-256 `6d398b9e321f0dd10ed433c807cf8586d17675f4103f02c16007353c7cf1db79`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-hogarth — 机制说明（mechanism_notes）

> 把 ACCEPTED 内部证据 1569918a037bdd5e（未公开；来源记录由维护者保留） 与 repo `f0089523…` 的 §4 参数、§8.2 八规则、§3.1 判据映射成「练习 / 决策 / 失败条件」。等级照录 [hogarth.md](../../dossiers/hogarth.md) L5；**全部 §8.2 阈值 `[归纳]`、未经渲染实验校准、未做像素测量**（L243、[hogarth.md](../../modules/hogarth.md) L49）。
> 专节：**§C OVERTURNED（交叉排线允许）作为已决事实**、**§E CE-1 PARTIAL REFUTATION scoped carve-out**（brief 点名）、**§G 20 权利行 CC0×11 + PD×9**。
> 本文件为 staging 内建议文本；repo READ-ONLY，不改任何 §8.2/§4 文本、不改 AUDIT 产物。

---

<a id="db-source-line-9"></a>
## §A 形式论机制：line-of-beauty S 曲线（`[自述]`）

| 项 | 内容 | 定位 |
|---|---|---|
| A-1 波状线 | 「加上**波状线 waving line**……比前述任何线都更能产生美……称它为『美的线』the line of beauty」 | [hogarth.md](../../dossiers/_corpus/hogarth.md) #22 L168–173（原文逐字 + `en->zh` 意译） |
| A-2 蛇形线 | 「**蛇形线 serpentine line** 同时朝不同方向起伏缠绕，牵引眼睛愉悦地沿连续多样行进……精确的蛇形线，或『优雅的线』line of grace」——图版以细金属丝绕锥体缠出 | [hogarth.md](../../dossiers/_corpus/hogarth.md) #23 L175–180 |
| A-3 前置概念 | 多样（Variety）为普遍快感之源（#20 L154）、「有组织的多样」（#21 L161） | [hogarth.md](../../dossiers/_corpus/hogarth.md) L154/L161 |
| A-4 底本 | 1833 Anecdotes / Gutenberg #51459（AUDIT 联网复核 `line of beauty`×7、`line of grace`×5、`THE LINE OF BEAUTY` 命中） | `AUDIT-hogarth/RESULT.md` §4；`coverage_manifest.json` R19；[hogarth.md](../../dossiers/hogarth.md) §9 R19 L277 |
| A-5 作品锚点 | 《美的分析》1753 出版（§11 年表 L355）；图版 1「S 形曲线的可视化教具」、练习「临摹线条系统，标 ≥5 处实例，3 件日常物各画一条最优 S 线」 | [hogarth.md](../../dossiers/hogarth.md) §12 #7 L411–414 |
| A-6 机制地位 | **形式分析工具（线条＝造型主变量）**，不是「是不是荷加斯」画面门 | §12 #7 L413；[hogarth.md](../../modules/hogarth.md) §8.1 负向 L32（`--no idealised beauty / decorative abstraction`） |

**关键边界**：§8.2 八条逐帧规则中**无一条**是 S 曲线阈值；§4 六参数中**无一项**控制 S 曲线。把 `line of beauty` 写进 moral-subject prompt 当风格词，会与 §8.1 负向段冲突（L32/L34）。S 曲线与「现代道德题材 + 系列叙事」是两条不同的轴：一条讲线条造型，一条讲叙事工程。

---

<a id="db-source-line-24"></a>
## §B 主机制 → §4 参数 → §8.2 规则 → 练习映射

| 机制 | §4 参数（默认，`[归纳]`） | §8.2 规则（`[归纳]`） | 练习（learning_path 阶梯） | 失败条件 |
|---|---|---|---|---|
| **M1 连环画叙事序列** | P1=8（L107，工作流）、P6=系列内复用（L112） | 规则2 L235 帧数≥6 / 可追踪元素 100% / ≥2 状态变化；规则7 L240 题刻≤2 行 | 阶梯2：8 行分镜表 + 抽帧复述测试（§12 #1 L384） | 抽帧不复述断裂；pair 误套（→ §E） |
| **M2a 对位 pair** | P2=70% + P3=65%（L108–109）、P4=50%（L110，警示 85%） | 规则5 L238 骨架≥70% / 相反标志物≥3 对 | 阶梯3：两张对位草图 + 两行题刻（§12 #3 L394） | 骨架相似度 <70%；把 pair 套规则2 |
| **M2b 单帧多线索** | P3=65%（L109） | 规则1 L234 线索≥5 / 可读文字≥1；规则4 L237 类型脸≥3 种、关键点偏差≤15% | 阶梯3：《时髦婚姻 1》列 ≥8 线索 + 视线链图（§12 #2 L389） | 线索<5；漫画式夸张脸 |
| **M2c 表面工艺（OVERTURNED）** | —（P5 管光不管线） | 规则8 L241 排线族≥2 方向（**交叉排线允许**）/ 覆盖率≥15% / 平涂≤10% / 无>12px 平滑渐变 | 阶梯3：版画变体按 §8.1 正向 L28 落地 | 禁交叉排线（→ §C） |
| **光线可读性** | P5=30%（L111） | 规则3 L236 画内单一硬光源=0 / 暗部 L<0.2 ≤35% / 近黑 L<0.08 ≤10% | 三查③（§8.1 中文说明 L229） | 画外单光源→卡拉瓦乔/伦勃朗越界（L115）；CE-3 |
| **定格 / 题刻** | — | 规则6 L239 模糊=0 / 1 个动作极值；规则7 L240 题刻≤2 行 | 阶梯2/3 分镜表「标题＋一行」 | CE-2「动作极值」未定义测量协议 |

> 起步门：P2≥中档 **且** P3≥中档才「是不是荷加斯」（§4 用法注 L114、§8.1 中文说明 L228）；P1 定叙事工程、P4 定警示档、P5/P6 定连续性。全部档位划分本身亦 `[归纳]`。

<a id="db-source-line-37"></a>
### §B.1 叙事序列机制的可操作三条（§3.1 L95–101，`[归纳]` + `[史料-转引]`）

1. **系列骨架**：N 帧＝N 场景，逐帧「标题＋一行动作＋道具状态」＝ Lane B 分镜表「内容」列原型。
2. **帧间连续性检查**：主角服装/道具列「进度表」逐帧核 ＝ B1–B4 一致性检查原案例。
3. **顺序与放行**：观看顺序写死（《啤酒街》先于《琴酒巷》）；订阅预览（先看画＝关键帧、后买印）＝「关键帧先行」验收原型。
4. 判据（§3.1 L91）：**「帧间是否存在进度依赖」**；角色复用 ≠ 连续叙事（Willie Gillis 式各帧自足仍归单帧档）。
5. 「分镜祖先」= Alan Parker（Observer 2000）经 Wikipedia 转引，**`[史料-转引]`、原刊未回查**（§10-5 降级；AUDIT RESULT §4 保持 partial），不得升级为 `[研究]`。

---

<a id="db-source-line-47"></a>
## §C OVERTURNED（交叉排线允许——与戈雅相反）= 已决事实 `fact(已决)` / `supported`

> brief 点名：carried as resolved fact。下游**直接采信，不再当作开放假设，不重新论证**。

| 项 | 内容 | 定位 |
|---|---|---|
| C-1 初稿假设 | 「荷加斯版画无交叉排线」 | [hogarth.md](../../dossiers/hogarth.md) 自审B #4 L444 |
| C-2 推翻依据 | contact sheet 逐张目检（Gin Lane / Beer Street / Rake 印本）：面部与暗部**密布交叉排线**；与戈雅（禁交叉排线＋飞尘块）正好相反 | L444（AUDIT claim `HG-OVERTURN-01`） |
| C-3 定论 | **OVERTURNED（初稿假设错误）→ 改为「交叉排线允许——与戈雅相反」**（§1-9 / §3.1） | L444 |
| C-4 落地三处 | §1-9 L43「排线族 ≥2 方向（交叉排线允许——**与戈雅相反**）」；§2-3 L54「明暗由线密度与交叉排线构成」；§8.2-8 L241「排线族 ≥2 方向（交叉排线允许）」 | [hogarth.md](../../dossiers/hogarth.md) L43/L54/L241；[hogarth.md](../../modules/hogarth.md) L47 |
| C-5 对侧互斥轴 | `goya.md` L39/L52「无交叉排线原则：只用平行细线＋平飞尘块，不做交叉排线」 | AUDIT claim `HG-OVERTURN-02`（`goya.md` L52） |
| C-6 账本一致 | GOALS A-103 L99「1 条 OVERTURNED（交叉排线）」；AUDIT RESULT §4「1/1 OVERTURNED accounted for」；claim map `HG-OVERTURN-01`/`-02` | `ops/GOALS.md` L99；`AUDIT-hogarth/RESULT.md` §4 |

**诚实边界（不夸大）**：
- AUDIT RESULT §4 明言「**未升级为 web-supported**（无 web 来源陈述它）」——这是**档案内已决事实**（contact sheet 目检 + goya 对照的互斥轴证据），不是外部佐证、不是像素实测、不是渲染实验。
- §8.2-8 的「≥2 方向 / ≥15% 覆盖率」仍是 `[归纳]` 阈值（L243）；OVERTURNED 只决定「交叉排线允许/禁止」这个**方向性结论**，不把数值阈值升级为已验证。
- 与戈雅组合时按 `conflicts.md` 预检 + N4 分区（§3.1 L99、§8.2 组合注意 L230），两轴不得互相复制。
- 本 shard **无写权**：不改 §8.2/§4 文本、不改 goya.md、不改 AUDIT 产物；只把 resolved fact 带进学习路径（learning_path 阶梯3、how-to-think D5）。

---

<a id="db-source-line-68"></a>
## §D 冲突行 / near-miss（沿用 AUDIT RESULT §6 口径，不改仓库）

| 行 | 内容 | 本 shard 处置 |
|---|---|---|
| C-01 硬阴影 | 荷＝均匀舞台光，与 Lane B 默认禁令**同侧**；显式声明 `even stage light, no single hard source` 即可 | mechanism §B 光线；how-to-think D6 |
| C-07 表面 | 荷＝线刻＋排线（与丢勒同族「排线明度」侧），组合线卡须分轴 | learning_path §7；§C 互斥轴旁注 |
| C-08 运动模糊 | 荷＝定格侧，全片运动模糊帧 = 0 声明（§8.2-6 L239） | §B 定格机制 |
| C-16 / C-17 | 荷＝满场编目式细节、负空间小；按 N4 分区（背景/装饰面可让） | 组合预检 |
| near-miss 口径 | card L77 / dossier 说「8 对」，§4 表实际 11 编号行（#9–#11 补 2026-10-16） | AUDIT 已报口径差，本 shard 不重设分母 |
| 512/513 行、§11 32/33 行、conflicts §5 415/421 行 | 计数口径漂移 | AUDIT RESULT §6 已报，本 shard 不改文件 |
| SUBSTANTIVE 漂移 | dossier §3.1 L86 / §10-8 L303 称「goya.md 无对侧条款 / 本档唯一写死正本」，但 `goya.md` L88（A-109 wave16）已有「vs 荷加斯…为主正本」条款 | AUDIT 判 `conflict` + supported goya L88，**未修**；本 shard 只引用「分工轴一致」，不碰「唯一正本」措辞 |

> 定位纪律沿用 `conflicts.md` §5.C L404「先怀疑行号、再怀疑内容」；本 shard 不改 conflicts.md。

---

<a id="db-source-line-84"></a>
## §E CE-1 PARTIAL REFUTATION → scoped carve-out（brief 点名，专节）

**来源**：`AUDIT-hogarth/counterexample.md` L7–23（CE-1），全部 `[inference]` 纸面反例、无帧、无像素、无真人练习；本 shard **未重跑、未渲染、未跑 §8.2 八规则自查**。

<a id="db-source-line-88"></a>
### E.1 被攻击的规则
- `dossiers/hogarth.md:235`（§8.2-2）：「系列帧数 ≥6；同一主角的可追踪元素每帧出现率 100%，且跨帧状态可列进度表（至少 2 次状态变化）」。
- `dossiers/hogarth.md:107`（§4 P1）：默认建议 **8**（浪子档；「大系列 8–12 帧」强档）；弱档才是「小系列 3–6 帧（成对/三段）」。

<a id="db-source-line-92"></a>
### E.2 反例对象（dossier 自身 canon）
《琴酒巷》×《啤酒街》(Gin Lane / Beer Street, 1751) —— **2 帧 pair**、**无同一主角**（对比街景人群，不是「同一主角跨帧推进」）；却是 dossier 自称的核心「道德对位结构 (pair)」指纹（§1-5 L39）与学习清单练习（§12 #3 L391–394），即「dossier 自己认定为荷加斯」。

<a id="db-source-line-95"></a>
### E.3 逐字套用结果
`帧数 ≥6`？2 ≥ 6 = FALSE；`同一主角可追踪元素 100%`？无共享主角，undefined/0；`≥2 次状态变化`？not applicable → 字面 §8.2-2 / P1 默认 8 **拒绝一张 dossier 自认的荷加斯作品**，作为必要条件即 **over-broad**。

<a id="db-source-line-98"></a>
### E.4 判定 = PARTIAL REFUTATION
- 规则对《浪子历程》8 /《浪女历程》6 /《勤奋与懒散》12 帧 **progress series 成立**；
- 但**不是荷加斯的必要条件**（AUDIT counterexample.md L23）；
- 需要显式 **applicability domain**：「progress-series variant only」。

<a id="db-source-line-103"></a>
### E.5 scoped carve-out（本 shard 记录的适用域收窄）
> **§8.2-2「系列进度规则」与 §4 P1 默认 8 的适用域 = progress-series variant only；pair/对位作品走 §8.2-5（对位规则：骨架≥70%、相反标志物≥3 对），不走 §8.2-2。**

- 依据：§4 P1 弱档「小系列 3–6 帧（成对/三段）」（L107）本身已给 pair 留位置；§3.1 L114 分工注也把 P1 定为「工作流参数…不进画面重叠计算」。不一致只在 §8.2-2 被写成**无条件逐帧检查**（AUDIT counterexample.md L21）。
- learning_path 阶梯2 把此 carve-out 写成「练习对象若为 2 帧 pair，停手不套 §8.2-2」；how-to-think D2 把它写成决策步「先判 progress-series vs pair」。
- **不改写 §8.2 文本、不改仓库**（repo read-only；AUDIT 已标未修，规则 owner / RULE lane 才有权落进规则文本）。

<a id="db-source-line-110"></a>
### E.6 CE-2 / CE-3（同批，诚实并列，不夸大）
- **CE-2 UNDER-SPECIFICATION**（L27–40）：§8.2-6「1 个动作极值」vs §1-3/§8.2-1「5+ 线索」——「动作极值」按全局拐点还是按姿态数无测量协议；非反驳，无 claim 被推翻。
- **CE-3 WEAKENED / hedge-dependent**（L44–50）：§1-8「画内单一硬光源=0」只靠「灯烛作道具但不成光锥主角」非操作化例外存活；§8.2-3 暗部代理阈值声明 `[归纳]`/未实测。

<a id="db-source-line-114"></a>
### E.7 等级 / 状态
CE-1 判定 `[inference]`；carve-out 为 `[归纳]`（研究者构造的适用域收窄）；support_status 记 `partial`（纸面判定，非渲染验证）。**不是实验验证、不是已证实机制修正**。

---

<a id="db-source-line-119"></a>
## §F 三查 + 两查（生成后自检，`[归纳]`）

来自 §8.1 中文说明 L229，加本 shard 两条 brief 强调点：
1. 每帧可辨认线索 ≥5、可读文字 ≥1？（§8.2-1）
2. 面孔「类型化但不夸张」（无漫画式扭曲）？（§8.2-4）
3. 光线均匀可读（画内单一硬光源 = 0、无近黑背景）？（§8.2-3）
4. **交叉排线是否保留**（OVERTURNED 已决事实，§8.2-8 / §8.1 正向 L28）？
5. **对位帧是否走 §8.2-5 而非 §8.2-2**（CE-1 carve-out）？

> 全部阈值 `[归纳]`、未做像素测量；本 shard 未执行任何生成/渲染/自查，以上为**建议自检清单**。

---

<a id="db-source-line-132"></a>
## §G 20 权利行（CC0×11 + PD×9）— 本机声明级

来源：`AUDIT-hogarth/rights_review.md` L13–34 + `coverage_manifest.json` L33 `{"CC0":11,"Public_domain":9,"unknown":0}`。全局 manifest [manifest.md](../../dossiers/_images/manifest.md) hogarth 行 L713–L732 + 本地 MANIFEST.md 20 行 + 20 `.jpg` 在盘（`ls | wc -l` = 20，AUDIT 已核）。

| # | file | license | source institution |
|---|---|---|---|
| 1 | a_harlots_progress_plate_1.jpg | CC0（Met Open Access） | The Met 399540 |
| 2 | analysis_of_beauty_plate_1.jpg | CC0（Met Open Access） | The Met 404837 |
| 3 | beer_street.jpg | CC0（Met Open Access） | The Met 399846 |
| 4 | four_stages_of_cruelty_1.jpg | CC0（Met 经 Commons） | The Met DP835381 |
| 5 | four_stages_of_cruelty_4.jpg | CC0（Met 经 Commons） | The Met DP835382 |
| 6 | gin_lane.jpg | CC0（Met Open Access） | The Met 399847 |
| 7 | industry_and_idleness_plate_1.jpg | CC0 | Cleveland Museum of Art 1967.118 |
| 8 | marriage_a_la_mode_1_the_marriage_settlement.jpg | Public domain | National Gallery, London NG113 |
| 9 | marriage_a_la_mode_6_the_ladys_death.jpg | Public domain | National Gallery, London NG118 |
| 10 | rakes_progress_1_the_heir.jpg | Public domain（Yorck） | Sir John Soane's Museum P40 |
| 11 | rakes_progress_3_the_tavern_scene.jpg | Public domain | Sir John Soane's Museum P42 |
| 12 | rakes_progress_8_the_madhouse.jpg | Public domain（Yorck） | Sir John Soane's Museum P47 |
| 13 | rakes_progress_print_1.jpg | CC0（Met Open Access） | The Met 399563 |
| 14 | rakes_progress_print_6.jpg | CC0（Met Open Access） | The Met 399569 |
| 15 | rakes_progress_print_8.jpg | CC0（Met Open Access） | The Met 399561（1763 重印） |
| 16 | self_portrait_with_palette.jpg | Public domain（Google Art Project） | Yale Center for British Art |
| 17 | south_sea_scheme.jpg | CC0（Met Open Access） | The Met 396205 |
| 18 | the_gate_of_calais.jpg | Public domain（Google Art Project） | Tate N01464 |
| 19 | the_painter_and_his_pug.jpg | Public domain | Tate N00112 |
| 20 | the_shrimp_girl.jpg | Public domain | National Gallery, London NG1162 |

- **CC0 = 11**（Met Open Access 10：#1,2,3,6,13,14,15,17 直取 8 + #4,5 Commons 捐赠件 2；Cleveland 1：#7）；**Public domain = 9**（#8,9,10,11,12,16,18,19,20：Yorck / Google Art Project / PD-art 油画扫描）；**unknown = 0**。
- 20/20 行都有 license label + source URL + attribution；**本机声明级**：无逐行 license-page 回查、无 `image_seen`（AUDIT rights_review.md L6/L38–40）。本 shard 不升级、不复制像素、不猜 PD。「Public domain」管辖有效性未独立裁定。
- 与学习路径的关系：`analysis_of_beauty_plate_1.jpg`（#2，Met 404837）正是 §12 #7 S 曲线练习的图版本体；`beer_street`/`gin_lane`（#3/#6）是 CE-1 pair 反例本体；`a_harlots_progress_plate_1`（#1）/ `rakes_progress_print_*`（#13–15）是 progress series 印本本体。**权利可寻址 ≠ 已目检**（read_scope=metadata）。

---

<a id="db-source-line-165"></a>
## §H 收口 / 未决

- §A S 曲线、§B 参数→规则→练习、§C OVERTURNED 已决事实、§E CE-1 carve-out、§G 20 权利行 = brief 五个强调点全部落位。
- 未决（不在本 shard 写权内）：CE-1 carve-out 落进 §8.2 规则文本（RULE/STYLE owner）；CE-2「动作极值」测量协议；CE-3「道具灯烛 vs 光锥主角」阈值；§8.2 阈值像素实测；20 行逐行 license truth + image_seen；dossier「唯一正本」措辞与 goya.md L88 的口径订正。
- 全部练习/自检为建议；`review:null`、`human_review.status=not_applicable`、无真人评价、无渲染实验。作者不自接受。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
