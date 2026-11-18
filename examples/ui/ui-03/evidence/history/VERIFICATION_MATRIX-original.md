# UI-03 五层验收矩阵（verification matrix）

每个层独立给结果；层与层不互相替代。**像素相似 ≠ 任务完成 ≠ 人类审美**；props/客观指标 ≠ 质量提升结论。
所有「real result」都指向本 lane 真实跑出的原始产物；untested 明确标注，不伪造成通过。

| 层 | 方法（可复演） | 真实结果 / 状态 | 证据 locator |
|---|---|---|---|
| **1. 几何 / 像素** | 同环境固定 320×200 viewport（headless `chrome-headless-shell` 156.0.8078.47, CDP `Page.captureScreenshot`）；`default.png` 作 baseline；用 **pixelmatch 8.0.0**（Playwright Test 同款库）计算差异像素；threshold `0.1`、maxDiffPixels `100`（Playwright doc 的 baseline/threshold 方法）。2-variant 矩阵：default↔hover、default↔dark；另加 default↔default-recheck 确定性对照。 | **已跑**。default↔hover = **631 / 64000** 像素（ratio 0.009859）；default↔dark = **59045 / 64000**（ratio 0.922578）；default↔default-recheck = **0 / 64000**（像素一致，证明同环境确定性）。三者均 `within_threshold` 判定：两个变体为 `false`（预期存在差异），对照为 `true`。这些是**几何数字**，不是审美、不是任务完成、不是接受结论。差异图 `raw/shots/diff-*.png`。 | `raw/visual.json` → `diffs[]`, `screenshots[]`, `methodology`; `raw/shots/*.png`; `fixture/run_visual.js` |
| **2. 行为** | (i) Node reducer 单测：点击 +1 / 键盘 +1 / disabled 阻断 / 重启用恢复 / 非法动作 no-op；(ii) 真 headless 浏览器内 dispatch `MouseEvent('click')` 与 `KeyboardEvent('keydown',{key:'Enter'})`，读回 DOM/state；(iii) disabled 后真实 click 不改 count。借 WebArena「程序化校验状态不变量」方法。 | **已跑，10/10 + 3/3 全通过**。Node checks `summary: total=10 passed=10 failed=0`（behavior 5/5、semantics 5/5），exit 0；headless DOM 交互 `total=3 passed=3 failed=0`（H1 real click count=1、H2 keyboard Enter count=2、H3 disabled 阻断 count 保持 2），exit 0。这是**功能/状态正确性**，不是视觉、审美或人类接受。 | `raw/checks.json`; `raw/visual.json` → `interactions.headless_behavior[]`, `interactions.summary`; `fixture/run_checks.js`; `fixture/run_visual.js` |
| **3. 语义** | 机械解析 `fixture/index.html`：role（原生 `<button type=button>`）、`aria-pressed`、`aria-label` accessible name 与组件常量比对、`aria-live="polite"`、可见文本标签；并在 headless 浏览器读回 LIVE DOM 复核。 | **已跑，通过**。静态 S1–S5 全 `ok:true`；LIVE DOM `role=button, ariaPressed=false, accessibleName="Add one to the counter" == constant`，`ok:true`。这是**标记/可访问性契约**，不等于视觉质量或人评。 | `raw/checks.json` → `semantics[]`; `raw/visual.json` → `interactions.live_semantics`; `fixture/index.html`; `fixture/component.js` |
| **4. 模型审美判断** | 若做，应由一个模型对 `raw/shots/*.png` 给出主观意见并标 `[归纳]/[推测]`；明确不作为质量结论。 | **UNTESTED（未做）**。本 lane 不产出模型审美意见；没有「模型觉得好看」这类 claim，也没有把它写成质量提升。理由：模型主观意见会污染分层验收，且与本 lane 交付的可判定结果无关。如后续需要，须单列为 `[推测]` 并配盲评协议。 | 本文件此行；`RESULT.md` 对应行 |
| **5. 人类判断** | 若做，需固定刺激 ID、配对/盲评、允许「不确定」、真实评者与时间、分歧与修订关系（按 03-RESEARCH-AGENDA §6）。 | **UNTESTED（未做）**。`human_review.status = not_applicable`，`actual_reviewer=null`，`record_path=null`。**没有任何人类验证声明**；不把「没有人评」写成「用户不认可」，也不把任一客观通过写成「人类接受」。 | `receipt.json` → `human_review`; 本文件此行 |

## 交叉判定（把层拼起来仍不能越界）

- 层 1+2+3 **全部通过**只能得到：`[归纳]` 本 fixture 在几何可复现、行为状态机、语义标记三方面可判定地符合其自身契约。
- 它**不能**推出：任务完成、可访问性合规（未做完整 WCAG 审计）、视觉美观、用户满意、UI 质量提升、或任何产品级结论。
- 层 4/5 为 untested，且本 lane 不含对照实验/主观评分，因此**不发布质量改进（quality improvement）结论**。
- Storybook MCP 仅核读方法（preview、框架 manifest 不一致）；WebArena 仅借用 functional-correctness 方法；二者「存在/被引用」都不作为质量证据。

## 环境一致性说明（针对 Playwright warning）

- baseline 与所有变体截图在**同一进程、同一 headless 二进制、同一 device metrics、同一窗口**内连续生成，满足 S14 的「same environment as baseline」前提。
- 第一次探针曾命中机器上已存在的用户 Chrome（端口 9333, Chrome/157.0.8103.51）；正式 driver 改为随机高端口 + `DevTools listening` 握手 + `/json/version` 回读，确认记录的是本进程启动的 `HeadlessChrome/156.0.8078.47`。该用户 Chrome 进程未被本 lane 触碰或关闭。
- `default-recheck` 与 `default` 像素差为 0，实证该环境几何可复现；跨 OS/浏览器/字体差异仍可能导致不同结果，按 doc 要求应各自维护 baseline。
