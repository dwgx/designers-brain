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
| A-27 | done | wave13·齐白石：412 行 v2 档案（§11 生平 + §12 临摹 9 件）+ 语料 25 条 + 图库 11 张公开（4 件 URAA 从严移入 `_private/`）+ 私有 2 件；分工 vs 马蒂斯/八大写死（3 互斥轴）；引文抽查 5/5 | `knowledge/domains/painters/dossiers/qi_baishi.md` | ArtistQiBaishi（wave13） |
| A-28 | done | wave13·伊藤若冲：447 行 v2 档案（§11 生平 + §12 临摹 9 件）+ 语料 24 条 + 图库 18 张（ColBase/Commons/Met）+ 私有补遗；分工 vs 北斋/克里姆特写死；自检全过 | `knowledge/domains/painters/dossiers/ito_jakuchu.md` | ArtistItoJakuchu（wave13） |
| A-29 | done | 名册：**59 位**候选（15 文化区；49 新增）+ wave 批次建议（8/7/7）；验收：349 行 + 机械检查全 PASS（候选 59 / §1=10 / §2=49 / 交集 ∅） | `knowledge/domains/painters/program/roster.md` | RosterBuilder（wave13） |
| A-30 | open | 学习产物：每大师「学习路径卡」+ 总学习路线（Owner 已批；roster 后启动） | `knowledge/domains/painters/program/learning/` | 主脑 |
| A-31 | done | 加固·达芬奇：§11（2688 字 + 39 行年表 + 27 来源）+ §12（9 件）；语料 16→22 条；验收：`_extract.py --check` 33/33 + URL 抽检 12/12 | `knowledge/domains/painters/dossiers/da_vinci.md` | BioDaVinci（wave14） |
| A-32 | done | 加固·米开朗基罗：§11（2816 字 + 35 行年表 + 14 来源）+ §12（8 件）；语料 +7 → 22 条；§10/语料缺口注 3 处已更新（Fattucci 信已找到）；「1509 揭幕」旧说 OVERTURNED；验收：`_extract.py --check` 33/33 + 引文 7/7 | `knowledge/domains/painters/dossiers/michelangelo.md` | BioMichelangelo（wave14） |
| A-33 | done | 加固·梵高：§11（2561 字 + 24 行年表 + 18 来源；16 条引文 byte-exact 核验）+ §12（10 件）；语料 20→36 条；「903 封」旧 [UNVERIFIED] 收口；验收：`_extract` 33/33 + skill selfcheck PASS | `knowledge/domains/painters/dossiers/van_gogh.md` | BioVanGogh（wave14） |
| A-34 | done | 加固·莫奈：§11（2108 字 + 42 行年表 + 14 新来源）+ §12（9 件）；语料 17→29 条；验收：`_extract.py --check` 33/33 + 序号连续 | `knowledge/domains/painters/dossiers/monet.md` | BioMonet（wave14） |
| A-35 | done | 加固·毕加索：§11（2169 字 + 51 行年表 + 19 来源 + 引语分级注）+ §12（10 件）；语料 16→24 条（含 Gilot 降级警示）；验收：check_w14.py ALL PASS + 引文 7/7（工自提交 e62e2ee） | `knowledge/domains/painters/dossiers/picasso.md` | BioPicasso（wave14） |
| A-36 | done | 加固·塞尚：§11（2297 字 + 31 行年表 + 16 来源；「绝交信」旧说 OVERTURNED）+ §12（9 件）；语料 17→24 条；验收：`_extract.py --check` 33/33 | `knowledge/domains/painters/dossiers/cezanne.md` | BioCezanne（wave14） |
| A-37 | done | 加固·马蒂斯：§11（2643 字 + 54 行年表 + 17 来源）+ §12（10 件）；语料 13→24 条；验收：`_extract.py --check` 33/33 + 引文抽查 5/5 | `knowledge/domains/painters/dossiers/matisse.md` | BioMatisse（wave14） |
| A-38 | done | 加固·北斋：§11（2080 字 + 34 行年表 + 16 来源）+ §12（10 件）；语料 +7 → 19 条；验收：`_extract.py --check` 33/33 + git diff 仅 2 文件 | `knowledge/domains/painters/dossiers/hokusai.md` | BioHokusai（wave14） |
| A-39 | done | 加固·卡拉瓦乔：§11（2444 字 + 44 行年表 + 19 来源；「2007 年书信」误传已核正）+ §12（9 件）；语料新建 22 条；验收：`_extract.py --check` 33/33 | `knowledge/domains/painters/dossiers/caravaggio.md` | BioCaravaggio（wave14） |
| A-40 | done | 加固·维米尔：§11（2578 字 + 39 行年表 + 14 来源 + 未找到 7 条）+ §12（10 件）；语料新建 22 条；验收：`_extract.py --check` 33/33 + git diff 纯插入 0 删除 | `knowledge/domains/painters/dossiers/vermeer.md` | BioVermeer（wave14） |
| A-41 | done | 加固·丢勒：§11（2426 字 + 25 行年表 + 12 来源）+ §12（10 件）；语料新建 27 条（德文原文+英译+中译）；验收：`_extract.py --check` 33/33 | `knowledge/domains/painters/dossiers/durer.md` | BioDurer（wave14） |
| A-50 | done | 模块卡扩展 11→**20 张**（9 新画家入 ARTISTS + 生成 + README/domains.yaml 同步）；验收：`--check` **60/60** · skill `_selfcheck` PASS（domains 20/20）· 旧 11 卡零改动（sha256 全等）· `--write` 幂等 | `knowledge/domains/painters/modules/` | ModuleCards20（wave16） |
| A-51 | done | 索引合并（wave16 口径 20 位）：`_corpus/INDEX.md` 20 行/455 条 · `_images/manifest.md` 20 位（公开 104 张 + 私有例外 32 张）· `_index.md` 20 行；全表核验 PASS（重复 0、过时 21+ 处全修、缺失 26 处全补）；wave15/17 位次随各自收口另并 | `knowledge/domains/painters/dossiers/` | IndexMerge（wave16） |
| A-52 | done | wave17·弗里德里希：491 行 v2 档案（§11 2242 字 + 43 行 + 14 来源；§12 10 件）+ 语料 31 条 + 图库 12 张全 PD + 私有 6 件；分工 vs 透纳/康斯泰勃尔写死（各 4 判据）；引文 19/19 | `knowledge/domains/painters/dossiers/friedrich.md` | ArtistFriedrich（wave17） |
| A-53 | done | wave17·列宾：500 行 v2 档案（§11 ~2400 字 + 56 行 + 来源 ≥10；§12 9 件）+ 语料 23 条 + 图库 10 张全 PD + 私有 3+3 件（Стасов 通信集 OCR）；分工 vs 戈雅/米开朗基罗/伦勃朗写死；1 条 OVERTURNED（信日期讹误核正） | `knowledge/domains/painters/dossiers/repin.md` | ArtistRepin（wave17） |
| A-54 | done | wave17·拉维·瓦尔马：481 行 v2 档案（§11 2057 字 + 32 行 + 25 来源；§12 10 件）+ 语料 30 条 + 图库 17 张全 PD + 私有论文 2 件；分工 vs 欧洲学院派/谢尔吉尔写死（§3.7/§3.8）；系统首个印度大师 | `knowledge/domains/painters/dossiers/ravi_varma.md` | ArtistRaviVarma（wave17） |
| A-55 | done | wave17·德加：503 行 v2 档案（§11 2237 字 + 38 行 + 17 来源；§12 10 件）+ 语料 36 条 + 图库 13 张（Met CC0/奥赛/NGL）+ 私有 12 件；分工 vs 莫奈/修拉写死（各 4 轴 + 70/30 纪律）；引文原书级核验（Moore/Vollard 全文） | `knowledge/domains/painters/dossiers/degas.md` | ArtistDegas（wave17） |
| A-56 | done | wave17·高更：504 行 v2 档案（§11 2020 字 + 35 行 + 16 来源；§12 10 件）+ 语料 33 条（Noa Noa 法文版底本）+ 图库 20 张全 PD + 私有论文 2 件；分工 vs 马蒂斯/修拉/梵高写死（各判据 + 70/30）；1 条 OVERTURNED（信日期 1885→1888） | `knowledge/domains/painters/dossiers/gauguin.md` | ArtistGauguin（wave17） |
| A-57 | done | wave17·凡·艾克：483 行 v2 档案（§11 2020 字 + 37 行 + 12 来源；§12 10 件）+ 语料 20 条（题刻逐字转录）+ 图库 17 张 PD/CC0 + 私有 8 件；分工 vs 维米尔第一条款写死（4 判据对齐 vermeer.md）；1 条 OVERTURNED（「发明油画」→「定型者」） | `knowledge/domains/painters/dossiers/van_eyck.md` | ArtistVanEyck（wave17） |
| A-58 | done | wave17·恩格瓦雷：481 行 v2 档案（§11 2574 字 + 33 行 + 15 来源；§12 10 件）+ 语料 18 条 + 14 张图**全在 `_private/`**（公开侧零图；原住民伦理护栏 + ICIP 参考）；分工 vs 修拉写死（符号/大地 vs 光学混合） | `knowledge/domains/painters/dossiers/kngwarreye.md` | ArtistKngwarreye（wave17） |
| A-59 | done | 加固pass2·透纳：新增 §11（11.1 **2411 字** + 年表 40 行 + 来源 13 条）+ §12（10 件）；纯插入 +134/0；回归 60/60 | `knowledge/domains/painters/dossiers/turner.md` | HardTurner（wave16p2） |
| A-60 | done | 加固pass2·伦勃朗：新增 §11（11.1 **2977 字** + 年表 47 行 + 来源 28 条 + 11.4 口径注）+ §12（10 件）；纯插入 +180/0；回归 60/60；婚期两历并记等口径修正入 11.4 | `knowledge/domains/painters/dossiers/rembrandt.md` | HardRembrandt（wave16p2） |
| A-61 | done | 加固pass2·克里姆特：新增 §11（11.1 **2278 字** + 年表 40 行 + 来源 12 条）+ §12（10 件）；纯插入 +138/0；回归 60/60 | `knowledge/domains/painters/dossiers/klimt.md` | HardKlimt（wave16p2） |
| A-62 | done | 加固pass2·戈雅：§11.1 406→**2380 字**（12 段；子节归一 B.x→11.x 零残留；§11.3 补至 12 条目）；回归 60/60 | `knowledge/domains/painters/dossiers/goya.md` | HardGoya（wave16p2） |
| A-63 | done | 加固pass2·修拉：§11.1 450→**2488 字**（8 段；子节归一）；§C→§12 归一 + §B/§C 引用清理（0 残留）；回归 60/60 | `knowledge/domains/painters/dossiers/seurat.md` | HardSeurat（wave16p2） |
| A-64 | done | 加固pass2·霍珀：§11.1 205→**3017 字**（8 段；含 Whitney/AAA 档案 + Jo 日记线索；子节归一）；§12 9 件核对一致；回归 60/60 | `knowledge/domains/painters/dossiers/hopper.md` | HardHopper（wave16p2） |
| A-65 | done | 加固pass2·八大山人：§11.1 304→**2869 字**（9 段；含青云谱公案考辨/花押考释）；§0–§10/§12 字节比对零改动；回归 60/60 | `knowledge/domains/painters/dossiers/bada_shanren.md` | HardBada（wave16p2） |
| A-66 | done | 加固pass2·齐白石：§11.1 308→**2954 字**（8 段详述；子节归一 11.1/11.2/11.3）；§11 外零改动（逐字节核）；回归 60/60 | `knowledge/domains/painters/dossiers/qi_baishi.md` | HardQi（wave16p2） |
| A-67 | done | 加固pass2·伊藤若冲：§11.1 760→**2208 字**（六段；来源 13 条；子节归一）；《藤花亭画谱》查无→改用『藤景和画記』等实证材料并留档；回归 60/60 | `knowledge/domains/painters/dossiers/ito_jakuchu.md` | HardIto（wave16p2） |
| A-68 | done | wave18·广重：536 行 v2 档案（§11 2045 字 + 41 行 + 14 来源；§12 10 件）+ 语料 24 条 + 图库 18 张 PD/CC0（Met 12 CC0）+ 私有 10 件；分工 vs 北斋/贝赫扎德写死（G13 系列叙事清账）；引文 25/25 | `knowledge/domains/painters/dossiers/hiroshige.md` | ArtistHiroshige（wave18） |
| A-69 | done | wave18·萨金特：544 行 v2 档案（§11 2244 字 + 51 行 + 17 来源；§12 10 件）+ 语料 30 条（Charteris 1927 全文 OCR）+ 图库 14 张全 PD/CC0 + 私有 14 件；分工 vs 马奈/委拉斯开兹写死（vs 佐恩预写待对齐）；contact sheet 抓出 2 误取件已替换 | `knowledge/domains/painters/dossiers/sargent.md` | ArtistSargent（wave18） |
| A-70 | done | wave18·皮耶罗：500 行 v2 档案（§11 2206 字 + 46 行 + 11 来源；§12 10 件）+ 语料 24 条（《De prospectiva pingendi》中古意大利语原文）+ 图库 17 张（14 PD + 3 CC BY-SA）+ 私有 3 件；分工 vs 达芬奇/塞尚写死；2 条 OVERTURNED（Vasari 旧说） | `knowledge/domains/painters/dossiers/piero_della_francesca.md` | ArtistPiero（wave18） |
| A-71 | done | wave18·阿尔泰米西娅：517 行 v2 档案（§11 2028 字 + 47 行 + 12 来源；§12 10 件）+ 语料 29 条（庭审记录/书信；含 1653 戏谑墓志铭误传源头）+ 图库 16 张全 PD + 私有 5 件；分工 vs 卡拉瓦乔写死（4 判据 + 边界注 ≥2 轴）；引文 25/25 | `knowledge/domains/painters/dossiers/artemisia_gentileschi.md` | ArtistArtemisia（wave18） |
| A-72 | done | wave18·纳马吉拉：511 行 v2 档案（§11 2041 字 + 28 行 + 15 来源；§12 10 件）+ 语料 22 条 + 31 张图**全在 `_private/`**（公开侧零图；原住民伦理护栏 + 2029 版权警示）；分工 vs 康斯泰勃尔/透纳写死 | `knowledge/domains/painters/dossiers/namatjira.md` | ArtistNamatjira（wave18） |
| A-73 | done | wave18·萨拉希：544 行 v2 档案（§11 2147 字 + 41 行 + 16 来源；§12 10 件）+ 语料 44 条 + 22 张图**全在 `_private/`**（公开侧零图）；分工 vs 康定斯基/贝赫扎德写死（对侧口径互查一致） | `knowledge/domains/painters/dossiers/el_salahi.md` | ArtistElSalahi（wave18） |
| A-74 | done | wave18·吴冠中：500 行 v2 档案（§11 2052 字 + 47 行 + 17 来源；§12 10 件）+ 语料 40 条 + 25 张图**全在 `_private/`**（公开侧零图；版权护栏入 §8.1）；分工 vs 康定斯基/八大山人/黄公望写死（抽象线中文落点，与 kandinsky.md 互洽） | `knowledge/domains/painters/dossiers/wu_guanzhong.md` | ArtistWuGuanzhong（wave18） |
| A-75 | done | 索引合并二轮：三表并入 wave15/17（35 位/844 条；manifest 公开 273 张 + 私有例外 126 张；_index 35 行含 pass2 九行重算）；核验 **PASS 140 / FAIL 0**；两处口径决定留档（mucha 12/5、kandinsky 私有 11） | `knowledge/domains/painters/dossiers/` | IndexMerge2（wave16） |
| A-76 | done | 模块卡 20→**42 张**：22 位入 ARTISTS + 生成 + README/SKILL/domains.yaml 同步；验收：`--check` **126/126** · skill `_selfcheck` PASS · 旧 20 卡零改动（sha256 全等）· `--write` 幂等 | `knowledge/domains/painters/modules/` | ModuleCards42（wave16） |
| A-87 | running | wave20·赵孟頫（Zhao Mengfu）v2（书画同源） | `knowledge/domains/painters/dossiers/zhao_mengfu.md` | ArtistZhaoMengfu（wave20） |
| A-88 | running | wave20·倪瓒（Ni Zan）v2（一河两岸/极简） | `knowledge/domains/painters/dossiers/ni_zan.md` | ArtistNiZan（wave20） |
| A-89 | running | wave20·仇英（Qiu Ying）v2（工笔重彩） | `knowledge/domains/painters/dossiers/qiu_ying.md` | ArtistQiuYing（wave20） |
| A-90 | done | wave20·尾形光琳：529 行 v2 档案（§11 2287 字 + 32 行 + 16 来源；§12 10 件）+ 语料 24 条 + 图库 19 张全 PD/CC0 + 私有 9 件；分工 vs 克里姆特/马蒂斯写死（金地两说并存留档）；金地论争两说并存 | `knowledge/domains/painters/dossiers/ogata_korin.md` | ArtistOgataKorin（wave20） |
| A-91 | done | wave20·布莱克：476 行 v2 档案（§11 2147 字 + 32 行 + 12 来源；§12 10 件）+ 语料 28 条（Erdman 1988 逐字）+ 图库 18 张（17 PD + 1 CC0）+ 私有 5 组；分工 vs 蒙克/丢勒写死；3 条 OVERTURNED（信日期/Plate 5/YCBA） | `knowledge/domains/painters/dossiers/blake.md` | ArtistBlake（wave20） |
| A-92 | running | wave20·夏尔丹（Chardin）v2（静物触感） | `knowledge/domains/painters/dossiers/chardin.md` | ArtistChardin（wave20） |
| A-93 | running | wave20·马奈（Manet）v2（平面化现代性） | `knowledge/domains/painters/dossiers/manet.md` | ArtistManet（wave20） |
| A-94 | running | wave20·索罗拉（Sorolla）v2（强阳光） | `knowledge/domains/painters/dossiers/sorolla.md` | ArtistSorolla（wave20） |
| A-95 | running | wave20·佐恩（Zorn）v2（有限色板） | `knowledge/domains/painters/dossiers/zorn.md` | ArtistZorn（wave20） |
| A-96 | done | wave20·苏丹·穆罕默德：457 行 v2 档案（§11 2031 字 + 23 行 + 12 来源；§12 10 件）+ 语料 24 条 + 图库 16 张全 PD/CC0 + 私有 13 件；分工 vs 贝赫扎德（三轴复读对齐）/克里姆特写死；引文 26/26；AKM NC 图未采用（改 PD 版） | `knowledge/domains/painters/dossiers/sultan_mohammed.md` | ArtistSultanMohammed（wave20） |
| A-77 | done | wave19·范宽（重派）：426 行 v2 档案（§11 2119 字 + 26 行 + 14 来源；§12 8 件）+ 语料 26 条（含《宋朝名画评》四库本全文）+ 图库 8 张（PD/CC0/NPM 开放）+ 私有 10 件；分工 vs 黄公望（与 huang_gongwang.md 对称）/北斋/塞尚写死；1 条 OVERTURNED（「雨点皴」明始见） | `knowledge/domains/painters/dossiers/fan_kuan.md` | ArtistFanKuan-2（wave19） |
| A-78 | done | wave19·雪舟（重派·续写）：511 行 v2 档案（§11 2035 字 + 43 行 + 18 来源；§12 10 件）+ 语料 17 条（复核合格，26/26 HIT）+ 图库 18 张全 PD + MANIFEST + 私有 6 件；分工 vs 八大山人/徐渭/北斋写死；1 条 OVERTURNED（「首个日本水墨模块」） | `knowledge/domains/painters/dossiers/sesshu.md` | ArtistSesshu-2（wave19） |
| A-79 | done | wave19·康斯泰勃尔（重派·续写）：472 行 v2 档案（§11 2061 字 + 37 行 + 12 来源；§12 10 件）+ 语料 36 条 + 图库 17 张 PD/CC0 + MANIFEST；分工 vs 透纳/莫奈/弗里德里希写死（与 friedrich.md 互查一致）；引文 13/13 | `knowledge/domains/painters/dossiers/constable.md` | ArtistConstable-2（wave19） |
| A-80 | done | wave19·普桑（重派）：505 行 v2 档案（§11 2019 字 + 43 行；§12 10 件）+ 语料 24 条（Jouanny 1911 页码级）+ 图库 13 张全 PD/CC0 + 私有 7 件；分工 vs 达芬奇/米开朗基罗/弗里德里希写死（镜像互认）；scratch 核验 17/20 可用 | `knowledge/domains/painters/dossiers/poussin.md` | ArtistPoussin-2（wave19） |
| A-81 | done | wave19·勃鲁盖尔（重派）：v2 档案（§11 2066 字 + 41 行；§12 10 件）+ 语料 28 条（28/28 HIT）+ 图库 20 张全 PD + MANIFEST；分工 vs 北斋/米开朗基罗写死；commit 264a521+11e80f7 已随 sweep 入库 | `knowledge/domains/painters/dossiers/bruegel.md` | ArtistBruegel-2（wave19） |
| A-82 | done | wave19·埃尔·格列柯（重派）：497 行 v2 档案（§11 2044 字 + 36 行 + 14 来源；§12 10 件）+ 语料 30 条 + 图库 17 张全 PD/CC0 + 私有 5 件；分工 vs 蒙克/毕加索写死（与 munch.md 对称互锁）；1 条 OVERTURNED（散光说不采用）；引文 17/17 | `knowledge/domains/painters/dossiers/el_greco.md` | ArtistElGreco-2（wave19） |
| A-83 | done | wave19·荷尔拜因（重派）：504 行 v2 档案（§11 2170 字 + 47 行 + 14 来源；§12 10 件）+ 语料 26 条（题铭/遗嘱/van Mander 订正）+ 图库 13 张全 PD/CC0 + 私有 9 件；分工 vs 丢勒/伦勃朗写死；引文 18/18；scratch 核验弃用 10 件 | `knowledge/domains/painters/dossiers/holbein.md` | ArtistHolbein-2（wave19） |
| A-84 | done | wave19·艾瓦佐夫斯基（重派）：542 行 v2 档案（§11 2200 字 + 55 行 + 12 来源；§12 10 件）+ 语料 34 条 + 图库 14 张全 PD + 私有 5 件；分工 vs 透纳/北斋写死；2 条 OVERTURNED（版本修正）；引文 23/23；scratch 58 件核验 | `knowledge/domains/painters/dossiers/aivazovsky.md` | ArtistAivazovsky-2（wave19） |
| A-85 | done | wave19·欧姬芙（重派）：550 行 v2 档案（§11 2062 字 + 89 行 + 12 来源；§12 10 件）+ 语料 35 条 + 16 张图**全在 `_private/`**（公开侧零图）；分工 vs 马蒂斯/莫奈写死；引文 42/42；scratch 51 件核验后重取 4 件 | `knowledge/domains/painters/dossiers/okeeffe.md` | ArtistOkeeffe-2（wave19） |
| A-86 | done | wave19·里维拉（重派）：533 行 v2 档案（§11 2109 字 + 43 行 + 12 来源；§12 10 件）+ 语料 23 条 + 14 张图**全在 `_private/`**（公开侧零图）；分工 vs 米开朗基罗/戈雅写死 + 镜像 vs 卡罗互查；scratch 先核再用（OK=64） | `knowledge/domains/painters/dossiers/rivera.md` | ArtistRivera-2（wave19） |
| A-42 | done | wave15·慕夏：510 行 v2 档案（§11 2020 字 + 47 行 + 来源 ≥10；§12 10 件）+ 语料 25 条 + 图库 12 张（11 PD + 1 CC BY-SA 已署名）+ 私有 8 件；分工 vs 克里姆特写死（平面印刷档 × 材质工艺档）；引文 15/15 | `knowledge/domains/painters/dossiers/mucha.md` | ArtistMucha（wave15） |
| A-43 | done | wave15·蒙克：493 行 v2 档案（§11 2043 字 + 38 行 + 11 来源；§12 10 件）+ 语料 29 条（挪威语原文）+ 图库 13 张 + 私有论文 3 件；分工 vs 梵高写死（4 判据）；抽取直测 OK | `knowledge/domains/painters/dossiers/munch.md` | ArtistMunch（wave15） |
| A-44 | done | wave15·康定斯基：531 行 v2 档案（§11 2094 字 + 43 行 + 16 来源；§12 9 件）+ 语料 29 条（德文 6 条逐字核过）+ 图库 11 张（剔除 1 误认件）+ 私有 4 组；分工 vs 毕加索写死（解构↔抽象 4 判据） | `knowledge/domains/painters/dossiers/kandinsky.md` | ArtistKandinsky（wave15） |
| A-45 | done | wave15·委拉斯开兹：452 行 v2 档案（§11 2005 字 + 30 行 + 16 来源；§12 10 件）+ 语料 20 条 + 图库 12 张 + 私有高清 12 张；分工「光的第三档：画室与空气」写死（vs 伦勃朗/维米尔/达芬奇三对判分轴） | `knowledge/domains/painters/dossiers/velazquez.md` | ArtistVelazquez（wave15） |
| A-46 | done | wave15·博斯：505 行 v2 档案（§11 2070 字 + 24 行 + 12 来源；§12 10 件）+ 语料 26 条（无存世文字——档案转写+早期文献）+ 图库 10 张；分工 vs 戈雅写死（怪诞两档：噩梦 vs 百科）；抽取直测 OK | `knowledge/domains/painters/dossiers/bosch.md` | ArtistBosch（wave15） |
| A-47 | done | wave15·黄公望：427 行 v2 档案（§11 2017 字 + 26 行；§12 8 件）+ 语料 24 条（《写山水诀》11 条）+ 图库 10 张全 PD（富春山居三卷 + 剩山图）+ 私有 14 件；分工 vs 八大山人/塞尚/北斋/范宽写死；抽取 PARSE OK | `knowledge/domains/painters/dossiers/huang_gongwang.md` | ArtistHuangGongwang（wave13 尾单） |
| A-48 | done | wave15·卡罗：497 行 v2 档案（§11 2014 字 + 34 行；§12 9 件；含 2 条误传排除附录）+ 语料 24 条 + 13 张图**全在 `_private/`**（公开侧零图）；分工 vs 蒙克/里维拉写死；抽取 PASS | `knowledge/domains/painters/dossiers/kahlo.md` | ArtistKahlo（wave15） |
| A-49 | done | wave15·贝赫扎德：465 行 v2 档案（§11 生平 + §12 临摹清单）+ 语料 21 条 + 图库 12 张（PD/CC0）+ 私有 4 件；分工 vs 北斋/苏丹·穆罕默德写死；系统首个伊斯兰绘画大师 | `knowledge/domains/painters/dossiers/behzad.md` | ArtistBehzad（wave15） |

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
