<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-bosch；原正文 SHA-256 `ce429907ccf8411100fa6f45230b4196b6c080d8abed8e708251d097d1241ea9`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-bosch — 机制说明（§4 参数 + §8.2 规则 → 可执行练习映射）

> TASK_ID `LEARN-bosch` · A-30 · 消费 `AUDIT-bosch`（ACCEPTED）。Repo 只读 @ `f008952365a77e140cbda3f3959d43ef000f9a22`；唯一写区 内部证据 e5069c7b42e76424（未公开；来源记录由维护者保留）；NO repo writes / NO spawns / NO 新外部抓取 / NO 凭据。
> 主轴：**多联画（结构装置） × 想象生物群（拼装式混合体） × 道德叙事（可逐件解码）**。
> **严格分离**：`[自述]=0`（26 quotes，zero self-written）；本文件一切阈值/判据/练习映射均为 `[归纳]` 操作规则，不是博斯自述、不是像素实测值。反例 A 与身份门提案为 `[inference]` / design_candidate **未证伪**。
> 阈值来源：[bosch.md](../../dossiers/bosch.md) §4 L95–L107、§8.2 L231–L242、card L57–L69 / L44–L55；全部未像素实测（L242、§10-9 L314，分母＝假想参考帧）。

<a id="db-source-line-8"></a>
## §A §4 控制参数（6 个）→ 可执行练习映射

| 参数 | 弱 / 中 / 强（[bosch.md](../../dossiers/bosch.md) L99–L104；card L61–L66） | 默认 | 身份门角色 | 练习映射（learning_path §4） | 失败条件 |
|---|---|---|---|---|---|
| **P1 全景叙事密度** | 1–2 / 3–5 / ≥8 单元 | 60% | **联立三条之一**（L106） | rung2：单帧 ≥5 单元、焦点 ≤20%、地平线 ≥上 1/3 | P1=弱（单事件）+P6 土黑 → §4 L107 越界进戈雅 |
| **P2 生物发明强度** | 0–1 / 2–4（各 2 类部件）/ ≥5+物种表 | 50% | **联立三条之一**（L106） | rung1：≥3 混合体、每个 ≥2 类部件来源 | 退化为「单物种畸变/等比放大」→ L107 越界、§8.2-3 L235 排除 |
| **P3 尺度错乱度** | 正常 / 1–2 巨物 / 系统性巨型化 | 45% | 奇想强度（L106） | rung2：≥1 组 ≥2:1 巨物 vs 小人（§8.2-4 L236） | 把巨物做成单物种放大 → 与 P2 冲突 |
| **P4 道德对位结构** | 单讽喻 / 二元对位 / 三幕全景 | 70%（三联档） | **联立三条之一**（L106） | rung1 ≥2 组对位；rung2 三幕可读（§8.2-8 L240） | 形象不可逐件道德解码 → 滑向林飞龙仪式档（§3.1 L86–L89） |
| **P5 直视目光/猫头鹰** | 0 / 1–2 / ≥3（板缘成对） | 35% | 奇想强度（L106） | rung1：≥1 直视观众（§8.2-5 L237） | 只当装饰不写进自查 → 强度档落空 |
| **P6 色域明度** | 土色 / 混合 / 宝石亮色铺开 | 60% | 定档期（L106） | rung2：显式写值（§8.2-7 L239）+ 色板清单（§8.3 L249） | 收窄「土黑+白闪点」+P1 单事件 → L107 越界进戈雅 |

> **用法行（逐字，L106）**：「P1/P2/P4 定『是不是博斯』（全景多事件 + 生物发明 + 道德对位；**三条同时 ≥ 中档才成立**）；P3/P5 定『奇想强度』；P6 定档期」。
> **分工注（逐字，L107）**：「P6 一旦收窄为『土黑 + 白闪点』且 P1 降到单事件，即越界进入**戈雅**领域；P2 若退化为『单物种畸变』且无拼装部件，同样越界」。
> 三件主轴装置落点：P4→多联画三幕；P2→想象生物群；P1→全景编目（承载道德叙事）。

<a id="db-source-line-23"></a>
## §B §8.2 八条可判定规则 → 自查动作 + 失败条件

> 逐字见 [bosch.md](../../dossiers/bosch.md) L233–L240、card L46–L53。L242 自注「以上阈值为本项目 `[归纳]`，未对原作做像素测量；3/5 条与 §3.1 分工判据同轴」。

| # | 规则（缩写） | 阈值 | 自查动作 | 失败条件 / 反例触发 |
|---|---|---|---|---|
| 1 | 地平线规则 | 地平线 ≤40% 画面高度、景深 ≥2 | 边缘/地平线检测 + 深度带分割 | 地平线压低成「窗式近景」→ 失去俯瞰编目 |
| 2 | 多事件密度 | 单元 ≥5、单焦点 ≤20% | 连通域 + 动作簇聚类计数 | 单一大焦点 → 变戈雅式单事件 |
| 3 | 生物发明计数 | 混合体 ≥3、每个 ≥2 类部件、非等比放大 | 对象检测 + 部件来源标注 | **反例 A 的关键**：此条单独达标 ≠ 博斯（见 §D） |
| 4 | 尺度错乱 | ≥1 组 ≥2:1 | 目标框高度比 | 全写实比例 → P3 弱、奇想档落空 |
| 5 | 直视目光计数 | ≥1（板缘成对更佳） | 面部/眼向关键点 + 视线朝向 | 0 直视 → P5 弱 |
| 6 | 光照规则 | 无单点戏剧主光；日景暗带 ≤30%、夜景火光 ≥2 分散 | 亮度质心 + 光源连通域计数 | 单点提灯/火把聚焦 = 戈雅画内证据光（§3.1 判据④ L81） |
| 7 | 色域预算 | 蓝绿 15–35%、暖亮 ≥10%、土黑 ≤55%、V≥0.45/≤0.45 | HSV 掩膜统计 | 土黑主调收窄 → §4 L107 越界；C-15 色数冲突须显式声明色板 |
| 8 | 道德对位（系列帧） | 三幕/七罪序列；单帧 ≥2 组善恶成对 | 序列标注 + 成对元素计数 | **反例 A 的关键**：此条单独达标 ≠ 博斯（见 §D） |

> §8.1 中文使用说明（L227–L229）给的自查四件事 = 规则 3/4/6/5 的口语版；L229 给的组合预检口径（vs 戈雅=亮度/组织、vs 卡拉瓦乔=光源数、vs Lane B=硬阴影 C-01 显式声明「均匀环境光」）在本文 §C 展开。

<a id="db-source-line-40"></a>
## §C §8.1 / §3.1 派生关系（登记，不重跑）

- **§8.1 正向段**（card L19–L33）= §1 指纹的 prompt 化：elevated high horizon / three planes / many small figures / invented hybrid creatures from ≥2 parts / impossible scale / owls staring / even all-over illumination / jewel-like palette / thin matte paint / didactic moral allegory + burlesque humour。**负向段**（card L37–L42）明确排 `--no one-species monsters, single hard light source, sfumato soft edges, glossy varnish, photorealistic anatomy, ordinary scale logic, minimalism…`。
- **3/5 条同轴**（L242）：§8.2 规则 1（地平线/景深）、2（多事件）、3（生物计数）、6（光照）、7（色域）与 §3.1 五判据（L81：①生物计数 ②亮度/色域 ③画面组织 ④光源 ⑤情绪距离）中的前四条同轴；**规则 8（道德对位）是系列帧条件，不在 5 判据里**。正是这个「3/5 同轴 + 各自可数」的结构，给反例 A 留下缝隙（§D）。
- **分工衍生**：§3.1 L82（同轴不可分离→分区/分帧、禁折中灰调怪物）、L90（70/30 选主导轴）、L91（不借达·芬奇柔边/梵高笔触场/卡拉瓦乔单点硬光/丢勒·北斋版画线）；card L78 组合预检重点 C-01（硬阴影）/C-06（饱和度）/C-12（色相面积）/C-15（色数）。

<a id="db-source-line-46"></a>
## §D conflicts.md 中 bosch 相关的全部冲突行（grep 实测 + 回源）

- **零 bosch 专属行（事实非缺陷）**：`conflicts.md` 全文 421 行 `grep -niE 'bosch|博斯|Bosch|Jheronimus|Hieronymus'` = **0 命中**；18 条 C 行（§1 L32–L49）与 16 条 near-miss 编号行（§4，含 #9–#11 2026-10-16 补）均无此画家。依据 `AUDIT-bosch/RESULT.md` §6、`coverage-manifest.json → conflicts_rows_checked`（`artist_specific_C_rows=0` / `artist_specific_near_miss_rows=0`）。
- card L78 引用的 **C-01 / C-06 / C-12 / C-15 是「通用冲突轴引用（组合预检 Lane B 重点）」**，不是以 bosch 为模块 A/B 的专属冲突行；4 条在 conflicts.md 中均存在（§1 L32/L37/L43/L46）。
- **7 处跨档案行号漂移（只报告、不修复）**：C-01 caravaggio L76→77 / L213→214、michelangelo L175→176；C-15/C-16 matisse L82→88 / L187→193 / L180→186（+6）；C-12 van_gogh L203→205（+2）。规则文本无误，纯定位过期；`AUDIT-bosch/claim_evidence_map.md` §8 表 + `RESULT.md` §6 已登记，按 `conflicts.md` §5.C 标为文书层偏移，交 CONFLICT/RULE lane。
- **1 处计数口径漂移**：card L83 记「near-miss 8 对」，当前 §4 实测 16 编号行（#9–#11 标 2026-10-16 补）；与 AUDIT-durer 同类发现（8 vs 11）一致。**只登记、不改仓库**。

<a id="db-source-line-53"></a>
### 反例 A（本档案核心）：P1/P2/P4 联立 vs §8.2 各自可数 `[inference]`

> 照录 `AUDIT-bosch/RESULT.md` §4；目标 = §4 用法行 L106 + 分工注 L107 + §8.2 阈值 L233–L240。全部为**项目内操作规则的逻辑压力测试**，不是艺术史事实。

- **构造帧**：单事件、单肖像聚焦（P1=弱档 1–2 单元）、土色/黑为主 + 小面积白闪点（P6=弱档）、画内 1 个提灯证据光（§3.1 判据④ 的戈雅侧）、但把 P2 强行设成「≥3 个混合体、每个 ≥2 类部件来源」（满足 §3.1 判据①）、成对元素 ≥2（满足 §8.2-8）。
- **判定**：按 §4 L107 分工注，此帧**明确越界进戈雅**（P6 收窄 + P1 单事件）——这部分档案自洽，不构成反例。
- **反例点**：按 §4 L106「P1/P2/P4 三条同时 ≥ 中档才成立」，P1 未达中档 → **应判「不是博斯」**；但 §3.1 判据① 只数「生物发明计数」、§8.2-3 只数生物计数，并未要求同时看 P1/P6/光源。若一个自查脚本**只跑 §8.2-3（生物 ≥3）+ §8.2-8（成对 ≥2）两条**，这帧会被判为「博斯」，与 §4 L106 的三条联立判据矛盾。
- **结论**：不是推翻档案，而是暴露**判据粒度不一致** —— §3.1 的 5 条可判读判据被写成「各自可数」，而 §4 L106 要求「三条联立」；§8.2 自查表（L242 自注「3/5 条与 §3.1 分工判据同轴」）**没有把「P1/P2/P4 必须联立」写成第 9 条自查项**。

<a id="db-source-line-62"></a>
### 身份门 proposal（**未证伪 / not-falsified**，交 RULE/CONFLICT lane）

- 提案：在 §8.2 自查表加一条「**身份门：P1≥中 ∧ P2≥中 ∧ P4≥中，三者同时成立才允许打 bosch 标签；否则即使生物计数达标也判 not_bosch**」。
- 依据一致性：与 [bosch.md](../../dossiers/bosch.md) §10-9 L314「量化阈值为归纳、未实测，组合实验可按 §8.2 自查表回改」口径一致；与 §4 L106 逐字一致。
- **状态判定（关键）**：反例 A **没有证伪**这条提案，也**没有验证**它 —— 因此按「**作为 not-falsified 的设计候选保留（carried as not-falsified）**」登记：
  - 不升级为 `validated_rule` / `not falsified ≠ 通过`；
  - 本 lane **未**在真实图像/生成帧上跑像素实测（分母＝假想参考帧，§8.2 L242）、**未**跑组合实验、**未**宣称学习收益；
  - 不写入 [bosch.md](../../dossiers/bosch.md)、不改 §8.2、不改 `conflicts.md`（NO repo writes）；
  - 交 RULE/CONFLICT lane 定夺；若未来出现「P1 弱但其余强仍应判博斯」的具体可复现反例，按 §10-9 L314 回改。
- 与 [learning_path.md](learning_path.md) §4 rung3 / §6、[how-to-think.md](how-to-think.md) D8、[claim_evidence_map.md](claim_evidence_map.md) §D 同一口径。

<a id="db-source-line-73"></a>
### near-miss §4 缺口（登记，不补写）
- `conflicts.md` §4 near-miss 表无 bosch 行（全文 0 命中）；反例 A 暴露的「身份门」属「应补第 9 条自查项」而非 near-miss 表冲突行。AUDIT 的同类缺口（如 blake 的 near-miss 行）按「应补未补」登记，本 lane 不越权补 `conflicts.md`。

<a id="db-source-line-76"></a>
## §E 每条机制的失败条件速查（汇总）

| 机制 | 失败信号 | 定位 |
|---|---|---|
| 多联画/三幕 | 只剩单事件、无三幕/无成对 | L42、L102、L240、L389–L392 |
| 想象生物群 | 单物种畸变/等比放大、<3 混合体 | L35、L56、L100、L235、L107 |
| 道德叙事 | 形象不可逐件解码、纯奇观 | L67、L69、L86–L89 |
| 全景编目 | 单一焦点 >20%、地平线压低、<5 单元 | L33–L34、L99、L233–L234 |
| 平光环境光 | 单点戏剧主光/提灯证据光 | L38、L238、L81 判据④ |
| 宝石谱 | 土黑主调收窄、P6 弱 | L39、L104、L239、L107 |
| 身份门 | 只跑 §8.2-3+§8.2-8 就下「博斯」结论 | L106、L242、反例 A |
| 分工边界 | 折中成「灰调怪物」、借他模块机制 | L82、L90–L91、card L78 |
| 零自述纪律 | 写「博斯说/他认为/他的意图」 | L7、L306、corpus L4/L211、00-GOAL L9 |

<a id="db-source-line-90"></a>
## §F 10 张公开图权利行（1 PDM / 8 PD / 1 CC0，2 张归属争议保留）

> 逐张照录 `AUDIT-bosch/rights_review.md` §1 + `rights_review.json`；口径 = 本机 manifest 声明级（`declared_*`），本 lane **未联网复核**许可页、**未目检像素**（`image_seen=0`）、不含凭据。文件字节 sha256 全 10 张在 `rights_review.md` §2 / `rights_review.json → images[].file_sha256` 留存，本表不重抄 64 位长串以免抄录误差。

| # | file | 作品 | license label | 判定 | 归属争议 |
|---|---|---|---|---|---|
| 1 | `bosch/garden_of_earthly_delights.jpg` | 人间乐园三联（Prado P002823） | **Public Domain Mark**（PDM-owner，Prado 摄影复制品） | declared_PDM | — |
| 2 | `bosch/haywain_triptych.jpg` | 干草车三联（Prado P002052） | Public domain | declared_PD | — |
| 3 | `bosch/last_judgment_vienna.jpg` | 最后的审判（维也纳） | Public domain | declared_PD | — |
| 4 | `bosch/temptation_of_st_anthony.jpg` | 圣安东尼的诱惑（里斯本） | Public domain | declared_PD | — |
| 5 | `bosch/ship_of_fools.jpg` | 愚人船（Louvre RF 2218） | Public domain | declared_PD | — |
| 6 | `bosch/death_and_the_miser.jpg` | 死神与守财奴（NGA 1952.5.33） | **CC0**（NGA Open Access / IIIF） | declared_CC0 | — |
| 7 | `bosch/seven_deadly_sins.jpg` | 七宗罪与四末（Prado P002822） | Public domain | declared_PD | **争议保留**：BRCP 2015 追随者 / Prado 维持博斯 |
| 8 | `bosch/adoration_of_the_magi.jpg` | 三王来拜（Prado P002048，WGA） | Public domain | declared_PD | — |
| 9 | `bosch/christ_carrying_the_cross_ghent.jpg` | 负十字架的基督（根特 MSK 1902-H） | Public domain | declared_PD | **争议保留**：BRCP/2001 鹿特丹展判追随者 1530–40 |
| 10 | `bosch/cutting_the_stone.jpg` | 取出愚石（Prado P02056） | Public domain | declared_PD | — |

- **分布核对**：PDM 1（#1）+ PD 8（#2–#5、#7、#8、#9、#10）+ CC0 1（#6）= **10 行**；与 `coverage-manifest.json → images_audit.license_distribution {PDM:1, PD:8, CC0:1}`、`rights_review.md` §0 一致。
- **2 张归属争议保留**：#7 `seven_deadly_sins.jpg`、#9 `christ_carrying_the_cross_ghent.jpg` 仍收录、逐张标注；争议是**归属状态，不是权利缺口**（两张许可字段仍为 PD）；对应 [bosch.md](../../dossiers/bosch.md) §10-6 L311、§12-7/-9。
- **注 A（PDM-owner，不猜测 PD）**：#1 为「权利人对复制品的标记」，不是「作品已进公有领域」的自动推断；照抄标签为 `declared_PDM`，不升级为 PD（`rights_review.md` 注 A、dossier 自审 B-6 L460）。
- **unknown 项如实保留**：逐张 Commons imageinfo 许可/尺寸复核、馆方许可页取证、10 张像素目检均未在本轮做 → 「许可真实性 / 视觉内容与标题相符」为 `unverified`，不是 supported 也不是 defect。
- **私有层**：dossier §10-10 L315 记 1 件 NGA 全尺寸研究副本入私有层、1 件 Wikimedia 429 受阻；为公开 10 张之外的补充，不减少 `images_public=10`；本 lane 未读 `_private/INVENTORY_bosch.md`（非本 lane 输入）。

<a id="db-source-line-113"></a>
## §G 边界与状态

1. 全部阈值为 `[归纳]` 未实测（L242、§10-9 L314）；反例 A / 身份门为 `[inference]` / design_candidate **未证伪**，不等于验证通过；本 lane 不实测、不跑生成帧、不宣称学习收益。
2. `[自述]=0`：26 条语料零自写（L7、L306、corpus L4/L211、`coverage-manifest.json → zero_self_statements=true`）；本文件 §A–§F 全部为操作规则/档案记录，不冒充作者心理。
3. `conflicts.md` 零 bosch 专属行 + 7 处行号漂移 + near-miss 8-vs-16 口径：只报告、不修复（NO repo writes）。
4. 4 次外部取证（RF-01..04）沿用 AUDIT，本 lane 未新抓；原始特许状/意大利语原文/1788 首版/普拉多 Wayback 未回查，相关行 `partial`/`unverified` 保留。
5. 本产物 `submitted` / `review:null` / `human_review:not_applicable`；作者不自接受，待独立审者 gate。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
