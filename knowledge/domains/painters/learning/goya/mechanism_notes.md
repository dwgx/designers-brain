<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-goya；原正文 SHA-256 `b4dae094dac69907103fa6fc5bf42ff86030d07207a44be89a1f7c03b0691f9a`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-goya — 机制笔记（mechanism_notes）

> 内容：§1 §4 六控制参数 → 练习映射 / §2 §8.2 八条可判定规则 → 练习与自查映射 / §3 核心机制两半（暗色底 + 强光主体）/ §4 冲突行与越界失败条件 / §5 诚实降级 / §6 brief 四项强调点专节。
> 底本：仓库只读 [goya.md](../../modules/goya.md) / [goya.md](../../dossiers/goya.md) / [goya.md](../../dossiers/_corpus/goya.md) @ f0089523 + 内部证据 17d8c3be34400a32（未公开；来源记录由维护者保留）（ACCEPTED）。复用 AUDIT 61 行 claim map 的 locator 纪律与 3 条 fetch 锚点，不重审、不重跑 fetch、不改其产物。
> 全部机制名与阈值为 `[归纳]`（本项目操作规则）或 `[inference]`（AUDIT 反例推得），**未对原作像素测量**（dossier `§8.2 尾注:L244`、`§10-6:L298`）；练习均为建议练习，不写「已证实学习收益」。

---

<a id="db-source-line-9"></a>
## 1. §4 六控制参数 → 练习映射

> 原表：`dossiers/goya.md:§4:L95–102`（与 `modules/goya.md:§4:L57–64` 逐字一致）。六参数档位描述全部 `[归纳]`。

| 参数 | 弱 20–30% / 中 50–60% / 强 80–95%（默认） | 练习映射 | 失败条件 |
|---|---|---|---|
| **P1 事件即时性/新闻构图** | 闭合场面全在画内 / 裁切 1 组、动作落前景 / 背身+信息出画外+动作压进前景 1/3（**70%**） | [learning_path.md](learning_path.md) 阶梯一练习 1（重排「施害者出画外」版） | 决定性信息全入画、动作止步、构图完整 → 新闻感消失（反例 2《卡洛斯四世一家》） |
| **P2 光源证据性/画内光源** | 平光漫射 / 单一画内光源局部照明 / 提灯成构图主角、光锥定亮区（**60%**，夜戏升 80–95%） | 阶梯一练习 2（§8.2-1 四项自查）+「白天版」对照 | 光源出画外+亮部只落脸/手/道具 → 越界卡拉瓦乔；单光源连续衰减照单脸 → 越界伦勃朗（`§4 分工注:L105`） |
| **P3 怪诞强度** | 轻微漫画化 / 兽化面具女巫傀儡 / 噩梦库全开且绑讽喻（**40%**，克制） | 阶梯二练习 5（当代版「XX 的沉睡」、黑底 2 色「吞噬」） | 怪脱离开讽喻对象、为恐怖而恐怖；题解误标 `[自述]` |
| **P4 面孔预算/匿名化** | 面孔清晰可数 / 部分可见 / 施害者 0 面孔、受害者 ≤2、其余剪影（**70%**） | 阶梯一练习 1 + 阶梯三 A/B（vs 伦勃朗单脸心理） | 每张脸都画五官、给施害者正脸 → 匿名化失效 |
| **P5 黑度/色域收窄** | 洛可可亮色 / 土色低饱和+白黑两级 / 近单色暗调黑土白（**65%**） | 阶梯一练习 3（§8.2-5/6 HSV/高光自查） | 补光、多光源、甜色、镜面高光/清漆反光、喷绘渐变 |
| **P6 序列帧数（工作流参数）** | 单幅 1 帧 / 小系列 3–8 帧 / 大系列 ≥22 帧+题刻（**1**） | 阶梯二练习 4（3 灰阶结构图 + ≤4 词题刻 + 扩成 3–8 帧） | 把「82 帧」写成唯一真值（`§9 CC-4:L286` 自记 80/82/85 口径并存） |

> 用法（`§4 用法:L104`）：**P1/P2 定「是不是戈雅」（两条同时 ≥中档才成立）**；P3/P5 定「时期滑轨」；P4 定叙事；P6 不进画面重叠计算（`expansion.md` §4.3 规则 5 归工作流参数）。**边界**：此 gate 被 AUDIT `counterexample.md` 两条 `[inference]` 反例证明是时期/子类型特定，非通用风格测试（见 §5）。

---

<a id="db-source-line-26"></a>
## 2. §8.2 八条可判定规则 → 自查/练习映射

> 原表：`dossiers/goya.md:§8.2:L235–242`（与 `modules/goya.md:L44–51` 逐字一致）。八条阈值全部 `[归纳]`、未像素实测。

| # | 规则（可判定量） | 自查手段（原文） | 对应练习 | brief / 分工关联 |
|---|---|---|---|---|
| 1 | **提灯规则**：画内可见光源数 ∈[1,2]、光源在下 1/3×中央 1/3、亮区重心（前 10% 像素质心）落受害者包围盒、施害者组平均亮度 ≤全帧 40% | 亮度统计 + 包围盒 | 阶梯一练 2 | **A-23 光源数实测判据**；C-01/C-11；§3.1 分工「戈雅≥1/卡=0」 |
| 2 | **出画外规则**：主事件元素 ≥1 组裁切/背身；即时动作在下 1/3 前景带 | 姿态分类 + 空间排序 | 阶梯一练 1 | Met [R1]（AUDIT 记 429 → partial） |
| 3 | **面孔预算**：施害者面孔=0、受害者可辨面孔 ≤2、其余剪影 | 人脸检测计数 | 阶梯一练 1 / 阶梯三 vs 伦勃朗 | 分工 vs 伦勃朗（类型化群脸 vs 单脸心理） |
| 4 | **队列时间性**：受害者 ≥3 人、已死/濒死/将死 ≥两态 | 姿态分类 + 空间排序 | 阶梯一练 1 | R14「continuous procession」 |
| 5 | **色彩预算**：S≥0.6 面积 ≤3%；黑土色(H20–50,S≤0.4,V≤0.5) ≥60%；白高光连通域 ≤5 且须与「衬衫/尸布/刀锋/纸」相交；红仅在伤口/血 | HSV 掩膜 + 连通域 | 阶梯一练 3 | C-12；**暗色底**半 |
| 6 | **表面规则**：无镜面高光（亮度>0.95 且面积>0.5% 的斑=0）；哑光砂质均匀高频 | 高光检测 + 高频能量图 | 阶梯一练 3 | C-05（哑光砂质 vs 柔边渐变/笔触情绪场） |
| 7 | **版画帧附加**：交叉排线交叉点密度≈0（线方向族 ≤2 不交叉）；≥1 均匀飞尘区（≥10%、内方差 ≤5/255）；≥1 刮亮点（≥2 灰阶）；题刻 ≤1 行在下缘外 | 方向场分析 + 区域方差 | 阶梯二练 4 | C-07（vs 丢勒/北斋）；题刻制 |
| 8 | **怪诞帧附加**：非人/半人 ≥1 且与讽喻对象同框；恐惧面容 ≥1 | 对象检测 + 面容关键点 | 阶梯二练 5 | P3；Caprichos 43 / 黑画 |

> 第 1–3 条与 §3.1 分工判据同轴（`§8.2 尾注:L244`）。**组合实验时以本节自查表为准**——但本片未重跑任何组合实验，不声称 C-01 等「experimentally validated」。

---

<a id="db-source-line-45"></a>
## 3. 核心机制两半（brief 强调①：暗色底 + 强光主体）

「暗色底 + 强光主体」是本项目 `[归纳]` 的**机制标签**（档案/语料未用此二词），必须拆成可回源的操作半，成对使用：

| 半 | 组成 | 回源 locator | 等级 |
|---|---|---|---|
| **可见输出半：暗色底** | 土黄/棕/黑为底、白只作闪光、红只作血、哑光砂质无镜面 | `§1-6:L37`（R4 逐字）、`§1-7:L38`（R4 逐字）、`§8.2-5:L239`、`§8.2-6:L240` | `[研究]`（现象）+ `[归纳]`（阈值） |
| **不可见前提半：画内光源 + 强光主体** | 提灯/火把在画内可指认、置于两组之间地上；光只照受害者组、施害者沉阴影；光为「证据」非「神启」 | `§1-1:L32`、`§2-7:L55`、`§3.1:L79–80`、`§8.2-1:L235`、`modules/goya.md:L9/L44` | `[史料]`/`[研究]`（现象）+ `[归纳]`（判据数值） |

- **「画内光源数」是 A-23 唯一可实测判据轴**：§3.1（`L80`）「戈雅 ≥1（提灯型）／卡拉瓦乔 = 0」；§8.2-1 把它量化成四项自查（∈[1,2]、下 1/3×中央 1/3、亮区重心、≤40%）。R4 逐字（AUDIT `risk_fetch.md`）："A square lantern situated on the ground between the two groups throws a dramatic light on the scene. The brightest illumination falls on the huddled victims to the left"。
- **必须成对**：只有暗底无「可指认画内源 + 光落受害者群」= 普通暗调画；只有强光无暗色底/哑光约束 = 滑向卡拉瓦乔或舞台光。**即兴的亮部是可见输出，画内光源位置是不可见前提**。
- **诚实降级**：所有 `[归纳]` 数值分母＝假想参考帧、未像素实测；两条 `[inference]` 反例（AUDIT `counterexample.md`）说明它是**夜戏/处决子类型**签名，非全 oeuvre 必要条件。

---

<a id="db-source-line-60"></a>
## 4. 冲突行与越界失败条件

- card「冲突注记」（`modules/goya.md:L69–79`）列出的 goya 相关轴：`C-01`（×卡拉瓦乔，硬阴影/光源数）、`C-11`（亮部对象 群体 vs 脸手道具）、`C-12`（色相面积预算）、分工 vs 伦勃朗（面孔预算）、`C-05`（×达·芬奇/梵高，表面）、`C-07`（×丢勒/北斋，版画表面）、`C-17`（×米开朗基罗·负空间组，组合预检）。dossier `§3.1-e:L89` 指向 C-01/C-05/C-07/C-17。
- **conflicts 口径事实（AUDIT `RESULT.md §5` / `conflicts_locator_drift.md`）**：`grep -n -i 'goya|戈雅' conflicts.md` **零命中**；goya 的 C 行只来自 card 冲突注记，这些 C 行「涉及模块」不含 goya（goya 是后补引用方）；§4 near-miss 11 行无 goya 行，最近的是 #11（L357）。8 处被引用文件行号漂移（caravaggio/vermeer/hokusai）为**报告，不修**。
- **越界失败（`§4 分工注:L105`，`[归纳]` 判据）**：P2 弱/中 + 单光源连续衰减照单张脸 → 伦勃朗；P2 强 + 光源出画外、亮部只落脸/手/道具 → 卡拉瓦乔。此为**规则层判定，非实验验证**。
- **组合前**：按 `conflicts.md` C-01/C-11/C-12 预检（`modules/goya.md:§8.1 中文说明 L231`）；夜戏硬边光锥需按 C-01 句式改写（显式给出提灯半影宽度，`§8.3 L250`）。

---

<a id="db-source-line-69"></a>
## 5. 诚实降级（不静默升级）

| 项 | 事实 | 本片口径 |
|---|---|---|
| §4/§8.2 阈值 | `[归纳]`、未像素实测（分母＝假想参考帧，`L244`/`L298`） | 练习自查结果 ≠ 原作测量；不升 supported |
| 两条反例 | AUDIT `counterexample.md` 标 `[inference]` | 记为 gate 语义边界，非「已验证实验」、非画家意图断言 |
| 转记 | corpus #8 Brugada、#9/#10 Matheron、dossier 自审 B-2 降级「三导师」 | 标 `[reported speech]`，不冒充 `[自述]` |
| 题解归属 | corpus #5「理性沉睡」帕尔多手稿作者存疑，自审 B-3 降级 | 标 `[reported speech]` |
| 外部直读 | Prado [R10] 403、Met [R1] 429（AUDIT `risk_fetch.md`/dossier §9） | 用 R4/R14/R3 Wikipedia 同源描述交叉，不冒充直读馆方页 |
| 图像与许可 | 9 图 `image_seen=0`，许可页未逐站复核 | 只到「manifest 字段 + 文件字节存在」 |
| 语料 | 西语原信 / Matheron 1858 / Prideaux 1909 原书未直读 | 英译转引标 partial/unverified |
| 帧数 | 80/82/85 口径并存（`§9 CC-4:L286`） | 按上下文注明，不取唯一真值 |
| 练习 | 全部建议练习、`human_review=not_applicable` | 不写「已证实学习收益」 |

---

<a id="db-source-line-85"></a>
## 6. brief 四项强调点专节（逐一落地）

<a id="db-source-line-87"></a>
### ① 暗色底 + 强光主体机制（画内光源数实测判据）
见 §3（两半拆解）+ §1 P2 行 + §2 第 1/5/6 条 + `learning_path.md §3.1` + [how-to-think.md](how-to-think.md) D3/D4 + `claim_evidence_map.md §B`。**结论**：判据 =「画内可见光源数 ∈[1,2]（分工轴：戈雅≥1 / 卡拉瓦乔=0）+ 亮区重心落受害者包围盒 + 施害者 ≤全帧 40% + 暗色底/哑光约束」；R4 逐字支撑现象部分，`[归纳]` 数值未实测；两条 `[inference]` 反例限定为夜戏/处决子类型签名。

<a id="db-source-line-90"></a>
### ② A-23 写死 one-sided（caravaggio/rembrandt 零 reciprocal）作为 known-open 携带
`learning_path.md §7` + [how-to-think.md](how-to-think.md) D8 + `RESULT.md §3` + `claim_evidence_map.md §C` 四文件一致。**结论**：`caravaggio.md` / `rembrandt.md` 全文 `grep -i 'goya|戈雅'` **零命中**；`conflicts.md` 亦零命中；`hogarth.md §3.1` 明记「goya.md 无对侧条款……本档为唯一写死正本」。AUDIT claim map `S3.1-a`（`L35`）/`S3.1-b`（`L36`）均判 **partial**、`RESULT.md §5` 登记为适用边界、`conflicts_locator_drift.md §4` 记录、审者 `review-evidence.md §9` 确认。**「画内光源数」两侧数值各自成立且可实测，但「写死」是单向落盘，不是双向互引**。本片 5 文件一致作为 **open 项携带：不收口、不补对侧互引、不改仓库/审计产物、不升级为「已完成双向写死」**；收口路径交对应 dossier 写手 / CONFLICT·RULE lane。

<a id="db-source-line-93"></a>
### ③ R4/R14/R3 fetch 锚点作为已接受证据（accepted evidence）
`learning_path.md §2/§8` + `RESULT.md §0/§2` + `claim_evidence_map.md §D`。**结论**：AUDIT 3 次外网 fetch 全部 HTTP 200、逐字命中、sha256 入 `raw/risk_fetch_hashes.json` 与 `risk_fetch.md`：
- **R4** `The_Third_of_May_1808` — 398502 B — `f8f2e10a1e69369a85dbc4a4085f344071f456955f9f9d340b28899271d932f0`（提灯/背身/光落受害者/土色调/哑光砂质，A-23 核心）；
- **R14** `The_Disasters_of_War` — 409100 B — `35f0ed8aa3aa5ba3d5ba5e4ab842129602056baa93a79df2f1070ea16d016bde`（82 帧/1810–20/1863 出版/三段/Yo lo vi）；
- **R3** `Francisco_Goya` — 540157 B — `7f5dc028288d56674d778c3adbb9f886009116d26a114ec0440caa053fd6d34c`（「旧大师最后一位、现代人第一位」+ 生平）。
本片**作为 ACCEPTED 审计的已接受证据复用**：不重访 URL、不重算字节、不冒充本片自己 fetch；并同带 AUDIT 诚实限制（Prado 403 / Met 429 / 西语原信与原书未直读）。

<a id="db-source-line-100"></a>
### ④ rights drift 4CC0+5PD vs 汇总 3+6 携带
`learning_path.md §2/§6/§8` + [how-to-think.md](how-to-think.md) D8 + `RESULT.md §3` + `claim_evidence_map.md §E`。**结论**：逐行权利标签实为 **4 CC0（Met Open Access：Sleep of Reason / Yo lo vi / Manuel Osorio / Tauromaquia 18）+ 5 PD（Third of May / Saturn / Family of Charles IV / The Dog / Witches' Flight）= 9**；而 `_images/goya/MANIFEST.md` 头部、dossier `§10-9:L301`、GOALS A-23（`ops/GOALS.md:L37`）三处汇总写 **Met CC0×3 + Commons PD×6（3+6）**。AUDIT `rights_review.md` / `conflicts_locator_drift.md §3` / 审者 §9 均确认此漂移并采用逐行标签（逐对象权利记录）。本片**照实携带、不修仓库、不替仓库选定真值**；核 wave13 计数口径交 CONFLICT/RULE/IndexMerge lane。

---

<a id="db-source-line-105"></a>
## 7. 一句话收尾

「戈雅学习包 = 用 §4 六参数 + §8.2 八规则把『暗色底 + 强光主体（画内可指认光源 ≥1、只照受害者群）』做成可自查的创作决策序；其光源数判据是 A-23 唯一实测轴，但 gate 为夜戏/处决子类型签名、且『写死』单向；R4/R14/R3 三条 fetch 锚点作为 ACCEPTED 证据复用，权利 4+5 vs 3+6 漂移与其余 open 项一律携带不收口。」全部为建议练习 `[归纳]`，作者不自接受。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
