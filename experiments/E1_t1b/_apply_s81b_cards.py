#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E-02 · 把 §8.1b（纯风格段 / 场景可迁移性注记）写入 11 张模块卡。

口径（E-02 · E1_t1b，2026-10-15）：
  - 受影响模块（诊断 = 场景被替换）：新增「## §8.1b 纯风格段（场景可迁移）」= §8.1 正向段
    删除题材词（人物/肖像/室内/静物）与场景专属道具后、仅留视觉语言的编辑版（最小改写）。
  - 未偏置模块：新增「## §8.1b 场景可迁移性注记」（一句话）。
  - 插入位置：§8.1 之后、§8.2 之前；§8.1/§8.2/§4 正文不动（逐字校验不受影响，
    _extract.py 的 card_81 已支持在 §8.1b 处截断）。

用法:
  python _apply_s81b_cards.py --dry     # 预览（不写盘）
  python _apply_s81b_cards.py           # 备份 → 写入 → 校验
"""
import argparse
import json
import os
import shutil
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "knowledge", "domains", "painters", "modules"))
BACKUP_DIR = os.path.join(HERE, "_backup_cards_before_s81b")
ANCHOR = "## 代码艺术规则（§8.2 原样）"
WRAP_WIDTH = 78

# ---------------------------------------------------------------------------
# §8.1b 正文（单行逻辑文本；写卡时按 §8.1 同款折行）
# ---------------------------------------------------------------------------

PURE_STYLE = {
    "da_vinci": {
        "text": (
            "Renaissance oil painting in the manner of Leonardo da Vinci, sfumato: absolutely no hard "
            "contours anywhere, every light-to-shadow transition is a wide, continuous grey gradient, "
            "soft smoky modelling; single soft light from the upper left moulding forms out of deep "
            "shadow; aerial perspective — distant forms turn blue-grey, lose saturation and dissolve "
            "into haze; narrow earth palette of ochre, umber, muted blue and dull gold, overall low "
            "saturation; rocks shaped like rounded cones, wet atmosphere over shallow green water; "
            "invisible brushwork, glazed surface, matte, aged varnish warmth; contemplative, quiet, "
            "mysterious mood"
        ),
        "removed": "young woman、half-smile、curly hair、figures、flowers",
        "rewritten": "the figures→forms、distant mountains→distant forms",
    },
    "michelangelo": {
        "text": (
            "High Renaissance fresco in the manner of Michelangelo Buonarroti: colossal, heroic forms "
            "with clearly defined volumes; forms locked in serpentine torsion — counter-rotations "
            "forming an S-curve; forms designed to be seen from below, strong foreshortening, "
            "monumental scale; sculptural modelling — forms look chiselled out of the surface, "
            "hard-edged cast shadows, relief-like light and shadow; dense swirling composition of many "
            "interlocking forms rotating around a calm central axis; limited fresco palette of earthy "
            "ochre, muted green, pale violet and sky blue, matte plaster surface; an atmosphere of awe "
            "and terribilità"
        ),
        "removed": "nude figures、muscle groups、bodies（torsion）、drapery、idealised faces、flesh tones",
        "rewritten": "figures→forms（3 处）",
    },
    "picasso": {
        "text": (
            "Analytic Cubist painting in the manner of Picasso, autumn 1910: the scene fractured into "
            "40–120 semi-transparent angular planes; foreground and background merge into one shallow, "
            "crystalline lattice; 3–5 simultaneous viewpoints; palette restricted to 4–5 hues — ochre, "
            "umber, warm grey, slate, black — with at least 6 value steps; form modeled only by value "
            "jumps between flat planes, no gradients; matte oil-on-canvas surface, fine canvas weave; "
            "brightest values concentrated at the center, dark aura toward the edges; composition reads "
            "as monumental, melancholic."
        ),
        "removed": "portrait、seated man、anchors（hair/tie/watch/hands）、seated pose、frontally posed",
        "rewritten": "figure and background→foreground and background",
    },
    "cezanne": {
        "text": (
            "Late Cézanne landscape in the manner of his late period (1895–1906): the entire surface "
            "built from short, visible parallel brushstrokes (taches) of 0.5–1.5 cm equivalent, "
            "arranged in groups of 4–8 directional families that both model volume and unify the "
            "picture plane; forms constructed only by color modulation — light, half-tone and "
            "quarter-tone steps of ochre, orange, olive, viridian, cobalt and ultramarine — never by "
            "black shading; forms carry broken, multiple outlines, 30% of contour segments left open "
            "so forms merge into the background; a network of blue in shadows, contours and sky "
            "(12–15% of pixels); sky and earth painted with equal substance, no atmospheric recession, "
            "distant forms the same scale as near ones; shifting viewpoints within one frame; 5–8% of "
            "the canvas left thinly covered or bare, suggesting unfinish; dry, matte oil surface, fine "
            "canvas weave visible."
        ),
        "removed": "still-life foreground、Bathers period、tipped tabletop",
        "rewritten": "objects carry→forms carry、Bathers period→late period",
    },
    "caravaggio": {
        "text": (
            "Caravaggio-style tenebrist oil painting: one single hard directional light from high left, "
            "no fill light, no reflected light; background areas in near-black shadow (values under "
            "10% of the lit highlights); deep dark brown ground left visible inside the shadows as "
            "their mid-tone; violent chiaroscuro: lit passages bright and warm, shadows crushed, "
            "midtones suppressed; one frozen instant of dramatic action; the main motif pushed flat "
            "against the picture plane and cropped by the frame edge; restrained earth palette — "
            "ochre, madder red, lead white, bitumen black, one or two saturated accents; direct "
            "painting, broad final touches, impasto highlights on the lit edges"
        ),
        "removed": "faces and hands、gestures、working people as saints、dark interior（no landscape/no sky）、prop accent",
        "rewritten": "walls and floor→areas、figures pushed flat→the main motif pushed flat、narrative action→dramatic action",
    },
    "vermeer": {
        "text": (
            "quiet Dutch Golden Age painting: soft natural daylight from a single source on the LEFT, "
            "large pale areas catching the light, high-key tonality, deep shadows rendered as flat "
            "unmodulated areas of cool blue-grey paint (no detail inside shadows), dominant colour "
            "pair of natural ultramarine blue and ochre yellow with tiny red accents, specular "
            "highlights painted as small round globular dots (pointillés) on glossy surfaces, soft "
            "edges with no hard contour lines (sfumato, details deliberately omitted), matte and "
            "glossy surfaces distinguished only by the shape of their highlights, single-point "
            "perspective grid, thin translucent glazes over a light grey ground, smooth levigated "
            "paint surface with the canvas weave barely visible, dark neutral or deep green backdrop, "
            "timeless stillness, oil on canvas, museum-quality"
        ),
        "removed": "interior genre scene、single figure、window、plaster wall、object list（porcelain…bread crust）、tiled floor/window frames、Delft world",
        "rewritten": "single window→single source、plaster wall→pale areas、pushing the figure forward 删除",
    },
    "durer": {
        "text": (
            "Northern Renaissance engraving in the manner of Albrecht Dürer's burin master prints "
            "(1513-1514): pure black ink line work on warm off-white paper, no grey fill anywhere - "
            "every tone is built from parallel hatching and layered cross-hatching; hatching lines "
            "follow and wrap each volume; cross layers sit at 30-45 degrees; line spacing tapers from "
            "about 6px in the lights to 1.5px in the darks (1000px wide frame), darkest zones get 3 or "
            "more superimposed hatch directions; engraved lines swell slightly mid-stroke and end in "
            "fine points; hard contour lines separate every form: no soft edges, no sfumato, no "
            "airbrush; hyper-detailed microtexture; backgrounds closed with dense parallel line fields "
            "instead of empty space; calm, measured composition"
        ),
        "removed": "contrapposto figures、microtexture examples（hairs/grass/leaf）、monogram plate、cartellino、allegorical still-life",
        "rewritten": "calm measured figures…→calm, measured composition",
    },
}

NOTES = {
    "van_gogh": "§8.1 无人物/肖像/室内/静物题材词；E1_t1 灯塔场景保留，风格可直接跨场景迁移（cypress / wheat field / stars 等风景道具词仅作次要元素出现，可按需删除）。",
    "monet": "§8.1 无题材词；E1_t1 灯塔场景完整保留，风格可直接跨场景迁移（无需拆分）。",
    "matisse": "§8.1 仅含装饰母题词（dancer / snail / leaf / star）；E1_t1 未见人物实体化、场景保留，风格可迁移（如需更纯净可删母题词）。",
    "hokusai": "§8.1 含 Mount Fuji / tiny figures 等非主体题材词；E1_t1 中仅作远景与比例元素、未替换场景，风格可迁移（如需更纯净可删上述词）。",
}


def build_block(module_id):
    if module_id in PURE_STYLE:
        m = PURE_STYLE[module_id]
        wrapped = textwrap.fill(m["text"], width=WRAP_WIDTH, break_on_hyphens=False)
        return (
            "## §8.1b 纯风格段（场景可迁移）\n\n"
            "> 派生自 §8.1 正向段（E-02 · E1_t1b，2026-10-15）：删除题材词（人物/肖像/室内/静物）与场景专属道具，仅保留视觉语言（光/色/笔触/结构/构图规则）；用法：主题句 + 本段（同 §8.1 配方）。负向段沿用 §8.1 原文（本通道不发送）。\n"
            "> 删除项：%s；最小改写：%s。明细见 `experiments/E1_t1b/RESULTS_t1b.md` §2。\n\n"
            "**正向段（可直接粘贴）**：\n```\n%s\n```" % (m["removed"], m["rewritten"], wrapped)
        )
    note = NOTES[module_id]
    return (
        "## §8.1b 场景可迁移性注记\n\n"
        "> E-02 · E1_t1b 诊断（2026-10-15）：%s" % note
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    ids = ["da_vinci", "michelangelo", "van_gogh", "monet", "picasso", "cezanne",
           "matisse", "hokusai", "caravaggio", "vermeer", "durer"]
    os.makedirs(BACKUP_DIR, exist_ok=True)
    report = []
    for mid in ids:
        path = os.path.join(MODULES_DIR, mid + ".md")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        n_anchor = text.count(ANCHOR)
        assert n_anchor == 1, "%s: anchor count=%d" % (mid, n_anchor)
        assert "§8.1b" not in text, "%s: §8.1b already present" % mid
        block = build_block(mid)
        assert block.count("```") % 2 == 0, "%s: fence imbalance" % mid
        new_text = text.replace(ANCHOR, block + "\n\n" + ANCHOR, 1)
        kind = "pure_style" if mid in PURE_STYLE else "note"
        if args.dry:
            print("== %s [%s] ==\n%s\n" % (mid, kind, block[:400]))
        else:
            shutil.copy2(path, os.path.join(BACKUP_DIR, mid + ".md"))
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(new_text)
        report.append({"id": mid, "kind": kind, "chars": len(block)})

    if not args.dry:
        # 记录（审计用）
        rec = {
            "date": "2026-10-15",
            "task": "E-02 · E1_t1b · §8.1b 拆分",
            "pure_style": {k: {"text": v["text"], "removed": v["removed"], "rewritten": v["rewritten"]}
                           for k, v in PURE_STYLE.items()},
            "notes": NOTES,
            "inserted": report,
        }
        with open(os.path.join(HERE, "s81b_derivation.json"), "w", encoding="utf-8") as fh:
            json.dump(rec, fh, ensure_ascii=False, indent=2)
        print("done: %d cards updated (7 pure_style + 4 notes); backup -> %s" %
              (len(report), BACKUP_DIR))
    for r in report:
        print("  %-14s %-10s %5d chars" % (r["id"], r["kind"], r["chars"]))


if __name__ == "__main__":
    main()
