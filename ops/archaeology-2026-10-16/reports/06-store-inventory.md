# 06 · Store Inventory — DBrain OMP 会话材料全量清单（归档源；只读）

- 工：StoreInventory（Wave1）· 快照：**2026-10-16 上午 JST**（活会话仍在写入，标〔活〕）
- 方法：目录分页枚举 + 大小写多模式 glob 全量核验 + 定向 grep；**未整份读取任何 jsonl**。
- 口径：文件数=枚举值；大小=目录列表显示值合计（≈，1 位小数）；MB=10⁶ 量级表述。
- 与主脑侦察交叉核对：**一致**（见 §2.1）。

---

## 1 · `C:/Users/dwgx1/.omp/agent/sessions/` — 全 slug 扫描（Designers/DBrain，大小写不敏感）

变体核验（Designers/designers/DESIGNERS × Brain/brain/DBrain/dbrain）→ 命中 **6 个 slug**：

| # | slug | 文件数 | 大小 | 结构 | mtime 范围 |
|---|---|---|---|---|---|
| 1 | `--D--Project-Designers_Brain--` | ≈2,500〔活〕 | ≈340 MB | 2 会话：S-main（已死；树 2,446 文件，含 4 子目录）+ 22-41（活；Wave1 工场）+ 根 jsonl×2 | 2026-10-15 15:29 JST → 进行中（S-main 冻结于 10-16 06:28） |
| 2 | `--D--Project-Designers Brain--` | **0** | **0 B** | 空目录（仅占位） | 2026-10-15 下午 |
| 3 | `--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p1_grok-imagine-image--` | 2 | 330.7 KB | 2×jsonl + 1 空子目录 | 2026-10-15 09:34–09:38Z |
| 4 | `--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p2_grok-imagine-image-2.0--` | 1 | 12.6 KB | 1×jsonl + 1 空子目录 | 2026-10-15 09:37Z |
| 5 | `--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p3_grok-imagine-image-edit--` | 1 | 16.1 KB | 1×jsonl + 1 空子目录 | 2026-10-15 09:37Z |
| 6 | `--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p4_grok-imagine-image-lite--` | 1 | 31.5 KB | 1×jsonl + 1 空子目录 | 2026-10-15 09:37Z |

**合计：6 slugs / ≈2.5k 文件 / ≈340 MB。** 无其它大小写/连字符变体。p1–p4 全名见 §5 源清单。

---

## 2 · 主 slug 深清单（`--D--Project-Designers_Brain--`）

### 2.1 S-main 会话目录 `2026-10-15T06-29-46-426Z_01a13e40-a53a-7169-8317-62a0dc18de57/`

**根：2,420 条目 = 2,416 文件 + 4 子目录；树内共 2,446 文件（含子目录内 30 文件）；≈320 MB。**

按扩展名（根）：

| 扩展名 | 计数 | 大小（估） | 说明 |
|---|---|---|---|
| `*.jsonl` | **145** | ≈300 MB | 子代理/工转录（Artist*/Bio*/Hard*/ModuleCards* 等），多数 1–3.2 MB |
| `*.md` | **157** | <1 MB | 卡面/评审/交接；其中 `handoff-*.md` **12** |
| `*.log` | **2,114** | ≈17 MB | `*.bash.log`（主体）、`*.read.log`（≥200）、`*.eval.log`（≥200）、`*.bash-original.log` **175**、`*.async.log` **1** |
| 合计 | **2,416** | ≈320 MB | +4 子目录（内 30 文件）→ 树 2,446 |

- 核对：主脑侦察 144 子代理 jsonl + 157 md + 2114 log + 12 handoff + 4 子目录 → 本工独立枚举一致（jsonl 145 含 1 非子代理件；根合计 2,416）。

**空文件清单（0 B；根 27 个 + url-search 1 个 = 28 个）：**
`IndexMerge3.md` / `ArtistAivazovsky.md` / `ArtistConstable.md` / `ArtistFanKuan.md` / `ArtistRivera.md` / `ArtistHolbein.md` / `ArtistBruegel.md` / `ArtistElGreco.md` / `ArtistKahlo.md` / `ArtistMucha.md` / `ArtistHuangGongwang.md` / `ArtistTurner.md` / `ArtistRembrandt.md` / `ArtistQiBaishi.md` / `ArtistItoJakuchu.md` / `RosterBuilder.md` / `BioPicasso.md` / `BioCaravaggio.md` / `BioMichelangelo.md` / `BioDurer.md` / `BioVermeer.md` / `BioHokusai.md` / `BioDaVinci.md` / `BioMonet.md` / `BioCezanne.md` / `BioMatisse.md` / `BioVanGogh.md` / `url-search/1d2zoqpqmjt4t.pdf`

**异常模式：**
- `*.bash-original.log` **×175**（备份日志，合计 ≈1 MB；示例 `12960.bash-original.log` 10.3 KB）
- `7461.async.log` ×1（异步残件，13.3 KB）
- 无 `*.tmp / *.bak / *.orig / *.swp / .DS_Store / Thumbs.db`
- 近空 stub：`ArtistSesshu.md` 49 B / `ArtistPoussin.md` 53 B / `ArtistOkeeffe.md` 103 B

**4 子目录（逐目录）：**

| 子目录 | 文件数 | 内容 |
|---|---|---|
| `ArtistLiKeran/` | 6 | NamocXuzhou / QuotesLiKeran / TechniqueLit 各 jsonl+md |
| `local/` | 5 | namoc_xuzhou.md 19.6KB / quotes_raw_notes.md 1.1KB / quotes_raw.md 32.4KB / technique_lit.md 27.3KB / li_keran_probe.md 34B |
| `url-search/` | 17 | html×1 / txt×12 / pdf×2（含 1×0B）/ php×1 / …（下载件） |
| `ConsultWalkthrough/` | 2 | W01Reviewer jsonl 319.3KB + md 11.1KB |

**最大 20 文件（按列表显示尺寸）：**
1. ArtistChenHongshou.jsonl 3.2MB · 2. ArtistArtemisia.jsonl 3.2MB · 3. ArtistNiZan.jsonl 3.1MB · 4. AnimTest03Blender.jsonl 3.0MB · 5. ArtistZorn.jsonl 2.8MB · 6. ArtistMucha.jsonl 2.8MB · 7. ArtistLiKeran.jsonl 2.7MB · 8. ArtistQiuYing.jsonl 2.7MB · 9. ArtistHuangGongwang.jsonl 2.7MB · 10. ArtistFanKuan-2.jsonl 2.7MB · 11. ArtistXuBeihong.jsonl 2.6MB · 12. ArtistBruegel-2.jsonl 2.6MB · 13. ArtistTurner.jsonl 2.6MB · 14. IndexMerge.jsonl 2.6MB · 15. ArtistMirSayyidAli.jsonl 2.5MB · 16. ArtistSargent.jsonl 2.5MB · 17. ArtistNamatjira.jsonl 2.5MB · 18. ArtistWuGuanzhong.jsonl 2.5MB · 19. ArtistChardin.jsonl 2.5MB · 20. IndexMerge3.jsonl 2.5MB
（次位 2.4MB 档：ArtistTarsila / ArtistHiroshige / ArtistElSalahi / HardRembrandt / ArtistRepin / ArtistFriedrich / ArtistRockwell / ArtistXuWei / BioCaravaggio / ArtistItoJakuchu 等。）

### 2.2 22-41 会话目录 `2026-10-15T22-41-02-476Z_01a141b9-de0c-72f6-bad6-aa66796cdf82/`〔活〕

- 快照 ≈48 条目（持续增长）：**11 个工转录 jsonl**（StoreInventory / SubagentCatalog / HandoffDigest / EndgameReconcile / GarbageAudit / FOuterRecon / RosterCrosscheck / HtmlExportId / AbsorbCheck / SessionCondense / Archivist；0.3–2.1 MB）+ 35 个日志 + `local/`（reports/ + probe-write-test.md 62 B）。
- 根 jsonl：1.1 MB（进行中）。整个主 slug ≈2.5k 文件 / ≈340 MB。

---

## 3 · 其他位置（确切路径 + 数量）

### 3.1 `C:/Users/dwgx1/.omp/agent/archive/sessions/` — 逐 slug 查 DBrain：**全 0**
- 现存量：**7 slugs / 205 条目 = 130 个 `.jsonl.gz` + 75 个会话子目录**：genesis 73、`-.dwgx` 43、`-tmp` 40、`--C--tmp--` 41、`--E--dwgxhomecloud--` 4、launcher 2、Romantic 2。
- grep `Designers_Brain` 全库 **0 命中**；`DBrain` 仅 1 处假阳性（genesis url-search CSV 内 "wizardbrainz"）。
- （历史口径：333 会话/≈800MB，见 history-absorb README；吸收后已缩容。）

### 3.2 `C:/Users/dwgx1/.omp/agent/custom-session-files/`
- **91** 个文件（各 121–300 B；内容=会话 jsonl 绝对路径指针，样本 `a96286e` → `…AppData\Local\Temp\modelcheck-…\2026-10-14…jsonl`）。
- grep `designers|dbrain`：**0 命中**。

### 3.3 `C:/Users/dwgx1/.omp/agent/memories/`
- **34** 个 slug；grep `designers|dbrain`：**0 命中**。

### 3.4 `C:/Users/dwgx1/.omp/agent/terminal-sessions/`
- **319** 个 `wt-*`（快照）；其中 **4** 个引用 Designers_Brain（cwd `D:\Project\Designers_Brain`）：
  - `wt-08d22421-…` 196 B → 会话 22-41-02（在库）
  - `wt-5df1cb1d-…` 196 B → 会话 06-29-46（在库）
  - `wt-90882c39-…` 196 B → 会话 14-43-51（**不在库**）
  - `wt-d5322475-…` 202 B → 会话 22-30-09（**不在库**；仅有 HTML 导出）

### 3.5 `C:/Users/dwgx1/.dwgx/archive/`
- 结构：`history-absorb-2026-10-15/`（19 文件 = README + 13 digests + 5 aux；素材源=archive/sessions 333 会话；**无 DBrain**）、`chatgpt-lane-20260929/`、`hist2.db` 960 KB、`hist-copy.db` 928 KB。
- 全盘 `find ~/.dwgx -name '*.jsonl.gz'` → **0 个**（该树下 .gz 仅 19 个 .tar.gz：refs/tmp/ops，非会话数据）。
- 旁证（非会话材料，未列入复制）：`.dwgx/ops/boards/Designers_Brain.md`、`.dwgx/ops/detail-2026-10-16-designers-brain.md`、`.dwgx/ops/research-2026-10-15/B09-awesomeui-designersbrain.md`。

### 3.6 `C:/Users/dwgx1/.claude/projects/`（cwd=Designers_Brain）
- 24 个项目中 1 个命中：`D--Project-Designers-Brain/`
  - `61733a86-238c-403c-a118-fae02fc3dbef.jsonl` — 2026-10-15（07:09Z 起）· **3.1 MB** · cwd `D:\Project\Designers_Brain`（cross-dispatch db-c2）
  - `61733a86-…/tool-results/b3ji537kc.txt` 41.4 KB
- **【可选归档】只列，不入本批复制。**

### 3.7 `C:/Users/dwgx1/.codex/sessions/`（cwd=Designers_Brain）
- 1 个命中：`2026/10/15/rollout-2026-10-15T16-09-20-01a13e64-dfb4-7812-8dc9-f435343f2e9d.jsonl` — 2026-10-15 16:09 JST · **55.8 KB**（cross-dispatch db-c1）
- **【可选归档】只列。**

### 3.8 其他可选件
- 项目根 `D:/Project/Designers_Brain/omp-session-2026-10-15T22-30-09-428Z_01a141af-e714-737a-9b83-95a0938474e5.html` 600.4 KB（会话 22-30-09 的 HTML 导出；其 jsonl 本体不在库）。

---

## 4 · 垃圾清单（不删；建议移 `quarantine/Designers_Brain/`）

- **空目录 ×5**：`--D--Project-Designers Brain--`（整 slug，0 文件）；p1/p2/p3/p4 的会话子目录 ×4（各 0 文件）。
- **0 字节文件 ×28**：见 §2.1 清单（27 根 + 1 url-search）。
- **明显 temp**：`*.bash-original.log` ×175（S-main，≈1 MB）+ ×8（22-41 树，64.4 KB）；`local/li_keran_probe.md` 34 B；`local/probe-write-test.md` 62 B；`7461.async.log` 13.3 KB。

---

## 5 · 复制计划（可直接执行；只读清单，不代为执行）

**目标结构**：`F:/backup_famlti_family/sessions/Designers_Brain/raw-20261016/<原 slug 名>/`（与家族 lane 既有落点一致；F 侧已存在 `_make-sha256sums.py` / `_compare-raw-20261016.py` 可用于复制后比对）

**源清单（6 个，绝对路径）**：
1. `C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers_Brain--`
2. `C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers Brain--`
3. `C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p1_grok-imagine-image--`
4. `C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p2_grok-imagine-image-2.0--`
5. `C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p3_grok-imagine-image-edit--`
6. `C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p4_grok-imagine-image-lite--`

**robocopy 命令草稿**（先 `/L` 演练；逐 slug 执行；退出码 <8 = OK）：

```bat
robocopy "C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers_Brain--" "F:\backup_famlti_family\sessions\Designers_Brain\raw-20261016\--D--Project-Designers_Brain--" /E /COPY:DAT /DCOPY:DA /R:2 /W:1 /NP /TEE /LOG+:"F:\backup_famlti_family\sessions\Designers_Brain\_copy-log-raw.txt"
robocopy "C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers Brain--" "F:\backup_famlti_family\sessions\Designers_Brain\raw-20261016\--D--Project-Designers Brain--" /E /COPY:DAT /DCOPY:DA /R:2 /W:1 /NP /TEE /LOG+:"F:\backup_famlti_family\sessions\Designers_Brain\_copy-log-raw.txt"
robocopy "C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p1_grok-imagine-image--" "F:\backup_famlti_family\sessions\Designers_Brain\raw-20261016\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p1_grok-imagine-image--" /E /COPY:DAT /DCOPY:DA /R:2 /W:1 /NP /TEE /LOG+:"F:\backup_famlti_family\sessions\Designers_Brain\_copy-log-raw.txt"
robocopy "C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p2_grok-imagine-image-2.0--" "F:\backup_famlti_family\sessions\Designers_Brain\raw-20261016\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p2_grok-imagine-image-2.0--" /E /COPY:DAT /DCOPY:DA /R:2 /W:1 /NP /TEE /LOG+:"F:\backup_famlti_family\sessions\Designers_Brain\_copy-log-raw.txt"
robocopy "C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p3_grok-imagine-image-edit--" "F:\backup_famlti_family\sessions\Designers_Brain\raw-20261016\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p3_grok-imagine-image-edit--" /E /COPY:DAT /DCOPY:DA /R:2 /W:1 /NP /TEE /LOG+:"F:\backup_famlti_family\sessions\Designers_Brain\_copy-log-raw.txt"
robocopy "C:\Users\dwgx1\.omp\agent\sessions\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p4_grok-imagine-image-lite--" "F:\backup_famlti_family\sessions\Designers_Brain\raw-20261016\--D--Project-Designers_Brain-research-agent-art-cards-_image_probes-p4_grok-imagine-image-lite--" /E /COPY:DAT /DCOPY:DA /R:2 /W:1 /NP /TEE /LOG+:"F:\backup_famlti_family\sessions\Designers_Brain\_copy-log-raw.txt"
```

**预计总量**：**≈2.5k 文件 / ≈340 MB（≈3.4×10⁸ 字节）**；绝对主体 = S-main 目录（≈320 MB）。源不动；只进不删；收据/移动记 `receipts/`（由 Archivist 执行）。

**现状注记（本清单与执行对齐）**：Archivist 已启动复制——`raw-20261016/` 已有：主 slug（7:56 起，进行中，已见 06-29 树+2 jsonl）、p1–p4（8:09–8:12 完成，含空目录；字节 330.6k/12.5k/16.1k/31.4k）。待补：`--D--Project-Designers Brain--`（空 slug，可选）。

---

## 6 · 备注

1. **被引用未落库**：终端会话引用 2 个不在库的会话——`2026-10-15T22-30-09-428Z_01a141af-e714-…`（仅项目根 HTML 导出）与 `2026-10-15T14-43-51-676Z_01a14004-…`（全库未见）。归档时以上述现有件为准。
2. **方法边界**：glob 200 上限 → `*.read.log` / `*.eval.log` 为「≥200」；`*.bash.log` 未逐项枚举（总 log 数 2,114 为根合计倒推值，与侦察一致）。尺寸为列表显示值合计（≈）。
3. 本报告落点：`…/2026-10-15T22-41-02-476Z_01a141b9-…/local/reports/06-store-inventory.md`（工作区 `reports/` 同步由主脑处理）。
