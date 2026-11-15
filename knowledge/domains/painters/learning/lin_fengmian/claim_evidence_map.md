<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-lin_fengmian；原正文 SHA-256 `7843b036410b3582f2dae12ae0662a3c49ad24b85ae5abe4c33a297821bbca91`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-lin_fengmian — claim_evidence_map.md（逐 claim 文件:节:行号 + 子串定位）

> TASK_ID `LEARN-lin_fengmian`（A-30）· 依赖 内部证据 b52016264fa3f8e1（未公开；来源记录由维护者保留）（ACCEPTED）· Repo READ-ONLY @ `f008952365a77e140cbda3f3959d43ef000f9a22` · 写入仅 内部证据 645a7bc73c3ee7b0（未公开；来源记录由维护者保留）。
> 一行一 claim：`locator` 用 `文件:节:行号 + 子串`，grade 沿用档案（`[自述]/[史料]/[研究]/[归纳]`；corpus 另标 `[self-written]/[self-spoken]/[reported speech]/[reception]`），`support_status` ∈ {supported, partial, conflict, unverified, not_applicable}。**本片不重审 ACCEPTED 审计**：AUDIT [claim_evidence_map.md](claim_evidence_map.md)（70 行 61/2/1/6）与 `review-evidence.md`（审者独立复核）是证据底本，照实携带其 partial/conflict/unverified，不升级。
> `[归纳]` 全部标「本项目操作规则，未像素实测」；`[推测]` 计数 = 0；`[自述]` 不与 `[归纳]` 混写一句。

<a id="db-source-line-7"></a>
## §A 输入与依赖（开工 hash 复核，与 内部证据 04872e1230edb0c5（未公开；来源记录由维护者保留）

| claim_id | locator（文件:节:行号 + 子串） | grade | support_status | 依据 |
|---|---|---|---|---|
| C-DEP-01 | 内部证据 0b6b989278232233（未公开；来源记录由维护者保留）（card `9675d108…` / dossier `cabe2e6d…` / corpus `e31d0ca0…` / conflicts `314a24da…` / manifest `5698124d…` / GOALS `2727d1f0…`） | `[史料]` | supported | 开工 `sha256sum` 实测 6/6 与契约逐项吻合；`execution_dedup_key=49b2473c…` bound |
| C-DEP-02 | 内部证据 5e0e9d5b8d93d046（未公开；来源记录由维护者保留） `"status": "accepted"`；`:338` `"verdict": "accepted"`；`:323` reviewer=`ReviewGateAUDIT-lin_fengmian(glm-5.3-flash)`；`:374` author=`AuditLinFengmian(hy4free)`（≠ reviewer） | `[史料]` | supported | `review-evidence.md:54-56` "**accepted.**"；依赖为 ACCEPTED，本片复用不重审 |
| C-DEP-03 | 内部证据 09432353da923640（未公开；来源记录由维护者保留） "70 rows … 61/2/1/6 MATCH"；`:21-22` "Two metrics reconciled … VERIFIED"；`:44` "images_public=0 fact — VERIFIED"；`:39` "Dangling module→conflicts cross-reference confirmed" | `[史料]` | supported | 审者独立重跑两侧指标、D1、权利、3 次 fetch；本片不冒充本轮运行 |
| C-A30-01 | `package/01-AUDIT.md:271` "前置知识、重点作品及来源、要观察的机制、具体练习、可观察结果、常见失败、下一步及使用边界"；`:273` "练习效果尚未由人完成或评价时，明确为建议练习，不写'已证实学习收益'" | `[史料]` | supported | 八节形状 + 建议练习硬边界；[learning_path.md](learning_path.md) §1–§8 八标题齐全 |

<a id="db-source-line-16"></a>
## §B 主轴 A｜中西融合 · 方纸布阵（brief「方纸鸿蒙」）

| claim_id | locator | grade | support_status | 依据 |
|---|---|---|---|---|
| C-M1-01 | `dossiers/lin_fengmian.md:L22` "把西方现代主义的形色结构（印象派/野兽派/立体主义）转译为水墨与彩墨的抒情语言"；"方纸布阵" | `[研究]` | supported | 一句话能力定位 + capability 标签；`modules/lin_fengmian.md:L9` 浓缩 5 条同义 |
| C-M1-02 | `dossiers/lin_fengmian.md:L38` "方纸布阵（正方形满幅）…1:1±5%…四方等量扩展…常连签名的位置也没有" | `[研究]` | supported | §1 指纹表第 1 行；可观察量 = 画幅比/触满四边/负空间低且主动 |
| C-M1-03 | `dossiers/lin_fengmian.md:L39` "块面与线弦的二重唱"；`:L40` "墨彩调合（墨彩齐下）…墨中叠彩，彩中叠墨"；`:L41` "涂白（叠白法）…白分五彩"；`:L42` "民间瓷绘色" | `[研究]` | supported | §1 行 2–5；对应 §8.2 规则 2/3/4/5 |
| C-M1-04 | `_corpus/lin_fengmian.md:L10-L13` "繪畫底本質是繪畫，無所謂派別也無所謂「中西」" (#1)；`:L34-L38` "短長相補，世界新藝術之產生" (#5)；`:L136-L140` "介绍西洋艺术，整理中国艺术，调和中西艺术，创造时代艺术" (#21) | `[self-written]`/`[自述]` | supported | 调和中西的立场锚；`dossier :L70` 递进关系（整理/调和=方法，创造时代艺术=目的） |
| C-M1-05 | `dossiers/lin_fengmian.md:L55-L60` 柯罗蒙工作室 / 北京艺专 / 杭州艺专「中西画不分系」/ 重庆转水墨 / "墨彩齐下、纸背托色、惜纸如金" | `[史料]/[研究]` | supported | §2 技法 1–6；两阶段「取→炼」的史料路径 |
| C-M1-06 | `dossiers/lin_fengmian.md:L217` "两阶段状态机——阶段 A「取」…阶段 B「炼」…不得在「形式化」轴滑动" | `[归纳]` | unverified | §8.3 机制关系 `[归纳]`；规则层设计，非像素/生成实测 |
| C-M1-07 | `dossiers/lin_fengmian.md:L70` "调和中西，创造时代艺术"；`:L72` "画从记忆中来"；`:L75` "向民间与古典再发现" | `[自述]/[研究]` | supported | §3 创作原则 1/3/6；与 corpus #10/#12/#14/#15 互证 |
| C-M1-08 | brief「方纸鸿蒙」 vs 档案 `dossiers/lin_fengmian.md:L38/:L61`「方纸布阵」/「方构图」；`modules/lin_fengmian.md:L9` | `[归纳]` | supported | **术语澄清**：「方纸鸿蒙」是 brief 强调别名、非史料术语；本片 5 文件引用一律用正本「方纸布阵」，不把别名当档案原词 |

<a id="db-source-line-29"></a>
## §C 主轴 B｜戏曲人物变形机制（折叠 + 几何化）

| claim_id | locator | grade | support_status | 依据 |
|---|---|---|---|---|
| C-M2-01 | `_corpus/lin_fengmian.md:L104-L107` "像毕加索有时解决物体都折叠在一个平面上一样…一場一場的故事人物，也一個一個把它折疊在畫面上…不是求體積感而是求綜合的連續感" (#16) | `[self-spoken]`/`[自述]` | supported | 折叠自述锚；`:L107` 版本差异「體積感/體質感」留档；`dossier §10-5/L276` |
| C-M2-02 | `dossiers/lin_fengmian.md:L44` "戏曲折叠…把一场一场的故事人物，也一个一个把它折叠在画面上…求综合的连续感…借皮影几何" | `[自述]` | supported | §1 指纹第 7 行；= 平面化叠加 + 时空交错 + 无固定视点 + 无叙事时间线 |
| C-M2-03 | `dossiers/lin_fengmian.md:L64` "受同乡关良影响开始看戏…小本子画速写…用英文单词标注重要的色彩和特征…借皮影几何造型…1964 景德镇" | `[史料]/[研究]` | supported | §2 技法 10；折叠的工序与民间来源 |
| C-M2-04 | `dossiers/lin_fengmian.md:L75` "通过中国戏曲重新认识立体主义对时空的自由处理，借皮影的几何形打造中国式抽象效果" | `[自述]/[研究]` | supported | §3 原则 6；中西融合在题材层的落地 |
| C-M2-05 | `dossiers/lin_fengmian.md:L45` "静物的「洋味」与变形…像是压缩在斜面上…桌面、门窗变形、不合透视…几何秩序"；`:L85` "林 1940s 亦讲几何秩序，但几何被包在墨彩与抒情之内、不作独立主题" | `[研究]`/`[归纳]` | supported | 变形的可观察半 + 边界注（④轴仍在林侧）；对应 §8.2 规则 7 |
| C-M2-06 | `dossiers/lin_fengmian.md:L95` "① 造型——写实解剖与素描结构（徐）vs 线描＋色块抒情（林）"；`:L116` 警报③"明暗交界线＋解剖素描＋主题性大构图 → 越界徐悲鸿" | `[归纳]` | supported | 折叠 ≠ 解剖变形的分界；vs 徐四轴 |
| C-M2-07 | `dossiers/lin_fengmian.md:L113` "P6 折叠几何度…默认建议 50%"；`:L207` "几何构成 ≥2 处；透视有意变形 ≥1 处"；`:L206` "每帧 ≥1 母题…无叙事性事件"；`:L116` 警报⑤"零对象、纯抽象形式 → 康定斯基/赵无极侧" | `[归纳]` | unverified | P6/规则 6/7 阈值均 `[归纳]` 未像素实测；折叠仍须保母题 |
| C-M2-08 | `dossiers/lin_fengmian.md:L411-L424` §12 第 4/5/6 件《宇宙锋》"选一出戏的 3 个瞬间，折叠进一张方幅：不画舞台、不画透视；人物 ≥2 个交叠" /《火烧赤壁》/《舞》"忠实临摹 → 去背景 → 色块简化" | `[归纳]` | supported | 练习条目为本项目设计（§12 抬头 `:L394`）；成功自检 = "能不能读出一条「连续感」" |
| C-M2-09 | `_corpus/lin_fengmian.md:L52-L55` "便可覺到無限的淒涼"（#8, 1927 论旧剧）；`dossiers/lin_fengmian.md:L277` "1927 年对旧剧的态度（「凄凉」）→ 1950s 借戏曲深化立体主义：位移记录" | `[self-written]`/`[史料]` | supported | **态度位移**：不得用 #8 解释 #16；`§10-6` 明确留档 |

<a id="db-source-line-43"></a>
## §D images_public=0 事实（31 私有）— brief 强调点③

| claim_id | locator | grade | support_status | 依据 |
|---|---|---|---|---|
| C-IMG-01 | 内部证据 5807c1a2cd2ba9bd（未公开；来源记录由维护者保留） "images_public = 0 is a FACT, not a defect…31 images all in `_private/images_hi_res/lin_fengmian/`"；`:L12` `_images/manifest.md` L3228 "\| lin_fengmian \| 0 \| 31 \| 全部版权未清…公开侧 0 张 \|" | `[史料]` | supported | AUDIT 权利复核；`review-evidence.md §5` 独立复核 |
| C-IMG-02 | 内部证据 a27865ab08d9d8d3（未公开；来源记录由维护者保留） `"images_public": 0`；`:93` `"images_private": 31`；`:15` `"PUBLIC-SIDE ZERO IMAGES OK"`（check_lfm.py） | `[史料]` | supported | `dossier :L10` 版权纪律；`check_lfm.py` 全量 sha256 31/31 OK |
| C-IMG-03 | 内部证据 282e95779b53eb2b（未公开；来源记录由维护者保留） "No image was visually inspected this run (`image_seen = 0`)"；`:L68` "unknown stays unknown — none upgraded to PD/CC0/CC/public" | `[史料]` | supported | 本片沿用 `image_seen=0`；权利真实性/视觉内容不升级 |
| C-IMG-04 | `dossiers/lin_fengmian.md:L10` "1991 年逝世…中国著作权法 life+50 → 2041-12-31 前受保护…公开侧零图…不落任何图像文件、不引用私有层路径" | `[史料]` | supported | 权利主体＝家属/基金会及各馆藏；`rights_review.md:L19-L21` |

<a id="db-source-line-52"></a>
## §E 两指标调和（32/32 citation_check vs corpus 30）— brief 强调点④前半

| claim_id | locator | grade | support_status | 依据 |
|---|---|---|---|---|
| C-MET-01 | 内部证据 9f13da6eed8b4c17（未公开；来源记录由维护者保留） "citation_check.py/citation_check_output.txt → **32/32 PASS** + 12 扫描件目检. This is the GOALS A-112 '引文 32/32'"；`:81-86` "brief '引文 32/32' = citation_check.py 32/32 machine-comparison fragments…'32' is a citation metric, not a corpus heading count" | `[史料]` | supported | 32 条机器比对**片段**（一条语料可拆多片，如 #6/#20 各 2 条） |
| C-MET-02 | 内部证据 886d059b37c4c36a（未公开；来源记录由维护者保留） "`grep -c '^### '` corpus = **30** = ledger `corpus_quotes`"；`:79` "D4 dossier…「语料 28 条」 while actual count = 30"；`claim_evidence_map.md:L10` "corpus quotes 30 — matches ledger" | `[史料]` | supported | 语料条数 = 30；ledger `artist-shards.json[lin_fengmian].corpus_quotes=30` |
| C-MET-03 | 内部证据 0a11a7db1def28e7（未公开；来源记录由维护者保留） "§2 Two metrics reconciled (32/32 citation_check vs corpus 30) — VERIFIED…exactly 32 `[PASS]` lines…Corpus heading count = 30…Not conflated" | `[史料]` | supported | **审者独立重跑两侧**；二者是不同指标、非矛盾；本片不合流、不择一 |
| C-MET-04 | 内部证据 19a98aee242fb304（未公开；来源记录由维护者保留） "GOALS A-112 '引文 32/32' is citation_check.py's 32 machine-comparison fragments (32/32 PASS), a DIFFERENT metric — recorded, not conflated" | `[史料]` | supported | coverage-manifest 显式口径；`GOALS.md A-112` 行 |

<a id="db-source-line-61"></a>
## §F D1 dangling C-refs（known-open，携带不收口）— brief 强调点④后半

| claim_id | locator | grade | support_status | 依据 |
|---|---|---|---|---|
| C-D1-01 | `modules/lin_fengmian.md:L46` "C-01/C-05/C-06/C-12/C-17/C-18 为组合预检重点"；`:L69` 同列；`dossiers/lin_fengmian.md:L99` "组合时按 conflicts.md 预检（重点 C-01…C-18）"；`:L210` 重复 | `[归纳]` | **conflict** | card/dossier 把 6 条 C 行列为林「组合预检重点」，但下条显示 locators 无林专属 resolves |
| C-D1-02 | 内部证据 5e8b52ec5b4fd110（未公开；来源记录由维护者保留） "D1 (most material)…`grep -n "lin_fengmian\|林风眠\|lfm" conflicts.md` → **0 matches** (exit 1). The 6 C-rows exist (L55/L109/L123/L203/L272/L285) but name only 卡拉瓦乔/达芬奇/梵高/毕加索/马蒂斯/北斋/米开朗基罗…Do not fix here." | `[史料]` | supported | AUDIT 判定 dangling module→conflicts 交叉引用；reported NOT fixed |
| C-D1-03 | 内部证据 9623fb8c0b6a3fc8（未公开；来源记录由维护者保留） "§4 D1 dangling C-refs — VERIFIED…0 matches (exit 1)…Dangling module→conflicts cross-reference confirmed, correctly reported not fixed" | `[史料]` | supported | 审者独立 `grep -i -E 'lin_fengmian\|林风眠\|lfm'` 复核 |
| C-D1-04 | 内部证据 8aa21c110a7a1fa9（未公开；来源记录由维护者保留） "S3-12 §3.1 L99 … support_status=**conflict** …cites 6 conflicts.md C-rows…ZERO lin_fengmian/林风眠/lfm references → locators do NOT resolve"；`:L111-L115` D1 段 | `[归纳]` | supported | AUDIT 70 行中唯一 conflict 行；本片不把它升 supported |
| C-D1-05 | 本片 5 文件：`learning_path.md §6 F5` / `how-to-think.md §3 末+§4-1` / `mechanism_notes.md §5+§6④` / `claim_evidence_map.md §F` / `RESULT.md §3` | `[归纳]` | supported | **5 文件一致作为 known-open 携带**：不修仓库、不补 C 行、不升级为「已落地」；组合预检只当通用轴条款（conflicts.md §3 N1–N9），交 CONFLICT/RULE/卡同步 lane |

<a id="db-source-line-71"></a>
## §G AUDIT 已知 drift / 弱化项（照实携带，不改判）

| claim_id | locator | grade | support_status | 依据 |
|---|---|---|---|---|
| C-DR-01 | 内部证据 b789bbc23b308f00（未公开；来源记录由维护者保留） D2 near-miss 11 行(L345–L357) vs §5A(L365)/`modules/lin_fengmian.md:L74`"near-miss 8 对"；D3 对侧缺项注记 stale（`wu_guanzhong.md:L95`、`matisse.md:L72` post A-117 已回填）；D4「语料 28 条」文字 vs 30 | `[史料]` | supported | 三项 drift reported not fixed；`claim_evidence_map.md §Right/drift notes` |
| C-DR-02 | 内部证据 e4ee0dc2c1d5fd24（未公开；来源记录由维护者保留） "partial 2 (§3.1 vs 吴 / vs 马 对侧缺项注记 stale)"；`:46` "unverified 6 (§4 P1–P6 归纳阈值未实测)" | `[归纳]` | partial / unverified | AUDIT per-status 61/2/1/6 = 70（`:40-46`）；本片不升级 |
| C-DR-03 | 内部证据 9e5c54a82af2b95e（未公开；来源记录由维护者保留） R8 chinanews "same size 77622 B, different sha (dynamic content drift)…all 4 anchors ✓"；`:50-52` F1/F2/F3 非阻断发现 | `[史料]` | supported | 审者复访 hash 漂移但锚点级佐证成立；本片不重访、照实携带 |
| C-DR-04 | 内部证据 3483e31fbebacbee（未公开；来源记录由维护者保留） "Counterexample attempt…the rule is robust — §3.1/L85 already pre-empts…this is a rule-consistency check, not an empirical discriminator…no pixel-level falsification was possible" | `[归纳]` | unverified | 反例 = 规则一致性，非像素级证伪（分母＝假想参考帧）；`dossier :L284` |
| C-DR-05 | `dossiers/lin_fengmian.md:L273-L285` §10 异说并存（毁画数量/《舞》尺寸/生卒口径/妻女赴巴西/上海起点/场刊 URL/阈值未实测/图像层级） | `[史料]/[归纳]` | partial | 沿用 AUDIT 口径，不私自取一；`human_review=not_applicable` |

<a id="db-source-line-81"></a>
## 定位纪律自检

- 所有 repo locator 为 `文件:节:行号 + 子串`，可用 `read`/`grep` 程序化复核；AUDIT staging locator 同理。
- 语料引用带 `### 编号` + 行号 + 类型；繁体引文照录不转简（corpus header `:L6`）。
- `read_scope` 与 `access_status` 在 `receipt.json:claims[]` 按实标（fulltext/sections/citation_context/artifact/metadata）；`image_seen=0`，不冒充看过像素。
- `[自述]`/`[史料]`/`[研究]`/`[归纳]` 分栏，`[推测]`=0；`[归纳]` 一律带「未像素实测」；不把 AUDIT partial/conflict/unverified 升 supported（C-DEP-02/C-D1-04/C-DR-02）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
