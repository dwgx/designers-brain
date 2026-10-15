# 梵高 模块卡 — `van_gogh`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/van_gogh.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **厚涂＋可见笔触**：颜料堆到压出画布纹理；笔触方向分区（天空漩涡／地面短笔／树火焰状上升）
2. **互补色对置**：黄-蓝、橙-蓝成对并置，靠笔触并置产生「振动」
3. **高彩度黄蓝主导、少渐变**：色块直接并置，不做平滑过渡
4. **母题象征化与放大**：星月加同心光环；柏树贯穿近画顶
5. **浅空间／平面化**：日本版画式裁切与非对称构图；线条书写趣味强

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
oil painting in the style of Vincent van Gogh, post-impressionist,
thick impasto oil paint with visible brushstrokes and canvas weave,
swirling turbulent sky of cobalt and ultramarine with glowing lemon-yellow
stars ringed by concentric halos, complementary colour pairs (yellow/blue,
orange/blue) laid side by side, flame-like cypress rising almost to the top
edge, wheat field of short directional strokes, flat decorative space with
cropped asymmetric composition inspired by Japanese woodblock prints,
bold expressive outlines on key forms, colour used arbitrarily to express
feeling rather than to reproduce the scene, no smooth blending,
palette: cobalt blue, ultramarine, chrome yellow, lemon yellow, viridian,
vermilion, pure white highlights
```

**负向约束（--no）**
```
photorealistic, smooth gradients, airbrush, soft focus, pastel or muted
earth palette, grey overcast light, thin transparent glazes, watercolour
washes, 3D render, clean vector edges, perfectly symmetrical centred
composition, depth of field, HDR, lens flare, fine detail miniature work
```

## §8.1b 场景可迁移性注记

> E-02 · E1_t1b 诊断（2026-10-15）：§8.1 无人物/肖像/室内/静物题材词；E1_t1 灯塔场景保留，风格可直接跨场景迁移（cypress / wheat field / stars 等风景道具词仅作次要元素出现，可按需删除）。

## 代码艺术规则（§8.2 原样）

1. **笔触单元**：每笔 = 一条短线段，长 6–24 px（1080p 基准）；方向随区域场——天空 ∈ 慢速湍流场（±30° 内随噪声），麦田 ±15° 顺风，柏树 75–90° 上升。自查：抽样帧中天空区 ≥60% 笔触方向落在噪声场 ±20° 内。
2. **色数限制**：色相簇 ≤8（黄/橙/蓝/绿/紫/红/白/黑），且 ≥2 对互补簇同帧出现。自查：逐帧色相直方图聚类计数。
3. **厚涂模拟**：≥95% 画面被笔触覆盖；每笔带上亮下暗 1–2 px 边；全画无 >12 px 的无笔触平滑区。自查：边缘密度图 + 平滑区连通域扫描。
4. **漩涡运动**：天空笔触随旋度场漂移，角速度 2–6°/s；漩涡中心 2–3 个，半径 ≥ 画宽 25%。自查：光流场方向图（帧间差）。
5. **星体规则**：星 = 亮核 + ≥2 圈同心环，环亮度递减 ≥30%；星核直径 ≥40 px；闪烁周期 0.8–1.5 s、幅度 ≤±10%。自查：单星亮度时间序列。
6. **构图规则**：地平线在画高 25%–40%；至少一个竖直母题（柏树/尖塔）穿过地平线并达 ≥85% 画高；禁止水平居中对称。自查：竖直边缘检测 + 对称性指标。
7. **反约束（每帧可查的失败项）**：出现交叉淡化冒充形变 / 全局模糊 / 平滑渐变填充 / 色相簇 >8 / 摄影景深——任一出现即判不合规。

## 控制参数（§4 原样）

**P1 笔触表现强度**（默认 75%）[归纳]
- 弱: 笔触合并、表面较平滑，仅边缘保留方向感（早期努能时期风格）
- 中: 笔触清晰可辨、方向随形体，厚涂局部（巴黎—阿尔勒过渡）
- 强: 全覆盖厚涂、漩涡+火焰笔触、画布纹理压痕可见（星月夜/麦田系）

**P2 色彩主观度（arbitrary colour）**（默认 60%）[归纳]
- 弱: 接近固有色，仅提亮补色点缀（巴黎时期）
- 中: 局部夸张（脸更金黄、影子更蓝），背景简化成纯色场
- 强: 完全主观配色（柠檬黄脸 + 浓蓝「无限」背景；绿天黄地）

**P3 互补色对比强度**（默认 70%）[归纳]
- 弱: 相邻近似色为主
- 中: 每画面 ≥1 对互补色（黄/紫、橙/蓝）
- 强: 双互补对同时在场（黄-紫 + 橙-蓝），并置面积接近 1:1

**P4 图形化/线性程度**（默认 50%）[归纳]
- 弱: 无轮廓线，形体靠明暗
- 中: 关键形体带粗轮廓（收割机、椅子、头像）
- 强: 图形化描边 + 平面色块（Cloisonnism 式，如《阿尔勒的卧室》）

**P5 母题象征放大度**（默认 40%）[归纳]
- 弱: 天体/树按写生比例
- 中: 星与月加大 1.2–1.5 倍并加光晕
- 强: 柏树贯穿画幅 ≥85% 高度、天体带同心光环（星月夜）

**P6 表面粗糙度（厚涂高度）**（默认 70%）[归纳]
- 弱: 薄涂、可见底子
- 中: 中等厚度，笔痕留存
- 强: 高堆叠、可投影的厚涂（可被侧光看到起伏）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-05**（× 达·芬奇；本卡 §8.2-3 + §8.2-7）：笔触可见度（≥95% 覆盖 vs 只有渐变）
- **C-09**（× 维米尔；本卡 §8.2-4/-5）：运动预算（全画面场 2–6°/s vs 事件外 Δ≤1%）
- **C-12**（× 北斋 / 卡拉瓦乔；本卡 §4 P3 + §8.2-2）：色相面积预算（互补对近 1:1 vs 蓝 ≥40% / 土色系）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/van_gogh.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
