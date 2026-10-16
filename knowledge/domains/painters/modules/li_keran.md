# 李可染 模块卡 — `li_keran`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/li_keran.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **逆光成画眼**：画面最亮区（瀑布/水面/云气）位于景物之后或被重墨包围；主体正面最暗区与背景最亮区同框——「亮」从「黑」里渗出
2. **积墨的层叠黑**：墨分多遍积染、层理可辨（深色区 V≤0.2 而梯度连续、可辨层次 ≥5 级）——「黑中透亮」，无死黑、无油光
3. **满构图＋亮口定点**：留白 ≤15%、主峰/树冠触画幅边 ≥1 处；≥1 处「亮口」（V≥0.85 连通域）被重墨包围——「扑面而来」的体量；色彩克制：墨色区 ≥70%、朱砂只作特例档（《万山红遍》）
4. **对景写生的光学空间**：定点观察、画内光向统一（阴影方向一致度 ≥70%）；中景为主体、点景合计 ≤10%（白墙黑瓦/帆船/牧童）——「为祖国河山立传」
5. **瀑布＝垂直光柱＋沉涩笔法**：垂直亮带（高宽比 ≥5:1）切入黑山、带缘墨色烘染（「把光引入画面」）；用笔慢、重、涩、短促笔线积叠（北碑书法功底）；长题与印章（「废画三千」「白发学童」）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Ink-wash landscape in the manner of Li Keran — a backlit monumental landscape built from accumulated ink:
a towering massif faces the viewer, its face in deep shadow — near-black layered ink built up in many
translucent washes, yet every layer legible, the darkness breathing rather than flat; the light comes
from BEHIND the mountains: a rim of glow along ridges and tree crowns, and one brilliant light aperture
— a waterfall plunging as a vertical ribbon of white, or a river, or a gap of luminous mist — cutting
through the black mass as the brightest passage of the picture; composition full: mountain, trees and
mist packed to the edges, sky reduced to a sliver, the subject towering and immediate, never a distant
prospect; trees massed as ink clusters with firm trunks; tiny white-walled, black-tiled houses, boats,
a buffalo and a boy set as small accents deep in the scene; one directional backlight governs the whole
sheet, shadow direction consistent; palette restrained to ink blacks and greys with subtle ochre and
indigo washes; optionally a crimson register — cinnabar-red mountains layered with ink, a black-red
counterpoint (Wanshan Hongbian mode); texture of wet ink accumulating on absorbent paper, soft edges,
no hard cast shadows, no glossy surface; mood solemn, heavy, luminous-dark, monumental
```
**负向约束（`--no` 风格）**
```
--no impressionist colorism, colored shadows without black, broken color dots, pastel palette, haze
dissolving forms into atmosphere, soft-focus bokeh, shallow depth of field, catastrophic weather,
spiral vortex composition, empty literati vastness, dry hemp-fiber texture strokes, long horizontal
handscroll, dotted rain texture as sole modeling, single-point perspective corridor, photorealistic HDR,
anime, cartoon, 3D render, glossy oil sheen, gold leaf decoration, watermark, museum frame
```

## 代码艺术规则（§8.2 原样）

1. **逆光结构规则**：画内最亮区（V≥0.85）被暗部（V≤0.35）包围比例 ≥60%；光向一致度 ≥70%；「亮口」连通域 **1–3 个**（画眼集中，避免平均）。自查：亮度直方图 + 光源方向估计 + 连通域计数。（依据：[R5]「光引入画面」；§1-1/§1-5）
2. **积墨层次规则**：深色区（V≤0.35）内可辨明度层 **≥5 级**；无单一死黑连通域 >15% 画面；无镜面高光（V≥0.98 且面积>1%）。自查：局部直方图 + 分水岭分层计数 + 高光掩膜。（依据：[R5][R8]；§1-2）
3. **满构图规则**：留白（V≥0.9 且 S≤0.1 的近纸色区）**≤15%**；主体触画幅边 ≥1 处；无连续空白背景带（对照 C-17）。自查：纸色掩膜统计 + 边缘接触检测。（依据：[R20]「满」；§1-3）
4. **亮口形态规则**：垂直亮带（高宽比 ≥5:1）≥1（瀑布档）或水面亮区 ≥15% 面积（江景档）——二选一必居其一；亮口边缘有墨色烘染过渡带（≥0.5% 短边）。自查：形态学 + 连通域 + 梯度带宽。（依据：[R5][R6]；§1-10）
5. **色域规则**：常规档——无彩色区（S≤0.25）面积 ≥70%，彩色仅限赭石/花青/藤黄低饱和烘染；朱砂档——红色（H∈[0,15]∪[345,360]，S≥0.5）面积 30–70%，红区边缘黑墨交织（红黑边界黑墨占比 ≥30%）。自查：HSV 掩膜 + 边界统计。（依据：[R19] 朱砂与墨「反复叠加」；§1-8）
6. **柔边规则**：无硬投影——阴影边界过渡带 ≥1% 短边（软于卡拉瓦乔档）；全帧明度中位 ≤0.35；最亮/最暗比 ≥8:1（极限对比）。自查：梯度带宽 + 直方图。（依据：[R6][R8]；§1-2）
7. **点景规则**：点景（屋/船/人/牛）合计 ≤10% 面积、单体 ≤2%；白墙黑瓦对 ≤20 组；人物/牛高度 ≤画面高 1/10。自查：实例计数（检测或人工）。（依据：§1-7）
8. **体量规则**：主峰/主体面积 ≥25%；主体轮廓由墨块边缘生成（无细线勾描：边缘线宽 >2px 占比 ≤20%）；垂直元素（瀑布/树干/塔）≥1 条贯穿中景。自查：分区统计 + 边缘宽度直方图。（依据：[R8][R20]；§1-4）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–4 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **逆光强度（Backlight Intensity）**`[归纳]` | 平光/漫射——无明显光源方向（早期写生档） | 侧逆光——山体一侧受光、一侧沉黑 | 正逆光——景物正面全黑、边缘与缝隙透光、「亮口」切黑（招牌档） | **75%** |
| P2 | **积墨层数（Ink Layering）**`[归纳]` | 淡墨一遍、线条为主（40 年代线性结构档） | 3–5 遍积染、层次中等 | 10 遍级积染、墨黑如铁而透气（60 年代后档） | **70%** |
| P3 | **满构图度（Fullness）**`[归纳]` | 留白多、清疏（40 年代档；**越界：文人简淡档**） | 半满——主体占画面约 2/3 | 满幅顶天立地、留白 ≤15%（招牌档） | **80%** |
| P4 | **亮口强度（Light Release）**`[归纳]` | 无明确亮口（全暗档） | 一处水面/云气透亮 | 瀑布/江水/天空成最强亮口、与黑形成极限对比 | **70%** |
| P5 | **色域档（Color Register）**`[归纳]` | 纯水墨（无彩色） | 赭石/花青淡彩烘染 | 朱砂红为主色、黑红对撞（《万山红遍》档） | **40%** |
| P6 | **体量重量感（Mass & Weight）**`[归纳]` | 轻灵（**越界：文人逸笔档**） | 厚重 | 铁铸山体、纪念碑体量（满构图的重量） | **75%** |

> **用法**：P1/P2/P4 定「是不是李可染」（逆光＋积墨＋亮口——三条中 ≥2 条 ≥ 中档，且不得全部落弱档）；P3 是「满」档（与黄公望/范宽区分的核心判据之一）；P5 是色彩档（可关到纯墨档、可开到朱砂档）；P6 是体量参数。**越界警报（与 §3.1 对齐，组合实验按此判分）**：① 出现**披麻皴＋长卷** → 越界黄公望；② 出现**雨点皴＋巨碑中轴** → 越界范宽；③ 出现**无定向弥漫光＋形体溶解** → 越界莫奈/透纳；④ 出现**留白 ≥35%＋减笔符号** → 越界八大山人；⑤ 出现**线网银灰＋彩点** → 越界吴冠中。本表档位阈值为 `[归纳]`（本项目操作化建议，未经渲染实验校准）。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 黄公望）**（× 黄公望；本卡 §3.1 分工条款（第一写死条款））：传统山水 → 光学化山水：无光源平光＋披麻皴＋长卷 vs 定向逆光＋积墨团块＋定点写生——四判据（光／塑形单元／空间／目的），≥3 条同档即判定；选主导轴、不得同时启用两档标志机制
- **分工（vs 范宽）**（× 范宽；本卡 §3.1 分工条款（第一写死条款））：山体量感两条路：雨点皴密点＋巨碑中轴＋均匀光 vs 墨层积染＋满构图＋定向逆光/亮口——四判据（塑形单元／光／构图／墨法）
- **分工（vs 莫奈 / 透纳）**（× 莫奈 / 透纳；本卡 §3.1 分工条款（第二写死条款））：自然光 vs 墨的逆光：油彩大气光溶解形体（莫/透）vs 水墨定向逆光强化形体（李）——四判据（媒介色域／光源方向／光与形／目标）；「无定向弥漫光＋形体溶解」即越界
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 笔触可见度（积墨层理 vs「只有渐变」）／C-12 色相预算（墨黑为主＋朱砂亮口）／C-17 负空间（满构图 ≤15% 与 ≥35% 档互斥）／硬阴影禁令同侧（声明「墨色渲染、无硬边投影」）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/li_keran.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
