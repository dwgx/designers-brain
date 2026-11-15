<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-hokusai；原正文 SHA-256 `4c90af82877458cf1db2c750a61c4e5fe61793fcdb6668ef80b35b7ebe4839fc`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-hokusai — claim_evidence_map.md（逐条 locator）

> 任务 `LEARN-hokusai` ｜ 仓库只读 @ `f008952365a77e140cbda3f3959d43ef000f9a22` ｜ 证据基线 `AUDIT-hokusai`（ACCEPTED）。
> **本文件把 [learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md) 的每条主张映射到具体 locator + 证据级 + 支持状态。** 不新增史实、不新增 URL、不重审 AUDIT。

<a id="db-source-line-6"></a>
## 0. 来源代号与 SHA-256（冻结 head 实测 / AUDIT 实测）

| 代号 | 路径 | SHA-256 | 读范围 |
|---|---|---|---|
| **D** 档案 | [hokusai.md](../../dossiers/hokusai.md)（453 行） | `d03a260ccb0eeab64cb6b008ff6ae4a247456dbb0891c87d172c3708de0e330f` | `fulltext` / `sections` |
| **B** 模块卡 | [hokusai.md](../../modules/hokusai.md)（80 行） | `3a05011d61731596ab4a7309564d875112df87129cb68cddb70a7941646e62c2` | `fulltext` |
| **C** 语料 | [hokusai.md](../../dossiers/_corpus/hokusai.md)（140 行，19 quotes） | `a0ab837a967bba2f1e02c81614b7152a2a3addf84e20d82b74b1b6ac49d3aeb5` | `citation_context`（转录，原刊未直读） |
| **CF** 冲突清单 | [conflicts.md](../../../../cross/conflicts.md)（421 行） | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | `sections` |
| **AM** AUDIT coverage-manifest | 内部证据 555647794d78584b（未公开；来源记录由维护者保留） | `7241947f187f930f8237675cbd79989ac2bdcb84219c516a17f9698e620e0d87` | `fulltext` |
| **AR** AUDIT RESULT | 内部证据 44e740af1fedbf85（未公开；来源记录由维护者保留） | `e8b5e1fb1b9ac0fcb2eca0dd791e213ea9a323c29f1eabb610a218a6766c803d` | `fulltext` |
| **AC** AUDIT claim_evidence_map | 内部证据 9b3c0da133d01164（未公开；来源记录由维护者保留） | `8fc065d8562209156e3eb63ca14e78ed8f5b93941251013a373342877ddca874` | `fulltext` |
| **A30** 绑定形状 | `<package>/01-AUDIT.md` §8.1 `:269-274`（A-30） | 包内 SHA256SUMS 记录 `01-AUDIT.md` = `…`（见 SHA256SUMS:2） | `sections` |
| **TBR** task brief | `<package>/templates/task-brief.md` | 模板（未执行） | `sections` |

> SHA 由本 lane `sha256sum` 实测（D/B/C/CF）与 AUDIT 目录文件实测（AM/AR/AC），与 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） artists[25] 及 AUDIT RESULT §1 `:16-22` 一致。`retrieved_bytes_sha256` 在 receipt.claims 里用这些值。

<a id="db-source-line-22"></a>
## 1. Locator 约定

- `D:199` = 档案第 199 行（冻结 head 实测）；`D:199-205` = §8.2 规则 1–7；`D:73-78` = §4 P1–P6 表；`B:45` = 模块卡第 45 行。
- **行号是冻结 head 实测值**，不是 conflicts.md 里漂移的旧号。`CF:136` 等是 conflicts.md 自身的 section/detail 行号（稳定），但其**正文内** `hokusai.md L188/L189/L193` 已过期 → 见 §5 漂移表。
- 证据级：`[自述]`/`[史料]`/`[研究]`/`[归纳]`/`[推测]`（D:5）；`[自述]`(转述) 单列（C:4、AR §2）。
- 支持状态：`supported`（有 locator + 可读字节）/ `partial`（转录、非一手）/ `conflict`（冲突行记录）/ `unverified`（阈值未实测 / 词条无源）。

---

<a id="db-source-line-31"></a>
## 2. LP（learning_path.md）主张 → locator

| # | 主张（简） | 位置 | locator | 级 / 状态 |
|---|---|---|---|---|
| LP-01 | 8-section A-30 §8.1 形状（前置知识/作品/机制/练习/结果/失败/下一步/边界） | LP §1–§8 | A30 `:271-273`（01-AUDIT.md）；02-EXECUTION-PLAN Lane B `:62-64` | `[归纳]` supported |
| LP-02 | 等宽线 + 平涂是表面系统开关；「平涂 vs 排线」互斥 | LP §1.1、§3.3 | D `:29`(§1-1)、`D:199`(§8.2-1)、`B:45`、`CF:136`(C-07) | `[归纳]`/`[研究]` supported |
| LP-03 | 普鲁士蓝主导 ≥40%、留纸当高光 | LP §1.2、§3.3 | D `:30`(§1-2)、`D:37`(§1-9)、`D:200`(§8.2-2)、`B:46` | `[研究]`/`[史料]` supported |
| LP-04 | 波浪线组 / 曲线族 ≥3 级同向嵌套（第一强调） | LP §1.3、§3.1、§4 L1、§5 | D `:33`(§1-5)、`D:53`(§2-10)、`D:202`(§8.2-4)、`D:76`(P4)、`B:48`、`AM per_quote` 无直接（属图像机制） | `[归纳]`/`[研究]` supported |
| LP-05 | 远近挤压 ≤前景 1/4、上/下 1/3 带、1 条 15°–45° 主斜线、无消失点（第一强调） | LP §1.4、§3.2、§4 L2、§5 | D `:32`(§1-4)、`D:52`(§2-9)、`D:201`(§8.2-3)、`D:203`(§8.2-5)、`D:74-75`(P2/P3)、`B:47/:49` | `[归纳]`/`[研究]` supported |
| LP-06 | 绘→雕→印分工条款（原稿贴版即毁、书信纠正刻法、附样式示例；「大分工」强调） | LP §1.5、§3.6、§4 L3 步4、§5 第8行 | D `:50`(§2-7 `[史料]` [R1])、`D:46`(§2-3 一版一色)、`D:48`(§2-5 bokashi)、`AR §2` | `[史料]` supported + `[归纳]` 操作化 |
| LP-07 | 人物剪影 ≤1/8、≤6 线、不遮峰；留白 ≥35% | LP §1.6、§3.4/5、§5 | D `:34`(§1-6)、`D:35`(§1-7)、`D:204`(§8.2-6)、`D:205`(§8.2-7)、`D:77-78`(P5/P6) | `[归纳]` supported |
| LP-08 | §4/§8.2 阈值为 `[归纳]` 未实测、原作未像素测量 | LP 头注、§5 注、§8 | D `:453`(自审 D「我仍赌错的是什么」)、`D:253`(§10 缺口 7)、`AR §7(3)` | `[归纳]` unverified(诚实) |
| LP-09 | 语料 19 条 typing 已核、但 transcription-only、read_scope=citation_context | LP §1.7 | C `:5`/`:138-140`、`AM denominators/notes :6-27`、`AR §2 :26-55`、`AM per_quote :28-48` | `[史料]` partial |
| LP-10 | locator drift L188/189/193→199/200/204 known-open | LP §1.8、§6 注、§8 | `AR §3 :57-70`、`AM per_conflict :49-54`、`CF:136/:203/:258/:272` | observation supported |
| LP-11 | `возвращ` / 大返回词条无源 → 映射到曲线族同向回归 + 分工条款 | LP §3.1、§7.5、§8（EM-00） | 全仓 grep 无命中（仅 aivazovsky 俄文抓取，无关）；锚点 `D:202`/`D:50` | `[推测]` unverified / known-open |
| LP-12 | 重点作品 10 件（组）及来源沿用现有记录、3 张公共图 CC0(Met) | LP §2 表 | D `:16-21`(§0)、`D:344-397`(§12)、`D:215-234`(§9)、`AR §4 :72-76`、`AM :13-15` | `[史料]`/`[研究]` supported |
| LP-13 | 3 阶梯练习全为「建议练习」、无「已证实学习收益」 | LP §4 全 | A30 `:273`（01-AUDIT.md「明确为建议练习，不写已证实学习收益」）、`TBR`:接受标准 | `[归纳]` supported |
| LP-14 | L1 三级曲线族单色稿（步骤沿用 §12.1） | LP §4 L1 | `D:348-351`(§12.1)、`D:202`(§8.2-4)、`D:199`/`D:200` | `[归纳]` supported |
| LP-15 | L2 远近挤压 + 极简留白（步骤沿用 §12.2/12.3） | LP §4 L2 | `D:353-356`(§12.2)、`D:358-361`(§12.3)、`D:201`/`:203`/`:204` | `[归纳]` supported |
| LP-16 | L3 系列化 + 分工交接（步骤沿用 §12.9/12.6/12.4） | LP §4 L3 | `D:388-391`(§12.9)、`D:373-376`(§12.6)、`D:363-366`(§12.4)、`D:50`(§2-7) | `[归纳]` supported |
| LP-17 | 4 条冲突作为失败条件（C-07/12/16/17） | LP §6 表 | `CF:136/:203/:258/:272`、`AM per_conflict :49-54`、`B:70-73`(冲突注记) | observation supported |
| LP-18 | §8.1 `--no` 是生成护栏、非历史断言 | LP §6 注、§8 | `D:192`(§8.1 禁令范围)、`D:184-189`(负向段)、`B:30-37` | `[归纳]` supported |

---

<a id="db-source-line-56"></a>
## 3. HT（how-to-think.md）主张 → locator

| # | 主张（简） | 位置 | locator | 级 / 状态 |
|---|---|---|---|---|
| HT-01 | 严格 `[自述]` vs `[归纳]`/`[推测]` 分栏；不发明心理 | HT §0、§3 | `D:5`(分级定义)、`C:4`(typing 映射)、`AR §2 :26-55`、`D:405-413`(自审 B 反证) | supported |
| HT-02 | `[自述]` 非空但有限：仅修业志向/方法论（Q1/Q5/Q6/§5 六条/Q19），不含量化机制 | HT §0 | `D:84-110`(§5 自述 6 条)、`C:9-13`(Q1)、`C:37`(Q5)、`C:43`(Q6)、`C:129`(Q19)、`AM per_quote :28-48` | `[自述]` partial(转录) |
| HT-03 | Q14/Q16 = `[reported speech]` 转述、非 primary；Q13/Q15/Q17/Q18 = `[史料]` | HT §0、§3 | `C:4`、`AR §2 :46/:48/:45/:47/:49/:50`、`AM per_quote :41-47` | `[史料]`/`[自述]`(转述) supported |
| HT-04 | 步1 曲线族决策（≥3 级/同向弯/牺牲写实水花） | HT 步1 | `D:33`、`D:53`、`D:202`、`D:76`、`B:48`、`C:9-13`(Q1 气质参考) | `[归纳]`+`[研究]`+气质`[自述]`(非判据) |
| HT-05 | 步2 远近挤压决策（**无自述支撑，不编动机**） | HT 步2 | `D:32`、`D:52`、`D:201`/`:203`、`D:74-75`、`B:47/:49` | `[归纳]`+`[研究]`（明确无自述） |
| HT-06 | 步3 表面系统（等宽线/平涂/蓝 ≥40%）+ C-07/C-12 失效 | HT 步3 | `D:199`/`:200`/`:37`/`:46`/`:47`、`CF:136`/`:203` | `[归纳]`+`[史料]`+`[研究]` |
| HT-07 | 步4 留白 ≥35% + C-17 定义对齐（空白 vs 留白） | HT 步4 | `D:204`/`:34`/`:48`、`CF:272` | `[归纳]`+`[史料]` |
| HT-08 | 步5 人物剪影 + §6.3 北斋/歌麿分档（不写「人在自然前无力」的心理） | HT 步5 | `D:35`、`D:144-148`(§6.3)、`D:205`、`B:13` | `[归纳]` supported |
| HT-09 | 步6 绘→雕→印参数化交接（大分工）+ `возвращ` 无源 `[推测]` 映射 | HT 步6 | `D:50`(§2-7 `[史料]` [R1])、`D:46`/`:38`、`D:202`；全仓 grep 无源 | `[史料]`+`[归纳]`+`[推测]`(known-open) |
| HT-10 | 步7 版次微错位/木纹（质感、非判据） | HT 步7 | `D:38`(§1-10)、`D:180`(§8.1 prompt)、`B:27-28` | `[史料]`+`[归纳]`(顺序) |
| HT-11 | 每步带证据级；grade 分布诚实说明（7 步里自述仅气质参考） | HT §2 速查表后注 | `D:5`/`:453`、`C:4`、`AR §2` | supported |
| HT-12 | no invented psychology：不写「他想…」；强反例 Obrist/浪高/15卷/马蒂斯传承 | HT §0 禁止事项、§3 | `D:409-413`(自审 B)、`D:135`(§6.2 第7条 `[推测]`)、`D:249`(§10 缺口4)、`D:192` | supported |
| HT-13 | 转录-only 语料 read_scope=citation_context | HT §0、§3 | `C:5`/`:138-140`、`AR §2 :55`、`AM notes :23-26` | partial(诚实) |

---

<a id="db-source-line-76"></a>
## 4. MN（mechanism_notes.md）主张 → locator

| # | 主张（简） | 位置 | locator | 级 / 状态 |
|---|---|---|---|---|
| MN-01 | §4 六参数表（P1–P6、三档、默认 55/75/80/3级/1/8/40）与用法句 | MN §1 | `D:69-80`(表 `:73-78`、用法 `:80`)、`B:53-64` | `[归纳]` supported |
| MN-02 | §8.2 七规则原文（线宽/色数/构图/曲线族/尺度/负空间/人物） | MN §2 | `D:197-205`、`B:43-51` | `[归纳]` supported |
| MN-03 | 6 参数 → 练习动作 + 自查判据 + 失败条件映射 | MN §1 表 | `D:73-78` × `D:199-205` × `CF:136/:203/:258/:272` | `[归纳]` supported |
| MN-04 | 7 规则 → 练习自查步骤映射 | MN §2 表 | `D:199-205`、`B:45-51`、LP §4 | `[归纳]` supported |
| MN-05 | C-07 处置：着色系统二选一、禁拼接、线宽轴 N3 单主 | MN §3 表 | `CF:136-147`、`CF:311`(N3) | observation supported |
| MN-06 | C-12 处置：色相面积预算表、仅一个 ≥40%、梵高降档写进卡 | MN §3 表 | `CF:203-215`、`CF:314`(N4) | observation supported |
| MN-07 | C-16 处置：反约束带适用域、平涂系必删/加限定 | MN §3 表 | `CF:258-270`、`CF:305`(N1)、`CF:308`(N2) | observation supported |
| MN-08 | C-17 处置：空白 vs 留白定义对齐、分统计 | MN §3 表 | `CF:272-283`、`CF:314`(N4) | observation supported |
| MN-09 | N1/N3/N4/N9 通用口径（引用不改写） | MN §3.1 | `CF:305/:311/:314/:332` | observation supported |
| MN-10 | near-miss #5/#6 非冲突、但需显式取值 | MN §3 注 | `B:74`(冲突注记)、`CF:341` 起(§4 表) | observation supported |
| MN-11 | 8 条 per-mechanism 失败条件速查（M1–M8） | MN §4 | `D:199-205`/`:76`/`:75`/`:50`/`:38`、`CF:136/:203/:258/:272` | `[归纳]` supported |
| MN-12 | §8.2 是判分规则非旋钮；降档必须显式、辅模块冲突轴整条移除 | MN §1 注、§3.1 | `CF:311`(N3)、`CF:214`(C-12 降档写进卡) | observation supported |
| MN-13 | `возвращ` 无源 → 两条确证字节映射（同向回归 / 分工大回环） | MN §4 注 | 全仓 grep 无命中；锚点 `D:202`/`D:50` | `[推测]` unverified / known-open |
| MN-14 | 阈值未实测、不裁断冲突解法、locator drift known-open | MN §0/§5 | `D:453`/`:253`、`AR §3 :57-70`/`§7`、`AM per_conflict :49-54` | `[归纳]` unverified / observation |

---

<a id="db-source-line-97"></a>
## 5. locator drift 对照表（known-open，AUDIT §3）

| 冲突 | conflicts.md 正文旧号 | 真实档案行 | 真实模块卡行 | 证据 |
|---|---|---|---|---|
| C-07 (§8.2-1/-6) | `hokusai.md L188`/`L193` | `D:199`/`D:204` | `B:45`/`B:50` | `AR §3 :63-68`、`AM per_conflict :50` |
| C-12 (§8.2-2) | `L189` | `D:200` | `B:46` | `AR §3 :66`、`AM per_conflict :51` |
| C-16 (§8.2-1/-6) | `L193` | `D:199`/`D:204` | `B:45`/`B:50` | `AR §3 :67`、`AM per_conflict :52` |
| C-17 (§8.2-6, §4 P6) | `L193` | `D:204`/`D:78` | `B:50`/`B:62` | `AR §3 :68`、`AM per_conflict :53` |

> `AR §3 :70` 判定：这是 **pointer 缺陷**（conflicts.md 绝对行号漂移，与 A-38 插入 §11/§12 致档案增至 453 行一致），**冲突条款本身无需改动**；修复属 CONFLICT-07/12/16/17 lane，本 LEARN lane 只读、不修。ledger 记 drift +11（CAMPAIGN-STATE.md `:16`、route-decisions.md `:39/:60`）。

---

<a id="db-source-line-110"></a>
## 6. 支持状态汇总（分母 = 本文件 4 组共 44 条主张：LP 18 + HT 13 + MN 14 + 漂移/元 计 5 条并入）

| 状态 | 条数 | 说明 |
|---|---|---|
| `supported`（有稳定 locator + 可读字节） | 38 | 含 observation / `[归纳]` / `[史料]` / `[研究]` 锚点 |
| `partial`（转录底本、非一手） | 3 | HT-02/HT-13/LP-09：语料 citation_context |
| `unverified`（诚实保留） | 3 | LP-08/MN-14 阈值未实测；LP-11/MN-13/HT-09 `возвращ` 无源 known-open（合并计 1 组） |
| `conflict`（作为失败条件记录，非本 lane 裁断） | 4 行 C-07/12/16/17 | 见 §5、MN §3 |

> 分母声明：上表按「主张组」计，LP 18 / HT 13 / MN 14 = **45 条映射行**；其中 4 条 C 行在 LP-17/MN-05..08 重复出现，按「独立 locator 主张」去重后记入 supported。`unverified` 一律**不填成功值**（schema `support_status` 纪律）。

---

<a id="db-source-line-123"></a>
## 7. 「大返回/возвращ」known-open 专条（EM-00）

- **主张**：brief 强调含 `大 возвращ 分工条款` / `波浪线组+远近挤压机制`；`возвращ`（俄文「返回/回归」词根）在冻结仓库 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） 与 campaign 包内 **无匹配来源**。
- **核验动作**：本 lane 跑 内部证据 b09524fb2e18ceed（未公开；来源记录由维护者保留） → 命中仅 `knowledge/domains/painters/_scratch/aivazovsky/fetches/*`（俄文抓取，主题为 Aivazovsky，与 hokusai 无关）及 `AUDIT-aivazovsky/raw/*.html`。无 hokusai 命中、无 campaign 包命中。
- **不虚构来源**：不写「北斋有大返回理论」、不把 token 塞进 `[自述]`/`[史料]`。
- **可落地的两条确证映射**（`[推测]` + 字节锚点）：① 曲线族「每级重复上级曲率符号」= 同向回归（`D:202`/`B:48`）；② 绘→雕→印「画稿不回作者、由雕/摺分工完成并回传成品」= 分工大回环（`D:50` `[史料]` [R1]）。
- **消费方**：[learning_path.md](learning_path.md) §3.1/§7.5/§8、[how-to-think.md](how-to-think.md) 步 6/§3、[mechanism_notes.md](mechanism_notes.md) §4 注、`RESULT.md` §Known-open、`receipt.claims` EM-00（`support_status: unverified`）、`runner_receipt.json` limitations。
- **待决**：Owner/Main 确认是否另有出处；本 lane 不因不确定而停，按最小可证据化落地。

---

<a id="db-source-line-134"></a>
## 8. 数字与产物边界

- 所有数字可复跑：`sha256sum D B C CF AM AR AC`（见 §0）；`grep -nE '^## |^### ' D`；`grep -nE '^### C-(07|12|16|17)' CF`；`grep -c` corpus 19 quotes（AM `:7`）；行号均为冻结 head 实测。
- 无渲染、无像素测量、无人评、无联网、无凭据、无 repo 写入、无子代理（`spawns_allowed=false`）。
- `review: null`、`status: submitted`；独立审阅为单独 lane，作者不自验自收；`verify-receipt.py` 走 schema-only 分支（脚本 `:20-21`）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
