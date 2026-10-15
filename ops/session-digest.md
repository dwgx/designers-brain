# SESSION-DIGEST — Designers_Brain

> 用途：会话蒸馏。读这一份 ≈ 替代考古；要深挖按 §6 跳会话文件。
> 覆盖：omp 顶层会话 12 个（含图像探针 5 个）+ 子代理文件 39 个（未逐读）；handoff 4 份；截至 2026-10-15。
> 维护：收工仪式追加 §2（`skill://shougong`「项目蒸馏」节）；历史行不改写，更正用〔更正〕块。

## 1 · 现在在哪（≤10 行）

- 项目：**艺术家视觉语言蒸馏系统**（Owner: dwgx1；不建 git；不训练模型）。入口 `AGENTS.md` → 队列 `GOALS.md`（唯一状态权威）/ 手册 `WORKFLOW.md` / 日志 `OPS-LOG.md`。
- 状态（2026-10-15 21:3x）：**Lane A/B/C/D/E 全收，S（skill 化）收尾**——GOALS 51 项 done，仅 **S-05 open**（真实需求走查：多轮 + 真出图 + gate 实跑 + description 自主触发实测）。
- 主产物：A=`research/artists/`（11 档案 + `_corpus/` 126 条 + `_images/` 33 张）；B=`research/agent-art/`（工作流/迁移指南/冲突清单）+ `research/experiments/anim_test_01..03`（三条端到端）；E=`research/experiments/E1_t1|E1_t1b|E1_t1c|E2_t1`（7/7 偏置解除 + 组合 9/9）；S=`research/skill/` + `skills/designers-brain/`（建包 + junction ×4 + 盲测 PASS）。
- 通道：omp/deepseek 默认（跨家 6 单全收口）；claude 停用（3600s 超时）、codex 401；图像 = 网关直连（裸模型名 `grok-imagine-image-2.0`；768×1152；无负向）。
- 下一步：S-05 → 人评六维（`research/experiments/design.md` §5）→ 其余 12 卡端到端 / E3 强度扫描 / E4 换主题 / E2 第二批。
- 纪律：一个路径一个写手；GOALS/机器板归主脑；证据分级 `[自述]/[史料]/[研究]/[归纳]/[推测]`；对外接口现状见 `OPS-LOG.md` §8。

## 2 · 大事记

| 日期 | 波/车道 | 发生了什么 | 结果/证据 |
|---|---|---|---|
| 2026-10-15 15:2x | 启动 | 主脑开题：四车道 + LOOP 协议 + 8 核心画家选型定稿；wave1 派发（8 档案 + 4 研究线 + 3 跨家） | `PROJECT.md` / `WORKFLOW.md`；会话 `06-29-46` |
| 2026-10-15 下午 | A·wave1–2 | 11 份画家档案（252–382 行/份）+ `expansion.md`（18 缺口）+ 独立复核 31/31 CONFIRMED（4 处修正双闭环） | `research/artists/*.md`、`_review.md`；GOALS A-01..A-17 |
| 2026-10-15 下午 | B·wave1–5 | 15 卡结构蒸馏；**15/15 同源确认**（= `Vincentwei1021/mg-styles-15`，MIT）；HTML/Blender 工作流 + vsc 深拆（645 行）+ 迁移指南 v1.0（457 行）+ 冲突清单 18 条 / N1–N9 | `research/agent-art/**`；GOALS B-01..B-16 |
| 2026-10-15 16:06–16:31 | C·跨家 | DB-C1（codex 401 断供）→ DB-C1b ok（GitHub 69 候选 + Top10）；DB-C3 ok（opus55 16 实例）；DB-C2（claude 3600s 超时零产出）→ 拆两工 | `~/.dwgx/ops/board.md` DB-* 行；receipts（db-c1/db-c3） |
| 2026-10-15 17:22–17:52 | **A·语料线** | DB-C2b/C2c 完成 8 文件 **126 条**带来源原话（达芬奇16 / 米开朗基罗15 / 梵高20 / 莫奈17 + 毕加索16 / 塞尚17 / 马蒂斯13 / 北斋12）；C2b 崩溃后 **resume 补 3 份**；`INDEX.md` 建 | `research/artists/_corpus/`；board VERIFY（michelangelo / cezanne） |
| 2026-10-15 傍晚 | D·素材 | 33 张 PD 图 + manifest（Met15 / AIC4 / Cleveland3 / Commons11）；参考帧 15/15 映射 + 30 补帧；源视频回捞（Bilibili + YouTube） | `_images/manifest.md`；`source_video/refs/README.md` |
| 2026-10-15 晚 | B·端到端 ×3 | anim_test_01（像素卡，抓出 fillStyle 跨帧泄漏）→ anim_test_02（一笔画，连通 15/15）→ anim_test_03_blender（3D 质感 300 帧，9 机制，EEVEE P1）；**三条管线全部闭环** | 各目录 `out.mp4` / `checks.md`；GOALS B-07/B-17/B-19 |
| 2026-10-15 晚 | B-20 / E 线 | 图像通道解锁（网关直连）；E-01 36/36 → E-02 偏置 7 格拆 §8.1b 重跑 21/21 → E-03 解除 3/3（**7/7 全解除**）→ E-04 组合 9/9（N1/N4/N9 判定） | `image_channel.md`；`E1_t1`..`E1_t1c` / `E2_t1` + `RESULTS*` |
| 2026-10-15 晚 | 归档 / 清扫 | `owners research prompt/` → `research/origin_cards/`（24 处引用更新；原件只归档）；A-18 标注清扫 7/7；A-19 模块库 11 卡（校验 33/33） | GOALS A-18/A-19；OPS-LOG §11 |
| 2026-10-15 20:45–21:07 | S·wave9 | SkillEcosystem（superpowers + 8 参照 + 交互协议 v0）→ SkillSpec v0.2（556 行 + 草案 106 行 + 自检 36/36） | `research/skill/skill_ecosystem.md`、`skill_spec.md` |
| 2026-10-15 21:08–21:18 | S·wave10 | SkillBuild 建包：`skills/designers-brain/`（SKILL.md + references×9 + domains.yaml + 打包件×3 + junction ×4 全解析）；自查 PASS（checked=54） | `build_receipt.md`；GOALS S-03（done） |
| 2026-10-15 21:18–21:32 | S·盲测 | RED-GREEN 对照（「拾光」咖啡馆同一需求）：**行为增量成立**（3 修正 + 6 新增层）；候选数口径写回 spec | `research/skill/tests/{red,green}_transcript.md` + `test_report.md`；GOALS S-04（done） |
| 2026-10-15 晚 | 审计修复 | 外部审计（B09 等）F4/F6 落地：项目板 + registry 键 + AGENTS 入口；AUD15-DB-WF 并发口径修正 | board：I2-NEW-BOARDS-3 / AGENTS-DESIGNERSBRAIN / AUD15-DB-WF（均 ok） |
| 2026-10-15 晚 | 蒸馏 | 本 `SESSION-DIGEST.md` 生成；`shougong`（收工追加 §2）+ `考古.md`（先读 digest）保鲜链接线 | 本文件；board DIGEST-DBRAIN |

## 3 · 关键决策与教训

1. **四车道 + LOOP 协议**：A 画家 / B 代码艺术 / C 跨家派发 / D 联网；每轮 = GOALS 取目标 → 深研究 → 落盘（证据分级）→ 自审四段 → 主脑验收 → 新线入队。来源：`WORKFLOW.md`；`PROJECT.md` 决策日志。
2. **蒸馏口径 + 证据分级**：「创作原则」= 从作品/书信/史料归纳的操作规则，不冒充艺术家内心；`[自述]` 必须带出处；查不到写「未找到（已查:…）」；数字带分母与日期。来源：`AGENTS.md`；`research/artists/_crosscheck.md`（392 条对账）。
3. **确定性契约（determinism contract）**：`templates/determinism_contract.md` v0.1（C1–C10，可整段粘进提示词）；三线标定——网页线目标 **P0**（字节级，乱序重渲 3/3 SHA 一致）；Blender·EEVEE 实测 **P1**（视觉级，≤0.05% 像素差，同进程重渲仍不同）。**P0 自查必须含乱序重渲**（fillStyle 跨帧泄漏只有乱序才暴露）。来源：契约 §3 ①b；OPS-LOG §7；`anim_test_03_blender/checks.md`。
4. **风格段与题材段必须分离**：人物向模块 §8.1 含题材词 → 输出把场景替换成人物/室内；拆 §8.1b 纯风格段 + 从句级改写后 **7/7 解除或基本解除**。来源：E-02/E-03；GOALS。
5. **「管线可迁移，风格机制必须重写 + 配套机械检查」**（B-17 结论：跨风格复用管线骨架零改动；新问题全在风格机制）。来源：GOALS B-17。
6. **图像通道 = 网关直连 API**：裸模型名 `grok-imagine-image-2.0`（带 `buddyfarm/` 前缀反而 404）；**无负向通道**；尺寸固定回 768×1152；omp CLI 路径不可用。来源：OPS-LOG §9；`research/agent-art/cards/image_channel.md`。
7. **长任务死亡两处置**：claude 超时零产出 → 换通道拆小；omp 崩溃（exit=-1）→ 先查已落产物，能 **resume** 就 resume（DB-C2b 一次成功）。来源：OPS-LOG §2.7 / §6。
8. **跨家五步 + 一树一写手 + 越权教训**：board open 占写路径 → briefcheck → 派 → 核产物 → close --verify；工人不得写 GOALS / 机器板（2 次越权记录在案，后续 brief 补禁令句）。来源：`WORKFLOW.md` §4；OPS-LOG §10。
9. **15 卡 = mg-styles-15 同源（MIT）**，以该仓为参考实现；vsc（11,988★，Apache-2.0）为第二路线（Remotion + 真实截图）。来源：B-10/B-14；`cards/mg-styles-15_compare.md`。
10. **skill 化**：参照 superpowers 范式；命名裁定 `designers-brain`；SKILL.md <500 行 + references 指针（渐进披露）；激活 = junction ×4（零拷贝、逐条先核后建）；RED-GREEN 盲测为验收法。来源：S-01..S-04；`skill_spec.md`、`build_receipt.md`、`test_report.md`。
11. **「搜索失败 ≠ 内容缺口」**：web_search 全 provider 限流时用 read / curl / urllib / eval browser / GitHub API（全部实测可用），交付未受影响。来源：OPS-LOG §2.6 / §8。

## 4 · 死胡同 / 别重做

1. **claude 跨家后端**：首用即挂（3600s 超时、零产出、无 session id）→ 已停用；要用先小任务探针。来源：OPS-LOG §2.2；board DB-C2 failed。
2. **codex 后端**：401 断供（缺鉴权）→ 未再派（修复前别派）。来源：board DB-C1 failed（Missing bearer）。
3. **omp CLI 图像路径**：图像模型拒工具 → CLI 静默回退 deepseek 用 Pillow 画图 → 不可用；走网关直连。来源：OPS-LOG §9；探针会话 `09-29-02`。
4. **外部接口坑**：Met API v1 search 退役（410）→ 用 `/v1.1/search` 且直连须 curl；AIC IIIF 有 Cloudflare JS 挑战（用真 Chromium）；Commons 无毕加索干净复制品（用 Cleveland CC0）。来源：OPS-LOG §8。
5. **ffmpeg 本 build**：无 `-pattern_type glob`；非连续编号 `k%04d.png` 只读 1 帧（用 `-f concat`）；单帧落盘须 `-update 1`。来源：OPS-LOG §2.4；handoff。
6. **edit 工具长中文行**匹配失败 ×3（images_index / OPS-LOG）→ 改前先 read 精确原文或用短锚点；`OPS-LOG.md` 一律整份重写（write）不用 edit。来源：OPS-LOG §2.3 / §2.8。
7. **Blender 5.2 headless 两坑**：manual `frame_set` 不推进 Bullet（须 `point_cache` + `bake_all` 再读）；per-copy `rigidbody.object_add()` 或删 proto → 接触变软/蠕变（须 rb 加在 proto、副本继承、保 proto）。来源：`anim_test_03_blender/checks.md` §8。
8. **软体 PLAY 字模**两次尝试数值发散（heights ~1e14）→ 记录为诚实局限（用关键帧 squash&stretch 替代），别重做。来源：`anim_test_03_blender/checks.md` §4.7。
9. **裸 `bash` 解析到 WSL**（F: 盘未挂载会死）→ 一律 `"C:/Program Files/Git/bin/bash.exe"` 跑 .sh。来源：anim_test_03 handoff；`硬地板.md`。
10. **omp 瞬态 `Model "…" not found`**：先 `omp -p` 探针再重派，别换通道。来源：OPS-LOG §6。

## 5 · 未收口

1. **S-05**（唯一 open）：真实需求走查——多轮对话 + 真出图 + gate 文件实跑 + description 自主触发实测；产物路径「待定」。指向：`GOALS.md` L82。
2. 人评六维打分：E1/E1b/E1c/E2 均未打分（需人/视觉模型）。指向：`research/experiments/design.md` §5。
3. 端到端仅 3/15 卡（01/08/11）；其余 12 卡待做。指向：GOALS B-07/B-17/B-19。
4. E3 强度扫描 / E4 换主题迁移 / E2 第二批（透纳+莫奈、克里姆特+马蒂斯——先写分工说明）。指向：GOALS E 系列 + `design.md`。
5. 「还需要研究什么」清单（主会话 todo 项）未交 Owner。
6. 跨家通道修复项：codex 鉴权、claude 质量未知（未再使用）。指向：OPS-LOG §1。
7. 外部依赖：web_search 限流（替代路径可用）；B-16 建议的模板 v0.3 后续项（判例章回填）。指向：OPS-LOG §1 / GOALS B-16。
8. 注记：`design.md` §3「生成模型+版本：待定」实际已被 B-20 解决（grok-imagine 网关直连）——建议主脑更新〔未核：design.md 是否已改〕。

## 6 · 会话索引

> 路径前缀：`C:/Users/dwgx1/.omp/agent/sessions/--D--Project-Designers_Brain--/`（图像探针在 `...-_image_probes-p1..p4_grok-imagine-image*--` 子 slug；handoff 4 份在主会话目录内；`--D--Project-Designers Brain--` 为空目录）。子代理文件未逐读，按名检索（`Artist*` / `E*` / `Anim*` / `Skill*` / `Blind*` / `Dossier*` 等）。

| 文件 | 日期 | MB | 一句话 |
|---|---|---|---|
| `06-29-46_01a13e40`（主会话） | 10-15 | 4.3 | 主脑全程：wave1–10 派发 / 验收 / 记录（含 39 子代理文件、4 handoff） |
| `07-09-20_01a13e64` | 10-15 | 0.63 | DB-C3：opus55 证据链（evidence / gallery / gaps） |
| `07-10-50_01a13e66` | 10-15 | 0.46 | DB-C1b：GitHub 猎场（repos.md 69 行 + Top10 评估） |
| `08-24-22_01a13ea9`（902c） | 10-15 | 0.002 | 跨家探针 OK-PROBE |
| `08-24-40-626_01a13ea9`（d7b2） | 10-15 | 1.20 | DB-C2c：语料 B 半（毕加索 / 塞尚 / 马蒂斯 / 北斋，58 条） |
| `08-24-40-627_01a13ea9`（d7b3） | 10-15 | 1.63 | DB-C2b：语料 A 半（达芬奇 / 米开朗基罗 / 梵高 / 莫奈，68 条；含崩溃 resume） |
| `09-29-02_01a13ee4` | 10-15 | 0.010 | omp CLI 图像探针（失败留档：回退 Pillow） |
| `p1 09-34-04_01a13ee9` | 10-15 | 0.04 | 图像探针 p1（grok-imagine-image） |
| `p1 09-38-38_01a13eed` | 10-15 | 0.30 | 图像探针 p1b（URL 回传路径） |
| `p2 09-37-04_01a13eec` | 10-15 | 0.013 | 图像探针 p2（grok-imagine-image-2.0） |
| `p3 09-37-17_01a13eec` | 10-15 | 0.016 | 图像探针 p3（edit） |
| `p4 09-37-40_01a13eec` | 10-15 | 0.032 | 图像探针 p4（lite） |
| 子代理 ×39（主会话目录） | 10-15 | 51.5 | wave1–10 具名工人（归属见 §2；未逐读） |
