# 修拉 模块卡 — `seurat`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/seurat.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **点阵表面（近看点、退后形）**：纯色小点＋短线并排——「走近看形体溶解为补色点，退后重新聚成」
2. **补色并置（三对固定）**：橙↔蓝、红↔绿、黄↔紫；阴影＝亮部的补色（无黑阴影）
3. **高调白底透光**：白底预备；最亮处（面部／光源／火焰）让白底直接透出（0.5–5%）
4. **静止的横饰带人物**：「as immobile as sculptures」；几何大结构（水平／垂直分区、无线性透视）
5. **点彩边框＋两段表面体系**：四周连续色点边框（与画面色调对立和谐）；balayé 粗笔 → 点彩

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
oil painting in the style of Georges Seurat, neo-impressionist divisionism (pointillism),
a meticulously planned studio composition, the surface built from countless small dots
and short dashes of pure, unblended colour laid side by side, optical mixture of
complementaries (orange against blue, red against green, yellow against violet),
each touch kept distinct, no blending on the canvas, light-coloured white ground left
to show through in the brightest accents, simultaneous contrast: forms darkened along
their contours and lightened just beside them, shadows rendered in the complement of
the light (blue-violet shadows under orange light), figures arranged like a monumental
frieze, mostly in profile or frontal views, as still as sculpture, composition on clear
horizontal and vertical divisions with no linear perspective, a painted border of dots
framing the picture in opposed harmony,
palette: chrome orange, vermilion, cobalt blue, ultramarine, emerald green,
pale yellow-green, lemon and zinc yellow, violet, rose, pale blue-grey neutrals, white
```

**负向约束（--no）**
```
loose impasto, thick sweeping brushwork, gestural strokes, blended or smudged colour,
sfumato, chiaroscuro, black shadows, dark varnished browns, photographic detail,
crisp vector edges, neon saturation, 3D modelling, deep perspective, snapshot
spontaneity, wet-on-wet, palette-knife texture, symmetrical centred composition,
depth of field, HDR
```

## 代码艺术规则（§8.2 原样）

1. **点阵规则**：覆盖率 ≥85%；主点径 2–5 px、间距 2–6 px（1080p 短边基准）；点径分布单峰（CV ≤0.5）；无 >10 px 的无点平滑区（白底透光区除外）。自查：blob 检测 + 平滑区连通域扫描。
2. **白底透光规则**：近白像素（L* ≥92）占比 0.5–5%，且聚成 ≤10 个连通簇（面部/光源/高光）；不得整片留白 >2%。自查：亮度直方图 + 白区连通域。
3. **补色并置规则**：主色对为橙↔蓝（或红↔绿、黄↔紫）；互补色邻接（8 邻域）占比 ≥25%；阴影区色相 = 亮部色相 ±150–210°。自查：色相直方图 + 邻接矩阵。
4. **轮廓对比规则**：形体轮廓两侧 3–8 px 带内平均明度差 ≥20%；暗形体外侧 ≤10 px 存在亮晕（比背景均值 +2–5%）。自查：轮廓剖面采样。
5. **构图规则**：地面/舞台分界线位于画高 25–65%；人物正面/侧面/背面朝向占比 ≥75%；Hough 网格度（水平+垂直）≥60%；无消失点收敛。自查：线段检测 + 透视检查。
6. **边框规则**：四周连续点彩边框，宽 = 短边 1.5–4%；边框主色相与画面主调相差 120–210°。自查：边框区取样 + 色相差。
7. **色相与明度预算**：色相簇 ≤8；纯黑（L* <8）像素 ≤0.5%；平均明度 55–75%。自查：聚类 + 直方图。
8. **运动规则（动画）**：点阵整体静止（帧间位移 ≤0.5 px）；允许光源 ±3% 亮度闪烁（≤2 Hz）与水面微光；禁止物体级运动、镜头推移与颜色平滑过渡（morph）。自查：帧差光流 + 区域亮度时序。

## 控制参数（§4 原样）

**P1 点彩密度（点径与间距的细密程度）**（默认 70%）[归纳]
- 弱: 大点稀布（点径 5–8 px、间距 6–12 px，1080p 短边基准）；或仅局部点彩（《浴场》式「粗斜笔 + 局部点」）
- 中: 标准点阵（点径 2–5 px、间距 2–6 px，覆盖率 85–95%）
- 强: petit point 级（点径 1–3 px、高密度全覆盖 ≥95%；退后仍读出纯净色块）

**P2 光学混合/补色强度**（默认 65%）[归纳]
- 弱: 补色只在关键交界出现（邻接占比 <10%）
- 中: 主色对互补并置（橙↔蓝等，邻接占比 25–40%）
- 强: 全画面按补色系统铺陈（≥40%；「阴影=亮部补色」全面执行）

**P3 大画结构度（横饰带/几何）**（默认 60%）[归纳]
- 弱: 风景/小稿式自由构图（croqueton、海景）
- 中: 单一大主体 + 水平分带
- 强: 多人物横饰带 + 正面化/侧面化 + 几何网格分区（《大碗岛》《阅兵》《康康舞》）

**P4 线条方向表达（Charles Henry 轴）**（默认 50%）[归纳]
- 弱: 以水平线为主（平静档）
- 中: 水平与上行混合
- 强: 上行线主导（欢快/动感：《康康舞》《马戏》）或下行线主导（悲伤）——按目标情绪定向

**P5 边框强度**（默认 50%）[归纳]
- 弱: 无边框
- 中: 窄点彩边框（短边 1.5–2.5%）
- 强: 完整宽边框（短边 2.5–4%），与画面色调对立（opposed harmony）

**P6 明度基调与白底透光**（默认 55%）[归纳]
- 弱: 中低明度、无透白
- 中: 明亮但白底不透出
- 强: 高调 + 白底在面部/光源/高光处透出（1–5% 面积）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 莫奈）**（× 莫奈；本卡 §8.2-1）：表面/笔触轴：逗号笔触（4–12 px、覆盖 90–100%）vs 点阵（点径 2–5 px、≥85%）——同轴不可叠加，二选一或分区
- **分工（vs 莫奈）**（× 莫奈；本卡 §8.2-3/-4）：深度/色轴：大气包络（远景对比 ≤60%）vs 系统性补色对＋对比/晕——取值口径不同，组合时写死取值

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/seurat.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
