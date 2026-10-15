# 共性结构提炼（B-04 · patterns.md）

> 输入：`knowledge/agent-art/prompts/corpus.md`（A 类 24 条 + B 类 17 条）+ `knowledge/domains/motion-graphics/cards/structure.md`（15 卡解剖）+ `knowledge/domains/motion-graphics/origin/提示词全文.md`（内部 15 卡原文）。
> 输出：14 条可迁移模式 + 对照 15 卡的缺口清单。日期：2026-10-15；作者：PromptCorpusHunt。
> 对照基准（structure.md 的 15 卡结构）：**4 段 + 页头** = ① 任务头（固定句式：10 秒 MG / 1920×1080 / 30 帧 / 渲染器二选一 / 先 6 关键帧→动画→逐帧自查 / 音效代码合成卡点）② 画风段（4–8 条可判定规则）③ 内容段（【10 秒分镜 + 收尾文案】）④ 别做成（3–4 条反约束）。页头：「提示词　暂停截图，【】里换成你的」。

## 总表（先看结论）

| # | 模式 | 15 卡现状 | 外部证据（corpus 编号） |
|---|------|-----------|------------------------|
| P1 | 角色设定 | ✗ 缺 | A1 A16 A22 A23 |
| P2 | 任务句式（动宾+硬规格） | ✓ 有（固定句式） | A6 A8 A19 |
| P3 | 输出规格固定块 | ◐ 半（只有尺寸/帧率/时长） | A1 A2 |
| P4 | 可判定约束 | ✓ 有（画风段） | A1 A7 A11 A12 A13 |
| P5 | 反约束 / 禁列表 | ✓ 有（3–4 条） | A7 A9 A13 |
| P6 | 关键帧先行（低成本检查点） | ✓ 有（6 关键帧） | A1 A7 |
| P7 | 自查 → 自评 → 独立评审 | ◐ 半（只有逐帧自查） | A1 A3 A23 |
| P8 | 确定性渲染（纯函数/种子） | ✗ 未显式 | A1 A7 A13 A22 |
| P9 | 音画同源 + 卡点机制 | ◐ 半（有要求，无机制） | A1 A7 |
| P10 | 分镜节拍表（钩子/高潮/结尾） | ◐ 半（内容段有分镜） | A1 A13 |
| P11 | 输入槽与反问 | ◐ 半（有【】槽） | A7 |
| P12 | 素材许可与商标规避 | ✗ 仅拼贴卡一句 | A1 A2 |
| P13 | 交付清单（产物+报告） | ✗ 缺 | A1 |
| P14 | 对标基准 + 评分刻度 | ✗ 缺 | A1 A3 |

---

## P1 角色设定（Role assignment）

- **结构**：开头一句把模型钉到职业身份上，随后所有要求以该职业的口吻成立。
- **句式**：`You are the director, motion designer, engineer and sound designer of ONE 10-second motion-design film.`（A1）；`你是 opus 5.5，当前世界最强模型……`（A16）；`You are a senior motion-design jury member … You did NOT make this film.`（A3）。
- **证据**：A1、A3、A16、A22（skill 的 description 即角色）、A23。
- **15 卡对照**：内部 15 卡**没有角色设定**——直接「用代码做一支 10 秒的 MG 动画……」。外部体系把它放在最前，并常用「多重身份」（导演+动效+工程+声音）逼出全链路自检。
- **缺口**：**缺**。建议加进任务头首句（`You are the director / motion designer / engineer / sound designer of ONE 10-second MG film.`），成本一行。

## P2 任务句式（动词 + 产物 + 硬规格）

- **结构**：`make/build <时长> <体裁> <目的/动机>` 或中文 `做一个动画，快速回顾……`；规格（尺寸/帧率）常在同一句或下一行。
- **句式**：`make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.`（A6）；`做一个动画，快速回顾中华五千年的历史。风格轻松有趣，动画格式为线稿……`（A8）；内部：`用代码做一支 10 秒的 MG 动画（1920×1080，30 帧）……`。
- **证据**：A6、A8、A19、内部 15 卡（15/15 同构）。
- **15 卡对照**：**已具备且更强**（固定句式 + 渲染器二选一）。外部证明同一句式可裁到 1 句仍能出片（A6 17k 赞），但其可控性依赖模型自觉；我们保留完整任务头是对的。
- **缺口**：无（保留）。可选：把「动机句」（like it's your showreel / 务必引人入胜）并入任务头，给模型一个质量自压点。

## P3 输出规格固定块（Output (fixed)）

- **结构**：独立的固定段，写死全部交付规格：分辨率、帧率、时长（到毫秒）、编码、音频、响度、峰值、文件名。
- **句式**：`1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS integrated, true peak ≤ −1 dBTP. Final file: video.mp4.`（A1/A2）。
- **证据**：A1、A2。
- **15 卡对照**：内部卡只有「1920×1080，30 帧」+「10 秒」；**没有**编码/容器/音频采样率/响度/峰值/文件名。
- **缺口**：**半缺**（交付级规格）。建议 style_card 的「任务头」后加 `Output (fixed)` 一行——这正是「能跑一次」与「能当交付物」的分界线。

## P4 可判定约束（量化/物理规则）

- **结构**：把风格写成能逐帧机械检查的量：角度、帧数、色数、曲线、像素、时长。
- **句式**：`overshoot 用 cubic-bezier(0.34,1.56,0.64,1)，错峰 2–4 帧`（A2 明确示范）；`imageSmoothingEnabled = false` + `不要子像素位置、抗锯齿、渐变或 shadowBlur`（A11）；`把整体停止 3〜4 帧，然后做约 0.3 秒的慢动作`（A12）；`锁定的调色板（7 个 hex 值）`（A13）；内部：斜线 30°、16–32 色、8–12 张/秒、回弹约 8 帧。
- **证据**：A1、A2、A7、A11、A12、A13 + 内部 15 卡画风段。
- **15 卡对照**：**已具备**（画风段就是这个模式的产物）。外部唯一增量：**参数直接给代码/曲线数值**（cubic-bezier、hex 色值、种子常量），而不只是「角度/帧数」。
- **缺口**：无（增量：把可给的参数写成代码字面量）。

## P5 反约束 / 禁列表（Banned / 别做成 / 不要…）

- **结构**：一段只写禁止项；每条对着一个「模型默认退化行为」。
- **句式**：`Banned: bouncy easing, particle bursts, glows, gradients on UI chrome, mismatched icon strokes, dead time, anything that looks like a template.`（A7）；`Don't make it feel like a generic infographic or strategy game.`（A9）；`不要青色，不要品红，不要霓虹，不要彩虹，不要黑底配紫的「人工智能观感」`+`不要 TODO 注释、伪代码、占位符`+`开始按钮后面放着一张静止帧就是失败`（A13）；内部：`别做成：交叉淡化冒充形变、默认塑料材质……`。
- **证据**：A1（`A clean, template-looking result is a fail.`）、A7、A9、A13 + 内部 15 卡反约束段。
- **15 卡对照**：**已具备**（3–4 条/卡）。外部增量：禁项分三层——**风格禁项 / 技术禁项（TODO、占位符、伪代码）/ 质量兜底禁项（静止帧开局即失败）**；并配「失败判据」而非仅「禁止词」。
- **缺口**：无（增量：加「技术禁项」与「失败判据」两类）。

## P6 关键帧先行（低成本早期检查点）

- **结构**：先出静态样张/状态表给人类看，确认后才做动画；正式渲染前再逐帧/逐拍自检。
- **句式**：内部任务头：`先出 6 张关键帧给我看，再做动画，最后逐帧自查`；A1：`Key frames before motion. Build the look, render stills at 6–10 key times and actually look at them.`；A7：`Render one frame per beat before the full render. Fix anything off the grid, cramped or hard to read.` + `<start> Ask me for the inputs, then show me the state list on the beat grid before you write any code.`。
- **证据**：A1、A7 + 内部 15 卡。
- **15 卡对照**：**已具备**（这是 15 卡骨架纪律之一）。
- **缺口**：无（外部变体「先给我状态表/拍表」是升级版检查点，可选并入）。

## P7 自查 → 自评 → 独立评审（Check → Self-score → Jury）

- **结构**：三阶质量门：① 逐项技术自查（对照 checklist）② 自评分（1–10 分制、给定刻度）③ 换一个 AI/会话当评委，产出按影响排序的修改单，再改一轮。
- **句式**：A1：`Before you deliver, score yourself honestly 1–10 on style fidelity, concept wow … (6 = template-level, 8 = high-end agency, 9 = award shortlist). Aim for 9; fix whatever scores lowest first.`；A3：`You are a senior motion-design jury member … You did NOT make this film. Judge it harshly … Most first renders deserve 5–7. Do not inflate.` + `Give 5–10 fixes ordered by impact … At least one fix must raise the wow factor`；A23：`avoid adding more graphics; instead refine what has been created`。
- **证据**：A1、A3、A23。
- **15 卡对照**：内部只有「最后逐帧自查」（对应①）。**缺②（自评分制）与③（换人评审）**。
- **缺口**：**缺**。可直接把 A3 的 rubric 简化成我们「第二遍」流程（另开会话评审 → 贴回修改）。

## P8 确定性渲染（纯函数 / 种子 / 无状态）

- **结构**：显式要求「任意时刻可重绘同一帧」，禁止时间外状态与随机。
- **句式**：A1：`Rendering must be deterministic: every frame is a pure function of time t. Seeded randomness only; physics and particles precomputed or closed-form; no real-time clocks; no state-triggered CSS transitions.`；A7：`Every style is computed from time inside seek(t): no CSS transitions, no timers, no state carried between frames.`；A13：`只能使用设了种子的 RNG，种子常量为 0xA2E1 … 着色器里不要 Date.now，不要未设种子的噪声。`；A22：`ALWAYS use a seed for reproducibility … randomSeed(seed); noiseSeed(seed);`。
- **证据**：A1、A7、A13、A22。
- **15 卡对照**：15 卡靠「网页逐帧渲染 / Blender 渲染」隐含确定性，**没有一句话显式要求**。
- **缺口**：**缺**。建议在任务头固定句后加一行：`每帧是时间 t 的纯函数；随机只用种子随机；不用 Date.now / 实时时钟 / CSS transition。`

## P9 音画同源 + 卡点机制（cue sheet）

- **结构**：音乐音效同样用代码合成，且画面与声音共享同一张节拍表（单一事实来源）。
- **句式**：内部：`配乐音效也用代码合成、跟画面卡点`；A1：`Keep one cue sheet (beats and hit times) that both the picture and the sound read from.`；A7：`Analyze the song with numpy for the beat grid and start on a downbeat. Place every UI sound by its measured peak.`；A3 评审项：`visual hits aligned with audio onsets`。
- **证据**：A1、A3、A7 + 内部 15 卡。
- **15 卡对照**：**有要求，无机制**。外部把「卡点」落成文件（`cues.json`、`audio.py`）与可核对的评审项（hits vs onsets）。
- **缺口**：**半缺**（机制层）。可写进 B-02/B-03 管线：先出 `cues.json`，画面与音频同读。

## P10 分镜节拍表（钩子 → 升级 → 高潮 → 结尾）

- **结构**：按秒（或按拍）写出各段事件，首 0.5 秒必须有钩子，60–75% 处有 hero moment，结尾定帧并留微动。
- **句式**：A1：`a hook in the first 0.5 s (never open on more than 0.3 s of empty or black), an escalation, one unmistakable hero moment at ~60–75 % of the runtime, and a composed end frame held ~0.8–1.2 s with living micro-motion.`；A13：具名节拍 `0.0–4.0s DUST … 24.0–30.0s TOTALITY … 30.0–32.0s CODA 缓入与第 0 帧吻合`；内部内容段：`【10 秒分镜 + 结尾落地文案】`。
- **证据**：A1、A13 + 内部 15 卡。
- **15 卡对照**：**有分镜**（内容段自带收尾文案 = 验收锚点），但**没有**把「钩子 / hero moment / 定帧时长」写成显式三要素。
- **缺口**：**半缺**。建议 style_card 内容段加一行检查：`首 0.5s 钩子 / 60–75% 高潮 / 结尾定帧 0.8–1.2s（含微动）`。

## P11 输入槽与反问（【】/<inputs>/Ask me first）

- **结构**：把可替换内容留成槽位；更强者要求模型**先反问**收集输入，再开工。
- **句式**：内部页头：`提示词　暂停截图，【】里换成你的`；A7：`<inputs> Ask me for: 8 to 12 UI states I want the shape to become … and a royalty-free song around 120 BPM` + `<start> Ask me for the inputs, then show me the state list … before you write any code.`；A2：`想换成自己的内容：改 Creative seed 里的故事、品牌名、文案和配色`。
- **证据**：A2、A7 + 内部 15 卡（【】槽）。
- **15 卡对照**：**有槽（【】）但无反问**——15 卡是一次性投喂、无需交互。
- **缺口**：**半缺**。二选一：保持一次性投喂（现状），或加「先问三件事再动手」的开场协议（A7 式），后者适合 B-07 交互实验。

## P12 素材许可与商标规避

- **结构**：规定素材只能用可商用许可（CC0/PD/OFL/Apache），禁真实商标，虚拟品牌名，并记录来源到 CREDITS。
- **句式**：A1：`Assets: only CC0 / public domain / OFL / Apache / free-for-commercial-use. Record each source and licence in CREDITS.md. No real brand trademarks; invent brand names.`；A2：`品牌名和文案用虚构的，避免商标问题。`；内部：仅拼贴卡一句「素材只用公有领域的老照片和版画，不用 AI 人脸」。
- **证据**：A1、A2 + 内部 15 卡（单卡局部）。
- **15 卡对照**：**未通用化**（只在拼贴卡出现）。
- **缺口**：**缺**（通用化）。建议并入通用 Rules 段（一次写死，全卡继承）。

## P13 交付清单（Deliver：产物 + 报告）

- **结构**：除成片外，强制附带一份结构化报告：概念两句话、节拍表、签名特征的实现位置、技术路线、核对数字、自认的三个弱点。
- **句式**：A1：`Deliver: video.mp4, plus a short report: the concept in two sentences; a beat sheet with timecodes; how each signature feature is realised; the tech route; check numbers (duration, resolution, fps, loudness, true peak); your honest top-3 weaknesses.`
- **证据**：A1。
- **15 卡对照**：**没有交付报告要求**（只有成片 + 收尾文案锚点）。
- **缺口**：**缺**。这份报告同时是「人工验收的检查单」，建议加进 style_card。

## P14 对标基准 + 评分刻度（Benchmarks & rubric scale）

- **结构**：开头给「行业对标物」（谁的水准），评审时给「分数刻度定义」（6=模板级、8=头部机构、9=入围评奖），防模型/评审自嗨。
- **句式**：A1：`Benchmarks: Buck, ManvsMachine, Ordinary Folk, Giant Ant, Territory Studio, Apple keynote motion, Pentagram motion identities …`；A3：`(5 = competent student work; 6 = decent template level; 7 = solid professional; 8 = high-end agency work; 9 = award shortlist; 10 = best in the world). Most first renders deserve 5–7. Do not inflate.`；A1：`A clean, template-looking result is a fail.`
- **证据**：A1、A3。
- **15 卡对照**：**无对标物、无刻度**（15 卡默认「做得像样片」但没有把「像样片」翻译成可比较的锚）。
- **缺口**：**缺**。中文语境可给我们的对标物：B站/抖音头部设计账号、Motionographer 精选、Buck/ManvsMachine 等；刻度可直接沿用 6/8/9 三档。

---

## 对照 structure.md 15 卡：我们缺哪些模式（结论段）

**15 卡已具备（保留，别动）**：P2 任务句式（固定头）、P4 可判定约束（画风段）、P5 反约束（别做成）、P6 关键帧先行（三段流程）、P10 分镜（内容段雏形）、P9 卡点（要求层）。

**15 卡缺失（按补齐收益排序）**：
1. **P7 独立评审 + 自评分制**（收益最大：15 卡只有自查，外部是「制作→评审→修改→再评审」两轮闭环，A3 可直接裁剪使用）。
2. **P1 角色设定**（一行成本，全链路身份驱动）。
3. **P3 输出规格固定块**（补音频/编码/响度/文件名——决定产物能否直接交付）。
4. **P8 确定性渲染显式条款**（把隐含要求写死：纯函数 t、种子随机、禁 Date.now/CSS transition）。
5. **P13 交付报告**（概念/节拍表/核对数字/三个弱点 = 人工验收单）。
6. **P14 对标基准 + 评分刻度**（给「做得像样片」一个可比较的锚）。
7. **P12 素材许可与商标规避通用化**（从拼贴卡一条升级为通用 Rules）。
8. **P11 反问协议**（可选：先问输入再开工；与一次性投喂二选一）。
9. **P10 三要素显式化**（钩子 0.5s / 高潮 60–75% / 结尾定帧 0.8–1.2s）。
10. **P15 性能与环境约束**（60fps 目标、渲染管线固定步长——corpus A7/A11/A13；与 B-02/B-03 管线研究合并处理，不单列进 style_card）。

**两个极端样本（提醒不要过度泛化）**：外部体系存在光谱两端——A13/A1 的「工程规格书式」（长、可判定、可验收）与 A18/A16 的「放权式」（一句话，靠模型自觉）。15 卡处在中间偏规格侧；建议模板保留「规格书」为默认，另设 `放权实验卡` 单列，不要把两者混进同一张卡。

**外部体系与我们同构的确认**：A1 的 `Creative seed`（分镜+收尾）≈ 我们内容段；`Signature features（可检验）` ≈ 画风段；`Banned/别做成` ≈ 反约束段；`Key frames before motion` ≈ 6 关键帧。**两边是同一设计哲学的两种实现**——外部多出的正好是「质量门（P7/P13/P14）与工程条款（P3/P8/P15）」。

---

## 自审（四段）

### A 早产出
- `corpus.md` 先落盘（35.7KB），本文件随后；P1–P14 全部在 corpus 条目落地后才提炼，避免空转。

### B 反驳（挑 4 条最强结论逐条试推翻）
1. 「15 卡缺角色设定」→ 试推翻：重读 `knowledge/domains/motion-graphics/origin/提示词全文.md` 15 条全文，任务头均为「用代码做一支 10 秒的 MG 动画（…）」起句，无身份句 → **CONFIRMED**。跑过的命令：read 全文转录（15/15 条）。
2. 「外部 rubric 体系可整体搬用」→ 试推翻：A3 的评分维度（style_fidelity/concept_wow/motion_craft/design_typography/finish_texture/sound_sync/technical）以「MG 短片」为对象，我们的画家模块产物是「风格档案 + 组合实验」→ **WEAKENED**（只可搬「流程」：独立评审→修改单→再评审；维度需自建）。
3. 「P3 输出规格固定块缺失」→ 试推翻：内部 15 卡含「1920×1080，30 帧」「10 秒」「逐帧自查」，已覆盖分辨率/帧率/时长 → **WEAKENED**（改为「半缺」：缺音频/编码/响度/文件名，正文已按半缺写）。
4. 「P8 确定性是外部独有」→ 试推翻：内部卡「网页逐帧渲染」隐含需确定性帧才能捕获；且「逐帧自查」隐含可重放 → **WEAKENED**（结论改写为「未显式」而非「没有」，正文已按此措辞）。
5. 「Genuary/放权式样本算模式证据」→ 试推翻：A18/A16 无结构可提炼，仅证明「光谱存在」→ **CONFIRMED 但降级**（只作为「不要过度泛化」的反例引用，不作为模式证据）。

### C 机械验证
检查器：`bash` 计数 + `read` 抽 3 条 URL（与 corpus.md 文末「验证输出」节同一批）。
本文件计数（原样粘贴）：
```
$ grep -c "^## P" knowledge/agent-art/prompts/patterns.md
14
$ grep -c "^| P" knowledge/agent-art/prompts/patterns.md
14
```
（模式 14 条 ≥ brief 要求 8 条；3 条 URL read 原文见 corpus.md 文末）

### D 小结（≤14 行）
- 已确立：14 条模式中，15 卡**已具备 4 条**（P2 任务句式 / P4 可判定约束 / P5 反约束 / P6 关键帧先行）、**半缺 5 条**（P3 输出规格、P7 质量门、P9 卡点机制、P10 三要素、P11 反问）、**缺 5 条**（P1 角色设定 / P8 确定性条款 / P12 许可与商标 / P13 交付报告 / P14 对标与刻度）——计数口径与上方总表一致（4+5+5=14）。
- 被推翻/降级：Civitai 示例 prompt 假设（corpus.md 自审 B 第 4 条）、rubric 整体搬用、P3/P8「缺失」的绝对措辞（均降为半缺/未显式）。
- 未知：独立评审在我们项目里的「评审人」由谁当（主脑 vs 另一个模型）——留待主脑定。
- 下一步：把「P1/P3/P7/P8/P13/P14 六项」作为 `templates/style_card.md` 的候选增补，提交主脑评审；B-07 实验可直接用「有/无 P7 评审轮」做对照变量。
- 我仍赌错的是什么：高估了「社区 prompt 语料」的结构丰富度——821 作品里多数（如 A16/A18）只是一句话；真正结构化的是少数（A7/A13）与官方 skill（A22/A23）。下轮取语料应优先「带 rubric/模板的体系」而非「作品合集」。
