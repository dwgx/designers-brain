<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-chardin；原正文 SHA-256 `ed28840d2c033e5de0bc8bdbad90034cf793d2d7bd0b3e2a60fcfaa9a1d4b71b`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-chardin — claim → evidence map

- goal_id `Designers-Brain-Upgrade-20261115` · task_id `LEARN-chardin`（A-30 单片）· baseline `f008952365a77e140cbda3f3959d43ef000f9a22`
- 依赖：内部证据 382bee103ab3d7a6（未公开；来源记录由维护者保留）（**ACCEPTED**：磁盘 `receipt.json` `status=accepted` / `review.verdict=accepted` / `review-evidence.md` Verdict=accepted）。本 map **复用 ACCEPTED 审计的 locator 纪律与分母结论，不重审、不改仓库/审计产物**；AUDIT 的 `run_checks.py` 105/105 定位解析、`raw/*` fetch 缓存本 lane 不重跑。
- 每条 = `claim_id` + `文件:行号(可带锚点子串)` + 等级 + 支持状态 + basis（被引字节实际证明什么）。等级沿用 dossier `D:5` 图例（`[自述]` `[史料]` `[研究]` `[归纳]` `[推测]`）与 corpus `Q:4` 类型标签；`[推测]` 本片计数 = 0。
- `support_status`：supported / partial / conflict / unverified。**`[归纳]` 操作阈值一律标 `partial`（未对原作像素测量，`D:281,L212`），不升 supported**；转录层引文照 AUDIT 口径带注记。

<a id="db-source-line-8"></a>
## File key（开工 `sha256sum` 实测，见 `RESULT.md §0`）

| key | path | sha256 |
|---|---|---|
| D | [chardin.md](../../dossiers/chardin.md) | `323f72f30f1b490b0dd2c8d361e7ec628f67d7fb95e61870d559180fc703a832` |
| C | [chardin.md](../../modules/chardin.md) | `df57eb65bcc51889105ab76f2e9b0d1bf3e1990ce014b36ed7049e7bcee8c640` |
| Q | [chardin.md](../../dossiers/_corpus/chardin.md) | `7b11679f2fe454e9694121ae3d999074de4b037830867eb88fcf177c65b66495` |
| R | [manifest.md](../../dossiers/_images/manifest.md) | `5698124daf47c989fd26232a686ec54cda2658b623e1a302ddb5806ebf95b470` |
| X | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` |
| G | `ops/GOALS.md` | `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144` |
| IDX | [INDEX.md](../../dossiers/_corpus/INDEX.md) | （只读索引行，L74） |
| AR | 内部证据 d86f2b1ba0e3f9a9（未公开；来源记录由维护者保留） | `65af849e4f32748fed2aeb25c84cc7596df58931377ecc2c643019483aba5e91` |
| AM | 内部证据 8aa0e735ea612422（未公开；来源记录由维护者保留） | `13fb3d619b87fd03f0d6f5da4dc366002abed0a5a75a9f5131822bbd62a1d02c` |
| AC | 内部证据 79d8077627117572（未公开；来源记录由维护者保留） | `dc588fed4353a7e760de9f400b8555792d4fd10b0adc0459e0fd91d9e061cc15` |
| AE | 内部证据 c4f210bbdf634f77（未公开；来源记录由维护者保留） | `c36f91a87302feb984c24e971c0a78b57ed0fb446c7b83fff11a49f1374752b8` |
| AT | 内部证据 5508b414a6316524（未公开；来源记录由维护者保留） | `6e304471e124f654244e8b85c180024576614b30e78599da52d67d5c24ba9bad` |

---

<a id="db-source-line-27"></a>
## §A 质感层积 + 弱光源机制（brief ①；本项目 `[归纳]` 机制标签）

| claim_id | locator（file:line + 锚点子串） | 等级 | support | basis |
|---|---|---|---|---|
| C-M1-01 | `Q:76-81` 「Il place ses couleurs l'une après l'autre sans presque les mêler… mosaïque de pièces de rapport… point carré」（Q10 Raynal 1750） | `[史料]`(`[contemporary record]`) | supported | 「放而不混」= 同时代记录；`D:40`（§1-2）、`D:59`（§2-4）同引。非画家自述。 |
| C-M1-02 | `Q:90-95` 「Approchez-vous, tout se brouille, s'aplatit et disparaît ; éloignez-vous, tout se crée et se reproduit.」（Q12 Diderot 1763） | `[史料]`(`[contemporary record]`) | supported（转录层） | 远近检验 = 「放而不混」判读来源；**法文逐字未独立 web 复取**（`AM:130`），fetch3 英文旁证，不升一手。 |
| C-M1-03 | `Q:199-204` 「never disguise the rough texture of paint… Dragged roughly over the canvas」（Q27 Met Baetjer 2015） | `[研究]`(`[research]`) | supported | 表面保留颜料粗糙质地；**fetch3 逐字核**（`ed46f94b…d99b`，`AR:64` F3）。 |
| C-M1-04 | `Q:192-197` 「l'artiste peint par larges touches… il accordera une place de plus en plus grande aux reflets, aux transparences, au « fondu »」（Q26 Rosenberg 1979） | `[研究]`(`[research]`) | supported | 层积 + 罩染 + 揉合的时期演进；`D:48`（§1-10）、`D:65`（§2-10）同引。 |
| C-M1-05 | `C:44`（§8.2-1）「全帧『可辨笔触纹理』面积占比 **30–80%**… 禁止统一方向角度族（…峰值 ≤35%）」；`D:203` 同 | `[归纳]` | partial | 质感层积的可判定阈值；**未对原作像素测量**（`D:281` §10-7、`C:53`）。 |
| C-M1-06 | `C:49`（§8.2-6）「同屏可辨材质 ≥2 类、各有**专属表面处理**… 禁止两种材质共用同一处理（防『一律点彩』）」；`D:208` 同 | `[归纳]` | partial | 材质分工半；防 F2「一律点彩」。 |
| C-M2-01 | `D:42`（§1-4）「**柔和明暗（光为触感服务）**：漫射侧光…无戏剧性光源；暗部为暖褐/灰绿、保留层次；全画以中调为骨架，无纯黑大块」 | `[归纳]`+`[研究]` | partial | 弱光源定义；`AM:27` 判 S1-4 partial（`[归纳]` 未实测），本片不升。 |
| C-M2-02 | `Q:83-88` 「c'est la substance même des objets, c'est l'air et la lumière que tu prends à la pointe de ton pinceau」（Q11 Diderot 1763） | `[史料]`(`[contemporary record]`) | supported | 光为物/触感服务的总纲；**fetch3 英文旁证**（Met「grind 'the very substance'… dip your brush in air and light」，`AR:64`）。 |
| C-M2-03 | `Q:134-139` 「un travail systématique de reflets… envelopper chaque chose de la teinte et de la lumière de tout ce qui l'avoisine」（Q18 Goncourt 1864） | `[研究]`(`[research]`) | supported | 反光网络 = 每物带邻物色光；`D:41`（§1-3）、`D:60`（§2-5）同引。 |
| C-M2-04 | `C:45`（§8.2-2）「镜面高光连通域为**宽软形**（圆度 ≤0.7 或长宽比 ≥2；σ ≥2px）…跨物反光 ≥2 处…禁止 1–3px 圆点系统」；`D:204` 同 | `[归纳]` | partial | 宽软反光带 + 跨物反光 ≥2；未像素实测。 |
| C-M2-05 | `C:46`（§8.2-3）「纯黑像素（L*≤5）占比 ≤0.5%；阴影色相**暖**（H 20–60° 或灰绿 60–120°…禁止 200–250° 冷蓝主导）；暗部保留层次」；`D:205` 同 | `[归纳]` | partial | 弱光源的暗部可判定化；未像素实测。 |
| C-M2-06 | `D:196`（§8.1）「定调三件套：P1 触感密度 **70%** + P2 反光网络 **65%** + P4 光质柔和 **60%**… 缺 P2 会退化成普通暗调静物，缺 P4 会滑向卡拉瓦乔式的戏剧光」；`D:218`（§8.3-1）「防默认模板把光压平为无方向平光」 | `[归纳]` | partial | 两半必须成对（F1/F3）；「弱 ≠ 无方向平光」。 |

---

<a id="db-source-line-46"></a>
## §B Cochin/Diderot 闭环 — 逐字证据（brief ②）

| claim_id | locator（file:line + 锚点子串） | 等级 | support | basis |
|---|---|---|---|---|
| C-LOOP-01 | `Q:11-16` Q1「On se sert des couleurs, reprit M. Chardin, mais on peint avec le sentiment.」+「reconnoissoit」「Avec quoy donc」（`[reported speech]`） | `[自述转记]` | supported（转录层，原档未回查） | 唯一确证第一人称名句，Cochin 致 Haillet 信 1780；**fetch1 逐字核**（`94105c40…87e3`，`AR:62` F1 / `AE:28`）；原档私人文书未回查（`D:275` §10-1、`AT:528`）。`D:121`（§5-1）、`D:75`（§3-2）同。 |
| C-LOOP-02 | `D:58`（§2-3）「反复重画，直到达到**色调的断裂（rupture de tons）**与最终的**魔法般的和谐（accord magique）**」；`D:76`（§3-3） | `[史料]`（Cochin 1780，经 [R27]/[R33]/[R22] 转录） | supported（转录层） | 层积的「慢工/反复」半；fetch1 旁证「repeignait… rupture de tons… accord magique」（`AR:62`）。 |
| C-LOOP-03 | `Q:83-88` Q11 Diderot《Salon de 1763》论《Le Bocal d'olives》「substance même des objets… air et lumière」 | `[史料]` | supported | 闭环 B 环；`AR:64` F3 英文旁证；`AE:30`。 |
| C-LOOP-04 | `Q:90-95` Q12「Approchez-vous, tout se brouille… Éloignez-vous, tout se crée」 | `[史料]` | supported（转录层） | 闭环 B′；法文逐字未独立 web 复取（`AM:130` 明示保持 supported-via-transcription）；fetch3 英文「dip your brush in air and light」旁证。 |
| C-LOOP-05 | `Q:97-102` Q13「Denis Diderot called Chardin 'the great magician'.」（NGL 2018 转述） | `[史料]`（转述） | supported | 与 A 环「accord magique」呼应的锚点；非 Diderot 原句。 |
| C-LOOP-06 | `Q:134-139` Q18 Goncourt 1864「travail systématique de reflets」 | `[研究]` | supported | 闭环 C 环；把并置色「联结」而不「混」。 |
| C-LOOP-07 | `Q:199-204` Q27 Met「never disguise the rough texture of paint」+ `Q:206-211` Q28 NGL「keeping objects slightly out of focus… extraordinary beauty」 | `[研究]` | supported | 闭环 D 环（现代馆方）；Q27 fetch3 逐字核、CC0/Open Access 权利基础同页（`AR:64`）。 |
| C-LOOP-08 | `AM:129-130`「The 'closed loop' is the cross-support between: (a) Cochin 1780… (b) Diderot 1763… (c) 19c Goncourt (Q18)… (d) 20c Met/NGL (Q27/Q28)… jointly ground §1-2/§1-3/§1-4… re-anchored to §8.2 rules」；`AR:33`（§2 第 1 点） | `[归纳]`（AUDIT 结论，本片复用） | supported | **闭环是证据环、不是画家自述链**：A 为转记、B/B′/B″ 为同时代、C/D 为后世研究。`G:88` A-92「语料 28 条（Cochin/Diderot 闭环）」命名来源。本片 `learning_path.md §2` 逐字表 + `how-to-think.md §0/D7/D8` 落地。 |

---

<a id="db-source-line-61"></a>
## §C 分母辨析：引文 37/37 vs 语料 28（brief ③）

| claim_id | locator（file:line + 锚点子串） | 等级 | support | basis |
|---|---|---|---|---|
| C-DEN-01 | `G:88` A-92「语料 **28** 条（Cochin/Diderot 闭环）… 图库 **17** 张全 PD/CC0（**卢浮宫 11**）… **引文 37/37**」 | `[史料]`（GOALS 记录） | supported | **同句并列多个不同口径数字**；AUDIT `AR:31-37`（§2）、`AE:33-37`（§3）判「hint conflates two different denominators」。 |
| C-DEN-02 | `IDX:74`「chardin.md \| **28** \| 3 \| 5 \| 11 \| 书信 + 转记（Cochin/Diderot 闭环）；[research] 12 条另列；**引文 37/37**」 | `[史料]`（索引记录） | supported | 「3\|5\|11」为折叠分组（archive+contemporary 合并），`AM:137` H-IDX / `AE:49` F2 记为措辞瑕疵（非阻塞）；与实测逐条类型 2/4/1/10/11=28 为解读差异非缺陷。 |
| C-DEN-03 | `Q:4`（图例）+ 本 lane `grep -c '^### ' Q` = **28**、`grep '^- 类型：'` = 28（self-written 2 / reported speech 4 / archive 1 / contemporary record 10 / research 11 = 28） | `[史料]`（语料实测） | supported | **语料分母 = 28**，本 lane 复跑；AUDIT `AR:41`（§3 28/28/28/28）、`AC:18` `quote_count=28`、`AE:14`（审者 recount =28）独立复跑一致。 |
| C-DEN-04 | `D:478`「=== 引文抽查（**37 条 vs 本机源文件**，归一化后逐字命中）===」；`D:479-515` 逐条 `HIT | …`；`D:516`「--- 37/37 ---」；`D:548`（自审 D）「引文复抽（归一化）: 37/37」 | `[史料]`（作者自审记录） | supported（**块存在**） | **37/37 = dossier 自审 C 归一化引文抽查**，对象 = 作者 `_scratch/chardin/` 本机源文件，不是 `_corpus` 条数。 |
| C-DEN-05 | `AR:34`（§2 第 2 点）「did **not** re-run the author's 37-fragment byte-match… recorded as an author-claim, not re-certified by this lane」；`AR:97`（§9.5）、`AE:33-37`（§3 VERIFIED）、`AT:548-550`（unresolved #5） | `[归纳]`（AUDIT/审者结论） | supported | 37/37 块**已核实存在但未重跑**（`_scratch` 不在只读仓库）→ **作者自审主张、非本 lane 重认证**；分母 28 为独立核实。本片 `learning_path.md §2 分母辨析表` 分栏携带。 |
| C-DEN-06 | `C:53`/`D:212` §8.2 阈值注 + `D:281` §10-7 → 「`[归纳]` 未对原作做像素测量（分母＝假想参考帧）」 | `[归纳]` | partial | 第四个「分母」（假想参考帧）单独标注，不与 28/37/17 混算；`AM:78-91` §8.2 S82-1..8 全 partial。 |

---

<a id="db-source-line-74"></a>
## §D 图像机构拆分 17 = Louvre 11 + Met 3 + NGL 3（brief ④）

| claim_id | locator（file:line + 锚点子串） | 等级 | support | basis |
|---|---|---|---|---|
| C-IMG-01 | `R:564-580` 恰 17 行 `\| \`chardin/…jpg\` \|`，本 lane `sed -n '564,580p'` 复核 | `[史料]`（馆藏记录） | supported | 17 张公开图逐行可数；`AR:35`（§2 第 3 点）、`AE:17`（审者「exactly 17 `chardin/…jpg` rows」）独立复跑。 |
| C-IMG-02 | `R:564-580` 机构列：「卢浮宫（INV …）」×11、「The Met（…）」×3、「NGL（NG…）」×3 | `[史料]` | supported | 拆分 **11/3/3 = 17**；`AC:59-65` `images_institution_split`、`AE:17`、`AR:77`（§7）一致；`G:88`「卢浮宫 11」一致。 |
| C-IMG-03 | `AR:77`（§7）「17/17 public images… Public domain 9 + Public domain（PD-Art）5 + CC0 1.0 2 + CC0 1.0（Met Open Access）1 = 17, unknown 0」；`AC:66-73` `images_license_labels` | `[史料]`（权利记录） | supported | AUDIT `rights_review.md` 逐张 verbatim 标签；本 lane 沿用、不声称目检像素（`image_seen=0`）。 |
| C-IMG-04 | `D:31`（§0）「图库 17 张，全 PD/CC0：卢浮宫 11 + Met 3 + NGL 3」；`AE:44`（§4）「private research-copy layer = 10 hi-res jpg + 2 PDF = 12 items; `images_public=17` unaffected」 | `[史料]` | supported | chardin **不是 private-layer 艺术家**；GOALS A-92「私有 12 件」vs manifest 私有行 `\| chardin \| 17 \| 10 \|` 由 `AE:44` 对账，记录不静默重置。 |

---

<a id="db-source-line-85"></a>
## §E §4 参数 / §8.2 规则 / 练习映射（全部 `[归纳]`、未实测）

| claim_id | locator（file:line + 锚点子串） | 等级 | support | basis |
|---|---|---|---|---|
| C-PARAM-01 | `D:105-110`（§4）/`C:59-64` P1 70% / P2 65% / P3 70% / P4 60% / P5 65% / P6 50%；`D:112`/`C:66`「P1/P2 定「是不是夏尔丹」…两条 ≥ 中档才成立」 | `[归纳]` | partial | 六参数 + 用法门；`AM:71-77` S4-P1..P6/S4-USAGE 全 partial；CE-1 边界反例见 §G。 |
| C-PARAM-02 | `D:203-210`（§8.2 八规则）/`C:44-51` 逐字一致；`D:212`/`C:53`「以上阈值为本项目 `[归纳]`，**未对原作做像素测量**」 | `[归纳]` | partial | 八规则；`AM:84-91` S82-1..8 全 partial。 |
| C-PARAM-03 | `D:198`（§8.1）「生成后自查三件事：① 反光是否跨物（≥2 处邻物色）？② 高光是否宽软（无 1–3px 点状系统）？③ 暗部是否有暖色与层次？」 | `[归纳]` | partial | `how-to-think.md D7` 收笔回检来源；`D:196` 定调三件套。 |
| C-PARAM-04 | `D:379-433`（§12 临摹/学习清单 10 件，各含「看什么 / 学什么 / 怎么练」）；`D:433`（组合练习建议 + 第 11/12 件粉彩/银杯扩展） | `[史料]`（作品信息）+ `[归纳]`（练习设计） | supported（作品信息）/ partial（练习） | `learning_path.md §2/§4` 三阶梯作品映射来源；练习为本项目设计、`01-AUDIT.md:273` 要求标「建议练习」。 |
| C-PARAM-05 | `01-AUDIT.md:269-273`（A-30 §8.1）「每位路径至少明确：前置知识、重点作品及来源、要观察的机制、具体练习、可观察结果、常见失败、下一步及使用边界… 练习效果尚未由人完成或评价时，明确为建议练习，不写『已证实学习收益』」；`01-AUDIT.md:308-310`（§8.4） | `[归纳]`（验收规范） | supported | 本片 8 节形状（`learning_path.md §1-§8`）逐项对应；`human_review=not_applicable`。 |

---

<a id="db-source-line-97"></a>
## §F 分工 / 冲突预检（`[归纳]`，conflicts.md 无 chardin 具名行）

| claim_id | locator（file:line + 锚点子串） | 等级 | support | basis |
|---|---|---|---|---|
| C-CONF-01 | `D:85-90`（§3.1 vs 维米尔「光学室内 vs 触觉静物」5 判据 + 边界注「≥2 轴联合成立，尤②③⑤」）；`D:91-96`（vs 塞尚「结构 vs 质感」5 判据 + N4 不可拆）；`D:97`（系统其余模块禁令） | `[归纳]` | partial | 两条写死分工；自审 B1/B2 WEAKENED→补「≥2 轴」注（`D:449-450`）；`AM:63-64` S3.1-V/C 均 partial。 |
| C-CONF-02 | `X:32`（C-01 阴影硬度）、`X:36`（C-05 笔触可见度）、`X:42`（C-11 高光计数）、`X:43`（C-12 色相面积预算）、`X:44`（C-13 阴影色相）；`C:53`/`D:212`/`C:75` 夏站位注 | `[归纳]` | supported（as record） | 五条按 **ID** 引用（card `C:69-75`、dossier `D:97,212`）；`AM:142` 确认 ID 全解析（X:32/36/42/43/44 + 详条 X:55/109/188/203/217）。 |
| C-CONF-03 | `X:305`（N1 反约束一致性）、`X:311`（N3 轴所有权表）、`X:314`（N4 可拆/不可拆）、`X:326`（N7 高光分类口径） | `[归纳]` | supported | 组合预检处置口径；C-11 按 N7 单列「反光带」类、不并入点状计数。 |
| C-CONF-04 | `C:67`（四条越界警报：「① 表面压平、高光点状、冷调蓝阴影、地砖网格 → 越界维米尔；② tache 方向族、多轮廓、蓝网、裸露画布 → 越界塞尚；③ 画外单光 + 近黑背景… → 越界卡拉瓦乔；④ 平涂无笔触、无高光 → 越界马蒂斯」） | `[归纳]` | partial | `mechanism_notes.md §4`、`how-to-think.md D8` 逐条守；规则层判定、非实验验证。 |
| C-CONF-05 | `AR:53-55`（§4 conflicts.md drift）「zero literal `chardin`/`夏尔丹` occurrences（`grep -c -i`=0）… C-11/C-12/C-13 detail sections carry stale absolute line locators for *other* artists」；`AM:140-147`（drift 专节）；`AT:538-540`（unresolved #3） | `[归纳]`（AUDIT 结论，本片复用） | supported | **pointer gap、非语义错误**；card/dossier 按 ID 引用稳健。修复归 CONFLICT lane 单独写权，本片只登记、不改仓库。 |

---

<a id="db-source-line-109"></a>
## §G 反例与 open（照实携带、不收口）

| claim_id | locator（file:line + 锚点子串） | 等级 | support | basis |
|---|---|---|---|---|
| C-CE-01 | `AR:71`（§6 CE-1）「A late pastel self-portrait (1771 *Autoportrait aux besicles*)… Under a literal reading of D:112… that autograph canonical work would be judged 'not Chardin' — a genuine boundary counterexample to the *operational* gate」；`AM:164`（CE-1）；`AT:543-545`（unresolved #4） | `[inference]`（AUDIT） | unverified（未渲染） | 操作门边界反例、非归属错误；dossier §1-10/§2-7/§10-7 已承认 P6 时期滑轨/阈值未实测。判别动作：粉彩肖像豁免或 E 系列像素测量；本片阶梯三以 open 注记携带。 |
| C-CE-02 | `AR:73`（§6 CE-2）「§8.2-1 forbids『统一方向角度族』(peak ≤35%)… but §2-7/Q (Jeffares) describes late pastel as『纯色平行笔触』… contradiction is avoided only by medium scoping, which D:203 does not state explicitly」；`AM:166`（CE-2） | `[inference]`（AUDIT） | unverified（未渲染） | 介质 scope 未显式声明；本片按介质分栏、不升级。 |
| C-CE-03 | `AT:527-551`（unresolved #1–#5）：原话原档未回查 / €24,381,400 Artcurial 未复取 / conflicts.md 无 chardin 行 + 数值 locator 陈旧 / §4·§8.2 阈值未实测 / 37/37 未重跑 | `[史料]`（治理记录） | supported | 五项 open 全部照实携带；`learning_path.md §7/§8`、`how-to-think.md D8`、`mechanism_notes.md §7` 一致登记、不收口、不改写仓库/审计产物。 |

---

<a id="db-source-line-119"></a>
## §H 依赖 / 治理 / 等级红线

| claim_id | locator（file:line + 锚点子串） | 等级 | support | basis |
|---|---|---|---|---|
| C-DEP-01 | `AT:6` `status=accepted`；`AT:499-525` `review.verdict=accepted` / `reviewer_actor_id=ReviewGateAUDIT-chardin(glm-5.3-flash)` ≠ `author_actor_id=AuditChardin` / 19 `reviewed_artifact_hashes`；`AE:54`「**accepted.**」 | `[史料]`（治理记录） | supported | 依赖为 **ACCEPTED**（review gate 已裁定）；`RESULT.md §0` 记「AUDIT 作者原始 status=submitted，审者接受后磁盘为 accepted」两态如实分栏。本片复用不重审。 |
| C-DEP-02 | `AR:47`（§4）「78 claim rows — supported 55 / partial 23 / conflict 0 / unverified 0」；`AE:13`（审者 recount 78/55/23 MATCH）；`AC:40-57` `claims_total=78` | `[史料]`（AUDIT 结论） | supported | 本片**不把 partial 升 supported、不改审计产物**；`AM:47` 记 partial 为 `[归纳]` 操作阈值 + Q2/Q3 转录层。 |
| C-DEP-03 | `AR:27`（§1）「`python … _extract.py --check` → checks=228 ok=228 fail=0… _extract.py sha observed `4afa31ec…af44d4`」；`AC:18-25` `extractor_check`；`AE:43` 复现 | `[史料]`（AUDIT 结论） | supported | 228/228 对**该版本抽取器字节**有效、§8.1b 排除（`card_has_81b=false`）；本片未重跑、不冒充本轮运行。 |
| C-GOV-01 | `00-GOAL.md:9`「How to Think 必须区分作者可核实的自述与研究者推断，不能编造作者心理」；`D:10`「凡涉及『他心里如何』的表述，一律按**操作规则**处理」；`Q:5`「夏尔丹无画论、无书信集、无日记」 | `[归纳]`（红线） | supported | 本片 `[推测]` 计数 = 0、零句「夏尔丹觉得/想要」；`how-to-think.md §0/§3`。 |
| C-GOV-02 | `D:5`（证据分级图例）、`Q:4`（corpus 类型图例）、`Q:213`（口径注「#1–#6 为『他的声音』…引用建议格式」） | `[史料]`（体例） | supported | 全片等级分栏依据；`[自述]` 仅 Q2/Q3 两条且转录层。 |
| C-GOV-03 | `C:1-81`（81 行模块卡，§8.1/§8.2/§4 与 dossier 逐字一致）；`D:1-559`（560 行 v2 档案）；本片 `receipt.json` 内部证据 2fa9cbf359024f65（未公开；来源记录由维护者保留）、`spawns_allowed=false`、`status=submitted`、`review=null` | `[史料]`/`[归纳]`（治理） | supported | 仓库只读、无 git、无子代理、无凭据；作者不自接受，独立审者由单独 review-gate 承担；本包无 bound LEARN-chardin contract（仅 `AUDIT-chardin.contract.json`），verify-receipt.py 走 schema-only 提前返回（与 LEARN-sargent/monet 同口径）。 |

---

<a id="db-source-line-132"></a>
## 覆盖自审（本 map 自检）

- **分母自洽**：语料 28（C-DEN-03）/ 自审 37/37（C-DEN-04/05）/ 图像 17=11+3+3（§D）/ 假想参考帧（C-DEN-06）四个分母分栏；GOALS `G:88` 与 INDEX `IDX:74` 的同句并列按 AUDIT+审者辨析（C-DEN-01/02），不混用。
- **逐字状态诚实**：Q1 fetch1 逐字、Q27 fetch3 逐字、Q11 英文 fetch3 旁证、Q12 法文未独立复取、原档未回查（C-LOOP-01/02/03/04、C-CE-03）——全部沿用 AUDIT 口径，不升一手。
- **等级纪律**：`§A/C/E/F` 的 `[归纳]` 阈值/练习全 `partial`，不升 supported；`§G` 反例 `unverified`（`[inference]` 未渲染）；`[推测]` 计数 = 0。
- **不重审 ACCEPTED**：AUDIT 的 105/105 定位、`raw/*` fetch、4/4 外部取证、19 产物 hash 本片一律复用（`C-DEP-01/02/03`），未重跑、未改写其产物。
- **练习效果**：全部为建议练习，`human_review=not_applicable`，无「已证实学习收益」（`C-PARAM-05`）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
