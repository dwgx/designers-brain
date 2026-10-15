# 夏尔丹 模块卡 — `chardin`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/chardin.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **触觉的材质（tactile matter）**：同屏 ≥3 类材质各有专属表面处理（铜暖光／玻璃湿亮／面包颗粒）；反光软而宽、边缘柔融——表面保留颜料质地
2. **放而不混（juxtaposed, not blended）**：笔触一笔一笔并置、不预先调匀——近看「马赛克／针脚」、退后聚合（Diderot 远近检验）
3. **反光网络（reflets）**：≥2 处跨物反光（铜壶映肉红、玻璃含红蓝）——「每个物体都带上周围一切的颜色与光」
4. **柔和明暗＋浅空间中立场**：漫射侧光、暗部暖褐有层次、无纯黑大块；物体贴前缘、桌沿水平线（常略斜）＋简化中性背景
5. **谦卑母题＋悬浮静默＋重复变体**：日常器物与劳作主角化；人物停在「temps mort」动作中停；同构图 2–4 版、版间几乎不可分

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Jean Siméon Chardin-style still life of humble domestic objects, painted for the sense of touch:
a copper cauldron, an earthenware jug, a glass bottle, a loaf of bread, a knife, game and fruit
arranged close to the front edge of a wooden table; dense, stippled brushwork and layered glazes —
paint laid on in small touches, side by side, never smoothed; the surface keeps the rough texture of paint,
forms resolving only at a distance;
soft diffused daylight from the upper left, no dramatic shadows — warm brown and grey-green half-lights,
no pure black, no cold blue dominant; light wraps each object and links them together;
reflections carry the surroundings — a red gleam of meat in the copper, the fruit echoed in the glass,
the silver catching the cloth; every object borrows the colour and light of its neighbours;
restricted warm palette of ochre, umber, muted red and grey-green with silver-white highlights;
a shallow space: the shelf or tabletop edge runs across the lower picture, the background a simple
neutral half-tone field without incident; quiet suspended time — no narrative, no movement,
the humble elevated; 18th-century French still life, oil on canvas, museum quality
```
**负向约束（`--no` 风格）**
```
--no hard chiaroscuro, pure black, cold blue-grey shadow systems, ultramarine-dominant palette,
dramatic spotlight, single raking spotlight, isolated pin-point highlights (pointillés),
mirror-perfect glossy surfaces, levigated flat paint, visible bare canvas, geometric faceting,
multiple broken outlines, tipped tabletop, aerial perspective haze, high saturation, neon colours,
decorative gold leaf, narrative drama, allegorical props, motion blur, speed lines, text, watermark
```

## 代码艺术规则（§8.2 原样）

1. **触感表面规则**：全帧「可辨笔触纹理」面积占比 **30–80%**（介于「不可见」与「全覆盖」之间）；纹理粒径 2–8px（1080p 基准）；**禁止统一方向角度族**（方向直方图峰值占比 ≤35%——与塞尚的 4–8 角度族区分）。自查：高频能量图 + 梯度方向直方图。
2. **反光形态规则**：镜面高光连通域为**宽软形**（圆度 ≤0.7 或长宽比 ≥2；边缘过渡 σ ≥2px）；**禁止 1–3px 圆点系统**（维米尔档）；跨物反光 ≥2 处（对邻物色相做色调偏移检测）。自查：高光连通域形态 + 色相相关矩阵。
3. **明暗规则**：纯黑像素（L*≤5）占比 ≤0.5%；阴影色相**暖**（H 20–60° 或灰绿 60–120°，**禁止 200–250° 冷蓝主导**）；暗部保留层次（暗区内部亮度标准差 ≥2/255）。自查：直方图 + 阴影区色相/方差统计。
4. **空间规则**：单一视点；背景为「大块低细节区」（背景区边缘密度 ≤ 前景的 30%）；主体贴前缘（包围盒 ≥50% 画幅）；**无地砖网格/单点透视网格**（与维米尔区分）。自查：边缘密度分区 + 透视线检测。
5. **色彩规则**：全帧中位饱和 ≤0.45；高饱和（S≥0.6）面积 ≤8% 且集中于食物/织物/反光；色相簇 ≤8；主色为暖土（赭/棕/灰绿）。自查：饱和度直方图 + 色相聚类。
6. **材质对比规则**：同屏可辨材质 ≥2 类、各有**专属表面处理**（金属=宽软反光带；玻璃=透射+反光；面包/食物=颗粒点触；瓷=温润渐变）；禁止两种材质共用同一处理（防「一律点彩」）。自查：材质分区 + 局部表面统计。
7. **静止规则**：全片 0 帧运动模糊；除「反光/蒸汽等微动」（≤0.5% 像素）外帧间差 Δ ≤1%；人物档姿态为「动作中停」（无动作矢量链）。自查：帧差图 + 光流。
8. **完成度规则**：裸露画布/底色区 ≤1%；无骨架线可见；边缘无硬线（过渡带 ≥2px）；表面密实（无大面积单色平滑区——单一 64×64 块内 L* 梯度幅值均值 ≥0.5 且 ≤3）。自查：底色检测 + 边缘宽度中位数。

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1/2/3 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。与 `conflicts.md` 的关系：**C-01**（软光侧，顺风）、**C-05**（「可见但非全覆盖」档须显式取值）、**C-11**（按 N7 声明「反光带」类）、**C-12**（暖土色系显式取值）、**C-13**（暖褐/灰绿阴影）为组合预检重点。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **触感密度**（Tactile Density）`[归纳]` | 表面平滑、材质概括（晚期粉彩式轻处理） | 主要物体笔触可读、近观可见颗粒 | 全画稠密点触与堆叠——近看颜料、远看成物（La Raie/Le Buffet 档） | **70%** |
| P2 | **反光网络密度**（Reflex Network）`[归纳]` | 无跨物反光（各物孤立高光） | 各物自带软高光 + 1–2 处邻物色 | 系统性互映 ≥3 处（铜映肉红、玻璃映红蓝、银映果与布） | **65%** |
| P3 | **材质对比度**（Material Contrast）`[归纳]` | 单一材质主导 | 2–3 类（金属/玻璃/食物） | ≥4 类同屏、各有专属表面（金属钝光、玻璃湿亮、面包颗粒、瓷温润、织物哑光） | **70%** |
| P4 | **光质柔和度**（Light Diffusion）`[归纳]` | 方向性硬光与锐投影（**越界警报：卡拉瓦乔档**） | 单侧软光、暖褐阴影、无锐投影 | 包围漫射、全中调、无投影（晚期静物档） | **60%** |
| P5 | **空间浅度与中性场**（Shallow Space & Neutral Ground）`[归纳]` | 纵深可读、背景有细节（**越界警报：荷兰室内档**） | 桌面深度（前缘—背景两带）、背景简化 | 物体贴前缘、背景为单一中性半调（灰绿/褐） | **65%** |
| P6 | **表面整合度**（Finition / Blend）`[归纳]` | 大笔触并置明显（约 1730s 前中期） | 并置 + 局部揉合 | 反光、透明与 fondu 主导（约 1755 后晚期档） | **50%** |

> **用法**：P1/P2 定「是不是夏尔丹」（触感 + 反光网络，两条 ≥ 中档才成立）；P3/P4 定材质与光档；P5 定构图；P6 是**时期滑轨**（早期并置 ↔ 晚期揉合，工作流参数）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 表面压平、高光点状、冷调蓝阴影、地砖网格 → 越界**维米尔**；② tache 方向族、多轮廓、蓝网、裸露画布 → 越界**塞尚**；③ 画外单光 + 近黑背景 + 亮部只落脸/手 → 越界**卡拉瓦乔**；④ 平涂无笔触、无高光 → 越界**马蒂斯**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 维米尔）**（× 维米尔；本卡 §3.1 分工条款）：光学室内 vs 触觉静物：光功能／高光形态／表面／空间／阴影五判据（≥2 轴联合）；默认二选一
- **分工（vs 塞尚）**（× 塞尚；本卡 §3.1 分工条款）：静物：结构 vs 质感——五判据（≥2 轴）；不得折中成「半几何半触感」（N4 不可拆）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影（软光侧顺风）／C-05 笔触（可见但非全覆盖，显式取值）／C-11 高光计数（宽软反光按 N7 单列声明）／C-12 色相预算／C-13 阴影色相（暖褐／灰绿）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/chardin.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
