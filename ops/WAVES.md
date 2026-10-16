# WAVES — 波次台账（agent · 目标 · 结局）

> 用途：补 `ops/GOALS.md` 缺的一维——「哪个 agent 在哪一波、结局如何」（113 个嵌套转录的索引；下次考古不再全量重读）。**只追加、不改写历史行**；新波次在表末续行。
> 来源：全机深读报告（机内）`~/.dwgx/ops/research-2026-10-16-deepread/DEEP-DBRAIN.md` §③（10 顶层会话 + 113 嵌套转录）＋本波报告 `ops/archaeology-2026-10-16/reports/01–10`；派发全量（145 工单）见 `reports/09-session-index.md` §2。
> 结局词表：`done`（收口）· `killed`（被中断，无/少产出）· `partial`（部分落盘）· `resumed×N`（同会话续跑轮数）· 行内 ❌/✅ 表单工通道结果。
> 记法：波次 = 会话内编号；`站稳波` = 2026-10-16 考古/归档会话（产出 `ops/archaeology-2026-10-16/`）自编号。

| 波次 | agent | 目标 | 结局 |
|---|---|---|---|
| wave1 | ArtistRenaissance / ArtistVanGoghMonet / ArtistMatisseHokusai / ArtistPicassoCezanne / ArtistExpansion / PromptCorpusHunt / HtmlFrameRender / BlenderScript | 首批 8 位画家档案 + 扩展候选分析 + prompt 语料 + HTML/Blender 工作流 | done：8 档案（252–382 行/份）· expansion 649 行/18 缺口 · 语料 41 条 · 工作流 408/1021 行（10 探针） |
| wave1·跨家 | DB-C1 / DB-C1b / DB-C2 / DB-C2b / DB-C2c / DB-C3 | 跨家通道派发（codex/omp/claude）：候选搜集 / opus55 实例 / 语料批量 | C1 ❌（401）· C2 ❌（3600s 零产出）→ C1b ✅ 69 候选+Top10 · C3 ✅ · C2b/C2c ✅ 126 条 |
| wave2 | ArtistVermeer / ArtistDurer / ArtistCaravaggio / DossierReview / MgStyles15Compare | 3 档案 + 独立复核 + 15 卡同源比对 | done：3 档案 · 复核 31/31 CONFIRMED · 15/15 同源（mg-styles-15, MIT） |
| wave3 | AnimTest01 / ConflictsList / StyleCardTemplates / PipelineHandbook / ArtistCrosscheck | 端到端 #1 + 冲突体系（N1–N9）+ 风格卡模板 + 管线手册 | done：#1 成功（300 帧/24 色）· 18 冲突 + N1–N9 · style_card v0.2 + C1–C10 · 365 行手册 · 392 条对账 |
| wave4 | AuthorTutorial / ImageLibrary / VideoShotcraft | 教程拆解 + 代表作图库 + 镜头技巧调研 | done：教程 14 要点带帧号 · 图库 33 张/20.9 MB · vsc 9 借鉴点 |
| wave5 | AnimTest02 / TransferGuide / VideoShotcraftDeep / AnnotationSweep | 端到端 #2 + 迁移指南 + vsc 深拆 + 标注清扫 | done：#2 成功（一笔画 15/15）· 指南 v1.0 457 行 · 深拆 645 行 · 7/7 |
| wave6 | AnimTest03Blender / TemplatesV03 / ModuleLibrary / ImageChannelProbe / RefsMapping | 端到端 #3（Blender）+ 模板 v0.3 + 模块库 + 图像通道 + 参考帧 | done：#3 成功（300 帧/9 机制/P1）· v0.3 · 11 卡 checks=33 · 通道卡（B-20）· 15/15 + 30 补帧 |
| wave7 | ESeriesT1 → EStyleSep | 偏置诊断（E 系列） | done：E-01 36/36（偏置 7 格）→ §8.1b 拆分 → E-02 21/21（6/7 解除） |
| wave8 | MichelangeloV2 / ComboTest | 偏置修复 + 组合实验 | done：E-03 3/3（7/7 全解除）· E-04 组合 9/9 |
| wave9 | SkillEcosystem / SkillSpec | skill 生态调研 + 规格 | done：8 参照 + 协议 v0 · 规格 v0.2 556 行 + 自检 36/36 |
| wave10 | SkillBuild / BlindRED / BlindGREEN | skill 建包 + RED-GREEN 盲测 | done：包 + junction×4（checked=54）· 盲测行为增量成立（3 修正 + 6 新增层） |
| wave11 | ConsultWalkthrough（+ W01Reviewer）/ AutoTriggerProbe | 全链走查 + 自主触发实测 | done：走查（3 真图候选 + gate + 评审 64/64）· 触发 PASS |
| wave12·仓库 | RepoStandards / I18nZH / I18nJA / AuditZH / AuditJA | 仓库惯例研究 + zh/ja 翻译 + 独立审计 | done：惯例 289 行 · zh/ja 各 5 文件 · 审计 PASS-with-notes（已修） |
| wave12·画家 | ArtistTurner / ArtistRembrandt / ArtistKlimt | 第二批 3 档案（v1） | done：turner / rembrandt / klimt 3 份 v1 |
| wave13 | ArtistGoya / ArtistSeurat / ArtistHopper / ArtistBadaShanren / ArtistQiBaishi / ArtistItoJakuchu / RosterBuilder | 6 档案（v2）+ 名册 | done：goya / seurat / hopper / bada / qi / ito + roster 59 候选/15 文化区 |
| wave14 | BioDaVinci / BioMichelangelo / BioVanGogh / BioMonet / BioPicasso / BioCezanne / BioMatisse / BioHokusai / BioCaravaggio / BioVermeer / BioDurer | 生平加固 pass1（§11 ≥2000 字 + §12） | done：11/11（2080–2816 字）· 3 条旧说 OVERTURNED |
| wave15 | ArtistMucha / ArtistMunch / ArtistKandinsky / ArtistVelazquez / ArtistBosch / ArtistHuangGongwang / ArtistKahlo / ArtistBehzad | 8 位 v2 收口 | done：8/8（kahlo 图全私有） |
| wave16 | ModuleCards20 / IndexMerge | 模块卡 11→20 + 三索引对账 | done：卡 20（checks=60）· 索引对账 |
| wave16p2 | HardTurner / HardRembrandt / HardKlimt / HardGoya / HardSeurat / HardHopper / HardBada / HardQi / HardIto | 加固 pass2（§11.1 补写） | done：9/9 · `STATUS:` 首行约定落地（8/9） |
| wave17 | ArtistFriedrich / ArtistRepin / ArtistRaviVarma / ArtistDegas / ArtistGauguin / ArtistVanEyck / ArtistKngwarreye | 7 位 v2 | done：7/7（kngwarreye 私有 + 原住民伦理护栏） |
| wave18 | ArtistHiroshige / ArtistSargent / ArtistPiero / ArtistArtemisia / ArtistNamatjira / ArtistElSalahi / ArtistWuGuanzhong | 7 位 v2 | done：7/7（带 `STATUS: DONE`；后 3 位全私有） |
| wave16·补 | IndexMerge2 | 三表并 wave15/17 | done：35 位/844 条 · PASS 140/FAIL 0 |
| wave19 | ModuleCards42 + ArtistFanKuan / ArtistSesshu / ArtistConstable / ArtistPoussin / ArtistBruegel / ArtistElGreco / ArtistHolbein / ArtistAivazovsky / ArtistOkeeffe / ArtistRivera | 模块卡 20→42 + 10 位新画家 | 卡 42 ✅（checks=126）；画家 ×10 **killed**（宿主重启，dossier 0 份，RESUME.md 10/10 已写盘） |
| wave19·重派 | 同 wave19 ×10（`-2` 后缀，链接原单） | 先核 scratch 复用 → 重派 | done：10/10 收口（okeeffe / rivera 全私有） |
| wave20 | ArtistZhaoMengfu / ArtistNiZan / ArtistQiuYing / ArtistOgataKorin / ArtistBlake / ArtistChardin / ArtistManet / ArtistSorolla / ArtistZorn / ArtistSultanMohammed | 10 位 v2 | done：10/10 |
| wave21 | ArtistXuBeihong / ArtistLiKeran / ArtistSherGil / ArtistTarsila / ArtistChenHongshou / ArtistXuWei / ArtistHogarth / ArtistMirSayyidAli / ArtistDeChirico / ArtistRockwell | 10 位 v2 | done：10/10（5 位全私有；sher_gil 版权核正） |
| 收口三工 | ModuleCards62 / CrossLinkSync / IndexMerge3 | 卡 42→62 + 互引同步 + 索引三轮 | done：checks=186 · 互引 10 处 · 索引 62 位（PASS 257/0） |
| 站稳波·W1 | SubagentCatalog / HandoffDigest / EndgameReconcile / GarbageAudit / FOuterRecon / StoreInventory / HtmlExportId / AbsorbCheck / SessionCondense / RosterCrosscheck + Archivist | 考古深挖（子代理目录 / 蒸馏 / 对账 / 审计 / 勘察 / 盘点 / 鉴定 / 吸收 / 浓缩 / 核对）+ F: 归档执行 | partial：5 报告落盘（02/04/06/07/09）；5 工 **killed**（provider 503 波）；Archivist 90% 中断 |
| 站稳波·W1-R2 | SubagentCatalog2 / EndgameReconcile2 / FOuterRecon2 / AbsorbCheck2 / RosterCrosscheck2 + ArchivistFinish + CleanerProject | 重派 5 工 + 归档补完（补拷/比对/SHA/MANIFEST/收据）+ 项目垃圾隔离 | done：报告 03/05/08/10 + 子代理目录探针（`_sc2_listing.json`）；补拷 165/FAILED=0 → 2,545 文件（收据 §A）；louvre 移除 + quarantine 落盘 |
| 收口二工（wave21） | IndexMerge4 / ModuleCards72 | 索引四轮（wave21 并入）+ 模块卡 62→72 | done：verify **PASS 282/0**（72 位 / 1934 条 / 公开 723 + 私有 676）· checks=216 · count=72；commits `61c94cb` / `bae29c6` |
| wave22 | ArtistLinFengmian / ArtistUtamaro / ArtistLam / ArtistEnwonwu（重启后 lin/utamaro 由 `-2` 续跑） | roster 余位 4 位 v2（林风眠 / 喜多川歌麿 / 林飞龙 / 恩沃恩乌） | done：4/4（lam/enwonwu/lin 全私有；utamaro 全公开 PD；验收全过；重启零丢失） |

**本波报告（01–10）↔ 工**：01 SubagentCatalog2（探针占位）· 02 HandoffDigest · 03 EndgameReconcile2 · 04 GarbageAudit · 05 FOuterRecon2 · 06 StoreInventory · 07 HtmlExportId · 08 AbsorbCheck2 · 09 SessionCondense · 10 RosterCrosscheck2。

**追加规矩**：新波次在表末续行（四列齐）；失败/续跑如实记（`killed` / `resumed×N`）；细节以各工回执与报告为准，本表只做索引。
