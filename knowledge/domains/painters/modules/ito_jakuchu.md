# 伊藤若冲 模块卡 — `ito_jakuchu`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/ito_jakuchu.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 11 条）

1. **无轮廓成形**：不靠描边线，形与形由色面直接相接（「absence of outlining」）
2. **色彩浓密＋裏彩色**：高彩度、多色相（≥8 簇）、低饱和区极少；颜色上在绢正反两面（四层结构）
3. **高填充率＋母题重复**：画面几乎被填满（空区 ≤15%）；同一姿态模板重复 ≥10 次（群雀 58 羽）
4. **静态定格**：戏剧性姿态但完全冻结——无风动、无动线；静中有戏
5. **网格量化（升目）＋白羽金泥**：全画面 1cm 方格逐格上色、跨格渐变=0；白不用金而似金（暖白＋层次）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
a dense polychrome bird-and-flower painting on silk in the manner of Ito Jakuchu:
forms modelled entirely by colour — no outlines, no hatching; edges where one colour
area meets another; colours built in layers on both sides of the silk (urazaishiki),
mineral pigments (shell-white gofun, cinnabar, malachite, azurite, orpiment) worked
together with transparent dyes; near edge-to-edge composition — birds, fish, flowers,
insects packed toward the borders, almost no empty background; repeated poses and
rhythmic motif patterns reading like a design pasted onto the space; frozen theatrical
postures (a rooster striking a kabuki-like pose, a bird twisting to preen), everything
perfectly still; minute, meticulous detail — every feather, scale, petal and insect leg —
yet the whole reads as ornament; matte surfaces, no metallic shine; whites are
shell-white over an ochre back-layer, glowing like gold without gold; palette:
shell-white, cinnabar red, malachite green, azurite blue, orpiment yellow, ochre,
deep dye-greens, ink accents; high chroma, high fill, even enamel-like finish
```

**负向约束（`--no` 风格）**
```
--no outlines, black contour lines, hatching, crosshatching, metallic gold leaf,
gold foil, shiny metal, 3D render, photographic realism, soft blur, airbrush,
empty white background, minimalism, pastel colours, muted colours, fog,
atmospheric haze, motion blur, windswept motion, dynamic diagonal composition,
ukiyo-e wave curves, single uniform keyline, cel shading, gradient mesh,
drop shadows, glowing highlights, monochrome
```

## 代码艺术规则（§8.2 原样）

1. **无描边**：不存在宽度 ≥2px 且连续长度 >20px 的均匀深色轮廓线；相邻色区边界色差 ΔE ≥ 15（边界可读但不靠线）。
2. **彩度/色数**：色相簇 8–14 个；饱和像素（S ≥ 40%）占比 ≥55%；平均饱和度 ≥50%；低饱和区（S <15%）≤15% 面积。
3. **填充率**：主体覆盖 ≥85% 画面；最大连续背景空区 ≤8% 面积；空区只能作水面/天空且必须带色（不得为白纸）。
4. **升目模式（P3=100% 时）**：格边长 = 画面短边的 1/40–1/120；跨格渐变 = 0（相邻格独立取色）；每格主色数 = 1（允许格角 1 处加深）；格线对齐误差 ≤0.3 格。
5. **裏彩代理（图像级）**：白/浅色区色温相对中性偏暖（+200~600K）；镜面高光（亮度 >95% 且低饱和的孤立斑点）面积 ≤0.3%；「金色感」只能来自暖白+明度层次，不得出现金属反射带。
6. **姿态冻结（动画）**：主体像素位移 ≤1px/帧；允许的动只有极慢介质（水波 ≤2px/帧、无风感）；禁止翅膀/尾羽/花瓣的连续摆动（对照北斋「曲线族动势」互斥）。
7. **重复模板**：同类单元（鸟/鱼/花/虫）出现 ≥5 个时，姿态模板 ≤3 种；模板的分布呈图案节奏（间距变异系数 ≤0.3），不得随机散布。
8. **墨线规则**：墨只作两种用途——极细结构线（宽 ≤1.5px）与点/苔；不得用墨做大面积暗部（暗部由深色染料/颜料叠加，暗部不得出现纯黑 <5% 明度区块 >2% 面积）。

## 控制参数（§4 原样）

**P1 色彩浓密度（彩度×覆盖）**（默认 75%）`[归纳]`
- 弱：淡彩/一色——水墨或淡着色（晚年水墨、菜蟲譜灰底）
- 中：彩色但留底色空区（早期花鸟、部分押绘贴屏风）
- 强：高彩度满覆盖、多色相并置（動植綵絵 多数；向日葵雄鶏図）

**P2 画面填充率**（默认 80%）`[归纳]`
- 弱：覆盖 ≤50%（留白明显）
- 中：50–75%（主体+背景层次）
- 强：≥85%——空区只作水面/天空通道（牡丹小禽図、群鶏図）

**P3 网格化强度（升目/图案量化）**（默认 0%；实验档 100%）`[归纳]`
- 弱（0–20%）：纯写生，无格网、无模板重复
- 中（40–60%）：母题重复+图案化倾向（群雀「贴纹样」、空间填充纹样）
- 强（90–100%）：全画面 1cm 级均匀方格逐格量化（升目描き：鸟獣花木図屏風/樹花鳥獣図屏風/象と鯨図屏風）

**P4 裏彩深度（背面色彩层）**（默认 60%）`[归纳]`
- 弱：无裏彩或仅局部提亮（松叶薄裏彩）
- 中：关键元素裏彩（花萼绿青、瀑布胡粉、土坡黄土）
- 强：主体多层裏彩——白羽=胡粉+黄土（「白羽の下に金泥」档）；雪=正反双面胡粉

**P5 墨彩比（ink–colour balance）**（默认 20% 墨）`[归纳]`
- 弱：墨仅作线/点（纯浓彩）
- 中：墨参与造型（水墨淡彩：松梅群鶏図屏風）
- 强：墨一色为主（海宝寺群鶏図、墨竹、晚年简笔）

**P6 群像密度（多主体度）**（默认 中）`[归纳]`
- 弱：单主体（一鸡一花）
- 中：2–5 主体（双鸡、对幅）
- 强：群体 ≥10（群鶏 13 羽、群雀 58 羽、群鱼、五百罗汉）

> 用法：P1/P2 决定「是不是若冲的浓密」，P3 决定「写生↔升目」档位，P4 决定「色深不深」，P5/P6 决定题材面貌。三档描述可直接进逐帧自查表。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 北斋）**（× 北斋；本卡 §8.2-1/-6/-8）：线／动势／色彩三判据：等宽单线＋曲线族动势＋色数 ≤7 vs 无描边色面＋静态＋多色——负向段须重算（N1）
- **分工（vs 克里姆特）**（× 克里姆特；本卡 §8.2-5）：材质／图案／色彩逻辑三判据：金箔金属 vs 颜料模拟（暖白＋层次）；升目网格 vs 曲线图案块——「金色」来源二选一
- **分工（vs 马蒂斯 / 丢勒）**（× 马蒂斯 / 丢勒；本卡 §8.2-2）：平涂纯色（≤5%）/ 排线明暗 vs 有材质感的颜料层积——出现材质／纹理明度差即非马蒂斯域

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/ito_jakuchu.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
