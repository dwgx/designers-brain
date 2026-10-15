# 克里姆特 模块卡 — `klimt`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/klimt.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **金是材质，不是黄色颜料**：金／银／铂金箔直接施于画布；箔块接缝与碎屑可见——「画出来的表面」
2. **双分辨率共存**：写实面孔／手（体积塑形）× 平面图案（无体积渐变）；渲染落差 ≥1–2 级
3. **图案词汇固定**：螺旋／圆／「全视之眼」／方块／三角／十字／花点；角形给男性、圆形给女性
4. **平面化、取消透视**：无消失点、无投射阴影；近方形画幅＋满幅构图（主体包围盒 ≥60%）
5. **装饰配色＋材质对比**：金＋黑＋红＋蓝绿；同屏 ≥2 种材质（金属／油画肌理／平涂图案）清晰可分

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
decorative Art Nouveau painting in the manner of Gustav Klimt's golden period:
figures with realistically modelled faces and hands in soft oil paint, bodies
dissolving into flat ornamental garments; the picture reads as a flat decorated
surface, like a precious object, not a window into space; large fields of genuine
metal leaf applied to the canvas — gold, silver, platinum and composition-gold
(brass) grounds with visible square leaf seams, sprinkled metal flakes and
speckles; dark brown glaze over the metal; dense flat pattern vocabulary —
spirals, concentric circles, eye motifs, squares, checkerboards, triangles,
crosses, flower dots — covering garments, halos and background; fine firm
contour lines around faces and hands; no linear perspective, no cast shadows,
no volumetric modelling in the ornamental zones; near-square format, figure
cropped by the frame and fused with the ornament; palette: gold, black,
vermilion red, cobalt blue, emerald green, white; motifs: embrace, tree of
life, life-and-death allegory, femme fatale
```
**负向约束（`--no`）**
```
--no photographic realism, 3D render, CGI metal shader, uniform airbrushed
gold gradient, perfect mirror chrome, HDR, lens flare, depth of field,
linear perspective, vanishing point, cast shadows, chiaroscuro, sfumato,
airbrush soft gradients, watercolor wash, pastel palette, matte flat vector
cartoon, textureless solid gold fill, symmetric centred layout, watermark, text
```

## 代码艺术规则（§8.2 原样）

1. **金属材质规则**：金属区（镜面反射 + 箔块特征）面积 ≥30%（默认档；弱档 10–30%、强档 ≥50%，对应 P1）；金属区亮度动态范围（P95−P5，0–255 尺度）≥40%；可辨箔块边界（局部亮度跃变 ≥30）≥3 处；**平滑无特征渐变金属面积 ≤5%**（防 CG 金）。自查：镜面掩膜 + 亮度跃变扫描。
2. **图案密度可测（P2 的可判定定义；A_p/L_p 口径与 `matisse.md` §8.2 规则 8 同尺 + 材质硬约束）**：纹样覆盖面积比 $A_p$——**弱** $A_p\le5\%$；**中** $15\%\le A_p\le35\%$；**强** $A_p\ge50\%$（$L_p$ 同对方口径）。**克里姆特硬约束：纹样区内部明度动态范围 ≥10%（默认）/ ≥15%（强档）；≤5% 判为越界（马蒂斯 P4 域）、5–10% 为灰区（记警告，不得单独用于区分两人）**。自查：纹样掩膜 + 区域直方图。
3. **材质对比度规则**：同帧可辨材质类别 ≥2（金属 / 油画颜料 / 平涂图案 / 写实皮肤）；以镜面高光像素占比聚类——金属区 ≥15%、颜料区 ≤5%，两簇分离度（均值差/标准差）≥1.5。自查：材质聚类。
4. **写实-装饰渲染落差规则**：面孔+手区局部方差（9×9 窗口均值）与图案区局部方差之比 **≥2.0**；面孔区存在连续体积过渡（同向亮度梯度段 ≥3）；图案区无体积渐变（受规则 2 约束）。自查：局部方差图分区比。
5. **平面化规则**：消失点检测 = 0；投射阴影面积 ≤1%（画面内方向性软暗带 = 0）；空间深度仅由遮挡与图案区块位置提供。自查：透视线检测 + 阴影方向性检测。
6. **图案词汇与尺度规则**：允许单元集 {螺旋、圆/同心圆/眼、方块/棋盘、三角、十字、花点}；单元尺度（短边）∈ [2%, 15%] 画面短边；可检出重复周期 ≥3 个（自相关峰值）。自查：单元分类 + 自相关。
7. **构图与运动规则**：宽高比 0.8–1.25（近方形）；主体（人物/树/死亡）包围盒 ≥60% 画幅；动画时：金属光泽流动（镜面移动）≤2 px/帧、图案层**禁止物体级动画**、每 10 秒 ≥3 个 ≥0.8 秒静止构图、禁止快速硬切。自查：帧间光流 + 静止段统计。

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（见 §10）；规则 2 与 `matisse.md` §8.2 规则 8 配套使用（同尺 + 材质分界）；C-15 回填接口见 §10。

## 控制参数（§4 原样）

**P1 金箔/金属覆盖率（Metal Coverage）**（默认 60%）`[归纳]`
- 弱: 金属仅点缀（<20%：首饰、边框、局部衣饰），主体为油画色域（1898 前及部分晚期稿）
- 中: 20–50%：人物与图案主体为颜料，背景/衣饰大面积金属（《朱迪斯》《水蛇》一类）
- 强: ≥50%：金属底满铺 + 碎屑（《吻》《阿黛尔 I》级；粗测：二图金色相区 ≈72%/82% 画面，含金黄颜料区，见自审 C）

**P2 图案密度（带材质版，Pattern Density with Material）**（默认 55%）`[归纳]`
- 弱: 图案区 ≤5%（纯色 + 少量纹样）——此时必须同时检查材质约束，否则趋近马蒂斯边界
- 中: 15–35%：成组纹样覆盖衣饰/背景块面，纹理明度动态范围 ≥10%
- 强: ≥50%：满画面纹样 + 金属/纹理密度差（《阿黛尔 I》《死与生》生命侧）
- **边界注（与马蒂斯 P4 的分界判据）**：本参数只允许**带材质**图案——纹样区内部明度动态范围 **≥10%**（默认）且与主体区存在材质/纹理差；若图案区与主体区处理无差别（明度动态范围 ≤5%、同线宽同色阶层数）→ 判为**马蒂斯 P4 域**，应改用 `matisse.md` 模块（依据：`expansion.md` §6-B7；`matisse.md` §4 P4 边界注 + §8.2 规则 8）。面积档位与对方同尺（弱 ≤5% / 中 15–35% / 强 ≥50%），**差异只在材质硬约束**。

**P3 材质对比度（Material Contrast）**（默认 60%）`[归纳]`（expansion §1.5 立档：同屏 ≥2 种材质清晰可分）
- 弱: 单一主导材质（近单材质画面；<2 类可辨）
- 中: 同屏 2 种材质清晰可分（金属 + 颜料）
- 强: ≥3 种（金属/油画肌理/平涂图案/写实皮肤）清晰可分，边界可辨

**P4 纹理明度范围（Texture Value Range）**（默认 50%）`[归纳]`（expansion §1.5 立档；对侧硬约束 ≤5%）
- 弱: ≤5%（贴马蒂斯平涂边界——本模块不取，标注越界）
- 中: 5–15%（纹样内部有轻度明暗/材质起伏）
- 强: ≥15%（纹样内明暗与金属光泽起伏明显；《吻》衣饰、《阿黛尔 I》裙）

**P5 写实-装饰渲染落差（Realism–Ornament Render Gap）**（默认 60%）`[归纳]`（expansion §1.5 立档：差 ≥1 个渲染级别）
- 弱: 落差 <1 级（面孔与图案同一处理等级——越界）
- 中: =1 级（面孔体积塑形 vs 图案平涂）
- 强: ≥2 级（面孔高写实 + 图案完全符号化 + 金属材质层介入）

**P6 象征符号负载（Symbolic Load）**（默认 40%）`[归纳]`
- 弱: 无象征（纯肖像/纯装饰）
- 中: 单一象征母题（拥抱、树、花田）
- 强: 多层寓言系统（生死循环、命运三阶段、爱与惧）

> 用法：P1/P3/P4 定「是不是克里姆特（vs 马蒂斯）」；P2/P5 定「图案与写实如何对撞」；P6 定「装饰画 vs 寓言画」。三档描述可直接当判定标准写进自查表。
> 材质层声明（对 `conflicts.md` C-15 / N6 的接口）：本模块的金属/金箔/高光材质层**单列、不计入色数上限**；当克里姆特模块为主模块时，金属是**主材质**（面积由 P1 控制，可 ≥50%），N6 的「≤5% 面积」仅适用于**其他模块**的金属点缀豁免。C-15 的实测阈值回填接口见 §10。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-15**（× 马蒂斯 P4 边界；本卡 §4 P2 边界注 + §8.2-2）：色数/图案计数口径：带材质图案（纹样明度 ≥10%）vs 平涂纯色（≤5%）——越界即判马蒂斯 P4 域
- **C-15**（× Lane B 15/14/06/07 卡；本卡 §4 材质层声明 + §8.2-1）：金属/金箔材质层单列、不计色数上限（N6：他模块点缀 ≤5%；本模块为主按 P1 面积档）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/klimt.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
