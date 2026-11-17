<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-hogarth；原正文 SHA-256 `58e2de1eaa1a8a4ec253c1b901a35fcdb456cc460700db49be140dc7d4693da8`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-hogarth — How to Think（how_to_think）

> 回答「创作时先选什么、牺牲什么、为什么、何时失效」，**不是**作品外观形容词表（`03-RESEARCH-AGENDA.md` L14、`02-EXECUTION-PLAN.md` §Lane B L66）。
> **铁律**：不从画面外观反推作者心理，不把本项目 `[归纳]` 规则冒充荷加斯原意（`00-GOAL.md` L9、[hogarth.md](../../dossiers/hogarth.md) L5）。下表每一决策步都标等级：
> - `[自述]` = 作者写下/说出（corpus / §3 / §5，逐字可回引）——**可作为「他为什么这么决策」的依据**；
> - `[归纳]` = 本项目研究者为逐帧生成构造的操作规则——**是本 shard 的决策程序，不是作者内心**；
> - `[史料]/[研究]` = 输入材料（馆方/艺术史），仅作佐证；`[推测]` = 低置信，本文件不使用；
> - `fact(已决)` = AUDIT 已判定的 resolved fact（OVERTURNED 交叉排线），下游直接采信、不回退。

---

<a id="db-source-line-12"></a>
## §0 先问：我面对的是哪一类荷加斯问题？

| 问题类型 | 该读什么 | 不该读什么 |
|---|---|---|
| 他**为什么**把线条当造型主变量？ | `[自述]` 语料 #22/#23（美的线/优雅的线）、#20/#21（多样/有组织的多样） | 不要把 §8.2 阈值说成他的形式论 |
| 他**为什么**画系列而非单幅？ | `[自述]` corpus #1「field not broken up」、§3-1 L69「画如戏剧」、§3-5 L73「为用不为饰」 | 不要把 §4 P1=8 说成「他规定 8 帧」 |
| 我**怎么**逐帧生成/自检？ | `[归纳]` §8.2 八规则、§4 六参数、§3.1 分镜接口 | 不要把操作规则写成「荷加斯主张」 |

> AUDIT caveat 同口径：[hogarth.md](../../dossiers/hogarth.md) L243「以上阈值为本项目 `[归纳]`，未对原作做像素测量（分母＝假想参考帧）」。

---

<a id="db-source-line-24"></a>
## §1 创作决策序（D0→D6，每步：先选 / 牺牲 / 为什么 / 何时失效 / 等级）

<a id="db-source-line-26"></a>
### D0 — 先定「这是形式论练习，还是叙事工程任务？」`[自述]` 分流 + `[归纳]` 分工

- **先选**：若目标是「线条作为造型主变量」→ 走《美的分析》S 曲线（M0，阶梯1）；若目标是「现代道德题材逐帧生成」→ 走系列叙事（M1，阶梯2）。
- **牺牲**：形式论练习不追求「像不像荷加斯画面」；叙事任务不把 `line of beauty` 当 prompt 风格词。
- **为什么**：两者是不同轴。`[自述]` #22/#23 是 1753 年形式论；`[自述]` corpus #1/§3 是 1730s–50s 道德系列意图。[hogarth.md](../../modules/hogarth.md) §8.1 负向段 L32 反而排除 `idealised beauty / decorative abstraction`——把 S 曲线当风格词会撞车。
- **何时失效**：想在一次生成里同时满足「S 曲线理想美」与「可读道德剧」→ 两轴互斥，必须分任务。
- **等级**：分流依据 `[自述]`；「不进 §8.2 八规则」的判定为 `[归纳]`（观察：八规则无一条是 S 曲线阈值）。

<a id="db-source-line-34"></a>
### D1 — 先选叙事单位 = 系列，而非单幅 `[自述]` 意图 / `[归纳]` 判据

- **先选**：`系列`（6/8/12 帧成套），帧＝时间轴上的一站。
- **牺牲**：每帧自足性（对侧洛克威尔的强项，§3.1 L89–90）。
- **为什么** `[自述]`：corpus #1「modern moral subject… a field not broken up」；§1-1 L35「完整道德弧必须按序读」；§3-1 L69「我的画就是我的舞台（dumb show）」。
- **操作判据** `[归纳]`：§3.1 L91「判据＝帧间是否存在进度依赖」；§8.2-2 L235 帧数 ≥6 / 可追踪元素 100% / ≥2 次状态变化；§8.1 负向 L35 禁止 `single-frame isolation when a series is requested`。
- **何时失效**：**CE-1 carve-out**（见 D2）——pair/对位作品不走这一步。

<a id="db-source-line-42"></a>
### D2 — 给「系列进度规则」套适用域（CE-1 scoped carve-out）`[inference]` 判定 + `[归纳]` 收窄

- **先选**：先判作品属于 **progress-series**（《浪子历程》8 /《浪女历程》6 /《勤奋与懒散》12）还是 **pair/对位**（《琴酒巷》×《啤酒街》2 帧、双主角平行）。
- **牺牲**：把 §8.2-2 当「无条件必要条件」的省事做法。
- **为什么**：AUDIT `counterexample.md` L7–23 判 **CE-1 PARTIAL REFUTATION**——pair 是 dossier 自称 core 指纹（§1-5 L39 / §12 #3），却「2 帧、无同一主角」，逐字套 §8.2-2 会拒绝它。规则对 progress series 成立，但**不是荷加斯的必要条件**。
- **carve-out（本 shard 记录，不改仓库）**：§8.2-2 / P1 默认 8 的适用域 = **progress-series variant only**；pair 走 §8.2-5 对位规则。§4 P1 弱档「小系列 3–6 帧（成对/三段）」L107 已留位置，不一致只在 §8.2-2 被写成无条件逐帧检查。
- **何时失效 / 诚实边界**：carve-out 是 `[inference]` 纸面判定（AUDIT counterexample.md L21 proposed discriminating test 未执行、未渲染帧、未跑八规则自查）；**不是实验验证**。本 shard 无写权，不改 §8.2 文本、不改仓库。
- **等级**：CE-1 判定 `[inference]`；适用域收窄为 `[归纳]`（研究者构造的决策程序）。

<a id="db-source-line-51"></a>
### D3 — 建分镜表与进度表 `[归纳]`（接口来自 `[史料-转引]` + `[归纳]`）

- **先选**：N 帧＝N 场景，逐帧写「标题＋一行动作＋道具状态」（§3.1 L98）；把主角服装/道具列「进度表」逐帧核。
- **牺牲**：即兴、不写状态的「氛围帧」。
- **为什么**：§3.1 L95–101 Lane B 接口——分镜 = 分镜板、连续性检查 = B1–B4 原型、题刻 = 收尾文案槽；外部佐证 Alan Parker「分镜祖先」仅 `[史料-转引]`（Wikipedia 转引 Observer 2000，原刊未回查，§10-5 降级，AUDIT RESULT §4 保持 partial）。
- **何时失效**：抽掉任一帧同伴仍能完整复述 → 进度依赖不成立，回到单帧自足档（洛克威尔侧）。
- **等级**：接口 `[归纳]`；「分镜祖先」`[史料-转引]`，**不得升级为 `[研究]`**。

<a id="db-source-line-59"></a>
### D4 — 定「是不是荷加斯」的两条起步门 `[归纳]`

- **先选**：P2 剧场化 ≥70% + P3 线索密度 ≥65%（§4 L108–109；§8.1 中文说明 L228「两条同时 ≥中档才成立」）；再挂 §8.2-1（线索 ≥5、可读文字 ≥1）、§8.2-4（类型化面孔、关键点偏差 ≤15%）。
- **牺牲**：空旷极简场景、漫画式夸张脸（[hogarth.md](../../modules/hogarth.md) §8.1 负向 L34 `empty minimal scenes / caricature distortion`）。
- **为什么** `[归纳]`：§8.1 中文说明 L228 明确这是起步门；§4 用法注 L114「P2/P3 定是不是荷加斯」。作者侧 `[自述]` 只支持「性格而非漫画」（§3-4 L72、corpus #13「knowledge of character…caricatura as the lowest」），不提供 70%/65% 数值。
- **何时失效**：P2 或 P3 任一低于中档 → 退化为普通风俗画（§8.1 用法注同口径）；P3 升到高档 ≥8 线索＋文字≥2 是 Marriage 档，不是常态。
- **等级**：数值 `[归纳]`；「性格非漫画」意图 `[自述]`。

<a id="db-source-line-67"></a>
### D5 — 表面工艺：把 OVERTURNED 当已决事实 `fact(已决)`

- **先选**：版画帧按 `pure etching and engraving — bold confident line, cross-hatching for shadow, a caption or verse engraved below the image`（§8.1 正向 L28）；§8.2-8 L241 排线族 ≥2 方向、**交叉排线允许**、线覆盖率 ≥15%、平涂 ≤10%。
- **牺牲**：照抄戈雅「无交叉排线＋平飞尘块」。
- **为什么（已决，不重论证）**：AUDIT 自审B #4（L444）已把初稿假设「荷加斯版画无交叉排线」**OVERTURNED**，改为「交叉排线允许——与戈雅相反」，写入 §1-9 L43 / §2-3 L54 / §8.2-8 L241；对侧 `goya.md` L39/L52「无交叉排线原则」为互斥轴。AUDIT RESULT §4「1/1 OVERTURNED accounted for」、GOALS A-103 L99、claim `HG-OVERTURN-01`/`HG-OVERTURN-02`。
- **何时失效**：若生成结果禁掉了交叉排线 → 回到已被推翻的错误初稿；若与戈雅组合，按 `conflicts.md` 预检 + N4 分区（§3.1 L99），两轴不得互相复制。
- **等级**：`fact(已决)` / `supported`（AUDIT 内部核验：contact sheet 目检 + goya 对照）。**诚实边界**：AUDIT RESULT §4 明言「未升级为 web-supported（无 web 来源陈述它）」——采信为档案内已决事实，不冒充外部佐证、不重新开放为假设。

<a id="db-source-line-75"></a>
### D6 — 光线与警示档的越界检查 `[归纳]`

- **先选**：P5 光线戏剧度 30%（均匀舞台光）；P4 讽刺/道德强度 50%（警示题材 →85%）。
- **牺牲**：画外单光源、tenebrism、深黑背景（§8.1 负向 L32 `chiaroscuro drama / single spotlight / deep black backgrounds`）。
- **为什么**：§1-8 L42「为看清所有线索服务」；§8.2-3 L236 画内单一硬光源 = 0、暗部 L<0.2 ≤35%、近黑 L<0.08 ≤10%。**越界**：P5 升到「画外单光源＋亮部只落脸/手/道具」→ 卡拉瓦乔；「单光源连续衰减照单张脸」→ 伦勃朗（§4 分工注 L115）。
- **何时失效（CE-3）**：夜/室内 tavern 场景需可见灯烛才可读时，§1-8 只靠「灯烛作道具但不成光锥主角」非操作化例外存活 → **WEAKENED / hedge-dependent**（AUDIT counterexample.md L44–50）。与 Lane B 组合时 C-01 同侧，显式声明 `even stage light, no single hard source` 即可。
- **等级**：全部 `[归纳]`；CE-3 `[inference]`。

---

<a id="db-source-line-85"></a>
## §2 等级纪律核对表（防「把推断冒充原意」）

| 决策步 | 可归为作者原意的部分 | 只能是研究者程序的部分 |
|---|---|---|
| D0 | S 曲线形式论 `[自述]` #22/#23；道德题材意图 `[自述]` #1/§3 | 「两轴分流 / S 曲线不进 §8.2」`[归纳]` |
| D1 | 「field not broken up」「画如戏剧」`[自述]` | 帧数 6/8/12、100% 出现率、≥2 状态变化 `[归纳]` |
| D2 | 无（pair 是 `[史料]` [R17] 设计记录） | CE-1 carve-out `[inference]` + `[归纳]` |
| D3 | 无（接口是研究者构造） | 分镜表/进度表/B1–B4 映射 `[归纳]`；「分镜祖先」`[史料-转引]` |
| D4 | 「性格而非漫画」`[自述]` #13/§3-4 | 70%/65%/≥5 线索/≤15% 偏差 `[归纳]` |
| D5 | 「strong bold stroke」`[自述]` corpus #11；工艺 `[史料]` [R9] BM | §8.2-8 覆盖率/平涂阈值 `[归纳]`；OVERTURNED 结论 `fact(已决)` |
| D6 | 「为用不为饰」`[自述]` §3-5 | P5/P4 数值、暗部阈值、越界判据 `[归纳]` |

> 任何一步都**不得**写成「荷加斯规定/主张 P1=8、线索≥5、交叉排线比例」——这些是 `[归纳]` 操作规则（[hogarth.md](../../dossiers/hogarth.md) L5、L243）。

---

<a id="db-source-line-101"></a>
## §3 「何时失效」汇总（速查）

1. D0：把 S 曲线当 moral-subject 风格词 → 撞 §8.1 负向 `idealised beauty / decorative abstraction`。
2. D1：pair/对位作品套 §8.2-2 进度规则 → **CE-1**（→ D2 carve-out）。
3. D3：抽帧不复述断裂 → 无进度依赖，退回单帧档。
4. D4：P2 或 P3 < 中档 → 退化普通风俗画。
5. D5：禁交叉排线 → 回到已 OVERTURNED 的错误初稿；与戈雅组合未按 N4 分区 → 互斥轴互抄。
6. D6：升画外单光源 → 卡拉瓦乔/伦勃朗越界；夜景灯烛 → CE-3 hedge-dependent。
7. 全局：把 `[归纳]` 阈值当已像素实测 / 把建议练习当已证实学习收益 → 违反 A-30 口径（`01-AUDIT.md` L273）。

---

<a id="db-source-line-113"></a>
## §4 收口

- 本文件是**决策序**（how to think），不是 prompt 模板；参数/规则的逐条数值在 [mechanism_notes.md](mechanism_notes.md)，练习顺序在 [learning_path.md](learning_path.md)，逐 claim 定位在 [claim_evidence_map.md](claim_evidence_map.md)。
- 全部为研究者构造的建议决策程序；`review:null`、`human_review.status=not_applicable`、无真人评价、无渲染实验。作者不自接受。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
