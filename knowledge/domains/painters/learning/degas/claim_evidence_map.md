<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-degas；原正文 SHA-256 `74e1b309653b8308fc0ed0d8b997803ca0d0c240c7035524c3a9475cf78ca3f0`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-degas — claim → evidence map（每条论断带 locator）

> 任务 `LEARN-degas`（A-30 分片）· 依赖 `AUDIT-degas`（**ACCEPTED**，内部证据 c0f6a87194ae842f（未公开；来源记录由维护者保留） status=accepted / review.verdict=accepted / reviewer `ReviewGateAUDIT-degas(glm-5.3-flash)` ≠ author `AuditDegas` / 13 reviewed hashes == 13 artifacts）。
> **口径（复用 ACCEPTED 审计的 locator 纪律，不重新审计）**：每条论断给「来源文件 + 具体行/节定位 + 证据等级 + 支持状态」。内部证据 4874f193014ae79c（未公开；来源记录由维护者保留） 为只读回源（声明基线 `f008952365a77e140cbda3f3959d43ef000f9a22`，本 lane 开工已 sha256sum 复核三件冻结输入，见 `RESULT.md §2`）；内部证据 9eb2c8b19da8a064（未公开；来源记录由维护者保留） 为上游 ACCEPTED 产物；内部证据 fc18563381cb1319（未公开；来源记录由维护者保留） 为本 lane 生成。
> 等级沿用仓库口径：`[自述]`/`[self-written]`/`[reported speech]`/`[contemporary record]` = 作者/同时代人言语记录（德加一律带转记载体）；`[史料]` = 史实/馆藏/权利；`[研究]` = 馆方/学者分析；`[归纳]` = 项目操作规则/研究者归纳；`[推测]` 本 lane **不使用**（计数 0）。
> 版本列：仓库文件 = `f0089523…`；staging artifact = 本轮/上游生成（给 sha256）。`read_scope` 与 `access_status` 分开：外部 URL 本轮未重访 = `unknown`，本机文件 = `available`，原图像素目检 = 0（无 `image_seen`）。
> **行号纪律**：本表一律用**本机只读实测行号 + 子串**；AUDIT-degas 报告的 11 处 conflicts.md locator 漂移（C-DRIFT-1..11）本 lane 沿用登记、不改仓库（read-only, one writer per tree）。

---

<a id="db-source-line-11"></a>
## A. 输入与版本（本 lane 开工复核）

| # | claim_id | 论断（短） | kind/status | 证据定位（source : locator） | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 1 | LD-INPUT-CARD | card sha = `84f6d39f…4f0e` | fact/supported | [degas.md](../../modules/degas.md) 全文件 sha × `AUDIT-degas/coverage-manifest.json:hashes.card` × `RESULT.md §2` 实跑 | `[史料]`（字节实测） | 开工 sha256sum 全等 |
| 2 | LD-INPUT-DOSSIER | dossier sha = `8461d94e…f168` | fact/supported | [degas.md](../../dossiers/degas.md) 全文件 sha × `AUDIT-degas/coverage-manifest.json:hashes.dossier` × `RESULT.md §2` | `[史料]` | 全等（503 行） |
| 3 | LD-INPUT-CORPUS | corpus sha = `c4816389…5b07`（36 quotes） | fact/supported | [degas.md](../../dossiers/_corpus/degas.md) 全文件 sha × `AUDIT-degas/coverage-manifest.json:quote_count=36` × `RESULT.md §2` | `[史料]` | `grep -c '^### '`=36 沿用 AUDIT 计数 |
| 4 | LD-INPUT-CONFLICTS | conflicts.md sha = `314a24da…bbef` | fact/supported | [conflicts.md](../../../../cross/conflicts.md) 全文件 sha × `AUDIT-degas/receipt.json` input_hashes × `RESULT.md §2` | `[史料]` | 全等 |
| 5 | LD-INPUT-GOALS | ops/GOALS.md sha = `2727d1f0…1144` | fact/supported | `ops/GOALS.md` 全文件 sha（A-55 行 :61）× `RESULT.md §2` | `[史料]` | 全等 |
| 6 | LD-INPUT-AUDIT-RECEIPT | 上游 `AUDIT-degas/receipt.json` sha = `a69d5af5…a664` | fact/supported | 内部证据 c0f6a87194ae842f（未公开；来源记录由维护者保留） 全文件 sha（RECEIPT `input_hashes` 之一） | `[史料]`（字节实测） | 本 lane 复用 |
| 7 | LD-AUDIT-ACCEPTED | 上游 AUDIT-degas 已 ACCEPTED | fact/supported | 内部证据 c0f6a87194ae842f（未公开；来源记录由维护者保留）: status=accepted; review.verdict=accepted; reviewer_actor_id=`ReviewGateAUDIT-degas(glm-5.3-flash)` ≠ author_actor_id=`AuditDegas`; review.independent_from_author=true; 13 reviewed_artifact_hashes == 13 artifacts; review.evidence_path=内部证据 579d6824294f3c9d（未公开；来源记录由维护者保留） | `[史料]`（产物） | 本 lane 不重新审计，只复用结论 |
| 8 | LD-AUDIT-MANIFEST | AUDIT 182 行 claim map / 8 quotes / 13 images | fact/supported | 内部证据 c89bf80c39d1cccd（未公开；来源记录由维护者保留）: claims_total=182, per-status {supported:87,partial:34,conflict:11,unverified:50}=182, locator_failures=0, images_public=13, images_distribution.cc_by_sa_4_0_rows=1, external_fetches=5 | `[史料]`（产物） | 复用，不冒充本轮复跑 |

<a id="db-source-line-24"></a>
## B. 前置知识（learning_path §1）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 9 | LD-K1-APPARATUS | 风格 = 取景与工作装置（现场取材→画室记忆重构→裁切俯视→粉彩层积→反复重做），非「芭蕾滤镜」 | observation/supported | `dossiers/degas.md:17`（§0 一句话能力定位）、`:183`（§6.2 一句话总结）、`:51-61`（§2 技法 11 条） | `[归纳]`/`[研究]` | 非作者原话 |
| 10 | LD-K2-TWO-MECHANISMS | 两条主线：舞台逆光/俯视取景（偏心≥15%/切割/视平线≥55%/人工光亮部≤35%）+ 粉彩层积（覆盖≥70%/方向族2–5/色层≥2/底子≥5%） | fact/supported | `dossiers/degas.md:34-38`（§1-1/-2/-4/-5）、`:245-252`（§8.2-1/-2/-3/-5/-8）、`:254`（末注 `[归纳]`）；`modules/degas.md:9-13,45-52` | `[归纳]` | 数值非史料/非像素实测 |
| 11 | LD-K3-PARAMS | §4 六参数默认 70/60/55/65/55/2；P1/P2/P5 定身份、P3/P4 定时期媒介、P6 工作流 | fact/supported | `dossiers/degas.md:101-108`（§4 表）、`:110`（用法）；`modules/degas.md:58-67` | `[归纳]` | 各参数标 `[归纳]` |
| 12 | LD-K4-NO-THEORY | 德加无理论著作/系统宣言；文字散见笔记本/书信/同时代人转记；「内心如何」降级为操作规则 | fact/supported | `dossiers/degas.md:7`（§0 口径）、`:76`（§3-8）、`:117`（§5 口径） | `[史料]`/`[归纳]` | 本卡不发明理论 |
| 13 | LD-K5-7030 | 70/30 纪律：选一个主导轴 + 莫奈包络降档（≤弱档）保留德加轮廓线 | fact/supported | `dossiers/degas.md:86`（§3.1 组合纪律）、`:241`（§8.1 组合注意）；`modules/degas.md:74`（冲突注记 vs 莫奈） | `[归纳]` | 写死条款，可实验推翻 |
| 14 | LD-K6-N3-TENSION | **N3 张力（未决）**：dossier「降档」vs conflicts.md N3②「整条移除（不是调档）」；degas 在 conflicts.md 0 行，从未纳入轴所有权表 | observation/conflict | `dossiers/degas.md:86` × `conflicts.md:311-312`（N3②）、`:80`（C-02①）、`:93`（C-05②）、`:214`（C-12 降档要写进卡）；`AUDIT-degas/counterexample.md` §Relation、RESULT §70/30、`claim_evidence_map.csv` `[inference]` 行；`grep -cE 'degas|德加| Dega' conflicts.md`=0 | `[归纳]`/AUDIT `[inference]` | **本 lane 只携带、不裁决、不改仓库** |
| 15 | LD-K7-BOUNDARY | 四向越界警报（莫奈/修拉/卡拉瓦乔/米开朗基罗）+ C-05/C-08/C-09/C-12 预检 | fact/supported | `dossiers/degas.md:111`（§4 越界警报）、`:95`（§3.1 与系统其余模块）、`:260-262`（§8.3 三条）；`modules/degas.md:68,78` | `[归纳]` | 项目对齐口径 |
| 16 | LD-K8-8QUOTES | 8 条原书引文为 ACCEPTED 证据（Moore×5 + Vollard×3，8/8 命中） | observation/supported | 内部证据 3ae54236efe9186b（未公开；来源记录由维护者保留）（36 行，8 行 supported 指向原书行号）、`risk_fetch.md` §Verification（8/8 located）、`RESULT.md §A-55`；`_corpus/degas.md:7,12,111,120,129,162,169,276,283`；dossier 自审 B2/B3 `:449-450`、§10-1 `:294` | `[史料]`（原书级，AUDIT 复跑） | 复用，非本轮新抓 |

<a id="db-source-line-37"></a>
## C. 重点作品 / 权利 / 原书引文（learning_path §2）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 17 | LD-WORKS-12 | §12 临摹清单 10 件（各看/学/练），本路径引用不新增 | fact/supported | `dossiers/degas.md:380-434`（§12）、`:21-25`（§0 关键 5 件） | `[史料]`（作品）/`[归纳]`（练习） | 练习为本项目设计 |
| 18 | LD-RIGHTS-13 | 13 张公开图 = 5 Met CC0 + 6 Orsay Commons PD + 2 NGL | fact/supported | 内部证据 98175bb2d31b3b29（未公开；来源记录由维护者保留）（13 行表）、`coverage-manifest.json:images_distribution`、`_images/manifest.md:247-259`、`_images/degas/MANIFEST.md:11-49` | `[史料]`（权利） | 本轮未目检 `image_seen=0` |
| 19 | LD-NG486-CCBYSA | **NG486《Combing the Hair》照片 CC BY-SA 4.0 需署名 + share-alike，原作 PD 但照片许可不折叠** | fact/supported | 内部证据 05ca7d5fa7549bf7（未公开；来源记录由维护者保留）；`_images/manifest.md:255`；`_images/degas/MANIFEST.md:21,47`（「本 manifest 即署名记录/引用需署名」）；`dossiers/degas.md:26,303`；`coverage-manifest.json:cc_by_sa_4_0_rows=1` | `[史料]`（权利） | 唯一非 PD/CC0 行；本 lane 保留、不升级不降级 |
| 20 | LD-RIGHTS-MET-UNVERIFIED | Met 5 张 CC0 为 manifest-recorded（429/API 404 未重验）；Orsay Cloudflare 未重取 | fact/supported | 内部证据 0f3a72cf51e0abf5（未公开；来源记录由维护者保留）、`risk_fetch.md` F6/F7（429/404）、`RESULT.md §Risk fetches` | `[史料]`（诚实限制） | 不冒充本轮在线复核 |
| 21 | LD-8Q-MOORE-1 | #1「没有比我的艺术更不即兴」Moore 1891 原书 | fact/supported | 内部证据 caf83708b4b97fac（未公开；来源记录由维护者保留）（OCR `spontaiie-ous` 已校准）；`quote_audit.md:1`；`_corpus/degas.md:12-17`；`dossiers/degas.md:119-122` | `[自述]`（转记 Moore 1891） | 原书级，AUDIT 复跑 |
| 22 | LD-8Q-MOORE-14 | #14「你要自然的生命；我要人工的」(viefactice) | fact/supported | `raw/moore_1891.txt:13455`；`quote_audit.md:14`；`_corpus/degas.md:111-118`；`dossiers/degas.md:123-126` | `[自述]` | vs 莫奈一手依据 |
| 23 | LD-8Q-MOORE-16 | #16「就像你透过锁孔看」(key-hole) | fact/supported | `raw/moore_1891.txt:13788-13796`；`quote_audit.md:16`；`dossiers/degas.md:127-130` | `[自述]` | 锁孔/背面视角依据 |
| 24 | LD-8Q-MOORE-35 | #35「人类动物忙着自己；一只舔自己的猫」(原书补录) | fact/supported | `raw/moore_1891.txt:13782`（`bete`/`leche` 无重音 OCR）；`quote_audit.md:35`；`_corpus/degas.md:276-280` | `[自述]` | 原书核验新增 |
| 25 | LD-8Q-MOORE-36 | #36「很难像老大师们那样伟大」(原书补录) | fact/supported | `raw/moore_1891.txt:13642-13646`；`quote_audit.md:36`；`_corpus/degas.md:283-287` | `[自述]` | 原书核验新增 |
| 26 | LD-8Q-VOLLARD-15 | #15「画面里的空气不必是户外的空气」(flannel vest) | fact/supported | `raw/vollard_1927.txt:4055-4058`；`quote_audit.md:15`；`_corpus/degas.md:120-121`；`dossiers/degas.md:69` | `[自述]` | 反户外/画室依据 |
| 27 | LD-8Q-VOLLARD-20 | #20「人们叫我画舞女的画家…动作与漂亮衣裳」 | fact/supported | `raw/vollard_1927.txt:5525-5527`；`quote_audit.md:20`；`_corpus/degas.md:162-167` | `[自述]` | 职业劳动题材依据 |
| 28 | LD-8Q-VOLLARD-21 | #21「幸好我还没找到自己的风格」；wikiquote 转录用词语序差异已记录 | fact/supported | `raw/vollard_1927.txt:4933-4934`（"Well, I'm glad I haven't found my style yet…"）；`quote_audit.md:21,§A-55`；`_corpus/degas.md:169-174` | `[自述]` | 不静默「改正」转录差异 |
| 29 | LD-SECONDARY-UNVERIFIED | 6 个二手转记载体（Sérullaz/Jeanniot/Gammell/Valéry/Terrasse/Guérin 书信）原书未直读 → 对应语料 `unverified`/`partial`；#13 Shop-Talk「别展示光源」仅弱证据 | fact/supported | `dossiers/degas.md:294`（§10-1）；内部证据 244876b595eb2202（未公开；来源记录由维护者保留）；`_corpus/degas.md:103`（#13） | `[史料]`（诚实限制） | 不升级为 supported |

<a id="db-source-line-55"></a>
## D. 机制 / 练习 / 反例（learning_path §3-§6 / mechanism_notes）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 30 | LD-MECH-A | 舞台逆光/俯视取景 = P1+P3+§8.2-1/2/3 复合；「逆光」是学习路径标签，不新增仓库未载光位事实 | observation/supported | `dossiers/degas.md:37,105,111,216,245-247`；`modules/degas.md:9-11,45-47,62`；内部证据 6094a6531339cfb6（未公开；来源记录由维护者保留） | `[归纳]`/`[研究]` | brief 强调①；阈值未实测 |
| 31 | LD-MECH-B | 粉彩层积 = P4+§8.2-5/8 复合；hachure/固定剂再叠/monotype→粉彩；与 C-05 关系 | observation/supported | `dossiers/degas.md:52,54,107,249,252,260`；`modules/degas.md:49,52,63`；`conflicts.md:36,109-121`；`mechanism_notes.md §4` | `[归纳]`/`[研究]` | brief 强调② |
| 32 | LD-PRACTICE-3LADDER | 三阶梯练习（取景/粉彩/组合自律）全部建议练习 `[归纳]` | design_candidate/supported | 内部证据 c42c43fb5123aab7（未公开；来源记录由维护者保留）；`01-AUDIT.md:271,273`；`02-EXECUTION-PLAN.md:64-66`；`dossiers/degas.md:380-434`（§12 映射） | `[归纳]` | 无「已证实学习收益」 |
| 33 | LD-COUNTEREXAMPLES | 2 个 §4 反例 + 1 个 70/30 张力，均 `[inference]` 纸面、无渲染/无像素 | observation/supported | 内部证据 b19ad4573526cd0c（未公开；来源记录由维护者保留） Attempt 1（贝列里一家 false negative）/ Attempt 2（后台抓拍照 false positive）/ §Relation（70/30 vs N3）；`dossiers/degas.md:110,234,236,414-417` | `[inference]`（AUDIT） | 本 lane 只携带 |
| 34 | LD-IDENTITY-GATE | §4 用法 P1/P2/P5 ≥2 ≥中档 定「是不是德加」；早期肖像档被结构性排除 | fact/supported | `dossiers/degas.md:110`；`AUDIT-degas/counterexample.md` Attempt 1 | `[归纳]`/AUDIT `[inference]` | 时期边界 |

<a id="db-source-line-65"></a>
## E. 70/30 + N3 张力 / 冲突行（learning_path K6/§4阶梯三 / how-to-think D8 / mechanism_notes §6）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 35 | LD-7030-SOURCE | 70/30 出现在 dossier §3.1/§8.1 + 模块卡 + conflicts C-02/N3 | fact/supported | `dossiers/degas.md:86,241,451,495,500`；`modules/degas.md:74`；`conflicts.md:77`（C-02 L71 注）、`:311-312`（N3）、`:214`（C-12 降档写进卡） | `[归纳]` | 纪律口径一致 |
| 36 | LD-N3-REMOVE | N3②「辅模块冲突轴 §8.2 规则整条移除（不是调档），§8.2 是判分规则非强度旋钮」 | fact/supported | `conflicts.md:311-312`（N3 正本）、`:80`（C-02①）、`:93`（C-05②）、`:119`（C-05 轴所有权+反约束重算）、`:328`（N9） | `[归纳]` | 与 #35 口径相左 |
| 37 | LD-DEGAS-NO-ROW | degas/德加 在 conflicts.md / _crosscheck.md / _review.md 均 0 行；分工条款在 dossier §3.1 + roster:85/145 | fact/supported | 内部证据 65e0c10a78041858（未公开；来源记录由维护者保留）、`coverage-manifest.json:conflicts_degas_rows=0`；`grep -cE 'degas|德加' conflicts.md`=0（本 lane 复跑） | `[史料]`（覆盖结构，非缺陷） | AUDIT 已判 |
| 38 | LD-TENSION-UNRESOLVED | 张力为契约层未决：本 lane 并列记录、不静默选边、不写「已解决」、不改仓库 | observation/conflict | `AUDIT-degas/counterexample.md §Relation`、`RESULT.md §70/30`；内部证据 f1fce14a0a8ea821（未公开；来源记录由维护者保留）、`how-to-think.md D8`、`mechanism_notes.md §6` | `[归纳]`/AUDIT `[inference]` | 需 CONFLICT/RULE lane 写权后裁定 |
| 39 | LD-CONFLICT-RULES | C-05/C-08/C-09/C-12 为规则层判定，非 E2/E3 实验验证 | fact/supported | `dossiers/degas.md:260-262`（§8.3）、`:95`；`modules/degas.md:78`；`conflicts.md:36,43,109-121,203`；`AUDIT-degas/RESULT.md §Honest limits` | `[归纳]` | 不冒充组合实验通过 |
| 40 | LD-DRIFT-CARRIED | 11 处 conflicts.md locator 漂移（C-DRIFT-1..11）沿用 AUDIT 登记、未改仓库 | fact/supported | 内部证据 d691a88b7e24aab1（未公开；来源记录由维护者保留）、`claim_evidence_map.csv` C-DRIFT 行（11 行 support_status=conflict） | `[史料]`（诚实限制） | read-only, one writer per tree |

<a id="db-source-line-76"></a>
## F. 等级 / 边界 / 产物（RESULT.md §5 / receipt claims）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 41 | LD-GRADE-SEPARATION | `[自述]`/`[归纳]`/`[研究]`/`[史料]` 严格分栏；`[推测]`=0；无从画面推作者心理 | observation/supported | 内部证据 be9b9679cc44c516（未公开；来源记录由维护者保留）；`00-GOAL.md:9`；`dossiers/degas.md:7,117` | `[归纳]` | 红线 |
| 42 | LD-PRACTICE-UNVERIFIED | 练习 = 建议练习 `[归纳]`，human_review=not_applicable，零「已证实学习收益」 | fact/supported | `01-AUDIT.md:273`；内部证据 db90625325436d39（未公开；来源记录由维护者保留）、`RESULT.md §5`、receipt `human_review.status=not_applicable` | `[归纳]` | 不写学习成效 |
| 43 | LD-A30-SHAPE | learning_path.md 为 A-30 §8.1 八节形状 | fact/supported | `01-AUDIT.md:269-273`（§8.1 八节：前置知识/重点作品及来源/要观察的机制/具体练习/可观察结果/常见失败/下一步/使用边界）；[learning_path.md](learning_path.md) §1–§8 | `[归纳]`（结构） | 八标题齐全 |
| 44 | LD-STATUS-SUBMITTED | status=submitted、review=null、author 不自接受、无 bound LEARN-degas contract → schema-only 验证 | fact/supported | 内部证据 bb811b6faebfa1e2（未公开；来源记录由维护者保留）；内部证据 c33b8e9a20496b0c（未公开；来源记录由维护者保留） 无 `LEARN-degas.contract.json`（本 lane 核）；`templates/receipt.schema.json`；`tools/verify-receipt.py` | `[史料]`（产物状态） | 与 LEARN-monet/sargent 同口径 |
| 45 | LD-WRITE-SCOPE | 仅写 内部证据 783dc2444eb3e2ac（未公开；来源记录由维护者保留）；仓库只读、无 git、无子代理、无凭据 | fact/supported | `tasks-plan.json` `LEARN-degas.allowed_write_paths`=内部证据 16a22fd60f96ba87（未公开；来源记录由维护者保留）、`spawns_allowed=false`、`execution_kind=leaf_work_item`；`RESULT.md §6` | `[史料]`（契约） | brief 口径 |
| 46 | LD-7FILE-CONTRACT | 7 文件：5 内容 md（result_summary/learning_path/how_to_think/mechanism_notes/claim_evidence_map）+ runner_receipt.json + receipt.json | fact/supported | 内部证据 783dc2444eb3e2ac（未公开；来源记录由维护者保留） 目录盘点；`receipt.json:artifacts`（5 件）；required_artifact_kinds=`result_summary/learning_path/mechanism_notes/claim_evidence_map`（tasks-plan.json:2335-2340），`how_to_think` 追加登记 | `[史料]`（产物） | 与已 accepted 兄弟同形 |

---

<a id="db-source-line-89"></a>
## 复跑命令（本机只读 + 收口验证）

```bash
# 从公开仓库根目录执行；注释计数及行号来自源记录，不是此次投影重跑结果。
sha256sum knowledge/domains/painters/modules/degas.md knowledge/domains/painters/dossiers/degas.md knowledge/domains/painters/dossiers/_corpus/degas.md
sha256sum knowledge/cross/conflicts.md ops/GOALS.md
grep -cE 'degas|德加' knowledge/cross/conflicts.md          # 0（AUDIT 覆盖结构）
grep -n '^### ' knowledge/domains/painters/dossiers/_corpus/degas.md | wc -l   # 36
nl -ba knowledge/domains/painters/dossiers/degas.md | sed -n '86p;110p;111p;245,252p'
nl -ba knowledge/cross/conflicts.md | sed -n '80p;93p;311,312p'
```

> 原本机绝对路径与内部回执/schema验证命令留在维护者的私有复核记录。这里仅保留公开仓库相对路径的复核示例；本次投影没有执行这些命令，也没有更新其历史计数、行号或证据等级。

> 验证命令 **exit code 与 JSON 输出在 `RESULT.md §6` / 最终答复中如实报告**；为避免 receipt 自哈希循环，不把验证输出预写进本文件、不列为 artifact。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
