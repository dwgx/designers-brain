# 德加 模块卡 — `degas`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/degas.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **偏心裁切（「照片式裁剪」）＋高视点俯视**：主体重心偏离画面中心 ≥15% 画宽、≥1 个主要人物或道具被边缘切割；视平线 ≥55% 画高、地板透视收敛
2. **背面与转身视角**：焦点人物背对/侧背 ≥1/3、五官可辨度低——「看而不被看见」
3. **舞台/室内人工光**：脚灯/顶灯/排练室窗光/煤气灯——光有来源与方向；亮部集中 ≤35%、暗部成剪影、纱裙高亮
4. **粉彩层叠与方向性笔触＋线条优先**：排线/擦揉/多层覆盖 ≥70%、方向族 2–5；边缘梯度 ≤1% 短边（与印象派「边缘溶解」相反）
5. **职业劳动的真实瞬间＋重复变体＋过程可见**：排练/候场/系带（非表演状态、锁孔视角）；同一构图家族 ≥2 变体；未覆盖底子 ≥5%、拼接/覆盖痕迹

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Degas-style snapshot of indoor modern life — the frame used like a viewfinder, not a stage:
a rehearsal room or theatre interior under visible artificial light — footlights, ceiling lamps or a high studio window;
the viewpoint slightly above, tilted down along the diagonal of the room, the floorboards converging in sharp perspective;
figures placed along a diagonal, off-centre, cropped by the frame — an arm, a skirt or a whole dancer cut by the edge;
dancers in rehearsal or at rest rather than performing: adjusting a ribbon, tying a shoe, rubbing a tired muscle, stretching, waiting;
several figures seen from behind or in profile, faces barely readable, no eye contact with the viewer;
the light concentrated in a few passages — white tulle, skin, the sheen of the floor — the rest falling into warm shadow, silhouettes allowed;
pastel over monotype or charcoal: visible hatched strokes, rubbed and layered colour, edges kept crisp by drawing, the creamy ground showing through in places;
warm ochre, umber and brown floor against cool white, blue and grey tutus; a single red or orange accent (hair, fan, dress);
asymmetrical balance, unfinished corners, the feeling of a moment caught between two others;
palette: ochre, burnt sienna, umber, black, white lead, pale blue, viridian, touches of vermilion;
painterly, drawn, professional and unposed — a working moment, not a spectacle
[sculpture variant] wax-like small figure, natural stance mid-motion, tinted bronze surface, real cloth tutu, plain wooden base
```
**负向约束（`--no` 风格）**
```
--no plein-air natural light, atmospheric envelope, fog, soft dissolving contours, sfumato, no-outline merge,
uniform pointillist dots, optical colour mixture, scientific colour system, geometric freeze, hieratic frontal pose,
single outside light source with near-black background, spotlight on face only, glossy varnish, smooth gradients,
idealized classical nude, sculptural heroic anatomy, symmetrical centred composition, full uncropped figures,
stage-front ballet glamour, tutus in perfect rows, smiling faces turned to viewer, dramatic theatrical lighting from the front,
impasto energy fields, complementary-colour vibration over the whole canvas, decorative gold, text, cartoon, 3D render, photographic realism
```

## 代码艺术规则（§8.2 原样）

1. **偏心裁切规则**：画面主体（最大人物簇）重心偏离画面中心 **≥15% 画宽**；**≥1 个**主要人物/道具被画框边缘切割；对角元素（地板线/台边/谱架）横跨 ≥60% 画宽。自查：质心计算 + 边缘切割计数 + 直线检测（Hough）。（依据：[R9] NGL「asymmetrical composition cropped at the lower right」；[R3]「read as snapshots」）
2. **高视点地板规则**：视平线 ≥55% 画高（俯角 10–25°）；地板/工作平面占 ≥20% 面积；地板线族 ≥3 条向消失点收敛。自查：消失点估计 + 区域分割。（依据：[R4] Orsay「légère plongée…diagonale de la pièce」；Valéry 地板句）
3. **人工光规则**：存在方向性光源（亮暗分界夹角 ≤45°）或可见光路（脚灯排/窗光/灯罩）；亮部（V ≥0.9）集中面积 ≤35%；允许人物成剪影（暗部占比 ≥30% 时脸/手仍可读 ≥1 处）。自查：亮度直方图 + 光源检测。（依据：[R6] Shop-Talk「show the effect of the lighting」；[R3][R4]）
4. **背面/转身规则**：焦点人物（面积前 3 位的人形）中背对或侧背（面部关键点不可辨）**≥1/3**；直视观众的面孔 ≤1/3。自查：人脸关键点检测 + 姿态估计。（依据：[R1]「turned away from us」；[R10] keyhole）
5. **粉彩笔触规则**：可见笔触覆盖 ≥70%；方向族 **2–5 个**（方向场直方图主峰数）；平滑渐变带宽度 ≤2% 短边（禁 sfumato）；可见色层 ≥2（叠色痕迹）。自查：边缘方向场 + 渐变带检测 + 色彩层分析。（依据：[R1] Ukrainian「thickly with repeated strokes…layered」；[R3]「complex layers and textures」）
6. **失衡姿态规则**：至少 1 个人物处于「过程态」——重心投影偏离支撑面 ≥10% 身高（或单点支撑/悬吊，如《拉拉小姐》）；肢体非对称伸展（左右臂展差 ≥20%）。自查：姿态估计 + 支撑点计算。（依据：[R12] Met「ungainly poses」；[R2] 悬吊）
7. **序列/变体规则**（工作流参数）：同一构图家族（同一姿态/机位/房间）**≥2 变体**可对读；单帧发布时以「家族编号+变体序号」标注。自查：构图相似度聚类（结构相似性 SSIM ≥0.6 归族）。（依据：[R1]「repetition is exactly what the dancers do」；[R3]）
8. **未完成/过程规则**：可见未覆盖底子（纸/布底）≥5% 面积；允许拼贴/覆盖/重描痕迹；禁「全画均匀收尾」（四角与中心完成度差异 ≥1 档）。自查：底材色检测 + 完成度热力图。（依据：[R1] Combing「look unfinished」；Ukrainian「added a strip of paper」）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **抓拍裁切强度**`[归纳]` | 完整构图、主体居中、无切割（早期肖像/历史画档：《贝列里一家》） | 偏心构图 + 1–2 处画框切割（《舞蹈课》档） | 极端裁切 + 高视点 + 对角切入（《拉拉小姐》《浴女》档——「照片式裁剪」） | **70%** |
| P2 | **瞬间失衡度**`[归纳]` | 静止平衡姿态（肖像/浴女端坐档） | 日常动作（系带、擦背、拉伸——「非表演状态」） | 动作中途/失衡瞬间（arabesque、跃起、仰身平衡——《拉拉小姐》档） | **60%** |
| P3 | **人工光强度**`[归纳]` | 均匀漫光（排练室白天档） | 明确方向光 + 局部光斑（窗光/顶灯档） | 舞台脚灯：亮部集中、人物成剪影、地板反光（《罗贝尔恶魔》/《舞台上的排练》档） | **55%** |
| P4 | **粉彩层叠度（媒介参数）**`[归纳]` | 单层薄涂/独幅版画单色（monotype 原印档） | 多层排线 + 局部擦揉（中期粉彩档） | 厚层覆盖 + 刮擦 + 固定剂后再叠（晚期「火焰」档：《梳头》/乌克兰舞者） | **65%** |
| P5 | **背面/转身比例**`[归纳]` | 全正面肖像（肖像档） | 部分人物背对/侧背（《蓝色舞者》档） | 多数人物背对观众、面部不可辨认（《浴女》/候场档——「看而不被看见」） | **55%** |
| P6 | **系列/变体幅度**（工作流参数）`[归纳]` | 单幅（1 张） | 同一母题 3–8 变体（舞蹈课/蓝色舞者） | 同一姿态 20+ 变体 + 跨媒介重做（芭蕾全集；monotype→粉彩；蜡像→铜） | **2**（小幅变体起步） |

> **用法**：P1/P2/P5 定「是不是德加」（三条中 ≥2 条 ≥ 中档才成立）；P3/P4 定时期与媒介档（早期油画→中期粉彩→晚期厚层）；P6 是组稿参数（单幅 vs 变体群，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若「光」变为**无源自然光 + 大气包络**、边缘溶解、系列变量为时刻/天气 → 越界进入**莫奈**档；② 若笔触变为**均匀点阵 + 补色光学混合**、人物几何化定格 → 越界**修拉**档；③ 若出现**画外单光源 + 近黑背景 + 高光只落脸/手/道具** → 越界**卡拉瓦乔**档；④ 若人体变为**理想化力量裸体 + 雕塑式完成态** → 越界**米开朗基罗**档。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 莫奈）**（× 莫奈；本卡 §3.1 分工条款）：光与序列两条路写死：人工/室内光＋轮廓保持＋姿态机位变量 vs 自然光＋边缘溶解＋时刻变量——四轴判据，同用选主导轴（70/30）
- **分工（vs 修拉）**（× 修拉；本卡 §3.1 分工条款）：颗粒与瞬间：方向性粉彩手势层叠＋抓拍失衡 vs 点阵光学混合＋去瞬间——四轴互斥（同用须分区/取值）
- **分工（vs 米开朗基罗）**（× 米开朗基罗；本卡 §3.1 分工条款）：G11 定义句：抓拍瞬间（被截断的过程态）vs 雕塑式定格（完成态）；非理想化 vs 理想化
- **备查互引**（× 喜多川歌麿 / 佐恩（future）；本卡 §3.1 备查）：歌麿「定格美 vs 抓拍」、佐恩「蚀刻：不同目标」——对方入系统时生效
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 笔触 / C-08·C-09 运动预算 / C-12 色相预算

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/degas.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
