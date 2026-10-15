# 米开朗基罗 模块卡 — `michelangelo`

> A-19 模块库 ｜ 来源：档案 `research/artists/michelangelo.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `research/agent-art/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **人体即舞台**：肌肉分明的裸体主导画面；第一眼是敬畏（terribilità），不是优美
2. **扭转体**：肩线—髋线反向扭动、脊柱成 S 形；《最后的审判》整面墙呈「缓慢的旋转运动」
3. **雕塑性明暗**：形体像被「凿」出，硬边阴影、浮雕感
4. **仰视放大＋密集人群**：下排人物剧烈透视缩短；满构图人群绕中心涡旋（天顶 300 余人）
5. **英雄化裸体＋明亮湿壁画色**：超常肌群、无视惯例的裸体基督；肉色／土黄／暗绿／青蓝四族

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**：
```
High Renaissance fresco in the manner of Michelangelo Buonarroti: colossal muscular
nude figures, heroic anatomy with clearly defined muscle groups, bodies locked in
serpentine torsion — shoulders rotated against hips, spine forming an S-curve; figures
designed to be seen from below, strong foreshortening, monumental scale; sculptural
modelling — forms look chiselled out of the surface, hard-edged cast shadows, relief-like
light and shadow; dense swirling composition of many interlocking figures rotating around
a calm central axis; heavy clinging drapery that reveals the body underneath; idealised
faces, grave and intense, no soft smiles; limited fresco palette of flesh tones, earthy
ochre, muted green, pale violet and sky blue, matte plaster surface; an atmosphere of
awe and terribilità
```
**负向约束（--no）**：
```
--no sfumato haze, --no soft blurry edges, --no slender or effeminate bodies,
--no chubby childlike proportions, --no anime/manga faces, --no smiling serene faces,
--no pastel high-key palette, --no decorative ornament or gold leaf,
--no landscape backgrounds dominating the scene, --no visible impasto or painterly
brush texture, --no modern clothing, --no symmetric frontal standing pose
```

## 代码艺术规则（§8.2 原样）

> 参考 `templates/style_card.md` 的写法：把视觉语言翻译成**可逐帧自查**的量化/物理规则。

1. **比例**：主人物身高 ≥ 7.5 头长；肩宽 ≥ 2.5 头宽（英雄比例；对未成年人/儿童角色豁免）。
2. **扭转检测**：任一主人物肩线与髋线的投影夹角 ≥ 30°（弱档 10–20°，强档 45–70°）；同一画面里 ≥ 60% 的人物达到此值。
3. **硬边阴影**：形体转折处的明暗过渡带 ≤ 画面短边的 0.6%（对比达·芬奇模块的 ≥1.5%）；即"凿出来"的边缘。
4. **构图密度**：主体人群占画面面积 ≥ 55%；连续空白背景区域 ≤ 画面 15%。
5. **剪影可读性**：把帧缩到 25% 大小后，主要人物的轮廓仍可辨认（逐个主体做二值化剪影检查，轮廓断裂 ≤ 2 处）。
6. **色彩**：全帧平均饱和度 ≤ 0.5；强调色（S>0.6）同屏 ≤ 2 种；主色限定在肉色/土黄/暗绿/青蓝四族。
7. **未完成度**：允许 10–25% 的画面区域停留在"草稿/粗凿"状态（用局部高频能量检测定义：粗凿区 Laplacian 方差 ≥ 平坦区的 3 倍，且面积占比落在区间内）。

## 控制参数（§4 原样）

| 参数 | 弱档（可观察） | 中档 | 强档 | 默认 |
|---|---|---|---|---|
| **肌肉夸张度**`[归纳]` | 接近自然的柔和体量（早期《圣殇》） | 轮廓清晰的英雄体型（《大卫》） | 超常肌群、块块分明（天顶 ignudi、《最后的审判》基督） | **70%** |
| **扭转角**（肩线与髋线夹角）`[归纳]` | 正面站立、扭转 <15° | contrapposto 式扭转 20–35° | 螺旋扭体 45–70°（蛇形体） | **50%** |
| **浮雕强度**（塑形 vs 平涂）`[归纳]` | 平缓明暗、少投影 | 强明暗建模、体块清楚 | 形体像从墙面"凿出"，硬边投影 | **65%** |
| **构图密度 / 漩涡度**`[归纳]` | 单/少人物、留白多 | 3–5 人成组、局部聚散 | 满构图、多组人群绕中心旋转（《最后的审判》） | **60%** |
| **未完成度**`[归纳]` | 全部刻画到位 | 次要区域留草稿感 | 保留粗凿/未刻面（奴隶像一类的状态） | **15%** |

使用建议：默认组合≈"米开朗基罗式"；做"组合实验"时把扭转角与构图密度调高、把浮雕强度调高，就会快速吃掉对方的柔和笔触（与达·芬奇模块天然互斥，注意主辅 70/30 分配）。

## 冲突注记（→ conflicts.md）

组合前先读 `research/agent-art/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-01**（× Lane B 模板「硬阴影」禁令；本卡 §8.2-3）：阴影硬度（种子案例；反约束句须改写）
- **C-02**（× 达·芬奇；本卡 §8.2-3）：明暗过渡带宽度（≤0.6% vs ≥1.5% 短边）
- **C-17**（× 北斋 / 马蒂斯；本卡 §8.2-4）：负空间（≤15% vs ≥35% / ≥20%）
- **C-18**（× 毕加索 / 马蒂斯；本卡 §4 浮雕强度 + §8.2-3）：形体塑造（浮雕 vs 平涂）
- **near-miss（conflicts.md §4 表）**：#4（饱和度 → ≤0.35）、#7（与维米尔「物体边缘」量纲不同，需写清测量对象）

## 来源

- 档案（唯一正本）：`research/artists/michelangelo.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`research/agent-art/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`research/prompts/artist_modules/README.md`
