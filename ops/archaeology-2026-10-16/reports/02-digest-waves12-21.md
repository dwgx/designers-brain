# 02 · DIGEST-APPEND — waves12–21 段（S-main 收尾 · 2026-10-15 21:3x → 2026-10-16 06:28）

> 写手：02 号报告（handoff/子代理报告蒸馏）｜日期：2026-10-16｜状态：**完成（追加就绪，待主脑并入 `ops/session-digest.md`）**
> 用途：对 `ops/session-digest.md`（覆盖至 wave10/S 线，截至 10-15）的**追加补丁包**。历史行不改写；与旧行冲突处走〔更正〕块。
> 来源：S-main **12 份 handoff 全读** + **25 份子代理报告选读**（附 B）+ `ops/GOALS.md` / `ops/OPS-LOG.md` / git log / `_scratch/` 实盘核验。
> 路径约定：`S-main/` = `C:/Users/dwgx1/.omp/agent/sessions/--D--Project-Designers_Brain--/2026-10-15T06-29-46-426Z_01a13e40-a53a-7169-8317-62a0dc18de57/`（12 handoff、144 子代理 jsonl、157 md 均在此目录；简称后同）。
> 死线口径：S-main 于 **2026-10-16 06:28:31 JST** 被 SIGHUP 杀死（jsonl 末条 `session_exit`），死时主脑正 `wait` IndexMerge3。

**一句话结论**：S-main 死前已完成 wave11–21 全部（画家 program 62 位收口）+ 公开发布 + 收口三工中两工半（卡 62 已提交、互引已落盘未提交、索引三轮已提交）；死亡遗留 = A-107 未置 done + 2 commits 未推 + 工作树 9 文件 + GOALS.md 未提交。

---

## 0 · 缺口确认（对照旧 digest）

旧 digest 覆盖到：wave10 / S-04 盲测 / 审计修复 / 蒸馏（10-15 21:3x 为止）。**本段补齐**：wave11（S-05 收口）→ wave21 各波 + 仓库 git 化与公开发布 + 私有层政策 + provider 崩溃与 resume + 宿主重启被杀 + 收口三工（卡 62 / 交叉互引 / 索引三轮）+ 06:28 死亡点。旧 §2 表末行为「2026-10-15 晚 | 蒸馏 | …」，本报告 §2 行接其后续写。

---

## 1 · §2 追加行（23 行 · 整块追加到 digest §2 表末）

| 日期 | 波/车道 | 发生了什么 | 结果/证据 |
|---|---|---|---|
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

---

## 2 · §3 决策新增（第 12–23 条 · 追加到 digest §3 末）

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

---

## 3 · §4 死胡同新增（第 11–19 条 · 追加到 digest §4 末）

11. **Wikimedia 直连 429**：`upload.wikimedia.org`/`thumb.wikimedia.org` 对本机限流（curl 与浏览器均 429）→ 用 `Special:FilePath/<file>?width=N`、`thumb.php`、标准尺寸缩略（仅 250/330/500/960/1280/1920）、Wayback `im_` 镜像；Commons API 直连易 429。来源：S-main/handoff-2026-10-15T19-24-48-017Z.md；S-main/ArtistMirSayyidAli.md。
12. **馆站 403/Cloudflare**：britishmuseum.org、asia.si.edu、NGA/AGSA/DAAO、LOC/Honolulu、NPM 实况页等直读被拒 → Wayback 快照 + 真 Chromium（browser fetch）+ 媒体子域直取；searcharchives.bl.uk JSON 可用、collections.louvre.fr 重试可用。来源：S-main/ArtistMirSayyidAli.md、ArtistKngwarreye.md、handoff-2026-10-15T20-34-49-588Z.md。
13. **NPM 图库接口**：`Image/GetImage` 需 session randomCode → 批量抓取 403；改用 `iiifod.npm.gov.tw` IIIF（curl 可用）或浏览器 fetch；月刊 PDF 走 `NewChineseArtDownload.ashx`。来源：S-main/handoff-2026-10-15T18-52-57-205Z.md（决策行）。
14. **「藤花亭画谱」不存在**：NDL サーチ / CiNii / Brave / Yahoo / Baidu / Sogou / ja.wiki / 若冲书志年表全查无（「藤花亭」为梁廷枏斋号，与本画家无关）→ 别重做该检索；改用『藤景和画記』『若冲画譜』等可核材料。来源：S-main/HardIto.md。
15. **画廊图误标与不可用件**：陈洪绶 Commons「selfportrait_1635.jpg」实为《乔松仙寿图》（已移除换 `tanmei_tu`）；`LuJunYi.gif`/`quyuan_alt.jpg` 不可用弃用；sargent 联系表抓出 2 误取件已替换。教训：画廊图逐张核名 + 目检。来源：S-main/handoff-2026-10-15T20-34-49-588Z.md；GOALS A-69/A-101。
16. **维基不作结论级来源**：kngwarreye「1993 入选威尼斯」WEAKENED 不采用（1997 三源一致）；mir「卒年 1572」OVERTURNED 不采用；ru-wiki「4 of 14 Khamsa」留待核。来源：S-main/ArtistKngwarreye.md、ArtistMirSayyidAli.md。
17. **宿主重启杀光在飞子代理**：wave19×10 在重启中被杀（零产出）；「后台继续、不受压缩影响」≠ 不受重启影响 → 重启前先 sweep 落盘 + 记在飞清单；重启后核 scratch 重派，别等原工人。来源：OPS-LOG「重启前收拾/重启恢复」。
18. **私有计数口径坑**：第一轮按扩展名计数漏计 kandinsky `.hires`（内容实为 JPEG）→ 改按内容识别；QA 产物（`_` 前缀 / `contact_sheet*` / `cs_*`）须排除（de_chirico 26→25、zhao 12→9）；`.raw` 按内容计入（ni_zan 19）。来源：`_scratch/index_merge2/reconcile.md`、`_scratch/index_merge3/reconcile.md`。
19. **GBK 终端乱码 ≠ 文件问题**：仓库终端 cp936 使部分 bash 输出 CJK 乱码，文件本身 UTF-8 正常 → 勿因乱码改编码/重写文件。来源：S-main/handoff-2026-10-15T20-34-49-588Z.md。

---

## 4 · §5 未收口更新

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

## 5 · 〔更正〕块（建议插入 digest §5 与 §6 之间；新小节）

```markdown
## 〔更正〕（2026-10-16 追加）

- C1 · 旧 §1「不建 git」已失效：Owner 后续令已建 git 并发布 public 仓（`github.com/dwgx/designers-brain`）；OPS-LOG §14/§15 为准。
- C2 · 旧 §1「GOALS 51 项 done，仅 S-05 open」已失效：S-05 已 done（wave11）；现行 = 148 行（145 done / 1 running：A-107 / 2 open：A-30、S-06）。
- C3 · 旧 §6「handoff 4 份 / 子代理文件 39 个（未逐读）」需扩：S-main 目录实有 12 份 handoff、144 子代理 jsonl + 157 md（侦察口径见 `ops/archaeology-2026-10-16/MAIN-BRAIN.md` §2）；12 份速览见 `reports/02-digest-waves12-21.md` 附 A。
- C4 · 旧「截至 2026-10-15」口径需扩：S-main 实际运行至 2026-10-16 06:28:31 JST（SIGHUP 死亡；jsonl 末条 `session_exit`）；本 digest 的 10-15 21:3x → 10-16 06:28 段见 02 号报告 §2 追加行。
- C5 · 路径口径变更：旧 `research/...` 路径 → 重构后为 `knowledge/`、`experiments/`、`docs/`、`ops/`（映射见 `docs/MIGRATION.md`）；§6 前缀说明需补一句。
```

---

## 6 · 附 A · 12 份 handoff 速览（全读压缩）

| # | 文件（S-main/） | JST 时间 | 性质 | 一句话 |
|---|---|---|---|---|
| 1 | `handoff-2026-10-15T10-40-00-997Z.md` | 10-15 19:40 | 工·AnimTest03Blender | 300 帧渲染完成（757.8s）；`checks.md` 待生成（bg_87 软体重试在跑）；P1 确定性已定档 |
| 2 | `handoff-2026-10-15T10-42-32-003Z.md` | 10-15 19:42 | 工·AnimTest03Blender 续 | `make_checks_md.py` 编辑中（heredoc 失败，改 edit）；letter-mesh 软体两次发散记档；DOF/rerun 补数待注入 |
| 3 | `handoff-2026-10-15T10-47-14-473Z.md`※ | 10-15 19:47 | 项目级 | wave8 后全局快照：B-19 待改 done、E-02 在飞、OPS-LOG 补两条教训、板文件处置、C-02 reconcile 待跑 |
| 4 | `handoff-2026-10-15T11-06-38-802Z.md` | 10-15 20:06 | 项目级 | E-03/E-04 已交付待核；下一步四选项（人评/其余卡/E3/E4/第二批）；模块卡校验器与实验自校验器清单 |
| 5 | `handoff-2026-10-15T15-19-39-781Z.md` | 10-16 00:19 | 项目级 | wave12–14 完成、wave15 8 工在飞、wave16 收口 2 工（ModuleCards20/IndexMerge）、wave17 7 工在飞；私有层/流中断规程；在飞 14 工清单 |
| 6 | `handoff-2026-10-15T15-31-59-563Z.md` | 10-16 00:31 | 项目级 | wave15 收口 7 位（+huang_gongwang 尾单）；§11/§12 归一说明；在飞 10 工；domains count 11→20 同步指引 |
| 7 | `handoff-2026-10-15T15-41-48-393Z.md` | 10-16 00:41 | 工·IndexMerge | 三表合并完成（20 位；PASS 75/0）；待主脑验收 A-51；脚本可复用于后续轮次 |
| 8 | `handoff-2026-10-15T18-52-57-205Z.md` | 10-16 03:52 | 工·ArtistQiuYing | 四处落盘 3/4 完成（dossier §C 七块待填、INVENTORY 待写）；NPM IIIF/浏览器 fetch 路径留档 |
| 9 | `handoff-2026-10-15T19-24-48-017Z.md` | 10-16 04:24 | 工·ArtistNiZan | 四处落盘全完成（458 行/35 条/12 图/私有 36MB）；契约自测 PASS；待主脑索引/卡片 |
| 10 | `handoff-2026-10-15T20-34-49-588Z.md` | 10-16 05:34 | 工·ArtistChenHongshou | 四处落盘全完成（449 行/26 条/18 图/私有 8 件）；替换误标自画像；待提交 |
| 11 | `handoff-2026-10-15T20-42-26-030Z.md` | 10-16 05:42 | 工·ArtistMirSayyidAli | 档案/语料/图库/私有完成；R 编号重映射后待复跑复核（R1–R25）；待提交 |
| 12 | `handoff-2026-10-15T21-22-37-592Z.md` | 10-16 06:22 | 工·IndexMerge3 | 三表 35→62 方案与脚本就绪（build_new_rows 待跑）；口径决定（私有 54 行/QA 排除）；HEAD=ad961d3 |

※ 第 3 份文件名实为 `handoff-2026-10-15T10-47-14-540Z.md`（上表缩写笔误请以磁盘为准）。

---

## 7 · 附 B · 本次选读报告清单（25 份 + 说明）

- **收口三工**：`ModuleCards20.md`、`ModuleCards42.md`、`ModuleCards62.md`、`IndexMerge.md`、`IndexMerge2.md`（`IndexMerge3.md` 为 0 字节空文件 → 以 `_scratch/index_merge3/RECEIPT.md` 补齐）、`CrossLinkSync.md`。
- **加固 pass2**：`HardTurner/HardRembrandt/HardKlimt/HardGoya/HardSeurat/HardHopper/HardBada/HardQi/HardIto.md`（9 份）。
- **wave17–21 代表工**：`ArtistKngwarreye.md`、`ArtistHiroshige.md`、`ArtistOkeeffe-2.md`、`ArtistQiuYing.md`、`ArtistNiZan.md`、`ArtistChenHongshou.md`、`ArtistMirSayyidAli.md`、`ArtistXuBeihong.md`、`ArtistLiKeran.md`、`ArtistRockwell.md`。
- **skill 线**：`ConsultWalkthrough.md`、`AutoTriggerProbe.md`；**旧线抽查**：`AnnotationSweep.md`（内容与旧 digest 一致，无新增）。
- **空文件说明**：`Bio*.md`（11 份）与 `RosterBuilder.md` 为 0 字节 → 内容经 GOALS/OPS-LOG/handoff 及 `RosterBuilder.jsonl` 末条补齐（名册 349 行/42,109 B、59 候选、17✔/8✖ 探测台账）。
- 未逐读：其余 ~110 份子代理 jsonl/md（按需深挖；本报告只取收尾段）。

---

## 8 · 自审四段（简报格式）

- **A 早产出**：先读 digest/GOALS/OPS-LOG 定缺口 → 全读 12 handoff → 选读 25 份报告 → git log / jsonl 末条 / scratch 实盘核验 → 本报告落盘（无攒批）。
- **B 反驳**：①「覆盖到 06:28」——用 jsonl 末条 `session_exit` + git ahead 2 双证（CONFIRMED）；②「每行证据」——逐行核对路径存在性（commit 哈希 / scratch 文件 / S-main 文件，抽查命中）（CONFIRMED）；③「与旧 digest 无重复」——旧表止于 wave10/蒸馏，本表起 wave11，逐行去重核对（CONFIRMED）；④ 弱点：重启窗口（02:01→03:19）按 commit 空窗推定，非日志直证（WEAKENED，已注明口径）。
- **C 机械验证**：行数统计（§2 = 23 行 / §3 = 12 条 / §4 = 9 条 / 更正 = 5 条）；关键数字复跑命令 = `git log origin/main..main`（2）、`grep -c "| done " ops/GOALS.md`（144）、`ls _scratch/`（index_merge3 在位）；S-main 目录清点（12 handoff / 144 jsonl / 157 md）。
- **D 小结（≤14 行）**：见文首「一句话结论」。核心：wave11–21 全收口、三工两工半、死亡点遗留 2 未推 + 10 未提交 + A-107 未收口；本报告为追加就绪补丁，digest 本体未动。

---

## 9 · 整合说明（每块插入 digest 的位置）

| 本报告块 | 插入位置（`ops/session-digest.md`） | 操作 |
|---|---|---|
| §2 追加行（23 行） | **§2 表末**（现末行「2026-10-15 晚 · 蒸馏」之后） | 整块粘贴，不改旧行 |
| §3 决策（12–23） | **§3 末**（现第 11 条之后） | 顺序追加，编号续 12–23 |
| §4 死胡同（11–19） | **§4 末**（现第 10 条之后） | 顺序追加，编号续 11–19 |
| §5 未收口更新 | **§5** | 不整块替换：A 段为旧 1–8 项状态更新；B 段（9–15）追加为「（2026-10-16 更新）」子列表；S-05 的收口事实以〔更正〕C2 处理 |
| 〔更正〕块（C1–C5） | **§5 与 §6 之间**（新小节） | 按 digest 纪律「历史行不改写，更正用〔更正〕块」 |
| 附 A / 附 B | 不入正文 | 供 §6 会话索引扩写与后续核引用；可作 digest 文末附录 |
| 本报告文件 | `ops/archaeology-2026-10-16/reports/02-digest-waves12-21.md` | 交付物本体；digest 未动（Non-goals） |
