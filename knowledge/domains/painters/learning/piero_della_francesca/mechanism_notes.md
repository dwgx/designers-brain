<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-piero_della_francesca；原正文 SHA-256 `f32171064b2edb152658f26d9ee70429c72718eedb32813b973ebaf033f3b9f5`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-piero_della_francesca — mechanism_notes（机制笔记 / 皮耶罗·德拉·弗朗切斯卡）

> 本笔记把 dossier [piero_della_francesca.md](../../dossiers/piero_della_francesca.md) 的 §4 六参数、§8.2 **8 条**可判定规则、§1 指纹、§3 原则拆成「可迁移关系 + 失效边界」。全部阈值 `[归纳]`/`[UNVERIFIED]`，未做像素测量（分母＝假想参考帧），不得当作 validated_rule 或 E4 pass。[LEARN-piero_della_francesca]
> Rule-id counter（逐条 verbatim，分母＝§8.2 头部声明 8 条，实测解析 8 条）：§8.2-1, §8.2-2, §8.2-3, §8.2-4, §8.2-5, §8.2-6, §8.2-7, §8.2-8 —— **count=8 = hdr=8，一致**。[LEARN-piero_della_francesca]

<a id="db-source-line-6"></a>
## §A 适用模式与可检验假说（先选分支，不逐条强制串联）

原来的相邻 R1×R2、R2×R3、R3×R4、R4×R5、R5×R6 只能作为待检验的项目耦合假说；相邻编号和 N3 轴单主约定不证明必然依赖或因果关系。先分别列出几何、光照、色域与姿态条件，再提出只改变一个变量的局部比较。

| 条件 | 适用检查与记录边界 |
|---|---|
| day／night | 依据 dossier §4 P3 选择。R4 仅用于 night 画内光源分支；day 的 R4 = 不适用，不是失败或成功。 |
| 有可读投影 | 在声明适用的光照模型下检查 R3/R8；源 §12《鞭笞》的分区照明不能默认为全帧单光。 |
| 有意省影／无法判定 | §12《降生》允许作为表达比较；有意省影不提供阴影物理通过证据，资料不足记 unknown，不能将检测不到等同于不适用。 |
| still／video | 静态图只检查可见姿态、轮廓和模糊线索，不能产生光流证据；视频有足够帧与测量时才评 R6 光流。 |
| symmetry／非对称 | R6 镜像阈值仅在已声明对称构图时启用；非对称分支不据此判风格失败。 |
| 色域／对象／画幅 | R5 针对选择的浅色域模式；彩色本身允许。R1 的地面条件、R7 的建筑等统计对象须存在或另记不适用／未知，不能制造空分母通过。 |

源 §8.2 数值原样保留为未校准的项目代理。某条件不适用不表示全图获准；需要完整风格判断时仍要人工说明采用哪些模式及遗漏了哪些语义条件。

<a id="db-source-line-21"></a>
## §B §8.2 规则逐条（8 条，原文照录 + 自查）

<a id="db-source-line-23"></a>
### §B-1 — §8.2-1 · 轴线与网格规则
- 原文（照录 dossiers/piero_della_francesca.md §8.2 规则 1）：1. **轴线与网格规则**：画面含 **≥1** 条贯穿性垂直主轴（贯穿 ≥80% 帧高）；主要人物质心与轴线水平偏差 **≤2%** 帧宽；若有地面，网格/地砖行可数 **≥6** 行且近大远小单调。自查：列梯度投影 + 质心检测 + 地砖行计数。（依据：[R1] "the strict alignment of the dove, the bowl and Christ's praying hands"；网格结构）
- grade：`[归纳]` 阈值（未经渲染实验校准，`[UNVERIFIED]`）；自查方法见该行「自查：」段。
- 决策位：先声明轴线／人物及地面是否存在，再检查本条；不自动要求下一条通过。

<a id="db-source-line-28"></a>
### §B-2 — §8.2-2 · 透视收敛规则
- 原文（照录 dossiers/piero_della_francesca.md §8.2 规则 2）：2. **透视收敛规则**：建筑/地面直线元素向 **≤2** 个消失点收敛，拟合角度误差 **≤1.5°**；进深方向尺度比单调递减。自查：Hough 直线拟合 + 消失点求交。（依据：[R18] "precise perspective representation of space"；[R11] 贝壳穹顶可推算）
- grade：`[归纳]` 阈值（未经渲染实验校准，`[UNVERIFIED]`）；自查方法见该行「自查：」段。
- 决策位：有建筑／地面直线且视点假设明确时检查收敛；局部控制见 learning_path P-E1。

<a id="db-source-line-33"></a>
### §B-3 — §8.2-3 · 光一致规则
- 原文（照录 dossiers/piero_della_francesca.md §8.2 规则 3）：3. **光一致规则**：全帧投影方向夹角 **≤10°**；阴影长度 **≤物高 25%**（低斜度光）；无第二主光源（亮度次峰 ≤主峰 30%）。自查：阴影区域方向直方图 + 影长比。（依据：[R19] 影的透视计算；[R1] 晨光浅影）
- grade：`[归纳]` 阈值（未经渲染实验校准，`[UNVERIFIED]`）；自查方法见该行「自查：」段。
- 决策位：先选光照模式及阴影可见性；有意省影或资料不足不写本条物理 PASS。

<a id="db-source-line-38"></a>
### §B-4 — §8.2-4 · 画内光源规则（夜景档）
- 原文（照录 dossiers/piero_della_francesca.md §8.2 规则 4）：4. **画内光源规则（夜景档）**：夜景中全帧最亮连通域中心与可见发光体（天使/灯）距离 **≤5%** 帧宽；亮度沿距离**单调衰减**（径向拟合 R² ≥0.8）。自查：亮度场径向衰减拟合。（依据：[R16] "illumined by the light which proceeds from the angel himself"）
- grade：`[归纳]` 阈值（未经渲染实验校准，`[UNVERIFIED]`）；自查方法见该行「自查：」段。
- 决策位：仅 night 画内光源分支适用；day 为不适用，不是前后规则的必要条件。

<a id="db-source-line-43"></a>
### §B-5 — §8.2-5 · 浅色域规则
- 原文（照录 dossiers/piero_della_francesca.md §8.2 规则 5）：5. **浅色域规则**：全帧平均饱和度 **≤0.35**、明度中位 **≥0.55**；高饱和像素（S>0.75）面积 **≤3%**；主色相（面积 ≥2% 者）**≤5** 个。自查：HSV 统计。（依据：[R1] "pale tones"；[R2] 蛋彩→油彩的饱和度变化）
- grade：`[归纳]` 阈值（未经渲染实验校准，`[UNVERIFIED]`）；自查方法见该行「自查：」段。
- 决策位：在选定浅色域模式下检查饱和度等指标；pale blue／rose／crimson／ultramarine 不因是彩色而失败。

<a id="db-source-line-48"></a>
### §B-6 — §8.2-6 · 静止规则
- 原文（照录 dossiers/piero_della_francesca.md §8.2 规则 6）：6. **静止规则**：无运动模糊（模糊核 ≤1px，光流残差 ≤1px）；群像姿态镜像对称度 **≥70%**（若为对称构图）；直视画外者 **≤1**。自查：光流 + 镜像匹配 + 视线检测。（依据：[R14] "immobilità cerimoniale"；[R1] "find stillness"）
- grade：`[归纳]` 阈值（未经渲染实验校准，`[UNVERIFIED]`）；自查方法见该行「自查：」段。
- 决策位：静态与视频分开；光流需视频，对称阈值需事先声明对称构图。

<a id="db-source-line-53"></a>
### §B-7 — §8.2-7 · 几何轮廓规则
- 原文（照录 dossiers/piero_della_francesca.md §8.2 规则 7）：7. **几何轮廓规则**：云/树冠/山体轮廓可用 **≤6** 段折线近似（低多边形度）；建筑直线元素占比 **≥30%**；无碎片化高频轮廓。自查：多边形近似误差 + 直线占比。（依据：[R1] 鸽子前缩翅膀与云同形；[R6]）
- grade：`[归纳]` 阈值（未经渲染实验校准，`[UNVERIFIED]`）；自查方法见该行「自查：」段。
- 决策位：先声明云／树冠／山体／建筑等统计对象与分母；无适用对象或未知不得写数值 PASS。

<a id="db-source-line-58"></a>
### §B-8 — §8.2-8 · 投影几何规则
- 原文（照录 dossiers/piero_della_francesca.md §8.2 规则 8）：8. **投影几何规则**：**≥1** 处影子为可读几何形（圆/椭圆/多边形），其形状与光源方向自洽（误差 **≤15%**）；影可与主体构成视线路径（人工核）。自查：影子形状拟合 + 光向一致性。（依据：[R20] "the shadow cast by Jerome's legs that leads the eye … to the pages in his open book"）
- grade：`[归纳]` 阈值（未经渲染实验校准，`[UNVERIFIED]`）；自查方法见该行「自查：」段。
- 决策位：有可读影子及光源假设才检查；有意删影单列表达分支，不能据此声称投影几何已验证。


<a id="db-source-line-64"></a>
## §C §4 六参数三档（控制旋钮）
| P | 参数 | 默认 | grade |
|---|---|---|---|
| P1 | 几何秩序度（Geometric Order） | **70%** | `[归纳]` 三档 |
| P2 | 透视深度（Perspective Depth） | **75%** | `[归纳]` 三档 |
| P3 | 光的行为（Light Behavior） | **中（白昼均匀）** | `[归纳]` 三档 |
| P4 | 色域与表面（Palette & Surface） | **70%** | `[归纳]` 三档 |
| P5 | 静止与表情度（Stillness & Expression） | **75%** | `[归纳]` 三档 |
| P6 | 工作流参数（画幅体制） | **1**（单幅起步） | `[归纳]` 三档 |
- 三档（弱/中/强）原文见 [piero_della_francesca.md](../../dossiers/piero_della_francesca.md) §4；全部 `[归纳]`，档位划分本身 `[归纳]`。[LEARN-piero_della_francesca]

<a id="db-source-line-75"></a>
## §D 失效边界 / 强反例（纸面推演，no render）
| 边界 | 对象 | 判定 |
|---|---|---|
| D1 | §8.2-1 越界 | 已声明本条及其统计对象适用时，阈值不满足 → 局部 fail/not-satisfied；未知与不适用另记，纸面推演 `[inference]` |
| D2 | 题材与关系范围 | 物件名称可替换，但选定的几何—符号位置、光—叙事关系须保留或明确排除；不能宣称删掉这些关系仍完整验证该语义机制（dossier §3-5/§3-7、§12《降生》）。 |
| D3 | 冒充自述 | 仅 `[自述]`/`[self-written]` 可称本人言；§3 按各条原始等级引用；教学决策与 §8.2 数值是项目构造 |
| D4 | 把阈值当实测 | 未经像素测量/E4，交集与 near-miss 只记规则层，不升级 validated |
| D5 | 媒介越界 | 依据 module／§8.1 区分高饱和 neon、摄影感、3D render 等护栏；pale blue、rose、crimson、ultramarine 属允许的彩色范围，不能因“彩色”本身退档 |
- 反例是 `[inference]` 纸面推演：无渲染、无生成通道、无 E4；仅用于界定规则适用条件。[LEARN-piero_della_francesca]

<a id="db-source-line-85"></a>
## §E 定位方法与未决
- 所有 `文件 : 行号` 以基线 `f008952365a7…` 的 live 文件为准，开工 `sha256sum` 复核（见 RESULT §3）。[LEARN-piero_della_francesca]
- 未决：§4/§8.2 阈值未实测；[piero_della_francesca.md](../../dossiers/_corpus/piero_della_francesca.md) 外部原文/[R#] URL/扫描件未逐字回源（离线只读本机）；§8.3 野外样本状态沿用 AUDIT。由实验 lane 预注册后跑实测，本 lane 不越权。[LEARN-piero_della_francesca]
- `01-AUDIT.md` §8.1 A-30：练习是建议练习；`human_review.status=not_applicable`，`review:null` 作者不自接受。[LEARN-piero_della_francesca]

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
