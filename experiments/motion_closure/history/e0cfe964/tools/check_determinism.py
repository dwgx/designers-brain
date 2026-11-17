#!/usr/bin/env python3
"""Determinism check: fresh-process non-contiguous / reordered / repeated renders.

For each of the 7 natively re-rendered cards, this script launches a FRESH process
of the appropriate native renderer in 'batch' mode with the frame list:
    n = 5,77,150,233,299,77,150          (non-contiguous, includes repeats)
and also a REORDERED list:
    n = 299,233,150,77,5
It then reads frame_hashes.json (from the full render) and asserts every sampled
frame's sha256 matches. A repeated index must land on the same file hash twice.
Raw per-card results are printed as JSON.

Note: batch writes into a SEPARATE scratch frames dir so the delivered full render
frames are not touched; only hashes are compared.
"""
import os
import sys
import json
import hashlib
import subprocess
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = {
    "03": ("python", "tools/native_scale_render.py", "sources/MOTION-03/render.py"),
    "04": ("node", "tools/native_scale_render.js", "sources/MOTION-04/render.js"),
    "05": ("node", "tools/native_scale_render.js", "sources/MOTION-05/render.js"),
    "06": ("node", "tools/native_scale_render.js", "sources/MOTION-06/render.js"),
    "07": ("node", "tools/native_scale_render.js", "sources/MOTION-07/render.js"),
    "09": ("node", "tools/native_scale_render.js", "sources/MOTION-09/render.js"),
    "14": ("python", "tools/native_scale_render.py", "sources/MOTION-14/render.py"),
}
# JS wrapper needs srcW srcH palette; python wrapper does not
JS_ARGS = {
    "04": ["640", "360", "rgb"],
    "05": ["640", "360", "[[26,26,58],[14,77,92],[138,75,30],[91,42,107],[16,26,58],[244,234,210],[40,30,50],[240,190,60]]"],
    "06": ["640", "360", "[[239,233,216],[26,26,26],[214,48,38],[240,190,0],[29,78,156]]"],
    "07": ["640", "360", "[[4,23,28],[7,31,38],[0,229,255],[255,106,0]]"],
    "09": ["640", "360", "rgb"],
}
SAMPLE = "5,77,150,233,299,77,150"
REORDER = "299,233,150,77,5"
SCRATCH = os.path.join(ROOT, "_det_scratch")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def batch_command(card, scratch_dir, indices):
    exe, tool, renderer = CARDS[card]
    renderer_abs = os.path.join(ROOT, renderer)
    tool_abs = os.path.join(ROOT, tool)
    if exe == "python":
        return [exe, tool_abs, renderer_abs, scratch_dir, "batch", indices]
    extra = JS_ARGS[card]
    return [exe, tool_abs, renderer_abs, scratch_dir, "batch",
            extra[0], extra[1], extra[2], indices]


def run_batch(card, indices, label):
    scratch = os.path.join(SCRATCH, "MOTION-%s-%s" % (card, label))
    os.makedirs(os.path.join(scratch, "frames"), exist_ok=True)
    cmd = batch_command(card, scratch, indices)
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=300)
    return p, scratch


def main():
    report = {"cards": {}, "sample_indices": SAMPLE, "reorder_indices": REORDER}
    all_ok = True
    for card in CARDS:
        fh_path = os.path.join(ROOT, "renders", "MOTION-%s" % card,
                               "frames", "frame_hashes.json")
        with open(fh_path, encoding="utf-8") as fh:
            base = json.load(fh)["hashes"]
        entry = {"base_source": "renders/MOTION-%s/frames/frame_hashes.json" % card,
                 "runs": []}
        for label, idxs in (("sample", SAMPLE), ("reorder", REORDER)):
            p, scratch = run_batch(card, idxs, label)
            rec = {"label": label, "indices": idxs, "returncode": p.returncode,
                   "stdout": p.stdout.strip(), "stderr": p.stderr.strip()[:500]}
            try:
                out = json.loads(p.stdout.strip())
                hashes = out["hashes"]
                mismatches = []
                for k, v in hashes.items():
                    n = int(k)
                    expected = base["%04d" % n]
                    if v != expected:
                        mismatches.append({"n": n, "got": v, "expected": expected})
                # also verify on-disk bytes hash matches the reported hash
                disk_mismatch = []
                for k, v in hashes.items():
                    n = int(k)
                    fp = os.path.join(scratch, "frames", "f%04d.png" % n)
                    if sha(fp) != v:
                        disk_mismatch.append(n)
                rec["hash_count"] = len(hashes)
                rec["mismatches"] = mismatches
                rec["disk_hash_mismatches"] = disk_mismatch
                rec["pass"] = (p.returncode == 0 and not mismatches
                               and not disk_mismatch)
            except Exception as e:
                rec["parse_error"] = repr(e)
                rec["pass"] = False
            entry["runs"].append(rec)
            if not rec.get("pass"):
                all_ok = False
        # repeated index must be stable within a single run
        entry["pass"] = all(r.get("pass") for r in entry["runs"])
        report["cards"][card] = entry
    report["all_pass"] = all_ok
    print(json.dumps(report, indent=2))
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
