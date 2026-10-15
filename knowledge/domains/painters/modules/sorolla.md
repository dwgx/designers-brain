# 索罗拉 模块卡 — `sorolla`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/sorolla.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **白上加白**：白衣／白帆／白墙／浪花同屏 ≥3 种色温的白；白区内部可检出蓝、紫、绿、玫瑰色斑——「没有一种完全的白」
2. **正午顶光／高照度**：光源在画面上方；亮部占比大、暗部短促且有色（紫罗兰，非黑褐）——「我恨黑暗」
3. **长笔触＋亮部厚涂**：主体一笔成型（不碎、不分解）；亮部堆到纯铅白收尾；近处笔触长、远处转 crisp 小触
4. **紫罗兰阴影＋橙／桃反光＋反光网**：阴影用紫／蓝紫；湿皮肤、湿沙高光旁放橙／玫瑰／丁香；画面是反射的网（船帮／头巾／鱼／湿背）
5. **摄影式裁切＋运动定格＋边缘开放**：人物／阳伞／船被切断、俯视感；动作停在发生中；轮廓向相邻色面打开、消解景深

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
oil painting in the style of Joaquín Sorolla, Spanish luminism,
painted en plein air under direct midday Mediterranean sunlight,
high-key high-illumination scene with a blazing white-on-white core:
white sails, white clothes, sea foam and wet sand in several distinct
white temperatures; luminous whites tinted with blue, violet, rose
and pale green; violet and mauve shadows instead of black or brown;
long confident bravura brushstrokes laid in one pass, thick impasto
in the lights, crisp small touches only in the distance; water and wet
surfaces sparkling with broken reflections; orange and pink reflected
light on sunlit wet skin; high viewpoint, snapshot cropping, square or
wide format, sky reduced or cut off; figures caught mid-motion
(running, bathing, hauling nets), cheerful everyday beach life;
palette: lead white, cobalt blue, ultramarine, Prussian blue,
emerald green, chrome yellow, vermilion, rose, violet
```

**负向约束（--no）**
```
dark brown or black shadows, chiaroscuro, tenebrism, black outlines,
grey rainy weather, fog or atmospheric haze envelope, twilight or night,
muted desaturated palette, smooth blended gradients, photographic realism,
3D render, studio lighting, hard vector edges, symmetrical centred
composition, HDR, watermark, text
```

## 代码艺术规则（§8.2 原样）

1. **高调与去黑规则**：全画平均明度 ≥72%（0–100）；纯黑像素（明度 <6%）占比 ≤0.3%；暗部色相偏蓝紫（H 230–290°）。自查：直方图 + 暗部色相统计。
2. **白色分层规则**：白区（L ≥90%）内检出 ≥3 个色相簇（簇间色相间隔 ≥15°），每簇面积 ≥2%；白区整体明度动态范围 ≤8%（白上加白 = 高明度窄域 + 色相变化）。自查：白区色相聚类 + 明度范围。
3. **光照方向规则**：亮部重心与设定光源方位差 ≤30°；阴影长度 ≤ 人物高度 25%（正午短影）；阴影过渡带宽度 ≤4% 画面短边。自查：明度梯度方向场 + 阴影测量。
4. **笔触层级规则**：可见笔触覆盖率 ≥85%；近景笔触长度 ≥40px、远景 ≤12px（存在长度梯度）；亮部边缘粗糙度 ≥ 暗部的 1.3 倍。自查：边缘密度图分区 + 纹理能量。
5. **反光语法规则**：水面/湿表面闪点密度 ≥6 个/100×100px（L ≥97% 高光点）；湿表面区色相与相邻环境（天空/衣物）相关性 ≥0.5。自查：高光点计数 + 色相相关。
6. **构图规则**：地平线 ≥ 画高 55% 或不可见；存在 ≥1 条水平带（海/沙/滩）；主体被画框裁切（≥1 处触边）；无中心对称。自查：水平线检测 + 对称度。
7. **运动规则（动画）**：水/浪/衣裙位移 ≤3 px/帧；光斑闪烁周期 0.5–1.5 s；天气恒定（禁止雨/雾/阴切换）；人物动作幅度小（定格瞬间，不做「物体级」叙事）。自查：帧间光流 + 状态机检查。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **日照强度（照度感）**`[归纳]` | 薄云漫射光（亮部峰值 ≤85%，阴影软） | 明朗阳光（亮部 90–95%，阴影短） | 正午炽烈（亮部 ≥97% 纯白峰值、眩光感、阴影极短） | **75%** |
| P2 | **白色分层度（白上加白）**`[归纳]` | 白区 1–2 档色温（灰白+暖白） | 3–4 档（暖白/冷白/玫瑰白） | ≥5 档 + 白区内部色斑（蓝/绿/黄/紫满配，《Saliendo del baño》档） | **70%** |
| P3 | **笔触长度/速度感**`[归纳]` | 中短笔触收敛（早期档） | 可见长笔触 + 局部短触 | 大长笔一笔到位 + 飞白/拖痕（大画如速写，《渔获归来》档） | **75%** |
| P4 | **反光色比（紫罗兰/橙粉）**`[归纳]` | 灰调阴影（早期社会题材档） | 紫灰阴影 + 局部玫瑰反光 | 紫罗兰阴影 + 橙/桃反光全开（湿皮肤/湿沙/浪尖） | **65%** |
| P5 | **构图裁切强度（摄影感）**`[归纳]` | 完整构图、地平线可见 | 轻微裁切 + 高视点 | 强裁切/方画幅/无天空（瞬间感，《La hora del baño》档） | **55%** |
| P6 | **色彩去黑度（外光纯度）**`[归纳]` | 含褐黑（室内/肖像档） | 黑基本清除、蓝紫出现 | 全外光色域（无黑褐；白+蓝紫+黄红+绿松石） | **80%** |

> **用法**：P1 + P2 定「是不是索罗拉」（两条 ≥中档才成立）；P3 + P6 定「户外档 vs 肖像档」；P4 定「正午档 vs 黄昏档」；P5 是构图旋钮（与摄影感绑定）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若出现统一雾色/大气色收拢、远景对比 ≤60% → 越界**莫奈**档（或透纳档）；② 若色板收窄为四色封闭、白色只剩单档、光转为北窗受控 → 越界**佐恩**档；③ 若暗部塌陷近黑、画外单光源、高光只落脸/手 → 越界**卡拉瓦乔**档；④ 若空间压平、取消中间调、笔触转平面组织 → 越界**马奈**档（future）；⑤ 若出现雨/雾/风暴等天气事件 → 越界**透纳**档。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 莫奈）**（× 莫奈；本卡 §3.1 分工条款）：氛围光 vs 直射光：光机制／阴影／笔触／时间四轴＋判据四条；包络轴单主（莫奈 P3 只许弱档）
- **分工（vs 佐恩）**（× 佐恩；本卡 §3.1 分工条款（互查对齐））：阳光白 vs 有限色板：色板／白色角色／光机制／题材四轴＋判据四条；色板宽度轴单主
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 笔触／C-09 运动预算／C-12 色相预算

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/sorolla.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
