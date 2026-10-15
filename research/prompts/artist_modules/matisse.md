# 马蒂斯 模块卡 — `matisse`

> A-19 模块库 ｜ 来源：档案 `research/artists/matisse.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `research/agent-art/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **平涂色块**：内部明度变化 ≤5%、无描边无投影；剪裁硬边（直线段＋圆弧）
2. **色相少而纯**：5–8 个高纯度色、互补对撞；黑与彩同权
3. **空间＝色面积与方向**：无消失点；所有曲线回应隐含垂直轴
4. **留白是主角**：纸／底色可见 ≥20%；缩略图（64px）仍可读
5. **图案与主体同权**：纹样与人体同一平面处理；剪纸形状跨作品复用

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
paper cut-out composition in the manner of Matisse's late gouache découpée:
flat opaque gouache colours, shapes cut with scissors from hand-painted paper,
absolutely no shading, no gradients, no outlines, no drop shadows;
a small set of 5-7 fully saturated colours (ultramarine blue, cadmium red,
emerald green, lemon yellow, black, white); large interlocking organic silhouettes;
every curve answers to an implied vertical axis; generous white paper ground
visible between shapes (at least 20% of the surface); whole composition legible
at a glance; poster-like flatness, matte surface, slightly irregular scissor edges;
dancer / snail / leaf / star motifs allowed
```
**负向约束（`--no` 风格）**
```
--no gradient, airbrush, soft edges, blur, glow, outline stroke, drop shadow,
3D render, realistic lighting, cast shadow, perspective vanishing point,
more than 8 hues, muddy mixed greys, texture noise, photographic detail,
cluttered micro-detail, symmetrical centred layout, crosshatching
```

## §8.1b 场景可迁移性注记

> E-02 · E1_t1b 诊断（2026-10-15）：§8.1 仅含装饰母题词（dancer / snail / leaf / star）；E1_t1 未见人物实体化、场景保留，风格可迁移（如需更纯净可删母题词）。

## 代码艺术规则（§8.2 原样）

1. **色数**：同屏纯色块 ≤ 8（含黑白）；每块饱和度 ≥70%，明度分层 ≤3 级；除纸张底色外，任何渐变面积 ≤5% 画面。
2. **边缘**：所有形状边缘为"剪裁边"——无描边、无羽化、无投影；边缘由直线段与圆弧组成，相邻线段夹角 ≤15° 视为同一弧。
3. **垂直参照**：每帧至少存在一条可见或隐含的垂直轴（画布边界或物体轴线）；所有曲线的切线方向与垂直轴夹角 ∈ [0°, 75°]；"连续转向 >75° 且无垂直参照"的曲线计数必须为 0。
4. **面积配比**：最大色块占画面 25%–45%，次大 15%–30%，其余各 <12%；同一色相不得出现在两个相邻且面积相近（差 ≤3%）的块中（防"碎花"）。
5. **负空间**：相邻形状间隙 ≥ 最短边长的 2% 且 ≤12%；背景/纸色可见面积 ≥20%。
6. **运动（动画）**：形状入场 = 位移 + 旋转 ≤12°；缓动为单段 ease-in-out，过冲（overshoot）≤3%，回弹帧数 ≤1；**禁止用交叉淡化（crossfade）冒充形变**；每 10 秒至少 3 个"决定性构图"停留 ≥0.8 秒（对应"整体一眼可读"）。
7. **符号复用**：同一"符号形"（蜗牛螺旋、蓝色裸体、星/叶）在片中出现 ≥3 次且每次允许变形 ≤20%（对应 *Thèmes et Variations* 的"主题—变奏"结构）。
8. **图案密度可测（P4 的可判定定义）**：设纹样区（可识别的周期/重复结构）覆盖面积比 $A_p$、纹样边界总长度 $L_p$（像素，归一化到画面短边 $s$）——**弱**：$A_p\le5\%$ 且 $L_p\le0.5s$；**中**：$15\%\le A_p\le35\%$，$1s\le L_p\le3s$；**强**：$A_p\ge50\%$ 且 $L_p\ge4s$。三档共同硬约束：纹样区内部明度动态范围 ≤5%（与"带材质图案"的分界，见 §4 P4 边界注）、纹样与主体使用同一线宽与同一色阶层数。**判定失败即回退一档**。
   **档位映射（防混用）**：P4 的百分比是**旋钮值**，$A_p$ 是**实测值**，两者不同名不同义——旋钮 ≤30% → 弱档；40%–70% → 中档（默认 50% 即此档）；**≥80% → 强档**。测试时"P4=强"须同时满足旋钮 ≥80% 且实测 $A_p\ge50\%$，二者不一致以实测为准并记一条失配。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **色彩纯度（Color Purity）**`[归纳]` | 掺灰/土色，色相差小（近莫兰迪） | 纯色为主，允许 1–2 个低纯度调和色 | 全画面高纯度纯色对撞，无灰阶缓冲 | **85%**（剪纸期），油画期 65% |
| P2 | **色数上限（Palette Count）**`[归纳]` | 12–16 色 | 8–10 色 | 4–6 色（含黑白） | **7 色** |
| P3 | **平面化程度（Flattening）**`[归纳]` | 保留体积明暗与透视（1900 前风格） | 局部保留明暗，主体平涂 | 全平涂 + 无消失点，深度仅靠面积/遮挡 | **80%** |
| P4 | **装饰图案密度（Pattern Density）**`[归纳]` | 纯色背景无纹样 | 单一大纹样（一块壁纸/地毯） | 满画面纹样且与主体同权（《红色画室》级） | **50%** |
| P5 | **边缘硬度（Edge Hardness）**`[归纳]` | 软边/晕染 | 硬边但留笔触毛边 | 剪刀硬边，无羽化、无描边 | **90%**（剪纸），**60%**（油画） |
| P6 | **曲线克制（Curve Discipline）**`[归纳]` | 曲线自由，无垂直参照 | 主曲线回应垂直轴 | 所有曲线与隐含垂直成明确角度关系，无一条"疯狂曲线" | **70%** |

> 用法：P1/P3 定"是不是马蒂斯"，P5/P6 定"像剪纸期还是油画期"，P2/P4 定"抽象度"。三档描述可直接当判定标准写进自查表。
> **P4 边界（与"带材质图案"的分工判据）**：P4 只调**图案密度**，其承载面恒为"平涂纯色、无材质"（见 §1 指纹 1/3、§2 规则 1、§8.1 负向约束 `--no gradient/texture noise/glow`）。它**不含**材质区分、金属/金箔表面、纹理明度范围与"写实面孔 × 装饰"的渲染方式对撞——需要这些时不属于本模块，应交给克里姆特类模块（另立参数：材质对比度 / 纹理明度范围 / 写实-装饰渲染落差）。本判据为 `[归纳]`，可直接被 wave2 实验推翻。

## 冲突注记（→ conflicts.md）

组合前先读 `research/agent-art/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-06**（× 毕加索 / 达·芬奇 / 莫奈；本卡 §4 P1 + §8.2-1）：饱和度（每块 ≥70% vs 全帧 ≤35%）
- **C-15**（× Lane B 色数上限（克里姆特类缺口）；本卡 §4 P4 边界注 + §8.2-8）：色数计数口径（≤3 色 vs 金属/金箔层）
- **C-16**（× Lane B 02 卡反约束；本卡 §8.2-1/-2）：反约束适用域（「没有高光的平涂」误伤平涂系）
- **C-17**（× 米开朗基罗；本卡 §8.2-5）：负空间（≥20% vs ≤15%）
- **C-18**（× 米开朗基罗；本卡 §4 P3 + §8.2-2）：形体塑造（平涂 vs 浮雕）

## 来源

- 档案（唯一正本）：`research/artists/matisse.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`research/agent-art/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`research/prompts/artist_modules/README.md`
