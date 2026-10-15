# 苏丹·穆罕默德 模块卡 — `sultan_mohammed`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/sultan_mohammed.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 11 条）

1. **动势姿态**：偏轴 ≥30° 的人物 ≥1、事件性动势（奔／斗／坠／旋）——「比旁人更擅长描画奇兹尔巴什的仪态（ravish）」
2. **满幅色彩奢华**：色相簇 ≥6、高饱和 ≥35%、未图案化空场 ≤20%——矿物色平涂色场（青金／绿松石／朱红／橙／绿）
3. **平涂金天／金地**：金区明度动态 ≤5%（无光泽起伏）；金层 5–25%（金天档）或点缀；页缘大面积撒金
4. **拟人化岩山＋山体越框**：面孔／动物形嵌入岩山／云／水纹 ≥3 处；山石花木越出画心伸入页缘（名作档 3 侧）
5. **戏剧性预置＋微书细节＋署名嵌入**：预兆／指向装置 ≥1 与主体事件分离 ≥1/3 画面；织物／毛皮／水花可读；签名嵌入画内物件、文本栏与画心一体

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Sultan Muhammad-style Safavid miniature — a page from a royal Safavid manuscript (Tabriz, c. 1525–35):
a scene of courtly or mythic action at the height of Safavid color — lapis blue, turquoise, vermilion, orange, and leaf green
laid in flat, saturated pigment fields with no visible brushwork; a gold sky above, sprinkled gold across the page margins;
stacked planes and soaring mountains that break out of the painted frame into the margins on three sides;
rock formations, clouds and water animated with hidden faces and creatures — a lion's head, a horse, monkeys, dragons woven into the stone;
figures in leopard-skin robes and tall red Qizilbash turbans, whirling, galloping, gesturing — one figure points toward a distant event;
minute, jewel-like detail in textiles, fur, water and tilework; calligraphic text panels set into the page;
a drama quietly announced — a gaze, a gesture, a foreboding beneath the harmony;
opaque watercolor, ink, silver and gold on paper, gold-sprinkled borders, nasta'liq text panels
```
**负向约束（`--no` 风格）**
```
--no single-point perspective, converging lines, vanishing point, cast shadows from one light, chiaroscuro,
photographic depth of field, atmospheric haze, European easel composition, oil-paint impasto, visible brushwork,
metallic sheen, relief or texture on the gold, photorealistic faces, individual psychological portraiture,
restrained or muted palette, large empty unpatterned voids, watermark, 3D render, anime, cartoon, modern clothing
```

## 代码艺术规则（§8.2 原样）

1. **动势指数规则**：≥1 人物姿态偏轴 ≥30°（相对垂直轴）或画面含事件性动势（奔/斗/坠/旋）；全静场判失败。自查：姿态角度估计 + 事件计数。（依据：ravish 判据 [R14]；§3.1 轴①）
2. **满幅色彩规则**：色相簇 ≥6；高饱和（S ≥0.6）面积 ≥35%；未图案化空场 ≤20%。自查：色相直方图聚类 + 饱和度掩膜 + 空场检测。（依据：色彩奢华 [R1][R17]；§3.1 轴②）
3. **平涂金层规则**：金区（H 35–55°、S ≥0.5、V ≥0.7）为**平涂色面**——区域内部明度动态范围 ≤5%（无高光/光泽起伏）；面积 5–25%（金天档）或点缀档（≤5%）；金层单列、不计入色数上限（C-15/N6 接口）。自查：HSV 掩膜 + 区域明度方差。（依据：金天/撒金 [R1][R13]；vs 克里姆特判据①）
4. **拟人化岩山规则**：岩山/云/水纹中可辨面孔或动物形 ≥3 处。自查：局部区域目检（人检；模板匹配可选）。（依据：[R1][R9][R20]）
5. **无消失点规则（族征）**：全帧直线族中，平行后退线不得收敛——「消失点检验」= 0 组汇聚线（≥3 条线共点即失败）。自查：Hough 线检测 + 共点聚类。（依据：层叠平面 [R13][R18]；与贝赫扎德同侧）
6. **人物比例恒定规则（族征）**：人物高度不随「纵深」缩放；同帧人物高度方差 ≤15%。自查：人体框高度统计。（依据：无透视纵深语法 [R10][R18]）
7. **戏剧性装置规则**：画面含 ≥1 处「预兆/指向」装置——信号性手势（指向远处事件）、不祥凝视、局部异常（岩中脸/云中兽）；装置与主体事件的空间分离 ≥1/3 画面距离。自查：装置计数 + 位置校验。（依据：「on the brink of tragedy」[R13][R21]；AKM155「一人向上指洞穴」[R2]）
8. **文本整合规则（族征）**：文本栏/题记 ≥1 处，与画心同页一体（不悬浮）；书法线条密度与纹样同量级。自查：文本区域检测 + 位置校验。（依据：手抄本页整体设计 [R1][R12]）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母 = 假想参考帧）；1–2 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **动势指数**`[归纳]` | 全静场（端坐/静立为主） | 局部动作（奔跑/挥手/劳作，偏轴 <30°） | 旋转/飞扬/搏斗/坠落（≥1 处偏轴 ≥30° 或事件性动势） | **65%** |
| P2 | **色彩奢华度（矿物色域）**`[归纳]` | 收窄色域（≤4 簇，素净） | 5–7 簇（青金/绿松石/朱红/橙/绿） | ≥8 簇 + 高饱和铺陈（满幅） | **70%** |
| P3 | **满幅纹样密度**`[归纳]` | ≤10%（大色块为主） | 30–50%（织物/岩/花木成组） | ≥60%（满幅：锦袍、花木、砖饰、岩纹） | **65%** |
| P4 | **平涂金层面积与形态**`[归纳]` | ≤5%（点金/边框；近贝赫扎德档） | 5–20%（金云/金饰带） | ≥20%（金天/金地 + 撒金页缘；《古尤马尔斯》档） | **中-强 40%** |
| P5 | **拟人化景观密度**`[归纳]` | 0–1 处 | 2–5 处 | ≥6 处（「成百的面孔栖息于岩石」档） | **50%** |
| P6 | **版面整合度**（工作流参数）`[归纳]` | 单页画（无文本） | 画心 + 题记/文本栏 | 全版面（文本栏 + 撒金页缘 + 画心一体） | **中档** |

> **用法**：P1/P2/P3 定「是不是苏丹·穆罕默德（vs 贝赫扎德）」——三条中 ≥2 条 ≥ 中档才成立；P4 定「金层形态」（vs 克里姆特；平涂金彩档）；P5 定签名特征（拟人化岩山）；P6 是版面参数（单页 vs 全版面，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **分工注（与 §3.1 对齐）**：P1 降为「弱」且 P2/P3 同步收窄、空场增大，即越界进入**贝赫扎德**领域；P4 的金若出现光泽/材质（非平涂）或升成材质性金饰，即越界进入**克里姆特**领域；出现单点透视/光学景深 → 塞尚/欧洲体系；排线明暗 → 丢勒——组合实验按此判分。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 贝赫扎德）**（× 贝赫扎德；本卡 §3.1 分工条款（逐轴复读对齐））：同族错峰：动势＋色彩奢华 vs 静态平衡＋克制——判据三条；同侧项（层叠空间／页整体／无排线）无需改写
- **分工（vs 克里姆特）**（× 克里姆特；本卡 §3.1 分工条款）：装饰：细密画色（金＝平涂色面）vs 现代金（金＝金属材质）——判据三条；金层轴按 N3 单主、同屏分区（N4）
- **金层口径（接口登记）**（× C-15/N6；本卡 §3.1 金层口径）：平涂金彩 vs 金属材质量化分界建议（金区明度动态 ≤5% 平涂／≥10% 材质）——已登记、待 conflicts.md 回填
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合预检）：重点：C-15/N6 金层单列与声明／C-16 反约束适用域（「没有高光的平涂」句式改写）／C-17 空场口径／N3／N4

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/sultan_mohammed.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
