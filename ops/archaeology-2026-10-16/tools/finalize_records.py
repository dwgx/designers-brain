#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finalize standfirm records: digest §1 counts + OPS-LOG §17 + GOALS ST lane.
Run: python ops/archaeology-2026-10-16/tools/finalize_records.py
Idempotent-ish: aborts if already applied.
"""
import re, sys
from pathlib import Path

ROOT = Path(r"D:/Project/Designers_Brain")
DIG = ROOT/"ops"/"session-digest.md"
LOG = ROOT/"ops"/"OPS-LOG.md"
GOALS = ROOT/"ops"/"GOALS.md"

dig = DIG.read_text(encoding="utf-8")
log = LOG.read_text(encoding="utf-8")
goals = GOALS.read_text(encoding="utf-8")

# --- 1. digest §1: GOALS counts line -> current ---
n_done = len(re.findall(r"\| done \|", goals))
old_line = "GOALS：145 done / 1 running（A-107 待收口）/ 2 open（A-30、S-06）。"
new_line = f"GOALS：{n_done} done / 0 running / 2 open（A-30、S-06；A-107 本波收口）。"
assert dig.count(old_line) == 1, "digest goals line not found or not unique"
dig = dig.replace(old_line, new_line)
print(f"digest §1: goals line -> {n_done} done")

# --- 1b. VerifyDigest corrections (C2/C3/§6) ---
fixes = [
    ("现行 = 148 行（145 done / 1 running：A-107 / 2 open：A-30、S-06）。",
     "现行 = 148 行（A-107 已收口 `91194d2`；2 open：A-30、S-06）。"),
    ("12 份 handoff、144 子代理 jsonl + 157 md",
     "12 份 handoff、145 个 jsonl（含 1 非子代理件）+ 157 md"),
    ("（6 slugs + MANIFEST；家族根制度见其 README）",
     "（5 slugs 非空 + MANIFEST；空 slug 留待清理；家族根制度见其 README）"),
]
for _old, _new in fixes:
    _c = dig.count(_old)
    assert _c == 1, f"fix pattern count={_c}: {_old[:60]}"
    dig = dig.replace(_old, _new)
print("digest: 3 verification fixes applied")

DIG.write_text(dig, encoding="utf-8")

# --- 2. OPS-LOG §17 ---
assert "## 17. 站稳脚跟运维波" not in log, "OPS-LOG §17 already appended"
sec17 = """## 17. 站稳脚跟运维波（2026-10-16）—— 会话考古 / 家族归档 / 收口

- **fleet 同题波**：Owner 同一「站稳脚跟」提示词发给 ~10 个项目会话（07:30–07:44 起跑）；家族备份根 `F:/backup_famlti_family` 建立（SKIAPI 会话设计结构 + README + `_meta/CLAIMS.md` 认领制；协调者 = Any2API 会话，共享区 sessions-archive/sessions-aux/tarballs/孤儿桶归其与他会话）。
- **本波（DBrain 线，会话 `01a141b9`，07:41 起）**：
  1. **考古/蒸馏**：S-main（06-29-46）终态盘点（145 jsonl + 157 md + 2,114 log + 12 handoff；06:28 SIGHUP 死亡）→ 12 handoff 全读 + 25 报告选读 → `session-digest.md` 补齐 waves11–21 + 〔更正〕C1–C5（91→184 行）；机械件 = 浓缩 1,663 行 + 索引 648 行（抽验 3/3）。
  2. **归档**：6 slugs → `F:/backup_famlti_family/sessions/Designers_Brain/raw-20261016/`（2,545 文件 / 369,307,549 B；compare 非 live 差异 0；sha 143 条 141 一致 + 2 live；MANIFEST + SHA256SUMS + 收据）；e714 空槽位 HTML → `aux/`（唯一痕迹留档）。
  3. **清理**：项目树 71 件 + `_scratch/` 9 目录 → `quarantine/Designers_Brain/`（只移不删）；会话树零字节/备份日志清理另见收据。
  4. **收口**：死亡点 sweep（crosslink 10 处 + A-102/A-107/A-108/A-109）`91194d2`；E 系校验器漂移修复（3 断言 + 2 文本；4/4 复跑 PASS）`4bdccbb`；louvre WAF 页清除 `19773a3`；本波记录提交（见 git log）。**三检查后推送 origin/main。**
- **事故/教训**：① provider 503 波（08:2x–10:0x）杀死 5 工（transcript 失）→ `-2` 后缀重派 + 写盘纪律；② scout 子代理写项目树受限（`write` 拒；bash 重定向可行）；③ 校验器硬编码数字随卡数增长必破（`ok=33`→动态解析 ≥33 保底）；④ E2 verify 曾 EXIT=1 = 期望值漂移非回归（修复后全绿）。
- 家族侧：`receipts/Designers_Brain-standfirm-20261016.md`（§A 复制 / §B 隔离 / §C f-outer / §D 汇总）；`digests/Designers_Brain/`；`f-outer/Designers_Brain/README.md`（0 件）；`_meta/lane-Designers_Brain.md`。
"""
LOG.write_text(log.rstrip("\n") + "\n\n" + sec17, encoding="utf-8")
print("OPS-LOG §17 appended")

# --- 3. GOALS ST lane ---
anchor = "## 环境实测（2026-10-15，供后续引用）"
assert goals.count(anchor) == 1, "GOALS anchor not unique"
assert "Lane ST" not in goals, "ST lane already present"
st = """## Lane ST — 站稳运维（2026-10-16）

> 波记录：`ops/archaeology-2026-10-16/`（MAIN-BRAIN.md + reports 01–10）· 交接：`~/.dwgx/ops/detail-2026-10-16-designers-brain-standfirm.md`

| ID | 状态 | 目标 | 产出路径 | 归属 |
|---|---|---|---|---|
| ST-01 | done | 会话深度考古 + 蒸馏补齐（waves11–21 + 〔更正〕C1–C5；91→184 行；浓缩件/索引/子代理目录） | `ops/session-digest.md` + `ops/archaeology-2026-10-16/reports/` | 主脑（站稳波） |
| ST-02 | done | 会话全量归档 → 家族根：6 slugs / 2,545 文件 / 369,307,549 B；非 live 差异 0；MANIFEST + SHA256SUMS + 收据 | `F:/backup_famlti_family/sessions/Designers_Brain/` | ArchivistFinish（站稳波） |
| ST-03 | done | 垃圾隔离（只移不删）：项目树 71 件 + `_scratch` 9 目录 + 会话树零字节/备份日志 | `F:/backup_famlti_family/quarantine/Designers_Brain/` | CleanerProject / CleanerSession（站稳波） |
| ST-04 | done | 仓库收口：死亡点 sweep `91194d2` + 校验器同步 `4bdccbb` + louvre `19773a3` + 本波记录提交；三检查后推送 | git `main` | 主脑（站稳波） |
| ST-05 | done | 交接与家族回报：五件 detail + 机器板 + digests 副本 + receipts + 终报 | `~/.dwgx/ops/detail-2026-10-16-designers-brain-standfirm.md` 等 | 主脑（站稳波） |

"""
goals = goals.replace(anchor, st + anchor)
GOALS.write_text(goals, encoding="utf-8")
print("GOALS ST lane inserted")
print("ALL OK")
