<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-rembrandt；原正文 SHA-256 `4890be94c930f1088bd3a3110933e0a43c654e082351e13bf278e3eb7cf263e9`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-rembrandt — claim / evidence 图（逐 claim 带定位）

> 本图给 [learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md) 里**每一条实质 claim** 配 `文件 : 节 : 行` 定位（dossier / corpus / 卡 / conflicts / AUDIT 产物 / RF）。沿用 **ACCEPTED** 审计 内部证据 d5250627a2448454（未公开；来源记录由维护者保留） 的 locator 纪律，**不重审、不改 repo**。
> 基线 `f008952365a77e140cbda3f3959d43ef000f9a22`（repo READ-ONLY）。等级照录 dossier L4：`[自述]/[史料]/[研究]/[归纳]/[推测]`。
> **support_status 只评「本机档案内自洽 / 定位可寻址 / 类型正确 / 与 ACCEPTED 审计一致」**，不评外部原文真伪、不评学习成效（AUDIT 同口径）。
> 输入 hash（开工实测，见 `RESULT.md` §0）：card `a2108ab3…`、dossier `f59aab6d…`、corpus `031ad9a0…`、conflicts `314a24da…`、GOALS `2727d1f0…`；AUDIT RESULT `9c078474…`、claim_evidence_map `97dc6327…`、coverage-manifest `b1179299…`、fetch_index `f05b4ec6…`、review-evidence `070ac159…`。

---

<a id="db-source-line-10"></a>
## §A 分工条款 / 证据分级（三文件共用前提）

| claim_id | 内容 | 等级 | 定位 | support |
|---|---|---|---|---|
| C-DIV | 伦勃朗 = 光的**连续衰减 + 心理**（心理化光斑）；卡拉瓦乔 = 光的**开关 + 物理**；本档 P1 强档 = 连续衰减，其 P1/P3 强档整条禁用 | `[归纳]`（口径级，写死）/ AUDIT `validated_rule` | dossier L6 / L70 / L108；卡 L93；§8.1 L252；AUDIT `result.json` RE-DIV-01；[claim_evidence_map.md](claim_evidence_map.md) R-§4-DIV | supported |
| C-GRADE | 证据级定义（自述/史料/研究/归纳/推测） | 口径 | dossier L4；AUDIT [claim_evidence_map.md](claim_evidence_map.md) L3 | supported |
| C-BASE | 基线 = `f0089523…`，repo READ-ONLY，仅 内部证据 37afdf379f4b3624（未公开；来源记录由维护者保留） 可写 | 事实（本机） | AUDIT receipt `baseline_id` / `allowed_write_paths`；本 shard `sha256sum` 实测 | supported |
| C-SELF-EXISTS | 伦勃朗**有**真实自述（不同于维米尔的结构性无自述）：dossier §5 十条、corpus 17 条；`[self-written]` 11 / reported 2 / contemporary 5（#11 双标 → 18 tags/17 rows） | `[自述]`/事实 | dossier §5 L113-L170；corpus L163 自计；AUDIT R-§5-10 / R-CQ-01..17 / review-evidence.md §2 | supported |
| C-SELF-NO-THRESHOLD | **无任何自述规定数值阈值、决策顺序或「连续衰减」机制词**；所有阈值为 `[归纳]` | `[归纳]`（边界） | dossier L76 / §10-5 L320 / §8.2 L265；卡 §8.2 末注 | supported |

---

<a id="db-source-line-22"></a>
## §B 光暗分区机制（mechanism_notes §A / learning_path §3 / how-to-think D1-D3,D5）

| claim_id | 内容（含数值） | 等级 | 定位 | support |
|---|---|---|---|---|
| C-FALL-1 | 单光源 + 暗部塌陷：光自侧上方进入、画面内不现光源、背景 ≤ 全帧最亮 15%、暗部保微层次 | `[研究]` + `[归纳]` | dossier §1-1 L32（[R4][R1]）；卡 L9；AUDIT R-§1-01 | supported |
| C-SPOT-MAP | 面部亮斑地图（签名）：3–7 处（强档 4–7）集中于前额/鼻梁/颧骨/下巴/唇周、鼻梁最窄亮条、眼窝必暗、表情读不准 → 「活着的思考的心智」 | `[研究]`（NG 原话）+ `[归纳]`（3–7 区间） | dossier §1-2/3 L33-34（[R1]）；§4 P2 L83-86；§8.2-1 L256；卡 L10-11；**RF1** NG 页 `2a920f21…` 命中 `patterns of light and shadow`/`living, thinking mind`；AUDIT R-§1-02/03、R-RF1 | supported |
| FALLOFF-CONT | 连续衰减（非开关）：全画无硬切边、沿主光方向单调下降、过渡带 ≥8px、亮斑弥散 ≥15px（P1 强档）；§8.2-2 单调 ≥80%、跳变 >12% 阶跃边界 ≤1% | `[归纳]` | dossier §1-4 L35 / §4 P1 L78-81 / §8.2-2 L258；卡 L12、§8.2-2；AUDIT R-§1-04 | supported |
| C-SHADOW-ACTIVE | 暗部活性：暗区(<0.15) std ≥2/255（非死黑）、纯黑(≤0.03) ≤5%、暗部色相暖 H20–50°、亮暗比 ≥8:1 | `[归纳]` | dossier §8.2-3 L260 / §8.2-6 L263 / §4 P3 L88-91；卡 §8.2-3；AUDIT R-§4-P3 | supported |
| C-IMPASTO | 厚涂/排线做光：厚度地图与光斑地图重合（亮部厚涂立体化、暗部薄画草图态）；蚀刻排线＝同一明暗逻辑的线条版（加线压暗） | `[研究]`（形态）+ `[归纳]`（阈值） | dossier §1-6/8 L37/L39、§2-2/3/7 L48/49/53（[R3][R8][R10]）；§8.2-4/5 L261-262；AUDIT R-§1-06/08 | supported |
| C-ONE-LINE | 机制一句话：把卡拉瓦乔的「开关」升级成「调光器」（连续化/心理化/材质化） | `[归纳]`（本项目概括） | dossier §6.3 L146；AUDIT R-§4-DIV | supported |
| C-P1-P6-ALIGN | §4 P1-P6 ↔ §8.2 规则 1/2/3(P2/P1/P3)、5(P6) 对齐；与 caravaggio §8.2 互斥使用 | `[归纳]` | dossier §8.2 末注 L265/L110；卡 §8.2 末注；AUDIT R-§8-2 | supported |

---

<a id="db-source-line-36"></a>
## §C 群像叙事机制（mechanism_notes §B / learning_path §3-M5/§4-阶梯2 / how-to-think D4）

| claim_id | 内容 | 等级 | 定位 | support |
|---|---|---|---|---|
| C-GROUP-DOING | 群体叙事「正在做事」：组画 ≥2 个可读进行时动作，而非排排站静态肖像；光聚焦叙事关键物（队长手势/女孩） | `[研究]`（单源 CC-4）+ `[归纳]`（≥2 动作） | dossier §1-9 L40（[R2]）、§3-3 L64、§7-4 L204、§12-4 L438-441；**RF2** SK-C-5 `08721ed2…` 命中 `first to paint figures in a group portrait actually doing something`；AUDIT R-§1-09、R-RF2 | **supported（保持单源口径，不写死「第一个」为定论）** |
| C-GROUP-GAZE | 视线/手势分配：《解剖课》七人各看不同方向（[R42]）、《呢商》全体抬头（[R47]）、单人 `immersed in thought` | `[研究]` | dossier §1-10 L41（[R1][R4]）、§12-2 L430 / §12-8 L465 | supported |
| C-GROUP-DRAMA | 戏剧瞬间「一束光＋一个动作」《伯沙撒》；`Deep shadows and shafts of brilliant light`；冷色点火例外 | `[研究]` | dossier §1-1 L32、§12-3 L433-436（[R4]） | supported |
| C-GROUP-SELF | 自述侧「运动/情感最大值」`die meeste ende die naetuereelste beweechgelickheijt` = **唯一被学界公认的画论性自述**；Binstock 兼指内外 | `[自述]` | dossier §3-1 L62 / §5-1 L115-120；corpus #4 L36-42；AUDIT R-§3-01、R-CQ-04（CC-2 双转录一致） | supported |
| C-GROUP-COUNTER | 同代反证 Van Hoogstraten 1672「比全场都强，但我宁愿他多放点光」→ 暗部策略当年即激进 | `[reported speech]/[contemporary record]` | corpus #11；dossier §7-9 [R15] | supported |
| C-GROUP-INTERFACE | M-G2 光＝叙事聚光灯是「光暗分区 × 群像叙事」的咬合点（§2-1 先光后暗序列） | `[归纳]` | dossier §2-1 L47；§12-4 L439「光只允许落在 3 个关键物上」 | supported |

---

<a id="db-source-line-49"></a>
## §D 自述 10 条 / 语料 17 条（how-to-think §1 / mechanism_notes §B.1-M-G5）

| claim_id | 内容 | 等级 | 定位 | support |
|---|---|---|---|---|
| C-S1 | 1639-01-12 致 Huygens：`die meeste ende die naetuereelste beweechgelickheijt`（最充分最自然的运动/情感） | `[自述]` | corpus #4；dossier §5-1；Worp No.2020 p.425 × Strauss（CC-2） | supported |
| C-S2 | 1639-01-27「挂在强光里、站得远远地看」 | `[自述]` | corpus #5；dossier §5-2 / §3-2；Worp No.2032 | supported |
| C-S3/S4 | 1636-02 两信「画廊有强光」「忍不住献上最新作品」 | `[自述]` | corpus #6/#7；dossier §5-3/4 | supported |
| C-S5 | 《逃往埃及》素描自我批注（驴子/头/约瑟玛丽亚）≈ 工作笔记 | `[自述]` | corpus #3；dossier §5-5；remdoc e4525 | supported |
| C-S6 | Van Hoogstraten 转述教学「先把已知的做好」 | `[自述/转述]` | corpus #10；dossier §5-6 | supported |
| C-S7/S8 | Saskia 素描题字 / album amicorum 题词 | `[自述]` | corpus #15/#16；dossier §5-7/8 | supported |
| C-S9 | 1662 致 Ruffo 谈《亚历山大》与 600 弗罗林 | `[自述]` | corpus #8；dossier §5-9 | supported |
| C-S10 | 蚀刻底蜡/停蚀清漆两配方 | `[自述]` | corpus #1/#2；dossier §5-10 | supported |
| C-CORPUS-17 | 17 条语料；`grep -c '^### '`=17、ledger=17、INDEX L31=17、自计 L163=17；self 11/contemp 5/reported 2（#11 双标→18 tags/17 rows） | 事实（本机） | corpus L1-L163；AUDIT R-CQ-01..17、`RESULT.md` §4；review-evidence.md §2 | supported |
| C-CORPUS-GAP | Worp 丢空格规范化、`vouchen`/`voncken` 差异、Huygens 拉丁原稿未直读、remdoc 未回查、英译分歧 | 缺口（不补造） | corpus 末「缺口与待验证」；dossier §10-2/3/8 | supported（登记为缺口，外部真伪 `unverified`） |

---

<a id="db-source-line-66"></a>
## §E near-miss 11 行 reality / L107「8 对」— **known-open（本次点名重点）**

| claim_id | 内容 | 等级 | 定位 | support |
|---|---|---|---|---|
| C-NM-11 | `conflicts.md` §4 near-miss 表**实为 11 编号行**（#1–#11），#9/#10/#11 带「（2026-10-16 补）」 | 事实（本机实测） | [conflicts.md](../../../../cross/conflicts.md) L347-L357；AUDIT R-CF-01；review-evidence.md §4 复现 | supported |
| C-NM-8-STALE | 模块卡 `rembrandt.md` **L107** 仍写「near-miss 8 对」= 补 #9-#11 前的旧计数 → **stale** | 事实（漂移） | [rembrandt.md](../../modules/rembrandt.md) L107；AUDIT R-CF-02（`partial`）；review-evidence.md §4 确认 drift real | **partial**（已知开放，不关闭） |
| C-NM-0HIT | `grep -niE 'rembrandt\|伦勃朗' conflicts.md` = **0 命中**；18 C-row + 11 near-miss 无一涉及本档案 → 对 rembrandt = 空集；`conflicts_rows_checked=29` | 事实（本机） | AUDIT R-CF-01 / RESULT §6；review-evidence.md §4 | supported |
| C-NM-KNOWNOPEN | 本 shard 把 11/8 漂移作为 **known-open 携带**，不修正、不关闭、不改 repo / AUDIT 文件；订正属 CONFLICT / MODULE-CARD owner 与 INVENTORY lane | 口径（本 shard 决策） | AUDIT `receipt.json` unresolved #1；`RESULT.md` §4；[learning_path.md](learning_path.md) §6.1；[mechanism_notes.md](mechanism_notes.md) §C | supported（本 shard 行为声明） |
| C-NM-OTHER | 同属 known-open 的两处漂移：INDEX L31 `17\|12\|3\|6` vs 实测 11/2/5（#11 双标，AUDIT R-CF-03）；dossier §9 [R22] L301「4 文件」vs 6 文件 | 事实（漂移） | AUDIT R-CF-03 / RESULT §6 / review-evidence.md §4 | partial |

---

<a id="db-source-line-78"></a>
## §F RF1-RF4 accepted basis（mechanism_notes §D / learning_path §1.5 / how-to-think D0,D4）

| claim_id | 内容 | 等级 | 定位 | support |
|---|---|---|---|---|
| C-RF-BASIS | 4 次外部回源，HTTP 200、bytes+sha256 记录在 `fetch_index.json`；review-evidence.md §3 逐字节重算 **4/4 match**、RF2 锚句命中 → **accepted basis** | 事实（ACCEPTED 审计产物） | 内部证据 9911a9e595ed5f91（未公开；来源记录由维护者保留）；AUDIT R-RF1..4；review-evidence.md §3 | supported |
| C-RF1 | NG 艺术家页 `2a920f21…`（89,994 B）命中 `patterns of light and shadow`/`living, thinking mind`/`hard to read a precise expression` → §1-2/3 | `[研究]`（外部文本） | AUDIT RE-RF-01 / R-RF1；RF1.bin | supported |
| C-RF2 | Rijksmuseum SK-C-5 `08721ed2…`（299,117 B）命中 `first to paint figures in a group portrait actually doing something` → §1-9/§3-3（仍单源 CC-4） | `[研究]`（单源） | AUDIT R-RF2；RF2.bin | supported（不升级为定论） |
| C-RF3 | Wikipedia `67c5cd63…` 命中 `1606`/`Rembrandt never went abroad` → §0/§3-7 | `[研究]`（三手） | AUDIT R-RF3；RF3.bin | supported |
| C-RF4 | nl.wikipedia Saskia `683f8aa0…` 命中 `22 juni`/`Juliaanse kalender`/`2 juli`/`10 juni`/`ondertrouw` → §11.4 婚期两历并记（A-60 GOALS L66） | `[研究]`（三手） | AUDIT RE-114-01 / R-RF4；`ops/GOALS.md` L66；RF4.bin | supported |
| C-RF-BOUND | RF 只提供外部文本定性佐证；**不重新联网、不重设分母、不把 HTML 文本命中升级为原作像素真值、不把 CC-4 单源升级为定论** | 口径（本 shard 边界） | [mechanism_notes.md](mechanism_notes.md) §D；`RESULT.md` §4 | supported（行为声明） |

---

<a id="db-source-line-91"></a>
## §G 反例 / 练习 / 边界（mechanism_notes §E / learning_path §4 / how-to-think §4）

| claim_id | 内容 | 等级 | 定位 | support |
|---|---|---|---|---|
| C-COUNTER | §4 P1 强档 + §8.2-2 字面施加于《夜巡》1642（队长黑衣 vs 受光手）为具体候选反例 `[inference]`；吸收为 dossier §10 L320 已声明限制，非推翻 | `[inference]` / model_judgment | AUDIT `RESULT.md` §7、[claim_evidence_map.md](claim_evidence_map.md) R-COUNTER、`receipt.json` RE-COUNTER-01；review-evidence.md §5 | supported（判定为 inference + 作用域受限 + 原作像素 `unverified`） |
| C-COUNTER-NEXT | 下一步判别动作 = 参考帧像素测量，属 **A-12 组合实验 lane**，本 LEARN 不越权 | 口径 | dossier §10 L320 / §8.2 L265；AUDIT unresolved #5 | supported |
| C-PRACTICE | 三段练习阶梯（光暗分区 → 群像叙事 → 材质/版画+收口）为**建议练习**，顺序与 §12 L424-476 兼容、不重写 | `[归纳]`（建议） | [learning_path.md](learning_path.md) §4；dossier §12；01-AUDIT.md §8.1 L273 | not_applicable（建议，非事实主张；效果未经人评） |
| C-THRESHOLD-INDUCTION | §4 六参数 + §8.2 七阈值全部 `[归纳]`、未对原作做像素测量 | `[归纳]` | dossier L76 / L265 / §10-5 L320；卡 §8.2 末注；AUDIT R-§4-P1..P6、R-§8-2 | supported |
| C-RIGHTS | 6 张公开图 PD×4 + CC0×2（manifest L75-L80/L997-L1021）；外部许可页真实性与像素 `unverified`（无 image_seen） | 事实 + 缺口 | AUDIT R-RT / RE-RT-02 / `rights_review.md` | supported（字段）/ unverified（外部真值） |
| C-REVIEW | 本产物 `submitted`、`review:null`、`human_review.status=not_applicable`；作者不自接受；本包对 LEARN 未绑定 bound contract | 口径 | 本 shard `receipt.json`；AUDIT receipt unresolved 末条 | not_applicable |

---

<a id="db-source-line-104"></a>
## Per-status 计数（本图，与 receipt.claims 对齐口径）

- 本图 claim 行：§A 5 + §B 7 + §C 6 + §D 10 + §E 5 + §F 6 + §G 7 = **46 行**。
- 判定分布：`supported` 39 / `partial` 2 / `not_applicable` 3 / `unverified` 0 / `conflict` 0（另 C-RIGHTS 为 supported+unverified 双记按 supported 计）；**sum = 44 + 2 = 46** ✓。
- **known-open 不被关闭**：C-NM-8-STALE / C-NM-OTHER = `partial`，原样携带；AUDIT 三处 unresolved #1/#2/#3 的 next_discriminating_action 仍交 owner lane。
- 所有 locator 沿用 AUDIT `all_locators_resolve=true`（498 anchors 经 `audit_scripts.py` 校验在文件行数范围内）；本 shard 新增定位均指向现行文件实际行，未改写任何 repo 文件。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
