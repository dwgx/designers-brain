# 莫奈 模块卡 — `monet`

> A-19 模块库 ｜ 来源：档案 `research/artists/monet.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `research/agent-art/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **短逗号笔触、并置不混合**：高调浅色底；笔触「一笔一笔放上去」（示范间距约 1 英寸、厚 0.25 英寸）
2. **有色阴影、无黑**：阴影蓝紫（蓝天反射），不用黑
3. **大气包络**：同一道光铺满全画（enveloppe）；远景对比下降
4. **水面／天空镜像母题**：非对称、去线性透视、平面化
5. **系列重复**：同一母题 × 不同时刻／天气（干草堆／白杨／鲁昂大教堂）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
oil painting in the style of Claude Monet, french impressionism,
en plein air, broken comma-like brushwork with unblended strokes laid
side by side, light-toned ground and high-key palette, coloured shadows
(blue-violet) instead of black, atmospheric envelope unifying the whole
scene, soft haze and shimmering water with broken reflections,
asymmetrical cropped composition with no linear perspective and no
three-dimensional modelling, water surface occupying a large portion of
the canvas, sky and water mirroring each other,
palette: pale blue, lavender, rose, cream, turquoise, soft green,
pale yellow; soft edges dissolving between colour patches
```

**负向约束（--no）**
```
hard black outlines, chiaroscuro, dark varnished browns, smooth blending,
photographic detail, crisp vector edges, studio lighting, neon saturation,
3D modelling, symmetrical centred composition, depth of field, HDR
```

## 代码艺术规则（§8.2 原样）

1. **笔触规则**：短逗号形笔触，长 4–12 px、间距 2–6 px，覆盖率 90–100%；不得出现 >12 px 的无笔触平滑区。自查：边缘密度图 + 连通域扫描。
2. **明度规则**：全画平均明度 ≥65%（0–100）；纯黑像素（明度 <8%）占比 ≤0.5%；暗部色相偏蓝紫（H 220–280°）。自查：直方图 + 暗部色相统计。
3. **色相规则**：色相簇 ≤10 个；相邻簇明度差 ≤25%（浅色系并置）；饱和度中低（S ≤65%），避免高饱和撞色。自查：逐帧色相聚类。
4. **包络规则**：远景对比度 ≤ 近景的 60%；从远到近存在单调对比度梯度（线性拟合 R² ≥0.8）。自查：分区对比度测量。
5. **倒影规则**：若含水面，倒影区色相分布与上方天空区相关性 ≥0.7，且倒影区边缘密度低于实物区 ≥50%（倒影更碎更糊）。自查：色相直方图相关 + 边缘密度比。
6. **构图规则**：地平线在画高 30%–55%；左右视觉质量差 ≥15%（非对称）；无线性透视消失点收敛于画面中心。自查：质量分布 + 透视线检测。
7. **运动规则（动画）**：水面波纹位移 ≤2 px/帧、周期 1.5–3 s；雾气漂移 ≤1 px/帧；禁止快速硬切与「物体级」动画（船/人不许动，光与水面才动）。自查：帧间光流。

## 控制参数（§4 原样）

**P1 笔触破碎度**（默认 70%）[归纳]
- 弱: 笔触较大且彼此相接，形体边缘可读（早期勒阿弗尔时期）
- 中: 短逗号笔触为主，色块并置，边缘溶解
- 强: 极碎笔点（1–3 px 级）+ 高密度并置，近看是「乱色风暴」，退后成形（《印象·日出》水面、晚期睡莲）

**P2 明度基调（高调程度）**（默认 65%）[归纳]
- 弱: 中性明度，允许深绿/深褐
- 中: 整体偏亮，暗部不超过中灰
- 强: 全画高调、浅底透光，最暗处仍可读（雪景系列）

**P3 大气包络强度**（默认 50%）[归纳]
- 弱: 远景对比为近景的 80–100%，基本无统一雾色
- 中: 60–80%，远景轻度去饱和
- 强: ≤60%，全画色相向单一大气色收拢（雨/雾/晨昏；边界外=透纳领域）

**P4 阴影着色度**（默认 60%）[归纳]
- 弱: 阴影略偏蓝
- 中: 阴影明确蓝紫、无黑
- 强: 阴影即彩色场（紫/绿/粉），与亮部同为色彩事件

**P5 倒影/水面占比**（默认 40%）[归纳]
- 弱: 水面 <20%，倒影弱
- 中: 20–50%，倒影可辨、破碎
- 强: ≥50%，水面即主题（睡莲/泰晤士河系列）

**P6 系列变奏幅度**（同一构图的组内差异；工作流参数）[归纳]
- 弱: 同一时刻 2–3 张微差
- 中: 不同时段 4–8 张（晨/午/昏）
- 强: 全天+天气全谱 10+ 张（鲁昂大教堂式）

## 冲突注记（→ conflicts.md）

组合前先读 `research/agent-art/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-05**（× 达·芬奇；本卡 §8.2-1）：笔触可见度（90–100% 覆盖 vs 只有渐变）
- **C-06**（× 马蒂斯；本卡 §8.2-3，同侧旁证组）：饱和度（每块 ≥70% vs 全帧 ≤35%）
- **C-10**（× 塞尚；本卡 §4 P3 + §8.2-4）：深度衰减（大气包络 vs 反大气透视）
- **C-14**（× Lane B 06/07/13 卡反约束；本卡 §8.2-4）：渐变（禁令 vs 雾色渐变）
- **near-miss（conflicts.md §4 表）**：#4（饱和度上限组 → 取 ≤0.35）

## 来源

- 档案（唯一正本）：`research/artists/monet.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`research/agent-art/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`research/prompts/artist_modules/README.md`
