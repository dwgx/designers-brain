<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-monet；原正文 SHA-256 `e6e4685ea45ae63e05ddcd54590f1c10a2678cbf851426cd7cf2b6fcf533ace7`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-monet — claim → evidence map（每条论断带 locator）

> 任务 `LEARN-monet` · 依赖 `AUDIT-monet`（ACCEPTED，`review-gate-receipt.json` verdict=accepted）。
> **口径（复用 ACCEPTED 审计的 locator 纪律，不重新审计）**：每条论断给「来源文件 + 具体行/节定位 + 证据等级 + 支持状态」。内部证据 4874f193014ae79c（未公开；来源记录由维护者保留） 为只读回源（声明基线 `f008952365a77e140cbda3f3959d43ef000f9a22`，本 lane 开工已 sha256sum 复核三件冻结输入，见 `RESULT.md §2`）；内部证据 1849016386d530bd（未公开；来源记录由维护者保留） 为上游 ACCEPTED 产物；内部证据 5a7e31d55c785d46（未公开；来源记录由维护者保留） 为本 lane 生成。
> 等级沿用仓库口径：`[自述]`/`[self-written]`/`[reported speech]`/`[contemporary record]` = 作者/同时代人言语记录；`[归纳]` = 项目操作规则/研究者归纳；`[研究]` = 二手研究/文本比对；`[史料]` = 史实/权利记录；`[推测]` 本 lane **不使用**（计数 0）。
> 版本列：仓库文件 = `f0089523…`；staging artifact = 本轮/上游生成（给 sha256）。`read_scope` 与 `access_status` 分开：外部 URL 本轮未重访 = `unknown`，本机文件 = `available`，原图像素目检 = 0（无 `image_seen`）。
> **行号纪律**：conflicts.md 引用 `monet.md L200/L203` 有 +1 漂移；本表一律用**实测行号**（dossier §8.2-1=L201、§8.2-4=L204；card L44/L47；见 #LM-DRIFT 与 AUDIT-monet `RESULT.md §5.1`）。

---

<a id="db-source-line-11"></a>
## A. 输入与版本（本 lane 开工复核）

| # | claim_id | 论断（短） | kind/status | 证据定位（source : locator） | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 1 | LM-INPUT-CARD | card sha = ledger `840a01cd…788a5` | fact/supported | 内部证据 1bca04b26c8e3616（未公开；来源记录由维护者保留） × [monet.md](../../modules/monet.md) 全文件 sha × `RESULT.md §2` 实跑 | `[史料]`（字节实测） | 开工 sha256sum 全等 |
| 2 | LM-INPUT-DOSSIER | dossier sha = ledger `6b0e3e9d…d033e` | fact/supported | 内部证据 97b6222f90f54bf1（未公开；来源记录由维护者保留） × [monet.md](../../dossiers/monet.md) 全文件 sha × `RESULT.md §2` | `[史料]` | 全等 |
| 3 | LM-INPUT-CORPUS | corpus sha = ledger `5d51bb31…ae12b1`（29 quotes） | fact/supported | 内部证据 f74917f8c780834a（未公开；来源记录由维护者保留） × [monet.md](../../dossiers/_corpus/monet.md) 全文件 sha × `RESULT.md §2` | `[史料]` | 全等；29 条沿用 AUDIT 计数 |
| 4 | LM-INPUT-AUDIT-MANIFEST | 上游 `AUDIT-monet/coverage-manifest.md` sha = `b5c15463…1a76` | fact/supported | 内部证据 4f9cba36fbca886b（未公开；来源记录由维护者保留） 全文件 sha × `RESULT.md §2` × AUDIT `receipt.json:70` artifacts 登记值 | `[史料]`（字节实测） | RECEIPT input_hashes 第 4 项 |
| 5 | LM-INPUT-CONFLICTS | conflicts.md sha = `314a24da…bbef` | fact/supported | [conflicts.md](../../../../cross/conflicts.md) 全文件 sha × `RESULT.md §2` × AUDIT `receipt.json:31` | `[史料]` | 全等 |
| 6 | LM-AUDIT-ACCEPTED | 上游 AUDIT-monet 已 ACCEPTED | fact/supported | 内部证据 c54bb74470d1ff81（未公开；来源记录由维护者保留） verdict=accepted, `:16` blocking_defects=0；`receipt.json:6` status=accepted | `[史料]`（产物） | 本 lane 不重新审计，只复用结论 |

<a id="db-source-line-22"></a>
## B. 前置知识（learning_path.md §1）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 7 | LM-K1-STYLE | 风格 = 观察方法 + 制度化工作流（系列与包络是骨架） | observation/supported | `dossiers/monet.md:154`（§6 一句话注脚）；R2/R3 支撑 `:161-162` | `[归纳]`（dossier 自审结论） | 非作者原话 |
| 8 | LM-K2-THREE-RULES | 三条核心可判定规则：4–12px/90–100%/禁>12px；远景≤60%/R²≥0.8；S≤65% | fact/supported | `dossiers/monet.md:201,202,203,204`（§8.2-1/-2/-3/-4）× `modules/monet.md:44,45,46,47` 逐字一致 × `conflicts.md:115,129,180,235` 尾标 `[归纳]` | `[归纳]` | 数值非史料/非像素实测 |
| 9 | LM-K3-PARAMS | P1 默认70% / P3 默认50%且强档≤60%「边界外=透纳领域」 / P6 系列 | fact/supported | `dossiers/monet.md:76-79,86-89,101-104`（§4 P1/P3/P6）× `modules/monet.md:54-57,64-67,79-82` | `[归纳]` | 各参数标 `[归纳]` |
| 10 | LM-K4-CONFLICTS | C-05/C-10/C-14 为组合前必读；处置 N1/N3/N4/N5 | fact/supported | `conflicts.md:36,41,45`（总表）/`:109-121,176-186,229-242`（详节）/`:305-320`（N1/N3/N4/N5）× `modules/monet.md:84-92` 自列 × AUDIT `claim-evidence-map.md:#7-#10,#13-#20` | `[归纳]`（冲突判定） | Lane B 反约束 `[史料]` |
| 11 | LM-K5-SELF | 作者自述层（画真正看到的/母题次要/瞬间性包络/画空气）与 `[归纳]` 严格分开 | fact/supported | `dossiers/monet.md:62,63,64,65`（§3）× `_corpus/monet.md:28,35,51`（条目3/4/6） | `[自述转述]`/`[自述转引]` | dossier `:122` 原信未定位、`:243/:249` `[UNVERIFIED]`，不升级 |
| 12 | LM-K6-BOUNDARY | 莫奈=户外日常/静止瞬间/色点分解/好天气；透纳=天气事件/动势/灾难与崇高/边缘溶解 | observation/supported | `dossiers/monet.md:70` × `modules/monet.md:67` × `conflicts.md:180` × AUDIT `claim-evidence-map.md:#15` | `[归纳]`（项目对齐口径） | 边界口径，非史实断言 |

<a id="db-source-line-33"></a>
## C. 重点作品及来源（learning_path.md §2）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 13 | LM-WORKS-12 | §12 共 9 件临摹/学习清单，本文引用现有记录不新增作品 | fact/supported | `dossiers/monet.md:365`（§12 抬头）/`:369-412`（9 件） × AUDIT `RESULT.md §4`（§12=9 件复核） | `[史料]`（作品信息）/ `[归纳]`（练习映射） | 作品与权利沿用 |
| 14 | LM-WORKS-STROKE | 蛙塘/印象日出/睡莲日本桥 → 笔触与倒影练习 | observation/supported | `dossiers/monet.md:374-377,379-382,404-407` | `[归纳]`（映射） | 练习映射归本项目 |
| 15 | LM-WORKS-ENVELOPE | 印象日出/圣拉扎尔/鲁昂大教堂 → 包络练习 | observation/supported | `dossiers/monet.md:379-382,389-392,399-402` | `[归纳]`（映射） | 同上 |
| 16 | LM-WORKS-HUE | 干草堆/罂粟/露台 → 色温全谱、高调、色相收拢练习 | observation/supported | `dossiers/monet.md:369-372,384-387,394-397` | `[归纳]`（映射） | 同上 |
| 17 | LM-WORKS-RIGHTS | 3 张公开图权利/署名/许可 PD/CC0/CC0 有记录，本 lane 未目检 | fact/supported | `_images/manifest.md:29-31`+`:806-818` × AUDIT `rights-review.md` × `coverage-manifest.md:20`（image_seen=0）/`:31`（external unknown） | `[史料]`（权利账） | 不重访外部 URL |

<a id="db-source-line-43"></a>
## D. 机制与参数（learning_path.md §3 / mechanism_notes.md §1-§3）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 18 | LM-M1 | M1 短逗号笔触场：4–12px / 2–6px / 90–100% / 禁>12px 平滑区 | fact/supported | `dossiers/monet.md:201`（§8.2-1）× `modules/monet.md:44` × `conflicts.md:115`（C-05 侧 `[归纳]`） | `[归纳]` | 自查=边缘密度+连通域 |
| 19 | LM-M2 | M2 包络：远景≤近景60%、单调梯度 R²≥0.8、P3 强档≤60% 收拢 | fact/supported | `dossiers/monet.md:204`（§8.2-4）/`:86-89`（§4 P3）× `modules/monet.md:47,64-67` × `conflicts.md:180,184-185` | `[归纳]` | 分层拟合只在远景层 |
| 20 | LM-M3 | M3 色相：S≤65%、簇≤10、避免高饱和撞色；P3 强档色相收拢 | fact/supported | `dossiers/monet.md:203`（§8.2-3）/`:89` × `modules/monet.md:46` × `conflicts.md:129,350` × AUDIT `claim-evidence-map.md:#21,#22` | `[归纳]` | near-miss #4 取 ≤0.35 |
| 21 | LM-82-ALL-7 | §8.2 共 7 条逐帧可查规则（含 §8.2-5 倒影 / -6 构图 / -7 运动） | fact/supported | `dossiers/monet.md:199-207` × `modules/monet.md:42-50` | `[归纳]` | §8.2-7 属动画/低频局部场 |
| 22 | LM-4-ALL-6 | §4 共 6 个控制参数各三档（P1–P6） | fact/supported | `dossiers/monet.md:74-104` × `modules/monet.md:52-82` | `[归纳]` | 默认 70/65/50/60/40 |
| 23 | LM-MOTION-NOT-C09 | §8.2-7 是低频局部场，不并入 C-09 | observation/supported | `dossiers/monet.md:207` × `modules/monet.md:50` × `conflicts.md:329-330`(N8) × AUDIT `RESULT.md §3 C-09` / `claim-evidence-map.md:#11,#12` | `[归纳]`/`[研究]` | 文本比对，非实验 |

<a id="db-source-line-54"></a>
## E. 冲突行（learning_path.md §6 / mechanism_notes.md §4；指派 C-05/C-10/C-14）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 24 | LM-C05 | C-05 总表存在且含 Monet；Monet 侧引文逐字回源；阈值标 `[归纳]` 未冒充史料 | fact/supported | `conflicts.md:36,109-121,115` × `dossiers/monet.md:201`(实测 L201) × `modules/monet.md:44,88` × AUDIT `claim-evidence-map.md:#7,#8,#9,#10` | `[归纳]` | 解法 N1+N3（`:118-121,305-312`）；AUDIT 判 supported |
| 25 | LM-C10 | C-10 总表存在（莫奈×塞尚）；「边界外=透纳领域」与档案边界口径一致；E2c 待补 | fact/supported | `conflicts.md:41,176-186,180,184-186,335` × `dossiers/monet.md:204,86,89,70` × `modules/monet.md:47,64-67` × AUDIT `claim-evidence-map.md:#13,#14,#15,#16` | `[归纳]` | 分层解+N4（`:184-185,314-315`）；AUDIT 判 supported |
| 26 | LM-C14 | C-14 总表存在（覆盖级）；Monet 雾色渐变回源；反约束卡级资产非全局常量；Lane B 侧 `[史料]` 分层正确 | fact/supported | `conflicts.md:45,229-242,233,235,237-242,320` × `dossiers/monet.md:204` × `modules/monet.md:47,91` × AUDIT `claim-evidence-map.md:#17,#18,#19,#20` | `[归纳]`/`[史料]` | N1/N5（`:305-306,320`）；AUDIT 判 supported |
| 27 | LM-C06-NM4 | C-06（同侧旁证）+ near-miss #4（≤0.35）登记，非指派行 | fact/supported | `conflicts.md:37,123-134,129,350` × `dossiers/monet.md:203` × `modules/monet.md:89,46,92` × AUDIT `claim-evidence-map.md:#21,#22,#30` | `[归纳]` | 登记覆盖完整性，不改写 |
| 28 | LM-N-RULES | N1/N3/N4/N5/N9 组合规则可回源 | fact/supported | `conflicts.md:305-306,311-312,314-315,317-320,332-333` | `[归纳]` | N9「双标准」失败形态 |
| 29 | LM-TURNER-BOUNDARY | 「边界外=透纳领域」是练习硬边界 | observation/supported | `dossiers/monet.md:70,89` × `modules/monet.md:67` × `conflicts.md:180` × AUDIT `claim-evidence-map.md:#15` | `[归纳]` | 边界口径，非史实断言 |
| 30 | LM-DRIFT | conflicts.md:115/180/235 引 `monet.md L200/L203`，实测 L201/L204（+1 漂移）；本文用实测行号 | observation/conflict（登记） | `conflicts.md:115,180,235,404` × `dossiers/monet.md:201,204`（AUDIT `raw §6 nl -ba`） × `modules/monet.md:44,47` × AUDIT `RESULT.md §5.1`/`claim-evidence-map.md:#33`/`review-gate-receipt.json:21` | `[研究]`（文本比对） | 与 A-34 页码 ±1 不同对象；**未改仓库**（只读） |

<a id="db-source-line-66"></a>
## F. How-to-Think 等级分离（how-to-think.md）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 31 | LM-HT-SPLIT | 自述层与研究者推断严格分栏；每步带证据等级；`[推测]` 计数 0 | observation/supported | `how-to-think.md §0/§1/§5` × `00-GOAL.md:9` × `dossiers/monet.md:250`（未使用 `[推测]`）× AUDIT `RESULT.md §6` | `[归纳]`（本卡纪律） | 不从作品外观反推心理 |
| 32 | LM-HT-SELF-QUOTES | S1–S4/S7 的「为什么」上半来自作者言语记录（Perry/吉维尼/1890 信） | fact/supported | `dossiers/monet.md:62,63,65,113,117,123,125,127`（§3/§5）× `_corpus/monet.md:19,28,35,51`（条目2/3/4/6）× `dossiers/monet.md:47,53,54,55`（§2-1/-7/-8/-9） | `[自述]`/`[自述转述]`/`[研究]` | corpus 类型分级 `:4`；转录风险 `:5-6,147,247-251` 不静默消除 |
| 33 | LM-HT-INFER-ONLY | S5/S6 为纯 `[归纳]` 步（数值判据无作者自述支撑） | fact/supported | `how-to-think.md §2 S5/S6` × `dossiers/monet.md:201,203,204` × `conflicts.md:115,129,180,235` | `[归纳]` | 不写「莫奈要求 4–12 px」 |
| 34 | LM-HT-NO-PSYCH | 不含「从画面推作者心理」的句子 | observation/supported | `how-to-think.md §4` 反心理推断清单 × `00-GOAL.md:9` | `[归纳]` | 红线 |

<a id="db-source-line-75"></a>
## G. 练习、结果、失败、边界（learning_path.md §4-§8 / mechanism_notes.md §5-§6）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 35 | LM-LADDER-3 | 三条阶梯练习：comma-stroke field studies → atmospheric envelope gradients → hue-collapse discipline | design_candidate/supported（作为「建议练习」交付） | `learning_path.md §4` × `dossiers/monet.md:374-377,379-382,404-407`（阶梯一）/`:204,86-89,47,184-185`（阶梯二）/`:203,89,196,197,101-104,70`（阶梯三） | `[归纳]`（本项目设计） | **建议练习**，学习收益未经人评 |
| 36 | LM-A30-SHAPE | 学习路径含 A-30 §8.1 八节：前置知识/重点作品及来源/要观察的机制/具体练习/可观察结果/常见失败/下一步/使用边界 | fact/supported | `01-AUDIT.md:269-273`（§8.1）× `learning_path.md §1-§8` 八节标题 × `ops/GOALS.md:44`（A-30 open） | `[史料]`（spec）/ `[归纳]`（映射） | 练习效果须标建议练习（`:273`） |
| 37 | LM-PRACTICE-UNVERIFIED | 练习效果未由人完成/评价，标「建议练习」不写「已证实学习收益」 | fact/supported | `01-AUDIT.md:273` × `learning_path.md B1/§4 抬头` × `01-AUDIT.md:74`（人评字段另列） × 本 `receipt.json` human_review=not_applicable | `[史料]`（spec）/ `[归纳]`（严格执行） | 硬边界 |
| 38 | LM-OBSERVABLE | 可观察结果是练习产物自查口径，非原作像素实测 | observation/supported | `learning_path.md §5` × `dossiers/monet.md:201,203,204`（§8.2 自查法）× AUDIT `coverage-manifest.md:20`（原图目检=0） | `[归纳]` | 不声称原作被证实如此 |
| 39 | LM-FAILURES | 7 类常见失败（F1 抹平/C-05、F2 全局渐变禁令/C-14、F3 双标准/C-10、F4 高饱和/C-06、F5 越透纳边界、F6 等级混淆、F7 回源纪律） | observation/supported | `learning_path.md §6` × `conflicts.md:115,119,129,180,184-185,237-241,305-320,350` × `dossiers/monet.md:70,89,203` × AUDIT `coverage-manifest.md §2` | `[归纳]` | 规则层判定，非实验 |
| 40 | LM-BOUNDARY-TURNER | 使用边界含「边界外=透纳领域」为硬边界 | fact/supported | `learning_path.md B3 §8` × `dossiers/monet.md:70,89` × `modules/monet.md:67` × `conflicts.md:180` | `[归纳]` | 换模块，非 P3 延伸 |
| 41 | LM-NO-REPO-WRITE | 本 lane 仅写 内部证据 bfc951d3749e7e9c（未公开；来源记录由维护者保留），仓库只读、无 git、无子代理、无凭据 | observation/supported | 本 `receipt.json` `allowed_write_paths`=内部证据 bfc951d3749e7e9c（未公开；来源记录由维护者保留）、`spawns_allowed=false` × AUDIT `claim-evidence-map.md:#37`（同口径） | `[史料]`（产物声明） | 只读约束遵守 |
| 42 | LM-EXTRACT-228 | card §8.1/§8.2/§4 与 dossier 逐字一致（`_extract.py --check` 全库 228/228，Monet 占 3） | fact/supported | AUDIT `RESULT.md §2`/`§4`/`§7` × `claim-evidence-map.md:#34,#42` × `raw/extract-check.out`（全库）；本 lane **未重跑**，沿用 ACCEPTED 审计结论 | `[史料]`（上游实跑） | A-34「33/33」为 wave14 子集口径，不混用 |

---

<a id="db-source-line-90"></a>
## 支持状态汇总（分母 = 42 条论断）

- `supported` = **41**；`conflict`（登记的行号漂移 `#30`，非「未验证」）= **1**；`partial` = 0；`unverified` = 0；`not_applicable` = 0。
- `[推测]` 级结论 = **0**；无「从作品外观反推作者心理」的句子（见 #31/#34）。
- 所有 §8.2/§4/conflicts 数值均标 `[归纳]`，未冒充 `[自述]`/`[史料]`/像素实测（#8/#18/#19/#20/#33）。
- 练习 = **建议练习**，`human_review=not_applicable`，不写「已证实学习收益」（#35/#37）。
- 外部 URL 本轮**未重访**（`access_status=unknown`，见 AUDIT `coverage-manifest.md §2`）；3 张公开图**未目检**（`image_seen=0`）；#13–#17 作品/权利论断支持范围 =「本机文件内引用与记录仍存在且连贯」，不声称外部页面当前可访问。
- 本 lane `status=submitted`（非 accepted），`review=null`，独立审阅由 review gate 承担（见 `receipt.json`）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
