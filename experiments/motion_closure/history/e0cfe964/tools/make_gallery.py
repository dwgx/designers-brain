#!/usr/bin/env python3
"""Generate gallery/index.html and gallery/README.md from manifest measured data."""
import os
import json
import html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    man = json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))
    cards = man["cards"]
    rows = []
    for c in sorted(cards):
        p = cards[c]
        m = p["measured"]
        rel = p["platform"]["relation"]
        rel_label = {"same": "reused original", "restricted_adaptation": "native re-render (scaled geometry)"}.get(rel, rel)
        rows.append({
            "id": c, "slug": p["slug"], "mech": p["mechanism"],
            "res": "%dx%d" % tuple(m["dimensions_set"][0]) if m["dimensions_set"] else "n/a",
            "frames": m["decoded_frames"], "fps": m["fps"], "dur": m["duration_sec"],
            "sha": p["output_sha256"][:16], "size": p["size_bytes"],
            "kind": rel_label,
            "sheet": "contact_sheets/MOTION-%s.jpg" % c,
            "media": "../media/MOTION-%s.mp4" % c,
            "distinct": m["distinct_sample_count"],
        })

    # HTML
    h = ["<!doctype html>", "<html lang='en'><head><meta charset='utf-8'>",
         "<meta name='viewport' content='width=device-width,initial-scale=1'>",
         "<title>Designers_Brain Motion Closure — 12-card gallery</title>",
         "<style>body{font-family:system-ui,sans-serif;max-width:1200px;margin:2em auto;padding:0 1em;color:#1a1a1a}",
         "table{border-collapse:collapse;width:100%;font-size:14px}th,td{border:1px solid #ccc;padding:6px 8px;text-align:left}",
         "th{background:#eef2f7}.card{display:inline-block;margin:10px;width:300px;vertical-align:top}",
         ".card img{width:100%;border:1px solid #ccc}.note{background:#fff8e1;border-left:4px solid #f0ad4e;padding:10px;margin:1em 0}",
         "code{font-size:12px}video{width:100%}</style></head><body>",
         "<h1>Designers_Brain Motion Closure — 12-card gallery</h1>",
         "<div class='note'><strong>Honest status:</strong> These are model-rendered research artifacts; "
         "<code>human_review=pending</code> (no human aesthetic acceptance recorded). "
         "All 12 are raster-render proof at 1920x1080/300f/30fps/10s; five cards reuse the original "
         "valid 1080 mp4 after fresh full decode, seven are native re-renders of the frozen pure "
         "renderer with integer-scaled geometry. This is <em>not</em> browser/WebGL native-render proof. "
         "Evidence: full decode + deterministic batch hashes + truncated/swapped negative controls.</div>",
         "<h2>Measured data (fresh full decode of delivered bytes)</h2>",
         "<table><tr><th>Card</th><th>Slug / mechanism</th><th>Delivery kind</th><th>Res</th>"
         "<th>Frames</th><th>FPS</th><th>Dur</th><th>Distinct</th><th>Size</th><th>sha256 prefix</th></tr>"]
    for r in rows:
        h.append("<tr><td>%s</td><td>%s<br><small>%s</small></td><td>%s</td><td>%s</td>"
                 "<td>%s</td><td>%s</td><td>%ss</td><td>%s</td><td>%d</td><td><code>%s</code></td></tr>" % (
                     r["id"], html.escape(r["slug"]), html.escape(r["mech"]),
                     html.escape(r["kind"]), r["res"], r["frames"], r["fps"], r["dur"],
                     r["distinct"], r["size"], r["sha"]))
    h.append("</table><h2>Contact sheets (8 sampled frames each)</h2>")
    for r in rows:
        h.append("<div class='card'><strong>MOTION-%s — %s</strong><br>"
                 "<a href='%s'><img src='%s' alt='contact sheet MOTION-%s'></a><br>"
                 "<a href='%s'>view mp4</a> · <a href='../sources/MOTION-%s/README.md'>source/README</a></div>" % (
                     r["id"], html.escape(r["slug"]), r["sheet"], r["sheet"], r["id"],
                     r["media"], r["id"]))
    h.append("</body></html>")
    with open(os.path.join(ROOT, "gallery", "index.html"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(h))

    # Markdown README
    md = ["# Motion Closure gallery — 12 cards", "",
          "**Status:** model-rendered research artifacts; `human_review=pending`. "
          "Raster-render proof at 1920x1080/300f/30fps/10s, not browser/WebGL native-render proof.", "",
          "| Card | Slug | Delivery kind | Res | Frames | FPS | Dur | Distinct | Size | sha256 prefix |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        md.append("| %s | %s | %s | %s | %s | %s | %ss | %s | %d | `%s` |" % (
            r["id"], r["slug"], r["kind"], r["res"], r["frames"], r["fps"], r["dur"],
            r["distinct"], r["size"], r["sha"]))
    md += ["", "Open `index.html` for the contact sheets and per-card links. "
           "Per-card reproduction commands and honest adaptation notes are in "
           "`sources/MOTION-XX/README.md`. Manifest: `manifest.json` (original staging hashes "
           "and new output hashes recorded separately).",
           "Contact sheets: `gallery/contact_sheets/MOTION-XX.jpg` (8 frames sampled 0..299).", ""]
    with open(os.path.join(ROOT, "gallery", "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print(json.dumps({"gallery_html": True, "gallery_md": True, "cards": len(rows)}))


if __name__ == "__main__":
    main()
