<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-durer；原正文 SHA-256 `b368f3a6448c816222e254877e8230a4de233aecaa5d0500996fb1a6474633ee`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-durer — Claim / Evidence Map

> 每条 claim 给「定位(locator) + 读取范围(read_scope) + 证据级」；等级沿用 [durer.md](../../dossiers/durer.md) L5 `[自述]/[史料]/[研究]/[归纳]/[推测]`；推断显式标 `[归纳]`；未找到写成「未找到（已查: …）」。本文件为研究/学习产物，status=`submitted`，作者不自验收。
>
> 证据底本：内部证据 515b6554cf870390（未公开；来源记录由维护者保留）（ACCEPTED，reviewer `ReviewGateAUDIT-durer(glm-5.3-flash)`）。基线 `f008952365a77e140cbda3f3959d43ef000f9a22`。仓库文件与 内部工作区 文件位于不同根，回执 `path_or_id` 用稳定 ID 字符串 + 现场实测 sha256；内部证据 a001209d6061880a（未公开；来源记录由维护者保留） 只对 内部证据 1c1647f455f47eb0（未公开；来源记录由维护者保留） 下 artifacts 做字节复核。
>
> **定位纪律（brief known-open）**：C-07 正本 `conflicts.md` L136–L147 的标称行号 +2/+1 漂移；本文件一律用「文件全路径 + 实测行号 + 子串」，不复制过期行号。

---

<a id="db-source-line-11"></a>
## 输入哈希（本轮现场实测 sha256）

| path_or_id | sha256 | read_scope |
|---|---|---|
| [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | fulltext + citation_context |
| [durer.md](../../modules/durer.md) | `ad49cd7725dbbbbbc8fe18805f687c1d4ce5a0195a87e95588eb14654a55d988` | fulltext |
| [durer.md](../../dossiers/durer.md) | `4f5be577b7c98abc56e98573716aa4de68ac80891d50e4f9f51630ee13cb429e` | fulltext + sections |
| [durer.md](../../dossiers/_corpus/durer.md) | `7364a8eb34803f2042b4922fca077d2758184546964efbbaf1e546849bb5525a` | fulltext（沿用 AUDIT §3，未重开） |
| [hokusai.md](../../dossiers/hokusai.md) | `d03a260ccb0eeab64cb6b008ff6ae4a247456dbb0891c87d172c3708de0e330f` | citation_context |
| 内部证据 62b1281812ff65aa（未公开；来源记录由维护者保留） | `1ecfe5e83d809cfdd69345287255020645483c23fbb16ffd59983b6b096f2405` | fulltext |
| 内部证据 b0261e5b0acba88a（未公开；来源记录由维护者保留） | `8878411e49abec964af80fcf325a5a62f063f31c3206e0b65de32fd9d67f3e01` | fulltext |
| 内部证据 35441cc052a80acf（未公开；来源记录由维护者保留） | `8bfc0ffaa882b0875e86473f7bc2890303220a3430a35cf50f35425eb730e088` | fulltext |
| 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） | `e1ec2d11ed3b3458a2e233a101319ffdf12d253b22562a97d4e25618b1158ce9` | metadata |
| 内部证据 4ae7502a27185a8e（未公开；来源记录由维护者保留） | `7daf31bbac2826179f3d7beecb6e0ec30f9628acd638ce4b3bffc39bafc6c374` | metadata |

---

<a id="db-source-line-28"></a>
## A 组：任务形状与依赖（A-30 / Lane B）

<a id="db-source-line-30"></a>
### A1 · `LEARN-A30-SHAPE`
- claim_kind: observation ｜ support_status: supported
- statement: 本任务为 A-30「76 artist 学习路径」之一，Lane B 要求练习顺序「观察对象→创作决策→机制→参数→一次可做的练习→反例→自检」，且必须含 How to Think（先选什么/牺牲什么/为什么/何时失效）。
- source_refs:
  - `02-EXECUTION-PLAN.md` §Lane B L62–L66（练习顺序 + How to Think）｜ sections ｜ available
  - `01-AUDIT.md` §8.1 L271（8 段 A-30 形状）｜ sections ｜ available
  - `03-RESEARCH-AGENDA.md` L31/L125/R1 L114（76/76 覆盖、每项至少含观察/约束/过程/取舍/练习顺序/失败修正/机制假设/来源待证点）｜ sections ｜ available
  - `tasks-plan.json` `LEARN-durer` 项 L2441–L2483（required_artifact_kinds 四类、allowed_write_paths、dependency `AUDIT-durer`）｜ metadata ｜ available

<a id="db-source-line-39"></a>
### A2 · `LEARN-DURER-DEP-ACCEPTED`
- claim_kind: observation ｜ support_status: supported
- statement: 依赖 `AUDIT-durer` 的落盘回执 status=`accepted`、reviewer `ReviewGateAUDIT-durer(glm-5.3-flash)`、verdict=accepted；本 LEARN 消费其结论，不重审、不改 repo。
- source_refs:
  - 内部证据 f7c4253d78c06128（未公开；来源记录由维护者保留） `status` / `review` / `author_actor_id`（sha `5940721a8d6e5a607ef891edd20e6d19eb65a11b65632cf7b4df95333b6e5d19`）｜ artifact ｜ available
  - 内部证据 6ca49e93e5b4acd1（未公开；来源记录由维护者保留） `review.verdict=accepted` ｜ artifact ｜ available
  - 内部证据 8ec1d8e4dadc2b66（未公开；来源记录由维护者保留） §Verdict: ACCEPT ｜ sections ｜ available

---

<a id="db-source-line-49"></a>
## B 组：版画排线体系（brief 重点 ①）

<a id="db-source-line-51"></a>
### B1 · `DUR-M1-LINE-DENSITY-MONOTONE`
- claim_kind: observation ｜ support_status: supported
- statement: 丢勒机制为「明度→线密度单调映射」`s = lerp(8px, 1.2px, 1−L)`、线宽恒定 1.5–2px；灰由线密度合成、真实灰阶像素=0，禁止实心填充。等级 `[归纳]`（媒介事实 `[研究]`）。
- source_refs:
  - [durer.md](../../modules/durer.md) §8.2-1 **L64**「明度→线密度单调映射…s = lerp(8px, 1.2px, 1−L)」｜ fulltext ｜ sha `ad49cd77…` ｜ available
  - [durer.md](../../dossiers/durer.md) §8.2-1 **L208**（同串）＋§1-10 **L38**「两色媒介的假灰…真实灰阶像素=0」｜ fulltext ｜ sha `4f5be577…` ｜ available
  - 内部证据 62b1281812ff65aa（未公开；来源记录由维护者保留） §1/§5.1（sha 逐字节核对、C-07 丢勒侧回源）｜ sections ｜ sha `1ecfe5e8…` ｜ available

<a id="db-source-line-59"></a>
### B2 · `DUR-M2-M8-HATCH-RULES`
- claim_kind: observation ｜ support_status: supported
- statement: §8.2 共 8 条可判定规则（方向场/层数/收锋/轮廓连续/细节下限/缩略图一致/帧间稳定）与 §4 P1–P6 档位逐字一致；全部标 `[归纳]`、未经真实渲染器跑过。
- source_refs:
  - [durer.md](../../modules/durer.md) §8.2 **L64–L71**、§4 **L77–L82**｜ fulltext ｜ sha `ad49cd77…` ｜ available
  - [durer.md](../../dossiers/durer.md) §8.2 **L208–L215**、§4 **L76–L82**、§10 **L269**「§8.2 8 条未经真实渲染器跑过」｜ fulltext ｜ sha `4f5be577…` ｜ available
  - 内部证据 35441cc052a80acf（未公开；来源记录由维护者保留） §1（card 97 行全文 sha 核对）｜ artifact ｜ sha `8bfc0ff8…` ｜ available

<a id="db-source-line-67"></a>
### B3 · `DUR-HATCH-TECHNIQUE-GRADED`
- claim_kind: observation ｜ support_status: supported
- statement: 排线机制的研究层支撑：burin 推刀 → 线端收锋（量化 `[归纳][UNVERIFIED]`）、交叉排线用方向差做对比、`Adam and Eve` 线密度为早期雕版 2–3 倍。这些为 `[研究]`，不是丢勒自述。
- source_refs:
  - [durer.md](../../dossiers/durer.md) §2-1/2/3 **L44–L46**、§1-3 **L31**（`[UNVERIFIED]` 量化值未实测）｜ fulltext ｜ sha `4f5be577…` ｜ available

---

<a id="db-source-line-75"></a>
## C 组：比例几何机制（brief 重点 ②）

<a id="db-source-line-77"></a>
### C1 · `DUR-GEOMETRY-SELF-WRITTEN`
- claim_kind: observation ｜ support_status: supported
- statement: **唯一有 `[自述]` 支撑的机制层**：「没有几何，无人能成为绝对的艺术家」「方法要写成可教、可复制的书」「以测量超越灵感」「艺术藏在自然里」「美没有终审（相对美）」；配 `[研究]` 的《测量四书》四册、《比例四书》实测数百活人。
- source_refs:
  - [durer.md](../../dossiers/durer.md) §3 **L61–L66**（创作原则 1–6，标 `[自述]`/`[自述/研究]`）｜ sections ｜ sha `4f5be577…` ｜ available
  - [durer.md](../../dossiers/durer.md) §2-8 **L51**、§2-9 **L52**（测量/比例书结构）｜ sections ｜ sha `4f5be577…` ｜ available
  - [durer.md](../../dossiers/_corpus/durer.md)（27 条原话，AUDIT-durer §3 已核 27/27）｜ fulltext ｜ sha `7364a8eb…` ｜ available

<a id="db-source-line-85"></a>
### C2 · `DUR-GEOMETRY-PROPORTION-OBSERVABLE`
- claim_kind: observation ｜ support_status: supported
- statement: 作品层「数理秩序可见」：头身比 1504 Adam 1:7.4 → 1507 Eve 1:8.2、透视消失点明确（§1-8）；P6 几何秩序强档「圆规直尺式建构 + 测量级比例 + 单点透视」为 `[归纳]`。比例数字转引未回原始著录核对（§10 L271）、透视装置 `[UNVERIFIED]`（§10 L267）。
- source_refs:
  - [durer.md](../../dossiers/durer.md) §1-8 **L36**、§10 **L267/L271**｜ sections ｜ sha `4f5be577…` ｜ available
  - [durer.md](../../modules/durer.md) §4 P6 **L82**｜ fulltext ｜ sha `ad49cd77…` ｜ available

<a id="db-source-line-92"></a>
### C3 · `DUR-PRACTICE-LADDER-PROTOTYPES`
- claim_kind: design_candidate ｜ support_status: supported
- statement: §12 临摹清单（10 件，L355–L403）提供可操作练习原型：7.5 头身重建、中轴四横线自画像、先画线框再放物件、5 级明度地图→5 档线距、魔方阵验算 34、圆规直尺截角菱面体、毛流方向图 ≥6 区。练习顺序为本项目 `[归纳]` 编排，**不是丢勒自述的教学法**。
- source_refs:
  - [durer.md](../../dossiers/durer.md) §12 **L355–L403**｜ sections ｜ sha `4f5be577…` ｜ available
  - `01-AUDIT.md` §8.1 L273（练习为建议练习）｜ sections ｜ available

---

<a id="db-source-line-101"></a>
## D 组：C-07 carried（正本 L136–L147，brief 必携带）

<a id="db-source-line-103"></a>
### D1 · `C07-CANONICAL-CARRIED`
- claim_kind: observation ｜ support_status: supported
- statement: C-07（丢勒 × 北斋 / 表面着色系统 / 硬）正本为 `conflicts.md` §2 **L136–L147**：L143 后果（同帧互斥）、L145 着色系统二选一不可拆、L146 明确禁止「排线+平涂」拼接、L147 线宽轴归 Lane B 08 卡；总表 L38。AUDIT-durer §5.1 判「规则文本无误、C-07 成立（supported）」。本 LEARN 原样携带、不改写、不重判。
- source_refs:
  - [conflicts.md](../../../../cross/conflicts.md) §1 **L38**、§2 **L136–L147**｜ fulltext ｜ sha `314a24da…` ｜ available
  - 内部证据 62b1281812ff65aa（未公开；来源记录由维护者保留） §5.1 L112–L122（逐条回源 ✅）｜ sections ｜ sha `1ecfe5e8…` ｜ available
  - 内部证据 b0261e5b0acba88a（未公开；来源记录由维护者保留） `C07-TABLE-AND-DETAIL`｜ artifact ｜ sha `8878411e…` ｜ available

<a id="db-source-line-111"></a>
### D2 · `C07-HOKUSAI-SIDE-VERBATIM`
- claim_kind: observation ｜ support_status: supported
- statement: 北斋侧「线宽恒定变化 ≤30%、无排线无羽化」与「天空/水面单色平涂或留白 ≥35%」逐字回源（实测 [hokusai.md](../../modules/hokusai.md) **L45/L50**、[hokusai.md](../../dossiers/hokusai.md) **L199/L204**），与 C-07 L141 所引字符串一致。
- source_refs:
  - [conflicts.md](../../../../cross/conflicts.md) §2 **L141**（北斋侧引文）｜ citation_context ｜ sha `314a24da…` ｜ available
  - [hokusai.md](../../dossiers/hokusai.md) §8.2-1 **L199**、§8.2-6 **L204**｜ citation_context ｜ sha `d03a260c…` ｜ available
  - 内部证据 62b1281812ff65aa（未公开；来源记录由维护者保留） §1.1 L57（hokusai dossier sha 登记）、§5.1 L118｜ sections ｜ sha `1ecfe5e8…` ｜ available

<a id="db-source-line-119"></a>
### D3 · `C07-N3-N4-N1-GENERIC-RULES`
- claim_kind: observation ｜ support_status: supported
- statement: card L88 点名 §3 N1/N3/N6；N3（L311–L312，适用清单含 C-07）= 轴所有权表、辅模块 §8.2 整条移除；N4（L314–L315）= 同一全帧统计量不可拆、二选一（解释 C-07 为何不可分区）；N1（L305–L306）= 反约束一致性检查；N9（L332–L333）= 冲突轴不得双标准。
- source_refs:
  - [conflicts.md](../../../../cross/conflicts.md) §3 **L305–L333**（N1/N3/N4/N9 正本）｜ sections ｜ sha `314a24da…` ｜ available
  - [durer.md](../../modules/durer.md) L88/L90–L91（冲突注记点名 N1/N3/N6 与 C-07/near-miss #6）｜ fulltext ｜ sha `ad49cd77…` ｜ available

<a id="db-source-line-126"></a>
### D4 · `C07-NEAR-MISS-6`
- claim_kind: observation ｜ support_status: supported
- statement: near-miss #6（§4 L352）「丢勒 §8.2-1 线宽恒定 1.5–2px × 北斋 §8.2-1 ≤30% × Lane B 08 卡 = 三者同侧」，与 card L91 一致；P2 的 2–3 倍变化被显式划归 C-07，near-miss 只保留「线宽恒定」轴（AUDIT-durer §5.3 判自洽）。
- source_refs:
  - [conflicts.md](../../../../cross/conflicts.md) §4 **L352**｜ citation_context ｜ sha `314a24da…` ｜ available
  - 内部证据 62b1281812ff65aa（未公开；来源记录由维护者保留） §5.3 L139–L143｜ sections ｜ sha `1ecfe5e8…` ｜ available

---

<a id="db-source-line-135"></a>
## E 组：+2 locator drift known-open（brief 指派）

<a id="db-source-line-137"></a>
### E1 · `DRIFT-C07-LOCATOR-PLUS2-OPEN`
- claim_kind: observation ｜ support_status: supported（登记为 known-open，非阻断）
- statement: C-07 详条 L140–L142 引用行号在当前哈希源文件上整体偏移 +2（dossier 侧）/ +1（hokusai 侧）且 `durer.md`/`hokusai.md` 在 card 与 dossier 间同名歧义：L206→dossier L208/card L64；L208→L210/L66；L212→L214/L70；L76→L77/L78；hokusai L188→dossier L199/card L45；L193→L204/L50。规则文本逐字一致、子串命中，仅定位过期。本 LEARN 用实测行号规避，交 CONFLICT-07 写手统一，不改仓库。
- source_refs:
  - 内部证据 62b1281812ff65aa（未公开；来源记录由维护者保留） §5.2 **L124–L137**、§9.1 **L184**｜ sections ｜ sha `1ecfe5e8…` ｜ available
  - 内部证据 b0261e5b0acba88a（未公开；来源记录由维护者保留） `DRIFT-C07-LOCATOR`（`locator_actual.*`）｜ artifact ｜ sha `8878411e…` ｜ available
  - [conflicts.md](../../../../cross/conflicts.md) §2 **L140–L142**（被核对的过期引用）｜ citation_context ｜ sha `314a24da…` ｜ available
  - 本轮 `nl -ba` 实测：[durer.md](../../modules/durer.md) L64/66/70/78、[durer.md](../../dossiers/durer.md) L208/210/214/77、[hokusai.md](../../modules/hokusai.md) L45/50、[hokusai.md](../../dossiers/hokusai.md) L199/204｜ fulltext ｜ available

<a id="db-source-line-146"></a>
### E2 · `DRIFT-ATTACHED-OPEN`
- claim_kind: observation ｜ support_status: supported（登记，非阻断）
- statement: AUDIT-durer §9 附带 known-open：near-miss「8 对 vs 现 11 行」（§5.4/§9.2）、§8.1b 派生证据 [RESULTS_t1b.md](../../../../../experiments/E1_t1b/RESULTS_t1b.md) live 不可寻址（§6/§9.3）、自审「18 条 read 200 vs §9 表 21 ✅」（§2/§9.4）、3 图未 image_seen（§7/§9.5）。本 lane 全部只登记、不改写。
- source_refs:
  - 内部证据 62b1281812ff65aa（未公开；来源记录由维护者保留） §2 L68、§5.4 L145–L147、§6 L151–L155、§7 L159–L171、§9 L182–L189｜ sections ｜ sha `1ecfe5e8…` ｜ available

---

<a id="db-source-line-154"></a>
## F 组：边界 / 未验证（诚实登记）

<a id="db-source-line-156"></a>
### F1 · `LEARN-PRACTICE-EFFECTS-UNVERIFIED`
- claim_kind: design_candidate ｜ support_status: unverified
- statement: 全部练习为建议练习，未经真人完成或评价，也无模型审美评审；§8.2 阈值/§4 档位为 `[归纳]` 未实测；不能声称「已证实学习收益」「丢勒本人教学法」「审美通过」「76/76 覆盖」。
- source_refs:
  - `01-AUDIT.md` §8.1 L273 / §9 L322（学习建议不冒充学习成效）｜ sections ｜ available
  - [durer.md](../../dossiers/durer.md) §10 **L269**（§8.2 未跑渲染器）｜ sections ｜ sha `4f5be577…` ｜ available

<a id="db-source-line-163"></a>
### F2 · `LEARN-NO-IMAGE-NO-NETWORK-NO-EXPERIMENT`
- claim_kind: observation ｜ support_status: supported
- statement: 本 lane 0 次网络调用、未 image_seen（3 图沿用 AUDIT-durer 权利记录 metadata-only）、未跑 A-12/E2 组合实验、无 human review；外部 URL 可达性沿用 AUDIT-durer §9 口径不升级。
- source_refs:
  - 内部证据 62b1281812ff65aa（未公开；来源记录由维护者保留） §0 L25（无 image_seen）、§7 L169–L171（权利字段仅本机 manifest）、§9.5 L188｜ sections ｜ sha `1ecfe5e8…` ｜ available
  - 内部证据 35441cc052a80acf（未公开；来源记录由维护者保留） §4（image_seen=0 / read_scope=metadata）｜ artifact ｜ sha `8bfc0ff8…` ｜ available

---

<a id="db-source-line-172"></a>
## 支持状态汇总

| 组 | claim 数 | supported | unverified | conflict |
|---|---|---|---|---|
| A 任务形状/依赖 | 2 | 2 | 0 | 0 |
| B 排线体系 | 3 | 3 | 0 | 0 |
| C 比例几何 | 3 | 3 | 0 | 0 |
| D C-07 carried | 4 | 4 | 0 | 0 |
| E +2 drift known-open | 2 | 2 | 0 | 0 |
| F 边界/未验证 | 2 | 1 | 1 | 0 |
| **合计** | **16** | **15** | **1** | **0** |

> 本文件不含凭据；不含 `review`（作者不自验收）；`status=submitted`；独立审者 gate 为单独动作。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
