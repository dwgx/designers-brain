# 范宽 模块卡 — `fan_kuan`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/fan_kuan.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **巨碑式主山**：主峰中轴（偏移 ≤10% 宽）、高度 ≥60% 画面——徐悲鸿「一山頭，幾佔全幅面積三分之二」的压迫性崇高
2. **雨点皴（密点）**：短点／钉头千笔万笔叠搭（短笔 ≤ 山高 2%、覆盖山体 ≥60%）；湿笔浓墨层层渍染——「深暗如暮夜晦暝」
3. **三段式构图＋云雾留白**：近景巨石行旅／中景驴队溪涧／远景主山；水平亮带（35–60% 高）隔断中远——凝重中的「空气」
4. **方折轮廓＋山顶密林＋水际大石**：轮廓折角（60–120°）≥50% 拐点；峰顶矾头密林深色「冠」；水岸突兀大石 ≥1（宽 ≥15%）
5. **一线悬瀑＋点景渺小＋界画「铁屋」**：悬瀑垂直亮线（宽 ≤1%、高 ≥10%）、湍泉 3–5 级；人物 ≤1.5% 画高；寺观结构逐一可辨

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Monumental Northern Song landscape hanging scroll in the manner of Fan Kuan (范寬, c. 950–1030):
ink and light color on silk; one colossal central peak towering over the composition, occupying
about two thirds of the height, flanked by lower shoulders; the whole mountain mass built from
dense, short "raindrop" texture strokes — thousands of tiny centered-tip dashes stippled in
overlapping layers, direction varied but never chaotic, so the rock face reads as solid,
weather-beaten mass; contours drawn with angular, faceted ink lines; the summit crowned by a
dark band of dense scrub and conifer dots; midway down, a band of empty silk — mist — cuts the
mountain from the middle ground, leaving the peak suspended; a single thin waterfall falls from
a cleft, a white thread against dark rock, splashing into stepped rapids; in the lower quarter
huge boulders block the stream; trees with exposed claw-like roots, pines with needle clusters,
broadleaf trees as outlined leaf-clusters in faint color; at bottom right a tiny mule train of
four donkeys with two drivers winds along the road, barely visible against the mountain, and a
temple complex of precise tiled roofs half hidden among trees; wet, dark, layered ink — deep
shadow, "dark as dusk" — against a glowing ochre-brown silk ground; overall mood: sublime,
still, monumental; nature greater than man
```
**负向约束（`--no` 风格）**
```
--no saturated color, blue-green mineral pigments (azurite, malachite), gold, decorative
prettiness, sweet flowers, 3D or photorealistic rendering, western single-point perspective,
vanishing point, aerial perspective haze covering everything, symmetrical framing, human
figures larger than a fingertip, close-up faces, narrative action, glossy sheen, oil impasto,
flat vector style, uniform-width clean outlines, crosshatching, regular parallel hatching,
color-separated pointillism (Seurat-style dots of pure color), long wavy hemp-fiber strokes,
dry-brush feathering as the main texture, long horizontal handscroll format, bright daylight
glare, ukiyo-e or anime style
```

## 代码艺术规则（§8.2 原样）

1. **雨点皴覆盖**：主山区域（最大连通山体）内，短笔触（长度 ≤ 主山高 2%）纹理覆盖率 ≥ 60%；笔触方向角标准差 ≥ 20°（防规整排线）；不得出现单一方向平行排线占比 ≥ 30%。
2. **巨碑主山**：最大山体连通域高度 ≥ 画面高 60%；其水平重心与画面中线偏差 ≤ 10% 宽；顶部距画面上缘 ≤ 5% 高（或直抵上缘）。
3. **墨色层次**：山体区域明度直方图呈 ≥ 3 个可辨带；深色（≤40% 亮度）像素占山体面积 25–60%；不得出现内部标准差 < 5% 的平涂块（防死黑/防平涂）。
4. **云雾留白带**：≥ 1 条水平亮带（亮度 ≥ 纸色 90%）横贯 ≥ 60% 宽、位于画面高 35–60% 区间、面积占比 8–25%；带内连续墨线覆盖 ≤ 3%。
5. **悬瀑**：≥ 1 条垂直亮线（宽 ≤ 画面宽 1%、高 ≥ 画面高 8%、亮度 ≥ 纸色 95%），位于山体上 1/3–1/2 裂隙处。
6. **点景比例**：人物/驴马高度 ≤ 画面高 1.5%；总数 ≤ 8；全部位于画面下 1/4；面部无可辨细节（特征尺度 ≤ 3px）。
7. **轮廓方折**：主山轮廓拐点中折角（60–120°）占比 ≥ 50%；恒定曲率长弧 ≤ 30% 周长。
8. **点景与动画（动画时）**：云雾漂移 ≤ 0.5%/秒；瀑布允许纵向流动（≤ 2px/帧）但水线水平位置固定；点景位移 ≤ 1% 画幅/秒；不得出现推拉镜头、人物动作与墨迹闪变（帧间差 ≤ 1%）。

## 控制参数（§4 原样）

**P1 雨点皴密度（Raindrop-stroke Density）**（默认 强）`[归纳]`
- 弱: 皴点稀疏，山体以轮廓＋淡染为主（雪景简笔式）
- 中: 皴点成片但不塞满，留出山体结构线
- 强: 千笔万笔密布、层层叠搭（《谿山行旅图》式满皴）

**P2 主山压迫度（Monumental Dominance）**（默认 强）`[归纳]`
- 弱: 主山占画面高 ≤40%，群峰并置（平远式）
- 中: 主山占 40–60%，有陪峰
- 强: 主山占 ≥60%、中轴耸立、顶天立地（巨碑式）

**P3 墨色浓度（Ink Darkness）**（默认 中–强）`[归纳]`
- 弱: 淡墨为主、层次清爽（雪景留白多的画面）
- 中: 浓淡相济、山体层次 3 级可辨
- 强: 湿笔浓墨、深暗浑厚（「深暗如暮夜晦暝」；注意上限——「土石不分」为退化）

**P4 云雾留白带（Mist Band）**（默认 中）`[归纳]`
- 弱: 云雾仅局部点缀（≤5% 面积）
- 中: 山腰一条横向留白带（8–15% 面积、横贯 ≥60% 宽）
- 强: 大面积云雾缭绕、山体如浮（≥15% 面积，多带）

**P5 点景渺小比（Point-scenery Scale）**（默认 强=渺小）`[归纳]`
- 弱: 点景清晰可辨、高度 ≤ 画面高 3%
- 中: 点景高度 ≤ 2%、位于下 1/3
- 强: 点景高度 ≤ 1.5%、隐于下 1/4（《谿山行旅图》驴队式）

**P6 轮廓方折度（Angular Contour）**（默认 强）`[归纳]`
- 弱: 轮廓多圆弧长线
- 中: 方折与圆弧相间
- 强: 方折墨线主导、折角分明（山石如斧凿）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 黄公望）**（× 黄公望；本卡 §3.1 分工条款）：北宗／南宗式对照四轴写死：密点／巨碑／浓墨湿笔／立轴 vs 长线／长卷／淡墨积叠／手卷——判据四条，两卡禁项互列
- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款）：皴法质感 vs 等宽线：毛笔提按短点千叠 vs 刻线等宽＋平涂——媒介／质感生成／空间三判据
- **分工（vs 塞尚）**（× 塞尚；本卡 §3.1 分工条款）：山体量感两条路径：密点积墨 vs 色块调制＋几何推导——量感来源／空间／笔触单元三判据
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：笔触／线条、墨色浓度、负空间

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/fan_kuan.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
