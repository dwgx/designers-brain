# 荷加斯 模块卡 — `hogarth`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/hogarth.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **系列＝叙事单位**：6/8/12 帧成套、同一主角跨帧推进（服装/道具状态可列进度表）；帧间前后依赖——跳过一帧则因果断裂（「field not broken up」）
2. **剧场化场面调度**：人物成排横列于「台口」、关键动作推到前景（下 1/3）；横排/对位人物组 ≥2——「我的画就是我的舞台（dumb show）」
3. **单帧多线索＋题刻装置**：可辨文字 ≥2 处/帧、情节道具 ≥3 类、画中画 ≥1；印品下缘刻标题＋诗句——「别的画我们看；他的画我们读」（Lamb）
4. **「性格」而非漫画＋道德对位**：面部类型学（守财奴/纨绔子/教士…）不夸张变形（「没有一张是夸张的」）；成对印品正反并置（《啤酒街》×《琴酒巷》）、双主角平行剪辑
5. **均匀舞台光＋线刻排线**：画内单一点光源 = 0、暗部占比低（为可读性服务）；蚀刻＋雕刀、排线族 ≥2 方向（「strong bold stroke」）——低价大众（1 先令档）＋内嵌说明文字

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Hogarth-style modern moral subject — a scene staged like theatre, every clue legible:
the picture plane as a stage — figures arranged across the front, the key action pushed into the foreground;
one frozen moment from a larger story, its cause and consequence both visible inside the frame;
typological characters, not caricatures — a fop, a miser, a parson, a bawd, each face specific but unexaggerated;
an inventory of narrative clues — a readable letter, a ledger, a mirror, a clock, paintings-within-the-painting on the wall;
a moral counterpoint: folly answered by its consequence;
even, readable stage light — no single hard source, no tenebrism, the whole scene lit for inspection;
English rococo palette: brick reds, blue coats, buff and white, black accents; crisp readable colour;
[series variant] a numbered progress: the same protagonist across frames, costume and props declining with his fortune;
[print variant] pure etching and engraving — bold confident line, cross-hatching for shadow, a caption or verse engraved below the image
```
**负向约束（`--no` 风格）**
```
--no glamour, idealised beauty, heroic poses, chiaroscuro drama, single spotlight, deep black backgrounds,
soft-focus blur, atmospheric haze, impressionist brushwork, caricature distortion, exaggerated cartoon faces,
anachronistic objects, photographic realism, 3D render, anime, empty minimal scenes, decorative abstraction,
single-frame isolation when a series is requested (no progress dependency between frames)
```

## 代码艺术规则（§8.2 原样）

1. **线索计数规则**：每帧可辨认叙事线索（可读文字 / 情节道具 / 画中画或纹章）≥5 条；其中**可读文字 ≥1 处**（信件/账本/招牌/题词任一类）。自查：对象检测 + OCR 计数。
2. **系列进度规则（工作流）**：系列帧数 ≥6；同一主角的**可追踪元素**（服装主色、核心道具、随身物）在每帧出现率 100%，且跨帧状态可列「进度表」（至少 2 次状态变化）。自查：逐帧登记表 + 元素比对。
3. **光线规则**：全帧画内单一硬光源 = 0（灯烛允许作道具，但不得成为光锥主角）；暗部（L<0.2）占比 ≤35%、近黑（L<0.08）面积 ≤10%——「为看清服务」。自查：光源检测 + 直方图。
4. **面孔规则**：面孔为**类型化**（可归类社会类型 ≥3 种）；夸张度低——面部关键点比例偏差 ≤15%（无漫画式扭曲、无兽化）。自查：人脸关键点 + 比例比对。
5. **对位规则（成对帧）**：对位两张共享构图骨架（同机位/同尺度/同地平线；骨架相似度 ≥70%）、语义相反标志物 ≥3 对（如：酒器满/空、面容红润/枯槁、建筑完好/破败）。自查：结构相似度 + 标志物清单。
6. **定格规则**：运动模糊 = 0；每帧只允许 **1 个动作极值**（the single frozen action extreme）；画面时间＝事件拐点（前因物已在场、后果物已可读）。自查：模糊核检测 + 动作计数。
7. **题刻规则**：印品帧下缘题刻 ≤2 行（标题 + 诗句/说明）；题刻语义与画面道德判词一致（关键词表匹配：标题词 ∈ 画面语义标签）。自查：文本行检测 + 关键词比对。
8. **表面规则（版画帧）**：明暗由线密度构成——排线族 ≥2 方向（交叉排线允许）、线覆盖率 ≥15%；大面积平涂填充 ≤10%；无 >12 px 的平滑渐变区。自查：方向场分析 + 覆盖率统计。

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–3 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **系列化强度**（工作流参数）`[归纳]` | 单幅（1 帧，独立讽刺印品） | 小系列 3–6 帧（成对/三段） | 大系列 8–12 帧 + 每帧题刻/说明文（浪子 8 / 勤奋与懒散 12 档） | **8**（浪子档；单幅起步时置 1） |
| P2 | **剧场化程度**`[归纳]` | 自然场面：无台口感、人物散置 | 半舞台：前景事件＋对位人物组 | 全舞台：横排「台口」＋中心证据物＋两侧对位＋画中画评论层 | **70%** |
| P3 | **线索密度（编目强度）**`[归纳]` | 简洁：线索 3–5 条、无文字 | 中等：线索 5–8 条、文字 ≥1 | 高：线索 ≥8 条＋可读文字 ≥2 处＋画中画/纹章 ≥1（Marriage 档） | **65%** |
| P4 | **讽刺/道德强度**`[归纳]` | 温和风俗（无判词、无恶果） | 讽刺（ridicule：荒唐可笑的丑态） | 严酷警示（in terrorem：死亡/疯癫/酷刑直给——琴酒巷、残忍四阶段档） | **50%** |
| P5 | **光线戏剧度**`[归纳]` | 平光/天光（户外记录档） | 均匀室内光（多光源环境光） | 舞台聚光（无硬锥、无画外单光源——仍是「看清」逻辑） | **30%** |
| P6 | **角色复用度（跨帧连续性）**`[归纳]` | 单帧角色（一次性人物） | 系列内主角复用（服装状态推进） | 双主角平行（双轨对照——勤奋与懒散档） | **2 档（系列内复用）** |

> **用法**：P2/P3 定「是不是荷加斯」（剧场化＋线索密度；两条同时 ≥中档才成立）；P1 定叙事工程（单幅/小系列/大系列——工作流参数，不进画面重叠计算）；P4 定警示档位（讽刺→严酷）；P5/P6 定连续性（光＝可读性、角色＝进度载体）。
> **分工注（与 §3.1 对齐）**：P1 为**系列参数**——与洛克威尔组合时「叙事单位轴单主」（洛承担单帧、荷承担系列骨架）；P6 是**连续叙事核心**——「帧间进度依赖」整体属于本模块，不得与「帧内自足」同档并存；P5 一旦升到「画外单光源＋亮部只落脸/手/道具」即越界进入**卡拉瓦乔**领域，升到「单光源连续衰减照单张脸」即越界**伦勃朗**领域——组合实验按此判分。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 戈雅）**（× 戈雅；本卡 §3.1 分工条款）：系列叙事二分：都市道德剧 vs 战争纪实——四判据（叙事主体／连续性／情感机制／题刻功能）；系列连续性轴单主——「帧间进度」与「帧间独立」不可同档并存（需同作按 N4 分区）
- **分工（vs 洛克威尔）**（× 洛克威尔；本卡 §3.1 分工条款（同批互查））：连续叙事分镜原型 vs 单帧故事——四轴（叙事单位／因果链位置／情感温度／场景时代）＋细化判据⑤–⑦；判据＝「帧间是否存在进度依赖」
- **次级注记（vs 博斯 / 老勃鲁盖尔 / 列宾）**（× 博斯 / 老勃鲁盖尔 / 列宾；本卡 §3.1 次级注记）：防混淆：怪诞两档（物种发明 vs 社会类型）／全景两档（农民全景 vs 都市剧场）／社会横截面两档（目光网 vs 类型脸谱）
- **Lane B 接口（分镜/连续叙事）**（× Lane B；本卡 §3.1 接口条款）：分镜（系列＝分镜板，逐帧「标题＋动作＋道具状态」）／连续性检查（服装道具进度表＝B1–B4 原型）／题刻＝收尾文案槽；冲突预检：C-01 同侧（声明「even stage light」）／C-08 运动模糊＝0（定格侧）／C-07 与丢勒分轴／C-16·C-17 按 N4 分区

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/hogarth.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
