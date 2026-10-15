# 委拉斯开兹 模块卡 — `velazquez`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/velazquez.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **银灰底光**：低饱和银灰面积 ≥50%；无纯白/纯黑（两端各 ≤5% 像素）——全画面以灰调为骨架
2. **可见的空气**：人物轮廓不闭合、边缘被环境色「化开」；人物之间/远近之间的「空」有可读色斑；远景对比 ≤ 前景 60%
3. **碎笔触成像（borrones）＋无勾线无硬边**：近看散落笔痕/色斑（2–12 px 级）、远看自动合成形；不存在「勾线＋填色」边界
4. **亮部薄而透＋完成度分级**：高光区颜料薄（透出底子与笔势，与伦勃朗亮部厚涂相反）；面部精细、次要对象只给色斑量级——近看崩解、远看成立
5. **空间开口（门/窗/镜/画中画）＋视线轴＋背身/镜像**：构图含 ≥1 个第二空间（多层开口而非单室网格）；主人物视线出画（观者位置被构图预设）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
Velázquez-module court painting — the third tier of light: studio and air. Silvery ambient
studio light from several openings (window, door), no single spotlight, shadows transparent
and thin, highlights painted thin and luminous (a scrape of pale paint over the ground);
mid-grey tonality across the whole frame — no pure white, no pure black; visible air between
the figures — contours left open, edges dissolving into ambient grey, figures and far
background sharing one continuous air envelope (aerial perspective made by touch, not
gradient); loose alla prima brushwork — scattered dabs and strokes that only assemble into
form from a distance, near view falls apart, far view is a miracle; economy of means — faces
rendered with few decisive touches, hands, props, animals and drapery left as shorthand
smears; space built from openings rather than a grid — a door, a mirror, a
picture-within-the-picture, a viewer's position implied just outside the frame; figures look
out toward the viewer or into a mirror; Spanish court restraint — black and silver dress,
few props, dignity carried by posture and empty space; oil on canvas, museum quality,
17th-century Spanish court
```

**负向约束（`--no` 风格）**

```
--no single hard spotlight, pitch-black background, extreme chiaroscuro, heavy impasto in
lights, glowing halo, rim light, theatrical stage lighting, pointillés dots, hard contour
lines, closed outlines, smooth airbrushed gradients, sfumato fog, uniform finish everywhere,
glossy varnish, high saturation, neon colours, crowded symmetrical composition, motion blur,
text, watermark, signature, modern objects, 3D render, photographic realism
```

## 代码艺术规则（§8.2 原样）

1. **空气规则（轮廓开口）**：人物/对象轮廓边缘链**断口率 ≥20%**（不允许完整闭合轮廓）；轮廓过渡带 ≥4 px 且非均匀（存在断口与化开段）。自查：Canny 边缘图 + 轮廓闭合分析。
2. **银灰调**：全帧饱和度中位数 ≤0.35；纯白（V ≥0.95 且 S <0.05）与纯黑（V ≤0.05）像素各 ≤2%；灰调（S <0.25）面积 ≥45%。自查：HSV 直方图分位。
3. **多光源**：全帧亮斑连通域（V ≥0.85×max，面积 ≥0.1%）数量 ≥4，且质心分布于 ≥3 个不同高度带；最大亮斑面积 ≤3% 画面。自查：连通域 + 质心聚类。
4. **碎笔触成像**：笔触/色斑特征尺度集中于 **2–12 px**（1024 px 宽基准）；高频能量 ≤ 中频能量的 60%（不追求细节锐度）。自查：带通能量比。
5. **亮部薄涂（反伦勃朗）**：高光区（V 前 10%）的局部纹理能量 ≤ 中间调区的 80%。自查：分区 Laplacian 方差。
6. **空间开口**：≥1 个「第二空间」元素（门/窗/镜/画中画），该区域与主空间的明度差 ≥8/255 或色温差 ≥150K；远景对比 ≤ 前景 60%。自查：区域分割 + 对比测量。
7. **视线轴**：≥1 条「看向观者或镜面」的主视线（视线方向与画框法线夹角 ≤45°）；主人物面部朝向可判读。自查：面部朝向估计 + 视线向量。
8. **完成度分级**：面部区细节密度 ≥ 其余区域 3×；次要对象（手/道具/动物/织物）细节密度 ≤ 面部的 40%。自查：分区域高频能量比。

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），**未对原作做像素测量**（分母＝假想参考帧）；第 1–4 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

> 节级声明：以下档位划分与阈值为本项目 `[归纳]`（操作化），不冒充艺术家内心；描述中的引文来自馆方/档案原文（已在 §1–§3 标注）。

| # | 参数 | 弱 | 中 | 强 | 默认建议 |
|---|---|---|---|---|---|
| P1 | **直接画法（Alla Prima）** `[归纳]` | 多层罩染、表面平滑（早期塞维利亚精细风） | 湿画混接、局部厚涂 | 一次性落笔、笔痕可见、**近看崩解**、无回改 | **65%** |
| P2 | **空气密度（Ambiente）** `[归纳]` | 空气透明、背景实、轮廓闭合 | 轮廓轻微化开、远景降对比 | 「**人物之间都是空气**」：边缘化开、远近皆银灰包络、远对比 ≤60% | **65%** |
| P3 | **空间层数（Spatial Layering）** `[归纳]` | 单层（平面背景肖像） | 两层（门/窗后景） | 多层嵌套（镜/画中画/观者位；《宫娥》级） | **55%** |
| P4 | **笔触经济（Economy of Means）** `[归纳]` | 全画均匀完成 | 重点精、次要简 | 极限省略（次要物 1–2 笔；大面积 borrones） | **60%** |
| P5 | **银灰调（Silvery Tonality）** `[归纳]` | 暖土色系、红棕底（早期） | 灰底 + 局部饱和点缀（红/蓝 ≤10% 面积） | 冷银灰全域（饱和色 ≤5% 面积；两端无纯黑纯白） | **60%** |
| P6 | **光的多源柔性（Studio Light）** `[归纳]` | 单一侧光、深暗背景（tenebrist 早期） | 双光源（窗 + 门）柔化 | 画室多光源、**无单一主光斑**、阴影透明、亮部弥散 | **65%** |

> **用法**：P6 + P2 定「是不是第三档的委」（缺 P6 退化为卡拉瓦乔/伦勃朗系单光；缺 P2 退化为普通写实）；P1 + P4 定「直接画法强度」；P3 只在「空间与观看」题材拉满（宫娥类）；P5 定「银灰还是暖土」。
> **组合口径**（预检写死）：与伦勃朗/维米尔/达·芬奇组合时按 §3.1 判分轴处置（光轴、高光形态轴、空气轴各自单主）；与「Lane B」组合时，注意其模板级反约束「别做成：硬阴影」对本模块**无冲突**（本模块本来就要软边），但「别做成：渐变」会误伤 P2 强档的远景化开——需按 C-14 改写句式（「大气包络允许，但不得出现连续长渐变带」）。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 伦勃朗）**（× 伦勃朗；本卡 §3.1 分工条款）：光的第三档「画室与空气」：多光源弥散＋银灰全域 vs 连续衰减照单脸＋暗部塌陷——判分见条款（a）
- **分工（vs 维米尔）**（× 维米尔；本卡 §3.1 分工条款）：宫廷空间＋自反观看 vs 荷兰光学（单室单侧窗＋点状高光＋无痕表面）——高光形态与空间结构判分（b）
- **分工（vs 达·芬奇）**（× 达·芬奇；本卡 §3.1 分工条款）：空气的两种做法：笔触空气（断笔/色斑拼出）vs sfumato 渐变——「空气」轴单主（N3）（c）
- **旁注（vs 卡拉瓦乔）**（× 卡拉瓦乔；本卡 §3.1 d 旁注）：不复制硬光开关——亮暗边界被银灰化处理、背景由空气填充

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/velazquez.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
