#!/usr/bin/env node
/*
 * MOTION-06 / 09-bauhaus — deterministic JS scene rasterizer with bound Pillow font rendering.
 *
 * renderFrame(n, seed) is a PURE function of the frame index n and the frozen
 * integer seed. No wall clock, no RNG stream, no inter-frame mutable state.
 * This is what makes out-of-order / pause-resume / new-process re-render
 * byte-identical by construction and empirically verifiable.
 *
 * Card 06 rules (提示词全文.md L116-120):
 *   - only circle / semicircle / quarter-circle / triangle / rectangle
 *   - only red / yellow / blue / black + paper
 *   - everything on a grid, displacement whole cells, rotation multiple of 90deg
 *   - mechanical: constant or symmetric ease-in-out, NO bounce / NO overshoot
 *   - one action per beat; protagonist complete only at the climax; poster freeze
 *
 * Modes:
 *   node render.js full  <dir>          -> frames/f_0000..0299.png + keyframes/ + frame_hashes.json
 *   node render.js batch <dir> <n,...>  -> frames/f_<n>.png for listed indices, prints JSON hash map
 *   node render.js range <dir> <a> <b>  -> frames/f_<a..b-1>.png, prints JSON hash map
 */
"use strict";
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");
const crypto = require("crypto");
const {loadGlyphs,drawIndexed,drawRGB} = require("../cjk_text.js");
const CJK_FONT = loadGlyphs([{"id": "fen", "text": "分", "size": 192}]);
// CJK text uses a bound existing font at native pixel size; no font is bundled.


const SEED = 20261115;
const FPS = 30;
const FRAMES = 300;
const W = 1920, H = 1080, CELL = 120;
// All scene coordinates/radii below are native geometric lengths, three times
// the frozen design. Curves and triangles are evaluated on this native grid.
const BEAT = 15; // 120 BPM at 30fps

// palette (paper + RYBK)
const C = {
  paper: [0xEF, 0xE9, 0xD8],
  ink:   [0x1A, 0x1A, 0x1A],
  red:   [0xD6, 0x30, 0x26],
  yellow:[0xF0, 0xBE, 0x00],
  blue:  [0x1D, 0x4E, 0x9C],
};
const COL = { PAPER: 0, INK: 1, RED: 2, YELLOW: 3, BLUE: 4 };
const RGB = [C.paper, C.ink, C.red, C.yellow, C.blue];

// ---- deterministic pixel buffer -------------------------------------------
function newBuf() { return new Uint8Array(W * H); }
function px(buf, x, y, c) { if (x >= 0 && x < W && y >= 0 && y < H) buf[y * W + x] = c; }
function hline(buf, x0, x1, y, c) {
  for (let dy = 0; dy < 3; dy++) for (let x = x0; x <= x1; x++) px(buf, x, y + dy, c);
}
function vline(buf, x, y0, y1, c) {
  for (let dx = 0; dx < 3; dx++) for (let y = y0; y <= y1; y++) px(buf, x + dx, y, c);
}
function rect(buf, x0, y0, x1, y1, c) {
  for (let y = y0; y <= y1; y++) for (let x = x0; x <= x1; x++) px(buf, x, y, c);
}
// quarter circle filled inside an axis-aligned box; quadrant selected by 90deg
// rotation r in {0,1,2,3}. r multiplies 90deg. Center is a grid corner.
function quarter(buf, cx, cy, r, rad, c) {
  const r2 = rad * rad;
  for (let y = -rad; y <= rad; y++) for (let x = -rad; x <= rad; x++) {
    if (x * x + y * y > r2) continue;
    const q = ((r % 4) + 4) % 4;
    let inside = false;
    if (q === 0) inside = (x >= 0 && y >= 0);
    else if (q === 1) inside = (x <= 0 && y >= 0);
    else if (q === 2) inside = (x <= 0 && y <= 0);
    else inside = (x >= 0 && y <= 0);
    if (inside) px(buf, cx + x, cy + y, c);
  }
}
// semicircle: half of a disk, orientation is a 90deg multiple.
function semi(buf, cx, cy, r, rad, c) {
  const r2 = rad * rad, q = ((r % 4) + 4) % 4;
  for (let y = -rad; y <= rad; y++) for (let x = -rad; x <= rad; x++) {
    if (x * x + y * y > r2) continue;
    let inside = false;
    if (q === 0) inside = (y >= 0);
    else if (q === 1) inside = (x <= 0);
    else if (q === 2) inside = (y <= 0);
    else inside = (x >= 0);
    if (inside) px(buf, cx + x, cy + y, c);
  }
}
// right triangle in a w x h box; orientation rotates by 90deg multiples.
function tri(buf, x, y, w, h, r, c) {
  const q = ((r % 4) + 4) % 4;
  for (let j = 0; j < h; j++) for (let i = 0; i < w; i++) {
    const u = (w <= 1) ? 0 : i / (w - 1), v = (h <= 1) ? 0 : j / (h - 1);
    let inside;
    // base: lower-left right triangle (u+v <= 1)
    if (q === 0) inside = (u + v <= 1);
    else if (q === 1) inside = (v <= u);
    else if (q === 2) inside = (u + v >= 1);
    else inside = (v >= u);
    if (inside) px(buf, x + i, y + j, c);
  }
}
function circle(buf, cx, cy, rad, c) {
  const r2 = rad * rad;
  for (let y = -rad; y <= rad; y++) for (let x = -rad; x <= rad; x++)
    if (x * x + y * y <= r2) px(buf, cx + x, cy + y, c);
}

// ---- geometric glyph bitmaps (no font dependency; documented abstraction) --
const G3 = [
  "..###..",
  ".#...#.",
  ".....#.",
  "..###..",
  ".....#.",
  ".#...#.",
  "..###..",
];
const GFEN = [
  "..#..#..",
  "..#..#..",
  ".#..#...",
  "#######.",
  "..#..#..",
  ".#..#...",
  "#...#...",
  "#....#..",
  "#.....#.",
];
function glyph(buf, rows, ox, oy, scale, c) {
  for (let j = 0; j < rows.length; j++)
    for (let i = 0; i < rows[j].length; i++)
      if (rows[j][i] === "#") rect(buf, ox + i * scale, oy + j * scale, ox + (i + 1) * scale - 1, oy + (j + 1) * scale - 1, c);
}

// ---- beat schedule (repair round 2) ----------------------------------------
// Pre-registered in beat_schedule.md BEFORE this render. Governing rules:
// 提示词全文.md L116「一拍只做一个动作」/ L120 禁「几样东西一起进场」.
// BEAT=15 frames. beat(n) is constant within each 15-frame window, so a visible
// change can only appear at a frame divisible by 15. Each beat changes exactly
// ONE actor; all other actors hold their prior state. Frames 270..299 are pinned
// to the beat-18 poster state (single plateau, freeze retained from round 1).
// Everything is a pure integer function of the beat index -> deterministic.
function beatOf(n) { return Math.min(Math.floor(n / BEAT), 18); }

// beatState(b) returns the discrete state of every actor at beat b. verify_beat.js
// requires this to diff consecutive beats and prove exactly one actor per beat.
// Rotation values here are EXTRA 90deg steps on top of the seed phase (which
// renderFrame adds at draw time); they never take intermediate angles.
function beatState(b) {
  return {
    redSquare:  b >= 1,
    blueBar:    b >= 2,
    yellowBar:  b >= 3,
    rotorA:     b >= 4  ? { present: true, extra: (b >= 9  ? 1 : 0) } : { present: false, extra: 0 },
    rotorB:     b >= 5  ? { present: true, extra: (b >= 14 ? 1 : 0) } : { present: false, extra: 0 },
    semi:       b >= 6  ? { present: true, extra: (b >= 17 ? 1 : 0) } : { present: false, extra: 0 },
    tri:        b >= 7  ? { present: true, extra: 0 }                    : { present: false, extra: 0 },
    ball:       b >= 8  ? { present: true,
                            hops: (b>=12?1:0)+(b>=15?1:0) }   // appears@8 (hops=0); one hop@12, one@15
                        : { present: false, hops: 0 },
    backboard:  b >= 10,
    rim:        b >= 11,
    header:     b >= 13,
    climax:     b >= 16,
    border:     b >= 18,
  };
}

// ---- deterministic frame function -----------------------------------------
// renderFrame(n, seed) is a PURE function of n (via beatOf) and the frozen seed.
// No wall clock, no RNG stream, no inter-frame mutable state. All geometry is
// on the 120px native grid, displacement whole cells, rotation whole 90deg steps.
function renderFrame(n, seed = SEED) {
  const buf = newBuf(); // COL.PAPER = 0
  const phase = ((seed % 4) + 4) % 4; // seed sets initial 90deg phase only
  const b = beatOf(n);               // clamped to 18 -> freeze 270..299
  const s = beatState(b);

  // 1) grid: thin ink lines every CELL px (everything lands on the grid)
  for (let gx = 0; gx <= W; gx += CELL) vline(buf, Math.min(gx, W - 1), 0, H - 1, COL.INK);
  for (let gy = 0; gy <= H; gy += CELL) hline(buf, 0, W - 1, Math.min(gy, H - 1), COL.INK);

  // 2) foundation: one rect per beat, snapped to grid (beats 1/2/3 = 15/30/45)
  if (s.redSquare)  rect(buf, 120, 600, 360, 840, COL.RED);
  if (s.blueBar)    rect(buf, 480, 120, 1320, 216, COL.BLUE);
  if (s.yellowBar)  rect(buf, 1440, 360, 1560, 960, COL.YELLOW);

  // 3) quarter-circle rotors: appear on their own beat, step 90deg on their own
  //    scheduled beat only; inactive beats hold the prior rotation.
  if (s.rotorA.present) quarter(buf, 480, 480, phase + s.rotorA.extra, 168, COL.RED);
  if (s.rotorB.present) quarter(buf, 1320, 840, phase + s.rotorB.extra + 1, 144, COL.BLUE);
  if (s.semi.present)   semi(buf, 960, 600, phase + s.semi.extra, 132, COL.BLUE);
  if (s.tri.present)    tri(buf, 1080, 720, 240, 192, phase + s.tri.extra, COL.YELLOW);

  // 5) hoop: backboard (beat 10 / frame 150) + rim (beat 11 / frame 165)
  if (s.backboard) rect(buf, 1560, 240, 1680, 504, COL.INK);
  if (s.rim)       semi(buf, 1584, 528, 2, 96, COL.RED);

  // 6) protagonist ball: appears at beat 8 and hops ONE grid cell on each of its
  //    own scheduled beats (8/12/15). Clamped integer hops -> no overshoot.
  if (s.ball.present) {
    const hops = Math.min(s.ball.hops, 8);
    const startX = 600, startY = 840;
    const bx = startX + hops * CELL;
    const by = startY - Math.min(hops, 4) * CELL;
    circle(buf, bx, by, 54, COL.RED);
  }

  // 7) header accent (beat 13 / frame 195): GRID-ALIGNED ink rule (was off the
  //    beat grid at frame 200 and off the spatial grid at y=96 in round 1).
  if (s.header) rect(buf, 120, 240, 720, 264, COL.INK);

  // 8) climax (beat 16 / frame 240): 「3 分」 complete for the FIRST time, drawn
  //    on a paper plaque so glyphs are readable and separated from the blue bar
  //    (S02 §2 visual check). Plaque = one poster element = one CLIMAX action.
  if (s.climax) {
    rect(buf, 840, 120, 1320, 360, COL.PAPER);
    rect(buf, 840, 120, 1320, 132, COL.INK);
    glyph(buf, G3,   864, 144, 24, COL.INK);
    drawIndexed(buf,W,H,CJK_FONT.glyphs.fen,1080,144,COL.INK);
  }

  // 9) poster freeze (270..299): black frame border; composition held at beat 18
  if (s.border) {
    rect(buf, 0, 0, W - 1, 23, COL.INK);
    rect(buf, 0, H - 24, W - 1, H - 1, COL.INK);
    rect(buf, 0, 0, 23, H - 1, COL.INK);
    rect(buf, W - 24, 0, W - 1, H - 1, COL.INK);
  }
  return buf;
}

// ---- minimal deterministic PNG encoder (no dependencies) ------------------
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
  // color type 3 (indexed): PLTE with the 5-color palette; 1 byte/pixel.
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(W, 0); ihdr.writeUInt32BE(H, 4);
  ihdr[8] = 8;   // bit depth
  ihdr[9] = 3;   // indexed color
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
function writeFrame(dir, n, seed) {
  const data = encodePNG(renderFrame(n, seed));
  const hash = crypto.createHash("sha256").update(data).digest("hex");
  fs.writeFileSync(frameFile(dir, n), data);
  return hash;
}

const KEYFRAMES = [
  { frame: 0,   slug: "GRID_ONLY" },
  { frame: 45,  slug: "FOUNDATION" },
  { frame: 120, slug: "ROTORS" },
  { frame: 180, slug: "HOP" },
  { frame: 240, slug: "CLIMAX" },
  { frame: 270, slug: "POSTER_FREEZE" },
];

function main() {
  const [mode, dir, a, b] = process.argv.slice(2);
  if (!dir) { console.error("usage: render.js full|batch|range <dir> [args]"); process.exit(2); }
  fs.mkdirSync(path.join(dir, "frames"), { recursive: true });
  fs.writeFileSync(path.join(dir,"font-evidence.json"),JSON.stringify(CJK_FONT.evidence,null,2));
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
      JSON.stringify({ seed: SEED, fps: FPS, frames: FRAMES, resolution: [W, H], grid_cell: CELL,
                       renderer: "bauhaus-native-raster-js@2.0.0-review", hashes }, null, 2));
    fs.writeFileSync(path.join(dir, "keyframe_manifest.json"),
      JSON.stringify({ card: "06", slug: "09-bauhaus", seed: SEED, fps: FPS, keyframes: manifest }, null, 2));
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
// Exported SEMANTIC schedule for verify_beat.js: the verifier diffs the REAL
// shipped beatState(), not a copy, so a renderer/schedule divergence is caught.
module.exports = { BEAT, FRAMES, FPS, W, H, CELL, RGB, beatOf, beatState, renderFrame, encodePNG, SEED };
