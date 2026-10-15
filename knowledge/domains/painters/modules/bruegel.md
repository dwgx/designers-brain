# 老勃鲁盖尔 模块卡 — `bruegel`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/bruegel.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **鸟瞰全景**：视点抬到人群之上（地平线位于上 1/4–1/3、俯角 ≥15°）；全景连续——「让人群显形的唯一办法」
2. **人群即百科**：≥30–100 个匿名小人、每人一个独立动作（「230 个孩子玩 83 种游戏」）；最大人物聚类 ≤15% 画布、无主角
3. **季节作为结构＋单一基调**：组画＝六件十二月（月令／农事可读）；单件色调族＝单一季节——「不是细节的总和……而是整体效果」
4. **前景暗框＋纵深导引＋共时叙事**：下 1/4 暗框（repoussoir）＋≥1 条导引线；同帧 ≥3 类时间状态并存——主场景可「small, embedded, almost hidden」
5. **反理想化人体＋土色低饱和＋红点锚**：短壮弯曲的日常身体（身高／肩宽 <4）；全帧中位饱和 ≤0.45、红色小面积作锚——谚语／游戏／节庆可解码

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Bruegel-style panoramic narrative — a whole world under one season, seen from above:
an elevated bird's-eye viewpoint (horizon high in the frame), a vast continuous landscape —
village, fields, river, distant mountains — with no single vanishing-point axis;
dozens of small anonymous figures, each busy with their own task — reaping, resting,
playing, skating, talking — micro-episodes distributed evenly across the whole surface;
no hero, no center, no single focus;
one unified seasonal key, tonal unity — earth palette (ochre, brick red, forest green,
lead-white snow, slate-blue distance), small red accents as anchors;
a dark foreground frame (tree trunk, rocky ledge, buildings) with a path or river
leading the eye into the depth — the viewer placed inside the scene;
soft diffuse daylight, no dramatic single light; matte, precise, drawing-like surface;
minuteness — figures readable one by one, a painted encyclopedia of everyday life
```
**负向约束（`--no` 风格）**
```
--no single spotlight, hard cast shadows, chiaroscuro, theatre lighting,
no idealized heroic nudes, muscular anatomy, contrapposto display,
no concentric or rotational composition around one figure,
no single-point perspective axis, no staged theatrical tableau,
no empty void, no large blank negative space, no decorative flat pattern,
no storm event, turbulent waves, speed or energy field,
no modern city, artificial light, neon, night street,
no metallic gold, glossy varnish reflections, HDR gloss, 3D render, cartoon
```

## 代码艺术规则（§8.2 原样）

1. **鸟瞰规则**：地平线位于画面上 1/4–1/3；俯角 ≥15°（由田块/建筑透视估计）；画面无单一消失点主导（引导线消失点 ≥2 组或呈散点）。自查：地平线检测 + 透视估计。（依据：[R2] x-321）
2. **分布式人群规则**：人物 ≥30（中强档）且**无单一中心聚类**（最大聚类 ≤15% 画布面积）；每人独立动作（姿态重复率 ≤30%）。自查：实例分割 + 聚类 + 姿态去重。（依据：[R2] x-321「encyclopaedia」；[R9]）
3. **共时性规则**：同帧 ≥3 类不同时间活动并存（劳作/休息/游戏/仪式）；无统一叙事动线（无指向单一事件的视线/手势汇聚）。自查：场景分类 + 视线估计。（依据：[R2] x-320「same place at the same time」）
4. **季节基调规则**：全帧色相族 ≤4；季节可判（雪白 ≥15% 面积 → 冬；黄绿主族 → 夏；棕金 → 秋；灰褐+淡绿 → 早春）。自查：HSV 掩膜统计。（对照 C-12：蓝仅作远景大气，不主张 ≥40%）
5. **微缩细节规则**：人物高度中位 ≤ 画高 1/15；细节能量集中于 2–16px 尺度带；逐人动作可分类。自查：人物检测 + 多尺度能量比。（依据：[R2] x-321「slow and selective study」）
6. **前景暗框规则**：前景（下 1/4）明度中位 < 全帧中位 −0.1；≥1 条导引线（路径/河流/田垄）指向纵深；暗框元素 ≥1（树干/岩壁/建筑）。自查：亮度统计 + Hough 直线。（依据：[R3] lc_tour01「repoussoir」）
7. **反理想人体规则**：无英雄化裸体；人物身高/肩宽比 <4（短壮）；姿态多弯曲（蹲/倾/扭，对称站姿 ≤20%）。自查：姿态估计 + 比例统计。（依据：[R2] x-331；[R9]「stocky」）
8. **软光规则**：阴影边界梯度带宽 ≥2% 短边（软过渡）；无单点光源（高亮连通域 ≥2 或成带状）；暗部 V ≥0.05（不塌陷）。自查：梯度带宽 + 高光计数 + 直方图。（对照 C-01：与卡拉瓦乔/米开朗基罗硬光侧显式互斥；依据：[R3] methods_raking_light 所记漫射表面）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–2、6–8 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **全景俯角（bird's-eye tilt）**`[归纳]` | 平视/近景（《农民婚礼》《农民舞蹈》档） | 低俯角中景（《前往髑髅地》档） | 高俯角全景（《儿童游戏》《雪中猎人》档） | **70%** |
| P2 | **人群规模/微观情节数**`[归纳]` | ≤5 人（《农夫与掏鸟窝者》档） | 10–40 人、成组散布 | 100+ 人、全画铺开（《儿童游戏》230+ 档） | **60%** |
| P3 | **季节基调强度（tonal seasonality）**`[归纳]` | 季节模糊/中性（部分室内档） | 明确季相（色相族集中于一个季节） | 极端季相（《雪中猎人》「永久寒冷」档） | **65%** |
| P4 | **细节微缩度（minuteness）**`[归纳]` | 概括笔法、个体不可辨 | 个体动作可辨 | 逐人逐物可读（「缓慢而选择性细看」档） | **70%** |
| P5 | **反理想化度（anti-ideal bodies）**`[归纳]` | 接近自然比例（早期档） | 短壮农民体型 | 压扁/弯曲/躯干化（《盲人引盲》《乞丐》档） | **60%** |
| P6 | **谚语/民俗编码密度**`[归纳]` | 纯观察（《农民婚礼》《收割者》档） | 1–3 个民俗元素（风筝、节庆道具） | 全画可解码百科（《尼德兰谚语》《儿童游戏》档） | **40%** |

> **用法**：P1/P2/P4 定「是不是勃鲁盖尔」（三条中 ≥2 条 ≥ 中档才成立）；P3 定季节档（中性 → 单季 → 极端季相）；P5/P6 定人物与语义层（可关）。**越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若出现**单点硬光＋戏剧投影** → 越界卡拉瓦乔；② 若转为**天气事件/能量场/漩涡** → 越界透纳；③ 若出现**英雄化裸体＋向心旋转集中** → 越界米开朗基罗（分工轴）；④ 若出现**平面装饰＋大留白＋曲线族** → 越界北斋（分工轴）；⑤ 若以**新物种发明**为主装置 → 越界博斯；⑥ 若出现**现代都市/人造光/夜街** → 越界霍珀。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款）：系列叙事两档：油画全景／时间序列 vs 版画单景／母题连作——判据四条＋边界注（≥2 轴联合）；蓝轴按 C-12
- **分工（vs 米开朗基罗）**（× 米开朗基罗；本卡 §3.1 分工条款）：人群调度：理想人群档 vs 日常微观档——判据四条＋边界注（人体理想度轴）
- **分工（vs 博斯）**（× 博斯；本卡 §3.1 镜像条款）：现实端 vs 超现实端：「怪物设计」不互抄——bosch.md 预判（2026-10-15）本档案确认成立
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影（软侧同侧声明）／C-09 运动预算（静／定格侧）／C-12 蓝轴（远景大气蓝）／C-16 ／C-17 负空间（满构图 ≤15%）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/bruegel.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
