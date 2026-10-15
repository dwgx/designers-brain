# 蒙克 模块卡 — `munch`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/munch.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **声波线（波浪线族）**：天空/发丝/岸线画成连续起伏波带（≥3 条嵌套、共享走向）；《尖叫》天空＝同心波浪——「像把声音画出来」
2. **心理景观＋冻结瞬间**：≥1 处「物理不可能」（血云天/融化地平线）且与人物情绪同向；除线条波形外画面无运动（无运动模糊、姿态静止）
3. **去面孔化/面具化＋象征色区**：焦点人物可辨五官 ≤1；血红/蓝黑/病绿黄三锚点大块平色区（≥2 处 ≥8%）、硬转换
4. **舞台化压缩空间**：高视点＋斜线切前景（≥60% 画宽、10–30°）＋背后虚空；人物像「舞台上的演员」
5. **粗粝表面与版画质感＋母题重复与组画**：滴淌/刮擦/不上光（镜面高光 ≈0）；木刻刀痕/木纹、色数 ≤4；同一构图家族 ≥2 变体；《生命饰带》以蜿蜒岸线贯穿编组

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Munch-style psychological landscape — a state of mind rendered as scene, not observed from life:
one or two figures reduced to ciphers, faces featureless or mask-like, one figure at the emotional extreme;
the scene compressed onto a stage — a bridge or shoreline diagonal cuts across the high-viewpoint foreground,
the ground drops away into a void; behind it, water and a distant city dissolve into the dark;
the sky becomes a field of concentric, undulating bands — sound waves made visible —
blood-red and orange against a blue-black fjord;
colour as symbolic zones, flat and saturated with hard transitions: blood red, blue-black, sick green-yellow;
the sinuous shoreline weaves through; hair and contours undulate like radio waves;
matte, unvarnished surface — visible board texture, thinned paint, drips and scraped passages;
palette: cadmium red, vermilion, ultramarine to blue-black, viridian and sickly yellow-green, ochre, bone white;
symbolist and silent, frozen — love, anxiety and death as archetypes, no anecdote, no detail
[print variant] coarse woodcut or lithograph: gouged grain printed, jagged edges, flat colour blocks, heavy black key lines, ≤4 colours
```
**负向约束（`--no` 风格）**
```
--no cheerful daylight, naturalistic detail, readable faces, portrait likeness, smooth gradients, glossy varnish,
impasto fireworks, complementary-colour vibration across the whole canvas, decorative gold, deep linear perspective,
crowds, anecdote, genre scene, text, photorealistic skin, cosy interiors, soft sfumato, heavy chiaroscuro,
joyful saturated primaries everywhere, symmetry, cartoon, anime, 3D render, photographic realism
```

## 代码艺术规则（§8.2 原样）

1. **声波线规则**：天空区域（上 1/3）内检出 **≥3 条嵌套曲线带**，曲率符号一致、方向族夹角 ≤20°；线宽变异 ≤2:1。自查：边缘方向场直方图（主导族占比 ≥40%）+ 曲线拟合计数。（依据：[R6] MM N 43 波浪线＝无线电波；[R7]「血红线条被比作声波」）
2. **去面孔规则**：焦点人物（最大人形）可辨认五官特征数 **≤1**；全画面人脸关键点检测命中 ≤1 组（眼/鼻/嘴）。自查：人脸关键点检测 + 实例分割。（依据：[R6] T 2547「面具背后」；[R2][R3] featureless faces）
3. **色区规则**：**≥2 个**大面积平色区（各 ≥8% 画布）落于锚点——血红（H 0–15°，S ≥0.65）、蓝黑（H 210–250°，V ≤0.35）、病绿黄（H 60–95°，S 0.25–0.6）；全帧**中位饱和 ≤0.5**（与梵高式全幅振动区分）；色区边界梯度带宽 ≤2% 短边（硬转换）。自查：HSV 掩膜 + 区域统计。
4. **舞台斜线规则**：前景存在对角直线元素（桥/栏杆/岸线）横跨 **≥60% 画宽、倾角 10–30°**；地平线高度 ≥60% 画高（压缩空间）。自查：直线检测（Hough）+ 高度比。
5. **冻结规则**：全画面无运动模糊；人物姿态 = 静止；「振动」仅以**线条形状**存在。视频帧：事件外光流 Δ ≤1%/帧；波线区允许局部振荡（振幅 ≤2% 短边）。自查：模糊核检测 / 光流场。（与 C-09 运动预算对齐：蒙克站「冻结」侧）
6. **简化规则**：焦点平面人物数 **≤3**；每个人物内部细节边缘密度 ≤ 全帧均值的 1.2 倍；衣/发以 ≤3 个团块呈现。自查：边缘密度图 + 人物实例分割。（依据：[R6]「把周围刮掉一半、只留块面」）
7. **表面规则**：无镜面高光（V >0.95 且面积 >0.5% 的斑 = 0）；可见材料纹理（板纹/布纹频谱带）；允许 0–2 条竖向滴痕（不强制）。自查：高光检测 + 频谱分析。（依据：[R2] deliberate drips；[R5] matte/fragile）
8. **木刻/版画帧附加**：色数 **≤4**；黑主线宽厚（线宽中位数 ≥ 常规帧 2×）；边缘锯齿度高于阈值；木纹印痕（方向性纹理）存在。自查：色数统计 + 线宽/粗糙度分析。（依据：[R1][R9] 木刻革新与锯拼；[R5]）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–5 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **心理变形的外化度**`[归纳]` | 自然主义场景 + 气氛（写生/印象主义档：《晨》《卡尔·约翰街》） | 简化形体 + 1–2 个符号元素（《忧郁》《傍晚》档） | 全场景变形：《尖叫》档——声波天 + 无脸 + 空间融化 | **65%** |
| P2 | **波浪线强度（声波性）**`[归纳]` | 平静直线/水平线（室内档） | 岸线/发丝/树冠波动（《生命之舞》《桥上的少女》档） | 同心/放射波浪族环绕主体（《尖叫》《焦虑》档） | **60%** |
| P3 | **象征色区分档**`[归纳]` | 自然色域（写生档） | 1–2 个符号色区（病绿脸、红云） | 三区符号（血红/蓝黑/病绿黄）+ 平色带硬转换 | **55%** |
| P4 | **面孔预算（去面孔化）**`[归纳]` | 肖像级五官（肖像/自画像档） | 简化五官、背转/低头（《生命之舞》档） | 无脸/面具/骷髅化（《尖叫》主体） | **60%** |
| P5 | **空间压缩 / 舞台化**`[归纳]` | 深透视风景（早期档） | 浅舞台 + 背景（室内群像档：《死亡床边》） | 高视点 + 斜线 + 虚空（桥面档） | **55%** |
| P6 | **组画 / 变体性**（工作流参数）`[归纳]` | 单幅（1 帧） | 小系列 3–8 变体（同一母题多版本） | 完整饰带 ≥12 幅 + 房间编排（《生命饰带》/礼堂档） | **1**（单幅起步） |

> **用法**：P1/P2/P4 定「是不是蒙克」（三条中 ≥2 条 ≥ 中档才成立）；P3/P5 定时期与场景档（写生→象征→《尖叫》的滑轨）；P6 是组稿参数（单幅 vs 饰带，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若「情绪载体」转为**笔触能量场**（厚涂覆盖率 ≥60%、互补对近 1:1、全画面运动）→ 越界进入**梵高**档；② 若扭曲改为**纵向拉伸**且题材转宗教神圣 → 越界**格列柯**；③ 若场景转**都市夜景 + 人造光 + 几何建筑**、孤独成为主题 → 越界**霍珀**；④ 若出现**画外单光源 + 近黑背景 + 高光只落脸手道具** → 越界**卡拉瓦乔**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 梵高）**（× 梵高；本卡 §3.1 分工条款）：情绪两档写死：状态档（冷——场景变形＋冻结＋分区符号色）vs 能量档（热——笔触/色彩能量场＋全画面运动）——判据四条，同用须选主导轴（70/30）
- **分工（vs 弗里达·卡罗）**（× 弗里达·卡罗；本卡 §3.1 分工条款）：普世焦虑原型语法 vs 具体自传符号系统——判据：符号可解码性（是否需生平词典）
- **分工（vs 弗里德里希）**（× 弗里德里希；本卡 §3.1 镜像确认）：自然的身份：焦虑的症状（蒙克）vs 神性的崇高（弗里德里希）
- **分工（vs 埃尔·格列柯 / 布莱克）**（× 格列柯 / 布莱克；本卡 §3.1 分工条款）：扭曲两路（焦虑内爆 vs 宗教狂喜）；象征两路（私人心理 vs 自创神话体系）
- **组合预检（Lane B）**（× Lane B 与既有模块；本卡 §3.1 组合注记）：重点核查：C-01 硬阴影 / C-05 笔触 / C-09 运动预算 / C-12 色相预算（不借梵高厚涂振动、卡拉瓦乔近黑背景、霍珀人造光几何）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/munch.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
