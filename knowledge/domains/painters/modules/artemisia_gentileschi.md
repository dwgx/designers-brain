# 阿尔泰米西娅·真蒂莱斯基 模块卡 — `artemisia_gentileschi`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/artemisia_gentileschi.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **事件进行时（或刚过去）**：动作链（施力→接触→受力）≥2 环同框；无远观全景视角；画面时间＝「正在/刚发生」——心理在现场
2. **女性合力＋身体在做功**：施力者 ≥2 共担同一动作（为合力改写经文细节）；卷袖/露臂、用力方向可见；手是第二主角
3. **有动机的光**：主光单一侧光/烛光；画内光源（烛台）可承担叙事；光斑沿动作链分配（最亮区与动作轴相交）
4. **硬边明暗＋大块亮织物＋暴力物证**：暗区（V<0.25）≥40%；≥1 块高亮织物（≥10% 面积）；血弧/血渍/首级/凶器——暴力有物理后果
5. **复合情绪面孔＋贴平面裁切＋物证级细节**：≥2 条情绪线索（决心+厌恶）可同时读；主体 ≥80% 画幅、被边缘裁切；土色底＋蓝/红/金/白四色家族集中于叙事物；织物褶皱与金属高光小而准

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Artemisia Gentileschi-style dramatic narrative painting — the psychological scene at the moment it happens:
one or two women acting with full bodily force — sleeves rolled up, forearms bare and tense,
both hands visible at the point of action, gripping a sword, a hammer, a tent peg;
the action held at its extreme, or in its breath-held aftermath;
a single raking light with a narrative source — a candle, an oil lamp, a brazier, a tent opening —
the brightest passages falling along the chain of action: the striking arm, the resisting flesh, the deciding face;
hard-edged chiaroscuro across faces and arms, narrow and explicitly placed penumbra, no fill light;
large pale textiles as the stage — rumpled sheets, linen sleeves, silk drapery catching the light;
warm flesh against near-black interiors; a restricted earth palette of ochre, umber and bitumen black
with a few saturated accents — a lapis-blue gown, a crimson blood arc, a gold chain;
blood as physical evidence — a spurting arc, a stain on white linen, a severed head in a basket;
compound emotion on the faces — resolve mixed with disgust, fear mixed with focus — never a single scream;
the scene legible as shared labour, a domestic chore done with terrible force;
figures pressed close to the picture plane, cropped by the frame, leaning into the viewer's space;
17th-century Italian Baroque, oil on canvas, Caravaggesque tenebrism with narrative light
```
**负向约束（`--no` 风格）**
```
--no soft diffuse lighting, ambient fill light, multiple light sources, rim light, glow, bloom,
volumetric god rays, evenly lit scene, bright background, daylight landscape, sky, open air,
idealised heroic nudity, sculptural marble anatomy, ecstatic martyrdom spectacle,
serene faces, single flat emotion, glamour beauty, pastel palette, neon colours,
abstract shapes, decorative gold leaf, ornament flatness, cartoon, anime, 3D render,
HDR gloss, motion blur, speed lines, sequence panels, comic strip, text, watermark
```

## 代码艺术规则（§8.2 原样）

1. **叙事光源规则**：全帧可见光源计数 ∈ {0, ≥1}；**≥1 时必须是叙事道具**（烛/灯/火）且与人物/动作发生交互（被手持、被遮蔽、照亮接触点）；环境补光强度 ≤ 主光的 5%。（自查：光源检测 + 交互关系检查；对照 §3.1 判据①）
2. **光斑—动作绑定规则**：最亮连通域（亮度 ≥0.9×max）质心到「动作轴」（施力手→接触点→受力者）的距离 ≤10% 画宽；高光连通域数量 ∈ [2, 6]，每个必须与「手 / 脸 / 叙事物」之一相交。（自查：亮度质心 + 动作轴拟合；对照 §3.1 判据②）
3. **做功规则**：≥1 人物小臂裸露或衣袖卷起；前臂长轴与叙事动作方向夹角 ≤30°；接触点（手/武器/工具与对象）在画面内可见且 ≥1 处受光。（自查：姿态估计 + 接触点检测；对照 §3.1 判据③）
4. **定格规则**：运动模糊核 = 0；动作极值帧唯一（最大位移向量方向唯一）；无补间残影、无速度线。（与 C-08 对齐：定格类全片 0 帧运动模糊）
5. **暴力物证规则**：暴力场景物证数 ≥1（血弧 / 血渍 / 尸首 / 凶器），且「新鲜度」可读（血未干、凶器仍在手或旁侧）；血/器用高饱和红（HSV 红相 ±20°）或金属高光，合计面积 ≤8% 画面。（对照 C-12 色相预算：显式取值）
6. **复合情绪规则**：≥1 张脸具备 ≥2 条情绪线索（眉/眼/嘴/头部方向的不一致组合，如「手在杀、脸在忍」）；全帧「单一尖叫脸」数量 ≤1；视线方向 ∈ {目标, 出口, 观者} 且至少两处视线不共向。（自查：面部关键点 + 视线向量；对照 §3.1 判据④）
7. **贴平面与暗部规则**：主体包围盒 ≥70% 画幅、≥1 主体被画幅边缘裁切；暗区（V<0.25）占比 ≥35%；暗部保细节（暗区内部亮度标准差 ≥1.5/255）；纯黑像素（=0）占比 ≤10%。（自查：分割 + 直方图；与卡拉瓦乔 §8.2 同侧但阈值放宽——阿的叙事光允许亮织物大面积在场）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1/2/3/6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。与 `conflicts.md` 的关系：**C-01**（硬阴影——阿站硬光侧，反约束改写）、**C-08**（运动模糊——全片 0 帧）、**C-11**（高光计数——阿站「少而准」侧）、**C-12**（色相预算——四色家族显式取值）、**C-13**（阴影色相——深棕/黑）为组合预检重点。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **叙事光动机强度（Narrative Light Motivation）**`[归纳]` | 纯画外抽象光（最接近卡拉瓦乔档：光只作照明） | 画内可指认光源（烛/灯/火），但仅作照明 | 光源＝叙事道具：照亮动作两端、参与构图、可被人物遮蔽/手持（底特律烛台档） | **60%** |
| P2 | **动作张力（Action Tension）**`[归纳]` | 静默余波（事件后数分钟：聆听、撤离、后怕） | 动作进行中（对峙、预备、试探） | 动作极值（刃入、锤落、血在喷；决定性瞬间） | **70%** |
| P3 | **身体做功度（Bodily Exertion）**`[归纳]` | 单人静态（站/坐/持物，观者姿态） | 单人用力（一人施加、一人承受） | 双人合力：卷袖、接触点高光、肌肉用力方向可读 | **75%** |
| P4 | **暴力物证密度（Violence Evidence）**`[归纳]` | 0–1（仅武器暗示，无血） | 1–2（血渍 / 首级在篮 / 染血织物） | ≥3 同屏（血弧＋血渍＋尸首＋凶器） | **55%** |
| P5 | **心理复合度（Psychological Complexity）**`[归纳]` | 单一情绪（恐惧或决心，单点） | 2 条情绪线索（决心＋厌恶；恐惧＋专注） | 复合＋错位（手在杀、脸在忍；受害者视角的余悸；视线与动作分离） | **70%** |
| P6 | **贴平面/裁切度（Cropping）**`[归纳]` | 全身远景（主体 ≤60% 画幅，空间可读） | 大半身（60–80%，背景压暗） | 主体 ≥80% 画幅、被边缘裁切、前景物越出画面（底特律/乌菲齐档） | **70%** |

> **用法**：P1/P3 定「是不是真蒂莱斯基」的叙事档（两条中 ≥1 条 ≥ 中档才成立——光有动机或身体在做功）；P2/P4 定事件档（余波 → 极值；物证密度）；P5/P6 定心理与构图档。三档描述可直接当判定标准写进自查表。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若「画外单光＋零叙事动机＋光斑按脸/手/道具静物式分布」→ 越界**卡拉瓦乔**（P1 弱档连用即越界）；② 若「英雄化裸体＋仪式化大场面＋无新鲜物证」→ 越界**米开朗基罗**；③ 若「光在面部连续衰减＋单脸静观＋无动作链」→ 越界**伦勃朗**；④ 若「序列化/讽刺/黑白版画语言」→ 越界**戈雅**；⑤ 若「柔窗光＋点状高光＋无硬边」→ 越界**维米尔**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 卡拉瓦乔）**（× 卡拉瓦乔；本卡 §3.1 分工条款）：硬光同族分档写死：叙事动机（光沿动作链＋画内光源可叙事＋身体做功）vs 开关/物理——判定须 ①②③④ ≥2 轴联合成立（不得只看表情轴）
- **分工（vs 米开朗基罗）**（× 米开朗基罗；本卡 §3.1 分工条款）：力量：真实档（日常衣装＋劳动身体＋新鲜物证）vs 理想档（英雄裸体＋仪式化大场面）——判据四条
- **分工（vs 伦勃朗）**（× 伦勃朗；本卡 §3.1 二级注）：事件心理（多体＋动作链＋行动时间）vs 肖像心理（单脸＋连续衰减＋静观时间）
- **C-01 / C-08**（× Lane B；本卡 §3.1 组合预检）：硬光侧：反约束句按 C-01 改写并显式给出半影宽度；定格瞬间＝全片 0 帧运动模糊
- **C-11 / C-12 / C-13**（× 卡拉瓦乔 / 维米尔 / 塞尚；本卡 §3.1 组合预检）：高光站「少而准」侧；土色底＋四色家族显式取值；阴影色相深棕/黑

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/artemisia_gentileschi.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
