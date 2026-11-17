<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-el_greco；原正文 SHA-256 `199a68ad79d85cfdb570398aff2a6451028a1256f7aa56e8e801dddb98e2f280`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-el_greco — claim → evidence map（每条论断带 locator）

> 任务 `LEARN-el_greco` · 依赖 `AUDIT-el_greco`（attempt 2 **ACCEPTED**：内部证据 8efdb95ada77c348（未公开；来源记录由维护者保留） status=accepted；`review-evidence.md:10` "ACCEPT the author's submission"；review point 5 counterexample SOUND）。
> **口径（复用 ACCEPTED 审计的 locator 纪律，不重新审计）**：每条论断给「来源文件 + 具体行/节定位 + 证据等级 + 支持状态」。内部证据 4874f193014ae79c（未公开；来源记录由维护者保留） 为只读回源（声明基线 `f008952365a77e140cbda3f3959d43ef000f9a22`，本 lane 开工已 sha256sum 复核三件冻结输入，见 `RESULT.md §2`）；内部证据 f75c4567bbe7b985（未公开；来源记录由维护者保留） 为上游 ACCEPTED 产物；内部证据 bc2037c6863c377e（未公开；来源记录由维护者保留） 为本 lane 生成。
> 等级沿用仓库口径：`[自述]`/`[self-written]` = 本人书写（带转引链）；`[reported speech]` = 他人转记；`[contemporary record]`/`[史料]` = 同时代记录／馆藏；`[研究]`/`[later reception]` = 馆方／学者／后世；`[归纳]` = 项目操作规则／研究者归纳；`[推测]` 本 lane **不使用**（计数 0）。
> 版本列：仓库文件 = `f0089523…`；staging artifact = 本轮／上游生成（给 sha256）。`read_scope` 与 `access_status` 分开：外部 URL 本轮未重访 = `unknown`，本机文件 = `available`，原图像素目检 = 0（无 `image_seen`）。
> **主判据（反例带入）**：`扭曲方向 ≠ 题材域`；世俗题材不越界、判据冲突以 ① 扭曲方向 为准。§5-4「La pintura」语料缺口 = **known-open**。

---

<a id="db-source-line-11"></a>
## A. 输入与版本（本 lane 开工复核）

| # | claim_id | 论断（短） | kind/status | 证据定位（source : locator） | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 1 | LEG-INPUT-CARD | card sha = ledger `068fb227…a935` | fact/supported | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留）（`e1ec2d11…18ce9`）el_greco 条目 `card_sha256` × [el_greco.md](../../modules/el_greco.md) 全文件 sha × `RESULT.md §2` 实跑 | `[史料]`（字节实测） | 开工 sha256sum 全等 |
| 2 | LEG-INPUT-DOSSIER | dossier sha = ledger `44d2b2b9…d007` | fact/supported | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） el_greco 条目 `dossier_sha256` × [el_greco.md](../../dossiers/el_greco.md) 全文件 sha × `RESULT.md §2` | `[史料]` | 全等 |
| 3 | LEG-INPUT-CORPUS | corpus sha = ledger `e5a7efcc…cfd1`（30 quotes） | fact/supported | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） el_greco 条目 `corpus_sha256`/`corpus_quotes=30` × [el_greco.md](../../dossiers/_corpus/el_greco.md) 全文件 sha × `RESULT.md §2` | `[史料]` | 全等；30 条沿用 AUDIT 计数 |
| 4 | LEG-INPUT-MUNCH | munch.md sha = `d9894851…e79f9`（对称互锁回源） | fact/supported | [munch.md](../../dossiers/munch.md) 全文件 sha × `RESULT.md §2` | `[史料]` | §3.1 L84 逐字读 |
| 5 | LEG-INPUT-AUDIT-CEM | 上游 `AUDIT-el_greco/claim_evidence_map.md` sha = `87d9a323…1a12f` | fact/supported | 内部证据 495a791f847ee9e9（未公开；来源记录由维护者保留） 全文件 sha × `RESULT.md §2` | `[史料]`（字节实测） | RECEIPT input_hashes 项 |
| 6 | LEG-INPUT-AUDIT-RESULT | 上游 `AUDIT-el_greco/RESULT.md` sha = `3b36a5ae…9eee` | fact/supported | 全文件 sha × `RESULT.md §2` | `[史料]` | RECEIPT input_hashes 项 |
| 7 | LEG-INPUT-AUDIT-MANIFEST | 上游 `AUDIT-el_greco/coverage_manifest.json` sha = `c92f2c6e…f31b5` | fact/supported | 全文件 sha × `RESULT.md §2` × AUDIT `receipt.json` artifacts 登记值 | `[史料]` | RECEIPT input_hashes 项 |
| 8 | LEG-INPUT-AUDIT-REVIEW | 上游 `AUDIT-el_greco/review-evidence.md` sha = `4297ea45…e3cc` | fact/supported | 全文件 sha × `RESULT.md §2` × `review-gate-receipt.json` input_hashes | `[史料]` | RECEIPT input_hashes 项 |
| 9 | LEG-INPUT-CONFLICTS | conflicts.md sha = `314a24da…bbef` | fact/supported | [conflicts.md](../../../../cross/conflicts.md) 全文件 sha × `RESULT.md §2` × AUDIT `coverage_manifest.json.hashes.conflicts` | `[史料]` | 全等 |
| 10 | LEG-AUDIT-ACCEPTED | 上游 AUDIT-el_greco 已 ACCEPTED（attempt 2） | fact/supported | 内部证据 8efdb95ada77c348（未公开；来源记录由维护者保留） status=accepted × `review-evidence.md:8-19` ACCEPT + 6 点全 MATCH × `review-gate-receipt.json` | `[史料]`（产物） | 本 lane 不重新审计，只复用结论 |

<a id="db-source-line-26"></a>
## B. 前置知识（learning_path.md §1）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 11 | LEG-K1-CORPUS-SCARCITY | 文字存世极少（画论已佚）；存世＝批注＋题记＋书信／遗嘱；「他内心如何」降级为操作规则 | observation/supported | `dossiers/el_greco.md:7`（§0 特殊性）、`:110`（§5 抬头）、`:290`（§10-9） × AUDIT [claim_evidence_map.md](claim_evidence_map.md) EG-3-1 | `[研究]`/`[史料]`（口径） | 不写心理 |
| 12 | LEG-K2-GRISAILLE | 灰调底层机制：灰单色底 → 罩染炽热色相 → 红底透出 → 单层覆色、无厚涂 | fact/supported | `dossiers/el_greco.md:51,52,53`（§2-1/-2/-3）、`:209`（§8.1 brush 行） × `_corpus/el_greco.md:222-227`（Q29 Taubes） × AUDIT EG-2-1/-2/-3 | `[研究]`（Taubes）/`[归纳]`（映射） | **非作者自述** |
| 13 | LEG-K3-DISTORTION | 扭曲变形：纵向拉长（≥9 头身、加高 1.5 英尺）＋蛇形＋形体连续；连载体一起改 | fact/supported | `dossiers/el_greco.md:34,39,57`（§1-1/-6、§2-7）、`:68-71`（§3）、`:116-119`（§5-2）、`:136-139`（§5-7） × `_corpus/el_greco.md:34-40,58-64`（Q4/Q7） | `[自述]`/`[研究]`/`[归纳]` | 主卡主线② |
| 14 | LEG-K4-PARAMS-RULES | §8.2 八条 + §4 六参数（P1/P2/P4 定「是不是格列柯」，≥2 条 ≥ 中档） | fact/supported | `dossiers/el_greco.md:96-104`（§4）、`:228-235`（§8.2）、`:237`（阈值自述） × `modules/el_greco.md:45-52,58-68` × AUDIT `RESULT.md §2`（`_extract.py --check` 228/228） | `[归纳]` | 逐字一致 |
| 15 | LEG-K5-MASTER-CRITERION | **主判据 = 扭曲方向，不是题材域**；① 扭曲方向主／② 题材域辅；世俗题材不越界、冲突以 ① 为准 | observation/supported | `dossiers/el_greco.md:79-83`（§3.1，L82 判据＋边界注） × `munch.md:84` × `ops/GOALS.md:120`（A-82） × `modules/el_greco.md:74` × AUDIT `RESULT.md §6` / `review-evidence.md:55-59` / EG-GOAL-6 | `[归纳]`（写死，可被组合实验推翻） | **反例带入** |
| 16 | LEG-K6-SELF-LAYER | 作者自述层（Q1–Q10 操作陈述）与 `[归纳]` 严格分开，不作心理证据 | fact/supported | `dossiers/el_greco.md:112-151`（§5 十条） × `_corpus/el_greco.md:11-88`（§一/§二） | `[自述]`/`[reported speech]` | Q6/Q19 是转记 |
| 17 | LEG-K7-LAPINTURA-GAP | §5-4「La pintura…especulativa」在 dossier，30 条 corpus 无此条（known-open） | observation/partial | `dossiers/el_greco.md:68,124-127` × [el_greco.md](../../dossiers/_corpus/el_greco.md) 全文（grep moderadora/especulativa=0） × AUDIT `RESULT.md §8 #1` / EG-GAP-1 / EG-3-1 / `review-evidence.md:17` | `[自述]`（dossier 内）/`[归纳]`（缺口判定） | **不补写、不升级** |
| 18 | LEG-K8-CONFLICTS-ZERO | conflicts.md 对 el_greco 字面命中＝0；C-01/C-05/C-09/C-12 为预检指针；处置 N1/N3/N6 | fact/supported | `conflicts.md` 全文 / `:32,36,40,43`（总表）/`:303,305,311,323`（N1/N3/N6） × `dossiers/el_greco.md:88,224,241-245` × `modules/el_greco.md:4,70-76,81` × AUDIT EG-CF-1/-2/-4 | `[归纳]` | 本档无 conflicts 定位漂移 |

<a id="db-source-line-39"></a>
## C. 重点作品及来源（learning_path.md §2）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 19 | LEG-WORKS-12 | §12 共 10 件临摹/学习清单，本文引用现有记录不新增作品 | fact/supported | `dossiers/el_greco.md:364`（§12 抬头）/`:368-416`（10 件）/`:418`（组合建议） × AUDIT `RESULT.md §4` | `[史料]`（作品信息）/`[归纳]`（练习映射） | 沿用 |
| 20 | LEG-WORKS-GRISAILLE | §12-4/-2/-1 → 灰调底层／红底透出／「一亮点＋退灰」练习 | observation/supported | `dossiers/el_greco.md:383-386,373-376,368-371` | `[归纳]`（映射） | 练习映射归本项目 |
| 21 | LEG-WORKS-DISTORTION | §12-3/-8/-9/-7 → 锯齿轴／竖长幅／极端拉长／X 轴动作练习 | observation/supported | `dossiers/el_greco.md:378-381,403-406,408-411,398-401` | `[归纳]`（映射） | 同上 |
| 22 | LEG-WORKS-BOUNDARY | §12-5《托莱多风景》/§12-10《拉奥孔》为世俗题材不越界的锚点 | observation/supported | `dossiers/el_greco.md:388-391,413-416` × `dossiers/el_greco.md:82`（边界注） | `[归纳]`（映射/判据） | 反例带入 |
| 23 | LEG-WORKS-RIGHTS | 17 张公开图（11 Commons PD + 6 Met OA）权利有记录，本 lane 未目检、外部未重访 | fact/supported | `_images/manifest.md` + `_images/el_greco/MANIFEST.md` × AUDIT `RESULT.md §4`/`rights_review.md`/`RESULT.md §9` × `coverage_manifest.json.hashes` | `[史料]`（权利账） | `unverified`＝许可页/像素未独立目检 |

<a id="db-source-line-49"></a>
## D. 机制与参数（learning_path.md §3 / mechanism_notes.md §1-§3）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 24 | LEG-M1 | M1 灰调底层＋罩染：灰底→炽热罩染→红底透出→单层、无厚涂 | fact/supported | `dossiers/el_greco.md:51-54,209,229` × `_corpus/el_greco.md:222-227`（Q29） × AUDIT EG-2-1/-2/-3/-4 | `[研究]`/`[归纳]` | 自查＝罩染透出＋无厚涂 |
| 25 | LEG-M2 | M2 扭曲变形：高/宽 ≥3.5、人脸/人物 ≤0.11、轮廓连续无断裂、主判据＝扭曲方向 | fact/supported | `dossiers/el_greco.md:228,233`（§8.2-1/-6）、`:79-83`（§3.1）、`:96`（P1） × `modules/el_greco.md:45,50,60,68` × AUDIT `RESULT.md §6` | `[归纳]` | 世俗题材不越界 |
| 26 | LEG-M3 | M3 自有光＋酸色＋云幕：§8.2-3/-4/-5/-8、P3/P4/P5、越界警报③④ | fact/supported | `dossiers/el_greco.md:230,231,232,235,98-100,104,224` × `modules/el_greco.md:47,48,49,52,61-65,68` | `[归纳]` | 阈值分母＝假想参考帧 |
| 27 | LEG-M4 | M4 火舌笔触＋反复重画：§8.2-2、P2、Pacheco 贬义证词 | fact/supported | `dossiers/el_greco.md:54,55,74,229,97,243` × `_corpus/el_greco.md:113-132`（Q14/Q16） | `[史料]`/`[归纳]` | 贬义证词不升格自述 |
| 28 | LEG-82-ALL-8 | §8.2 共 8 条逐帧可查规则（含 -7 视频帧、-8 色相预算） | fact/supported | `dossiers/el_greco.md:226-237` × `modules/el_greco.md:43-54` | `[归纳]` | -7 属视频帧域 |
| 29 | LEG-4-ALL-6 | §4 共 6 个控制参数各三档（P1–P6），默认 65/55/55/60/55/1 | fact/supported | `dossiers/el_greco.md:92-104` × `modules/el_greco.md:56-68` | `[归纳]` | P6 工作流参数 |
| 30 | LEG-82-7-C09 | §8.2-7「弱上升场」与 C-09 对齐，站冻结与全画面场之间，不并入静态阶梯 | observation/supported | `dossiers/el_greco.md:234,244` × `modules/el_greco.md:51` × `conflicts.md:40` | `[归纳]` | 文本比对，非实验 |
| 31 | LEG-EXT-1 | §4/§8.2 阈值自述「未对原作像素测量，分母＝假想参考帧」 | fact/supported | `dossiers/el_greco.md:237`、`:289`（§10-8）、`:103`（§4 用法） × AUDIT [claim_evidence_map.md](claim_evidence_map.md) EG-EXT-1 | `[归纳]`（正确标注） | 不构成可证伪事实 |

<a id="db-source-line-62"></a>
## E. 冲突行 / 主判据 / 互锁（learning_path.md §6 / mechanism_notes.md §4）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 32 | LEG-CRITERION-COUNTEREXAMPLE | 反例：若题材域当主判据，世俗题材被误判进蒙克档；边界注封堵 → 反例不推翻，主判据必须是扭曲方向 | observation/supported（`[inference]` 逻辑检验，非像素实测） | AUDIT `RESULT.md §6` × `dossiers/el_greco.md:82`（边界注） × `review-evidence.md:55-59`（SOUND，正确限定） | `[归纳]` | 本卡原样带入 |
| 33 | LEG-MUNCH-L84 | `munch.md §3.1 L84` 对称互锁：vs 埃尔·格列柯（扭曲两路），判据＝题材域＋扭曲方向 | fact/supported | `munch.md:84` 逐字 × `dossiers/el_greco.md:79-83` × `ops/GOALS.md:120` × AUDIT `review-evidence.md:48` / EG-GOAL-6 | `[归纳]`（roster §2.6 配对） | L84 两名并列、el_greco L82 明定 ① 主判据，无矛盾 |
| 34 | LEG-PICASSO-CRITERION | vs 毕加索：①变形机制（面片拆解＋多视点 vs 连续拉伸）主判据；②形体连续性；不得机制混写 | fact/supported | `dossiers/el_greco.md:84-87` × `modules/el_greco.md:75` × `dossiers/el_greco.md:233`（§8.2-6） | `[归纳]` | 同谱系两端 |
| 35 | LEG-OVERBOUND-4 | §4 越界警报四条（蒙克／毕加索／卡拉瓦乔／梵高）为换模块信号 | fact/supported | `dossiers/el_greco.md:104` × `modules/el_greco.md:68` × `dossiers/el_greco.md:224` | `[归纳]` | 非强档延伸 |
| 36 | LEG-CEM-ZERO-HIT | C-01/C-05/C-09/C-12 的 §2 正文无格列柯文件行号引用 → 本档无 conflicts 漂移 | fact/supported | `conflicts.md:55-70,109-121,164-175,203-216` × AUDIT EG-CF-1/-2/`audit_scripts.out` | `[归纳]` | 零命中，预检指针 |
| 37 | LEG-N-RULES | N1 反约束一致性／N3 轴所有权／N6 色数口径可回源；模块卡 L4 指针一致 | fact/supported | `conflicts.md:303,305,311,323` × `modules/el_greco.md:4` × AUDIT EG-CF-4 | `[归纳]` | 采纳状态 N1/N3/N6 |
| 38 | LEG-DRIFT-NEARMISS | near-miss 表实测 11 行 vs 自审「8 条」／卡「8 对」＝+3 计数漂移（不修） | observation/conflict（登记） | `conflicts.md:347-357` × `dossiers/el_greco.md:365`（自审 A） × `modules/el_greco.md:81` × AUDIT EG-CF-3 / `RESULT.md §8 #3` | `[归纳]`（文本比对） | 与 A-34 页码 ±1 不同对象 |
| 39 | LEG-DRIFT-13VS14 | §11.3 标题「13 条」vs 实测 14 个 R-id，GOALS 写 14（不修） | observation/conflict（登记） | `dossiers/el_greco.md:354`（§11.3）/`:356-359`（R 列表） × `ops/GOALS.md:120` × AUDIT EG-GOAL-4 / `RESULT.md §8 #2` | `[归纳]`（文本比对） | 文档内部矛盾 |
| 40 | LEG-DRIFT-COUNTS | §11.1 CJK 2040 vs GOALS 2044 字；497 行 vs wc 496（尾部换行口径） | observation/partial（登记） | `dossiers/el_greco.md:299-301`（§11.1） × `ops/GOALS.md:120` × AUDIT EG-GOAL-1/-2 | `[归纳]` | 历史计数口径未复现，不改写 |
| 41 | LEG-OVERTURNED | 散光说／大麻说／病因论不采用（OVERTURNED）；Q28「表达而非病因」 | fact/supported | `dossiers/el_greco.md:288`（§10-7）、`:437`（自审 B 表第 3 行） × `_corpus/el_greco.md:215-220`（Q28） × `ops/GOALS.md:120` × AUDIT EG-GOAL-5 / `review-evidence.md:47` | `[史料]`（档案结论） | 不复活病因论 |
| 42 | LEG-TYPE-1 | corpus 实测 9/13/2/6 vs §0 L26／§5 L110「自述 10／同时代 14／后世 6」＝合并口径差（总数 30 一致） | observation/partial（登记） | `dossiers/el_greco.md:26,110` × [el_greco.md](../../dossiers/_corpus/el_greco.md) 全文 × AUDIT `RESULT.md §8 #9` / EG-TYPE-1 / `coverage_manifest.json.quote_type_breakdown` | `[归纳]` | 非内容错误 |

<a id="db-source-line-78"></a>
## F. How-to-Think 等级分离（how-to-think.md）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 43 | LEG-HT-SPLIT | `[自述]` 与 `[归纳]`／`[推测]` 严格分栏；每步带证据等级；`[推测]` 计数 0 | observation/supported | `how-to-think.md §0/§1/§5` × `00-GOAL.md:9` × `dossiers/el_greco.md:7,110,288` × AUDIT `RESULT.md §7` | `[归纳]`（本卡纪律） | 不从作品外观反推心理 |
| 44 | LEG-HT-SELF-QUOTES | S1/S3/S4 的「为什么」上半来自作者言语记录（Q1–Q7、Q4/Q7/Q2、§5 十条，带转引链） | fact/supported | `dossiers/el_greco.md:112-151` × `_corpus/el_greco.md:11-88` | `[自述]`/`[reported speech]` | 转引链风险不静默消除 |
| 45 | LEG-HT-RESEARCH-ONLY | S2 灰调底层为纯 `[研究]`（Taubes）＋`[归纳]`，**无 `[自述]`**；S6 Pacheco 为 `[史料]`（带贬义） | fact/supported | `how-to-think.md §2 S2/S6` × `_corpus/el_greco.md:113-132,222-227` × `dossiers/el_greco.md:51-55,74` | `[研究]`/`[史料]`/`[归纳]` | 不升格为自述 |
| 46 | LEG-HT-INFER-ONLY | S5 为纯 `[归纳]` 步（§8.2 数值无作者自述支撑）；S4 主判据为 `[归纳]` | fact/supported | `how-to-think.md §2 S4/S5` × `dossiers/el_greco.md:79-83,228-235,237` × AUDIT EG-EXT-1 | `[归纳]` | 不写「格列柯要求 ≥9 头身」 |
| 47 | LEG-HT-NO-PSYCH | 不含「从画面推作者心理」、不复活病因论、不把类型学标签写成心理 | observation/supported | `how-to-think.md §4` 反心理推断清单 × `00-GOAL.md:9` × `dossiers/el_greco.md:288,437` × `_corpus/el_greco.md:215-220` | `[归纳]` | 红线 |

<a id="db-source-line-88"></a>
## G. 练习、结果、失败、边界（learning_path.md §4-§8 / mechanism_notes.md §5-§6）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 48 | LEG-LADDER-3 | 三条阶梯练习：grisaille-and-glaze → elongation-and-continuity → unseen-light/acid-colour/cloud-curtain discipline | design_candidate/supported（作为「建议练习」交付） | `learning_path.md §4` × `dossiers/el_greco.md:51-54,368-386`（阶梯一）/`:79-83,228,233,378-411`（阶梯二）/`:97-100,104,230-235,243-245,388-391`（阶梯三） | `[归纳]`（本项目设计） | **建议练习**，学习收益未经人评 |
| 49 | LEG-A30-SHAPE | 学习路径含 A-30 §8.1 八节：前置知识／重点作品及来源／要观察的机制／具体练习／可观察结果／常见失败／下一步／使用边界 | fact/supported | `01-AUDIT.md:269-273`（§8.1） × `learning_path.md §1-§8` 八节标题 × `ops/GOALS.md:44` | `[史料]`（spec）/`[归纳]`（映射） | 练习须标建议练习（`:273`） |
| 50 | LEG-PRACTICE-UNVERIFIED | 练习效果未由人完成／评价，标「建议练习」不写「已证实学习收益」 | fact/supported | `01-AUDIT.md:273` × [learning_path.md](learning_path.md) 抬头/§4/B1 × 本 `receipt.json` human_review=not_applicable | `[史料]`（spec）/`[归纳]`（严格执行） | 硬边界 |
| 51 | LEG-OBSERVABLE | 可观察结果是练习产物自查口径，非原作像素实测 | observation/supported | `learning_path.md §5` × `dossiers/el_greco.md:228-235`（§8.2 自查法）×`:237`（假想参考帧）× AUDIT `RESULT.md §4` | `[归纳]` | 不声称原作被证实如此 |
| 52 | LEG-FAILURES | 9 类常见失败（F1 题材域当主判据／F2 厚涂盖灰底／F3 拼接边／F4 越界③④／F5 等级混淆／F6 心理+病因论／F7 §5-4 缺口／F8 双主导轴／F9 回源与状态） | observation/supported | `learning_path.md §6` × `dossiers/el_greco.md:51-55,79-88,104,124-127,237,288,437` × `conflicts.md:305,311,323` × AUDIT `RESULT.md §8 #1/#9`、EG-GAP-1、EG-CF-3 | `[归纳]` | 规则层判定，非实验 |
| 53 | LEG-BOUNDARY-CRITERION | 使用边界含「主判据＝扭曲方向而非题材域」为硬边界（反例带入） | fact/supported | `learning_path.md B3` × `dossiers/el_greco.md:82` × `munch.md:84` × AUDIT `RESULT.md §6` / `review-evidence.md:48,55-59` | `[归纳]` | 世俗题材不越界 |
| 54 | LEG-BOUNDARY-GAP | 使用边界含 §5-4「La pintura」语料缺口 known-open（不补写、不升级） | fact/supported | `learning_path.md B5/§6 F7` × `dossiers/el_greco.md:124-127` × AUDIT `RESULT.md §8 #1`/`§9`、EG-GAP-1、`review-evidence.md:17` | `[归纳]`（缺口判定） | 随卡携带 |
| 55 | LEG-NO-REPO-WRITE | 本 lane 仅写 内部证据 59e85d75e4eca17a（未公开；来源记录由维护者保留），仓库只读、无 git、无子代理、无凭据 | observation/supported | 本 `receipt.json` `allowed_write_paths`=内部证据 59e85d75e4eca17a（未公开；来源记录由维护者保留）、`spawns_allowed=false` × AUDIT `RESULT.md §6`（0 repo writes/0 spawns/0 credentials） | `[史料]`（产物声明） | 只读约束遵守 |
| 56 | LEG-EXTRACT-228 | card §8.1/§8.2/§4 与 dossier 逐字一致（`_extract.py --check` 全库 228/228，el_greco 占 3） | fact/supported | AUDIT `RESULT.md §2`/`§3` × `coverage_manifest.json.extract_check` × `AUDIT-el_greco/audit_scripts.out`；本 lane **未重跑**，沿用 ACCEPTED 审计结论 | `[史料]`（上游实跑） | 228/228 钉在本次实际内容 |

---

<a id="db-source-line-104"></a>
## 支持状态汇总（分母 = 56 条论断，逐行 `grep -cE '^\| [0-9]+ \| LEG-'` 实测 = 56）

- `supported` = **51**（其中 `fact/supported` 38 · `observation/supported` 12 · `design_candidate/supported` 1）；`partial` = **3**（EG-GAP-1 语料缺口 #17、计数口径 #40、类型口径 #42）；`conflict`（登记） = **2**（near-miss 11-vs-8 #38、§11.3 13-vs-14 #39）；`unverified` = 0；`not_applicable` = 0。**合计 51+3+2 = 56**。
- **#23 的 `supported` 有明确限定**：仅指「本机权利账记录存在且连贯」；AUDIT `RESULT.md §4` 把「Commons/Met 许可页真实性 + 17 张图像像素」标为 `unverified`（未独立目检，`image_seen=0`）。本 lane 对 AUDIT 的 `unverified` 结论**原样携带**，不升级、不抹去，故不另起一行 `unverified` 计数；该限定写在本表备注列与 `RESULT.md §5`。
- `[推测]` 级结论 = **0**；无「从作品外观反推作者心理」、无病因论复活（#41/#43/#47）。
- 所有 §8.2/§4/§3.1/conflicts 数值均标 `[归纳]`，未冒充 `[自述]`/`[史料]`/像素实测（#14/#26/#28/#29/#31/#46）。灰调底层标 `[研究]`（Taubes）而非自述（#12/#24/#45）。
- **主判据 #15/#25/#32/#33/#53**：扭曲方向 ≠ 题材域，反例带入、munch L84 对称互锁，原样携带。
- **§5-4 缺口 #17/#54**：known-open，`partial`，不补写、不升级。
- 练习 = **建议练习**（#48/#50），`human_review=not_applicable`，不写「已证实学习收益」。
- 外部 URL 本轮**未重访**（`access_status=unknown`，AUDIT `RESULT.md §9`）；17 张公开图**未目检**（`image_seen=0`）；#19–#23 作品／权利论断支持范围 =「本机文件内引用与记录仍存在且连贯」，不声称外部页面当前可访问。
- 本 lane `status=submitted`（非 accepted），`review=null`，独立审阅由 review gate 承担（见 `receipt.json`）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
