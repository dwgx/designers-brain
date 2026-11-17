#!/usr/bin/env python3
"""Generate per-card README.md (reproduction block) from manifest + provenance.

Writes sources/MOTION-XX/README.md for each card with exact commands, params,
source/output sha separation, adaptation notes and honest status.
"""
import os
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def repro(card, p, prov):
    origin = p["origin"]
    res = p["params"]["resolution"]
    if card in ("02", "10", "12", "13", "15"):
        ext = prov["cards"][card]["original"]["renderer_file"]
        return (
            "# Reuse (no re-render)\n\n"
            "The delivered mp4 `media/MOTION-%s.mp4` is the immutable staging original, "
            "reused after a fresh full-decode (300 frames confirmed). The frozen renderer "
            "source is provided for reference only.\n\n"
            "```bash\n"
            "python tools/fresh_decode.py media/MOTION-%s.mp4   # decoded_frames=300, 1920x1080, 30fps\n"
            "```\n" % (card, card)
        )
    # re-rendered cards
    scale = p["params"]["geometry_scale"]
    if card in ("03", "14"):
        cmd_render = ("python tools/native_scale_render.py "
                      "sources/MOTION-%s/render.py renders/MOTION-%s full" % (card, card))
        cmd_batch = ("python tools/native_scale_render.py "
                     "sources/MOTION-%s/render.py _det_scratch/MOTION-%s-sample batch "
                     "5,77,150,233,299,77,150" % (card, card))
    else:
        pal = {
            "04": "rgb", "09": "rgb",
            "05": "[[26,26,58],[14,77,92],[138,75,30],[91,42,107],[16,26,58],[244,234,210],[40,30,50],[240,190,60]]",
            "06": "[[239,233,216],[26,26,26],[214,48,38],[240,190,0],[29,78,156]]",
            "07": "[[4,23,28],[7,31,38],[0,229,255],[255,106,0]]",
        }[card]
        cmd_render = ("node tools/native_scale_render.js "
                      "sources/MOTION-%s/render.js renders/MOTION-%s full 640 360 '%s'"
                      % (card, card, pal))
        cmd_batch = ("node tools/native_scale_render.js "
                     "sources/MOTION-%s/render.js _det_scratch/MOTION-%s-sample batch "
                     "640 360 '%s' 5,77,150,233,299,77,150" % (card, card, pal))
    return (
        "# Native re-render (frozen renderer + integer geometry scale S=%d)\n\n"
        "```bash\n"
        "# 1. render 300 native 1920x1080 PNG frames + frame_hashes.json\n"
        "%s\n"
        "# 2. deterministic fresh-process sample (non-contiguous / repeated)\n"
        "%s\n"
        "# 3. encode to mp4v MP4 (30fps / 1920x1080 / 300f)\n"
        "python tools/encode_frames.py renders/MOTION-%s/frames media/MOTION-%s.mp4 300\n"
        "# 4. verify all 12 delivered mp4s (full decode)\n"
        "python verify_all.py --dir .\n"
        "```\n" % (scale, cmd_render, cmd_batch, card, card)
    )


def main():
    man = json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))
    prov = json.load(open(os.path.join(ROOT, "provenance.json"), encoding="utf-8"))
    for card, p in man["cards"].items():
        o = p["original"]
        m = p["measured"]
        lines = [
            "# MOTION-%s — %s" % (card, p["slug"]),
            "",
            "Model-rendered research artifact. `human_review=pending` (no human aesthetic acceptance).",
            "",
            "## Contract / mechanism",
            "",
            "- Origin: %s" % p["origin"],
            "- Mechanism (from staging INVENTORY): %s" % prov["cards"][card]["mechanism"],
            "- Platform: target_renderer=`%s`; executed=`%s`; relation=`%s`." % (
                p["platform"]["target_renderer"], p["platform"]["executed_renderer"],
                p["platform"]["relation"]),
            "- Raster proof only — %s" % ("not a browser/WebGL native render."
                if "browser_native" in p["platform"] and not p["platform"]["browser_native"]
                else "platform as declared."),
            "- Audio: `%s`." % p["platform"]["audio"],
            "",
            "## Params",
            "",
            "- seed: `%s`" % p["params"]["seed"],
            "- resolution: `%s` (fps %s, frames %s)" % (
                p["params"]["resolution"], p["params"]["fps"], p["params"]["frames"]),
            "- schedule: %s" % p["params"]["schedule"],
            "- renderer: `%s`" % p["params"]["renderer"],
            "",
            "## Source vs output hashes (kept separate)",
            "",
            "- ORIGINAL staging renderer (%s) sha256: `%s`" % (
                o["renderer_file"], o["renderer_sha256"]),
            "- ORIGINAL staging mp4 (%s) sha256: `%s`" % (
                o["mp4_file"], o["mp4_sha256"]),
            "- ORIGINAL resolution: `%s`" % o["old_resolution"],
            "- DELIVERED mp4 sha256: `%s`" % p["output_sha256"],
            "- DELIVERED renderer copy sha256: `%s`" % p["renderer_source_sha256"],
            "",
            "## Measured (fresh full decode of delivered mp4)",
            "",
            "- decoded_frames: `%s`; dimensions: `%s`; fps: `%s`; duration: `%ss`" % (
                m["decoded_frames"], m["dimensions_set"], m["fps"], m["duration_sec"]),
            "- distinct first/mid/last signatures: `%s`" % m["distinct_sample_count"],
            "- size_bytes: `%s`" % p["size_bytes"],
            "- contact sheet: `gallery/contact_sheets/MOTION-%s.jpg` (8 keyframes)" % card,
            "",
            "## Adaptation notes (honesty)",
            "",
            p["notes"],
            "",
            "## Reproduction",
            "",
            repro(card, p, prov),
            "",
        ]
        path = os.path.join(ROOT, "sources", "MOTION-%s" % card, "README.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
    print(json.dumps({"readmes": len(man["cards"]), "ok": True}))


if __name__ == "__main__":
    main()
