# HTTP 400 复现（最小无私密版）— grok-imagine-image 不支持 tools

> **2026-11-16 · G7-S8 处置（S18 校准：quarantine-original / reference-minimal-repro）**：原始 HTTP 运行快照
> `p1_grok-imagine-image_400.json`（旧 blob sha256 `354cda69662a109192ccde9a481ea067617b99bcda9ce2cf3dbddf83e0f84ee0`，
> 56,390 B / 486 行）含完整 system/user 消息正文（25,310 / 459 字符）、工具 schema 与私网 endpoint——
> **已从 public candidate 排除**（`git rm`；原件保留在旧 git 历史与 campaign staging 证据中，本处置不重写历史、不删除归档）。
> 本文件 = 与 400 问题相关的最小、无私密请求/响应结构 + 证据 hash；仅删除 Authorization 字段**不足以**公开整份 raw。

## 最小复现结构

```json
{
  "provider": "buddyfarm",
  "api": "openai-completions",
  "model": "grok-imagine-image",
  "method": "POST",
  "endpoint": "<config: 经环境变量 IMAGE_GEN_ENDPOINT 显式提供；原私网地址已从公开侧移除>",
  "body": {
    "model": "grok-imagine-image",
    "stream": true,
    "stream_options": {"include_usage": true},
    "max_completion_tokens": 2940,
    "tools": "<存在（图像生成上游不支持）>",
    "messages": "<省略：完整消息正文属非公共运行上下文>"
  },
  "errorResponse": {
    "status": 400,
    "message": "400 图片生成模型不支持 tools\n图片生成模型不支持 tools (type=invalid_request_error param=upstream_error)"
  }
}
```

## 要点（历史测量结论，非当前可用性保证）

- 失败条件：向图像生成模型（`grok-imagine-image` 系）的 chat/completions 请求携带 `tools` 字段 → 上游 400
  `invalid_request_error`（"图片生成模型不支持 tools"）。去 tools 重试即通过（该批次其余请求 200）。
- 原始证据：旧 blob `354cda69662a109192ccde9a481ea067617b99bcda9ce2cf3dbddf83e0f84ee0`（sha256，未公开）。
  Authorization 字段在原件中已脱敏（10 字符占位，非 Bearer 明文）——但 S18 判定：header 脱敏 ≠ raw 快照可公开。
- 处置链：staging/CANDIDATE-PREP/phase4/g7-final-report.md（G7-S8 行）；
  校准依据 SUP/g7-inherited-calibration.md §G7-S8。
