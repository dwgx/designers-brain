<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-klimt；原正文 SHA-256 `d6dbb6d35d1761dc1c268c86fae1ab553fcdaee10c50b610d50ccb0960fb64a8`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-klimt — claim → evidence map（每条论断带 file:line locator）

> 任务 `LEARN-klimt`（A-30）· 依赖 `AUDIT-klimt`（**ACCEPTED**，内部证据 26dfbc22d6fa3609（未公开；来源记录由维护者保留） verdict=accepted, blocking_defects=0；`receipt.json` status=accepted）。
> **口径（复用 ACCEPTED 审计的 locator 纪律，不重新审计）**：每条论断给「来源文件 + 具体行/节定位 + 证据等级 + 支持状态」。内部证据 4874f193014ae79c（未公开；来源记录由维护者保留） 为只读回源（声明基线 `f008952365a77e140cbda3f3959d43ef000f9a22`，本 lane 开工已 sha256sum 复核三件冻结输入，见 `RESULT.md §2`）；内部证据 2f213f0391f811ec（未公开；来源记录由维护者保留） 为上游 ACCEPTED 产物；内部证据 0b1d7e9366d3226c（未公开；来源记录由维护者保留） 为本 lane 生成。
> 等级沿用仓库口径（`dossiers/klimt.md:4`）：`[自述]`/`[self-written]`/`[reported speech]`/`[contemporary record]` = 作者/同时代人言语记录；`[归纳]` = 项目操作规则/研究者归纳；`[研究]` = 二手研究/文本比对；`[史料]` = 史实/权利记录；`[推测]` 本 lane **不使用**（计数 0，dossier `:304`）。
> 版本列：仓库文件 = `f0089523…`；staging artifact = 本轮/上游生成（给 sha256）。`read_scope` 与 `access_status` 分开：外部 URL 本轮未重访 = `unknown`，本机文件 = `available`，6 张公开图未目检 = 无 `image_seen`。
> **行号纪律**：AUDIT `locator_drift.md` 登记 conflicts.md:249 引 `matisse.md` L82/L187 实测为 L88/L193（+6）、klimt.md:74/:289「现行版 L83/L188-189」过期；本表一律用**实测行号 + 子串**定位。

---

<a id="db-source-line-11"></a>
## A. 输入与版本（本 lane 开工复核）

| # | claim_id | 论断（短） | kind/status | 证据定位（source : locator） | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 1 | LK-INPUT-CARD | card [klimt.md](../../modules/klimt.md) sha = `e9abb827…11ed1a` | fact/supported | `AUDIT-klimt/coverage-manifest.json:7` × 内部证据 1bb6907745f310a3（未公开；来源记录由维护者保留） × 本 lane 开工 sha256sum（`RESULT.md §2`） | `[史料]`（字节实测） | ledger_match=true |
| 2 | LK-INPUT-DOSSIER | dossier [klimt.md](../../dossiers/klimt.md) sha = `5f023be5…2b4175` | fact/supported | `AUDIT-klimt/coverage-manifest.json:6` × `AUDIT-klimt/RESULT.md:26` × 本 lane sha256sum | `[史料]` | ledger_match=true |
| 3 | LK-INPUT-CORPUS | corpus [klimt.md](../../dossiers/_corpus/klimt.md) sha = `8ce491e9…8547a`，**11 条** | fact/supported | `AUDIT-klimt/coverage-manifest.json:8,17-19` × `quote_audit.md:4-5` × 本 lane sha256sum | `[史料]` | quote_count=11，headers `:10,18,26,35,43,50,60,68,75,82,89` |
| 4 | LK-INPUT-CONFLICTS | `conflicts.md` sha = `314a24da…bbef` | fact/supported | `AUDIT-klimt/coverage-manifest.json:10` × `RESULT.md:30` × 本 lane sha256sum | `[史料]` | 全等 |
| 5 | LK-INPUT-AUDIT-MAP | 上游 `claim_evidence_map.csv` sha = `ed37f0eb…4bae4`（62 行） | fact/supported | `AUDIT-klimt/receipt.json` artifacts 登记值 × 本 lane sha256sum × `coverage-manifest.json:21-23`（claims_total=62） | `[史料]` | RECEIPT input_hash 之一 |
| 6 | LK-INPUT-AUDIT-MANIFEST | 上游 `coverage-manifest.json` sha = `e9d9881e…9c6392` | fact/supported | `AUDIT-klimt/receipt.json` artifacts 登记值 × 本 lane sha256sum | `[史料]` | RECEIPT input_hash 之一 |
| 7 | LK-AUDIT-ACCEPTED | 上游 AUDIT-klimt 已 **ACCEPTED** | fact/supported | 内部证据 c6fdd80c8c341918（未公开；来源记录由维护者保留） verdict=accepted, `:16` blocking_defects=0；`receipt.json:6` status=accepted, review.verdict=accepted | `[史料]`（产物） | 本 lane 不重新审计，只复用结论 |
| 8 | LK-REPO-BASELINE | 仓库只读、基线 `f0089523…`、无 git 操作 | fact/supported | `AUDIT-klimt/coverage-manifest.json:4,45-46`（repo_writes=0） × 本 `receipt.json` allowed_write_paths / spawns_allowed | `[史料]`（产物声明） | 遵守 |

<a id="db-source-line-24"></a>
## B. 前置知识（learning_path.md §1）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 9 | LK-K1-POSITIONING | 能力定位 = 装饰性平面 + 金箔工艺 + 图案化；图案当独立图层系统；写实面孔 × 装饰图案对撞 | observation/supported | `dossiers/klimt.md:15`（§0 一句话）、`:6`（分工抬头）；`modules/klimt.md:9-13`（浓缩 5 条） | `[归纳]`（能力标签）/ `[研究]` 支撑 | 非作者原话 |
| 10 | LK-K2-GOLD-IS-MATERIAL | 金是材质不是黄色颜料；箔块接缝/碎屑/罩染；金属区非平滑渐变金 | fact/supported | `dossiers/klimt.md:32`（§1-1 [R1][R2]）、`:47`（§2-1）、`:48`（§2-2 Jahn）、`modules/klimt.md:9` × AUDIT CSV:6（KL-1-1 supported） | `[研究]` | live Wikipedia 'gold leaf' 3 hits 佐证（AUDIT CSV:6） |
| 11 | LK-K3-PLANAR-DUAL | 平面分割（无消失点/无投射阴影）+ 双分辨率共存（面孔体积 × 图案平涂） | fact/supported | `dossiers/klimt.md:33`（§1-2）、`:35`（§1-4）、`:41`（§1-10）、`modules/klimt.md:10,12` × AUDIT CSV:7,9 | `[研究]`/`[归纳]` | KL-1-2 supported；KL-1-4 partial |
| 12 | LK-K4-82-SEVEN | §8.2 共 7 条逐帧可查规则（金属/图案密度/材质对比/落差/平面化/词汇尺度/构图运动） | fact/supported | `dossiers/klimt.md:235-243`（§8.2-1–7）× `modules/klimt.md:43-51`（原样）× `:245`（明标 `[归纳]`、未像素实测） | `[归纳]` | 全部阈值性质 |
| 13 | LK-K5-4-SIX | §4 共 6 控制参数各三档（P1–P6），默认 60/55/60/50/60/40；用法 P1/P3/P4 定 vs 马蒂斯 | fact/supported | `dossiers/klimt.md:81-114`（§4）、`:114`（用法）、`modules/klimt.md:55-88` × AUDIT CSV:39-44（六行 **unverified**） | `[归纳]` | **不升级为 supported**；AUDIT 判 unverified |
| 14 | LK-K6-DIVISION | 分工（写死 2026-10-15）：克里姆特=装饰工艺/金箔/图案密度带材质/象征；马蒂斯=色彩设计/剪纸/大色块平衡；分界判据 >5% 材质差 | fact/supported | `dossiers/klimt.md:6`（抬头）、`:71-77`（§3 分工块）× AUDIT CSV:34-38（KL-3-D1–D5） | `[归纳]`（项目对齐口径） | 非史实断言；「有条件通过」立档 `:77` |
| 15 | LK-K7-C15-N6 | C-15：金属/金箔/高光材质层单列不计色数；N6 ≤5% 仅适用他模块点缀；本模块为主按 P1 面积档 | fact/supported | `conflicts.md:46`（总表）、`:244-256`（块）、`:323-324`（N6）× `dossiers/klimt.md:115`、`:299`（§10-5）× `modules/klimt.md:89,95-96` × AUDIT CSV:46,63 | `[归纳]`（冲突判定）/ `[史料]`（Lane B 反约束） | C-15 回填 TODO `:256`/`:421` |
| 16 | LK-K8-SELF | 作者自述层：不解释（1913）、自我隐去/不画自画像、工作纪律、Ravenna 明信片 | fact/supported | `dossiers/klimt.md:64,65,68,69`（§3）、`:121-129`（§5）× `_corpus/klimt.md:10,18,26,35`（Q1–Q4）× AUDIT CSV:28-29,32,50 | `[自述]`/`[自述转述]`/`[self-written]` | Q1 德文原题未定位、Q4 馆方英译；不升级 |
| 17 | LK-K9-D25 | near-miss D25 语料缺口：corpus v0.1=**11 条**，v2 ≥15 未决，无 v2 corpus | fact/supported | `AUDIT-klimt/coverage-manifest.json:17-20`（quote_count/kb_note_D25）× `quote_audit.md:5-9,26-37` × `_corpus/klimt.md:96-103` × `dossiers/klimt.md:296-303` | `[史料]`（计数）/ `[归纳]`（缺口登记） | review-gate `checks.d25_flagged_unresolved=true` |
| 18 | LK-K10-LOOS | 「All art is erotic」非克里姆特之言，是 Loos《Ornament and Crime》(1908)，已剔除 | fact/supported | `dossiers/klimt.md:301`（§10-7）× `_corpus/klimt.md:101` × AUDIT CSV:58（KL-LOOS-MISATTR supported）× `raw/loos_ornament.html`（sha `f2af1477…`） | `[史料]`（live fetch 已核） | review-gate `loos_exclusion_bytes_verified` |

<a id="db-source-line-39"></a>
## C. 重点作品及来源（learning_path.md §2）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 19 | LK-WORKS-5 | §0 关键作品 5 件表（吻/阿黛尔 I/朱迪斯 I/死与生/Stoclet），本文引用现有记录不新增作品 | fact/supported | `dossiers/klimt.md:16-24`（§0 表）× AUDIT CSV:5（KL-0-WORKS）× `RESULT.md §3`（6 图 6/6） | `[史料]`（作品信息）/ `[归纳]`（练习映射） | 对象页 403 经 Wayback、朱迪斯对象页未直读（`:295`） |
| 20 | LK-WORKS-LADDER1 | 阶梯一取《吻》《阿黛尔 I》对照《朱迪斯 I》→ 金箔装饰层 / P1 档 | observation/supported | `dossiers/klimt.md:20,21,22`、`:47-51`（§2-1–5）、`:86`（P1 强档） | `[归纳]`（映射） | 练习映射归本项目 |
| 21 | LK-WORKS-LADDER2 | 阶梯二取《吻》《死与生》Stoclet → 平面分割 + 双分辨率 | observation/supported | `dossiers/klimt.md:20,23,24`、`:33-35,40,41`、`:62-63`、`:191`（§7-3）、`:321`（§11 Stoclet）、`:286`（gold→grey，AUDIT CSV:60 KL-DEATH-GREY supported） | `[归纳]`（映射） | gold→grey 有 live Wikipedia 佐证 |
| 22 | LK-WORKS-LADDER3 | 阶梯三取 near-miss #9/#10 三选/灰区 → 分工边界与组合自律 | observation/supported | `dossiers/klimt.md:71-77,92,238` × `conflicts.md:355,356` × `modules/klimt.md:66,95-96` | `[归纳]`（映射） | 与马蒂斯 A-07 对照，不新增作品 |
| 23 | LK-WORKS-RIGHTS | 6 张公开图权利/署名/许可有逐字记录（6/6 PD/开放许可），本 lane 未目检 | fact/supported | `_images/manifest.md:53-58` + AUDIT `rights_review.md` × `coverage-manifest.json:26-28`（images_public=6） × review-gate `rights_rows_verified_verbatim=6/6` | `[史料]`（权利账） | 不重访外部 URL、image_seen=0 |
| 24 | LK-WORKS-EXTERNAL | 外部 URL（R1–R23）本轮未重访；作品/权利沿用现有记录 | fact/supported | `dossiers/klimt.md:253-279`（§9 表）× AUDIT `coverage-manifest.json:32-39`（external_fetches=5） × `RESULT.md §4`（honest negatives） | `[史料]`（产物声明） | access_status=unknown |


<a id="db-source-line-51"></a>
## D. 机制与参数（learning_path.md §3 / mechanism_notes.md §1-§3）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 25 | LK-M1-METAL-LEAF | M1 金箔装饰层：§8.2-1 面积 ≥30% / P95−P5 ≥40 / 箔块边界 ≥3 处 / 平滑渐变金属 ≤5%；P1 三档 | fact/supported | `dossiers/klimt.md:237`（§8.2-1）、`:83-86`（P1）、`:32`（§1-1）、`:233`（退化处理）× `modules/klimt.md:45,57` × AUDIT `counterexample.md:10-23`（CE-1） | `[归纳]` | P1 在 AUDIT = unverified |
| 26 | LK-M2-PLANAR | M2 平面分割 + 双分辨率：消失点=0 / 投射阴影 ≤1% / 局部方差比 ≥2.0 / 同向梯度段 ≥3 / 近方形包围盒 ≥60% | fact/supported | `dossiers/klimt.md:240,241,243`（§8.2-4/-5/-7）、`:104-107`（P5）、`:33,35`（§1-2/-4）× `modules/klimt.md:48,49,51,78` | `[归纳]` | 数值非像素实测 |
| 27 | LK-M3-EXCLUSIVE | M3 带材质图案 + 分工专属判据：$A_p$ 弱≤5/中15–35/强≥50%、明度 ≥10% 默认 / ≤5% 越界 / 5–10% 灰区不得单独区分 | fact/supported | `dossiers/klimt.md:238`（§8.2-2）、`:88,92`（P2 边界注）、`:99-102`（P4）、`:75`（§3 判据）× `modules/klimt.md:46,62-66,73-76` × `conflicts.md:355,356` | `[归纳]` | CE-2 指出 §3「>5%」与 §8.2-2「≥10%」不一致 |
| 28 | LK-M4-VOCAB | M4 图案词汇/材质对比/象征负载：材质 ≥2 类分离度 ≥1.5、允许单元集、短边 [2%,15%]、重复 ≥3、P6 三档 | fact/supported | `dossiers/klimt.md:239,242,243`（§8.2-3/-6/-7）、`:94`（P3）、`:109`（P6）、`:34`（§1-3）、`:41`（§1-10）× `modules/klimt.md:47,50,51,68,83` | `[归纳]` | §1-9 角/圆身份编码为 `[研究]` + §7-1 批评读法，不写成心理 |
| 29 | LK-M5-CONFLICTS | M5 边界与冲突横切：C-15/N6/near-miss #9/#10/N1/N3 接入练习 | fact/supported | `conflicts.md:244-256,323-324,355,356,375,421` × `dossiers/klimt.md:115,231,232` × `modules/klimt.md:91-96` × AUDIT CSV:46,63 | `[归纳]` | 规则层判定，非实验 |
| 30 | LK-82-ALL-7 | §8.2 共 7 条规则（含 -5 平面化 / -6 词汇 / -7 运动） | fact/supported | `dossiers/klimt.md:237-243` × `modules/klimt.md:45-51` | `[归纳]` | -7 含动画判据，静态练习不套用 |
| 31 | LK-4-ALL-6 | §4 共 6 参数各三档；六行在 AUDIT 均 `unverified` | fact/supported | `dossiers/klimt.md:83-113` × `modules/klimt.md:57-86` × AUDIT CSV:39-44（`unverified`） × `coverage-manifest.json:22`（per_status unverified=6） | `[归纳]` | **保持 unverified** |

<a id="db-source-line-63"></a>
## E. 冲突行（learning_path.md §6 / mechanism_notes.md §4）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 32 | LK-C15 | C-15 总表/块存在；Lane B 色数上限 × 金属高光材质冲突；解法=材质层单列；回填 TODO | fact/supported | `conflicts.md:46,244-256,249,251,253-256` × `dossiers/klimt.md:115,299` × `modules/klimt.md:89,95-96` × AUDIT CSV:46（KL-4-N2）、:63（KL-C15 supported） | `[归纳]`/`[史料]` | 分层正确（AUDIT CSV:63） |
| 33 | LK-N6 | N6「色数只约束平涂色块层；金属层单列、面积 ≤5%、须卡内声明」；本模块为主时按 P1 | fact/supported | `conflicts.md:323-324` × `dossiers/klimt.md:115` × `modules/klimt.md:89` | `[归纳]` | ≤5% 仅他模块点缀 |
| 34 | LK-NM9 | near-miss #9 三选：金属＋人物→克里姆特 / 金水材质→光琳 / 平涂纯色→马蒂斯，金来源不混用 | fact/supported | `conflicts.md:355` × AUDIT `coverage-manifest.json:30`（conflicts_rows_detail）、`locator_drift.md:16-17` | `[归纳]` | 2026-10-16 补 |
| 35 | LK-NM10 | near-miss #10：≤5% 平涂金彩 / ≥10% 金属材质 / 5–10% 灰区须显式取值 | fact/supported | `conflicts.md:356` × `dossiers/klimt.md:238,99-102` × AUDIT `counterexample.md:25-33`（CE-2） | `[归纳]` | 与 §3 分工判据 `:75` 阈值不一致 |
| 36 | LK-SELFREVIEW-C5 | self-review C-5 确认 C-15 是「计数口径」问题，非能力缺失 | fact/supported | `conflicts.md:375` × AUDIT CSV:63 | `[归纳]` | CONFIRMED 作为口径问题，未升级实验 |
| 37 | LK-BACKFILL-TODO | C-15 实测阈值回填仍 TODO（接口 = §4 P1 + §8.2-1，分母 = 金属层面积占比） | fact/supported | `conflicts.md:256,421` × `dossiers/klimt.md:299`（§10-5） | `[归纳]` | A-12 待补，不冒充完成 |
| 38 | LK-DRIFT | conflicts.md:249 引 matisse.md L82/L187 实测 L88/L193（+6）；「8 对」vs 11 行；登记不修复 | observation/conflict（登记） | `conflicts.md:249,80,101,365,385-386` × `dossiers/klimt.md:74,289` × AUDIT `locator_drift.md:5-25`、`coverage-manifest.json:31` | `[研究]`（文本比对） | 只读 lane 不改仓库；与 A-34 页码 ±1 不同对象 |
| 39 | LK-CE-INFERENCE | CE-1（统计达标但机制缺席）/ CE-2（5–10% 灰区阈值不一致）为 `[inference]` 纸面反例，无帧无测量无盲评 | fact/supported | AUDIT `counterexample.md:1-3,10-36,38-41` × `coverage-manifest.json:41-42`（counterexample_attempts=2, inference_only=true） | `[归纳]`（登记） | 不作实测结论 |

<a id="db-source-line-76"></a>
## F. How-to-Think 等级分离（how-to-think.md）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 40 | LK-HT-SPLIT | 自述层与研究者推断严格分栏；D1–D8 每步带等级；`[推测]` 计数 0；不从画面推心理 | observation/supported | `how-to-think.md §0/§1/§4/§5` × `00-GOAL.md:9` × `dossiers/klimt.md:304`（未使用 `[推测]`）× AUDIT `coverage-manifest.json:24`（claims_by_grade 无 `[推测]`） | `[归纳]`（本卡纪律） | 红线 |
| 41 | LK-HT-D7-SELF | D7 是唯一以 `[自述]`/`[自述转述]` 为决策来源的一步，只取带类型标注言语记录 | fact/supported | `how-to-think.md §2 D7` × `_corpus/klimt.md:26-31`（Q3 `[reported speech]`）、`:10-16`（Q1 `[self-written]` 转引）× `dossiers/klimt.md:64,65,68`、`:121-123` | `[自述]`/`[自述转述]` | Q1 德文原题未定位（`:99`、dossier `:296`）、Q3 来源未重访；风险不消除 |
| 42 | LK-HT-NO-CONTEMP-PSYCH | Q8 Tietze 1919 性格记录（`[contemporary record]`）未进入任何决策步「为什么」；不写「因性格羞怯所以不解释」 | observation/supported | `how-to-think.md §0/§2 D7/§4` × `_corpus/klimt.md:68-73`（Q8）× `00-GOAL.md:9` | `[归纳]` | 反心理推断清单 |
| 43 | LK-HT-INFER-ONLY | D4/D8 为纯 `[归纳]` 步（项目规则，无作者自述支撑）；D1/D2/D3/D5/D6 含 `[研究]` | fact/supported | `how-to-think.md §1/§2 D4,D8/§5` × `dossiers/klimt.md:15,63,71-77,92,114,238` × `conflicts.md:355,356` | `[归纳]` | 不写「克里姆特要求 ≥10%」 |
| 44 | LK-HT-NO-INVENTED | §3-2「装饰即内容」是 `[归纳]`、§1-9 角/圆编码是 `[研究]` + 批评读法，均未升格为作者意图 | fact/supported | `how-to-think.md §0/§2 D4,D5` × `dossiers/klimt.md:63`（§3-2 明标 `[归纳]`）、`:40`（§1-9 [R1]）、`:189`（§7-1 Fliedl）× AUDIT CSV:27（KL-3-2 `[归纳]`）、:14（KL-1-9） | `[归纳]`/`[研究]` | 无发明心理学 |
| 45 | LK-HT-LOOS-NOT-USED | 「All art is erotic」不进入任何决策步 | observation/supported | `how-to-think.md §0/§4` × `dossiers/klimt.md:301` × `_corpus/klimt.md:101` | `[史料]` | 误挂已剔 |

<a id="db-source-line-87"></a>
## G. 练习、结果、失败、边界（learning_path.md §4-§8 / mechanism_notes.md §5-§6）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 46 | LK-LADDER-3 | 三条阶梯：metal-leaf layer studies → planar segmentation / dual-resolution → division-vs-exclusive-criterion discipline | design_candidate/supported（作为**建议练习**交付） | `learning_path.md §4` × `dossiers/klimt.md:48,50,237,83-86`（阶梯一）/`:240,241,243,104-107`（阶梯二）/`:71-77,88,92,99,114,115,231,232,238`（阶梯三） × `conflicts.md:355,356,323-324` | `[归纳]`（本项目设计） | **建议练习**，学习收益未经人评 |
| 47 | LK-A30-SHAPE | 学习路径含 A-30 §8.1 八节：前置知识/重点作品及来源/要观察的机制/具体练习/可观察结果/常见失败/下一步/使用边界 | fact/supported | `01-AUDIT.md:269-273`（§8.1）× `learning_path.md §1-§8` 八节标题 × `00-GOAL.md:9` | `[史料]`（spec）/ `[归纳]`（映射） | 练习须标建议练习（`:273`） |
| 48 | LK-PRACTICE-UNVERIFIED | 练习效果未由人完成/评价，标「建议练习」不写「已证实学习收益」 | fact/supported | `01-AUDIT.md:273` × `learning_path.md §4 抬头 / B1` × 本 `receipt.json` human_review=not_applicable | `[史料]`（spec）/ `[归纳]`（严格执行） | 硬边界 |
| 49 | LK-OBSERVABLE | 可观察结果是练习产物自查口径，非原作像素实测；§4 六参数保持 unverified | observation/supported | `learning_path.md §5` × `dossiers/klimt.md:237-243`（§8.2 自查法）× `dossiers/klimt.md:245,298` × AUDIT `RESULT.md §4` / `coverage-manifest.json:22` | `[归纳]` | 不声称原作被证实如此 |
| 50 | LK-FAILURES | 9 类常见失败（F1 渐变金 / F2 金属当第4色 / F3 平涂越界 / F4 灰区 / F5 透视阴影 / F6 等级混淆 / F7 误挂与 D25 / F8 回源 / F9 心理推断） | observation/supported | `learning_path.md §6` × `conflicts.md:244-256,323-324,355,356` × `dossiers/klimt.md:92,233,238,240,241,245,298,301,304` × AUDIT `counterexample.md` | `[归纳]` | 规则层判定，非实验 |
| 51 | LK-DIVISION-VS-CRITERION | 分工句（`:73-75`）与克里姆特-专属硬约束（§8.2-1/-2/-4 + C-15/N6 + near-miss #9/#10）分层，不互相替代 | observation/supported | `learning_path.md B3 / §4 阶梯三 / how-to-think.md §2 D8` × `dossiers/klimt.md:71-77,238` × `conflicts.md:355,356` × AUDIT `counterexample.md:25-33` | `[归纳]` | 本片指派强调点 |
| 52 | LK-GOLD-PLANAR-EMPHASIS | 强调「金箔装饰层与平面分割」贯穿三阶梯 | observation/supported | `learning_path.md 抬头 / §3 M1,M2 / §4 / §8 B` × `dossiers/klimt.md:15,32,35,48,50,237,241` × `modules/klimt.md:9,12,45,49` | `[归纳]` | 本片指派强调点 |
| 53 | LK-NO-REPO-WRITE | 本 lane 仅写 内部证据 43f01f49c1f17f05（未公开；来源记录由维护者保留），仓库只读、无 git、无子代理、无凭据 | observation/supported | 本 `receipt.json` allowed_write_paths / spawns_allowed=false × AUDIT `coverage-manifest.json:44-46`（repo_writes=0, spawns=0） | `[史料]`（产物声明） | 只读约束遵守 |
| 54 | LK-EXTRACT-228 | card §8.1/§8.2/§4 与 dossier 逐字一致（`_extract.py --check` 全库 228/228，klimt 占 3） | fact/supported | AUDIT `RESULT.md §2` / `coverage-manifest.json:16`（extractor_check） × `modules/klimt.md:3-5`；本 lane **未重跑**，沿用 ACCEPTED 审计结论 | `[史料]`（上游实跑） | 不混用 wave 子集口径 |

---

<a id="db-source-line-103"></a>
## 支持状态汇总（分母 = 54 条论断）

- `supported` = **53**；`conflict`（登记的行号/行计数漂移 `#38`，非「未验证」）= **1**；`partial` = 0；`unverified` = 0；`not_applicable` = 0。
- `[推测]` 级结论 = **0**；无「从作品外观反推作者心理」的句子（#40/#42/#45/#50）。`[contemporary record]`（Q8/Q9/Q10/Q11）未进入任何决策步「为什么」。
- 所有 §8.2/§4/conflicts 数值均标 `[归纳]`，未冒充 `[自述]`/`[史料]`/像素实测（#12/#13/#25–#31/#43/#49）；**6 个 §4 参数沿用 AUDIT 的 `unverified`，不升级为 supported**（#13/#31/#49）。
- 练习 = **建议练习**，`human_review=not_applicable`，不写「已证实学习收益」（#46/#48）。
- **D25**：corpus v0.1 = 11 条、v2 ≥15 未决（#17/#50）；Q1 德文原题未定位、Q2 档案原件 `[UNVERIFIED]`、Q4–Q8 德文原文未取得、约 400 件 Flöge 书信未公开全文（#16/#41）。「All art is erotic」属 Loos、已剔除（#18/#45）。
- **分工 vs 专属判据**分层（#51）、**金箔装饰层与平面分割**主线（#52）均落到 locator；CE-1/CE-2 为 `[inference]` 纸面反例（#39），不作实测结论。
- 外部 URL 本轮**未重访**（`access_status=unknown`，#24）；6 张公开图**未目检**（`image_seen=0`，#23）；#19–#24 作品/权利论断支持范围 =「本机文件内引用与记录仍存在且连贯」，不声称外部页面当前可访问。
- 本 lane `status=submitted`（非 accepted），`review=null`，独立审阅由 review gate 承担（见 `receipt.json`）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
