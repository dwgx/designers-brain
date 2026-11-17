<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-artemisia_gentileschi；原正文 SHA-256 `b6370525e59aca07c56ecc2a7adb5fcd155b2bfd16c60912ea75302bf6c5988f`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-artemisia_gentileschi — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-artemisia_gentileschi/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 d06921edbc01daa8（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 cc37523955c6de57（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/artemisia_gentileschi.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `d96a2c6b3c5c48c814c5c352fb14eb3dfda16b8e90ed239cb44879c2e12c61e0`；`§0`、`§1`、`§4`、`§8.2:L190-200`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [artemisia_gentileschi.md](../../modules/artemisia_gentileschi.md) sha256 `477149b4d510979e7f4e8045ec82b1dde4f12b88a9519255624604a8b19ca81a`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [artemisia_gentileschi.md](../../dossiers/_corpus/artemisia_gentileschi.md) sha256 `db0dca32cb680780fc16dff787fb2fb39f0b11f89700235cbdae2bc497699291`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 7 条规则逐条回源（7 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/artemisia_gentileschi.md:L191` §8.2-1「1. **叙事光源规则**：全帧可见光源计数 ∈ {0, ≥1}；**≥1 时必须是叙事道具**（烛/灯/火）且与人物/动作发生交互（被手持、被遮蔽、照亮接触点）；环境补光强度 ≤ 主光的 5%。（自查：光源检测 + 交…」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/artemisia_gentileschi.md:L192` §8.2-2「2. **光斑—动作绑定规则**：最亮连通域（亮度 ≥0.9×max）质心到「动作轴」（施力手→接触点→受力者）的距离 ≤10% 画宽；高光连通域数量 ∈ [2, 6]，每个必须与「手 / 脸 / 叙事物」之一相交。（自…」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/artemisia_gentileschi.md:L193` §8.2-3「3. **做功规则**：≥1 人物小臂裸露或衣袖卷起；前臂长轴与叙事动作方向夹角 ≤30°；接触点（手/武器/工具与对象）在画面内可见且 ≥1 处受光。（自查：姿态估计 + 接触点检测；对照 §3.1 判据③）」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/artemisia_gentileschi.md:L194` §8.2-4「4. **定格规则**：运动模糊核 = 0；动作极值帧唯一（最大位移向量方向唯一）；无补间残影、无速度线。（与 C-08 对齐：定格类全片 0 帧运动模糊）」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/artemisia_gentileschi.md:L195` §8.2-5「5. **暴力物证规则**：暴力场景物证数 ≥1（血弧 / 血渍 / 尸首 / 凶器），且「新鲜度」可读（血未干、凶器仍在手或旁侧）；血/器用高饱和红（HSV 红相 ±20°）或金属高光，合计面积 ≤8% 画面。（对照…」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/artemisia_gentileschi.md:L196` §8.2-6「6. **复合情绪规则**：≥1 张脸具备 ≥2 条情绪线索（眉/眼/嘴/头部方向的不一致组合，如「手在杀、脸在忍」）；全帧「单一尖叫脸」数量 ≤1；视线方向 ∈ {目标, 出口, 观者} 且至少两处视线不共向。（自查：…」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/artemisia_gentileschi.md:L197` §8.2-7「7. **贴平面与暗部规则**：主体包围盒 ≥70% 画幅、≥1 主体被画幅边缘裁切；暗区（V<0.25）占比 ≥35%；暗部保细节（暗区内部亮度标准差 ≥1.5/255）；纯黑像素（=0）占比 ≤10%。（自查：分割…」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-28"></a>
## §C §1 视觉指纹（10 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/artemisia_gentileschi.md:§1-1`「\| 1 \| **事件进行时（或刚过去）**：专画动作的极值或余波——不画前因、不画全景；定格但保留「势能」。**心理在现场**：动作与情绪同时可读 \| 动作链（施力→接触→受力）≥2 环同框；无远观全…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/artemisia_gentileschi.md:§1-2`「\| 2 \| **女性合力**：致命动作由**两个女性共同完成**（或女性对男性施力）；为「合力」甚至改写经文细节——Abra 被放进帐篷内（经文里她等在外面） \| 施力者 ≥2 且同一动作；接触点被两…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/artemisia_gentileschi.md:§1-3`「\| 3 \| **身体在做功**：卷起的袖子、裸露小臂、绷紧的肌肉、可见的用力方向；**手是第二主角**（多双手同时在光里） \| ≥1 人物卷袖/露臂；施力方向与动作一致；高光连通域与「手」相交；手臂长…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/artemisia_gentileschi.md:§1-4`「\| 4 \| **有动机的光**：单光源多为侧光/烛光；**画内光源可出现且承担叙事**（底特律版画内烛台；乌菲齐版隐含帐灯）；光斑沿**动作链**分配——照亮施力点、接触点、受力点 \| 主光方向单一（…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/artemisia_gentileschi.md:§1-5`「\| 5 \| **硬边明暗（与卡拉瓦乔同族）＋大块亮织物**：背景近黑，但**白床单/衣袖/丝绸**是事件舞台——大面积高亮织物承接光；血/器/首级是叙事标点 \| 暗区（V<0.25）占比 ≥40%；≥…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/artemisia_gentileschi.md:§1-6`「\| 6 \| **暴力物证（新鲜度）**：喷射的血弧（乌菲齐版）、床单上的血渍、篮中首级、仍握在手里的凶器——暴力有**物理后果** \| ≥1 件「新鲜」暴力物证（血未干、首级在场）；血/器用高饱和红/…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/artemisia_gentileschi.md:§1-7`「\| 7 \| **复合情绪的面孔**：决心+厌恶、恐惧+专注、后怕+警觉——不是单一尖叫；**视线方向承担叙事**（Judith 看血与出口、Abra 看门/看风） \| ≥2 条情绪线索同时可读；视线方…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/artemisia_gentileschi.md:§1-8`「\| 8 \| **贴平面＋裁切**：人物被推到画面最前、被边缘裁切；动作轴为对角线；空间浅、背景压暗但保留织物/帐幕的空间暗示 \| 主体包围盒 ≥80% 画幅；≥1 主体被裁切；动作轴与画面对角线夹角…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/artemisia_gentileschi.md:§1-9`「\| 9 \| **色域：土色底＋四色家族**：赭/棕/黑为底；**蓝**（朱迪斯裙）、**红**（衣/血）、**金/黄**（丝绸/灯焰）、**白**（床单）四族点缀；饱和色集中在叙事物上 \| 全帧中位饱…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/artemisia_gentileschi.md:§1-10`「\| 10 \| **物证级细节**：珠宝、剑柄、床帐、发丝——Longhi 称其衣装细节出自「全欧最讲究的衣橱」（Casa Gentileschi）；织物褶皱可数、金属高光小而准 \| 织物褶皱分辨率高；…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-43"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/artemisia_gentileschi.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/artemisia_gentileschi.md:§8.2 尾注:L199`「> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1/2/3/6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。与 `conflicts.md` 的关系：…」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-artemisia_gentileschi/mechanism_notes.md:§5`（7 条 counters，逐条回指 §8.2-1…§8.2-7） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-51"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 e239325f8a513387（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-artemisia_gentileschi/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-artemisia_gentileschi/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **28 行**（§A5+§B7+§C10+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 7 行 = dossier §8.2 的 7 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
