<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-de_chirico；原正文 SHA-256 `810b5553a0fb3d663b499c4e91434d3a679b8353f49ccaea20916519423be5dd`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-de_chirico — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-de_chirico/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 9b3b2dfcce7ceddf（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 801b2445d4f9071f（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/de_chirico.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `cc0f61fa949289cfc5f933165449490cd31c8f69c956b88cd4a8f0aee62ba722`；`§0`、`§1`、`§4`、`§8.2:L244-257`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [de_chirico.md](../../modules/de_chirico.md) sha256 `914832f4b7ea3e1d650f3b201ed6cc7f2b99226057ae792301c5c0ae9b2ef124`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [de_chirico.md](../../dossiers/_corpus/de_chirico.md) sha256 `39ad269f8f8847443d5ff61096174e4dd471511a343d21835a3afce84fe9d0c7`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/de_chirico.md:L247` §8.2-1「\| 1 \| **超长投影** \| 主投影长度 ÷ 投影源高度 ≥2.5；投影边缘过渡带 ≤2 px；投影方向直方图主峰 ±5° 内占比 ≥80%（允许 ≤1 处矛盾影） \| 投影主轴角度直方图 + 长度比测量 \|」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/de_chirico.md:L248` §8.2-2「\| 2 \| **人烟预算** \| 真人连通域 = 0（若出现 ≤1 且面积 ≤2%、无视线交汇）；非人形体（雕像/模型/影子）1–3 个 \| 人物检测 + 面积与视线向量检查 \|」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/de_chirico.md:L249` §8.2-3「\| 3 \| **古典构件** \| 拱/柱/塔/墙/三角楣 ≥4 类；现代构件（玻璃幕墙/霓虹/现代招牌/车辆）像素占比 ≤0.5%；画面内可读现代文字 = 0 \| 构件分类检测 + 文字检测 \|」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/de_chirico.md:L250` §8.2-4「\| 4 \| **封闭透视** \| 单点透视：消失点位于画内建筑/墙之上或被其覆盖（不可达画外）；地平线高度 30–55%；≥2 条透视线收束角误差 ≤5° \| 直线段霍夫变换 + 消失点拟合 \|」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/de_chirico.md:L251` §8.2-5「\| 5 \| **色域与平涂** \| 色相簇 ≤8；砖红+赭+深绿+蓝绿四族合计 ≥60%；平均饱和度 ≤0.45；荧光/霓虹色（S ≥0.7 且 H ∈[160,200]∪[300,340]）≤1%；单色块内部明度标准差…」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/de_chirico.md:L252` §8.2-6「\| 6 \| **硬边** \| 明暗/影边界过渡带中位数 ≤2 px（1024 px 宽画布）；无 ≥8 px 羽化；影块为简单多边形（边数 ≤6） \| 梯度宽度统计 + 形状简化度 \|」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/de_chirico.md:L253` §8.2-7「\| 7 \| **静默（动画附加）** \| 相机固定；帧间差 ≤1%；允许运动仅蒸汽/云 ≤0.5%/s 漂移（或全静止） \| 帧差图 + 漂移拟合 \|」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/de_chirico.md:L254` §8.2-8「\| 8 \| **舞台构成** \| 前区铺地（下缘 1/4 高度带）为空 ≥25% 画面；≥1 个画中框（拱/门/墙洞）或被画边裁切；主体建筑中轴偏移 ≤1/6 画宽 \| 分区覆盖统计 + 边界相交检测 \|」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（12 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/de_chirico.md:§1-1`「\| 1 \| **空旷广场（piazza）作为舞台** \| 大面积石铺前区（常 ≥25% 画面）＋围合建筑＋高地平线；真人≈0；画面「等一场不会发生的事件」 \| `[研究]`（[R26] Tate：「D…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/de_chirico.md:§1-2`「\| 2 \| **超长投影（low-sun cast shadows）** \| 低角度日光造成**被拉长的硬边投影**，横贯铺地、跨越画面；投影与物体高度比常 ≥3；投影本身成为构图主角 \| `[研究]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/de_chirico.md:§1-3`「\| 3 \| **古典建筑构件** \| 拱廊/柱廊/拱门/砖塔/烟囱/高墙/三角楣/钟表；「意大利性」的形体语汇（非现代都市构件） \| `[研究]`（[R26][R34]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/de_chirico.md:§1-4`「\| 4 \| **雕像与人体模型（statues / mannequins）** \| 石膏像、古典头像、裁缝人体模型、无头躯干——**「人的在场」以非人形式出现**；人像无面孔/无目光交流 \| `[研究…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/de_chirico.md:§1-5`「\| 5 \| **封闭透视（closed perspective）** \| 单点/多点透视的消失点被墙、建筑或影封堵（无出口）；Tate 词条：「distorted perspective … unde…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/de_chirico.md:§1-6`「\| 6 \| **意大利黄昏调色板** \| 赭黄铺地、砖红、深绿、藏青/墨绿阴影；天空常为**翠绿或深蓝绿**（非自然天蓝）；大面积平涂、色块边界清晰 \| `[研究]`（[R26]：「emerald g…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/de_chirico.md:§1-7`「\| 7 \| **火车与「时间机器」** \| 静止/半静止的蒸汽火车（白色固体状蒸汽）、钟表、日晷、地图——时间的物件化；火车常被墙挡住只露烟柱 \| `[研究]`（[R26][R19]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/de_chirico.md:§1-8`「\| 8 \| **物件的谜式并置（enigmatic juxtaposition）** \| 不相干的物同框且**无叙事连接**：橡胶手套、饼干、洋蓟、香蕉、绿球、蛋、地图、鱼形浮雕（[R26][R37]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/de_chirico.md:§1-9`「\| 9 \| **硬边与线描性** \| 轮廓线明确（Tate：heavy black outlines、crude hatching lines「像素描或版画」）；形体平、体积感靠**影**不靠渐变 \|…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/de_chirico.md:§1-10`「\| 10 \| **无事件（no event）** \| 画面没有动作、没有叙事高潮、没有可发生的下一步；Tate 语：「atmosphere of mystery and enigma」 \| `[研究]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F11 | `dossiers/de_chirico.md:§1-11`「\| 11 \| **影子/背影的人形** \| 偶发人形＝无面剪影、背对者或**影子本身**（「a man who walks in the sun」的影）；不提供表情信息 \| `[归纳]`（据 [R16][R18] 等；与 §3.1 判据④同轴） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F12 | `dossiers/de_chirico.md:§1-12`「\| 12 \| **舞台正面性（theatrical staging）** \| 构图近剧场布景（1914 年曾被批评为「scenery」，他抗议——「his works had nothing to do with scenery … proved by their titles」）；正面/微斜视点、建筑居中 \| `[史料/研究]`（[R26]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-46"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/de_chirico.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/de_chirico.md:§8.2 尾注:L256`「> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 [style_card.md](../../../../../templates/style_card.md) 的填写规则对齐。第 1/2/3 条与 §3.1 判据③④①同轴，组合实…」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-de_chirico/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-54"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 f43099c3c682e3d3（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-de_chirico/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-de_chirico/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **31 行**（§A5+§B8+§C12+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
