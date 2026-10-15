# 吴冠中 模块卡 — `wu_guanzhong`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/wu_guanzhong.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **银灰统调（silvery-grey）**：黑/白/灰为主调、低饱和区 ≥85%——亮部与暗部都向灰收敛（「江南春阴」）
2. **白墙黑瓦的几何化＋点线面构成**：黑块白块对照交错、建筑边缘多为水平/垂直直线段；以点、线、面为造型主语
3. **线的自主与书写**：藤蔓/荷梗/石纹线独立行走（悬空/穿越/成族）、线宽随提按变化——「粗线昂扬、瘦线穿流」
4. **灰调中的彩点＋形式提炼**：彩点＝窗/人/衣/花、面积极小（「色彩的浓缩点」）；招牌/装饰/门窗细节被省略为块与点
5. **半抽象（风筝不断线）＋纸白与白墙同构＋搬家写生**：母题锚点保留 1–3 个；白域 30–60% 多为结构性白；不同地点景物重组进同一构图

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
Semi-abstract modern Chinese ink-and-colour painting in a silvery-grey register: whitewashed
walls and black-tiled roofs reduced to flat black-and-white planes that interlock, contrast and
cascade; the whole picture built from dots, lines and planes — a handful of concentrated colour
dots (windows, figures, laundry, blossoms, lamps) set like inlaid gems into the grey; a Jiangnan
spring-mist mood, the palette held to black, white, warm grey and pale ochre with tiny
high-saturation accents; brush-drawn lines with varying pressure — vines winding over walls,
gnarled branches, lotus stalks, rock fissures, waterway contours — lines that leave the shapes
and travel on their own; large calm areas of paper-white that read as walls, water or sky;
composition assembled from recombined viewpoints (elements moved from different places), the
architecture simplified to geometry, rooftops seen slightly from above; one to three recognisable
anchors kept legible (swallows, a bridge, a house, garden rocks, a tree); matte ink and light
colour washes on xuan paper, dry-brush and bristle traces visible, no varnish, no gloss; a
painterly oil counterpart is allowed — thin matte oil with the same grey-and-dot logic; quiet,
lyrical, exact, monumental when scaled up
```

**负向约束（`--no` 风格）**

```
--no photorealistic detail, readable signboards, windows and roof-tiles drawn in full, large
high-saturation colour blocks, complementary-colour clashes organised as colour music, pure
geometric abstraction with zero subject, Mondrian grids, Pollock drips, heavy impasto, glossy
varnish, 3D rendering, drop shadows, text, watermark, fake signatures, decorative frames,
tenebrist gloom, a single animal or flower as the sole subject floating in a vast empty void,
hemp-fiber texture strokes with layered ink accumulation, hard-edged neon city, anime, chibi,
photographic realism
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **银灰统调** | 低饱和像素（S ≤0.30）占比 ≥80%；全帧平均饱和度 ≤0.28；色相簇 ≤6 | 逐帧 HSV 直方图 + 色相聚类 |
| 2 | **彩点预算** | 高饱和（S ≥0.60）像素面积 1–8%；连通彩点数 5–40；单点面积 ≤2%；彩点邻域对比（ΔL）≥0.25 | 连通域统计 + 局部对比度 |
| 3 | **几何块面** | 建筑/墙体区水平或垂直边缘占比 ≥50%；近黑（L ≤0.15）与近白（L ≥0.85）块面各 ≥4 块且互相咬合 | 边缘角度直方图 + 灰阶块面分割 |
| 4 | **线自主性** | 线宽 p90/p10 ≥2（提按）；≥1 条线穿越 ≥1/2 画幅，或 ≥8 条同向线成族；线端不收死 | 骨架提取 + 宽度统计 |
| 5 | **点线面覆盖** | 线网覆盖 15–45%；点（墨点+彩点）覆盖 5–25%；三要素同帧共存（各 >5%） | 逐帧分块覆盖统计 |
| 6 | **白域结构** | 白/近白（L ≥0.85）面积 30–60%；其中 ≥60% 与墨线或黑块咬合（有明确边界）——非悬置留白 | 白域分割 + 边界接触检测 |
| 7 | **母题锚点预算** | 可辨锚点（燕/桥/屋/石/树类）1–3 个；锚点总面积占比 0.5–15%（可辨但非写实主体） | 形状检测 + 面积占比 |
| 8 | **运动预算（动画附加）** | 全片无叙事位移；点/线漂移 ≤2%/s；帧间差 ≤1.5% | 帧差图 + 调制曲线拟合 |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 `templates/style_card.md` 的填写规则对齐。署名合规：输出不得含文字/伪签名（见 §8.1 版权护栏）。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **银灰统调强度**（Silver-Grey Unifying Tone）`[归纳]` | 彩色区域较大、灰调不统（早期油画/速写） | 银灰为主，彩色成组点缀（江南系列典型） | 近全灰调，彩色点 <2% 面积、靠对比发光（双燕/忆江南档） | **80%**（本模块身份） |
| P2 | **几何简化度**（Geometric Simplification）`[归纳]` | 建筑细节可辨（门窗/瓦当；扎什伦布寺档） | 块面化，细节选择性省略 | 纯黑白块面 + 点线（近乎抽象；中国城/忆江南档） | **75%** |
| P3 | **点线面构成度**（Dot-Line-Plane Density）`[归纳]` | 线描为主、面留白（速写档） | 线面并置、点少量 | 点线面满构（狮子林/都市之夜/汉柏档） | **70%** |
| P4 | **线的自主性**（Line Autonomy）`[归纳]` | 线=轮廓（贴边勾形） | 线半独立（部分穿越、延伸出形） | 线为主体：藤蔓/荷梗/石纹成族、粗线昂扬瘦线穿流（甦醒/残荷档） | **75%** |
| P5 | **母题锚点残留**（Motif Anchor / Kite String）`[归纳]` | 锚点全沉（近乎纯抽象；朱颜未改档） | 锚点隐约（1–2 个可辨物） | 风景/建筑明确可辨（扎什伦布寺/宁波水乡档） | **60%**（中–强；风筝不断线） |
| P6 | **彩点预算**（Colour-Dot Budget）`[归纳]` | ≤5 处彩点 | 5–20 处、成组分布（水巷档） | >20 处或成片组（夜之眼档：都市之夜） | **50%** |

> 用法：**P1+P2 定「是不是吴冠中」**（银灰统调 + 几何简化；两条同时 ≥中档才成立）；P3/P4 定「线面构成纯度」；P5 是**风筝线**（越低越抽象、但不得为零——纯抽象属康定斯基/朱颜未改特例）；P6 切「江南静档/都市夜档」。
> 数据来源：档位阈值为 `[归纳]`（本项目操作化建议，未经渲染实验校准）；特征观察取自 [R3][R4][R11][R12]。
> **分工注（与 §3.1 对齐）**：P1 强档（银灰）+ P6 中低档（彩点浓缩）是本模块专属；**「高纯色声部 + 互补对撞 + 零对象」整体属于康定斯基模块，禁止在本模块同档出现**——需要抽象感时不得同时取消银灰统调与母题锚点（P5=0 且 P1 弱 → 越界警报）。**「白眼符号 / 单主体 ≤30 笔 / ≥60% 精神场留白」属八大山人模块**；**「披麻皴 + 点苔 + 积墨」属黄公望模块**——均不得在本模块出现。本注为 `[归纳]`。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 康定斯基）**（× 康定斯基；本卡 §3.1 分工条款）：抽象线中文落点：自然母题提炼＋水墨（风筝不断线）vs 零对象＋理论推导——冲突轴＝母题残留度与色彩角色，同屏显式分区
- **分工（vs 八大山人）**（× 八大山人；本卡 §3.1 分工条款）：水墨线谱系：减（单主体 ≤30 笔、留白 ≥60% 精神场）vs 收束（点线面网络、白域 30–60% 结构性）——两卡禁项互列
- **分工（vs 黄公望）**（× 黄公望；本卡 §3.1 分工条款）：积（披麻皴＋点苔积墨）→ 减（八大）→ 抽象收束（吴）三档互斥——不得同屏出现越界元素
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-17 负空间 / 线条 / 色域；与马蒂斯组合需显式分轴（色彩轴归马、线轴归吴）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/wu_guanzhong.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
