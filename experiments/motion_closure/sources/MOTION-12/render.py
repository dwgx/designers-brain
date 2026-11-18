#!/usr/bin/env python3
"""
MOTION-12 / card 12 "手绘线条沸腾" (cel-boil) deterministic renderer.  R2 (S06-B repair).

Pure function of frame number: pixels = f(frame). No wall-clock, no Math.random,
no stateful integration. All randomness is seeded via a per-element PRNG keyed
by (SEED, element_id, pose_id, boil_version, boil_group), so any frame can be
rendered in any order, after a pause/resume, or in a fresh process and yield
identical bytes.

R2 repairs (supervision S06-MOTION-AND-CONTENT-DELTA.md §B):
  (1) EXPLICIT 12 Hz POSE CLOCK. R1's held_frame=(frame//2)*2 produced 15
      pose anchors/sec in a 30 fps container (not the claimed 12). Here
      POSE_HZ=12 and t = pose_id/12; an explicit 2/3 alternating hold pattern
      (6*2 + 6*3 = 30 frames) maps 12 pose anchors into each 30 output frames,
      giving exactly 12 anchors/30 frames and 120 anchors/300 frames. The pose
      schedule is published verbatim by `python render.py schedule`.
  (2) BOIL CLOCK IS INDEPENDENT. boil_variant() keeps its own [2,2,3,2,3]
      12-frame cadence, unmodified from R1; it is NOT tied to the pose clock.
  (3) SMEAR relocated into real flight. R1's SMEAR_FRAME=152 sat after u had
      already reached 1 (~f138 under the old clock), i.e. on a stationary
      clamped endpoint. R2's SMEAR_FRAME=105 is mid-flight (pose 42, t=3.5,
      u=0.3125, d(hx)/du=900, d(hy)/du=-240*pi*cos(pi*u)!=0); the ghost trail
      is elongated ALONG the instantaneous velocity vector. Only frame 105 has
      the smear; see `schedule.py` for trajectory/neighbour verification.

Card-12 画风段 (origin/提示词全文.md L188), implemented literally:
  - 每张画备 3-4 版略有不同的线稿: 4 boil variants (BOIL_VARIANTS = 4)
  - 每 2-3 帧轮换: independent boil clock, HOLD_PATTERN=[2,2,3,2,3] (12-frame cycle)
  - 静止时线也在抖: even held drawings get a tiny per-variant jitter offset
  - 动作一拍二, 每秒 12 张: explicit 12 Hz pose clock -> 12 drawings/sec,
    each held 2 or 3 frames inside the 30 fps container (see reconciliation in plan.md)
  - 线条两头细、中间粗: stroke width tapers at the ends (polyline with variable width)
  - 快动作插 1 帧拉长的残影: SMEAR_FRAME inserts a single velocity-aligned ghost
  - 烟、火花、速度线都手画: hand-drawn arcs / spark rays / speed strokes
  - 全画面铺一层淡纸纹: static seeded paper-grain layer
内容段 (L190): alarm clock startles itself -> curls up -> vibrates wildly ->
  hammer flies off -> sun rises -> 「早安」 text shivers throughout.
"""
import hashlib
import json
import math
import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ----------------------------------------------------------------------------
# Seed / spec fields (all fixed, recorded verbatim in plan.md)
# ----------------------------------------------------------------------------
SEED = 20261115
FPS = 30
FRAMES = 300
DURATION_S = 10.0
WIDTH, HEIGHT = 1920, 1080
KEY_FRAMES = [0, 45, 90, 150, 225, 285]
BOIL_VARIANTS = 4

# ---- (R2) EXPLICIT 12 Hz POSE CLOCK mapped into the 30 fps container -------
# 12 pose anchors per second; 30/12 = 2.5 output frames per anchor, realised
# by alternating 2- and 3-frame holds. 6*2 + 6*3 = 30 -> exactly 12 anchors
# in every 30 output frames (120 anchors across 300 frames / 10 s).
POSE_HZ = 12
POSE_HOLD_PATTERN = [2, 3] * 6          # 12 entries, sum = 30
assert len(POSE_HOLD_PATTERN) == 12 and sum(POSE_HOLD_PATTERN) == FPS

# ---- INDEPENDENT BOIL CLOCK (unchanged from R1) ---------------------------
# variant rotates every 2-3 frames on its own 12-frame cycle; it is not tied
# to the pose clock. Mean hold 2.4 frames -> "每 2-3 帧轮换".
HOLD_PATTERN = [2, 2, 3, 2, 3]

# ---- (R2) SMEAR: one frame inside genuine hammer flight -------------------
HAMMER_T0 = 3.0            # pose-clock seconds at which the hammer launches
HAMMER_FLIGHT_S = 1.6      # u = (t - HAMMER_T0) / HAMMER_FLIGHT_S, u in [0,1]
SMEAR_FRAME = 105          # pose 42, t = 3.5, u = 0.3125 (mid-flight, nonzero velocity)
SMEAR_GHOSTS = 4
SMEAR_STEP = 46.0          # px between elongated ghosts along -velocity

INK = (38, 30, 26, 255)
PAPER = (243, 234, 214, 255)
RED = (198, 72, 52, 255)
GOLD = (214, 158, 60, 255)
SUN = (232, 176, 62, 255)
FONT_CJK_CANDIDATES = [
    "C:/Windows/Fonts/msyh.ttc",    # Microsoft YaHei
    "C:/Windows/Fonts/simhei.ttf",
    "C:/Windows/Fonts/simsun.ttc",
]

HERE = Path(__file__).resolve().parent
FRAME_DIR = HERE / "frames"
STILL_DIR = HERE / "stills"
CHECK_DIR = HERE / "checks"


# ----------------------------------------------------------------------------
# Deterministic PRNG: hash(seed, element, pose_id, variant, group) -> stream.
# Nothing is carried between frames.
# ----------------------------------------------------------------------------
def seeded(seed, *parts):
    h = hashlib.sha256((str(seed) + "|" + "|".join(map(str, parts))).encode()).digest()
    return int.from_bytes(h[:8], "big")


def rng_for(*parts):
    return np.random.default_rng(seeded(SEED, *parts))


# ----------------------------------------------------------------------------
# (R2) EXPLICIT POSE SCHEDULE: frame -> (pose_id, pose_t, hold_len, anchor_frame)
# Built once, deterministically, from the 12 Hz clock. This is the authoritative
# pose clock; nothing else derives pose time.
# ----------------------------------------------------------------------------
def _build_pose_schedule():
    sched = []
    pid = 0
    f = 0
    while f < FRAMES:
        hold = POSE_HOLD_PATTERN[pid % len(POSE_HOLD_PATTERN)]
        start = f
        for _k in range(hold):
            if f >= FRAMES:
                break
            sched.append((f, pid, pid / POSE_HZ, hold, start))
            f += 1
        pid += 1
    return sched


POSE_SCHEDULE = _build_pose_schedule()


def pose_of_frame(frame):
    """(pose_id, pose_t, hold_len, anchor_frame) for an output frame.

    pose_t = pose_id / POSE_HZ is the ONLY picture time source: an explicit
    12 Hz clock. Consecutive output frames sharing a pose_id are the 2/3-frame
    holds ("一拍二" mapped into a 30 fps container)."""
    return (POSE_SCHEDULE[frame][1], POSE_SCHEDULE[frame][2],
            POSE_SCHEDULE[frame][3], POSE_SCHEDULE[frame][4])


def boil_variant(frame):
    """INDEPENDENT boil rotation cadence: pure function of frame; 2-3 frame
    holds over a 12-frame cycle, 4 variants. NOT tied to the pose clock."""
    cycle = sum(HOLD_PATTERN)  # 12
    pos = frame % cycle
    g = 0
    acc = 0
    for i, h in enumerate(HOLD_PATTERN):
        if pos < acc + h:
            g = i
            break
        acc += h
    turns = frame // cycle
    return (turns * len(HOLD_PATTERN) + g) % BOIL_VARIANTS, g, pos - acc


def smear_active(frame):
    """Exactly one output frame carries the smear."""
    return frame == SMEAR_FRAME


def hammer_trajectory(t):
    """Hammer flight state at pose-clock time t (exposed for verification).

    Returns (u, hx, hy, vx, vy). vx,vy are velocity w.r.t. u; du/dt is a
    positive constant so the direction is the true flight direction."""
    u = min(1.0, max(0.0, (t - HAMMER_T0) / HAMMER_FLIGHT_S))
    hx = 960 + 60 + 900 * u
    hy = 470 - 240 * math.sin(math.pi * u)
    vx = 900.0
    vy = -240.0 * math.pi * math.cos(math.pi * u)
    return u, hx, hy, vx, vy


# ----------------------------------------------------------------------------
# Paper grain: static seeded layer, identical for every frame & every process.
# ----------------------------------------------------------------------------
_GRAIN_CACHE = {}


def paper_grain():
    if "g" not in _GRAIN_CACHE:
        r = rng_for("paper-grain")
        g = r.normal(0, 5.5, (HEIGHT, WIDTH)).astype(np.int16)
        # faint fibrous streaks
        yy = np.arange(HEIGHT, dtype=np.float32)[:, None]
        fibre = (np.sin(yy * 0.09 + r.uniform(0, 6.28)) * 2.0).astype(np.int16)
        _GRAIN_CACHE["g"] = np.clip(g + fibre, -14, 14)
    return _GRAIN_CACHE["g"]


def load_font(size):
    for p in FONT_CJK_CANDIDATES:
        if os.path.isfile(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


_FONT_CACHE = {}


def font(size):
    if size not in _FONT_CACHE:
        _FONT_CACHE[size] = load_font(size)
    return _FONT_CACHE[size]


# ----------------------------------------------------------------------------
# Pen-like stroke: thin at both ends, thick in the middle ("两头细、中间粗").
# Drawn as a variable-width polyline using tapered circular caps.
# ----------------------------------------------------------------------------
def jitter_point(r, x, y, amp):
    return x + r.uniform(-amp, amp), y + r.uniform(-amp, amp)


def pen_stroke(draw, pts, r, base_w=6.0, amp=2.2):
    """Variable-width polyline; width tapers to ~1px at the two ends."""
    n = len(pts)
    if n < 2:
        return
    for i in range(n - 1):
        frac = (i + 0.5) / (n - 1)
        taper = math.sin(math.pi * frac) ** 0.6  # 0 at ends, 1 in middle
        w = max(1.0, base_w * (0.22 + 0.78 * taper))
        x0, y0 = jitter_point(r, pts[i][0], pts[i][1], amp)
        x1, y1 = jitter_point(r, pts[i + 1][0], pts[i + 1][1], amp)
        draw.line([(x0, y0), (x1, y1)], fill=INK, width=int(round(w)))
        rr = w / 2.0
        draw.ellipse([x1 - rr, y1 - rr, x1 + rr, y1 + rr], fill=INK)


def arc_points(cx, cy, rx, ry, a0, a1, steps=18, wobble=0.0, r=None):
    pts = []
    for i in range(steps + 1):
        a = a0 + (a1 - a0) * i / steps
        wob = 0.0
        if wobble and r is not None:
            wob = r.uniform(-wobble, wobble)
        pts.append((cx + (rx + wob) * math.cos(a), cy + (ry + wob) * math.sin(a)))
    return pts


# ----------------------------------------------------------------------------
# Scene phases (内容段). Time is derived ONLY from the 12 Hz pose clock
# (t = pose_id / POSE_HZ); it is never frame/FPS.
# ----------------------------------------------------------------------------
def phase_of(t):
    # 0-1.2 curl/anticipation, 1.2-3.0 vibrate, 3.0-5.0 hammer flies,
    # 5.0-7.5 sun rises, 7.5-10.0 「早安」 shiver + settle
    if t < 1.2:
        return "curl"
    if t < 3.0:
        return "vibrate"
    if t < 5.0:
        return "hammer"
    if t < 7.5:
        return "sun"
    return "title"


def clock_geometry(t, variant, r):
    """Return (cx, cy, rx, ry, squash, tilt, shake_x, shake_y) for the alarm clock."""
    cx, cy = 960.0, 560.0
    ph = phase_of(t)
    if ph == "curl":
        # 憋气缩成一团: shrink into a ball
        k = min(1.0, t / 1.2)
        squash = 1.0 - 0.42 * math.sin(math.pi * k) ** 0.8
        rx = 250.0 * squash
        ry = 250.0 * (1.0 + 0.10 * math.sin(math.pi * k))
        shake_x = shake_y = 0.0
    elif ph == "vibrate":
        # 疯狂震动: violent jitter, deterministic per pose-frame
        rx = ry = 250.0
        amp = 16.0 + 10.0 * math.sin(math.pi * (t - 1.2) / 1.8)
        shake_x = r.uniform(-amp, amp)
        shake_y = r.uniform(-amp, amp)
    elif ph == "hammer":
        rx = ry = 250.0
        shake_x = r.uniform(-4, 4)
        shake_y = r.uniform(-4, 4)
    else:  # sun / title
        rx = ry = 250.0
        shake_x = 3.0 * math.sin(t * 9.0)   # closed-form, not integrated
        shake_y = 2.0 * math.cos(t * 7.0)
    # boil micro-jitter on the contour even when "static"
    bj = r.uniform(-2.2, 2.2)
    tilt = r.uniform(-0.03, 0.03)
    cx += shake_x
    cy += shake_y + bj
    return cx, cy, rx, ry, tilt


def draw_clock(draw, t, variant, r, with_smear=False):
    cx, cy, rx, ry, tilt = clock_geometry(t, variant, r)
    ph = phase_of(t)

    # two bells on top (hand-drawn arcs)
    for side in (-1, 1):
        bx = cx + side * rx * 0.62
        by = cy - ry * 0.92
        bell = arc_points(bx, by, 62, 46, math.pi, 2 * math.pi, steps=14,
                          wobble=2.4, r=r)
        pen_stroke(draw, bell, r, base_w=6.5, amp=1.8)
        # bell clapper dot
        pen_stroke(draw, [(bx, by + 44), (bx, by + 54)], r, base_w=4)

    # main round body: 4 arcs (slightly different per boil variant)
    wob = 3.0 + variant * 0.7  # each boil version differs a little
    body = []
    for q in range(4):
        body += arc_points(cx, cy, rx, ry,
                           -math.pi / 2 + q * math.pi / 2,
                           -math.pi / 2 + (q + 1) * math.pi / 2,
                           steps=16, wobble=wob, r=r)[:-1]
    body.append(body[0])
    pen_stroke(draw, body, r, base_w=8.0, amp=2.0)

    # inner face ring
    face = arc_points(cx, cy, rx * 0.82, ry * 0.82, 0, 2 * math.pi,
                      steps=40, wobble=1.4, r=r)
    pen_stroke(draw, face, r, base_w=3.5, amp=1.0)

    # clock hands (angle from t, closed form)
    hand_a = -math.pi / 2 + t * 0.9
    pen_stroke(draw, [(cx, cy),
                      (cx + rx * 0.55 * math.cos(hand_a),
                       cy + ry * 0.55 * math.sin(hand_a))], r, base_w=6.0)
    hand_b = -math.pi / 2 + t * 0.15
    pen_stroke(draw, [(cx, cy),
                      (cx + rx * 0.36 * math.cos(hand_b),
                       cy + ry * 0.36 * math.sin(hand_b))], r, base_w=4.0)
    draw.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=INK)

    # ticks
    for i in range(12):
        a = -math.pi / 2 + i * math.pi / 6
        p0 = (cx + rx * 0.72 * math.cos(a), cy + ry * 0.72 * math.sin(a))
        p1 = (cx + rx * 0.79 * math.cos(a), cy + ry * 0.79 * math.sin(a))
        pen_stroke(draw, [p0, p1], r, base_w=3.0, amp=0.8)

    # legs
    for side in (-1, 1):
        lx = cx + side * rx * 0.5
        pen_stroke(draw, [(lx, cy + ry * 0.9), (lx + side * 30, cy + ry * 0.9 + 46)],
                   r, base_w=6.0)

    if ph == "vibrate":
        # hand-drawn speed lines (抖动)
        for i in range(9):
            a = r.uniform(0, 2 * math.pi)
            d0 = rx + 30
            d1 = d0 + r.uniform(40, 110)
            p0 = (cx + d0 * math.cos(a), cy + d0 * math.sin(a))
            p1 = (cx + d1 * math.cos(a), cy + d1 * math.sin(a))
            pen_stroke(draw, [p0, p1], r, base_w=3.0, amp=1.2)


def draw_hammer(draw, t, variant, r, smear=False):
    """铃锤飞了出去: hammer flies out; one velocity-aligned smear on SMEAR_FRAME.

    (R2) The smear ghosts trail BEHIND the hammer along the instantaneous
    velocity vector (computed from hammer_trajectory), so the elongated trail
    extends along the actual movement instead of sitting at a clamped endpoint.
    """
    ph = phase_of(t)
    if ph not in ("hammer", "sun", "title"):
        return
    u, hx, hy, vx, vy = hammer_trajectory(t)
    ang = u * 5.0
    if smear:
        vlen = math.hypot(vx, vy)
        ux, uy = vx / vlen, vy / vlen          # unit flight direction
        for k in range(1, SMEAR_GHOSTS + 1):
            gx = hx - ux * SMEAR_STEP * k       # trail behind, along -velocity
            gy = hy - uy * SMEAR_STEP * k
            # each ghost stroke is elongated ALONG the movement direction
            pen_stroke(draw, [(gx - ux * 40, gy - uy * 40),
                              (gx + ux * 40, gy + uy * 40)], r,
                       base_w=3.0, amp=1.0)
    # hammer handle + head (hand drawn)
    c, s = math.cos(ang), math.sin(ang)
    p0 = (hx - 46 * c - 90 * s, hy - 46 * s + 90 * c)
    p1 = (hx + 46 * c + 90 * s, hy + 46 * s - 90 * c)
    pen_stroke(draw, [p0, p1], r, base_w=9.0, amp=1.6)
    # head bar
    hp0 = (p1[0] - 55 * c, p1[1] - 55 * s)
    hp1 = (p1[0] + 55 * c, p1[1] + 55 * s)
    pen_stroke(draw, [hp0, hp1], r, base_w=14.0, amp=1.4)
    # sparks (hand-drawn little crosses)
    for i in range(6):
        sx = hx + r.uniform(-70, 70)
        sy = hy + r.uniform(-70, 70)
        pen_stroke(draw, [(sx - 10, sy), (sx + 10, sy)], r, base_w=2.5)
        pen_stroke(draw, [(sx, sy - 10), (sx, sy + 10)], r, base_w=2.5)


def draw_smoke(draw, t, variant, r):
    """烟: hand-drawn rising smoke curls (closed-form, seeded)."""
    if phase_of(t) in ("curl",):
        return
    for i in range(3):
        base_x = 960 + (i - 1) * 210
        base_y = 300 - 60 * ((t * 0.5 + i * 0.33) % 1.0)
        pts = []
        for j in range(12):
            p = j / 11.0
            pts.append((base_x + 34 * math.sin(p * 6.0 + i + t * 1.2),
                        base_y - p * 150))
        pen_stroke(draw, pts, r, base_w=3.2, amp=2.0)


def draw_sun(draw, t, variant, r):
    """太阳升起: sun rises with hand-drawn rays."""
    ph = phase_of(t)
    if ph not in ("sun", "title"):
        return
    u = min(1.0, max(0.0, (t - 5.0) / 2.2))
    sy = 900 - 430 * u
    sx = 1520.0
    rr = 120.0
    body = arc_points(sx, sy, rr, rr, 0, 2 * math.pi, steps=40,
                      wobble=2.0 + variant * 0.5, r=r)
    pen_stroke(draw, body, r, base_w=7.0, amp=1.4)
    for i in range(12):
        a = i * math.pi / 6 + variant * 0.05
        p0 = (sx + (rr + 18) * math.cos(a), sy + (rr + 18) * math.sin(a))
        p1 = (sx + (rr + 55) * math.cos(a), sy + (rr + 55) * math.sin(a))
        pen_stroke(draw, [p0, p1], r, base_w=4.0, amp=1.2)


def draw_title(draw, t, variant, r):
    """「早安」两个字一直在抖: shivering hand-lettered title."""
    if phase_of(t) not in ("sun", "title"):
        return
    f = font(150)
    # deterministic shiver (closed-form + seeded per-variant offset)
    jx = 4.0 * math.sin(t * 13.0) + r.uniform(-3, 3)
    jy = 3.0 * math.cos(t * 11.0) + r.uniform(-3, 3)
    # draw twice with tiny offset = hand-drawn doubling / boil
    for (ox, oy, col) in [(jx, jy, INK), (jx + 2.5, jy - 2.0, RED)]:
        draw.text((960 + ox, 840 + oy), "早安", font=f, fill=col,
                  anchor="mm", stroke_width=0)


# ----------------------------------------------------------------------------
# Frame render: pure function of `frame`.
#   pose clock : pose_id / POSE_HZ   (explicit 12 Hz, 2/3-frame holds)
#   boil clock : boil_variant(frame) (independent 12-frame cycle)
#   smear      : frame == SMEAR_FRAME only
# ----------------------------------------------------------------------------
def render_frame(frame):
    variant, group, _ = boil_variant(frame)          # INDEPENDENT boil clock
    pid, t, hold, anchor = pose_of_frame(frame)      # explicit 12 Hz pose clock
    # local RNG keyed by (element, pose_id, boil variant, boil group)
    # -> order-independent and pure in `frame`.
    r = rng_for("frame", pid, variant, group)

    img = Image.new("RGBA", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(img)

    draw_smoke(draw, t, variant, r)
    draw_sun(draw, t, variant, r)
    draw_clock(draw, t, variant, r)
    draw_hammer(draw, t, variant, r, smear=smear_active(frame))
    draw_title(draw, t, variant, r)

    # 全画面铺一层淡纸纹: static seeded grain added in integer space
    arr = np.asarray(img).astype(np.int16).copy()
    grain = paper_grain()
    arr[:, :, 0] = np.clip(arr[:, :, 0] + grain, 0, 255)
    arr[:, :, 1] = np.clip(arr[:, :, 1] + grain, 0, 255)
    arr[:, :, 2] = np.clip(arr[:, :, 2] + grain, 0, 255)
    out = Image.fromarray(arr.astype(np.uint8), "RGBA").convert("RGB")
    return out


def frame_path(frame):
    return FRAME_DIR / f"f{frame:04d}.png"


def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def emit_schedule():
    """Publish the ACTUAL pose-id schedule (300 rows) as JSON + markdown."""
    CHECK_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for (f, pid, t, hold, anchor) in POSE_SCHEDULE:
        v, g, _ = boil_variant(f)
        rows.append({
            "frame": f, "pose_id": pid, "pose_t": round(t, 6),
            "hold_len": hold, "anchor_frame": anchor,
            "is_pose_anchor": f == anchor,
            "boil_variant": v, "boil_group": g,
            "smear": smear_active(f),
        })
    out = {
        "pose_hz": POSE_HZ, "fps": FPS, "frames": FRAMES,
        "pose_hold_pattern": POSE_HOLD_PATTERN,
        "pattern_sum_per_second": sum(POSE_HOLD_PATTERN),
        "anchors_per_30_frames": len({r["pose_id"] for r in rows if r["frame"] < 30}),
        "total_pose_ids": len({r["pose_id"] for r in rows}),
        "boil_clock_independent": True,
        "boil_hold_pattern": HOLD_PATTERN,
        "smear_frame": SMEAR_FRAME,
        "rows": rows,
    }
    (CHECK_DIR / "pose_id_schedule.json").write_text(
        json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    lines = [
        "# MOTION-12 R2 — explicit pose-id schedule (12 Hz clock in 30 fps container)",
        "",
        f"- `POSE_HZ = {POSE_HZ}`, `POSE_HOLD_PATTERN = {POSE_HOLD_PATTERN}` "
        f"(12 anchors, sum = {sum(POSE_HOLD_PATTERN)} frames/sec)",
        f"- pose_t = pose_id / {POSE_HZ}; 12 anchors per 30 output frames; 120 across 300",
        f"- boil clock INDEPENDENT: `HOLD_PATTERN = {HOLD_PATTERN}` (12-frame cycle)",
        f"- SMEAR_FRAME = {SMEAR_FRAME} (mid-flight, velocity-aligned ghost)",
        "",
        "| frame | pose_id | pose_t | hold | anchor_frame | is_anchor | boil_variant | smear |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['frame']:04d} | {r['pose_id']:3d} | {r['pose_t']:.4f} | "
            f"{r['hold_len']} | {r['anchor_frame']:04d} | "
            f"{'Y' if r['is_pose_anchor'] else '.'} | {r['boil_variant']} | "
            f"{'Y' if r['smear'] else '.'} |")
    (CHECK_DIR / "pose_id_schedule.md").write_text("\n".join(lines) + "\n",
                                                    encoding="utf-8")
    print("schedule: 300 rows -> checks/pose_id_schedule.json / .md")
    print("  anchors per 30 frames:", out["anchors_per_30_frames"],
          "total pose ids:", out["total_pose_ids"])
    return out


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd == "schedule":
        emit_schedule()
        return
    if cmd == "keys":
        STILL_DIR.mkdir(parents=True, exist_ok=True)
        for i, f in enumerate(KEY_FRAMES):
            render_frame(f).save(STILL_DIR / f"k{i}.png")
        print("keys", KEY_FRAMES)
        return
    FRAME_DIR.mkdir(parents=True, exist_ok=True)
    if cmd == "all":
        frames = range(FRAMES)
    elif cmd.startswith("batch:"):
        # explicit frame list: e.g. "batch:0,7,19,..." (out-of-order friendly)
        frames = [int(x) for x in cmd.split(":", 1)[1].split(",") if x != ""]
    elif cmd.startswith("range:"):
        a, b = cmd.split(":", 1)[1].split("-")
        frames = range(int(a), int(b) + 1)
    else:
        print("unknown cmd", cmd)
        sys.exit(2)
    for f in frames:
        render_frame(f).save(frame_path(f))
    print("rendered", len(list(frames)) if not isinstance(frames, range) else
          (frames.stop - frames.start), "frames ->", FRAME_DIR)


if __name__ == "__main__":
    main()
