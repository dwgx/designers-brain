# 透纳 模块卡 — `turner`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/turner.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **大气占主导、地平线被「吃掉」**：雾／雨／雪／蒸汽吞噬远景；渺小人类与船被天气吞没（崇高尺度）
2. **边缘溶解分级（0–100%）**：0%＝轮廓清晰；100%＝完全溶解于光雾——晚期实验画「no outlines」
3. **光源＝全图最高明度点**：日／月／火为单一最亮核＋放射渐变；低角度逆光剪影
4. **两种动势结构：对角线／旋涡**：事件级动势（铁路／船身／栈桥；风暴的雪、浪、烟）
5. **透明叠色＋色温梯度**：水彩逻辑入油画（透明层叠加、留白／刮亮）；亮部推白／金、暗部转紫冷

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
oil painting in the style of J.M.W. Turner, british romanticism,
weather as the protagonist: a storm, gale or fiery sunrise dominating
the whole scene, atmosphere swallowing the horizon, sublime terror
and grandeur, extreme edge dissolution — outlines melt into light,
fog, spray and rain, luminous vortex of wind, clouds, snow and sea,
single dramatic light source (sun or fire) as the brightest point,
radial glow spreading through mist, backlit silhouettes, vast nature
against tiny human figures, thin translucent glazes like watercolour
built up in many layers, light glowing from beneath the surface,
paint dragged, dabbed, scraped and scumbled, palette-knife flecks of
spray, warm light — white, gold, orange, crimson — against cool
violet-blue shadows, no neutral greys, strong diagonals and swirling
composition, low horizon or no horizon,
palette: white, gold, orange, crimson, violet, indigo, slate blue,
smoke brown; edges blurred and colours blending into one another
```

**负向约束（--no）**
```
hard outlines, crisp horizon line, flat even lighting, cloudless
clear sky, calm static water, muddy brown shadows, smooth clean
digital gradients, photographic detail, sharp vector edges, neon
saturation, complementary colour clashes, opaque flat impasto
without glazing, symmetrical centred composition, HDR, depth of
field, text, watermark
```

## 代码艺术规则（§8.2 原样）

1. **大气对比规则**：远景（地平线带上 1/3）对比度 ≤ 近景的 40%（强档；中档 40–60%）；从近到远对比度单调下降（线性拟合 R² ≥0.8）。自查：分带（近/中/远 3 带）对比度测量。
2. **边缘溶解规则**：主体边缘区最大梯度 ≤ 全帧最大梯度的 30%（强档）/ 30–60%（中档）；强档下地平线带不得出现全帧最大梯度——最强边缘必须属于光源或动势线。自查：梯度图（Sobel/Canny）+ 地平线带扫描。
3. **色温规则**：暗部（L≤25%）平均色相 H ∈ [230°, 290°]（紫-蓝）；亮部（L≥75%）平均 H ∈ [20°, 60°]（黄-橙）或向白推（S ≤35%）；中性灰像素（S ≤8%）占比 ≤10%。自查：亮/暗部色相统计 + 中性像素计数。
4. **光源规则**：全帧亮度前 0.5% 像素集中于单一连通域（光源）；以光源为中心的径向亮度剖面单调不增（R² ≥0.7）；其他区域亮度峰值 ≤ 光源区的 80%。自查：亮度直方图 + 连通域 + 径向剖面。
5. **动势规则（动画）**：光流方向直方图单峰或双峰（对角线 ±30° / 切向旋转），主方向能量占比 ≥60%；若为旋涡场，存在唯一涡心（|ω| 峰值位于画面 30–70% 区域）；天气元素（雨/雪/浪/雾/烟）位移 ≤3 px/帧、禁止硬切；船/人/建筑等实体对象不做「物体级」动画（只有天气与光在动）。自查：帧间光流 + 涡度图。
6. **叠色/材质规则**：高光区（L≥85%）饱和度 ≤50%（发光感，非白颜料堆砌）；全画饱和度 ≤75%；亮部笔触/层痕密度 ≥ 暗部的 1.2×（能量集中于光与动势线）。自查：饱和度-明度散点 + 分区域边缘密度。
7. **事件完整度规则**：画面含 ≥1 个天气事件元素（雨/雪/浪/雾/烟/火），事件元素覆盖 ≥40% 画面；全画动势方向一致（风向单向，且与光源方位的关系全画统一）。自查：元素分区 + 方向一致性检查。

## 控制参数（§4 原样）

**P1 大气能见度（雾 / 雨 / 雪幕浓度）**（默认 60%）[归纳]
- 弱: 能见度 ≥10 km；远景对比 60–100%，无统一幕色（早期地形画）
- 中: 能见度 3–10 km；远景对比 40–60%，轻度幕色、远处去饱和
- 强: 能见度 <3 km；远景对比 ≤40%，地平线溶解、全画向单一色光收拢（《暴风雪》档；莫奈强档之外）
- 自查：分区对比度 + 地平线梯度（见 §8.2-1/-2）

**P2 边缘溶解强度**（默认 55%）[归纳]（0–100% 天然强度参数）
- 弱 0–30%: 轮廓与地平线清晰可辨
- 中 30–70%: 轮廓软化、形体仍可辨（《无畏号》船体）
- 强 70–100%: 无轮廓、无地平线，形体完全溶解于光 / 雾（《暴风雪》《诺勒姆城堡·日出》）
- 自查：边缘梯度图（主体区最大梯度 / 全帧最大梯度）（见 §8.2-2）

**P3 事件动势强度**（默认 60%）[归纳]
- 弱: 平静 / 微风；单组对角线
- 中: 强风 / 蒸汽 / 急流；多组对角线、方向一致
- 强: 旋涡结构（涡心 + 切向流场）或灾难事件（火 / 沉船），全画面场
- 自查：光流方向直方图 + 涡度估计（见 §8.2-5）
- 注：静水波纹属莫奈领域（其 §4 P5）；本参数只覆盖事件级动势。

**P4 色温梯度（亮暖 ↔ 暗冷）**（默认 65%）[归纳]
- 弱: 中性灰主导，局部暖点
- 中: 亮暖 / 暗冷两段式可测
- 强: 亮部向白 / 金推、暗部向紫-蓝推；中性灰占比极低（色相直方图双峰）
- 自查：亮部 / 暗部平均色相偏移 + 中性像素占比（见 §8.2-3）

**P5 光源戏剧度**（默认 60%）[归纳]
- 弱: 漫射天光，无光源盘
- 中: 单一光源（日 / 月 / 火），放射渐变可读
- 强: 光源为全图最亮、光晕大、边缘溶解于光；低角度逆光剪影（日出 / 日落 / 火光）
- 自查：亮度峰值位置 + 径向亮度剖面单调性（见 §8.2-4）
- Blender 映射：太阳高度角 / 强度 / 体积光半径

**P6 透明叠色层感**（默认 55%）[归纳]
- 弱: 单层厚涂主导，笔触即色
- 中: 2–3 层罩染可读，颜色由层积产生
- 强: 多层透明叠色、发光感（光从底层透出）；高光留出 / 刮出
- 自查：明度-饱和度分层台阶 + 层痕可见度（见 §8.2-6）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 莫奈）**（× 莫奈；本卡 §8.2-1/-2 + §4 P1/P3）：天气事件 vs 户外日常（边界写死）：莫奈强档止步于远景对比 ≤60%；灾难天气、事件动势、边缘完全溶解归透纳
- **分工（vs 莫奈）**（× 莫奈；本卡 §4 P3 注）：静水波纹属莫奈领域（其 §4 P5）；本参数只覆盖事件级动势

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/turner.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
