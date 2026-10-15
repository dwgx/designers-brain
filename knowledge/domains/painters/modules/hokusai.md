# 葛饰北斋 模块卡 — `hokusai`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/hokusai.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **线为骨架**：等宽、连续、无排线的轮廓线；色块贴线平涂
2. **普鲁士蓝主导**：蓝系常占 ≥40% 面积（1830 年代「蓝色革命」）
3. **非对称＋单条强斜线**：主体从不居中；尺度戏法（远景富士被压到 ≤ 前景 1/4）
4. **曲线族／螺旋**：大浪生成小浪、小浪生成波纹（≥3 级嵌套）；负空间 ≥35%
5. **人＝剪影＋极简线**（≤6 条/人）；装饰图案与写实同画面；留纸当高光

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Japanese ukiyo-e woodblock print in the manner of Hokusai's late landscape prints:
flat colour areas printed inside a single uniform-width black keyline; no hatching,
no rendering, no gradients except a fine bokashi fade in the sky;
dominant Prussian blue with indigo, white paper reserved for foam and snow,
muted ochre/grey/black accents; asymmetric composition built on one strong diagonal;
one dominant motif (wave / wind / waterfall / rain) drawn as a family of nested curves,
each small curve repeating the big one; distant Mount Fuji reduced to 1/4 of the
foreground element and pushed off-centre; tiny silhouetted figures with at most six
detail lines; at least 35% untouched sky or water; visible woodblock grain and
slightly misregistered colour plates
```
**负向约束（`--no` 风格）**
```
--no gradient shading, airbrush, soft blending, photorealistic water simulation,
3D render, perspective vanishing-point realism, hatching/crosshatching,
more than 7 hues, warm colour cast, muddy earth palette, centred symmetrical layout,
large detailed faces, dramatic rim light, cast shadows, lens flare, texture noise,
western oil-painting brushwork, glowing highlights, cluttered background
```

## §8.1b 场景可迁移性注记

> E-02 · E1_t1b 诊断（2026-10-15）：§8.1 含 Mount Fuji / tiny figures 等非主体题材词；E1_t1 中仅作远景与比例元素、未替换场景，风格可迁移（如需更纯净可删上述词）。

## 代码艺术规则（§8.2 原样）

1. **线宽**：轮廓线宽恒定，同一元素内变化 ≤30%；无排线、无羽化（线与色块之间无抗锯齿过渡带 >1px）。
2. **色数**：主色 ≤7（普鲁士蓝、靛蓝、白/纸、赭、灰、黑、一点淡红或淡黄）；蓝色系面积占比 ≥40%。
3. **构图**：主体中心偏离画布几何中心 ≥10% 画幅；存在且仅存在一条 15°–45° 的主斜线；无单点透视消失点。
4. **曲线族**：流体（浪/云/雾）由同心曲线构成，尺度嵌套 ≥3 级；每一级曲线的曲率符号与上一级一致（同向弯），相位错帧 ≥2 帧（动画时）。
5. **尺度对比**：远景主体高度 ≤ 前景元素的 1/4，且落在画面上/下 1/3 带内（不得压在中线）。
6. **负空间**：天空/水面单色平涂或留白 ≥35% 面积；留白内部不得有均匀噪点或渐变（除天空允许 ≤1 段 bokashi）。
7. **人物**：人物/船等前景元素 ≤3 组，每组高度 ≤ 画面高度 1/8，细节线 ≤6 条；人物不得遮挡主曲线族的"峰"（戏剧焦点）。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **普鲁士蓝主导度（Blue Dominance）**`[归纳]` | 蓝只作点缀（≤15% 面积） | 蓝为天空/水面主色（35%–45%） | 近乎单色蓝印（aizuri-e，≥70%） | **55%** |
| P2 | **构图非对称度（Asymmetry）**`[归纳]` | 主体居中，左右均衡 | 主体偏 1/4 画幅 | 主体压到边角 + 单条强斜线贯穿 | **75%** |
| P3 | **尺度对比（Scale Contrast）**`[归纳]` | 远近主体同大 | 远景 ≈ 前景 1/2 | 远景 ≤ 前景 1/4（富士被浪压小） | **80%** |
| P4 | **曲线族层级（Curve Nesting）**`[归纳]` | 单一曲线轮廓 | 2 级（大浪→小浪） | ≥3 级（大浪→小浪→波纹/雨丝） | **3 级** |
| P5 | **人物简省度（Figure Economy）**`[归纳]` | 人物占画面高度 ≥1/4，细节多 | 1/8 高度，线 ≤12 条 | 剪影级（线 ≤6 条/人，≤3 组） | **1/8 高度、8 条线** |
| P6 | **负空间比例（Negative Space）**`[归纳]` | ≤20%（满构图） | 35% | ≥55%（大留白，如《凯风快晴》） | **40%** |

> 用法：P1 决定"是不是北斋蓝"，P4 决定"浪像不像北斋的浪"，P2/P3/P6 决定戏剧性强度。三档描述可直接进逐帧自查表。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-07**（× 丢勒；本卡 §8.2-1/-2/-6）：表面着色系统（平涂 vs 排线）
- **C-12**（× 卡拉瓦乔 / 梵高；本卡 §4 P1 + §8.2-2）：色相面积预算（蓝 ≥40% vs 土色系 / 互补对 1:1）
- **C-16**（× Lane B 02 卡反约束；本卡 §8.2-1/-6）：反约束适用域（「没有高光的平涂」误伤平涂系）
- **C-17**（× 米开朗基罗；本卡 §4 P6 + §8.2-6）：负空间（≥35% vs ≤15%）
- **near-miss（conflicts.md §4 表）**：#5（色相上限组 → 取 ≤5）、#6（线宽恒定，与丢勒/08 卡同侧）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/hokusai.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
