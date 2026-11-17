<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-goya；原正文 SHA-256 `c854ec3e79627b982d854aeb8cabdb15e3769ac586c720d4ee75fe986d13c938`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-goya — claim_evidence_map

> 逐 claim 带 `文件:节:行号 + 子串` 定位（沿用 ACCEPTED `AUDIT-goya/claim_evidence_map.md` 的 locator 纪律，61/61 已由 AUDIT 与独立审者程序化回源）。本片 locator 为**本包自述**（指向本包 5 文件 + 仓库只读输入 + AUDIT 产物）。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；corpus `[self-written]/[reported speech]/[contemporary record]`；AUDIT 反例 `[inference]`。support_status ∈ {supported, partial, conflict, unverified, not_applicable}。
> 约定：`@ f0089523` = 仓库只读 commit `f008952365a77e140cbda3f3959d43ef000f9a22`；`AUDIT` 前缀 = 内部证据 17d8c3be34400a32（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 2b6870abd1657993（未公开；来源记录由维护者保留）。本片 `[推测]` 计数 = 0。

<a id="db-source-line-7"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LG-DEP-01 | `AUDIT/receipt.json`: `"status": "accepted"`, `"review": {"verdict": "accepted", "reviewer_actor_id": "ReviewGateAUDIT-goya(glm-5.3-flash)"}`, `author_actor_id: "AuditGoya"`, `19 artifacts == 19 reviewed_artifact_hashes` | `[史料]` | supported | 依赖底本已 ACCEPTED；审者≠作者；见 `AUDIT/review-evidence.md:§9 "ACCEPT"` |
| LG-DEP-02 | `AUDIT/coverage-manifest.json`: `claims_total=61`, `per_status_counts={supported:17,partial:42,unverified:2}`, `locator_verification.all_resolve=true total_checked=61`, `external_fetches_count=3`, `images_rights_row_level={CC0:4,Public_domain:5,unknown:0}` | `[史料]` | supported | AUDIT 61 行 claim map / 3 fetch / 9 图逐行权利结论；本片复用不重审 |
| LG-IN-01 | 内部证据 a6cc8803dc5b3b10（未公开；来源记录由维护者保留）: sha256 `06076de8…9873`, 85 行；`L9` 画内证据光、`L44` 提灯规则、`L66` P1/P2 用法、`L73` C-01、`L84` near-miss 8 对 | `[史料]` | supported | 开工现场 `sha256sum` 实测，与 `artist-shards.json` 及 AUDIT §1 表一致 |
| LG-IN-02 | 内部证据 6a329060b3e1baa9（未公开；来源记录由维护者保留）: sha256 `a50f0d27…ee73`, 512 行；`§1-1:L32`、`§4:L97-102`、`§8.2:L235-242`、`§10-6:L298`、`§10-9:L301`、`§12:L390-433` | `[史料]` | supported | 同上；本片所有机制/作品/阈值回源此档案 |
| LG-IN-03 | 内部证据 f20ca1ed2b37b277（未公开；来源记录由维护者保留）: sha256 `fd9efc70…fddd`, 22 条 `###`；`#1 L10-15`、`#6 L46-51`、`#9 L69-74`、`#10 L76-81`、`#5 L38-44` | `[史料]` | supported | 语料 22 条；AUDIT `quote_audit.md` 22/22 有中文意译；本片不重跑 |

<a id="db-source-line-17"></a>
## §B 暗色底 + 强光主体 / 画内光源数实测判据（brief ①；8 行）

| claim_id | locator | grade | status | basis |
|---|---|---|---|---|
| LG-M1-01 | `dossiers/goya.md:§1-1:L32` 子串「画内可见光源数 ≥1（对照卡拉瓦乔 = 0）」「提灯置于两组人之间地上」；`modules/goya.md:L9`「光源在画内且可指认（≥1）」 | `[史料]`/`[研究]` + `[归纳]`判据 | supported | AUDIT claim map `S1-1`（supported，R4 逐字「A square lantern situated on the ground between the two groups」）|
| LG-M1-02 | `dossiers/goya.md:§8.2-1:L235` / `modules/goya.md:L44`「画内可见光源数 ∈ [1,2]…亮区重心…落在受害者组包围盒内；施害者组平均亮度 ≤ 全帧平均亮度的 40%」 | `[归纳]` | partial | 四项可实测判据；但 `§8.2 尾注:L244` + `§10-6:L298` 明记「未对原作做像素测量（分母＝假想参考帧）」→ 不升 supported |
| LG-M1-03 | `dossiers/goya.md:§3.1:L80`「① 画内可见光源数：戈雅 ≥1（提灯型）／卡拉瓦乔 = 0；② 主体组织…；③ 背景…」 | `[归纳]` | partial | AUDIT claim map `S3.1-a`（`L35`）判 partial（对侧零命中，见 §C）；分工判据为写死文本、非实验 |
| LG-M1-04 | `AUDIT/risk_fetch.md:claim#1` + `raw/risk_fetch_hashes.json:R4`: `f8f2e10a…d0`, 398502 B, HTTP 200；逐字「The brightest illumination falls on the huddled victims to the left」「Seen nearly from behind」 | `[研究]` | supported | R4 作为 ACCEPTED 证据复用（brief ③）|
| LG-M1-05 | `dossiers/goya.md:§1-6:L37`「土黄/棕/黑为底，白只作闪光…红只作血」+ `§1-7:L38`「哑光砂质」；R4 逐字「earth tones and black, punctuated by bright flashes of white」「a granular solution producing a matte, sandy finish」 | `[研究]` | supported | AUDIT claim map `S1-6`/`S1-7`（均 supported）；本片「暗色底」半 |
| LG-M1-06 | `dossiers/goya.md:§8.2-5:L239`（S≥0.6 ≤3% / 黑土色 ≥60% / 白高光连通域 ≤5 / 红仅伤口）、`§8.2-6:L240`（无镜面高光、哑光砂质） | `[归纳]` | partial | 可自查规则；阈值未像素实测（`L244`）|
| LG-M1-07 | `dossiers/goya.md:§2-7:L55`「把提灯放在两组人**之间**的地上——光源位置本身就是构图轴线；光只照亮受害者组，施害者沉入阴影」 | `[研究]` | supported | AUDIT claim map `S2-7`（supported，R4 逐字）；「强光主体」半 |
| LG-M1-08 | `AUDIT/counterexample.md:反例1/反例2` 均标 `[inference]`；《农神吞噬其子》无画内提灯、《卡洛斯四世一家》P1/P2 弱档仍为戈雅正典 | `[inference]` | partial | AUDIT `RESULT.md §7`；证明「画内光源数≥1 ⇒ 戈雅」是**夜戏/处决子类型签名**，非全 oeuvre 必要件；非已验证实验、非画家意图 |

<a id="db-source-line-30"></a>
## §C A-23 写死 one-sided 作为 known-open 携带（brief ②；6 行）

| claim_id | locator | grade | status | basis |
|---|---|---|---|---|
| LG-ONE-01 | `AUDIT/RESULT.md:§5:L116`「A-23『写死』单向事实：caravaggio.md / rembrandt.md 全文 grep -i 'goya\|戈雅' 零命中——分工条款只写在 goya.md §3.1 一侧」 | `[归纳]` | partial | 单向落盘事实；AUDIT 登记为适用边界，不改仓库 |
| LG-ONE-02 | `AUDIT/claim_evidence_map.md:S3.1-a:L35`「caravaggio.md 无『戈雅/goya』对侧条款——GOALS A-23『分工写死』为单向」、`S3.1-b:L36`「rembrandt.md 无…对侧条款，分工为单向」 | `[归纳]` | partial | 两条均判 partial，不升级 |
| LG-ONE-03 | `AUDIT/claim_evidence_map.md:S3.1-d:L38`「hogarth.md §3.1 明记『goya.md（wave13 定稿）无对侧条款……本档为唯一写死正本』」 | `[归纳]` | partial | 两档口径需并读；`review-evidence.md` F2 注记 hogarth 引文在 dossier L86/L303 |
| LG-ONE-04 | `AUDIT/conflicts_locator_drift.md:§1`「grep -n -i 'goya\|戈雅' conflicts.md → 零命中」、`§4`「单向『写死』事实」；`coverage-manifest.json:conflicts_rows_checked.literal_goya_or_geya_hits_in_conflicts=0` | `[史料]` | supported | goya 的 C 行只来自 card 冲突注记（C-01/C-11/C-12/C-05/C-07/C-17 + vs-伦勃朗），非 conflicts 正本具名 |
| LG-ONE-05 | `ops/GOALS.md:A-23:L37`「分工 vs 卡拉瓦乔/伦勃朗写死（画内光源数等可实测判据）」 | `[史料]` | supported | GOALS 原文确实写「写死」；但 AUDIT 证明落盘单向 → 记为口径适用边界 |
| LG-ONE-06 | `LEARN/learning_path.md:§7` + `how-to-think.md:D8` + `mechanism_notes.md:§6②` + `RESULT.md:§3` 四文件一致「作为 known-open 携带，不收口、不补对侧互引、不升级为已完成双向写死」 | `[归纳]` | supported | 本包 5 文件一致携带；收口交对应 dossier 写手 / CONFLICT·RULE lane |

<a id="db-source-line-41"></a>
## §D R4/R14/R3 fetch 锚点作为 accepted evidence（brief ③；5 行）

| claim_id | locator | grade | status | basis |
|---|---|---|---|---|
| LG-FETCH-01 | `AUDIT/coverage-manifest.json:external_fetches[0]`: `R4_third_of_may`, url `…/The_Third_of_May_1808`, `http_status=200`, `bytes=398502`, `sha256=f8f2e10a1e69369a85dbc4a4085f344071f456955f9f9d340b28899271d932f0` | `[史料]` | supported | AUDIT 实测；逐字命中见 `risk_fetch.md`「Verbatim corroboration」|
| LG-FETCH-02 | `AUDIT/coverage-manifest.json:external_fetches[1]`: `R14_disasters_of_war`, `http_status=200`, `bytes=409100`, `sha256=35f0ed8aa3aa5ba3d5ba5e4ab842129602056baa93a79df2f1070ea16d016bde`；逐字「series of 82 prints created between 1810 and 1820」「not published until 1863」「I saw this (plate 44)」 | `[史料]` | supported | 同上；序列帧/题刻/出版史证据 |
| LG-FETCH-03 | `AUDIT/coverage-manifest.json:external_fetches[2]`: `R3_francisco_goya`, `http_status=200`, `bytes=540157`, `sha256=7f5dc028288d56674d778c3adbb9f886009116d26a114ec0440caa053fd6d34c`；「last of the Old Masters and the first of the moderns」 | `[史料]` | supported | 同上；生平/定位证据 |
| LG-FETCH-04 | `AUDIT/risk_fetch.md:Honest limits`「Prado [R10] 直连 403…Met [R1] 直读 429…西语原信 / Matheron 1858 / Prideaux 1909 原书均未直读」 | `[史料]` | supported | 诚实限制一并携带；3/3 reachable 无 IncompleteRead、未触发 RESUME |
| LG-FETCH-05 | `AUDIT/review-evidence.md:§9`「3/3 fetch-cache sha + anchors」由审者独立复现 → `Verdict ACCEPT` | `[史料]` | supported | 本片作为 **ACCEPTED 证据复用**，不重访 URL、不重算字节、不冒充本片自己 fetch |

<a id="db-source-line-51"></a>
## §E rights drift 4CC0+5PD vs 3+6（brief ④；5 行）

| claim_id | locator | grade | status | basis |
|---|---|---|---|---|
| LG-RIGHT-01 | `AUDIT/rights_review.md:Aggregate & discrepancy`「Row-level count…**4 CC0 + 5 PD = 9 public images**」；`coverage-manifest.json:images_rights_row_level={CC0:4,Public_domain:5,unknown:0,guessed_pd:0}` | `[史料]` | supported | 逐行逐对象权利记录；9/9 有 license label，0 unknown、0 猜测 PD |
| LG-RIGHT-02 | `AUDIT/rights_review.md:per-image table`: CC0 4 件（Sleep of Reason / Yo lo vi pl.44 / Manuel Osorio / Tauromaquia pl.18）、PD 5 件（Third of May / Saturn / Family of Charles IV / The Dog / Witches' Flight） | `[史料]` | supported | 逐行标签明细；全局 `_images/manifest.md` L81–L89 与之逐行一致 |
| LG-RIGHT-03 | `dossiers/goya.md:§10-9:L301`「9 张已核（Met 3 张 CC0 + Commons PD 6 张）」；`ops/GOALS.md:A-23:L37`「Met CC0×3 + PD×6」；`_images/goya/MANIFEST.md 头部`（AUDIT RESULT §4 L105 转录） | `[史料]` | conflict | 三处汇总写 **3 CC0 + 6 PD**，与逐行 4+5 不一致 → 标 conflict（口径漂移），不修 |
| LG-RIGHT-04 | `AUDIT/conflicts_locator_drift.md:§3`「另一处口径漂移（非行号，一并记录）」+ `AUDIT/review-evidence.md:§9`「rights drift confirmed with honest registration」 | `[史料]` | supported | 审者独立确认漂移；AUDIT 采用逐行标签（逐对象权利记录）|
| LG-RIGHT-05 | `LEARN/learning_path.md:§2/§6/§8` + `how-to-think.md:D8` + `mechanism_notes.md:§6④` + `RESULT.md:§3` 四文件一致「照实携带、不修仓库、不替仓库选定真值」 | `[归纳]` | supported | 核 wave13 计数口径交 CONFLICT/RULE/IndexMerge lane；9 图 image_seen=0、许可真实性未升级 |

<a id="db-source-line-61"></a>
## §F 学习交付物形状与纪律（7 行）

| claim_id | locator | grade | status | basis |
|---|---|---|---|---|
| LG-A30-01 | `package/01-AUDIT.md:§8.1:L269-273`「每位路径至少明确：前置知识、重点作品及来源、要观察的机制、具体练习、可观察结果、常见失败、下一步及使用边界…练习效果…明确为建议练习，不写『已证实学习收益』」 | `[史料]` | supported | A-30 八节形状；`LEARN/learning_path.md` §1–§8 八标题齐全 |
| LG-A30-02 | `LEARN/learning_path.md:§0` 三阶梯（基础/进阶/比较）+ §7 可替换分支与跨艺术家比较 | `[归纳]` | supported | 满足「总路线说明基础/进阶顺序、可替换分支和跨艺术家比较方式」|
| LG-A30-03 | `LEARN/how-to-think.md:§0` 严格分栏表 + D1–D8 决策序；`[自述]`/`[reported speech]`/`[归纳]` 不混写一句；`[推测]` 计数 = 0 | `[归纳]` | supported | `dossiers/goya.md:§0:L7`「凡本档案标 [自述] 者 = 有明确文本出处」+ 00-GOAL.md:L9 不从外观反推心理 |
| LG-A30-04 | `dossiers/goya.md:§12:L386-435` 9 件「看什么/学什么/怎么练」+ `§5 口径:L111`「任何一条都不得当作画论体系引用」 | `[史料]` | supported | 练习条目为 `[归纳]`（本项目设计），作品信息 `[史料]`；本片沿用不重编生平 |
| LG-A30-05 | `AUDIT/counterexample.md:Consequence`「the gate's semantic boundary is narrower than 'all Goya'…recorded as a boundary condition a LEARN path must state」 | `[inference]` | supported | 本片 5 文件均声明「夜戏/处决子类型签名，非全 oeuvre 必要件」，满足 AUDIT 交接要求 |
| LG-A30-06 | `LEARN/learning_path.md:§5`、「RESULT.md:§5」、`receipt.json:human_review.status=not_applicable` 全部「建议练习、无人评、不写已证实学习收益」 | `[归纳]` | supported | 01-AUDIT.md L273；`review=null`、作者不自接受 |
| LG-A30-07 | `RECEIPT.json:required_artifact_kinds` 对应 `task-registry.json:LEARN-goya` = {result_summary, learning_path, mechanism_notes, claim_evidence_map}（另含 how_to_think） | `[史料]` | supported | 7-file contract = 5 内容 md + runner_receipt.json + receipt.json |

<a id="db-source-line-73"></a>
## §G 携带的 open / 诚实边界（6 行）

| claim_id | locator | grade | status | basis |
|---|---|---|---|---|
| LG-OPEN-01 | `AUDIT/RESULT.md:§9:1` conflicts.md 无 goya 字面命中 + 8 处被引用文件行号漂移；`AUDIT/conflicts_locator_drift.md:§2` 8 行 DRIFT 表 | `[史料]` | supported | 报告不修；交 CONFLICT/RULE lane；本片不改仓库 |
| LG-OPEN-02 | `AUDIT/RESULT.md:§9:2` A-23 单向写死；`§9:3` 权利 4+5 vs 3+6；`§9:4` 9 图许可真实性/像素未独立复核（image_seen=0） | `[史料]` | supported | 全部作为 open 携带，见 §C/§E |
| LG-OPEN-03 | `AUDIT/RESULT.md:§9:5` Prado 403 / Met 429 / 西语原信与 Matheron·Prideaux 原书未直读；`§9:6` §4/§8.2 阈值 `[归纳]` 未实测 | `[史料]` | supported | partial/unverified 不升级；R4/R14/R3 为 Wikipedia 同源交叉 |
| LG-OPEN-04 | `AUDIT/review-evidence.md:§9`「Findings F1–F3 cosmetic/non-blocking; author's honest-limit registrations … are correctly kept as unresolved rather than upgraded」 | `[史料]` | supported | 独立审者确认；本片沿用不重审 |
| LG-OPEN-05 | `LEARN/RESULT.md:§3` + `receipt.json:review=null, status=submitted, execution_dedup_key=null, author_actor_id=LearnGoya` | `[归纳]` | supported | 作者不自接受；无 bound LEARN-goya contract，`verify-receipt.py` 对 submitted 只跑 JSON Schema 结构门 |
| LG-OPEN-06 | 内部证据 43fbca080d776e3f（未公开；来源记录由维护者保留）, 0 仓库写入 / 0 子代理 / 0 凭据 | `[归纳]` | supported | 仅 staging 写；repo READ-ONLY @ f0089523（开工 sha 复核，见 RESULT §0）|

> 合计 42 行（§A5 + §B8 + §C6 + §D5 + §E5 + §F7 + §G6）。本片 `[推测]` = 0；无「已证实学习收益 / 已完成对齐 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
