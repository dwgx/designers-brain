<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-sargent；原正文 SHA-256 `373d337987f7691d987fe16cd2b43747ecfb4dd1db74b228052b2d045a5e841d`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-sargent — claim_evidence_map

> goal `Designers-Brain-Upgrade-20261115` · task `LEARN-sargent`（A-30）· source `f008952365a77e140cbda3f3959d43ef000f9a22`（只读）· 上游 `AUDIT-sargent` **ACCEPTED** · status `submitted`
> 每 claim 1 行：`claim_id · grade · support_status · locator（文件:节:行号 + 子串）· basis`。等级沿用原档词表（`[自述]`/`[reported speech]`/`[contemporary record]`/`[史料]`/`[研究]`/`[归纳]`）；`[归纳]` 为本项目操作规则，**不冒充史料/自述/像素实测**；`[推测]` 计数 = 0。
> 本 lane **不重审 ACCEPTED 审计**：凡引 AUDIT 结论均标注其产物 hash 与判定（partial/supported），照实携带 open 项。`retrieved_bytes_sha256` / `read_scope` / `access_status` 的完整字段见 `receipt.json` `claims[].source_refs`；本文件用「路径:L行」简写定位，全部行号为本机 `nl -ba` 实测。

<a id="db-source-line-7"></a>
## 覆盖

| 区块 | 行数 |
|---|---|
| §A 输入/依赖/边界（C-INPUT / C-DEP / C-OPEN） | 8 |
| §B brief 强调①：布上湿上光即兴 + 预写锚点（C-M1-* / C-M2-*） | 12 |
| §C brief 强调②：Zorn pending NOT closed（C-ZORN-*） | 6 |
| §D brief 强调③：Charteris 1927 OCR 底本（C-CHAR-*） | 5 |
| §E brief 强调④：KB 尺寸漂移 + 近失配 drift（C-DRIFT-*） | 4 |
| §F §4/§8.2/§12 机制与练习映射（C-RULE-* / C-PRACTICE-*） | 10 |
| §G 等级纪律 / 失败条件 / 反例（C-GRADE-* / C-FAIL-*） | 8 |
| **claims_total** | **53** |

按正文 53 个 `C-*` 条目逐条重数（2026-11-18 文本计数更正）：`supported` **39** / `partial` **9** / `not_applicable` **5**。这是历史条目标签的准确汇总，不重新裁决任何 claim；原摘要 45/6/2 未与正文对应。Zorn 条目的旧标签属于旧时点，其现行处置按本文件 F20-B 收口注记；2 次 HTTP 429 与 `image_seen=0` 也不升级为新回访/新看图。

---

<a id="db-source-line-24"></a>
## §A 输入 / 依赖 / 边界

- **C-INPUT-01** `[史料]` `supported` — 三件冻结输入 hash 开工 `sha256sum` 实测与 内部证据 8bdce9d3eb3461f8（未公开；来源记录由维护者保留）
  - locator: [sargent.md](../../modules/sargent.md) = `3f9df9ad…8b62`；[sargent.md](../../dossiers/sargent.md) = `9d03a6f7…d272`；[sargent.md](../../dossiers/_corpus/sargent.md) = `32bc85d5…5a68`
  - basis: 与 内部证据 a51fb647946f8ced（未公开；来源记录由维护者保留） `input_hashes[]`（L17/L22/L26）及 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） 逐字一致；本 lane 开工实跑（见 `runner_receipt.json` cmd-1）。
- **C-INPUT-02** `[史料]` `supported` — 次要输入 hash 实测
  - locator: [conflicts.md](../../../../cross/conflicts.md) = `314a24da…bbef`；[zorn.md](../../dossiers/zorn.md) = `6ad27b47…0fca`；[zorn.md](../../modules/zorn.md) = `5302cd97…0377`；`ops/GOALS.md` = `2727d1f0…1144`
  - basis: 与 AUDIT-sargent 契约 L41/L53/L57/L49 登记值一致。
- **C-DEP-01** `[史料]` `supported` — 上游 `AUDIT-sargent` 为 ACCEPTED，可复用不重审
  - locator: 内部证据 94a562fdfb879499（未公开；来源记录由维护者保留） `status=accepted`；`:L632-652` `review.verdict=accepted` / `reviewer_actor_id=ReviewGateAUDIT-sargent(glm-5.3-flash)`；内部证据 91f878a11a2686c5（未公开；来源记录由维护者保留） 抬头 `Verdict: PASS`；`AUDIT-sargent/review-gate-receipt.json`
  - basis: 作者=`AuditSargent`、审者独立（`independent_from_author=true`）；13 个 reviewed_artifact_hashes 与 artifacts 一致。产物 hash：`RESULT.md`=`816d346b…1731c`、[claim_evidence_map.md](claim_evidence_map.md)=`c1a04dd4…83cfcf`、`receipt.json`=`8be5a3d1…3e3b`、`coverage-manifest.json`=`c24c010d…167d`。
- **C-DEP-02** `[史料]` `partial` — 上游 AUDIT 的 10 个 partial / 1 unverified 判定照实携带、不静默升级
  - locator: `AUDIT-sargent/RESULT.md:L25`（`claims_total=84` = 73 supported / 10 partial / 1 unverified）；`:L59-L64`（§4③）、`:L92-L99`（§8 unresolved）
  - basis: 本 LEARN 不改写 AUDIT 产物、不把 partial 升 supported；`review-evidence.md §1` reviewer 独立复算 73/10/1 = 84 ✓。
- **C-OPEN-01** `[归纳]` `supported` — 本片为 A-30 §8.1 八节形状
  - locator: `package/01-AUDIT.md:L269-L273`（§8.1：前置知识/重点作品及来源/要观察的机制/具体练习/可观察结果/常见失败/下一步/使用边界）；[learning_path.md](learning_path.md) §1–§8 标题
  - basis: 8 节齐全；[learning_path.md](learning_path.md) 抬头声明「练习效果未由人完成或评价时明确为建议练习，不写已证实学习收益」（`01-AUDIT.md:L273`）。
- **C-OPEN-02** `[归纳]` `supported` — 仓库只读、无子代理、无凭据、仅写 staging
  - locator: 内部证据 dff4e60c3b71bb59（未公开；来源记录由维护者保留）（内部证据 c5bba421d3e152eb（未公开；来源记录由维护者保留）、`required_artifact_kinds`）；`receipt.json` `spawns_allowed=false`、`allowed_write_paths`
  - basis: 与 LEARN-monet/vermeer 同构；`status=submitted` 不经 accepted 语义门。
- **C-OPEN-03** `[归纳]` `not_applicable` — 全部练习 = 建议练习，学习收益未经人评（design_candidate）
  - locator: `01-AUDIT.md:L273`；[learning_path.md](learning_path.md) 抬头 + §4 抬头 + §8 B1；`receipt.json` `human_review.status=not_applicable`
  - basis: 0 条「已证实学习收益」表述；`human_review=not_applicable`。
- **C-OPEN-04** `[归纳]` `supported` — `status=submitted` / `review=null` / 作者不自接受
  - locator: `receipt.json` `status` / `review` / `author_actor_id=LearnSargent`；`verify-receipt.py:L20-L23` 仅结构门
  - basis: 与 LEARN-monet 同口径；`execution_dedup_key=null`（submitted 允许 null，见 schema），独立审者由 review gate 承担。

<a id="db-source-line-51"></a>
## §B brief 强调① — 布上湿上光即兴 + 预写锚点机制

> 本区块全部为**本项目 `[归纳]` 机制标签**串联的可回源操作纪律；档案/语料从未用「布上湿上光即兴」「预写锚点」二词（`learning_path.md K2/K3`、`how-to-think.md §0`、`mechanism_notes.md §3`）。行文中不得写成「萨金特提出『预写锚点』」。

- **C-M1-01** `[史料]` `supported` — 「布上/一次流」：alla prima、无预备素描、直接上布铺色、保留速写新鲜感
  - locator: `modules/sargent.md:L19`（`alla prima, painted in one flow, no underdrawing`）；`dossiers/sargent.md:L51`（§2-1，[R14]/[R11]）、`L322`（§11.1 卡罗勒斯画室）；`L200`（§7-2 Heilbrunn `preserve the freshness of the sketch`）
  - basis: 双源 [R14]×[R11]；AUDIT [claim_evidence_map.md](claim_evidence_map.md) SA-2-01 supported。
- **C-M1-02** `[归纳]` `supported` — 「湿/单层」：色层 ≤3、无多层罩染、干笔拖痕 ≥2
  - locator: `modules/sargent.md:L44`（§8.2-2）、`L32`（`--no academic underpainting`）；`dossiers/sargent.md:L254`（§8.2-2）、`L39`（§1-6 暗薄亮厚）
  - basis: §8.2 阈值 `[归纳]`、未像素实测（`L262`）；AUDIT SA-1-06 supported。
- **C-M1-03** `[reported speech]` `supported` — 「上光/亮暗最后」：中调起步、向暗部推进、最后处理最亮与最暗，避开 false accents（价值分类法）
  - locator: `_corpus/sargent.md:L13-L17`（#1，Charteris 1927 行 1693–1702，转记 William James，`[reported speech]`）；`dossiers/sargent.md:L52`（§2-2）、`L39`（§1-6）、`L137-L139`（§5-2）
  - basis: 一手转记；AUDIT [claim_evidence_map.md](claim_evidence_map.md) SA-2-02 supported、`RESULT.md:L43` 抽样 L1693-1702 命中。
- **C-M1-04** `[史料]`+`[归纳]` `supported` — 「即兴/速度与风险」：El Jaleo 数日完成、Madame X 赌注、水彩 = 「在紧急情况下尽力而为」
  - locator: `dossiers/sargent.md:L71`（§3-3）、`L59`（§2-9）、`L445`（§12-9）；`_corpus/sargent.md:L178-L183`（#22，Charteris L4747–4750）；`L92-L97`（#11 书信 `[self-written]`）
  - basis: [R13]/[R10]/[R5]；AUDIT SA-3-03 / SA-2-09 supported。
- **C-M1-05** `[归纳]` `supported` — M1 可判定自查 = §8.2-1/-2/-3
  - locator: `modules/sargent.md:L43`（≥60% / ≤2% 短边 / 方向族 3–6）、`L44`（≤30 笔 / 干笔 ≥2 / 色层 ≤3）、`L45`（V≥0.85 ≥25% / S≥0.6 ≤10% 连通域 1–3）
  - basis: 与 dossier `L253-L255` 逐字一致；`L52` 标 `[归纳]`。
- **C-M1-06** `[归纳]` `partial` — 「即兴 ≠ 无准备」的失败条件（只练 M1 丢 M2）
  - locator: `learning_path.md §6 F1`；`_corpus/sargent.md:L13-L17`（false accents）；`how-to-think.md D4`
  - basis: 规则层推导，非实验验证；标 partial 以避免把「机制配对」写成已验证学习律。
- **C-M2-01** `[reported speech]` `supported` — 价值锚 / 起形锚（色斑到位、线定角度、垂线、构图「像偶然」但素描稿须严肃规划）
  - locator: `_corpus/sargent.md:L27-L33`（#3，Charteris L8870 / L8852–8854）、`L35-L41`（#4，Charteris L8945 / L8948–8952）；`dossiers/sargent.md:L54`（§2-4）、`L75`（§3-7）、`L145-L147`（§5-4）
  - basis: 课堂记录（Haley，RA 1897–1900）；AUDIT SA-2-04 supported。
- **C-M2-02** `[reported speech]`+`[自述]` `supported` — 距离锚（退后看全画、羊径、翻过来夹腋下看）
  - locator: `_corpus/sargent.md:L19-L25`（#2，Charteris L8929–8934）、`L92-L97`（#11，Charteris L3024–3033，`[self-written]`）；`dossiers/sargent.md:L53`（§2-3）、`L25`（#2 注「羊径」）、`L157-L159`（§5-7）
  - basis: #2 为课堂记录、#11 为书信，二者分栏不混写；AUDIT SA-2-03 / [claim_evidence_map.md](claim_evidence_map.md) SA-Q11。
- **C-M2-03** `[史料]` `supported` — 光窗锚（《康乃馨》每日几分钟、事先架画具摆模特、花谢换假花）
  - locator: `dossiers/sargent.md:L204`（§7-6 Tate 2023 原文）、`L58`（§2-8）、`L408-L411`（§12-2）；`L411`（「只画 3 次、每次 5 分钟」）
  - basis: [R7] 创作过程页；AUDIT `RESULT.md §6` 记该页 HTTP 200、但主作品页 mauvish 正文未取到 = partial（诚实保留）。
- **C-M2-04** `[自述]`+`[史料]` `supported` — 社交装置锚（先看悬挂位置/审衣橱/定装束；卡门西塔派对先查地板/地毯/吊灯）
  - locator: `_corpus/sargent.md:L107-L113`（#13，Charteris L5522–5530，`[self-written]`）；`dossiers/sargent.md:L56`（§2-6 8–10 次坐/脸一次坐完/审衣橱/最后选画框）、`L72`（§3-4）
  - basis: 书信原文 + [R11]；AUDIT SA-3-04 supported。
- **C-M2-05** `[归纳]` `supported` — 「预写锚点」= 五类锚点结构（价值/起形/距离/光窗/社交装置）为本项目机制标签
  - locator: `learning_path.md K3`；`how-to-think.md D1-D3`；`mechanism_notes.md §3 M2`
  - basis: 由 C-M2-01..04 归纳；**非史料术语**；dossier `L7` 明言「凡涉内心如何一律降级为可执行操作规则」，本标签即操作规则化产物。
- **C-M2-06** `[归纳]` `not_applicable` — 3 阶梯练习按「先锚后即兴」设计（design_candidate）
  - locator: `learning_path.md §4` 阶梯一（锚点卡→一次流）/ 阶梯二（光窗预置→3×5 分钟）/ 阶梯三（高调+边界自律）；`how-to-think.md §1` D1–D8
  - basis: 建议练习，未经人评；不写「已证实学习收益」。

<a id="db-source-line-92"></a>
## §C brief 强调② — Zorn 收口 pending NOT closed（open，不收口）

> **2026-11-18 收口核验**：本节为收口前状态记录——dossier §4 L124、module L66/L72/L74、zorn dossier §3.1 L81 已于 2026-11-16 按 F20-B 收口（对齐完成）。C-ZORN-05/06 的「pending NOT closed」判定已过时；行保留不删。

- **C-ZORN-01** `[归纳]` `supported` — 四轴内容已同名对齐（可比较、可用）
  - locator: `dossiers/sargent.md:L94-L100`（§3.1 第三写死条款：色板宽度/炫技位置/题材·社会装置/光，`L95-L100`）；`dossiers/zorn.md:L81`（§3.1 第一写死条款，`L82-L87`）；`modules/zorn.md:L74`
  - basis: 与 `roster.md §1` 佐恩条目（原文 `[推测]` 级）按 wave 规程四轴同名对齐；AUDIT `RESULT.md:L59` 判「四轴内容已同名对齐」。
- **C-ZORN-02** `[史料]` `partial` — dossier `L94` 与 GOALS 记「收口」，但状态标记残留
  - locator: `dossiers/sargent.md:L94`（「2026-10-16 收口」）、`L545`（自审 D「已确立…与 zorn.md §3.1 四轴同名对齐」）、`L550`（下一步「与佐恩条款已按四轴同名对齐」）；`ops/GOALS.md:L105`（A-109「sargent×zorn 收口」）、`L113`（A-117「sargent L117 冻结区」）、`L75`（A-69「vs 佐恩预写待对齐」）、`L91`（A-95「同名对齐，回改待收口」）
  - basis: 「记收口」与「状态标记未回改」并存 → partial；AUDIT [claim_evidence_map.md](claim_evidence_map.md) SA-PEND-03 判 partial。
- **C-ZORN-03** `[史料]` `partial` — 三处「预写/(future)」状态标记 + `L117` 冻结区例外未回改
  - locator: `modules/sargent.md:L66`（「越界**佐恩**档（**预写**）」）、`L72`（「× 马奈（**future**）」）、`L74`（「× 佐恩（**future**）…佐恩档案落地后按 wave 规程回改对齐」）；`dossiers/sargent.md:L124`（§4 越界警报③「佐恩档（**预写**）」）、`L117`（P2 行 = GOALS A-109/A-117 标注冻结区例外）
  - basis: AUDIT `RESULT.md:L60-L64`、[claim_evidence_map.md](claim_evidence_map.md) SA-4-BOUND(partial) / SA-PEND-03(partial)；本片不改写。
- **C-ZORN-04** `[史料]` `partial` — `zorn.md:L81` 把「预写→对齐回改」收口**外派**
  - locator: `dossiers/zorn.md:L81`（「其『预写→对齐回改』收口由主脑/萨金特侧按 wave 规程执行，本档案先行自证一致」）
  - basis: 与 C-ZORN-02 的「已收口」直接矛盾；AUDIT `RESULT.md:L63`、审者 `review-evidence.md §3` 第 4 点。
- **C-ZORN-05** `[史料]` `supported` — 独立审者四点互读确认 **Zorn pending NOT closed**
  - locator: 内部证据 3539bef273271a5b（未公开；来源记录由维护者保留）（4 点表：dossier L94 / module L66 / module L72-L74 / zorn L81 → 「Zorn pending 确认 NOT closed」）；内部证据 f57098a0c7a54a27（未公开；来源记录由维护者保留）；`AUDIT-sargent/receipt.json review.verdict=accepted`
  - basis: reviewer-run 逐处原文实读；AUDIT `RESULT.md §8-1` 列 unresolved #1「佐恩回改待收口…交卡同步/冻结区裁定 lane」。
- **C-ZORN-06** `[归纳]` `supported` — 本片把 Zorn 作为 open 项携带（5 文件一致、不收口、不升级）
  - locator: `learning_path.md K6 / §4 阶梯三 / §6 F6 / §7-2 / §8 B4`；`how-to-think.md D8 / §3.5 / §5`；`mechanism_notes.md §6②`；`RESULT.md`；本文件 §C
  - basis: 与 AUDIT 判定一致；「预写/(future) 状态标记」（本区块）与 §B「预写锚点」（学习标签）**同形异义，全文不混用**。

<a id="db-source-line-113"></a>
## §D brief 强调③ — Charteris 1927 全文 OCR 证据底本

- **C-CHAR-01** `[史料]` `supported` — 底本 = Charteris《John Sargent》(1927) 全文 OCR（archive.org `johnsargent00char` 的 `_djvu.txt`）
  - locator: `_corpus/sargent.md:L5`（底本声明）、`L7`（#1–#24 逐条行号定位）、`L8`（引用格式建议）；`dossiers/sargent.md:L287`（§9 R10）、`L206`（§7-8）、`L461`（自审 A）
  - basis: AUDIT `RESULT.md §4①` 判 supported；`ops/GOALS.md:L75`（A-69）同记。
- **C-CHAR-02** `[史料]` `supported` — 两份 OCR 字节全等、20301 行、4 处抽样命中、archive.org metadata 200
  - locator: 内部证据 d05d88b8083be3f5（未公开；来源记录由维护者保留）（scratch ↔ `_private/books` 字节全等 20301 行；抽样 L1693-1702 / L5338-5341 / L11045 / L11064）；`review-evidence.md §2`（`cmp` 字节全等、`wc -l`=20301、L5338–5341 含 `No, I do not judge, I only chronicle`、L11045 含 `On the evening of the 14th`）；`RESULT.md §6 #5`（archive.org metadata HTTP 200 / 83395B / 27 files）
  - basis: reviewer 独立复现；AUDIT [claim_evidence_map.md](claim_evidence_map.md) SA-PEND-01 supported。
- **C-CHAR-03** `[史料]` `supported` — 语料 30 条类型分布 + #1–#24 行号可复核
  - locator: `_corpus/sargent.md:L246`（统计：本人书写 9 / 转记·课堂记录 13 / 同时代记录 6 / 后世评价 2；24 条经 Charteris 行号定位）、`L7`；内部证据 a6a747fade0f93cb（未公开；来源记录由维护者保留）（30 条逐条 EN 原文 + 中译 + 类型）
  - basis: AUDIT `RESULT.md:L25,L42`、审者 `review-evidence.md §1` 复算 30 / 9-13-6-2 ✓。
- **C-CHAR-04** `[史料]` `partial` — #8「lose a friend」= 二手转引、Charteris 全文零命中；更早原始记录未回查
  - locator: `_corpus/sargent.md:L68-L73`（#8，来源 Bentley & Esar 1951，标注「原书未读，Charteris 全文无此句——二手转引，已查」）；`dossiers/sargent.md:L304-L305`（§10-3/4）、`L472`（自审 B6 WEAKENED）、`L548`
  - basis: AUDIT `RESULT.md:L44` 弱化项、`RESULT.md §6 #4`（en.wikiquote 命中 1951 转引 → 降级成立）；本片保持弱化、不升级。
- **C-CHAR-05** `[史料]` `partial` — 外部取证诚实 partial（2×Met 429、Tate 创作过程正文未取到）
  - locator: 内部证据 306231c85ea0acbc（未公开；来源记录由维护者保留）（7 次 fetch：5×200 + 2×429）、`§8-3`；`coverage-manifest.json` `external_fetches_detail`；`review-evidence.md §4.3`
  - basis: 2 次 429 为诚实 unverified/partial，不推翻 dossier §9 的 2026-10-16 本机实测 ✅；本 lane 不重访、不补直连。

<a id="db-source-line-131"></a>
## §E brief 强调④ — KB 尺寸漂移 + near-miss 计数漂移

- **C-DRIFT-01** `[史料]` `supported` — 图像 KB 口径漂移（artist-local 明细未回改）
  - locator: `_images/sargent/MANIFEST.md:L38,L40`（ladyrose 371 KB / hammersley 393 KB）；`_images/manifest.md:L1787,L1796`（492 KB / 443 KB）；磁盘实测 503520 B / 453348 B
  - basis: AUDIT `RESULT.md §5`、[claim_evidence_map.md](claim_evidence_map.md) SA-DRIFT-02、`review-evidence.md §4.2` 三项独立复现；替换前旧值。
- **C-DRIFT-02** `[史料]` `supported` — 漂移起因 = 2 张误取件已替换、许可/文件名/来源无误
  - locator: `dossiers/sargent.md:L470`（自审 B4：contact sheet 抓出 2 张画框+签名细节照 → Met 官方 CC0 全画版 DT1151/DT2064）；`_images/sargent/MANIFEST.md:L51,L57`；`_images/manifest.md:L322,L325`；`ops/GOALS.md:L75`（A-69 ②）
  - basis: AUDIT `RESULT.md §4②` 判 supported、[claim_evidence_map.md](claim_evidence_map.md) SA-PEND-02；本片 `image_seen=0`，不声称本轮看过像素。
- **C-DRIFT-03** `[史料]` `supported` — near-miss 计数漂移（8 对 vs 11 行）
  - locator: `modules/sargent.md:L80`（「18 条 C + N1–N9 + near-miss 8 对」）；`conflicts.md §4 L347-L357`（实测 11 编号行，#9–#11 标 2026-10-16 补）
  - basis: AUDIT `RESULT.md §5`、[claim_evidence_map.md](claim_evidence_map.md) SA-DRIFT-01、审者 `review-evidence.md §4.1`；旧口径残留，交 CONFLICT/RULE lane。
- **C-DRIFT-04** `[归纳]` `supported` — 两项 drift 均登记为 open，不改写仓库/不升级为事实错误
  - locator: `AUDIT-sargent/RESULT.md §5,§8-2`；`learning_path.md §2 注 / §7-3 / §8 B5`；`mechanism_notes.md §6④`
  - basis: 只涉明细口径；conflicts.md **无 sargent/zorn 具名 C 行**（AUDIT SA-CONF-01），C-05/08/09/12 为通用轴条款、引用有效。

<a id="db-source-line-146"></a>
## §F §4 / §8.2 / §12 机制与练习映射

- **C-RULE-01** `[归纳]` `supported` — §4 六参数三档 + 默认值 + 用法
  - locator: `dossiers/sargent.md:L114-L123`（P1 70% / P2 55% / P3 60% / P4 55% / P5 50% / P6 油画；`L123` 用法 P1+P3 定「是不是」、P2+P5 定「社交档 vs 单色档」、P6 工作流参数）；`modules/sargent.md:L56-L65` 逐字一致
  - basis: AUDIT [claim_evidence_map.md](claim_evidence_map.md) SA-4-P1..P6 supported；`expansion.md §4.3 规则 5`。
- **C-RULE-02** `[归纳]` `supported` — §8.2 八条规则阈值 + 自查列
  - locator: `dossiers/sargent.md:L253-L260`（§8.2-1..8）、`L262`（阈值 `[归纳]`、未像素实测、1–6 条与 §3.1 同轴）；`modules/sargent.md:L43-L50`
  - basis: AUDIT `RESULT.md §1` 逐字校验；`_extract.py --check` 228/228 中 Sargent 占 3 项。
- **C-RULE-03** `[归纳]` `supported` — 四条越界警报（马奈/委拉斯开兹/佐恩/卡拉瓦乔）
  - locator: `modules/sargent.md:L66`；`dossiers/sargent.md:L124`
  - basis: ③「佐恩档（预写）」的状态标记问题见 §C（open）；AUDIT SA-4-BOUND partial。
- **C-RULE-04** `[归纳]` `supported` — C-05/08/09/12 为通用轴条款、conflicts.md 无具名行
  - locator: `conflicts.md:L36,L39,L40,L43`（§1 总表）、`L109,L149,L164,L203`（§2 详条）、`L305-L320`（N1/N3/N4）；`modules/sargent.md:L75`；`dossiers/sargent.md:L108,L268-L270`
  - basis: AUDIT [claim_evidence_map.md](claim_evidence_map.md) SA-CONF-01 supported、`RESULT.md §5`；C-08/C-09 萨金特 = 定格侧。
- **C-RULE-05** `[归纳]` `supported` — §12 10 件临摹清单（作品/看什么/学什么/怎么练）
  - locator: `dossiers/sargent.md:L399-L453`（§12，10 件 + `L453` 组合练习建议）、`L401`（「练习条目为 `[归纳]`，作品信息为 `[史料]`」）
  - basis: 本片阶梯一/二/三分别取 §12-1/10/4、§12-2/7/3、§12-5/6/9；不新增作品。
- **C-RULE-06** `[归纳]` `supported` — §8.1 生成后自查三件事 + 三档先跑
  - locator: `dossiers/sargent.md:L247`（P1 70% + P3 60% + P4 55% 起步）、`L248`（①笔触可见且一次性 ②光单一主导且暗部透明 ③空间浅但仍立体）、`L249`（组合预检写死）
  - basis: 用作 D7 收笔回检与 M1 自查口径。
- **C-PRACTICE-01** `[归纳]` `not_applicable` — 阶梯一 anchored one-flow portrait（design_candidate）
  - locator: `learning_path.md §4 阶梯一`；`dossiers/sargent.md:L403-L406,L448-L451`；`_corpus/sargent.md:L13-L17,L27-L33,L35-L41`
  - basis: 建议练习；锚点卡为本项目设计、非史料物件。
- **C-PRACTICE-02** `[归纳]` `not_applicable` — 阶梯二 pre-set light window + step-back（design_candidate）
  - locator: `learning_path.md §4 阶梯二`；`dossiers/sargent.md:L408-L411,L433-L436,L413-L416,L204,L248`
  - basis: 建议练习；「只画 3 次、每次 5 分钟」沿用 §12-2 `L411`，不声称学习收益。
- **C-PRACTICE-03** `[归纳]` `not_applicable` — 阶梯三 high-key single-accent + boundary discipline（design_candidate）
  - locator: `learning_path.md §4 阶梯三`；`dossiers/sargent.md:L423-L426,L428-L431,L443-L446,L124,L94`
  - basis: 建议练习；组合自律含 C-ZORN open 注记。
- **C-PRACTICE-04** `[归纳]` `supported` — 全部练习明确「未由人完成或评价」
  - locator: `01-AUDIT.md:L273`；[learning_path.md](learning_path.md) 抬头 + §4 抬头 + §5 注 + §8 B1；`receipt.json` `human_review`
  - basis: 0 条「已证实学习收益」；grep 可复算（所有「已证实」均为否定/免责语境）。

<a id="db-source-line-179"></a>
## §G 等级纪律 / 失败条件 / 反例

- **C-GRADE-01** `[史料]` `supported` — 萨金特无理论著作；凡「内心如何」降级为可执行操作规则
  - locator: `dossiers/sargent.md:L7`（口径写在前面的特殊性）、`L130`（§5 口径）、`L76`（§3-8「无宣言、无理论」）；`_corpus/sargent.md:L5,L6`
  - basis: 本片 `[推测]` 计数 = 0；`00-GOAL.md:L9` 红线。
- **C-GRADE-02** `[归纳]` `supported` — 严格分栏（自述 / 转记 / 史料·研究 / 归纳 / 推测禁用）
  - locator: `how-to-think.md §0,§5`（D1–D8 每步等级汇总表）；[learning_path.md](learning_path.md) 抬头等级口径；`dossiers/sargent.md:L5`（证据分级定义）
  - basis: D1–D8 全部「为什么」可回指 corpus/dossier/conflicts 具体行；无心理推断。
- **C-GRADE-03** `[归纳]` `supported` — 阈值 `[归纳]`、未对原作像素测量（分母＝假想参考帧）
  - locator: `modules/sargent.md:L52`；`dossiers/sargent.md:L262,L308`；`AUDIT-sargent/coverage-manifest.json`（`image_seen=0`）
  - basis: AUDIT `RESULT.md §8-5` unresolved；本片不补像素实测、不升级。
- **C-FAIL-01** `[归纳]` `supported` — F1 即兴≠无准备 / F2 笔触抹平 / F3 暗部近黑 / F4 高饱和铺满 / F5 运动模糊 / F6 Zorn 误收口 / F7 等级混淆 / F8 回源纪律
  - locator: `learning_path.md §6` F1–F8（逐条带 locator）；`mechanism_notes.md §1-§4` 失败条件列
  - basis: 与 AUDIT `RESULT.md §5/§8`、conflicts.md 一致；F6 专指 C-ZORN-*。
- **C-FAIL-02** `[归纳]` `partial` — §4 反例尝试（AUDIT SA-COUNTER-01）：P2 弱档近单色收窄 × 佐恩四色封闭收窄 → 色板宽度轴单主无法裁决谁持收窄权
  - locator: `AUDIT-sargent/RESULT.md §7:L89-L90`（判「规则空白，非事实错误」，未做像素/生成实测）；[claim_evidence_map.md](claim_evidence_map.md) SA-COUNTER-01；`dossiers/sargent.md:L117`（P2 弱档）、`L95`（色板宽度轴）
  - basis: AUDIT 判 `[inference]` 规则空白、不升级为视觉机制结论；本片照实携带、不改判。
- **C-FAIL-03** `[史料]` `partial` — 诚实弱化项照实保留（不静默消除）
  - locator: `dossiers/sargent.md:L306`（卒日 14/15 双口径）、`L307`（1915-vs-1916）、`L302-L303`（NPG/ISG 直连受阻）、`L310`（水彩 2000+ 单一来源）、`L304`（更早原始记录未回查）；`AUDIT-sargent/RESULT.md §8`
  - basis: AUDIT 逐项登记 unresolved；本片在 `learning_path.md §6 注 / §7-5 / §8 B5` 携带。
- **C-FAIL-04** `[归纳]` `supported` — 权利/图像真实性未升级（14 张权利字段可判、许可真实性与视觉内容未升级）
  - locator: `AUDIT-sargent/RESULT.md §3,§8-4`（`henry_james_1913.jpg` NPG 第三方主张注记；Commons/Met 许可页未逐站复核；无 `image_seen`）；`rights_review.json`
  - basis: 本 lane `image_seen=0`、外部 URL 未重访；作品/权利沿用现有记录。
- **C-FAIL-05** `[归纳]` `supported` — 同形异义不混用：「预写锚点」（§B 学习标签）vs「预写/(future)」（§C 状态标记）
  - locator: `how-to-think.md §0` 同形异义警告 + `D8`；`mechanism_notes.md §6②`；`learning_path.md K3 注 / K6 / §3 观察纪律`
  - basis: 全文两词分栏；避免把 Zorn 状态残留误读为学习机制、或把学习标签误当收口动作。

---

> 源 receipt 的代表性 `claims[]` 与其公共投影 `source-claims.json` 含 **10** 个 claim；本文列 **53** 个细分条目，二者不是一一对应。细分条目保留各自 locator/basis；代表性 source_refs 的 `retrieved_bytes_sha256` / `read_scope` / `access_status` / `version` 见 `source-claims.json`，原 receipt 由维护者归档。原 locator 属源版本，不能自动证明当前文件同一行号仍命中；本轮未回写旧 AUDIT 或旧 receipt。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
