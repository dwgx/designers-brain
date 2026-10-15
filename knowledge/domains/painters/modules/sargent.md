# 萨金特 模块卡 — `sargent`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/sargent.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **一笔到位（bravura 笔触效率）**：笔触可见覆盖 ≥60%、面部可辨笔画 ≤30、无预备素描分层——「把速写的清新保留进完成作」
2. **高调亮部＋单点饱和**：亮部（V ≥0.85）面积 ≥25%、高饱和（S ≥0.6）面积 ≤10%、纯色斑 ≤3 处
3. **社交姿态装置＋主导光**：身体轴向偏画面轴 ≥15°、手持物 ≥1、视线多斜视；单一主导光（高侧窗/黄昏/脚光）、高光斑集中 ≤35%
4. **边缘锐利与飞白并存＋暗部透明亮部堆叠**：关键边缘梯度 ≤1% 短边、干笔拖痕 ≥2 处；「从中调起步、最后处理最亮与最暗」
5. **拉长比例浅空间＋「只记录，不判断」＋织物即第二主角**：头身比 ≥8、背景 ≤2 层；情绪中性克制、背景无叙事符号；织物/家具面积 ≥40%

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Sargent-style bravura society portrait — alla prima, painted in one flow, no underdrawing:
a single sitter placed off-axis in a shallow interior, body turned ~15–30° from the picture plane, one hand holding a fan, a flower or a fold of the dress;
the face caught in a few decisive strokes — structure first, features reduced to spots in their right places; the rest of the figure and the dress loosened, dabs and drags of paint suggesting silk, velvet, pearls;
one dominant light — a high studio window, the mauve light of dusk, or stage footlights — falling on face and fabric, the rest of the room sinking into a transparent shadow that lets the ground show through;
high-key values: large pale areas (ivory, silver, rose, black-and-white) punctuated by one or two saturated accents — a red sash, a green lining, a gold brooch;
edges kept crisp where form must read, dry-brush scumbles elsewhere; the brushstroke left visible, confident and once-only;
the social presence is the subject: an elegant posture held mid-gesture, no psychological narrative, no eye contact required;
palette: lead white, ivory black, ochre, Mars yellow, vermilion, madder, viridian, cobalt or synthetic ultramarine, sienna, Mars brown;
19th-century oil on canvas, museum quality, Edwardian grand-manner portrait
[watercolor variant] transparent washes layered 2–4 times, paper left white for the light, quick directional strokes, touches of gouache and wax crayon, everything given with the intensity of a dream
```
**负向约束（`--no` 风格）**
```
--no preliminary drawing visible, academic underpainting, smooth invisible brushwork, sfumato gradients, airless tight rendering,
flat planes, suppressed mid-tones, posterized blocks, deliberate modernist flattening,
silver-grey ambient envelope between figures, contours dissolving into air, near-view breakdown,
four-colour closed palette, monochrome brown studies, limited-palette tonal precision,
single candle-lit spotlight with near-black background, dramatic tenebrism, heavy chiaroscuro,
sentimental expression analysis, deep psychological gloom,
digital smoothness, airbrushed skin, photo-bash, 3D render, cartoon, text
```

## 代码艺术规则（§8.2 原样）

1. **笔触可见性规则**：可见笔触覆盖 **≥60%**；平滑渐变带宽度 ≤2% 短边（禁 sfumato）；笔触方向族 3–6 个。自查：边缘方向场 + 渐变带检测。（依据：[R14]「freshness of the sketch」；[R2]「dabs」）
2. **一笔到位/破笔规则**：面部区域笔画数（边缘连通域）**≤30**；存在干笔拖痕（高频细线族）≥2 处；无「多层罩染」痕迹（色层 ≤3）。自查：连通域计数 + 高频线检测。（依据：[R14]；[R10] 价值分类法）
3. **高调与点缀规则**：亮部（V ≥0.85）面积 **≥25%**；高饱和（S ≥0.6）面积 **≤10%** 且连通域 1–3 个。自查：明度/饱和度直方图 + 连通域。（依据：[R2] 织物/长裙；[R13]）
4. **主导光规则**：存在单一主导光源（亮暗分界夹角 ≤45°）；亮部集中面积 ≤35%；**暗部透明**（暗部均值 V ≥0.15；近黑大块 ≥25% 面积即违规）。自查：亮度直方图 + 光源方向估计。（依据：[R7] 黄昏光；[R13] 脚光）
5. **浅空间规则**：背景梯度层数 ≤2；人物-背景对比保持（人物边缘可描、无化开）；透视收敛线 ≤1 组。自查：区域分割 + 消失点估计。（依据：[R4]「shallow space」；`velazquez.md` §3.1 空气轴对读）
6. **姿态装置规则**：身体轴向偏离画面轴 **≥15°**；手持物 ≥1 连通域（与手部重叠）；视线方向偏离镜头轴 ≥20°（或不可辨）。自查：姿态估计 + 手持物检测。（依据：[R3]「vivacious pose」）
7. **织物面积规则**：织物/家具面积 **≥40%**；质感高光斑 ≥2 处（小尺度高光密度峰）。自查：材质分割 + 高光峰检测。（依据：[R2]「opulent gowns against the brocade sofa」）
8. **水彩变体规则**（媒介参数）：纸白保留 **≥10%**；色彩层数 2–4；扫笔方向族 ≥2。自查：纸白掩膜 + 层数直方图。（依据：[R5] 媒介混合；[R11]「joyful fluidness」）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **笔触效率（bravura）**`[归纳]` | 平滑收笔、笔触隐没（早期学院档） | 可见流畅笔触 + 局部点触（肖像档） | 一笔到位 + 飞白 + 干笔拖痕（《X 夫人》/《康乃馨》档） | **70%** |
| P2 | **色域宽度**`[归纳]` | 单色/近单色（《持玫瑰的夏洛特》档——单色调色板 [R4]） | 主色 + 2–3 处点缀 | 全色板社交炫技（《温德姆姐妹》/《X 夫人》档） | **55%** |
| P3 | **社交在场感（姿态装置）**`[归纳]` | 静态正对、无手持物（正式委托档） | 偏轴坐姿 + 1 件手持物 | vivacious pose + 织物炫技 + 视线装置（《哈默斯利夫人》档 [R3]） | **60%** |
| P4 | **光类型（主导光强度）**`[归纳]` | 均匀画室漫光 | 主导侧光/窗光（肖像档） | 黄昏天光/舞台脚光（《康乃馨》[R7]/《El Jaleo》[R13] 档） | **55%** |
| P5 | **空间压缩（浅空间）**`[归纳]` | 深背景（户外/风景档） | 浅背景（半身/全身像档） | 贴背景浅空间 + 剪影强调（《持玫瑰》档 [R4]） | **50%** |
| P6 | **媒介与即兴度**（工作流参数）`[归纳]` | 木炭/石墨素描（「Mugs」档 [R11]） | 油画 alla prima（主档） | 水彩透明即兴（旅行档 [R11]） | **油画** |

> **用法**：P1 + P3 定「是不是萨金特」（≥2 条 ≥中档才成立）；P2 + P5 定「社交档 vs 单色档」；P4 定场景（画室/户外/舞台）；P6 是组稿参数（媒介轴，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若空间被**压平**、中间调被取消、笔触转向平面组织 → 越界进入**马奈**档；② 若笔触**退远融解**、银灰包络、人物间空气可见 → 越界**委拉斯开兹**档；③ 若色板收窄为四色封闭、炫技点转向「精确」 → 越界**佐恩**档（预写）；④ 若出现**画外单光源 + 近黑背景 + 高光只落脸/手/道具** → 越界**卡拉瓦乔**档。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 马奈）**（× 马奈（future）；本卡 §3.1 分工条款）：alla prima 两条路：笔触＝表演/完成＋保持体积＋完整明暗 vs 平面组织＋取消中间调——四轴判据、轴单主
- **分工（vs 委拉斯开兹）**（× 委拉斯开兹；本卡 §3.1 分工条款）：同一谱系两种观看距离：近观保持（炫技即目的、空气退场）vs 退远融解为空气——空气轴/笔触融解轴各单主
- **分工（vs 佐恩）**（× 佐恩（future）；本卡 §3.1 预写条款）：色板宽度轴单主：广阔色板＋炫技 vs 四色封闭＋控制——佐恩档案落地后按 wave 规程回改对齐
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 笔触 / C-08·C-09 运动预算 / C-12 色相预算

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/sargent.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
