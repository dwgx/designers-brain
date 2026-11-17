<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-turner；原正文 SHA-256 `bee52f3eea86f0f55d4e00b66fe9a01ad134b2beff6c932c11f891a4fbf080db`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-turner — Claim → Evidence Map

> 上游 `AUDIT-turner` = ACCEPTED（`review-gate-receipt.json:13` verdict=accepted / `:14` blocking_defects=0）；本 lane 不重新审计，复用其 locator 纪律、覆盖口径与 15 条 claims.csv 的登记。
> 每条论断给：**locator（实测行号 + 子串）+ 证据等级 + 支持状态 + source_ref 的 sha256**。`read_scope` 与 `access_status` 按实际读取口径；外部 URL 本轮未重访（`access_status=unknown`）、图未目检（无 `image_seen`）。
> 等级：`[自述]` 本人写下/说出带出处 · `[史料]` 当时记录/馆藏 · `[研究]` 艺术史家/博物馆 · `[归纳]` 本项目操作规则 · `[推测]`=0（`dossiers/turner.md:4`）。
> 支持状态：`supported` / `partial` / `conflict` / `unverified` / `not_applicable`（schema 口径）。
> 全部引用文件哈希 = 开工 `sha256sum` 实测值，见 `RESULT.md §2`。

**输入文件哈希（本 lane 实测，供下列 source_ref 复用）**

| 文件 | sha256 | 读取范围 |
|---|---|---|
| [turner.md](../../modules/turner.md) | `e3a2dcb28c8211274753f54b2af51bd3b890ef990e790b7d1fca94440414b372` | fulltext |
| [turner.md](../../dossiers/turner.md) | `3e26685f8930ef9923aa3b3fd263b64fa6664943f4578441987a88cdb7b1a2f4` | fulltext (479 行) |
| [turner.md](../../dossiers/_corpus/turner.md) | `3de2032499e88c3c0c31546441720b0893510f1b6255dd4eff7bb1c9ebc7e142` | fulltext (19 quotes) |
| `conflicts.md` | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | sections (C-05/C-10/N3/N4) |
| [INDEX.md](../../dossiers/_corpus/INDEX.md) | `b74bf44fe2e9523f6f14f7171bce00bbc1729143a0634e4b5c789595e33c65b4` | sections (L30 turner row) |
| `ops/GOALS.md` | `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144` | sections (L34 A-20 / L65 A-59) |
| `AUDIT-turner/coverage-manifest.json` | `6d6809ec2367758b0e2d2659979b86b507d4951c7f9379776154f743f5e48f93` | artifact |
| `AUDIT-turner/RESULT.md` | `5cf2134016f40864010c65a081eeb152e19a3dae9b2bf07b14ad7f5cd2b89f39` | sections |
| `AUDIT-turner/claims.csv` | `114fbcb239be35e31db5679a63a6a9241665ade23873a3b88563d0873d31fa62` | fulltext (15 行) |
| `AUDIT-turner/counterexample.md` | `3687f59872714d2a7dae2f10af58324bb5238dc8d46d5750fa534bc5e5c0532d` | fulltext (CX-1..CX-10) |
| `AUDIT-turner/review-gate-receipt.json` | `f5e6e30f7a7c6731eb0f0ea85536952ad29f97ce63bc7a50f4bbd42fac2cfe98` | artifact |
| `00-GOAL.md` (package) | `3799710118a32d6aeaf2f2fdc9524f779ba4d1132318e1a7422413df44fbfa81` | sections (L9) |
| `01-AUDIT.md` (package) | `738d6a5a7dde17e444a594c1116da7322f2b0b127cc000c43c835f7f4e65aacf` | sections (§8.1 A-30) |

---

<a id="db-source-line-29"></a>
## A. 输入 / 依赖 / 形状（#1–#5）

**#1 LEARN-TURNER-INPUT-HASHES** · `fact` · `supported` · `[史料]`
- 四项 `input_hashes`（card / dossier / corpus / AUDIT coverage-manifest）开工 `sha256sum` 实测，与 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） turner 条目（L863-873，sha `e1ec2d11ed3b3458a2e233a101319ffdf12d253b22562a97d4e25618b1158ce9`）及 AUDIT `RESULT.md §2` / `receipt.json:45-59` 登记值一致。
- source_ref: 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） L863-873 `artists[turner] card_sha256/dossier_sha256/corpus_sha256/corpus_quotes=19/images_public=6` · read_scope `sections` · sha `e1ec2d11…8ce9` · `available`；内部证据 46618e91f52eeebd（未公开；来源记录由维护者保留） §2 · `artifact` · `available`。

**#2 LEARN-TURNER-DEPENDENCY-ACCEPTED** · `fact` · `supported` · `[史料]`
- `AUDIT-turner` = ACCEPTED：`review-gate-receipt.json:13` verdict=accepted、`:14` blocking_defects=0、`:11` reviewer_model=glm-5.3-flash、`:17-32` checks（dual_account_verified / c10_ownership_verified / verify_receipt_exit=0 / rerun_by_reviewer=true）；`receipt.json:6` status=accepted。本 lane 不重审。
- source_ref: 内部证据 d1cff3b8e413de68（未公开；来源记录由维护者保留） L11-32 · `artifact` · sha `f5e6e30f…fe98` · `available`；内部证据 2eb823fca36640c0（未公开；来源记录由维护者保留） L6/`L45-59` · `artifact` · sha `c323dc5c…9b12`（本 lane 实测） · `available`。

**#3 LEARN-TURNER-A30-SHAPE** · `fact` · `supported` · `[史料]`
- `01-AUDIT.md:271` 八节形状（前置知识 / 重点作品及来源 / 要观察的机制 / 具体练习 / 可观察结果 / 常见失败 / 下一步 / 使用边界）；`:273`「练习效果尚未由人完成或评价时，明确为建议练习，不写『已证实学习收益』」。本 lane [learning_path.md](learning_path.md) §1–§8 齐备，抬头标「建议练习」。
- source_ref: `01-AUDIT.md (package)` L271/L273 §8.1 A-30 · `sections` · sha `738d6a5a…aacf` · `available`；[learning_path.md](learning_path.md) §1-§8 · `artifact` · `available`。

**#4 LEARN-TURNER-REQUIRED-KINDS** · `fact` · `supported` · `[史料]`
- `task-registry.json:4584-4588` LEARN-turner `required_artifact_kinds` = `result_summary` / `learning_path` / `mechanism_notes` / `claim_evidence_map`；`:4577-4578` allowed_write_paths = 内部证据 6a2ee5cd8f7c5f53（未公开；来源记录由维护者保留）；`:4574-4575` dependencies = `AUDIT-turner`。四者齐备，`how_to_think` 为模板交付物 #2 追加登记（与 LEARN-monet 同口径）。
- source_ref: 内部证据 4ae7502a27185a8e（未公开；来源记录由维护者保留） L4569-4590 LEARN-turner 条目 · `sections` · sha `7daf31bb…c374` · `available`。

**#5 LEARN-TURNER-CARD-VERBATIM** · `observation` · `supported` · `[史料]`
- [turner.md](../../modules/turner.md) §8.1/§8.2/§4 与 dossier 逐字一致；AUDIT `raw/extract-check.out` 末行 `checks=228 ok=228 fail=0` exit 0（`claims.csv:2` TURNER-CARD-VERBATIM）。本 lane 用实测行号 + 子串，不依赖漂移行号。
- source_ref: `raw/extract-check.out` (AUDIT-turner) last line · `artifact` · `available`；[turner.md](../../modules/turner.md) L46-54/L56-94 · `fulltext` · sha `e3a2dcb2…b372` · `available`。

---

<a id="db-source-line-53"></a>
## B. 大气光效（#6–#12，本轮重点）

**#6 大气包络 P1/§8.2-1** · `observation` · `supported` · `[归纳]`
- 「远景（地平线带上 1/3）对比度 ≤ 近景 40%（强档；中档 40–60%）；从近到远单调下降 R²≥0.8」；P1 强档「远景对比 ≤40%，地平线溶解、全画向单一色光收拢（《暴风雪》档；**莫奈强档之外**）」。
- source_ref: [turner.md](../../modules/turner.md) L48 §8.2-1 / L58-62 P1 · `sections` · sha `e3a2dcb2…b372` · `available`；[turner.md](../../dossiers/turner.md) L235 / L76-80 / L228 强度调节 · `sections` · sha `3e26685f…a2f4` · `available`。

**#7 单一亮核 + 径向 glow P5/§8.2-4 + §8.1** · `observation` · `supported` · `[归纳]` + prompt 词
- 「全帧亮度前 0.5% 像素集中于单一连通域；径向亮度剖面单调不增 R²≥0.7；其他区域亮度峰值 ≤ 光源区 80%」；§8.1「single dramatic light source … radial glow spreading through mist」「light glowing from beneath the surface」。
- source_ref: [turner.md](../../modules/turner.md) L51 §8.2-4 / L83-88 P5 / L24-27 §8.1 正向 · `sections` · sha `e3a2dcb2…b372` · `available`；[turner.md](../../dossiers/turner.md) L238 / L32-33 §1-1/1-2 · `sections` · sha `3e26685f…a2f4` · `available`。

**#8 亮暖暗冷 P4/§8.2-3** · `observation` · `supported` · `[归纳]`
- 「暗部 L≤25% 平均 H∈[230°,290°]；亮部 L≥75% 平均 H∈[20°,60°]或向白推 S≤35%；中性灰 S≤8% 占比 ≤10%」；§8.1「warm light — white, gold, orange, crimson — against cool violet-blue shadows, no neutral greys」。
- source_ref: [turner.md](../../modules/turner.md) L50 / L77-81 / L29-30 · `sections` · sha `e3a2dcb2…b372` · `available`；[turner.md](../../dossiers/turner.md) L237 / L95-99 · `sections` · sha `3e26685f…a2f4` · `available`。

**#9 边缘溶解 P2/§8.2-2** · `observation` · `supported` · `[归纳]`（Tate 描述 `[研究]`）
- 「主体边缘区最大梯度 ≤ 全帧最大梯度 30%（强档）/30–60%（中档）；强档下地平线带不得出现全帧最大梯度——最强边缘必须属于光源或动势线」；Tate「no outlines – edges are blurred…」。
- source_ref: [turner.md](../../modules/turner.md) L49 / L64-68 / L38 负向「crisp horizon line」 · `sections` · sha `e3a2dcb2…b372` · `available`；[turner.md](../../dossiers/turner.md) L236 / L34 §1-3 / L82-86 · `sections` · sha `3e26685f…a2f4` · `available`。

**#10 透明叠色 / 发光感 P6/§8.2-6 + 技法来源** · `observation` · `supported` · `[归纳]`（技法 `[研究]`）
- 「高光区 L≥85% 饱和度 ≤50%（发光感非白颜料堆砌）；全画饱和度 ≤75%；亮部笔触/层痕密度 ≥ 暗部 1.2×」；技法源 `dossiers/turner.md:47` §2-1 水彩逻辑移植油画（[R4] Tate × [R9] Met，CC-1 **CONFIRMED** 双源，`:283`）。
- source_ref: [turner.md](../../modules/turner.md) L53 / L90-94 / L27 · `sections` · sha `e3a2dcb2…b372` · `available`；[turner.md](../../dossiers/turner.md) L240 / L47 / L49 / L283 · `sections` · sha `3e26685f…a2f4` · `available`。

**#11 事件动势 + 完整度 P3/§8.2-5/-7** · `observation` · `supported` · `[归纳]`
- 「主方向能量 ≥60%、旋涡则唯一涡心（画面 30–70% 区）、天气元素位移 ≤3px/帧禁硬切、实体对象不作物件级动画」；「≥1 天气事件元素、覆盖 ≥40%、全画动势方向一致」。
- source_ref: [turner.md](../../modules/turner.md) L52 / L54 / L70-75 · `sections` · sha `e3a2dcb2…b372` · `available`；[turner.md](../../dossiers/turner.md) L239 / L241 / L88-93 · `sections` · sha `3e26685f…a2f4` · `available`。

**#12 大气光效 = A1–A5 合成（教学重组）** · `observation` · `supported` · `[归纳]`
- 无独立「大气光效」规则；#6–#10 的合成可读结果，光核与溶解争梯度时按 §8.2-2 光核优先。这是本 lane 的 `[归纳]` 重组，不冒充已验证单条规则。
- source_ref: [turner.md](../../modules/turner.md) L48-53 / L24-30 · `sections` · sha `e3a2dcb2…b372` · `available`；[mechanism_notes.md](mechanism_notes.md) §3.1 · `artifact` · `available`。

---

<a id="db-source-line-85"></a>
## C. 水体反光（#13–#17，本轮重点，诚实）

**#13 档案无独立「水体反光」数值规则** · `fact` · `supported` · `[史料]`（缺口登记）
- §8.2 七条（L48-54）、§4 六参数（L58-94）逐条核对，无水面反射阈值；`conflicts.md` 18 条 C 无「水体反光」行。本 lane 不虚构、不把教学重组写成已验证判分规则。
- source_ref: [turner.md](../../modules/turner.md) L48-54 / L58-94 全文扫描 · `fulltext` · sha `e3a2dcb2…b372` · `available`；`conflicts.md` §C 总表 L30-49 全文扫描 · `sections` · sha `314a24da…bbef` · `available`。

**#14 锚点1 — 水面反射为主 / 火光与水光** · `observation` · `supported` · `[归纳]`（练习级）
- `dossiers/turner.md:406` §12-3「对同一夜事件画两稿…其中一稿**以水面反射为主**；水彩稿练「湿时擦除」留出**火光与水光**」；`:404`「反转明暗——建筑苍白、火为主光源」。
- source_ref: [turner.md](../../dossiers/turner.md) L403-406 §12-3 · `sections` · sha `3e26685f…a2f4` · `available`。

**#15 锚点2 — 水面构图 ≥50% / 把场景写成光** · `observation` · `supported` · `[归纳]`（构图级）
- `dossiers/turner.md:408-410` §12-4「水面与船群为主部」「把『场景』写成『光』」「水面构图 ≥50%」「建筑只留 2 个可辨特征」。
- source_ref: [turner.md](../../dossiers/turner.md) L407-410 §12-4 · `sections` · sha `3e26685f…a2f4` · `available`。

**#16 锚点3 — §8.1 正/负向措辞** · `observation` · `supported` · `[归纳]`（prompt 措辞）
- `modules/turner.md:27`「light glowing from beneath the surface」；`:39` 负向禁「calm static water」；`:38` 禁「flat even lighting」、`:41` 禁「smooth clean digital gradients」。
- source_ref: [turner.md](../../modules/turner.md) L19-44 §8.1 · `sections` · sha `e3a2dcb2…b372` · `available`。

**#17 水体反光 = 三锚点 + B1/B2 教学重组** · `observation` · `partial` · `[归纳]`
- B1（归属）：`modules/turner.md:75` P3 注「静水波纹属莫奈领域（其 §4 P5）；本参数只覆盖事件级动势」、`:101` 冲突注记、`dossiers/turner.md:70` 边界写死 → 水面只承载事件光反射。B2（不反客为主）：借 `:51` §8.2-4「其他区域亮度峰值 ≤ 光源区 80%」精神 → 反射不得成第二连通域。**B2 是练习自律，不是档案数值规则**，故整条标 `partial`（三锚点 supported、重组部分为本 lane 归纳，未经人评/实验）。
- source_ref: [turner.md](../../modules/turner.md) L75 / L101 / L51 / L39 · `sections` · sha `e3a2dcb2…b372` · `available`；[turner.md](../../dossiers/turner.md) L70 / L403-410 · `sections` · sha `3e26685f…a2f4` · `available`；[learning_path.md](learning_path.md) §3-B / [mechanism_notes.md](mechanism_notes.md) §3.2 · `artifact` · `available`。

---

<a id="db-source-line-109"></a>
## D. 冲突行 / 边界（#18–#21）

**#18 C-10 = 莫奈 × 塞尚，所有权归莫奈；Turner 非 party** · `observation` · `supported` · `[史料]` + `[归纳]`
- `conflicts.md:41` C-10 行「莫奈 × 塞尚 | 深度衰减」；`:180` 莫奈侧「远景对比 ≤60% + 单调梯度 R²≥0.8」「§4 P3 强档（雨/雾/晨昏；**边界外=透纳领域**）」；`:181` 塞尚侧「反大气透视 + 空间压缩」；`:184` 分层解；`:186` E2c 待补。Turner 只在 `:180` 被点名为边界外，不是 party。
- source_ref: `conflicts.md` L41 / L176-186 · `sections` · sha `314a24da…bbef` · `available`；`AUDIT-turner/claims.csv` TURNER-C10-BOUNDARY / -TRIPLE（行 10-11）· `sections` · sha `114fbcb2…fa62` · `available`。

**#19 「边界外=透纳领域」三路互证** · `observation` · `supported` · `[归纳]`
- `dossiers/monet.md:89`（强档「边界外=透纳领域」）/`:195`「不要进入透纳的『灾难天气』档：那里应换模块」；`dossiers/turner.md:6`（分工写死）/`:70`（越过该档归透纳）/`:79`（强档「《暴风雪》档；莫奈强档之外」）；`modules/turner.md:100`（灾难天气/事件动势/边缘完全溶解归透纳）。AUDIT `RESULT.md §5`、`review-evidence.md §2` 已复核（含 bare-name locator 澄清：L89/L195 属 dossier monet.md，非 98 行模块卡）。
- source_ref: [turner.md](../../dossiers/turner.md) L6 / L70 / L79 · `sections` · sha `3e26685f…a2f4` · `available`；[turner.md](../../modules/turner.md) L100-101 · `sections` · sha `e3a2dcb2…b372` · `available`；`AUDIT-turner/review-evidence.md` §2/§6 · `sections` · sha `325ae43f…3bf4` · `available`。

**#20 C-05 非 Turner 冲突** · `observation` · `supported` · `[史料]`
- `conflicts.md:36`「C-05 达·芬奇 × 梵高/莫奈/塞尚 笔触可见度」、`:109-122` 正文；Turner 全文不出现。AUDIT `counterexample.md` CX-9 登记为 attribution note（莫奈既是 C-05 party 又是 Turner 边界伙伴），不发明 Turner 规则。
- source_ref: `conflicts.md` L36 / L109-122 · `sections` · sha `314a24da…bbef` · `available`；`AUDIT-turner/counterexample.md` CX-9 · `sections` · sha `3687f598…532d` · `available`。

**#21 N3/N4 处置口径** · `observation` · `supported` · `[归纳]`
- `conflicts.md:311-312` N3 轴所有权表（每轴一个持有者、冲突轴 §8.2 整条移除）；`:314` N4 可拆/不可拆判别。仅组合卡场景适用，单模块决策序不触发；本 lane 不改写 Turner 任何规则。
- source_ref: `conflicts.md` L305-315 / L332-333 · `sections` · sha `314a24da…bbef` · `available`。

---

<a id="db-source-line-129"></a>
## E. 双账户 CC-2（#22–#26，本轮点名，诚实）

**#22 v1 抽取契约不变（A-20/A-59 共存）** · `observation` · `supported` · `[史料]`
- `dossiers/turner.md:308` marker「wave16p2 加固（GOALS A-59）：新增 §11/§12…**v1 抽取契约 §4/§8.1/§8.2 不受影响**」；`GOALS.md:34`（A-20 wave12，dossier 底座）/`:65`（A-59 纯插入 +134/0）。AUDIT `claims.csv` TURNER-DUAL-ACCOUNT-COEXIST。
- source_ref: [turner.md](../../dossiers/turner.md) L306-308 · `sections` · sha `3e26685f…a2f4` · `available`；`ops/GOALS.md` L34 / L65 · `sections` · sha `2727d1f0…1144` · `available`。

**#23 等级分裂 = 记录 CONFIRMED / 事实 WEAKENED** · `observation` · `supported` · `[归纳]`
- `dossiers/turner.md:284` §9 CC-2「主体一致、真伪存疑点已并列；**记录 CONFIRMED / 事实 WEAKENED**」；`:445` 自审 B1「Holcomb 质疑其与 Vernet 轶事相似、`Ariel` 船名无法核实 → **WEAKENED**（档案已按「他声称／记录如此」表述，双说并存）」。
- source_ref: [turner.md](../../dossiers/turner.md) L283-284 / L445 · `sections` · sha `3e26685f…a2f4` · `available`；`AUDIT-turner/claims.csv` TURNER-DUAL-ACCOUNT-GRADE（行 8）· `sections` · sha `114fbcb2…fa62` · `available`。

**#24 语料层 q10 = [reported speech] + 两说并存** · `observation` · `supported` · `[史料]`
- `_corpus/turner.md:85-91` q10 全句「lashed for four hours」、类型 `[reported speech]`、注「Adele Holcomb 曾质疑…但 Kingsley 的记录表明 Turner 本人坚持其真——**两说并存**」；`INDEX.md:30` turner 行「『绑桅四小时』记录链双说并存」。
- source_ref: [turner.md](../../dossiers/_corpus/turner.md) L85-91 · `citation_context` · sha `3de20324…e142` · `available`；[INDEX.md](../../dossiers/_corpus/INDEX.md) L30 · `sections` · sha `b74bf44f…65b4` · `available`。

**#25 单一原始来源同时持有两说** · `observation` · `supported` · `[史料]`
- AUDIT `counterexample.md` CX-1：Tate N00530 目录条目 L7「no ship called Ariel is known…」+ L8「Adele Holcomb has cast doubts… **AND** Ruskin added a report of a conversation between Rev. William Kingsley and Turner in which the artist stressed the truth」；`kingsley_seg.txt` L1 逐字「lashed for four hours」。两说在同一捕获条目并存，不是断言。
- source_ref: `AUDIT-turner/counterexample.md` CX-1 · `sections` · sha `3687f598…532d` · `available`；`AUDIT-turner/claims.csv` TURNER-DUAL-ACCOUNT-PRIMARY（行 7）/ `raw/quote-spotcheck.out` · `artifact` · `available`。

**#26 本 lane 对 CC-2 的处置（诚实带过）** · `observation` · `supported` · `[归纳]`
- 作为《暴风雪》接受史并存记载读；不作 [自述] 事实、不作心理推断依据、不删任一说、不升级确证；v1 抽取契约不受影响。§10 `Ariel` 未决、「The sun is God」未采信、Q5 两跳 `[UNVERIFIED 直源]` 保持 unknown。
- source_ref: [turner.md](../../dossiers/turner.md) L289-302 §10 / L445 / L476-477 · `sections` · sha `3e26685f…a2f4` · `available`；[how-to-think.md](how-to-think.md) §5 · `artifact` · `available`。

---

<a id="db-source-line-153"></a>
## F. 等级 / 边界 / 诚实声明（#27–#33）

**#27 How to Think 分栏 + [推测]=0** · `observation` · `supported` · `[归纳]`
- `00-GOAL.md:9`「How to Think 必须区分作者可核实的自述与研究者推断，不能编造作者心理」；`dossiers/turner.md:4` 五级定义。[how-to-think.md](how-to-think.md) §0 四栏（A 作者言语 / B 史料研究 / C 操作规则 / D 禁止）、§4 反心理推断清单 4 条、§6 `[推测]` 计数=0。
- source_ref: `00-GOAL.md (package)` L9 · `sections` · sha `37997101…fa81` · `available`；[how-to-think.md](how-to-think.md) §0/§4/§6 · `artifact` · `available`。

**#28 练习 = 建议练习，未写「已证实学习收益」** · `fact` · `supported` · `[史料]`
- `01-AUDIT.md:273`；[learning_path.md](learning_path.md) 抬头 + §4 声明 + §8；`human_review=not_applicable`。
- source_ref: `01-AUDIT.md (package)` L273 · `sections` · sha `738d6a5a…aacf` · `available`；[learning_path.md](learning_path.md) 抬头/§4/§8 · `artifact` · `available`。

**#29 card_has_81b=false 为 gap，STYLE-turner 独立任务** · `fact` · `supported` · `[史料]`
- AUDIT `RESULT.md §6.1`、`coverage-manifest.json`「card_has_81b=false gap explicit」、ledger `artist-shards.json:865`；AUDIT `counterexample.md` CX-10 明确「extractor 228/228 只证明 §8.1/§8.2/§4 逐字匹配，**不**证明 E4」。本 lane 不起草 §8.1b、不声称 E4。
- source_ref: `AUDIT-turner/coverage-manifest.json` module_card.card_has_81b / card_has_81b_gap · `sections` · sha `6d6809ec…8f93` · `available`；`AUDIT-turner/counterexample.md` CX-10 · `sections` · sha `3687f598…532d` · `available`。

**#30 P1/P2 是否同一物理量 = 未决** · `observation` · `unverified` · `[归纳]`
- `dossiers/turner.md:479` 自审 D-8「若 P2 边缘溶解与 P1 大气能见度在实测中不可分…两参数需合并——已为两者保留独立自查项供实验检验」。本 lane 不合并、不裁决，如实登记。
- source_ref: [turner.md](../../dossiers/turner.md) L479 · `sections` · sha `3e26685f…a2f4` · `available`。

**#31 外部来源 / 图像边界** · `fact` · `supported` · `[史料]`
- 外部 URL（R1–R38：Tate/NG/Met/MoMA/MFA/archive.org/Gutenberg/Wayback 等）本轮未重访，`access_status=unknown`；6 张公开图未目检（无 `image_seen`），权利沿用 `_images/turner/MANIFEST.md`（5 PD + 1 CC BY 3.0，norham 需署名）+ AUDIT `rights_review.md`。作品版本钉死：burning_houses = 克利夫兰 1942.647（AUDIT CX-5），不与费城本/泰特本混称。
- source_ref: `AUDIT-turner/coverage-manifest.json` images / gaps_and_boundaries / not_claimed · `sections` · sha `6d6809ec…8f93` · `available`；`AUDIT-turner/counterexample.md` CX-4/CX-5 · `sections` · sha `3687f598…532d` · `available`。

**#32 E2c 莫奈+塞尚待补 + 规则层 ≠ 实验验证** · `observation` · `supported` · `[归纳]`
- `conflicts.md:186` E2 建议加「莫奈+塞尚」组（现表无）；本 lane 不重跑 A-12/E2，C-05/C-10/C-14 标签是规则层 `[归纳]` 判断，非实验验证。`submitted ≠ accepted`。
- source_ref: `conflicts.md` L186 / L332-333 · `sections` · sha `314a24da…bbef` · `available`。

**#33 写入边界 / 无 repo 写** · `fact` · `supported` · `[史料]`
- 仅写 内部证据 6a2ee5cd8f7c5f53（未公开；来源记录由维护者保留）（`task-registry.json:4577-4578`）；仓库只读、无 git 操作、无子代理派发、无凭据、无 `image_seen`。`author_actor_id=LearnTurner`、`review=null`（author 不自我验收）、`status=submitted`。
- source_ref: 内部证据 4ae7502a27185a8e（未公开；来源记录由维护者保留） L4577-4578 / L4569-4590 · `sections` · sha `7daf31bb…c374` · `available`；内部证据 46618e91f52eeebd（未公开；来源记录由维护者保留） §7/§8 · `artifact` · `available`。

---

<a id="db-source-line-185"></a>
## G. 汇总

- 论断总数 **33**：`supported` 30 / `partial` 1（#17 水体反光教学重组）/ `unverified` 1（#30 P1/P2 未决）/ `conflict` 0（C-10 已按「非 Turner 冲突」正确归属，无需 conflict 状态；行号漂移见 #19 澄清，不单列 conflict）/ `not_applicable` 0。
- 等级分布：操作/重组 `[归纳]` 为主体；技法来源 `[研究]`（#10）；史料/登记 `[史料]`（输入哈希、冲突表、CC-2 记录链、A-30 形状）；**`[自述]` 升级 = 0、`[推测]` = 0**。
- 三分母不混称：本 lane 复核的对象数 = 13 个输入/来源文件（见上表）；复核的论断数 = 33；AUDIT 上游已 inventoried/reviewed/supported 的分母另见其 `coverage-manifest.json`，本 lane 不重算、不混称。
- 「来源存在 ≠ 来源支持」：外部 URL 均 `access_status=unknown`，只作为档案内登记值引用，不作为本轮 re-visit 支持。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
