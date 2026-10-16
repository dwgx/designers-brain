# 05 · F: 外层勘察 — DBrain 相关件（FOuterRecon2）

> **工**：FOuterRecon2（Wave1-R2 重派；原 FOuterRecon 死于 08:2x–10:0x provider 503 波，transcript 已失）· 会话 `01a141b9-de0c-72f6-bad6-aa66796cdf82`（DBrain 站稳脚跟运维）
> **快照**：2026-10-16 ≈10:2x–11:1x JST（相对读数均为快照时点）· **只读**：未移动、未删除、未打开任何 zip/tar 内容、未整读 jsonl
> **口径**：大小 =「du 实测（在案值，标 du）」或「列表显示值合计（≈ / ≥）」；日期 = 工具相对读数
> **交叉线**：SKIAPI `F-PULL-CANDIDATES`（截至本件未落盘）· Any2API `FAMOPS-8-fouter-survey`（协调者 reports/，截至本件未落盘）→ 收口时三线去重

---

## 0 · 摘要

1. **PULL→`f-outer/Designers_Brain` 候选 = 0 件**：F: 外层（根 + 重点目录）全查，未发现应拉入的 DBrain 专属件。
2. 唯一强命名件 = `F:/远古历史/Designers_Brain/`：**空桶**（DBrain 旧材料归档位，10-16 建立待填）→ **NOTE**（不 PULL）。
3. 已就位（非候选，勿重复）：`F:/1.txt` → `f-outer/_misc/1.txt`（68B）；e714 会话 HTML → `sessions/Designers_Brain/aux/`（MOVES 10:13 行）；DBrain 会话副本 + `SHA256SUMS.txt` 已落 `sessions/Designers_Brain/raw-20261016/`。
4. 重点目录逐项核查（§3）：`dwgxachive` / `Backups` / `_omp-backups`（大 tar 复核 0 命中）/ `origin-backups` / `hmc-backup-20261014` / `sbx-work` / `mus2c` → **均无 DBrain 相关件**。
5. **禁读树零触碰**（§5，附全量访问清单）；大 zip 仅列名（§6）。

---

## 1 · F:/ 根全枚举（现存 25 项 + 已迁 2 项）

> 对照任务书列名（24 项）：**22 项在根、2 项已迁**（`1.txt`、`romantic-archive`，见下表后注）；任务书外根级现存：`QQ20261014-201039-HD.mp4/.zip`、`System Volume Information`（一并列出）。
> **禁读树**（`重装`、`TerraResearch`、`origin-solii-bulk`）**不列** —— 零触碰，证明见 §5。

| # | 项 | 大小 | 日期（读数） | 一句话 |
|---|---|---|---|---|
| 1 | `backup_famlti_family/` | ≈45GB（粗算） | 2h 前 | 全机 OMP 会话家族备份根（本单归属）：sessions / f-outer / receipts / _meta / tarballs…；在盘大件 romantic-archive 26GB、老会话 tar 4.9GB、SKIAPI 716MB、DBrain ≈340MB |
| 2 | `远古历史/` | ≥0.6GB（合计） | 2h 前 | 旧考古材料归档区（21 项目桶；主件 Any2API 会话导出 552MB；DBrain 桶为空） |
| 3 | `Backups/` | ≈27GB（粗算） | 10h 前 | T0/T1/T2 备份制度根：AwesomeUI slim-cold 22.5GB + _cold-misc ≈4.8GB + _omp-sessions 空占位 |
| 4 | `dwgxachive/` | ≥8.15GB（合计） | 17h 前 | 杂档根：Any2API 临时 lanes + OMP 构建 target + 云端备份记录 + 3 归档（8.15GB）；**内含禁读子树（未触碰）** |
| 5 | `Romantic-backup-20261015/` | ≈42GB（日志值） | 19h 前 | Romantic 全量备份（181,781 件 / 42.1GB）；Legacy 保留原位不搬 |
| 6 | `Romantic-depot-public-25841461/` | ≈303MB（合计） | 19h 前 | VRChat depot 副本 4 件；Legacy 不搬 |
| 7 | `dwgx-cold/` | ≈20GB（du） | 19h 前 | genesis 冷档（INDEX/MANIFEST/RESTORE 制度；≈29 项 cold-*） |
| 8 | `QQ20261014-201039-HD.zip` | 2.2GB | 23h 前 | QQ 录屏 zip（Owner 裁「都留」） |
| 9 | `mus2c/` | ≈40MB+（合计） | 23h 前 | 个人音乐/视频（hiphop 专辑树 + 5 视频 38.2MB） |
| 10 | `QQ20261014-201039-HD.mp4` | 2.2GB | 1d 前 | 同上 mp4 版 |
| 11 | `origin-backups/` | 5.4MB（合计） | 1d 前 | genesis「origin」仓 R3 保护 bundle 冷套件 3 件 |
| 12 | `hmc-backup-20261014/` | 4.0GB（du） | 2d 前 | HMC 线异地备份（mcsmanager / grok-home / bench×2 / artex×103 tar / rw×9 仓 / w7-world / napcat） |
| 13 | `_omp-backups/` | 17.2GB（du） | 2d 前 | OMP 备份树：crash-dumps 13.1GB + 老会话 tar 4.9GB + debugger 84.5MB |
| 14 | `Project/` | ≈1.4GB+（合计） | 3d 前 | 姊妹工程区（VD / MCPC / src / DepthARK / UI / shitoudao-Web / 源码） |
| 15 | `sbx-work/` | 120KB（du） | 4d 前 | clients.lol（VRChat 客户端数据库）沙箱副本 |
| 16 | `Media/` | ≈30GB+（粗算） | 2w 前 | 个人媒体库（方块人 ≈17GB、采样 8GB、音乐 ≈5GB…） |
| 17 | `OTHER/` | ≈62GB+（粗算） | 2w 前 | 杂项：`备份/系统/` SBX 冻结 vhdx 58.4GB 为主件 |
| 18 | `WSL/` | 13.2GB（du） | 3w 前 | WSL Ubuntu-24.04 备份 |
| 19 | `SELF LLM/` | 368KB（du） | 1mo 前 | opt-in 人设/工作流件（zip 95.8KB + 解包） |
| 20 | `UnityVRChat/` | 8.0GB（du） | 1mo 前 | VRChat 世界素材（世界/） |
| 21 | `15/` | 1.1GB（du） | 1mo 前 | 电影《15》(Royston Tan 2003) 媒体件 |
| 22 | `$RECYCLE.BIN/` | —（多数不可读） | 1mo 前 | 回收站 11 SID；最新可见仅 1 元数据件（$I4T1R76.zip 148B）；未见 DBrain 件 |
| 23 | `MC/` | ≈3.5GB+（合计） | 1mo 前 | Minecraft 资产（地图 / 服务端核心 / 材质包） |
| 24 | `TOOL/` | 7.3GB（du） | 8mo 前 | 本机工具集（IDA / debugger / java / 压缩 / 语音…） |
| 25 | `System Volume Information/` | 不可读（Access denied） | 8mo 前 | 系统卷信息（无访问权限） |

**已迁（不在根，按 MOVES.tsv 10:09–10:10 行）**：
- `F:/1.txt` → `f-outer/_misc/1.txt`：68B · 2026-10-16 10:10（内容 = codex / oh-my-pi 两行 URL，OMP 工具链线索）
- `F:/romantic-archive/` → `f-outer/Romantic/romantic-archive/`：26GB · 2026-10-16 10:10

---

## 2 · DBrain 相关判定表

> 只列 DBrain 相关件（含弱关联与已就位件）；**未执行任何搬动**（0 moves；如需收据由执行会话落 MOVES.tsv）。

| # | 路径 | 大小 | 日期 | 是什么 | 相关度 | 建议 |
|---|---|---|---|---|---|---|
| 1 | `F:/远古历史/Designers_Brain/` | **0B（空目录）** | 2026-10-16（本日建立） | DBrain 旧材料归档桶（已建、待 DBrain 会话填充） | **强**（命名直属） | **NOTE** —— 不 PULL（空）；与 f-outer 制度区分（旧材料留 `远古历史/`） |
| 2 | `F:/backup_famlti_family/f-outer/_misc/1.txt` | **68B** | 2026-10-16 10:10 迁入（原件 3w 前） | OMP 工具链线索小件（codex / oh-my-pi URL） | 弱（OMP 生态；非 DBrain 专属） | **NOTE** —— 已归集；无动作 |
| 3 | `F:/backup_famlti_family/sessions/Designers_Brain/`（`raw-20261016/` + `aux/`） | **≈340MB**（raw，在途收口） | 2026-10-16 | DBrain 会话全量副本 + SHA256SUMS（27KB，已落）；aux 含 e714 HTML | **强**（本家件） | **NOTE** —— 家族 lane 自有落点；非 f-outer 范围 |
| — | （结论行）**PULL 候选：0 件** | — | — | f-outer 无 DBrain 子目录；本次全查未发现应拉件 | — | **不动作**（后续出现时按制度追加） |

明细（第 3 行）：`aux/` = README.md 432B + `omp-session-…e714….html` 600.4KB（10:13 移入，sha256 校验后移出项目根）；`raw-20261016/` = 主 slug（2 会话 + 2 根 jsonl）+ p1–p4 镜像；`SHA256SUMS.txt` 27.0KB「just now」落盘，比对输出（`_compare-raw-20261016.out.txt`、`_sha256-crosscheck.out.txt`）在盘。

**已核查「无命中」（负结果，供复核）**：`dwgxachive`（全列无 Designers/画家/brain 命名）· `Backups`（小件 grep 0）· `_omp-backups`（大 tar 清单 0 命中；crash-dumps/debugger 无关）· `origin-backups`（genesis）· `hmc-backup-20261014`（全列无）· `sbx-work`（clients.lol）· `mus2c`（音乐）—— 详见 §3。

---

## 3 · 重点目录逐项核查记录

### 3.1 `F:/远古历史/Designers_Brain/` —— 复核（已知空）
- 实况：**空目录**（read 返回 `(empty directory)`；含名深扫亦仅返回该目录自身）。
- 用途：`F:/远古历史/README.md`（10-16 立）列其 =「Designers_Brain（DBrain）」旧考古材料归档位；规则 = 只进不删、各会话自搬。
- 结论：**NOTE**（空；非 f-outer 范畴；待 DBrain 旧材料波自行填充）。

### 3.2 `F:/dwgxachive/` —— 全列（找 Designers/画家/brain）
- 方法：根 + 子项逐级枚举（read 分页，≈1,000 行全覆盖）+ 名称定向扫描（glob）+ 小文件抽查；**zip/tgz 未开（仅列名）**；**`origin-soliii-bulk/` 未进入（禁读，仅记录名）**。
- 子项实况：
  - `D-tmp-buildtargets-20261015/`：10 个 OMP 构建 target（Rust：debug/release/.rustc_info.json/CACHEDIR.TAG）—— 无 DBrain 命名。
  - `Any2API-tmp-lanes-20261015/`：W6–W41 / L01–L19 / P01–P77 系列 **180+ 顶层 lanes**（Any2API 研究临时件；含近名 `W33-design` 等已逐一目检）—— **无 Designers/画家/brain 命中**。
  - `云端备份记录/`：UnityVRChat 云端备份/清理记录（57 件记录 + 工序脚本）—— 无。
  - `ZCode-main.zip` 41.4MB / `ORIGIN_Blender_Project_Handoff_20260908_v1.zip` 7.5GB / `claude-code-2.1.88.tgz` 29.8MB —— 仅列名。
  - `origin-soliii-bulk/` —— **禁读子树：未进入、未展开**（父级枚举自动显示其名与子项名预览属工具行为，未做任何进一步访问）。
- 限制：深扫 `**/*rain*` 等 glob 5s 超时（记录在案；结论以全列表扫描为准）。

### 3.3 `F:/Backups/` —— 找 DBrain
- 全树 4 子项：`README.md` / `_cold-misc-20261015/`（kiro-re + pgdata + pgsql ≈4.8GB）/ `AwesomeUI/2026-10-15-slim-cold/`（22.5GB）/ `_omp-sessions/`（**空占位**）。
- 小件 grep「designers|dbrain|画家」= **0 命中**（README、两 MANIFEST、_deleted 清单）。
- 结论：**无 DBrain 件**；`_omp-sessions/` 为会话归档预留位（未来位）。

### 3.4 `F:/_omp-backups/` —— 找 DBrain 会话
- 三子项：`crash-dumps/`（21 件 watchdog dmp，含 12.1GB 大件）/ `debugger-_re-work-20261013/`（dxgkrnl 符号 7 件）/ `omp-sessions-older-than-5d-20261012.tar` 4.9GB（**仅列名，未开**）。
- **大 tar 复核**：对既有清单 `_meta/omp-sessions-older-than-5d-20261012.contents.txt` grep `esigners|dbrain` → **0 命中**（此前「Brain」命中均为 WindsurfAPI `Pr*Brain` 文件，非 DBrain）。
- 结论：**无 DBrain 会话**（与 lane 卡「pre-20261012 无」一致）。

### 3.5–3.8 其余重点目录
- `origin-backups/`：3 件（bundle 5,674,868B + BUNDLE-RECEIPT + DRILL-TRANSCRIPT）；= genesis「origin」仓 R3 保护套件 —— 无 DBrain。
- `hmc-backup-20261014/`：9 顶层全列（mcsmanager / grok-home / bench×2 / artex×103 tar / napcat / rw×9 仓 / w7-world 工程树 / grok-bundle）—— **无 Designers/画家/brain**。
- `sbx-work/`：clients.lol 沙箱（120KB：13 TOML + docs + api.json）—— 无。
- `mus2c/`：个人音乐（hiphop + 5 视频）—— 无。

---

## 4 · 协同与状态注记

- **家族侧 DBrain 状态**（快照）：`sessions/Designers_Brain/raw-20261016/` 复制完成 + `SHA256SUMS.txt` 已落（27KB）；`aux/` 含 e714 HTML；`quarantine/Designers_Brain/`（project-tree、project-scratch）已建；`digests/Designers_Brain/`、`receipts/Designers_Brain*` 截至本件**未见**（在途）。`f-outer/Designers_Brain/` 不存在（无候选）。
- **交叉线待去重**：SKIAPI `F-PULL-CANDIDATES`（`ops/archaeology-2026-10-16/reports/`，未落盘）· Any2API `FAMOPS-8-fouter-survey`（协调者 reports/，未落盘）。
- `_omp-backups/` 已有主（Any2API `tarballs/` 认领；launcher 明确不动 crash-dumps/debugger）；`dwgxachive` 子件与 Any2API 线相关 → 任何拉动先协调 + CLAIMS。
- 本工**未执行搬动、未写任何 F: 路径**；如需 `f-outer/Designers_Brain/` 占位或后续拉动，由执行会话按制度落 MOVES.tsv + 收据。

---

## 5 · 「禁读树零触碰」证明

**禁读树（不扫不碰）**：`F:/重装` · `F:/TerraResearch` · `origin-solii-bulk`（拼写变体 `origin-soliii-bulk`；实际落点 `F:/dwgxachive/origin-soliii-bulk/`）。

1. **声明**：本次作业全程**未对上述三树发起任何访问调用**（无 read、无 grep、无 glob、无进入、无内容读取）；对 `dwgxachive` 的「全列」按**逐子项**执行并**主动跳过** `origin-soliii-bulk/`。
2. **显示说明**（如实披露）：目录枚举工具会对父级列表自动渲染子项名（含少量预览）；三树之名仅在此类**不可控显示**中出现，未据此做任何操作、未展开。
3. **可复核访问清单**（本次全部 F: 访问，去重到目录级）：
   - **read**：`F:/`、`F:/1.txt`（不存在）、`F:/远古历史/`（含 Designers_Brain / _README / 本机杂项 / cloud / 治理）、`F:/dwgxachive/`（含 D-tmp-buildtargets、Any2API-tmp-lanes、云端备份记录；**不含 origin-soliii-bulk**）、`F:/Backups/`（含 README / _cold-misc / AwesomeUI / _omp-sessions）、`F:/_omp-backups/`（含 crash-dumps）、`F:/origin-backups/`、`F:/hmc-backup-20261014/`（含 artex / rw / w7-world / grok-bundle）、`F:/sbx-work/`、`F:/mus2c/`、`F:/backup_famlti_family/`（README / f-outer / _meta / receipts / sessions / digests / quarantine / tarballs / sessions-aux / sessions-archive）、`F:/dwgx-cold/`（含 INDEX.md）、`F:/Romantic-backup-20261015/`、`F:/$RECYCLE.BIN/`、`F:/MC/`、`F:/Media/`、`F:/OTHER/`（含 备份/）、`F:/Project/`、`F:/SELF LLM/README.md`；QQ 两件仅随根列表读数。
   - **grep**：`…/_meta/omp-sessions-older-than-5d-20261012.contents.txt`、`F:/Backups` 4 小件、`F:/远古历史` 9×MANIFEST.md。
   - **glob**：`F:/dwgxachive/*`、`…/Any2API-tmp-lanes-20261015/*`（+深扫超时项）、`…/D-tmp-buildtargets-20261015/**`、`…/云端备份记录/**`、`F:/远古历史/*esigners*` 系列、`F:/_omp-backups/**/*esigners*`（0 命中）、`F:/hmc-backup-20261014/**/*esigners*`（超时）、`F:/dwgx-cold/**/*esigners*`（超时）。
   - **以上无一条落在三树内部。**
4. **旁证**：`F:/dwgx-cold/INDEX.md`、`F:/Backups/README.md`、`F:/远古历史/README.md`、家族 README、CLAIMS 等制度文档均复述同一禁读清单 —— 本件与之一致。

---

## 6 · 方法与限制

- 相对时间读数为快照时点（2026-10-16 上午 JST）；大小口径见页首；du 值来源为在案实测（引用标注）。
- **未打开**任何 zip/tar/tgz 内容（唯一例外 = 既有「清单文本」（contents.txt）的 grep，非归档本体）；未整读任何 jsonl。
- glob 5s 超时项已逐处标注（「非证明性缺失」）—— 相关结论以全列表扫描为准。
- 本件落点：`local://reports/05-f-outer-recon.md`；工作区 `ops/archaeology-2026-10-16/reports/` 收编由主脑处理（与 04/06/07 同惯例）。
