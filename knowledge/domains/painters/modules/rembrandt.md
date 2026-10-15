# 伦勃朗 模块卡 — `rembrandt`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/rembrandt.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **单光源＋暗部塌陷**：光自侧上方进入、人物从暗里「浮」出；背景压暗但保留微弱层次（非死黑）
2. **面部亮斑地图（签名）**：3–7 处亮斑（前额／鼻梁／颧骨／下巴／唇周）；眼窝留暗、表情读不准
3. **连续衰减（非开关）**：亮→暗为连续渐变、无硬切边——硬切即越界到卡拉瓦乔
4. **窄色域＋大明度差**：赭／棕／黑／暖黄为骨架、红蓝小面积点缀；亮暗比 ≥8:1
5. **厚涂＋半透明叠层**：亮部「用颜料塑皮肤」（近看崩坏、远看成立）；蚀刻排线＝同一明暗逻辑的线条版

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
oil painting in the style of Rembrandt van Rijn, Dutch Golden Age,
a single warm light source entering from high left into a dark room,
the light modelled as a continuous falloff — glowing highlights
dissolving into deep, readable shadows, no hard shadow edges, no
cut-out shapes; on the face a map of a few concentrated highlights
(forehead, nose bridge, cheekbone, chin), eye sockets left in shadow
so the expression stays unreadable — the living, thinking mind behind
the face; narrow earthy palette: ochre, umber, warm browns, bone black,
lead-tin yellow, muted madder red and a whisper of cool blue only as
small accents, low saturation, wide tonal range; thick impasto in the
lit passages, broad loaded brushstrokes, palette-knife dabs, paint
built up like clay, scratches into the wet paint, translucent glazing
layers in the flesh; darks kept thin and sketchy, warm darkness;
textures — fur, velvet, gold, linen, flesh — each told apart by how
the light dies across it; quiet stillness, inner life, a half-length
figure emerging from darkness
```

**负向约束（--no）**
```
--no hard-edged cutout shadows, hard light switch, tenebrism two-level
contrast, no-falloff spotlight, pure black voids, crushed midtones,
flat even lighting across the face, multiple light sources, rim light,
backlight, lens flare, glow, neon colours, high saturation, pastel
palette, photographic realism, smooth airbrushed gradients, 3D render,
cartoon, crisp vector edges, symmetrical centred composition, HDR
```

## 代码艺术规则（§8.2 原样）

1. **光斑地图规则**：高光连通域（亮度 ≥ 0.85 × 帧最大）数量 ∈ [3, 7]，且全部与「面部 / 主体关键区」相交；眼窝区（双眼包围盒）平均亮度 ≤ 面部平均的 60%；鼻梁亮带宽度 ≤ 面部宽的 15%。自查：连通域扫描 + 分区亮度。
2. **衰减连续性规则**：沿主光方向采样，亮度单调下降区间占比 ≥ 80%；明暗边界过渡带宽度 ≥ 8 px；相邻像素亮度跳变 > 12% 的「阶跃边界」像素占比 ≤ 1%。自查：梯度幅值图 + 单调性拟合。
3. **暗部活性规则**：暗区（亮度 < 0.15）内部亮度标准差 ≥ 2/255（非死黑）；纯黑（≤ 0.03）像素占比 ≤ 5%；暗部色相暖（H 20–50°）。自查：直方图 + 暗部色相统计。
4. **厚涂纹理规则**：亮部高频纹理能量 ≥ 暗部的 1.5 ×；笔触特征尺度 8–20 px（晚期档）；亮部边缘「粗糙度」（边界亮度局部方差）高于暗部 ≥ 30%。自查：高频滤波 + 边缘粗糙度。
5. **排线规则（版画 / 线条渲染模式）**：线密度（条/px）与局部亮度负相关，线性拟合 R² ≥ 0.8；暗部叠加 ≥ 2 个方向（交叉角 30–60°）；最亮区留白覆盖率 ≤ 20%。自查：线检测 + 分区密度-亮度回归。
6. **色域规则**：色相簇 ≤ 6；饱和度 S ≤ 50%（强调色除外、面积 ≤ 5%）；明度动态范围 ≥ 8:1（95 分位 vs 5 分位）。自查：色相聚类 + 直方图。
7. **运动规则（动画）**：全帧光强漂移 ≤ 2%/s；光源闪烁（若有烛 / 火）0.5–2 Hz、幅度 ≤ 3%；禁止硬切与「物体级」运动（人 / 物不许动）；面部光斑位置漂移 ≤ 2 px/帧。自查：帧间光流 + 亮度序列。

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（见 §10）；规则 1/2/3 与 §4 P2/P1/P3 对齐，规则 5 与 P6 对齐；与 `caravaggio.md` §8.2 的对应规则**互斥使用**（其 2/3 条为本模块负向）。

## 控制参数（§4 原样）

> 节级声明：以下档位划分与阈值为本项目 `[归纳]`（操作化），不冒充艺术家内心；描述中的引文来自馆方/信件原文（已在 §1–§3 标注）。

**P1 衰减连续性（Falloff Continuity）**（默认 75%）`[归纳]`
- 弱: 明暗之间允许可读的边界与台阶；过渡带 <4 px；仍可有局部硬边（道具、衣褶）
- 中: 过渡带 4–15 px；主要形体边缘柔和；允许少量明确边界
- 强: 全画明暗均为连续渐变、**无硬切边**；沿主光方向亮度单调衰减（无「跳变」）；亮斑边缘弥散 ≥15 px（对比：卡拉瓦乔强档 = 无反射硬光、边界硬——**本模块不采用**）

**P2 面部光斑地图（Face Spot Map）**（默认 70%）`[归纳]`
- 弱: 光只作整体侧向照明（一侧亮一侧暗）；面部亮斑 ≤2 处
- 中: 面部亮斑 3–5 处（前额 / 鼻梁 / 颧骨 / 下巴 / 唇周）；眼窝开始留暗
- 强: 亮斑 4–7 处且分布成「地图」；**眼窝 / 眼周必暗**；鼻梁为最窄亮条；表情读不准（eyes obscured）——「心智在面孔之后」

**P3 暗部塌陷深度（Shadow Depth, readable）**（默认 65%）`[归纳]`
- 弱: 暗部为中间调（≥25% 亮度），层次完整
- 中: 暗部 10–25%，保留可辨结构
- 强: 背景/暗部压至 ≤8–10%，但**仍有微弱层次**（非死黑）；亮暗比 ≥8:1（对比：卡拉瓦乔强档 = 中间调被抽空、直方图双峰——**本模块不采用**）

**P4 厚涂与表面（Impasto & Surface）**（默认 60%）`[归纳]`
- 弱: 表面平滑、笔触隐蔽（早期光洁风）
- 中: 亮部可见笔触与轻微堆叠；褶皱、首饰、织物处厚涂
- 强: 宽笔触 / 刮刀痕；亮部厚涂到立体化（「用颜料塑皮肤」）；**近看崩坏、远看成立**（观看距离设完成度）

**P5 色域收窄（Palette Restraint）**（默认 70%）`[归纳]`
- 弱: 色相较多（≥8 簇），允许冷色场
- 中: 5–7 簇，土色系为骨架，红蓝小面积点缀
- 强: ≤4 簇（赭 / 棕 / 黑 / 暖黄），近单色阶；高饱和只出现在 1–2 个道具/细节上

**P6 蚀刻排线梯度（Hatching Gradient）**（默认 55%，版画 / 线条渲染模式用）`[归纳]`
- 弱: 排线仅作轮廓与浅阴影，密度差 ≤2:1
- 中: 排线密度随暗度增加（3–4 档），最暗处出现交叉排线
- 强: 线密度 = f(明度) 连续函数（暗部叠 2–3 层交叉线）；排线本身塑出光斑与衰减（对照 [R8]「加线加深阴影」）

> **分工口径（与卡拉瓦乔，必须写死，来源 `expansion.md` §6-B2 与 §1.1/§4.3 冲突规则）**：两人同属「从黑暗里打光」一族（视觉结果重叠约 60%，为本批最高，见 `expansion.md` §0.2）。本档案固定为——**伦勃朗 = 光的连续衰减 + 心理（心理化光斑）**；**卡拉瓦乔 = 光的开关 + 物理（硬光戏剧 / 舞台感）**。落到参数上：**本模块 P1 的强档是「连续衰减」**；**卡拉瓦乔的 P1 强档（无反射硬光、无补光）与 P3 强档（中间调压缩、直方图双峰）为其模块专属**——本模块一律不采用、组合实验中不得复制。判分口径：出现「硬切光斑 / 亮暗两级无过渡 / 无反射单光源」→ 判卡拉瓦乔；出现「亮斑地图 + 连续衰减 + 暗部保层次」→ 判伦勃朗。本判据为 `[归纳]`，可被 wave3 组合实验（A-12）推翻；对方档案的同款条款见 `caravaggio.md` §4 分工注。
> **用法**：P1/P2/P3 定「是不是心理化的伦勃朗光」；P4/P5 定材质与色域；P6 只在版画/线条渲染（代码艺术）模式启用。三档描述可直接当判定标准写进自查表（§8.2）。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 卡拉瓦乔）**（× 卡拉瓦乔；本卡 §4 分工口径 + §8.2-1/-2/-3）：光的衰减方式（冲突轴）：连续衰减＋亮斑地图 vs 硬光开关——其 P1/P3 强档整条禁用（N3）
- **分工（vs 达·芬奇）**（× 达·芬奇；本卡 §8.2-2 + §4 P1）：渐变方向性：禁用 sfumato 的全画无向柔边——渐变必须沿光轴单调
- **C-01**（× Lane B 模板；本卡 §8.1 负向段）：顺风项——硬阴影禁令对本模块顺风；须显式写回 directional＋deep readable darks（防默认柔光同化）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/rembrandt.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
