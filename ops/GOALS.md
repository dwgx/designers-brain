# GOALS — LOOP 队列

> 主脑维护。每条 = 一个可完成、可验收的研究目标。状态：`open` / `running` / `done` / `blocked`。
> 发现新线头 → 追加子条目（标 parent）。完成条件 = 一个能看的文件或一条能跑的命令。

## Lane A — 画家蒸馏

| ID | 状态 | 目标 | 产出路径 | 归属 |
|---|---|---|---|---|
| A-01 | done | 达·芬奇档案（252 行 / 17 URL） | `knowledge/domains/painters/dossiers/da_vinci.md` | ArtistRenaissance |
| A-02 | done | 米开朗基罗档案（265 行 / 15 URL） | `knowledge/domains/painters/dossiers/michelangelo.md` | ArtistRenaissance |
| A-03 | done | 梵高档案（296 行 / 23 URL；复核 15/15） | `knowledge/domains/painters/dossiers/van_gogh.md` | ArtistVanGoghMonet |
| A-04 | done | 莫奈档案（306 行 / 19 URL） | `knowledge/domains/painters/dossiers/monet.md` | ArtistVanGoghMonet |
| A-05 | done | 毕加索档案（296 行 / 20 URL；复核 16/16；自纠 1 条流传误挂引文） | `knowledge/domains/painters/dossiers/picasso.md` | ArtistPicassoCezanne |
| A-06 | done | 塞尚档案（306 行 / 20 URL） | `knowledge/domains/painters/dossiers/cezanne.md` | ArtistPicassoCezanne |
| A-07 | done | 马蒂斯档案（288 行 / 20 URL） | `knowledge/domains/painters/dossiers/matisse.md` | ArtistMatisseHokusai |
| A-08 | done | 葛饰北斋档案（297 行 / 19 URL） | `knowledge/domains/painters/dossiers/hokusai.md` | ArtistMatisseHokusai |
| A-09 | done | 扩展候选分析（649 行 / 88 URL；18 条能力缺口 G1-G18） | `knowledge/domains/painters/dossiers/expansion.md` | ArtistExpansion |
| A-10 | done | 原话语料 8 文件 126 条（16/15/20/17/16/17/13/12；逐条带来源+类型；INDEX.md 已建） | `knowledge/domains/painters/dossiers/_corpus/` | 跨家 OmpCorpusA/B（DB-C2b/C2c 均 ok） |
| A-11 | done | 独立复核（31 条抽检全 CONFIRMED；4 处标注级修正已派回） | `knowledge/domains/painters/dossiers/_review.md` | DossierReview（wave2） |
| A-12 | done(v0.1) | 组合实验设计 v0.1（wave3 用真实模块修订） | `experiments/design.md` | 主脑 |
| A-13 | done | 源视频回捞（教程片 + 展示片均已下载至 `knowledge/domains/motion-graphics/sources/`；仓库 videos/ 15 支成片可 raw 直取） | `knowledge/domains/motion-graphics/sources/` | 主脑 |
| A-14 | done | 逐条对账（392 条：自述支撑 100 / 研究 153 / 史料 46 / 纯归纳 93；20 条纯归纳指纹列为实验优先验证对象） | `knowledge/domains/painters/dossiers/_crosscheck.md` | ArtistCrosscheck（wave3） |
| A-15 | done | 卡拉瓦乔档案（359 行 / 31 URL；发现硬阴影冲突 → B-12） | `knowledge/domains/painters/dossiers/caravaggio.md` | ArtistCaravaggio（wave2） |
| A-16 | done | 维米尔档案（382 行 / 39 URL） | `knowledge/domains/painters/dossiers/vermeer.md` | ArtistVermeer（wave2） |
| A-17 | done | 丢勒档案（349 行 / 24 URL） | `knowledge/domains/painters/dossiers/durer.md` | ArtistDurer（wave2） |
| A-18 | done | 标注清扫（7/7 问题修复；§4 补 64 条 [归纳]；6 处口径归一 [研究]；11 份文件头已标） | `knowledge/domains/painters/dossiers/*.md` | AnnotationSweep（wave5） |
| A-19 | done | 模块库：11 张模块卡 + README + 校验器（33/33 逐字一致；sha256 抽检 IDENTICAL） | `knowledge/domains/painters/modules/` | ModuleLibrary（wave6） |
| E-01 | done | E0+E1 首批图像实验：36/36 张（12 格 × 3）+ RESULTS.md + sheet_all.png；实测：裸模型名、无负向通道、尺寸 768×1152 | `experiments/E1_t1/` | ESeriesT1（wave7） |
| E-02 | done | 题材偏置诊断（12 格 → 7 格偏置）+ §8.1b 纯风格段拆分（7 卡 + 4 卡注记）+ E1b 重跑 21/21 张；同格对照：6/7 解除或基本解除、1 部分解除（michelangelo）；验收：`python _verify_t1b.py` → VERIFY PASS；`python _extract.py --check` → checks=33 ok=33 fail=0 | `experiments/E1_t1b/` | EStyleSep（wave7） |
| E-03 | done | michelangelo 深度解除：§8.1b v2 从句级改写 → 重测 **3/3 解除**（云/浪/岩承载体块扭转；v1 原样存档可审计）——**7/7 全部解除或基本解除** | `experiments/E1_t1c/` | MichelangeloV2（wave8） |
| E-04 | done | E2 首批组合：9/9 张（融合成立：e2a 厚涂×高调、e2b 两语言在场、e2c 分区一致）；N1/N4/N9 全记录；双标准零出现（e2b 单侧化已记录） | `experiments/E2_t1/` | ComboTest（wave8） |

| A-20 | done | 第二批·透纳：345 行档案 + 语料 19 条 + 图库 5 张（全 PD）；分工 vs 莫奈写死（复读引用 monet §3）；验收：`_extract` 抽取跑通（§8.1/§8.2/§4）+ 回归 33/33 | `knowledge/domains/painters/dossiers/turner.md` | ArtistTurner（wave12） |
| A-21 | done | 第二批·伦勃朗：413 行档案 + 语料 17 条 + 图库 6 张（超 v2 口径）；分工 vs 卡拉瓦乔写死（光=连续衰减+心理）；验收：结构同构检查 PASS | `knowledge/domains/painters/dossiers/rembrandt.md` | ArtistRembrandt（wave12） |
| A-22 | done | 第二批·克里姆特：379 行档案 + 语料 11 条 + 图库 3 张；分工 vs 马蒂斯写死；验收：抽取契约实测 PASS（§8.1=1465 chars / §8.2=7 条 / §4=6 参数） | `knowledge/domains/painters/dossiers/klimt.md` | ArtistKlimt（wave12） |
| A-23 | done | wave13·戈雅：472 行 v2 档案（§11 生平 + §12 临摹清单）+ 语料 22 条 + 图库 9 张（Met CC0×3 + PD×6）+ 私有 2 件；分工 vs 卡拉瓦乔/伦勃朗写死（画内光源数等可实测判据）；抽取直测 PASS | `knowledge/domains/painters/dossiers/goya.md` | ArtistGoya（wave13） |
| A-24 | done | wave13·修拉：443 行 v2 档案（§11 生平 + §12 临摹清单）+ 语料 19 条 + 图库 10 张 + 私有层（Met 1991 目录 PDF + OCR）；分工 vs 莫奈写死；抽取实测 PASS | `knowledge/domains/painters/dossiers/seurat.md` | ArtistSeurat（wave13） |
| A-25 | done | wave13·霍珀：460 行 v2 档案（§11 生平 + §12 临摹清单）+ 语料 25 条 + **图库 9 张全在 `_private/`**（公开侧零图，权利行逐张）；分工 vs 维米尔写死；抽取实测 PASS | `knowledge/domains/painters/dossiers/hopper.md` | ArtistHopper（wave13） |
| A-26 | done | wave13·八大山人：370 行 v2 档案（§11 生平 + §12 临摹清单）+ 语料 22 条 + 图库 9 张（全 PD/CC0）+ 私有补遗 5 条；分工 vs 北斋写死；抽取预演 PARSE OK | `knowledge/domains/painters/dossiers/bada_shanren.md` | ArtistBadaShanren（wave13） |
| A-27 | running | wave13·齐白石 v2（vs 马蒂斯/八大分工；版权图审慎） | `knowledge/domains/painters/dossiers/qi_baishi.md` | ArtistQiBaishi（wave13） |
| A-28 | done | wave13·伊藤若冲：447 行 v2 档案（§11 生平 + §12 临摹 9 件）+ 语料 24 条 + 图库 18 张（ColBase/Commons/Met）+ 私有补遗；分工 vs 北斋/克里姆特写死；自检全过 | `knowledge/domains/painters/dossiers/ito_jakuchu.md` | ArtistItoJakuchu（wave13） |
| A-29 | done | 名册：**59 位**候选（15 文化区；49 新增）+ wave 批次建议（8/7/7）；验收：349 行 + 机械检查全 PASS（候选 59 / §1=10 / §2=49 / 交集 ∅） | `knowledge/domains/painters/program/roster.md` | RosterBuilder（wave13） |
| A-30 | open | 学习产物：每大师「学习路径卡」+ 总学习路线（Owner 已批；roster 后启动） | `knowledge/domains/painters/program/learning/` | 主脑 |
| A-31 | done | 加固·达芬奇：§11（2688 字 + 39 行年表 + 27 来源）+ §12（9 件）；语料 16→22 条；验收：`_extract.py --check` 33/33 + URL 抽检 12/12 | `knowledge/domains/painters/dossiers/da_vinci.md` | BioDaVinci（wave14） |
| A-32 | running | 加固·米开朗基罗：§11 + §12 | `knowledge/domains/painters/dossiers/michelangelo.md` | BioMichelangelo（wave14） |
| A-33 | done | 加固·梵高：§11（2561 字 + 24 行年表 + 18 来源；16 条引文 byte-exact 核验）+ §12（10 件）；语料 20→36 条；「903 封」旧 [UNVERIFIED] 收口；验收：`_extract` 33/33 + skill selfcheck PASS | `knowledge/domains/painters/dossiers/van_gogh.md` | BioVanGogh（wave14） |
| A-34 | done | 加固·莫奈：§11（2108 字 + 42 行年表 + 14 新来源）+ §12（9 件）；语料 17→29 条；验收：`_extract.py --check` 33/33 + 序号连续 | `knowledge/domains/painters/dossiers/monet.md` | BioMonet（wave14） |
| A-35 | running | 加固·毕加索：§11 + §12 | `knowledge/domains/painters/dossiers/picasso.md` | BioPicasso（wave14） |
| A-36 | done | 加固·塞尚：§11（2297 字 + 31 行年表 + 16 来源；「绝交信」旧说 OVERTURNED）+ §12（9 件）；语料 17→24 条；验收：`_extract.py --check` 33/33 | `knowledge/domains/painters/dossiers/cezanne.md` | BioCezanne（wave14） |
| A-37 | done | 加固·马蒂斯：§11（2643 字 + 54 行年表 + 17 来源）+ §12（10 件）；语料 13→24 条；验收：`_extract.py --check` 33/33 + 引文抽查 5/5 | `knowledge/domains/painters/dossiers/matisse.md` | BioMatisse（wave14） |
| A-38 | done | 加固·北斋：§11（2080 字 + 34 行年表 + 16 来源）+ §12（10 件）；语料 +7 → 19 条；验收：`_extract.py --check` 33/33 + git diff 仅 2 文件 | `knowledge/domains/painters/dossiers/hokusai.md` | BioHokusai（wave14） |
| A-39 | running | 加固·卡拉瓦乔：§11 + §12 | `knowledge/domains/painters/dossiers/caravaggio.md` | BioCaravaggio（wave14） |
| A-40 | done | 加固·维米尔：§11（2578 字 + 39 行年表 + 14 来源 + 未找到 7 条）+ §12（10 件）；语料新建 22 条；验收：`_extract.py --check` 33/33 + git diff 纯插入 0 删除 | `knowledge/domains/painters/dossiers/vermeer.md` | BioVermeer（wave14） |
| A-41 | running | 加固·丢勒：§11 + §12 | `knowledge/domains/painters/dossiers/durer.md` | BioDurer（wave14） |
| A-42 | running | wave15·慕夏（Mucha）v2 全规格 | `knowledge/domains/painters/dossiers/mucha.md` | ArtistMucha（wave15） |
| A-43 | running | wave15·蒙克（Munch）v2 | `knowledge/domains/painters/dossiers/munch.md` | ArtistMunch（wave15） |
| A-44 | running | wave15·康定斯基（Kandinsky）v2 | `knowledge/domains/painters/dossiers/kandinsky.md` | ArtistKandinsky（wave15） |
| A-45 | running | wave15·委拉斯开兹（Velázquez）v2 | `knowledge/domains/painters/dossiers/velazquez.md` | ArtistVelazquez（wave15） |
| A-46 | running | wave15·博斯（Bosch）v2 | `knowledge/domains/painters/dossiers/bosch.md` | ArtistBosch（wave15） |
| A-47 | running | wave15·黄公望 v2（水墨山水） | `knowledge/domains/painters/dossiers/huang_gongwang.md` | ArtistHuangGongwang（wave15） |
| A-48 | running | wave15·弗里达·卡罗（Kahlo）v2（版权图入 `_private/`） | `knowledge/domains/painters/dossiers/kahlo.md` | ArtistKahlo（wave15） |
| A-49 | running | wave15·贝赫扎德（Behzād）v2（波斯细密画） | `knowledge/domains/painters/dossiers/behzad.md` | ArtistBehzad（wave15） |

## Lane B — Agent 代码艺术

| ID | 状态 | 目标 | 产出路径 | 归属 |
|---|---|---|---|---|
| B-01 | done | 15 卡结构蒸馏 | `knowledge/domains/motion-graphics/cards/structure.md` | 主脑 |
| B-02 | done | HTML/WebGL 逐帧渲染工作流（408 行 / 34 URL；B-09 并入 §5） | `knowledge/agent-art/html/workflow.md` | HtmlFrameRender |
| B-03 | done | Blender bpy 工作流（1021 行 + 10 个实测探针 + 样张） | `knowledge/agent-art/blender/workflow.md` | BlenderScript |
| B-04 | done | prompt 语料（41 条）+ 模式对照（14 条） | `knowledge/agent-art/prompts/` | PromptCorpusHunt |
| B-05 | done | repo 猎场（69 行候选 + Top10 评估 + 31 条 API 证据） | `knowledge/agent-art/github/` | 跨家 OmpGitHunt（DB-C1b） |
| B-06 | done | Opus 5.5 证据链（16 外部实例） | `knowledge/agent-art/opus55/` | 跨家 OmpOpus55（DB-C3） |
| B-07 | done | 端到端验证 #1：**非 Opus 模型跑通**——300 帧 / 24 色 / 合成音轨，端到端 21s；抓出「乱序重渲才暴露」的 fillStyle 静默 bug | `experiments/anim_test_01/` | AnimTest01（wave3，coder） |
| B-08 | done | 迁移指南 v1.0（457 行 / 7 节 / 17 个可复制文本块；契约最小集 + 模型适配矩阵 T1–T4 + 17 条坑） | `knowledge/cross/transfer_guide.md` | TransferGuide（wave5） |
| B-09 | done | 逐帧自查自动化调研（并入 B-02 §5） | 见 B-02 | HtmlFrameRender |
| B-10 | done | mg-styles-15 溯源与逐条对照（**15/15 同源确认**；管线/评审/音频拆解；MIT 边界） | `knowledge/domains/motion-graphics/cards/mg-styles-15_compare.md` | MgStyles15Compare（wave2） |
| B-11 | done | 外部发现落成 templates（style_card v0.2 + 确定性契约 C1–C10 + 7 维评审 rubric） | `templates/` + `knowledge/cross/review_rubric.md` | StyleCardTemplates（wave3） |
| B-12 | done | Lane A×B 冲突清单（18 条冲突 + N1–N9 组合规则 + 8 对 near-miss；75/75 引用核验） | `knowledge/cross/conflicts.md` | ConflictsList（wave3） |
| B-13 | done | mg-styles-15 管线手册（365 行逐文件拆解：渲染/音频/Blender/评审 + 抄/不抄 18 条） | `knowledge/domains/motion-graphics/cards/mg-styles-15_handbook.md` | PipelineHandbook（wave3） |
| B-14 | done | video-shotcraft 调研（仓已定位：11,988★ / Apache-2.0；124 镜头卡 + Remotion 路线 + 验收工程；9 条借鉴点） | `knowledge/domains/motion-graphics/cards/video_shotcraft.md` | VideoShotcraft（wave4） |
| B-16 | done | vsc 深拆（645 行：三层卡库同步门 / 27 条判例规则 / 2 帧号验收链 + 干净上下文终检 / 工作台 parity） | `knowledge/domains/motion-graphics/cards/video_shotcraft_handbook.md` | VideoShotcraftDeep（wave5） |
| B-18 | done | 模板 v0.3/v0.2：判例式规则格式 + 2 帧号验收 + 两轴推导 + 干净上下文终检（196/221 行） | `templates/style_card.md` + `review_rubric.md` | TemplatesV03（wave6） |
| B-19 | done | 端到端验证 #3（Blender 线）：3D 质感卡 300 帧 / 10s 交付（弹珠+PLAY+推镜；9 项机制机械证据；确定性 P1 ≤0.05% 像素）——**三条管线全部端到端验证** | `experiments/anim_test_03_blender/` | AnimTest03Blender（wave6） |
| B-20 | done | 图像通道：**网关直连 API 可用**（grok-imagine-image/-2.0/-lite + edit + video 全实测；omp CLI 路径不可用已解剖）；E 系列解锁 | `knowledge/cross/image_channel.md` + `_image_probes/` | ImageChannelProbe（wave6） |
| B-17 | done | 端到端验证 #2：一笔画卡跑通——300 帧、**一根线机械连通验证 15/15**、乱序重渲 5/5；结论「**管线零改动可迁移，风格机制必须重写+配套机械检查**」 | `experiments/anim_test_02/` | AnimTest02（wave5，coder） |
| B-15 | done | 作者教程片拆解（14 条要点带帧号；两智能体分工「三句话」法；62 帧+18 接触表；51 帧号零缺失） | `knowledge/domains/motion-graphics/cards/author_tutorial.md` | AuthorTutorial（wave4） |

## Lane C — 跨家派发通道

| ID | 状态 | 目标 | 归属 |
|---|---|---|---|
| C-01 | done | 跨家工人记账与收口（DB-C1 failed(401)→DB-C1b ok；DB-C2 failed(claude 超时)→拆 2 工 DB-C2b/C2c ok；DB-C3 ok；共 6 单全收口） | 主脑 |
| C-02 | done | 跨家收口对账：board reconcile 中 DB-* 零未收口（2026-10-15 核；验收：`board.py list` 查 DB-C2b → CLOSE ok + VERIFY） | 主脑 |

## Lane D — 联网/浏览器

| ID | 状态 | 目标 | 产出路径 | 归属 |
|---|---|---|---|---|
| D-01 | done | 素材索引（18 图 + 15 裁切 + 对话作品；CDN 抽 1 条实测可达） | `knowledge/INDEX.md` | 主脑 |
| D-02 | done | 代表作图库（11 位 × 3 张 = 33 张 / 20.9MB / 全 PD-开放许可 + manifest 282 行；Met 15 / AIC 4 / Cleveland 3 / Commons 11） | `knowledge/domains/painters/dossiers/_images/` | ImageLibrary（wave4） |
| D-03 | done | 参考帧映射：15/15 映射表 + 30 张补帧（t3/t8）；验收：30 张存在 + 抽查 01-flat-vector_t8 / 18-hanazi_t3（ffprobe+sha256，见 refs/README.md §5）→ `refs/README.md` | `knowledge/domains/motion-graphics/sources/refs/` | RefsMapping（wave6） |

## Lane S — Skill 化（Designers_Brain 设计顾问）

| ID | 状态 | 目标 | 产出路径 | 归属 |
|---|---|---|---|---|
| S-01 | done | 生态调研：superpowers 体系 + 8 参照；格式规范（agentskills.io）/ 触发机制 / 提问协议（12+5 条问法）；refs 留档 23 文件 | `docs/skill/skill_ecosystem.md` + `docs/skill/refs/` | SkillEcosystem（wave9） |
| S-02 | done | skill 规格 v0.2（556 行）+ SKILL.md 草案（106 行）+ 自检脚本（checked=36 ok=36）；命名裁定 `designers-brain` | `docs/skill/skill_spec.md` + `docs/skill/draft/SKILL.md` | SkillSpec（wave9） |
| S-03 | done | 建包落地 + 激活：SKILL.md 106 行 + references×9 + domains.yaml + 打包件×3；junction ×4 全解析；验收：`python docs/skill/_selfcheck.py` → PASS（checked=54 / junctions=4/4）+ `_extract.py --check` 33/33 | `skills/designers-brain/` + `docs/skill/build_receipt.md` | SkillBuild（wave10） |
| S-04 | done | 盲测（RED-GREEN）：**行为增量成立**（3 修正 + 6 新增层）；候选数口径裁定写回；报告：`docs/skill/test_report.md` | `docs/skill/tests/` | 主脑（wave10） |
| S-05 | done | 走查（演练版）：全链真跑 4 轮（首问包 → 推荐单 → 3 真图候选 + 展示后停 → 定稿 + gate + 独立评审）；机械 64/64；自主触发：新鲜 omp 进程 catalog 已含 designers-brain | `docs/skill/walkthrough_01/` + `docs/skill/tests/autotrigger_probe.md` | ConsultWalkthrough（wave11） |
| S-06 | open | skill 改进 4 条（走查发现）：近似 opt-out 口径 / 无字 KV↔海报边界 / 组合建议可判读观察点 / rubric 静态图适配 → spec v0.3 补丁 | `docs/skill/skill_spec.md` | 主脑 |

## Lane R — Repo & Release

| ID | 状态 | 目标 | 产出路径 | 归属 |
|---|---|---|---|---|
| R-01 | done | 仓库重构：research/ → knowledge/ + experiments/ + docs/ + ops/；引用重写（99 文件）；验证器全回归 PASS（33/33 · skill selfcheck · E×4 · W01 64/64 · anim×3） | `docs/MIGRATION.md` | 主脑 |
| R-02 | done | 英文主文档 11 件（README/ARCHITECTURE/WORKFLOW/PROTOCOLS/ROADMAP/CONTRIBUTING/AGENTS/CLAUDE/NOTICE/LICENSE×2） | 根目录 + `docs/` | 主脑 |
| R-03 | done | i18n：zh-CN + ja（README + 四文档）落盘 + 独立审计（PASS-with-notes；问题 3+5 条全部修正） | `docs/i18n/` + `README.<lang>.md` | I18nZH / I18nJA + AuditZH/JA |
| R-04 | done | **GitHub public 发布**：https://github.com/dwgx/designers-brain（main @ ae0680b；1008 文件 / 369 MiB；许可检测 CC-BY-4.0 + MIT；topics ×7）；验收：远端 README 抓取 + gh api 元数据 + git ls-remote | github.com/dwgx/designers-brain | 主脑 |

## 环境实测（2026-10-15，供后续引用）

- node v24.19.0 · npm 11.17.0 · ffmpeg n9.0.1 · Python 3.14.7 · **ImageMagick 未装**
- Blender 5.2.1 LTS @ `D:/Software/Blender Foundation/Blender 5.2/blender.exe`（不在 PATH）；内置 Python 3.13.13；RTX 5070 Ti Laptop 可识别
- puppeteer 缓存：`C:/Users/dwgx1/.cache/puppeteer`（chrome + chrome-headless-shell）
- web_search 全 provider 限流（2026-10-15 全天）；替代 = read / curl / urllib / eval browser / GitHub API（全部实测可用）
- codex 后端 401 断供（缺鉴权）；claude/omp 后端正常

## 记账约定

- 完成时把状态改 `done` + 一行「验收：<跑过的命令/文件>」。被推翻的结论从产物删掉，并在本条写「OVERTURNED: …」。
