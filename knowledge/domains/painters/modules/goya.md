# 戈雅 模块卡 — `goya`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/goya.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **画内光源的「证据光」**：提灯／火把／营火——光源在画内且可指认（≥1）；光只为事件照明
2. **关键元素出画外＋即时动作推前景**：行刑队背身／裁切；决定性信息在画外（新闻式构图）
3. **施害者匿名化＋受害者群像**：施害者 0 面孔、制式重复队列；受害者连续体＋一个情感极值
4. **低饱和暗调＋黑土白三件套**：土黄／棕／黑为底、白只作闪光（衬衫／尸布／刀光）、红只作血；哑光砂质
5. **版画语言＋序列帧叙事**：细平行线＋平飞尘块＋刮亮（无交叉排线）；题刻短句＋组画（80/82/33/22）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Goya-style narrative painting — an event caught mid-action, treated as an eyewitness report:
key elements placed outside the picture frame — the firing squad seen from behind,
cropped at the frame edge; the immediate action pushed into the lower foreground;
perpetrators anonymous and faceless, repeated as a mechanical rank;
victims as a continuous queue inside one frame — the already dead, the dying, the next to die;
one in-scene light source (a square lantern set on the ground between the two groups)
falls hardest on the victims and casts the executioners into shadow;
a single victim at the emotional extreme, arms thrown up, white shirt blazing;
palette of earth ochres, umber, black and lead white, one blood-red accent only;
matte granular finish, blunt loose brushwork, no theatricality, no glory;
monumental night scene with a readable townscape silhouette in the far distance
[print variant] fine parallel etched lines, large flat aquatint washes, burnished highlights,
no cross-hatching, one short caption etched below the image
```
**负向约束（`--no` 风格）**
```
--no idealised heroes, triumphant or heroic poses, classical composition, allegorical halo,
soft studio lighting, multiple light sources, fill light, reflections, glossy varnish,
sweet pastel palette, cheerful daylight, decorative beauty, glamour, pomp, pageantry,
motion blur, smooth airbrushed gradients, single-psychological-portrait focus,
facial detail on every figure, symmetry, cartoon, anime, 3D render, photographic realism
```

## 代码艺术规则（§8.2 原样）

1. **提灯规则（画内光源）**：夜戏/处决帧中，画内可见光源数 ∈ [1,2]，且光源位于画面下 1/3 × 中央 1/3 区域；亮区重心（亮度前 10% 像素的质心）落在受害者组包围盒内；施害者组平均亮度 ≤ 全帧平均亮度的 40%。（依据：普拉多对《第三五月》的官方描述「光强烈照亮英雄」`[研究]`[R10]）
2. **出画外规则**：主事件元素（施害组/决定性上下文）≥1 组被画框裁切或呈背身；「即时动作」（帧内最大姿态偏移的载体）位于画面下 1/3 前景带。（依据：Met「关键元素置于画外、即时动作推向前景」`[研究]`[R1]）
3. **面孔预算**：施害者面孔可见数 = 0；受害者可见面孔（可辨认五官）≤ 2；其余人物以体态/剪影/团块呈现。自查：人脸检测计数。
4. **队列时间性**：受害者组 ≥3 人，且同帧可读出「已死（卧地）/濒死（倒伏）/将死（站立待决）」三态中至少两态。自查：姿态分类 + 空间排序。
5. **色彩预算**：饱和色（S ≥ 0.6）像素面积 ≤ 3%；黑+土色系（H 20–50°、S ≤ 0.4、V ≤ 0.5）合计 ≥ 60% 面积；白色高光连通域 ≤ 5 个，且每个必须与「衬衫/尸布/刀锋/纸」四类对象之一相交；红色仅允许出现在伤口/血迹区域。自查：HSV 掩膜 + 连通域。
6. **表面规则**：全帧无镜面高光（亮度 > 0.95 且面积 > 0.5% 的镜面斑 = 0）；高频粗糙度均匀（哑光砂质，Laplacian 方差带内无 >12 px 平滑区）。自查：高光检测 + 高频能量图。
7. **版画帧附加**：交叉排线交叉点密度 ≈ 0（线方向族 ≤ 2 且互不交叉）；≥1 块均匀飞尘区（面积 ≥ 10%、内部亮度方差 ≤ 5/255）；≥1 个刮亮点（比周围飞尘亮 ≥ 2 个灰阶）；题刻 ≤ 1 行、位于画面下缘外。自查：方向场分析 + 区域方差。
8. **怪诞帧附加**：非人/半人形象 ≥1 且与讽喻对象同框（人的行为与兽形并置）；恐惧面容（张口/瞪眼）≥1。自查：对象检测 + 面容关键点。

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–3 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **事件即时性 / 新闻构图强度**`[归纳]` | 闭合场面：事件全在画内、动作止步、构图完整 | 关键元素部分出画外（裁切 1 组）；动作落前景 | 施害者背身/裁切、决定性信息在画外、动作压进前景 1/3（《第三五月》级） | **70%** |
| P2 | **光源的「证据性」（画内光源）**`[归纳]` | 平光/漫射（挂毯期、白天记录档） | 单一画内光源（提灯/火把）局部照明，环境仍可读 | 光源成为构图主角（中央提灯，光锥决定亮区分布） | **60%** |
| P3 | **怪诞强度**`[归纳]` | 现实场景 + 轻微漫画化（肖像讽刺级） | 兽化/面具/女巫/傀儡等半怪形象进入画面 | 噩梦形象库全开（食子、飞女、巨人、怪兽集会）且与讽喻对象绑定 | **40%**（默认克制，讽喻按需升档） |
| P4 | **面孔预算 / 匿名化**`[归纳]` | 面孔清晰可数（群像肖像级） | 群体中部分面孔可见、个体化有限 | 施害者 0 面孔（全背身）；受害者 ≤2 面孔且类型化；其余以体态/剪影叙事 | **70%** |
| P5 | **黑度 / 色域收窄**`[归纳]` | 洛可可亮色（挂毯草图档） | 土色系低饱和、白黑两级加强 | 近单色暗调（黑画档：土黄/棕/黑 + 白闪点） | **65%** |
| P6 | **序列帧数**（工作流参数）`[归纳]` | 单幅（1 帧） | 小系列 3–8 帧（同一母题/事件的多面） | 大系列 ≥22 帧 + 每帧题刻（奇想集 80 / 战祸 82 / 斗牛术 33 / 胡言集 22 档） | **1**（单幅起步） |

> **用法**：P1/P2 定「是不是戈雅」（新闻构图 + 证据光；两条同时≥中档才成立）；P3/P5 定时期（挂毯期→黑画档的滑轨）；P4 定叙事（谁有脸、谁没有）；P6 是组稿参数（单幅 vs 系列，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **分工注（与 §3.1 对齐）**：P2 一旦为「弱/中」且画面转入「单光源连续衰减照单张脸」，即越界进入**伦勃朗**领域；P2 为「强」但光源移到画外、亮部只落脸/手/道具，即越界进入**卡拉瓦乔**领域——组合实验按此判分。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-01**（× 卡拉瓦乔 / Lane B；本卡 §8.2-1 + §4 P2）：硬阴影改写：提灯半影宽度显式给出（画内光源 ≥1 vs 卡拉瓦乔 =0）
- **C-11**（× 卡拉瓦乔；本卡 §8.2-1）：亮部对象（群体 vs 脸/手/道具）
- **C-12**（× 卡拉瓦乔；本卡 §8.2-5）：色相面积预算（饱和色 ≤3%、黑＋土色 ≥60%；组合前按 C-12 预检）
- **分工（vs 伦勃朗）**（× 伦勃朗；本卡 §8.2-3）：面孔预算（类型化群脸 vs 单脸心理）
- **C-05**（× 达·芬奇 / 梵高；本卡 §8.2-6）：表面系统（哑光砂质、干涩笔触 vs 柔边渐变 / 笔触情绪场）
- **C-07**（× 丢勒 / 北斋；本卡 §8.2-7）：版画表面（细平行线＋平飞尘＋刮亮、无交叉排线）
- **C-17**（× 米开朗基罗 · 负空间组；组合预检）：负空间（组合前按 C-17 预检）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/goya.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
