# 洛克威尔 模块卡 — `rockwell`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/rockwell.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **单帧故事**：一帧压缩完整故事弧（因果线索 ≥2：前因物证＋后果表情/文字）、画面时间＝事件拐点（前后 1–3 秒）——「distill a narrative into a single frame」
2. **镜头感构图**：具体视点＋景别；画中框（门/窗/柜台/镜）≥1 或前景遮挡 ≥1、非对称裁切——「strategies similar to those used by filmmakers」
3. **目光/表情的阅读链＋业余剧团**：视线向量 ≥2、链长 ≥3 节点（《The Gossips》链式耳语）；模特为邻居/亲友、表情夸张可读——「像演员的脸」
4. **日常美国母题＋叙事道具**：小镇/家庭/孩子/老人（「the everyday people of America, especially old men and boys」）；道具承担情节（行囊棍/*Mein Kampf*/报头「Bombing」）；色彩明亮可读（暖调底＋少量高饱和、无 tenebrism，为报刊印刷服务）
5. **理想化滤镜＋版式意识**：排除 sordid/ugly（「I paint life as I would like it to be」）；竖构图、上部留出刊名区、64px 缩略图可读——「不能含蓄，必须一目了然」；1963 后转报告文学档（社会议题为显式例外）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
American narrative illustration in the mid-century Saturday Evening Post manner: a single,
self-contained story moment — one readable beat of everyday American life whose before-and-after is
implied by clues inside the frame (an open letter, a packed suitcase, a hobo stick on the floor, a
newspaper headline); ordinary people cast from small-town life — a boy, a policeman, a grandmother,
a barber, neighbours, a postman — each figure posed and directed with a readable expression and a
clear gaze direction; cinematic staging: a specific viewpoint and framing, a doorway, window, counter
or mirror acting as a frame-within-the-frame, foreground objects guiding the eye, slightly off-centre
composition; warm, legible palette — soft daylight or one readable interior light, local colour kept
bright and approachable (warm greys, ochres, brick red, a few saturated accents), faces lit clearly;
storytelling props and period detail placed with care, props carrying the plot; crisp, controlled
drawing with a smooth, finished surface, values arranged for legibility at newsstand size (one clear
focal point readable in a thumbnail); humour and affection as the default tone, gravity allowed when
the story demands it; American small-town or family setting, mid-20th century, oil on canvas
```

**负向约束（`--no` 风格）**

```
--no text, watermark, signature, fake signatures; ambiguous narratives that need a caption; abstract
or purely formal composition; art-historical pastiche or bravura brushwork for its own sake; heavy
chiaroscuro with near-black backgrounds; single candlelit tenebrism; empty unpopulated space as the
subject; faceless anonymous crowds; avant-garde distortion; motion blur (frozen moment only); gore or
cruelty as spectacle; caricature of real persons; cold cyan/teal grading; anamorphic lens flares;
anime, chibi, 3D render, photographic realism
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **单帧叙事** | 帧内因果线索 ≥2（物证/表情/文字三类中 ≥2 类）；跨帧依赖 = 0（系列化时按帧清单显式声明） | 线索标注清单 + 依赖检测 |
| 2 | **阅读顺序链** | 视线向量 ≥2 或表情链 ≥3 节点；主链覆盖 ≥3 个可辨对象；全帧焦点数 = 1 | 视线向量夹角统计 + 焦点检测 |
| 3 | **镜头调度** | 画中框 ≥1 或前景遮挡物 ≥1；主体质心偏离画面中心 ≥8% 画宽；视点高度明确（平/俯/仰三选一） | 边界框位置 + 边缘相交统计 |
| 4 | **光（可读性光）** | 主光 1 个且来源可指认；半影宽度显式 2–6% 短边（防硬阴影禁令误伤）；暗区（V<0.25）≤25%；禁 tenebrism 双峰直方图 | 梯度宽度统计 + 直方图 |
| 5 | **色板** | 暖调底（暖灰/米/赭/橄榄）为主；高饱和（S ≥0.60）面积 ≤12% 且集中 ≥3 处；全帧平均饱和度 ≤0.45 | 逐帧 HSV 直方图 + 色相聚类 |
| 6 | **道具与文字** | 叙事道具 ≥3 类；文字元素 ≤3 处且与情节相关；64px 缩略图可读（焦点唯一、主对比 ≥30% 明度差） | 缩略图测试 + 道具标注 |
| 7 | **定格（运动预算）** | 运动模糊帧数 = 0；运动以姿态/道具暗示；before/after 线索 ≥1 对；全片无叙事位移时判为「氛围帧」（非本模块典型，须显式声明） | 帧差图 + 姿态线索清单 |
| 8 | **群像预算** | 人物 1–8；每人物表情/姿态可辨率 ≥80%；主角面积 ≤35%；禁「零人物空场」（霍珀域）与「无面孔施虐队列」（戈雅域） | 人物检测 + 表情分类 + 面积统计 |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 `templates/style_card.md` 的填写规则对齐。第 4/7 条为与 Lane B 的接口条款（C-01/C-08 处置的代码侧落地）；第 1/2 条为分镜接口（每格自足 + 阅读顺序）；第 7/8 条为表演接口（定格 + 群像表演预算）。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **单帧叙事强度**（Single-Frame Narrative）`[归纳]` | 氛围场景，无可读事件（习作/纯风景） | 单一事件可读（一笑一闹，因果线索 1 条） | **完整故事弧**：因果线索 ≥2、before/after 均可推断（《The Runaway》《Saying Grace》档） | **80%**（本模块身份） |
| P2 | **镜头感**（Cinematic Staging）`[归纳]` | 正面平视全景、无框景（早期封面） | 明确视点/景别；轻微非对称 | **画中框＋前景遮挡＋偏心裁切**（《Shuffleton's》《The Runaway》档） | **70%** |
| P3 | **群像调度**（Cast Direction / Gaze Chain）`[归纳]` | 1–2 人、无视线关系 | 3–5 人、视线可读 | **链式目光/表情群像**（《The Gossips》14 人链档） | **60%** |
| P4 | **理想化滤镜**（Idealization）`[归纳]` | 报告文学档：直面冲突、不修饰（1963 后社会议题；**非缺陷，为后期正档**） | 温情但保留真实（含小窘迫、小失误） | **全理想化**：排除 sordid/ugly（战前/战时主档） | **70%**（后期作品降至 20–30%） |
| P5 | **幽默度**（Humor）`[归纳]` | 严肃/感伤（《Breaking Home Ties》《Saying Grace》） | 会心一笑（《The Runaway》《Doctor and the Doll》） | 闹剧/童趣（《No Swimming》《Before the Shot》） | **50%** |
| P6 | **细节密度**（Detail / Prop Density）`[归纳]` | 简洁、道具 ≤2 类（习作档） | 叙事道具 3–5 类、文字 ≤3 处 | **物证级细节**（April Fool 49 处「错误」；《Shuffleton's》档） | **65%** |

> 用法：**P1+P2 定「是不是洛克威尔」**（单帧故事＋镜头感；两条同时 ≥中档才成立）；P3/P6 定「叙事密度」；P4/P5 切「理想化/幽默」与「后期报告文学」两档。三档描述可直接作判定标准写进自查表。
> 数据来源：档位阈值取自 [R2][R3][R5][R11][R14][R16]；**档位划分本身为 `[归纳]`**（本项目操作化建议，未经渲染实验校准）。
> **分工注（与 §3.1 对齐）**：**「帧间依赖 / 系列序号」整体属于荷加斯模块，禁止在本模块同档出现**（需要系列感时不得同时取消单帧自足）；**「空场/零人物/无事件」整体属于霍珀模块**；**「施害者匿名队列/暴力物证」属于戈雅模块**。与 Lane B 组合时：P1/P2 为主轴，运动区域数上限 = 1、运动模糊帧 = 0（显式声明）。本注为 `[归纳]`。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 荷加斯）**（× 荷加斯；本卡 §3.1 分工条款（同批互查））：叙事两档：单帧故事 vs 道德组画——四轴（叙事单位／因果链位置／情感温度／场景时代）＋细化判据⑤–⑦；判据＝「帧间是否存在进度依赖」；叙事单位轴单主
- **Lane B 接口（分镜/表演）**（× Lane B；本卡 §3.1 接口条款）：分镜：每格自足＋阅读顺序（第一→第二→第三阅读点）；表演：姿态暗示运动＋表情可读＋情绪外包（「父亲不能表露，狗替他表露」）——霍珀管空间/取景、本模块管叙事调度/表演
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 机制条款）：C-01/C-08/C-09 同口径：定格侧显式声明「motion blur frames = 0；motion implied by pose and props」；如需戏剧光按 N5 给出半影宽度（默认 2–6% 短边）；叙事轴单主（N3）
- **次级注记（vs 戈雅 / 霍珀 / 德加）**（× 戈雅 / 霍珀 / 德加；本卡 §3.1 次级注记）：防混淆：叙事-纪实两端（日常理想主义 vs 灾难/批评）／镜头感两档（满场事件 vs 空场孤独）／取景两档（叙事调度 vs 抓拍失衡）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/rockwell.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
