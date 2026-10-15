# 荷尔拜因 模块卡 — `holbein`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/holbein.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **物证级表面（材质全息）**：同画 ≥3 类材质各有专属高光／纹理签名（缎面宽高光、毛皮逐根、金线逐股）——「a supreme display of Holbein's skill」
2. **净面（无排线、无笔触纹）**：hatching＝0、纹理尺度 <2px——明暗由薄层罩染平滑过渡；表面如珐琅（高抛光底色透出）
3. **「外硬内柔」边缘＋静默面容**：轮廓梯度带 ≤2px、面部过渡 ≥2% 短边；面部动作单元≈0、瞳孔高光点精确——「冷静」两派读法并存
4. **属性清单＋文字入画＋几何构图**：可辨识道具 ≥3 件（刻度／文字可读）；画内文字 ≥1 处、字符 ≥1% 画高；中轴锚点 ±5%、三角／圆形结构线 ≥1 组
5. **平面背景＋受控畸变**：背景为单色／织纹平面（无纵深）；变形骷髅等「须特定条件才成立」的装置 ≥1——常态面积 ≤8%、不干扰主体

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Holbein-style portrait precision — evidence-grade surface, objective stillness:
one or two sitters, posed calmly and symmetrically, half-length or full-length,
faces still and closed-mouthed, gaze level at the viewer, no emotion performed,
painted as if from life — likeness first, no flattery;
every material delivered to the touch: satin with broad soft sheen, fur with individual hairs,
gold thread painted strand by strand, glass and metal with precise small highlights,
linen, velvet, parchment, wood — each with its own light signature;
clean edges, enamel-smooth surface, no hatching, no visible brushstrokes,
modelling by thin translucent glazes only;
flat background — plain blue, green damask curtain, or neutral wall; no landscape depth;
even soft single light, no hard cast shadows, dark areas keep their detail;
identity encoded by objects: a table of instruments, books with readable spines,
letters, a flower, a dagger, gloves — each object legible, each detail countable;
painted inscriptions: signature, date, age, a motto on a functional surface
(floor, book edge, sheath, headband);
at most one quietly hidden device — a crucifix behind a curtain,
a slip reading Veritas odium parit, or an anamorphic shape readable from one side;
palette of deep black, crimson, gold, blue-green and warm flesh —
saturated darks, restrained mid-tones, texture over colour
```
**负向约束（`--no` 风格）**
```
--no hatching, crosshatching, engraved line shading, visible brushstrokes, impasto,
rough texture, palette-knife marks,
hard cast shadows, theatrical chiaroscuro, single hard spotlight, candlelit darkness,
tenebrism, glowing skin, psychological light pools,
stormy sky, dramatic weather, landscape depth, open window views, genre action,
crowds, narrative gesture, exaggerated expression, open mouths, tears,
neon, high-saturation complementary vibration, rainbow palette,
ornamental gold flat pattern, decorative flattening,
systematic elongation or distortion beyond the single controlled device,
cartoon, anime, 3D render, HDR gloss
```

## 代码艺术规则（§8.2 原样）

1. **净面规则**：hatching/crosshatching 检出 = 0；可见笔触覆盖率 ≤5%；表面纹理以 <2px 尺度为主（无粗肌理）。自查：方向滤波器 + 频域能量统计。（依据：§1-2；与丢勒分工轴）
2. **「外硬内柔」边缘规则**：物体边界梯度带宽 ≤2px（1000px 参考帧）；面部内过渡带宽 ≥2% 短边；边界外 3px 内无 >30% 的中间值羽化带。自查：梯度剖面抽样。（依据：§1-3）
3. **材质分化规则**：≥3 类材质各自高光签名可分类（缎=宽软高光；毛皮=纤维级纹理+软阴影；金=点/线状高光；玻璃=小镜面点；纸=低反差微纹理）；每类面积 ≥5%。自查：高光形状分类 + 纹理统计。（依据：§1-1）
4. **物证清单规则**：≥3 件道具/文字，每件达「可读」标准（文字 OCR 置信 ≥0.8，或仪器刻度可数）；人物-道具接触关系 ≥1 处（肘靠/手按/持握）。自查：OCR + 接触点检测。（依据：§1-6）
5. **铭文规则**：画内文字字符高度 ≥ 全画高 1%；位于功能表面（地面/书页/书脊/鞘/头带）；≥1 处为「自指」（签名/年龄/箴言）。自查：文字框高度 + 载体分类。（依据：§1-7）
6. **软光规则**：无画内光源（高亮连通域 ≥2 或成带状）；阴影边界带宽 ≥2% 短边；暗部 V ≥0.05；亮度阶跃 ≤10%/px（无硬切投影）。自查：亮度质心 + 阶跃检测。（对照 C-01：与卡拉瓦乔硬光侧显式互斥）
7. **几何构图规则**：中轴 ±5% 有锚点（物台/人物/装置）；可检出对称或三角/圆结构线 ≥1 组。自查：Hough 直线 + 对称性检验。（依据：§1-9）
8. **变形装置规则（可选，启用时）**：变形元素面积 ≤8%；正常视角下为「干扰色块」（主体读解不受损）；斜视角/仿射校正后与目标形状 **IoU ≥0.5**。自查：仿射校正 + IoU。（依据：§1-10；《大使们》骷髅）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **物证级细节密度**`[归纳]` | 简化表面：面部/手为主，服饰概括（早期/素描感档） | 标准完成度：面部+服饰+2–3 件道具 | 全交付：每根毛、每股金线、每针脚（《大使们》档） | **70%** |
| P2 | **净面程度（无排线/无笔触）**`[归纳]` | 轻微肌理可见（草图感/早期档） | 干净表面（标准肖像档） | 珐琅级净面（《大使们》《克里斯蒂娜》档） | **65%** |
| P3 | **情绪克制（客观度）**`[归纳]` | 微表情、有温度（早期肖像档） | 静默标准：注视、口闭、无动作 | 面具级静默（《克里斯蒂娜》《安妮》档） | **60%** |
| P4 | **铭文/文本密度**`[归纳]` | 0–1 处（仅签名） | 1–2 处（签名+年龄/箴言） | ≥3 处（签名+年龄×2+书签+铭牌；《大使们》档） | **50%** |
| P5 | **光线档**`[归纳]` | 高调均匀（近无影平光） | 单向柔光（默认） | 较强定向但仍软边（无硬切投影） | **55%** |
| P6 | **隐藏装置强度（变形/象征）**`[归纳]` | 无（纯肖像档） | 象征隐藏（十字架、书签、暗喻物） | 全面变形元素（骷髅级）+ 观看角度设计 | **30%** |

> **用法**：P1/P2/P3 定「是不是荷尔拜因」（三条中 ≥2 条 ≥ 中档才成立）；P4/P5 定文本与光档；P6 是可选装置（多数作品在「中」以下——不要为了荷尔拜因硬塞变形）。**越界警报（与 §3.1 对齐，组合实验按此判分）**：① 出现**排线/交叉排线** → 越界丢勒；② 出现**硬切光斑/戏剧投影/烛光** → 越界卡拉瓦乔（或拉图尔/伦勃朗）；③ 出现**可见厚涂笔触/肌理表达** → 越界伦勃朗/梵高；④ 出现**全画系统性拉长**（非单点变形） → 越界格列柯；⑤ 出现**装饰金平面+图案化** → 越界克里姆特；⑥ 出现**高彩度补色并置** → 越界梵高。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 丢勒）**（× 丢勒；本卡 §3.1 分工条款）：线的密度 vs 材质的物证：排线明暗 vs 净面罩染——判据四条＋边界注（≥2 轴联合）；同屏「谁管线、谁管面」
- **分工（vs 伦勃朗）**（× 伦勃朗；本卡 §3.1 分工条款）：客观 vs 心理：信息照明 vs 情感照明——判据四条＋边界注（心理是否被画内光／笔触承载）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影（无硬阴影／软光侧）／C-05 笔触（近无笔触侧）／C-12 色相预算（低饱和＋深黑＋金，靠材质不靠彩度）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/holbein.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
