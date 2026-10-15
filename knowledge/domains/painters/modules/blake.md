# 布莱克 模块卡 — `blake`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/blake.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **铁丝轮廓线（wirey bounding line）**：主要形体 ≥80% 由连续硬线围合（过渡 ≤1px）、线宽 2–3:1 变化——「分明、锐利、如铁丝一般」
2. **无排线明暗**：交叉排线 0 命中；灰阶交给手工水彩／彩色墨／留白——「反雷诺兹／反伦勃朗式涂抹」立场的图像化
3. **图文同版（页面即作品）**：文字为手写体蚀刻、与图同一印刷层同一墨色；文字区 5–40% 沿边／成条／环绕——「彼此增加意义」
4. **辐射光装置＋英雄裸体**：单中心辐射光场 ≥8%、射线 ≥6 条（光源在画内）；肌肉分明人体姿态违反重力（躯干轴偏离竖直 ≥15°）
5. **命名神谱锚点＋对称涡旋**：≥1 具名神话人物（Urizen／Los／Orc…）或谱系象征物；中心轴对称为主（≥60%）或涡旋辐射——对偶结构

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Blake-style visionary illuminated page — relief etching, text and image cut on the same plate and printed together:
firm wirey bounding outlines drawn with a flowing, flame-like hand — every form enclosed by a distinct sharp contour, line weight swelling and thinning 2-3:1, no cross-hatching anywhere, no tonal modelling by line density;
light and colour applied afterwards as translucent hand washes — pale blues, olive greens, ochre, rose madder, grey-violet, gold accents kept under 5% — flat within each zone, glowing rather than shaded; beneath the washes the print remains pure line on cream paper;
the composition reads as a page, not a painting: hand-lettered text (etched script, not typography) woven into the design — words curving along margins, sitting in bands above or below the figure, or dropping vertically through the image, in the same ink and the same etched line as the drawing;
a named figure from Blake's own pantheon — Urizen the bearded lawgiver with compasses and open book, Los the smith with hammer and tongs, Orc the youth wreathed in flames, Albion asleep, Enitharmon veiled — heroic muscular bodies, nude or semi-nude, in impossible gravity: soaring, diving, kneeling, arms flung wide, twisting on a spiral;
visionary apparatus: radiating beams from a single centre, orbs and sun-disks, clouds rolled like scrolls, pointed flames, stars, compasses, scales, an open book;
composition on a central axis or vortex — light radiating from one source, a circle, gothic arch or cave framing the scene, symmetrical wings of cloud;
small scale, dense detail, a thick ruled border; the whole page is one object — image, verse and frame inseparable
[single-colour variant] uncoloured line state — black ink only on cream paper, all energy in the contour and the etched script
```
**负向约束（`--no` 风格）**
```
--no crosshatching, --no hatched shading, --no tonal line-density gradients, --no stipple, --no mezzotint grain,
--no aquatint tone, --no sfumato, --no soft airbrush transitions, --no blurry edges, --no photographic realism,
--no oil-painting modelling, --no impasto, --no visible brush texture, --no dramatic chiaroscuro,
--no typographic or printed-font text, --no clean vector lettering on a separate layer, --no calligraphy flourish for its own sake,
--no flat modern vector illustration, --no 3D render, --no anime, --no watermark, --no cheerful pastel greeting-card mood
```

## 代码艺术规则（§8.2 原样）

1. **轮廓线规则**：≥3 个主要形体，各 ≥80% 边界有连续硬轮廓（边缘过渡带 ≤1px）；轮廓线宽变异比 2–3:1（铁丝/火焰感）。自查：Sobel 边缘 + 线宽剖面采样。（依据：[R12] E550）
2. **无排线规则**：交叉排线 **0 命中**——任何由 ≥2 层线交叉构成的阴影区不得出现；明暗由平涂色区承担（单区明度标准差 ≤12/255）。自查：线方向直方图 + 交叉检测 + 分区明度统计。（与 C-07 联动）
3. **图文同版规则**：≥1 处**手写体文字区**（面积 5–35% 页面），与图像同一墨色、同一质感层；文字为手写蚀刻感，不得为排印字体。自查：文字区检测 + 手写/排印分类。（依据：[R3][R6]）
4. **上色规则**：色区平涂（单区明度变化 ≤12%）；主色 ≤10；金点缀 ≤5% 面积；允许纸白（未上色区）；单色墨档 = 全帧单色（蓝绿/橄榄绿/黑任选）。自查：色彩量化 + 分区统计。（依据：[R9][R10]）
5. **辐射光规则**：≥1 处单中心辐射装置（射线 ≥6 条，或环形光晕/光球），面积 ≥8%；光源在画内（云中/球中/火焰中）。自查：径向梯度检测 + 光源定位。（依据：[R9]）
6. **非重力动态规则**：≥1 个人物呈腾空/俯冲/螺旋扭转（人物包围盒底部无支撑物，或躯干轴偏离竖直 ≥15°）；不得为写实日常步态。自查：姿态粗检测 + 支撑关系检查。（依据：[R5][R7]）
7. **神谱锚点规则**：≥1 个**可点名**的象征物（罗盘/天平/书卷/锤钳/蛇/火焰球/葡萄藤）且与主题对应；人物若出现，须与命名神谱一致（可点名、有谱系关系）。自查：物件清单 + 主题对照表。（依据：[R5]）
8. **页面框规则**：≥1 条粗边框线或拱门/光球/洞穴等「页面建筑」元素；构图中心轴对称 ≥60%，或具明确涡旋（旋转对称分量 ≥1）。自查：镜像差分对称检测 + 边框检测。（依据：[R7][R9]）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–2 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **轮廓线强度（Bounding-Line Hardness）**`[归纳]` | 局部轮廓、边缘允许 2–4px 过渡（早期素描档） | 主要形体清晰轮廓（≥60% 边界、≤2px 过渡） | 全画面硬「铁丝」轮廓（≥80% 边界、≤1px 过渡、线宽变异 2–3:1；《耶路撒冷》档） | **80%** |
| P2 | **手工上色度（Hand-Colour Saturation）**`[归纳]` | 单色墨印、未上色（线描本） | 局部淡彩（人物/关键物上色） | 全画面饱和水彩 + 彩色墨（多色本；《欧洲》蓝绿墨档） | **70%** |
| P3 | **神谱密度（Named Pantheon Density）**`[归纳]` | 1–2 个神话人物/象征物 | 3–5 个具名人物或象征物 | 满幅神谱 + 文字板（体系叙事；《耶路撒冷》档） | **60%** |
| P4 | **文字板比例（Text-Plate Ratio）**`[归纳]` | 0%（纯图像；大彩色版画档） | 标题/题词条（5–15% 页面） | 文字与图像同权（25–40% 页面；《天堂与地狱》档） | **30%** |
| P5 | **动态能量（Visionary Dynamism）**`[归纳]` | 静立/端坐（肖像、静观档） | 行走/跪拜/举手（叙事中档） | 腾空/俯冲/螺旋扭转/双臂展开（「火焰状」动态；《亘古常在者》《约伯记》档） | **70%** |
| P6 | **发光装置（Visionary Apparatus）**`[归纳]` | 无光晕/无云（早期线描档） | 局部光晕或云 ≤15% 面积 | 辐射光/光球/火焰场 ≥20%（《欧洲》《约伯记》档） | **60%** |

> **用法**：P1/P2/P4 定「是不是布莱克」（三条中 ≥2 条 ≥ 中档才成立）；P3/P5/P6 定题材与强度档（书页叙事 → 大版画幻视 → 满幅神谱）。P1 是**负向护栏的正向表述**——「有铁丝轮廓」等价于「无排线明暗」的一半；生成后先查 P1 与「交叉排线 0 命中」（§8.2-2）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若明暗由交叉排线/线密度承担 → 越界**丢勒**；② 若符号退化为纯情绪变形、无命名神谱/文字 → 越界**蒙克**；③ 若线为单根等宽线、无文字板 → 越界**北斋**；④ 若出现涂抹式渐变、sfumato 或厚涂笔触 → 越界**达·芬奇/油画传统**（布莱克明令反对）；⑤ 若金/材质成为主装置（>5%）→ 越界**克里姆特**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 蒙克）**（× 蒙克；本卡 §3.1 分工条款（与 munch.md §3.1 对称互锁））：象征两路：自创神话体系 vs 私人心理——判据四条；符号系统轴不可混用（命名神谱 vs 情绪原型）
- **分工（vs 丢勒）**（× 丢勒；本卡 §3.1 分工条款）：版画两路：浮雕蚀刻＋图文一体 vs 排线明暗——判据五条；线功能与文字地位轴同轴不可叠加（系统新轴）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-07 排线轴（与北斋同站「无排线」侧，机制不同）／C-12 色相面积／C-14·C-16 渐变与反约束适用域

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/blake.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
