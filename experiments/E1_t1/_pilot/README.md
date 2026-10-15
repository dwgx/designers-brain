# _pilot — 管线试跑与参数探针（非 36 张正式产物）

本目录**不属于** E1_t1 的 12 格 × 3 张正式产物；是开跑前的一次管线验证与参数探针留档（2026-10-15）。

## 1. 管线试跑（6 张，与正式格同配方、同模型、同 size）

- `e0_baseline/`：主题句裸 prompt × 3（img_01..03 + req/resp 原样 JSON）
- `e1_van_gogh/`：主题句 + 梵高模块 §8.1 正向段 × 3（同上）
- `pilot_log.jsonl`：逐张尝试日志（同 run_log.jsonl 格式）

用途：验证「直连网关 → 下载 → 落盘 → 哈希」全链可用，并预览基线/风格化输出差异。
**不计入**正式统计（正式产物在 `../cells/`，日志在 `../run_log.jsonl`）。

## 2. 参数探针（2 张）

- `probe_redcircle_a.jpg`：`{"model":"grok-imagine-image-2.0","prompt":"a red circle on a white background","n":1}` → 200，768×1152 JPEG（无 size 参数）。
- `probe_redcircle_b.jpg`：同上 + `"size":"1024x1536"` + `"negative_prompt":"blue, green"` → 200，768×1152。
  结论：`negative_prompt` 为未知字段、被静默忽略（grok2api 请求 schema 无负向参数）；`size` 映射纵横比 2:3，像素尺寸由上游决定（不严格）。
- （另有 2 次带 `buddyfarm/` 前缀的模型名请求 → `model_not_found`，未落图；见 RESULTS.md §3。）

## 3. 与正式产物的关系

正式 36 张不包含本目录任何图片；正式重试与失败记录以 `../run_log.jsonl` 为准。
