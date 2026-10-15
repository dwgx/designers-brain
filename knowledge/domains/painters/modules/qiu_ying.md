# 仇英 模块卡 — `qiu_ying`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/qiu_ying.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **勾线先行、匀称细劲**：衣纹「匀称线条」描法、轮廓连续、粗细变化克制——秀劲如「铁线／游丝」一系
2. **矿物重彩＋色不掩笔**：石青／石绿／赭石／朱砂大面积勾廓晕染（「浓烈大胆又清雅脱俗」）；石绿厚薄随墨皴配合、色墨咬合
3. **界画精密＋器物文玩密度**：楼阁栏杆「皆用界笔画成，精细入神」；琴棋书画、器皿古玩入画（主题「器用」20+ 项）——密度型精密
4. **长卷叙事＋仕女「仇派」**：可独立成幅的小场景组接、行进侍女串联；眉目清秀、体格纤细——「虽周昉复起，未能过也」
5. **敷色「艳而不媚」＋一稿多本**：色浓而和色多、对比靠色相组织；临摹「与真无异」、皆有稿本；金色仅作底材／细线点缀（无贴箔材质层）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
A Ming-dynasty Chinese gongbi heavy-colour painting in the qinglu (blue-and-green) manner, painted on silk: forms first defined by fine, even, continuously drawn brush outlines — slender figures, flowing drapery lines, and ruled-line architecture drawn with a straightedge; colour built from ground mineral pigments — azurite blue, malachite green, cinnabar red, ochre — laid in thin translucent washes that are layered and modulated, so that the ink outline stays visible beneath the colour (colour never buries the brush line); the silk ground subtly visible; a courtly garden or immortal landscape with ornate pavilions, balustrades, lattice doors and tiled roofs rendered with jiehua precision, ornamented rocks, willows, blossoming plum and peach, peacocks and mandarin ducks; slender, dignified court ladies with fine features and high chignons, attendants carrying fans, trays, musical instruments; objects of literati life — qin, weiqi boards, scrolls, antiquities, porcelain and bronze vessels — described in fine detail; composition as an episodic handscroll: several self-contained vignettes (flower-picking, dressing, music-making, portrait-painting) linked by figures walking or glancing across the scene; colours clear, rich yet harmonious — brilliant without vulgarity; brushwork meticulous yet fluent, never stiff; atmosphere serene, elegant, quietly luxurious; a connoisseur's copy after the Song academy manner, with the refined literati taste of the Wu School
```

**负向约束（`--no` 风格）**

```
--no metal leaf, gold foil, silver foil, metallic sheen or reflective surfaces, mosaic pattern blocks, ornamental flat fields pasted over the picture, western Art-Nouveau decoration, carved woodblock line quality, uniform knife-cut lines, flat colour-block printing, registration marks, ink-wash-only monochrome, sketchy xieyi brushwork as the dominant mode, heavy impasto, visible canvas weave, oil painting, chiaroscuro, cast shadows, photorealism, 3D render, neon, text, watermark, fake signatures, decorative frames
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **勾线连续与匀称** | 主体轮廓线连续率 ≥95%；线宽级差 p90/p10 ≤2.5（匀称）；收笔不虚断 | 骨架提取 + 线宽统计 |
| 2 | **青绿主色预算** | 石青/石绿家族色相占比 ≥25%（大青绿档）或 ≥10%（淡彩档）；青绿:赭朱面积比 ≥2:1（大青绿档） | 逐帧 HSV 色相聚类 |
| 3 | **色不掩线** | 色层下墨线可辨率 ≥80%（沿轮廓采样线/底对比） | 边缘检测 + 色区采样 |
| 4 | **界画直线度** | 建筑区直线段占比 ≥60%；主要结构线闭合（栏杆/檐口/门框） | 霍夫线检测 + 闭合度 |
| 5 | **细密密度** | 长卷档：可辨人物 ≥15 人/米（《汉宫春晓》114 人 / 5.74m ≈ 20 人/m）；册页档：3–10 人/页 | 目标检测 + 人工点算 |
| 6 | **渲染过渡带宽** | 单色块内部明度动态范围 5–25%（有层次，非平涂、非写实渐变）；色带过渡宽度 3–8px（绢本晕染尺度） | 局部明度剖面 |
| 7 | **器用密度** | 每 1000cm² 可辨器物（琴棋书画/器皿/文玩）≥4 件（长卷档） | 器物标注统计 |
| 8 | **运动预算（动画附加）** | 长卷平移展开 ≤2% 画幅宽/秒；人物微动帧间差 ≤0.5%；无突变转场；卷轴边缘稳定 | 帧差图 + 速度拟合 |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 `templates/style_card.md` 的填写规则对齐。署名合规：输出不得含文字/伪签名。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **青绿重彩强度**（Mineral Colour Intensity）`[归纳]` | 浅绛/淡彩——赭石为主、青绿仅点缀（《秋江待渡》档） | 青绿并用而清雅（《梧竹书堂》档） | 大青绿浓烈：石青石绿大面积勾廓晕染（《桃源仙境图》《仙山楼阁》档） | **65%**（本模块身份） |
| P2 | **勾线精密**（Outline Precision）`[归纳]` | 兼工带写、树石率笔（部分背景） | 常规工细：衣纹匀称、五官细线 | 寸人豆马级：小尺幅高密度（册页/长卷人物，「须眉毕具」[R34]） | **70%** |
| P3 | **界画密度**（Ruled Architecture Density）`[归纳]` | 点景楼台 1–2 处 | 楼阁数座、栏杆结构可循 | 宫苑建筑群体（《汉宫春晓》《仙山楼阁》档） | **60%** |
| P4 | **器物装饰细密**（Object & Ornament Density）`[归纳]` | 器皿 1–3 件 | 器物成组（琴棋书画+器皿） | 满密度：文玩、乐器、器皿、织物纹样成片（《汉宫春晓》档） | **55%** |
| P5 | **长卷叙事段数**（Scroll Episode Count）`[归纳]` | 单景/双景（挂轴、扇面） | 3–5 段（《清明上河图》节选、《浔阳琵琶》类） | 多段连续叙事（《汉宫春晓》14 段级；《清明上河图》全卷 987cm [R42]） | **50%** |
| P6 | **人物密度**（Figure Density）`[归纳]` | 点景人物 1–3（纯山水） | 人物组 4–15（故事画单页） | 群像 >30（《汉宫春晓》114 人 [R4]） | **60%** |

> 用法：**P1+P2 定「是不是仇英重彩档」**（青绿矿物色 + 匀称勾线；两条同时 ≥中档才成立）；P3/P4 定「精密密度」；P5/P6 切「册页/挂轴档 ↔ 长卷档」。
> **分工注（与 §3.1 对齐）**：**「金属箔贴面 + 装饰图案块 + 写实面孔对撞」整体属于克里姆特模块**，禁止在本模块同档出现——本模块的金色只能是颜料/金笺/细线；**「刻线等宽 + 套色平涂 + 无渲染」属于北斋模块**，不得以版画机制冒充工笔；**「无轮廓线色面 + 升目网格」属于伊藤若冲模块**。本注为 `[归纳]`。
> 数据来源：档位阈值为 `[归纳]`（本项目操作化建议，未经渲染实验校准）；特征观察取自 [R3][R4][R5][R6][R8][R9][R13]。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 克里姆特）**（× 克里姆特；本卡 §3.1 分工条款）：装饰金 vs 矿物重彩：材质系统不同——判据四条；「金色」来源二选一（金属箔 or 颜料／金笺），负向约束按 N1 重算
- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款）：精密线：工笔 vs 版画——判据四条（密度型 vs 图形型）；线轴、色轴显式分区
- **简表（vs 若冲 / 八大 / 齐 / 黄 / 丢勒）**（× 伊藤若冲 / 八大山人 / 齐白石 / 黄公望 / 丢勒；本卡 §3.1 简表）：东亚浓彩两端／工写两极／职业 vs 文人／「线的三种材质」（毛笔／铜版／木刻，同屏按 C-07 口径预检）——判据两式

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/qiu_ying.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
