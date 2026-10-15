# 弗里达·卡罗 模块卡 — `kahlo`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/kahlo.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **自传性主角＋正面凝视/镜像构图**：自画像 55–60 两种计数并存；正面/近正面、目光直视观者；构图源自镜中像（病床上方装镜、以镜作画）
2. **象征身体（器官化）＋血线/根/藤**：外露心脏血管、钉子石膏柱、飞床胎儿、鹿身；血管/脐带/根须式连线——红＝血与生命同一种红
3. **墨西哥民间色（饱和平涂）＋服饰身份符号**：高饱和色区平涂并置（洋红/钴蓝/翠绿/黄/血红）、少混合少渐变；Tehuana 裙/huipil/玉石/花饰为固定构件
4. **压缩舞台/植被墙＋小画幅近距离**：主体夹在画面平面与植被墙之间的窄空间；尺幅多 30–60 cm 级（「intimate scale」，与壁画家巨幅对照）
5. **双身/分身＋题字绶带＋痛苦与生命力并置**：自我一分为二（两颗心相连）；绶带/字条书写文字与日期；黑幽默与「Viva la Vida」

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
Mexican modernist self-portrait painting in the manner of mid-20th-century Mexican folk surrealism,
a single woman shown frontally from the chest or waist up, staring directly at the viewer with an
unflinching steady gaze, placed in a compressed shallow stage between the picture plane and a wall
of tropical foliage or a flat colored backdrop, wearing a traditional Tehuana dress or embroidered
huipil with a rebozo shawl and jade or bead necklaces, flowers woven into braided hair, accompanied
by symbolic animals (a spider monkey, a parrot) and symbolic objects arranged around her like an
offering (a thorn necklace, a hummingbird pendant, a broken column, ribbons with inscriptions),
emblematic anatomical symbols treated flatly (a visible heart, arteries as thin red lines, a spinal
column), saturated folk palette of magenta, cobalt blue, emerald green, yellow and blood red laid
in flat controlled zones with hard clean edges and smooth restrained brushwork, small devotional
retablo-like format meant for close viewing, precise dates or hand-lettered inscriptions painted on
the composition, oil on canvas or masonite, intimate autobiographical icon
```

**负向约束（`--no` 风格）**

```
--no melting clocks or dream surrealism, photorealistic rendering, impressionist broken brushwork,
heavy impasto, sfumato haze or soft gradients, monumental mural scale, multi-figure historical
crowds, deep vanishing-point perspective, European aristocratic dress, muted beige palette, 
candlelit tenebrism, 3D render, modern printed typography, watermark, glossy gallery lighting,
generic fashion-model pose, smiling stock-photo expression
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **正视性** | 面部轴线与画幅垂直中轴夹角 ≤10°；瞳孔方向朝镜头（±15°） | 面轴角度 + 视线向量检测 |
| 2 | **自传指涉物计数** | ≥2 个来自生平符码表的可识别物（事故/手术/迭戈/民族服饰/宠物） | 符号清单核对（对照 §5/§12 符码表） |
| 3 | **民间色与平涂** | 色相簇 6–9；≥3 个区域饱和度 ≥60%；色区内色彩方差 ≤5% | 直方图 + 色相聚类 + 区域方差 |
| 4 | **硬边/无羽化** | 明暗与色区过渡带 ≤2 px（1024 px 宽画布）；禁止 ≥8 px 的羽化渐晕 | 梯度宽度统计取中位数 |
| 5 | **背景压缩** | 背景纵深 ≤2 个平面；无收敛透视（消失点缺失或 ≥2 个互相矛盾）；植被/幕布覆盖背景区 ≥60% | 透视线检测 + 背景分割 |
| 6 | **单人·画幅语义** | 人物数 =1（≥90% 帧）；主体占画面高度 40–70%；边缘裁切 ≤1 处 | 人物检测 + 边界框统计 |
| 7 | **符号清晰呈现** | 动物/植物/首饰符号 ≥2 类，均处于焦平面（无景深虚化，边缘清晰度 ≥ 主体 80%） | 清晰度图 + 类别检测 |
| 8 | **全片静止（动画档）** | 相机固定；帧间差 ≤1%；仅允许花/鸟微动（可选，≤2%） | 帧差图：非微动区非零像素占比 |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 `templates/style_card.md` 的填写规则对齐。第 2 条依赖 §5/§12 建立的**生平符码表**（事故-飞床/手术-断柱/迭戈-肖像坠饰/民族-服饰/宠物-猴与鹦鹉）。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **自传具体度**（Autobiographical Specificity）`[归纳]` | 通用肖像/静物，无生平指涉（**越界：无差别肖像档**） | 个人化但半可读：1 个符号可对应个人（如单朵花/单只猴） | **具体事件/人物密集指涉**：可命名的事故、手术、婚姻、民族符码 ≥2 件 | **80%**（本模块身份） |
| P2 | **民间色彩强度**（Folk Color）`[归纳]` | 低饱和欧式色域、自然混合（**越界：学院档**） | 1–2 个饱和民间色区，其余克制 | **全画面民间色系平涂块面**（洋红/钴蓝/翠绿/黄/血红） | **75%** |
| P3 | **象征身体密度**（Symbolic Body Density）`[归纳]` | 身体完整、无器官符号（早期肖像档） | 1–2 个身体符号（绷带、石膏、眼泪） | **打开的/被替代的身体**：外露心脏、钉柱、鹿身、分裂双身 | **70%** |
| P4 | **正面凝视/镜像度**（Frontal Gaze / Mirror）`[归纳]` | 侧身/低头/回避对视 | 半正面、目光含蓄 | **全正面直视 + 镜像结构（含双身变体）** | **80%** |
| P5 | **服饰与纹样密度**（Dress & Pattern）`[归纳]` | 素衣/西装（*Cropped Hair* 的反常档） | 单一民间元素（一条披肩/一串珠） | **全套 Tehuana/huipil + 玉石珠链 + 发花** | **70%** |
| P6 | **画幅与观看距离**（Intimate Scale）`[归纳]` | 大画幅、远观（**越界：壁画档**） | 中型画幅 | **还愿画级小画幅（长边 30–60 cm 级）+ 近距单人对视**（例外：《Las dos Fridas》式双身巨幅须显式标注为「例外档」） | **85%** |

> 用法：**P1/P4 定「是不是卡罗」**（自传指涉 + 正面镜像）；**P3/P5 定「身体与身份的符号强度」**；**P2/P6 定「民间色彩与小画幅」的底盘**。三档描述可直接作判定标准写进自查表。
> 数据来源：档位阈值取自 [R3][R6][R7][R10][R11][R19]；**档位划分本身为 `[归纳]`**（本项目操作化建议，未经渲染实验校准）。
> **分工注（写死，与 §3.1 对齐）**：P1 强档（自传具体指涉）＋P4 强档（正面镜像）是本模块专属；**「通用情绪原型符号（无生平指涉）」＋「全场景变形」组合整体属于蒙克模块，禁止在本模块同档出现**；**「公共巨幅＋群像＋历史叙事」整体属于里维拉模块，禁止在本模块同档出现**。需要大场景时不得同时保留本模块的「正面单人＋符号身体」标志机制（见 §3.1 与 §8.1 越界警报）。本注为 `[归纳]`。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 蒙克）**（× 蒙克；本卡 §3.1 分工条款）：具体自传符号系统 vs 普世焦虑原型语法——符号可解码性测试（具体事件指涉物 ≥2 件 → 卡罗档）；同屏必须显式分区、默认二选一
- **分工（vs 里维拉）**（× 里维拉（future）；本卡 §3.1 分工条款）：私密小幅＋正面单人＋私人题材 vs 公共巨幅＋多人群像＋集体叙事——四条判据 ≥3 条归判；默认不并置
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 笔触 / C-12 色相预算 / C-14 渐变

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/kahlo.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
