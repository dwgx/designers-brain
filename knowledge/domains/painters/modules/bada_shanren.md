# 八大山人 模块卡 — `bada_shanren`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/bada_shanren.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **大留白**：白多于墨——空白（纸色）≥55%（默认 60–70%）；主体悬置、下方全空
2. **极少笔画（减笔）**：主体 ≤30 笔（强档 ≤15）——鱼／鸟／猫以个位数至十几笔写出
3. **白眼／方眼**：瞳孔点上角、视线朝上外——「白眼向天」符号
4. **单色墨＋墨分五色**：色相数 ≈1（彩色 ≤1%）；干湿浓淡 ≥3 级（渗化／飞白）；圆笔中锋、无排线
5. **悬置构图＋书法性款印**：主体压上部／边角；行草题款＋花押（「哭之笑之」）参与构图；冷峻静物感

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Chinese xieyi (expressive) ink painting in the manner of Bada Shanren (八大山人):
monochrome ink on paper; a single subject — one lone bird / fish / duck / cat / lotus —
painted with the fewest possible strokes (under about 30), each stroke loaded and
rounded, centered-tip (zhongfeng) brushwork with hidden tips; forms reduced to
geometric archetypes, the animal anthropomorphic, still, and slightly defiant;
the eye drawn as an angular, square-ish shape with a single ink-dot pupil set at the
top corner, gazing upward and outward (the "white-eye"); the subject floats high or
in one corner of a vast untouched paper field (at least 60% blank paper), with nothing
below it — no water line, no ground line; ink tonality spanning 2–4 gradations from
dense black to pale grey; wet saturated washes for leaves and rocks against dry,
flying-white brushstrokes for stalks and branches; a vertical column of cursive
calligraphy and one or two red seals as compositional counterweights; mood: cold,
still, austere, minimal — "few ink dots, many tears"
```
**负向约束（`--no` 风格）**
```
--no color, chroma, gold, colored washes, gradients beyond ink bleed, airbrush,
soft blending, photorealistic textures, hatching / crosshatching, western shading,
outlines around filled shapes, detailed feathers / fur / scales, multiple subjects
crowding the frame, centered symmetrical composition, full-bleed background, water
ripples, ground line, horizon line, busy decoration, cute round eyes, pupils centered
in the eye, photorealistic lighting, cast shadows, lens flare, cluttered background
```

## 代码艺术规则（§8.2 原样）

1. **留白**：纸色 / 空白像素 ≥55%（默认 60–70%）；空白区内不得出现纹理、均匀噪点或渐变（除单笔渗化的 1 级过渡带，面积 ≤2% 画幅）。
2. **单色墨**：彩色像素（饱和度 >10%）≤1%；墨色覆盖 ≥3 个可分辨灰阶（如 0–15% / 40–60% / 80–95% 三段）。
3. **笔画预算**：主体连通墨迹组件 ≤30（强档 ≤15）；允许且鼓励单笔内部墨色渐变（一笔从浓到淡）。
4. **白眼**：眼部为棱角形（4±1 边）；瞳孔墨点中心位于眼眶包围盒上半部（≤ 眼眶中心 −20% 高度）；瞳孔面积 ≤ 眼眶面积 25%。
5. **悬置构图**：墨迹重心高于画布几何中心 ≥5% 画幅（或主体位于左 / 右边带）；主体包围盒距画布边缘 ≥8% 短边；主体下方 ≥30% 高度内无墨迹。
6. **圆笔与飞白**：笔画端点圆（藏锋）——端点无尖刺、曲率半径 ≥ 线宽 50%；飞白（干笔）≥1 处、面积 ≤15% 主体。
7. **静态性（动画时）**：主体位移 = 0；不得出现运动线 / 速度线 / 风纹；仅允许墨色渗化或 ≤1px 呼吸级变化；题款与印章为静态元素。

## 控制参数（§4 原样）

**P1 留白率（Negative Space）**（默认 60%）`[归纳]`
- 弱: 40–50%（早期册页，物象较满）
- 中: 55–65%（成熟期典型）
- 强: ≥70%（"白多于墨"，单鱼 / 单禽）

**P2 笔墨经济度（笔画预算，Stroke Economy）**（默认 40）`[归纳]`
- 弱: 主体 ≤80 笔（早期《传綮写生册》级）
- 中: 主体 ≤40 笔（成熟期）
- 强: 主体 ≤15 笔（"一笔圈出鸟身"级）

**P3 白眼符号化（White-eye Symbolism）**（默认 中–强）`[归纳]`
- 弱: 圆眼、直视（早期）
- 中: 方眼、视线偏上
- 强: 方眼 + 瞳孔顶角 + 缩颈 / 独立（"白眼向天"符号）

**P4 墨色层次跨度（Ink Tonality）**（默认 4 级）`[归纳]`
- 弱: 2 级（浓 / 淡）
- 中: 3–4 级
- 强: 5 级（焦浓重淡清）+ 干湿对比

**P5 圆笔度（Centered-brush Roundness）**（默认 中）`[归纳]`
- 弱: 见棱角（早年锐利）
- 中: 方圆兼有
- 强: 全圆笔藏锋（晚年圆浑）

**P6 悬置度（Compositional Suspension）**（默认 中–强）`[归纳]`
- 弱: 主体近中心
- 中: 主体偏上 1/3
- 强: 压顶 / 边角 + 下方全空（悬空感）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-07**（× 丢勒；本卡 §8.2-6）：表面系统：排线明暗 vs 无排线（墨色层次＋空白）
- **C-17**（× 米开朗基罗；本卡 §8.2-1）：负空间（≥60% vs ≤15% 硬冲突轴）——组合需二选一
- **分工（vs 北斋）**（× 北斋；本卡 §8.2-7）：动／静：曲线族＋螺旋动势 vs 无风无动的书写性圆笔——动势轴归北斋、留白与符号轴归八大（N1/N3）
- **分工（vs 齐白石）**（× 齐白石；本卡 §8.2-2）：同族两档互斥：冷峻／极简 vs 热烈／生机——色彩轴归齐、极简减笔轴归八大（N3）
- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §8.1 负向段）：边界：单色墨迹／书写性 vs 彩色剪纸块面／平涂无墨

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/bada_shanren.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
