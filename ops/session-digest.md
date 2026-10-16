# SESSION-DIGEST — Designers_Brain

> 用途：会话蒸馏。读这一份 ≈ 替代考古；要深挖按 §6 跳会话文件。
> 覆盖：S-main（06-29-46；终态 145 jsonl + 157 md + 2,114 log + 12 handoff）+ 图像探针 p1–p4 + 本波（22-41-02）；截至 2026-10-16（死亡点 06:28 + 本波增补）。
> 维护：收工仪式追加 §2（`skill://shougong`「项目蒸馏」节）；历史行不改写，更正用〔更正〕块。

## 1 · 现在在哪（≤10 行）

- 项目：**艺术家视觉语言蒸馏系统**（Owner: dwgx1；已建 git + public 仓 `github.com/dwgx/designers-brain`；不训练模型）。入口 `AGENTS.md` → 队列 `GOALS.md`（唯一状态权威）/ 手册 `WORKFLOW.md` / 日志 `OPS-LOG.md`。
- 状态（2026-10-16 上午）：**画家 program 62 位全收口**（wave1–21；档案 62 / 语料 1613 条 / 图库公开 618 + 私有例外 676）；模块卡 **62 张**（checks 186/186）；三索引三轮合并（PASS 257/0）；skill 走查收口（S-05 done）。GOALS：145 done / 0 running / 2 open（A-30、S-06；A-107 本波收口）。
- 主产物：A=`knowledge/domains/painters/`（dossiers 62 + `_corpus/` + `_images/` + `modules/` 62 卡）；B=`knowledge/agent-art/` + `experiments/anim_test_01..03`；E=`experiments/E1_t1..E2_t1`；S=`skills/designers-brain/`（junction ×4）；R=public 仓发布。
- 通道：omp/deepseek 默认（全部 in-session 子代理）；claude 停用、codex 401；图像 = 网关直连（`grok-imagine-image-2.0`；768×1152；无负向）。
- 2026-10-16 06:28：S-main 被 SIGHUP 杀死（死亡点遗留：2 commits 未推 + 10 文件未提交 + A-107 未收口）→ **本考古运维波接手**：会话归档 → `F:/backup_famlti_family/sessions/Designers_Brain/`；蒸馏补齐（本文件）；垃圾隔离；仓库收口；记录见 `ops/archaeology-2026-10-16/`。
- 下一步：A-30 学习路径卡 / S-06 spec v0.3 / wave21 主表并入（下轮索引）/ 模块卡 62→72 / E3/E4 与人评六维（详见 §5 更新块）。
- 纪律：一个路径一个写手；GOALS/OPS-LOG/机器板归主脑；证据分级 `[自述]/[史料]/[研究]/[归纳]/[推测]`；对外接口现状见 `OPS-LOG.md` §8。

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
| 2026-10-15 21:3x–22:0x | S·wave11 | S-05 走查（演练版）全链真跑：首问包 → 推荐单 → 3 张真图候选 + 展示后停 → 定稿（维米尔×莫奈）+ gate 文件 + 独立评审；自主触发探针（新鲜 omp 进程 catalog 已含 designers-brain） | `docs/skill/walkthrough_01/`（24 文件；机械 64/64；评审 7 维 7/6/7/7/7）+ `docs/skill/tests/autotrigger_probe.md`；S-main/ConsultWalkthrough.md；GOALS S-05 |
| 2026-10-15 22:1x–22:3x | 仓库 | git 落地（Owner 令）+ 目录重构（research/ → knowledge/experiments/docs/ops）+ 全英文化 + i18n zh/ja（独立审计后修正） | commits `f40a633`→`2aad143`→`534924e`→`15ea5ff`；`docs/MIGRATION.md`；OPS-LOG §14 |
| 2026-10-15 22:5x | 发布 | GitHub 公开发布：public 仓、CC BY 4.0（内容）+ MIT（代码）、secret scan 零命中、license 检测通过、topics×7 | `https://github.com/dwgx/designers-brain`；commit `13849cc`；OPS-LOG §15 |
| 2026-10-15 深夜 | A·wave12 | 第二批画家 3/3：turner 345 行 / rembrandt 413 行 / klimt 379 行（v2 规格 + 语料 + 图库；分工写死） | `knowledge/domains/painters/dossiers/{turner,rembrandt,klimt}.md`；GOALS A-20..A-22；commit `297a3d1` |
| 2026-10-15 深夜 | A·wave13 | 6/6：goya/seurat/hopper/bada_shanren/qi_baishi/ito_jakuchu（v2 全规格；hopper 图全私有）+ RosterBuilder 名册 59 候选（349 行 / 15 文化区 / 批次建议 8/7/7） | dossiers/*.md + `program/roster.md`；GOALS A-23..A-29 |
| 2026-10-15 深夜 | 私有层政策 | Owner 令「就算侵权也没事——做不公开的东西」→ 仓内 `_private/`（`.gitignore` + `.git/info/exclude` 双保险、永不提交）；版权未清图只进私有；qi 4 件 URAA 从严移入；公开侧只列作品清单 | `_private/` + `_private/INVENTORY_*.md`；OPS-LOG §16；S-main/ArtistKngwarreye.md（同法） |
| 2026-10-15 深夜 | 崩溃与 resume | provider 批量流中断 ×2（4 工 / 10 工同批失败，多在 11–15 分钟处）→ 全数 resume 同会话 + 「每 10–15 分钟写盘」纪律；Owner 令③「保持原样重跑、不降规格」→ 补开 wave15 保并发（在飞 21 工） | OPS-LOG §16；S-main/handoff-2026-10-15T15-19-39-781Z.md |
| 2026-10-16 00:0x | A·wave14 加固 pass1 | 原 11 位各补 §11（2080–2816 字 + 年表 + 来源）+ §12；3 条旧说 OVERTURNED（塞尚「绝交信」/米氏「1509 揭幕」/齐白石「画吾自画」归属） | GOALS A-31..A-41；commit `8f3d7f4`；OPS-LOG §16 |
| 2026-10-16 00:3x | A·wave15 | 8/8 收口：mucha/munch/kandinsky/velazquez/bosch/huang_gongwang/kahlo/behzad（kahlo 13 图全私有） | commits `54f4173`/`ce39724`；GOALS A-42..A-49 |
| 2026-10-16 00:3x | 收口·卡 20 | 模块卡 11→20：9 新卡 + README + domains.yaml（checks=60；旧 11 卡零改动；幂等） | commit `5c52d97`；S-main/ModuleCards20.md；GOALS A-50 |
| 2026-10-16 00:4x | 收口·索引一轮 | 三表并入 20 位：INDEX 20 行/455 条 · manifest 公开 104 + 私有例外 32 · _index 20 行（PASS 75/0；重复 0） | `knowledge/domains/painters/_scratch/index_merge/RECEIPT.md`；commit `d7bb6fe`；GOALS A-51 |
| 2026-10-16 00:4x–01:1x | A·wave16p2 加固 pass2 | 9/9：turner/rembrandt/klimt/goya/seurat/hopper/bada/qi/ito 补 §11.1（2208–3017 字）+ 子节归一（B.x→11.x）；纯插入（turner +134/0、rembrandt +180/0 等） | GOALS A-59..A-67；commit `f953073`；S-main/Hard{Turner,Rembrandt,Klimt,Goya,Seurat,Hopper,Bada,Qi,Ito}.md |
| 2026-10-16 00:5x | A·wave17 | 7/7：friedrich/repin/ravi_varma/degas/gauguin/van_eyck/kngwarreye（kngwarreye 14 图全私有 + 原住民伦理护栏） | commit `1df839c`；GOALS A-52..A-58 |
| 2026-10-16 01:2x | 收口·索引二轮 | 三表并入 35 位：844 条 · 公开 273 + 私有 126 · _index 35 行（PASS 140/0；口径决定：mucha 12/5、kandinsky `.hires`=11） | commit `8d070d0`；S-main/IndexMerge2.md；GOALS A-75 |
| 2026-10-16 01:2x–01:5x | A·wave18 | 7/7：hiroshige/sargent/piero_della_francesca/artemisia_gentileschi/namatjira/el_salahi/wu_guanzhong（后 3 位全私有） | commit `8daf1f5`；GOALS A-68..A-74 |
| 2026-10-16 01:5x–02:0x | 收口·卡 42 | 模块卡 20→42（wave15×8 + wave17×7 + wave18×7 入 ARTISTS；checks=126；旧 20 卡零改动；幂等） | commit `d4272ef`（随 `9b49748` 推）；S-main/ModuleCards42.md；GOALS A-76 |
| 2026-10-16 02:0x | 重启（被杀） | 宿主重启杀死 wave19×10（零 dossier，scratch 残留 3–68 件/工可复用）；ModuleCards42 收尾完成并随 sweep 推 | OPS-LOG「重启前收拾/重启恢复」；commits `f890667`/`d4272ef`/`9b49748` |
| 2026-10-16 03:2x–03:5x | A·wave19 重派 | 十位重派（`-2` 后缀、链接原单、先核 scratch 复用）→ 10/10 收口（okeeffe/rivera 全私有） | commits `d4c8043`/`4356762`；GOALS A-77..A-86 |
| 2026-10-16 03:5x | 分叉处置 | 远端分叉（`4af3f70`）→ sweep + merge `cab2234`（5 文件取本地较新态）→ 广播「勿自行 push；commit 自己写路径可以」 | commits `cab2234`/`ca5fb15`；OPS-LOG「推送分叉处置」 |
| 2026-10-16 03:2x–05:5x | A·wave20 | 10/10：zhao_mengfu/ni_zan/qiu_ying/ogata_korin/blake/chardin/manet/sorolla/zorn/sultan_mohammed | commits `13ddfe4`/`f5ec090`/`3234f9c` 等；GOALS A-87..A-96 |
| 2026-10-16 04:5x–05:5x | A·wave21 | 10/10：xu_beihong/li_keran/sher_gil/tarsila/chen_hongshou/xu_wei/hogarth/mir_sayyid_ali/de_chirico/rockwell（5 位全私有；sher_gil 版权核正：印度 life+60→PD 2002） | commits `02adc1c`/`ad961d3`；GOALS A-97..A-106 |
| 2026-10-16 06:0x–06:2x | 收口三工 | ModuleCards62：42→62（checks 186；旧 42 卡 raw sha256 全等）· CrossLinkSync：互引 10 处（9 文件 +31/−15；回归 186/186）· IndexMerge3：35→62（PASS 257/0；公开 618 / 私有 54 位 676 张） | commits `457aacb`/`cea77cb`；S-main/ModuleCards62.md、S-main/CrossLinkSync.md、`_scratch/index_merge3/RECEIPT.md` |
| 2026-10-16 06:28 | 死亡点 | SIGHUP 杀死 S-main（主脑正 `wait` IndexMerge3）；未收口：A-107 未置 done、工作树 9 文件 + GOALS.md 未提交、2 commits 未推 | S-main jsonl 末条 `session_exit`（reason=sighup，21:28:31Z）；`git status`（ahead 2） |
| 2026-10-16 07:4x–11:3x | 站稳运维波（收口） | 全链收口：考古蒸馏（digest 91→182）→ F: 归档（raw-20261016 终态 2,622 件 / 385,738,161 B；V1 5/5）→ 隔离 644+236 件（只移不删）→ 仓库 9 笔推送 `ad961d3..0763abe`（三检查全过；V3 10/10）→ 终态对账 PASS(±live,+moved)；压缩 #1 收工仪式（板重写 + 影子覆盘） | `ops/archaeology-2026-10-16/`（FINAL-REPORT + reports 01–13 + V1–V3）；F: `receipts/Designers_Brain-standfirm-20261016.md` §A–§D；板 `~/.dwgx/ops/boards/Designers_Brain.md` |
| 2026-10-16 15:2x–15:4x | 运维尾波 | .omp 自清（DBrain 桶）114 件 → `quarantine/Designers_Brain/session-tree-2-20261016/` · 跨会话互研回帖 ×4（FLEET-LOUNGE / IRC.md / LOBBY / FLEET-CHAT）· .dwgx 历史清理（AgentRule `.before-*` 93 + 本板 1 → 备份 tar 后删） | 收据 `receipts/Designers_Brain-sessionclean2-20261016.md` + `receipts/_dwgx-history-clean-20261016.md`；F: `quarantine/_agentrule-board-history-20261016/` |

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
12. **规格 v2（画家档案）+ 两轮加固结构**：§11「生平与年代轴（详细）」= 11.1 叙述 ≥2000 CJK 字 + 11.2 年表 ≥15 行 + 11.3 来源 ≥10 条；§12 临摹/学习清单 5–10 件；语料 ≥15 条；图库 ≥6 张；§11/§12 插在「自审四段」之前、既有节零改动（保 `_extract.py` §4/§8.1/§8.2 抽取契约）。理由：Owner「生平要详细」「全面挖完」+ 全部可机械验收（每工自测 + 主脑复核）。来源：`knowledge/domains/painters/program/README.md` §1；GOALS A-31..A-106；S-main/handoff-2026-10-15T15-19-39-781Z.md。
13. **波次编号顺延规则**：加固 = wave14；新画家批自 wave15 起；roster 的「wave14–16」为建议序、执行时 +1；收口波 = wave16 系（16 / 16p2）。理由：多批并行防编号撞车与误收口；已写入 program README §2。来源：`program/README.md` §2；OPS-LOG §16。
14. **私有层政策（含版权保守与逐国核正）**：仓内 `_private/`（双保险 ignore、永不提交、不进发布）；版权未清/未过保护期图只进私有（hopper/kahlo/kngwarreye/namatjira/el_salahi/wu_guanzhong/okeeffe/rivera/xu_beihong/li_keran/tarsila/de_chirico/rockwell 全私有；qi 4 件 URAA 从严；sher_gil 逐张理据 + 印度 PD 2002 核正）；公开侧只列作品清单 + 馆藏链接，并逐工验证「公开侧零版权图」。理由：Owner 授权「做不公开的东西」+ 公开仓风险隔离。来源：OPS-LOG §16；`_private/README.md`；各 `_private/INVENTORY_*.md`；S-main/ArtistOkeeffe-2.md、ArtistXuBeihong.md。
15. **provider 流中断处置规程**：探针（`omp -p`）→ resume 同会话（零产出从头、半产出核完整性补齐）→ brief 强制「每 10–15 分钟写盘」→ **不降规格、不减并发**（补开新批次补位）；「以轮次换完整率」。理由：两次批量中断（4 工/10 工）实测有效；Owner 令③。来源：OPS-LOG §16；S-main/handoff-2026-10-15T15-19-39-781Z.md。
16. **被杀/重启恢复规程**：读板 + GOALS → `ls _scratch/` 核各工残留 → 重派「先核 scratch 复用」；重派单 `-2` 后缀并链接原单；残余小活（如 ModuleCards42 收尾）用 1 个 coder 收。理由：wave19×10 被宿主重启杀死（零产出，但 scratch 3–68 件/工可复用）；复用省重做。来源：OPS-LOG「重启前收拾/重启恢复」；GOALS A-77..A-86（`-2` 命名先例）。
17. **推送纪律（分叉后收紧）**：worker 不得自行 `git push`（可 commit 自己写路径）；主脑统一 sweep + push 前三检查；分叉处置 = sweep → merge（冲突取本地较新态）→ 推 → 全员广播。理由：远端分叉事故（worker scoped commit 与主脑 sweep 交错）。来源：OPS-LOG「推送分叉处置」；S-main/ArtistNiZan.md（「do NOT git push」）；commit `cab2234`。
18. **共享文件合并归主脑/专职工**：`_corpus/INDEX.md`、`_images/manifest.md`、`_index.md`、`domains.yaml`、`modules/_extract.py` ARTISTS、GOALS/OPS-LOG 等由主脑或专职工合并；工人只写四处落盘（dossier/corpus/images/private）或只留片段。理由：一图一写手；并发写共享文件必坏。来源：S-main/handoff-2026-10-15T15-19-39-781Z.md（决策行）；`docs/PROTOCOLS.md`。
19. **索引收口口径 = 按批 + 以磁盘为准**：每轮固定「本批 N 位」，未收批注明「未纳入（在产）」；与简报数字冲突时以磁盘实数为准并留「口径决定」档（mucha 12/5、kandinsky `.hires`=11、mir 8、QA 排除、wave21 私有并入 54 行）。理由：三轮合并先例；可复核、可一键回退（`reconcile.md`）。来源：`_scratch/index_merge{2,3}/reconcile.md`；S-main/IndexMerge2.md、handoff-2026-10-15T21-22-37-592Z.md。
20. **模块卡纪律 = 机械抽取**：`_extract.py --write` 生成（禁手写）；扩表以 ARTISTS 为单一入口；验收 = `--check` 全绿（终态 186/186）+ 旧卡零改动（raw sha256）+ `--write` 幂等（多跑逐字节）。理由：卡与档案逐字一致（§8.1/§8.2/§4 逐字比对）；审计可复跑。来源：S-main/ModuleCards20.md、ModuleCards42.md、ModuleCards62.md；GOALS A-50/A-76/A-108。
21. **分工条款写死 + 交叉互引**：每档案 §3.1 写死与对侧画家的分工判据；对侧逐轴/逐条对齐；跨批用专职工做互引小修（A-109 共 10 处）+ `conflicts.md` near-miss 追加（不重排）。理由：防两模块混同；组合实验需要可判读边界。来源：S-main/CrossLinkSync.md；GOALS A-109；`knowledge/cross/conflicts.md` §4。
22. **归属分级纪律**：只有直接签名/馆方归属可写「作者级」；无签名作品（如《哈姆扎纳马》）保持馆方/归属级、不升格；存疑款（Custodia「Ali」）判伪并留档。理由：学术诚实；防把归属说成事实。来源：S-main/ArtistMirSayyidAli.md（决策行）。
23. **原住民伦理护栏**：涉及原住民艺术家（kngwarreye/namatjira）时只采公开出版/馆方文本、不解读或转用神圣/限制性内容、引文注明转写/译者、§8.1 附文化护栏（ICIP 参考 + 使用禁区）。理由：Owner 授权 ≠ 无伦理边界；两工已按此执行。来源：S-main/ArtistKngwarreye.md；GOALS A-58/A-72。

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
11. **Wikimedia 直连 429**：`upload.wikimedia.org`/`thumb.wikimedia.org` 对本机限流（curl 与浏览器均 429）→ 用 `Special:FilePath/<file>?width=N`、`thumb.php`、标准尺寸缩略（仅 250/330/500/960/1280/1920）、Wayback `im_` 镜像；Commons API 直连易 429。来源：S-main/handoff-2026-10-15T19-24-48-017Z.md；S-main/ArtistMirSayyidAli.md。
12. **馆站 403/Cloudflare**：britishmuseum.org、asia.si.edu、NGA/AGSA/DAAO、LOC/Honolulu、NPM 实况页等直读被拒 → Wayback 快照 + 真 Chromium（browser fetch）+ 媒体子域直取；searcharchives.bl.uk JSON 可用、collections.louvre.fr 重试可用。来源：S-main/ArtistMirSayyidAli.md、ArtistKngwarreye.md、handoff-2026-10-15T20-34-49-588Z.md。
13. **NPM 图库接口**：`Image/GetImage` 需 session randomCode → 批量抓取 403；改用 `iiifod.npm.gov.tw` IIIF（curl 可用）或浏览器 fetch；月刊 PDF 走 `NewChineseArtDownload.ashx`。来源：S-main/handoff-2026-10-15T18-52-57-205Z.md（决策行）。
14. **「藤花亭画谱」不存在**：NDL サーチ / CiNii / Brave / Yahoo / Baidu / Sogou / ja.wiki / 若冲书志年表全查无（「藤花亭」为梁廷枏斋号，与本画家无关）→ 别重做该检索；改用『藤景和画記』『若冲画譜』等可核材料。来源：S-main/HardIto.md。
15. **画廊图误标与不可用件**：陈洪绶 Commons「selfportrait_1635.jpg」实为《乔松仙寿图》（已移除换 `tanmei_tu`）；`LuJunYi.gif`/`quyuan_alt.jpg` 不可用弃用；sargent 联系表抓出 2 误取件已替换。教训：画廊图逐张核名 + 目检。来源：S-main/handoff-2026-10-15T20-34-49-588Z.md；GOALS A-69/A-101。
16. **维基不作结论级来源**：kngwarreye「1993 入选威尼斯」WEAKENED 不采用（1997 三源一致）；mir「卒年 1572」OVERTURNED 不采用；ru-wiki「4 of 14 Khamsa」留待核。来源：S-main/ArtistKngwarreye.md、ArtistMirSayyidAli.md。
17. **宿主重启杀光在飞子代理**：wave19×10 在重启中被杀（零产出）；「后台继续、不受压缩影响」≠ 不受重启影响 → 重启前先 sweep 落盘 + 记在飞清单；重启后核 scratch 重派，别等原工人。来源：OPS-LOG「重启前收拾/重启恢复」。
18. **私有计数口径坑**：第一轮按扩展名计数漏计 kandinsky `.hires`（内容实为 JPEG）→ 改按内容识别；QA 产物（`_` 前缀 / `contact_sheet*` / `cs_*`）须排除（de_chirico 26→25、zhao 12→9）；`.raw` 按内容计入（ni_zan 19）。来源：`_scratch/index_merge2/reconcile.md`、`_scratch/index_merge3/reconcile.md`。
19. **GBK 终端乱码 ≠ 文件问题**：仓库终端 cp936 使部分 bash 输出 CJK 乱码，文件本身 UTF-8 正常 → 勿因乱码改编码/重写文件。来源：S-main/handoff-2026-10-15T20-34-49-588Z.md。

## 5 · 未收口

1. **S-05**（唯一 open）：真实需求走查——多轮对话 + 真出图 + gate 文件实跑 + description 自主触发实测；产物路径「待定」。指向：`GOALS.md` L82。
2. 人评六维打分：E1/E1b/E1c/E2 均未打分（需人/视觉模型）。指向：`research/experiments/design.md` §5。
3. 端到端仅 3/15 卡（01/08/11）；其余 12 卡待做。指向：GOALS B-07/B-17/B-19。
4. E3 强度扫描 / E4 换主题迁移 / E2 第二批（透纳+莫奈、克里姆特+马蒂斯——先写分工说明）。指向：GOALS E 系列 + `design.md`。
5. 「还需要研究什么」清单（主会话 todo 项）未交 Owner。
6. 跨家通道修复项：codex 鉴权、claude 质量未知（未再使用）。指向：OPS-LOG §1。
7. 外部依赖：web_search 限流（替代路径可用）；B-16 建议的模板 v0.3 后续项（判例章回填）。指向：OPS-LOG §1 / GOALS B-16。
8. 注记：`design.md` §3「生成模型+版本：待定」实际已被 B-20 解决（grok-imagine 网关直连）——建议主脑更新〔未核：design.md 是否已改〕。


### 2026-10-16 更新（站稳波）

### A. 旧 §5 逐项状态（1–8）

1. **S-05** → **已收口**（wave11；`docs/skill/walkthrough_01/`）。旧行以〔更正〕C2 处理。
2. 人评六维打分 → **仍未做**（2026-10-16 复核：无新证据；`experiments/design.md` §5 未动）。
3. 端到端 12 卡 → **仍 3/15**（wave12–21 无新增 anim test；资源全在画家 program）。
4. E3 强度扫描 / E4 换主题 / E2 第二批 → **仍未做**（E 系列止于 E-04）。
5. 「还需要研究什么」清单 → **仍未见交付**（未核到新证据）。
6. 跨家通道修复 → **仍 open**（codex 401、claude 未再用；本段全部 in-session 子代理）。
7. web_search 限流 + B-16 模板 v0.3 后续项 → **仍 open**（限流持续；替代路径继续可用）。
8. `design.md` §3「生成模型+版本：待定」→ **仍未更新**（2026-10-16 复查 L27 仍「待定」；实际已由 grok-imagine 网关直连解决——建议主脑更新）。

### B. 新增未收口（9–15）

9. **A-107 待收口**：IndexMerge3 已完工（verify 257/0、commit `cea77cb`），GOALS 未置 done（主脑死亡点遗留）。
10. **死亡点善后**：2 commits 未推（`457aacb`、`cea77cb`）；工作树 9 文件（CrossLinkSync 互引）+ `ops/GOALS.md` 未提交 → 需 sweep / 提交 / 推送。
11. **wave21 主表并入（下轮）**：语料 10 文件 / 321 条、公开 105 张、档案 10 行（私有 251 张已并入本轮私有例外节）。
12. **模块卡 wave21 十位待扩**（62→72；徐渭/陈洪绶等保留 `（future）` 标记）。
13. **私有层例外节口径复核**：54 行（62 位 + wave21 已收口并入）vs 若仅取 62 位范围则 44 行（IndexMerge3 留档、可一键回退）。
14. **A-30（学习路径卡）open；S-06（skill spec v0.3 补丁 4 条）open**。
15. **wave22 未开**（roster 顺延：林飞龙/恩沃恩乌等）；遗留小项：qiu_ying 私有 6 项待补、kngwarreye §10 待办（威尼斯公告年份等）、ni_zan 水竹居图已补（`ad886ea`）。

---

## 〔更正〕（2026-10-16 追加）

- C1 · 旧 §1「不建 git」已失效：Owner 后续令已建 git 并发布 public 仓（`github.com/dwgx/designers-brain`）；OPS-LOG §14/§15 为准。
- C2 · 旧 §1「GOALS 51 项 done，仅 S-05 open」已失效：S-05 已 done（wave11）；现行 = 148 行（A-107 已收口 `91194d2`；2 open：A-30、S-06）。
- C3 · 旧 §6「handoff 4 份 / 子代理文件 39 个（未逐读）」需扩：S-main 目录实有 12 份 handoff、145 个 jsonl（含 1 非子代理件）+ 157 md（侦察口径见 `ops/archaeology-2026-10-16/MAIN-BRAIN.md` §2）；12 份速览见 `reports/02-digest-waves12-21.md` 附 A。
- C4 · 旧「截至 2026-10-15」口径需扩：S-main 实际运行至 2026-10-16 06:28:31 JST（SIGHUP 死亡；jsonl 末条 `session_exit`）；本 digest 的 10-15 21:3x → 10-16 06:28 段见 02 号报告 §2 追加行。
- C5 · 路径口径变更：旧 `research/...` 路径 → 重构后为 `knowledge/`、`experiments/`、`docs/`、`ops/`（映射见 `docs/MIGRATION.md`）；§6 前缀说明需补一句。

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

### 2026-10-16 考古波（站稳运维）增补

> 本波由新会话 `2026-10-15T22-41-02-476Z_01a141b9-de0c` 执行；S-main 实际运行至 2026-10-16 06:28:31 JST（sighup）。波内报告：`ops/archaeology-2026-10-16/reports/`（01–10 号 + MAIN-BRAIN.md）。

| 文件 | 日期 | 说明 |
|---|---|---|
| S-main `06-29-46_01a13e40`（终态） | 10-15→10-16 | 主脑全程：wave1–21；终态 = 145 jsonl + 157 md（含 12 handoff）+ 2,114 log + 4 子目录；06:28 死亡点见 §2 |
| `22-41-02_01a141b9`（本波） | 10-16 | 考古运维：归档 → F:、蒸馏补齐、垃圾隔离、仓库收口、handoff |
| `01a141af-e714`（空槽位） | 10-15 | 0 消息、未持久化；唯一痕迹 = HTML 导出（已归 F: `sessions/Designers_Brain/aux/`） |
| 会话归档 | — | `F:/backup_famlti_family/sessions/Designers_Brain/raw-20261016/`（5 slugs 非空 + MANIFEST；空 slug 留待清理；家族根制度见其 README） |

