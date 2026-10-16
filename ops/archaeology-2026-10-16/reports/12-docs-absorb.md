# 12 · DOCS-ABSORB — deepread 修订项 ④⑤（DB-7/8/9/6）落地（PROTOCOLS + ARCHITECTURE + WAVES + i18n）

> 写手：DocsAbsorb（站稳波 12 号）｜日期：2026-10-16｜状态：**完成（文件已落盘；未 commit）**
> 范围：① `docs/PROTOCOLS.md`（§8 检查①改路径级 + 新增 §12 + 固化 `templates/resume.md`）；② `docs/ARCHITECTURE.md`（新增 §3.4 `_private/` 契约）；③ `ops/WAVES.md`（新建，首版）；④ `docs/i18n/{zh-CN,ja}/PROTOCOLS.md` 同步。
> 来源：`ops/archaeology-2026-10-16/reports/08-absorb-check.md` §2 项 4/5 · `~/.dwgx/ops/research-2026-10-16-deepread/REVISION-BOARD.md` §L（DB-6..9 行）· `DEEP-DBRAIN.md` §③/§5.6/§6.B/§8。
> 纪律：逐文件最小 diff；不动数字计数（CountsFix 单管）；不动其它文档；不 commit；一写手一路径。

---

## 0 · 一句话结论

**DB-6/7/8/9 四项全部落地为文件**：PROTOCOLS §8 检查①改路径级（ModuleCards42 拒推事故的流程修复）、新增 §12「provider 抖动期工作法」、`templates/resume.md` 固化（与 `loop_goal.md` 并列）、ARCHITECTURE §3.4「`_private/` private-layer contract」、`ops/WAVES.md` 首版（**29 数据行** = wave1–21 + 收口三工 + 站稳波 W1/W1-R2）。i18n zh/ja 已同步（标记 3 处「（待复核）」）。

---

## 1 · 逐项 diff 摘要

### 1.1 `docs/PROTOCOLS.md` §8 检查① → 路径级（DB-7）

- **变更**：三检查①由「working tree clean」改为 **path-level clean**——`git status --porcelain <your write paths>` 为空 + 全树 `git status --porcelain` 只允许出现**已声明**的他人路径、须在回复中逐条列出；括注「本路径级规则即 ModuleCards42 拒推事故的修复」。
- **diff 规模**：1 行替换（本文件累计 +10/−1）。
- **依据**：DEEP-DBRAIN §④「push 三检查①被兄弟工单污染」+ 08 报告 §2 项 4。

### 1.2 `docs/PROTOCOLS.md` §12 新增「Provider-flap working method」（DB-8）

- **新节**（4 条）：每 10–15 分钟写盘（小段增量）→ 先探针再 **resume 同会话**（零产出从头 / 半产出从断点）→ 四段 `RESUME.md`（模板指针 `templates/resume.md`）→ **以轮次换完整率、绝不以降规格换完成率**。
- **位置说明**：置于 §11 之后（编号只增不改——不触动既有 §1–§11 与外部对「PROTOCOLS §8」的引用）。

### 1.3 `templates/resume.md` 固化（DB-8）

- **新文件**，与 `loop_goal.md` 并列：文件头（任务 / 写路径契约 / 状态 / 写盘时间）+ **四段**（已完成步骤 / 已抓素材清单 + URL / 下一步 / 已核实结论）+ 规矩行。
- **底稿**：wave19 十份 `RESUME.md` 实测结构（08 报告 §8.1：10/10 结构齐）；出处 `docs/PROTOCOLS.md` §12 · `ops/OPS-LOG.md` §16。

### 1.4 `docs/ARCHITECTURE.md` §3.4「The `_private/` private-layer contract」（DB-9）

- **新节**（4 条）：双保险忽略（`.gitignore` + `.git/info/exclude`）/ **INVENTORY 格式**（`ID | 标题 | … | 文件路径`，单写手合并）/ 公开侧零版权图 / **原住民伦理护栏**（Kngwarreye、Namatjira）/ **版权到期警示**（Namatjira 2029〔AU life+70〕、Hopper 1967+70）。
- **位置**：§3.3 之后、§4 之前（§3.x 子节编号只增）。

### 1.5 `ops/WAVES.md` 新建（DB-6）

- **一表四列**（波次 / agent / 目标 / 结局）：**29 数据行** = wave1–21（含 wave1·跨家、wave16·补、wave19·重派）+ 收口三工 + 站稳波 W1/W1-R2。
- **来源**：DEEP-DBRAIN §③ 19 波总表（转四列）+ 本波报告 01–10（02 补 wave20/21/收口；09 供 145 工单交叉；10 供名册口径）。
- **附加**：结局词表、报告↔工映射（01–10）、追加规矩；**兼作 deepread 指针落点**（文件头：`~/.dwgx/.../DEEP-DBRAIN.md`，替代 08 报告建议的 digest §6 方案）。

### 1.6 i18n 同步（`docs/i18n/zh-CN/PROTOCOLS.md` + `docs/i18n/ja/PROTOCOLS.md`）

- 两文件各三处：① baseline 行下加「Patch 2026-10-16」注；② §8 同句改路径级；③ §12 新增（按现有译文风格，术语沿用项目既有中文/日文口径）。
- **「（待复核）」标记 3 处**：zh §8（流程修复句）· ja §8（同句）· ja §12 标题——均为无既有译例的新表述，**仅标记措辞层面**（事实均有 commit/报告背书）。

---

## 2 · 复核输出（原样）

### 2.1 `git diff --stat`（本次改动文件）

```
 docs/ARCHITECTURE.md         |  9 +++++++++
 docs/PROTOCOLS.md            | 11 ++++++++++-
 docs/i18n/ja/PROTOCOLS.md    | 12 +++++++++++-
 docs/i18n/zh-CN/PROTOCOLS.md | 12 +++++++++++-
 4 files changed, 41 insertions(+), 3 deletions(-)
```

新增（未跟踪）：`ops/WAVES.md`（7,890 B）· `templates/resume.md`（1,215 B）· 本报告。

### 2.2 每节首行摘录

**① PROTOCOLS §8（改后首行）**

```
- Commit messages: English, imperative, no AI attribution. `commit` is free; **push requires the three checks** pasted in the reply: (1) **path-level clean** — `git status --porcelain <your write paths>` is empty, and the full-tree `git status --porcelain` contains only other writers' *declared* paths, each listed item-by-item in the reply (a whole-tree "clean" check never holds under parallel work — this path-level rule is the fix adopted after the ModuleCards42 push refusal); (2) local log matches intent, (3) diff stat has no unrelated files.
```

**② PROTOCOLS §12（新节首行）**

```
## 12. Provider-flap working method

When the model provider is unstable (streams ending mid-answer, batch failures), long-running work follows this method:
```

**③ ARCHITECTURE §3.4（新节首行）**

```
### 3.4 The `_private/` private-layer contract

`_private/` is the in-repo private research layer: copyrighted or otherwise unpublishable material (books, papers, hi-res images, videos) kept for depth. It is protected by a **double ignore guard** (`.gitignore` + `.git/info/exclude`) and never committed — `git status` must never show it.
```

**④ templates/resume.md（首行）**

```
# RESUME 写盘模板（provider 抖动期续跑）
```

**⑤ ops/WAVES.md（首行）**

```
# WAVES — 波次台账（agent · 目标 · 结局）
```

**⑥ zh-CN §8（改后首行）**

```
- 提交信息：英文、祈使句、不署 AI 名。`commit` 自由；**push 前必须通过三项检查**并在回复中粘贴：(1) **路径级干净**——`git status --porcelain <你的写路径>` 为空，且全树 `git status --porcelain` 只允许出现**已声明**的他人路径，并须在回复中逐条列出（多工并发下「全树干净」永远不成立——本项即 ModuleCards42 拒推事故的流程修复（待复核））；(2) 本地日志与意图相符，(3) diff stat 无无关文件。
```

**⑦ zh-CN §12（新节首行）**

```
## 12. provider 抖动期工作法

当 provider 不稳定时（流中途断开、批量失败），长任务按本工作法执行：
```

**⑧ ja §8 / §12（首行）**

```
- コミットメッセージ：英語、命令形、AI の帰属表示なし。`commit` は自由です。**push には 3 つのチェック**を返信に貼付することが必要です：(1) **パスレベルのクリーン**——`git status --porcelain <自分の書き込みパス>` が空であり、ツリー全体の `git status --porcelain` には**宣言済み**の他者のパスだけが現れ、返信で 1 件ずつ列挙すること（並行作業では「ツリー全体がクリーン」は決して成立しない——これは ModuleCards42 の push 拒否事案に対するプロセス修正（待复核））；(2) ローカルのログが意図と一致、(3) diff の統計に無関係なファイルがない。
```

```
## 12. プロバイダー不安定期の作業方法（待复核）

モデルプロバイダーが不安定なとき（応答ストリームの途中終了、バッチ失敗など）、長時間の作業はこの方法に従います：
```

### 2.3 WAVES 表行数 / 列校验

```
$ grep -c "^| " ops/WAVES.md          → 30   （表头 1 + 数据 29）
$ grep "^| " ops/WAVES.md | grep -vc "波次"   → 29
$ grep "^| " ops/WAVES.md | awk -F'|' '{print NF-1}' | sort | uniq -c
     30 5                              （全部行 4 列、无破行）
```

### 2.4 范围声明（只动本单文件）

`git status --porcelain` 核对：本次新增/改动 = 4 个 `M`（PROTOCOLS ×3 + ARCHITECTURE）+ `?? ops/WAVES.md`、`?? templates/resume.md`（+ 本报告）。其余 `M`（README×3 / ROADMAP×3 = CountsFix；GOALS / session-digest = 既有）与 `??`（archaeology 目录 / digest 备份）**均非本工产物，未触碰**。

---

## 3 · 未决项清单

1. **i18n「（待复核）」3 处**：zh §8 一句、ja §8 同句、ja §12 标题（`プロバイダー不安定期の作業方法`）——建议复核/母语者过目；其余按项目既有术语对齐（写盘 / resume 同会话 / 在飞 / 以轮次换完整率 等），未加标记。
2. **`docs/WORKFLOW.md` 未同步**检查①路径级口径（DB-7 原文曾提 `ops/WORKFLOW.md`；本单 Non-goal 限定只动 PROTOCOLS）——可作后续一行小项。
3. **i18n `docs/i18n/{zh-CN,ja}/ARCHITECTURE.md` 未同步 §3.4**（本单范围外；该文件头已有「可能滞后」声明）。
4. **未 commit**（纪律：不 commit）——4 改 + 3 新随主脑收口 sweep；`.before-standfirm-20261016` 备份件处置另案。
5. **WAVES 首版范围注**：含 wave20/21/收口/重派行（系报告 02 覆盖 wave11–21；保台账与 GOALS 一致）；「起始时间」列未含（四列约束），细节指向 DEEP-DBRAIN §③ / 报告 02。

---

## 4 · 自审四段

- **A 早产出**：先读源（08 §2 项4/5 → REVISION-BOARD §L → DEEP-DBRAIN §③ 全表 + §5.6/§6.B）→ 现态盘点（PROTOCOLS / ARCHITECTURE / templates / i18n / `_private` README+INVENTORY 实例 / wave19 RESUME 实测样本）→ 逐文件最小 diff 落盘（无攒批）。
- **B 反驳**：①「拒推事故」引用是否属实——08 报告 + DEEP-DBRAIN §④ 双证（ModuleCards42 末条回执原文「① 未过」）；②「RESUME 四段」口径——wave19 十份实测（08 §8.1）+ OPS-LOG §16，非自创；③ 弱点：WAVES 的「目标」列为编者归纳（非逐字转抄），已在文件内声明「细节以各报告为准」；i18n 未经独立审计（已标 3 处待复核）。
- **C 机械验证**：`git diff --stat` 4 files +41/−3；WAVES 30 行（表头 1 + 数据 29）、全行 4 列；首行摘录 8 处（§2.2）；范围核对通过（§2.4）。
- **D 小结**：DB-6/7/8/9 全落地；未决 5 条（i18n 复核为主）；不 commit，等收口。
