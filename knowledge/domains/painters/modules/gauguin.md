# 高更 模块卡 — `gauguin`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/gauguin.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **平涂色块**：单区明度变化 ≤5%、笔触被抹平（与印象派/塞尚的笔触构造直接对立）；哑光表面（peinture à l'essence、近壁画）
2. **景泰蓝式粗轮廓（Cloisonnism）**：深色粗轮廓线勾出形体、内部平涂——「pure colour separated by heavy black outlines」
3. **象征性/非自然色彩**：红草地、柠檬黄天空、粉沙滩、紫阴影——色彩按情绪/象征逻辑选择（「把色彩从模仿再现中解放出来」）
4. **色带层叠空间（天空常被删除）＋装饰图案与人物同权**：无传统透视、2–4 条水平色带构成骨架；布料/雕像/树冠图案与人物同权
5. **简化古拙＋静穆神秘＋母题群**：正面/侧面化、姿态庄严静止（hieratic）；布列塔尼→塔希提/马克萨斯→宗教图像；「明亮中放入如此多的神秘」

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Gauguin-style synthetist composition — flat colour areas bounded by heavy dark contours (cloisonnism), painted from memory and imagination rather than observed from life:
broad matte fields of stridently non-natural colour — a red field where grass would be, a lemon-yellow sky, pink sand, violet shadows;
forms simplified to their essence: hieratic figures, frontal or profile, arranged across shallow stacked bands of green, yellow and red — no vanishing point, the sky sometimes deleted or replaced by pure colour or pattern;
decorative motifs interwoven with figures — pareu cloth, carved idols enlarged to the scale of gods, patterned tree canopies;
symbolist stillness and mystery — bright yet silent, timeless, no anecdote, no gesture of everyday life;
matte unvarnished surface — thinned oil (peinture à l'essence), brushwork suppressed within each colour area, visible canvas weave;
palette: vermilion, cadmium yellow, chrome green, cobalt blue, violet, ochre, black contour lines;
setting: Breton women in white coiffes before a wayside calvary, or vahine resting in a tropical grove under mango trees
[print variant] woodcut: blocks gouged like wood sculpture, bold black key lines, flat colour blocks, rough grain, deliberately crude edges
```
**负向约束（`--no` 风格）**
```
--no naturalistic colour, realistic lighting, gradients, aerial perspective, pointillist dots, optical mixing,
impasto, visible directional brushstrokes, complementary-colour vibration across the whole canvas, glossy varnish,
single-point perspective, deep space, atmospheric effects, sfumato, dramatic chiaroscuro, decorative gold,
sweet pastel harmony, cute doll faces, photographic realism, crowds in motion, narrative detail, text, watermark,
3D render, anime
```

## 代码艺术规则（§8.2 原样）

1. **平涂度规则**：主要色块（各 ≥5% 画布面积）内部明度标准差 ≤5%（0–255 尺度 ≤12）、色相变化 ≤8°；全帧「渐变带」（连续过渡 >2% 短边）面积 ≤10%。自查：区域分割 + 分区统计。
2. **轮廓线规则**：暗轮廓（明度 ≤30%）线宽 ≥0.3% 短边；覆盖主要形体边界 ≥60%；线宽变异 ≤2:1（不得时粗时细如书法）。自查：边缘/线条检测 + 暗像素掩膜。（依据：[R3]「heavy black outlines」）
3. **色数规则**：主色 ≤10（含黑轮廓）；**光学混合点阵 0 命中**（点径 ≤2 px 的孤立像素簇不得成规模 ≥5% 面积）。自查：色彩量化 + 点阵检测。（与修拉模块的分离判据）
4. **硬边界规则**：色块边界梯度带 ≤1% 短边（无羽化、无抗锯齿宽边）；相邻色块明度跳变 ≥15%。自查：边界梯度剖面。（依据：[R3]「no subtle gradations」）
5. **空间规则**：线性透视消失点检测 0 命中；水平色带 ≥2 层（绿/黄/红类）；天空区（如存在）为纯色或图案、**非渐变**。自查：直线透视检测 + 色带分割。（依据：[R8]「天空消失了」）
6. **装饰同权规则**：图案区与人物区渲染级别差 ≤1 级（同为平涂）；强档图案密度 ≥10% 面积（pareu/纹样/树冠图案化）。自查：分区渲染级别比对。（依据：[R1]「decorative abstract patterning with figuration」）
7. **象征色锚点规则**：≥1 处非自然色区（红草地/黄天/粉沙/紫影）≥8% 面积，且与主题锚定（宗教/神话/异域——须能指出对应关系）。自查：色相异常检测 + 主题对照表。
8. **合成/静止规则（视频帧附加）**：场景不可对景复原（多源拼合特征：人物/神像/纹样来源异质）；静止悬置——事件外光流 Δ ≤1%/帧；无运动模糊、无镜头运动（与 C-09 运动预算的「冻结」侧一致）。自查：光流场 + 模糊核检测。（依据：[R13]「drawn from fantasy and memory」）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–5 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **平面色块度**`[归纳]` | 可见方向性笔触、局部厚涂（印象派学徒档：《Vaugirard 菜园》1879） | 局部平涂 + 局部笔触（过渡档：《四个布列塔尼女人》1886） | 全画面平涂、单区明度变化 ≤5%、无渐变（成熟档：《黄色基督》《Arearea》） | **80%** |
| P2 | **轮廓线强度（景泰蓝度）**`[归纳]` | 无暗轮廓（早期档） | 部分形体勾线（关键形体 1–2 处/帧） | 全画面粗暗轮廓（线宽 ≥0.3% 短边、明度 ≤30%、覆盖 ≥60% 形体边界；《黄色基督》档） | **70%** |
| P3 | **象征色彩度**`[归纳]` | 接近自然色（仅提纯；早期档） | 强化/非典型色（紫草地、橙沙、粉径；布列塔尼档） | 符号化映射（红草地、柠檬黄天、粉沙滩——非自然色与主题绑定；《布道后的幻象》《黄色基督》档） | **70%** |
| P4 | **空间压缩/层叠度**`[归纳]` | 保留透视深度（早期风景档） | 浅空间 2–3 层（布列塔尼室内/田野档） | 3+ 水平色带层叠、无消失点、天空删除或图案化（《Arearea》《我们从何处来》档） | **65%** |
| P5 | **装饰-象征母题整合度**`[归纳]` | 无装饰（早期） | 服装/器物纹样（coiffe、pareu 局部） | 满画面装饰节奏与人物同权（树冠图案化、雕像/神像、纹样覆盖 ≥10% 面积） | **60%** |
| P6 | **记忆-想象合成度**（方法/工作流参数）`[归纳]` | 对景写生（早期印象派档） | 现场速写 + 工作室合成（布列塔尼档） | 无现场——多源拼合（照片/文献/记忆/他画；《我们从何处来》档） | **70%** |

> **用法**：P1/P2/P3 定「是不是高更」（三条中 ≥2 条 ≥ 中档才成立）；P4/P5 定时期与题材档（布列塔尼→塔希提→晚期）；P6 为**方法/组稿参数**（不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流类」单列）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若色块内出现渐变/笔触纹理（>5%）且无轮廓线 → 越界进入**马蒂斯/塞尚**档；② 若表面出现点阵/光学混合（≥40%）→ 越界**修拉**；③ 若出现厚涂方向性笔触（覆盖 ≥60%）+ 互补对全场振动 → 越界**梵高**；④ 若出现物理不可能的变形（声波天/融化空间/无脸化）→ 越界**蒙克**；⑤ 若色彩沦为纯装饰配比、无象征读法 → 越界**马蒂斯**（装饰端）。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §3.1 分工条款）：平面化服务什么：象征端（暗轮廓＋象征色彩＋神话层）vs 装饰端（无描边＋平衡配比＋无象征负担）——判据四条，70/30 选主导
- **分工（vs 修拉）**（× 修拉；本卡 §3.1 分工条款）：综合 vs 分色（1886 第八次印象派展同场对立）：整块平涂＋暗轮廓 vs 点阵光学混合＋无轮廓——表面轴同轴不可叠加
- **分工（vs 梵高）**（× 梵高；本卡 §3.1 分工条款）：色块端 vs 笔触端（阿尔勒九周两极）：可见笔触 ≤15% vs ≥60%——不得折中成「半厚涂的平涂」
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 笔触可见度 / C-06 饱和度预算 / C-12 色相面积 / C-16 平涂系反约束适用域

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/gauguin.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
