# 陈洪绶 模块卡 — `chen_hongshou`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/chen_hongshou.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **变形比例（头大身短）**：主要人物头长÷全身长 ≥1/6（强档 ≥1/5）、头宽÷肩宽 ≥0.75、面型方正——「与身体相比显然不合比例」
2. **线质两档**：壮年版画方折瘦硬（「方折直拐的瘦硬线条」）；晚年高古游丝描（「一笔勾出，不另起笔，紧劲连绵，如行云流水」）——长线单笔连续、线宽均匀（变化 ≤1.5×）
3. **装饰性图案＋古器物陈设**：松石造型图案化（「颇富图案装饰趣味」）；器物（瓶罍/尊卤/几案/屏风）1–8 件/图——「尤其喜欢用古器物作为画面的构成部分」
4. **高古奇骇的面容＋背景压缩**：面孔方正、五官紧凑、表情克制（仪式感、静穆）；背景留白 ≥35%、无透视消失点——《九歌图》「no background setting」
5. **设色古艳＋线是骨架**：矿物色（石青石绿/朱/赭）「brilliant coloring with mineral pigments」、色不掩线；无排线/无渐变填充——「铁线」细匀墨线；款「洪绶」「老莲」＋刻工署名

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Late-Ming figure painting and woodblock illustration in the manner of Chen Hongshou (陳洪綬,
1598–1652): archaic and deliberately distorted figure types — oversized heads on short, plump
bodies, squarish faces, compact features, long narrow eyes; figures posed in calm ceremonial
stillness, single viewpoint; drapery drawn as long, springy, continuous brush lines, each fold
in a single unbroken stroke (gaogu yousi miao, "ancient gossamer-thread" line), capable of
switching to crisp, square-turned, staccato strokes in the woodblock-card mode; bold decorative
patterning — stylized pines and rocks reduced to pattern, patterned drapery, archaic bronzes,
Han tiles and vessels, screens, banana leaves; mineral-pigment color, antique and intense
(shiqing shilv blue-green, vermilion, ochre) laid so it never hides the line; compressed or
empty backgrounds, a single flat prop (screen, rock, stone table) doing the spatial work;
baimiao ink drawing for woodblock plates with a title panel, wine-game colophon and engraved
signature at the edge; flat decorative space, no cast shadows, no perspective
```
**负向约束（`--no` 风格）**
```
--no photorealistic rendering, western perspective, cast shadows, chiaroscuro, crosshatching,
dense parallel hatching, stipple shading, engraved uniform lines without brush character,
naturalistic proportions, sweet or pastel palette, sentimental prettiness, heavy impasto,
glossy oil surface, sfumato, airbrush gradients, 3D render, anime faces, random caricature
without archaic decorum, modern clothing, crowded full-bleed background
```

## 代码艺术规则（§8.2 原样）

1. **变形比例**：主要人物头长（下颌至头顶）÷ 全身长 ≥ 1/6（强档 ≥1/5）；头宽 ÷ 肩宽 ≥ 0.75；面轮廓的方直段（曲率 ≤ 阈值）占周长 ≥40%。`[归纳]`
2. **一笔连绵的线**：衣纹主轮廓线中，单笔连续长度 ≥60px（1000px 参考帧）的笔画占比 ≥50%；单笔中段线宽变化 ≤1.5×（「游丝档」）；「方折档」允许线宽恒定但转折角 ≥45° 的折点 ≥2 处/100px。`[归纳]`
3. **无排线**：全帧交叉排线（两组以上线方向夹角 ≥15° 且密度 >2 线/10px）面积 ≤1%；线密度与局部明度的单调映射不成立（|r| ≤0.4）；单色实心填充面积 ≤10%。`[归纳]`
4. **装饰纹样密度**：可辨纹样单元（松针组、云纹、器物纹、衣纹图案）≥1 单元/1000px²（强档）；器物/陈设元素 1–8 件/画面；纹样重复率（同类单元 ≥2 次）≥50%。`[归纳]`
5. **背景压缩**：人物画背景留白（高亮均质区）≥35%；透视线收敛点数量 ≤1 且不在画内；平面道具（屏风/石/案）承担 ≥1 个空间分层。`[归纳]`
6. **设色古艳**：彩色像素（饱和度 >15%）≤45%；色相 ≤4 族（石青/石绿/朱/赭黄）；单块饱和度 ≥70% 的连通域面积 ≤3%；线迹穿过色块的可见度 ≥60%。`[归纳]`
7. **版画字段（插图/叶子档）**：题名/题赞文字区（文字列或框）存在且 ≤8% 画面；纯白描（无灰阶填充带）；刻工署名（角落小字）1 处；动画时人物位移 ≤1% 画幅/秒（酒牌为静帧语义，禁叙事推拉）。`[归纳]`

## 控制参数（§4 原样）

**P1 变形强度（Deformation）**（默认 中-强）`[归纳]`
- 弱: 比例温和、近写实（早年册页如《山水人物花卉图》册部分页）
- 中: 头大身短可见、面型方正（《升庵簪花图》《斜倚薰笼图》）
- 强: 极端夸张（《水浒叶子》《博古叶子》版画人物）

**P2 线质档（Line Quality）**（默认 中）`[归纳]`
- 弱（游丝档）: 圆润纤劲、一笔连绵（《博古叶子》《九歌图》卷）
- 中: 清圆细劲、铁线控制（《宣文君授经图》《斜倚薰笼图》）
- 强（方折档）: 方折直拐、瘦硬顿挫（《水浒叶子》）

**P3 装饰密度（Ornament）**（默认 中）`[归纳]`
- 弱: 简淡、少纹样（《屈子行吟图》式白描）
- 中: 器物纹样适量（人物画中 1–3 件古器）
- 强: 满幅图案化（松石规律化、器皿密陈，如《乔松仙寿图》《博古叶子》）

**P4 古器物陈设（Antiquity Props）**（默认 中）`[归纳]`
- 弱: 无器物（纯人物/花鸟）
- 中: 1–3 件（几案、瓶罍、屏风）
- 强: 多件成组（《博古叶子》「器具得五十二」级密度）

**P5 设色档（Color Mode）**（默认 中-强）`[归纳]`
- 弱: 水墨白描（版画稿、墨笔）
- 中: 淡彩（浅绛、薄矿物色）
- 强: 矿物重彩古艳（石青石绿、朱、赭；色不掩线）

**P6 背景压缩（Background Compression）**（默认 中-强）`[归纳]`
- 弱: 有景（花鸟、山水背景）
- 中: 简景（一二树石）
- 强: 无背景/纯留白（《九歌图》卷式）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 毕加索）**（× 毕加索；本卡 §3.1 分工条款）：同做「变形」：古拙线造型 vs 形体解构——判据（头长比/面片折线夹角／轮廓一笔连续 vs 折线串／单视点 vs 多视点）；两卡禁项互列（陈禁面片化/多视点；毕禁头大身短装饰性比例）
- **分工（vs 丢勒）**（× 丢勒；本卡 §3.1 分工条款）：同做「版画」：白描＋插图设计 vs 排线明度映射——判据（排线网／文字设计区／长线一笔 vs 短线密排）；线质与用途轴
- **分工（vs 赵孟頫）**（× 赵孟頫；本卡 §3.1 分工条款（逐轴对齐））：同用线：书法性（端庄古意）vs 古拙变形（大头短身）——三判据（比例／圆转 vs 方折／装饰密度）；与 `zhao_mengfu.md` §3.1 预写条款逐轴对齐
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：线条、色域、负空间

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/chen_hongshou.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
