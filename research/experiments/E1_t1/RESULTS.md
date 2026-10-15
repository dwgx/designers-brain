# E1_t1 · E0+E1 首批图像实验（T1「暴风雨中的海边灯塔」）

> **E-01**（wave7）· 2026-10-15 · 直连网关 `/v1/images/generations` · 模型 `grok-imagine-image-2.0`
> 12 格 × 3 张 = **36/36 张**；重试 1 次、失败 1 次（总尝试 37）。
> 配方：`prompt = 主题句 + " " + 模块卡 §8.1 英文正向段`（逐行解包为单行）；负向段未随请求发送（通道无负向参数，见 §3）。
> 主题句（全格逐字一致）：`A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead.`

## 1. 结果总表（12 行）

| # | 格 | 模块 | 模型 | 尺寸（请求 → 实回） | 耗时 | sha256 前 8 位（img_01 / 02 / 03） |
|---|----|------|------|--------------------|------|-----------------------------------|
| 1 | e0_baseline | 基线（无风格段） | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 51.2s（均 17.1s/张） | 71c50d88 / 2fa08527 / 75bdf061 |
| 2 | e1_da_vinci | 达·芬奇 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 65.0s（均 21.7s/张） | 1530216e / 7a6add24 / a90063d5 |
| 3 | e1_michelangelo | 米开朗基罗 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 72.4s（均 24.1s/张） | 98b89e61 / 8e4f902e / ed1c573b |
| 4 | e1_van_gogh | 梵高 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 55.2s（均 18.4s/张） | 68e9179b / 48e59bbc / 2a7dd4cd |
| 5 | e1_monet | 莫奈 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 54.0s（均 18.0s/张） | 9893ec7c / 7c830f5d / 6ed446e6 |
| 6 | e1_picasso | 毕加索 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 69.1s（均 23.0s/张） | d3c4e39d / 077f72c3 / 26d33b07 |
| 7 | e1_cezanne | 塞尚 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 74.5s（均 24.8s/张） | 3f449509 / 59135bee / d859d1ab |
| 8 | e1_matisse | 马蒂斯 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 53.1s（均 17.7s/张） | a10577b7 / 45b2623c / 5b223c90 |
| 9 | e1_hokusai | 葛饰北斋 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 58.8s（均 19.6s/张） | fff67728 / db05e27e / 68cd70a8 |
| 10 | e1_caravaggio | 卡拉瓦乔 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 71.6s（均 23.9s/张） | ab6ab90a / 9542c47e / acb1a310 |
| 11 | e1_vermeer | 维米尔 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 72.0s（均 24.0s/张） | 355e5bab / 150d4630 / 906e48d8 |
| 12 | e1_durer | 丢勒 | grok-imagine-image-2.0 | 1024x1536 → 768×1152×3 | 79.8s（均 26.6s/张） | cbf0f822 / 2c0a3912 / b296869c |

耗时口径：该格全部尝试的「请求→落盘」时长合计（含重试尝试；不含请求间隔与重试等待）；明细见 `run_log.jsonl`。

## 2. 每格 prompt 全文

> 下为实际发送的 prompt 全文（`req_*.json` 内为原样请求体）。负向段原文一并附上（未发送，备查）。

### 1) e0_baseline — 基线（无风格段）

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead.
```

### 2) e1_da_vinci — 达·芬奇

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. Renaissance oil painting in the manner of Leonardo da Vinci, sfumato: absolutely no hard contours anywhere, every light-to-shadow transition is a wide, continuous grey gradient, soft smoky modelling; single soft light from the upper left moulding the figures out of deep shadow; figures emerge from a dark grotto-like ground; aerial perspective — distant mountains turn blue-grey, lose saturation and dissolve into haze; narrow earth palette of ochre, umber, muted blue and dull gold, overall low saturation; a young woman seated in three-quarter view, her arms, torso and head each subtly turned in slightly different directions, arrested mid-motion; an ambiguous half-smile that suggests emotion without revealing its cause; soft curly hair falling in continuous ribbons; rocks shaped like rounded cones, wet atmosphere over shallow green water; flowers and plants that are hybrids of several species, not any real plant; invisible brushwork, glazed surface, matte, aged varnish warmth; contemplative, quiet, mysterious mood
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
--no hard outlines, --no cel shading, --no comic linework, --no high saturation, --no neon colors, --no flat even lighting, --no multiple light sources, --no visible brush strokes or impasto, --no crisp photographic edges, --no symmetric frontal pose, --no open-mouth grin or clear emotion, --no sharp geometric mountains, --no modern clothing
```

### 3) e1_michelangelo — 米开朗基罗

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. High Renaissance fresco in the manner of Michelangelo Buonarroti: colossal muscular nude figures, heroic anatomy with clearly defined muscle groups, bodies locked in serpentine torsion — shoulders rotated against hips, spine forming an S-curve; figures designed to be seen from below, strong foreshortening, monumental scale; sculptural modelling — forms look chiselled out of the surface, hard-edged cast shadows, relief-like light and shadow; dense swirling composition of many interlocking figures rotating around a calm central axis; heavy clinging drapery that reveals the body underneath; idealised faces, grave and intense, no soft smiles; limited fresco palette of flesh tones, earthy ochre, muted green, pale violet and sky blue, matte plaster surface; an atmosphere of awe and terribilità
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
--no sfumato haze, --no soft blurry edges, --no slender or effeminate bodies, --no chubby childlike proportions, --no anime/manga faces, --no smiling serene faces, --no pastel high-key palette, --no decorative ornament or gold leaf, --no landscape backgrounds dominating the scene, --no visible impasto or painterly brush texture, --no modern clothing, --no symmetric frontal standing pose
```

### 4) e1_van_gogh — 梵高

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. oil painting in the style of Vincent van Gogh, post-impressionist, thick impasto oil paint with visible brushstrokes and canvas weave, swirling turbulent sky of cobalt and ultramarine with glowing lemon-yellow stars ringed by concentric halos, complementary colour pairs (yellow/blue, orange/blue) laid side by side, flame-like cypress rising almost to the top edge, wheat field of short directional strokes, flat decorative space with cropped asymmetric composition inspired by Japanese woodblock prints, bold expressive outlines on key forms, colour used arbitrarily to express feeling rather than to reproduce the scene, no smooth blending, palette: cobalt blue, ultramarine, chrome yellow, lemon yellow, viridian, vermilion, pure white highlights
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
photorealistic, smooth gradients, airbrush, soft focus, pastel or muted earth palette, grey overcast light, thin transparent glazes, watercolour washes, 3D render, clean vector edges, perfectly symmetrical centred composition, depth of field, HDR, lens flare, fine detail miniature work
```

### 5) e1_monet — 莫奈

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. oil painting in the style of Claude Monet, french impressionism, en plein air, broken comma-like brushwork with unblended strokes laid side by side, light-toned ground and high-key palette, coloured shadows (blue-violet) instead of black, atmospheric envelope unifying the whole scene, soft haze and shimmering water with broken reflections, asymmetrical cropped composition with no linear perspective and no three-dimensional modelling, water surface occupying a large portion of the canvas, sky and water mirroring each other, palette: pale blue, lavender, rose, cream, turquoise, soft green, pale yellow; soft edges dissolving between colour patches
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
hard black outlines, chiaroscuro, dark varnished browns, smooth blending, photographic detail, crisp vector edges, studio lighting, neon saturation, 3D modelling, symmetrical centred composition, depth of field, HDR
```

### 6) e1_picasso — 毕加索

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. Analytic Cubist portrait in the manner of Picasso, autumn 1910: a seated man fractured into 40–120 semi-transparent angular planes; figure and background merge into one shallow, crystalline lattice; 3–5 simultaneous viewpoints per object; a few recognizable anchors survive (a wave of dark hair, the knot of a tie, a watch chain, hands clasped in the lap); palette restricted to 4–5 hues — ochre, umber, warm grey, slate, black — with at least 6 value steps; form modeled only by value jumps between flat planes, no gradients; matte oil-on-canvas surface, fine canvas weave; brightest values concentrated at the center, dark aura toward the edges; traditional seated pose preserved; composition reads as monumental, melancholic, frontally posed.
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
--no single-point perspective, photorealistic rendering, airbrushed shading, smooth gradients, saturated complementary colors, decorative floral patterns, 3D-rendered lighting or drop shadows, glossy surfaces, visible brushwork impasto, text or signage, lens vignette, chromatic aberration
```

### 7) e1_cezanne — 塞尚

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. Late Cézanne landscape with a still-life foreground, in the manner of the Bathers period (1895–1906): the entire surface built from short, visible parallel brushstrokes (taches) of 0.5–1.5 cm equivalent, arranged in groups of 4–8 directional families that both model volume and unify the picture plane; forms constructed only by color modulation — light, half-tone and quarter-tone steps of ochre, orange, olive, viridian, cobalt and ultramarine — never by black shading; objects carry broken, multiple outlines, 30% of contour segments left open so forms merge into the background; a network of blue in shadows, contours and sky (12–15% of pixels); sky and earth painted with equal substance, no atmospheric recession, distant forms the same scale as near ones; slightly tipped tabletop and shifting viewpoints within one frame; 5–8% of the canvas left thinly covered or bare, suggesting unfinish; dry, matte oil surface, fine canvas weave visible.
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
--no chiaroscuro, black cast shadows, single-point perspective, atmospheric haze, photorealistic detail, smooth blended gradients, glossy varnish, palette-knife impasto (that is the 1860s style), narrative action, dramatic poses, facial expression detail, high-contrast lighting, neon colors
```

### 8) e1_matisse — 马蒂斯

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. paper cut-out composition in the manner of Matisse's late gouache découpée: flat opaque gouache colours, shapes cut with scissors from hand-painted paper, absolutely no shading, no gradients, no outlines, no drop shadows; a small set of 5-7 fully saturated colours (ultramarine blue, cadmium red, emerald green, lemon yellow, black, white); large interlocking organic silhouettes; every curve answers to an implied vertical axis; generous white paper ground visible between shapes (at least 20% of the surface); whole composition legible at a glance; poster-like flatness, matte surface, slightly irregular scissor edges; dancer / snail / leaf / star motifs allowed
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
--no gradient, airbrush, soft edges, blur, glow, outline stroke, drop shadow, 3D render, realistic lighting, cast shadow, perspective vanishing point, more than 8 hues, muddy mixed greys, texture noise, photographic detail, cluttered micro-detail, symmetrical centred layout, crosshatching
```

### 9) e1_hokusai — 葛饰北斋

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. Japanese ukiyo-e woodblock print in the manner of Hokusai's late landscape prints: flat colour areas printed inside a single uniform-width black keyline; no hatching, no rendering, no gradients except a fine bokashi fade in the sky; dominant Prussian blue with indigo, white paper reserved for foam and snow, muted ochre/grey/black accents; asymmetric composition built on one strong diagonal; one dominant motif (wave / wind / waterfall / rain) drawn as a family of nested curves, each small curve repeating the big one; distant Mount Fuji reduced to 1/4 of the foreground element and pushed off-centre; tiny silhouetted figures with at most six detail lines; at least 35% untouched sky or water; visible woodblock grain and slightly misregistered colour plates
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
--no gradient shading, airbrush, soft blending, photorealistic water simulation, 3D render, perspective vanishing-point realism, hatching/crosshatching, more than 7 hues, warm colour cast, muddy earth palette, centred symmetrical layout, large detailed faces, dramatic rim light, cast shadows, lens flare, texture noise, western oil-painting brushwork, glowing highlights, cluttered background
```

### 10) e1_caravaggio — 卡拉瓦乔

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. Caravaggio-style tenebrist oil painting: one single hard directional light from high left, no fill light, no reflected light; background walls and floor in near-black shadow (values under 10% of the lit highlights); deep dark brown ground left visible inside the shadows as their mid-tone; violent chiaroscuro: lit passages bright and warm, shadows crushed, midtones suppressed; one frozen instant of a narrative action; faces and hands catch the light; gestures point at the narrative object; figures pushed flat against the picture plane, half-length or three-quarter figures cropped by the frame edge; ordinary working people as saints — weathered faces, torn clothes, dirty fingernails, contemporary 17th-century Roman clothing; plain dark interior, no landscape, no sky; restrained earth palette — ochre, madder red, lead white, bitumen black, one or two saturated accents on a prop; direct painting, broad final touches, impasto highlights on the lit edges
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
--no soft diffuse lighting, ambient light, multiple light sources, rim light, backlight, glow, bloom, lens flare, volumetric rays, evenly lit faces, bright background, landscape, sky, daylight, symmetry, idealised anatomy, smooth airbrushed gradients, pastel palette, neon colours, cartoon, 3D render, photographic realism, motion blur, fog, haze, mirror, chandelier, candles visible in frame, halo disc, crowd
```

### 11) e1_vermeer — 维米尔

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. quiet Dutch Golden Age interior genre scene, single figure (one or two people) absorbed in a silent everyday action, soft natural daylight entering from a single window on the LEFT, large pale plaster wall catching the light, high-key tonality, deep shadows rendered as flat unmodulated areas of cool blue-grey paint (no detail inside shadows), dominant colour pair of natural ultramarine blue and ochre yellow with tiny red accents, specular highlights painted as small round globular dots (pointillés) on porcelain, pewter, brass, pearls and bread crust, soft edges with no hard contour lines (sfumato, details deliberately omitted), matte and glossy surfaces distinguished only by the shape of their highlights, single-point perspective grid of tiled floor (29.3 cm tiles) and leaded window frames, thin translucent glazes over a light grey ground, smooth levigated paint surface with the canvas weave barely visible, dark neutral or deep green backdrop pushing the figure forward, timeless stillness, 17th-century Delft domestic world, oil on canvas, museum-quality
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
--no harsh chiaroscuro, hard black shadows, pure black, rim light, multiple light sources, warm tungsten light, high dynamic range, glossy varnish reflections, visible impasto in flesh, thick outlines, cel shading, saturated primary palette, neon colours, crowded composition, motion blur, speed lines, text, watermark, signature, modern objects, fantasy elements
```

### 12) e1_durer — 丢勒

```text
A lighthouse on a rocky coast in a storm, towering waves crashing against the rocks, dark storm clouds overhead. Northern Renaissance engraving in the manner of Albrecht Dürer's burin master prints (1513-1514): pure black ink line work on warm off-white paper, no grey fill anywhere - every tone is built from parallel hatching and layered cross-hatching; hatching lines follow and wrap each volume; cross layers sit at 30-45 degrees; line spacing tapers from about 6px in the lights to 1.5px in the darks (1000px wide frame), darkest zones get 3 or more superimposed hatch directions; engraved lines swell slightly mid-stroke and end in fine points; hard contour lines separate every form: no soft edges, no sfumato, no airbrush; hyper-detailed microtexture - individual hairs, grass blades, leaf veins, stone pores; backgrounds closed with dense parallel line fields instead of empty space; calm measured figures in contrapposto with stated head-to-body proportions; a small dated monogram plate (AD-like initials) and an invented Latin cartellino; allegorical objects placed as a dense still-life of symbols (compass, sphere, ladder, hourglass, bell, magic square) when the theme is allegorical
```

负向段（`--no`，通道不支持负向参数、未发送；原文备查）：

```text
--no color, --no greyscale gradients, --no smooth shading, --no airbrush, --no sfumato, --no soft focus, --no bokeh, --no photographic rendering, --no painterly brushwork, --no digital halftone dots, --no cel shading, --no manga screentone, --no uniform line weight, --no grey flood fill, --no floating glow, --no 3D render, --no empty white background areas, --no impressionist dabs
```

## 3. 缺口与偏差（gaps）

1. **负向段未发送**：本通道（grok-imagine 系）请求 schema 无负向参数——`negative_prompt` 字段实测不报错也不产生可核实效果（判定：未知字段被静默忽略）；故 §8.1 负向段不随请求发送，原文记录于 §2 与 `prompts.json`。
2. **provider 前缀（反直觉）**：直连 API 必须用**裸模型名** `grok-imagine-image-2.0`；带 `buddyfarm/` 前缀反而 `model_not_found`（2026-10-15 实测 2 次）。omp CLI 侧口径相反（须带前缀）——两侧勿混。
3. **size 参数不严格**：请求 `1024x1536`（映射 2:3），实回 768×1152×3——像素尺寸由上游决定，不严格等于请求值；本表按「请求 → 实回」双记。
4. **重试/失败**：重试 1 次、失败尝试 1 次——e1_michelangelo img_03 attempt 1: http 502: {"error":{"message":"上游服务暂不可用","type":"server_error","param":"","code":"upstream_unavailable"}}（重试后均已恢复；明细见 `run_log.jsonl` 与 `*_failN.*` 文件）。
5. **母题冲突（prompt 层观察，未干预）**：部分模块 §8.1 含人物母题（达·芬奇「young woman」、米开朗基罗「nude figures」、毕加索「seated man」、维米尔「interior figure」、卡拉瓦乔人物布光），与 T1 灯塔场景叠加后是否呈现「人物+灯塔」混合，留待人评（§5 维度）；按要求模块段原样保留（迁移性归 E4）。
6. **评分**：本表不含人评打分（design.md §5 六维：构图/造型/色彩/笔触与质感/情绪/响应度），待评分者补。
7. **媒体 URL**：生成后立即下载落盘（URL 有效期未核；与 B-20 卡口径一致，不复用旧 URL）。

## 4. 文件清单与复现

- `cells/<cell>/`：`req_*.json` / `resp_*.json` / `img_*.jpg`（每格 3 组；失败尝试另有 `*_failN.*`）
- `sheet_<cell>.png` ×12 · `sheet_all.png`（12 行总表）· `prompts.json` · `run_log.jsonl` · `sha256_manifest.txt`
- 脚本：`_extract_prompts.py` → `_gen.py`（重试 ≤2、间隔 0.8s）→ `_sheets.py` → `_report.py` → `_verify.py`（验收）
- 复现：`python _extract_prompts.py && python _gen.py batch && python _sheets.py && python _report.py && python _verify.py`
- 模块卡校验：`python research/prompts/artist_modules/_extract.py --check` → `checks=33 ok=33 fail=0`（2026-10-15 复核）

## 5. 机械核验（2026-10-15）

- 图片文件：**36/36 存在**；Pillow 打开校验 36/36 通过；sha256 去重后 36 个（全部唯一）。
- 请求/响应 JSON：req 36 份 / resp 36 份（均含于各格目录）。
- 全量哈希：`sha256_manifest.txt`。
- 验收脚本：`python _verify.py` → `VERIFY PASS`（36/36 张 + 12 行表 + sheet_all.png + 12 格 sheet 全部就位）。

---

> 落款：ESeriesT1（wave7）· 2026-10-15 · 产物自校验可复跑（见 §4）；引用请带路径。
