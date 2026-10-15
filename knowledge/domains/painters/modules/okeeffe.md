# 欧姬芙 模块卡 — `okeeffe`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/okeeffe.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **单主体放大＋出框裁切**：1 个主形 ≥70% 画幅、≥1 处被边缘裁切、无环境参照——「make them look big like the huge buildings」
2. **抽象简化（选择／剔除／强调）**：细节结构 ≈0、形状 ≤5 组主形；系列末尾近乎纯抽象（「只剩 jack 本身」）——不画植物学细节
3. **清晰轮廓＋连续柔和渐变**：轮廓干净、内部无缝渐变（肉感／曲面）、笔触可见度 ≈0——「crisply contoured forms, subtle tonal transitions」
4. **尺度错位＋系列演进**：花＝建筑级、骨＝山水级；同母题 6–8+ 版单向递进（写实→抽象）——系列是方法不是重复
5. **平光＋浅空间＋物作为主体**：投影 ≈0、画内光源＝0（光＝清晰度）；无透视、背景即色域；人物出现率 ≈0（花／骨／山／门／云）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Georgia O'Keeffe-style magnification painting — one small thing enlarged until it becomes the whole world:
a single subject — a flower, a bone, a shell, a hill, a door — filling the canvas, cropped by the frame,
pressed close to the picture plane so there is no environment, no horizon, no context;
forms simplified to a few sweeping curves and ovals — selection, elimination, emphasis — no botanical detail,
no texture noise, no busy edges;
smooth seamless gradations modelling soft volume — petals like flesh, bone surfaces like dunes —
crisp clean contours over continuous tonal transition, no visible brushwork, no impasto;
an even, shadowless light — light as clarity, no cast shadows, no dramatic contrast, no light source in frame;
soft high-key palette of blush pink, ivory, pale blue and grey-green, with one small saturated accent
held at the core of the subject — a red canna, a yellow sun, that blue that will always be there;
shallow flat space — the background is a color field, not a place;
quiet monumental scale — the small thing treated like a skyscraper, the desert reduced to bands;
a series sensibility: this canvas is one step in a sequence, from realistic to almost pure form;
20th-century American modernism, oil on canvas, smooth matte surface, museum reproduction quality
```
**负向约束（`--no` 风格）**
```
--no multiple subjects, pattern all-over decoration, flat hard-edged color blocks, wallpaper or textile motifs,
harsh shadows, chiaroscuro, dramatic lighting, cast shadow, multiple light sources, glow, bloom, god rays,
visible brushstrokes, impasto, palette-knife texture, broken color, pointillism, dotted brushwork,
photo-realistic detail, botanical illustration, insects, still-life tabletop with many objects,
deep perspective, vanishing point, wide establishing landscape, horizon line in close-ups,
neon colors, high-saturation color clash, gradient banding, HDR gloss, 3D render, anime, cartoon,
text, signature, watermark, frame
```

## 代码艺术规则（§8.2 原样）

1. **单主体规则**：全帧最大连通主体占画幅 ≥70%（强档；中档 ≥50%）；存在 ≥1 处主体被画框裁切；第二主体（若有）面积 ≤10% 且不与主体同权。（自查：分割 + 面积比；对照 §3.1 判据①）
2. **简化规则**：主体轮廓的曲率拐点 ≤12 个（强档；中档 ≤24）；细节结构（<2% 画面的碎块）数量 ≤3；纹理能量（高频分量占比）低于参考帧的 30%。（自查：边缘曲率 + 频域；对照 §3.1 判据②——「无平涂块、无硬边色界」）
3. **无缝渐变规则**：主体内部亮度梯度连续（相邻 16px 窗口均值差 ≤2/255）；全帧「平涂色块」（面积 ≥5% 且内部标准差 ≤1.5/255）数量 = 0；无带纹（gradient banding 检测）。（与 C-05 对齐：全片 0 帧可见笔触；与 C-14 对齐：渐变必须存在且无缝）
4. **平光规则**：投影区域（由主光源方向推算的阴影连通域）面积 ≤2% 画幅；画内可见光源计数 = 0；全帧明暗对比（P95−P5 亮度差）≤120/255（柔档）。（与 C-01 同侧：显式声明「无投影」；对照 §3.1 判据⑤）
5. **色彩规则**：全帧中位饱和度 ≤0.45；高饱和像素（S>0.6）占比 ≤8% 且集中为 ≤3 个连通域、均与主体核心相交；色相家族 ≤6（软色域）；蓝系允许作为底域在场。（对照 C-06：欧站低饱和侧、显式取值）
6. **尺度规则**：主体感知尺度标记——单主体长边 ≥画幅长边 80%（微距档）；或极端画幅比（≥2:1，天空/沙漠档）且地平线缺失或位于上/下 1/8 之外。（自查：构图模板 + 地平线检测）
7. **系列规则**（系列模式时启用）：组内帧数 ≥3；跨帧「简化度」单调不减、「放大度」单调不减（允许平台期）；组内主体类别恒定（同母题）；组内背景色域变化 ≤1 个色相族。（自查：跨帧指标序列；对照 §3.1 判据④——单向递进）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1/2/4/5 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。与 `conflicts.md` 的关系：**C-01**（硬阴影——欧站「无投影」侧、同侧声明）、**C-05**（笔触可见度——欧站「无笔触」侧、与梵高/莫奈硬冲突）、**C-06**（饱和度——欧站低饱和侧）、**C-14**（渐变——须改写 Lane B 反约束）为组合预检重点。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **放大与裁切（Magnification/Crop）**`[归纳]` | 主体 ≤50% 画幅、含环境参照 | 主体 50–70%、轻微裁切 | 微距：主体 ≥70%、被边缘裁切、出框（无环境） | **80%** |
| P2 | **简化度（Simplification）**`[归纳]` | 保留结构细节（可辨认脉络/明暗层次） | 形状简化、细节省略（花可辨、无纹理） | 近乎抽象：只剩轮廓/色域（系列末张档） | **70%** |
| P3 | **系列推进（Series Progression）**`[归纳]` | 单件独立（无系列语境） | 2–3 版本变体（同母题微调） | ≥5 版本演进链（写实→抽象单向递进） | **50%** |
| P4 | **色彩柔和度（Chromatic Softness）**`[归纳]` | 硬色块/高对比（近平面档——越界警报） | 柔和高调＋1–2 处饱和重音 | 连续柔和渐变为主（蓝绿音乐档：全帧无硬色界） | **65%** |
| P5 | **平光度（Light Flatness）**`[归纳]` | 可见明暗对比与投影（越界警报） | 平光、弱投影、低对比 | 全平光：无投影、无画内光源（光＝清晰度） | **85%** |
| P6 | **尺度错位（Scale Displacement）**`[归纳]` | 正常比例（1× 感知） | 轻微放大（2–3× 感知） | 极端错位（花如建筑、骨如山水；Sky IV 档） | **75%** |

> **用法**：P1/P5 定「是不是欧姬芙」的起步（两条中 ≥1 条 ≥ 中档才成立——单主体放大或全平光）；P2/P6 定简化与尺度档；P3/P4 定系列与色彩档。三档描述可直接当判定标准写进自查表。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若「多元素平铺＋平涂纯色＋图案同权」→ 越界**马蒂斯**（P4 弱档连用即越界）；② 若「破碎笔触＋有色阴影＋环境光场」→ 越界**莫奈**（P5 弱档连用即越界）；③ 若「硬光戏剧＋近黑背景＋画外单光源」→ 越界**卡拉瓦乔/伦勃朗**；④ 若「人造光几何＋建筑精确＋投影计算」→ 越界**霍珀**；⑤ 若「点彩/光学混合」→ 越界**修拉**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §3.1 分工条款）：平面 vs 放大：平涂／多元素／尺度恒定 vs 单主体／连续渐变／出框——判据四条（≥2 轴联合），边界注（剪纸／Black Cross）
- **分工（vs 莫奈）**（× 莫奈；本卡 §3.1 分工条款）：系列：光驱动 vs 形式驱动（放大／简化单向递进）——判据四条（≥2 轴联合），边界注（睡莲／Evening Star）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记（预检写死））：重点：C-05 笔触（无笔触侧，与梵高／莫奈硬冲突）／C-06 饱和度（低饱和侧）／C-14 渐变（句式改写）／C-01 硬阴影（无投影，显式声明）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/okeeffe.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
