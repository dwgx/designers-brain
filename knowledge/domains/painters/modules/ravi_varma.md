# 拉维·瓦尔马 模块卡 — `ravi_varma`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/ravi_varma.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **舞台式场面（proscenium tableau）**：柱/幕布/墙等框景元素 ≥1、纵深 ≤2 层——「台下—台上」正对观看、人物按走位排列
2. **主角「亮相」姿态＋出画指涉**：正面/3/4 正面、目光出画 ≥1；动作定格于戏剧极值（高潮前一瞬）；叙事关键在画外（视线＋标题补全）
3. **类型化理想人体＋柔光象牙肤**：英雄/美人模板跨画复现；面部阴影边缘梯度平缓、暗部不黑（非 tenebrism）——光服务于识读
4. **图像志清晰化＋情感姿态语法（nayika/rasa）**：法器可逐件辨认、正面/近正面 ≥80%；每人物 ≥1 个语义手势
5. **织物珠宝「清单式」密度＋暖调底色＋复制友好**：每人物珠宝 ≥3 件、织物高光沿褶皱走向；赭/棕/红/金暖底、冷色点缀；缩印仍可读（oleograph-ready）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
a 19th-century Indian oil painting in the manner of Raja Ravi Varma:
a mythological scene from the Mahabharata or Ramayana, staged like a theatre tableau;
figures posed on a shallow proscenium-like stage, classical columns and heavy drooping
curtains framing palace interiors; the protagonist half-turned toward the viewer,
heroic gesture frozen at the climactic moment; smooth academic realism — idealized
figures, soft even lighting, gently modelled chiaroscuro, no harsh shadows; skin like
polished ivory; rich silk sarees and brocades with crisp heavy folds; dense gold
jewellery — necklaces, temple ornaments, armlets, earrings — rendered with tangible
weight; idealised faces with large expressive eyes, calm and readable; sentimental,
devotional and heroic mood; warm palette of ochre, deep red, saffron, gold, ivory and
pale blue with small cold accents; museum-grade finish, invisible brushwork,
oil on canvas
```

**负向约束（`--no` 风格）**
```
--no flat folk-art stylisation, miniature-painting flattening, woodblock print look,
single uniform keyline, cel shading, visible brush texture, impasto, sketchy strokes,
hard-edged black shadows, tenebrism, gore, photographic grain, modern clothing,
neon colours, cool colour grading, cubist distortion, collage, text, watermark,
cartoon, anime, 3D render, glowing highlights
```

## 代码艺术规则（§8.2 原样）

1. **光**：主光单侧或顶部柔光；面部阴影边缘梯度平缓（阴影边界过渡 ≥8px 的软边）；无硬边阴影块（边缘梯度 >15%/px 的阴影边界 = 0）；暗部明度不低于纯黑 +8%。
2. **对比度**：画面最大明度差 ≤70%（非 tenebrism）；面部最亮/最暗比 ≤2.5:1；背景与主体明度差 ≤35%。
3. **构图（舞台）**：背景框景元素（柱/幕/墙/拱）≥1 且占画面 ≥25%；纵深分层 ≤2；人物组重心位于下部 2/3；无 ≥3 条收敛于同一点的透视引导线。
4. **人物**：主要人物面部朝向正面或 3/4 正面（合计 ≥80% 人物）；主角视线方向 = 出画（对观众）或对情节点 ≥1 处；理想化比例（头身 1:7.5–8，肩宽/头宽比 ≥2.2）。
5. **服饰珠宝**：每主要人物可辨珠宝件数 ≥3（项链/耳饰/臂钏/戒指/头饰）；织物高光带沿褶皱方向分布（≥3 条连续高光带/人物）；褶皱线条 ≥5 条/人物。
6. **手部语义**：每手一个可命名动作（持物/指示/合十/扶额/叉腰）；手部尺寸偏小（手长 ≤脸长 ×1.1）；避免强烈透视缩短（前缩手指数量 ≤1）。
7. **叙事结构**：取「高潮前一瞬」——画面含 ≥1 个可命名的双层动作（如「借口拔刺、实则回眸」）；画外指涉（视线出画）与标题共同补全叙事 ≥1 处。
8. **复制适配（P6=强时）**：缩至 256px 宽时主要人物 ≥2 可辨；轮廓闭合（主要人物外轮廓无断裂）；色块化后（8 色量化）人物与背景分离度 ΔE ≥ 20。

> 口径：以上 8 条为 `[归纳]`——从作品与资料归纳的**未实测参数**；实测偏离即以实测分布修正（见自审 D）。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **舞台调度度**`[归纳]` | 单/双人肖像式（背景留白或纯色） | 2–4 人小组 + 道具，浅背景 | ≥5 人群像 + 柱/幕全景（Baroda/Mysore 级） | **70%** |
| P2 | **理想化/类型化**`[归纳]` | 观察性肖像（个体特征优先） | 家庭/日常场景美化（柔化个体） | 神祇/英雄类型（理想脸 + 类型身） | **75%** |
| P3 | **光戏剧性**`[归纳]` | 平光（白天记录档） | 柔窗光单侧（肖像档） | 夜色/月光/火光单光源（Radha 型） | **45%** |
| P4 | **服饰珠宝密度**`[归纳]` | 素色简装（速写档） | 纱丽 + 少量饰物（日常档） | 锦缎 + 全套珠宝「比人闪」（宫廷/神像档） | **65%** |
| P5 | **图像志正面性（达显）**`[归纳]` | 叙事侧身（故事优先） | 3/4 面向（叙事与识读兼顾） | 完全正面 + 法器清单（礼拜像 / 印刷档） | **55%** |
| P6 | **复制适配度**（工作流参数）`[归纳]` | 私密速写/草图（不进复制） | 展览油画（复制需再设计） | 印刷用正面构图（缩印可读、轮廓清晰） | **60%** |

> **用法**：P1/P2 决定「是不是拉维的场面」；P3 决定「白天↔夜色」；P4 决定「宫廷↔日常」；P5/P6 决定「叙事画↔达显像」——印刷档（P5 强 + P6 强）即 Press 图像志。
> **分工注（与 §3.7/§3.8 对齐）**：P3 一旦转入「硬边明暗切割 + 画内无光源」，越界进入卡拉瓦乔域；P2 弱 + P3 中但画面转入「单张脸连续衰减」，越界进入伦勃朗域；P2 弱 + 个体凝视 + 后印象派色，越界进入谢尔吉尔域——组合实验按此判分。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 欧洲学院派线）**（× 卡拉瓦乔/伦勃朗/维米尔/达·芬奇；本卡 §3.7 分工条款）：技术输入→本土化转译：柔光均匀化（识读与礼拜）vs 硬光开关/心理光斑/光学室内——不得同时上「硬光开关」与「达显正面性」（N1 重算）
- **分工（vs 谢尔吉尔）**（× 谢尔吉尔（future）；本卡 §3.8 分工条款）：民族图像两档：复制＋标准化神祇＋礼拜凝视（darshan）vs 独幅＋个体观察＋现代主义凝视
- **分工（vs 北斋）**（× 北斋；本卡 §3.9 简表）：大众印刷两路：石版彩印（明暗渐层＋套色）vs 木版（等宽线＋平涂＋留白）——判据两式
- **组合预检（Lane B）**（× Lane B；本卡 §3.9 组合预检）：重点：C-01（柔光、禁硬边）/ C-05（表面平滑、无可见笔触）/ C-07（印刷 vs 油画表面两分）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/ravi_varma.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
