#!/usr/bin/env node
/*
 * MOTION-13 / 01-flat-vector — deterministic pure-JS raster renderer.
 * Card 13 「扁平矢量」 (FLAT VECTOR), slug 01-flat-vector.
 * Story 「番茄的旅行」: 种子发芽 → 晒太阳 → 被摘下 → 坐货车 → 进厨房 → 番茄意面.
 *
 * renderFrame(n, seed) is a PURE function of the frame index n and the frozen
 * integer seed. No wall clock, no RNG stream, no inter-frame mutable state.
 * This makes out-of-order / pause-resume / new-process re-render byte-identical
 * by construction and empirically verifiable (the calibrated determinism trio).
 *
 * Card 13 rules (origin/提示词全文.md L200-204 / refs README §1 row 1):
 *  - ONLY solid fills; NO gradients / NO textures; shadow = a darker SOLID block
 *    of the SAME hue (identical R:G:B ratio, integer-scaled).
 *  - people/objects built from circle / rounded-rect / triangle primitives.
 *  - entrance OVERSHOOT 5-10% then spring back; landing SQUASH ~10%.
 *  - ONE hero does a big move at a time; other actors STAGGER 2-4 frames.
 *  - transitions are CARRIED by a shape in the scene: one shape enlarges to
 *    fill the frame and BECOMES the next scene's background (no fade/cut).
 *  - 别做成: no gradients, no inconsistent line widths, no same-frame pop-in of
 *    everything, no fade/cross-dissolve transitions.
 *  - RED TOMATO stays on screen the WHOLE film (L202): ONE persistent red hero
 *    tomato is drawn on top of EVERY frame (the "One Dot" signature of the
 *    reference film popwise), including during transitions and the finale.
 *
 * Determinism contract C1-C10: pure fn of t=frame/fps, seeded only (frozen SEED;
 * actually NO randomness needed — closed-form, which is stronger), no clocks,
 * one cue sheet (SCENES) read by picture + sound (silence is a pre-registered
 * valid choice per 02-EXECUTION-PLAN §78), 1920x1080@30fps 300 frames,
 * 6 stills first (C10), last still contains end copy 「番茄意面」.
 *
 * Modes:
 *   node render.js keys  <dir>            -> stills/k0..k5.png + keyframe_manifest.json (6 stills FIRST)
 *   node render.js full  <dir>            -> frames/f_0000..0299.png + keyframes/ + frame_hashes.json + keyframe_manifest.json
 *   node render.js batch <dir> <n,...>    -> frames/f_<n>.png (fresh process), prints JSON hash map
 *   node render.js range <dir> <a> <b>    -> frames/f_<a..b-1>.png (fresh process), prints JSON hash map
 */
"use strict";
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");
const crypto = require("crypto");

const SEED = 20261115;          // frozen; matches the 3 pilots
const FPS = 30;
const FRAMES = 300;             // 10.000 s
const W = 1920, H = 1080;       // card local spec 1920x1080
const BEAT = 15;                // 120 BPM @ 30fps (one cue sheet)
const FREEZE = 270;             // frames 270..299 = settled finale poster (true freeze)

// ---- palette (SOLID colors only; NO gradients) ------------------------------
// A same-hue darker shadow = integer scale of a base hue (provably same ratio).
const BASE = {
  cream:  [0xF7, 0xF1, 0xE1], ink:    [0x23, 0x1F, 0x20],
  soil:   [0x7A, 0x53, 0x33], leaf:   [0x3E, 0x8E, 0x4A],
  tomato: [0xE2, 0x3B, 0x2E], sun:    [0xF5, 0xC5, 0x2E],
  sky:    [0x8C, 0xD2, 0xE3], truck:  [0x3A, 0x6E, 0xA5],
  wall:   [0xEF, 0xE3, 0xCE], pasta:  [0xF2, 0xD0, 0x7A],
  plate:  [0xFA, 0xFA, 0xF6],
};
function shade(rgb, k) { return rgb.map(v => Math.max(0, Math.min(255, Math.round(v * k)))); }

// indexed-color PNG palette: every color is a SOLID entry; shadows are darker
// SOLID entries of the SAME hue (precomputed integer scales, ratio preserved).
const PALETTE = [
  BASE.cream,  BASE.ink,
  BASE.soil,   shade(BASE.soil, 0.72),
  BASE.leaf,   shade(BASE.leaf, 0.72),
  BASE.tomato, shade(BASE.tomato, 0.70),
  BASE.sun,    shade(BASE.sun, 0.80),
  BASE.sky,    shade(BASE.sky, 0.78),
  BASE.truck,  shade(BASE.truck, 0.72),
  BASE.wall,   shade(BASE.wall, 0.86),
  BASE.pasta,  shade(BASE.pasta, 0.82),
  BASE.plate,  shade(BASE.plate, 0.86),
];
const COL = {
  CREAM: 0, INK: 1,
  SOIL: 2, SOIL_D: 3, LEAF: 4, LEAF_D: 5,
  TOMATO: 6, TOMATO_D: 7, SUN: 8, SUN_D: 9,
  SKY: 10, SKY_D: 11, TRUCK: 12, TRUCK_D: 13,
  WALL: 14, WALL_D: 15, PASTA: 16, PASTA_D: 17,
  PLATE: 18, PLATE_D: 19,
};
// HUE_BASE_GROUPS: shadow index -> base index (for the "same-hue shadow" check)
const SHADOW_OF = { 3: 2, 5: 4, 7: 6, 9: 8, 11: 10, 13: 12, 15: 14, 17: 16, 19: 18 };

// ---- deterministic pixel buffer -------------------------------------------
function newBuf(fill) { const b = new Uint8Array(W * H); if (fill) b.fill(fill); return b; }
function px(buf, x, y, c) { x |= 0; y |= 0; if (x >= 0 && x < W && y >= 0 && y < H) buf[y * W + x] = c; }
function rect(buf, x0, y0, x1, y1, c) {
  x0 |= 0; y0 |= 0; x1 |= 0; y1 |= 0;
  for (let y = Math.max(0, y0); y <= Math.min(H - 1, y1); y++)
    for (let x = Math.max(0, x0); x <= Math.min(W - 1, x1); x++) buf[y * W + x] = c;
}
// axis-aligned rounded rectangle (integer radius). Solid fill only.
function rrect(buf, x0, y0, x1, y1, r, c) {
  x0 |= 0; y0 |= 0; x1 |= 0; y1 |= 0;
  const r2 = r * r;
  for (let y = y0; y <= y1; y++) for (let x = x0; x <= x1; x++) {
    let cx = null, cy = null;
    if (x < x0 + r && y < y0 + r) { cx = x0 + r; cy = y0 + r; }
    else if (x > x1 - r && y < y0 + r) { cx = x1 - r; cy = y0 + r; }
    else if (x < x0 + r && y > y1 - r) { cx = x0 + r; cy = y1 - r; }
    else if (x > x1 - r && y > y1 - r) { cx = x1 - r; cy = y1 - r; }
    if (cx === null) { px(buf, x, y, c); continue; }
    const dx = x - cx, dy = y - cy;
    if (dx * dx + dy * dy <= r2) px(buf, x, y, c);
  }
}
function circle(buf, cx, cy, rad, c) {
  cx |= 0; cy |= 0; if (rad <= 0) return;
  const r2 = rad * rad;
  for (let y = Math.max(0, cy - rad); y <= Math.min(H - 1, cy + rad); y++)
    for (let x = Math.max(0, cx - rad); x <= Math.min(W - 1, cx + rad); x++) {
      const dx = x - cx, dy = y - cy;
      if (dx * dx + dy * dy <= r2) px(buf, x, y, c);
    }
}
// ellipse via scaled radius (for squash & stretch ~10%)
function ellipse(buf, cx, cy, rx, ry, c) {
  cx |= 0; cy |= 0; if (rx <= 0 || ry <= 0) return;
  const rx2 = rx * rx, ry2 = ry * ry;
  for (let y = Math.max(0, cy - Math.ceil(ry)); y <= Math.min(H - 1, cy + Math.ceil(ry)); y++)
    for (let x = Math.max(0, cx - Math.ceil(rx)); x <= Math.min(W - 1, cx + Math.ceil(rx)); x++) {
      const dx = x - cx, dy = y - cy;
      if (dx * dx / rx2 + dy * dy / ry2 <= 1) px(buf, x, y, c);
    }
}
// upright triangle with apex (ax,ay) and base y=by spanning [ax-bw, ax+bw].
function triangle(buf, ax, ay, by, bw, c) {
  ax |= 0; ay |= 0; by |= 0; bw |= 0;
  const dir = Math.sign(by - ay) || 1;
  for (let y = ay; dir > 0 ? y <= by : y >= by; y += dir) {
    const t = Math.abs(y - ay) / Math.max(1, Math.abs(by - ay));
    const half = Math.round(bw * t);
    for (let x = ax - half; x <= ax + half; x++) px(buf, x, y, c);
  }
}

// ---- easing (deterministic, closed-form) -----------------------------------
function clamp(v, a, b) { return v < a ? a : (v > b ? b : v); }
function smooth(t) { t = clamp(t, 0, 1); return t * t * (3 - 2 * t); }
// entrance OVERSHOOT 5-10% then spring back: 0 -> 1.08 -> 1.0 (peak +8%).
function overshoot(t) {
  t = clamp(t, 0, 1);
  if (t <= 0.6) return 1.08 * smooth(t / 0.6);
  return 1.08 - 0.08 * smooth((t - 0.6) / 0.4);
}
// landing SQUASH ~10%: max |deviation| = 0.10, brief window after landing.
function landingSquash(t, landT) {
  if (t < landT || t > landT + 0.30) return { sx: 1, sy: 1 };
  const u = (t - landT) / 0.30;
  const s = Math.sin(Math.PI * u) * 0.10;
  return { sx: 1 + s, sy: 1 - s };
}
function prog(n, start, dur) { return clamp((n - start) / dur, 0, 1); }

// ---- the pre-registered CUE SHEET (one table, read by picture AND sound) ----
// Scene beats (frame @30fps). heroDur = entrance window of the ONE red hero.
// Secondary actors STAGGER 2-4 frames behind the hero onset (scene.start).
// S5 heroDur=15 so the finale is fully settled by FREEZE=270.
const SCENES = [
  { id: "S0_GARDEN",  start: 0,   heroDur: 30, bg: COL.SKY,   label: "种子发芽" },
  { id: "S1_SUN",     start: 60,  heroDur: 30, bg: COL.SKY,   label: "晒太阳" },
  { id: "S2_PICK",    start: 105, heroDur: 30, bg: COL.CREAM, label: "被摘下" },
  { id: "S3_TRUCK",   start: 150, heroDur: 30, bg: COL.SKY,   label: "坐货车" },
  { id: "S4_KITCHEN", start: 210, heroDur: 30, bg: COL.WALL,  label: "进厨房" },
  { id: "S5_PASTA",   start: 255, heroDur: 15, bg: COL.CREAM, label: "番茄意面" },
];
function sceneAt(n) {
  let s = SCENES[0];
  for (const sc of SCENES) if (n >= sc.start) s = sc;
  return s;
}
// STAGGER offsets of the secondary actors (frames behind the hero onset).
// All are in {2,3,4} -> verifier checks "stagger 2-4 frames" AND "no same-frame
// pop-in of everything" (no offset == 0). NEG control: set one to 0 -> FAIL.
const SECONDARY_OFFSETS = {
  sun: 3, leafA: 2, leafB: 4, sunDisc: 2, hand: 3, truckWindow: 2,
  pot: 3, steam: 4, plate: 2, sauce: 2,
};
// settled per-scene anchor of the ONE persistent red hero tomato (always on screen)
const HERO_ANCHORS = {
  S0_GARDEN:  { x: 960,  y: 700, s: 0.30 },
  S1_SUN:     { x: 960,  y: 600, s: 0.55 },
  S2_PICK:    { x: 960,  y: 420, s: 1.00 },
  S3_TRUCK:   { x: 700,  y: 560, s: 0.75 },
  S4_KITCHEN: { x: 1500, y: 600, s: 0.90 },
  S5_PASTA:   { x: 1500, y: 470, s: 0.80 },
};
// The hero's state for frame n: position/scale with entrance overshoot + squash.
function heroAt(n) {
  const sc = sceneAt(n);
  const a = HERO_ANCHORS[sc.id];
  const e = 0.18 + 0.90 * overshoot(prog(n, sc.start, sc.heroDur)); // min 0.18 -> red hero visible from f0 (card L202)
  const { sx, sy } = landingSquash(n / FPS, (sc.start + sc.heroDur) / FPS);
  const startY = a.y - 260;
  const y = Math.round(startY + (a.y - startY) * Math.min(e, 1.08) / 1.08);
  const settled = (prog(n, sc.start, sc.heroDur) === 1);
  return { x: a.x, y, scale: a.s * e, sx, sy, settled };
}

// ---- primitive: the ONE red hero tomato -------------------------------------
// circle body + leaf/stem triangles + same-hue SOLID shadow (no gradient/blur)
function drawTomato(buf, cx, cy, scale, squash) {
  const r = Math.round(120 * scale);
  if (r < 2) { circle(buf, cx, cy, 2, COL.TOMATO); return; }
  const sx = squash.sx, sy = squash.sy;
  ellipse(buf, cx + Math.round(18 * scale), cy + Math.round(26 * scale),
          Math.round(r * sx * 0.92), Math.round(r * sy * 0.92), COL.TOMATO_D);
  ellipse(buf, cx, cy, Math.round(r * sx), Math.round(r * sy), COL.TOMATO);
  const leafR = Math.round(60 * scale);
  triangle(buf, cx, cy - Math.round(r * sy) - 2,
           cy - Math.round(r * sy) - Math.round(40 * scale), leafR, COL.LEAF);
  for (let k = -2; k <= 2; k++)
    triangle(buf, cx + Math.round(k * 34 * scale), cy - Math.round(r * sy) + 4,
             cy - Math.round(r * sy) - Math.round(6 * scale), Math.round(14 * scale), COL.LEAF_D);
  rrect(buf, cx - Math.round(10 * scale), cy - Math.round(r * sy) - Math.round(46 * scale),
             cx + Math.round(10 * scale), cy - Math.round(r * sy) - Math.round(18 * scale),
             Math.round(6 * scale), COL.LEAF);
}

// ---- 5x7 bitmap glyph (solid pixels, no font file) for the end copy --------
const GLYPHS = {
  "番": ["00100","11111","10101","10101","11111","10101","10101"],
  "茄": ["01010","11111","01010","11111","01010","10101","01010"],
  "意": ["00100","11111","01010","11111","10101","11111","00100"],
  "面": ["11111","10001","11111","10101","10101","11111","10101"],
};
function glyph(buf, ch, x0, y0, scale, c) {
  const g = GLYPHS[ch]; if (!g) return;
  for (let r = 0; r < 7; r++) for (let col = 0; col < 5; col++)
    if (g[r][col] === "1") rect(buf, x0 + col * scale, y0 + r * scale,
                                 x0 + (col + 1) * scale - 1, y0 + (r + 1) * scale - 1, c);
}

// ---- scene painters (scenery + staggered secondary actors) -----------------
// NO red tomato here: the single persistent hero is drawn once on top in
// renderFrame. Secondary onsets are staggered SECONDARY_OFFSETS.* frames.
function bgFill(buf, c) { buf.fill(c); }
function ground(buf, y, c, cd) {
  rect(buf, 0, y, W - 1, H - 1, c);
  rect(buf, 0, y, W - 1, y + 26, cd);   // same-hue darker SOLID edge (not gradient)
}
function sceneGarden(buf, n, sc) {
  bgFill(buf, COL.SKY);
  ground(buf, 820, COL.SOIL, COL.SOIL_D);
  const sunT = prog(n, sc.start + SECONDARY_OFFSETS.sun, 22);
  if (sunT > 0) {
    const sr = Math.round(90 * overshoot(sunT));
    circle(buf, 1650, 200, sr, COL.SUN);
    circle(buf, 1650, 200, Math.round(sr * 0.8), COL.SUN_D); // SOLID inner disc, no glow
  }
  // sprout (secondary) with 2/4-frame staggered leaves
  const grow = overshoot(prog(n, sc.start, 40));
  const stemTop = 820 - Math.round(300 * grow);
  rrect(buf, 940 - 14, stemTop, 940 + 14, 820, 10, COL.LEAF);
  const l1 = overshoot(prog(n, sc.start + SECONDARY_OFFSETS.leafA, 26));
  const l2 = overshoot(prog(n, sc.start + SECONDARY_OFFSETS.leafB, 26));
  triangle(buf, 940, stemTop + 60, stemTop + 60 - Math.round(120 * l1), Math.round(70 * l1), COL.LEAF);
  triangle(buf, 940, stemTop + 120, stemTop + 120 + Math.round(110 * l2), Math.round(64 * l2), COL.LEAF_D);
  circle(buf, 940, stemTop, Math.round(10 * grow), COL.SOIL_D);
}
function sceneSun(buf, n, sc) {
  bgFill(buf, COL.SKY);
  ground(buf, 820, COL.SOIL, COL.SOIL_D);
  const sunT = prog(n, sc.start + SECONDARY_OFFSETS.sunDisc, 20);
  circle(buf, 1620, 220, Math.round(130 * overshoot(sunT)), COL.SUN);
  const stemT = prog(n, sc.start + 4, 24);
  rrect(buf, 940 - 14, 820 - Math.round(160 * stemT), 940 + 14, 820, 10, COL.LEAF);
}
function scenePick(buf, n, sc) {
  bgFill(buf, COL.CREAM);
  ground(buf, 860, COL.SOIL, COL.SOIL_D);
  const handT = prog(n, sc.start + SECONDARY_OFFSETS.hand, 24);
  const hy = Math.round(-180 + 300 * handT);
  rrect(buf, 840, hy, 1080, hy + 140, 40, COL.TRUCK);
  rect(buf, 840, hy + 110, 1080, hy + 140, COL.TRUCK_D); // same-hue SOLID shadow
}
function sceneTruck(buf, n, sc) {
  bgFill(buf, COL.SKY);
  rect(buf, 0, 900, W - 1, H - 1, COL.WALL);
  for (let x = 0; x < W; x += 160)
    rect(buf, x + ((n * 2) % 160), 980, x + 80 + ((n * 2) % 160), 996, COL.CREAM);
  const drive = overshoot(prog(n, sc.start, 44));
  const tx = Math.round(-500 + (700 + 500) * drive);
  rrect(buf, tx - 220, 620, tx + 180, 820, 20, COL.TRUCK);
  rrect(buf, tx + 180, 680, tx + 320, 820, 18, COL.TRUCK);
  rect(buf, tx - 220, 790, tx + 320, 820, COL.TRUCK_D); // same-hue SOLID shadow
  circle(buf, tx - 120, 820, 46, COL.INK);
  circle(buf, tx + 240, 820, 46, COL.INK);
  circle(buf, tx - 120, 820, 20, COL.CREAM);
  circle(buf, tx + 240, 820, 20, COL.CREAM);
  const winT = prog(n, sc.start + SECONDARY_OFFSETS.truckWindow, 20);
  if (winT > 0) rrect(buf, tx + 200, 700, tx + 300, 760, 8, COL.SKY);
}
function sceneKitchen(buf, n, sc) {
  bgFill(buf, COL.WALL);
  rect(buf, 0, 760, W - 1, H - 1, COL.CREAM);
  rect(buf, 0, 760, W - 1, 786, COL.WALL_D);
  const drop = overshoot(prog(n, sc.start + SECONDARY_OFFSETS.pot, 30));
  const py = Math.round(-260 + (560 + 260) * drop);
  rrect(buf, 760, py, 1160, py + 260, 30, COL.TRUCK);
  rect(buf, 760, py + 230, 1160, py + 260, COL.TRUCK_D); // same-hue SOLID shadow
  rrect(buf, 720, py - 20, 1200, py + 20, 14, COL.INK);
  const steamT = prog(n, sc.start + SECONDARY_OFFSETS.steam, 24);
  if (steamT > 0) {
    triangle(buf, 880, py - 60, py - 60 - Math.round(90 * steamT), Math.round(26 * steamT), COL.PLATE);
    triangle(buf, 1040, py - 60, py - 60 - Math.round(110 * steamT), Math.round(26 * steamT), COL.PLATE);
  }
}
function scenePasta(buf, n, sc) {
  bgFill(buf, COL.CREAM);
  rect(buf, 0, 840, W - 1, H - 1, COL.WALL);
  rect(buf, 0, 840, W - 1, 866, COL.WALL_D);
  // plate: big flat shape, lands with squash ~10%; settles by FREEZE (270)
  const land = overshoot(prog(n, sc.start + SECONDARY_OFFSETS.plate, 13));
  const { sx, sy } = landingSquash(n / FPS, (sc.start + SECONDARY_OFFSETS.plate + 13) / FPS);
  const pr = Math.round(360 * land);
  ellipse(buf, 980, 660, Math.round(pr * 0.98), Math.round(pr * 0.98), COL.PLATE_D);
  ellipse(buf, 960, 640, Math.round(pr * sx), Math.round(pr * sy), COL.PLATE);
  ellipse(buf, 960, 640, Math.round(pr * 0.72), Math.round(pr * 0.62), COL.PASTA);
  ellipse(buf, 960, 636, Math.round(pr * 0.60), Math.round(pr * 0.50), COL.PASTA_D);
  ellipse(buf, 960, 630, Math.round(pr * 0.52), Math.round(pr * 0.42), COL.PASTA);
  const sauceT = prog(n, sc.start + SECONDARY_OFFSETS.sauce, 13);
  if (sauceT > 0) {
    circle(buf, 880, 600, Math.round(46 * overshoot(sauceT)), COL.TOMATO);
    circle(buf, 1040, 660, Math.round(40 * overshoot(sauceT)), COL.TOMATO);
    circle(buf, 960, 690, Math.round(30 * overshoot(sauceT)), COL.TOMATO_D);
  }
}

// ---- CARRY transition (element-driven, NO fade) -----------------------------
// In the last 8 frames of scenes S0..S4, a SOLID shape of the NEXT scene's
// background color grows from the frame center to fill the whole frame. When it
// fills it IS the next background (the cut is "carried" by an object in the
// scene). NO opacity / NO cross-dissolve: pure solid coverage growth.
// The persistent red hero is drawn AFTER carry, so it rides ON the growing
// shape and stays on screen (card L202) even during full coverage.
function carry(buf, n) {
  const s = sceneAt(n);
  const idx = SCENES.indexOf(s);
  if (idx >= SCENES.length - 1) return;        // last scene: no outgoing carry
  const next = SCENES[idx + 1];
  const wStart = next.start - 8;
  if (n < wStart) return;
  const u = clamp((n - wStart) / 8, 0, 1);
  const maxR = Math.round(Math.hypot(W, H) / 2 * 1.05); // > half-diagonal at u=1
  const rad = Math.round(maxR * smooth(u));
  circle(buf, 960, 540, rad, next.bg);         // grows to BECOME next background
}

// ---- FREEZE: frames 270..299 are the settled final still (C10) -------------
function effectiveFrame(n) { return (n >= FREEZE) ? FREEZE : n; }

function renderFrame(n, seed) {
  n = effectiveFrame(n);
  const buf = newBuf(COL.CREAM);
  const sc = sceneAt(n);
  switch (sc.id) {
    case "S0_GARDEN":  sceneGarden(buf, n, sc);  break;
    case "S1_SUN":     sceneSun(buf, n, sc);     break;
    case "S2_PICK":    scenePick(buf, n, sc);    break;
    case "S3_TRUCK":   sceneTruck(buf, n, sc);   break;
    case "S4_KITCHEN": sceneKitchen(buf, n, sc); break;
    case "S5_PASTA":   scenePasta(buf, n, sc);   break;
  }
  carry(buf, n);
  // ONE persistent red hero tomato, ALWAYS on screen (drawn last, on top).
  const h = heroAt(n);
  drawTomato(buf, h.x, h.y, h.scale, { sx: h.sx, sy: h.sy });
  // END COPY 「番茄意面」 on the finale poster (solid bitmap glyphs).
  if (n >= FREEZE) {
    const g = 14;
    glyph(buf, "番", 640, 900, g, COL.INK);
    glyph(buf, "茄", 740, 900, g, COL.INK);
    glyph(buf, "意", 840, 900, g, COL.INK);
    glyph(buf, "面", 940, 900, g, COL.INK);
  }
  return buf;
}

// ---- minimal deterministic indexed-color PNG encoder (no dependencies) -----
function crc32(buf) {
  let c, crc = 0xFFFFFFFF;
  for (let i = 0; i < buf.length; i++) {
    c = (crc ^ buf[i]) & 0xFF;
    for (let k = 0; k < 8; k++) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
    crc = c ^ (crc >>> 8);
  }
  return (crc ^ 0xFFFFFFFF) >>> 0;
}
function chunk(type, data) {
  const len = Buffer.alloc(4); len.writeUInt32BE(data.length, 0);
  const t = Buffer.from(type, "ascii");
  const crc = Buffer.alloc(4); crc.writeUInt32BE(crc32(Buffer.concat([t, data])), 0);
  return Buffer.concat([len, t, data, crc]);
}
function encodePNG(buf) {
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(W, 0); ihdr.writeUInt32BE(H, 4);
  ihdr[8] = 8; ihdr[9] = 3; ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0; // 8-bit indexed
  const plte = Buffer.alloc(PALETTE.length * 3);
  PALETTE.forEach((rgb, i) => { plte[i * 3] = rgb[0]; plte[i * 3 + 1] = rgb[1]; plte[i * 3 + 2] = rgb[2]; });
  const raw = Buffer.alloc((W + 1) * H);
  for (let y = 0; y < H; y++) {
    raw[y * (W + 1)] = 0; // filter: none (verifier decodes filter-0 rows)
    for (let x = 0; x < W; x++) raw[y * (W + 1) + 1 + x] = buf[y * W + x];
  }
  const sig = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
  return Buffer.concat([
    sig, chunk("IHDR", ihdr), chunk("PLTE", plte),
    chunk("IDAT", zlib.deflateSync(raw, { level: 9 })), chunk("IEND", Buffer.alloc(0)),
  ]);
}
function frameFile(dir, n) { return path.join(dir, "frames", "f_" + String(n).padStart(4, "0") + ".png"); }
function writeFrameTo(dir, n, seed) {
  const data = encodePNG(renderFrame(n, seed));
  const hash = crypto.createHash("sha256").update(data).digest("hex");
  fs.writeFileSync(frameFile(dir, n), data);
  return hash;
}

const KEYFRAMES = [
  { frame: 40,  slug: "K0_SEED_SPROUT" },     // settled garden (C10 revision: still shows the stage)
  { frame: 85,  slug: "K1_SUN_TOMATO" },
  { frame: 130, slug: "K2_PICKED" },
  { frame: 185, slug: "K3_TRUCK" },
  { frame: 235, slug: "K4_KITCHEN" },
  { frame: 270, slug: "K5_PASTA_END_COPY" },  // finale poster / end copy (C10)
];

function main() {
  const [mode, dir, a, b] = process.argv.slice(2);
  if (!dir) { console.error("usage: render.js full|keys|batch|range <dir> [args]"); process.exit(2); }
  fs.mkdirSync(path.join(dir, "frames"), { recursive: true });
  let hashes = {};
  if (mode === "keys") {
    fs.mkdirSync(path.join(dir, "stills"), { recursive: true });
    const manifest = [];
    for (let i = 0; i < KEYFRAMES.length; i++) {
      const kf = KEYFRAMES[i];
      const data = encodePNG(renderFrame(kf.frame, SEED));
      const dst = path.join(dir, "stills", "k" + i + ".png");
      fs.writeFileSync(dst, data);
      manifest.push({ keyframe: kf.slug, frame: kf.frame, t_seconds: kf.frame / FPS,
        path: "stills/k" + i + ".png", sha256: crypto.createHash("sha256").update(data).digest("hex") });
    }
    fs.writeFileSync(path.join(dir, "keyframe_manifest.json"),
      JSON.stringify({ card: "13", slug: "01-flat-vector", seed: SEED, fps: FPS, keyframes: manifest }, null, 2));
    console.log(JSON.stringify({ mode: "keys", keyframes: manifest.length, ok: true }));
  } else if (mode === "full") {
    fs.mkdirSync(path.join(dir, "keyframes"), { recursive: true });
    const manifest = [];
    for (let n = 0; n < FRAMES; n++) {
      hashes[n] = writeFrameTo(dir, n, SEED);
      const kf = KEYFRAMES.find(k => k.frame === n);
      if (kf) {
        const src = fs.readFileSync(frameFile(dir, n));
        const dst = path.join(dir, "keyframes", "kf_" + String(n).padStart(4, "0") + ".png");
        fs.writeFileSync(dst, src);
        manifest.push({ keyframe: kf.slug, frame: n, t_seconds: n / FPS,
          path: "keyframes/kf_" + String(n).padStart(4, "0") + ".png",
          sha256: crypto.createHash("sha256").update(src).digest("hex") });
      }
    }
    fs.writeFileSync(path.join(dir, "frames", "frame_hashes.json"),
      JSON.stringify({ seed: SEED, fps: FPS, frames: FRAMES, resolution: [W, H],
        renderer: "flat-vector-raster-js@1.0.0", card: "13", slug: "01-flat-vector", hashes }, null, 2));
    fs.writeFileSync(path.join(dir, "keyframe_manifest.json"),
      JSON.stringify({ card: "13", slug: "01-flat-vector", seed: SEED, fps: FPS, keyframes: manifest }, null, 2));
    console.log(JSON.stringify({ mode: "full", frames: FRAMES, keyframes: manifest.length, ok: true }));
  } else if (mode === "batch") {
    for (const n of a.split(",").map(Number)) hashes[n] = writeFrameTo(dir, n, SEED);
    console.log(JSON.stringify(hashes));
  } else if (mode === "range") {
    const lo = Number(a), hi = Number(b);
    for (let n = lo; n < hi; n++) hashes[n] = writeFrameTo(dir, n, SEED);
    console.log(JSON.stringify(hashes));
  } else { console.error("unknown mode " + mode); process.exit(2); }
}
if (require.main === module) main();
// Export the REAL shipped functions for verifiers (no copy drift).
module.exports = {
  SEED, FPS, FRAMES, W, H, BEAT, FREEZE, SCENES, KEYFRAMES, PALETTE, COL, BASE,
  SHADOW_OF, SECONDARY_OFFSETS, HERO_ANCHORS, shade, sceneAt, heroAt,
  renderFrame, effectiveFrame, overshoot, landingSquash, prog, smooth, clamp,
  encodePNG, frameFile, writeFrameTo, drawTomato,
};
