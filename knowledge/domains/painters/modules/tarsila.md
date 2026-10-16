# 塔西拉·多·阿马拉尔 模块卡 — `tarsila`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/tarsila.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **cores caipiras 热带色板**：蓝/玫粉/黄/绿 4 主色全开＋白色调出梯度（「tudo em gradações… mistura de branco」）——被贬为「土气」的颜色被正名为国土色（azul puríssimo / rosa violáceo / amarelo vivo / verde cantante）
2. **几何化简形（软立体主义）**：树＝球＋柱、屋＝方块、山＝弧、云＝涡卷；形体完整圆润、从不碎裂——「separate shapes, simplified, rounded, and almost abstract」
3. **夸张与前缩的身体**：头小、肢大、唇厚、乳单、足巨（Abaporu 的脚、A Negra 的唇/乳）——身体部件被单独放大为构图事件（「distortion and exaggeration of the body」）
4. **平面层次＋平涂零投影**：天/地/水＝连续色带（背景层数 2–4、无消失点）；平涂＋深色轮廓、投影 ≈0、内部渐变 ≤2 色阶——「pintura limpa」
5. **热带植物志＋现代图标＋梦境生物**：香蕉叶（对角绿块）/仙人掌＋太阳花/木瓜树每画 ≥1 种标志植物；铁路/电线杆/加油站与棕榈同框；cuca/urutu 等「发明出来的动物」入画

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Tarsila do Amaral-style tropical modernism — a Brazilian landscape or figure painted as a geometricized dream:
soft Cubism without fragmentation — every form kept whole and rounded, simplified into spheres, arcs and blocks
(a tree is a ball on a column, a house a cube, a hill an arc, a river a ribbon);
cores caipiras palette — the four country colors turned national: purest blue, violet pink, vivid yellow, singing green,
mixed with white into soft gradations, laid as clean flat paint with dark outlines, no shadows, no visible brushwork;
stacked planar space — earth, sky and water as successive bands of color, no vanishing point;
one iconic tropical plant per scene — banana leaf as a single diagonal shape, a cactus crowned with a sun-flower,
a papaya tree with hanging fruit, a palm;
bodies soft and boneless, seated or lying quietly, with one part exaggerated — an enormous foot, full lips, a single breast;
a hint of the dreamlike and the invented — a strange animal in the forest, a moon with a face, a glowing egg, a snake on a hill;
modern icons welcome inside the tropics — a railway line, a gas pump, telephone poles, a tram;
oil on canvas, flat matte surface, clean poster-like clarity, museum reproduction quality
```
**负向约束（`--no` 风格）**
```
--no fragmentation, multiple viewpoints, collage elements, letters or newspaper scraps, analytic cubism grid,
all-over patterns, wallpaper or textile motifs, decorative ornament covering the canvas,
realistic chiaroscuro, cast shadows, dramatic lighting, visible brushstrokes, impasto, sfumato, pointillism,
botanical illustration detail, jungle undergrowth realism, photo-realism, 3D render, HDR gloss, neon glow,
gritty texture, dirt, noise, sepia, monochrome grey, anime, cartoon, text, signature, watermark, frame
```

## 代码艺术规则（§8.2 原样）

1. **色板规则**：全帧主色相 ≤5（蓝/玫粉/黄/绿 + 白）；高饱和像素（S>0.6）占比 15–40%；每种主色至少 1 个 ≥3% 画幅的连通块；白混梯度带（相邻色阶差 ≤12/255）在场。（自查：色相直方图 + 连通域；对照 §3.1 判据①）
2. **完整形规则**：全帧「碎裂主体」（同色域被 ≥3 条非轮廓线切割）数量 = 0；主体轮廓闭合（无拼贴物、无字母、无多视点重叠）。（自查：边缘图 + 连通域；对照 §3.1 判据②——毕加索侧越界警报）
3. **几何化简规则**：主形曲率拐点 ≤12 个/主体；树=球+柱、屋=方块、山=弧的模板命中率 ≥1；写实纹理能量（高频分量）低于参考帧 30%。（自查：曲率 + 频域）
4. **平涂规则**：投影区域 ≤2% 画幅；画内可见光源 = 0；可见笔触帧数 = 0；色块内部标准差 ≤2/255（「pintura limpa」）。（对照 C-01/C-05：显式声明「无投影、无笔触」）
5. **层次规则**：背景色带层数 2–4；消失点检测 = 无；天地水至少两级分节；主体允许出框（≥1 边裁切）。（对照 §3.1 判据④）
6. **植物符号规则**：每帧 ≥1 个热带植物符号（香蕉叶单块/太阳花仙人掌/木瓜树/棕榈）；植物为单件符号、不得成 all-over 图案（图案化即滑向马蒂斯侧，对照 §3.1 判据②）。（自查：符号模板 + 图案检测）
7. **梦境-夸张规则**（梦境模式时启用）：≥1 个幻想元素（非现实动物/悬浮形/重复形）；≥1 个身体部件夸张（尺度 ≥1.5× 自然比例，Abaporu 档 ≥2.5×）。（自查：目标检测 + 比例测量）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1/2/4/6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。与 `conflicts.md` 的关系：**C-06**（饱和度——塔站高饱和侧、显式取值）、**C-18**（形体塑造——塔站平涂/化简侧）、**C-05**（笔触——塔站无笔触侧）、**C-01**（硬阴影——塔「无投影」同侧、显式声明）为组合预检重点。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **热带色板度（Cores caipiras）**`[归纳]` | 欧洲灰调/学院色（越界警报：学院派） | 4 主色在场、掺白梯度控制 | 四色名句全开、饱和块大面积、白色梯度精细 | **80%** |
| P2 | **几何化简度（Geometric Simplification）**`[归纳]` | 写实细节、自然轮廓 | 形体球/弧/方块化（树=球+柱） | 完全符号化（屋=方块、山=弧、河=飘带） | **75%** |
| P3 | **前缩夸张（Distortion/Exaggeration）**`[归纳]` | 自然比例 | 局部夸张（唇/乳/手） | 巨型部件（Abaporu 巨足档） | **60%** |
| P4 | **梦境性（Fantasy/Dream）**`[归纳]` | 直接风景/人物 | 神秘动物、月亮、重复形 | 纯梦象（悬浮形体、变形的物） | **50%** |
| P5 | **平面层次（Planar Stacking）**`[归纳]` | 单层平涂、无背景分节 | 2–3 层色带（天/地/水） | planos sucessivos + 主体出框 | **65%** |
| P6 | **现代图标密度（Modern Icons）**`[归纳]` | 纯自然（无现代物） | 铁路/电线杆/加油站/电车入画 | 工业群像（Operários 档） | **40%** |

> **用法**：P1/P2 定「是不是塔西拉」的起步（两条中 ≥1 条 ≥ 中档才成立——热带色板或几何化简形）；P3/P4 定梦境-夸张档；P5/P6 定空间与现代性档。三档描述可直接当判定标准写进自查表。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若「all-over 图案＋图案与主体同权＋宽色相自由调用」→ 越界**马蒂斯**（P1 连用「设计」档即越界）；② 若「物象碎裂＋多视点＋拼贴物＋棕灰单色」→ 越界**毕加索**（P2 弱档连用即越界）；③ 若「工业机械质感＋金属色＋管道体」→ 越界**莱热**；④ 若「壁画工程尺度＋历史全景」→ 越界**里维拉**；⑤ 若「细描丛林＋植物学细节」→ 越界**卢梭式**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §3.1 分工条款（第一写死条款））：色彩：欧洲设计 vs 热带——色板来源（装饰系统 vs 被贬本土色正名）／图案系统（all-over vs 无）／色的组织／空间与尺度；判定须 ≥2 轴联合（尤其①③）；组合选主导轴并显式声明色板规程
- **分工（vs 毕加索）**（× 毕加索；本卡 §3.1 分工条款（第二写死条款））：立体主义：来源/发明 vs 转译/食人——来源方向／碎裂度（解体重组 vs 形体完整）／色彩／题材主体性；≥2 轴联合（尤其①④）；N4 二选一或分区（不可双开）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-06 饱和度（高饱和侧）／C-18 形体塑造（平涂/化简侧）／C-05 笔触（无笔触侧）／C-01 硬阴影（无投影同侧、显式声明）；句式改写：C-14（「渐变仅限掺白软过渡、不得成图案系统」）；不借莱热/卢梭（future）机械质感与丛林细描

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/tarsila.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
