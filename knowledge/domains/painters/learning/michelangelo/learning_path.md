<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-michelangelo；原正文 SHA-256 `9d8160d322c8177fef74e983edde0c373c41992ec87d5371071cd75a687d683e`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# learning_path — LEARN-michelangelo（A-30 单画家学习路径）

- **task_id**: `LEARN-michelangelo` · **lane**: `learning` · **artist**: `michelangelo`
- **goal_id**: `Designers-Brain-Upgrade-20261115` · **baseline_id**: `DB-20261115-baseline`
- **依赖**: `AUDIT-michelangelo`（ACCEPTED；本轮不重审，复用其 locator 纪律）· **repo（只读）**: 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22`
- **形状**（01-AUDIT.md §8.1 / 00-GOAL §8.1 之 A-30）：前置知识 → 重点作品及来源 → 要观察的机制 → 具体练习（≥3 阶梯）→ 可观察结果 → 常见失败 → 下一步 → 使用边界。
- **证据规则**：每条事实带 `file:line` locator；等级沿用来源标注 `[自述]/[自述·转引]/[史料]/[研究]/[归纳]/[实测]`，研究者推断显式标 `[归纳]/[推测]` 或 `[INFERENCE]`；**所有练习一律为「建议练习」，不写「已证实学习收益」**（01-AUDIT.md:273）。
- **本轮点名强调**：硬边阴影 `≤0.6% 短边`（凿出边缘）、构图密度 `≥55%` + 空白 `≤15%`、浮雕强度，及冲突 C-01/C-02/C-17/C-18；练习阶梯 = 凿边人体研究 → 满构图掩膜 → 形体塑造 vs 平涂分区（C-18 拆分）。

---

<a id="db-source-line-12"></a>
## 1. 前置知识

先具备以下四项，再进入本路径；否则机制观察会落空。每项均为可回源的知识，不是新造材料。

| # | 前置知识 | 内容 | locator（等级） |
|---|---|---|---|
| P1 | 减法雕塑观 | 雕刻 = `per forza di levare`（靠「减」去多余），非「加」；一块大理石里已「圈住」概念，手只执行 | `_corpus/michelangelo.md:17-23`（[self-written] 致 Varchi 信）、`:25-39`（Rime 151/152）；`dossiers/michelangelo.md:43-45`（§2-6/7 `[自述]`）、`:54-56`（§3-2/3 `[自述]`）|
| P2 | 浮雕是绘画的裁判 | 「画越接近浮雕越被看好」——形体靠明暗切出、像被「凿」出来 | `_corpus/michelangelo.md:9-15`（[self-written]）、`dossiers/michelangelo.md:56`（§3-4 `[自述]`）、`:30`（§1-8 `[归纳]`）|
| P3 | 人体为叙事载体 | 肌肉分明的裸体主导画面；terribilità（威压感）先于优美；扭转体（肩—髋反扭、S 形脊柱）| `dossiers/michelangelo.md:23-29`（§1-1/2/3/6 `[研究]`）；`modules/michelangelo.md:9-13`（浓缩 5 条）|
| P4 | 量化语言（§8.2 / §4） | 五控制参数（肌肉夸张 70% / 扭转角 50% / 浮雕强度 65% / 构图密度 60% / 未完成度 15%）与 7 条可判定规则 | `dossiers/michelangelo.md:62-72`（§4）、`:170-180`（§8.2）；`modules/michelangelo.md:79-95`（原样）|

> 交叉参照：卡/档案/语料三处 §4·§8.2·§8.1 逐字一致（AUDIT-michelangelo `RESULT.md` §1.1 INP-07，复用 BASELINE-P1 `raw/extract-check.out` L2）。本卡 HAS §8.1b（`modules/michelangelo.md:39`），但 E4 纯风格迁移仍 `[UNVERIFIED]`（AUDIT `RESULT.md` §0 能力边界）。

---

<a id="db-source-line-27"></a>
## 2. 重点作品及来源（引用现有记录，不重造生平）

沿用档案 §0 关键作品 + §12 临摹清单 + §9 来源表 + §11.10 来源 S 编号。**作品年份/馆藏/权利沿用现有记录**（01-AUDIT.md:273）；外部 URL 本轮未联网复核（AUDIT `coverage_manifest.json` read_scope_note `unverified`）。

| 作品 | 年份 / 馆藏 | 主要观察项 | 来源（locator / 来源号）| 权利 |
|---|---|---|---|---|
| 《大卫》David | 1501–1504，佛罗伦萨学院美术馆（领主广场为复制品）| 承重/自由腿 contrapposto、肩—髋反向扭转、未完成凿痕 | `dossiers/michelangelo.md:13`（§0 `[来源14]`）、`:340-343`（§12.2）；来源 14 = `dossiers/michelangelo.md:204` en.wikipedia《Michelangelo》| 图 `david.jpg` = CC BY-SA 4.0（摄影 Livioandronico2013），**非 PD**（AUDIT `RESULT.md` §3；`_images/manifest.md` L24）|
| 西斯廷天顶 | 1508–1512，梵蒂冈博物馆（1512-10-31 揭幕）| ignudi 极限扭转、下排剧烈缩短（仰视）、九格叙事、giornata 接缝 | `dossiers/michelangelo.md:14`（§0 `[来源10][来源11]`）、`:350-353`（§12.4）；来源 10/11 = `:199-200` 梵蒂冈官方页；正确年表 `:281`（§11.9）| 图 `creation_of_adam.jpg` = Public domain（`manifest.md` L23）|
| 《最后的审判》 | 1536–1541，西斯廷祭坛墙，梵蒂冈 | 满墙人群绕中心涡旋、分组环绕、中心轴 | `dossiers/michelangelo.md:15`（§0 `[来源12]`）、`:365-368`（§12.7）；来源 12 = `:201` | — |
| 《圣殇》Pietà | 1497 受托、约 1500，圣彼得大教堂 | 金字塔闭合、衣褶深谷 vs 软体、克制哀恸 | `dossiers/michelangelo.md:16`（§0 `[来源14]`）、`:335-338`（§12.1）| 图 `pieta.jpg` = CC0（摄影 Jebulon）（`manifest.md` L25）|
| 《圣家族》Doni Tondo | 1503–04，乌菲齐 | 圆框螺旋链、背景裸体群像的浮雕感、平涂 vs 强明暗对照 | `dossiers/michelangelo.md:345-348`（§12.3）| — |
| 《摩西》Moses | 1513–15，圣彼得镣铐教堂 | 坐姿「将起未起」、衣不遮体 | `dossiers/michelangelo.md:355-358`（§12.5）| — |
| 《垂死的奴隶》《被缚的奴隶》 | 1513–16，卢浮宫 | 粗凿与精刻并存、用体块边界读形 | `dossiers/michelangelo.md:17`（§0）、`:360-363`（§12.6）| — |
| 《隆达尼尼圣殇》 | 1550s–64，米兰斯福尔扎城堡 | 晚期「减法到底」、母子垂直叠合、反复改刻层痕 | `dossiers/michelangelo.md:370-373`（§12.8）| — |

> **历史项保护**：「1509 揭幕」旧说已被记录为 OVERTURNED，当前零处仍断言（AUDIT `claim_evidence_map.md:11-17` OVT-01..07）；1509 在档案中还有合法的不同事件（1509-01-27 致父信，语料条目 16），不得误删。本路径采用 **1512-10-31 揭幕**（`dossiers/michelangelo.md:281`）。

---

<a id="db-source-line-46"></a>
## 3. 要观察的机制（本轮点名为核心）

把视觉语言翻译成「可逐帧自查」的量（§8.2 口径）。这些是**项目操作规则 `[归纳]`，可被 A-12 实验推翻**（`conflicts.md:10-26` §0）。

| M | 机制 | 可判定阈值 | locator |
|---|---|---|---|
| **M1** | **硬边阴影（凿出边缘）** | 形体转折处明暗过渡带 **≤ 画面短边的 0.6%**，即「凿出来」的边缘；1920 宽下 ≤11.5 px | `dossiers/michelangelo.md:176`（§8.2-3）；`modules/michelangelo.md:81`（原样）；`conflicts.md:33`（C-02 表）、`:71-83`（C-02 逐条）|
| **M2** | **构图密度 + 负空间** | 主体人群占画面 **≥55%**；连续空白背景区域 **≤ 画面 15%** | `dossiers/michelangelo.md:177`（§8.2-4）；`modules/michelangelo.md:82`；`conflicts.md:48`（C-17 表）、`:272-283`（C-17 逐条）|
| **M3** | **浮雕强度（塑形 vs 平涂）** | 强档「形体像从墙面『凿出』、硬边投影」，默认 **65%**；由强明暗建模而非渐变塑造体积 | `dossiers/michelangelo.md:68`（§4 浮雕强度）；`modules/michelangelo.md:93`；`conflicts.md:49`（C-18 表）、`:285-296`（C-18 逐条）|
| M4 | 扭转检测 | 主人物肩—髋投影夹角 ≥30°（强档 45–70°），≥60% 人物达标 | `dossiers/michelangelo.md:175`（§8.2-2）；`modules/michelangelo.md:80` |
| M5 | 剪影可读性 | 缩到 25% 后主要人物轮廓可辨认，轮廓断裂 ≤2 处 | `dossiers/michelangelo.md:178`（§8.2-5）；`modules/michelangelo.md:83` |
| M6 | 限色 / 饱和度 | 全帧平均饱和度 ≤0.5；强调色（S>0.6）同屏 ≤2；主色限肉色/土黄/暗绿/青蓝四族 | `dossiers/michelangelo.md:179`（§8.2-6）；`modules/michelangelo.md:84` |

**机制之间的耦合**（`[归纳]`，来自 §4 使用建议）：把扭转角、构图密度、浮雕强度同时调高会「快速吃掉对方的柔和笔触」——M1/M2/M3 是一组彼此加强的「凿出 + 填满」操作，不是三个独立旋钮（`dossiers/michelangelo.md:72`；`modules/michelangelo.md:97`）。

---

<a id="db-source-line-63"></a>
## 4. 具体练习（建议练习 · 三级阶梯）

> **全部为「建议练习」（suggested exercises），练习效果尚未由人完成或评价，本轮不宣称任何「已证实学习收益」**（01-AUDIT.md:273；03-RESEARCH-AGENDA.md:125）。每级给「操作 / 可判定检查 / 关联机制」，并复用 §12 既有练习骨架。练习后按 §12 通用建议记录五参数取值与自评（达标/接近/不达标）（`dossiers/michelangelo.md:333`）。

<a id="db-source-line-67"></a>
### 阶梯 1 — 凿边人体研究（chiseled-edge figure studies）｜主攻 M1 + M3

- **操作**（建议）：
  1. 取《大卫》或天顶 ignudi 的单个人体照片，画其外轮廓剪影（不画内部），检验剪影仍可读（接 M5，§12.1-① `dossiers/michelangelo.md:338`）。
  2. 用炭笔/数字笔把一处「受光面→阴影面」的转折画成两版：A = 柔边渐变，B = 硬边过渡。用取色/剖面量过渡带宽度，令 B ≤ 画面短边的 0.6%（M1）。
  3. 同组人物画「平涂 vs 强明暗」两版，对照 §4 浮雕强度弱/强两档（§12.3-② `dossiers/michelangelo.md:348`）。
- **可判定检查**：过渡带宽度（px / 画面短边）；B 版是否出现「硬边投影」而非软阴影；剪影缩到 25% 是否仍成立。
- **关联**：M1（`dossiers/michelangelo.md:176`）、M3（`:68`）、M5（`:178`）；自述依据 P2（`_corpus/michelangelo.md:9-15`）。

<a id="db-source-line-76"></a>
### 阶梯 2 — 满构图掩膜（crowded-composition masking）｜主攻 M2

- **操作**（建议）：
  1. 画一张 12 人绕 1 中心的「微型审判」构图（§12.7-② `dossiers/michelangelo.md:368`），先只画剪影色块。
  2. 对成品做二值化「主体掩膜」：统计主体占画面面积，令 **≥55%**；再统计最大的**连续**空白背景连通域，令 **≤15%**（M2）。
  3. 裁 6 个局部各标「运动方向箭头」，检查是否指向中心轴（§12.7-① `dossiers/michelangelo.md:368`）；做一张 3×3 九格叙事板验证「动作接力」（§12.4-② `dossiers/michelangelo.md:353`）。
- **可判定检查**：主体面积比 ≥55%；最大连续空白连通域 ≤15%；箭头指向一致性；缩到 25% 后轮廓断裂 ≤2 处（M5）。
- **关联**：M2（`dossiers/michelangelo.md:177`）、M4（`:175`）、M5（`:178`）。
- **口径提醒**：此处的「空白」= 无内容区域；不要与北斋/马蒂斯的「留白」（低信息密度、可含平涂色块）混算——见 C-17 定义对齐（`conflicts.md:272-283`，尤其「定义对齐（必须写进卡）」条）。

<a id="db-source-line-86"></a>
### 阶梯 3 — 形体塑造 vs 平涂背景分区（form-casting vs flat-background split，C-18 partition）｜主攻 M3 + 四条冲突的落地

- **操作**（建议）：
  1. 用阶梯 2 的满构图作底，显式写一张**「主体掩膜 / 背景掩膜」分区表**（C-18 解法 1，`conflicts.md:294`）：主体人物 = 米开朗基罗式建模（允许明暗与硬边投影）；背景/装饰面 = 平涂（ΔE≤6 占比 ≥85%、无投影）。
  2. 按掩膜**分区判分**：人物区套 M1（≤0.6% 短边）+ M3（浮雕强度），背景区套平涂判据（毕加索 §8.2-6 / 马蒂斯 §8.2-2，见 `conflicts.md:285-296`）。
  3. 走一遍四条冲突的自查：C-01 把「别做成：硬阴影」反约束整条改写为显式半影宽度声明（N5 `conflicts.md:317-320`）；C-02 单主轴归主模块 / 写死分区表（N3 `conflicts.md:311-312`）；C-17 先做「空白 vs 留白」定义对齐；C-18 按上面分区表拆分。
- **可判定检查**：分区表是否写死 + 掩膜定义；主体塑造方式覆盖 ≥70% 画面面积（C-18 比例条 `conflicts.md:296`）；冲突轴上是否只保留一行（N9 `conflicts.md:332-333`）。
- **关联**：C-01（`conflicts.md:55-69`）、C-02（`:71-83`）、C-17（`:272-283`）、C-18（`:285-296`）；§3 N1/N3/N4/N5/N9（`conflicts.md:300-339`）；卡 §冲突注记（`modules/michelangelo.md:99-107`）。

> 阶梯递进关系（本路径 `[归纳]`）：1 练单体的「凿出边缘」，2 练多体的「填满 + 不留白」，3 练把 1 的浮雕语言与平涂系模块在同一帧共存的分区纪律。§12 的 8 件作品练习（`dossiers/michelangelo.md:335-373`）作为每一级的可替换观察素材，不额外新造。

---

<a id="db-source-line-99"></a>
## 5. 可观察结果

完成阶梯后应能**在产出上量到**（不是「感觉像」，也不是学习成效结论）：

| # | 可观察结果 | 量法 / 阈值 | locator |
|---|---|---|---|
| R1 | 明暗转折带是「刀切」而非「云雾」 | 过渡带 ≤ 短边 0.6%；1920 宽 ≤11.5 px | `dossiers/michelangelo.md:176`；`conflicts.md:71-83`（C-02 后果段给出 ≥28.8px vs ≤11.5px 对照）|
| R2 | 主体「被凿出」的浮雕感 | 强明暗建模 + 硬边投影，浮雕强度强档 65% | `dossiers/michelangelo.md:68`；`modules/michelangelo.md:93` |
| R3 | 满构图、少连续空白 | 主体 ≥55%；最大连续空白 ≤15% | `dossiers/michelangelo.md:177`；`modules/michelangelo.md:82` |
| R4 | 缩略仍可读 | 25% 尺寸剪影可辨、断裂 ≤2 处 | `dossiers/michelangelo.md:178` |
| R5 | 扭转与限色达标 | 肩—髋夹角 ≥30°、≥60% 人物达标；平均饱和度 ≤0.5、强调色 ≤2 | `dossiers/michelangelo.md:175,179` |
| R6 | 组合时不出现双标准 | 冲突轴自查表只保留持有者一行；分区表写死 | `conflicts.md:311-312`（N3）、`:332-333`（N9）|

> 这些是**产出物的可判定属性**，均来自 §8.2 / §4 / conflicts 的既有规则；[INFERENCE] 由上述规则派生为「练习应瞄准的目标」，**不是**对学习者能力或学习收益的测量。

---

<a id="db-source-line-116"></a>
## 6. 常见失败（反例）

| # | 失败形态 | 触发原因 | 判据 / 修正 | locator |
|---|---|---|---|---|
| F1 | 软边 / sfumato 吃掉硬边阴影 | 把达·芬奇式柔过渡或默认软光一起套用 | 过渡带 >0.6% 短边即失败；按 C-02 轴所有权归主模块或分区 | `conflicts.md:71-83`（C-02）；`dossiers/michelangelo.md:168`（§8.1 中文说明「sfumato 会吃掉硬边阴影」）|
| F2 | 「别做成：硬阴影」字面禁令误伤 | Lane B 模板反约束未改写 | C-01：把禁令改写为「显式半影宽度声明」，否则产出退回柔和自然光 | `conflicts.md:55-69`（C-01 后果/解法）、`:331`（N5 改写句式）|
| F3 | 折中成中间值，两边都不像 | 同时满足 ≥1.5% 与 ≤0.6% 的空交集 | 1920 宽下约 20px 的折中两边判分都不过；禁止同帧双标准 | `conflicts.md:71-83`（C-02 后果）；`dossiers/michelangelo.md:72`（天然互斥 70/30）|
| F4 | 空场过大（留白过多） | 把北斋/马蒂斯负空间预算直接套用 | 连续空白 >15% 即违反 M2；C-17 须先做定义对齐（空白≠留白）| `conflicts.md:272-283`（C-17）；`dossiers/michelangelo.md:177` |
| F5 | 主体被压平 / 平涂与浮雕同帧打架 | 未做主体—背景分区 | C-18：主体被凿出违反平涂判据、被压平违反浮雕规则；用分区表 + 掩膜拆分 | `conflicts.md:285-296`（C-18 后果/解法）|
| F6 | 量纲误判（近失 #7） | 把「物体边缘过渡带」与「形体转折明暗带」混测 | 二者量纲不同（≥2px vs ≤0.6% 短边），卡内须写清测量对象 | `conflicts.md:353`（§4 near-miss #7 行）；卡 §冲突注记 `modules/michelangelo.md:107` |
| F7 | 把「未完成面」误当刻意 non-finito 美学 | 从作品外观倒推作者心理 | 档案明注：粗凿是历史状态，不等于他刻意主张的美学 | `dossiers/michelangelo.md:32`（§1-10）；[how-to-think.md](how-to-think.md) §自述/归纳分离 |
| F8 | 宣称「已证实学习收益」 | 把建议练习当成实验结论 | 本轮练习均为建议、未经人评；E4 / A-12 实验未复现 | `01-AUDIT.md:273`；AUDIT `RESULT.md` §0 能力边界 `[UNVERIFIED]` |

---

<a id="db-source-line-131"></a>
## 7. 下一步

1. **接入 A-30 总路线**（由协调者/集成者写）：本路径作为 76 条之一，按 `01-AUDIT.md:271` 总路线挂「基础/进阶顺序、可替换分支、跨艺术家比较」。跨艺术家比较的现成锚点 = 四条冲突：与达·芬奇（C-02 过渡带）、北斋/马蒂斯（C-17 负空间）、毕加索/马蒂斯（C-18 形体塑造）、Lane B 模板（C-01 反约束）比较（均 `conflicts.md`）。
2. **与盘（横向）**：对照 `LEARN-da_vinci` / `LEARN-hokusai` / `LEARN-matisse` / `LEARN-picasso` 的对应轴，统一「空白/留白」「过渡带」口径后再做组合卡（C-17 定义对齐 `conflicts.md:272-283`）。
3. **纵向（纵深）**：待 RECOVERY 恢复 `experiments/E1_t1c` 后复现 §8.1b v2 的 T1 3/3，再谈 E4 纯风格迁移；A-12 组合规则（N1/N3/N4/N9）落地后，用 E2/E2b/E2c 检验 C-01/C-02/C-18 的分区解是否真能产出（`conflicts.md:339` 配套、AUDIT `RESULT.md` §4 交接建议③）。
4. **来源补齐（非本路径范围）**：外部 URL（梵蒂冈/维基/Gutenberg/Wikisource）本轮未联网复核；Condivi 训练章节未逐字直读（`dossiers/michelangelo.md:213-221` §10 缺口）。由带网络的来源核验 lane 处理，不在此伪造。

---

<a id="db-source-line-140"></a>
## 8. 使用边界

- **建议练习，非成效证明**：全部练习为「建议练习」；练习效果尚未由人完成或评价，不写「已证实学习收益」（01-AUDIT.md:273）。产出物的可判定属性（§5）是**目标**，不是学习测量。
- **规则等级**：§4 / §8.2 / conflicts 解法均为项目操作规则 `[归纳]`，可被 A-12 实验推翻（`conflicts.md:10-26`）；不是米开朗基罗本人主张，也不是史实。
- **自述 vs 推断**：How-to-Think 中作者自述与研究者推断严格分离，见 [how-to-think.md](how-to-think.md)；不从作品外观编造作者心理（`00-GOAL.md:9`）。
- **不升级史实**：外部 URL 本轮未联网复核、图像仅到 metadata/权利行未 `image_seen`（AUDIT `coverage_manifest.json` `unverified` / `read_scope_note`）；史实真值不因本路径升级。
- **能力不冒进**：本卡 HAS §8.1b（`modules/michelangelo.md:39`），但 E4 纯风格迁移、E1_t1c v2 3/3、A-12 组合实验均未复现，`[UNVERIFIED]` 保留（AUDIT `RESULT.md` §0）。
- **权利边界**：三张公开图 = 1 PD（creation_of_adam）+ 1 CC BY-SA 4.0（david，须署名 Livioandronico2013 + SA）+ 1 CC0（pieta）；不得统称 PD（AUDIT `RESULT.md` §3）。
- **只读契约**：本轮零仓库写入、零 git 变更、零子代理；产物仅在 内部证据 7a16f6a75561ca45（未公开；来源记录由维护者保留）。conflicts.md 的 C-01/02/17/18 数字行号 locator 相对冻结树有漂移（AUDIT `RESULT.md` §1.5），本文件以 `grep -n` 实测的 §2 语义锚点 + 实际行号为准，行号回填交 CONFLICT-* 迁移任务。

## 同一条目的附页

- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
