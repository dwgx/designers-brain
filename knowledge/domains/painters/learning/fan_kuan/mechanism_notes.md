<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-fan_kuan；原正文 SHA-256 `7512e98fa1a583c6ead92c83a5a295b17054526a786c08b9aff973364e833d1c`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-fan_kuan — 机制笔记（§4 参数 / §8.2 规则 → 练习映射 · 开放项 · 失败条件）

> 证据底本：内部证据 d1cb1fe5c1a7bc81（未公开；来源记录由维护者保留）（ACCEPTED：RESULT.md / claim_evidence_map.csv 135 行 / counterexample.md / rights_review.md / quote_audit.md / coverage-manifest.json）。**复用不重审**，沿用 `文件 : 节 : 行号` 定位。基线 `f008952365a77e140cbda3f3959d43ef000f9a22`（READ-ONLY）；本 lane NO repo writes / NO subagent spawns / NO credentials。
>
> **等级总纪律**：§4 六参数、§8.2 八规则、`conflicts.md` 判定全为 `[归纳]` 规则层，**未对原作做像素测量**（[fan_kuan.md](../../dossiers/fan_kuan.md) §10-8 L272、§D L425；`AUDIT-fan_kuan/RESULT.md` §7-2）。`_extract.py --check` 228/228 校验「卡↔档案逐字一致」，**不是**阈值对原作的像素验证（RESULT §2 L27）。`[史料]`/`[研究]`/`[归纳]`/`[推测]` 分离照 [fan_kuan.md](../../dossiers/fan_kuan.md)；范宽无文字传世，Q1/Q2 为转述（corpus L4、L199）。
>
> **brief 三项强调落地索引**：① 雨点皴（密点短笔 + 名称晚出）→ §A M1、§B P1/§8.2-1、§D-1；② 立幅主峰压迫机制 → §A M2、§B P2/§8.2-2、§D-2；③ OVERTURNED / FK-B-02 开放项 / NPM 署名 → §D-3（OVERTURNED）、§D-4（FK-B-02）、§D-6（NPM 署名）。所有练习为**建议练习**，非已证实学习收益（`01-AUDIT.md` §8.1 L273）。

---

<a id="db-source-line-11"></a>
## §A 机制→判定量→等级（M1–M7，对齐 learning_path.md §3）

| 机制 | 可判定量 | 来源定位（档案 / 卡） | 等级 |
|---|---|---|---|
| **M1 雨点皴 / 密点积墨** | 短笔触（长 ≤主山高 2%）覆盖率 ≥60%；方向角标准差 ≥20°；单一方向平行排线 <30% | [fan_kuan.md](../../dossiers/fan_kuan.md) §8.2-1 L202；§1-2 L30；§2-1 L42；卡 L49 | `[归纳]`（阈值）/ `[史料]` 郭若虚「搶筆俱均」Q6 L50 / `[研究]` 刘芳如 |
| **M2 立幅主峰压迫** | 连通域高度 ≥60% 画高；重心偏差 ≤10% 宽；顶部距上缘 ≤5% 高 | [fan_kuan.md](../../dossiers/fan_kuan.md) §8.2-2 L203；§1-1 L29；§4 P2 L83–86；卡 L50 | `[归纳]`（阈值）/ `[史料]` 徐悲鸿 2/3、赵孟頫「山勢逼人」Q18 L134 |
| M3 三段式云雾留白带 | 亮带亮度 ≥纸色 90%、横贯 ≥60% 宽、画高 35–60%、面积 8–25%、带内墨线 ≤3% | §8.2-4 L205；§1-3 L31；§2-6 L47 | `[归纳]` / `[史料]` NPM 三段式 |
| M4 墨色浓重分层 | 明度直方 ≥3 带；深色（≤40% 亮度）25–60%；禁内部 std<5% 平涂块 | §8.2-3 L204；§1-7 L35；§2-2 L43 | `[归纳]` / `[史料]` 米芾「深暗如暮夜晦暝」Q11 L85 |
| M5 方折轮廓 + 山顶密林 + 水际大石 | 折角 60–120° ≥50% 拐点；长弧 ≤30% 周长；山顶 10% 高带深色密林；水岸巨石 ≥1（宽 ≥15%） | §8.2-7 L208；§1-4/5/6 L32–34；§2-3/4/5 L44–46 | `[归纳]` / `[史料]` 米芾 Q9 L71 |
| M6 一线悬瀑 + 点景渺小 | 亮线宽 ≤1% 画宽、高 ≥8% 画高、亮度 ≥95% 纸色、位于上 1/3–1/2；点景 ≤1.5% 画高、≤8 个、下 1/4、面部 ≤3px | §8.2-5/6 L206–207；§1-8/9 L36–37 | `[归纳]` / `[史料]+[研究]` NPM「懸絲瀑布」 |
| M7 界画「铁屋」 | 建筑群 ≥1、屋脊/飞檐/斗栱/柱椽可辨、以墨笼染 | §1-10 L38；§2-9 L50；Q6 L50 | `[史料]` 郭若虚 |
| M8 动画护栏（若转 motion） | 云雾漂移 ≤0.5%/秒；瀑布纵向 ≤2px/帧、水线水平固定；点景位移 ≤1%/秒；帧差 ≤1%；禁推拉/人物动作/墨迹闪变 | §8.2-8 L209；卡 L56 | `[归纳]` |

---

<a id="db-source-line-26"></a>
## §B §4 六参数 → 可判定规则 → 练习变体（逐条映射）

[fan_kuan.md](../../dossiers/fan_kuan.md) L78–106 / [fan_kuan.md](../../modules/fan_kuan.md) L60–88 逐字一致（228/228）。每档弱/中/强都是 `[归纳]` 操作档位，**无原作逐帧实测支撑**（`claim_evidence_map.csv` FK-S4-*-W/M/S 全标 `unverified`，§10-8 L272）。

| 参数（默认） | 三档（照录） | 对应 §8.2 可判定量 | 练习落点（learning_path §4） | 失败/退化条件 |
|---|---|---|---|---|
| **P1 雨点皴密度**（强）L78–81 | 弱稀疏/中成片/强满皴 | §8.2-1：覆盖 ≥60%、方向 std ≥20°、单一方向 <30% | 阶梯 2 三档变体 | 披麻长线 / 等宽线 / 规则排线 / Seurat 色点 / 干笔羽状主纹理（卡 L40–44 负向）；覆盖 <60% |
| **P2 主山压迫度**（强）L83–86 | 弱 ≤40% / 中 40–60% / 强 ≥60% 中轴顶天 | §8.2-2：≥60% 高、重心 ≤10% 宽、顶部 ≤5% | 阶梯 1 三档 + 立轴/横卷对照 | 横卷/平远（→黄公望 §3.1 L67/L71）、主峰 <60%、中轴偏移 |
| **P3 墨色浓度**（中–强）L88–91 | 弱淡/中 3 级/强湿笔浓墨「土石不分为退化」 | §8.2-3：深色 25–60%、≥3 带、禁平涂 | 阶梯 3 P3 档 | 纯黑死墨 / 灰平 / 青绿重彩；**P3 强自带退化注** 与米芾 Q10/Q11 正面描述张力（FK-CE-01） |
| **P4 云雾留白带**（中）L93–96 | 弱 ≤5% / 中 8–15% 一条 / 强 ≥15% 多带 | §8.2-4：8–25%、带内墨线 ≤3%、画高 35–60% | 阶梯 3 P4 档 | 满幅云雾 / 多带切断主山连通域；与 P1 强争同像素集（FK-CE-01） |
| **P5 点景渺小比**（强=渺小）L98–101 | 弱 ≤3% / 中 ≤2% / 强 ≤1.5% 下 1/4 | §8.2-6：≤1.5%、≤8 个、下 1/4、面部 ≤3px | 阶梯 1 尺度对照 | 人物 >指尖 / 近景特写 / 叙事动作（卡 L40–41 负向） |
| **P6 轮廓方折度**（强）L103–106 | 弱圆弧/中相间/强方折主导 | §8.2-7：折角 60–120° ≥50%、长弧 ≤30% | 阶梯 1 大形 + 阶梯 3 | 圆润曲线（§8.1 退化处理 L197 追加 `axe-cut corners`） |

> **默认旋钮组合**（§8.1 中文说明 L196 / 卡）：P1 强 + P2 强 + P3 中–强 + P4 中 + P5 强 + P6 强。FK-CE-01 的反例正是把 P3/P4 也推到强（见 §D-5）。

---

<a id="db-source-line-43"></a>
## §C §8.2 八规则 → 练习自查表

| # | 规则（逐字要点） | 自查脚本量 | 练习用档 | locator |
|---|---|---|---|---|
| 1 | 雨点皴覆盖 ≥60%、方向 std ≥20°、单一平行 <30% | 短笔长 / 覆盖率 / 方向角分布 | 阶梯 2 | [fan_kuan.md](../../dossiers/fan_kuan.md) L202 / 卡 L49 |
| 2 | 巨碑主山 ≥60% 高、重心 ≤10% 宽、顶部 ≤5% | 连通域高 / 重心 / 顶部距 | 阶梯 1 | L203 / 卡 L50 |
| 3 | 墨色 ≥3 带、深色 25–60%、禁 std<5% 平涂 | 明度直方 / 深色占比 / 局部 std | 阶梯 3 | L204 / 卡 L51 |
| 4 | 亮带 ≥90% 纸色、横贯 ≥60%、画高 35–60%、8–25%、带内墨线 ≤3% | 亮带面积 / 位置 / 带内墨线 | 阶梯 3 | L205 / 卡 L52 |
| 5 | 悬瀑亮线宽 ≤1%、高 ≥8%、亮度 ≥95%、上 1/3–1/2 | 垂直亮线几何 | 阶梯 1 观察 | L206 / 卡 L53 |
| 6 | 点景 ≤1.5% 高、≤8 个、下 1/4、面部 ≤3px | 点景高度 / 计数 / 位置 | 阶梯 1 | L207 / 卡 L54 |
| 7 | 轮廓折角 60–120° ≥50%、长弧 ≤30% | 拐点折角分布 | 阶梯 1 | L208 / 卡 L55 |
| 8 | 动画：云雾 ≤0.5%/秒、瀑布 ≤2px/帧、帧差 ≤1% | 帧差图 / 位移 | （motion lane，本 LEARN 不跑） | L209 / 卡 L56 |

> 8 条在 `claim_evidence_map.csv` 对应 FK-S82-01…08（L57–64）全标 **`unverified`**：理由逐字「§10-8 自述未实测；`_extract.py --check` 校验的是与模块卡逐字一致(228/228)，不是阈值对原作的像素测量」。本 LEARN **不升级**这些状态。

---

<a id="db-source-line-60"></a>
## §D 开放项 / 冲突 / 反例 / 权利（brief 强调点专节）

<a id="db-source-line-62"></a>
### D-1 雨点皴：操作有据、名称晚出（OVERTURNED 携带）
- **操作端（supported）**：郭若虚《圖畫見聞誌》「峯巒渾厚，勢狀雄強，**搶（上聲）筆俱均**」（corpus Q6 L50 / [fan_kuan.md](../../dossiers/fan_kuan.md) §5-5 L122）；刘芳如「中鋒短線，千筆萬筆，逐層疊搭，線條的方向也並不一致，但整體卻毫不紊亂」（§2-1 L42）；NPM 著录「皴法：雨點皴」（§7-1 L152）。→ `FK-S2-01`（claim map L12）**supported**。
- **名称端（OVERTURNED）**：「『雨點皴』則出自明代著錄，諸如陳繼儒《妮古錄》、唐志契《繪事微言》、汪珂玉《珊瑚網》、朱謀垔《畫史會要》…北宋時代『雨點皴』之名尚未出現」——刘芳如《默與神遇》原文（`AUDIT-fan_kuan/RESULT.md` §4.2，`raw/artouch_liufangru.html` HTTP 200，逐字命中）。[fan_kuan.md](../../dossiers/fan_kuan.md) §10-4 L268、§自审 B-2 L391、§1-2 L30 按「**操作先于名称**」改写。
- **判定口径（不改写）**：`FK-S1-02`（claim map L3）= **partial**「操作描述有据；但『雨点皴』名称为明代晚出 → 名称部分不成立」；`FK-B-02`（L91）= **conflict**（OVERTURNED）。本 LEARN 全程携带此口径，练习/决策里讲「北宋密点短笔操作（后明人追认名）」，**不写「范宽用雨点皴」**。
- **附带**：zh.wikipedia「范寬」条「雨點皴」为 **redlink（页面不存在）**（`RESULT.md` §4.3），不可据以证术语史，反印证「名称非通行北宋术语」。

<a id="db-source-line-68"></a>
### D-2 立幅主峰压迫机制（[[归纳]] 操作化 + 史料观察对象）
- 操作化：§8.2-2（L203 / 卡 L50）≥60% 高 + 重心 ≤10% 宽 + 顶部 ≤5%；P2 强档（L86 / 卡 L68）「中轴耸立、顶天立地（巨碑式）」。
- 观察对象（非阈值来源）：徐悲鸿「一山頭，幾佔全幅面積三分之二」（§1-1 L29 / corpus Q24）、赵孟頫「大圖闊幅，山勢逼人」（corpus Q18 L134–138）、NPM 2021「巨碑式山水畫的典範」（§7-8 L159）、NPM「近、中、遠三段式…突顯近景渺小行旅與主山巍峨崇高的對比」（§7-1 L152）。
- 分工边界：纵向立轴 / 高远 vs 黄公望横向长卷 / 平远（§3.1 L67、L70 判据②、L71 两卡互禁）。

<a id="db-source-line-73"></a>
### D-3 OVERTURNED（明代著录先于雨点皴名）—— 全程携带、不升级、不改写
- AUDIT 唯一 OVERTURNED 项（Task brief A-77）：「『雨点皴』为北宋术语」被推翻，名称确出**明代**四种著录，北宋郭若虚只称「**槍筆**」（`RESULT.md` §1 Verdict、§4.2；claim map FK-W-02 L133 `supported`；dossier §自审 B-2 L391）。
- 本 LEARN 立场：**沿用 ACCEPTED 审计的判定，不重审、不复核公网、不升级为实验验证**；只在 how-to-think D3 / learning_path §3 M1、§6-1、§8 / 本文件 D-1 / RESULT.md 记录。不写 repo、不改 AUDIT、不改 conflicts.md。
- `FK-S1-02=partial` + `FK-B-02=conflict` 两条口径原样保留；「操作先于名称」是所有产物共同约束。

<a id="db-source-line-78"></a>
### D-4 **FK-B-02 冲突行（郭若虛 槍筆）作为开放项** —— brief 指定，不裁决
- **行本身**：`claim_evidence_map.csv` L91 `FK-B-02`：「『雨点皴是范宽的北宋术语』→ 明代著录始见 [OVERTURNED]」，grade `[研究]`，support_status **conflict**，locator `dossiers/fan_kuan.md:391`（自审 B-2），basis 注明「经 artouch web 原文独立复核一致」。同族：`FK-B-03`（L92 王翬 Commons 源链接 5099→5100）、`FK-B-04`（L93「如行夜山」出处未立）亦标 conflict；`FK-B-01/L95` supported、`FK-B-05` supported(修正)。
- **为何是「开放项」而非「已登记冲突」**：`grep -Ei '范宽|范寬|Fan Kuan|fan_kuan|雨点皴|雨點皴' knowledge/cross/conflicts.md` → **0 命中**；§4 near-miss 表 11 行亦无 fan_kuan（`RESULT.md` §5 L46；claim map `FK-X-01` L129 `supported`）。`conflicts_rows_checked.total = 0` 的原因是 fan_kuan 卡 **wave19 并入、晚于 B-12 清单（18 C 行 + N1–N9 + 11 near-miss）**——**不是漏审、不是缺陷**。因此郭若虚「槍筆」（北宋操作词）与明代「雨点皴」（后起名称）的**术语层对应**在 `conflicts.md` **没有可挂的专属行**。
- **本 shard 的处置（开放、不越权）**：
  1. 只在 LEARN 产物里**记录**：FK-B-02 是术语层「名称晚出」的 conflict 行，端点 = corpus Q6 L50「搶筆俱均」× 刘芳如明代四种著录（`RESULT.md` §4.2）；
  2. **不**把它判定为新的 C 行 / near-miss 行、**不**改写 `conflicts.md`、**不**改写 AUDIT 任何产物、**不**声称「已登记」或「已消解」；
  3. **可判定的下一步**留给 conflicts owner / INVENTORY：在下轮统一清单里补一行「术语层：北宋操作词『槍筆』 vs 明代追认名『雨点皴』，处置=操作/名称分层（操作 supported、名称 OVERTURNED）」，并按 §3 N1/N4/N9 给出现值；本 LEARN 不越权。
- **conflicts.md 通用规则**（组合预检仍要走）：§3 N1（笔触/线条）、N3/N4（墨色浓度、负空间；显式取值或分区）、N9（组合卡验收口径 = 主模块规则全集 + 辅模块非冲突轴）。[fan_kuan.md](../../dossiers/fan_kuan.md) §3.1-4 L74 与卡 L92–97 已指向它。
- **定位漂移（AUDIT 只报告不修，照录）**：`conflicts.md` §5-C 复跑示例 michelangelo L175→现 **L176**、da_vinci L162→现 **L163**（各 +1）；§2 C-01 L62「michelangelo L175」现为另一条；§5-B-2 L372「michelangelo §4 L71」为历史行号未逐条重跑（`RESULT.md` §5 L48–50；claim map `FK-X-02` L130 `partial`）。本 LEARN 不改 conflicts.md（非写权）。

<a id="db-source-line-88"></a>
### D-5 失败条件 / 反例（直接复用 AUDIT `counterexample.md` / FK-CE-01，不重跑）
- `FK-CE-01`（claim map L136 `partial`）：**`[inference]` 纸面反例**——P1 强（满皴 ≥60%）+ P3 强（浓墨至「土石不分」）+ P4 强（≥15% 多带云雾）同时拉满 → §8.2-1/3/4 在**同一像素集合**上争面积（亮带不许墨线 vs 满皴要求密点；浓墨深暗被亮带稀释），且触发 P3 强档自带「土石不分为退化」注记（L91）与米芾 Q10/Q11「晚年用墨太多，土石不分」正面史料的未消解张力（`counterexample.md` L19–27）。
- **边界**：0 帧渲染、0 像素测量，**不推翻任何 §8.2 规则**，只暴露「缺跨参数联合约束 / 轴所有权表」（L27–28）。可判定下一步：给 `conflicts.md` §3 N3/N4 补「纹理覆盖轴 / 云雾带轴 / 深色占比轴」分区掩膜定义；实测三强可共存则反写 §4 档位说明（L28）。
- **与 conflicts.md 关系**：无 fan_kuan 专属行可挂（§D-4），故标「待补」方向，不冒充已登记冲突（`counterexample.md` L29）。
- **其它失败条件**（learning_path §6 全表）：披麻/长卷（→黄公望）、等宽线（→北斋）、色块推导（→塞尚）、规则排线、主峰 <60%、纯黑死墨、满幅云雾、点景放大/推拉动画、把阈值说成实测、把转述写成「范宽写道」、静默折中组合取值、误用 NPM 开放资料图不署名。

<a id="db-source-line-94"></a>
### D-6 **NPM 署名要求（brief 强调，必须落地）**
- 8 张公开图权利构成（`AUDIT-fan_kuan/rights_review.md` L20）：**PD ×3 + CC0 ×4 + NPM 开放资料 ×1**；`unknown_license_count = 0`。
- 唯一带**强制署名**的是 `wanghui_fa_fankuan.jpg`（王翬《紅林秋霁》「法范寬山水」，清·康熙十一年 1672，NPM）：许可逐字「**开放资料（政府资料开放授权条款，相容 CC BY 4.0；署名：国立故宫博物院）**」（`rights_review.md` L14；本地 `_images/fan_kuan/MANIFEST.md:18`；全局 `_images/manifest.md:366`；claim map `FK-R-04` L124 `supported`）。→ **§12-8 练习（learning_path §2）若用该图，必须保留「国立故宫博物院」署名**；其余 7 张 PD-Art / CC0 无强制署名，机构照录于作品字段。
- 正确源：NPM IIIF `Collection/Detail/5100?dep=P`（`MANIFEST.md:18`）。**误链纠正**：[fan_kuan.md](../../dossiers/fan_kuan.md) §自审 B-3 L392 / `rights_review.md` L7 记 Commons 源链接 ID **5099（= 仿李成山水）→ 5100（= 法范寬山水）** OVERTURNED；claim map `FK-B-03` L92 `conflict`。练习引用用 5100，不沿用误链。
- 未收录（公开侧无开放许可）：雪山萧寺图 / 群峰雪霁图 / 海山图（`rights_review.md` L22–24）；§12-4/§12-6 只能「读著录 + 文字临摹」，不冒充已取高清。本 lane 只引用权利记录、不复制像素、不重新授权、不逐张目检（AUDIT §3 image_seen=0）。

<a id="db-source-line-100"></a>
### D-7 分工条款（vs 黄公望 / 北斋 / 塞尚，`[归纳]` 可被实验推翻）
[fan_kuan.md](../../dossiers/fan_kuan.md) §3.1 L63–74：
- **vs 黄公望**：四轴（皴法单元密点/长线、构图纵巨碑/横长卷、墨法浓湿/淡积、形制立轴/手卷）+ 4 条可判读判据（L70）+ 两卡互禁（L71）；与 `huang_gongwang.md` §3.1 对称（§10-12 L276）。
- **vs 北斋**：毛笔提按短点千叠 vs 刻线等宽 + 平涂（媒介/质感/空间三判据，L72）。
- **vs 塞尚**：密点积墨量感 vs 色块调制 + 几何推导（量感来源/空间/笔触单元三判据，L73）。
- **与系统其余模块**：组合按 `conflicts.md` 预检，重点笔触/线条、墨色浓度、负空间（L74；卡 L92–97）。hokusai/cezanne 对侧条款「本轮首落、待后续波次互查」（§10-12 L276）——不冒充已完成互查。

---

<a id="db-source-line-109"></a>
## §E 状态与边界（不升级清单）

| 项 | AUDIT 状态 | 本 LEARN 处置 |
|---|---|---|
| §4 六参数 / §8.2 八规则 | `partial`/`unverified`（§10-8 L272；claim map FK-S4-*/FK-S82-*） | 保持 unverified；练习为建议，非实测 |
| §1-2「雨点皴」名称 | `partial`（FK-S1-02） | 保持 partial；OVERTURNED 携带 |
| FK-B-02（槍筆 / 明代著录） | `conflict`（OVERTURNED） | **开放项**：只记录、不裁决、不改写 conflicts.md |
| conflicts.md fan_kuan 专属行 | 0 命中（FK-X-01 supported，非缺陷） | 如实记录；组合走 §3 N1/N3/N4/N9 |
| FK-CE-01 反例 | `partial` `[inference]` | 复用、不重跑、不升级为实验验证 |
| NPM 开放资料署名 | FK-R-04 supported | 落地为 §12-8 练习的硬性署名要求 |
| 真迹/传称 | §10-3 L267 待核 | 传称作品练「样式」不冒充真迹定论 |
| 外部来源 | Q20/Q23/Q24/Q26 转引、四处出处未找到（§7-4、§10-5） | 标 unverified；本 lane 离线只读本机 |
| `card_has_81b=false` / §8.3 野外样本 | gap / 未找到（AUDIT §7-1、§7-3；L213–214） | 属 STYLE / RECOVERY / 实验 lane，不越权 |
| 练习效果 | 无 human review | `human_review.status=not_applicable`，不写「已证实学习收益」 |

> 与同目录接口：[learning_path.md](learning_path.md) §4 三段阶梯、[how-to-think.md](how-to-think.md) D1–D8 决策序、[claim_evidence_map.md](claim_evidence_map.md) 逐 claim 定位、`RESULT.md` 结果摘要。证据底本：内部证据 d1cb1fe5c1a7bc81（未公开；来源记录由维护者保留）（ACCEPTED）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
