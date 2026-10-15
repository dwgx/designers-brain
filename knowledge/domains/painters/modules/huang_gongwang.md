# 黄公望 模块卡 — `huang_gongwang`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/huang_gongwang.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **披麻皴＋干笔积叠**：山体长披麻皴（≥3 线/组、随山势下垂、无斧劈钉头）；淡墨起稿逐层积至浑厚、墨色可辨层次 3–5 级
2. **长卷时空**：纵横比 ≥5:1（《富春山居图》约 19:1）、段落 3–5 段疏密交替——「逐旋填剳，阅三四载」的历时累积
3. **平远/阔远＋点苔醒山**：水面（留白/淡墨）面积 ≥30%；每处山体苔点 ≥20、落于轮廓线与凹处
4. **树法＋点景极小**：松针扇形/横点、杂树混点、「松树不见根」；渔舟/屋舍/人物皆「点」级（人物 ≤ 树高 1/5）
5. **浅绛设色＋纸色为主调＋款印题跋**：赭石为主、彩色像素 ≤20%；纸色 40–60%、浓墨 ≤10%；自题述缘起、后跋层层叠加

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Chinese literati landscape handscroll in the manner of Huang Gongwang (黃公望, 1269–1354):
ink on paper, optionally with a light-ocher "qianjiang" wash; a continuous river landscape —
soft, rounded Jiangnan hills rising from flat water; mountain surfaces drawn with long,
loose "hemp-fiber" texture strokes (pima cun): slightly wavy dry-brush lines in groups,
following the slope, built up in layers from pale ink to darker accents, then finished with
clusters of dark moss dots (diantai) along ridges, rock edges and shadow pockets; trees as
crisp silhouettes — pines with fan-like needle dots, mixed trees as ink dabs, straight clean
trunks, no exposed roots; a wide, calm river as a luminous paper-white band running through
the scroll, with a few tiny boats, thatched huts, a bridge and one or two fishermen as
minute point-scenery; dry brush and feathery "flying white" (feibai) textures, no wet blobs;
restrained color — pale ocher on exposed earth, thin blue-green on vegetation; the
composition unfolds horizontally as a slow rhythm of dense and sparse passages (mountain
cluster → open water → village → mountain), to be read section by section like a journey;
overall mood: level-and-far (pingyuan), serene, "plain and natural" (pingdan tianzhen),
paper breathing, never crowded, never sweet; a modest column of calligraphy and a few red
seals close the composition
```
**负向约束（`--no` 风格）**
```
--no saturated color, vivid green/blue, opaque mineral pigments (azurite, malachite),
gold, glossy sheen, oil-paint impasto, 3D or photorealistic rendering, hard uniform black
outlines, ax-cut (fupi) or raindrop (yudian) texture strokes, dense uniform stippling,
crosshatching, western single-source lighting, chiaroscuro, cast shadows, vanishing-point
perspective, symmetrical or centered composition, full-bleed clutter, water reflections
with sharp highlights, detailed faces, narrative action, sweet decorative prettiness
```

## 代码艺术规则（§8.2 原样）

1. **披麻皴单元**：山体表面纹理线成组出现（≥3 线/组），组内线与线方向夹角 ≤30°、沿坡向延展；单线端点无钉头/折角（折角 ≤1 处/10 线）；线宽变化平缓（同一线内宽度变化 ≤50%）。
2. **积墨层次**：山体区域明度直方图呈 3–5 个可分辨带；淡墨（相对纸色降幅 ≤45%）覆盖山体面积 ≥50%；浓墨醒点 ≤10% 山体面积；不得出现一次成型的中灰平涂块（内部标准差 >6%）。
3. **水面/留白**：水面（纸色高亮带，亮度 ≥ 纸色 90%）面积 ≥25%；横向贯穿 ≥60% 画幅宽度；水面上仅允许极淡的墨线（波纹/远岸，覆盖率 ≤3%）。
4. **点苔**：苔点簇 ≥3 处/画面段；单点直径 ≤ 山体高度的 2%；点落位距山体轮廓线 ≤ 5% 山体高度的比例 ≥60%。
5. **长卷节奏**：长卷（纵横比 ≥5:1）须有 ≥3 段疏密交替——以段落墨迹覆盖率极差 ≥30%（相对）为界；单段内不得出现左右镜像对称（镜像相关系数 ≤0.6）。
6. **色域**：彩色像素（饱和度 >15%）≤20%；色相 ≤2 族（赭黄系 / 青绿系）；全帧平均饱和度 ≤35%；单块饱和度 ≥70% 的连通彩色区域面积 ≤2%（防重彩退化）。
7. **点景与动画（动画时）**：点景元素（舟/屋/人/桥）总位移 ≤1% 画幅/秒；仅允许水面 ≤2px 波动与云气 ≤0.5%/秒 漂移；不得出现人物特写、叙事动作或镜头推拉；墨迹不得闪变（帧间差 ≤1%）。

## 控制参数（§4 原样）

**P1 披麻皴密度（Hemp-fiber Texture Density）**（默认 中）`[归纳]`
- 弱: 山石以淡墨勾廓为主、皴线稀疏（《九峰雪霁图》式雪景简笔）
- 中: 典型长披麻、疏密有致（《富春山居图》）
- 强: 长披麻满布、层层叠加（《天池石壁图》式繁复）

**P2 积墨层数（Ink Accumulation Layers）**（默认 3–4 级）`[归纳]`
- 弱: 2 级（淡/浓）
- 中: 3–4 级
- 强: 5 级（焦浓重淡清）＋干湿对比

**P3 长卷段落节奏（Scroll Rhythm）**（默认 中）`[归纳]`
- 弱: 单段平缓（局部小景）
- 中: 3–5 段疏密交替（《富春山居图》）
- 强: 多段强对比（峰峦—江面—村落—峰峦，段落落差大）

**P4 浅绛色度（Light-ocher Wash）**（默认 弱–中）`[归纳]`
- 弱: 纯水墨（《九峰雪霁图》）
- 中: 淡赭＋墨青局部（《丹崖玉树图》）
- 强: 赭石/墨青/墨绿冷暖互补（《天池石壁图》）

**P5 平远/阔远纵深（Level-distance Depth）**（默认 中–强）`[归纳]`
- 弱: 高远为主（层叠山体）
- 中: 平远＋阔远（江面隔开两岸）
- 强: 阔远主导（大面积水面，山体退居上下带）

**P6 点景密度（Point-scenery Density）**（默认 中）`[归纳]`
- 弱: 几乎无人烟（纯山水）
- 中: 少量渔舟/屋舍（每段 1–3 处）
- 强: 村落/桥梁/人物较多（仍为"点"级）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 八大山人）**（× 八大山人；本卡 §3.1 分工条款）：水墨家族分档写死：山水长卷＋披麻皴积墨 vs 花鸟单页＋减笔白眼——两卡禁项互列（黄禁白眼/≥60% 留白/一笔造型）
- **分工（vs 塞尚）**（× 塞尚；本卡 §3.1 分工条款）：结构推导（一次成型几何网格）vs 笔墨累积（多层叠加在时间中生长）——判据三条
- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款）：纸本水墨长卷（毛笔提按/飞白/渗化）vs 版画等宽刻线＋平涂——线条/色彩/叙事装置三判据
- **分工（vs 范宽）**（× 范宽（future）；本卡 §3.1 分工条款）：披麻长线＋淡墨积叠＋横向连续 vs 雨点密皴＋浓墨湿笔＋纵向巨碑——判据三条

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/huang_gongwang.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
