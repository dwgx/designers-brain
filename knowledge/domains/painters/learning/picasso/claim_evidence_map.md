<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-picasso；原正文 SHA-256 `63d6510ba7f8f61d445dfaa9e8ee4d110ecfb80912aa8e4ee7b5903a926a5c8c`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-picasso · claim_evidence_map.md

> 任务 `LEARN-picasso`｜作者 LearnPicasso（hy4free）｜日期 2026-11-15｜kind: `claim_evidence_map`
> 作用：把 [learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md) 中**每一条实质 claim** 落到可判定 locator（dossier / corpus / 模块卡 / conflicts / 已 ACCEPTED 的 AUDIT 分片），并标证据级与支持状态。沿用 AUDIT claim_evidence_map.md 的 locator 纪律，不重审、不改仓库。
> 仓库基线：内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22`，**只读**。
> 判定口径（沿用 AUDIT）：supported / partial / conflict / unverified；「来源存在」≠「来源支持」；「结论是项目操作规则」≠「史实」；`[归纳]` 配方 ≠ 毕加索自述。

---

<a id="db-source-line-10"></a>
## 0. 输入指纹（sha256 实测 2026-11-15，开头已核对一致）

| source_id | 路径（repo 相对 / staging 相对） | sha256（前 12 / 全值见 receipt.json） |
|---|---|---|
| PS-CARD | [picasso.md](../../modules/picasso.md) | `201e4397ad08…` |
| PS-DOSSIER | [picasso.md](../../dossiers/picasso.md) | `ec4ca31cdc3e…` |
| PS-CORPUS | [picasso.md](../../dossiers/_corpus/picasso.md) | `b61049952a4a…` |
| PS-CONFLICTS | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96cc…` |
| PS-AUDIT-CLAIM | 内部证据 3485fbe8aeb88ab7（未公开；来源记录由维护者保留） | `00a72a7a37b5…` |
| PS-AUDIT-COV | 内部证据 d48e4f8350b9e483（未公开；来源记录由维护者保留） | `8d2592759bde…`（= 本 receipt `input_hashes` 中的 AUDIT coverage-manifest） |
| PS-AUDIT-RESULT | 内部证据 fd8cb9c982996ddb（未公开；来源记录由维护者保留） | `84663b89e6fd…` |
| PS-AUDIT-RIGHTS | 内部证据 ffa519fde5a94a3d（未公开；来源记录由维护者保留） | `10b2b18b7a15…` |
| PS-GOAL | `<package>/01-AUDIT.md`（A-30 §8.1 形状） | 包内文件；形状条文 `L269–273` |
| PS-GOALS | `ops/GOALS.md`（A-35 目标层） | `2727d1f079e1…` |

> locator 写法：`PS-xxx L<行>`；AUDIT 分片用「§节 / CE-xxx」。所有行号以本次实测 `grep -n` 为准（见 runner_receipt.json commands）。

---

<a id="db-source-line-29"></a>
## 1. learning_path.md 的 claim → locator

<a id="db-source-line-31"></a>
### 1.1 前置知识 / 主轴（§1、§3）

| claim_id | claim（摘自 learning_path） | locator | 证据级 | 支持状态 |
|---|---|---|---|---|
| LP-C01 | 四条量化轴：全帧唯一色相 ≤5（分析 ≤3）+ 明度级 ≥6、平均饱和度 ≤35%、ΔE≤6≥85%、平面化零渐变 | PS-CARD `L59`（§8.2-1）、`L64`（§8.2-6）、`L74`（§4 P3）；PS-DOSSIER `L172`、`L177`、`L78` | `[归纳]`（项目操作规则） | supported（规则存在且可寻址） |
| LP-C02 | 色相/明度/饱和度/ΔE 四量是「可测自查」的基础 | PS-CARD `L59`/`L64`；PS-DOSSIER §8.2 `L170–179` | `[归纳]` | supported |
| LP-C03 | 分析/综合立体主义分期差别决定 P3 强弱档与色数放宽 | PS-DOSSIER `L164`（§8.1 中文说明）；PS-DOSSIER §11.2 `L252` | `[归纳]`/`[研究]` | supported |
| LP-C04 | 「自述/他人记录/回忆录追记」非同一证据级 | PS-DOSSIER §11.3 `L314`；PS-CORPUS `L121`、`L147`、`L154`；PS-AUDIT-CLAIM §4（CE-A35-*） | `[史料]`/`[归纳]` | supported |
| LP-C05 | 全帧统计 vs 分区掩膜两种判分；C-06 全帧均值型不可拆、C-18 可分区 | PS-CONFLICTS C-06 `L130–135`、C-18 `L292–296` | `[归纳]` | supported |
| LP-C06 | 视觉指纹 12 条（面片化边缘/近单色/平涂/浅浮雕/多视点等） | PS-DOSSIER §1 `L25–36`（`L25` 面片、`L27` 近单色、`L29` 平涂、`L30` 浅浮雕、`L31` 多视点） | `[研究]`（馆方）/ `[归纳]`（9/12） | partial（「馆方描述存在」≠「操作规则已验证」，见 AUDIT CE-STRUCT-3） |

<a id="db-source-line-42"></a>
### 1.2 重点作品及来源（§2）

| claim_id | claim | locator | 证据级 | 支持状态 |
|---|---|---|---|---|
| LP-C07 | W1《卡恩维勒肖像》1910 / AIC 111060 / 单色棕灰 ≤5 色相 / 面片明度差 ≥8 / 3–5 锚点 | PS-DOSSIER §12.4 `L361–365`（含 https://www.artic.edu/artworks/111060/…） | `[史料]` 著录 + `[归纳]` 练习 | supported（沿用现有记录） |
| LP-C08 | W2《三个音乐家》1921 / MoMA 78630 / 拼图平涂 / 中心亮暗环 / ΔE 自查 | PS-DOSSIER §12.6 `L371–375`（含 MoMA URL）；PS-CARD §8.2-5 `L63` | `[史料]` + `[归纳]` | supported |
| LP-C09 | W3《老吉他手》1903–04 / AIC 28067 / 近单色蓝绿 / 5 级明度草图 | PS-DOSSIER §12.1 `L346–350` | `[史料]` + `[归纳]` | supported |
| LP-C10 | W4《有藤椅的静物》1912 / 巴黎毕加索博物馆 / 实物材料 + 字母 | PS-DOSSIER §12.5 `L366–370` | `[史料]` + `[归纳]` | supported |
| LP-C11 | 3 张公开图为 CC0（CMA Open Access）、本分片未目检图像 | PS-AUDIT-COV §2.2 `L55–64`；PS-AUDIT-RIGHTS | `[归纳]` 审计层 | supported（沿用 AUDIT），但 `image_seen` 为空 |

<a id="db-source-line-52"></a>
### 1.3 练习阶梯与可观察结果（§4、§5）

| claim_id | claim | locator | 证据级 | 支持状态 |
|---|---|---|---|---|
| LP-C12 | 练习 1 单色族色盘：≤5 色相 / ≥6 明度级 / ≤35% 饱和度 / 64px 剪影 | PS-CARD `L59`/`L66`；PS-DOSSIER §12.1 `L349`、§12.4 `L364` | `[归纳]` 配方 + `[建议练习]` | supported（配方存在）；**练习效果 unverified** |
| LP-C13 | 练习 2 平涂拼装：40–120 面片 / ≤3 角度族 / ΔE≤6≥85% / 明度中心 ≥8 / 64px 锚点 | PS-CARD `L60–66`；PS-DOSSIER §12.6 `L374`、§2-1 `L40`、§2-3 `L42` | `[归纳]` + `[研究]` + `[建议练习]` | supported（规则存在）；效果 unverified |
| LP-C14 | 练习 3 主体/背景分区（C-18）：主体掩膜 + 分区判分 + ≥70% 面积比 | PS-CONFLICTS C-18 `L292–296` | `[归纳]` 项目操作规则 | supported（方案存在）；**未做组合实验验证** → partial |
| LP-C15 | C-16 嵌入点：反约束「没有高光的平涂」须带适用域或删除 | PS-CONFLICTS C-16 `L266–270` | `[归纳]` | supported |
| LP-C16 | 练习全为「建议练习」，效果未经真人完成/评价，不写已证实学习收益 | PS-GOAL §8.1 `L273`；PS-AUDIT-RESULT §九 `L84–87`（human_review 口径） | 契约口径 | supported（契约要求） |
| LP-C17 | 「可观察结果」仅为按 §8.2 可自测的产出特征，非学习成效 | PS-CARD §8.2 `L59–66`；PS-GOAL §8.1 `L273` | `[归纳]` + 契约 | supported |

<a id="db-source-line-63"></a>
### 1.4 常见失败 / 下一步 / 边界（§6–§8）

| claim_id | claim | locator | 证据级 | 支持状态 |
|---|---|---|---|---|
| LP-C18 | F1 模型默认用渐变画立体，负向段须保留 | PS-DOSSIER §8.1 `L166`；PS-CARD `L30–36` | `[归纳]` | supported |
| LP-C19 | F3 C-06 空交集 / 轴单主 / 均值型不可拆 | PS-CONFLICTS `L130–134` | `[归纳]` | supported |
| LP-C20 | F5 C-18 同帧双标准互相判违规 / 分区解 | PS-CONFLICTS `L292–296` | `[归纳]` | supported；未验证（同 LP-C14） |
| LP-C21 | F6 回忆录转述不得当自述（Q20/Q21 已标、Q10/Q11/Q15 未标） | PS-CORPUS `L121`/`L147`/`L154`/`L68`/`L74`/`L100`；PS-AUDIT-CLAIM §4 CE-A35-2 | `[归纳]` 审计 | supported |
| LP-C22 | F7「来源存在」≠「来源支持」（URL 列 §9 ≠ 已访问；书名+页码 ≠ 原书已读） | PS-AUDIT-COV §3 `L92`；PS-AUDIT-CLAIM §5 `L92–95` | `[归纳]` 审计 | supported |
| LP-C23 | 待验证：C-06/C-18 解未做组合实验、三书原刊未直核、3 图未目检、练习无人评 | PS-AUDIT-RESULT §八 `L75–80`、§五 `L48–52`；PS-GOAL §8.4 `L308–310` | `[归纳]` 审计 + 契约 | supported（如实挂账） |
| LP-C24 | A-30 形状（前置知识→…→使用边界）与「建议练习不冒充学习成效」 | PS-GOAL §8.1 `L269–273`；PS-GOAL §9 表 `L322` | 契约 | supported |
| LP-C25 | 四条量化轴 / 三条冲突为 `[归纳]` 项目操作规则、非史实、可被 A-12 推翻 | PS-CARD 行内 `[归纳]` 标 `L72–77`；PS-AUDIT-RESULT §六 `L62` | `[归纳]` | supported |

---

<a id="db-source-line-78"></a>
## 2. how-to-think.md 的 claim → locator

| claim_id | claim | locator | 证据级 | 支持状态 |
|---|---|---|---|---|
| HT-C01 | 三种标签（`[自述]`/`[自述·转述]`/`[归纳]/[推测]`）读法与「不从画面外观编造心理」 | PS-AUDIT-CLAIM §输入指纹/§5；PS-GOAL `L9`、§8.1 `L271`；03-RESEARCH-AGENDA `L125` | 契约 + `[归纳]` 审计 | supported |
| HT-C02 | Q13 是语料中唯一 `[self-written]` 手记 | PS-CORPUS `L88–92`；PS-AUDIT-CLAIM CE-Q13 `L42`、CE-A35-2 | `[自述]`（条）/ 审计 | supported |
| HT-C03 | dossier §3 十条标 `[自述]` 但底本为 1923/1935 他人记录/译本 → 口径张力 | PS-DOSSIER §3 `L55–66`；PS-CORPUS Q1–Q24 类型标；PS-AUDIT-CLAIM CE-STRUCT-1 `L61` | `[归纳]` 审计 | **conflict（口径）**，如实记录 |
| HT-C04 | 步骤 1「先锁色域牺牲颜色表现力」及失效条件（C-06） | PS-CARD `L59`/`L30–36`/`L73`；PS-DOSSIER §2-4 `L43`、`L164`；PS-CONFLICTS `L130–134` | `[归纳]` 配方 + `[研究]` | supported |
| HT-C05 | 步骤 2「先锁锚点牺牲整体可读性」及「先定锚点再炸形体」 | PS-DOSSIER §2-1 `L40`、§2-9 `L48`；PS-CARD `L66`/`L72`/`L77`；PS-DOSSIER `L165` | `[研究]` + `[归纳]` | supported |
| HT-C06 | 步骤 3 面片/多视点/轮廓断口阈值 | PS-CARD `L60–62`；PS-DOSSIER §1-1 `L25`、§1-6 `L30`、§1-7 `L31`、§2-2 `L41`；PS-DOSSIER §3.1 `L70` | `[归纳]` + `[研究]` | supported |
| HT-C07 | 步骤 4 平面化/平涂（ΔE≤6≥85%、零渐变）及 C-16/C-18 失效条件 | PS-CARD `L64`/`L74`/`L63`；PS-DOSSIER §1-5 `L29`、§1-12 `L36`、§2-3 `L42`、`L166`；PS-CONFLICTS `L266–270`/`L292` | `[归纳]` + `[研究]` | supported |
| HT-C08 | 步骤 5 组合口径：轴所有权/反约束适用域/分区掩膜三选一 | PS-CONFLICTS C-06 `L123–135`、C-16 `L258–271`、C-18 `L285–297`；PS-CARD `L79–81`；PS-CONFLICTS `L303` | `[归纳]` | supported；解未验证（同 LP-C14） |
| HT-C09 | 步骤 6「引用前过证据卫生关」是本分片 `[归纳]` 工序 | 本分片自产（how-to-think §2.3）；依据 PS-DOSSIER §11.3 `L314`、PS-CORPUS `L121`、PS-AUDIT-CLAIM §5 | `[归纳]`（本分片） | supported（工序存在）；非史料 |
| HT-C10 | Gilot 书中对话为十年后追记「重构」、按 `[自述·转述（回忆录）]` 使用、Q20/Q21 逐条标注 | PS-DOSSIER §11.3 `L314`；PS-CORPUS `L121`/`L147`/`L154` | `[史料]`/`[研究]` 档案 + 项目口径 | supported |
| HT-C11 | 引用须带「回忆录转述」标注并降置信度 | PS-CORPUS `L121`；PS-AUDIT-CLAIM CE-A35-1 `L83` | 项目口径 | supported |
| HT-C12 | A-35 降级警示在四处同时存在（GOALS/档案/语料/索引） | PS-GOALS `L49`；PS-DOSSIER `L230`/`L314`；PS-CORPUS `L121`/`L147`/`L154`；INDEX `L21`；PS-AUDIT-RESULT §五 `L39–46`、PS-AUDIT-CLAIM §4 `L80–88` | `[归纳]` 审计（ACCEPTED） | supported |
| HT-C13 | 覆盖缺口：Q10/Q11/Q15（v1 区）未带 memoir 标 | PS-CORPUS `L68`/`L74`/`L100`；PS-AUDIT-CLAIM CE-A35-2 `L84`；PS-AUDIT-RESULT `L49` | `[归纳]` 审计 | **partial**（如实记录，不静默补标） |
| HT-C14 | 编号误指：唯一 hand-written 是 Q13，corpus `L6` 写「Q11 手记」自相矛盾 | PS-CORPUS `L6` vs `L88–92`/`L114`；PS-AUDIT-RESULT `L50`、PS-AUDIT-CLAIM CE-STRUCT-2 | `[归纳]` 审计 | supported（矛盾存在） |
| HT-C15 | INDEX 2/3/2 为出现次数而非条目数；条目数=1/2/1 | INDEX `L21`；PS-AUDIT-CLAIM CE-STRUCT-2 `L62`；PS-AUDIT-RESULT `L51` | `[归纳]` 审计 | supported |
| HT-C16 | 三书原刊原文未直核、24 条无一逐字原刊 verified | PS-DOSSIER `L213`、PS-CORPUS `L179`、PS-AUDIT-RESULT `L52`/`L78`；PS-AUDIT-CLAIM CE-STRUCT-4 `L64` | `[研究]` 缺口声明 | **unverified（如实保留）** |
| HT-C17 | 名言不收编：B-4 OVERTURNED、B-2 WEAKENED 改挂 1935 Zervos | PS-AUDIT-RESULT §七 `L67`；PS-DOSSIER 自审 B `L403–434` | `[归纳]` 审计 | supported |
| HT-C18 | 证据卫生 6 步工序（查类型标/分级/不用于心理复原/不收编名言/不升级/挂账） | 本分片自产（how-to-think §2.3）；依据同上 HT-C10…HT-C17 | `[归纳]`（本分片） | supported（工序存在） |
| HT-C19 | §1 每步带证据级 + 「何时失效」列；「为什么」落到参数/馆方描述而非心理 | 本分片结构；依据 PS-GOAL `L9`、PS-CARD 行内 `[归纳]` 标 | `[归纳]` 设计 | supported |
| HT-C20 | 练习效果/学习收益无人评；human_review=not_applicable | PS-AUDIT-RESULT §九 `L86`；PS-GOAL §8.4 `L308–310` | 契约 | supported |

---

<a id="db-source-line-105"></a>
## 3. mechanism_notes.md 的 claim → locator

| claim_id | claim | locator | 证据级 | 支持状态 |
|---|---|---|---|---|
| MN-C01 | §4 P1–P6 参数表（弱/中/强/默认）逐字一致于模块卡与档案 | PS-CARD `L70–77`；PS-DOSSIER `L74–81`；PS-CARD `L5`（`_extract.py --check` 逐字校验声明） | `[归纳]`（行内标） | supported（文本存在；本次未复跑校验器，见边界） |
| MN-C02 | §8.2 规则 1–8 阈值（含 ★ 四条 emphasis） | PS-CARD `L59–66`；PS-DOSSIER `L172–179` | `[归纳]` | supported |
| MN-C03 | §8.2-5 ↔ P5、§8.2-6 ↔ P3 的对应为原文标明 | PS-DOSSIER `L177`；PS-CARD `L64` | `[归纳]` | supported |
| MN-C04 | P1→练习 2 / P2→练习 1 / P3→练习 2+3 / P4→W4 / P5→练习 1+2 / P6→练习 1+2 的映射 | 本分片自产映射（mechanism_notes §1）；依据 PS-CARD `L70–77`、PS-DOSSIER §12 `L346–397` | `[归纳]`（本分片设计） | supported（映射存在，非史实） |
| MN-C05 | 各参数/规则失败条件（渐变退化、高饱和顶穿、C-16 误伤、C-18 双标准、锚点全失…） | PS-DOSSIER `L166`；PS-CONFLICTS `L130`/`L266`/`L292`；PS-CARD `L66` | `[归纳]` | supported |
| MN-C06 | C-06 毕加索侧 = §8.2-1 全帧均值 ≤35%，N4 不可拆侧 | PS-CARD `L59`；PS-CONFLICTS `L128`/`L134`；PS-AUDIT-CLAIM CE-C06 `L72` | `[归纳]` | supported |
| MN-C07 | C-16 毕加索侧 = §8.2-6 平涂判据；解 = 反约束带适用域 | PS-CARD `L64`；PS-CONFLICTS `L264`/`L268–270`；PS-AUDIT-CLAIM CE-C16 `L73` | `[归纳]` | supported |
| MN-C08 | C-18 毕加索侧 = §4 P3 + §8.2-6；解 = 分区掩膜 + 分区判分 + ≥70% 面积比 | PS-CARD `L74`/`L64`；PS-CONFLICTS `L290`/`L292`/`L294`/`L296`；PS-AUDIT-CLAIM CE-C18 `L74` | `[归纳]` | supported；未验证 |
| MN-C09 | 三条冲突为 `[归纳]` 项目操作规则、非史实、可被 A-12 推翻；AUDIT 裁定「现状成立、无需改写」 | PS-AUDIT-RESULT §六 `L54–62`；PS-CONFLICTS `L303` | `[归纳]` 审计 | supported |
| MN-C10 | near-miss #4 取 ≤0.35 / #5 取 ≤5，与 emphasis 一致 | PS-CARD `L86`；PS-CONFLICTS §4 表 | `[归纳]` | supported |
| MN-C11 | C-15 金属/金彩材质层豁免口径（P4 失败条件引用） | PS-CONFLICTS `L244–256` | `[归纳]` | supported |
| MN-C12 | C-06/C-18 解未做组合实验验证；只产出可判分方案，不宣称 E2/E4 通过 | PS-AUDIT-RESULT §八 `L80` | `[归纳]` 审计 | supported（如实挂账） |
| MN-C13 | 图像未目检 / 三书未直核 / 练习无人评 / 写路径仅 staging / 无子代理 / 无凭据 | PS-AUDIT-COV §4 `L97`；PS-AUDIT-RESULT §九 `L84–87`；本分片契约 | 契约 | supported |

---

<a id="db-source-line-125"></a>
## 4. 逐条 locator 覆盖核对

- 本表 claim 数：learning_path **25**（LP-C01…C25）+ how-to-think **20**（HT-C01…C20）+ mechanism_notes **13**（MN-C01…C13）= **58 条**；**58/58 带 locator**，指向 PS-CARD / PS-DOSSIER / PS-CORPUS / PS-CONFLICTS / PS-AUDIT-* / PS-GOAL / PS-GOALS，无「无说明空格」。
- 证据级分层：`[自述]` 仅用于 Q13 与 dossier §3 的项目口径（附冲突注）；`[自述·转述]` / `[自述·转述（回忆录）]` 用于 corpus 转述条；`[史料]`/`[研究]` 用于馆方著录与描述；`[归纳]` 用于 §4/§8.2/冲突/审计/本分片设计；`[推测]` **本分片未使用**（不从画面外观编造心理）。
- 支持状态如实分布：多数 supported（规则/记录存在）；口径张力 **conflict**（HT-C03）、覆盖缺口 **partial**（HT-C13）、原刊未核 **unverified**（HT-C16）、组合解 **partial/未验证**（LP-C14、MN-C08/MN-C12）——均不静默升级。
- **不冒充**：未把「馆方描述存在」写成「操作规则已验证」（LP-C06 partial）；未把「URL 列 §9」写成「已访问」；未把「转录记录存在」写成「逐字原话已核」；未把 `[归纳]` 配方写成毕加索自述；未把建议练习写成已证实学习收益。

<a id="db-source-line-132"></a>
## 5. 边界声明

- 本文件为 `[归纳]` LEARN 映射层，沿用 AUDIT（已 ACCEPTED）的证据判定，不重审、不改仓库、不新增外部抓取。
- 行号以本次 `grep -n` 实测为准；模块卡 §8.1/§8.2/§4 与档案逐字一致是**档案声明**（PS-CARD `L5`），本次**未复跑** `_extract.py --check`（只读 LEARN 分片，不冒充已验收；AUDIT RESULT §九 `L84` 同口径）。
- 本 LEARN 分片只读仓库、写路径仅 内部证据 3470f8168a15b3c4（未公开；来源记录由维护者保留）、`spawns_allowed=false`、产物无凭据、`submitted` ≠ `accepted`。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
