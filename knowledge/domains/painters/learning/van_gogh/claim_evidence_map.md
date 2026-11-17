<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-van_gogh；原正文 SHA-256 `a62e6fca1b159a8adb76b73e7ae6b33aae42e950a5ad418dc1e2f5ed8caa9bf6`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-van_gogh — claim → evidence map（每条论断带 locator）

> 任务 `LEARN-van_gogh` (A-30) · 依赖 `AUDIT-van_gogh`（**ACCEPTED**，内部证据 d5ff79b15cbba596（未公开；来源记录由维护者保留） `review.verdict=accepted`、reviewer `ReviewGateAuditVanG`、`independent_from_author=true`）。
> **口径（复用 ACCEPTED 审计的 locator 纪律，不重新审计）**：每条论断给「来源文件 + 具体行/节定位 + 证据等级 + 支持状态」。内部证据 4874f193014ae79c（未公开；来源记录由维护者保留） 为只读回源（声明基线 `f008952365a77e140cbda3f3959d43ef000f9a22`，本 lane 开工 `sha256sum` 实跑复核四件冻结输入，见 `RESULT.md §2`）；内部证据 736a717f169d9664（未公开；来源记录由维护者保留） 为上游 ACCEPTED 产物；内部证据 9af561c2622b4a1d（未公开；来源记录由维护者保留） 为本 lane 生成。
> 等级沿用仓库口径：`[自述]`/`[self-written]`/`[reported speech]` = 作者/同时代人言语记录；`[归纳]` = 项目操作规则/研究者归纳；`[研究]`/`[史料]` = 二手研究/博物馆史实/权利记录；`[推测]` 本 lane **不使用（计数 0）**。
> 版本列：仓库文件 = `f0089523…`；staging artifact = 本轮/上游生成（给 sha256）。`read_scope` 与 `access_status` 分开：外部 URL 本轮未重访 = `unknown`，本机文件 = `available`，原图像素目检 = 0（无 `image_seen`）。
> **行号纪律（本卡点名）**：`conflicts.md:168` 把 §8.2-4/§8.2-5 写成 `L205/L206`，**实测 dossier = L207/L208**（+2 漂移）；C-05/C-12 同属 +2。本表一律用**实测行号**（dossier §8.2-1=L204…-7=L210；card 对应 46–52；见 #LVG-DRIFT 及 `AUDIT-van_gogh/claim_evidence_map.md:97-99`）。
> **双账户纪律（本卡点名）**：903 事实 `supported` / 措辞 `partial`、gate 复核 submitted 版与当前 accepted 版、`execution_status`/`knowledge_status`/`human_review` 三类状态分离——见 #LVG-DUAL-*，均**如实并存、不合并**。

---

<a id="db-source-line-12"></a>
## A. 输入与版本（本 lane 开工复核）

| # | claim_id | 论断（短） | kind/status | 证据定位（source : locator） | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 1 | LVG-INPUT-DOSSIER | dossier sha = ledger `aa170a18…4cd14` | fact/supported | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） × [van_gogh.md](../../dossiers/van_gogh.md) 全文件 sha × `RESULT.md §2` 实跑 | `[史料]`（字节实测） | 开工 sha256sum 全等 |
| 2 | LVG-INPUT-CORPUS | corpus sha = ledger `24f027d8…6acd1`（36 quotes） | fact/supported | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） × [van_gogh.md](../../dossiers/_corpus/van_gogh.md) 全文件 sha × `RESULT.md §2`；`grep -c '^### '`=36 | `[史料]` | 全等；36 条沿用 AUDIT 计数 |
| 3 | LVG-INPUT-CARD | card sha = ledger `bf0e0bb6…5ebfcc` | fact/supported | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） × [van_gogh.md](../../modules/van_gogh.md) 全文件 sha × `RESULT.md §2` | `[史料]` | 全等 |
| 4 | LVG-INPUT-CONFLICTS | conflicts.md sha = `314a24da…aabbef` | fact/supported | [conflicts.md](../../../../cross/conflicts.md) 全文件 sha × `RESULT.md §2` × AUDIT `receipt.json:31` | `[史料]` | 全等 |
| 5 | LVG-INPUT-AUDIT-MAP | 上游 `AUDIT-van_gogh/claim_evidence_map.md` sha = `cac08be3…c322f` | fact/supported | 内部证据 867e4fa59031e19f（未公开；来源记录由维护者保留） 全文件 sha × `RESULT.md §2` × AUDIT `receipt.json:100-102` artifacts 登记值 | `[史料]`（字节实测） | RECEIPT input_hashes 第 5 项 |
| 6 | LVG-AUDIT-ACCEPTED | 上游 AUDIT-van_gogh 已 ACCEPTED | fact/supported | 内部证据 ffc9118a323bebb3（未公开；来源记录由维护者保留） verdict=accepted、`:39` reviewer、`:40` independent=true；`receipt.json:6` status=accepted、`:678` verdict=accepted | `[史料]`（产物） | 本 lane 不重新审计，只复用结论 |

<a id="db-source-line-23"></a>
## B. 前置知识（learning_path.md §1）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 7 | LVG-K1-STYLE | 风格 = 厚涂笔触方向场 + 互补色并置机制 + 一次完成/临摹即翻译工作法；不是「黄色向日葵/星空」符号 | observation/supported | `modules/van_gogh.md:7-13`（视觉指纹 5 条）；`dossiers/van_gogh.md:31-42`(§1)/`:48-51`(§2-1/-2/-4)/`:199`(§8.1 中文说明第 2 条「至少给一个互补对与一个定向笔触场」) | `[归纳]`（浓缩/映射）/ `[自述]` 支撑 | 非作者原话 |
| 8 | LVG-K2-DIR-FIELD | 厚涂笔触方向场三层：6–24px 单元 + 三区方向场（天空±30°/麦田±15°/柏树75–90°）+ ≥95% 覆盖/无>12px 平滑区 | fact/supported | `dossiers/van_gogh.md:204`(§8.2-1 实测)/`:206`(§8.2-3 实测) × `modules/van_gogh.md:46,48` 逐字一致 × `dossiers/van_gogh.md:176-186`(§8.1) × `conflicts.md:114` 尾标 `[归纳]` | `[归纳]` | 数值非史料/非像素实测；**本卡点名机制一** |
| 9 | LVG-K3-COMPL | 互补色机制三层：簇≤8 且 ≥2 对互补簇同帧 + P3 强档近 1:1 + 靠笔触并置振动（`no smooth blending`） | fact/supported | `dossiers/van_gogh.md:205`(§8.2-2 实测)/`:85-88`(§4 P3)/`:49`(§2-2)/`:115-119`(§5 R3/R6)/`:184,191`(§8.1) × `modules/van_gogh.md:47,66-69,10` | `[归纳]`（阈值）+ `[自述]`（情感语法） | 二者分列，不互相翻译；**本卡点名机制二** |
| 10 | LVG-K4-PARAMS | §4 六参数 P1–P6，主线相关 P1 默认75%/P3 70%/P6 70% | fact/supported | `dossiers/van_gogh.md:73-104`(§4) × `modules/van_gogh.md:54-84` | `[归纳]` | 各参数标 `[归纳]` |
| 11 | LVG-K5-CONFLICTS | C-05/C-09/C-12 为组合前必读；处置 N1/N3/N4/N8/N9 | fact/supported | `conflicts.md:36,40,43`(总表)/`:109-121,164-174,203-215`(详节)/`:305-333`(N) × `modules/van_gogh.md:86-92` 自列 × AUDIT `claim_evidence_map.md:91-101` 判 cross-links accurate | `[归纳]`（冲突判定） | AUDIT 记录不 author fixes |
| 12 | LVG-K6-SELF | 作者自述层（任意用色/互补婚配/无固定笔法/一次完成/临摹翻译/日本平涂）与 `[归纳]` 严格分开 | fact/supported | `dossiers/van_gogh.md:109-136`(§5 R1–R9)/`:63-69`(§3) × `_corpus/van_gogh.md:11-30`(条目1–4)/`:4`(类型分级)/`:6`(规范化声明) | `[自述]`/`[self-written]` | 英文译句非亲笔（let569 例外）；§5 R1 `:111` 注明流行转述是意译改写，不升级 |
| 13 | LVG-K7-DUAL | dual-account：903 双状态、gate 两阶段、三类状态分离 | fact/supported | `dossiers/van_gogh.md:252`(§10)/`:390`(§11.3) × AUDIT `RESULT.md:20-21`/`receipt.json:275-327` × `05-RELEASE-ACCEPTANCE.md:34-38` | `[史料]`（产物/spec）/ `[归纳]`（口径） | 详见 #LVG-DUAL-* |

<a id="db-source-line-35"></a>
## C. 重点作品及来源（learning_path.md §2）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 14 | LVG-WORKS-12 | §12 共 10 件/组临摹学习清单，本卡引用现有记录不新增作品 | fact/supported | `dossiers/van_gogh.md:395`(§12 抬头)/`:399-447`(10 件) × AUDIT `RESULT.md §5`（§12「PD」简写登记） | `[史料]/[研究]`（作品信息）/ `[归纳]`（练习映射） | 作品与权利沿用 |
| 15 | LVG-WORKS-DIR | 星月夜/麦田与柏树/罗纳河星夜 → 方向场与漩涡练习 | observation/supported | `dossiers/van_gogh.md:429-437`(§12-7/-8)/`:424-427`(§12-6)/`:431`(「笔触方向场先于颜色」) | `[归纳]`（映射） | 练习映射归本项目 |
| 16 | LVG-WORKS-COMPL | 自画像/夜间咖啡馆/向日葵/卧室 → 互补对练习 | observation/supported | `dossiers/van_gogh.md:404-407,419-422,409-412,414-417` | `[归纳]`（映射） | 同上 |
| 17 | LVG-WORKS-RIGHTS | 3 张公开图 Met CC0；§12「PD 高清」为简写；书信译本非 PD | fact/supported | `_images/manifest.md` × AUDIT `rights_review.md`/`claim_evidence_map.md:86-89`/`RESULT.md §3` × `dossiers/van_gogh.md:397` | `[史料]`（权利账） | 不重访外部 URL；`receipt.json unresolved[0]` 登记标签订正 |

<a id="db-source-line-44"></a>
## D. 机制与参数（learning_path.md §3 / mechanism_notes.md §1-§3）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 18 | LVG-M1-DIRFIELD | M1 厚涂笔触方向场：三区方向场 + ≥95% 覆盖 + 自查口径 | fact/supported | `dossiers/van_gogh.md:204,206`(实测) × `modules/van_gogh.md:46,48` × `conflicts.md:114`(C-05 侧) × `dossiers/van_gogh.md:200`(生成后自查「笔触方向是否分区」) | `[归纳]` | 点名机制一；自查=方向直方图+边缘密度+连通域 |
| 19 | LVG-M2-COMPL | M2 互补色机制：≥2 对互补簇、P3 近 1:1、并置非调和 | fact/supported | `dossiers/van_gogh.md:205,85-88,184,191,200` × `modules/van_gogh.md:47,66-69` × `conflicts.md:209`(C-12 侧) × `dossiers/van_gogh.md:118-119`(§5 R6 自述) | `[归纳]`+`[自述]` 分列 | 点名机制二 |
| 20 | LVG-M3-MOTION | M3 漩涡/星体场：角速度 2–6°/s、闪烁 0.8–1.5 s（**实测 L207/L208**） | fact/supported | `dossiers/van_gogh.md:207,208`(实测) × `modules/van_gogh.md:49,50` × `conflicts.md:168,170,329-330`(C-09/N8) | `[归纳]` | 与 M1 方向场**不同轴**（空间 vs 时间） |
| 21 | LVG-82-ALL-7 | §8.2 共 7 条逐帧可查规则（实测 L204–L210） | fact/supported | `dossiers/van_gogh.md:202-210` × `modules/van_gogh.md:44-52` | `[归纳]` | 逐条自带「自查」 |
| 22 | LVG-4-ALL-6 | §4 共 6 个控制参数各三档（默认 75/60/70/50/40/70） | fact/supported | `dossiers/van_gogh.md:73-104` × `modules/van_gogh.md:54-84` | `[归纳]` | 默认档非史料常数 |
| 23 | LVG-81B | 卡 §8.1b 存在（11/76 非 65-gap），是 E1_t1b 诊断非 E4 pass | fact/supported | `modules/van_gogh.md:40-42` × AUDIT `claim_evidence_map.md:39,105` | `[归纳]`/E1_t1b | 不升级为 validated |

<a id="db-source-line-55"></a>
## E. 冲突行（learning_path.md §6 / mechanism_notes.md §4；指派 C-05/C-09/C-12）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 24 | LVG-C05 | C-05 存在且含 van_gogh；「≥95% 覆盖/平滑渐变」引文逐字回源；阈值标 `[归纳]` | fact/supported | `conflicts.md:36,109-121,114,118-121,305-312` × `dossiers/van_gogh.md:206`(实测 L206)/`:210`(L210) × `modules/van_gogh.md:48,52,90` × AUDIT `claim_evidence_map.md:97` | `[归纳]` | 解法 N1+N3；AUDIT 判 cross-link accurate |
| 25 | LVG-C09 | C-09 存在（全画面场 2–6°/s vs 单点事件）；N8 运动区域数 | fact/supported | `conflicts.md:40,164-174,168,170,329-330` × `dossiers/van_gogh.md:207,208`(实测 L207/L208) × `modules/van_gogh.md:49,50,91` × AUDIT `claim_evidence_map.md:98` | `[归纳]` | **旧行号 L205/L206 漂移见 #LVG-DRIFT** |
| 26 | LVG-C12 | C-12 存在（互补对近 1:1 vs 北斋蓝≥40%/卡拉瓦乔土色）；降档 ≥1:3 写进卡 | fact/supported | `conflicts.md:43,203-215,209,211-215` × `dossiers/van_gogh.md:205`(实测 L205)/`:88`(P3) × `modules/van_gogh.md:47,66-69,92` × AUDIT `claim_evidence_map.md:99` | `[归纳]` | 旧行号 L203 漂移 |
| 27 | LVG-N-RULES | N1/N3/N4/N8/N9 组合规则可回源；N9 禁双标准 | fact/supported | `conflicts.md:305-306,311-312,314-315,329-330,332-333` × `CONFLICT-04/RESULT.md:69`(「两套数字」规范层) | `[归纳]` | 「记录两套数字 ≠ 裁决」 |
| 28 | LVG-DRIFT | **L207/208 drift**：conflicts.md:168 引 L205/L206，实测 L207/L208；同类 C-05 L204/L208→L206/L210、C-12 L203→L205，均 +2 | observation/conflict（登记） | `conflicts.md:114,168,209` × `dossiers/van_gogh.md:204-210`(本 lane `nl -ba` 实跑，`RESULT.md §2`) × `modules/van_gogh.md:46-52` × AUDIT `claim_evidence_map.md:97-99`(实测行号)/`review-evidence.md:42`(drift class) | `[研究]`（文本比对） | 规则编号/引号文本正确，仅行号偏移；与 A-34 页码 ±1 不同对象；**未改仓库** |
| 29 | LVG-GAP-A | AUDIT map 级 `raw/letters/about_1.txt`/`letters_index.txt` 不存在；receipt 级走 `raw/about_2009_quote.txt` | observation/supported | AUDIT `review-evidence.md:59` × 本 lane `ls raw/letters/` 实跑 × AUDIT `receipt.json:145-147`(about_2009_quote 存在) | `[研究]`（产物核对） | 本卡 903 引用只走 receipt/RESULT 级 locator |

<a id="db-source-line-66"></a>
## F. dual-account 双账户状态（本卡点名携带）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 30 | LVG-DUAL-903 | 903 事实 `supported` / 「收口」措辞 `partial` 两账户并存；§10 L252 `[UNVERIFIED]` 与 §11.3 note 2 同时在档 | fact/supported | AUDIT `receipt.json:275-311`(AVG-903-CLOSURE supported)/`:314-327`(TEXTUAL-GAP partial) × `dossiers/van_gogh.md:252,390` × AUDIT `RESULT.md:20-21`/`claim_evidence_map.md:68-76` | `[史料]`（产物/档案） | **不合并、不伪造单一裁决** |
| 31 | LVG-DUAL-GATE | gate 复核 `receipt.json@0bf134e2…`(submitted)→verdict=accepted；当前 `receipt.json@181ec23a…` 升 accepted = 同任务两阶段 | fact/supported | AUDIT `review-gate-receipt.json:15`(input hash 0bf134e2…)/`:50`(verdict accepted) × 本 lane `sha256sum receipt.json`=`181ec23a…` × `receipt.json:6` status=accepted × `review-gate-runner-receipt.json`(verify ok:true on submitted) | `[史料]`（字节实测） | 不是矛盾；两阶段状态 |
| 32 | LVG-DUAL-3STATUS | 三类状态分别保存；本 lane submitted/review=null/human_review=not_applicable | fact/supported | `05-RELEASE-ACCEPTANCE.md:34-38` × 本 `receipt.json` × AUDIT `RESULT.md §Limitations` | `[史料]`(spec)/`[归纳]`(执行) | `submitted ≠ accepted`；不填模拟人评 |
| 33 | LVG-DUAL-RIGHTS | §12「PD」是 CC0 简写、书信译本非 PD —— 两个权利对象不混称 | fact/supported | `dossiers/van_gogh.md:397` × AUDIT `rights_review.md`/`claim_evidence_map.md:86-89`/`receipt.json unresolved[0]` | `[史料]`（权利账） | 标签订正属后继 STYLE lane |

<a id="db-source-line-75"></a>
## G. How-to-Think 等级分离（how-to-think.md）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 34 | LVG-HT-SPLIT | 自述层与研究者推断严格分栏；每步带证据等级；`[推测]` 计数 0 | observation/supported | `how-to-think.md §0/§1/§5` × `00-GOAL.md:9` × `dossiers/van_gogh.md:256`（未使用 `[推测]`）× AUDIT `RESULT.md §5` | `[归纳]`（本卡纪律） | 不从作品外观反推心理 |
| 35 | LVG-HT-SELF-QUOTES | S1/S2/S4/S6 的「为什么」上半来自作者言语记录（信 663/673/596/535/805） | fact/supported | `dossiers/van_gogh.md:109-136`(§5)/`:63-69`(§3) × `_corpus/van_gogh.md:11-30` × `dossiers/van_gogh.md:48-57`(§2) | `[自述]`/`[self-written]` | corpus `:4` 类型分级、`:6` 规范化风险不静默消除 |
| 36 | LVG-HT-INFER-ONLY | S3/S5/S7 为纯 `[归纳]` 步（数值判据无作者自述支撑） | fact/supported | `how-to-think.md §2 S3/S5/S7` × `dossiers/van_gogh.md:204-210` × `conflicts.md:114,168,209` | `[归纳]` | 不写「梵高要求 6–24px/1:1/2–6°/s」 |
| 37 | LVG-HT-NO-PSYCH | 不含「从画面推作者心理」的句子（尤其《星月夜》/生平） | observation/supported | `how-to-think.md §4` 反心理推断清单 × `00-GOAL.md:9` × `dossiers/van_gogh.md:250`(信777 所指作品未定 [UNVERIFIED]) × AUDIT `claim_evidence_map.md:80` | `[归纳]` | 红线 |

<a id="db-source-line-84"></a>
## H. 练习、结果、失败、边界（learning_path.md §4-§8 / mechanism_notes.md §5-§8）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 38 | LVG-LADDER-3 | 三条阶梯：impasto direction-field studies → complementary-pair juxtaposition → swirl/star field + combination discipline | design_candidate/supported（作为「建议练习」交付） | `learning_path.md §4` × `dossiers/van_gogh.md:204-210,429-437,404-422,424-427` × `conflicts.md:119,211-215,305-333` | `[归纳]`（本项目设计） | **建议练习**，学习收益未经人评 |
| 39 | LVG-A30-SHAPE | 学习路径含 A-30 §8.1 八节：前置知识/重点作品及来源/要观察的机制/具体练习/可观察结果/常见失败/下一步/使用边界 | fact/supported | `01-AUDIT.md:269-273`(§8.1) × `learning_path.md §1-§8` 八节标题 × `ops/GOALS.md`(A-30) | `[史料]`(spec)/`[归纳]`(映射) | 练习效果须标建议练习（`:273`） |
| 40 | LVG-PRACTICE-UNVERIFIED | 练习效果未由人完成/评价，标「建议练习」不写「已证实学习收益」 | fact/supported | `01-AUDIT.md:273` × `learning_path.md B1/§4 抬头` × 本 `receipt.json` human_review=not_applicable | `[史料]`(spec)/`[归纳]`(执行) | 硬边界 |
| 41 | LVG-OBSERVABLE | 可观察结果是练习产物自查口径，非原作像素实测 | observation/supported | `learning_path.md §5` × `dossiers/van_gogh.md:200,204-210`(§8.2 自查法) × AUDIT `RESULT.md §5`(image_seen 未声称) | `[归纳]` | 不声称原作被证实如此 |
| 42 | LVG-FAILURES | 9 类常见失败（F1 抹平/C-05、F2 方向不分、F3 互补不足、F4 C-12、F5 C-09、F6 双标准、F7 等级混淆、F8 权利标签、F9 符号化） | observation/supported | `learning_path.md §6` × `conflicts.md:114,119,168,209,211-215,305-333` × `dossiers/van_gogh.md:199-210,397` × AUDIT `rights_review.md` | `[归纳]` | 规则层判定，非实验 |
| 43 | LVG-NO-REPO-WRITE | 本 lane 仅写 内部证据 cb00d006baf9ff41（未公开；来源记录由维护者保留），仓库只读、无 git、无子代理、无凭据 | observation/supported | 本 `receipt.json` `allowed_write_paths`=内部证据 cb00d006baf9ff41（未公开；来源记录由维护者保留）、`spawns_allowed=false` × AUDIT `claim_evidence_map.md:5`（同口径） | `[史料]`（产物声明） | 只读约束遵守 |
| 44 | LVG-EXTRACT-228 | card §8.1/§8.2/§4 与 dossier 逐字一致（`_extract.py --check` 全库 228/228，van_gogh 占 3） | fact/supported | AUDIT `RESULT.md §2`/`§4` × `claim_evidence_map.md:38` × `raw/extract_check.out`（`[van_gogh] §8.1 ok · §8.2 ok · §4 ok`）；本 lane **未重跑**，沿用 ACCEPTED 审计结论 | `[史料]`（上游实跑） | A-33「33/33」为 wave14 子集口径，不混用 |
| 45 | LVG-16-QUOTES | 16 条 A-33 引文「wording 级 supported、literal byte-exact overstated」（13 word-exact + 3 已声明规范化）；20 条旧语料状态不升级 | fact/supported | AUDIT `RESULT.md §2`/`claim_evidence_map.md:43-66` × `_corpus/van_gogh.md:6,7,288` × `receipt.json:329-460`(AVG-16-QUOTES) | `[史料]`（产物结论）/ `[归纳]` | 本卡不自称逐字节核验、不升级旧语料 |

---

<a id="db-source-line-99"></a>
## 支持状态汇总（分母 = 45 条论断）

- `supported` = **44**；`conflict`（登记的行号漂移 `#28`，非「未验证」）= **1**；`partial` = 0；`unverified` = 0；`not_applicable` = 0。
  - 注：903 的 `partial` 是**上游 AUDIT 内的账户状态**（#30 如实携带），本表该条论断本身 `supported`（「两账户并存」这一事实成立）；本 lane 不自造 `partial`。
- `[推测]` 级结论 = **0**；无「从作品外观反推作者心理」的句子（#34/#37）。
- 所有 §8.2/§4/conflicts 数值均标 `[归纳]`，未冒充 `[自述]`/`[史料]`/像素实测（#8/#9/#18/#19/#36）。
- 练习 = **建议练习**，`human_review=not_applicable`，不写「已证实学习收益」（#38/#40）。
- **两条点名强调**：M1 方向场（#8/#18/#38 阶梯一）、M2 互补色（#9/#19/#38 阶梯二）。
- **L207/208 drift**（#28）：+2 行号偏移已登记，全部 locator 用实测行号；**dual-account**（#30/#31/#32/#33）如实并存、不合并。
- 外部 URL 本轮**未重访**（`access_status=unknown`）；3 张公开图**未目检**（`image_seen=0`）；#14–#17 作品/权利论断支持范围 =「本机文件内引用与记录仍存在且连贯」，不声称外部页面当前可访问。
- 本 lane `status=submitted`（非 accepted），`review=null`，独立审阅由 review gate 承担（见 `receipt.json`）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
