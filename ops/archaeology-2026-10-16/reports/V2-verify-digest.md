STATUS: DONE

# V2 · 独立抽查 — `ops/session-digest.md` 与 `02-digest-waves12-21.md` 声明准确性

> 验证者：**VerifyDigest**（独立；非被验产物作者）· 只读取证；未改 digest、未 commit。
> 时点：2026-10-16 10:30–10:50 JST（各命令含时点/口径注记）。
> 对象：`ops/session-digest.md`（本波更新版；磁盘实测 **182 行** / 32,347 B / mtime 10:14:23；任务描述称 184 行——见「说明项 4」）＋ `ops/archaeology-2026-10-16/reports/02-digest-waves12-21.md`（170 行）。
> 判定词汇：CONFIRMED / WEAKENED / FAILED / [UNVERIFIED]。

## 0 · 总判

- 指定抽查 8 条：**7 CONFIRMED · 1 WEAKENED · 0 FAILED**（第 7 条 2/3 子项吻合，jsonl 数差 1：144 → 145）。
- 另注记 1 项（§1 GOALS 数字）：**WEAKENED**（时点差——A-107 已于核验前收口）。
- **总判：PASS（成立）**——未发现虚构、伪造或结论性错误；2 处 WEAKENED 均为计数口径/时点差问题，已列修正建议（3 条修正 + 1 条说明，≤5）。
- 覆盖面：§1×4（语料 / 图库 / checks / GOALS 注记）、§2×2（wave21 / 收口三工）、§3×1、〔更正〕×1、§6×1。

---

## 1 · §2「wave21 commits `02adc1c`/`ad961d3`」— CONFIRMED

```
$ git log --oneline | grep -E "02adc1c|ad961d3"
02adc1c ops: launch wave21 (10 artists: xu_beihong/li_keran/sher_gil/tarsila/chen_hongshou/xu_wei/hogarth/mir_sayyid_ali/de_chirico/rockwell) + wave20 closeouts
ad961d3 feat: wave21 COMPLETE (10/10) + GOALS closeouts
```

- 提交时间：`02adc1c` = 2026-10-16 04:56:39 +0900；`ad961d3` = 05:59:27 +0900——与 §2 行（digest L55）「04:5x–05:5x」吻合。
- 附验：GOALS A-97..A-106 共 10 行全部 `done`（`grep -cE "^\| A-(9[7-9]|10[0-6]) \| done \|"` = 10）。

## 2 · §2「IndexMerge3 PASS 257/0 · commit `cea77cb`」— CONFIRMED

```
$ git show -s --format="%h | %ci | %s" cea77cb
cea77cb | 2026-10-16 06:27:12 +0900 | feat: index merge round 3 (62 artists; wave18/19/20 + full recompute) — 三索引 35→62；公开 273→618；私有例外 18→54 位 676 张；verify 257 PASS/0 FAIL

$ python knowledge/domains/painters/_scratch/index_merge3/verify_indices.py    # 只读脚本（唯一 open 为 rb）；退出码 0
…
[PASS] _index 头部图库引用（618 张 + 676 张） — 实测 公开 618 / 私有 676
[PASS] _index 未纳入（在产）注明
[PASS] _index 新三节存在
INFO 磁盘档案未纳入（在产，wave21）: ['chen_hongshou', 'de_chirico', 'hogarth', 'li_keran', 'mir_sayyid_ali', 'rockwell', 'sher_gil', 'tarsila', 'xu_beihong', 'xu_wei']
========================================================================
汇总：PASS 257 / FAIL 0
========================================================================
```

- 独立计数：`[PASS]` = 257、`[FAIL]` = 0；重跑输出与在盘 `verify_indices_output.txt` **逐字节一致**（各 21,116 B；`diff` → identical）。脚本可重跑结论成立。

## 3 · §1「语料 1613 条」— CONFIRMED

- `dossiers/_corpus/INDEX.md` 头部（L10 并入行）：`…→ **合计 62 文件 1613 条**（62 位画家）。`
- 独立重算：表内数据行 = 62；「条目」列合计 = **1613**（awk 求和）。
- verify 脚本同项：`[PASS] INDEX 行数 == 62 — 62`（且逐行 (条目/sw/rs/cr) == 磁盘重数）。
- 口径备注：1613 为 62 位三表口径；磁盘另有 wave21 十位（10 文件 / 321 条）待下轮并入（digest §5 B.11 已注明）。

## 4 · §1「公开图 618」— CONFIRMED

- `dossiers/_images/manifest.md` 头部（并入行）：`…→ **现共 62 位画家 / 公开 618 张**（另有私有层例外 676 张——公开/私有分开记…）。`
- 独立重算：`## 总表` 节数据行 = **618**；`## 私有层例外` 节 = 54 行（表头 + 54 位）。
- verify 脚本同项：`[PASS] _index 头部图库引用（618 张 + 676 张） — 实测 公开 618 / 私有 676`。

## 5 · §1「checks 186/186」— CONFIRMED

```
$ python knowledge/domains/painters/modules/_extract.py --check    # 退出码 0
…（62 卡逐张 ok）…
checks=186 ok=186 fail=0   # 62 卡 × §8.1/§8.2/§4 逐字比对
```

- 186 = 62 卡 × 3 节；模块目录 `.md` = 63（62 卡 + README）。

## 6 · §3 决策来源文件（抽 2 条：#12、#19）— CONFIRMED

- **#12（规格 v2 + 两轮加固）来源**：`knowledge/domains/painters/program/README.md` **§1「档案规格 v2（wave13 起适用）」在盘**，内容与决策描述一致（§11 叙述 ≥2000 字 / 年表 ≥15 行 / 来源 ≥10 条；§12 5–10 件；语料 ≥15 条；图库 ≥6 张；插在「自审四段」之前、既有节不动、保 `_extract.py` 抽取契约）。佐证来源同在：`S-main/handoff-2026-10-15T15-19-39-781Z.md` ✓；GOALS A-31 / A-106 行 ✓。
- **#19（索引收口口径 = 按批 + 以磁盘为准）来源**：`_scratch/index_merge2/reconcile.md` ✓、`_scratch/index_merge3/reconcile.md` ✓（§0 口径决定 7 条在盘：mucha 12/5、kandinsky `.hires`=11、mir_sayyid_ali 8、QA 排除、wave21 私有并入 54 行、快照 001/002）。佐证：`S-main/IndexMerge2.md` ✓、`S-main/handoff-2026-10-15T21-22-37-592Z.md` ✓。

## 7 · 〔更正〕C3「12 handoff / 144 jsonl / 157 md」— WEAKENED（2/3 吻合；jsonl 差 1）

实测（S-main 目录 `C:/Users/dwgx1/.omp/agent/sessions/--D--Project-Designers_Brain--/2026-10-15T06-29-46-426Z_01a13e40-…/`）：

```
$ ls handoff-*.md | wc -l   → 12        ✅（10-40-00-997Z … 21-22-37-592Z 共 12 份）
$ ls *.md | wc -l           → 157       ✅（= 145 工 md + 12 handoff；jsonl↔md 逐名对照，多出的 12 份恰为 handoff）
$ ls *.jsonl | wc -l        → 145       ❌ 声明 144（差 1）
$ ls *.log | wc -l          → 2114      ✅
$ 子目录                     → 4         ✅（ArtistLiKeran / ConsultWalkthrough / local / url-search）
```

- **jsonl 实为 145**（多方法一致：`ls|wc`、glob、逐名清点 145/145）。全部 145 份均带 `parentSession` 字段指向主会话 jsonl（`…01a13e40-….jsonl`）＝**全部为子代理/工转录**；主会话 jsonl 本体在 **slug 根层（目录外）**，不在该目录内（且无任何文件携带主会话 id / 标题）。
- 误因（留档）：MAIN-BRAIN §2 侦察行「144 子代理 jsonl」源自其笔记「145（1 main + 144 subagent）」——「1 main」不成立；06 号报告「145 含 1 非子代理件」为同一误推的调和。**正确值 = 145**；digest §6「145 jsonl」为正确数。
- 影响面：digest C3（L148）与 02 报告 L6 / L112（及 §8C L155 自审行）均写「144 子代理 jsonl」→ 建议改 **145**。

## 8 · §6 增补行「e714 HTML 已归 F: `sessions/Designers_Brain/aux/`」— CONFIRMED（附 1 处轻微口径差）

```
$ ls -la "F:/backup_famlti_family/sessions/Designers_Brain/aux/"
README.md                                                          432 B
omp-session-2026-10-15T22-30-09-428Z_01a141af-e714-737a-9b83-95a0938474e5.html   614,860 B   （mtime 2026-10-16 10:13:55 +0900）
```

- 项目根已无该文件（`find` 零命中；`git status` 不再列该 untracked）；aux/README 记录「copy 校验 sha256 相等后移出项目根」。
- 轻微口径差（同表下一行 L181）：「raw-20261016/（6 slugs + MANIFEST）」——实为 **5 个 slug 目录**（第 6 个空 slug「Designers Brain」未复制，MANIFEST 表内已注明）；`MANIFEST.md` / `SHA256SUMS.txt` 位于上一级 `sessions/Designers_Brain/`。建议注明「源 6、复制 5（空 slug 未复制）」。（低危，不影响本行结论。）

## 9 ·（注记）§1「145 done / 1 running」— WEAKENED（时点差；A-107 已收口）

- 实测（2026-10-16 **10:41 JST**）：
```
$ grep -c "| done |" ops/GOALS.md      → 145     （精确 done 行）
$ grep -c "| running |" ops/GOALS.md   → 0
$ grep -c "| open |" ops/GOALS.md      → 2       （A-30、S-06）
```
  总行 148；另有 A-12 行 `done(v0.1)`（不被上述 grep 命中）→ 含之则 done 类 = **146/148**。
- **时点差**：digest §1（L10）/ C2（L147）的「**1 running（A-107 待收口）**」为本波**中途快照**（A-108/A-109 已置 done、A-107 未置；03 号报告实测 done 144 / running 1；计入 `done(v0.1)` 得「145 done」口径）。**A-107 已于 commit `91194d2`（10:19:01；diff 实测 A-107/A-108/A-109 running→done）收口** → 现 running=0。精确 `grep` 数恰仍为 145，但口径已不同（原 = 144+1(v0.1)；现 = 145 精确 + v0.1 另计）。
- 备注：核验时 GOALS.md 正被主脑追加「A-30 排期」注记（状态计数未变）。

---

## 10 · 需修正清单（≤5）

| # | 位置 | 现文 | 建议 |
|---|---|---|---|
| 1 | `session-digest.md` §1（L10）+ C2（L147） | 「145 done / 1 running（A-107 待收口）」 | 改为「**146 done（含 `done(v0.1)`；`grep -c "| done |"` 精确 = 145）/ 0 running（A-107 已收口，`91194d2`）/ 2 open（A-30、S-06）**」 |
| 2 | `session-digest.md` C3（L148）+ `02-digest-waves12-21.md`（L6、L112；L155 可加注） | 「144 子代理 jsonl」 | 改为「**145 子代理 jsonl**（均 `parentSession` → 主会话；主 jsonl 在 slug 根层，不在目录内）」 |
| 3 | `session-digest.md` §6 增补行「会话归档」（L181） | 「raw-20261016/（6 slugs + MANIFEST）」 | 注明「**源 6 slug、复制 5（空 slug 未复制）；MANIFEST / SHA256SUMS 在上一级**」（低危） |
| 4 | （说明，非修正） | 任务描述称 digest「184 行」 | 磁盘实为 **182 行**（10:14:23 修掉整合残留标题「## 4 · §5 未收口更新」后；digest 本体无行数声明）——仅口径说明 |

## 11 · 复核命令清单（可重跑）

```bash
# 1) commits
git log --oneline | grep -E "02adc1c|ad961d3|cea77cb|457aacb"
git show -s --format="%h | %ci | %s" 02adc1c ad961d3 cea77cb 91194d2
# 2) IndexMerge3 verify（只读）
python knowledge/domains/painters/_scratch/index_merge3/verify_indices.py; echo EXIT=$?
# 3) 语料合计（期望 1613）
awk -F'|' '/^\| .*\.md \|/ {gsub(/ /,"",$3); if ($3 ~ /^[0-9]+$/) s+=$3} END{print s}' knowledge/domains/painters/dossiers/_corpus/INDEX.md
# 4) 公开图合计（期望 总表 618）— 同 §4 方法（分节后数表格数据行）
# 5) 模块卡（期望 checks=186 ok=186 fail=0）
python knowledge/domains/painters/modules/_extract.py --check | tail -1
# 6) 来源文件
ls knowledge/domains/painters/program/README.md knowledge/domains/painters/_scratch/index_merge{2,3}/reconcile.md
# 7) S-main 计数（期望 145 jsonl / 157 md / 12 handoff / 2114 log / 4 子目录）
cd "C:/Users/dwgx1/.omp/agent/sessions/--D--Project-Designers_Brain--/2026-10-15T06-29-46-426Z_01a13e40-a53a-7169-8317-62a0dc18de57" && ls *.jsonl | wc -l && ls *.md | wc -l && ls handoff-*.md | wc -l && ls *.log | wc -l
# 8) F: 实点
ls -la "F:/backup_famlti_family/sessions/Designers_Brain/aux/"
# 9) GOALS（时点 2026-10-16 10:41 JST：145 / 0 / 2）
grep -c "| done |" ops/GOALS.md; grep -c "| running |" ops/GOALS.md; grep -c "| open |" ops/GOALS.md
```

---

*本报告 = 唯一新增产物；被验文件零改动（digest / 02 报告 / GOALS / F: 均未触碰；未 commit）。*
*上下文快照：仓库 `main...origin/main [ahead 5]`；`ops/session-digest.md`、`ops/GOALS.md` 为工作树未提交修改。*
