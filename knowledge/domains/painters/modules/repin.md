# 列宾 模块卡 — `repin`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/repin.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **群像＝社会横截面**：人物 ≥8 且身份类别 ≥3（服饰/职业可辨）；前/中/远景各可独立读故事
2. **目光网状构图＋心理极值瞬间**：注视向量 ≥3 条、≥2 对相互注视；单一情感极值人物 ≥1、表情可读非中性——「事件后 1–3 秒」的停顿感
3. **环境光而非舞台光**：户外光研究（尘埃/正午/雪地/窗光）；明暗层次 ≥3、阴影有环境色、无单一硬光锥
4. **土色-肤色主导＋材质触感笔触**：土色系＋肤色 ≥60%、高饱和 ≤5%；可见笔触覆盖 ≥70%、随形体/衣褶——「物质本身」
5. **分层景深＋道具叙事＋「未完成」现场感**：景深带 ≥3；叙事道具 ≥3 类参与讲故事；多版本跨年修改、低完成度区域 ≥1——「完成＝此刻为止」

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Repin-style social realist painting — a wide horizontal group scene treated as a cross-section of society:
several figures of different classes (peasants, officials, clergy, soldiers, children, beggars)
arranged in receding bands; readable individualized faces — every face a character, not a type;
eyes linked in a network of gazes (several mutual looks, a newcomer noticed by many);
one emotional extreme as the anchor (uproarious laughter / sudden grief / the shock of a return),
everyone else in modulated in-between states;
environmental daylight — noon haze, dust, window light — natural colored shadows,
no single theatrical spotlight; earth-tone palette with honest skin tones,
white shirts and uniforms as accents, one saturated note (red or blue) used sparingly;
confident visible brushwork, wet-in-wet — cloth feels like cloth, skin like skin, metal like metal;
narrative props that tell the story (icons, portraits on the wall, ropes, spears, ledgers);
a moment just after the event — the instant the situation becomes readable;
composed like a chapter of a novel, not like a stage set
[portrait variant] a single sitter caught mid-conversation, unposed, impatient,
hands and eyes as telling as the face, window light, dark but colored background
```
**负向约束（`--no` 风格）**
```
--no single spotlight or stage lighting, no faceless anonymous ranks, no heroic nude musculature,
no single-face chiaroscuro portrait, no poster-flat color fields, no swirling impasto emotion field,
no cross-hatching print surface, no glossy academic varnish, no symmetrical ceremonial arrangement,
no cartoon, anime, 3D render, photographic copy, no empty decorative crowds, no idealized bodies
```

## 代码艺术规则（§8.2 原样）

1. **群像规则**：人数 ≥8 时，身份类别（服饰/职业可辨）≥3；画面分前/中/远 3 个层带，每层 ≥2 人。（依据：《库尔斯克》70+ 人物、分层排布 `[史料]`[R2]）
2. **目光网规则**：注视向量 ≥3 条；相互注视对 ≥2；「新入场者」被 ≥2 人注视。自查：面部朝向/瞳孔方向检测。
3. **情感极值规则**：全帧表情强度峰值人物 = 1（可归类：笑/惊/怒/悲）；其余人物强度 ≤ 峰值的 70%。（依据：《哥萨克》「笑」为全画主角 `[研究]`[R2]）
4. **环境光规则**：全帧可见光源 ≥1 且为环境型（日光/窗）；无单一光锥；阴影饱和度 > 0（有色阴影）；明暗层次 ≥3 带。（依据：外光实验 `[研究]`[R2][R4]）
5. **色彩预算规则**：土色系+肤色面积 ≥60%；白色连通域 ≥3 处；高饱和（S≥0.6）面积 ≤5%。（自查：HSV 掩膜 + 连通域）
6. **笔触规则**：可见笔触覆盖 ≥70%；笔触方向随形体/衣褶；最大平滑渐变区 ≤2% 面积。（对照「материя как таковая」原则 `[自述]`[R10]）
7. **道具规则**：叙事道具 ≥3 类（墙上图像/器物/服装细节）；每件道具与人物关系可述（人工核）。（依据：《意外归来》墙面四件套 `[史料]`[R2]）
8. **现场感规则**：存在 ≥1 处低完成度区域（粗率笔触但非空白）或可辨版本痕迹；无 3D/照片质感。（依据：跨年修改史 `[史料]`[R2][R3]）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–2 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **群像密度（人数）**`[归纳]` | 1–2 人（单肖像/双人；如《穆索尔斯基像》） | 3–10 人（家庭/小组；如《意外归来》7 人） | 20–80+ 人（游行/哥萨克/国务会议） | **50%**（3–10 起步） |
| P2 | **社会横截面强度（阶层并置）**`[归纳]` | 单一阶层（肖像/习作档） | 2–3 个阶层并置（家庭 + 仆从 + 军人） | 全阶层谱系同框（神职/警察/富/贫/乞；《库尔斯克》级） | **60%** |
| P3 | **心理瞬间强度**`[归纳]` | 平静/工作状态（托尔斯泰耕地档） | 情绪可读（微笑/沉思/期待） | 情感极值（嚎哭/爆笑/狂怒；雷帝/哥萨克/索菲亚档） | **50%** |
| P4 | **目光网状度**`[归纳]` | 单向注视（肖像看画外/看模特） | 两人对视（对话档） | 全网（≥3 注视链 + 新入场者被全体注视；《意外归来》档） | **55%** |
| P5 | **户外光研究度（plein-air）**`[归纳]` | 工作室光（暗背景肖像） | 侧窗/单一环境光源 | 户外直射研究（尘埃/正午/雪地；《库尔斯克》档） | **45%** |
| P6 | **修改/未完成感**`[归纳]` | 精细完成（学院式收尾） | 可见笔触（直画肖像档） | 明显现场修改痕迹（局部草率/层叠；《意外归来》改脸档） | **40%** |

> **用法**：P1+P2 定「是不是列宾的叙事画」（群像 + 横截面；两条同时 ≥ 中档才成立）；P3 定心理强度；P4 定家庭/群体叙事（关系网）；P5/P6 定「户外光 + 现场感」的时期滑轨（早期学院 → 1880s 外光巅峰 → 晚年直率）。
> **分工注（与 §3.1 对齐）**：P5 若升到「强」且变为单一硬光锥、亮部只落脸/手/道具——越界进入**卡拉瓦乔**领域；P4 若塌缩为「单脸光斑地图」——越界进入**伦勃朗**领域；P2 为「弱」且 P3 为「强」= 纯心理肖像（仍是列宾，但叙事档关闭）。组合实验按此判分。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 戈雅）**（× 戈雅；本卡 §3.1 分工条款）：「有立场的画面」二分：日常与仪式的社会横截面（面孔全可读＋环境光）vs 灾难与暴力的新闻构图（施害者 0 面孔＋证据光）——判据四条
- **分工（vs 米开朗基罗）**（× 米开朗基罗；本卡 §3.1 分工条款）：群像两条路：劳损真实身体＋疲态尊严＋队列/横带 vs 英雄化人体＋涡旋环绕——判据三条
- **分工（vs 伦勃朗）**（× 伦勃朗；本卡 §3.1 分工条款）：心理载体：多张脸的目光网＋全身姿态＋道具 vs 单张脸的光斑地图
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影 / C-05 笔触可见度 / C-12 色相面积预算

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/repin.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
