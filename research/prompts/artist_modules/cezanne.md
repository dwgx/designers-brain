# 塞尚 模块卡 — `cezanne`

> A-19 模块库 ｜ 来源：档案 `research/artists/cezanne.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `research/agent-art/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **离散笔触（tache）铺满全画面**：按局部结构成组（4–8 个方向族）
2. **色阶代替明暗**：红↔绿色阶塑形、无黑阴影；暖冷交错编织
3. **轮廓破碎与多重线**：一物常 2–3 条轮廓，形体互渗；蓝网贯穿（阴影／轮廓／天空）
4. **反大气透视＋空间压缩**：远近同尺度、视点游移、透视不自洽
5. **几何化块面＋未完成感**：裸露画布／骨架线，作品停在「进行中」

## 图像 prompt（§8.1 原样）

**正向段（可粘贴）**：
```
Late Cézanne landscape with a still-life foreground, in the manner of the
Bathers period (1895–1906): the entire surface built from short, visible
parallel brushstrokes (taches) of 0.5–1.5 cm equivalent, arranged in groups of
4–8 directional families that both model volume and unify the picture plane;
forms constructed only by color modulation — light, half-tone and quarter-tone
steps of ochre, orange, olive, viridian, cobalt and ultramarine — never by
black shading; objects carry broken, multiple outlines, 30% of contour segments
left open so forms merge into the background; a network of blue in shadows,
contours and sky (12–15% of pixels); sky and earth painted with equal
substance, no atmospheric recession, distant forms the same scale as near
ones; slightly tipped tabletop and shifting viewpoints within one frame;
5–8% of the canvas left thinly covered or bare, suggesting unfinish; dry,
matte oil surface, fine canvas weave visible.
```
**负向约束（--no 风格）**：
```
--no chiaroscuro, black cast shadows, single-point perspective, atmospheric
haze, photorealistic detail, smooth blended gradients, glossy varnish,
palette-knife impasto (that is the 1860s style), narrative action, dramatic
poses, facial expression detail, high-contrast lighting, neon colors
```

## §8.1b 纯风格段（场景可迁移）

> 派生自 §8.1 正向段（E-02 · E1_t1b，2026-10-15）：删除题材词（人物/肖像/室内/静物）与场景专属道具，仅保留视觉语言（光/色/笔触/结构/构图规则）；用法：主题句 + 本段（同 §8.1 配方）。负向段沿用 §8.1 原文（本通道不发送）。
> 删除项：still-life foreground、Bathers period、tipped tabletop；最小改写：objects carry→forms carry、Bathers period→late period。明细见 `research/experiments/E1_t1b/RESULTS_t1b.md` §2。

**正向段（可直接粘贴）**：
```
Late Cézanne landscape in the manner of his late period (1895–1906): the
entire surface built from short, visible parallel brushstrokes (taches) of
0.5–1.5 cm equivalent, arranged in groups of 4–8 directional families that
both model volume and unify the picture plane; forms constructed only by color
modulation — light, half-tone and quarter-tone steps of ochre, orange, olive,
viridian, cobalt and ultramarine — never by black shading; forms carry broken,
multiple outlines, 30% of contour segments left open so forms merge into the
background; a network of blue in shadows, contours and sky (12–15% of pixels);
sky and earth painted with equal substance, no atmospheric recession, distant
forms the same scale as near ones; shifting viewpoints within one frame; 5–8%
of the canvas left thinly covered or bare, suggesting unfinish; dry, matte oil
surface, fine canvas weave visible.
```

## 代码艺术规则（§8.2 原样）

> 把塞尚视觉语言翻译成可逐帧自查的量化规则（对应 `templates/style_card.md` 画风段写法）：

1. **笔触**：笔触长轴 8–24 px（1080p 基准），全帧笔触方向收敛为 4–8 个角度族，同族内偏差 ≤25°；笔触覆盖率 ≥80%（边缘检测密度判定）。
2. **色阶建模**：全帧近黑像素（L* ≤10）占比 ≤0.5%；单一物体内部色相数 ≥3、明度级（L* 分桶）≥5；无单方向光源渐变（任一 64×64 块内 L* 梯度幅值均值 ≤2）。
3. **轮廓**：物体轮廓线宽 2–4 px；≥30% 轮廓段存在断口或第二重线（双线错位 ≥3 px）。
4. **蓝调**：阴影与轮廓区域中蓝色像素（H 200–250°）占比 ≥15%；天空与地面区域的平均饱和度差 ≤15%。
5. **空间**：无单点透视——画面中任意两条近水平结构线（桌沿/地平线）夹角 ≥2°；远景物体高度 ÷ 近景同类物体高度 ≥0.5（空间压缩）。
6. **未完成**：画面 ≥5% 面积保留底色或稀薄覆盖（与完成区平均色差 ΔE ≥15）。
7. **明度直方图**：全帧 L* 直方图无单一桶占比 >20%（防止大面积均匀天空块）；暖冷像素占比均在 30–70% 之间（暖冷交错编织）。
8. **构图骨架**：主要体块重心连成的多边形近似三角形（重心三角形面积 ÷ 画面面积 ≥0.25），对应金字塔构图。

## 控制参数（§4 原样）

| # | 参数 | 弱 | 中 | 强 | 默认建议 |
|---|---|---|---|---|---|
| P1 | **笔触可见度**（tache 尺寸与方向一致性）`[归纳]` | 笔触 1.5–3 cm 等值、边缘柔和、方向较随机 | 0.8–1.5 cm、按局部结构分组 | ≤0.8 cm、密集平行、4–8 角度族清晰 | **中强（对应 1880 后成熟期）** |
| P2 | **轮廓破碎度**`[归纳]` | 连续单线轮廓 | 1–2 处断口或第二重线 | ≥30% 轮廓段断裂/双线错位，形体互渗 | **中档** |
| P3 | **色阶建模度**（明暗 vs 色阶）`[归纳]` | 保留古典明暗、黑影塑形 | 明暗+色阶混合，阴影含蓝 | 纯色阶建模，全画无黑阴影（L*≤10 像素 ≤0.5%） | **强档**（仍像塞尚的关键） |
| P4 | **空间压缩度**`[归纳]` | 单点透视，纵深自然 | 局部畸变（桌沿错位、地平线抬高） | 多点透视 + 远近同尺度 + 反大气透视 | **中强** |
| P5 | **蓝色密度**（阴影/轮廓/天空蓝像素占比）`[归纳]` | <8% | 8–15% | ≥15%，蓝网贯穿人物与风景 | **中档（12% 左右）** |
| P6 | **未完成感**（裸露底色面积）`[归纳]` | 0–2%，完整收尾 | 2–8%，局部留白 | ≥8%，大面积裸露或骨架线可见 | **中档（5–8%）** |

## 冲突注记（→ conflicts.md）

组合前先读 `research/agent-art/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-04**（× 卡拉瓦乔；本卡 §8.2-7）：直方图单桶上限（无 >20% vs 暗带 ≥40%＋背景均匀）
- **C-05**（× 达·芬奇；本卡 §8.2-1）：笔触可见度（≥80% 覆盖 vs 只有渐变）
- **C-10**（× 莫奈；本卡 §4 P4 + §8.2-5）：深度衰减（反大气透视 vs 大气包络）
- **C-13**（× 卡拉瓦乔；本卡 §8.2-4）：阴影色相（蓝 ≥15% vs 深棕黑暗部）

## 来源

- 档案（唯一正本）：`research/artists/cezanne.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`research/agent-art/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`research/prompts/artist_modules/README.md`
