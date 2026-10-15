# 图像生成通道调研与探针（B-20 · E 系列前置）

> 任务：盘点本机可用的「图像生成通道」（供 E 系列风格实验用），逐个实测并留档。
> 方法：omp CLI 探针 ×6 + 直连网关探针 D1–D8 + D3b + 本机只读扫描（2026-10-15 晚，全部实测；原始输出全量留档在 `research/agent-art/cards/_image_probes/`）。
> 环境：omp v18.10.4 · 网关 `http://192.168.11.4:3000/v1`（公网同实例 `https://api.skiapi.dev`）· RTX 5070 Ti Laptop · Python 3.14（Pillow 12.3）。
> 证据分级：`[实测]`=本次跑过/读过（命令与输出在案）；`[自述]`=他方文档原话（SKIAPI/BuddyFarm，2026-10-12/13 版）；`[归纳]`=本次总结；`[UNVERIFIED]`=未跑未核。
> 姊妹材料：`D:/Project/SKIAPI/docs/operations/media-models-console.md`（同题矩阵，10-12/10-13 测，本卡 10-15 复测互证）· `D:/Project/BuddyFarm/docs/ANALYST-2026-10-12.md`（池 403 噪声口径）。
> 合规口径：全程**未碰任何账号/浏览器登录页**（唯一一次浏览器访问是 omp 回退模型的自动行为，匿名态、被登录墙挡下，见 §2.4）；对网关的调用使用本机既有 `BUDDYFARM_API_KEY`（与 omp 同源），只读盘点未改任何配置。

## 0. 结论速览（先看这）

1. **可用通道已找到：直连网关 API 出「真图」。** `grok-imagine-image / -2.0 / -lite` 经 `/v1/chat/completions` 或 `/v1/images/generations` 均返回真实生成图（JPEG，markdown 图链或 `data[0].url`）；`-edit` 走 `/v1/images/edits`（JSON `image.url`）；`grok-imagine-video` 走 `/v1/videos` 任务流。本卡实测 **6 张直连生成图 + 4 张 omp 对照图 + 1 段视频，全部下载并校验**（含一张「暴风雨灯塔·油画风格」，即 E 系列目标场景）。**E 系列可直接用（走直连 API，不走 omp CLI）。** `[实测]`
2. **omp CLI 默认路径不可用，且有「静默回退」陷阱。** `omp -p --model buddyfarm/grok-imagine-image` 因请求携带 tools 被上游 400 拒绝（`图片生成模型不支持 tools`），随后 omp **静默回退**到 `buddyfarm/deepseek-v4.1-flash`；回退模型用 **Python/Pillow 代码画图**并落盘——文件是真 PNG，但**不是生成模型产物**。这正是「grok-imagine-image 返回 Python/Pillow 代码绘图」现象的机制：**不是图像模型不会出图，而是 omp 的 fallback 链在替它"画"**（三层机制与证据见 §2.3）。`[实测]`
3. **裸模型名有坑。** `--model grok-imagine-image`（不带 provider 前缀）会被模糊匹配到 zenmux 提供商（无 key）→ `No API key found for zenmux`；必须写全 `buddyfarm/grok-imagine-image`。`[实测]`
4. **本机没有现成本地出图环境。** ComfyUI 曾于 9/30 装过（视频向，54 个任务全 completed），**现已被删**（目录/模型/进程全无）；stable-diffusion 系未发现；除 `BUDDYFARM_API_KEY` 外无任何图像 API key。`[实测]`
5. **下一步（建议）：** E 系列直接用 §6 的 recipe（推荐 `grok-imagine-image-2.0`，快用 `-lite`）；omp CLI 路径不用；本地线如需再找 Owner 拍板（清单见 §5）。

## 1. 通道对照表

| # | 通道 | 实测结果 | 可用性 | 限制 | 下一步 |
|---|---|---|---|---|---|
| 1 | omp CLI × `buddyfarm/grok-imagine-image` | 400 `图片生成模型不支持 tools` → 静默回退 deepseek → Pillow 画 512×512 PNG（12399B）；末轮 403；exit=1，37s | ❌ 不可用 | ①tools 被上游拒 ②静默 fallback 伪装结果 ③偶发上游 403 | 弃用；改直连（#5） |
| 2 | omp CLI × `buddyfarm/grok-imagine-image-2.0` | 同机制；exit=0（12s）；stdout 自述 "generated programmatically (Python/PIL)" | ❌ 不可用 | 同上 | 同上 |
| 3 | omp CLI × `buddyfarm/grok-imagine-image-edit` | 400 `图片编辑模型请使用 /v1/images/edits...` → 回退 → Pillow 图；exit=0（24s） | ❌ 不可用 | 同上；edit 模型需输入图 | 同上 |
| 4 | omp CLI × `buddyfarm/grok-imagine-image-lite` | 同机制；末轮 403；exit=1（32s） | ❌ 不可用 | 同上 | 同上 |
| 4b | omp CLI `--no-tools` 变体 | MCP 工具仍在 → 400 复现 → 回退模型改走浏览器（grok.com/imagine，匿名需登录）→ 120s 超时零产出 | ❌ 不可用 | MCP 工具无法一键禁用 | 忽略此路径 |
| 5 | **直连 `/v1/chat/completions`**（无 tools） | ✅ 3/3 模型返回 markdown 图链；图片公网可达（JPEG） | ✅ 可用 | 回复是文本，需自抽 URL；需 key | E 系列路径 A |
| 6 | **直连 `/v1/images/generations`** | ✅ `data[0].url`；带 `size` 参数（实回 1152×768，未严格等于请求） | ✅ 可用 | size 行为不完全可控；JPEG 输出 | **E 系列路径 B（推荐）** |
| 7 | **直连 `/v1/images/edits`** | ✅ JSON `image.url`（hosted URL）→ 改色成功；multipart/base64 均被拒 | ✅ 可用（纯 API） | 必须 hosted URL；控制台无入口 | 编辑/风格迁移实验 |
| 8 | **直连 `/v1/videos`** | ✅ 1s / 1280×720 / H.264 MP4；create→completed 约 37s | ✅ 可用 | 任务式轮询；更高档依赖账号 tier | 视频实验 |
| 9 | 公网域名 `api.skiapi.dev` | ✅ 与 LAN 同实例，chat 路径 200 | ✅ 可用 | 需 key；媒体 URL 公网可达 | 跨机/远程使用 |
| 10 | 本机 ComfyUI（历史） | ⚠️ 曾装（9/30 视频实验），现目录已删、无残留 | ❌ 当前不可用 | 重装需下载模型（GB 级） | 如需本地线：Owner 拍板 |
| 11 | 本机 stable-diffusion 系 | ❌ 未发现（无安装/模型/包） | ❌ | — | 放弃或重装 |
| 12 | 其它图像 API key | ❌ 未发现（仅 `BUDDYFARM_API_KEY`；其余全是 .env.example 模板） | ❌ | — | 见 §5 |
| 13 | grok.com 网页（浏览器） | ❌ 需登录（匿名态不可生成）；不使用 Owner 账号 | ❌（且不采用） | — | 不做 |

> 计数口径：omp CLI 探针 6 次（4 模型 + 裸名 + `--no-tools`）；直连网关探针 D1–D8 + D3b（含 2 次失败格式尝试，§3 全部留档）；本机扫描见 §4。全部原始输出见 `_image_probes/`（§7 文件树）。

## 2. 探针 A：omp CLI（原样命令与输出）

### 2.1 命令与执行矩阵

命令模板（逐模型执行；工作目录=各自探针目录，产物即落于此）：

```bash
cd "D:/Project/Designers_Brain/research/agent-art/cards/_image_probes/<pN>_<模型>"
"C:/Users/dwgx1/AppData/Local/omp/omp.exe" -p --no-title --max-time 120s --model buddyfarm/<模型id> \
  "Generate one image: a red circle on a white background. Save it to ./red_circle.png in the current working directory, then reply with the saved path or explain what you produced."
```

| 探针 | 模型（--model 实参） | exit | 耗时 | 产物文件 | 产物格式 | stdout/stderr |
|---|---|---|---|---|---|---|
| P1 | `buddyfarm/grok-imagine-image` | 1 | 37s | `red_circle.png` 12399B | PNG 512×512 | stdout 空；stderr=403（末轮） |
| P2 | `buddyfarm/grok-imagine-image-2.0` | 0 | 12s | `red_circle.png` 3359B | PNG 512×512 | stdout=自述「programmatically」 |
| P3 | `buddyfarm/grok-imagine-image-edit` | 0 | 24s | `red_circle.png` 3359B | PNG 512×512 | stdout=自述「Pillow」 |
| P4 | `buddyfarm/grok-imagine-image-lite` | 1 | 32s | `red_circle.png` 3397B | PNG 512×512（手写 zlib/struct） | stdout 空；stderr=403 |
| P1a | `grok-imagine-image`（裸名，对照） | 1 | 2s | 无 | — | stderr=`No API key found for zenmux` |
| P1b | `buddyfarm/grok-imagine-image` + `--no-tools` | 1 | 120s | 无 | — | stderr=`Deadline exceeded` |

> 关键点：**4 个模型全部走了同一个三段式**：①400（tools 被拒）→ ②静默回退 deepseek-v4.1-flash → ③用代码画图。产物「图像文件」确实产出了（落点在探针 cwd），格式是真 PNG，但**内容来自代码绘制而非图像模型**（见 §2.3）。`[实测]`

### 2.2 原样输出（全量）

**P1a 裸模型名失败（`--model grok-imagine-image`，2s）：**

```
Working...
46412 | ` + `Use /login, set an API key environment variable, or create ${Xt()}
46413 | 
46414 | ` + "Then use /model to select a model.");
46415 |       }
46416 |       const E = await this.#B.getApiKey(this.model, this.sessionId);
46417 |         throw new Error(`No API key found for ${this.model.provider}.
                      ^
error: No API key found for zenmux.

Use /login, set an API key environment variable, or create C:\Users\dwgx1\.omp\agent\agent.db
      at #Qs (B:/~BUN/root/chunks/cli-ah31rv0s.js:46417:15)
      at async #io (B:/~BUN/root/chunks/cli-ah31rv0s.js:46163:26)


[Recovery]
  Main: omp --resume 01a13ee8-ad42-738c-8544-716cf2d3ce7e
```

（根因：omp 内置 zenmux 提供商目录里也有同名模型，模糊匹配优先命中它；zenmux 无 key。日志证据：`_evidence/p1a_bare_id_omp_log.log` —— `Phase1 skipped: no API key for phase1 model / provider=zenmux / model=x-ai/grok-imagine-image-2.0`。）

**P1（grok-imagine-image）stderr：**

```
Working...
403 the model provider refused this request; retry later or change the request - request content was rejected by content policy; adjust the prompt and retry
the model provider refused this request; retry later or change the request - request content was rejected by content policy; adjust the prompt and retry (type=invalid_request_error)
```

**P1 会话轨迹（原样摘录，`_evidence/sessions/p1_session.jsonl`）：**

```
[2] MODEL_CHANGE: buddyfarm/grok-imagine-image   (fallback=false)
[3] user: "Generate one image: a red circle on a white background. Save it to ./red_circle.png ..."
[4] MODEL_CHANGE: buddyfarm/deepseek-v4.1-flash  (role=fallback, resolvedModelIsFallback=true)
[6] assistant ERROR(400): 400 图片生成模型不支持 tools
    图片生成模型不支持 tools (type=invalid_request_error param=upstream_error)
    raw-http-request=C:\Users\dwgx1\.omp\logs\http-400-requests\1792056847020-ddf77s23lex1.json
[8] assistant TOOL eval: { Pillow 画圆脚本 }        ← 回退模型（deepseek）写的代码
[10] toolResult: saved red_circle.png | 12399 bytes | verify: (512,512) center px (255,0,0)
[11] assistant ERROR(403): 403 ... content policy ...
[12] session_exit
```

**P2（-2.0）stdout（全文）：**

```
Done. I generated the image programmatically (Python/PIL) and saved it to:

**`./red_circle.png`** → `D:\Project\Designers_Brain\research\agent-art\cards\_image_probes\p2_grok-imagine-image-2.0\red_circle.png`

Details:
- 512×512 PNG, white background, red circle (RGB 220, 30, 30) centered with a 64px margin
- Verified: center pixel is red `(220, 30, 30)`, corner pixels are white `(255, 255, 255)`

Note: I don't have a generative image model available in this session, so I produced the image by drawing it directly — which gives an exact, clean result for a simple shape like this.
```

**P3（-edit）stdout（全文）：**

```
Done — image generated and verified (I rendered it programmatically with Pillow, since no image-model tool is available in this session).

- **Saved to:** `D:\Project\Designers_Brain\research\agent-art\cards\_image_probes\p3_grok-imagine-image-edit\red_circle.png`
- **Contents:** 512×512 PNG, white background, solid red circle (RGB 220, 30, 30) centered with a 64px margin — confirmed by re-reading the file.
```

**P4（-lite）stderr：**

```
Working...
403 the model provider refused this request; retry later or change the request - request content was rejected by content policy; adjust the prompt and retry
the model provider refused this request; retry later or change the request - request content was rejected by content policy; adjust the prompt and retry (type=invalid_request_error)
```

**P1b（`--no-tools` 变体）stderr：**

```
Working...
Deadline exceeded
```

### 2.3 现象解剖：「Python/Pillow 代码绘图」是怎么发生的（把这一现象写清楚）

**现象**：以 `buddyfarm/grok-imagine-image` 为目标模型跑 omp CLI 探针，最终「生成」出的是一张 512×512 PNG 红圆——由**一段 Python/Pillow 绘图代码执行**得来；`-2.0` / `-edit` / `-lite` 三个模型表现完全相同。表面看像「模型不务正业」，实际机制是三层叠加（全部有原始记录）：

1. **第一层：图像模型拒收 tools。** omp 是 agent 框架，请求体默认带 11 个工具 schema（`body.tools` 有 11 项，见 raw 记录）。网关把 `grok-imagine-image` 路由到**真正的图像生成模型**，该模型不支持 tools → 上游直接 400：`图片生成模型不支持 tools`。原始记录（`_evidence/http400/p1_grok-imagine-image_400.json`）：
   ```jsonc
   { "provider":"buddyfarm", "model":"grok-imagine-image",
     "url":"http://192.168.11.4:3000/v1/chat/completions",
     "body": { "model":"grok-imagine-image", "stream":true, "tools":[11 项], "messages":[…] },
     "errorResponse": { "status":400, "message":"400 图片生成模型不支持 tools\n图片生成模型不支持 tools (type=invalid_request_error param=upstream_error)" } }
   ```
2. **第二层：omp 静默回退（关键）。** omp 配置 `modelFallback: true` + `fallbackChains: buddyfarm/* → buddyfarm/deepseek-v4.1-flash:max`，400 触发**自动重试并换模型**；会话日志记 `resolvedModelIsFallback=true`，但 **CLI 界面无任何提示**——用户视角只会看到「最后出了一张图」，不会知道出图的是回退后的文本模型。
3. **第三层：回退模型用代码画图。** `deepseek-v4.1-flash` 有 eval/bash 工具但没有出图工具，于是按「生成图片」的指令**写 Pillow 代码绘制**（P4 甚至是手写 zlib/struct 手工拼 PNG）。所以产物是真 PNG、内容却是「代码绘图」——这也解释了为什么它是 512×512 的精确几何图形，而非生成模型风格的图。

**结论**：`[实测]` 该现象与图像模型本身无关，是 **omp 封装层（tools 参数 + 静默 fallback）** 的产物。要拿生成模型的图，必须**绕过 omp** 直连网关（§3）——去掉 tools 后同一模型 6 秒即返回真实图片 URL。附带坑：`-edit` 模型在 chat 路径会报另一句 400（`图片编辑模型请使用 /v1/images/edits…`），同样触发回退。

**副产品说明**：如果目标恰好是「代码绘图」（如 B 系列代码作画对照），这条 omp 路径倒是能稳定产出 Pillow 图——但它不可控（有时末轮 403、有时耗时 120s），**不作为通道推荐**。`[归纳]`

### 2.4 附注：`--no-tools` 变体（已测，不通）与浏览器路线

`--no-tools` 只关「内置工具」，**MCP 工具（chrome-devtools/codegraph）仍会附带** → 400 复现、再次回退；且这次回退模型改走浏览器路线：打开 `grok.com/imagine` 尝试匿名生成 → 被登录墙拦下（`No auth token — anonymous user`）→ 转而用 `file://` 浏览本地探针文件 → 最终 120s `Deadline exceeded`、零产出。`[实测]`

> 两点说明：①该浏览器行为是**回退模型的自动选择**，全程匿名态、未登录任何账号、未生成任何内容；②即便能登录也不应采用——「不使用 Owner 账号/浏览器」是硬约束。此路线判定为**死路**，不再挖。

## 3. 探针 B：直连网关（原样命令与输出）

### 3.1 拓扑与凭据（只读说明）

- 网关：`http://192.168.11.4:3000/v1`（本机 omp `models.yml` 中 buddyfarm 的 baseUrl；= 公网 `https://api.skiapi.dev` 同一实例）。`[实测]`（`_gateway_models.json`：33 个模型，含 5 个 grok-imagine 系）
- 凭据：`BUDDYFARM_API_KEY`（从 `~/.omp/agent/.env` 读取，**未写入任何产物**）。`[实测]`
- 调用形态：OpenAI 兼容。图像三条路：chat（markdown 图链）/ generations / edits；视频走任务式 `/v1/videos`。媒体文件托管在 `api.skiapi.dev/v1/media/images/<id>`，**公网直达（无需额外鉴权）**。`[实测]`

### 3.2 chat 路径（D1/D2/D3b：三模型全通；D3：-edit 指路）

```bash
curl -sS "http://192.168.11.4:3000/v1/chat/completions" -H "Authorization: Bearer $BUDDYFARM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"grok-imagine-image","messages":[{"role":"user","content":"Generate an image: a red circle on a white background."}],"stream":false}'
```

**D1（grok-imagine-image，6.5s）原样响应：**

```json
{"choices":[{"finish_reason":"stop","index":0,"message":{"content":"![image](https://api.skiapi.dev/v1/media/images/img_tLVwYW89UQQLP5_xyMGczk-MEW83n6pM)","reasoning_content":"","role":"assistant"}}],"created":1792056942,"id":"chatcmpl_20ede60be47736d0b9d33e839ffd501c","model":"grok-imagine-image","object":"chat.completion","usage":{"completion_tokens":22,"prompt_tokens":14,"total_tokens":36}}
```

**D2（-2.0，6.2s）原样响应：**

```json
{"choices":[{"finish_reason":"stop","index":0,"message":{"content":"![image](https://api.skiapi.dev/v1/media/images/img_OTZl6h8-ffH6Oq5c9TqV7m_5TPkcpI-G)","reasoning_content":"","role":"assistant"}}],"created":1792056969,"id":"chatcmpl_36cd19af6cee49991051cdc2ef70a1ec","model":"grok-imagine-image-2.0","object":"chat.completion","usage":{"completion_tokens":22,"prompt_tokens":14,"total_tokens":36}}
```

**D3（-edit 在 chat 路径，0.03s）原样响应（指路 /v1/images/edits）：**

```json
{"error":{"message":"图片编辑模型请使用 /v1/images/edits，并在当前请求中显式提供输入图片","type":"invalid_request_error","param":"","code":null}}
```

**D3b（-lite，2.2s）原样响应：**

```json
{"choices":[{"finish_reason":"stop","index":0,"message":{"content":"![image](https://api.skiapi.dev/v1/media/images/img_2fSKWPGdsDUoBcVrzLR1Egsiycl9ZKHn)","reasoning_content":"","role":"assistant"}}],"created":1792056972,"id":"chatcmpl_f36d4eb3897320349d9dd8f3eaecef23","model":"grok-imagine-image-lite","object":"chat.completion","usage":{"completion_tokens":22,"prompt_tokens":14,"total_tokens":36}}
```

下载校验（原样命令输出）：`HTTP 200` ×3，`image/jpeg`；D1=83715B(768×1152) · D2=55234B(768×1152) · D3=616431B(832×1248)。文件：`d1_grok_imagine_image.jpg` / `d2_grok_imagine_image_2.0.jpg` / `d3_grok_imagine_image_lite.jpg`。`[实测]`

### 3.3 `/v1/images/generations`（D5/D8：含 E 系列目标场景实测）

**D5（灯塔·油画风格，5.9s）原样响应：**

```json
{"created":1792057202,"data":[{"mime_type":"image/jpeg","revised_prompt":"","url":"https://api.skiapi.dev/v1/media/images/img_L5JXyBXT2yx9nn5AKUrh-VwJXp9F_26u"}]}
```

请求体（原样）：`{"model":"grok-imagine-image","prompt":"a lighthouse on a rocky coast in a storm, oil painting style","n":1}` → 下载为 `d5_lighthouse.jpg`（352379B，768×1152 JPEG）。**肉眼核验：笔触感油画、风暴氛围、灯塔主体——E 系列场景可用。** `[实测]`

**D8（-2.0 + `size:"1536x1024"`，12.7s）原样响应：**

```json
{"created":1792057624,"data":[{"mime_type":"image/jpeg","revised_prompt":"","url":"https://api.skiapi.dev/v1/media/images/img_b3R8lYmLb1aOaukMFmMuVrXyy01T2DqC"}]}
```

下载为 `d8_lighthouse_1536x1024.jpg`（435725B）——**实际返回 1152×768，未严格等于请求的 1536×1024**。`[实测]`（size 参数被接受但未精确兑现；如需精确尺寸建议生成后裁剪/缩放，或按 SKIAPI 文档口径 `size ∈ auto|1024x1024|1024x1536|1536x1024` 再试 `[自述]`。）

### 3.4 `/v1/images/edits`（D4：格式三连测，仅 hosted URL 可用）

**失败①（multipart 表单，0.03s）原样响应：** `{"error":{"message":"图片编辑仅支持 application/json","type":"invalid_request_error","param":"","code":"invalid_request"}}`

**失败②（JSON + base64 内联，0.008s）原样响应：** `{"error":{"message":"图片编辑 JSON 请求无效","type":"invalid_request_error","param":"","code":"invalid_request"}}`

**成功（JSON + `image.url`，10.6s）原样响应：**

```json
{"created":1792057196,"data":[{"mime_type":"image/jpeg","revised_prompt":"","url":"https://api.skiapi.dev/v1/media/images/img_c-2Eh9PRsK-Y7_JThye4wkIn10GQzcw8"}]}
```

请求体（原样）：`{"model":"grok-imagine-image-edit","prompt":"make the red shape blue, keep everything else the same","image":{"url":"https://api.skiapi.dev/v1/media/images/img_tLVwYW89UQQLP5_xyMGczk-MEW83n6pM"},"n":1}` → 下载为 `d4_edit_result.jpg`（167395B，832×1248）——**红色圆顶被改为蓝色、其余保持**，编辑有效。`[实测]`

### 3.5 `/v1/videos`（D6：任务式，全链 200）

**创建（0.02s）原样响应：**

```json
{"id":"task_DP5eJIg3N562gNVP0JbNZi0LxuVnYnW0","object":"video","model":"grok-imagine-video","status":"queued","progress":0,"created_at":1792057475}
```

**轮询（约 37s 后）原样响应：**

```json
{"completed_at":1792057512,"created_at":1792057475,"id":"task_DP5eJIg3N562gNVP0JbNZi0LxuVnYnW0","model":"grok-imagine-video","object":"video","progress":100,"seconds":"1","status":"completed"}
```

**取内容：** `HTTP 200, 249103 bytes, type=video/mp4`；魔数 `ftypisom` ✓；ffprobe：`h264 1280×720`，`duration=1.04s`，含 aac 轨。文件：`d6_video_test.mp4`。`[实测]`

> 注：首测曾报 `Invalid token` —— 系我脚本里 key 尾带 `\r` 所致（修掉后 200），**非通道问题**，如实记录。

### 3.6 公网域名（D7）与交叉核对

**D7（`https://api.skiapi.dev` chat 路径，5.8s）原样响应：**

```json
{"choices":[{"finish_reason":"stop","index":0,"message":{"content":"![image](https://api.skiapi.dev/v1/media/images/img_sd0pzWhSTbhkp446hcWoPLrLTCEvABgt)","reasoning_content":"","role":"assistant"}}],"created":1792057466,"id":"chatcmpl_dc553084064f5e010961c9a83274b11b","model":"grok-imagine-image-lite","object":"chat.completion","usage":{"completion_tokens":22,"prompt_tokens":10,"total_tokens":32}}
```

**交叉核对（`[自述]` vs `[实测]`）**：SKIAPI 的 `media-models-console.md`（10-12/10-13 测）结论为「三模型 chat + generations 双通、edit 走 JSON `image.url`、video 经 `/v1/videos` 修复后 11/11=200」——**与本卡 10-15 的独立复测逐项一致**（唯一新增观察：size 参数未严格兑现；`-edit` 必须 hosted URL，b64 不支持，与文档同）。媒体 URL 公网可达性：本卡 8 个 URL 全 200（JPEG 魔数校验）。`[实测]`

## 4. 本机其它候选盘点（只读；不碰账号）

### 4.1 stable-diffusion / ComfyUI —— 结论：现在都没有

- **ComfyUI：曾装、已删。** 证据链：① `AppData/Local/comfy-cli/config.ini` 指向 `D:\LLM_Model\ComfyUI-MiniMax-H3\ComfyUI_windows_portable\ComfyUI`；② comfy-cli 的 54 个任务记录（2026-09-30，全部 completed，输出均为 `output\video\*.mp4`，i2v/t2v 视频向）；③ 现状核查：该目录**已不存在**（`D:/LLM_Model/` 只剩 RWKV 文本模型；多轮全盘搜索零命中：D:/ 至 8 层、C:/Users 至 5 层、Program Files/ProgramData 至 4 层）；④ 无 8188 端口监听、无相关进程。`[实测]`
- **stable-diffusion 系：未发现。** `*stable-diffusion* / *sd-webui* / *automatic1111* / *invokeai* / *fooocus*` 全盘零命中；无 `*.safetensors/*.ckpt` 模型文件；Python 环境无 torch/diffusers（仅 Pillow/imageio/scikit-image）；HuggingFace 缓存只有 OCR/whisper 模型。`[实测]`

### 4.2 其它图像 API key 配置 —— 结论：未发现（负结果，已查处如下）

- 环境变量（进程 + 注册表）：除 `BUDDYFARM_API_KEY` 外，`OPENAI/STABILITY/REPLICATE/FAL/TOGETHER/HF/DASHSCOPE/ARK/VOLC/SILICONFLOW/GEMINI/XAI…` 全部未设置。`[实测]`
- 本机各配置：`~/.omp/agent/.env` 仅 1 个 key（BUDDYFARM）；`D:/Project/*` 扫描命中的全是参考仓库的 `.env.example` 模板（无真 key）；WindsurfAPI 的 `.env` 仅面板密码。`[实测]`
- 提示：**`BUDDYFARM_API_KEY` 本身就是「图像通道的钥匙」**（grok-imagine 系由它解锁）——不算「缺 key」，算「已有但仅此一条」。`[归纳]`

### 4.3 omp 其它 provider / 其它 CLI

- omp 全量模型表（`_omp_models_full.txt`，250 行）核查：**图像生成模型只在 buddyfarm 出现**（grok-imagine ×5）；deepseek / google-antigravity / opencode-go / opencode-zen / rwkv-local 均无出图模型。`[实测]`
- `google-antigravity`（Gemini 系）等**未做出图探针**——属 Owner 账号资源，本轮只读盘点、不碰；如后续要用需 Owner 明确（见 §5）。`[归纳]`
- `~/.grok/bin/grok.exe` = 「Grok Build TUI」文本 agent，帮助无图像相关选项；`D:/opt/grok/farm` = 账号池基建（grok2api 上游）。均未动用。`[实测]`

### 4.4 端口与服务

- 监听端口排查：无 8188/7860（ComfyUI/SD 常用）；未见本地出图服务。网关侧 `192.168.11.4:3000`（LAN）与 `api.skiapi.dev`（公网）即本卡所有通道的宿主。`[实测]`

## 5. 需要 Owner 提供什么（清单）

> 现状：**最低需求=0**——E 系列用直连 API（§6）即可开工。以下均为「可选增强」，按需勾选：

1. **（可选）第三方图像 API key**：若要更强/更风格化的模型（SD/Flux 类、商用 API），需要 Owner 提供 1 个 key（Stability / Replicate / fal / OpenAI Images / 即梦等任一）。本机目前**没有任何**此类 key。`[实测支撑]`
2. **（可选）本地线拍板**：若要本地出图（离线、免配额），需 Owner 批准重装 ComfyUI 或 SD 系 + 下载模型（GB 级；本机 9/30 曾装 ComfyUI 跑视频，证明 GPU 可用，但已删）。`[实测支撑]`
3. **（可选）用量口径**：E 系列批量出图会消耗 BuddyFarm 池额度（grok 号池），如需大批量（几十~几百张），请确认走 `BUDDYFARM_API_KEY` 共享池是否 OK、有无张数上限。
4. **（可选）视频增强**：grok-imagine-video 现已可用（1s/720p 实测）；更长/更高清依赖账号 tier（SKIAPI 文档口径：视频需 SuperGrok 档）——如需要，属 GrokFarm 补号立项。
5. **（可选）Gemini 系出图评估**：omp 的 `google-antigravity` 通道（Gemini 系）是否具备出图能力未测（属 Owner 账号资源）；如想启用，需要 Owner 一句话授权再评估。

## 6. 给 E 系列的用法建议（可直接抄）

**推荐配方：`/v1/images/generations` + `grok-imagine-image-2.0`（质量）/ `-lite`（最快，~2s）。**

```bash
# 1) 取 key（本机已配置，读取即可；不要打印到日志/产物）
BFKEY=$(grep -o 'BUDDYFARM_API_KEY=.*' "C:/Users/dwgx1/.omp/agent/.env" | cut -d= -f2- | tr -d '\r\n')

# 2) 出图（LAN；公网把域名换成 https://api.skiapi.dev 亦可）
curl -sS "http://192.168.11.4:3000/v1/images/generations" \
  -H "Authorization: Bearer $BFKEY" -H "Content-Type: application/json" \
  -d '{"model":"grok-imagine-image-2.0","prompt":"a lighthouse on a rocky coast in a storm, oil painting style","n":1}'
# → {"created":...,"data":[{"mime_type":"image/jpeg","url":"https://api.skiapi.dev/v1/media/images/img_..."}]}

# 3) 立即下载落盘（URL 有效期未核，建议生成后马上存）
curl -sS -o out.jpg "https://api.skiapi.dev/v1/media/images/img_..."
```

**注意事项（全部实测得出）：**

1. **不要经 omp CLI 出图**（§2.3 陷阱：tools 被拒 + 静默回退成代码绘图）；直连 API 是唯一可靠路径。
2. **模型选择**：`-2.0`（66K 上下文、质量档）· `-lite`（最快）· `image`（基础）。**prompt 用英文**更稳（实测英文全通）。
3. **输出是 JPEG**（非 PNG，无透明通道）；如需 PNG/特定尺寸，后处理转换（本机有 Pillow）。`size` 参数可传但**未严格兑现**（D8 实测）。
4. **偶发错误**：`403 content policy`（上游概率性风控，重试即可）· `503 no healthy account`（池冷却，稍后重试）——均非确定性失败。`[实测+自述]`
5. **编辑/风格迁移**：走 `/v1/images/edits`，`image.url` 必须是**已托管的图 URL**（先用生成接口拿 URL；不支持 base64）。
6. **批量建议**：脚本里加 2~3 次重试 + 间隔；生成后统一命名落盘到实验目录（保持 E 系列可追溯）。

## 7. 证据清单、复现与自查

### 7.1 文件树（`research/agent-art/cards/_image_probes/`，关键文件）

```
_image_probes/
├─ _raw_outputs_all.txt          ← 全量原始输出汇总（本卡 §2/§3 引用的原文都在）
├─ _sha256_manifest.txt          ← 关键产物哈希
├─ _gateway_models.json          ← 网关模型表（33 个）
├─ _omp_models_full.txt          ← omp 全量模型表（250 行）
├─ d1_grok_imagine_image.jpg     ← 直连 chat 产物（83715B 768×1152）
├─ d2_grok_imagine_image_2.0.jpg ← -2.0 产物（55234B）
├─ d3_grok_imagine_image_lite.jpg← -lite 产物（616431B）
├─ d4_edit_result.jpg            ← edits 产物（红→蓝，167395B）
├─ d5_lighthouse.jpg             ← 灯塔油画（352379B）★ E 系列样例
├─ d8_lighthouse_1536x1024.jpg   ← size 参数实测（实回 1152×768）
├─ d6_video_test.mp4             ← 视频产物（249103B，h264 720p 1.04s）
├─ p1_grok-imagine-image/        ← P1/P1a/P1b：stdout/stderr/meta + red_circle.png(12399B)
├─ p2_grok-imagine-image-2.0/    ← P2 同上（3359B）
├─ p3_grok-imagine-image-edit/   ← P3 同上（3359B）
├─ p4_grok-imagine-image-lite/   ← P4 同上（3397B）
├─ _d1…_d8*.json                 ← 直连探针请求/响应原文
└─ _evidence/
   ├─ sessions/                  ← P1/P1b/P2/P3/P4 会话 JSONL（model_change/回退证据）
   ├─ http400/                   ← 5 个 400 原始请求记录（含 tools 数量与错误原文）
   └─ p1a_bare_id_omp_log.log    ← 裸模型名失败日志
```

### 7.2 复现命令（任选）

```bash
# 复现 omp CLI 现象（30~40s，会在 cwd 落一张「代码绘图」PNG）：
"C:/Users/dwgx1/AppData/Local/omp/omp.exe" -p --no-title --max-time 120s \
  --model buddyfarm/grok-imagine-image "Generate one image: a red circle on a white background. Save it to ./red_circle.png ..."

# 复现直连出图（6s 出 URL）：
curl -sS "http://192.168.11.4:3000/v1/images/generations" -H "Authorization: Bearer $BFKEY" \
  -H "Content-Type: application/json" -d '{"model":"grok-imagine-image","prompt":"a red circle on a white background","n":1}'

# 机械校验（全部产物可打开 + 规格）：
python -c "from PIL import Image; [print(f, Image.open(f).format, Image.open(f).size) for f in [...]]"
ffprobe -v error -show_format d6_video_test.mp4
```

### 7.3 自查记录（LOOP：A 早产出 / B 反驳 / C 机械验证 / D 小结）

- **B 反驳（对最强结论逐条试推翻，全部 CONFIRMED）：**
  1. 「omp CLI 不可用」→ 试 `--no-tools` 变体仍不可用（MCP 工具残留）；对照直连 API 可用 ⇒ **CONFIRMED**（本质是封装层问题）。
  2. 「直连 API 出的是真图」→ 反证检查：产物为画风图（笔触/氛围，非几何代码可轻易伪造）+ edit 操作有效（红→蓝）+ 与 SKIAPI 既有 11/11 矩阵一致 ⇒ **CONFIRMED**。
  3. 「本机无 ComfyUI/SD」→ 穷举：目录删除证据 + 全盘搜索 + 模型文件搜索 + 端口检查 ⇒ **CONFIRMED**（限定语：曾有、已删）。
  4. 「-edit 必须 hosted URL」→ multipart 415 / base64 400 / hosted URL 200 三连测 ⇒ **CONFIRMED**。
  5. 「视频可用」→ create→completed→content 全链 200 + ftyp/ffprobe 校验 + SKIAPI 文档互证 ⇒ **CONFIRMED**。
- **C 机械验证（检查器：Pillow + ffprobe + sha256，原样输出见 §7.1 两清单）：** 10 个图像文件全部 `Image.open` 通过（JPEG×6 / PNG×4）；`d6_video_test.mp4` = h264 1280×720 1.04s；sha256 全量在 `_sha256_manifest.txt`。
- **D ≤14 行小结：**
  - 已确立：直连网关 3 模型出图 + edit + video 全通（8 图 1 视频）；omp CLI 路径不可用且会把代码绘图伪装成结果（机制已解剖）；裸模型名会误命中 zenmux；本机无 SD/ComfyUI/其它 key。
  - 被推翻：无（初始假设「grok-imagine 不是生成模型」被推翻——它是真图像模型，只是 omp 封装层让它"看起来像"代码绘图）。
  - 未知：媒体 URL 有效期；size 参数精确行为；grok-imagine 系列能否出更高分辨率（2k）未测；antigravity 出图能力未测（需 Owner）。
  - 下一步：E 系列按 §6 recipe 开工；如需更强模型/本地线 → §5 清单找 Owner。

---

> 落款：ImageChannelProbe（wave6）· 2026-10-15 · 本卡所有结论均可在 `_image_probes/` 内复核；引用请带路径。
