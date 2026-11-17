#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MOTION-15 / card 15 「综艺花字 (VARIETY TEXT)」 deterministic renderer.

CONTRACT (same pipeline as pilots MOTION-02/06/12):
  render_frame(n) is a PURE function of the frame index n and the frozen SEED.
  No wall-clock, no RNG stream, no inter-frame state, no Date.now, no process
  globals that mutate. Every animated parameter is a closed-form / integer
  function of n.  render order, process boundaries and pauses cannot change
  any frame byte.  This is what makes the determinism trio decidable.

Usage (from staging/MOTION-15/):
  python -X utf8 render.py full .        # 300 frames + 6 keyframes + hashes + manifest
  python -X utf8 render.py batch . 0 7 63 128 199 255 299   # arbitrary frame set (fresh process)
  python -X utf8 render.py hash . 0 7 63                    # print sha256 for given frames only

Card-15 rules implemented (see plan.md §3, beat_schedule.md):
  - round bold CJK font (msyhbd.ttc)
  - >=2 stroke layers: outer colored stroke + white inner stroke  (里白外彩)
  - hard offset shadow (solid INK, no blur/glow)                    (一道硬投影)
  - 8-frame overshoot+rebound pop (POP_CURVE, peak 1.18)           (放大过头再回弹约8帧)
  - per-char 2-frame stagger                                        (错开2帧)
  - idle wobble while held                                          (停着时轻轻晃)
  - emotion symbols matched to captions                            (情绪配符号)
  - 2-3 frame beat lag (BEAT_LAG=3)                                 (字比节拍晚2-3帧落下)
  - high saturation, <=3 accent hues (RED/YELLOW/INK)              (同屏不超过三种颜色)
  - no long sentences (<=4 chars), no thin font, no glow            (别做成)
"""
import hashlib
import json
import math
import os
import sys
from pathlib import Path

import numpy as np

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# FROZEN SPEC (pre-registered in plan.md before render)
SEED = 20261115
FPS = 30
FRAMES = 300
W, H = 1920, 1080
FREEZE_FROM = 270
FONT_PATH = "C:/Windows/Fonts/msyhbd.ttc"

# Fixed 5-tuple exact palette (strict, no AA from our drawing primitives)
PAPER = (255, 242, 204)   # background (structural neutral)
WHITE = (255, 255, 255)   # 里白 inner stroke (structural, mandatory)
RED = (255, 59, 48)       # accent 1
YELLOW = (255, 204, 0)    # accent 2
INK = (26, 26, 26)        # accent 3 = hard shadow + outlines
ACCENTS = {RED, YELLOW, INK}
PALETTE = {PAPER, WHITE, RED, YELLOW, INK}

# Palette array for deterministic exact-palette quantization (built once, after PALETTE).
_PAL = np.array(sorted(PALETTE), dtype=np.int32)  # int32: (255-26)^2 fits, no int16 overflow

def quantize_to_palette(img):
    """Snap every pixel to the nearest of the 5 exact palette colors.
    Deterministic (pure function of the input pixels): the card's high-saturation
    / limited-color look is enforced by construction, eliminating font AA shades.
    Ties are resolved by the fixed sorted order (minor index), so no ambiguity.
    """
    a = np.asarray(img, dtype=np.int32).reshape(-1, 3)
    dist = ((a[:, None, :] - _PAL[None, :, :]) ** 2).sum(axis=2)  # (N,5)
    idx = dist.argmin(axis=1)
    out = _PAL[idx].astype(np.uint8).reshape(img.height, img.width, 3)
    return Image.fromarray(out, "RGB")

# 8-frame pop: overshoot to 1.18 then rebound to 1.00
POP_CURVE = [0.00, 0.72, 1.10, 1.18, 1.14, 1.07, 1.02, 1.00]
PER_CHAR_STAGGER = 2
BEAT_LAG = 3
HARD_SHADOW = (9, 9)      # (dx, dy) solid offset

# 4 花字 segments: (text, grid_beat, emotion)
SEGMENTS = [
    ("完美早餐", 1, "proud"),      # LAND = 15*1 + 3 = 18
    ("焦了？！", 5, "surprise"),   # LAND = 15*5 + 3 = 78
    ("烫烫烫", 9, "awkward"),    # LAND = 15*9 + 3 = 138
    ("外焦里嫩", 13, "proud"),     # LAND = 15*13 + 3 = 198 (holds -> freeze)
]

def land_frame(grid_beat):
    return 15 * grid_beat + BEAT_LAG

def seg_window(idx):
    """visible window [land, next_land) except last -> FREEZE_FROM..end."""
    land = land_frame(SEGMENTS[idx][1])
    if idx + 1 < len(SEGMENTS):
        end = land_frame(SEGMENTS[idx + 1][1])
    else:
        end = FRAMES
    return land, end

# ---------------------------------------------------------------------------
# deterministic seeded helpers (pure functions of their args, no stream state)
# ---------------------------------------------------------------------------
def _h(*parts):
    s = "|".join(str(p) for p in parts)
    return int.from_bytes(hashlib.sha256((str(SEED) + "|" + s).encode()).digest()[:4], "big")

def _font(size):
    return ImageFont.truetype(FONT_PATH, size)

# ---------------------------------------------------------------------------
# drawing primitives (all emit exact palette colors, NO anti-aliasing)
# ---------------------------------------------------------------------------
def rounded_rect(d, box, r, fill, outline=None, width=0):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

def paste_stamp(canvas, stamp, xy):
    """alpha_composite an RGBA stamp onto the RGB canvas using binary alpha mask."""
    x, y = int(xy[0]), int(xy[1])
    region = canvas.crop((x, y, x + stamp.width, y + stamp.height)).convert("RGBA")
    out = Image.alpha_composite(region, stamp)
    canvas.paste(out.convert("RGB"), (x, y))

def build_text_stamp(text, size, face, outer_color, outer_w, inner_w, shadow=True):
    """
    Build a 花字 character stamp with:
      layer 0: hard offset shadow (solid INK silhouette at +HARD_SHADOW)  [hard shadow]
      layer 1: outer colored stroke (outer_w)                             [外彩]
      layer 2: white inner stroke (inner_w)                               [里白]
      layer 3: solid face fill                                            [字]
    Returns (RGBA stamp, stroke_layer_count=2).
    """
    font = _font(size)
    # measure
    probe = Image.new("L", (4, 4), 0)
    pd = ImageDraw.Draw(probe)
    bbox = pd.textbbox((0, 0), text, font=font, stroke_width=outer_w)
    pad = outer_w + 18
    w = (bbox[2] - bbox[0]) + 2 * pad + HARD_SHADOW[0]
    h = (bbox[3] - bbox[1]) + 2 * pad + HARD_SHADOW[1]
    ox = pad - bbox[0]
    oy = pad - bbox[1]

    def draw_layers(target, dx=0, dy=0):
        d = ImageDraw.Draw(target)
        pos = (ox + dx, oy + dy)
        # hard shadow (drawn first, behind everything) only on the main pass
        return d, pos

    stamp = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(stamp)

    # hard shadow silhouette: solid INK, offset, NO blur / NO alpha gradient
    if shadow:
        d.text((ox + HARD_SHADOW[0], oy + HARD_SHADOW[1]), text, font=font,
               fill=(INK[0], INK[1], INK[2], 255), stroke_width=outer_w,
               stroke_fill=(INK[0], INK[1], INK[2], 255))

    # outer colored stroke
    d.text((ox, oy), text, font=font, fill=(face[0], face[1], face[2], 255),
           stroke_width=outer_w, stroke_fill=(outer_color[0], outer_color[1], outer_color[2], 255))
    # white inner stroke (inner_w < outer_w) + face fill in one pass
    d.text((ox, oy), text, font=font, fill=(face[0], face[1], face[2], 255),
           stroke_width=inner_w, stroke_fill=(WHITE[0], WHITE[1], WHITE[2], 255))

    return stamp, 2  # stroke_layer_count

def star(d, cx, cy, r, color):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=color)

def spiky_burst(d, cx, cy, r_out, r_in, spikes, color):
    pts = []
    for i in range(spikes * 2):
        ang = -math.pi / 2 + i * math.pi / spikes
        rr = r_out if i % 2 == 0 else r_in
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=color)

def radial_lines(d, cx, cy, r0, r1, count, color, width):
    for i in range(count):
        ang = -math.pi / 2 + i * 2 * math.pi / count
        x0 = cx + r0 * math.cos(ang); y0 = cy + r0 * math.sin(ang)
        x1 = cx + r1 * math.cos(ang); y1 = cy + r1 * math.sin(ang)
        d.line([(x0, y0), (x1, y1)], fill=color, width=width)

def sweat_drop(d, cx, cy, w, h, color):
    # teardrop: polygon (rounded bottom, pointed top), exact color
    pts = [(cx, cy - h / 2), (cx + w / 2, cy + h / 3),
           (cx, cy + h / 2), (cx - w / 2, cy + h / 3)]
    d.polygon(pts, fill=color)
    d.ellipse([cx - w / 2, cy, cx + w / 2, cy + h / 2], fill=color)

# ---------------------------------------------------------------------------
# background tableau (toaster + toasts + hands): pure function of n
# ---------------------------------------------------------------------------
def draw_tableau(d, n):
    m = n if n < FREEZE_FROM else FREEZE_FROM
    # ground line
    d.rectangle([0, 880, W, 886], fill=INK)
    # toaster body
    rounded_rect(d, [660, 560, 1260, 880], 36, fill=YELLOW, outline=INK, width=10)
    # toaster slot
    rounded_rect(d, [740, 560, 1180, 612], 22, fill=INK)
    # lever
    d.rectangle([1260, 640, 1300, 720], fill=RED, outline=INK, width=6)
    # two toasts rising: pop height is a closed-form of m (pure)
    if m >= 15:
        rise = max(0, min(1.0, (m - 15) / 12.0))
        ease = rise * rise * (3 - 2 * rise)
        for k, (bx) in enumerate([820, 1020]):
            top = 600 - int(260 * ease) + (k * 14)
            # charred toast: dark bread with crust + char marks (INK + RED accent)
            rounded_rect(d, [bx, top, bx + 170, top + 220], 26, fill=INK, outline=INK, width=8)
            rounded_rect(d, [bx + 14, top + 14, bx + 156, top + 206], 20, fill=WHITE)
            # char marks appear after beat 3 (m>=45): 焦
            if m >= 45:
                d.rectangle([bx + 40, top + 60, bx + 130, top + 150], fill=INK)
                d.ellipse([bx + 50, top + 70, bx + 80, top + 100], fill=RED)
                d.ellipse([bx + 100, top + 120, bx + 130, top + 150], fill=RED)
    # hand (poke) from right after beat 4 (m>=60), retracts after m>=105
    if 60 <= m < 150:
        px = 1500 - int(360 * max(0, min(1.0, (m - 60) / 15.0)))
        if m >= 105:
            px = 1140 + int(200 * max(0, min(1.0, (m - 105) / 20.0)))
        rounded_rect(d, [px, 470, px + 150, 560], 40, fill=RED, outline=INK, width=8)
        # one pointing finger
        d.rounded_rectangle([px - 70, 495, px + 10, 530], radius=18, fill=RED, outline=INK, width=6)
    # juggling two hands during beats 9-12 (135<=m<195): sine toss (closed-form)
    if 135 <= m < 195:
        u = (m - 135) / 60.0
        for k, basex in enumerate([430, 1300]):
            jx = basex + int(70 * math.sin(2 * math.pi * u + k * math.pi))
            jy = 470 - int(90 * abs(math.sin(math.pi * u * 2 + k * math.pi)))
            rounded_rect(d, [jx, jy, jx + 150, jy + 90], 40, fill=RED, outline=INK, width=8)

# ---------------------------------------------------------------------------
# emotion symbols (matched per 花字): pure function of n + segment
# ---------------------------------------------------------------------------
def draw_emotion(d, n, emotion, cx, cy):
    m = n if n < FREEZE_FROM else FREEZE_FROM
    if emotion == "proud":
        # 4 stars at seeded positions
        for i in range(4):
            sx = cx + (-1 if i % 2 == 0 else 1) * (360 + _h("star", i) % 120)
            sy = cy + (-1 if i < 2 else 1) * (150 + _h("starY", i) % 90)
            star(d, sx, sy, 46 + (_h("starR", i) % 22), YELLOW)
            star(d, sx, sy, 22, RED)
    elif emotion == "surprise":
        # 爆炸框 + 放射线
        radial_lines(d, cx, cy, 210, 330, 12, RED, 14)
        spiky_burst(d, cx, cy, 230, 150, 12, YELLOW)
        spiky_burst(d, cx, cy, 150, 96, 12, RED)
        d.ellipse([cx - 70, cy - 70, cx + 70, cy + 70], fill=WHITE, outline=INK, width=10)
    elif emotion == "awkward":
        # 汗珠 + 括号小字
        for i in range(3):
            sx = cx + (-1 if i % 2 == 0 else 1) * (300 + i * 70)
            sy = cy - 120 + i * 60
            sweat_drop(d, sx, sy, 34, 60, WHITE)
        # bracketed small text 「(好烫)」
        f = _font(46)
        d.text((cx - 150, cy + 170), "(好烫)", font=f, fill=INK, stroke_width=3, stroke_fill=WHITE)

# ---------------------------------------------------------------------------
# 花字 composition: one segment active in its window, pure function of n
# ---------------------------------------------------------------------------
def draw_huazi(canvas, n):
    m = n if n < FREEZE_FROM else FREEZE_FROM
    d = ImageDraw.Draw(canvas)
    for idx, (text, gb, emo) in enumerate(SEGMENTS):
        land, end = seg_window(idx)
        if not (land <= m < end):
            continue
        # emotion symbol first (behind text)
        draw_emotion(d, m, emo, W // 2, 300)
        # per-char pop with 2-frame stagger
        FACE_SIZE = 200
        outer_color = RED if emo == "proud" else YELLOW
        face_color = YELLOW if emo == "proud" else RED
        # precompute per-char widths for centering
        stamps = []
        for ci, ch in enumerate(text):
            st, _ = build_text_stamp(ch, FACE_SIZE, face_color, outer_color,
                                     outer_w=14, inner_w=7, shadow=True)
            stamps.append(st)
        total_w = sum(s.width for s in stamps) + 12 * (len(stamps) - 1)
        x0 = (W - total_w) // 2
        y0 = 250
        for ci, (ch, st) in enumerate(zip(text, stamps)):
            start = land + ci * PER_CHAR_STAGGER
            age = m - start
            if age < 0:
                continue  # not yet landed (stagger)
            if age < len(POP_CURVE):
                scale = POP_CURVE[age]
            else:
                scale = 1.0  # held
            if scale <= 0.0:
                continue
            # idle wobble ONLY while held (after pop completes): ±1.2° + ±2px
            wobble_deg = 0.0
            wobble_dy = 0
            if age >= len(POP_CURVE):
                wobble_deg = 1.2 * math.sin(2 * math.pi * (m - start) / 14.0)
                wobble_dy = int(2 * math.sin(2 * math.pi * (m - start) / 11.0))
            # scale stamp (NEAREST preserves exact palette)
            nw = max(1, int(st.width * scale))
            nh = max(1, int(st.height * scale))
            scaled = st.resize((nw, nh), Image.NEAREST)
            if wobble_deg != 0.0:
                scaled = scaled.rotate(wobble_deg, resample=Image.NEAREST,
                                       expand=True, fillcolor=(0, 0, 0, 0))
            # center each char in its slot
            slot_x = x0 + sum(s.width for s in stamps[:ci]) + 12 * ci
            px = slot_x + (st.width - scaled.width) // 2
            py = y0 + (st.height - scaled.height) // 2 + wobble_dy
            paste_stamp(canvas, scaled, (px, py))
        # cartoon pop-impact burst on the exact LAND frame (visual sfx marker, no audio)
        if m == land:
            radial_lines(d, W // 2, 300, 60, 150, 10, WHITE, 10)

# ---------------------------------------------------------------------------
# endcard (final segment held): a framing border + corner stars
# ---------------------------------------------------------------------------
def draw_endcard(canvas, n):
    m = n if n < FREEZE_FROM else FREEZE_FROM
    if land_frame(SEGMENTS[-1][1]) <= m:
        d = ImageDraw.Draw(canvas)
        d.rectangle([60, 60, W - 60, H - 60], outline=INK, width=14)
        for (cx, cy) in [(120, 120), (W - 120, 120), (120, H - 120), (W - 120, H - 120)]:
            star(d, cx, cy, 40, RED)
            star(d, cx, cy, 18, YELLOW)

# ---------------------------------------------------------------------------
# PUBLIC: pure render_frame(n)
# ---------------------------------------------------------------------------
def render_frame(n):
    """PURE function of n (+ frozen SEED). Returns a 1920x1080 RGB PIL Image."""
    n = int(n)
    m = n if n < FREEZE_FROM else FREEZE_FROM   # freeze clamp
    canvas = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(canvas)
    # subtle flat panel stripes (structural, exact palette, deterministic of m)
    for i in range(0, W, 240):
        if (i // 240 + (m // 30)) % 2 == 0:
            d.rectangle([i, 0, i + 6, 60], fill=YELLOW)
    draw_tableau(d, m)
    draw_huazi(canvas, m)
    draw_endcard(canvas, m)
    # K0 title hint (frames 0..14, before first 花字)
    if m < 15:
        f = _font(70)
        d = ImageDraw.Draw(canvas)
        d.text((W // 2 - 210, 120), "综艺花字", font=f, fill=INK,
               stroke_width=6, stroke_fill=WHITE)
    return quantize_to_palette(canvas)

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def frame_path(root, n):
    return Path(root) / "frames" / ("f%04d.png" % n)

def save_frame(root, n):
    p = frame_path(root, n)
    render_frame(n).save(p, "PNG")
    return p

def cmd_full(root):
    root = Path(root)
    (root / "frames").mkdir(parents=True, exist_ok=True)
    (root / "keyframes").mkdir(parents=True, exist_ok=True)
    (root / "checks").mkdir(parents=True, exist_ok=True)
    hashes = {}
    for n in range(FRAMES):
        p = save_frame(root, n)
        hashes["f%04d" % n] = sha256_file(p)
    fh = {"schema": "1.0", "task_id": "MOTION-15", "seed": SEED, "fps": FPS,
          "frames": FRAMES, "resolution": [W, H], "freeze_from": FREEZE_FROM,
          "hashes": hashes}
    (root / "checks" / "frame_hashes.json").write_text(
        json.dumps(fh, ensure_ascii=False, indent=1), encoding="utf-8")
    # 6 keyframes (pre-registered in plan.md §4)
    kf_frames = [0, 30, 90, 150, 210, 270]
    kf_slugs = ["TITLE_ONLY", "BREAKFAST_POP", "BURNT_SURPRISE",
                "HOT_AWKWARD", "PROUD_STARS", "ENDCARD_FREEZE"]
    kf_manifest = []
    for i, (n, slug) in enumerate(zip(kf_frames, kf_slugs)):
        kp = root / "keyframes" / ("k%d.png" % i)
        render_frame(n).save(kp, "PNG")
        kf_manifest.append({"index": i, "frame": n, "t_s": round(n / FPS, 3),
                            "slug": slug, "sha256": sha256_file(kp)})
    (root / "keyframe_manifest.json").write_text(
        json.dumps({"task_id": "MOTION-15", "keyframes": kf_manifest},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    print("FULL OK: %d frames + 6 keyframes; frame_hashes.json + keyframe_manifest.json written" % FRAMES)

def cmd_batch(root, frames):
    root = Path(root)
    (root / "frames").mkdir(parents=True, exist_ok=True)
    out = {}
    for n in frames:
        p = save_frame(root, n)
        out["f%04d" % n] = sha256_file(p)
    print(json.dumps(out, ensure_ascii=False))

def cmd_hash(root, frames):
    out = {}
    for n in frames:
        out["f%04d" % n] = sha256_file(frame_path(root, n))
    print(json.dumps(out, ensure_ascii=False))

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    mode, root = sys.argv[1], sys.argv[2]
    if mode == "full":
        cmd_full(root)
    elif mode == "batch":
        cmd_batch(root, [int(x) for x in sys.argv[3:]])
    elif mode == "hash":
        cmd_hash(root, [int(x) for x in sys.argv[3:]])
    else:
        print("unknown mode: " + mode); sys.exit(2)

if __name__ == "__main__":
    main()
