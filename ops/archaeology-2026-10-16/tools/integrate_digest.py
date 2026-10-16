#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integrate 02-digest-waves12-21.md into ops/session-digest.md (standfirm wave).

- Backup: ops/session-digest.md.before-standfirm-20261016 (only if not exists)
- Exact-anchor insertions; asserts everywhere; historical lines not rewritten.
- Run from anywhere: python integrate_digest.py
"""
import re, sys, shutil
from pathlib import Path

ROOT = Path(r"D:/Project/Designers_Brain")
DIG = ROOT / "ops" / "session-digest.md"
RPT = ROOT / "ops" / "archaeology-2026-10-16" / "reports" / "02-digest-waves12-21.md"

dig = DIG.read_text(encoding="utf-8")
rpt = RPT.read_text(encoding="utf-8")

if "〔更正〕（2026-10-16 追加）" in dig:
    sys.exit("ALREADY APPLIED - abort")

def section(text, start_marker, end_marker):
    i = text.index(start_marker)
    j = text.index(end_marker, i)
    return text[i:j]

# ---- extract blocks from report ----
sec2 = section(rpt, "## 1 · §2 追加行", "## 2 · §3")
rows2 = [l for l in sec2.splitlines() if re.match(r"^\| 2026-", l)]
assert len(rows2) == 23, f"rows2={len(rows2)}"

sec3 = section(rpt, "## 2 · §3", "## 3 · §4")
items3 = [l for l in sec3.splitlines() if re.match(r"^\d+\. ", l)]
assert len(items3) == 12, f"items3={len(items3)}"

sec4 = section(rpt, "## 3 · §4", "## 4 · §5")
items4 = [l for l in sec4.splitlines() if re.match(r"^\d+\. ", l)]
assert len(items4) == 9, f"items4={len(items4)}"

sec5 = section(rpt, "## 4 · §5", "## 5 · 〔更正〕").strip("\n")
assert "### A." in sec5 and "### B." in sec5

secC = section(rpt, "## 5 · 〔更正〕", "## 6 · 附 A")
m = re.search(r"```markdown\n(.*?)\n```", secC, re.S)
assert m, "correction fence not found"
corr = m.group(1).strip("\n")
assert "C1" in corr and "C5" in corr

# ---- header ----
old_header = "> 覆盖：omp 顶层会话 12 个（含图像探针 5 个）+ 子代理文件 39 个（未逐读）；handoff 4 份；截至 2026-10-15。"
new_header = "> 覆盖：S-main（06-29-46；终态 145 jsonl + 157 md + 2,114 log + 12 handoff）+ 图像探针 p1–p4 + 本波（22-41-02）；截至 2026-10-16（死亡点 06:28 + 本波增补）。"
assert dig.count(old_header) == 1, "header anchor"
dig = dig.replace(old_header, new_header)

# ---- §1 replace ----
sec1_new = """## 1 · 现在在哪（≤10 行）

- 项目：**艺术家视觉语言蒸馏系统**（Owner: dwgx1；已建 git + public 仓 `github.com/dwgx/designers-brain`；不训练模型）。入口 `AGENTS.md` → 队列 `GOALS.md`（唯一状态权威）/ 手册 `WORKFLOW.md` / 日志 `OPS-LOG.md`。
- 状态（2026-10-16 上午）：**画家 program 62 位全收口**（wave1–21；档案 62 / 语料 1613 条 / 图库公开 618 + 私有例外 676）；模块卡 **62 张**（checks 186/186）；三索引三轮合并（PASS 257/0）；skill 走查收口（S-05 done）。GOALS：145 done / 1 running（A-107 待收口）/ 2 open（A-30、S-06）。
- 主产物：A=`knowledge/domains/painters/`（dossiers 62 + `_corpus/` + `_images/` + `modules/` 62 卡）；B=`knowledge/agent-art/` + `experiments/anim_test_01..03`；E=`experiments/E1_t1..E2_t1`；S=`skills/designers-brain/`（junction ×4）；R=public 仓发布。
- 通道：omp/deepseek 默认（全部 in-session 子代理）；claude 停用、codex 401；图像 = 网关直连（`grok-imagine-image-2.0`；768×1152；无负向）。
- 2026-10-16 06:28：S-main 被 SIGHUP 杀死（死亡点遗留：2 commits 未推 + 10 文件未提交 + A-107 未收口）→ **本考古运维波接手**：会话归档 → `F:/backup_famlti_family/sessions/Designers_Brain/`；蒸馏补齐（本文件）；垃圾隔离；仓库收口；记录见 `ops/archaeology-2026-10-16/`。
- 下一步：A-30 学习路径卡 / S-06 spec v0.3 / wave21 主表并入（下轮索引）/ 模块卡 62→72 / E3/E4 与人评六维（详见 §5 更新块）。
- 纪律：一个路径一个写手；GOALS/OPS-LOG/机器板归主脑；证据分级 `[自述]/[史料]/[研究]/[归纳]/[推测]`；对外接口现状见 `OPS-LOG.md` §8。
"""
i1 = dig.index("## 1 · 现在在哪")
i2 = dig.index("## 2 · 大事记")
dig = dig[:i1] + sec1_new + "\n" + dig[i2:]

# ---- §2 append ----
anchor2 = "| 2026-10-15 晚 | 蒸馏 | 本 `SESSION-DIGEST.md` 生成；`shougong`（收工追加 §2）+ `考古.md`（先读 digest）保鲜链接线 | 本文件；board DIGEST-DBRAIN |"
assert dig.count(anchor2) == 1, "anchor2"
dig = dig.replace(anchor2, anchor2 + "\n" + "\n".join(rows2))

# ---- §3 append ----
anchor3 = "11. **「搜索失败 ≠ 内容缺口」**"
idx = dig.index(anchor3)
eol = dig.index("\n", idx)
dig = dig[:eol] + "\n" + "\n".join(items3) + dig[eol:]

# ---- §4 append ----
anchor4 = "10. **omp 瞬态"
idx = dig.index(anchor4)
eol = dig.index("\n", idx)
dig = dig[:eol] + "\n" + "\n".join(items4) + dig[eol:]

# ---- §5 update + corrections before §6 ----
sec6add = """
### 2026-10-16 考古波（站稳运维）增补

> 本波由新会话 `2026-10-15T22-41-02-476Z_01a141b9-de0c` 执行；S-main 实际运行至 2026-10-16 06:28:31 JST（sighup）。波内报告：`ops/archaeology-2026-10-16/reports/`（01–10 号 + MAIN-BRAIN.md）。

| 文件 | 日期 | 说明 |
|---|---|---|
| S-main `06-29-46_01a13e40`（终态） | 10-15→10-16 | 主脑全程：wave1–21；终态 = 145 jsonl + 157 md（含 12 handoff）+ 2,114 log + 4 子目录；06:28 死亡点见 §2 |
| `22-41-02_01a141b9`（本波） | 10-16 | 考古运维：归档 → F:、蒸馏补齐、垃圾隔离、仓库收口、handoff |
| `01a141af-e714`（空槽位） | 10-15 | 0 消息、未持久化；唯一痕迹 = HTML 导出（已归 F: `sessions/Designers_Brain/aux/`） |
| 会话归档 | — | `F:/backup_famlti_family/sessions/Designers_Brain/raw-20261016/`（6 slugs + MANIFEST；家族根制度见其 README） |
"""
block56 = "\n### 2026-10-16 更新（站稳波）\n\n" + sec5 + "\n\n" + corr + "\n"
i6 = dig.index("## 6 · 会话索引")
dig = dig[:i6] + block56 + "\n" + dig[i6:]

# ---- §6 append ----
anchor6 = "| 子代理 ×39（主会话目录） | 10-15 | 51.5 | wave1–10 具名工人（归属见 §2；未逐读） |"
assert dig.count(anchor6) == 1, "anchor6"
dig = dig.replace(anchor6, anchor6 + "\n" + sec6add)

# ---- backup + write ----
bak = DIG.with_name("session-digest.md.before-standfirm-20261016")
if not bak.exists():
    shutil.copy2(DIG, bak)
DIG.write_text(dig, encoding="utf-8")
print("OK")
print("new line count:", len(dig.splitlines()))
print("rows2:", len(rows2), "items3:", len(items3), "items4:", len(items4))
