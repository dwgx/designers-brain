#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E-03 · E1_t1c · 将 §8.1b v2（从句级改写版）写入 michelangelo 模块卡。

口径（E-03 · E1_t1c，2026-10-15）：
  - 触发：E-02（E1_t1b）同格重跑发现 michelangelo「部分解除」——仅删题材名词不足；
    风格语言（serpentine torsion / 雕塑式体积 / 仰视透视 / many interlocking forms）
    仍与人体绑定，输出中巨型肌肉形体随风格回归（云体巨人/盘绕巨体）。
  - 动作（v2 从句级改写）：把人体绑定从句改写成可迁移到无机物的等价视觉语言——
    ① 体积块面扭转→岩石/浪体（+云）块体的扭转；② 仰视透视→低角度构图；
    ③ 肌肉起伏→表面雕塑化起伏；另清扫 2 处 forms→masses。保留可判定阈值。
  - v1 原样保留（可审计）：卡内「### v1 审计存档」小节（逐字块）+ 本目录
    `s81b_v1_snapshot.md`（整节逐字）+ 备份 `_backup_card_before_v2/michelangelo.md`。

用法:
  python _apply_s81b_v2.py --dry     # 预览（不写盘）
  python _apply_s81b_v2.py           # 备份 → 快照 → 写卡 → 自检
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "knowledge", "domains", "painters", "modules"))
CARD = os.path.join(MODULES_DIR, "michelangelo.md")
BACKUP_DIR = os.path.join(HERE, "_backup_card_before_v2")
WRAP_WIDTH = 78

SECTION_HEAD = "## §8.1b 纯风格段（场景可迁移）"
NEXT_HEAD = "\n## 代码艺术规则（§8.2 原样）"
V2_MARKER = "**正向段 v2（可直接粘贴）**："
ARCHIVE_HEAD = "### v1 审计存档（E-02 原版，2026-10-15；勿用于生成）"

# ---------------------------------------------------------------------------
# v2 正文（单行逻辑文本；写卡时按 §8.1 同款折行 width=78）
# ---------------------------------------------------------------------------
V2_TEXT = (
    "High Renaissance fresco in the manner of Michelangelo Buonarroti: colossal "
    "masses with clearly defined volumes; rock, wave and cloud masses locked in "
    "serpentine torsion — counter-rotating blocks forming an S-curve; low-angle "
    "composition, strong foreshortening, monumental scale; sculptural modelling — "
    "surfaces rise and fall as if chiselled from solid mass, hard-edged cast "
    "shadows, relief-like light and shadow; dense swirling composition of many "
    "interlocking masses rotating around a calm central axis; limited fresco "
    "palette of earthy ochre, muted green, pale violet and sky blue, matte "
    "plaster surface; an atmosphere of awe and terribilità"
)

# 从句级前后对照（逐处；含保留阈值说明）
CLAUSE_MAP = [
    {
        "n": 1,
        "clause_v1": "colossal, heroic forms with clearly defined volumes",
        "clause_v2": "colossal masses with clearly defined volumes",
        "change_type": "形体词清扫（heroic forms→masses）",
        "kept": "colossal（尺度）/ clearly defined volumes（体积可读性）",
        "reason": "「heroic forms」是英雄人体词；与后句扭转联读会被实体化为裸体肌体。"
                  "主语改为无机「masses」，尺度与体积可判定性不变。",
    },
    {
        "n": 2,
        "clause_v1": "forms locked in serpentine torsion — counter-rotations forming an S-curve",
        "clause_v2": "rock, wave and cloud masses locked in serpentine torsion — "
                     "counter-rotating blocks forming an S-curve",
        "change_type": "体积块面扭转→岩石/浪体（+云）块体的扭转",
        "kept": "serpentine torsion / S-curve（几何可判定，对应 §8.2-2 扭转检测的视觉源）",
        "reason": "扭转主体显式绑定无机块体（岩石/浪体为主，云体一并纳入——E-02 证据中"
                  "「云体巨人」是主要人体化载体之一）；counter-rotations→counter-rotating "
                  "blocks（块面级表述）。",
    },
    {
        "n": 3,
        "clause_v1": "forms designed to be seen from below, strong foreshortening, monumental scale",
        "clause_v2": "low-angle composition, strong foreshortening, monumental scale",
        "change_type": "仰视透视→低角度构图",
        "kept": "strong foreshortening / monumental scale（透视与尺度可读性）",
        "reason": "视角升格为构图级属性（低角度构图），不再暗示「供仰视的（人物）形体」。",
    },
    {
        "n": 4,
        "clause_v1": "sculptural modelling — forms look chiselled out of the surface, "
                     "hard-edged cast shadows, relief-like light and shadow",
        "clause_v2": "sculptural modelling — surfaces rise and fall as if chiselled from "
                     "solid mass, hard-edged cast shadows, relief-like light and shadow",
        "change_type": "肌肉起伏→表面雕塑化起伏",
        "kept": "hard-edged cast shadows / relief-like light and shadow（§8.2-3 硬边阴影，"
                "过渡带 ≤0.6% 短边）",
        "reason": "塑造对象从「forms（会读成肌体）」改为「surface 的起伏」；chiselled 保留"
                  "「凿出」的雕刻感。",
    },
    {
        "n": 5,
        "clause_v1": "dense swirling composition of many interlocking forms rotating around "
                     "a calm central axis",
        "clause_v2": "dense swirling composition of many interlocking masses rotating around "
                     "a calm central axis",
        "change_type": "形体词清扫（interlocking forms→masses）",
        "kept": "dense / swirling / calm central axis（§8.2-4 构图密度 ≥55%、空白 ≤15%）",
        "reason": "「many interlocking forms」是 E-02 点名的另一人体触发词；改为 masses。",
    },
    {
        "n": 6,
        "clause_v1": "limited fresco palette of earthy ochre, muted green, pale violet and "
                     "sky blue, matte plaster surface",
        "clause_v2": "（不变）",
        "change_type": "保留",
        "kept": "§8.2-6 色彩（全帧饱和 ≤0.5、强调色 ≤2、四族限色）",
        "reason": "无人体绑定（flesh tones 已于 v1 删除）。",
    },
    {
        "n": 7,
        "clause_v1": "an atmosphere of awe and terribilità",
        "clause_v2": "（不变）",
        "change_type": "保留",
        "kept": "氛围词（无形体绑定）",
        "reason": "terribilità 为风格签名，无人体绑定。",
    },
]

THRESHOLDS_KEPT = [
    "S-curve 反扭（serpentine torsion + counter-rotating blocks）→ §8.2-2 扭转检测的视觉源",
    "hard-edged cast shadows → §8.2-3 硬边阴影（明暗过渡带 ≤0.6% 短边）",
    "dense swirling composition + calm central axis → §8.2-4 构图密度（人群/主体 ≥55%、空白 ≤15%）",
    "limited fresco palette（四族）→ §8.2-6 色彩（全帧饱和 ≤0.5、强调色 ≤2）",
    "monumental scale / strong foreshortening → 尺度与透视可读性（剪影可读性 §8.2-5 的构图前提）",
]


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def find_section(text: str):
    i = text.find(SECTION_HEAD)
    if i < 0:
        raise SystemExit("FATAL: §8.1b section head not found")
    if text.count(SECTION_HEAD) != 1:
        raise SystemExit("FATAL: §8.1b section head not unique")
    j = text.find(NEXT_HEAD, i)
    if j < 0:
        raise SystemExit("FATAL: §8.2 heading not found after §8.1b")
    return i, j, text[i:j]


def extract_fence_after(sec: str, marker: str) -> str:
    m = sec.find(marker)
    if m < 0:
        raise SystemExit("FATAL: marker not found: %s" % marker)
    j = sec.find("```", m)
    k = sec.find("```", j + 3)
    if j < 0 or k < 0:
        raise SystemExit("FATAL: fence not found after marker")
    return sec[j + 3:k]


def build_new_section(v1_block_exact: str) -> str:
    wrapped_v2 = textwrap.fill(V2_TEXT, width=WRAP_WIDTH, break_on_hyphens=False)
    note1 = (
        "> v2 修订（E-03 · E1_t1c，2026-10-15）：E-02 重跑发现「部分解除」——灯塔回中心"
        "但巨型肌肉形体仍环绕；仅删题材名词不足，扭转/雕塑体积/仰视透视等风格语言本身把"
        "人形带回。本版从句级改写为可迁移到无机物的等价语言：① 体积块面扭转→岩石/浪体"
        "（+云）块体的扭转；② 仰视透视→低角度构图；③ 肌肉起伏→表面雕塑化起伏；另清扫 2 处 "
        "forms→masses。可判定阈值保留：S-curve 反扭、硬边阴影、漩涡构图、限色。"
    )
    note2 = (
        "> 用法：主题句 + 本段（同 §8.1 配方）；负向段沿用 §8.1 原文（本通道不发送）。v2 的"
        "块体名词（岩石/浪体/云体）对应 T1 场景无机块体，换场景时按同类替换。"
    )
    note3 = (
        "> 审计：v1（E-02 原版）逐字存档见下方「v1 审计存档」小节；逐处前后对照见 "
        "`experiments/E1_t1c/RESULTS_t1c.md` §2 与 `s81b_v2_derivation.json`。"
    )
    archive_note = (
        "> 原样保留供审计与 E1_t1b 复现（v1 单行文本 sha256 "
        "`3326164fb5666fb9cd5dc896ea3cd267c4c95f9f568e2d96c8909cbc0ee24c2c`；"
        "整节全文另存 `experiments/E1_t1c/s81b_v1_snapshot.md`）。"
    )
    parts = [
        SECTION_HEAD,
        "",
        note1,
        note2,
        note3,
        "",
        V2_MARKER,
        "```",
        wrapped_v2,
        "```",
        "",
        ARCHIVE_HEAD,
        "",
        archive_note,
        "",
        "```" + v1_block_exact + "```",
    ]
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    text = open(CARD, encoding="utf-8").read()
    i, j, old_section = find_section(text)

    # 当前 v1 块（逐字，含首尾换行）与单行文本
    v1_block = extract_fence_after(old_section, "**正向段（可直接粘贴）**：")
    v1_single = " ".join(v1_block.split())

    # 自检：v1 单行 sha 必须与 E1_t1b 记录一致
    V1_SHA_EXPECT = "3326164fb5666fb9cd5dc896ea3cd267c4c95f9f568e2d96c8909cbc0ee24c2c"
    got = sha256_text(v1_single)
    if got != V1_SHA_EXPECT:
        raise SystemExit("FATAL: v1 sha mismatch: %s != %s" % (got, V1_SHA_EXPECT))

    new_section = build_new_section(v1_block)
    new_text = text[:i] + new_section + text[j:]

    # 自检：新文本里 §8.1b 只有一个、v2 块可解包且与 V2_TEXT 一致、v1 存档与原文逐字一致
    _, _, sec2 = find_section(new_text)
    v2_block = extract_fence_after(sec2, V2_MARKER)
    assert " ".join(v2_block.split()) == V2_TEXT, "v2 block mismatch"
    assert v1_block in sec2, "v1 archive block not verbatim"

    wrapped_v2 = textwrap.fill(V2_TEXT, width=WRAP_WIDTH, break_on_hyphens=False)
    if args.dry:
        print("== DRY RUN ==")
        print("old section: %d chars, sha=%s" % (len(old_section), sha256_text(old_section)[:16]))
        print("new section: %d chars" % len(new_section))
        print("---- new section preview ----")
        print(new_section)
        return

    # 写盘：备份 → 快照 → 写卡 → 自检
    os.makedirs(BACKUP_DIR, exist_ok=True)
    shutil.copy2(CARD, os.path.join(BACKUP_DIR, "michelangelo.md"))

    with open(os.path.join(HERE, "s81b_v1_snapshot.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(old_section)

    with open(CARD, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(new_text)

    # 审计 JSON
    rec = {
        "date": "2026-10-15",
        "task": "E-03 · E1_t1c · michelangelo §8.1b v2 从句级改写",
        "trigger": ("E-02 · E1_t1b §4.2：部分解除——灯塔回中心但巨型肌肉形体仍环绕；"
                    "风格语言（serpentine torsion / 雕塑式体积 / 仰视透视 / many interlocking forms）"
                    "与人体绑定，仅删题材名词不足。"),
        "v1": {
            "text": v1_single,
            "text_sha256": sha256_text(v1_single),
            "section_sha256": sha256_text(old_section),
            "snapshot": "experiments/E1_t1c/s81b_v1_snapshot.md（整节逐字）",
            "card_archive": "michelangelo.md §8.1b → ### v1 审计存档（逐字块）",
            "backup": "experiments/E1_t1c/_backup_card_before_v2/michelangelo.md",
        },
        "v2": {
            "text": V2_TEXT,
            "text_sha256": sha256_text(V2_TEXT),
            "wrapped": wrapped_v2,
            "card_block": "michelangelo.md §8.1b → **正向段 v2（可直接粘贴）**",
        },
        "clause_map": CLAUSE_MAP,
        "thresholds_kept": THRESHOLDS_KEPT,
        "notes": ("v2 以无机块体（岩石/浪体/云体）承载原人体绑定语言；换场景时把块体名词替换为"
                  "该场景的无机块体。未加入显式反人物短语（保持「仅从句级改写」的实验纯度——"
                  "若重跑仍绑定，记为新问题/后续手段）。"),
    }
    with open(os.path.join(HERE, "s81b_v2_derivation.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rec, fh, ensure_ascii=False, indent=2)

    print("wrote card: %s" % CARD)
    print("  v1 sha=%s" % sha256_text(v1_single)[:16])
    print("  v2 sha=%s" % sha256_text(V2_TEXT)[:16])
    print("wrote s81b_v1_snapshot.md + s81b_v2_derivation.json")
    print("backup -> %s" % os.path.join(BACKUP_DIR, "michelangelo.md"))

    # 逐字校验（模块库工具）
    r = subprocess.run([sys.executable, "_extract.py", "--check"], cwd=MODULES_DIR,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    tail = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "(no output)"
    print("module check: %s" % tail)


if __name__ == "__main__":
    main()
