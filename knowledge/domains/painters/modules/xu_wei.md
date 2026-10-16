# 徐渭 模块卡 — `xu_wei`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/xu_wei.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **泼墨晕散、水气淋漓**：湿笔大块铺陈、边缘晕散渗化（湿墨区 ≥40%、边缘渐变带 ≥2px）——「墨气淋漓酣畅」的「雨润」感（淡墨加胶矾挥洒）
2. **狂草式笔线**：行笔迅疾、提按大（线宽变化 ≥2.5×）、连贯线群如草书连笔；飞白出现——「以草书笔法作画，行笔豪迈而不肆野」
3. **偶发墨点＋造型简率**：独立小墨点 3–30（≤0.2% 画幅）、泼溅区 0.3–3%；每元素笔数预算 ≤20 笔、轮廓缺口多——「不求形似求生韵」
4. **墨阶跨度大＋留白对撞**：可辨灰阶 ≥5 级、干湿同帧并存；空白 25–45%、浓墨区 8–35%——「全幅不见物象但见墨影」
5. **长题诗款＋爆发情绪**：草书/行书题诗 ≥2 行（常七绝整首）、款印 1–3 方；单色水墨为主（彩色 ≤5%）；动势读数高、无静物式摆置——「老夫一扫秋园卉」

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Ming dynasty daxieyi (large freehand) ink painting in the manner of Xu Wei (徐渭, 1521–1593):
splashed-ink flowers on paper — wet saturated washes poured and pressed with a broad brush,
ink blooming and bleeding softly at the edges; wild cursive (kuangcao) brush lines that whip
and coil like calligraphy, accelerating, skipping dry into feibai streaks mid-stroke; forms
sketched in just a few loaded strokes, deliberately "not seeking likeness" (buqiu xingsi) —
grape clusters as strings of ink pearls, peony heads as blots with darker centers, lotus
leaves as slashed wet planes; accidental ink dots and stray splashes left in the picture as
part of the design; ink tonality spanning the full five gradations from burnt-black to pale,
wet and dry in the same frame; large areas of empty paper set against dense black passages;
a long column of unruly cursive calligraphy carrying the artist's own poem down one side,
one or two red seals; mood: explosive, released, defiant, slightly bitter — the energy of a
storm let out in one breath, "ink splashing like rain breaking open"
```
**负向约束（`--no` 风格）**
```
--no fine gongbi outlines, neat even-width contours, careful detail rendering, symmetrical
vase arrangements, decorative prettiness, flat opaque color blocks, airbrushed gradients,
photorealistic petals or dewdrops, delicate crosshatching, pale transparent watercolor
without ink presence, western chiaroscuro, geometric abstraction, cute or sweet mood,
gold ornament, tidy printed calligraphy, watermarks or borders
```

## 代码艺术规则（§8.2 原样）

1. **湿墨渗散**：晕散湿墨区（边缘存在 ≥2px 渐变的墨区）占墨迹总面积 ≥40%（强档 ≥60%）；墨区边缘平均过渡带宽 ≥3px；不得出现硬边单色填充块（内部标准差 >8% 的均色区面积 ≤5%）。
2. **狂草线群**：主体长线（长度 ≥10% 画幅短边）线宽变化 ≥2.5×；一笔内方向连续变化（曲率积分 ≥ 同长度直线的 3 倍）；飞白（笔画内露白丝缕）≥1 处 / 主体；等宽刻线（变化 ≤30% 且长度 >10% 画幅）面积 ≤1%。
3. **偶发墨点**：独立小墨点（面积 ≤0.2% 画幅、与主体距离 >1% 画幅）计数 3–30；泼溅区总面积 0.3–3% 画幅；墨点间距方差高（不得呈均匀噪点/规则排列）；主体轮廓上允许「意外」缺口 ≥1 处。
4. **墨阶与干湿**：可分辨灰阶 ≥5 级（焦、浓、重、淡、清）；湿区（软边）与枯区（飞白）在同一帧并存；单一墨阶占比 ≤50%。
5. **造型简率**：每元素（花头/叶/蟹/竹枝）笔数预算 ≤20 笔（强档 ≤8）；元素轮廓完整性低（缺口 ≥15% 周长）；不得出现细节纹理（叶脉细线 ≤2 条/叶）。
6. **留白与对撞**：留白（纸色）面积 25–50%；浓墨区（≤20% 灰阶）面积 8–35%；空白区不得出现纹理、均匀噪点或渐变。
7. **动画规则（动画时）**：墨迹渗化动画允许——单笔扩散速度 ≤2px/帧、单笔渗化总时长 ≤1.5s；笔线生长速度 ≥3× 常规书写速度（爆发感）；主体位移 = 0；不得出现镜头推拉、叙事动作；印章与题款静态；帧间非墨区差 ≤1%。

## 控制参数（§4 原样）

**P1 泼墨湿度（Splash Wetness）**（默认 强）`[归纳]`
- 弱: 干笔为主、枯笔飞白（《驴背吟诗图》档、雪竹档）
- 中: 湿墨为主、局部泼染（《五月莲花图》「点染不苟」精整档）
- 强: 泼墨淋漓、水气蓊郁（《杂花图》《水墨葡萄图》《蕉石牡丹图》档）

**P2 狂草行笔度（Cursive Momentum）**（默认 强）`[归纳]`
- 弱: 行楷笔意、收束（题款/精整小品）
- 中: 行草连势（《水墨牡丹图》题款行书档）
- 强: 狂草爆发线群、连贯不辍（《杂花图》枝藤、《写生 卷》竹枝档）

**P3 偶发密度（Accidental Ink Events）**（默认 中）`[归纳]`
- 弱: 几乎无洒点（《五月莲花图》「点染不苟」）
- 中: 自然点洒、飞溅若干（多数成熟期作品）
- 强: 泼洒/倾泻明显（大写意爆发帧；墨点 20+、泼溅区 ≥1% 画幅）

**P4 墨阶跨度（Ink Tonality）**（默认 5 级）`[归纳]`
- 弱: 2–3 级（浓/淡）
- 中: 4 级（焦浓重淡）
- 强: 5 级（焦、浓、重、淡、清）+ 干湿枯润并存

**P5 留白率（Void Ratio）**（默认 30–45%）`[归纳]`
- 弱: ≤15%（《杂花图》满墨局部段）
- 中: 25–45%（《黄甲图》「留出大片空白表现秋水」）
- 强: ≥50%（精整小品/简笔档）

**P6 情绪强度（Expressive Intensity）**（默认 强）`[归纳]`
- 弱: 戏笔（游戏感为主）
- 中: 戏谑 + 自嘲（题画诗常见口吻）
- 强: 磊块不平、激越（爆发帧；「笔底明珠无处卖」档）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 八大山人）**（× 八大山人；本卡 §3.1 分工条款（第一写死条款））：写意同族分档：爆发/湿润 vs 冷峻/减笔——四判据（情绪温度／墨面湿度／笔法／空间题材）；判定须 ≥2 轴联合；爆发轴归徐、减笔轴归八大（N3）
- **分工（vs 齐白石）**（× 齐白石；本卡 §3.1 分工条款（第二写死条款））：文人狂态 vs 民间趣味——四判据（姿态情绪／色彩／精度结构／墨法）；色彩轴归齐、爆发/湿墨轴归徐（N3）
- **分工（vs 雪舟）**（× 雪舟；本卡 §3.1 预写条款（对齐））：「徐渭＝爆发档」条款与 `sesshu.md` §3.1 预写一致；破墨洒点同族、须以题材轴为主联合 ≥2 轴
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-07 表面系统／C-12 色相预算／C-17 负空间（留白 25–45%；与八大 ≥60% 组合取交集并显式取值）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/xu_wei.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
