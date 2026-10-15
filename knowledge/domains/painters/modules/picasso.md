# 毕加索 模块卡 — `picasso`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/picasso.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **面片化边缘**：形体碎成 10°–40° 折角的「水晶切面」；浅浮雕空间
2. **多视点同框**：同一物体的正面／侧面／俯视被同时画出
3. **近单色棕灰域**：赭／灰／棕／黑、低饱和；明度中心亮（暗环包亮心）
4. **平涂无渐变**：面片互相咬合如拼图；体量靠角度差与明度跳变，不靠明暗
5. **锚点残留＋材料入侵**：3–5 个具象锚点（发浪／领结／表链）；字母、乐谱、报纸、木纹进入画面

## 图像 prompt（§8.1 原样）

**正向段（可粘贴）**：
```
Analytic Cubist portrait in the manner of Picasso, autumn 1910: a seated man
fractured into 40–120 semi-transparent angular planes; figure and background
merge into one shallow, crystalline lattice; 3–5 simultaneous viewpoints per
object; a few recognizable anchors survive (a wave of dark hair, the knot of a
tie, a watch chain, hands clasped in the lap); palette restricted to 4–5 hues —
ochre, umber, warm grey, slate, black — with at least 6 value steps; form modeled
only by value jumps between flat planes, no gradients; matte oil-on-canvas
surface, fine canvas weave; brightest values concentrated at the center, dark
aura toward the edges; traditional seated pose preserved; composition reads as
monumental, melancholic, frontally posed.
```
**负向约束（--no 风格）**：
```
--no single-point perspective, photorealistic rendering, airbrushed shading,
smooth gradients, saturated complementary colors, decorative floral patterns,
3D-rendered lighting or drop shadows, glossy surfaces, visible brushwork
impasto, text or signage, lens vignette, chromatic aberration
```

## §8.1b 纯风格段（场景可迁移）

> 派生自 §8.1 正向段（E-02 · E1_t1b，2026-10-15）：删除题材词（人物/肖像/室内/静物）与场景专属道具，仅保留视觉语言（光/色/笔触/结构/构图规则）；用法：主题句 + 本段（同 §8.1 配方）。负向段沿用 §8.1 原文（本通道不发送）。
> 删除项：portrait、seated man、anchors（hair/tie/watch/hands）、seated pose、frontally posed；最小改写：figure and background→foreground and background。明细见 `experiments/E1_t1b/RESULTS_t1b.md` §2。

**正向段（可直接粘贴）**：
```
Analytic Cubist painting in the manner of Picasso, autumn 1910: the scene
fractured into 40–120 semi-transparent angular planes; foreground and
background merge into one shallow, crystalline lattice; 3–5 simultaneous
viewpoints; palette restricted to 4–5 hues — ochre, umber, warm grey, slate,
black — with at least 6 value steps; form modeled only by value jumps between
flat planes, no gradients; matte oil-on-canvas surface, fine canvas weave;
brightest values concentrated at the center, dark aura toward the edges;
composition reads as monumental, melancholic.
```

## 代码艺术规则（§8.2 原样）

> 把毕加索视觉语言翻译成可逐帧自查的量化规则（对应 `templates/style_card.md` 画风段写法）：

1. **色数**：全帧唯一色相 ≤5（分析档 ≤3），明度级（L* 分桶）≥6；平均饱和度（HSL S）≤35%。
2. **面片**：画面分割为 40–120 个多边形面片，单片面积 ≤ 画面 6%，长宽比 ≤4:1，面片主轴角度收敛到 ≤3 个角度族（±7° 容差）。
3. **多视点**：画面中 ≥3 处局部结构使用彼此不同的灭点（延长线交点分散在画面外 ≥2 个位置）。
4. **轮廓断口**：任意 100×100 px 网格内连续轮廓总长 ≤ 网格对角线 ×2；轮廓断口密度 ≥ 每 200 px 1 个。
5. **明度中心**：中心 1/3 区域平均 L* 比四边 10% 边缘带高 ≥8（《三个音乐家》规律；对应 P5）。
6. **平涂判据**：相邻像素 ΔE ≤6 的像素对占比 ≥85%（即无渐变面；对应 P3 强档）。
7. **文字块**（若启用）：≤3 处，字高一致（±10%），旋转角与邻近面片主轴偏差 ≤5°。
8. **锚点验收**：缩略图缩至 64px 宽时，人工仍能辨认 ≥1 个人物剪影 + ≥3 个具象锚点（发/手/器物/领口）。

## 控制参数（§4 原样）

| # | 参数 | 弱 | 中 | 强 | 默认建议 |
|---|---|---|---|---|---|
| P1 | **视角碎裂度**（同一物体同时呈现的视点数）`[归纳]` | 1 个视点，仅把形体简化为多边形，仍统一透视 | 2–3 个视点局部并置（脸正面+侧面） | ≥4 个视点全画面拼合，整体可辨识度降到 50% 以下 | **75%**（中偏强，对应 1910 分析期） |
| P2 | **色域收敛度**（全画面独立色相数）`[归纳]` | 6–8 色相，保留环境色 | 4–5 色相（赭/棕/灰/蓝灰） | 2–3 色相近单色，明度级 ≥6 | **3–5 色相（中档）** |
| P3 | **平面化程度**（明暗渐变的残留）`[归纳]` | 保留体积渐变与投影 | 局部平涂，交界处用硬边 | 全平涂面片拼合，零渐变 | **强档**（分析期）/ **中档**（肖像类任务） |
| P4 | **拼贴/文字密度**`[归纳]` | 0 处材料暗示 | 1–2 处（一小段乐谱或字母） | 报纸、木纹、藤编纹 ≥3 处显性拼贴 | **中档（1–2 处）** |
| P5 | **明度中心化**（中心 vs 边缘明度差 ΔL*）`[归纳]` | ΔL* < 5，明度均匀 | ΔL* 5–12 | ΔL* ≥ 15，暗环包亮心 | **中强（ΔL* 10–15）** |
| P6 | **锚点保留数**（可辨识具象特征个数）`[归纳]` | 0–1（接近纯抽象） | 3–5（发、手、领、器物） | ≥8，形体基本可读 | **3–5（中档）** |

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-06**（× 马蒂斯；本卡 §8.2-1）：饱和度（全帧 ≤35% vs 每块 ≥70%）
- **C-16**（× Lane B 02 卡反约束；本卡 §8.2-6）：反约束适用域（「没有高光的平涂」误伤平涂系）
- **C-18**（× 米开朗基罗；本卡 §4 P3 + §8.2-6）：形体塑造（平涂 vs 浮雕）
- **near-miss（conflicts.md §4 表）**：#4（饱和度上限组 → 取 ≤0.35）、#5（色相上限组 → 取 ≤5）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/picasso.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
