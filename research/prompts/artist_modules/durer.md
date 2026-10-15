# 丢勒 模块卡 — `durer`

> A-19 模块库 ｜ 来源：档案 `research/artists/durer.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `research/agent-art/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **排线即明度**：所有「灰」由线密度合成；几乎无实心涂黑（实心填充 ≤5%）
2. **排线随形体弯曲**（包裹形体）；线端收锋（中段鼓、端点尖）
3. **硬轮廓、无渐变**（与达·芬奇机制相反）；细节全幅均匀（逐根毛发／逐片草叶）
4. **微观观察视角**：对象占满画面；象征物密集堆叠（≥8 件静止陈列）
5. **数理秩序＋签名系统**：头身比／透视可见；AD 花押与年份几乎总在版上

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Northern Renaissance engraving in the manner of Albrecht Dürer's burin master prints (1513-1514):
pure black ink line work on warm off-white paper, no grey fill anywhere - every tone is
built from parallel hatching and layered cross-hatching;
hatching lines follow and wrap each volume; cross layers sit at 30-45 degrees;
line spacing tapers from about 6px in the lights to 1.5px in the darks (1000px wide frame),
darkest zones get 3 or more superimposed hatch directions;
engraved lines swell slightly mid-stroke and end in fine points;
hard contour lines separate every form: no soft edges, no sfumato, no airbrush;
hyper-detailed microtexture - individual hairs, grass blades, leaf veins, stone pores;
backgrounds closed with dense parallel line fields instead of empty space;
calm measured figures in contrapposto with stated head-to-body proportions;
a small dated monogram plate (AD-like initials) and an invented Latin cartellino;
allegorical objects placed as a dense still-life of symbols (compass, sphere, ladder,
hourglass, bell, magic square) when the theme is allegorical
```
**负向约束（`--no` 风格）**
```
--no color, --no greyscale gradients, --no smooth shading, --no airbrush, --no sfumato,
--no soft focus, --no bokeh, --no photographic rendering, --no painterly brushwork,
--no digital halftone dots, --no cel shading, --no manga screentone,
--no uniform line weight, --no grey flood fill, --no floating glow, --no 3D render,
--no empty white background areas, --no impressionist dabs
```

## §8.1b 纯风格段（场景可迁移）

> 派生自 §8.1 正向段（E-02 · E1_t1b，2026-10-15）：删除题材词（人物/肖像/室内/静物）与场景专属道具，仅保留视觉语言（光/色/笔触/结构/构图规则）；用法：主题句 + 本段（同 §8.1 配方）。负向段沿用 §8.1 原文（本通道不发送）。
> 删除项：contrapposto figures、microtexture examples（hairs/grass/leaf）、monogram plate、cartellino、allegorical still-life；最小改写：calm measured figures…→calm, measured composition。明细见 `research/experiments/E1_t1b/RESULTS_t1b.md` §2。

**正向段（可直接粘贴）**：
```
Northern Renaissance engraving in the manner of Albrecht Dürer's burin master
prints (1513-1514): pure black ink line work on warm off-white paper, no grey
fill anywhere - every tone is built from parallel hatching and layered
cross-hatching; hatching lines follow and wrap each volume; cross layers sit
at 30-45 degrees; line spacing tapers from about 6px in the lights to 1.5px in
the darks (1000px wide frame), darkest zones get 3 or more superimposed hatch
directions; engraved lines swell slightly mid-stroke and end in fine points;
hard contour lines separate every form: no soft edges, no sfumato, no
airbrush; hyper-detailed microtexture; backgrounds closed with dense parallel
line fields instead of empty space; calm, measured composition
```

## 代码艺术规则（§8.2 原样）

1. **明度→线密度单调映射**：对 1000px 宽参考帧，像素亮度 L∈[0,1] 决定排线间距 s = lerp(8px, 1.2px, 1−L)；线宽恒定 1.5–2px。自查：任取两个 16×16 区块，若块均值 L₁<L₂，则 s₁≤s₂（单调性必须处处成立）。
2. **排线方向场**：主排线方向 = 形体等高线切向 ±(30°–45°)；同一形体上方向 ≥2 段、段间差 ≥25°；交叉层与主层夹角 ∈[25°, 50°]。
3. **层数规则**：L>0.75 → 0–1 层；0.35<L≤0.75 → 2 层；L≤0.35 → ≥3 层。任何区域单色实心填充 ≤5% 画面面积（画框/边线例外）。
4. **线端收锋**：每条排线两端宽度 ≤ 中段宽度的 30%；允许的等宽线仅限轮廓线与结构线（其余等宽线必须重画）。
5. **轮廓连续性**：物体轮廓线为全图最连续的线（最长连续段 ≥ 形体周长 60%），线宽 ≥1.5× 内部排线宽，抗锯齿过渡 ≤1px。
6. **细节下限**：主体内部排线数 ≥200 根（512×512 帧）；毛发/草叶类 ≥300 根独立线段；背景纯空白 ≤10% 面积。
7. **缩略图一致性**：将画面 2×2 下采样后，实心黑面积 ≤8%、纯白 ≤35%——排线应在缩小时自然融合为灰，**不得**出现新的实心区（出现即说明原图用了填充而非排线）。
8. **帧间稳定性（动画）**：相邻帧同区域的线距变化 ≤10%、方向变化 ≤10°；无物体运动解释的明度跳变 >0.1 视为「排线闪烁」，判不合格。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **排线密度梯度（Hatch Density）**`[归纳]` | 仅暗部加单向平行线；线距 ≥6px | 平行 + 一层交叉（2 层）；暗部线距 ≈3px | ≥3 层多方向交叉；暗部线距 ≤1.5px，明暗差全靠线密度 | **70%** |
| P2 | **线端收锋（Burin Swell-Taper）**`[归纳]` | 线宽恒定（±10%） | 两端轻微收细 | 每根线中段鼓、端点成尖；单线宽变化 2–3 倍 | **65%** |
| P3 | **轮廓硬度（Contour Hardness）**`[归纳]` | 边缘柔化、允许 2–4px 过渡 | 清晰轮廓 + ≤2px 过渡 | 硬轮廓（≤1px 过渡）、零 sfumato；形体分离全靠线 | **85%** |
| P4 | **细节密度（Detail Density）**`[归纳]` | 主体细、背景简化 | 全幅一致的中等细节 | 逐根毛发/逐片草叶；主体 ≥300 独立纹理线 | **80%**（自然研究 90%；叙事场景 55%） |
| P5 | **象征堆叠度（Symbolic Object Density）**`[归纳]` | 0–1 件符号物 | 3–5 件 | ≥8 件可点名符号，静止陈列不互动 | **50%**（寓意画 85%；肖像 5%） |
| P6 | **几何秩序（Geometric Order）**`[归纳]` | 自由手比例 | 明确头身比/透视结构 | 圆规直尺式建构痕迹 + 测量级比例 + 单点透视 | **60%** |

> 用法：P1 决定「像不像丢勒的灰」，P3/P2 决定「像不像铜版」，P4/P5 决定题材档位（自然研究 vs 寓意画），P6 决定「北方 vs 意大利」的建构感。三档描述可直接进逐帧自查表（见 §8.2）。

## 冲突注记（→ conflicts.md）

组合前先读 `research/agent-art/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-07**（× 北斋；本卡 §4 P1/P2 + §8.2-1/-3/-7）：表面着色系统（排线 vs 平涂）
- **near-miss（conflicts.md §4 表）**：#6（线宽恒定，与北斋/08 卡同侧）

## 来源

- 档案（唯一正本）：`research/artists/durer.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`research/agent-art/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`research/prompts/artist_modules/README.md`
