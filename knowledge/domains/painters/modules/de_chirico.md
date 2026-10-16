# 德·基里科 模块卡 — `de_chirico`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/de_chirico.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **空旷广场＋舞台正面性**：大面积石铺前区（常 ≥25% 画面）＋围合建筑＋高地平线；近剧场布景的正面/中心透视、真人 ≈0——「De Chirico's quiet square」、等一场不会发生的事件
2. **超长投影**：低角度日光拉出被拉长的硬边投影（影/物高比常 ≥3）、横贯铺地、跨越画面、本身是构图主角——「dead patches of sun and dire shadows」
3. **古典建筑构件＋雕像/人体模型**：拱廊/柱廊/砖塔/三角楣/钟表；石膏像、无头躯干、影子——「人的在场」以非人形式出现（plaster casts … symbols of the human presence）
4. **封闭透视＋黄昏调色板＋硬边**：消失点被墙/建筑/影封堵（无出口）；赭黄/砖红/深绿/藏青平涂、天空常为翠绿或深蓝绿——「emerald green for the sky」；轮廓明确（heavy black outlines）
5. **无事件＋谜式并置＋时间物件**：没有动作与叙事高潮；不相干物同框且无叙事连接（橡胶手套/饼干/洋蓟/绿球）；火车/钟表/日晷被物件化——「atmosphere of mystery and enigma」

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
Metaphysical painting of an empty Italian piazza on a late autumn afternoon: a wide stage-like
square of warm ochre stone paving, enclosed by classical arcades, long colonnades, high walls
and a red-brick tower; the perspective sharply recedes and is closed off by a wall or a silent
building — no way out; an extremely long, hard-edged cast shadow, cast by a statue or an unseen
object at a low sun angle, stretches across the pavement, its length several times the height
of its source; a white plaster statue or a headless tailor's dummy stands on a low plinth; a
stationary steam train shows only a solid white plume of smoke above a wall; a clock on the
arcade; a few enigmatic objects — a rubber glove, biscuits, artichokes, bananas, a green ball —
juxtaposed without any narrative connection; palette of brick red, ochre, deep green and dark
blue-green, emerald-green sky; crisp outlines, flat matte volumes, no visible brushwork; zero
people, absolute stillness, silence, a faint sense of unease and enigma; slightly theatrical
staging as if the square were a stage; oil on canvas, early 20th century, Italian metaphysical
painting
```

**负向约束（`--no` 风格）**

```
--no modern city, neon signs, billboards, glass storefronts, night electric light pools,
street lamps glowing, crowds, people interacting, visible motion, action, melting clocks,
deformed bodies, double images, dream monsters, psychedelic colours, heavy impasto, visible
brushstrokes, impressionist broken colour, sfumato, soft diffused light, pointillism,
photorealistic detail, tourists, picturesque postcard, warm nostalgic glow, anime, 3D render,
text, watermark, signature, fake signature
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **超长投影** | 主投影长度 ÷ 投影源高度 ≥2.5；投影边缘过渡带 ≤2 px；投影方向直方图主峰 ±5° 内占比 ≥80%（允许 ≤1 处矛盾影） | 投影主轴角度直方图 + 长度比测量 |
| 2 | **人烟预算** | 真人连通域 = 0（若出现 ≤1 且面积 ≤2%、无视线交汇）；非人形体（雕像/模型/影子）1–3 个 | 人物检测 + 面积与视线向量检查 |
| 3 | **古典构件** | 拱/柱/塔/墙/三角楣 ≥4 类；现代构件（玻璃幕墙/霓虹/现代招牌/车辆）像素占比 ≤0.5%；画面内可读现代文字 = 0 | 构件分类检测 + 文字检测 |
| 4 | **封闭透视** | 单点透视：消失点位于画内建筑/墙之上或被其覆盖（不可达画外）；地平线高度 30–55%；≥2 条透视线收束角误差 ≤5° | 直线段霍夫变换 + 消失点拟合 |
| 5 | **色域与平涂** | 色相簇 ≤8；砖红+赭+深绿+蓝绿四族合计 ≥60%；平均饱和度 ≤0.45；荧光/霓虹色（S ≥0.7 且 H ∈[160,200]∪[300,340]）≤1%；单色块内部明度标准差 ≤6% | 逐帧 HSV 直方图 + 色相聚类 + 块内方差 |
| 6 | **硬边** | 明暗/影边界过渡带中位数 ≤2 px（1024 px 宽画布）；无 ≥8 px 羽化；影块为简单多边形（边数 ≤6） | 梯度宽度统计 + 形状简化度 |
| 7 | **静默（动画附加）** | 相机固定；帧间差 ≤1%；允许运动仅蒸汽/云 ≤0.5%/s 漂移（或全静止） | 帧差图 + 漂移拟合 |
| 8 | **舞台构成** | 前区铺地（下缘 1/4 高度带）为空 ≥25% 画面；≥1 个画中框（拱/门/墙洞）或被画边裁切；主体建筑中轴偏移 ≤1/6 画宽 | 分区覆盖统计 + 边界相交检测 |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 `templates/style_card.md` 的填写规则对齐。第 1/2/3 条与 §3.1 判据③④①同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **投影拉长度**（Shadow Elongation）`[归纳]` | 投影短、接近正午光（早期 1910 档） | 明显斜长影、方向基本一致 | **超长投影横贯画面**，长/源高 ≥3，边缘刀切，可局部矛盾（本模块身份） | **85%** |
| P2 | **空旷度/人烟预算**（Emptiness & Figure Budget）`[归纳]` | 2–3 个剪影式人形在场 | 0–1 真人 ＋ 1–2 雕像/模型 | **真人=0**，仅雕像/人体模型/影子（≤3 个非人形体） | **80%** |
| P3 | **古典构件密度**（Classical Vocabulary）`[归纳]` | 1–2 个古典元素点缀 | 拱廊/柱/塔/墙成组（3–4 类） | 满构古典舞台：拱廊＋雕像＋高墙＋塔（≥5 类构件） | **70%** |
| P4 | **透视封闭度**（Closed Perspective）`[归纳]` | 开放地平线、透视通向画外 | 部分被建筑遮挡 | **消失点被墙/建筑封堵**（无出口），透视可局部矛盾 | **75%** |
| P5 | **意大利黄昏色档**（Italian Dusk Palette）`[归纳]` | 冷灰/单色（素描与版画档） | 赭＋深绿为主、天空蓝绿 | **砖红＋赭黄＋深绿＋藏青**四族高纯度平涂、翠绿天空（谜之日档） | **70%** |
| P6 | **静默/无事件强度**（Silence / No-Event）`[归纳]` | 有轻微动作迹象（烟/旗） | 凝固瞬间、无事件进行 | **绝对静止**：无风无动作，蒸汽/云呈固体状，时钟静止 | **80%** |

> 用法：**P1＋P2 定「是不是德·基里科」**（超长影＋无人；两条同时 ≥中档才成立）；P3/P4 定「舞台感」（古典构件＋封闭透视）；P5 切「黄昏档/素描档」；P6 是「不安」的来源（越低越平静、越高越凝固）。
> 数据来源：档位阈值为 `[归纳]`（本项目操作化建议，未经渲染实验校准）；特征观察取自 [R16]–[R37]。
> **分工注（与 §3.1 对齐）**：P1 强档（超长影）＋P2 强档（真人=0）＋P3 古典构件是本模块专属；**「霓虹/现代招牌/玻璃橱窗/夜光池」组合整体属于霍珀模块，禁止在本模块同档出现**——需要城市感时不得同时保留本模块的「古典构件＋超长影」标志机制（见 §3.1 与 §8.1 越界警报）。**「变形/双图像/融化物」属达利模块（预写）**——不得在本模块出现。本注为 `[归纳]`。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 霍珀）**（× 霍珀；本卡 §3.1 分工条款（空城两型））：古典广场/超长投影 vs 现代都市/人造光——五轴判据（建筑语汇／光源性质／投影行为／人烟人物／空间取景）；组合默认二选一，同屏须显式分区
- **分工（vs 达利）**（× 达利（future）；本卡 §3.1 预写条款）：形而上空间 vs 梦境奇观——四判据（变形/双义／人物戏剧／空间／情绪）；本档禁「变形/双图像/融化物/梦境怪物」；达利卡产出后回填对齐
- **次级注记（vs 皮耶罗 / 弗里德里希）**（× 皮耶罗·德拉·弗朗切斯卡 / 弗里德里希；本卡 §3.1 次级注记）：几何秩序两档（数学化空间＋有人物叙事 vs 舞台谜题＋无人）／静默两档（自然崇高/背影凝视 vs 城市广场/无人）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影／C-12 色相预算／C-17 负空间

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/de_chirico.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
