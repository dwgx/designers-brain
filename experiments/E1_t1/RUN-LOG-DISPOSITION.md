# run_log.jsonl 处置注记（G7-S5 · 2026-11-16 · H4CandidatePrep）

> 依据：SUP/g7-inherited-calibration.md §G7-S5 + S18 路由摘要（媒体 URL 按「媒体公开权利/locator」处置，
> 不得因 provider 域名删除整份历史日志）。

1. **保留什么**：`run_log.jsonl`（37 条记录）整体保留——cell / attempt / status（200 与 502）/ 时间 / 尺寸 /
   sha256 字段是 E1_t1 的复现证据链；本注记不改动 jsonl 任何字节。
2. **36 条媒体 URL（`https://api.skiapi.dev/v1/media/images/img_…`）**：定性为**历史 locator**——
   记录「当时产物在 provider 托管侧的取回地址」，**不构成当前可用性承诺，也不构成对 URL 所指内容的权利验证**
   （本次未联网重验其可访问性 / 内容 / 许可）。消费方引用这些 URL 时必须带「历史 locator、未验权利」口径。
   provider 域名本身不是凭据（S18 判定）；未发现 userinfo 或敏感 query 参数名。
3. **36 个 SHA 字段**：是产物内容锚点；若媒体 URL 失效，以 sha 比对 `cells/<cell>/` 内落盘副本。
4. **关联处置**：请求端点私网地址已在 `E1_t1/_gen.py` 中改为显式环境变量配置（G7-S4，
   `IMAGE_GEN_ENDPOINT` / `IMAGE_GEN_API_KEY`）；本日志中的历史请求记录不改写（git 历史保留原值）。
5. **凭证边界**：本文件与日志均不含 API key 值；日志中的 `Authorization` 相关字段（如有）为脱敏/变量名形态。
