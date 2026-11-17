<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-da_vinci；原正文 SHA-256 `13e0f055fc2943f1c3250afdf13f750d4f8ac98d815d2699b3abf5e8e4a67800`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-da_vinci — Claim → Evidence Map

- task_id `LEARN-da_vinci` ｜ 证据基 内部证据 252842d84192cfe1（未公开；来源记录由维护者保留）（**ACCEPTED**）｜ 只读仓库 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22`
- 目的：让 [learning_path.md](learning_path.md)、[how-to-think.md](how-to-think.md)、[mechanism_notes.md](mechanism_notes.md) 中**每一条主张**都能寻址到 dossier / corpus / conflicts / 既有 AUDIT 记录（A-30「零缺失本地引用」）。
- 分级沿用 dossier `L4–L5`：`[自述]/[史料]/[研究]/[归纳]/[推测]`；`[归纳]` 是**操作规则**，不冒充艺术家内心（`DOS:L5`）。
- 「支持状态」口径：`supported` = 本机文件内声明/可机械复现；`partial` = 二级转引/单源；`unverified` = 未与纸本/在线/像素复核；`conflict` = 跨模块硬/覆盖冲突（已登记）。

<a id="db-source-line-8"></a>
## 0. 源短码（开工逐字节 sha256 实测，见 RESULT.md §1）

| 短码 | 文件（相对 repo 根或 内部工作区） | sha256 | read_scope |
|---|---|---|---|
| `DOS` | [da_vinci.md](../../dossiers/da_vinci.md) @ f0089523 | `56b02e9b629636529f66524f74c6e46d32f1f8deee8364b5dad151d34f0e634c` | fulltext |
| `CARD` | [da_vinci.md](../../modules/da_vinci.md) @ f0089523 | `34d85edb2ede277906a3e7ff70322ea594b2df7651e5315573f25a67f238e7ab` | fulltext |
| `COR` | [da_vinci.md](../../dossiers/_corpus/da_vinci.md) @ f0089523 | `15f0fd1d593f895e2371a72162398da5c5369b822622cc49f19d2c8ecc1b0765` | fulltext |
| `CONF` | [conflicts.md](../../../../cross/conflicts.md) @ f0089523 | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | fulltext + citation_context |
| `GOAL` | 执行包 `01-AUDIT.md` §8.1 / §8.4（A-30 规格） | （执行包只读，非本轮回执字节校验对象） | sections |
| `AUD-R` | 内部证据 c544392b35db457b（未公开；来源记录由维护者保留）（ACCEPTED） | `8916dedff53d6b8a0d2d0ce913f3ee692189d47914496fc4530722ad3548f428` | fulltext |
| `AUD-C` | 内部证据 c59eea53272d6558（未公开；来源记录由维护者保留） | `c9e3158cd91f6abfa3e705e162e51193b24993dd833ee90073db9998a7e7c684` | fulltext |
| `AUD-M` | 内部证据 bc0bc8883530901b（未公开；来源记录由维护者保留） | `13892f54468d53270173448745c916f4c082c6b19b4dca52bb28c445db41e590` | fulltext |

- 现场实测行号：`DOS:L162–168` = §8.2 七条；`CARD:L63–69` = §8.2 七条；`DOS:L63–73` = §4 五参数；`DOS:L327–377` = §12 学习清单。
- 定位漂移：`CONF` 对 da_vinci §8.2 行号 off-by-one + 文件名歧义（`AUD-R §5 末`、`AUD-C DV-CF-LOC`）；本文引用 `CONF` 用「§+行区间」，规则条目用实测行号。

<a id="db-source-line-24"></a>
## 1. 结构 / 元主张（identity & provenance）

| claim_id | 主张 | 等级 | 支持状态 | 定位 |
|---|---|---|---|---|
| LP-META-01 | task_id `LEARN-da_vinci`、lane=learning、status=submitted、依赖 `AUDIT-da_vinci`、required_artifact_kinds 4 项、spawns_allowed=false | `[史料]` | supported | `tasks-plan.json L2062–2103`（执行包）；本轮回执 `receipt.json` |
| LP-META-02 | 本 lane 0 仓库写入 / 0 子代理 / 0 网络 / 无凭据；仅写 内部证据 da336e113891348d（未公开；来源记录由维护者保留） | `[史料]` | supported | `RESULT.md §6`；`runner_receipt.json` |
| LP-META-03 | 3 个 repo 输入 sha256 与 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） 登记值逐字节一致 | `[史料]` | supported | 内部证据 11f53996d0ded93d（未公开；来源记录由维护者保留）；现场 `sha256sum`（`RESULT.md §1`）；`AUD-R §1`、`AUD-C DV-IN-01` |
| LP-META-04 | A-30 §8.1 八要素 = 前置知识/重点作品及来源/要观察的机制/具体练习/可观察结果/常见失败/下一步/使用边界；练习效果未人评时写「建议练习」，不写「已证实学习收益」 | `[史料]` | supported | `GOAL 01-AUDIT.md L271, L273`（§8.1） |
| LP-META-05 | How to Think 须区分作者核实自述与研究者推断，不能编造作者心理 | `[史料]` | supported | `GOAL 00-GOAL.md L9`；`01-AUDIT.md L306–308`（§8.4）；`DOS:L5` |
| LP-META-06 | 证据分级 `[自述]/[史料]/[研究]/[归纳]/[推测]`，`[归纳]` 不冒充艺术家内心 | `[史料]` | supported | `DOS:L4–L5`；`AUD-R §0` |

<a id="db-source-line-35"></a>
## 2. 前置知识 / 作品 & 权利（learning_path §1–§2）

| claim_id | 主张 | 等级 | 支持状态 | 定位 |
|---|---|---|---|---|
| LP-PRE-01 | 前置概念：中间调 `L∈[40,70]`、纯黑白 `≤3%`、过渡带 ≥1.5% 短边、Laplacian ≤2、连续硬边 ≤40px、`S≤0.35`、远景 210°±20、单光源 ≤15° | `[归纳]` | supported | `DOS:L162–168`（§8.2）、`CARD:L63–69`；`DOS:L160`「可逐帧自查」 |
| LP-PRE-02 | §4 五参数（含默认 70/60/55/45/65%）与档位 | `[归纳]` | supported | `DOS:L63–73`、`CARD:L71–81` |
| LP-PRE-03 | sfumato 文本由来 = Trattato II,67「ad uso di fumo」，经 Melzi 死后汇编、1651 首印 | `[自述/史料]` | partial | `DOS:L77`、`DOS:L91–93`、`DOS:L195–198`（§9 交叉核对 B）；`AUD-R §3.4–3.5` 外部章号 unverified |
| LP-W-01 | 《蒙娜丽莎》卢浮宫 INV 779 / 油彩杨木板 79.4×53.4cm / 约1503 起持续修改 / 找最硬边找不到 | `[史料/研究]` | supported | `DOS:L13`（§0-1）、`DOS:L332–335`（§12.1）、`DOS:L118`（§7-1）、`DOS:L184`（§9 [7]） |
| LP-W-02 | 《岩间圣母》伦敦版 NG1093 / 1491/2–1508 / 189.5×120cm / 暗底浮现·左上单一柔光·三阶段史 | `[史料/研究]` | supported | `DOS:L14`（§0-2）、`DOS:L337–340`（§12.2）、`DOS:L119`（§7-2）、`DOS:L185`（§9 [8]） |
| LP-W-03 | 《最后的晚餐》米兰恩宠圣母修道院 / 约1492/94–1498 / 四组三人·基督头=消失点 | `[史料/研究]` | supported | `DOS:L15`（§0-3）、`DOS:L342–345`（§12.3） |
| LP-W-04 | 其余 6 件重点作品（圣母子与圣安妮/施洗者圣约翰、抱银貂的女子、吉内芙拉·德·本奇、维特鲁威人、三王来朝未完成稿、手稿页） | `[史料/研究]` | supported | `DOS:L16`、`DOS:L347–375`（§12.4–12.9） |
| LP-RT-01 | 3 张公开图像 = 2 PD + 1 CC BY-SA 4.0（last_supper），不可统称 PD；images_manifest=false | `[史料/归纳]` | supported | `AUD-R §7`、`AUD-C DV-RT-01/02`、`AUD-M denominators.public_images`；`_images/manifest.md L20–22` |
| LP-RT-02 | 本轮未目检像素（image_seen=0）、未独立复核 Commons 许可页 | `[史料]` | supported | `AUD-R §7`、`AUD-M public_images.image_seen=0` |
| LP-BIO-01 | 生平材料沿用 §11 / corpus 17–22，不新增；A-31「2688 字」未复现 | `[史料/归纳]` | partial | `DOS:L210–230`、`COR:L136–182`；`AUD-R §6`、`AUD-C DV-A31-02` |

<a id="db-source-line-50"></a>
## 3. 机制 & 判分线（learning_path §3/§5、mechanism_notes §2）

| claim_id | 主张 | 等级 | 支持状态 | 定位 |
|---|---|---|---|---|
| LP-M1 | sfumato：无轮廓线、宽连续灰度带；过渡带 ≥1.5% 短边、硬边 ≤40px | `[归纳]`（规则）+`[研究/自述]`（锚） | supported | `DOS:L162–163`、`DOS:L23`、`DOS:L38/L40`、`DOS:L91–93`、`COR:L24–30`；`CARD:L63–64` |
| LP-M2 | 烟式中间调：`L∈[40,70] ≥55%`、纯黑白 ≤3% | `[归纳]`（规则）+`[研究]`（锚） | supported | `DOS:L164`、`DOS:L24`、`COR:L42–55`；`CARD:L65` |
| LP-M3 | 笔触不可见：平坦区 Laplacian 方差 ≤2、只有渐变 | `[归纳]`（规则）+`[自述/研究]`（锚） | supported | `DOS:L168`、`DOS:L91–93`、`DOS:L38`；`CARD:L69`、`CARD:L29` |
| LP-M4 | 空气透视：远景 210°±20、相对近景饱和降 ≥30% | `[归纳]`（规则）+`[自述]`（锚） | supported | `DOS:L166`、`COR:L64–69`（cap.423）、`COR:L71–76`（cap.902）、`DOS:L41`；`CARD:L67` |
| LP-M5 | 单一柔光/暗底浮现：夹角 ≤15°、补光 ≤主光 40% | `[归纳]`（规则）+`[研究]`（锚） | supported | `DOS:L167`、`DOS:L42`、`DOS:L26`；`CARD:L68` |
| LP-M6 | 窄色域低饱和：均值 S≤0.35、S>0.6 ≤5% | `[归纳]`（规则）+`[研究]`（锚） | supported | `DOS:L165`、`DOS:L25`；`CARD:L66` |
| LP-R-01 | 自查表 R1–R7（含测法）逐条对应 §8.2 七条 | `[归纳]` | supported | `DOS:L160–168`、`CARD:L63–69` |
| LP-R-02 | §4 P5「表情模糊度」无 §8.2 数值量规，不伪造阈值 | `[归纳]` | supported | `DOS:L71`、`DOS:L335`、`DOS:L355`；`mechanism_notes §1/§6 G1` |
| LP-R-03 | 1920 换算基数差异（短边 vs 长边）记为待统一口径 | `[归纳]` | unverified | `DOS:L163` 原文「短边」 vs `CONF §2 L78`「1920 宽 ≥28.8px」；`AUD-R §5 末` |
| LP-P-01 | 「像达·芬奇」最小组合 = Sfumato ≥中档 + 空气透视 ≥中档 + 色域 ≤中档 | `[归纳]` | supported | `DOS:L73`、`CARD:L81` |
| LP-P-02 | §8.1b 纯风格段（场景可迁移，删题材词）可作无人物题材替换分支 | `[归纳]` | supported | `CARD:L41–57`；`AUD-R §1` `card_has_81b=true` |

<a id="db-source-line-66"></a>
## 4. 练习阶梯 / 观察结果 / 失败（learning_path §4–§6、mechanism_notes §4）

| claim_id | 主张 | 等级 | 支持状态 | 定位 |
|---|---|---|---|---|
| LP-EX-01 | 阶梯1 灰阶梯度：A5 局部、禁描边、先灰阶后叠色层；量 R2/R3/R7 | `[归纳]`（建议练习） | supported（为建议，非成效） | `DOS:L335`（§12.1）、`DOS:L337–340`（§12.2）、`DOS:L377`、`DOS:L162–164/L168` |
| LP-EX-02 | 阶梯2 空气透视分层：按 z 排序、色相收蓝、饱和降 ≥30%、远景只留模糊中间暗调 | `[归纳]`（建议练习） | supported（为建议，非成效） | `DOS:L166`、`DOS:L165`、`DOS:L68`（§4 强档）、`COR:L64–69`、`CARD:L48–56` |
| LP-EX-03 | 阶梯3 边缘链纪律 ≤40px：Sobel/Canny + 镜检自校 | `[归纳]`（建议练习） | supported（为建议，非成效） | `DOS:L162–163`、`DOS:L335`、`COR:L111–116`（cap.401 置镜）、`COR:L24–30` |
| LP-EX-04 | 3 条阶梯「建议练习」，练习效果未人评/未验证学习收益 | `[史料]` | supported | `GOAL 01-AUDIT.md L273`；`01-AUDIT.md L306–308`（§8.4）；本轮 `human_review=not_applicable` |
| LP-F-01 | F1 过渡带不足/折中 → C-02 两边不过 | `[归纳]` | conflict（已登记） | `DOS:L163`；`CONF §2 L71–82`（§1 L33）；`AUD-C DV-CF-02` |
| LP-F-02 | F2 直方图双峰 → C-03 退化、全帧不可拆 | `[归纳]` | conflict（已登记） | `DOS:L164`；`CONF §2 L84–95`（§1 L34）、`§3 N4 L314–315`；`AUD-C DV-CF-03` |
| LP-F-03 | F3 可见笔触/把平滑渐变当违规 → C-05 镜像禁令 | `[归纳]` | conflict（已登记） | `DOS:L168`；`CONF §2 L109–121`（§1 L36）；`AUD-C DV-CF-05` |
| LP-F-04 | F4 高饱和冲破 S≤0.35 → C-06，达·芬奇为同侧旁证 | `[归纳]` | conflict（已登记） | `DOS:L165`；`CONF §2 L123–134`（§1 L37）；`AUD-C DV-CF-06` |
| LP-F-05 | F5 照抄「别做成：渐变」 → C-14 覆盖冲突 | `[归纳]` | conflict（已登记） | `CONF §2 L229–242`（§1 L45）、`§3 N1 L305`/`N5 L320`；`AUD-C DV-CF-14` |
| LP-F-06 | F6/F7/F8/F9（纯黑白溢出、把归纳当内心、权利误用、长边换算） | `[归纳]` | supported | `DOS:L164/L162`、`DOS:L5`、`AUD-R §7`、`DOS:L163 vs CONF §2 L78` |

<a id="db-source-line-81"></a>
## 5. How-to-Think 决策序（how-to-think.md §1–§2）

| claim_id | 主张（先选/牺牲/为什么） | 等级 | 支持状态 | 定位 |
|---|---|---|---|---|
| HT-S1 | 先选明暗而非颜色；自述「躲阴影者躲开艺术荣耀」 | 自述 `[自述]` + 操作 `[归纳]` | supported（文本级） | `DOS:L94–96`（III,406）、`DOS:L58`、`COR:L49–55`；`DOS:L39,L69–70` |
| HT-S2 | 先选经验/自然而非二手成法 | 自述 `[自述]` + 操作 `[归纳]` | supported（文本级） | `DOS:L54–56`、`COR:L88–100`、`COR:L104–130`；`DOS:L44` |
| HT-S3 | 先选边界化开而非勾线填色 | 自述 `[自述]` + 研究 `[研究]` + 操作 `[归纳]` | partial（自述含汇编边界） | `DOS:L91–93`、`COR:L24–30`、`DOS:L23`；`DOS:L38,L40,L162–163` |
| HT-S4 | 先选中间调而非极黑白 | 研究 `[研究]` + 自述 `[自述]` + 操作 `[归纳]` | supported | `DOS:L24`、`COR:L42–55`；`DOS:L164` |
| HT-S5 | 先选距离衰减而非等清晰度 | 自述 `[自述]` + 操作 `[归纳]` | supported（文本级） | `COR:L64–69`、`COR:L71–76`、`COR:L57–62`；`DOS:L41,L166` |
| HT-S6 | 先选单光源而非多光源戏剧（光源方向是馆方研究，非自述） | `[研究]` + 操作 `[归纳]` | supported | `DOS:L42`；`DOS:L167`、`CARD:L35` |
| HT-S7 | 先选慢工与自校而非一次定稿 | 自述 `[自述]` + 史料 `[史料]`(转引) + 操作 `[归纳]` | partial | `DOS:L59`、`COR:L111–123`、`DOS:L61`、`COR:L152–157`、`DOS:L47`；`DOS:L48,L335,L377`；`AUD-R §4` |
| HT-S8 | 先选笔触隐形而非笔触表现 | 自述 `[自述]` + 研究 `[研究]` + 操作 `[归纳]` | supported | `DOS:L91–93`、`DOS:L38`；`DOS:L168`、`CARD:L29` |
| HT-SEP-01 | 自述仅证「文本中写了价值排序/禁忌」，不推断心理、动机、情绪 | `[史料]` | supported | `GOAL 00-GOAL.md L9`、`01-AUDIT.md L306–308`；`DOS:L5` |
| HT-SEP-02 | §8.2 七条 / §4 五参数 / §2 十一条 / 使用建议 全部 `[归纳]`，非达·芬奇意图 | `[归纳]` | supported | `DOS:L5,L160`、`DOS:L34–48,L63–73,L162–168,L73`；`CONF §3 N3 L312` |
| HT-SEP-03 | 画面「神秘/安静」是现代 prompt 氛围词，非从外观反推的心理 | `[归纳]` | supported | `CARD:L30,L56`；`DOS:L5` |
| HT-BND-01 | 自述硬边界：Melzi 汇编 / 1651 首印 / 1890 章号外部未核 / 「ad uso di fumo」可能含润色 | `[史料/归纳]` | unverified | `DOS:L77,L195–198,L424`；`AUD-R §3.5`、`COR:L188–190` |

<a id="db-source-line-98"></a>
## 6. 冲突行 5/5（mechanism_notes §3、learning_path §6–§7）

| claim_id | 主张 | 等级 | 支持状态 | 定位 |
|---|---|---|---|---|
| CF-02 | 达·芬奇 ≥1.5% 短边 vs 米开朗基罗 ≤0.6%，硬冲突交集空；轴单主/分区表 | `[归纳]` | supported（conflict 已登记） | `CONF §1 L33`、`§2 L71–82`、`§3 N3 L311–312`；`DOS:L163`；`AUD-R §5`、`AUD-C DV-CF-02` |
| CF-03 | 达·芬奇中间调 ≥55% vs 卡拉瓦乔 ≤25%+暗带≥40%，全帧不可拆，二选一 | `[归纳]` | supported（conflict 已登记） | `CONF §1 L34`、`§2 L84–95`、`§3 N4 L314–315`；`DOS:L164`；`AUD-C DV-CF-03` |
| CF-05 | 达·芬奇 Laplacian≤2「只有渐变」vs 梵高/莫奈/塞尚笔触轴，镜像禁令 | `[归纳]` | supported（conflict 已登记） | `CONF §1 L36`、`§2 L109–121`、`§3 N1 L305`；`DOS:L168`；`AUD-C DV-CF-05` |
| CF-06 | 马蒂斯每块≥70% vs 毕加索均值≤35%；达·芬奇 §8.2-4 为同侧旁证 | `[归纳]` | supported（conflict 已登记） | `CONF §1 L37`、`§2 L123–134`、`§4 L350`；`DOS:L165`；`AUD-C DV-CF-06/DV-CF-NM` |
| CF-14 | Lane B 06/07/13「别做成：渐变」vs 达·芬奇 sfumato，覆盖冲突/反约束适用域 | `[归纳]` | supported（conflict 已登记） | `CONF §1 L45`、`§2 L229–242`、`§3 N1 L305`/`N5 L320`；`DOS:L163,L168`；`AUD-C DV-CF-14` |
| CF-NM | near-miss #4 四上限取 ≤0.35；§3 N1/N3/N6 采纳状态与 CARD:L4 指针一致 | `[归纳]` | supported | `CONF §3 L303,L305,L311`、`§4 L350`；`CARD:L4,L92`；`AUD-C DV-CF-NM` |
| CF-LOC | `CONF` 对 da_vinci §8.2 行号 off-by-one + 文件名歧义，移交冲突 lane | `[归纳]` | supported | `AUD-R §5 末`、`AUD-C DV-CF-LOC`（实测 `DOS:L162–168` vs `CARD:L63–69`） |

<a id="db-source-line-110"></a>
## 7. 未决 / 诚实登记

| claim_id | 主张 | 等级 | 支持状态 | 定位 / next action |
|---|---|---|---|---|
| U-01 | Trattato 1890 版章号外部正确性未核（不联网、无纸本） | `[归纳]` | unverified | `COR:L188–190 [UNVERIFIED]`、`AUD-R §3.5`；允许联网时回源 it.wikisource 逐 cap 比对 |
| U-02 | da_vinci 单档 Trattato 引文仅覆盖 5/8 部（缺 quarta/settima/ottava） | `[归纳]` | supported（未找到已登记） | `AUD-R §3.4`、`AUD-C DV-TR-03/04`、`AUD-M trattato_parti_in_davinci`；本 LEARN 不依赖该 3 部 |
| U-03 | 3 张图像许可页/像素未独立复核 | `[史料]` | unverified | `AUD-R §7`、`AUD-M image_seen=0`；需视觉/权利复核时另立 lane |
| U-04 | 练习效果未人评、未验证学习收益 | `[史料]` | not_applicable | `GOAL 01-AUDIT.md L273`；本轮 `human_review.status=not_applicable` |
| U-05 | 「短边」vs「1920 长边」换算基数冲突未裁定 | `[归纳]` | unverified | `DOS:L163` vs `CONF §2 L78`；移交冲突 lane 统一口径 |
| U-06 | P5 表情模糊度无数值量规 | `[归纳]` | not_applicable | `DOS:L71`、`mechanism_notes §6 G1`；不伪造阈值 |

<a id="db-source-line-121"></a>
## 8. 覆盖自审

- 本 map 列出 **LP-META(6) + LP-PRE(3) + LP-W/RT/BIO(7) + LP-M/R/P(9) + LP-EX/F(10) + HT-S/SEP/BND(12) + CF(7) + U(6) = 60 条 claim_id**，覆盖 [learning_path.md](learning_path.md)（§0–§8）、[how-to-think.md](how-to-think.md)（§0–§4）、[mechanism_notes.md](mechanism_notes.md)（§0–§7）全部结构性主张。
- **零缺失本地引用**：每条均给 `DOS/CARD/COR/CONF` 实测行号或 `AUD-R/AUD-C/AUD-M` 的节号/claim_id；无外链依赖、无凭空数值。
- 未把 `supported` 扩大解释为「纸本正确 / 像素验证 / 人评通过 / 学习成效」；`unverified`/`not_applicable`/`conflict` 均如实标注。
- 仅写 内部证据 da336e113891348d（未公开；来源记录由维护者保留）；仓库只读、0 子代理、0 网络、无凭据；status `submitted`、review `null`、`human_review.status=not_applicable`。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
