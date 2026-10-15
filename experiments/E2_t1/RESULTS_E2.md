# E2_t1 · E2 首批组合实验（T1「暴风雨中的海边灯塔」· 70/30 主辅）

> **E-04**（wave8 · ComboTest）· 2026-10-15 · 直连网关 `http://192.168.11.4:3000/v1/images/generations` · 模型 `grok-imagine-image-2.0`（裸名）
> 3 格 × 3 张 = **9/9 张**（0 重试、0 失败；请求→落盘合计 194.4s，均 ≈21.6s/张；wall 202s）。
> 配方：`prompt = 主题句 + 70/30 融合句 + 主段 + 辅段 [+ 分区句（仅 e2c）]`；主/辅段**逐字**取自模块卡（7 卡 §8.1b 纯风格段 / 4 卡 §8.1 正向段+注记口径）；负向段未随请求发送（通道无负向参数）。
> 主题句（全格逐字一致）：`A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead.`
> 三格：**e2a** 莫奈(主)+梵高(辅) ｜ **e2b** 达·芬奇(主)+卡拉瓦乔(辅)（C-01/C-02/C-03 检验）｜ **e2c** 莫奈(主)+塞尚(辅)（C-10 分区解法）。
> 上游：`design.md` §2（E2/E2b/E2c 行）与 §5b（N4/N9 口径）；`conflicts.md` §3（N1–N9 正本）、C-01/C-02/C-03/C-10；`E1_t1b/RESULTS_t1b.md`（§8.1b 拆分与通道口径）。

## 0. 口径（本批固定项）

- **主/辅段来源（逐字，逐行解包为单行，内容不变）**：

| 格 | 主段（来源） | 辅段（来源） | 主段 sha256 前 8 | 辅段 sha256 前 8 |
|---|---|---|---|---|
| e2a | `monet.md` §8.1 正向段（4 卡注记口径：无题材词，可迁移） | `van_gogh.md` §8.1 正向段（4 卡注记口径；风景道具词仅作次要元素） | 6d09117b | c97b5031 |
| e2b | `da_vinci.md` §8.1b 纯风格段（7 卡） | `caravaggio.md` §8.1b 纯风格段（7 卡） | 21015cfe | e651a3eb |
| e2c | `monet.md` §8.1 正向段（4 卡注记口径） | `cezanne.md` §8.1b 纯风格段（7 卡） | 6d09117b | 9a3502cb |

- **70/30 融合句（写入 prompt）**：`Fusion of two painterly languages: <Main> dominant (70%), <Aux> secondary (30%).`（比例为本批固定参数；§8 开放决策的 60/40、80/20 扫描留待后续批）
- **分区句（仅 e2c）**：按 C-10 要求①「显式写分层边界」写入（② 对比梯度限远景层、③ 近景禁雾色 为自查口径）；全文见 §2.3。
- **生成侧 vs 验收侧（关键口径）**：本批为**原始融合尝试**——生成侧同时保留双方特征（e2c 另加显式分区句）；**验收侧**按 N3/N4/N9 单主/分区口径执行。两层分开记录，正是为了检验「不可拆轴是否真的互斥」（design.md §2 E2b 行）。
- **通道坑位（沿用 E1 系列，实测复现）**：① 裸模型名 `grok-imagine-image-2.0`（带 `buddyfarm/` 前缀反而不通）；② 无负向通道（负向段只留档、不发送）；③ size 请求 `1024x1536`、实回 **768×1152**（不严格，由上游决定）。
- **N1/N4/N9 落地位置**：N1 = 负向段重算（§3；未发送）；N3/N4 = 轴所有权与二选一/分区判定（§4）；N9 = 组合卡验收口径（§5）；「冲突轴上是否出现双标准」两级检查（§6）。

## 1. 结果总表（3 行）

| # | 格 | 主/辅 | 模型 | 尺寸（请求 → 实回） | 耗时 | sha256 前 8 位（img_01 / 02 / 03） |
|---|----|------|------|--------------------|------|-----------------------------------|
| 1 | e2a_monet_van_gogh | 莫奈(主) + 梵高(辅) | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 53.9s（均 18.0s/张） | abdb8f68 / 622981fb / 6e4ad0e6 |
| 2 | e2b_da_vinci_caravaggio | 达·芬奇(主) + 卡拉瓦乔(辅) | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 64.0s（均 21.3s/张） | 33fcb950 / 94cd05fa / 55e70d21 |
| 3 | e2c_monet_cezanne | 莫奈(主) + 塞尚(辅) | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 76.5s（均 25.5s/张） | 05d33ceb / 5aa57c4e / 26369138 |

耗时口径：该格全部尝试的「请求→落盘」时长合计（含重试尝试；不含请求间隔与重试等待）；明细见 `run_log.jsonl` / `stats_e2.json`。

## 2. 每格 prompt 全文

> 下为实际发送的 prompt 全文（与 `req_*.json` 请求体内逐字一致；`prompts_e2.json` 为单一来源）。

### 2.1 e2a_monet_van_gogh（prompt sha256 前 8：a889d23f）

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. Fusion of two painterly languages: Claude Monet dominant (70%), Vincent van Gogh secondary (30%). oil painting in the style of Claude Monet, french impressionism, en plein air, broken comma-like brushwork with unblended strokes laid side by side, light-toned ground and high-key palette, coloured shadows (blue-violet) instead of black, atmospheric envelope unifying the whole scene, soft haze and shimmering water with broken reflections, asymmetrical cropped composition with no linear perspective and no three-dimensional modelling, water surface occupying a large portion of the canvas, sky and water mirroring each other, palette: pale blue, lavender, rose, cream, turquoise, soft green, pale yellow; soft edges dissolving between colour patches oil painting in the style of Vincent van Gogh, post-impressionist, thick impasto oil paint with visible brushstrokes and canvas weave, swirling turbulent sky of cobalt and ultramarine with glowing lemon-yellow stars ringed by concentric halos, complementary colour pairs (yellow/blue, orange/blue) laid side by side, flame-like cypress rising almost to the top edge, wheat field of short directional strokes, flat decorative space with cropped asymmetric composition inspired by Japanese woodblock prints, bold expressive outlines on key forms, colour used arbitrarily to express feeling rather than to reproduce the scene, no smooth blending, palette: cobalt blue, ultramarine, chrome yellow, lemon yellow, viridian, vermilion, pure white highlights
```

### 2.2 e2b_da_vinci_caravaggio（prompt sha256 前 8：b412f97d）

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. Fusion of two painterly languages: Leonardo da Vinci dominant (70%), Caravaggio secondary (30%). Renaissance oil painting in the manner of Leonardo da Vinci, sfumato: absolutely no hard contours anywhere, every light-to-shadow transition is a wide, continuous grey gradient, soft smoky modelling; single soft light from the upper left moulding forms out of deep shadow; aerial perspective — distant forms turn blue-grey, lose saturation and dissolve into haze; narrow earth palette of ochre, umber, muted blue and dull gold, overall low saturation; rocks shaped like rounded cones, wet atmosphere over shallow green water; invisible brushwork, glazed surface, matte, aged varnish warmth; contemplative, quiet, mysterious mood Caravaggio-style tenebrist oil painting: one single hard directional light from high left, no fill light, no reflected light; background areas in near-black shadow (values under 10% of the lit highlights); deep dark brown ground left visible inside the shadows as their mid-tone; violent chiaroscuro: lit passages bright and warm, shadows crushed, midtones suppressed; one frozen instant of dramatic action; the main motif pushed flat against the picture plane and cropped by the frame edge; restrained earth palette — ochre, madder red, lead white, bitumen black, one or two saturated accents; direct painting, broad final touches, impasto highlights on the lit edges
```

### 2.3 e2c_monet_cezanne（prompt sha256 前 8：6a83bbe3）

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. Fusion of two painterly languages: Claude Monet dominant (70%), Paul Cézanne secondary (30%). oil painting in the style of Claude Monet, french impressionism, en plein air, broken comma-like brushwork with unblended strokes laid side by side, light-toned ground and high-key palette, coloured shadows (blue-violet) instead of black, atmospheric envelope unifying the whole scene, soft haze and shimmering water with broken reflections, asymmetrical cropped composition with no linear perspective and no three-dimensional modelling, water surface occupying a large portion of the canvas, sky and water mirroring each other, palette: pale blue, lavender, rose, cream, turquoise, soft green, pale yellow; soft edges dissolving between colour patches Late Cézanne landscape in the manner of his late period (1895–1906): the entire surface built from short, visible parallel brushstrokes (taches) of 0.5–1.5 cm equivalent, arranged in groups of 4–8 directional families that both model volume and unify the picture plane; forms constructed only by color modulation — light, half-tone and quarter-tone steps of ochre, orange, olive, viridian, cobalt and ultramarine — never by black shading; forms carry broken, multiple outlines, 30% of contour segments left open so forms merge into the background; a network of blue in shadows, contours and sky (12–15% of pixels); sky and earth painted with equal substance, no atmospheric recession, distant forms the same scale as near ones; shifting viewpoints within one frame; 5–8% of the canvas left thinly covered or bare, suggesting unfinish; dry, matte oil surface, fine canvas weave visible. Split the scene into two explicit layers at the horizon: the sky and the distant water layer follow the atmospheric envelope — soft haze, a gradual falling-off of contrast confined to this layer, colour gathered into one air tone; the mid-ground and foreground layer (rocks, waves, the lighthouse) follows the structural treatment — compressed space, near and far forms at the same scale, shifting viewpoints, and no fog or haze colour in this near layer.
```

## 3. N1 反约束一致性检查记录（组合前重算）

> 口径（conflicts.md §3 N1）：反约束段每条必须与画风段正向规则不矛盾；组合卡引入第二模块时必须重算——凡与新模块正向规则冲突的默认禁令，删除或改写，不许两条并存。本批对**两卡负向池（原文）逐条 × 两卡正向规则**核对；命中项按 N5 句式优先改写。改写仅解除「禁令 vs 正向」的字面矛盾，**不改变验收口径**（§4/§5 另述）。负向段未发送（通道无负向）。
> 计数口径：按词级条计（逗号分条）。

### 3.1 e2a（池 27 = 莫奈 12 + 梵高 15 → 一致 23 / 命中 4）

| # | 反约束（来源） | 对照画风规则 | 判定 | 处置（改写后，留档） |
|---|----------------|--------------|------|----------------------|
| 1 | `hard black outlines`（莫奈） | 梵高正向：`bold expressive outlines on key forms` | 冲突 | 限定：禁「无差别硬黑勾线」；关键形体上的表现性粗轮廓除外 |
| 2 | `pastel or muted earth palette`（梵高） | 莫奈正向：`light-toned ground and high-key palette`（pale blue/lavender/rose/cream…） | 冲突 | 删除 `pastel` 字样：禁「灰暗泥土色系」；高调浅色系不受限 |
| 3 | `smooth gradients`（梵高） | 莫奈正向：`atmospheric envelope`（雾色/对比梯度） | 冲突 | 限定：禁「空气刷式平滑渐变」；大气包络渐变除外 |
| 4 | `soft focus`（梵高） | 莫奈正向：`soft haze…soft edges dissolving` | 冲突 | 限定：禁「摄影式柔焦」；绘画性软边/大气柔度除外 |

一致项 23 条（逐条核对，无冲突）：
- 莫奈 11：chiaroscuro / dark varnished browns / smooth blending / photographic detail / crisp vector edges / studio lighting / neon saturation / 3D modelling / symmetrical centred composition / depth of field / HDR
- 梵高 12：photorealistic / airbrush / grey overcast light / thin transparent glazes / watercolour washes / 3D render / clean vector edges / perfectly symmetrical centred composition / depth of field / HDR / lens flare / fine detail miniature work
- 附注：`smooth blending`（莫奈禁）与梵高正向 `no smooth blending` 同向；`crisp vector edges`（莫奈）与 `clean vector edges`（梵高）同向——两卡表面倾向高度一致。

重算说明：表内 4 条按「处置」列替换 + 其余原样 = 组合卡负向段修订版（留档件；未发送）。

### 3.2 e2b（池 43 = 达·芬奇 13 + 卡拉瓦乔 30 → 一致 34 / 命中 9（归为 6 组））

| # | 反约束（来源） | 对照画风规则 | 判定 | 处置（改写后，留档） |
|---|----------------|--------------|------|----------------------|
| 1 | `crisp photographic edges`（达·芬奇） | 卡拉瓦乔正向：`one single hard directional light…`（硬光；C-01 半影口径） | 冲突 | 限定：禁摄影/数字脆边；显式声明的硬光受光边为例外（半影 ≤0.6% 短边；C-01 拆分口径） |
| 2 | `soft diffuse lighting`（卡拉瓦乔） | 达·芬奇正向：`single soft light from the upper left` | 冲突 | 限定：禁漫射环境光；单一柔方向主光除外 |
| 3 | `smooth airbrushed gradients`（卡拉瓦乔） | 达·芬奇正向：`wide, continuous grey gradient`（sfumato） | 冲突 | 限定：sfumato 过渡带除外 |
| 4 | `fog, haze`（卡拉瓦乔） | 达·芬奇正向：`dissolve into haze`（空气透视） | 冲突 | 分区限定：近景/中景禁雾霾；远景空气透视雾除外 |
| 5 | `visible brush strokes or impasto`（达·芬奇） | 卡拉瓦乔正向：`impasto highlights on the lit edges` | 冲突 | 限定：平滑区禁可见笔触；受光边缘厚涂高光除外 |
| 6 | `landscape, sky, daylight`（卡拉瓦乔） | 组合题材（T1 海景灯塔；原句适用域=室内题材） | 冲突（适用域） | 限定：禁「明亮白昼风景/开阔蓝天」；暗风暴场景不受限（N2 适用域原则） |

一致项 34 条（逐条核对，无冲突）：
- 达·芬奇 11：hard outlines / cel shading / comic linework / high saturation / neon colors / flat even lighting / multiple light sources / symmetric frontal pose / open-mouth grin or clear emotion / sharp geometric mountains / modern clothing
- 卡拉瓦乔 23：ambient light / multiple light sources / rim light / backlight / glow / bloom / lens flare / volumetric rays / evenly lit faces / bright background / symmetry / idealised anatomy / pastel palette / neon colours / cartoon / 3D render / photographic realism / motion blur / mirror / chandelier / candles visible in frame / halo disc / crowd
- 附注：`multiple light sources`（两卡同禁）、`flat even lighting`（达·芬奇禁）与卡拉瓦乔「violent chiaroscuro」同向——两卡在「单光源/反平光」上同侧；表面与明暗的镜像禁令集中在表内 1–5 组（即 C-01/C-02/C-03 家族）。

重算说明：表内 6 组按「处置」列替换 + 其余原样 = 组合卡负向段修订版（留档件；未发送）。

### 3.3 e2c（池 25 = 莫奈 12 + 塞尚 13 → 一致 23 / 命中 2）

| # | 反约束（来源） | 对照画风规则 | 判定 | 处置（改写后，留档） |
|---|----------------|--------------|------|----------------------|
| 1 | `atmospheric haze`（塞尚） | 莫奈正向：`atmospheric envelope…soft haze` | 冲突 | 分区限定：近景/中景禁雾；远景层包络除外（C-10 分区口径） |
| 2 | `smooth blended gradients`（塞尚） | 莫奈正向：`soft edges dissolving…`（包络梯度） | 冲突 | 分区限定：中近景块面禁平滑渐变；远景层包络除外 |

一致项 23 条（逐条核对，无冲突）：
- 莫奈 12：hard black outlines / chiaroscuro / dark varnished browns / smooth blending / photographic detail / crisp vector edges / studio lighting / neon saturation / 3D modelling / symmetrical centred composition / depth of field / HDR
- 塞尚 11：chiaroscuro / black cast shadows / single-point perspective / photorealistic detail / glossy varnish / palette-knife impasto (1860s) / narrative action / dramatic poses / facial expression detail / high-contrast lighting / neon colors
- 附注：`chiaroscuro`、`black cast shadows`、`single-point perspective`（塞尚禁）与莫奈「coloured shadows / no linear perspective」同向——两卡在「反学院明暗 / 反线性透视」上同侧；命中的 2 组正是 C-10 的负向段投影（雾与渐变）。

重算说明：表内 2 条按「处置」列替换 + 其余原样 = 组合卡负向段修订版（留档件；未发送）。

## 4. N4 判定（冲突轴：二选一 / 分区）

> 判别标准（conflicts.md §3 N4）：同一像素统计量（全帧均值/直方图占比/全帧计数）→ 不可拆，二选一；可分区域/对象类别 → 可拆，但必须写死分区表 + 掩膜定义，自查按掩膜分区统计。

### 4.1 e2a：无命中 C 条 → 无冲突轴

- 逐条核对两卡冲突注记所列 C 条（monet：C-05/C-06/C-10/C-14；van_gogh：C-05/C-09/C-12）——均以第三方模块为对手，本对不命中；§4 near-miss 表亦无命中。
- **判定：N4 不适用（无需二选一/分区）**。

### 4.2 e2b：C-01 / C-02（同轴口径）/ C-03 → 二选一（主=达·芬奇）

| 轴 | 主侧主张 | 辅侧主张 | 类型 | 判定 |
|---|---|---|---|---|
| 阴影硬度/反约束（C-01） | 达·芬奇：无硬边；过渡带 ≥1.5% 短边 | 卡拉瓦乔：单一硬光、亮部边界硬（半影 ≤0.6% 改写口径） | 反约束层（N1 改写，§3.2 表 1/2 行）+ 验收层单主 | 反约束互开例外后，验收归主：**达·芬奇持有** |
| 明暗过渡带宽度（C-02 同轴） | ≥1.5% 短边（软） | 硬边（≤0.6% 口径） | 同一像素统计量 → **不可拆 → 二选一** | **达·芬奇持有**；辅侧整条移除（验收）；本批未写分区表 |
| 直方图/中间调（C-03） | 中间调 ≥55%；纯黑+纯白 ≤3% | 中间带 ≤25%；暗带 ≥40%（含 §8.2-2/-3 背景压暗机制） | 同一统计量（全帧直方图）→ **不可拆 → 二选一** | **达·芬奇持有**；辅侧 §8.2-2/-3 整条移除（验收） |

- 注：C-02 正本为达·芬奇×米开朗基罗对；本格按同一「过渡带宽度」轴对卡拉瓦乔硬边口径执行同判（C-01 改写给出 2D 侧半影 ≤0.6% 的口径）。
- 实测见 §6/§7.2（原始融合下的单侧化结果）。

### 4.3 e2c：C-10 → 可拆（分层）→ 分区

| 轴 | 主侧主张 | 辅侧主张 | 类型 | 判定 |
|---|---|---|---|---|
| 深度衰减/空间（C-10） | 莫奈：大气包络（远景对比 ≤60%、单调梯度、色相收拢） | 塞尚：反大气透视（远近同尺度、空间压缩、无大气后退） | 可分区域（按地平线分层）→ **可拆 → 分区** | **分区：远景层=莫奈；中近景层=塞尚** |

**分区表（写死）**：

| 层 | 边界/掩膜 | 持有模块 | 标准（自查口径） |
|---|---|---|---|
| 远景层（天空+远海/远岸；地平线以上及线以下远景带） | 地平线分割（目检；脚本侧按地平线 y 分区） | 莫奈 | 远景对比 ≤60% 近景；单调对比度梯度（**仅本层拟合**）；色相向单一大气色收拢 |
| 中近景层（礁岩/浪/灯塔/近水面） | 同上（地平线以下中近景） | 塞尚 | 远近同尺度（高度比 ≥0.5）；多点透视；**无雾色** |

- 已按 C-10 要求①「显式写分层边界」写入 prompt（分区句，§2.3）；②（梯度仅远景层拟合）③（近景禁雾色）为自查口径。

## 5. N9 判定（组合卡验收口径）

> 口径（conflicts.md §3 N9）：逐帧自查表 = 主模块规则全集 + 辅模块**非冲突轴**规则；冲突轴上只保留持有者一行；「冲突轴上出现双标准」列为失败形态之一。

### 5.1 e2a：自查表 = 莫奈全集 + 梵高全集

| 模块 | 处置 | 明细 |
|---|---|---|
| 莫奈（主） | 全集保留 | §8.2 7 条（笔触/明度/色相/包络/倒影/构图/运动） |
| 梵高（辅） | 全集保留（无冲突轴 → 无移除） | §8.2 7 条（笔触单元/色数/厚涂/漩涡/星体/构图/反约束项） |
| 取值注记 | — | 笔触覆盖率 ≥95%（两卡同向取严）；色相簇 ≤8（取严）；梵高互补对保留「≥2 对出现」，「面积近 1:1」降为「≥1:3」（C-12 同类预防性取值，写明） |

**判定：无双标准（逐轴单标准）；无冲突轴行。**

### 5.2 e2b：自查表 = 达·芬奇全集 + 卡拉瓦乔保留 5 条

| 模块 | 处置 | 明细 |
|---|---|---|
| 达·芬奇（主） | 全集保留 | §8.2 7 条（无硬边/过渡带/中间调/低饱和/远景色偏/单光源/笔触不可见） |
| 卡拉瓦乔（辅） | **移除 2 条** | §8.2-2 背景明度上限、§8.2-3 中间调压缩（直方图/明暗分布轴，C-03） |
| 卡拉瓦乔（辅） | 保留 5 条 | §8.2-1 光源单一性、-4 光斑三处、-5 贴平面、-6 定格、-7 暗部保细节 |
| 取值注记 | — | 环境光/补光上限取严 ≤5%（辅卡）；纯黑占比取严 ≤3%（主卡）；对象映射：脸/手/关键道具 → 灯室/礁岩/浪峰（题材映射注记） |
| 冲突轴单主行 | — | 过渡带/半影 ≥1.5% 短边（主）；直方图中间调 ≥55%（主） |

**判定：无双标准（冲突轴单主 + 其余轴显式取值）；「半影宽度」按主模块口径列入自查（C-01 验收项）。**

### 5.3 e2c：自查表 = 莫奈全集 + 塞尚全集（深度轴按分区表）

| 模块 | 处置 | 明细 |
|---|---|---|
| 莫奈（主） | 全集保留 | §8.2 7 条 |
| 塞尚（辅） | 全集保留（8 条） | §8.2 1–8；其中 §8.2-5（空间）**按分区表适用**：仅中近景层 |
| 深度轴 | 分区表（§4.3） | 远景层=莫奈包络；中近景层=塞尚压缩——各层单标准 |
| 取值注记 | — | 笔触覆盖率 ≥90%（两卡交集 90–100%）；笔触长取交集 [8,12] px；阴影/轮廓蓝取交集 H 220–250 |

**判定：无双标准（深度轴按掩膜分区、各层单标准）。**

## 6. 冲突轴上是否出现双标准——判定

> 失败形态（N9）：「冲突轴上出现双标准」。两级检查：**卡/表层面**（设计）与**输出层面**（9 张目检）。

**卡/表层面**（N3/N4/N9 落地后逐格核对）：

| 格 | 冲突轴 | 持有 | 对方处置 | 表内双标准？ |
|---|---|---|---|---|
| e2a | 无 | — | — | 无 |
| e2b | 过渡带/半影 | 达·芬奇 | 卡拉瓦乔硬边条移出验收 | **无** |
| e2b | 直方图/中间调 | 达·芬奇 | 卡拉瓦乔 §8.2-2/-3 移除 | **无** |
| e2c | 深度/空间 | 分区（远=莫奈 / 中近=塞尚） | —（分区表+掩膜） | **无** |

**输出层面**（9 张目检；单评审描述性）：

- **e2a：未出现。** 全画面单一笔触/色彩标准；无「硬黑勾线 vs 表现性轮廓」「高调色系 vs 灰暗泥土」的拉扯。
- **e2b：未出现并存；但实测「单侧化」**——硬度轴取软侧（未见刀切式硬边亮部）、直方图轴取暗侧（暗部主导，更接近辅侧压缩）。即：输出没有同时按两套标准执行，而是各轴各取一侧——支持「不可拆轴」判定（二选一成立），并暴露「原始融合下输出可能落辅侧（直方图）」这一风险（生成侧若不显式约束，主持有标准不自动达成）。
- **e2c：未出现。** 近景无雾、色块饱和；远景带呈浅色收拢——按分区表各层单标准呈现；未见「近景雾+远景压平」式分裂。

**汇总：三格均未出现「冲突轴上双标准」**（设计层零容忍达成；输出层未观测到该失败形态；e2b 的「单侧化」另行记录，不属双标准）。

## 7. 输出观察（9 张目检；单评审描述性）

### 7.1 e2a（莫奈主 × 梵高辅）——融合成立

- **img_01**：灯塔居左崖顶；天空钴蓝/奶油白大漩涡 + 2–3 枚带同心光环的发光黄「星/日」（梵高母题）；巨浪拍岩、白色泡沫；高调浅色系（粉/薰衣草点缀）；全画面厚涂。
- **img_02**：灯塔居右、灯室发光；粉/薰衣草/蓝云涡；海面碎笔触泡沫；高调柔亮；厚涂明显。
- **img_03**：多枚光环星体；粉/奶油/蓝天空；灯塔居中；蓝绿海面 + 亮泡沫；黄绿礁岩。
- **总评**：单一画面、无撕裂——梵高贡献厚涂/漩涡/星体光环/蓝黄互补；莫奈贡献高调浅色系与色块并置的柔化统一。风暴感被改写为「发光黄昏/星夜」氛围（云亮、有星），浪仍汹涌。N1 改写方向与输出相符（无硬黑勾线、无摄影柔焦、无空气刷渐变）。

### 7.2 e2b（达·芬奇主 × 卡拉瓦乔辅）——两语言均在场、单侧化

- **img_01**：暗调海景：单一高位左上光（暖赭云隙光）；背景近黑；礁岩赭褐；海面白沫；远处礁石在雾中（左）；边缘柔和、无刀切；表面平滑无厚涂。
- **img_02**：同类；更柔；灯室未亮；暗部大片；远礁雾化。
- **img_03**：大浪拍岩（右）；暖光斑；赭褐礁岩；整体暗。
- **总评**：卡拉瓦乔=明暗结构（单光源、近黑背景、戏剧性）；达·芬奇=表面与过渡（软边、雾化远景、平滑表面、土色域）。未见硬边亮部（辅侧硬光标准未实体化为半影）；直方图整体偏暗（暗部主导，更接近辅侧压缩）——硬度轴取主（软）侧、直方图轴取辅（暗）侧的单侧化组合；主模块「中间调 ≥55%」未达成（原始融合结果，待生成侧约束复验）。

### 7.3 e2c（莫奈主 × 塞尚辅）——分区方向一致

- **img_01**：全画面短笔触 taches；灯塔居左；蓝/薰衣草/奶油/粉天空；赭/橙/橄榄崖壁 + 蓝网；海面蓝白；地平线远海浅色带。
- **img_02**：灯塔居右；薰衣草/奶油云；崖壁 taches（赭+蓝）；远海浅带（左）。
- **img_03**：灯塔居右；大浪；赭/橄榄礁岩；薰衣草/蓝天空。
- **总评**：近/中景=饱和色块体块（塞尚），无雾色；远景带=浅色收拢（莫奈包络）；空间压缩感（地平线偏高、远近尺度接近）。tache 笔触与高调色系高度融合，未见「近景雾+远景压平」分裂。分区解法目检可判分。

### 7.4 C 条初判（实测线索；定案归 conflicts.md 正本更新）

| C 条 | 初判 | 依据（本批实测） |
|---|---|---|
| C-01（硬阴影/反约束） | **CONFIRMED（口径可用）** | 负向段 2 处互开例外（§3.2 表 1/2 行）；输出未出现「未声明硬阴影」退化 |
| C-02 同轴（过渡带宽度） | **CONFIRMED（互斥）** | 输出未同时呈现 ≥1.5% 与 ≤0.6% 两套；取软侧 |
| C-03（直方图/中间调） | **CONFIRMED（不可拆/二选一）** | 输出单侧化（暗侧），两标准未能同时满足；附注：原始融合下输出落辅侧——生成侧需显式约束主口径 |
| C-10（深度衰减） | **初步支持（分区可判分）** | 近景无雾 / 远景收拢，分区方向一致；像素级 R²/对比度比待自动化复核 |

（以上为单评审目检的初步判定，供主脑收口时参考；像素级复核见 §8。）

## 8. 缺口与偏差

1. **评分口径**：本报告为单评审（agent 目检）描述性观察；design.md §5 六维人评打分（构图/造型/色彩/笔触/情绪/响应度）待评分者补。
2. **生成侧未加「验收侧单主」约束**（除 e2c 分区句）——本批设计为「原始融合尝试」，e2b 直方图轴的实测单侧化即其数据；如需按主模块口径达标，需在生成侧显式约束（后续批）。
3. **像素级判据未自动化**：半影宽度、直方图占比、覆盖率、梯度 R² 等未测量——本批为目检描述；建议接 §8.2 自查脚本（E 系列后续）。
4. **负向段未发送**（通道无负向）：N1 记录为组合卡层留档；其对生成的影响无法直接观测。
5. **计数口径注**：N1 池按词级条计（逗号分条；e2b 表内 `fog, haze`、`landscape, sky, daylight` 各归为一组展示）；机读版见 `combo_records.json`。
6. **C 条初判为描述性**：CONFIRMED/OVERTURNED 定案与回填（conflicts.md §3、style_card、design.md 三处同步）归主脑/后续复核。

## 9. 文件清单与复现

- `cells/<cell>/`：`req_*.json` / `resp_*.json` / `img_*.jpg`（3 格 × 3 组；**req/resp 原样留档**、未做清洗；本批 0 失败尝试文件）
- `sheet_e2a_monet_van_gogh.png` · `sheet_e2b_da_vinci_caravaggio.png` · `sheet_e2c_monet_cezanne.png` · `sheet_all_e2.png`（3 行总表）
- `prompts_e2.json`（prompt 单一来源 + 段落 sha）· `combo_records.json`（N1/N4/N9 机读版）· `stats_e2.json` · `run_log.jsonl` · `sha256_manifest_e2.txt`
- 脚本链：`_extract_prompts_e2.py` → `_gen_e2.py batch`（重试 ≤2、间隔 0.8s）→ `_sheets_e2.py` → `_manifest_e2.py` → `_verify_e2.py`（验收）
- 复现：`python _extract_prompts_e2.py && python _gen_e2.py batch && python _sheets_e2.py && python _manifest_e2.py && python _verify_e2.py`
- 模块卡校验回归：`python knowledge/domains/painters/modules/_extract.py --check` → `checks=33 ok=33 fail=0`

## 10. 机械核验（2026-10-15）

运行 `python _verify_e2.py`：

```text
① 图片: 9 个 img_*.jpg（期望 9）；打开失败 0；哈希重复组 0
② req/resp: req 9 / resp 9（期望各 9）；失败尝试文件 req 0 / resp 0
③ RESULTS_E2.md: 关键词缺 无；缺格 无；融合句出现 4 次；prompt sha 前8命中 {'e2a_monet_van_gogh': True, 'e2b_da_vinci_caravaggio': True, 'e2c_monet_cezanne': True}；prompt 全文缺 无
④ sheet_all_e2.png: 存在 944x1020
④ sheet_<cell>.png: 3/3
⑤ prompts_e2.json 重抽复核: 一致
⑥ combo_records.json: OK（cells=['e2a_monet_van_gogh', 'e2b_da_vinci_caravaggio', 'e2c_monet_cezanne']）
⑦ 模块卡逐字校验: ok=33 fail=0

VERIFY PASS — 9/9 张 + RESULTS_E2.md（N1/N4/N9/双标准） + sheet_all_e2 + 3 格 sheet + 重抽复核 + 逐字校验(33/33) 全部就位。
```

---

> 落款：ComboTest（wave8）· 2026-10-15 · 产物自校验可复跑（见 §9）；引用请带路径。
