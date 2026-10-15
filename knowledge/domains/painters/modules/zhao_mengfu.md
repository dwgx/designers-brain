# 赵孟頫 模块卡 — `zhao_mengfu`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/zhao_mengfu.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **以书入画（线是「写」出来的）**：石用飞白、树用篆籀、竹用八法；同一线内线宽 ≥2 倍变化、线端起收有锋——「书画本来同」
2. **飞白＋干笔**：石面／枯干干笔疾扫、丝缕露白；渴笔、墨色层次 3–5 级、笔触独立可辨——「用笔千古不易」
3. **古意青绿＋简率近古**：空勾少皴＋石青石绿敷染、色不掩笔；形简神完——「似乎简率，然识者知其近古」
4. **平远为主＋点景微小**：水泽坡岸横向展开、地平线低；渔舟／屋舍／人物 ≤ 树高 1/5——压缩实际距离的装饰性空间
5. **唐风鞍马＋款印系统**：工笔设色、线描圆润秀劲「犹如篆籀」；款「子昂」＋朱文印常见组合、题跋层层叠加

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Yuan-dynasty literati painting in the manner of Zhao Mengfu (趙孟頫, 1254–1322):
brush-written lines where every stroke is visibly written, not drawn — pressure-sensitive
calligraphic linework with clear entry and exit strokes, feibai (dry-brush "flying white")
streaks in rocks and old tree trunks, seal-script (zhuanshu) brushwork in tree forms, bamboo
leaves flicked in the eight basic brush methods; rocks outlined with flying-white sweeps and
almost no texture strokes; sparse, "plain and ancient" (guyi) composition on a wide level
expanse of water and low banks; pale blue-green mineral washes (shiqing shilv) laid thin so
color never hides the brush, optionally mixed with light ochre wash and ink; trees as crisp
groups — willows as hanging line-clusters, pines with needle clumps, bare old trees with
twisted calligraphic trunks; tiny point-scenery (a fishing boat, a hut, a bridge, one or two
figures) at less than one-fifth tree height; paper breathing with generous empty water;
restrained and dignified, archaic elegance without sweetness; a modest column of calligraphy
and a red seal (趙氏子昂) close the composition
```
**负向约束（`--no` 风格）**
```
--no uniform-width outlines, printed or engraved linework, crosshatching, stipple shading,
dense parallel hatching, hard-edged black contours, filling-in of flat color blocks, opaque
thick mineral paint, saturated or sweet color, glossy sheen, oil impasto, photorealistic or
3D rendering, western single-source lighting, chiaroscuro, cast shadows, vanishing-point
perspective, symmetrical centered composition, crowded full-bleed detail, decorative
pretty-prettiness, exaggerated or distorted figures, carved-seal stiffness without brush
movement
```

## 代码艺术规则（§8.2 原样）

1. **书写性线质**：主体元素轮廓线中，同一线内线宽变化 ≥2 倍的比例 ≥30%（提按证据）；线端见收锋/顿挫（端点切线角突变 ≥30° 或线宽先增后减）；等宽描线（线宽变化 ≤30% 且长度 >10% 画幅）比例 ≤10%。
2. **飞白与干笔**：石面/枯干区域中，笔画内出现「露白丝缕」（亮线穿插于墨线内部，宽度 ≤ 线宽 40%）的笔画占比 ≥20%；墨色层次（明度直方图可分辨带）≥3 级；不得出现一次成型的中灰平涂块（内部标准差 >6%）。
3. **无排线**：全帧交叉排线（两组以上线方向夹角 ≥15° 且密度 >2 线/10px）面积 ≤1%；单色实心填充（墨色均匀块）面积 ≤15%；「明暗由线密度变化」的单调映射不成立（线密度与局部明度相关系数 |r| ≤0.5）。
4. **色不掩笔**：彩色像素（饱和度 >15%）≤35%；色相 ≤3 族（青绿系/赭黄系/墨色）；单块饱和度 ≥70% 的连通彩色区域面积 ≤2%；线迹穿过色块的可见度 ≥60%（色块不覆盖线）。
5. **平远与留白**：水面/空纸（高亮带）面积 ≥30%；横向贯穿 ≥50% 画幅宽度；地平线位于画面高度 30–70% 带内；无强透视消失点（透视线收敛点数量 ≤1 且不在画内）。
6. **点景微小**：点景元素（舟/屋/人/桥）体量 ≤ 树高的 20%；每 1000px 宽画面 ≤3 处；人物为剪影级（面部细节像素 ≤0.1% 画面）。
7. **款印与动画（动画时）**：款识区（角落文字列）≤5% 画面；红色印章色块 1–3 处；点景元素总位移 ≤1% 画幅/秒；水面波动 ≤2px、云气漂移 ≤0.5%/秒；不得出现人物特写、叙事动作或镜头推拉；墨迹不得闪变（帧间差 ≤1%）。

## 控制参数（§4 原样）

**P1 书写性线质（Calligraphic Line Quality）**（默认 强）`[归纳]`
- 弱: 线以匀称勾勒为主（早年工细档，如《幽篁戴胜图》竹枝双勾）
- 中: 提按可见、锋颖含蓄（《鹊华秋色图》）
- 强: 提按悬殊＋飞白＋篆籀转折（《秀石疏林图》）

**P2 古意设色档（Archaic Color Mode）**（默认 水墨-浅绛）`[归纳]`
- 弱: 纯水墨（《水村图》《秀石疏林图》）
- 中: 浅绛＋水墨（《鹊华秋色图》）
- 强: 青绿空勾敷染（《谢幼舆丘壑图》《洞庭东山图》《秋郊饮马图》）

**P3 简率程度（Simplicity/Spareness）**（默认 中-强）`[归纳]`
- 弱: 元素较密、刻画细致（早年《幽篁戴胜图》工致档）
- 中: 疏密有致（《鹊华秋色图》）
- 强: 极简空勾（《吴兴清远图》空勾山形、点缀小树）

**P4 平远纵深（Level-distance Depth）**（默认 中-强）`[归纳]`
- 弱: 前景压缩、平面化（《秀石疏林图》纯近景）
- 中: 平远为主（《鹊华秋色图》）
- 强: 平远开阔、水面横贯（《水村图》《吴兴清远图》）

**P5 点景密度（Point-scenery Density）**（默认 低）`[归纳]`
- 弱: 几乎无人烟（《吴兴清远图》仅小树点缀）
- 中: 少量渔舟/屋舍（《水村图》屋舍舟船掩映）
- 强: 人物鞍马成组（《秋郊饮马图》《浴马图》《人骑图》）

**P6 干笔飞白比（Dry-brush / Feibai Ratio）**（默认 中）`[归纳]`
- 弱: 湿笔圆润（书法性的行书线，如《洛神赋》式行书卷）
- 中: 干湿相济（《鹊华秋色图》）
- 强: 飞白主导（《秀石疏林图》石与枯干）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款）：毛笔书写性 vs 版画刻线：线质／明暗／色笔关系三轴＋判据四条；两卡禁项互列（禁飞白／篆籀 ↔ 禁等宽刻线）
- **分工（vs 丢勒）**（× 丢勒；本卡 §3.1 分工条款）：书写性 vs 排线密度：明暗机制轴／线质轴＋判据三条——无排线、墨色积层 vs 密度映射
- **分工（vs 陈洪绶）**（× 陈洪绶（future）；本卡 §3.1 预写条款）：同用线：书法性（端庄古意）vs 古拙变形（大头短身）——造型／线质／用途三轴，待陈卡落地对齐
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：线条、色域、负空间

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/zhao_mengfu.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
