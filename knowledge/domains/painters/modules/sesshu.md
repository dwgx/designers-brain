# 雪舟 模块卡 — `sesshu`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/sesshu.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **刚健的斧劈轮廓＋构造性岩组**：岩缘直线段 ≥60%、单段 ≤8% 画高；岩组可分层 ≥3、接缝明确——「構築的で堅固」的脚手架式山体
2. **墨阶分明＋破墨融合**：墨分浓淡 4–5 级（湿渲染云、淡墨远山、浓墨近岩）；局部墨面溢出轮廓与空气交融，骨架线始终可读
3. **留白作云水＋移动视点**：留白率 30–60%、横向云带贯通 ≥50% 画宽；长卷／实景图视点区 ≥2、无法用单一灭点还原（写生再構成）
4. **一点集中的主客关系＋点景极小**：主焦点 1 处（达磨／家屋／舟旗），余者墨色尺寸从属；点景 ≤5% 画高、细节线 ≤12 条／实例
5. **淡彩克制＋款记长题**：彩色区饱和度 ≤30%、色相 ≤2 族（「寒々しい色の淡彩」）；款「四明天童第一座」＋自赞长题——书法即画面构件

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Sesshū-style suibokuga ink landscape — Muromachi Zen ink painting on paper:
monochrome sumi ink in four to five distinct tones — pale wash for mist and far mountains,
deep black for near rocks; assertive ax-cut rock contours, short angular straight strokes that
chop the cliff edge; rocks built as stacked, jointed block masses that read as a solid scaffold;
one or two haboku splashes where ink flies off the brush and cliff, tree and air dissolve together,
while the ink skeleton stays legible; large reserved-paper areas for sky and water, horizontal mist
bands; a single dominant focus — a tiny pavilion, a bridge, a boat with one figure, a flagpole —
set small in a vast landscape; progressive, shifting viewpoints — several vantage points
recombined in one scene, no emphasized single-point vanishing lines; a few pines with radial
needle clusters and dot-leafed trees; a breath of pale ochre and indigo wash over the ink;
inscription column and seal marks at the edge
```
**负向约束（`--no` 风格）**
```
--no hatching or crosshatch shading, no uniform-width woodblock keylines, no flat colour blocks,
no Prussian blue dominant palette, no ukiyo-e wave spirals, no gold leaf, no decorative pattern fields,
no chiaroscuro, no single candle or spotlight source, no western oil impasto, no photographic realism,
no 3D render, no single-point perspective with vanishing lines, no crowded detailed faces,
no saturated floral colour, no single-subject minimalist composition on empty ground,
no wild cursive splashed-flower explosion, no watermark, no lettering overlays
```

## 代码艺术规则（§8.2 原样）

1. **斧劈轮廓规则**：山岩边缘由短直线段组构成——直线段占比 ≥60%、单段长 ≤8% 画高、转角锐化（≤120°）；长弧勾山 ≤1 处（弧长 ≥20% 画宽 的连续弧）。自查：线段检测 + 方向/长度统计。（依据：[R5][R7]）
2. **构造岩组规则**：岩组可分层 ≥3、层界可检出（相邻层纹理方向差 ≥20°）；重复岩形模板 ≥2 处（顶双凹型）；层内纹理方向方差 ≤25°。自查：纹理方向直方图 + 模板匹配。（依据：[R5][R14]）
3. **破墨/泼墨规则**：≥1 处墨面区——无硬轮廓（边缘明度梯度 ≤2/255 每像素段）、区内可辨 ≥1 条浓墨结构线（骨架保留）；洒点群方向与笔势一致（方差 ≤30°）。自查：边缘梯度 + 结构线检测。（依据：[R2][R3]）
4. **墨阶规则**：全帧墨色明度分层 4–5 带；淡墨（相对纸色降幅 ≤40%）面积 ≥35%；浓墨（降幅 ≥70%）≤25%；无一次成型的灰平涂块（内部标准差 >5%）。自查：明度直方图 + 区域统计。（依据：[R3][R2]）
5. **留白/云气规则**：留白（纸色 ±5%）面积 30–60%；≥1 条横向云带贯通 ≥50% 画宽；水面留白与云带可区分（水面波纹线覆盖 ≤3%）。自查：纸色掩膜 + 横带检测。（依据：[R4][R17]）
6. **散点视点规则**（长卷/实景帧）：无被强调的单点透视消失线（直线汇聚点 ≤1 组且不位于画面中心轴 ±10%）；视点区 ≥2（前后景尺度比异常点 ≥1 处——实景再構成标志）。自查：透视线检测 + 尺度比统计。（依据：[R4][R17]）
7. **点景规则**：点景实例（舟/屋/人/桥）高 ≤5% 画高、细节线 ≤12 条/实例；主焦点 1 个（位于画面三分区）；点景不承担明暗（无投影）。自查：实例分割 + 线条计数。（依据：[R2][R15]）
8. **静场规则（动画时）**：帧间光流 Δ ≤1.5%/帧；仅允许云雾 ≤0.5%/秒 漂移与水面 ≤2px 波动；墨迹不得闪变（帧间差 ≤1%）；无镜头推拉与运动模糊核。自查：光流场 + 模糊核检测。（与 C-09 对齐：雪舟站「静」侧；依据：水墨为静态媒介 + §3.1 判据④）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–3/5/6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（低档） | 中（中档） | 强（高档） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **破墨/泼墨强度**（墨面融合度）`[归纳]` | 轮廓完整、墨面 ≤10%（工整期/倣古挂轴） | 局部破墨 20–40%（崖・树・水际） | 大面积泼墨 ≥50%、形体与空气交融（《破墨山水図》档） | **40%** |
| P2 | **斧劈刚健度**（轮廓）`[归纳]` | 圆笔勾山（学习作・拙宗期） | 直线段 40–60% | 斧劈直线段 ≥60% + 锐角断笔（《秋冬》《天橋立》档） | **强** |
| P3 | **构造性（岩组层叠）**`[归纳]` | 单层坡石、结构松弛 | 2–3 层岩组、接缝清晰 | 多层叠压 + 悬崖 + 岩窟（《慧可断臂図》档） | **强** |
| P4 | **留白/云气率**`[归纳]` | 15–25%（浓密构图） | 30–45%（云带、水面） | ≥50%（《破墨山水図》档：大空场） | **中（35%）** |
| P5 | **点景密度**`[归纳]` | 0–2 组（纯景档） | 3–8 组（舟・桥・屋） | ≥10 组 + 建筑细描（《天橋立図》档） | **中** |
| P6 | **墨阶跨度 + 淡彩**`[归纳]` | 2–3 级、无彩 | 4 级、淡彩薄罩 | 5 级 + 湿渲染 + 淡彩（破墨・慧可档） | **中强（4 级）** |

> **用法**：P2/P3 定「是不是雪舟」（两条中 ≥1 条 ≥ 中档 + 另一条 ≥ 弱-中 才成立）；P1 定「破墨档位」（工整 → 局部破墨 → 大泼墨）；P4/P5 定构图密度（留白与点景反向搭配：大留白 ↔ 低点景）；P6 定墨彩档（单色 → 淡彩）。**越界警报（与 §3.1 对齐，组合实验按此判分）**：① 圆润披麻/长弧勾山 → 越界黄公望；② 单主体悬置 + 留白 ≥60% + 一笔造型 → 越界八大；③ 狂草爆发 + 花卉大写意 → 越界徐渭；④ 等宽线 + 平涂 + 蓝 ≥40% → 越界北斋；⑤ 排线塑形/实心黑 → 越界丢勒；⑥ 画内单点光源 + 暗部塌陷 → 越界卡拉瓦乔/伦勃朗。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 八大山人 / 徐渭）**（× 八大山人 / 徐渭（future）；本卡 §3.1 分工条款）：水墨谱系三档写死：刚健／实景（构造山水）vs 减笔／冷峻（单主体 ≤40 笔）vs 爆发（大写意）——判据四条；空间轴归雪舟、减笔经济轴归八大、爆发轴归徐渭（N3）
- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款）：水墨 vs 版画：提按／墨阶 4–5 级 vs 等宽刻线＋平涂——判据四条；表面系统二选一（N4），蓝轴按 C-12
- **分工（vs 齐白石 / 黄公望 / 伊藤若冲）**（× 齐白石 / 黄公望 / 伊藤若冲；本卡 §3.1 分工条款）：毛笔水墨家族第二层分档：色彩轴归齐、皴法／空间轴各自单主、若冲只取水墨轨（色彩轨整条移除）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-07 表面系统／C-12 蓝轴／C-16 反约束适用域／C-17 负空间

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/sesshu.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
