<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-sorolla；原正文 SHA-256 `1ab3386fc9a5290f2d7da44e6eece49be74e86258a587868111f67e66c466237`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-sorolla — claim → evidence map（每条论断带 locator）

> 任务 `LEARN-sorolla` · 依赖 `AUDIT-sorolla`（**ACCEPTED**，`receipt.json` status=accepted / review.verdict=accepted / reviewer=`ReviewGateAUDIT-sorolla(glm-5.3-flash)`；`review-evidence.md` "Verdict: PASS — 2 minor findings, non-blocking"）。本 lane **不重新审计**，复用其 75 行 claim/evidence locator 纪律。
> **口径**：每条论断给「来源文件 + 具体行/节定位 + 证据等级 + 支持状态」。内部证据 4874f193014ae79c（未公开；来源记录由维护者保留） 为只读回源（声明基线 `f008952365a77e140cbda3f3959d43ef000f9a22`，本 lane 开工已 sha256sum 复核三件冻结输入，见 `RESULT.md §2`）；内部证据 f3a53970e669cd35（未公开；来源记录由维护者保留） 为上游 ACCEPTED 产物；内部证据 0487bd3371fd0e1c（未公开；来源记录由维护者保留） 为本 lane 生成。
> 等级沿用仓库口径（dossier §0 L5 / corpus header L4）：`[自述]`/`[reported speech]`/`[contemporary record]`/`[self-written]` = 作者/同时代人言语记录；`[史料]` = 史实/权利记录；`[归纳]` = 项目操作规则/研究者归纳；`[研究]` = 二手研究/文本比对；`[推测]` 本 lane **不使用**（计数 0）。
> 版本列：仓库文件 = `f0089523…`；staging artifact = 本轮/上游生成（给 sha256）。`read_scope` 与 `access_status` 分开：外部 URL 本轮未重访 = `unknown`（其 1909 实核结论由 AUDIT-sorolla 承担，本 lane 复用），本机文件 = `available`，原图像素目检 = 0（无 `image_seen`）。
> **行号纪律**：全部用**实测行号 + 子串**；conflicts.md near-miss 口径漂移（8 vs 11）与 C-05/C-09/C-12 非专属由 AUDIT 登记，本表照录、不修仓库。

---

<a id="db-source-line-11"></a>
## A. 输入与版本（本 lane 开工复核）

| # | claim_id | 论断（短） | kind/status | 证据定位（source : locator） | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 1 | LS-INPUT-CARD | card sha = ledger `c22ecd03…ac733`（80 行，§8.1/§8.2/§4 与 dossier 逐字一致） | fact/supported | 内部证据 29ffb199b11378e6（未公开；来源记录由维护者保留） 实跑；AUDIT `coverage-manifest.json:module_dossier_extract_contract` 全 true | `[史料]`（字节实测） | 开工 sha256sum 全等 |
| 2 | LS-INPUT-DOSSIER | dossier sha = ledger `1b619242…fac0e`（451 行 v2 规格） | fact/supported | 内部证据 d7f029d13261008b（未公开；来源记录由维护者保留） | `[史料]` | 全等 |
| 3 | LS-INPUT-CORPUS | corpus sha = ledger `9d3fa7b0…c4b0`（31 条，1909 两卷本 OCR 行号级） | fact/supported | 内部证据 5ae4acdbe8044168（未公开；来源记录由维护者保留）；AUDIT `coverage-manifest.json:quote_count=31` | `[史料]` | 全等；31 条沿用 AUDIT 计数 |
| 4 | LS-INPUT-AUDIT-MANIFEST | 上游 `AUDIT-sorolla/coverage-manifest.json` sha = `2aee90d5…ecad9` | fact/supported | 内部证据 f72ae127ac414c45（未公开；来源记录由维护者保留） 全文件 sha × `RESULT.md §2` × AUDIT `receipt.json` artifacts 登记值 | `[史料]`（字节实测） | RECEIPT input_hashes 第 4 项 |
| 5 | LS-INPUT-CONFLICTS | conflicts.md sha = `314a24da…abef` | fact/supported | [conflicts.md](../../../../cross/conflicts.md) 全文件 sha × `RESULT.md §2` × AUDIT `coverage-manifest.json:hashes.conflicts` | `[史料]` | 全等 |
| 6 | LS-AUDIT-ACCEPTED | 上游 AUDIT-sorolla 已 **ACCEPTED**（review.verdict=accepted，独立审者 glm-5.3-flash；gate "PASS", 2 minor non-blocking） | fact/supported | 内部证据 62d2ba0e0853889a（未公开；来源记录由维护者保留） status=accepted, `:review.verdict`=accepted；`review-gate-receipt.json`；`review-evidence.md:5`；`receipt.json:author_actor_id`=AuditSorolla ≠ reviewer | `[史料]`（产物） | 本 lane 不重新审计，只复用结论 |
| 7 | LS-AUDIT-RECEIPT-HASH | AUDIT `receipt.json` sha = `42fce86a…4bf`；`review-gate-receipt.json` sha = `265e5e1d…c168` | fact/supported | 本 lane 开工 sha256sum 实跑 × `RESULT.md §2` | `[史料]`（字节实测） | 作为 ACCEPTED 证据引用 |

<a id="db-source-line-23"></a>
## B. 前置知识（learning_path.md §1 / how-to-think.md S1）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 8 | LS-K1-LUMINISM | 索罗拉 = 直射阳光的实写系统，唯一「无包络/无雾/无晨昏」纯直射档；本人拒绝被称印象派 | observation/supported | `dossiers/sorolla.md:16,18,20`（§0）；`modules/sorolla.md:9-13`；AUDIT `RESULT.md §1` | `[研究]`+`[归纳]` | 非作者原话 |
| 9 | LS-K2-WHITE-ON-WHITE | 白上加白：同屏 ≥3 种色温的白、「没有一种完全的白」；整体 high-key | observation/supported | `dossiers/sorolla.md:33,41`（§1-1/-9）；`modules/sorolla.md:9`；§8.2-1/-2 `:185,186` | `[研究]`/`[史料]`（现象）+ `[归纳]`（判据） | 判据数值非史料 |
| 10 | LS-K3-PARAMS | §4 六参数各三档，P1+P2 定身份（≥中档才成立） | fact/supported | `dossiers/sorolla.md:101-108`；`modules/sorolla.md:56-65`（原样逐字一致） | `[归纳]` | 默认 75/70/75/65/55/80% 非史料常数 |
| 11 | LS-K4-DIVISION | vs 莫奈（氛围光 vs 直射光，四轴）、vs 佐恩（阳光白 vs 有限色板，四轴）+ 越界警报 5 条 | fact/supported | `dossiers/sorolla.md:79-93`（§3.1）、`:109`（警报）；`modules/sorolla.md:66,72-74`；`conflicts.md:311`（N3） | `[归纳]` | 分工条款写死 |
| 12 | LS-K5-SELF | 作者自述层全部为 1909 两卷本 `[reported speech]` 转记，转记不当内心证据 | fact/supported | `dossiers/sorolla.md:115-123`（§5）；`_corpus/sorolla.md:15,22,30,45,87,98`；dossier §0 `:7`、corpus header `:6` | `[自述转记]` | 不升级为确定心理 |
| 13 | LS-K6-SCOPE | §4/§8.2 阈值只刻画「正午高照度 beach/luminism 档」，非全部 oeuvre | observation/supported | `dossiers/sorolla.md:395`（§B-3 WEAKENED→收窄）；AUDIT `coverage-manifest.json:counterexample_attempt`；`RESULT.md §8` | `[归纳]`/`[inference]` | 量词边界，不是新缺陷 |

<a id="db-source-line-34"></a>
## C. 海滩逆光 + 白裙高调机制（本轮强调；learning_path §2/§3、how-to-think S2/S3、mechanism_notes §4）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 14 | LS-MECH-BACKLIGHT-NAME | 「海滩逆光 + 白裙高调」是本项目对一组作品的归纳性命名，不是史料术语/作者自述 | fact/supported | `learning_path.md §1 K2/§3 M2`、`how-to-think.md S2/S3`、`mechanism_notes.md §4` 抬头声明 | `[归纳]` | 等级边界，避免装成史实 |
| 15 | LS-MECH-HIGHKEY | 高调去黑：平均明度 ≥72%、纯黑 ≤0.3%、暗部 H 230–290° | fact/supported | `dossiers/sorolla.md:185`（§8.2-1）、`:41`（§1-9 high-key）；`modules/sorolla.md:46` | `[归纳]` | 数值非像素实测 |
| 16 | LS-MECH-WHITE-LAYERS | 白上加白可判定版：白区(L≥90%) ≥3 色相簇、每簇≥2%、明度动态范围 ≤8% | fact/supported | `dossiers/sorolla.md:186`（§8.2-2）、`:33`（§1-1）；`:102`（P2）；`modules/sorolla.md:47` | `[归纳]` | 「高明度窄域 + 色相变化」 |
| 17 | LS-MECH-TRANSLUCENT | 逆光 + 半透布料 + 室内外光交界「刺目之光与滤过的柔光同框」；透光白 vs 反光白分层 | observation/supported | `dossiers/sorolla.md:362-368`（§12-6/-7「逆光下透光白与反光白的区别」「透光白与反光白的层次」）、`:366`([R3] 馆方指南)、`:36,40,44`（§1-4/-8/-12 反光网） | `[研究]`（现象）+ `[归纳]`（练习映射/判据） | 分层是练习结构，不是史料断言 |
| 18 | LS-MECH-REFLECTION | 反光语法：湿表面闪点 ≥6 个/100×100px、色相与环境相关 ≥0.5；橙/桃/丁香反光贴高光 | fact/supported | `dossiers/sorolla.md:189`（§8.2-5）、`:104`（P4）、`:36`（§1-4）；`modules/sorolla.md:12,50` | `[归纳]`（判据）+ `[研究]`（现象） | 「太阳不只在天空」`:44` |
| 19 | LS-MECH-TOP-LIGHT | 正午顶光：亮部重心与光源差 ≤30°、阴影 ≤人物高 25%、过渡带 ≤4% 短边 | fact/supported | `dossiers/sorolla.md:187`（§8.2-3）、`:34`（§1-2）、`:101`（P1）；`modules/sorolla.md:48` | `[归纳]` | 短影且有色，非黑 |
| 20 | LS-MECH-STROKE | 长笔一笔定型：覆盖 ≥85%、近 ≥40px/远 ≤12px、亮部粗糙度 ≥暗部 1.3×；不分解不碎 | fact/supported | `dossiers/sorolla.md:188`（§8.2-4）、`:35`（§1-3）、`:82`（vs 莫奈笔触轴）；`modules/sorolla.md:49` | `[归纳]` | 碎短分解 = 越界莫奈 |
| 21 | LS-MECH-CROP | 摄影裁切：地平线 ≥画高 55% 或不可见、≥1 水平带、主体触边、无中心对称 | fact/supported | `dossiers/sorolla.md:190`（§8.2-6）、`:37,38,39`（§1-5/-6/-7）；`modules/sorolla.md:51` | `[归纳]` | — |

<a id="db-source-line-47"></a>
## D. 1909 两卷本 OCR 行号级锚点（**ACCEPTED 上游证据**，本 lane 复用，不重跑）

| # | claim_id | 论断（短） | kind/status | 证据定位（含 OCR 行号） | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 22 | LS-1909-ANCHORS-ACCEPTED | AUDIT-sorolla 外部实核 3 次 decisive CONFIRMED：garage 1677–1681、parti pris 1420–1424、sunlight 667–670 **精确命中**；transient 1387–1390 ✓；3 处 ±2/±9/±21 行 OCR 漂移已登记 | fact/supported | 内部证据 d88909ec781d10da（未公开；来源记录由维护者保留） (RF-1/RF-2/RF-3)；`RESULT.md §8`；`claim_evidence_map.md:85-89`；`review-evidence.md` Q07/§1 | `[史料]`（ACCEPTED 产物） | **本 lane 未重访外部 URL、未重跑 OCR**；复用结论 |
| 23 | LS-1909-GARAGE | "a studio is only a garage…" — Starkweather，Vol.II **行 1677–1681** | observation/supported | `_corpus/sorolla.md:45-49`（条目 #5，来源行 Vol.II 1677–1681）；`dossiers/sorolla.md:117`（§5-3） | `[reported speech]`（转记） | how-to-think S4/清单#5 引用；不当「轻视室内」心理推断 |
| 24 | LS-1909-PARTI-PRIS | "Go to nature with no parti pris…" — Starkweather，Vol.II **行 1420–1424** | observation/supported | `_corpus/sorolla.md:30-34`（条目 #3，Vol.II 1420–1424）；`dossiers/sorolla.md:118`（§5-4）、`:69`（§3-3） | `[reported speech]`（转记） | how-to-think S4 决策来源；外部实核精确命中 |
| 25 | LS-1909-TRANSIENT | "Every effect is so transient…" — Starkweather，Vol.II **行 1388–1390**（外部实核 1387–1390） | observation/supported | `_corpus/sorolla.md:22-27`（条目 #2）；`dossiers/sorolla.md:115`（§5-1） | `[reported speech]`（转记） | how-to-think S5 速度决策 |
| 26 | LS-1909-SUNLIGHT | "It is impossible really to paint sunlight…" — Starkweather，Vol.II **行 668–670**（外部实核 667–670 精确） | observation/supported | `_corpus/sorolla.md:87-91`（条目 #11）；`dossiers/sorolla.md:121`（§5-7） | `[reported speech]`（转记） | how-to-think S5；清单#6 禁性格补语 |
| 27 | LS-1909-HATE-DARKNESS | "I hate darkness…" — *Evening Post* 1909-02-05，Vol.II **行 2405–2410**（Press 汇编） | observation/supported | `_corpus/sorolla.md:98-102`（条目 #12）；`dossiers/sorolla.md:116`（§5-2）、`:67`（§3-1 光是主角） | `[reported speech]`（转记） | 清单#1 禁「他厌恶黑暗」心理句 |
| 28 | LS-1909-NO-CORRECTION-WEAKENED | "he paints with the hand of God / 从不修改" 单一来源，dossier §B-4 已 WEAKENED，不进主规则 | observation/supported (conflict 登记) | `_corpus/sorolla.md:118-123`（条目 #15，标「单一来源，慎用」）；`dossiers/sorolla.md:396`（§B-4）；`:53`（§2-3 慎用「从不修改」） | `[contemporary record]`（匿名同场画家，记者转引） | 不升级为硬规则/性格推断 |

<a id="db-source-line-59"></a>
## E. 分工 / 四轴 compressed mirror（how-to-think S7、mechanism_notes §6）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 29 | LS-ZORN-FOUR-AXES-MIRROR | vs 佐恩四轴（色板/白色角色/光机制/题材）在 `sorolla.md §3.1` 与 `zorn.md §3.1「vs 索罗拉」` **逐条一致**（compressed mirror：同组四轴、反向取值、互为边界） | observation/supported | `dossiers/sorolla.md:86-92`（vs 佐恩四轴 + 互查记录）；`dossiers/zorn.md:95`（vs 索罗拉四轴）；`modules/zorn.md:76`（互引）；`ops/GOALS.md:90`（A-94「四轴逐条一致」）；AUDIT `coverage-manifest.json:zorn_mutual_check_four_axes_consistent=true` | `[归纳]`（分工条款）+ `[史料]`（AUDIT 产物/GOALS 登记） | 本轮按 assignment「noted」登记 |
| 30 | LS-ZORN-N3 | 「色板宽度」轴单主（N3）；索不借四色封闭、佐不借全光谱 | fact/supported | `dossiers/sorolla.md:92`；`dossiers/zorn.md:95`；`conflicts.md:311`（N3 轴所有权表） | `[归纳]` | 组合纪律 |
| 31 | LS-MONET-ENVELOPE | vs 莫奈「大气包络轴单主」；莫奈 P3 只许弱档、索不得引入包络 | fact/supported | `dossiers/sorolla.md:79-85`（四轴 + 组合纪律）；`modules/sorolla.md:66`（越界警报①） | `[归纳]` | 第一写死条款 |
| 32 | LS-OVERRUN-5 | 越界警报 5 条：雾色→莫奈/透纳；四色封闭→佐恩；暗背景→卡拉瓦乔；平面组织→马奈；天气事件→透纳 | fact/supported | `dossiers/sorolla.md:109`；`modules/sorolla.md:66` | `[归纳]` | 可判读换模块判据 |

<a id="db-source-line-68"></a>
## F. 冲突 / 漂移（沿用 AUDIT，不升级、不修仓库）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 33 | LS-CONFLICTS-NOT-SPECIFIC | C-05/C-09/C-12 并非索罗拉专属：conflicts.md **零 sorolla/索罗拉 提及**，三条是 Lane-B 通用注记（引用未悬空但「重点」过度） | observation/supported | `conflicts.md:36,40,43`（总表）、`:109-121,164-176,203-214`（详节）；AUDIT `coverage-manifest.json:conflicts_rows_checked.C05_C09_C12_are_sorolla_specific=false` / `sorolla_specific_C_rows=0`；`RESULT.md §42-46` | `[归纳]`（AUDIT 结论） | 不写成「索罗拉专属冲突」 |
| 34 | LS-NEAR-MISS-DRIFT | near-miss 口径漂移：module L79 / dossier §0 写「8 对」，conflicts.md §4 实 **11** 编号行（#9–#11 "2026-10-16 补"） | observation/conflict | `modules/sorolla.md:79`；[sorolla.md](../../dossiers/sorolla.md) §0/§8.3；`conflicts.md:341-357`；AUDIT `RESULT.md §42-44` / `claim_evidence_map.md:101` | `[归纳]`（AUDIT 登记） | 交 CONFLICT/RULE lane；本 lane 照录 |
| 35 | LS-C05-SIDE | 索「长笔一笔定型、不分解」与 C-05「只有渐变」是对侧；组合需显式分层 | observation/supported | `dossiers/sorolla.md:188`（§8.2-4）、`:82`；`conflicts.md:109-121` | `[归纳]` | 规则层，非实验验证 |
| 36 | LS-C09-MOTION | §8.2-7 运动规则（≤3 px/帧、天气恒定）不并入 C-09；本地 motion-graphics grep sorolla 零命中 | observation/supported | `dossiers/sorolla.md:191,195`（§8.2-7 / §8.3 检索结果）；`conflicts.md:164-176` | `[归纳]` | 属下一步 motion 线 |

<a id="db-source-line-77"></a>
## G. 反例 / scope 边界（mechanism_notes §5、learning_path §8）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 37 | LS-COUNTEREXAMPLE | §4 P1/§8.2-1 与「无雾无晨昏」 vs 2 张暗调室内件 + 《¡Triste herencia!》(1899)：结论规则不被推翻、只收窄为正午高照度档 | observation/supported | `dossiers/sorolla.md:395`（§B-3）、`:369-372`（§12-8）；AUDIT `coverage-manifest.json:counterexample_attempt` / `RESULT.md §36,§8` | `[归纳]`/`[inference]` | AUDIT 已下结论；无新缺陷 |
| 38 | LS-NO-IMAGE-SEEN | 13 张公开图 `image_seen` 未发生；「13/13 PD」为声明标签事实；外部 license 页未重核 | fact/supported | AUDIT `coverage-manifest.json:images_public_note` / `rights_review.md` / `RESULT.md §48-52` | `[史料]`（AUDIT 登记） | 本 lane 不目检、不升级 |
| 39 | LS-WORKS-12 | §12 共 10 件临摹/学习清单；作品与权利沿用现有记录，不新增、不重新取证 | fact/supported | `dossiers/sorolla.md:337-380`（§12）、`:21-26`（§0 关键作品 5 件）；`_images/manifest.md`（13 行） | `[史料]`（作品）/ `[归纳]`（练习映射） | 阶梯一/二/三引用见 C 段 |

<a id="db-source-line-85"></a>
## H. 交付物 / A-30 形状 / 等级边界

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 40 | LS-A30-8-SECTIONS | [learning_path.md](learning_path.md) 为 A-30 §8.1 八节形状（前置知识/重点作品/要观察机制/具体练习/可观察结果/常见失败/下一步/使用边界） | fact/supported | `01-AUDIT.md:269-273`（§8.1）、`learning_path.md §1-§8` 标题 | `[史料]`（spec）+ `[归纳]`（本 lane 结构） | 练习标建议练习、不写已证实学习收益 |
| 41 | LS-HT-GRADE-SEPARATION | [how-to-think.md](how-to-think.md) 严格分栏、`[推测]`=0、无从画面推心理；每步带等级 | observation/supported | `how-to-think.md §0/§1/§3`；`00-GOAL.md:9`；dossier §0 `:7`；corpus header `:6` | `[归纳]`（结构） | 反心理推断清单 6 条 |
| 42 | LS-PRACTICE-UNVERIFIED | 全部练习 = 建议练习；学习收益未经人评，`human_review=not_applicable` | fact/supported | `01-AUDIT.md:273`；`learning_path.md §4 抬头/§5`；`mechanism_notes.md §7`；`receipt.json:human_review` | `[归纳]`（spec） | 不写「已证实学习收益」 |
| 43 | LS-7-FILE-CONTRACT | 本 lane 7 文件 = 5 内容产物（RESULT/learning_path/how-to-think/mechanism_notes/claim_evidence_map）+ runner_receipt.json + receipt.json | fact/supported | 内部证据 547a47a7d5e9884b（未公开；来源记录由维护者保留） 实存文件；`RESULT.md §3`；`receipt.json:artifacts`（5 件 kind 齐备 required_artifact_kinds：result_summary/learning_path/mechanism_notes/claim_evidence_map） | `[史料]`（本 lane 产物） | how_to_think 为 A-30 追加登记 |

---

<a id="db-source-line-96"></a>
## 汇总

- 论断总数 **43**：A 输入 7 · B 前置 6 · C 机制 8 · D 1909 锚点 7 · E 分工/mirror 4 · F 冲突 4 · G 反例 3 · H 交付物 4。
- `support_status`：`supported` = 42，`conflict` = 1（#34 near-miss 漂移，如实登记为冲突而非抹平），`unverified`/`not_applicable` = 0。`[推测]` 计数 = **0**。
- 外部来源本轮 `access_status=unknown`（未重访）；1909 两卷本 OCR 行号级的外部实核由 **AUDIT-sorolla（ACCEPTED）** 承担，本 lane 复用其结论（#22），不冒充亲自实核。本机文件 `available`；原图像素目检 = 0。
- 所有数值型阈值均为 `[归纳]`；所有作者言语均为 `[reported speech]/[contemporary record]` 转记并带 corpus/OCR 行号；练习均为建议练习。逐条 locator 可回源至 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f0089523…`（只读）与 内部证据 92dd4fcf8110568c（未公开；来源记录由维护者保留）（ACCEPTED 产物）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
