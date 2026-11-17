#!/usr/bin/env node
/*
 * MOTION-09 / 12-aurora-glass — card 09 玻璃拟态 / GLASSMORPHISM
 * Deterministic dependency-free pure-JS raster renderer (truecolor RGB PNG).
 *
 * renderFrame(n, seed) is a PURE function of n + the frozen seed:
 *  - no wall clock, no RNG stream, no inter-frame mutable state;
 *  - m = min(n, 270) => frames 270..299 are byte-identical (pre-registered hold).
 *
 * Modes:
 *   node render.js full  <dir>            -> 300 frames + 6 keyframes + frame_hashes.json + keyframe_manifest.json
 *   node render.js batch <dir> n,n,..     -> re-render listed frames, print {n:sha256} (for determinism trio)
 *   node render.js range <dir> lo hi      -> re-render [lo,hi), print {n:sha256}
 *   node render.js kf    <dir>            -> render the 6 keyframes only (write keyframes/kf_*.png)
 *
 * The renderer exports its SEMANTIC constants (PALETTE, ACTIONS, SWEEP, ease,
 * driftAmp, blurredLightAt, glassMetrics) so verify_rules.js checks the SHIPPED
 * semantics rather than a copied one (pos + neg controls).
 */
"use strict";
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");
const crypto = require("crypto");

const SEED = 20261115;
const FPS = 30, FRAMES = 300;
const W = 640, H = 360;

/* ---- card-09 palette: dark base + 3 ADJACENT warm hues ----------------------
 * Hues chosen on the color wheel so the circular span (amber 36 -> peach 22 ->
 * rose 345) is < 90 degrees; NO complementary (opposite) pair. The dark ink
 * base is neutral (not a hue), so it cannot form a complementary pair. */
const PALETTE = [
  { name: "amber", rgb: [242, 176,  86], hue: 36 },
  { name: "peach", rgb: [240, 140, 122], hue: 22 },
  { name: "rose",  rgb: [226, 110, 148], hue: 345 },
];
const BG = [16, 16, 26];          // dark base 暗底
const CARD_TINT = [235, 235, 245];
const BRIGHT_EDGE = [255, 255, 255];
const SWEEP_RGB = [255, 252, 240];
const HOLD = 270;

/* ---- pre-registered action schedule (see beat_schedule.md) ----------------- */
const ACTIONS = [
  { id: "CARD_A",    onset: 30,  dur: 30, layer: 0 },
  { id: "CARD_B",    onset: 66,  dur: 30, layer: 1 },
  { id: "CARD_C",    onset: 102, dur: 30, layer: 2 },
  { id: "HIGHLIGHT", onset: 180, dur: 30, layer: -1 },  // the ONE sweep
  { id: "APP_NAME",  onset: 216, dur: 30, layer: -1 },
  { id: "END_HOLD",  onset: 270, dur: 30, layer: -1 },
];
const SWEEP_INTERVALS = [{ start: 180, end: 210 }];     // exactly ONE
const APP_NAME_ONSET = 216;                             // > sweep.end
const DEPTH_AMPS = [2, 4, 7];                            // strictly increasing: near moves faster

/* sine ease — monotone 0..1, max EXACTLY 1.0 (no overshoot / no bounce) */
function ease(t) {
  if (t <= 0) return 0;
  if (t >= 1) return 1;
  return 0.5 - 0.5 * Math.cos(Math.PI * t);
}
function actionE(action, m) {
  if (m < action.onset) return 0;
  const t = (m - action.onset) / action.dur;
  return ease(t);
}
function driftAmp(layer) { return DEPTH_AMPS[Math.max(0, Math.min(2, layer))]; }

/* ---- light field ----------------------------------------------------------
 * 3 large soft blobs drifting slowly (one full sin/cos period over 300 frames),
 * additive so nearby blobs MERGE (融合). Pure function of m. */
const BLOBS = [
  { cx: 200, cy: 150, r: 150, hue: 0, px: 0.9, py: 0.6 },
  { cx: 410, cy: 210, r: 165, hue: 1, px: -0.7, py: 0.8 },
  { cx: 320, cy: 110, r: 140, hue: 2, px: 0.5, py: -0.5 },
];
function fineLightAt(x, y, m) {
  const ph = (2 * Math.PI * m) / FRAMES;
  let r = 0, g = 0, b = 0;
  for (const bl of BLOBS) {
    const bx = bl.cx + bl.px * 26 * Math.sin(ph + bl.hue * 2.1);
    const by = bl.cy + bl.py * 20 * Math.cos(ph + bl.hue * 1.7);
    const d2 = (x - bx) * (x - bx) + (y - by) * (y - by);
    const w = Math.exp(-d2 / (2 * bl.r * bl.r));   // soft gaussian falloff
    const c = PALETTE[bl.hue].rgb;
    r += w * c[0]; g += w * c[1]; b += w * c[2];
  }
  return [r, g, b];
}
/* blurred version of the light behind the glass: box-blur (radius ~6px) of the
 * fine field. This is the 毛玻璃 "透出后面虚化的光". Deterministic, pure. */
function blurredLightAt(x, y, m) {
  const R = 6; let r = 0, g = 0, b = 0, cnt = 0;
  for (let dy = -R; dy <= R; dy += 2) for (let dx = -R; dx <= R; dx += 2) {
    const v = fineLightAt(x + dx, y + dy, m);
    r += v[0]; g += v[1]; b += v[2]; cnt++;
  }
  return [r / cnt, g / cnt, b / cnt];
}
/* exported glass metrics: prove glass has (a) non-empty light behind and
 * (b) a *blurred* value distinct from the crisp fine field. */
function glassMetrics(m) {
  const probes = [[200, 150], [410, 210], [320, 110]]; // near blob centers
  let minBlur = Infinity, minDist = Infinity;
  for (const [x, y] of probes) {
    const bl = blurredLightAt(x, y, m), fi = fineLightAt(x, y, m);
    const lum = bl[0] + bl[1] + bl[2];
    const dist = Math.abs(bl[0] - fi[0]) + Math.abs(bl[1] - fi[1]) + Math.abs(bl[2] - fi[2]);
    if (lum < minBlur) minBlur = lum;
    if (dist < minDist) minDist = dist;
  }
  return { min_blur_luminance: minBlur, min_blur_vs_fine_distance: minDist };
}

/* ---- pixel buffer helpers ------------------------------------------------- */
function newBuf() { return new Uint8Array(W * H * 3); }
function px(buf, x, y, rgb) {
  if (x < 0 || x >= W || y < 0 || y >= H) return;
  const i = (y * W + x) * 3;
  buf[i] = Math.max(0, Math.min(255, rgb[0] | 0));
  buf[i + 1] = Math.max(0, Math.min(255, rgb[1] | 0));
  buf[i + 2] = Math.max(0, Math.min(255, rgb[2] | 0));
}
function addPx(buf, x, y, rgb, a) {
  if (x < 0 || x >= W || y < 0 || y >= H) return;
  const i = (y * W + x) * 3;
  buf[i]   = Math.max(0, Math.min(255, (buf[i]   + rgb[0] * a) | 0));
  buf[i+1] = Math.max(0, Math.min(255, (buf[i+1] + rgb[1] * a) | 0));
  buf[i+2] = Math.max(0, Math.min(255, (buf[i+2] + rgb[2] * a) | 0));
}
function blendPx(buf, x, y, rgb, a) {
  if (x < 0 || x >= W || y < 0 || y >= H) return;
  const i = (y * W + x) * 3;
  buf[i]   = (buf[i]   * (1 - a) + rgb[0] * a) | 0;
  buf[i+1] = (buf[i+1] * (1 - a) + rgb[1] * a) | 0;
  buf[i+2] = (buf[i+2] * (1 - a) + rgb[2] * a) | 0;
}
/* 5x7 ASCII bitmap font (documented abstraction, no bundled font dependency) */
const FONT = {
  "0":["01110","10001","10011","10101","11001","10001","01110"],
  "1":["00100","01100","00100","00100","00100","00100","01110"],
  "2":["01110","10001","00001","00010","00100","01000","11111"],
  "3":["11111","00010","00100","00010","00001","10001","01110"],
  "4":["00010","00110","01010","10010","11111","00010","00010"],
  "5":["11111","10000","11110","00001","00001","10001","01110"],
  "6":["00110","01000","10000","11110","10001","10001","01110"],
  "7":["11111","00001","00010","00100","01000","01000","01000"],
  "8":["01110","10001","10001","01110","10001","10001","01110"],
  "9":["01110","10001","10001","01111","00001","00010","01100"],
  "2":["01110","10001","00001","00010","00100","01000","11111"],
  ":":["00000","00100","00100","00000","00100","00100","00000"],
  "A":["01110","10001","10001","11111","10001","10001","10001"],
  "B":["11110","10001","10001","11110","10001","10001","11110"],
  "C":["01111","10000","10000","10000","10000","10000","01111"],
  "D":["11110","10001","10001","10001","10001","10001","11110"],
  "E":["11111","10000","10000","11110","10000","10000","11111"],
  "F":["11111","10000","10000","11110","10000","10000","10000"],
  "G":["01111","10000","10000","10111","10001","10001","01110"],
  "H":["10001","10001","10001","11111","10001","10001","10001"],
  "I":["01110","00100","00100","00100","00100","00100","01110"],
  "J":["00111","00010","00010","00010","10010","10010","01100"],
  "K":["10001","10010","10100","11000","10100","10010","10001"],
  "L":["10000","10000","10000","10000","10000","10000","11111"],
  "M":["10001","11011","10101","10101","10001","10001","10001"],
  "N":["10001","11001","10101","10011","10001","10001","10001"],
  "O":["01110","10001","10001","10001","10001","10001","01110"],
  "P":["11110","10001","10001","11110","10000","10000","10000"],
  "Q":["01110","10001","10001","10001","10101","10010","01101"],
  "R":["11110","10001","10001","11110","10100","10010","10001"],
  "S":["01111","10000","10000","01110","00001","00001","11110"],
  "T":["11111","00100","00100","00100","00100","00100","00100"],
  "U":["10001","10001","10001","10001","10001","10001","01110"],
  "V":["10001","10001","10001","10001","10001","01010","00100"],
  "W":["10001","10001","10001","10101","10101","11011","10001"],
  "X":["10001","10001","01010","00100","01010","10001","10001"],
  "Y":["10001","10001","01010","00100","00100","00100","00100"],
  "Z":["11111","00001","00010","00100","01000","10000","11111"],
  " ":["00000","00000","00000","00000","00000","00000","00000"],
  "/":["00001","00001","00010","00100","01000","10000","10000"],
  ".":["00000","00000","00000","00000","00000","01100","01100"],
  "-":["00000","00000","00000","11111","00000","00000","00000"],
};
/* 12x12 abstract CJK bitmaps for 晴 / 朗 (documented abstraction, not a font) */
const GLYPH_QING = [
 "001111111100","001000000100","001000000100","001111111100",
 "001010100100","001010100100","001111111100","001010100100",
 "001010100100","001111111100","001000000100","001111111100",
];
const GLYPH_LANG = [
 "001111111100","001010000100","001111111100","001010000100",
 "001111111100","001010000100","001111111100","001000100100",
 "001000100100","001010100100","001001000100","001111111100",
];
function drawBitmap(buf, rows, ox, oy, s, rgb, a) {
  for (let r = 0; r < rows.length; r++) {
    const row = rows[r];
    for (let c = 0; c < row.length; c++) {
      if (row[c] !== "1") continue;
      for (let dy = 0; dy < s; dy++) for (let dx = 0; dx < s; dx++)
        blendPx(buf, ox + c * s + dx, oy + r * s + dy, rgb, a);
    }
  }
}
function drawText(buf, text, ox, oy, s, rgb, a) {
  let cx = ox;
  for (const ch of text.toUpperCase()) {
    const g = FONT[ch] || FONT[" "];
    drawBitmap(buf, g, cx, oy, s, rgb, a);
    cx += 6 * s;
  }
}

/* ---- glass cards ----------------------------------------------------------
 * 3 rounded-rect cards, each with a bright 1.4px edge + a frosted interior that
 * shows the BLURRED light behind it. Entrance = sine opacity + gentle up-float. */
const CARDS = [
  { x: 40,  y: 70,  w: 250, h: 95,  layer: 0, label: "QING 26", cjk: null },
  { x: 300, y: 130, w: 290, h: 90,  layer: 1, label: "SUNRISE 06:12", cjk: null },
  { x: 90,  y: 215, w: 250, h: 100, layer: 2, label: "WEEK 7 DAYS", cjk: null },
];
function roundRectInside(x, y, rx, ry, rw, rh, rad) {
  // true if (x,y) is inside the rounded rect with corner radius rad
  if (x < rx || x > rx + rw || y < ry || y > ry + rh) return false;
  const cx = Math.min(Math.max(x, rx + rad), rx + rw - rad);
  const cy = Math.min(Math.max(y, ry + rad), ry + rh - rad);
  const dx = x - cx, dy = y - cy;
  if (x >= rx + rad && x <= rx + rw - rad) return true;
  if (y >= ry + rad && y <= ry + rh - rad) return true;
  return dx * dx + dy * dy <= rad * rad;
}
function edgeDist(x, y, rx, ry, rw, rh, rad) {
  const cx = Math.min(Math.max(x, rx + rad), rx + rw - rad);
  const cy = Math.min(Math.max(y, ry + rad), ry + rh - rad);
  const dx = x - cx, dy = y - cy;
  const inner = Math.sqrt(dx * dx + dy * dy);
  if (x >= rx + rad && x <= rx + rw - rad) return Math.min(y - ry, ry + rh - y);
  if (y >= ry + rad && y <= ry + rh - rad) return Math.min(x - rx, rx + rw - x);
  return rad - inner;
}

/* ---- the ONE highlight sweep --------------------------------------------- */
function sweepX(m) {
  if (m < SWEEP_INTERVALS[0].start || m > SWEEP_INTERVALS[0].end) return null;
  const t = (m - SWEEP_INTERVALS[0].start) / (SWEEP_INTERVALS[0].end - SWEEP_INTERVALS[0].start);
  return -120 + t * 880;   // band center x for the diagonal line x + 0.35y = s
}

/* ---- deterministic frame function ---------------------------------------- */
function renderFrame(n, seed) {
  const m = Math.min(n, HOLD);            // freeze plateau 270..299
  const buf = newBuf();
  // dark base + drifting additive light field (3 adjacent warm hues, merging)
  for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
    const [lr, lg, lb] = fineLightAt(x, y, m);
    px(buf, x, y, [BG[0] + lr * 0.55, BG[1] + lg * 0.55, BG[2] + lb * 0.55]);
  }
  // glass cards (frosted interior = blurred light behind; near layers drift faster)
  const cardE = [actionE(ACTIONS[0], m), actionE(ACTIONS[1], m), actionE(ACTIONS[2], m)];
  for (let k = 0; k < CARDS.length; k++) {
    const e = cardE[k];
    if (e <= 0) continue;
    const c = CARDS[k];
    const amp = driftAmp(c.layer);
    const ph = (2 * Math.PI * m) / FRAMES;
    const drift = Math.round(amp * Math.sin(ph + c.layer * 1.3));
    const ry = c.y + drift + Math.round((1 - e) * 6);   // gentle up-float
    const rx = c.x;
    const R = 18;
    for (let yy = Math.max(0, ry - 1); yy < Math.min(H, ry + c.h + 1); yy++) {
      for (let xx = Math.max(0, rx - 1); xx < Math.min(W, rx + c.w + 1); xx++) {
        if (!roundRectInside(xx, yy, rx, ry, c.w, c.h, R)) continue;
        const ed = edgeDist(xx, yy, rx, ry, c.w, c.h, R);
        if (ed < 1.4) {
          // 一圈细亮边 (1.4px bright border)
          blendPx(buf, xx, yy, BRIGHT_EDGE, e * 0.9);
        } else {
          // frosted glass: translucent card tint + BLURRED light behind
          const [br, bg, bb] = blurredLightAt(xx, yy, m);
          const a = 0.30 * e;
          blendPx(buf, xx, yy, [br * 0.7 + CARD_TINT[0] * 0.3,
                               bg * 0.7 + CARD_TINT[1] * 0.3,
                               bb * 0.7 + CARD_TINT[2] * 0.3], a);
        }
      }
    }
    // card label: fade-in + gentle up-float only (no scale/rotate/bounce)
    drawText(buf, c.label, rx + 16, ry + 22, 3, [250, 250, 255], e);
    // small value accents (documented abstraction)
    drawText(buf, ["26C", "06:12", "7D"][k], rx + 16, ry + 52, 2, [255, 240, 220], e);
  }
  // the ONE highlight sweep: single diagonal band, only in [180,210]
  const sx = sweepX(m);
  if (sx !== null) {
    for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
      const d = Math.abs((x + 0.35 * y) - sx);
      if (d < 14) {
        const a = 0.30 * (1 - d / 14);
        addPx(buf, x, y, SWEEP_RGB, a);
      }
    }
  }
  // App name 「晴朗」 appears AFTER the sweep (onset 216 > 210)
  const nameE = actionE(ACTIONS[4], m);
  if (nameE > 0) {
    const floatY = 250 + Math.round((1 - nameE) * 6);
    drawBitmap(buf, GLYPH_QING, 268, floatY, 4, [255, 255, 255], nameE);
    drawBitmap(buf, GLYPH_LANG, 316, floatY, 4, [255, 255, 255], nameE);
    drawText(buf, "QINGLANG", 240, floatY + 56, 2, [240, 230, 255], nameE);
  }
  return buf;
}

/* ---- minimal deterministic truecolor-RGB PNG encoder (no deps) ------------ */
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
  ihdr[8] = 8; ihdr[9] = 2;   // truecolor RGB, 8-bit
  ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0;
  const raw = Buffer.alloc((W * 3 + 1) * H);
  for (let y = 0; y < H; y++) {
    raw[y * (W * 3 + 1)] = 0;  // filter: none
    for (let x = 0; x < W * 3; x++) raw[y * (W * 3 + 1) + 1 + x] = buf[y * W * 3 + x];
  }
  const sig = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
  return Buffer.concat([
    sig, chunk("IHDR", ihdr),
    chunk("IDAT", zlib.deflateSync(raw, { level: 9 })),
    chunk("IEND", Buffer.alloc(0)),
  ]);
}
function frameFile(dir, n) {
  return path.join(dir, "frames", "f_" + String(n).padStart(4, "0") + ".png");
}
function writeFrame(dir, n, seed) {
  const data = encodePNG(renderFrame(n, seed));
  const hash = crypto.createHash("sha256").update(data).digest("hex");
  fs.writeFileSync(frameFile(dir, n), data);
  return hash;
}
const KEYFRAMES = [
  { frame: 0,   slug: "BLOBS_ONLY" },
  { frame: 45,  slug: "CARD_A" },
  { frame: 120, slug: "ALL_CARDS" },
  { frame: 180, slug: "SWEEP_ONSET" },
  { frame: 240, slug: "APP_NAME" },
  { frame: 270, slug: "END_HOLD" },
];

function main() {
  const [mode, dir, a, b] = process.argv.slice(2);
  if (!dir) { console.error("usage: render.js full|batch|range|kf <dir> [args]"); process.exit(2); }
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
          keyframe: kf.slug, frame: n, t_seconds: n / FPS,
          path: "keyframes/kf_" + String(n).padStart(4, "0") + ".png",
          sha256: crypto.createHash("sha256").update(src).digest("hex"),
        });
      }
    }
    fs.writeFileSync(path.join(dir, "frames", "frame_hashes.json"),
      JSON.stringify({ seed: SEED, fps: FPS, frames: FRAMES, resolution: [W, H],
                       renderer: "glassmorphism-raster-js@1.0.0", hashes }, null, 2));
    fs.writeFileSync(path.join(dir, "keyframe_manifest.json"),
      JSON.stringify({ card: "09", slug: "12-aurora-glass", seed: SEED, fps: FPS, keyframes: manifest }, null, 2));
    console.log(JSON.stringify({ mode: "full", frames: FRAMES, keyframes: manifest.length, ok: true }));
  } else if (mode === "batch") {
    for (const n of a.split(",").map(Number)) hashes[n] = writeFrame(dir, n, SEED);
    console.log(JSON.stringify(hashes));
  } else if (mode === "range") {
    const lo = Number(a), hi = Number(b);
    for (let n = lo; n < hi; n++) hashes[n] = writeFrame(dir, n, SEED);
    console.log(JSON.stringify(hashes));
  } else if (mode === "kf") {
    fs.mkdirSync(path.join(dir, "keyframes"), { recursive: true });
    for (const kf of KEYFRAMES) {
      const src = encodePNG(renderFrame(kf.frame, SEED));
      const dst = path.join(dir, "keyframes", "kf_" + String(kf.frame).padStart(4, "0") + ".png");
      fs.writeFileSync(dst, src);
      console.log("KF " + kf.slug + " frame=" + kf.frame + " sha256=" + crypto.createHash("sha256").update(src).digest("hex"));
    }
  } else { console.error("unknown mode " + mode); process.exit(2); }
}
if (require.main === module) main();
module.exports = {
  SEED, FPS, FRAMES, W, H, HOLD, PALETTE, BG, ACTIONS, SWEEP_INTERVALS,
  APP_NAME_ONSET, DEPTH_AMPS, CARDS, ease, actionE, driftAmp,
  fineLightAt, blurredLightAt, glassMetrics, sweepX, renderFrame, KEYFRAMES,
};
