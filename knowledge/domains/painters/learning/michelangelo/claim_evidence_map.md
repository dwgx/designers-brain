<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-michelangelo；原正文 SHA-256 `858fa0db29802b265bc6ae4cacd19704a47e39758008165a1681255e46b3354d`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# claim_evidence_map — LEARN-michelangelo

> 本 LEARN 路径（[learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md)）中**每条事实性/规则性 claim** 的回源表。等级沿用 AUDIT-michelangelo 与冻结源标注：`[自述]`/`[自述·转引]`/`[史料]`/`[研究]`/`[归纳]`/`[实测]`/`[INFERENCE]`；`[归纳]` = 项目操作规则（可被 A-12 实验推翻，见 `conflicts.md:10-26`），不是米开朗基罗本人主张。
> **依赖**：`AUDIT-michelangelo`（ACCEPTED，[claim_evidence_map.md](claim_evidence_map.md) / `RESULT.md` / `coverage_manifest.json`）。本轮不重审，复用其 locator 纪律。
> **四个输入哈希开局已实测一致**（见 `RESULT.md` §1）：card `9b50095e…a3d3ab1a2044`、dossier `45ee9cef…f6e8eca83a`、corpus `9a8888a5…1761bd8fee`、conflicts `314a24da…aabbef`（与 内部证据 d07fd23689a24201（未公开；来源记录由维护者保留） 及 AUDIT `coverage_manifest.json:63-66` 一致）。
> **locator 口径**：`dossiers/`= [michelangelo.md](../../dossiers/michelangelo.md)；`modules/`= [michelangelo.md](../../modules/michelangelo.md)；`corpus/`= [michelangelo.md](../../dossiers/_corpus/michelangelo.md)；`conflicts.md`= [conflicts.md](../../../../cross/conflicts.md)；`01-AUDIT.md`/`00-GOAL.md`= 执行包根。行号以冻结树 `f0089523` 的 `grep -n` 实测为准；C-01/02/17/18 的数字行号 locator 漂移见 AUDIT `RESULT.md` §1.5（语义锚点仍正确）。

---

<a id="db-source-line-10"></a>
## A. 前置 / 输入完整性（observation · supported）

| claim_id | 事实 | 等级 | locator |
|---|---|---|---|
| INP-01 | 四输入哈希 = ledger + AUDIT coverage-manifest（card/dossier/corpus/conflicts）| 机械 | 内部证据 d07fd23689a24201（未公开；来源记录由维护者保留）；AUDIT `coverage_manifest.json:63-66`；本轮 `RESULT.md` §1 实测 |
| INP-02 | 卡 §8.1/§8.2/§4 与档案逐字一致 | 机械（复用基线）| AUDIT `RESULT.md` §1.1 INP-07（BASELINE-P1 `raw/extract-check.out` L2）|
| INP-03 | 本卡 HAS §8.1b（L39）| 机械 | `modules/michelangelo.md:39`；AUDIT `claim_evidence_map.md:9` INP-05 |
| INP-04 | `images_public=3`（PD / CC BY-SA 4.0 / CC0 三类分明）| 机械 | AUDIT `RESULT.md` §3；`_images/manifest.md` L23-25；`coverage_manifest.json:11`（`image_seen=0`）|
| INP-05 | 「1509 揭幕」OVERTURNED、当前零断言；1512-10-31 为采用年表 | `[史料]` | AUDIT `claim_evidence_map.md:11-17`（OVT-01..07）；`dossiers/michelangelo.md:281`；`corpus/michelangelo.md:165-171`（条目 19 改注）|

<a id="db-source-line-20"></a>
## B. learning_path.md 的 claim（A-30 形状各节）

| claim_id | claim（出现在 learning_path.md 哪节）| 等级 | locator |
|---|---|---|---|
| LP-01 | 减法雕塑观（per forza di levare / 石中已含概念）为自述 | `[自述]` | `corpus/michelangelo.md:17-23,25-39`；`dossiers/michelangelo.md:43-45,54-56` |
| LP-02 | 浮雕是绘画的裁判（画越接近浮雕越好）为自述 | `[自述]` | `corpus/michelangelo.md:9-15`；`dossiers/michelangelo.md:56,83-85` |
| LP-03 | 人体即舞台 / terribilità / 扭转体 / 密集人群为可观察指纹 | `[研究]` | `dossiers/michelangelo.md:23-29`；`modules/michelangelo.md:9-13` |
| LP-04 | 五控制参数默认值（70/50/65/60/15）| `[归纳]` | `dossiers/michelangelo.md:66-70`；`modules/michelangelo.md:91-95` |
| LP-05 | 重点作品年份/馆藏/来源号（大卫/天顶/最后的审判/圣殇/Doni Tondo/摩西/奴隶/隆达尼尼）| `[研究]`+`[史料]` | `dossiers/michelangelo.md:12-17`（§0）、`:186-204`（§9 来源表）、`:330-373`（§12 八件）、`:298-318`（§11.10 S 编号）|
| LP-06 | 三图权利 = 1 PD + 1 CC BY-SA 4.0 + 1 CC0 | `[史料]` | AUDIT `RESULT.md` §3；`_images/manifest.md` L23-25 |
| LP-07 | **硬边阴影 ≤ 画面短边 0.6%（「凿出来」的边缘）** | `[归纳]` | `dossiers/michelangelo.md:176`（§8.2-3）；`modules/michelangelo.md:81`；`conflicts.md:33,71-83`（C-02）|
| LP-08 | **构图密度 ≥55% + 连续空白背景 ≤15%** | `[归纳]` | `dossiers/michelangelo.md:177`（§8.2-4）；`modules/michelangelo.md:82`；`conflicts.md:48,272-283`（C-17）|
| LP-09 | **浮雕强度强档「凿出、硬边投影」默认 65%** | `[归纳]` | `dossiers/michelangelo.md:68`（§4）；`modules/michelangelo.md:93`；`conflicts.md:49,285-296`（C-18）|
| LP-10 | 扭转 ≥30° / ≥60% 人物达标；剪影 25% 可读、断裂 ≤2；限色 ≤0.5 / 强调色 ≤2 | `[归纳]` | `dossiers/michelangelo.md:175,178,179`；`modules/michelangelo.md:80,83,84` |
| LP-11 | 三参数（扭转/密度/浮雕）调高会「吃掉对方柔和笔触」，与达·芬奇天然互斥 70/30 | `[归纳]` | `dossiers/michelangelo.md:72,168`；`modules/michelangelo.md:97` |
| LP-12 | 三级阶梯练习骨架（凿边人体 / 满构图掩膜 / 形体-平涂分区）复用 §12 既有练习 | `[归纳]`（本路径编排）| `dossiers/michelangelo.md:338,343,348,353,368`；[learning_path.md](learning_path.md) §4（本文件产物）|
| LP-13 | **练习一律为「建议练习」，不写「已证实学习收益」** | 规范 | `01-AUDIT.md:273`；`03-RESEARCH-AGENDA.md:125,131`；`00-GOAL.md:24` |
| LP-14 | 常见失败 F1–F8（软边吃掉硬边 / C-01 字面禁令 / 折中值 / 留白过大 / 平涂浮雕打架 / 量纲误判 #7 / non-finito 心理 / 冒称收益）| `[归纳]`+规范 | `conflicts.md:55-83,272-296,353`；`dossiers/michelangelo.md:32,168,177`；`01-AUDIT.md:273` |
| LP-15 | 下一步接入 A-30 总路线（基础/进阶/可替换分支/跨艺术家比较）| 规范 | `01-AUDIT.md:271`；`03-RESEARCH-AGENDA.md:31,125,131` |
| LP-16 | 使用边界：规则 `[归纳]` 可推翻、自述/推断分离、不升级史实、E4 未复现 | 规范 | `00-GOAL.md:9`；`conflicts.md:10-26`；AUDIT `RESULT.md` §0 能力边界、`coverage_manifest.json` `unverified` |

<a id="db-source-line-41"></a>
## C. how-to-think.md 的 claim（决策序）

| claim_id | claim | 等级 | locator |
|---|---|---|---|
| HT-01 | S1「先定概念、手听命于理智」= 自述 | `[自述]` | `corpus/michelangelo.md:25-31`（Rime 151）、`:173-179`（信 CDXXXV「画是用脑子画的」）；`dossiers/michelangelo.md:54` |
| HT-02 | 起稿分段、拆架看效果后放大尺度 = 可观察工作流程 | `[研究]` | `dossiers/michelangelo.md:39-40`（§2-2/3）|
| HT-03 | S2「减」立形 = 自述 | `[自述]` | `corpus/michelangelo.md:17-23,33-39`；`dossiers/michelangelo.md:43,55` |
| HT-04 | 不画金饰（「画中人物本是穷人」）= 转述自述 | `[自述·转引]` / `[reported speech]` | `corpus/michelangelo.md:43-49`；`dossiers/michelangelo.md:60,100` |
| HT-05 | S3「浮雕是绘画裁判」= 自述，且同信有「哲学上同一」的自我修正 | `[自述]` | `corpus/michelangelo.md:9-15`（含 `:15` 注）、`:123-128`（条目 15）；`dossiers/michelangelo.md:56,83-85` |
| HT-06 | 雕塑家身份优先 / goiter 诗「我不是画工」/「不情愿也做完」| `[史料]`+`[自述]` | `dossiers/michelangelo.md:53,58,78-81,106-109`；`corpus/michelangelo.md:108-114` |
| HT-07 | 「嫌十二使徒方案是 poor thing、要求全权」= 自述·转引 | `[自述·转引]` | `dossiers/michelangelo.md:57`；`corpus/michelangelo.md:149-155`（条目 17）|
| HT-08 | S4 人体承载叙事 + 满构图 = `[研究]`+`[归纳]`（非自述）| `[研究]`+`[归纳]` | `dossiers/michelangelo.md:11,23,25,28,177,178` |
| HT-09 | S5 强档推满 / S6 轴所有权·分区 = `[归纳]`（非自述）| `[归纳]` | `dossiers/michelangelo.md:66-72,168`；`conflicts.md:305-333`（N1/N3/N4/N9）|
| HT-10 | 不推断心理：未完成面是历史状态、非刻意 non-finito 美学；terribilità 是同代人概括 | 规范 + `[归纳]` | `dossiers/michelangelo.md:24,32`；`00-GOAL.md:9` |
| HT-11 | 不把 `[归纳]` 参数/规则写成「米开朗基罗认为」；`[研究·百科]` 只作来历注脚 | 规范 | `conflicts.md:10-26`；`dossiers/michelangelo.md:114-118`（§6）|
| HT-12 | 失效条件（S1 需现场应变 / S2 平涂组合 / S3 达芬奇持轴 / S4 未定义对齐 / S5 70/30 / S6 未写分区表）| `[归纳]` / `[推测]`（已逐条标注）| `conflicts.md:71-83,272-296,305-333`；[how-to-think.md](how-to-think.md) §0 表、§1 各「何时失效」|

<a id="db-source-line-58"></a>
## D. mechanism_notes.md 的 claim（params/rules → practice）

| claim_id | claim | 等级 | locator |
|---|---|---|---|
| MN-01 | §4 五参数弱/中/强/默认三档原文 | `[归纳]` | `dossiers/michelangelo.md:62-72`；`modules/michelangelo.md:87-97` |
| MN-02 | §8.2 七条可判定规则原文（比例/扭转/硬边/密度/剪影/色彩/未完成度）| `[归纳]` | `dossiers/michelangelo.md:170-180`；`modules/michelangelo.md:75-85` |
| MN-03 | §8.1 负向段 `--no sfumato haze / soft blurry edges / symmetric frontal standing pose` 等 | `[归纳]` | `dossiers/michelangelo.md:157-163`；`modules/michelangelo.md:30-37` |
| MN-04 | C-01 级别=覆盖、解法=半影宽度+显式声明改写（N5）| `[归纳]` | `conflicts.md:32,55-69,305-306,317-320`；AUDIT `claim_evidence_map.md:21` |
| MN-05 | C-02 级别=硬、≥1.5% vs ≤0.6% 空交集、1920 宽 ≥28.8px vs ≤11.5px、N3 轴所有权 | `[归纳]` | `conflicts.md:33,71-83,311-312`；AUDIT `claim_evidence_map.md:22` |
| MN-06 | C-17 级别=硬、空白≤15% vs 留白≥35%/≥20%、定义对齐（空白≠留白）| `[归纳]` | `conflicts.md:48,272-283`；AUDIT `claim_evidence_map.md:23` |
| MN-07 | C-18 级别=退化、作用对象可分离、分对象拆分 + 主体掩膜 + ≥70% 面积 | `[归纳]` | `conflicts.md:49,285-296,314-315`（N4）；AUDIT `claim_evidence_map.md:24` |
| MN-08 | §3 N1/N3/N4/N5/N9 通用组合规则为 `[归纳]` 正本 | `[归纳]` | `conflicts.md:300-339`（§3 头 `:300` 明注采纳状态；N1 `:305`、N3 `:311`、N4 `:314`、N5 `:317`、N9 `:332`）|
| MN-09 | near-miss #7（物体边缘 ≥2px vs 形体转折 ≤0.6% 短边，量纲不同）| `[归纳]` | `conflicts.md:353`（§4 表 #7）；`modules/michelangelo.md:107` |
| MN-10 | near-miss #4（四饱和度上限取 ≤0.35）| `[归纳]` | `conflicts.md:345`（§4 表 #4 行）；`modules/michelangelo.md:107` |
| MN-11 | C-01 旁证：blender 出厂 `size=0.25` 半影 3px→235px 差 78 倍 | `[实测]` | `conflicts.md:55-69`（C-01 引 `blender/workflow.md:442`）；AUDIT `claim_evidence_map.md:21`、AUDIT `RESULT.md` §1.4 |
| MN-12 | 卡 §冲突注记把 C-01/02/17/18 + near-miss #4/#7 一一列出 | `[归纳]` | `modules/michelangelo.md:99-107` |
| MN-13 | 每机制失败条件（M1–M6、未完成度、#7、组合双标准）| `[归纳]` | [mechanism_notes.md](mechanism_notes.md) §5（本文件产物，逐行回源到 §8.2 / §4 / conflicts，见该表「判据 locator」列）|

<a id="db-source-line-76"></a>
## E. 边界 / 未验证（如实保留，不升级）

| claim_id | 内容 | 状态 | locator |
|---|---|---|---|
| UNV-01 | 练习为建议练习、未经人评、不宣称学习收益 | 规范约束 | `01-AUDIT.md:273`；[learning_path.md](learning_path.md) §4/§8 |
| UNV-02 | 外部 URL 未联网复核；图像 `image_seen=0` | `[UNVERIFIED]` | AUDIT `coverage_manifest.json:7,77-82`；AUDIT `RESULT.md` §2.2 |
| UNV-03 | E4 纯风格迁移 / E1_t1c §8.1b v2「T1 3/3」/ A-12 组合实验未复现 | `[UNVERIFIED]` | AUDIT `RESULT.md` §0 能力边界、§4 交接建议③；`modules/michelangelo.md:44` |
| UNV-04 | Condivi 训练章节未逐字直读、`[研究·百科]` 级 | 已知缺口 | `dossiers/michelangelo.md:213-221`（§10 缺口 1）、`:114-118` |
| UNV-05 | conflicts.md 四条行号 locator 相对冻结树漂移；精确回填交 CONFLICT-* | `[归纳]` | AUDIT `RESULT.md` §1.5；本轮 `grep -n` 实测（§2 头 C-01=55 / C-02=71 / C-17=272 / C-18=285）|

---

**点名项判定**：本轮强调的「硬边阴影 ≤0.6% 短边」「构图密度 ≥55% + 空白 ≤15%」「浮雕强度」「C-01/C-02/C-17/C-18」「三级阶梯（凿边人体 → 满构图掩膜 → 形体/平涂 C-18 分区）」全部落表，且每条均有 `file:line` 回源；自述与归纳严格分栏（C 节 HT-01..07 为自述/史料，HT-08..09 与 B/D 节为 `[归纳]`）；练习效果一律标「建议练习」，无「已证实学习收益」表述。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
