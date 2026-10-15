# 维米尔 模块卡 — `vermeer`

> A-19 模块库 ｜ 来源：档案 `research/artists/vermeer.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `research/agent-art/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **单一左侧窗光、高调**：大面积浅灰白墙面接光
2. **点状高光（pointillés）**：1–3mm 圆点厚涂亮点；暗部平坦（大块无变化色面）
3. **冷调阴影**：蓝／绿而非黑；群青蓝 × 赭黄主色对，红只作小点缀
4. **无硬线（sfumato）、细节主动省略**；材质靠高光形状区分；表面平滑（织纹不可见）
5. **人物 1–2 人、动作冻结**；房间几何网格（地砖＋窗框单点透视）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
quiet Dutch Golden Age interior genre scene, single figure (one or two people) absorbed in a
silent everyday action, soft natural daylight entering from a single window on the LEFT,
large pale plaster wall catching the light, high-key tonality, deep shadows rendered as flat
unmodulated areas of cool blue-grey paint (no detail inside shadows), dominant colour pair of
natural ultramarine blue and ochre yellow with tiny red accents, specular highlights painted as
small round globular dots (pointillés) on porcelain, pewter, brass, pearls and bread crust,
soft edges with no hard contour lines (sfumato, details deliberately omitted), matte and glossy
surfaces distinguished only by the shape of their highlights, single-point perspective grid of
tiled floor (29.3 cm tiles) and leaded window frames, thin translucent glazes over a light grey
ground, smooth levigated paint surface with the canvas weave barely visible, dark neutral or
deep green backdrop pushing the figure forward, timeless stillness, 17th-century Delft domestic
world, oil on canvas, museum-quality
```

**负向约束（`--no` 风格）**

```
--no harsh chiaroscuro, hard black shadows, pure black, rim light, multiple light sources,
warm tungsten light, high dynamic range, glossy varnish reflections, visible impasto in flesh,
thick outlines, cel shading, saturated primary palette, neon colours, crowded composition,
motion blur, speed lines, text, watermark, signature, modern objects, fantasy elements
```

## §8.1b 纯风格段（场景可迁移）

> 派生自 §8.1 正向段（E-02 · E1_t1b，2026-10-15）：删除题材词（人物/肖像/室内/静物）与场景专属道具，仅保留视觉语言（光/色/笔触/结构/构图规则）；用法：主题句 + 本段（同 §8.1 配方）。负向段沿用 §8.1 原文（本通道不发送）。
> 删除项：interior genre scene、single figure、window、plaster wall、object list（porcelain…bread crust）、tiled floor/window frames、Delft world；最小改写：single window→single source、plaster wall→pale areas、pushing the figure forward 删除。明细见 `research/experiments/E1_t1b/RESULTS_t1b.md` §2。

**正向段（可直接粘贴）**：
```
quiet Dutch Golden Age painting: soft natural daylight from a single source on
the LEFT, large pale areas catching the light, high-key tonality, deep shadows
rendered as flat unmodulated areas of cool blue-grey paint (no detail inside
shadows), dominant colour pair of natural ultramarine blue and ochre yellow
with tiny red accents, specular highlights painted as small round globular
dots (pointillés) on glossy surfaces, soft edges with no hard contour lines
(sfumato, details deliberately omitted), matte and glossy surfaces
distinguished only by the shape of their highlights, single-point perspective
grid, thin translucent glazes over a light grey ground, smooth levigated paint
surface with the canvas weave barely visible, dark neutral or deep green
backdrop, timeless stillness, oil on canvas, museum-quality
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **单一左向平行光 + ≤1 个弱填充光** | 主光方向 = 画面左（±15°）；填充光强度 ≤ 主光 15% | 逐帧统计：所有高光像素的"法线↔主光"夹角 ≤60°；无第二组反向高光 |
| 2 | **平坦暗部** | 暗部（亮度 ≤ 受光面 25%）内部亮度标准差 ≤ 5/255 | 对暗部区域跑局部 std，超阈即"暗部出现了不该有的细节" |
| 3 | **点状高光（pointillés）** | 圆点直径 1–3 px（1024 px 宽画布）；软边 σ = 0.5–1 px；数量按 P3 分档（0–2 / 5–20 / 100+） | 连通域分析：亮点面积分布应集中在单峰、圆度 >0.7；出现"线状高光"即违规 |
| 4 | **色板 ≤8 色相，蓝-黄主色对** | 蓝相 200–230°、黄相 35–50°；阴影色相相对受光面**向蓝偏移 ≥15°** | 逐帧直方图：色相簇 ≤8；取"受光/阴影"同名材质像素比较色相偏移 |
| 5 | **无硬边** | 任意物体边缘过渡带 ≥2 px；禁止 1 px 描边 | Canny 边缘图上统计边缘宽度中位数；检测到闭合 1 px 轮廓即违规 |
| 6 | **单点透视 + 网格几何** | 消失点 1 个，位于画面高度 55–65%；地砖网格为等比方形（29.3 cm 比例） | 反向投影地砖角点，检查同一消失点；网格尺寸方差 ≤2% |
| 7 | **动态范围压缩** | 受光面亮度上限 ≤88%、暗部下限 ≥8%（禁纯白/纯黑） | 逐帧 min/max 与直方图两端 1% 分位检查 |
| 8 | **全画面静止，单一事件在动** | 除事件区域（牛奶流/烛焰/烟）外，帧间差 Δ ≤1% | 帧差图：事件区域外非零像素占比 ≤1% |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；第 3、6 条的量纲换算依赖 Steadman 的地砖尺寸（29.3 cm / 14.6 cm，[R14]）。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **单侧窗光主导度**（Window-Light Dominance）`[归纳]` | 漫射光/双侧光，无明显方向 | 单侧窗光，阴影柔和、投影短 | 单侧强窗光 + 暗背景，投影与遮挡关系明确 | **75%** |
| P2 | **暗部平坦度**（Shadow Flatness）`[归纳]` | 暗部保留细节与渐层（近似暗箱前的荷兰风俗画） | 暗部整体压平，仍见轮廓 | 暗部为纯色平面（如 *Woman in Blue Reading a Letter* 蓝缎裙阴面） | **70%** |
| P3 | **点状高光密度**（Pointillé Density）`[归纳]` | 0–2 个光点（仅眼睛/珍珠级） | 局部 5–20 点（金属、瓷、面包） | 满画面数百点（Rijksmuseum 对 *The Milkmaid* 的描述："hundreds of colourful dots"） | **50%**（人物特写）／**80%**（静物/器物） |
| P4 | **群青蓝权重**（Ultramarine Weight）`[归纳]` | 蓝仅作点缀（≤5% 面积） | 蓝为第二主色，与赭黄成对 | 蓝为主色（*Woman in Blue*、头巾占画面 1/4 以上） | **60%** |
| P5 | **边缘柔化度**（Sfumato / Edge Softness）`[归纳]` | 硬边、轮廓清晰（早期室内，"sharp, sometimes to the point of brittleness"） | 轮廓柔和但形体可读 | 无硬线、细节主动省略（耳环挂钩不画） | **80%**（成熟期） |
| P6 | **表面平滑度**（Surface Levigation）`[归纳]` | 笔触可见/厚涂（早期历史画、晚期 *The Guitar Player* 的 "calligraphic" 笔触） | 局部笔触（点彩、布料褶） | 釉层压平、织纹几乎不可见（"levigated effect"） | **85%**（成熟室内） |

> 用法：P1/P2 定"是不是维米尔"，P3/P5 定"是不是成熟期"，P4/P6 定"蓝调还是黄调、平滑还是笔触化"。三档描述可直接作为判定标准写进自查表。
> 数据来源：三档中的引文与阈值均来自 [R2][R12][R20][R21][R22][R24]；**档位划分本身为 `[归纳]`**（本项目的操作化建议，未做渲染实验）。

## 冲突注记（→ conflicts.md）

组合前先读 `research/agent-art/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-08**（× Lane B「运动模糊」禁令；本卡 §8.2-8）：运动模糊（定格 = 全片 0 帧）
- **C-09**（× 梵高；本卡 §8.2-8）：运动预算（事件外 Δ≤1% vs 全画面场）
- **C-11**（× 卡拉瓦乔；本卡 §4 P3 + §8.2-3）：高光计数（100+ 点 vs [2,5] 连通域）
- **near-miss（conflicts.md §4 表）**：#1/#2/#3/#8（× 卡拉瓦乔）、#5（× 北斋/毕加索）、#7（× 米开朗基罗）

## 来源

- 档案（唯一正本）：`research/artists/vermeer.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`research/agent-art/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`research/prompts/artist_modules/README.md`
