#!/usr/bin/env node
/*
 * MOTION-10 / 06-collage — deterministic pure-JS raster renderer (COLLAGE / 拼贴).
 *
 * renderFrame(n, seed) is a PURE function of the frame index n and the frozen
 * integer seed. No wall clock, no Math.random, no inter-frame mutable state.
 * This makes out-of-order / pause-resume / new-process / independent-full
 * re-render byte-identical BY CONSTRUCTION, and empirically verifiable.
 *
 * Card 10 spec (提示词全文.md L160-168):
 *   - every element has a scissor-cut white border or torn-paper rough edge
 *   - a small drop shadow => visible stacking / layering
 *   - photos are halftone or high-contrast B/W; background is old newsprint/kraft
 *   - deliberately wrong proportions: big head small body, hands bigger than a person
 *   - the picture updates only 8-12 times per second, each time jittering 1-2 px
 *   - jaw + wings rotate around a 图钉 (pin) pivot; beak swaps 2-3 cut-out frames
 *   - transition is a hand's action: a sheet of paper flips over to cover the frame
 *   - NOT smooth tween, NOT clean digital photos
 *
 * 内容: 老版画猫头鹰当上报社主编，嘴一张一合念头条，报纸从身后飞出来，
 *      大标题斜着拍下「猫头鹰日报」
 *
 * Implementation: 1920x1080 indexed-color (8 palette entries) software raster.
 *   12 Hz tick clock: tick = floor(2n/5) (0..119), HELD across 2-3 30fps frames
 *   -> no smooth tween between visual states (card forbids it). A seeded ±2px
 *   whole-canvas jitter is the "每次随机抖一两个像素". All randomness is a pure
 *   integer hash of (i, j, salt, seed) — there is NO RNG stream.
 *
 * Modes:
 *   node render.mjs full  <dir>          -> frames/f_0000..0299.png + keyframes/ +
 *                                          frames/frame_hashes.json + keyframe_manifest.json
 *   node render.mjs batch <dir> <n,...>  -> frames/f_<n>.png for listed indices, prints JSON hash map
 *   node render.mjs range <dir> <a> <b>  -> frames/f_<a..b-1>.png, prints JSON hash map
 *   node render.mjs one   <n>            -> prints JSON {sha256, tick, beakPhase, jitter}
 */
"use strict";
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");
const crypto = require("crypto");

const SEED = 20261115;
const FPS = 30;
const FRAMES = 300;
const W = 1920, H = 1080;
const VISUAL_HZ = 12;
const TICKS = FRAMES * VISUAL_HZ / FPS; // 120

// ---- 8-color indexed palette (newsprint / collage cut-outs) -----------------
// index: 0 paper bg, 1 ink, 2 cut white, 3 halftone grey, 4 stamp red,
//        5 shadow dark, 6 torn-edge light, 7 title black
const RGB = [
  [214, 199, 166], // 0 PAPER_BG 旧报纸/牛皮纸
  [30, 28, 24],    // 1 INK 高反差黑白
  [250, 248, 240], // 2 WHITE 剪刀剪的白描边
  [150, 140, 120], // 3 GREY 网点/中间调
  [176, 52, 40],   // 4 RED 印章(唯一彩色点缀)
  [92, 82, 70],    // 5 DARK 影子
  [235, 226, 205], // 6 LIGHT 撕纸毛边亮侧/半调高光
  [18, 16, 14],    // 7 BLACK_DEEP 标题黑块
];
const C = { BG: 0, INK: 1, WHITE: 2, GREY: 3, RED: 4, SHADOW: 5, LIGHT: 6, BLACK: 7 };

// ---- deterministic integer hash -------------------------------------------
// Pure function: (i, j, salt, seed) -> uint32. No RNG stream, no state.
function imul(a, b) { return Math.imul(a, b) | 0; }
function hash32(i, j, salt, seed) {
  let h = (imul(i | 0, 374761393) + imul(j | 0, 668265263) +
           imul(salt | 0, 2246822519) + imul(seed | 0, 3266489917)) | 0;
  h = imul(h ^ (h >>> 13), 1274126177);
  h ^= h >>> 16;
  return h >>> 0;
}
const h01 = (i, j, salt, seed) => hash32(i, j, salt, seed) / 4294967296;

// 12 Hz tick clock: pure function of frame index.
function tickOf(n) { return Math.floor(n * VISUAL_HZ / FPS); } // floor(2n/5)

// seeded ±2px whole-canvas jitter (card: 每次随机抖一两个像素).
function jitterOf(tick, seed) {
  const dx = (hash32(tick, 0, 11, seed) % 5) - 2;
  const dy = (hash32(tick, 0, 13, seed) % 5) - 2;
  return [dx, dy];
}
// beak cut-out frame substitution: 3 discrete shapes, no morph.
function beakPhase(tick) { return Math.floor(tick / 2) % 3; }

// ---- pixel buffer ----------------------------------------------------------
function newBuf() { return new Uint8Array(W * H); }
function px(buf, x, y, c) {
  x = x | 0; y = y | 0;
  if (x >= 0 && x < W && y >= 0 && y < H) buf[y * W + x] = c;
}
function rect(buf, x0, y0, x1, y1, c) {
  for (let y = y0 | 0; y <= (y1 | 0); y++) for (let x = x0 | 0; x <= (x1 | 0); x++) px(buf, x, y, c);
}
function hline(buf, x0, x1, y, c) { rect(buf, x0, y, x1, y, c); }
function vline(buf, x, y0, y1, c) { rect(buf, x, y0, x, y1, c); }

// filled circle (integer midpoint) — for halftone dots, eyes, pin head, stamp.
function disc(buf, cx, cy, r, c) {
  const r2 = r * r;
  for (let y = -r; y <= r; y++) {
    const dx = Math.floor(Math.sqrt(Math.max(0, r2 - y * y)));
    hline(buf, cx - dx, cx + dx, cy + y, c);
  }
}
// ring (annulus) for stamp / pin outline.
function ring(buf, cx, cy, rOuter, rInner, c) {
  const ro2 = rOuter * rOuter, ri2 = rInner * rInner;
  for (let y = -rOuter; y <= rOuter; y++) for (let x = -rOuter; x <= rOuter; x++) {
    const d2 = x * x + y * y;
    if (d2 <= ro2 && d2 > ri2) px(buf, cx + x, cy + y, c);
  }
}

// scanline polygon fill with a deterministic torn/serrated edge on the LEFT
// and RIGHT borders (card: 撕纸毛边). Standard even-odd scanline.
function fillPoly(buf, pts, c, edgeColor, torn, seed, salt) {
  if (pts.length < 3) return;
  let ymin = Infinity, ymax = -Infinity;
  for (const p of pts) { if (p[1] < ymin) ymin = p[1]; if (p[1] > ymax) ymax = p[1]; }
  ymin = Math.max(0, Math.floor(ymin)); ymax = Math.min(H - 1, Math.ceil(ymax));
  const xs = [];
  for (let y = ymin; y <= ymax; y++) {
    xs.length = 0;
    for (let k = 0; k < pts.length; k++) {
      const [x1, y1] = pts[k], [x2, y2] = pts[(k + 1) % pts.length];
      if ((y1 <= y && y2 > y) || (y2 <= y && y1 > y)) {
        xs.push(x1 + (y - y1) * (x2 - x1) / (y2 - y1));
      }
    }
    xs.sort((a, b) => a - b);
    for (let i = 0; i + 1 < xs.length; i += 2) {
      let l = Math.ceil(xs[i]), r = Math.floor(xs[i + 1]);
      if (r < 0 || l >= W) continue;
      l = Math.max(0, l); r = Math.min(W - 1, r);
      if (torn && edgeColor !== undefined) {
        const lj = (hash32(y, Math.floor(xs[i]), salt, seed) % 5) - 2;
        const rj = (hash32(y, Math.floor(xs[i + 1]), salt + 7, seed) % 5) - 2;
        hline(buf, l, r, y, c);
        for (let t = 0; t < torn; t++) { px(buf, l + lj - t, y, edgeColor); px(buf, r + rj + t, y, edgeColor); }
      } else {
        hline(buf, l, r, y, c);
      }
    }
  }
}

// Draw a cut-out element: shadow copy (offset 6,7) -> 3px WHITE border (scissor
// cut) -> the fill polygon with a torn edge. Border = the polygon dilated by 3px
// via 8 offset copies; this yields a crisp, non-antialiased scissor outline.
function cutout(buf, pts, fillColor, seed, salt, opts) {
  opts = opts || {};
  const shadow = opts.shadow === false ? null : [6, 7];
  const bw = opts.border === undefined ? 3 : opts.border;
  const torn = opts.torn === undefined ? 2 : opts.torn;
  const shifted = (dx, dy) => pts.map(p => [p[0] + dx, p[1] + dy]);
  if (shadow) {
    fillPoly(buf, shifted(shadow[0] + 2, shadow[1] + 2), C.SHADOW, undefined, 0, seed, salt + 91);
    fillPoly(buf, shifted(shadow[0], shadow[1]), C.SHADOW, undefined, 0, seed, salt + 91);
  }
  // white scissor border = union of the polygon translated over a 3px disc
  for (let dy = -bw; dy <= bw; dy++) for (let dx = -bw; dx <= bw; dx++) {
    if (dx * dx + dy * dy > bw * bw + bw) continue;
    fillPoly(buf, shifted(dx, dy), C.WHITE, undefined, 0, seed, salt + 17);
  }
  // torn-paper edge on the fill
  fillPoly(buf, pts, fillColor, C.LIGHT, torn, seed, salt);
}

// rotate a point list around a pivot (card: 下巴/翅膀绕图钉转).
function rotate(pts, cx, cy, angle) {
  const cs = Math.cos(angle), sn = Math.sin(angle);
  return pts.map(p => {
    const x = p[0] - cx, y = p[1] - cy;
    return [cx + x * cs - y * sn, cy + x * sn + y * cs];
  });
}

// ---- halftone / high-contrast B-W "photograph" -----------------------------
// A clipped halftone dot screen + hatch strokes inside a polygon region test.
function halftoneRegion(buf, cx, cy, rx, ry, seed, salt, phase) {
  const step = 11;
  for (let y = cy - ry; y <= cy + ry; y += step) {
    for (let x = cx - rx; x <= cx + rx; x += step) {
      const nx = (x - cx) / rx, ny = (y - cy) / ry;
      if (nx * nx + ny * ny > 1) continue;
      // local tone: darker near the edge, lighter center -> variable dot radius
      const tone = 0.55 + 0.4 * (nx * nx + ny * ny);
      const jitter = h01(x, y, salt, seed) * 0.15;
      const r = Math.max(1, Math.round((tone + jitter) * (step * 0.52)));
      disc(buf, x + (phase ? (phase % 3) : 0), y, r, C.INK);
    }
  }
  // a few hatch strokes (high-contrast engraving feel)
  for (let k = -3; k <= 3; k++) {
    const yy = cy + k * 26;
    hline(buf, cx - rx * 0.7, cx + rx * 0.5, yy, C.INK);
  }
}

// ---- background: old newsprint / kraft paper -------------------------------
function drawBackground(buf, seed) {
  rect(buf, 0, 0, W - 1, H - 1, C.BG);
  // column rules
  for (let x = 60; x < W; x += 120) vline(buf, x, 40, H - 40, C.GREY);
  // tiny "newsprint type" dashes, deterministic, pure
  for (let y = 70; y < H - 40; y += 22) {
    for (let x = 70; x < W - 40; x += 120) {
      const h = hash32(x, y, 3, seed);
      const len = 30 + (h % 60);
      hline(buf, x, x + len, y, C.GREY);
      if ((h >>> 8) % 3 === 0) hline(buf, x, x + len - 10, y + 7, C.GREY);
    }
  }
  // fibre speckle (old-paper grain)
  for (let i = 0; i < 2600; i++) {
    const x = hash32(i, 1, 5, seed) % W;
    const y = hash32(i, 2, 5, seed) % H;
    px(buf, x, y, (hash32(i, 3, 5, seed) % 2) ? C.LIGHT : C.GREY);
  }
  // masthead thin rules (top band)
  hline(buf, 40, W - 40, 44, C.INK);
  hline(buf, 40, W - 40, 48, C.INK);
}

// ---- slanted title 「猫头鹰日报」 as hard black cut-out blocks ---------------
// 5 glyph-like blocks (no font file), drawn rotated by ~-11deg as a group.
function drawTitle(buf, tick, seed) {
  // "slammed down" entrance: ticks 60..72 the title scales/rotates into place.
  let appear = 1;
  let angle = -0.19;
  if (tick >= 60 && tick < 72) {
    const t = (tick - 60) / 12;
    appear = t;               // grows from 0 to 1
    angle = -0.19 - (1 - t) * 0.7; // more slanted while flying in
  }
  if (tick < 60) return; // not yet on screen before the slam
  const scale = 0.35 + 0.65 * appear;
  const cx = 980, cy = 250;
  // 5 rectangular glyph blocks of varying width (title cut-outs)
  const glyphW = [120, 110, 130, 100, 140];
  let x = -320;
  for (let g = 0; g < 5; g++) {
    const w = Math.round(glyphW[g] * scale);
    const h = Math.round(150 * scale);
    const local = [[x, -h / 2], [x + w, -h / 2], [x + w, h / 2], [x, h / 2]];
    const pts = rotate(local, 0, 0, angle).map(p => [p[0] + cx, p[1] + cy]);
    // inner black glyph, with a WHITE cut border + shadow (layered collage)
    cutout(buf, pts, C.BLACK, seed, 700 + g, { border: 3, torn: 2, shadow: true });
    // a couple of INK "holes" inside each glyph for a carved/letterpress look
    const holeY = cy - 30 * scale;
    disc(buf, cx + x + w * 0.5, holeY, Math.round(14 * scale), C.INK);
    x += w + 18;
  }
  // the RED stamp appears once the title has landed (ticks >= 72)
  if (tick >= 72) {
    const sx = 1500, sy = 230;
    ring(buf, sx, sy, 70, 60, C.RED);
    disc(buf, sx, sy, 8, C.RED);
    for (let a = 0; a < 8; a++) {
      const ang = a * Math.PI / 4;
      hline(buf, sx + Math.round(20 * Math.cos(ang)), sx + Math.round(50 * Math.cos(ang)),
            sy + Math.round(20 * Math.sin(ang)), C.RED);
    }
  }
}

// ---- newspaper sheets flying out from behind the owl -----------------------
function drawNewspapers(buf, tick, seed) {
  if (tick < 24) return; // start flying after K1
  const n = Math.min(4, Math.floor((tick - 24) / 8) + 1);
  for (let i = 0; i < n; i++) {
    const t = tick - 24 - i * 8;
    const px0 = 520 + (hash32(i, 0, 31, seed) % 900) + t * 3;
    const py0 = 620 - t * 2 + i * 60;
    const w = 230 + (hash32(i, 1, 31, seed) % 90);
    const h = 150;
    const ang = (hash32(i, 2, 31, seed) % 100) / 100 * 0.5 - 0.25;
    const local = [[0, 0], [w, 0], [w, h], [0, h]];
    const pts = rotate(local, w / 2, h / 2, ang).map(p => [p[0] + px0 - w / 2, p[1] + py0 - h / 2]);
    cutout(buf, pts, C.LIGHT, seed, 500 + i, { border: 3, torn: 2, shadow: true });
    // headline dashes on the sheet (high-contrast print)
    for (let r = 0; r < 5; r++) {
      const yy = py0 + 24 + r * 22;
      hline(buf, px0 - w / 2 + 16, px0 - w / 2 + 16 + (60 + (hash32(i, r, 33, seed) % 120)), yy, C.INK);
    }
  }
}

// ---- the owl editor (big head, small body) ---------------------------------
function drawOwl(buf, tick, seed) {
  const cx = 770, cy = 560;
  // per-tick pivot angles (card: 下巴、翅膀绕图钉转)
  const jawAngle = Math.sin(tick * 0.30) * 0.42;   // jaw opens/closes
  const wingAngle = Math.sin(tick * 0.17) * 0.55;  // wing flaps around a pin

  // ---- wings (drawn BEHIND the body, rotate around a pin pivot) ----
  const pinL = [cx - 210, cy + 40], pinR = [cx + 210, cy + 40];
  const wingL = [[-170, -40], [-20, -110], [40, 10], [-30, 90], [-170, 60]];
  const wingR = [[170, -40], [20, -110], [-40, 10], [30, 90], [170, 60]];
  cutout(buf, rotate(wingL, 0, 0, -wingAngle).map(p => [p[0] + pinL[0], p[1] + pinL[1]]),
         C.INK, seed, 201, { border: 3, torn: 2, shadow: true });
  cutout(buf, rotate(wingR, 0, 0, wingAngle).map(p => [p[0] + pinR[0], p[1] + pinR[1]]),
         C.INK, seed, 202, { border: 3, torn: 2, shadow: true });

  // ---- body (deliberately SMALL vs the head) ----
  const body = [[cx - 120, cy + 120], [cx + 120, cy + 120],
                [cx + 95, cy + 300], [cx - 95, cy + 300]];
  cutout(buf, body, C.GREY, seed, 210, { border: 3, torn: 2, shadow: true });
  // halftone on body (高反差黑白 photo feel)
  halftoneRegion(buf, cx, cy + 210, 100, 90, seed, 211, tick);

  // ---- head: BIG high-contrast halftone "old engraving" cut-out ----
  const hr = 250;
  // white scissor border ring + shadow first
  ring(buf, cx + 6, cy + 7, hr + 8, hr - 2, C.SHADOW);
  ring(buf, cx, cy, hr + 5, hr - 3, C.WHITE);
  disc(buf, cx, cy, hr, C.LIGHT);
  halftoneRegion(buf, cx, cy, hr - 14, hr - 14, seed, 220, tick);
  // ear tufts (torn paper)
  cutout(buf, [[cx - 210, cy - 190], [cx - 150, cy - 320], [cx - 90, cy - 200]],
         C.INK, seed, 221, { border: 3, torn: 2, shadow: false });
  cutout(buf, [[cx + 210, cy - 190], [cx + 150, cy - 320], [cx + 90, cy - 200]],
         C.INK, seed, 222, { border: 3, torn: 2, shadow: false });
  // big eyes (high-contrast B/W)
  for (const ex of [cx - 90, cx + 90]) {
    disc(buf, ex, cy - 40, 78, C.WHITE);
    disc(buf, ex, cy - 40, 72, C.INK);
    disc(buf, ex, cy - 40, 40, C.LIGHT);
    disc(buf, ex - 6, cy - 46, 22, C.BLACK);
    disc(buf, ex + 8, cy - 30, 7, C.WHITE);
  }
  // ---- beak: 3 discrete cut-out shapes, swapped per phase (no morph) ----
  const bp = beakPhase(tick);
  const beakShapes = [
    [[cx - 46, cy + 20], [cx + 46, cy + 20], [cx, cy + 120]],               // closed
    [[cx - 52, cy + 16], [cx + 52, cy + 16], [cx + 20, cy + 95], [cx - 20, cy + 95]], // half
    [[cx - 60, cy + 10], [cx + 60, cy + 10], [cx + 34, cy + 70],
     [cx, cy + 150], [cx - 34, cy + 70]],                                    // wide open (reading headline)
  ];
  cutout(buf, beakShapes[bp], C.BLACK, seed, 230, { border: 2, torn: 1, shadow: true });

  // ---- jaw/chin rotating around a 图钉 pivot (visible pin) ----
  const jawPin = [cx, cy + 150];
  const jaw = [[-150, -10], [150, -10], [120, 70], [-120, 70]];
  const jawPts = rotate(jaw, 0, 0, jawAngle).map(p => [p[0] + jawPin[0], p[1] + jawPin[1]]);
  cutout(buf, jawPts, C.GREY, seed, 240, { border: 3, torn: 2, shadow: true });
  halftoneRegion(buf, jawPin[0], jawPin[1] + 30, 110, 34, seed, 241, tick);
  // the 图钉 (pin) pivot dots
  for (const p of [jawPin, pinL, pinR]) {
    disc(buf, p[0] + 6, p[1] + 7, 9, C.SHADOW);
    disc(buf, p[0], p[1], 9, C.RED);
    disc(buf, p[0], p[1], 4, C.INK);
    disc(buf, p[0] - 2, p[1] - 2, 2, C.WHITE);
  }
}

// ---- hand paper-flip transition (ticks 96..103) ---------------------------
// An oversized hand + a big sheet of paper rotate/scale over the whole canvas
// and cover it at tick 100; the 报头 is on the far side. No smooth tween: the
// sheet's discrete state changes only per 12Hz tick.
function drawHandFlip(buf, tick, seed) {
  if (tick < 96 || tick > 103) return false;
  const t = tick - 96; // 0..7
  // coverage: grows 0 -> 1 by tick 100 (frame 250), then recedes by 103
  let cover;
  if (t <= 4) cover = Math.min(1, (t + 1) / 5);
  else cover = Math.max(0, 1 - (t - 4) / 4);
  if (cover <= 0) return false;
  const shW = Math.round(W * 1.15 * cover), shH = Math.round(H * 1.15 * cover);
  const sx = (W - shW) / 2, sy = (H - shH) / 2;
  const ang = -0.12 + t * 0.03;
  const local = [[0, 0], [shW, 0], [shW, shH], [0, shH]];
  const pts = rotate(local, shW / 2, shH / 2, ang).map(p => [p[0] + sx, p[1] + sy]);
  cutout(buf, pts, C.LIGHT, seed, 900, { border: 4, torn: 3, shadow: true });
  // "the other side": masthead lines on the flipped sheet
  if (cover > 0.55) {
    hline(buf, sx + 120, sx + shW - 120, sy + 160, C.INK);
    hline(buf, sx + 120, sx + shW - 120, sy + 166, C.INK);
    for (let r = 0; r < 6; r++)
      hline(buf, sx + 120, sx + 120 + (200 + (hash32(t, r, 77, seed) % 400)), sy + 220 + r * 40, C.GREY);
  }
  // an OVERSIZED hand cut-out (bigger than a person) reaching in from the right
  const handCx = W - 260 + Math.round(120 * (1 - cover));
  const handCy = H / 2 + 120;
  const hand = [[handCx - 170, handCy - 60], [handCx + 60, handCy - 140],
                [handCx + 150, handCy - 60], [handCx + 120, handCy + 180],
                [handCx - 150, handCy + 150]];
  cutout(buf, rotate(hand, handCx, handCy, -0.2 + t * 0.05),
         C.GREY, seed, 910, { border: 4, torn: 3, shadow: true });
  // fingers (3 thick cut-out bars) — deliberately too big
  for (let f = 0; f < 3; f++) {
    const fy = handCy - 120 + f * 90;
    rect(buf, handCx - 60, fy, handCx + 170, fy + 46, C.WHITE);
    rect(buf, handCx - 56, fy + 4, handCx + 166, fy + 42, C.GREY);
  }
  return true;
}

// ---- master frame function (PURE) ------------------------------------------
function renderFrame(n, seed) {
  const tick = tickOf(n);
  const buf = newBuf();
  // 1. old-newsprint background (static base, no wall clock)
  drawBackground(buf, seed);
  // 2. newspapers flying out from behind
  drawNewspapers(buf, tick, seed);
  // 3. the owl editor (big head / small body / pivot jaw + wings / beak swap)
  drawOwl(buf, tick, seed);
  // 4. slanted 「猫头鹰日报」 title + RED stamp
  drawTitle(buf, tick, seed);
  // 5. hand paper-flip transition (covers the frame at tick 100)
  drawHandFlip(buf, tick, seed);

  // 6. whole-canvas ±2px jitter (card: 每次随机抖一两个像素). Applied as a
  //    pure translation of the completed collage; clipped edges show PAPER_BG.
  const [jdx, jdy] = jitterOf(tick, seed);
  if (jdx !== 0 || jdy !== 0) {
    const out = newBuf();
    for (let y = 0; y < H; y++) {
      const sy = y - jdy;
      if (sy < 0 || sy >= H) { out.fill(C.BG, y * W, y * W + W); continue; }
      out.fill(C.BG, y * W, y * W + W);
      const dstStart = Math.max(0, jdx);
      const dstEnd = Math.min(W, W + jdx);
      for (let x = dstStart; x < dstEnd; x++) out[y * W + x] = buf[sy * W + (x - jdx)];
    }
    return { buf: out, tick, jdx, jdy, beakPhase: beakPhase(tick) };
  }
  return { buf, tick, jdx, jdy, beakPhase: beakPhase(tick) };
}

// ---- minimal deterministic PNG encoder (indexed, 8-color, no deps) ---------
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
  ihdr[8] = 8;  // bit depth
  ihdr[9] = 3;  // indexed color
  ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0;
  const plte = Buffer.alloc(RGB.length * 3);
  RGB.forEach((rgb, i) => { plte[i * 3] = rgb[0]; plte[i * 3 + 1] = rgb[1]; plte[i * 3 + 2] = rgb[2]; });
  const raw = Buffer.alloc((W + 1) * H);
  for (let y = 0; y < H; y++) {
    raw[y * (W + 1)] = 0; // filter: none
    for (let x = 0; x < W; x++) raw[y * (W + 1) + 1 + x] = buf[y * W + x];
  }
  const sig = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
  return Buffer.concat([
    sig,
    chunk("IHDR", ihdr),
    chunk("PLTE", plte),
    chunk("IDAT", zlib.deflateSync(raw, { level: 9 })),
    chunk("IEND", Buffer.alloc(0)),
  ]);
}
function frameFile(dir, n) {
  return path.join(dir, "frames", "f_" + String(n).padStart(4, "0") + ".png");
}
function pngBytes(n, seed) { return encodePNG(renderFrame(n, seed).buf); }
function writeFrame(dir, n, seed) {
  const data = pngBytes(n, seed);
  const hash = crypto.createHash("sha256").update(data).digest("hex");
  fs.writeFileSync(frameFile(dir, n), data);
  return hash;
}

const KEYFRAMES = [
  { frame: 0,   tick: 0,   label: "K0 旧报纸底 + 猫头鹰主编剪贴登场(大头小身)" },
  { frame: 60,  tick: 24,  label: "K1 嘴剪纸第1态 / 下巴绕图钉张开 / 念头条" },
  { frame: 120, tick: 48,  label: "K2 报纸从身后飞出(三层叠影) / 翅膀转" },
  { frame: 180, tick: 72,  label: "K3 大标题斜着拍下 猫头鹰日报 (旋转黑块)" },
  { frame: 240, tick: 96,  label: "K4 大手翻纸转场盖住画面" },
  { frame: 299, tick: 119, label: "K5 定格报头 + 印章 / 抖动收束" },
];

function main() {
  const [mode, dir, a, b] = process.argv.slice(2);
  if (!dir) { console.error("usage: render.mjs full|batch|range <dir> [args] | one <n>"); process.exit(2); }
  if (mode === "one") {
    const n = Number(dir);
    const f = renderFrame(n, SEED);
    const h = crypto.createHash("sha256").update(encodePNG(f.buf)).digest("hex");
    console.log(JSON.stringify({ frame: n, sha256: h, tick: f.tick, beakPhase: f.beakPhase, jitter: [f.jdx, f.jdy] }));
    return;
  }
  fs.mkdirSync(path.join(dir, "frames"), { recursive: true });
  let hashes = {};
  if (mode === "full") {
    fs.mkdirSync(path.join(dir, "keyframes"), { recursive: true });
    const manifest = [];
    for (let n = 0; n < FRAMES; n++) {
      hashes[n] = writeFrame(dir, n, SEED);
      const kf = KEYFRAMES.find(k => k.frame === n);
      if (kf) {
        const src = fs.readFileSync(frameFile(dir, n));
        const dst = path.join(dir, "keyframes", "kf_" + String(n).padStart(4, "0") + ".png");
        fs.writeFileSync(dst, src);
        manifest.push({
          keyframe: kf.label, frame: n, tick: kf.tick, t_seconds: +(n / FPS).toFixed(4),
          path: "keyframes/kf_" + String(n).padStart(4, "0") + ".png",
          sha256: crypto.createHash("sha256").update(src).digest("hex"),
        });
      }
    }
    fs.writeFileSync(path.join(dir, "frames", "frame_hashes.json"),
      JSON.stringify({
        seed: SEED, fps: FPS, frames: FRAMES, resolution: [W, H],
        visual_hz: VISUAL_HZ, ticks: TICKS,
        renderer: "collage-raster-js@1.0.0",
        tick_formula: "floor(2*n/5)",
        hashes,
      }, null, 2));
    fs.writeFileSync(path.join(dir, "keyframe_manifest.json"),
      JSON.stringify({ card: "10", slug: "06-collage", seed: SEED, fps: FPS,
                       keyframes: manifest }, null, 2));
    console.log(JSON.stringify({ mode: "full", frames: FRAMES, keyframes: manifest.length, ok: true }));
  } else if (mode === "batch") {
    const list = a.split(",").map(Number);
    for (const n of list) hashes[n] = writeFrame(dir, n, SEED);
    console.log(JSON.stringify(hashes));
  } else if (mode === "range") {
    const lo = Number(a), hi = Number(b);
    for (let n = lo; n < hi; n++) hashes[n] = writeFrame(dir, n, SEED);
    console.log(JSON.stringify(hashes));
  } else { console.error("unknown mode " + mode); process.exit(2); }
}
if (require.main === module) main();

// Exported SEMANTIC functions for verify.js: the verifier re-derives claims from
// the REAL shipped tickOf/jitterOf/beakPhase (required, not copied), so a
// renderer/claim divergence is caught. Never a hand-copied number.
module.exports = {
  SEED, FPS, FRAMES, W, H, VISUAL_HZ, TICKS, RGB, C,
  tickOf, jitterOf, beakPhase, hash32, renderFrame, pngBytes, encodePNG,
  KEYFRAMES,
};
