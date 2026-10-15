# 达·芬奇 模块卡 — `da_vinci`

> A-19 模块库 ｜ 来源：档案 `research/artists/da_vinci.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `research/agent-art/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **无轮廓线**：亮暗过渡为宽而连续的灰色带，无「勾线＋填色」边界——sfumato 招牌
2. **烟式中间调**：灰层次极多、深色不脏、亮部不闪，整体像隔一层薄雾
3. **窄色域、低饱和**：同屏色相少（晚期主为蓝／黄／棕三家族）；人物从暗部「浮」出
4. **空气透视**：远景转蓝、边缘化开、对比下降——山体像被雾吃掉一截
5. **谜样表情＋微扭转**：微笑停在「将笑未笑」；三／四分之三姿势「转身到一半」；卷发呈连续带状（绳结纹样）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**：
```
Renaissance oil painting in the manner of Leonardo da Vinci, sfumato: absolutely no hard
contours anywhere, every light-to-shadow transition is a wide, continuous grey gradient,
soft smoky modelling; single soft light from the upper left moulding the figures out of
deep shadow; figures emerge from a dark grotto-like ground; aerial perspective — distant
mountains turn blue-grey, lose saturation and dissolve into haze; narrow earth palette of
ochre, umber, muted blue and dull gold, overall low saturation; a young woman seated in
three-quarter view, her arms, torso and head each subtly turned in slightly different
directions, arrested mid-motion; an ambiguous half-smile that suggests emotion without
revealing its cause; soft curly hair falling in continuous ribbons; rocks shaped like
rounded cones, wet atmosphere over shallow green water; flowers and plants that are
hybrids of several species, not any real plant; invisible brushwork, glazed surface,
matte, aged varnish warmth; contemplative, quiet, mysterious mood
```
**负向约束（--no）**：
```
--no hard outlines, --no cel shading, --no comic linework, --no high saturation,
--no neon colors, --no flat even lighting, --no multiple light sources,
--no visible brush strokes or impasto, --no crisp photographic edges,
--no symmetric frontal pose, --no open-mouth grin or clear emotion,
--no sharp geometric mountains, --no modern clothing
```

## §8.1b 纯风格段（场景可迁移）

> 派生自 §8.1 正向段（E-02 · E1_t1b，2026-10-15）：删除题材词（人物/肖像/室内/静物）与场景专属道具，仅保留视觉语言（光/色/笔触/结构/构图规则）；用法：主题句 + 本段（同 §8.1 配方）。负向段沿用 §8.1 原文（本通道不发送）。
> 删除项：young woman、half-smile、curly hair、figures、flowers；最小改写：the figures→forms、distant mountains→distant forms。明细见 `research/experiments/E1_t1b/RESULTS_t1b.md` §2。

**正向段（可直接粘贴）**：
```
Renaissance oil painting in the manner of Leonardo da Vinci, sfumato:
absolutely no hard contours anywhere, every light-to-shadow transition is a
wide, continuous grey gradient, soft smoky modelling; single soft light from
the upper left moulding forms out of deep shadow; aerial perspective — distant
forms turn blue-grey, lose saturation and dissolve into haze; narrow earth
palette of ochre, umber, muted blue and dull gold, overall low saturation;
rocks shaped like rounded cones, wet atmosphere over shallow green water;
invisible brushwork, glazed surface, matte, aged varnish warmth;
contemplative, quiet, mysterious mood
```

## 代码艺术规则（§8.2 原样）

> 参考 `templates/style_card.md` 的写法：把视觉语言翻译成**可逐帧自查**的量化/物理规则。用于 HTML 逐帧或 Blender 渲染时的自动检查。

1. **无硬边**：对每帧做边缘检测（Sobel/Canny），人物区域内的连续边缘链长度 ≤ 40 px；超过即判"轮廓线泄漏"。
2. **明暗带宽度**：任一"受光面→阴影面"的过渡带宽度 ≥ 画面短边的 1.5%（即不存在一条线上明暗突变）。
3. **中间调占比**：帧直方图中 L∈[40,70] 的像素 ≥ 55%；纯黑（L<8）与纯白（L>92）合计 ≤ 3%。
4. **低饱和**：全帧平均 HSV 饱和度 ≤ 0.35；S>0.6 的像素 ≤ 5%。
5. **远景色偏**：按深度 z 排序，远景区域的色相向 210°±20（蓝）收敛，且相对近景饱和度下降 ≥ 30%。
6. **单光源**：场景主光只有一盏（或等效一盏）；由阴影方向反推的光源方向夹角 ≤ 15°；补光强度 ≤ 主光的 40%。
7. **笔触不可见**：平坦区域的高频能量（Laplacian 方差）≤ 2——即画面上看不到笔触纹理，只有渐变。

## 控制参数（§4 原样）

| 参数 | 弱档（可观察） | 中档 | 强档 | 默认 |
|---|---|---|---|---|
| **Sfumato 强度**（边缘弥散度）`[归纳]` | 亮部边缘可辨、局部有清晰轮廓（早期作品） | 阴影一侧边缘化开、亮部保留结构（伦敦版《岩间圣母》） | 全画面无任何硬边，脸部五官只靠灰度层次读（《蒙娜丽莎》） | **70%** |
| **空气透视深度**`[归纳]` | 远山轮廓清楚、色相变化小 | 远山转蓝灰、边缘发虚 | 远景溶进雾/水汽，山体与天空几乎并成一层 | **60%** |
| **明度对比（chiaroscuro）**`[归纳]` | 高调均匀光，画面整体亮 | 单侧柔光、暗部成片（洞窟场景） | 大面积深暗、主体只在关键处受光 | **55%** |
| **色域宽度 / 饱和度**`[归纳]` | 多色相、局部饱和（早期/未完成作品） | 土色系为主+蓝黄点缀 | 近单色：蓝-棕-灰，饱和极低（晚期） | **45%** |
| **表情模糊度**（微笑/情绪）`[归纳]` | 表情中性明确 | 轻微笑意、不解释原因 | 完全谜题化：嘴角与眼角互为暗示（《蒙娜丽莎》） | **65%** |

使用建议：五个参数独立可调；"像达·芬奇"的最小组合是「Sfumato ≥ 中档 + 空气透视 ≥ 中档 + 色域 ≤ 中档」。

## 冲突注记（→ conflicts.md）

组合前先读 `research/agent-art/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-02**（× 米开朗基罗；本卡 §8.2-1/-2）：明暗过渡带宽度（≥1.5% vs ≤0.6% 短边）
- **C-03**（× 卡拉瓦乔；本卡 §8.2-3）：直方图/中间调（≥55% vs ≤25%）
- **C-05**（× 梵高 / 莫奈 / 塞尚；本卡 §8.2-7）：笔触可见度（只有渐变 vs ≥95% 笔触覆盖）
- **C-06**（× 马蒂斯；本卡 §8.2-4，同侧旁证组）：饱和度（每块 ≥70% vs 全帧 ≤35%）
- **C-14**（× Lane B 06/07/13 卡反约束；本卡 §8.2-2/-7）：渐变（禁令 vs sfumato/包络）
- **near-miss（conflicts.md §4 表）**：#4（饱和度上限组：达·芬奇/毕加索/莫奈/米开朗基罗 → 取 ≤0.35）

## 来源

- 档案（唯一正本）：`research/artists/da_vinci.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`research/agent-art/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`research/prompts/artist_modules/README.md`
