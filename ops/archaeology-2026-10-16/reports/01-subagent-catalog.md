# 01 · 子代理目录（SubagentCatalog）— S-main 工作件总表

> **v1.1 完整版**（覆盖 v0.9/v1.0；jsonl 145/145 已全量提取；md 157/157 已分类、非空 130 件首行已全采；4 子目录已列内容）
> 写手：SubagentCatalog2（scout）· 2026-10-16 · 目标目录（冻结于 10-16 06:28:31 JST SIGHUP）：
> `C:/Users/dwgx1/.omp/agent/sessions/--D--Project-Designers_Brain--/2026-10-15T06-29-46-426Z_01a13e40-a53a-7169-8317-62a0dc18de57/`

## 0 · 摘要计数（对账 ✓）

- 目录条目 **2420** = `*.jsonl` **145** ＋ `*.md` **157** ＋ 日志 **2114**（bash/eval/read/async.log）＋ 子目录 **4**
- 口径：浏览器目录清单实测（精确字节 + epoch mtime，已存 `_sc2_listing.json`）；本工无 bash，改用 `read`+jq `[., inputs]` 全流提取，逐文件取：首条用户消息 / agent / 末条 assistant 文本 / 末 3 条工具命令 / exit / error。
- 波次（w）为推断值：w14 加固 / w15-w16 / w16p2 加固 / w17 / w18 / w19（首轮+重派）/ w20 / w21 / 收口；时间锚：epoch 1792099711 = 10-16 06:28:31 JST。
- mtime 列 = 会话 jsonl 最后写入时刻（JST，±1 分钟内）。

## 1 · jsonl 总表（145/145）

> 分组 = 按时段；行内 波次 供检索。类型 = 会话 agent 角色（researcher/coder/verifier/task）。

### 1.1 早期批 · 10-15 16:16–19:54（32）

| 文件名 | 类型 | 大小 | mtime | 波次 | 一句话角色 | 状态 |
|---|---|---|---|---|---|---|
| BlenderScript.jsonl | 转录·researcher | 1.1MB | 10-15 16:26 | 早期 | Blender 工作流+脚本（research/agent-art/blender/） | DONE |
| PromptCorpusHunt.jsonl | 转录·researcher | 1.1MB | 10-15 16:27 | 早期 | 提示词语料 41 例（B-04） | DONE |
| ArtistRenaissance.jsonl | 转录·researcher | 1.4MB | 10-15 16:29 | 早期 | 达·芬奇/米开朗基罗两档案 | DONE |
| ArtistMatisseHokusai.jsonl | 转录·researcher | 1.1MB | 10-15 16:47 | 早期 | 马蒂斯/北斋两档案（冻结） | DONE |
| ArtistExpansion.jsonl | 转录·researcher | 2.1MB | 10-15 16:51 | 早期 | 扩展候选分析（A-09，681 行） | DONE |
| ArtistDurer.jsonl | 转录·researcher | 1.1MB | 10-15 16:56 | 早期 | 丢勒档案（A-17） | DONE |
| ArtistVermeer.jsonl | 转录·researcher | 1.5MB | 10-15 16:56 | 早期 | 维米尔档案（A-16） | DONE |
| ArtistCaravaggio.jsonl | 转录·researcher | 1.2MB | 10-15 16:57 | 早期 | 卡拉瓦乔档案（359 行） | DONE |
| MgStyles15Compare.jsonl | 转录·researcher | 900KB | 10-15 16:57 | 早期 | mg-styles-15 对照卡（388 行） | DONE |
| StyleCardTemplates.jsonl | 转录·researcher | 1.0MB | 10-15 16:58 | 早期 | 确定性契约+style_card v0.2 | DONE |
| ArtistVanGoghMonet.jsonl | 转录·researcher | 1.4MB | 10-15 16:59 | 早期 | 梵高/莫奈两档案 | DONE |
| ArtistPicassoCezanne.jsonl | 转录·researcher | 1.5MB | 10-15 17:01 | 早期 | 毕加索/塞尚两档案 | DONE |
| ArtistCrosscheck.jsonl | 转录·researcher | 960KB | 10-15 17:22 | 早期 | 11 档案对账（_crosscheck.md） | DONE |
| ConflictsList.jsonl | 转录·researcher | 1.2MB | 10-15 17:35 | 早期 | conflicts.md 冻结（B-12） | DONE |
| VideoShotcraft.jsonl | 转录·researcher | 670KB | 10-15 17:36 | 早期 | 分镜卡（B-14） | DONE |
| AuthorTutorial.jsonl | 转录·researcher | 1.1MB | 10-15 17:45 | 早期 | 作者教程卡（B-15） | DONE |
| AnimTest01.jsonl | 转录·coder | 1.1MB | 10-15 17:52 | 早期 | 动画测试 #1（anim_test_01） | DONE |
| ImageLibrary.jsonl | 转录·researcher | 850KB | 10-15 17:55 | 早期 | 代表作图库（D-02） | DONE |
| HtmlFrameRender.jsonl | 转录·researcher | 1.0MB | 10-15 18:02 | 早期 | HTML 工作流回填 | DONE |
| PipelineHandbook.jsonl | 转录·researcher | 950KB | 10-15 18:01 | 早期 | mg-styles-15 手册回填（B-07） | DONE |
| TransferGuide.jsonl | 转录·researcher | 860KB | 10-15 18:11 | 早期 | 迁移指南 v1.0（457 行） | DONE |
| AnnotationSweep.jsonl | 转录·researcher | 1.5MB | 10-15 18:13 | 早期 | 标注修正 11 档案 | DONE |
| VideoShotcraftDeep.jsonl | 转录·researcher | 1.1MB | 10-15 18:13 | 早期 | 分镜手册深化（645 行） | DONE |
| AnimTest02.jsonl | 转录·coder | 1.9MB | 10-15 18:35 | 早期 | 动画测试 #2（B-17 out.mp4） | DONE |
| ModuleLibrary.jsonl | 转录·researcher | 1.1MB | 10-15 18:46 | 早期 | 模块库目录（artist_modules） | DONE |
| TemplatesV03.jsonl | 转录·researcher | 1.7MB | 10-15 18:47 | 早期 | style_card.md v0.3 | DONE |
| RefsMapping.jsonl | 转录·researcher | 820KB | 10-15 18:50 | 早期 | 参考映射（D-03） | DONE |
| ImageChannelProbe.jsonl | 转录·researcher | 1.2MB | 10-15 18:58 | 早期 | 图像通道探针卡 | DONE |
| ESeriesT1.jsonl | 转录·coder | 1.4MB | 10-15 19:25 | 早期 | E1_t1 首批实验 36 张（E-01） | DONE |
| AnimTest03Blender.jsonl | 转录·coder | 3.0MB | 10-15 19:53 | 早期 | 动画端到端验证 #3（B-19） | DONE |
| EStyleSep.jsonl | 转录·researcher | 1.8MB | 10-15 19:54 | 早期 | 风格分离实验（E-02） | DONE |
| DossierReview.jsonl | 转录·researcher | 1.1MB | 10-15 16:56 | 早期 | 独立复核（_review.md 480 行） | DONE |

### 1.2 中段 · 10-15 20:06–23:59（29）

| 文件名 | 类型 | 大小 | mtime | 波次 | 一句话角色 | 状态 |
|---|---|---|---|---|---|---|
| MichelangeloV2.jsonl | 转录·researcher | 1.3MB | 10-15 20:08 | 早期 | michelangelo.md §8.1b 修订 v2 | DONE |
| ComboTest.jsonl | 转录·coder | 1.4MB | 10-15 20:13 | 早期 | E2 组合实验（E-04） | DONE |
| SkillEcosystem.jsonl | 转录·researcher | 1.3MB | 10-15 21:14 | 技能线 | 技能生态调研（refs 23 件） | DONE |
| SkillSpec.jsonl | 转录·researcher | 2.3MB | 10-15 21:14 | 技能线 | 技能规格 v0.1+自检脚本 | DONE |
| SkillBuild.jsonl | 转录·coder | 1.1MB | 10-15 21:25 | 技能线 | 技能包落地与激活 | DONE |
| BlindRED.jsonl | 转录·task | 212KB | 10-15 21:30 | 技能线 | 盲测红稿（普通用户模拟） | DONE |
| BlindGREEN.jsonl | 转录·task | 1.0MB | 10-15 21:38 | 技能线 | 盲测绿稿（按 SKILL 协议） | DONE |
| AutoTriggerProbe.jsonl | 转录·task | 300KB | 10-15 21:50 | 技能线 | 自动触发探针 | DONE |
| ConsultWalkthrough.jsonl | 转录·coder | 1.5MB | 10-15 22:14 | 技能线 | 技能演练 walkthrough_01 | DONE |
| RepoStandards.jsonl | 转录·researcher | 800KB | 10-15 22:32 | 技能线 | 仓库规范（289 行） | DONE |
| I18nZH.jsonl | 转录·researcher | 1.1MB | 10-15 22:45 | i18n | 中文文档五件套 | DONE |
| I18nJA.jsonl | 转录·researcher | 1.3MB | 10-15 22:46 | i18n | 日文文档五件套 | DONE |
| AuditZH.jsonl | 转录·verifier | 870KB | 10-15 22:57 | i18n | 中文对照审计报告 | DONE |
| AuditJA.jsonl | 转录·verifier | 1.1MB | 10-15 23:00 | i18n | 日文对照审计报告 | DONE |
| ArtistKlimt.jsonl | 转录·researcher | 2.2MB | 10-15 23:34 | w13 | 克里姆特 v2（A-22） | DONE |
| RosterBuilder.jsonl | 转录·researcher | 1.4MB | 10-15 23:35 | w13 | 59 位候选名单 roster.md | DONE |
| ArtistRembrandt.jsonl | 转录·researcher | 2.0MB | 10-15 23:40 | w12 | 伦勃朗 v2 三处（A-21） | DONE |
| ArtistSeurat.jsonl | 转录·researcher | 2.1MB | 10-15 23:44 | w13 | 修拉 v2（A-24） | DONE |
| ArtistTurner.jsonl | 转录·researcher | 2.6MB | 10-15 23:44 | w12 | 透纳 v2 三处（A-20） | DONE |
| ArtistHopper.jsonl | 转录·researcher | 1.9MB | 10-15 23:44 | w13 | 霍珀 v2（A-64 前身） | DONE |
| ArtistGoya.jsonl | 转录·researcher | 1.9MB | 10-15 23:45 | w15 | 戈雅 v2（A-23） | DONE |
| BioHokusai.jsonl | 转录·researcher | 1.9MB | 10-15 23:52 | w14加固 | 北斋加固（A-38） | DONE |
| BioMonet.jsonl | 转录·researcher | 1.7MB | 10-15 23:53 | w14加固 | 莫奈加固（A-34） | DONE |
| BioVermeer.jsonl | 转录·researcher | 1.9MB | 10-15 23:55 | w14加固 | 维米尔加固（A-40） | DONE |
| ArtistItoJakuchu.jsonl | 转录·researcher | 2.4MB | 10-15 23:56 | w15 | 伊藤若冲 v2（A-28） | DONE |
| BioCezanne.jsonl | 转录·researcher | 2.2MB | 10-15 23:56 | w14加固 | 塞尚加固 | DONE |
| BioDaVinci.jsonl | 转录·researcher | 1.8MB | 10-15 23:59 | w14加固 | 达·芬奇加固（A-31） | DONE |
| BioMatisse.jsonl | 转录·researcher | 1.9MB | 10-15 23:59 | w14加固 | 马蒂斯加固（A-37） | DONE |
| BioVanGogh.jsonl | 转录·researcher | 2.2MB | 10-15 23:59 | w14加固 | 梵高加固（A-33） | DONE |

### 1.3 凌晨批 · 10-16 00:00–02:02（51）

| 文件名 | 类型 | 大小 | mtime | 波次 | 一句话角色 | 状态 |
|---|---|---|---|---|---|---|
| BioDurer.jsonl | 转录·researcher | 2.3MB | 10-16 00:01 | w14加固 | 丢勒加固（A-41） | DONE |
| ArtistQiBaishi.jsonl | 转录·researcher | 1.9MB | 10-16 00:02 | w15 | 齐白石 v2+与八大互核 | DONE |
| ArtistBadaShanren.jsonl | 转录·researcher | 2.3MB | 10-16 00:03 | w15 | 八大山人 v2+与齐白石互核 | DONE |
| BioMichelangelo.jsonl | 转录·researcher | 2.0MB | 10-16 00:03 | w14加固 | 米开朗基罗加固 | DONE |
| BioPicasso.jsonl | 转录·researcher | 2.0MB | 10-16 00:11 | w14加固 | 毕加索加固（A-32，e62e2ee） | DONE |
| BioCaravaggio.jsonl | 转录·researcher | 2.4MB | 10-16 00:13 | w14加固 | 卡拉瓦乔加固（A-39） | DONE |
| ArtistMunch.jsonl | 转录·researcher | 2.1MB | 10-16 00:21 | w15 | 蒙克 v2（A-43） | DONE |
| ArtistBosch.jsonl | 转录·researcher | 2.2MB | 10-16 00:26 | w15 | 博斯 v2（A-46） | DONE |
| ArtistKahlo.jsonl | 转录·researcher | 2.3MB | 10-16 00:26 | w15 | 卡罗 v2（A-48） | DONE |
| ArtistMucha.jsonl | 转录·researcher | 2.8MB | 10-16 00:28 | w15 | 慕夏 v2 | DONE |
| ArtistVelazquez.jsonl | 转录·researcher | 2.2MB | 10-16 00:31 | w15 | 委拉斯开兹 v2 | DONE |
| ArtistBehzad.jsonl | 转录·researcher | 2.1MB | 10-16 00:34 | w17 | 贝赫扎德 v2 | DONE |
| ArtistKandinsky.jsonl | 转录·researcher | 2.1MB | 10-16 00:38 | w17 | 康定斯基 v2 | DONE |
| ModuleCards20.jsonl | 转录·coder | 2.0MB | 10-16 00:39 | w16系 | 模块卡 11→20（A-50） | DONE |
| ArtistRaviVarma.jsonl | 转录·researcher | 2.3MB | 10-16 00:42 | w17 | 拉维·瓦尔马 v2（A-54） | DONE |
| ArtistHuangGongwang.jsonl | 转录·researcher | 2.7MB | 10-16 00:44 | w15 | 黄公望 v2 | DONE |
| IndexMerge.jsonl | 转录·coder | 2.6MB | 10-16 00:49 | w16系 | 三份共享索引首轮合并 | DONE |
| ArtistFriedrich.jsonl | 转录·researcher | 2.4MB | 10-16 00:54 | w17 | 弗里德里希 v2（A-52） | DONE |
| ArtistKngwarreye.jsonl | 转录·researcher | 2.1MB | 10-16 00:54 | w17 | 恩格瓦雷 v2（A-58） | DONE |
| ArtistVanEyck.jsonl | 转录·researcher | 2.3MB | 10-16 00:55 | w17 | 凡·艾克 v2（A-57） | DONE |
| ArtistDegas.jsonl | 转录·researcher | 2.1MB | 10-16 00:56 | w17 | 德加 v2（A-55） | DONE |
| ArtistRepin.jsonl | 转录·researcher | 2.4MB | 10-16 00:57 | w17 | 列宾 v2 | DONE |
| ArtistGauguin.jsonl | 转录·researcher | 2.2MB | 10-16 00:58 | w17 | 高更 v2（A-56） | DONE |
| HardTurner.jsonl | 转录·researcher | 1.6MB | 10-16 01:08 | w16p2加固 | 透纳 §11 扩写（A-59） | DONE |
| HardQi.jsonl | 转录·researcher | 1.3MB | 10-16 01:08 | w16p2加固 | 齐白石 §11 扩写（A-66） | DONE |
| HardKlimt.jsonl | 转录·researcher | 1.7MB | 10-16 01:09 | w16p2加固 | 克里姆特 §11 扩写 | DONE |
| HardSeurat.jsonl | 转录·researcher | 1.5MB | 10-16 01:10 | w16p2加固 | 修拉 §11 扩写（A-63） | DONE |
| HardHopper.jsonl | 转录·researcher | 1.5MB | 10-16 01:10 | w16p2加固 | 霍珀 §11 扩写（A-64） | DONE |
| HardIto.jsonl | 转录·researcher | 2.1MB | 10-16 01:16 | w16p2加固 | 伊藤若冲 §11 扩写 | DONE |
| HardBada.jsonl | 转录·researcher | 2.0MB | 10-16 01:17 | w16p2加固 | 八大山人 §11 扩写（A-65） | DONE |
| HardGoya.jsonl | 转录·researcher | 2.0MB | 10-16 01:18 | w16p2加固 | 戈雅 §11 补写（A-62，07c42f5） | DONE |
| HardRembrandt.jsonl | 转录·researcher | 2.4MB | 10-16 01:19 | w16p2加固 | 伦勃朗 §11 补写 | DONE |
| ArtistElSalahi.jsonl | 转录·researcher | 2.4MB | 10-16 01:33 | w18 | 萨拉希 v2（A-73） | DONE |
| ArtistHiroshige.jsonl | 转录·researcher | 2.4MB | 10-16 01:33 | w18 | 歌川广重 v2（A-68） | DONE |
| ArtistWuGuanzhong.jsonl | 转录·researcher | 2.5MB | 10-16 01:34 | w18 | 吴冠中 v2（A-74） | DONE |
| IndexMerge2.jsonl | 转录·coder | 2.0MB | 10-16 01:37 | w16系 | 索引二轮并入（A-75） | DONE |
| ArtistNamatjira.jsonl | 转录·researcher | 2.5MB | 10-16 01:43 | w18 | 纳马吉拉 v2（A-72） | DONE |
| ArtistPiero.jsonl | 转录·researcher | 1.9MB | 10-16 01:44 | w18 | 皮耶罗 v2（A-70） | DONE |
| ArtistSargent.jsonl | 转录·researcher | 2.5MB | 10-16 01:45 | w18 | 萨金特 v2（A-69） | DONE |
| ArtistArtemisia.jsonl | 转录·researcher | 3.2MB | 10-16 01:59 | w18 | 阿尔泰米西娅 v2（A-71） | DONE |
| ArtistAivazovsky.jsonl | 转录·researcher | 1.9MB | 10-16 02:02 | w19首轮 | 艾瓦佐夫斯基 v2 | 未完成（宿主重启杀死→-2 重派） |
| ArtistConstable.jsonl | 转录·researcher | 970KB | 10-16 02:02 | w19首轮 | 康斯泰勃尔 v2 | 未完成（→-2） |
| ArtistElGreco.jsonl | 转录·researcher | 1.2MB | 10-16 02:02 | w19首轮 | 埃尔·格列柯 v2 | 未完成（→-2） |
| ArtistFanKuan.jsonl | 转录·researcher | 1.5MB | 10-16 02:02 | w19首轮 | 范宽 v2 | 未完成（→-2） |
| ArtistBruegel.jsonl | 转录·researcher | 1.1MB | 10-16 02:02 | w19首轮 | 勃鲁盖尔 v2 | 未完成（→-2） |
| ArtistHolbein.jsonl | 转录·researcher | 1.1MB | 10-16 02:02 | w19首轮 | 荷尔拜因 v2 | 未完成（→-2） |
| ArtistOkeeffe.jsonl | 转录·researcher | 930KB | 10-16 02:02 | w19首轮 | 欧姬芙 v2 | 未完成（→-2） |
| ArtistPoussin.jsonl | 转录·researcher | 1.1MB | 10-16 02:02 | w19首轮 | 普桑 v2 | 未完成（→-2） |
| ArtistRivera.jsonl | 转录·researcher | 810KB | 10-16 02:02 | w19首轮 | 里维拉 v2 | 未完成（→-2） |
| ArtistSesshu.jsonl | 转录·researcher | 1.2MB | 10-16 02:02 | w19首轮 | 雪舟 v2 | 未完成（→-2） |
| ModuleCards42.jsonl | 转录·coder | 1.8MB | 10-16 02:02 | w16系 | 模块卡 20→42（A-76） | DONE（恰于重启时刻收尾） |

### 1.4 重派与晚批 · 10-16 03:47–04:33（18）

| 文件名 | 类型 | 大小 | mtime | 波次 | 一句话角色 | 状态 |
|---|---|---|---|---|---|---|
| ArtistSesshu-2.jsonl | 转录·researcher | 1.6MB | 10-16 03:48 | w19重派 | 雪舟 v2 续写补全 | DONE |
| ArtistConstable-2.jsonl | 转录·researcher | 2.3MB | 10-16 03:58 | w19重派 | 康斯泰勃尔 v2（A-79） | DONE |
| ArtistHolbein-2.jsonl | 转录·researcher | 2.0MB | 10-16 03:58 | w19重派 | 荷尔拜因 v2（A-83） | DONE |
| ArtistOkeeffe-2.jsonl | 转录·researcher | 2.4MB | 10-16 03:58 | w19重派 | 欧姬芙 v2（A-85） | DONE |
| ArtistOgataKorin.jsonl | 转录·researcher | 2.3MB | 10-16 03:58 | w19期 | 尾形光琳 v2（A-90） | DONE |
| ArtistPoussin-2.jsonl | 转录·researcher | 2.3MB | 10-16 03:58 | w19重派 | 普桑 v2（A-80） | DONE |
| ArtistRivera-2.jsonl | 转录·researcher | 2.0MB | 10-16 03:59 | w19重派 | 里维拉 v2 续跑收口 | DONE |
| ArtistBruegel-2.jsonl | 转录·researcher | 2.6MB | 10-16 04:00 | w19重派 | 勃鲁盖尔 v2（推送纪律回执） | DONE |
| ArtistBlake.jsonl | 转录·researcher | 2.2MB | 10-16 04:01 | w20 | 布莱克 v2（A-91） | DONE |
| ArtistSultanMohammed.jsonl | 转录·researcher | 2.1MB | 10-16 04:01 | w20 | 苏丹·穆罕默德 v2（A-96） | DONE |
| ArtistElGreco-2.jsonl | 转录·researcher | 2.0MB | 10-16 04:03 | w19重派 | 埃尔·格列柯 v2（A-82） | DONE |
| ArtistFanKuan-2.jsonl | 转录·researcher | 2.7MB | 10-16 04:03 | w19重派 | 范宽 v2 | DONE |
| ArtistAivazovsky-2.jsonl | 转录·researcher | 2.4MB | 10-16 04:04 | w19重派 | 艾瓦佐夫斯基 v2 续跑（A-84） | DONE |
| ArtistManet.jsonl | 转录·researcher | 2.3MB | 10-16 04:04 | w20 | 马奈 v2（A-93） | DONE |
| ArtistChardin.jsonl | 转录·researcher | 2.5MB | 10-16 04:06 | w20 | 夏尔丹 v2 | DONE |
| ArtistQiuYing.jsonl | 转录·researcher | 2.7MB | 10-16 04:08 | w20 | 仇英 v2（A-89） | DONE |
| ArtistZhaoMengfu.jsonl | 转录·researcher | 2.3MB | 10-16 04:12 | w20 | 赵孟頫 v2 | DONE |
| ArtistNiZan.jsonl | 转录·researcher | 3.1MB | 10-16 04:33 | w20 | 倪瓒 v2（A-88） | DONE |

### 1.5 收尾批 · 10-16 05:25–06:28（15）

| 文件名 | 类型 | 大小 | mtime | 波次 | 一句话角色 | 状态 |
|---|---|---|---|---|---|---|
| ArtistRockwell.jsonl | 转录·researcher | 2.4MB | 10-16 05:25 | w21 | 洛克威尔 v2（A-106） | DONE |
| ArtistSherGil.jsonl | 转录·researcher | 2.3MB | 10-16 05:31 | w21 | 谢尔吉尔 v2（A-99） | DONE |
| ArtistDeChirico.jsonl | 转录·researcher | 2.3MB | 10-16 05:33 | w21 | 德·基里科 v2（A-105） | DONE |
| ArtistXuBeihong.jsonl | 转录·researcher | 2.6MB | 10-16 05:36 | w21 | 徐悲鸿 v2（A-97） | DONE |
| ArtistHogarth.jsonl | 转录·researcher | 2.1MB | 10-16 05:39 | w21 | 荷加斯 v2（A-103） | DONE |
| ArtistLiKeran.jsonl | 转录·researcher | 2.7MB | 10-16 05:40 | w21 | 李可染 v2（A-98，三 scout 并入） | DONE |
| ArtistChenHongshou.jsonl | 转录·researcher | 3.2MB | 10-16 05:45 | w21 | 陈洪绶 v2（A-101） | DONE |
| ArtistMirSayyidAli.jsonl | 转录·researcher | 2.5MB | 10-16 05:51 | w21 | 米尔·赛义德·阿里 v2 | DONE |
| ArtistTarsila.jsonl | 转录·researcher | 2.4MB | 10-16 05:52 | w21 | 塔西拉 v2（A-100） | DONE |
| ArtistZorn.jsonl | 转录·researcher | 2.8MB | 10-16 06:02 | w20 | 佐恩 v2 全收口（A-95） | DONE |
| ArtistSorolla.jsonl | 转录·researcher | 2.2MB | 10-16 06:04 | w21 | 索罗拉 v2（A-94） | DONE |
| ArtistXuWei.jsonl | 转录·researcher | 2.4MB | 10-16 06:05 | w21 | 徐渭 v2（A-102） | DONE |
| ModuleCards62.jsonl | 转录·coder | 2.3MB | 10-16 06:17 | 收口 | 模块卡 42→62（A-108） | DONE |
| CrossLinkSync.jsonl | 转录·researcher | 1.6MB | 10-16 06:22 | 收口 | 互引同步 10 处（A-109） | DONE |
| IndexMerge3.jsonl | 转录·coder | 2.5MB | 10-16 06:28 | 收口 | 索引三轮合并 35→62 | DONE（commit cea77cb；会话被 SIGHUP 终止） |

## 2 · md 总表（157/157；非空 130 件首行已全采）

> 分类：子代理报告（= 交主脑回执）/ handoff（= 主脑自动交接）/ 空文件 / 片段（工作中间稿）。
> 首行采集：`<file>:1-1:raw` 精确单行法（法见 §5）；已覆盖全部非空 md（130/130）。handoff 12 件均为「## Goal」开头的自动交接模板（49–72 行）。
> 尺寸 = 字节四舍五入；mtime = JST。

| 文件名 | 分类 | 大小 | mtime | 首行（截断） |
|---|---|---|---|---|
| AnimTest01.md | 子代理报告 | 2.2KB | 10-15 17:52 | 交付完成。全部在 `…/anim_test_01/` 内，未动项目其它文件。 |
| AnimTest02.md | 子代理报告 | 2.8KB | 10-15 18:28 | B-17 完成。以下为交付结果。 |
| AnimTest03Blender.md | 子代理报告 | 1.4KB | 10-15 19:46 | STATUS: DONE（恢复句…） |
| AnnotationSweep.md | 子代理报告 | 5.6KB | 10-15 18:06 | 全部完成并逐项验证。以下为交付报告。 |
| ArtistAivazovsky-2.md | 子代理报告 | 3.3KB | 10-16 03:57 | All green. The assignment is complete — writing the final receipt: |
| ArtistAivazovsky.md | 空文件 | 0B | 10-16 02:02 | — |
| ArtistArtemisia.md | 子代理报告 | 3.9KB | 10-16 01:52 | STATUS: DONE（A-71·wave18…） |
| ArtistBadaShanren.md | 子代理报告 | 2.8KB | 10-15 23:36 | All checks pass…回执 |
| ArtistBehzad.md | 子代理报告 | 797B | 10-16 00:27 | All confirmed — stale retry job is moot… |
| ArtistBlake.md | 子代理报告 | 2.7KB | 10-16 03:54 | All done — final receipt: |
| ArtistBosch.md | 子代理报告 | 2.5KB | 10-16 00:19 | 博斯（A-46）四处落盘完成，v2 规格齐全… |
| ArtistBruegel-2.md | 子代理报告 | 1.2KB | 10-16 03:53 | 收到——推送纪律确认，无需任何修正动作： |
| ArtistBruegel.md | 空文件 | 0B | 10-16 02:02 | — |
| ArtistCaravaggio.md | 子代理报告 | 2.8KB | 10-15 16:50 | STATUS: DONE（产物 research/artists/caravaggio.md） |
| ArtistChardin.md | 子代理报告 | 2.1KB | 10-16 03:59 | 全部完成，自测全项通过。交付如下： |
| ArtistChenHongshou.md | 子代理报告 | 2.5KB | 10-16 05:38 | All deliverables are committed and verified. Final receipt: |
| ArtistConstable-2.md | 子代理报告 | 2.7KB | 10-16 03:48 | STATUS: DONE — wave19·康斯泰勃尔（A-79）… |
| ArtistConstable.md | 空文件 | 0B | 10-16 02:02 | — |
| ArtistCrosscheck.md | 子代理报告 | 1.7KB | 10-15 17:22 | STATUS: DONE（交付 research/artists/_crosscheck.md） |
| ArtistDeChirico.md | 子代理报告 | 2.9KB | 10-16 05:27 | 全部完成。以下为回执（LOOP 协议格式）。 |
| ArtistDegas.md | 子代理报告 | 3.6KB | 10-16 00:49 | All checks complete. The assignment is finished — here is the receipt. |
| ArtistDurer.md | 子代理报告 | 2.3KB | 10-15 16:49 | 交付完成：`research/artists/durer.md`（349 行 / 45.6 KB） |
| ArtistElGreco-2.md | 子代理报告 | 2.4KB | 10-16 03:56 | 全部完成。以下为回执（Receipt）： |
| ArtistElGreco.md | 空文件 | 0B | 10-16 02:02 | — |
| ArtistElSalahi.md | 子代理报告 | 2.2KB | 10-16 01:26 | All four deliverables are complete and every self-test passes. Final receipt: |
| ArtistExpansion.md | 子代理报告 | 2.7KB | 10-15 16:17 | **A-09 完成**：`research/artists/expansion.md`（649 行 / 61,944 字节）已落盘… |
| ArtistFanKuan-2.md | 子代理报告 | 1.9KB | 10-16 03:56 | **STATUS: DONE** — wave19·范宽 四处落盘完成… |
| ArtistFanKuan.md | 空文件 | 0B | 10-16 02:02 | — |
| ArtistFriedrich.md | 子代理报告 | 2.4KB | 10-16 00:47 | All checks pass. The assignment is complete — here is the receipt. |
| ArtistGauguin.md | 子代理报告 | 1.7KB | 10-16 00:51 | ✅ **A-56 高更（Gauguin）v2 完成——四处落盘、全部验收项通过。** |
| ArtistGoya.md | 子代理报告 | 3.5KB | 10-15 23:38 | All deliverables verified and complete. Final receipt: |
| ArtistHiroshige.md | 子代理报告 | 3.0KB | 10-16 01:26 | STATUS: DONE |
| ArtistHogarth.md | 子代理报告 | 2.7KB | 10-16 05:32 | 全部完成。以下为 ArtistHogarth（wave21 / A-103）交付回执。 |
| ArtistHolbein-2.md | 子代理报告 | 2.5KB | 10-16 03:50 | 全部完成。最终交付与验收摘要： |
| ArtistHolbein.md | 空文件 | 0B | 10-16 02:02 | — |
| ArtistHopper.md | 子代理报告 | 3.2KB | 10-15 23:38 | All checks green. Everything is complete — here is the receipt. |
| ArtistHuangGongwang.md | 空文件 | 0B | 10-15 23:58 | — |
| ArtistItoJakuchu.md | 空文件 | 0B | 10-15 23:43 | — |
| ArtistKahlo.md | 空文件 | 0B | 10-15 23:58 | — |
| ArtistKandinsky.md | 子代理报告 | 1.8KB | 10-16 00:31 | **STATUS: DONE** |
| ArtistKlimt.md | 子代理报告 | 3.3KB | 10-15 23:27 | All checks pass. The assignment is complete — here is the delivery receipt. |
| ArtistKngwarreye.md | 子代理报告 | 3.2KB | 10-16 00:47 | All four deliverables are complete and verified. Here is the completion receipt. |
| ArtistLiKeran.md | 子代理报告 | 1.4KB | 10-16 05:33 | **A-98 李可染 · 收尾完成（三个 scout 全部并入）** |
| ArtistManet.md | 子代理报告 | 3.2KB | 10-16 03:57 | 全部完成并通过自测。以下为回执（A-93 · wave20 · 马奈 v2）。 |
| ArtistMatisseHokusai.md | 子代理报告 | 3.1KB | 10-15 16:18 | 两份档案已完成并落盘。 |
| ArtistMirSayyidAli.md | 子代理报告 | 1.9KB | 10-16 05:44 | 交付完成，收尾如下（已写好五件交接 `_scratch/mir_sayyid_ali/RESUME.md`） |
| ArtistMucha.md | 空文件 | 0B | 10-15 23:58 | — |
| ArtistMunch.md | 子代理报告 | 1.9KB | 10-16 00:14 | 任务完成。（A-43 回执） |
| ArtistNamatjira.md | 子代理报告 | 2.4KB | 10-16 01:36 | STATUS: DONE |
| ArtistNiZan.md | 子代理报告 | 2.4KB | 10-16 04:26 | **STATUS: DONE（终态）— A-88 倪瓒 v2 四处落盘 100% 完成** |
| ArtistOgataKorin.md | 子代理报告 | 2.3KB | 10-16 03:49 | 任务完成。尾形光琳 v2 全规格四处落盘 + 自测全项通过，已提交 `0a802cd`… |
| ArtistOkeeffe-2.md | 子代理报告 | 3.8KB | 10-16 03:49 | Everything is confirmed and committed. Final state is clean — here is the complete receipt. |
| ArtistOkeeffe.md | 片段 | 103B | 10-16 02:02 | AIC caps at 843px for restricted works; OKM/MoMA give high-res… |
| ArtistPicassoCezanne.md | 子代理报告 | 2.0KB | 10-15 16:22 | STATUS: DONE |
| ArtistPiero.md | 子代理报告 | 2.8KB | 10-16 01:37 | STATUS: DONE |
| ArtistPoussin-2.md | 子代理报告 | 2.7KB | 10-16 03:48 | **A-80 · wave19·普桑 v2 — 完成。四处落盘 + 自测全项通过。** |
| ArtistPoussin.md | 片段 | 53B | 10-16 02:02 | Now writing the corpus file with the verified quotes. |
| ArtistQiBaishi.md | 空文件 | 0B | 10-15 23:14 | — |
| ArtistQiuYing.md | 子代理报告 | 1.9KB | 10-16 04:01 | STATUS: DONE — 仇英档案（A-89）四处落盘全交（commit `57cba1d`，未 push）… |
| ArtistRaviVarma.md | 子代理报告 | 4.0KB | 10-16 00:35 | STATUS: DONE |
| ArtistRembrandt.md | 空文件 | 0B | 10-15 23:14 | — |
| ArtistRenaissance.md | 子代理报告 | 1.9KB | 10-15 16:22 | STATUS: DONE |
| ArtistRepin.md | 子代理报告 | 2.3KB | 10-16 00:50 | All checks pass and numbers are consistent. The assignment is complete — here is the final report. |
| ArtistRivera-2.md | 子代理报告 | 3.1KB | 10-16 03:44 | All checks converged and consistent. The assignment is complete — here is the final receipt: |
| ArtistRivera.md | 空文件 | 0B | 10-16 02:02 | — |
| ArtistRockwell.md | 子代理报告 | 2.1KB | 10-16 05:18 | All work is complete and verified. Final wrap-up: |
| ArtistSargent.md | 子代理报告 | 3.1KB | 10-16 01:38 | **STATUS: DONE** |
| ArtistSesshu-2.md | 子代理报告 | 2.6KB | 10-16 03:41 | ✅ 全部完成，按 Contract 自测全项通过。 |
| ArtistSesshu.md | 片段 | 49B | 10-16 02:02 | All 18 images verified correct. Now the MANIFEST: |
| ArtistSeurat.md | 子代理报告 | 3.6KB | 10-15 23:37 | All checks complete. Everything is on disk. Here is the delivery receipt: |
| ArtistSherGil.md | 子代理报告 | 2.0KB | 10-16 05:24 | 完成。A-99（wave21·谢尔吉尔）全量交付，回执如下： |
| ArtistSorolla.md | 子代理报告 | 2.0KB | 10-16 05:57 | **A-94 索罗拉（Sorolla）交付完成** — 四处落盘 + 全项自测通过 |
| ArtistSultanMohammed.md | 子代理报告 | 2.5KB | 10-16 03:54 | **A-96 苏丹·穆罕默德（wave20）v2 全规格完成…** 未 push（`c6dd46b` 待 sweep）。 |
| ArtistTarsila.md | 子代理报告 | 2.4KB | 10-16 05:45 | 交付完成。收据如下： |
| ArtistTurner.md | 空文件 | 0B | 10-15 23:14 | — |
| ArtistVanEyck.md | 子代理报告 | 1.9KB | 10-16 00:48 | All four places are final and verified. The assignment is complete — here's the delivery report. |
| ArtistVanGoghMonet.md | 子代理报告 | 2.2KB | 10-15 16:21 | 两份档案已完成并通过自审。最终报告： |
| ArtistVelazquez.md | 子代理报告 | 2.2KB | 10-16 00:24 | 任务完成。四处落盘、v2 规格齐全、分工条款写死、自审四段已全部落盘并复核通过。 |
| ArtistVermeer.md | 子代理报告 | 2.6KB | 10-15 16:49 | **STATUS: DONE**（A-16 · `research/artists/vermeer.md`，382 行 / 31 KB） |
| ArtistWuGuanzhong.md | 子代理报告 | 2.6KB | 10-16 01:27 | All four deliverables are complete and verified. Final state: |
| ArtistXuBeihong.md | 子代理报告 | 3.1KB | 10-16 05:29 | **A-97 徐悲鸿（wave21）交付完成 — 四处落盘，自测全项通过，已提交（`1f3291b`）。** |
| ArtistXuWei.md | 子代理报告 | 2.8KB | 10-16 05:58 | **A-102 · wave21·徐渭（ArtistXuWei）— 交付回执** |
| ArtistZhaoMengfu.md | 子代理报告 | 2.7KB | 10-16 04:05 | All four paths are in place and committed. Final receipt: |
| ArtistZorn.md | 子代理报告 | 1.6KB | 10-16 05:55 | **最终回执 — wave20 · 佐恩（A-95）· 全部收口** |
| AuditJA.md | 子代理报告 | 1.9KB | 10-15 22:53 | 完了しました。監査レポートを `docs/notes/i18n-audit-ja.md` として落盤しました… |
| AuditZH.md | 子代理报告 | 1.6KB | 10-15 22:50 | 审计完成，`docs/notes/i18n-audit-zh.md` 已落盘（唯一新增文件，未改动任何被审文件）。 |
| AuthorTutorial.md | 子代理报告 | 2.2KB | 10-15 17:38 | B-15 完成，产物落盘并全部机械核验通过。 |
| AutoTriggerProbe.md | 子代理报告 | 1.4KB | 10-15 21:43 | File complete and verified. Final result: |
| BioCaravaggio.md | 空文件 | 0B | 10-15 23:58 | — |
| BioCezanne.md | 空文件 | 0B | 10-15 23:43 | — |
| BioDaVinci.md | 空文件 | 0B | 10-15 23:43 | — |
| BioDurer.md | 空文件 | 0B | 10-15 23:43 | — |
| BioHokusai.md | 空文件 | 0B | 10-15 23:43 | — |
| BioMatisse.md | 空文件 | 0B | 10-15 23:43 | — |
| BioMichelangelo.md | 空文件 | 0B | 10-15 23:43 | — |
| BioMonet.md | 空文件 | 0B | 10-15 23:43 | — |
| BioPicasso.md | 空文件 | 0B | 10-15 23:58 | — |
| BioVanGogh.md | 空文件 | 0B | 10-15 23:43 | — |
| BioVermeer.md | 空文件 | 0B | 10-15 23:43 | — |
| BlenderScript.md | 子代理报告 | 2.5KB | 10-15 16:19 | STATUS: DONE |
| BlindGREEN.md | 子代理报告 | 2.1KB | 10-15 21:31 | 已完成。说明一下过程与产物： |
| BlindRED.md | 子代理报告 | 655B | 10-15 21:23 | 已完成，`research/skill/tests/red_transcript.md` 已落盘（目录为新建）… |
| ComboTest.md | 子代理报告 | 2.4KB | 10-15 20:06 | All deliverables are complete and verified. Here's the final receipt: |
| ConflictsList.md | 子代理报告 | 2.5KB | 10-15 17:24 | **B-12 交付完成：`research/agent-art/conflicts.md`（415 行 / 56,390 bytes，无占位符）。** |
| ConsultWalkthrough.md | 子代理报告 | 2.9KB | 10-15 22:06 | All checks pass and write scope stayed clean. The walkthrough is complete. Final report: |
| CrossLinkSync.md | 子代理报告 | 4.0KB | 10-16 06:15 | A-109 交叉互引同步 —— 全部 10 处小修完成，回执如下。 |
| DossierReview.md | 子代理报告 | 1.7KB | 10-15 16:49 | STATUS: DONE |
| ESeriesT1.md | 子代理报告 | 1.8KB | 10-15 19:18 | All done and verified. Final state of the experiment: |
| EStyleSep.md | 子代理报告 | 2.6KB | 10-15 19:47 | All checks pass. E-02 is complete. Final result: |
| handoff-2026-10-15T10-40-00-997Z.md | handoff | 10.0KB | 10-15 19:40 | ## Goal（自动交接模板） |
| handoff-2026-10-15T10-42-32-003Z.md | handoff | 9.1KB | 10-15 19:42 | ## Goal（自动交接模板） |
| handoff-2026-10-15T10-47-14-540Z.md | handoff | 9.4KB | 10-15 19:47 | ## Goal（自动交接模板） |
| handoff-2026-10-15T11-06-38-802Z.md | handoff | 8.6KB | 10-15 20:06 | ## Goal（自动交接模板） |
| handoff-2026-10-15T15-19-39-781Z.md | handoff | 10.1KB | 10-16 00:20 | ## Goal（自动交接模板） |
| handoff-2026-10-15T15-31-59-563Z.md | handoff | 9.1KB | 10-16 00:32 | ## Goal（自动交接模板） |
| handoff-2026-10-15T15-41-48-393Z.md | handoff | 7.2KB | 10-16 00:42 | ## Goal（自动交接模板） |
| handoff-2026-10-15T18-52-57-205Z.md | handoff | 9.2KB | 10-16 03:53 | ## Goal（自动交接模板） |
| handoff-2026-10-15T19-24-48-017Z.md | handoff | 7.7KB | 10-16 04:25 | ## Goal（自动交接模板） |
| handoff-2026-10-15T20-34-49-588Z.md | handoff | 9.6KB | 10-16 05:35 | ## Goal（自动交接模板） |
| handoff-2026-10-15T20-42-26-030Z.md | handoff | 9.2KB | 10-16 05:42 | ## Goal（自动交接模板） |
| handoff-2026-10-15T21-22-37-592Z.md | handoff | 8.8KB | 10-16 06:22 | ## Goal（自动交接模板） |
| HardBada.md | 子代理报告 | 2.6KB | 10-16 01:10 | STATUS: DONE |
| HardGoya.md | 子代理报告 | 1.7KB | 10-16 01:11 | STATUS: DONE |
| HardHopper.md | 子代理报告 | 2.9KB | 10-16 01:03 | All verifications pass. The work is complete — final receipt below. |
| HardIto.md | 子代理报告 | 3.0KB | 10-16 01:09 | All checks complete. Final report: |
| HardKlimt.md | 子代理报告 | 2.8KB | 10-16 01:02 | All acceptance criteria verified. The task is complete — final report follows. |
| HardQi.md | 子代理报告 | 2.6KB | 10-16 01:01 | STATUS: DONE |
| HardRembrandt.md | 子代理报告 | 2.8KB | 10-16 01:12 | All work is complete and verified. The GOALS.md change is the main brain's… |
| HardSeurat.md | 子代理报告 | 2.5KB | 10-16 01:03 | Work complete and verified. Final receipt: |
| HardTurner.md | 子代理报告 | 2.5KB | 10-16 01:01 | STATUS: DONE |
| HtmlFrameRender.md | 子代理报告 | 2.4KB | 10-15 16:17 | STATUS: DONE |
| I18nJA.md | 子代理报告 | 6.1KB | 10-15 22:39 | All checks complete and cross-links verified. The assignment is done — here is the receipt. |
| I18nZH.md | 子代理报告 | 4.7KB | 10-15 22:38 | All five files are final and verified. Here is the completion receipt: |
| ImageChannelProbe.md | 子代理报告 | 2.3KB | 10-15 18:51 | All done. Final state verified: `image_channel.md` = 396 lines / 32.7KB… |
| ImageLibrary.md | 子代理报告 | 2.9KB | 10-15 17:55 | STATUS: DONE |
| IndexMerge.md | 子代理报告 | 9.8KB | 10-16 00:42 | Everything is synced and verified. The assignment is complete — here is the final receipt: |
| IndexMerge2.md | 子代理报告 | 13.3KB | 10-16 01:30 | IndexMerge2 完成：三表已并入 wave15×8 + wave17×7 并全量重算 35 行… |
| IndexMerge3.md | 空文件 | 0B | 10-16 06:28 | — |
| MgStyles15Compare.md | 子代理报告 | 2.4KB | 10-15 16:50 | STATUS: DONE |
| MichelangeloV2.md | 子代理报告 | 2.8KB | 10-15 20:00 | All checks green. The task is complete — here's the final state of every deliverable… |
| ModuleCards20.md | 子代理报告 | 9.4KB | 10-16 00:32 | STATUS: DONE |
| ModuleCards42.md | 子代理报告 | 2.6KB | 10-16 02:02 | STATUS: DONE |
| ModuleCards62.md | 子代理报告 | 7.4KB | 10-16 06:10 | 回执如下（原样输出）： |
| ModuleLibrary.md | 子代理报告 | 7.2KB | 10-15 18:39 | All validation passes. The assignment is complete… |
| PipelineHandbook.md | 子代理报告 | 2.7KB | 10-15 16:57 | **DONE — 产物已落盘**：`…/mg-styles-15_handbook.md`（365 行，44.9 KB）。 |
| PromptCorpusHunt.md | 子代理报告 | 2.5KB | 10-15 16:20 | B-04 完成，两份产物已落盘并机械验证。 |
| RefsMapping.md | 子代理报告 | 2.2KB | 10-15 18:43 | 全部完成，收尾核对通过。最终报告： |
| RepoStandards.md | 子代理报告 | 2.3KB | 10-15 22:25 | **`repo_standards.md` 已落盘（289 行 / 34.1KB），验收五项全覆盖。** |
| RosterBuilder.md | 空文件 | 0B | 10-15 23:14 | — |
| SkillBuild.md | 子代理报告 | 2.1KB | 10-15 21:18 | 一切就绪，最终清点无遗漏。任务完成。 |
| SkillEcosystem.md | 子代理报告 | 2.6KB | 10-15 21:01 | All checks pass. The assignment is complete — final receipt: |
| SkillSpec.md | 子代理报告 | 743B | 10-15 21:07 | **收口更新**（两线 R1 关闭）： |
| StyleCardTemplates.md | 子代理报告 | 3.5KB | 10-15 16:58 | 三件产物已落盘并通过验收对照；另推翻 workflow §4 一条拼图命令… |
| TemplatesV03.md | 子代理报告 | 2.5KB | 10-15 18:39 | All checks pass. Both files are complete and verified. Final state: |
| TransferGuide.md | 子代理报告 | 1.8KB | 10-15 18:04 | STATUS: DONE |
| VideoShotcraft.md | 子代理报告 | 1.8KB | 10-15 17:29 | B-14 完成。产物：`…/video_shotcraft.md`（31.5KB / 307 行…） |
| VideoShotcraftDeep.md | 子代理报告 | 2.5KB | 10-15 18:06 | **STATUS: DONE** |

## 3 · 四个子目录内容

| 子目录 | 文件 | 大小(≈) | 角色（一句话） |
|---|---|---|---|
| **ArtistLiKeran/**（6 件；李可染单的三条并行 scout 转录） | ArtistLiKeran.NamocXuzhou.jsonl | 2.0MB | 南博/徐州线素材 scout 转录 |
| | ArtistLiKeran.QuotesLiKeran.jsonl | 2.4MB | 李可染语录 scout 转录 |
| | ArtistLiKeran.TechniqueLit.jsonl | 2.6MB | 技法文献 scout 转录 |
| | ArtistLiKeran.NamocXuzhou.md | 2.8KB | 对应回执 |
| | ArtistLiKeran.QuotesLiKeran.md | 3.3KB | 对应回执 |
| | ArtistLiKeran.TechniqueLit.md | 2.6KB | 对应回执 |
| **ConsultWalkthrough/**（2 件；技能演练） | ConsultWalkthrough.W01Reviewer.jsonl | 319KB | W01 评审员演练转录 |
| | ConsultWalkthrough.W01Reviewer.md | 11.1KB | 演练报告 |
| **local/**（5 件；李可染 scout 的原始材料落盘） | namoc_xuzhou.md | 19.6KB | 南博/徐州资料整理 |
| | quotes_raw.md | 32.4KB | 语录原文 |
| | quotes_raw_notes.md | 1.1KB | 语录批注 |
| | technique_lit.md | 27.3KB | 技法文献整理 |
| | li_keran_probe.md | 34B | 探针小注 |
| **url-search/**（17 件；抓取缓存，来源网页/PDF） | dok41aq0w7th.html | 52.8KB | 抓取件（HTML） |
| | 2k6decy23ccee.txt / 2ncjgme79gszd.txt / 29rd68z4ply43.txt | 153/40/100KB | 抓取件（文本） |
| | 3uf2odt7fsbtl.txt / 33qslww0j5xoy.txt / 3lps9llah7m0j.txt | 176/47/179KB | 抓取件（文本） |
| | 154yfsj2kzuad.pdf | 137KB | 抓取件（PDF） |
| | 271nvjamue1zj.php | 62KB | 抓取件（PHP 页） |
| | 1ux8rpufjoqah.txt / lmlq99to1jli.txt / 36xkny9u4dyw3.txt | 73/149/228KB | 抓取件（文本） |
| | 3h3x0utofpcka.txt / 11fm588hz2qdq.txt / 3fxhxe6lyhswu.txt / 2xf8lduwc73zg.txt | 20/217/97/239KB | 抓取件（文本） |
| | 1d2zoqpqmjt4t.pdf | 0B | **空抓取（失败残留）** |

## 4 · 异常清单（终版）

1. **空文件（0B）×27（全为 .md）**：ArtistAivazovsky / ArtistBruegel / ArtistConstable / ArtistElGreco / ArtistFanKuan / ArtistHolbein / ArtistHuangGongwang / ArtistItoJakuchu / ArtistKahlo / ArtistMucha / ArtistQiBaishi / ArtistRembrandt / ArtistRivera / ArtistTurner / BioCaravaggio / BioCezanne / BioDaVinci / BioDurer / BioHokusai / BioMatisse / BioMichelangelo / BioMonet / BioPicasso / BioVanGogh / BioVermeer / IndexMerge3 / RosterBuilder（+ url-search/1d2zoqpqmjt4t.pdf）。
2. **片段/中间稿 ×3**：ArtistSesshu.md（49B）、ArtistPoussin.md（53B）、ArtistOkeeffe.md（103B）——均为 wave19 首轮被杀时的半截稿。
3. **>5MB：无**。最大件：ArtistArtemisia.jsonl 3.4MB；次之 ChenHongshou 3.4MB、NiZan 3.2MB、AnimTest03Blender 3.1MB。
4. **疑似重复：无逐字节同件**。同名对（X / X-2，共 10 对：Aivazovsky、Bruegel、Constable、ElGreco、FanKuan、Holbein、Okeeffe、Poussin、Rivera、Sesshu）= wave19 首轮被杀后的重派关系；BioX 与 ArtistX 为不同波次件。
5. **同刻批量死亡**：10 个 wave19 首轮 jsonl + ModuleCards42.jsonl 共享 mtime `1792083711`（10-16 02:01:51）——宿主重启时统一落盘时刻；IndexMerge3 止于 06:28:31（SIGHUP）。
6. **md 首行缺口：已补齐（130/130 非空全采）**——v1.0 遗留 ~75 件，2026-10-16 收工轮以 `<file>:1-1:raw` 精确单行法 7 次批量调用补全；12 件 handoff 均为「## Goal」开头的自动交接模板（49–72 行）。
7. **子目录尺寸为浏览器显示值（≈）**，非精确字节。

## 5 · 方法与复跑

- **提取法（单文件）**：`read "<S-main>/<X>.jsonl?q=[., inputs] as $a | {u: (…首条用户…), ag: (…agent…), t: (…末3条工具…), a: (…末条assistant…), x: (…exit…), e: (…error…)}&limit=1"`；多文件用 `;` 拼接，**首段须无 `?`**（用 md `:1` 当占位），一次最多 11 段。
- **md 首行（精确单行）**：`read "<file>:1-1:raw;…"`（≤11 段/次；**区间形式 `1-1` 才精确**——单值 `:raw:1`/`:1:raw` 会返回整段）。旧法 `:1` / grep `\A` 会带 ~20 行。
- **目录清单**：Chrome 打开 `file://` 目录页（精确字节+epoch 存 `_sc2_listing.json`）。
- **对账**：2420 = 145 jsonl + 157 md + 2114 日志 + 4 目录；jsonl 145/145 全部取到 {u,ag,t,a,x,e}；md 157/157 分类，27 空、3 片段、12 handoff、115 报告。

## 6 · 状态与交接

- **状态：COMPLETE（v1.1）**。验收对照：全量表 ✓（jsonl 145 + md 157 + 子目录 17 文件）、异常清单 ✓、计数对账 ✓、md 首行 130/130 ✓。
- 过程文件（本报告为最终交付）：`_sc2_listing.json`（精确清单）、`_sc2_rows_b56/b78/b910.md`（分批中间行，已并入本表）。建议主脑收集后可将过程文件归档或删除。
- 残余精度项（不影响验收）：① handoff 12 件仅采首行/未读内容；② 子目录尺寸为近似值；③ 波次列为推断值（时间窗+文件名模式）。
- 建议后续：把本目录纳入 archaeology 报告集索引（与 02-digest / 09-session-index 并列）；如需对特定件深挖（如 handoff 或 IndexMerge 系），按 §5 单文件模板直取。
