# 萨拉希 模块卡 — `el_salahi`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/el_salahi.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **字母骨架（letter-bone）**：画面结构由阿拉伯字母构件构成/演化（alif 竖笔、圆环、点群）——「break down the bone of the letter」；≥1 处可辨字母构件
2. **面具/头形与双眼**：面具式头部、拉长头形、成对「离体之眼」、头顶新月
3. **索默土色系＋线为主角**：黑/白/焦赭/土黄为主、少渐变、高纯色仅点缀；线＝一切之本（「all images can be reduced to lines」）、笔势带书写速度感、线宽变化大
4. **平涂浅空间＋有机生长构图**：无线性透视、形体与图案互相咬合；从「核」生长、无草图先行；多联分块（九联/三联）各自装裱又组合成整体
5. **黑白粒子-整体＋冥想式重复＋文字残影**：中期约 17 年黑白粒子阶段（「the particle and the whole」）；点/短笔/braille 式重复、小尺度（药盒/信封后经丝网放大）；字母可辨度受控（介于不可读与可读标语之间）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
Mid-century Sudanese calligraphic abstraction (Khartoum School / Hurufiyya register): a painting whose
structure is built from the bones of Arabic letters — alif-like verticals, rounded bowls, clustered
diacritic dots — written first and then broken down, so that animal, human and plant forms emerge out of
the once-abstract letterforms; mask-like heads with stretched faces and paired disembodied eyes, crescents
set on top of heads, arabesques where limbs should meet; a limited sombre palette of black, white, burnt
sienna and yellow ochre, at most one small accent of blue or red; flat shallow space, no linear
perspective, no vanishing point; abstract form, pattern and figure blur into each other through
over-painting; matte oil and enamel paint on hand-woven damouriya cotton with visible stitched strips, or
pen-and-ink on paper and card; deliberate drips, wrinkled paint surface, dry-brush and ballpoint traces;
an organically grown composition spreading from a single nucleus with no pre-sketch, sometimes cut into
separately framed panels that read as one; monumental square canvas or small vertical medicine-packet
cards; quiet, meditative, written rhythm; no signature, no gloss
```

**负向约束（`--no` 风格）**

```
--no photorealistic rendering, single-point perspective, vanishing point, three-dimensional illusion,
academic portraiture, glossy impasto, neon or candy colors, high-purity complementary color clashes,
color-as-sound abstraction, hard-edge geometric grid, all-over drip painting, illuminated manuscript
page, gold leaf, carpet-like tiling, decorative micro-calligraphy, fully legible slogans or long
readable text, poster typography, narrative crowd scenes with architectural cutaways, 3D render, drop
shadows, text captions, watermark, signature, frame, borders
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **字母骨架在场** | ≥1 类可辨字母构件（alif 竖笔 / 圆环 / 点群）；笔画线宽 p90/p10 ≥ 2.5；连写段落 ≥1/3 画幅长 | 形态检测（竖笔段/闭环/点簇）+ 笔画宽度统计 |
| 2 | **索默色域** | 色相簇 ≤6；平均饱和度 ≤45%；高纯色（S≥70%）面积 ≤10% | 逐帧直方图 + 色相聚类 |
| 3 | **有机生长/分块** | 分块数 1–12；块间主笔势方向相关系数 ≥0.5（同源）或单幅呈「核→外」尺度梯度（近核笔画密度 ≥ 边缘 1.5 倍） | 分块检测 + 主方向相关 + 密度梯度图 |
| 4 | **面具/胚胎形象预算** | 头形/面具锚点 0–5 个；单锚点面积 ≤8%；双眼成对出现（≥1 对） | 形状检测 + 成对性检查 |
| 5 | **黑白粒子-整体** | 双色像素占比 ≥85%（黑白档）；粒子尺度方差大（p90/p10 ≥ 4）；缩略图（1/16）下读为单一整体形（连通域 ≤3） | 二值化统计 + 多尺度连通域 |
| 6 | **书写运动预算** | 全片无叙事位移；若为动画，笔迹生长速度调制 ≤2%/s；帧间差 ≤1.5% | 帧差图 + 生长曲线拟合 |
| 7 | **基底显影** | 折痕/braille/窗膜/拼接缝可见但 ≤15% 面积；≥1 条主笔沿痕迹走向（相关系数 ≥0.4） | 线检测 + 痕迹掩膜相关 |
| 8 | **越界检查（组合护栏）** | 金箔 0；细密画书页框 0；高纯度互补对撞对 0；可读标语/整行文本 0；纯几何硬边网格 0 | 按 §3.1 判据逐项清单核对 + OCR 扫描（仅计「可读句」） |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 `templates/style_card.md` 的填写规则对齐。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **书法骨架强度**（Calligraphic Armature）`[归纳]` | 线脱离字母：纯手势/装饰曲线，无字根 | 字母骨架局部可辨（1–2 类构件，如 alif 竖笔群） | 字根清晰成段落：连写笔势 + 点群 + 圆环并存，拆解层次可读（*They Always Appear* 档） | **75%**（本模块身份；vs 康定斯基判据①） |
| P2 | **索默色域度**（Sombre Earth Palette）`[归纳]` | 多色高彩（>6 色相簇；**越界：滑向色彩声部化**） | 土色系 + 1–2 处点缀色（蓝/红） | 黑白 + 焦赭/土黄 ≤4 色、近单色阶（1980s 黑白档；*The Inevitable*） | **70%**（vs 康定斯基判据③） |
| P3 | **有机生长/分块度**（Organic Growth & Panels）`[归纳]` | 单一构图、边界封闭（普通架上画） | 2–4 块/双联，块间笔势同源 | ≥5 块多联（九联 *The Inevitable*）或整组「各自装裱又成整体」（粒子-整体档） | **50%**（单幅档与多联档按用途切换） |
| P4 | **面具/胚胎形象密度**（Mask & Embryo Forms）`[归纳]` | 0 处可辨头形（纯抽象观感） | 1–3 处隐约头形/胚胎形（半浮现） | ≥4 处面具头形 + 双眼成对（*They Always Appear* 档） | **55%** |
| P5 | **书写运动性**（Written Motion）`[归纳]` | 线描摹、匀速、无速度感 | 中速连笔、局部顿挫 | 高密度草书速度：连续缠绕长笔段、线宽方差大（连写段落 ≥1/3 画幅） | **65%** |
| P6 | **基底显影度**（Found-Support Traces）`[归纳]` | 平净底材、无材料痕迹 | 布纹/纸纹/拼接缝可见 | 药盒折痕、braille 印痕、信封窗、食物袋折线可见并参与构图（Pain Relief / Behind the Mask 档） | **40%**（小画档切 85%） |

> 用法：**P1 + P2 定「是不是萨拉希」**（书法骨架 + 索默色域）；P3 切「单幅/多联」；P4 决定面具头形显隐（外部观看者能否看到具象锚点）；P5 切「描摹/书写」；P6 切「干净面/材料显影」。
> 数据来源：档位阈值为 `[归纳]`（本项目操作化建议，未经渲染实验校准）；特征观察取自 [R4][R5][R16][R29][R33][R34]。
> **分工注（写死）**：**P1 强档 + P2 中强档（索默）是本模块专属**；「高纯度互补对撞 + 无字母构件 + 张力对位构图」整体属于康定斯基模块，禁止在本模块同档出现；「微书图案 + 书页装帧 + 金」整体属于贝赫扎德/细密画模块，禁止混入（见 §3.1）。本注为 `[归纳]`。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 康定斯基）**（× 康定斯基；本卡 §3.1 分工条款）：抽象两路径写死：书法线（书写笔势＋字母残影＋材质化色＋有机生长）vs 理论/音乐性（元素语法＋色彩声部）——可组合但分轴（N3）
- **分工（vs 贝赫扎德）**（× 贝赫扎德；本卡 §3.1 分工条款）：伊斯兰图像：现代书法（单幅、无叙事空间、墨+土色、无金）vs 手抄本细密画（层叠叙事＋微书＋金）——判据四条
- **同批注记（vs 吴冠中）**（× 吴冠中；本卡 §3.1 同批注记）：水墨自然抽象 vs 书法线抽象——不写死互斥，组合细则待主脑裁定
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：金层按 C-15 处理（点状 ≤5% 或移除）；C-16 反约束适用域；C-17 负空间口径

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/el_salahi.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
