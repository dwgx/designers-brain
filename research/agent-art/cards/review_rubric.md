# AI 评审表 · 7 维 + 干净上下文终检（v0.2，改编自 mg-styles-15 `rubric.md` + vsc `final-review.md`）

> 版本 v0.2（2026-10-15）｜归属 GOALS B-11（StyleCardTemplates）｜v0.2 修订：B-18（TemplatesV03）
> 来源：① `Vincentwei1021/mg-styles-15` 的 `rubric.md`（raw 直读 2026-10-15；MIT，Copyright (c) 2026 Vincentwei1021）——§1–§3 为其中文改编版；② `Vincentwei1021/video-shotcraft` 的 `references/final-review.md`（raw 直读 2026-10-15；Apache-2.0）——§5「干净上下文终检」改编自它（vsc handbook §3.5 / §5.1 #5；「违反须记录」见 §2.6 / §5.1 #1）。§7 附两条 read 原样输出。
> 配套：`templates/style_card.md` v0.3（评审步骤引用本表；含判例式规则格式与 2 帧号）；`templates/determinism_contract.md`（评审前先跑 §3 自查）。
> 用法：成片 → 另开会话粘 §1（评审）→ 把评审贴回制作会话粘 §3（修改）→ 复评 → 交付前跑 §5 干净上下文终检（独立子代理，带帧号证据）。评分口径：7 维 1–10，目标 ≥9。

## 1. 第一轮 · 评审提示词（中文改编版，可直接粘）

```text
你是一位资深动态设计评委（对标：Motionographer 编辑、Buck / ManvsMachine 创意总监、抖音/B站顶级设计账号主理人）。
片子不是你做的。请严厉且精确地评审，目标是让它达到入围奖项 / 高端商业水准。客气无用，具体才是一切。

成片：<video.mp4 路径>。它用的提示词：<粘贴风格卡，至少含任务头、画风段、输出规格、别做成四段>。

1. 先认真看片：抽 contact sheet（每 0.5 s 一帧）、最快/最重要的动作段与高光时刻的 filmstrip、5–8 个关键时刻的全分辨率帧；
   在全分辨率下看小细节：边缘、字排、锯齿、banding、纹理、削波。
2. 核对规格：恰好 10.00 s；分辨率与帧率符合规格；有声；响度 ≈ −14 LUFS（±1）；真峰 ≤ −1 dBTP；
   除有意为之无黑帧；无意外静止段；视觉命中点与音频 onset 对齐。
3. 7 个维度各打 1–10 分（5 = 合格学生作业；6 = 模板水平；7 = 扎实专业；8 = 一线代理商；9 = 入围奖项；
   10 = 世界最强。首轮成片大多 5–7，Do not inflate——不许放水）：
   - style_fidelity 风格保真：一眼可识别为规范形态；每条签名特征与关键技法都在位、做对。
   - concept_wow 概念爆点：点子清楚；前 0.5 s 有钩子；有一个不容错认的高光时刻；结尾帧收得漂亮。
   - motion_craft 运动工艺：缓动、间距、重叠、预备与跟随、弧线、转场、运动模糊；没有死的或抖的运动。
   - design_typography 设计与字体：构图、层级、网格、字排（含中文）、色板、负空间。
   - finish_texture 质感与完成度：光照、纹理、颗粒、辉光与细节符合风格；无 banding、锯齿、瑕疵。
   - sound_sync 声音与同步：音乐性、风格正确性、音效设计、与画面同步、混音与母带。
   - technical 技术：规格达标、字体已加载、无故障、无削波与爆音。
4. 给出 5–10 条按「对最终印象的影响力」排序的修复。每条：时码、错在哪（可观察的现象）、为什么重要、
   具体怎么做（技法 + 数字：缓动曲线、帧数、像素、颜色、字体、版式改动）。宁要几个大升级，不要一堆挑刺；
   至少一条要抬 wow 因子，而不是只抛光。
5. 以下情况标 critical：看起来 generic / AI 模板感；中文文案不自然；fallback 字体或豆腐块；任何规格失败。
输出：评分表、critical 问题、修复清单。
```

## 2. 7 维评分表

| # | 维度（key 保留英文） | 中文名 | 判据（看什么） |
|---|---|---|---|
| 1 | `style_fidelity` | 风格保真 | 一眼可识别为规范形态；每条签名特征与关键技法都在位、做对 |
| 2 | `concept_wow` | 概念爆点 | 点子清楚；前 0.5 s 钩子；不容错认的高光时刻；结尾帧收得漂亮 |
| 3 | `motion_craft` | 运动工艺 | 缓动、间距、重叠、预备/跟随、弧线、转场、运动模糊；无死的/抖的运动 |
| 4 | `design_typography` | 设计与字体 | 构图、层级、网格、字排（含中文）、色板、负空间 |
| 5 | `finish_texture` | 质感与完成度 | 光照、纹理、颗粒、辉光、细节符合风格；无 banding/锯齿/瑕疵 |
| 6 | `sound_sync` | 声音与同步 | 音乐性、风格正确、音效设计、与画面同步、混音与母带 |
| 7 | `technical` | 技术 | 规格达标、字体已加载、无故障、无削波/爆音 |

**共用锚点（1–10）**：5 = 合格学生作业 ｜ 6 = 模板水平 ｜ 7 = 扎实专业 ｜ 8 = 一线代理商 ｜ 9 = 入围奖项 ｜ 10 = 世界最强；首轮成片大多 5–7；**Do not inflate**。
**评分行模板**：`| 维度 | 分（1–10） | 一句判词（含时码） |`

## 3. 第二轮 · 修改提示词（中文改编版，可直接粘）

```text
一位独立评委评审了你的片子，完整评审如下：
<粘贴评审>

把片子提升到入围奖项水准（每个维度目标 ≥ 9）：
- 先把当前成片与源码存为版本 N。
- 落实每一条 critical 与每一条高影响修复；如果有更好的解法可以替换清单里的做法，但要说明理由。
  在清单之外看到更大的升级（尤其是 wow 因子）也去做。评委列为优点的地方不许回退。
- 全分辨率重渲，重核规格，逐帧检查直到修复真正落地。
- 报告你落实 / 跳过了哪些修复，以及为什么。
```

## 4. 规格检查清单（spec check）

评审前先跑 `templates/determinism_contract.md` §3 的自查命令，把结果作为评审输入：

- [ ] 时长 exactly 10.00 s（或卡内声明规格）
- [ ] 分辨率 / 帧率符合卡内规格
- [ ] 帧数正确（30fps×10s = 300；`ffprobe -count_frames`）
- [ ] 有声；响度 ≈ −14 LUFS（±1）；真峰 ≤ −1 dBTP（`loudnorm`）
- [ ] 除有意为之无黑帧；无意外静止段（`freezedetect`）
- [ ] 视觉命中点与音频 onset 对齐（cue 表 vs 音轨包络）
- [ ] 无 fallback 字体 / 豆腐块；中文标点正确

## 5. 干净上下文终检（v0.2 新增；交付前最后一道）

> 来源：vsc handbook §3.5 / §5.1 #5——改编自 video-shotcraft 的 `references/final-review.md`（raw 直读 2026-10-15；Apache-2.0）。**裁剪口径**：输入清单按本项目裁剪（不照搬原 17 项）；检查项按我们的 7 维表分组（不照搬原 P/F/V/S/B/D/A/Q 八组）。

**纪律**：

- **独立终检**：派一个**干净上下文的子代理**（新会话 / 新 task agent，不参与制作）；**不给它制作过程中的理由、辩解、修改历史或预期结论**。
- **制作者确认偏差不可避免**：制作者自查 ≠ 终检；**首检永不直接交给用户**（「镜头视角很差」这类问题不许留给用户发现）。
- 每条结论**必须带帧号证据**（帧号 + 截图路径）；**缺输入标「无法验证」，不许猜**；输入互相冲突时**报告冲突来源**，不自行挑一个当真相；**不许用「整体不错」代替逐项检查，也不许为报告好看全部标通过**。
- **违反须记录**：规则（`S#` / `F#`）可以有意识地违反（风格需要），但每次违反必须写进项目说明文档（哪条、为什么）；**未记录的违反 = 缺陷**——终检核对记录完整性。

**审查输入（裁剪版；缺项标「无法验证」）**：

1. 最新成片 MP4 + 关键帧（6 关键帧 + 2 个验收帧号静帧）；
2. 使用的卡提示词全文（任务头 / 画风段 / 内容段 / 别做成 / 输出规格块）；
3. 机械自查报告（帧数 = 300、10.000000 s、色数、乱序重渲逐帧 SHA256、响度 / 真峰——命令 + 结果原样）；
4. 上一轮评审记录（7 维评分表 + 修复清单）与落实 / 跳过报告（版本 N 存档）；
5. 违反记录（见上「违反须记录」）；
6. 源码与渲染命令（可复跑）；素材与许可记录（CREDITS.md）。

**检查项分组（按 7 维表裁剪）**——逐组给结论：

| 组 | 查什么 |
|---|---|
| `style_fidelity` 风格保真 | 画风段 `S#` 逐条 ✓/✗、反约束 `F#` 逐条 ✓/✗（带帧号）；签名特征在关键帧可见 |
| `concept_wow` 概念爆点 | 前 0.5 s 钩子；高光时刻；结尾帧收尾文案（末帧锚点） |
| `motion_craft` 运动工艺 | 缓动 / 重叠 / 预备跟随；无死的、抖的运动；hold 呼吸 |
| `design_typography` 设计与字体 | 构图 / 层级 / 字排（中文）/ 色板 / 负空间；半像素、锯齿、文字锐度 |
| `finish_texture` 质感与完成度 | 材质 / 光照 / 颗粒符合风格；无 banding / 瑕疵；放大看细节 |
| `sound_sync` 声音与同步 | 卡点对齐（cue 表 vs 实际）；响度 ≈ −14 LUFS ±1、真峰 ≤ −1 dBTP；无削波 |
| `technical` 技术 | 规格（300 帧 / 10.000 s / 分辨率）；两跑一致（乱序重渲逐帧 SHA256）；字体加载 / 无豆腐块；无意外黑帧、静止段 |

**报告格式（帧号证据）**：

```text
style_fidelity ✗ f0210：画风段 S3「斜线一律 30°」在射线段被打破。
motion_craft ✗ f0150：落定后无 hold，直接切走。
sound_sync ✓ 6/6 卡点对齐（cue 表回测）。
technical ✗ f0290：两跑一致未通过（f0290 SHA256 不一致）→ 先修非确定性源。
```

末段按严重程度列出**必须修复项 / 建议优化项 / 无法验证项**；修复回流：画面实现 → §3 修改轮；卡 / 规格 → 改卡或改计划；声音 → 音频段。**必须修复项清零 + critical 清零后才可交付**。

（与 §1–§3 的关系：§1 / §3 是迭代期评审（打分 + 修改），§5 是交付前收口——两者不互相替代。）

## 6. 改动点（相对仓库 `rubric.md` 原文）

1. **语言**：提示词正文由英文改为中文（本项目评审会话用中文）；7 个维度 key、锚点关键句（"Do not inflate"）、5–10 条修复、时码要求保留原文。
2. **输入槽位化**：`<video.mp4 路径>` 与「粘贴风格卡」改为必填槽位，并写明至少含「任务头 / 画风段 / 输出规格 / 别做成」四段（对应本地四段卡）。
3. **评审前置自查**：新增 §4 spec 检查清单，指向 `determinism_contract.md` §3——先跑机器自查，评委以自查报告为输入（原版只要求评委自己抽帧核对）。
4. **锚点中文改写**：原版括号内英文判据逐条译成中文（§2 表 + §1 第 3 步）；分数锚点（5=学生…10=世界最强）与「首轮大多 5–7」语义不变。
5. **保留不动**：两轮制（评审 → 修改）、critical 旗标四类、修复清单排序规则、修改轮「存版本 N / 可替换须说明理由 / 不回退优点 / 重渲复核」。
6. **无删减项**：原版两段提示词的全部要求均保留（评委身份对标、看片方式、规格项、7 维、修复格式、critical、修改轮）。

**v0.2 追加（相对 v0.1，2026-10-15，B-18）**：

7. **干净上下文终检**（新增 §5）：独立子代理 + 带帧号证据 + 7 维分组检查（改编自 vsc `final-review.md`；输入清单裁剪、检查项按 7 维表分组——不照搬原 17 项）。
8. **违反须记录**（§5）：规则可有意识违反，但必须写进项目说明文档（哪条、为什么）；未记录 = 缺陷（来源：vsc handbook §2.6 / §5.1 #1）。
9. **帧号证据格式**（§5）：结论一律「维度 ✗ f####：现象」；缺输入标「无法验证」；不许「整体不错」、不许全部标通过（来源：vsc handbook §3.5 / §5.1 #5）。

**MIT 署名**：改编自 `Vincentwei1021/mg-styles-15` 的 `rubric.md`（MIT License，Copyright (c) 2026 Vincentwei1021）。按 MIT 条款，本文件及再分发需保留上述版权与许可声明。

## 7. 来源验证（read 原样输出，2026-10-15）

URL：`https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/rubric.md`

````
URL: https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/rubric.md
Content-Type: text/plain
Method: text

---

# 评审提示词：让另一个 AI 当评委，再拿评审意见改一轮

原片都是这样迭代出来的：制作 → 独立评审 → 按评审修改 → 再评审。下面两段提示词可以直接用。

## 第一步：评审（另开一个 AI 会话，把成片路径告诉它）

```text
You are a senior motion-design jury member (think: Motionographer editor, Buck/ManvsMachine creative director, a 抖音/B站
top design-account lead for the Chinese styles). You did NOT make this film. Judge it harshly and precisely so it can reach
award-level / high-end commercial quality. Kindness is useless here; specificity is everything.

The film: <path to video.mp4>. The prompt it was made from: <paste the style prompt, or at least its Style, Output and
Signature features sections>.

1. Look at the film properly: extract a contact sheet (a frame every 0.5 s), filmstrips around the fastest and most
   important moves and the hero moment, and full-resolution frames at 5–8 key times. Look at small details at full
   resolution: edges, type setting, aliasing, banding, texture, clipping.
2. Check the spec: exactly 10.00 s, resolution and fps as specified, audio present, loudness ≈ −14 LUFS (±1), true peak
   ≤ −1 dBTP, no black frames except intended, no unintended static spans, visual hits aligned with audio onsets.
3. Score 1–10 on each dimension (5 = competent student work; 6 = decent template level; 7 = solid professional; 8 = high-end
   agency work; 9 = award shortlist; 10 = best in the world). Most first renders deserve 5–7. Do not inflate.
   - style_fidelity: instantly recognisable canonical form; every signature feature and technique present and correct
   - concept_wow: a clear idea, a hook in the first 0.5 s, an unmistakable hero moment, a satisfying end frame
   - motion_craft: easing, spacing, overlap, anticipation and follow-through, arcs, transitions, motion blur; no dead or
     jittery motion
   - design_typography: composition, hierarchy, grid, type setting (CJK too), palette, negative space
   - finish_texture: lighting, texture, grain, glow and detail appropriate to the style; no banding, aliasing or artifacts
   - sound_sync: musicality, genre-correctness, sound design, sync to picture, mix and master
   - technical: spec compliance, fonts loaded, no glitches, clipping or popping
4. Give 5–10 fixes ordered by impact on the final impression. Each: timecode(s), what is wrong (observable), why it matters,
   and a concrete how-to (technique and numbers: easing curve, frame counts, px, colours, font, layout change). Prefer a few
   big upgrades over many nitpicks. At least one fix must raise the wow factor, not just polish.
5. Flag as critical: anything that reads as generic or AI-template, unnatural Chinese copy, fallback fonts or tofu, and any
   spec failure.
Return: the score table, the critical issues, and the fix list.
```
````

（以上为 read 工具输出前 41 行原样节选，含工具自带的 URL/Content-Type/Method 头；第二步修改提示词与全文见该 URL，逐条中文对照见本文件 §1–§3。）

**URL 2（v0.2 新增）**：`https://raw.githubusercontent.com/Vincentwei1021/video-shotcraft/main/references/final-review.md`

````
URL: https://raw.githubusercontent.com/Vincentwei1021/video-shotcraft/main/references/final-review.md
Content-Type: text/plain
Method: text

---

# final-review — 成片独立终检

独立审查 Agent 使用本清单验证“成片是否符合当前创作模式的制作基准”，并结合
`aesthetic-rules.md` 检查视觉技术质量。审查 Agent 必须处于干净上下文，不参与
制作；不要给它制作过程中的理由、辩解、修改历史或预期结论。

…

```text
P1 ✓ 产品定位和核心卖点清楚。
F2 ✗ 第 340 帧：已确认的知识图谱功能没有出现在成片。
V3 ✗ 第 420 帧：大面积琥珀纸张材质偏离已确认的深蓝科技方向。
S2 ✗ 第 515 帧：用户选择 whip-pan，实际实现为 flash-cut。
Q2 ✗ 第 615 帧：3D 推近后正文文字发糊，见关键帧 f615.png。
```

…

最后按严重程度列出必须修复项、建议优化项和无法验证项。不要用没有证据的
“整体不错”代替逐项检查，也不要为了报告好看而全部标记通过。
````

（以上为 read 工具输出节选：交接原则 / 报告格式 / 末段纪律；全文见该 URL。）
