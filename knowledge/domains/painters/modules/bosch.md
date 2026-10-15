# 博斯 模块卡 — `bosch`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/bosch.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **全景高视点＋单帧多叙事单元**：地平线 ≥ 上 1/3、可辨景深平面 ≥2；独立叙事单元 ≥5、无单一焦点（编目式密度）
2. **混合生物（拼装式）＋尺度错乱**：混合体 ≥3/帧、每个可拆出 ≥2 类可辨识部件来源；≥1 元素与人体比例 ≥2:1
3. **平光/环境光＋薄涂哑光**：画内单点主光源 = 0（夜景靠多重火光、不聚焦单张脸）；镜面高光 ≈0、起稿可透视——与传统光滑釉面相反
4. **色板「宝石谱」＋怪脸漫画**：azurite 蓝＋铜绿＋黄＋朱砂红＋铅白亮色铺开（对照戈雅「土黑＋白闪点」）；夸张兽化面孔、点线式起稿
5. **直视目光（猫头鹰）＋道德对位结构**：猫头鹰/半人直视观众 ≥1（常成对置板缘）；三联天堂—人间—地狱三幕＋帧内善恶成对 ≥2 组

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Bosch-style moral panorama — an encyclopedic triptych landscape, seen from an elevated
high horizon in three superimposed depth planes; a teeming scene of many small figures
(several narrative episodes in one frame, no single focus);
invented hybrid creatures assembled from two or more recognizable parts —
eggshell torsos, tree-trunk legs, bird heads, arrows, knives, musical instruments;
objects and animals at impossible scale — giant fruit, oversized birds, huge vessels
set among tiny human figures; proportion and terrestrial logic abandoned;
owls staring straight out at the viewer at the panel edges;
even all-over illumination — no single theatrical light source, daylight or
multiple fires in a night spectacle;
jewel-like palette spread across the surface: azurite blue, verdigris and malachite greens,
lead-tin yellow, vermilion and madder red, lead white — earth tones only as underpainting;
thin, matte, translucent paint layers with a quick sure touch, sketchy underdrawing
showing through in places; late-medieval didactic detail, moral allegory and
burlesque humour at once
```
**负向约束（`--no` 风格）**
```
--no single focus or hero, spotlight lighting, single hard light source, chiaroscuro,
sfumato soft edges, glossy varnish reflections, smooth airbrushed gradients,
photorealistic anatomy, uniform texture, one-species monsters, ordinary scale logic,
empty negative space, minimalism, pastel sweetness, anime/cartoon simplification,
3D render, photographic realism, modern clothing, clean digital line art
```

## 代码艺术规则（§8.2 原样）

1. **地平线规则**：地平线位于画面上 1/3 以上（画面高度的 ≤40% 处）；地平线以下可辨景深平面 ≥2（前/中/远）。自查：边缘/地平线检测 + 深度带分割。（依据：[R1]「three superimposed planes… elevation of the horizon line」）
2. **多事件密度**：单帧可辨叙事单元 ≥5（小群体/动作簇）；任一焦点簇面积 ≤20%（无单一焦点）。自查：连通域 + 动作簇聚类计数。
3. **生物发明计数**：混合体 ≥3 个/帧；每个可拆出 ≥2 类来源部件（动物/植物/器物/人体），且**不是**单物种的等比放大。自查：对象检测 + 部件来源标注。（依据：[R16]「compound animals」；[R1]）
4. **尺度错乱**：≥1 组元素的「等效比例」与人形 ≥2:1（巨果/巨鸟/巨器 vs 小人）。自查：目标框高度比。
5. **直视目光计数**：直视观众的形象 ≥1（优先猫头鹰，且成对置于板缘更佳）。自查：面部/眼向关键点 + 视线朝向。
6. **光照规则**：全帧无单点戏剧主光源（亮度前 10% 像素的质心不集中于单一对象）；日景=均匀天光（暗带 ≤30%）、夜景=≥2 处独立火光且分布分散。自查：亮度质心 + 光源连通域计数。（对照：戈雅 §8.2-1「画内光源 ∈[1,2] 且聚焦」）
7. **色域预算**：蓝绿系（azurite/verdigris 域，H 150–250）面积 15–35%；暖亮色（黄/朱/红淀）≥10%；土黑系 ≤55%；整体平均明度 V ≥ 0.45（乐园档）/ ≤0.45（夜档）。自查：HSV 掩膜统计。
8. **道德对位（系列帧）**：成组帧须可读「天堂→人间→地狱」或「七罪」序列；单帧须含 ≥2 组善/恶成对元素（天使↔魔鬼、祈祷↔敛财等）。自查：序列标注 + 成对元素计数。

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；3/5 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **全景叙事密度**（单帧叙事单元数）`[归纳]` | 1–2 个单元（单场景聚焦，如《死神与守财奴》） | 3–5 个单元（小群像 + 背景事件） | ≥8 个单元（Garden 中央板/地狱板级「编目」） | **60%** |
| P2 | **生物发明强度**（混合体数量与拼装复杂度）`[归纳]` | 0–1 个轻度混合（单处畸变） | 2–4 个混合体，各 2 类部件 | ≥5 个 + 成体系「物种表」（地狱板级） | **50%** |
| P3 | **尺度错乱度**（巨型化元素 vs 人体）`[归纳]` | 正常比例（写实档） | 1–2 个巨型元素（一个巨果/巨鸟） | 系统性巨型化（果实/动物/器物 ≫ 人） | **45%** |
| P4 | **道德对位结构**`[归纳]` | 单帧讽喻（一个罪/一个教训） | 二元对位（天使↔魔鬼、善↔恶成对） | 三幕全景（天堂—人间—地狱 + 帧内反转） | **70%**（三联档） |
| P5 | **直视目光/猫头鹰**`[归纳]` | 0（无人直视观众） | 1–2 处（含 1 只猫头鹰） | ≥3 处，含板缘成对猫头鹰 | **35%** |
| P6 | **色域明度**`[归纳]` | 土色为主（夜/地狱/单色底） | 混合（蓝绿 + 土色均衡） | 宝石亮色铺开（乐园/人间档） | **60%** |

> **用法**：P1/P2/P4 定「是不是博斯」（全景多事件 + 生物发明 + 道德对位；三条同时 ≥ 中档才成立）；P3/P5 定「奇想强度」（角色/场景设计时升档）；P6 定档期（夜/地狱↔乐园滑轨）。
> **分工注（与 §3.1 对齐）**：P6 一旦收窄为「土黑 + 白闪点」且 P1 降到单事件，即越界进入**戈雅**领域；P2 若退化为「单物种畸变」且无拼装部件，同样越界。组合实验按此判分。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 戈雅）**（× 戈雅；本卡 §3.1 分工条款）：怪诞两档写死：百科档（明亮/全景/编目/物种发明）vs 噩梦档（黑暗/单帧/在场）——判据五条；同轴不可分离，须分区/分帧、禁折中成「灰调怪物」
- **预判（vs 达利）**（× 达利（future）；本卡 §3.1 预判）：道德编码的物种发明（有系统/可解码）vs 梦境符号的自传化（反系统）——待达利入系统时写死
- **预判（vs 勃鲁盖尔）**（× 老勃鲁盖尔（future）；本卡 §3.1 预判）：发明新物种＋道德编目 vs 人群调度＋日常微观——「怪物设计」不得互抄
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影（博斯无戏剧光源）/ C-06 饱和度 / C-12 色相面积 / C-15 色数

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/bosch.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
