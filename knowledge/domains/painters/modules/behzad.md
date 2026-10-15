# 贝赫扎德 模块卡 — `behzad`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/behzad.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 11 条）

1. **层叠平面空间（无单点透视）＋建筑切分叙事**：消失点检验 ≈0；空间分区 ≥2 层；建筑剖面 ≥2 层、同建筑内事件 ≥2——空间读作时间
2. **微书级精度＋手抄本页整体设计**：织物/砖石/器物满布可读纹样；可读铭文/题记 ≥1；画面与书板/边框/书法共排版（单页/对开为设计单位）
3. **人物＝理想类型＋姿态/视线编排**：类型化面孔为主、情绪姿态 ≥1（低头/回首/伸手）；视线链 ≥3 跳（A 看 B、B 指向 C）
4. **克制色阶＋金点＋明度对比**：矿物色有限套色、大面积未图案化空场；金作点状强调（光环/器皿/边框、小且集中）；明度分层清晰组织前后与焦点
5. **「签名式」枯树曲枝＋题记嵌入物件＋叙事游戏性**：树少叶、枝呈锐角折线；签名/纪年藏于器物；与主叙事无关的嵌入细节 ≥1

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Behzad-style Persian manuscript illumination — a page from a deluxe Timurid book (Herat school, late 15th century):
a non-perspectival, layered space — flat planes stacked vertically, the ground line raised high,
parallel receding edges that never converge, no vanishing point;
architecture cut open as a section — a multi-storey palace or garden courtyard,
rooms and terraces readable one after another, doors and arches framing the episodes,
so that the sequence of chambers reads as a sequence of time;
small figures arranged by gesture and gaze — the eye led from figure to figure across the page,
idealized types with subtle moods, servants and courtiers choreographed in a ring;
sufis whirling, or workers on a scaffold, each face a type, each posture a note;
large unpatterned open areas for the subject to "dance around";
minute precision — textile patterns, brickwork, tilework and arabesque drawn at microscript scale;
restrained mineral palette — lapis, turquoise, ochre, cinnabar used sparingly,
gold only as pin-point accents (haloes, vessels, border rules);
ink outlines precise and controlled, no hatching for shading;
text panels in fine nasta'liq calligraphy integrated into the composition;
opaque watercolor, ink and gold on paper, ruled margins, illuminated headpiece
```
**负向约束（`--no` 风格）**
```
--no single-point perspective, converging lines, vanishing point, cast shadows from one light,
photographic depth of field, atmospheric haze, European easel composition,
oil-paint impasto, expressive brushwork for its own sake, cross-hatching, engraved line shading,
full-page saturated multicolor, photorealistic faces, individual psychological portraiture,
unintegrated empty text box, watermark, 3D render, anime, cartoon, modern clothing
```

## 代码艺术规则（§8.2 原样）

1. **无消失点规则**：全帧直线族中，平行后退线不得收敛——「消失点检验」= 0 组汇聚线（≥3 条线共点即失败）。自查：Hough 线检测 + 共点聚类。（依据：层叠平面空间 `[研究]`[R4][R6]）
2. **层叠分区规则**：画面须有 ≥2 个由建筑/台地/墙线切分的空间分区；事件点 ≥2 个分区（时间-空间转译可读）。自查：分区掩膜 + 事件对象计数。（依据：空间读作时间 `[研究]`[R1][R6]）
3. **人物比例恒定规则**：人物高度不随「纵深」缩放（上下位置变化 ≠ 大小变化）；同帧人物高度方差 ≤15%。自查：人体框高度统计。（依据：无透视纵深语法 `[研究]`[R4]）
4. **微书图案规则**：≥1 区域存在高频可读图案（砖/织物/瓷砖），图案频率高于全帧中位数；同时保留 ≥1 块「未图案化空场」（面积 ≥10%）。自查：高频能量图 + 空白区检测。（依据：微书精度 + 空场节奏 `[研究]`[R2][R4]）
5. **金预算规则**：金色（H 40–55°、S ≥0.5、V ≥0.7）面积 ≤5%，连通域 ≤7 个，每个须与「光晕/器皿/边框/宝座」之一相交。自查：HSV 掩膜 + 连通域。（依据：金只做点状 `[研究]`[R4]；计数口径按 C-15）
6. **色阶克制规则**：色相簇 ≤8；最大色相簇面积 ≥20%（主调存在）；高饱和（S ≥0.7）面积 ≤25%（无全帧高饱和铺底）。自查：色相直方图聚类。（依据：克制色阶 `[研究]`[R4][R12]）
7. **文本整合规则**：文本栏/题记 ≥1 处，且与画面构图相交（不悬浮于空白角落）；书法线条密度与图案密度同量级。自查：文本区域检测 + 位置校验。（依据：手抄本页整体设计 `[史料]`[R1][R6]）
8. **勾线无排线规则**：明暗由色块深浅与勾线表达；交叉排线交叉点密度 ≈ 0；轮廓线宽度全帧方差小。自查：方向场 + 线宽统计。（依据：赫拉特晚期勾线特征 `[研究]`[R2][R4]）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母 = 假想参考帧）；1–2 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **空间层叠度**`[归纳]` | 单层地面场景（前景-中景两带） | 2–3 层平面叠置（建筑/台地切分） | 多层剖面：内外景同框、同建筑多事件（《优素福》档） | **70%** |
| P2 | **建筑叙事强度**`[归纳]` | 自然景观为主，建筑作点缀 | 建筑框景、划分区域 | 建筑 = 叙事机器（多室/多层/门径序列） | **75%** |
| P3 | **微书细节密度**`[归纳]` | 简化表面（大色块） | 织物/砖石可读纹样 | 满页微书级图案（近观档） | **65%** |
| P4 | **色阶克制 / 金预算**`[归纳]` | 多彩多套色 | 矿物色有限套 + 点金 | 近单色阶 + 极少量金（克制档） | **55%** |
| P5 | **人群调度度**`[归纳]` | 1–2 人 | 小群像（3–7 人）姿态编排 | 群体场面（≥8 人，类型多样、视线链） | **50%** |
| P6 | **文本整合度**（工作流参数）`[归纳]` | 单页画（无文本） | 单页 + 题记/书板 | 全版面（文本栏 + 边框 + 画心一体设计） | **中档** |

> **用法**：P1/P2 定「是不是贝赫扎德」（层叠空间 + 建筑叙事；两条同时 ≥ 中档才成立）；P3/P4 定时期与气质（赫拉特精细档 → 晚年克制档的滑轨）；P5 定叙事（几人、什么关系）；P6 是版面参数（单页 vs 全版面，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **分工注（与 §3.1 对齐）**：P1 降为「弱」且画面转入「单点透视/光学景深」，即越界进入**塞尚/欧洲体系**领域；P2 为「强」且色与纹样同步升到满幅、姿态动势化，即越界进入**苏丹·穆罕默德**领域；P4 的「金」若升成面积性金饰，即越界进入**克里姆特**领域——组合实验按此判分。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款）：叙事图像两条路写死：手抄本多层空间＋群体调度＋微书＋诗行共排版 vs 版画平面剪影——判据四条，不得互相复制
- **分工（vs 苏丹·穆罕默德）**（× 苏丹·穆罕默德（future）；本卡 §3.1 分工条款）：同族错峰（先贝后苏）：静态平衡＋克制色阶＋空场 vs 动势旋转＋满幅色彩纹样——判据三条
- **缺口登记**（× 塞尚/丢勒/克里姆特；本卡 §3.1 缺口登记）：系统首个「无透视叙事空间」——不借几何深度/排线明暗/金饰密度（金只点状、按 C-15 单列 ≤5%）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合预检）：重点：C-16（金点≠高光，句式改写）/ C-17（空场 vs 留白口径）/ C-15（金层计数）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/behzad.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
