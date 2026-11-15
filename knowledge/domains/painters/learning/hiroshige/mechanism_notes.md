<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-hiroshige；原正文 SHA-256 `70ee221c817f4a60cb9fcd8423fbb8cc5496416f5b89919f5300a763c524c7f5`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-hiroshige · mechanism_notes.md（机制 → 练习映射）

> 任务 `LEARN-hiroshige`｜作者 LearnHiroshige（hy4free）｜2026-11-15｜kind: `mechanism_notes`
> 仓库 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22` **只读**；证据底座 = 已 ACCEPTED 内部证据 4919edab864eb7ff（未公开；来源记录由维护者保留）。
> **读法**：本表把模块卡 `§4 六参数` + `§8.2 八规则`（与档案 §4/§8.2 逐字一致，`_extract.py --check` = 228/228）映射成**可执行练习**与**可判定失败条件**。全部阈值 = `[归纳]`（分母＝假想参考帧，**未对原作做像素测量**，`modules/hiroshige.md:54`）；练习 = **建议练习 `[归纳]`**，效果未经人评（`01-AUDIT.md:273`）。
> **本片强调**：M-A 雨雪风大气瞬间、M-B 斜视角构图机制；证据底座 Met 12 CC0；744→747 known-open 见 §5。

---

<a id="db-source-line-10"></a>
## 1. §4 六控制参数 → 练习映射（参数表 + 默认 + 失败条件）

| 参数 | 三档（[hiroshige.md](../../modules/hiroshige.md)） | 默认 | 对应练习轴 | 失败条件（可判定） | locator |
|---|---|---|---|---|---|
| **P1 系列叙事强度** | 弱=单张名所／中=10–30 张主题组／强=55–120 张宿场·月令·方位推进 | **70%** | 阶梯 3（§12-1/-2/-8 序列骨架 + 版本变奏） | 跨帧题名框位置方差 >5%、落款漂移、画幅比例不一 → §8.2-1 FAIL；单张自足叙事 ≠ 本档 | `modules:60`；`dossiers:99` |
| **P2 天气/时刻强度** | 弱=晴天白昼／中=晨昏·雨雪·月雾之一为主角／强=极端天气入题名 | **60%** | **M-A / 阶梯 1**（雨雪雾月四符号） | 天气符号面积 <15%、同系列天气命名 <2 张 → §1-2 FAIL；一次性事件现场 → 越界透纳；风拆成曲线族 → 越界北斋 | `modules:61`；`dossiers:100` |
| **P3 渐印大气梯度 bokashi** | 弱=平涂为主渐变 <10%／中=单段主梯度带长边 ≥30%／强=多段大面积渐印 ≥2 带 | **65%** | 阶梯 2→3（天空/水面/雾的连续梯度） | 无 ≥1 条连续梯度带、带内明度差 >2/255（≥3% 跳变）、方向非单调 → §8.2-3 FAIL；CX-2「有渐印 ≠ 有 Hiroshige blue」 | `modules:47,62`；`dossiers:101` |
| **P4 裁剪框景强度** | 弱=全景平视／中=近景入边缘一角 ≥1 处与框相交／强=近景 ≥1/3 被切断、远景被框住 | **60%** | **M-B / 阶梯 2**（§12-6/-7/-10 枝·窗·孔三框） | 边缘带 10% 内前景占用 <15%、前景纹理 >10 边缘点/千像素、远景符号偏离中轴 ±25% → §8.2-4 FAIL | `modules:48,63`；`dossiers:102` |
| **P5 旅人密度** | 弱=0–2 人纯景／中=3–8 人行列·渡口·茶屋／强=≥10 人成组 | **50%** | 阶梯 1a 参考练习（雨中 5–8 人同向、雪 ≤2 人，**人数随原作档变**）；阶梯 1b 单点变量 A/B（**旅人数固定 = 5 人**，仅天气变化）；阶梯 3（日本橋 ≥8 组） | 人物高 >10% 画高、细节线 >8 条/人、朝向方差 >30°、人脸关键点 >1 组 → §8.2-5 FAIL；可辨五官/特写 → 负向段；把 1a 的人数差异带进 1b A/B → 违反控制变量（S01 修复点） | `modules:49,64`；`dossiers:103` |
| **P6 蓝 Hiroshige blue 与色调** | 弱=棕绿蓝 <15%／中=25–40% 与渐印绑定／强=≥40% 蓝主导多段渐印 | **55%** | 阶梯 3（色相预算 + C-12 二选一） | 蓝系面积 不在 25–40%、渐印带内蓝 <60%、纯平涂大块蓝 >1 块、主色 >8、饱和 ≥0.85 纯色块 >5% → §8.2-6 FAIL；命名 partial 不得当判据 | `modules:50,65`；`dossiers:104` |

> **用法（原文口径，`modules:67`）**：`P1/P2/P4` 定「是不是广重」——**三条中 ≥2 条 ≥ 中档才成立**；`P3/P6` 定大气与色档；`P5` 是人物层参数（可关）。**CX-1（AUDIT `counterexample.md`）关键反例**：这个数值闸门是**必要过滤器、不是充分身份判据**——用北斋式曲线族/尺度戏法/渺小剪影仍可过闸，却违反 §3.1 分工条款 ≥2 轴；判定必须叠加分工轴（`dossiers:83` 边界注）。

---

<a id="db-source-line-25"></a>
## 2. §8.2 八规则 → 自查量 + 练习 + 失败条件（逐条）

| # | 规则（`modules/hiroshige.md:45-52`） | 可判定自查量 | 练习落点 | 失败条件 | 证据级 / 依据 |
|---|---|---|---|---|---|
| 1 | **系列一致性** | 题名框位置方差 ≤5% 画幅、落款固定、画幅比例一致 | 阶梯 3（§8.2-1 框检测 + 位置统计） | 跨帧框位漂移或版式不一 | `[归纳]`；依据 `[R7]` 题名框/改印（`corpus Q21`） |
| 2 | **天气线族**（M-A 核心） | 雨：方向方差 ≤10°、长度方差 ≤20%、15°–45°、线宽变化 ≤30%、无交叉、无排线塑形；雪：V≥0.9 白区**无颜料边缘** | **阶梯 1**（庄野白雨 / 蒲原夜雪） | 雨滴（禁）、排线塑形（越界丢勒）、雪白区带颜料边 | `[归纳]`；作品《庄野》《大はし》+ 留纸工艺 `[R2]` |
| 3 | **渐印 bokashi** | 每帧 ≥1 条连续梯度带（长边 ≥30%）、带内相邻像素明度差 ≤2/255、方向单调、优先天空/水面 | 阶梯 2→3 | 梯度带缺失 / banding / 硬边 | `[归纳]`；工艺 `[R2][R7]` |
| 4 | **裁剪框景**（M-B 核心） | ≥1 前景与画框相交、边缘带 10% 内被占 ≥15%、前景纹理 ≤10 边缘点/千像素、远景符号中轴 ±25% | **阶梯 2**（§12-6/-7/-10） | 全景平视 / 近景无遮挡 / 单点透视消失线 | `[归纳]`；`corpus Q20`「too close to the lens」**转引 partial** |
| 5 | **旅人** | 高 ≤10% 画高、细节线 ≤8 条、朝向方差 ≤30°、人脸关键点 ≤1 组 | 阶梯 1/3 | 特写/可辨脸/逆行列 | `[归纳]`；`corpus Q15`「integrating local inhabitants」 |
| 6 | **色相预算** | 蓝 H190–250° 面积 25–40%、其中 ≥60% 在渐印带、饱和 ≥0.85 纯色块 ≤5%、主色 ≤8 | 阶梯 3（+CX-2 分离检查） | 平涂大块蓝 / 撞色 / >8 主色 | `[归纳]`；C-12 蓝轴；`corpus Q19` 命名 **partial** |
| 7 | **竖幅叠层** | 近/中/远三层（纵向边缘密度递减 ≥2 级或尺度比 ≥3×）、地平线在上/下 1/3（不在中线 ±5%） | 阶梯 2/3（横 vs 竖 §12-8） | 地平线居中 / 层数不足 / 横版强套竖叠 | `[归纳]`；`[R1]` 近中远叠合构图 |
| 8 | **静场运动预算** | 帧间光流 Δ ≤2%/帧、无运动模糊核/镜头特效、雨线族整体视差 ≤10%/秒 | 全阶梯边界（「天气在动、画面不动」） | 运镜/爆炸动势/速度线 → 越界北斋或透纳 | `[归纳]`；C-09 静侧；`dossiers:90` |

> **CX 反例（AUDIT `counterexample.md`，全部 `[inference]`，非完成的真人实验）**：
> - **CX-1（主反例）**：过 §4 闸门但用北斋曲线族/尺度戏法/渺小剪影 → 违反 §3.1 ≥2 轴分工；判别证据是 `dossiers:83` 边界注。→ 本表把 §3.1 分工轴作为 **P1/P2/P4 的必要叠加检查**。
> - **CX-2**：§8.2-3（≥1 梯度带）与 §8.2-6（蓝 ≥60% 在带内）**可同时满足但互不蕴含** → 阶梯 3 必须把「渐印」与「蓝轴」分开练、分开判。
> - **CX-3**：§8.2-8 群体视差 ≤10%/s 与逐像素 Δ≤2%/frame 需先定义**测量口径**才能进任何 E4 runner（本片不跑实验，只挂账）。
> - **CX-4**：24/25/23 三口径反例（非机制，见 `learning_path.md §1` 读法纪律）。

---

<a id="db-source-line-46"></a>
## 3. 两条主机制的因果链（把机制讲成「为什么这样排练习」）

<a id="db-source-line-48"></a>
### M-A 雨雪风大气瞬间（weather-as-subject chain）

```
[史料/研究] 馆方 Q15「signaling shifts in time and weather」
   → [归纳] P2 定天气为主角 (默认 60%)
   → [归纳] §8.2-2 把天气拆成可数符号：雨斜线族 / 雪留纸白 / 雾横带 / 月单发光体
   → [归纳] §8.2-8 静场：天气在动(雨线整体 ≤10%/s 视差)、画面不动(光流 ≤2%/帧)
   → [归纳] 分工边界：可重访系列情绪(广重) vs 一次性事件现场(透纳)；风不是第五符号而是动势题材(≥2 轴联合)
```
- **为什么阶梯 1 先练**：`learning_path.md §4 阶梯 1` 已分两栏——**1a 参考练习**（逐件临摹《庄野白雨》5–8 人 /《蒲原夜雪》≤2 人，**旅人数随原作档变化，不是单点变量实验**）先把天气符号参数化；**1b 单点变量 A/B**（**旅人数固定 = 5 人**、其余输入固定，**仅天气类型变化**）才把天气真正锁成**单一可变量**，避免把「气氛」与「事件」混成一团。旧稿把两者写在一起、却称「旅人数固定」= 控制变量自相矛盾（S01 报，repair_round=1 已修正）。
- **失败根因**：把雨线当排线（丢勒）、把雪画成白颜料（违留纸白）、把风拆成曲线族（北斋）、把夕立画成风暴现场（透纳）。
- **诚实边界**：「Hiroshige blue＝普鲁士蓝」命名 partial（Q19 转引，英文页未复核）；线族/留白参数是 `[归纳]` 假想参考帧，非原作像素实测。

<a id="db-source-line-61"></a>
### M-B 斜视角构图机制（oblique / cropped framing chain）

```
[研究·转引] Q20「too close to the lens」(partial, Potter 2007 原刊未直读)
   → [归纳] P4 裁剪强度 (默认 60%) + §8.2-4 边缘带占用 ≥15% / 远景中轴 ±25%
   → [归纳] §8.2-7 竖幅三层叠合(近特写→中事件→远符号) + 地平线 1/3 带
   → [归纳] §8.1 负向段禁单点透视消失线 / 戏剧投影 / 写实体积
   → [归纳] 分工边界：裁剪框景+水平纵深(广重) vs 单斜线+曲线族嵌套(北斋)；框景≠霍珀都市孤独
```
- **为什么阶梯 2 在阶梯 1 之后**：阶梯 1 的 **1b A/B**（旅人数固定、仅天气变化）先把「天气」锁成受控变量，再单独操练「近景裁切把视线推向画外」；否则两个变量同时变，无法归因。1a 参考练习的人数差异属跨作品对照、不作因果归因（见 `learning_path.md §4 阶梯 1a` 修复说明）。
- **失败根因**：全景平视（P4 弱）、近景有细部（违「无细部」机制）、加消失线/投影（负向段）、把 §8.1 正向段 `a cropped foreground element cut by the picture edge` 读成单点透视许可（`dossiers:56` 的「夸张单点透视」是研究描述，不解除生成禁令）。
- **诚实边界**：Q20 是转引 partial；§8.2-4/-7 全部 `[归纳]`；CX-1 提醒「过闸 ≠ 身份」。

---

<a id="db-source-line-76"></a>
## 4. 冲突 / 预检轴（AUDIT 已报：conflicts.md 无广重命名 C 行）

> 内部证据 36335830bbf50adb（未公开；来源记录由维护者保留）、`claim_evidence_map.md §C G13-CONFLICTS-ZERO`、`coverage-manifest.json → conflicts_locator_drift[]`：
> `conflicts.md`（sha `314a24da…`，421 行）是**原始 20 卡的冻结台账**（18 条 C-01..C-18 + §4 near-miss 11 行）；`grep -i 'hiroshige|广重|広重'` **零命中** → **没有广重 party 的 C 行**。模块卡 `冲突注记`（`modules:73-77`）与 `dossiers §3.1`（`:84/:89/:91`）引用的 C-07/C-09/C-12/C-16 是**邻接预检轴**，当事人为丢勒/北斋/梵高/莫奈/马蒂斯/米开朗基罗等，广重不是 party。

| 预检轴 | 本片引用方式 | 对应冲突 ID | 处置口径 | 证据级 |
|---|---|---|---|---|
| **vs 北斋**（写死主条款） | 系列骨架 + 动势结构 ≥2 轴联合；蓝轴二选一 | C-12（蓝 ≥40% 只许一方）；同侧 C-07/C-16（平涂/无排线） | 选主导轴（建议 70/30）；天气轴同屏二选一或分区 N4；雨线族显式声明「母题线、不承担明暗」 | `[归纳]`（`dossiers:79-84`） |
| **vs 贝赫扎德**（写死主条款） | 叙事单位：序列帧 vs 单页场景 | C-15（金/金属层）、C-16（反约束适用域）、C-17（空场 vs 留白） | 叙事单位二选一或分区；渐印带与微书图案密度不得互串 | `[归纳]`（`dossiers:85-89`） |
| **vs 透纳**（镜像条款） | 天气时间性：可重访版本 vs 一次性事件 | C-09（静侧运动预算） | 广重站静侧；一次性风暴现场归透纳 | `[归纳]`（`dossiers:90`；`modules:76`） |
| **同侧（丢勒 / Lane B 02）** | 平涂/无排线/硬阴影禁令与平面天光共侧 | C-07/C-16 无需改写 | 显式声明「flat ambient light, no cast shadows」 | `[归纳]`（`modules:77`；`dossiers:220`） |
| **越界警报（§4）** | 五类越界：①曲线族/动势→北斋 ②一次性天气→透纳 ③建筑剖面/图内书法→贝赫扎德 ④排线/实心黑→丢勒 ⑤画内单光源/暗部塌陷→卡拉瓦乔/伦勃朗 | — | 组合实验按 §8.2 自查表判分 | `[归纳]`（`modules:67`） |

> **规则层互斥 ≠ 实验验证**：C-06 可拆 / C-18 分区 / C-12 二选一等**未经本 lane 或 AUDIT 组合实验验证**（AUDIT `RESULT.md §9`）；本表只产出「可判分方案」，不宣称 E2/E4 通过。`conflicts.md` 数值行号（L188/L189/L193 引 hokusai §8.2）**已 stale**，re-anchoring 属 CONFLICT-xx lane（repo 只读，AUDIT 只报不改）→ 见 §5 known-open。

---

<a id="db-source-line-93"></a>
## 5. 证据底座与 known-open（本片挂账，不静默改写）

<a id="db-source-line-95"></a>
### 5.1 Met 12 件 CC0 证据底座（逐件可核，沿用 AUDIT 本轮活检）

12 objectID：`36922 / 56915 / 56916 / 36932 / 37248 / 55433 / 36539 / 56689 / 53783 / 36719 / 45294 / 36545`，AUDIT 本轮 Met object API 全部返回 `isPublicDomain=true`（内部证据 4c6d0d1ec0cdd328（未公开；来源记录由维护者保留）；`raw/met_*.json`；`coverage-manifest.json → external_fetches`）。
- **精确口径**：18 张图 = **12 Met CC0 + 6 Commons `Public domain`**（Rijksmuseum 2 / LoC 1 / Brooklyn 1 / AIC 1 / GoogleArtProject 1）。**6 件不是 CC0**；「18 张全 PD/CC0」是宽松合称（`dossiers:7,27`）。逐行源/标签/归属见 `rights_review.md`。
- **著录范式**：`corpus Q24`（Met object 55433，`[史料]`：`isPublicDomain: true` / Credit Line: The Howard Mansfield Collection, Purchase, Rogers Fund, 1936）。
- **本片边界**：**未复访 API、未目检 18 张图**（`image_seen=0`），仅沿用 AUDIT 本轮的字节哈希 + 权利台账 + CC0 活检记录；不新增、不升级权利判定。

<a id="db-source-line-102"></a>
### 5.2 v1.1 total 744→747 漂移 = known-open（核心挂账）

| 项 | 值 | 来源 |
|---|---|---|
| 历史快照 | `total=744`（2026-10-16 实测） | `dossiers/hiroshige.md:158` §7-3 / R12 |
| 活 API | `v1.1/search?q=Hiroshige` → `total=**747**`（+3） | AUDIT `RESULT.md §2`；`coverage-manifest.json → external_fetches[2]`（`met_v11_search.json` sha `b2b9a062…`） |
| 端点状态 | `v1/search` **RETIRED (2026-10-01)** → unavailable | AUDIT `external_fetches[3]`（sha `2db82187…`） |
| AUDIT 判定 | `conflict` / stale-locator（744 是历史快照，**不能按原文复跑**） | `claim_evidence_map.md §C G13-MET-744`；`RESULT.md §9-2` |

- **本片处理**：引用「Met 检索量」时**三件并列**（744 历史 / 747 活值 / v1 retired），不写成任一单值现状、不把 744 当可复跑结果、不把 +3 说成「错误修正」。**known-open**：活 API 会继续漂移，下一次复跑需重新取 `v1.1/search` 并登记 retrieval time + endpoint 版本。
- **同类挂账**：§5「完整语料 23 条」stale（`dossiers:110` vs 实际 24 条 Q1–Q24）；三口径「24 语料 / 25 探针 / 23 stale」分母不同（AUDIT G13 清账）。

<a id="db-source-line-114"></a>
### 5.3 其它 honest unresolved（沿用 AUDIT，不升级）

- 亲笔层极薄：`corpus Q1` 辞世句归属存疑（两处表记并存）；`Q2`《甲州日記》日记正文与狂歌 11 首逐字未取得（前半 1923 烧失）。
- 转引清单：`Q5/Q12/Q13/Q17–Q23` 原刊/原书未直读；`Q19`「Hiroshige blue」命名未在英文页复核到（partial）；Amsden 1912 英译需 OCR 安全归一（自审 B5）。
- `card_has_81b=false`（ledger `artists[hiroshige]`）：§8.1b 纯风格缺节属 `STYLE-hiroshige` lane，**不占本学习路径分母**（`03-RESEARCH-AGENDA.md:125-126`）。
- §8.2 数值阈值 `[归纳]`/未实测（分母＝假想参考帧）；无 E4 rendering 实验在本 lane 运行；conflicts.md 行号漂移待 CONFLICT-xx re-anchor。
- 练习 = 建议练习、`human_review=not_applicable`、无「已证实学习收益」；外部 URL 本轮未重访（`access_status=unknown`）。

---

<a id="db-source-line-124"></a>
## 6. 复跑命令（只读，供独立审阅核对）

```bash
# 从公开仓库根目录执行；注释计数及行号来自源记录，不是此次投影重跑结果。
sha256sum knowledge/domains/painters/modules/hiroshige.md \
          knowledge/domains/painters/dossiers/hiroshige.md \
          knowledge/domains/painters/dossiers/_corpus/hiroshige.md \
          knowledge/cross/conflicts.md ops/GOALS.md \
          knowledge/domains/painters/dossiers/_images/manifest.md
nl -ba knowledge/domains/painters/modules/hiroshige.md | sed -n '43,67p'   # §8.2 八规则 + §4 六参数 + 越界警报
grep -c '^### ' knowledge/domains/painters/dossiers/_corpus/hiroshige.md   # = 24 (Q1-Q24), 非 25
grep -n '744\|747\|v1.1\|retired' knowledge/domains/painters/dossiers/hiroshige.md
```

> 原本机绝对路径与内部回执/schema验证命令留在维护者的私有复核记录。这里仅保留公开仓库相对路径的复核示例；本次投影没有执行这些命令，也没有更新其历史计数、行号或证据等级。

> 本文件为机制映射，不运行图像生成、不重访外部 URL、不跑组合实验、不改仓库。逐条 locator / 证据级见 [claim_evidence_map.md](claim_evidence_map.md)；八节路径见 [learning_path.md](learning_path.md)；决策序分栏见 [how-to-think.md](how-to-think.md)。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
