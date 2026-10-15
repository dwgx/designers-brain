# 卡拉瓦乔 模块卡 — `caravaggio`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/caravaggio.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **单光源、无反射、背景近黑**：光从画外高处来；画面内可见光源数 = 0
2. **两级明暗（tenebrism）**：中间调被压缩（直方图双峰）；暗部非死黑——深棕底作中间调
3. **人物贴住画面平面**：被边缘裁切；手势是叙事主语，光斑只落脸／手／道具
4. **反理想化人体＋当代服装**：脏指甲、破衣缝当圣徒；定格瞬间（无运动模糊）
5. **色域收窄**：赭／红棕／铅白／黑土色系；深色底参与塑形（亮部在其上「塑出」）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Caravaggio-style tenebrist oil painting:
one single hard directional light from high left, no fill light, no reflected light;
background walls and floor in near-black shadow (values under 10% of the lit highlights);
deep dark brown ground left visible inside the shadows as their mid-tone;
violent chiaroscuro: lit passages bright and warm, shadows crushed, midtones suppressed;
one frozen instant of a narrative action; faces and hands catch the light;
gestures point at the narrative object; figures pushed flat against the picture plane,
half-length or three-quarter figures cropped by the frame edge;
ordinary working people as saints — weathered faces, torn clothes, dirty fingernails,
contemporary 17th-century Roman clothing; plain dark interior, no landscape, no sky;
restrained earth palette — ochre, madder red, lead white, bitumen black,
one or two saturated accents on a prop; direct painting, broad final touches,
impasto highlights on the lit edges
```
**负向约束（`--no` 风格）**
```
--no soft diffuse lighting, ambient light, multiple light sources, rim light, backlight,
glow, bloom, lens flare, volumetric rays, evenly lit faces, bright background,
landscape, sky, daylight, symmetry, idealised anatomy, smooth airbrushed gradients,
pastel palette, neon colours, cartoon, 3D render, photographic realism, motion blur,
fog, haze, mirror, chandelier, candles visible in frame, halo disc, crowd
```

## §8.1b 纯风格段（场景可迁移）

> 派生自 §8.1 正向段（E-02 · E1_t1b，2026-10-15）：删除题材词（人物/肖像/室内/静物）与场景专属道具，仅保留视觉语言（光/色/笔触/结构/构图规则）；用法：主题句 + 本段（同 §8.1 配方）。负向段沿用 §8.1 原文（本通道不发送）。
> 删除项：faces and hands、gestures、working people as saints、dark interior（no landscape/no sky）、prop accent；最小改写：walls and floor→areas、figures pushed flat→the main motif pushed flat、narrative action→dramatic action。明细见 `experiments/E1_t1b/RESULTS_t1b.md` §2。

**正向段（可直接粘贴）**：
```
Caravaggio-style tenebrist oil painting: one single hard directional light
from high left, no fill light, no reflected light; background areas in
near-black shadow (values under 10% of the lit highlights); deep dark brown
ground left visible inside the shadows as their mid-tone; violent chiaroscuro:
lit passages bright and warm, shadows crushed, midtones suppressed; one frozen
instant of dramatic action; the main motif pushed flat against the picture
plane and cropped by the frame edge; restrained earth palette — ochre, madder
red, lead white, bitumen black, one or two saturated accents; direct painting,
broad final touches, impasto highlights on the lit edges
```

## 代码艺术规则（§8.2 原样）

1. **光源单一性**：全帧可见光源数 = 0（光从画外来）；主光方向固定为左上或右上（方向向量取 (±0.7, −0.7) 一类）；环境光强度 ≤ 主光的 5%。
2. **背景明度上限**：背景区域（非人物/非道具像素）最大亮度 ≤ 0.10 × 全帧最大亮度；背景亮度标准差 ≤ 全帧 5%（禁光晕渐变）。
3. **中间调压缩（直方图双峰）**：亮度直方图中，中间带 [0.35, 0.65] 像素占比 ≤ 25%；暗带 [0, 0.25) 占比 ≥ 40%。（强档默认；中档放宽到 ≥25% / ≤40%）
4. **光斑三处法则**：高光连通域（亮度 ≥ 0.9 × max）数量 ∈ [2, 5]，且每个连通域必须与"脸 / 手 / 关键道具"之一相交；人物背部的高光连通域数 = 0。
5. **贴平面构图**：主人物包围盒高度 ≥ 画幅高 80%；至少 1 个主体被画幅边缘裁切；地平线（若出现）不得高于画幅下缘以上 15%。
6. **定格瞬间**：每帧只允许 1 个"动作极值"（最大手势位移向量的方向唯一）；运动模糊核 = 0；手势向量的延长线在 ±15° 内指向叙事对象中心。
7. **暗部保细节**：暗区（亮度 < 0.15）内部亮度标准差 ≥ 1.5/255（非死黑）；纯黑像素（=0）占比 ≤ 10%（对应 §1-3 的"底色作中间调"）。

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（见 §10）；3、5 两条与 `expansion.md` §1.2 的三条建议（光源仰角、背景明度上限 8%、贴平面）对齐。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **光源聚焦度 / 硬度（Light Hardness）**`[归纳]` | 柔和环境光，多个光源或天光；有反射补光 | 单一方向光，允许少量反射；亮部边界略软 | 单一硬光（画外、高置 30°–60° 仰角），无反射、无补光，亮部边界硬 | **85%**（本模块强档即其身份） |
| P2 | **背景明度上限（Background Ceiling）**`[归纳]` | 背景可达全帧最亮的 40–50%（近自然室内） | ≤20% | ≤8–10%（近黑，墙/地几乎只剩轮廓暗示） | **10%** |
| P3 | **中间调压缩（Midtone Compression）**`[归纳]` | 全调域，中间调充足（学院式渐变） | 中间调 [0.35,0.65] 占比 25–40% | ≤25%，直方图双峰；暗带 [0,0.25) ≥40% | **30%**（比强档松一档，保可读性） |
| P4 | **贴平面度（Figure-to-Plane）**`[归纳]` | 人物在景深中，有明确地面/环境纵深 | 半身/大半身，背景压暗但仍有空间暗示 | 主人物高度 ≥ 画幅 80%、被边缘裁切、前景物越出画面 | **80%** |
| P5 | **色域收窄（Palette Restraint）**`[归纳]` | 色相多、含冷色与高纯色（晚期以后被弃） | 土色系为主，1–2 个饱和强调色（红/绿） | 近乎单色阶：赭/红棕/铅白/黑，饱和色仅出现在道具 | **60%**（罗马期）／晚期取 85% |
| P6 | **手势—光斑绑定（Gesture & Highlight Binding）**`[归纳]` | 光均匀落在全身；手部无特别强调 | 脸部优先受光，手部次之 | 光斑只落在**脸 / 手 / 关键道具**三类对象；高光连通域 ≤5 且都与三者相交 | **85%** |

> **分工口径（与伦勃朗，必须写死，来源 `expansion.md` §1.1/§1.2 与 §4.3 冲突规则）**：两人同属"从黑暗里打光"一族（视觉重叠 ~60%），本档案固定为——**卡拉瓦乔 = 光的开关 + 物理（硬光戏剧）**；**伦勃朗 = 光的连续衰减 + 心理（心理化光斑）**。落到参数上：P1 的强档（无反射硬光）与 P3 的强档（中间调双峰）**是本模块专属**；一旦把 P1 降到中档并允许"光在面部连续衰减"，产出就进入伦勃朗的地盘，组合实验里必须按此判分。本判据为 `[归纳]`，可被 wave3 实验推翻。
> **用法**：P1/P2 定"是不是卡拉瓦乔"；P4/P6 定叙事（贴平面 + 手势受光）；P3/P5 定时期（罗马期 vs 晚期）。三档描述可直接当判定标准写进自查表。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-01**（× Lane B 模板「硬阴影」禁令；本卡 §4 P1 + §8.2-1）：阴影硬度（种子案例；反约束句须改写）
- **C-03**（× 达·芬奇；本卡 §4 P3 + §8.2-3）：直方图/中间调（≤25% vs ≥55%）
- **C-04**（× 塞尚；本卡 §8.2-2/-3）：直方图单桶上限（暗带 ≥40% vs 无 >20%）
- **C-08**（× Lane B「运动模糊」禁令；本卡 §8.2-6）：运动模糊（定格 = 全片 0 帧）
- **C-11**（× 维米尔；本卡 §8.2-4）：高光计数（[2,5] vs 100+ 点）
- **C-12**（× 北斋 / 梵高；本卡 §4 P5 + §8.1）：色相面积预算（土色系收窄 vs 蓝 ≥40% / 互补对 1:1）
- **C-13**（× 塞尚；本卡 §4 P5 + §8.2-2/-7）：阴影色相（深棕黑 vs 蓝 ≥15%）
- **near-miss（conflicts.md §4 表）**：#1/#2/#3/#8（× 维米尔，需显式取值）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/caravaggio.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
