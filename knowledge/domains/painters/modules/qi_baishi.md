# 齐白石 模块卡 — `qi_baishi`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/qi_baishi.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **红花墨叶**：纯红（洋红／胭脂）花头与浓墨叶直接并置、几乎无过渡色——红区边缘邻接墨／空白 ≥60%
2. **工写双分辨率**：工笔草虫（翅脉／触须可辨）× 写意花叶（一笔一叶）同框——细度比 ≥5–10×
3. **墨分五色（水的体系）**：焦浓重淡清＋水痕／渍墨／飞白；虾体透明感＝淡墨多层＋留白（不勾轮廓线）
4. **民间色彩＋金石用笔**：洋红／藤黄／花青点缀式使用；中锋圆线、行笔迟涩（篆籀气）；单刀篆刻
5. **似与不似＋构图张力**：造型停在「似与不似之间」；一边极密一边极空；长题多印参与构图平衡

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
traditional Chinese ink painting in the style of Qi Baishi (齐白石), xieyi freehand brushwork,
vermilion red blossoms set against dense black ink leaves (honghua moye 红花墨叶), strong red-and-ink contrast,
gongbi fine-brush insects (translucent wings, articulated legs, thin antennae) juxtaposed with bold loose
flower-and-leaf strokes — two levels of precision in one frame,
ink graded from charred black to pale grey with visible water bleed and dry-brush feibai streaks,
generous unpainted paper left as water, sky and air, asymmetric composition anchored to one side,
small pure accents of folk palette: vermilion, gamboge yellow, indigo, vegetable green,
supple round brush lines with seal-script (jinshi) strength, spontaneous but controlled,
short poetic inscription and red seals at the edge,
raw xuan paper texture, wet-on-wet ink diffusion
```

**负向约束（`--no` 风格）**
```
oil paint, impasto, canvas weave, western linear perspective, vanishing point,
smooth digital gradients, airbrush, 3D rendering, HDR, photographic detail,
flat vector color blocks, hard cut-paper edges, gold leaf, metallic foil,
neon or fluorescent colors, chiaroscuro, hard cast shadows, perfectly symmetrical composition,
equal-width mechanical outlines, cross-hatching shading, glow effects
```

## 代码艺术规则（§8.2 原样）

1. **墨阶规则**：全帧墨色（去彩色后）直方图可辨 ≥5 级（焦 L<12%、浓 12–30%、重 30–50%、淡 50–70%、清 >70%）；焦墨区占比 2–15%；纯黑（L<5%）占比 ≤8%。自查：明度直方图 + 峰计数。
2. **红墨对比规则**：纯红像素（H∈[340°,360°]∪[0°,10°]、S ≥0.6）面积 3–15%（强档 ≥15%）；红区边缘邻接墨黑或纸白的比例 ≥60%（「红与墨绑定」判据）。自查：色相掩膜 + 邻接统计。
3. **工写落差规则**：笔触宽度分布呈双峰——最细 5% 笔触 ≤2 px、最粗 5% ≥20 px（1080p 基准），双峰比 ≥8×；或（无虫帧）笔触宽度变异系数 ≥0.35。自查：笔画骨架宽度统计。
4. **留白规则**：未涂布区（接近纸色、低纹理方差）≥30%；主体包围盒 ≤ 画面 55%；空白不得被均匀噪点填充。自查：纸色掩膜 + 包围盒。
5. **民间色规则**：高饱和色（S ≥0.6）总占比 ≤20%；色相簇 ≤6（红/黄/蓝/绿/墨/纸）；无荧光色（H 品红区间外、S >0.9 占比 = 0）。自查：饱和度掩膜 + 色相聚类。
6. **线条规则**：无等宽机械线（线宽变异系数 ≥0.25）；无排线（hatch）纹理（方向性平行线密度 ≤2 条/cm²）；线条端点圆润（非剪裁硬端）。自查：线宽统计 + 方向场。
7. **水痕规则**：笔触边缘存在渗化过渡带（2–8 px 渐晕），硬边剪裁（过渡带 ≤1 px）比例 ≤10%；干笔飞白条纹区每 100×100 px ≥5 条（若声明飞白档）。自查：边缘过渡宽度分布。
8. **构图与款印规则**：左右/上下视觉质量差 ≥15%（非对称）；题款+印章 ≥1 处、总面积 ≤8%；款识为竖排中文短题（不出现拉丁字母）。自查：质量分布 + 文本区域检测。

## 控制参数（§4 原样）

**P1 红墨对比强度（Vermilion–Ink Contrast）**（默认 60%）`[归纳]`
- 弱: 纯红面积 ≤5%，红偏赭/胭脂暗调；墨叶为主（近纯水墨）
- 中: 纯红面积 5–15%，花头数点、与墨叶相邻
- 强: 纯红面积 ≥15%，大红大黑直接对撞（红花墨叶典型帧；红区 H 340–360°、S ≥70%）

**P2 工写落差（Detail Register Gap）**（默认 70%）`[归纳]`
- 弱: 全写意（无工虫；全画面单一精度）
- 中: 局部 1–2 只草虫，细度约为花叶笔触宽度的 1/5
- 强: 极细草虫（翅脉/触须可辨，线宽 ≤1 px 级）与极粗花叶（笔触宽 ≥ 虫体长 1/5）同框——双分辨率

**P3 墨阶数（Ink Tone Levels）**（默认 5 级）`[归纳]`
- 弱: 2–3 级（焦浓 + 淡）
- 中: 5 级（焦、浓、重、淡、清；虾体分层）
- 强: ≥7 级连续过渡 + 水痕渍墨（透明感优先，如虾身/花瓣）

**P4 留白率（Void Ratio）**（默认 40%）`[归纳]`
- 弱: <15%（密体构图）
- 中: 15–35%
- 强: ≥35%（主体一角、大片空白承担水/天/空气）

**P5 民间色占比（Folk Palette Ratio）**（默认 15%）`[归纳]`
- 弱: ≤5%（近纯水墨，彩仅点醒）
- 中: 5–20%（红/黄/蓝 2–3 色点缀）
- 强: ≥20%（多色并置：洋红、藤黄、花青、汁绿；仍以墨压阵）

**P6 金石笔性（Seal-Script Brush Character）**（默认 60%）`[归纳]`
- 弱: 行笔流畅、锋颖尖利
- 中: 中锋圆劲、转折见笔
- 强: 迟涩圆厚、飞白、如篆如刻（藤蔓/枝干如篆籀；参《祀三公山碑》体势）

> 用法：P1/P2 定「是不是红花墨叶 + 工写」；P3/P4 定水墨气息；P5 定民间色档位；P6 定金石质感。三档描述可直接写进自查表。组合时：与马蒂斯组合按 §3 分工（表面/红轴二选一）；与八大组合温度轴二选一。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §8.2-1/-7）：表面系统：平涂色块（内部 ≤5%、无描边）vs 水墨表面（墨阶／水痕／飞白）——不可拆，二选一（N4）
- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §8.2-2）：红的使用：大面平涂色块 vs 花头点缀、永远与墨绑定——红轴单主（N3）
- **分工（vs 八大山人）**（× 八大山人；本卡 §4 P1）：同族两档互斥：热烈／生机／色彩 vs 冷峻／极简——色彩轴归齐、极简减笔轴归八大
- **C-17**（× 米开朗基罗；本卡 §8.2-4）：负空间（≥30% 与八大／北斋／马蒂斯同侧，取交集并显式取值；与米氏 ≤15% 按 N4 二选一）
- **互斥（邻近模块）**（× 北斋 / 丢勒 / 克里姆特；本卡 §8.2-6）：机制互斥：等宽线＋色块平涂 / 排线明暗 / 金箔图案图层——均不采用

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/qi_baishi.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
