#!/usr/bin/env node
/*
 * MOTION-04 / 10-synthwave (card 04 Synthwave 复古未来) — deterministic pure-JS raster renderer.
 *
 * renderFrame(n) is a PURE function of the frame index n and the frozen integer
 * seed. No wall clock, no RNG stream, no inter-frame mutable state. Semantic layer
 * is a pure function of beat(n); VHS artifacts (scanlines, RGB 1-2px split, one
 * dropped frame) are pure functions of n. This is what makes out-of-order /
 * pause-resume / new-process re-render byte-identical by construction and
 * empirically verifiable.
 *
 * Card 04 rules (提示词全文.md L88-96):
 *   - 地平线上一颗带横条缺口的渐变太阳 (striped gradient sun with horizontal gaps)
 *   - 地面是朝镜头滚来的透视网格, 网格线带一亮一淡两层光 (rolling perspective grid, bright+dim glow)
 *   - 标题是带高光的金属铬字, 砸下来时一道光扫过, 字不发光 (chrome title, one light sweep, NOT glowing)
 *   - 录像带质感: 扫描线, 红蓝通道错开一两个像素, 偶尔跳一帧 (scanlines, RGB split 1-2px, occasional frame skip)
 *   - 天空深紫到品红, 霓虹只用品红和青 (deep-purple->magenta sky, neon ONLY magenta+cyan)
 *   - 内容: 午夜电台片头, 铬字「午夜电台」砸下, 「FM 88.8」一笔笔亮起
 *   - 别做成: 录像带效果重到看不清字、光糊住字、紫品青以外的颜色
 *
 * Modes (same CLI contract as pilots, for determinism.js fresh-process checks):
 *   node render.js full  <dir>          -> frames/f_0000..0299.png + keyframes/ + frame_hashes.json
 *   node render.js batch <dir> <n,...>  -> frames/f_<n>.png for listed indices, prints JSON hash map
 *   node render.js range <dir> <a> <b>  -> frames/f_<a..b-1>.png, prints JSON hash map
 */
"use strict";
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");
const crypto = require("crypto");

const SEED = 20261115;
const FPS = 30;
const FRAMES = 300;
const W = 640, H = 360;
const BEAT = 15;            // 120 BPM at 30 fps
const HORIZON = 200;        // sky/ground divide
const SKIP_FRAME = 256;     // declared VHS "跳一帧": frame 256 repeats frame 255

// ---- finite palette --------------------------------------------------------
const MAGENTA = [255, 45, 149];   // neon accent 1 (allowed)
const CYAN    = [22, 224, 255];   // neon accent 2 (allowed)
const DIM_CYAN = [10, 90, 120];   // dim grid glow (dark cyan, allowed)
const INK     = [20, 6, 31];      // dark purple plate/ground
const GROUND  = [26, 6, 48];      // ground base
const WHITE   = [244, 233, 255];  // chrome highlight / light sweep (near-gray)

function lerp(a, b, t) { return Math.round(a + (b - a) * t); }
function gradient(from, to, steps) {
  const out = [];
  for (let i = 0; i < steps; i++) {
    const t = steps === 1 ? 0 : i / (steps - 1);
    out.push([lerp(from[0], to[0], t), lerp(from[1], to[1], t), lerp(from[2], to[2], t)]);
  }
  return out;
}
// sky: deep purple -> magenta (L92 "天空深紫到品红")
const SKY = gradient([42, 10, 74], [192, 30, 120], 16);
// sun: yellow -> magenta (L92 "渐变太阳")
const SUN = gradient([255, 216, 107], [255, 45, 149], 16);
// chrome vertical ramp (metal band, dark->light->highlight->dark); near-gray only
const CHROME = [
  [60, 60, 85], [110, 110, 140], [190, 190, 215],
  WHITE, [150, 150, 180], [70, 70, 100],
];

// ---- deterministic RGB pixel buffer ---------------------------------------
function newBuf() { return Buffer.alloc(W * H * 3); }   // all zeros (black); overwritten below
function setpx(buf, x, y, c) {
  if (x < 0 || x >= W || y < 0 || y >= H) return;
  const i = (y * W + x) * 3;
  buf[i] = c[0]; buf[i + 1] = c[1]; buf[i + 2] = c[2];
}
function hline(buf, x0, x1, y, c) { for (let x = x0; x <= x1; x++) setpx(buf, x, y, c); }
function vline(buf, x, y0, y1, c) { for (let y = y0; y <= y1; y++) setpx(buf, x, y, c); }
function rect(buf, x0, y0, x1, y1, c) {
  for (let y = y0; y <= y1; y++) for (let x = x0; x <= x1; x++) setpx(buf, x, y, c);
}
function line(buf, x0, y0, x1, y1, c) { // Bresenham
  let dx = Math.abs(x1 - x0), sx = x0 < x1 ? 1 : -1;
  let dy = -Math.abs(y1 - y0), sy = y0 < y1 ? 1 : -1;
  let err = dx + dy, x = x0, y = y0;
  for (;;) {
    setpx(buf, x, y, c);
    if (x === x1 && y === y1) break;
    const e2 = 2 * err;
    if (e2 >= dy) { err += dy; x += sx; }
    if (e2 <= dx) { err += dx; y += sy; }
  }
}

// ---- abstract geometric glyph bitmaps (no font; documented abstraction) ----
// 「午夜电台」 9x9 each; "FM 88.8" 5x7 (+ 3x7 dot). These are geometric stand-ins,
// NOT a real bundled typeface (same honest disclosure as pilot MOTION-06 「分」).
const G_WU = [
  "....#....", "...###...", "..##.##..", ".##...##.", "#########",
  "....#....", "....#....", "....#....", "....#....",
];
const G_YE = [
  "....#....", ".#######.", "..#...#..", ".##...##.", "##..#..##",
  "...###...", "..#####..", ".##...##.", "##.....##",
];
const G_DIAN = [
  "..#####..", "..#...#..", "..#...#..", "..#####..", "..#...#..",
  "..#...#..", "..#####..", "......#..", "....###..",
];
const G_TAI = [
  "...###...", "..#####..", ".##...##.", "....#....", "..#####..",
  "..#...#..", "..#...#..", "..#####..", ".........",
];
const GF = ["#####", "#....", "#....", "####.", "#....", "#....", "#...."];
const GM = ["#...#", "##.##", "#.#.#", "#...#", "#...#", "#...#", "#...#"];
const G8 = [".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."];
const GDOT = ["...", "...", "...", "...", "...", "...", ".#."];
const TITLE_CHARS = [G_WU, G_YE, G_DIAN, G_TAI];
const TITLE_BOX = { x0: 160, y0: 106, x1: 480, y1: 190 }; // chrome nameplate
const FM_Y = 214, FM_SC = 5, FM_X = 232;
// FM cells: F,M,(space),8,8,.,8 with stroke-group 1/2/3 ("一笔笔亮起")
const FM_CELLS = [
  { g: GF, group: 1, w: 5 }, { g: GM, group: 1, w: 5 },
  { g: null, group: 1, w: 3 },                 // space
  { g: G8, group: 2, w: 5 }, { g: G8, group: 2, w: 5 },
  { g: GDOT, group: 3, w: 3 }, { g: G8, group: 3, w: 5 },
];

// ---- beat schedule (pre-registered in beat_schedule.md BEFORE render) ------
// beatOf(n) is constant within each 15-frame window; >=18 clamps to 18 (freeze).
function beatOf(n) { return Math.min(Math.floor(n / BEAT), 18); }
// state(b): every actor is a step function of the beat; s>=18 pinned (freeze).
function state(b) {
  const s = Math.min(b, 18);
  return {
    sunStep:   (s <= 4 ? s : (s >= 10 ? 5 : 4)),
    gridOn:    s >= 5,
    gridTier:  s >= 6,
    gridPhase: (s >= 7 ? 1 : 0) + (s >= 8 ? 1 : 0) + (s >= 9 ? 1 : 0),
    title:     s >= 11,
    sweep:     s === 11,               // ONE light sweep (L92 "一道光扫过")
    fm:        Math.min(Math.max(s - 12, 0), 3),
    vhs:       s >= 16,
    border:    s >= 18,               // final ident card = freeze onset
    hold:      s >= 18,
  };
}

// ---- semantic layer (NO VHS) — pure function of beat(n) -------------------
function drawSun(buf, step) {
  const cx = W / 2, R = 70;
  const cy = 210 - step * 16;         // rises from below horizon to 130
  for (let y = cy - R; y <= Math.min(cy + R, HORIZON - 1); y++) {
    for (let x = cx - R; x <= cx + R; x++) {
      if ((x - cx) * (x - cx) + (y - cy) * (y - cy) > R * R) continue;
      const t = (y - (cy - R)) / (2 * R);
      const idx = Math.max(0, Math.min(SUN.length - 1, Math.floor(t * (SUN.length - 1))));
      setpx(buf, x, y, SUN[idx]);
    }
  }
  // 横条缺口: horizontal cut-out gaps, height increasing toward the bottom.
  for (let k = 0; k < 7; k++) {
    const top = cy + k * 12, hgt = 3 + k * 2;
    for (let y = top; y < top + hgt && y < HORIZON; y++) {
      for (let x = cx - R; x <= cx + R; x++) {
        if ((x - cx) * (x - cx) + (y - cy) * (y - cy) > R * R) continue;
        const skyIdx = Math.max(0, Math.min(SKY.length - 1,
          Math.floor((y / (HORIZON - 1)) * (SKY.length - 1))));
        setpx(buf, x, y, SKY[skyIdx]);   // show sky through the gap
      }
    }
  }
}
function drawGrid(buf, phase, tier) {
  const off = (phase * 6) % 18;       // rolling toward camera
  for (let i = 1; i <= 12; i++) {
    const y = HORIZON + Math.floor((H - HORIZON) * Math.pow(i / 12, 1.7)) + off;
    if (y < HORIZON || y >= H) continue;
    hline(buf, 0, W - 1, y, CYAN);                                  // bright tier
    if (tier) hline(buf, 0, W - 1, Math.min(H - 1, y + 3), DIM_CYAN); // dim tier
  }
  for (let j = -8; j <= 8; j++) {
    const xb = Math.round(W / 2 + j * 44);
    line(buf, W / 2, HORIZON, xb, H - 1, CYAN);
    if (tier) line(buf, W / 2 + 3, HORIZON, xb + 3, H - 1, DIM_CYAN);
  }
}
function drawTitle(buf, sweep) {
  rect(buf, TITLE_BOX.x0, TITLE_BOX.y0, TITLE_BOX.x1, TITLE_BOX.y1, INK); // dark nameplate
  const SC = 8, gap = 8;
  const totalW = 4 * 9 * SC + 3 * gap;
  const TX = Math.round((W - totalW) / 2), TY = 110;
  for (let ci = 0; ci < 4; ci++) {
    const ox = TX + ci * (9 * SC + gap), rows = TITLE_CHARS[ci];
    for (let j = 0; j < 9; j++) for (let i = 0; i < 9; i++) {
      if (rows[j][i] !== "#") continue;
      const idx = Math.max(0, Math.min(CHROME.length - 1,
        Math.floor((j / 9) * (CHROME.length - 1))));
      for (let dy = 0; dy < SC; dy++) for (let dx = 0; dx < SC; dx++)
        setpx(buf, ox + i * SC + dx, TY + j * SC + dy, CHROME[idx]);
    }
  }
  if (sweep) { // single white light sweep across the title (beat 11 only)
    for (let x = TITLE_BOX.x0 - 10; x < TITLE_BOX.x1 + 10; x++) {
      const y = TITLE_BOX.y0 + Math.floor((x - (TITLE_BOX.x0 - 10)) * 0.22);
      for (let d = 0; d < 4; d++) setpx(buf, x, y + d, WHITE);
    }
  }
}
function drawFM(buf, fm) {
  let x = FM_X;
  for (const cell of FM_CELLS) {
    const cw = cell.w * FM_SC;
    if (cell.g && cell.group <= fm) {
      for (let j = 0; j < cell.g.length; j++) for (let i = 0; i < cell.g[j].length; i++) {
        if (cell.g[j][i] !== "#") continue;
        for (let dy = 0; dy < FM_SC; dy++) for (let dx = 0; dx < FM_SC; dx++)
          setpx(buf, x + i * FM_SC + dx, FM_Y + j * FM_SC + dy, CYAN);
      }
    }
    x += cw + 6;
  }
}
function drawBorder(buf) { // final ident card: magenta outer + cyan inner neon frame
  rect(buf, 0, 0, W - 1, 3, MAGENTA);
  rect(buf, 0, H - 4, W - 1, H - 1, MAGENTA);
  rect(buf, 0, 0, 3, H - 1, MAGENTA);
  rect(buf, W - 4, 0, W - 1, H - 1, MAGENTA);
  rect(buf, 6, 6, W - 7, 7, CYAN);
  rect(buf, 6, H - 8, W - 7, H - 7, CYAN);
  rect(buf, 6, 6, 7, H - 7, CYAN);
  rect(buf, W - 8, 6, W - 7, H - 7, CYAN);
}
function semanticFrame(n) {
  const s = state(beatOf(n));
  const buf = newBuf();
  for (let y = 0; y < HORIZON; y++) {
    const idx = Math.max(0, Math.min(SKY.length - 1,
      Math.floor((y / (HORIZON - 1)) * (SKY.length - 1))));
    for (let x = 0; x < W; x++) setpx(buf, x, y, SKY[idx]);
  }
  for (let y = HORIZON; y < H; y++) for (let x = 0; x < W; x++) setpx(buf, x, y, GROUND);
  drawSun(buf, s.sunStep);
  if (s.gridOn) { drawGrid(buf, s.gridPhase, s.gridTier); hline(buf, 0, W - 1, HORIZON, CYAN); }
  if (s.title) drawTitle(buf, s.sweep);
  if (s.fm > 0) drawFM(buf, s.fm);
  if (s.border) drawBorder(buf);
  return buf;
}

// ---- VHS layer (pure functions of n) ---------------------------------------
function applyScanlines(buf, vn) {
  const out = Buffer.from(buf);
  const factor = (vn % 2 === 0) ? 0.72 : 0.80;
  for (let y = 0; y < H; y += 2) {
    for (let x = 0; x < W; x++) {
      const i = (y * W + x) * 3;
      out[i] = Math.floor(out[i] * factor);
      out[i + 1] = Math.floor(out[i + 1] * factor);
      out[i + 2] = Math.floor(out[i + 2] * factor);
    }
  }
  return out;
}
function applyRGBSplit(buf, shift) {
  const out = Buffer.from(buf);
  for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
    const i = (y * W + x) * 3;
    const xr = Math.min(W - 1, x + shift), xb = Math.max(0, x - shift);
    out[i] = buf[(y * W + xr) * 3];         // R shifted +shift (1-2 px)
    out[i + 2] = buf[(y * W + xb) * 3 + 2]; // B shifted -shift
    // G stays at x
  }
  return out;
}
function renderFrame(n) {
  if (n === SKIP_FRAME) n = SKIP_FRAME - 1;  // VHS "跳一帧": 256 repeats 255
  const semi = semanticFrame(n);
  const active = state(beatOf(n)).vhs;
  if (!active) return semi;
  const vn = n >= 270 ? 270 : n;             // freeze VHS params at frame 270
  const s1 = applyScanlines(semi, vn);
  const shift = 1 + (vn % 2);                // 1-2 px (L92 "错开一两个像素")
  return applyRGBSplit(s1, shift);
}

// ---- palette guard (art layer only; VHS chromatic fringe is a declared transform) ----
function forbiddenHue(r, g, b) {
  const green = g > r + 40 && g > b + 40;                     // green accent
  const orangeRed = r > 180 && b < 100 && (r - g) > 70 && g < 170; // orange / pure red
  const pureBlue = b > r + 80 && b > g + 80 && r < 110;      // pure blue accent
  return green || orangeRed || pureBlue;
}
function paletteViolations(buf) {
  let n = 0;
  for (let p = 0; p < W * H; p++) {
    const i = p * 3;
    if (forbiddenHue(buf[i], buf[i + 1], buf[i + 2])) n++;
  }
  return n;
}
function eqColor(buf, x, y, c) {
  const i = (y * W + x) * 3;
  return buf[i] === c[0] && buf[i + 1] === c[1] && buf[i + 2] === c[2];
}

// ---- minimal deterministic PNG encoder (RGB truecolor, color type 2) ------
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
  ihdr[8] = 8;   // bit depth
  ihdr[9] = 2;   // color type 2 = truecolor RGB
  ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0;
  const raw = Buffer.alloc((W * 3 + 1) * H);
  for (let y = 0; y < H; y++) {
    raw[y * (W * 3 + 1)] = 0; // filter: none
    buf.copy(raw, y * (W * 3 + 1) + 1, y * W * 3, (y + 1) * W * 3);
  }
  const sig = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
  return Buffer.concat([
    sig,
    chunk("IHDR", ihdr),
    chunk("IDAT", zlib.deflateSync(raw, { level: 9 })),
    chunk("IEND", Buffer.alloc(0)),
  ]);
}
function frameFile(dir, n) {
  return path.join(dir, "frames", "f_" + String(n).padStart(4, "0") + ".png");
}
function writeFrame(dir, n) {
  const data = encodePNG(renderFrame(n));
  const hash = crypto.createHash("sha256").update(data).digest("hex");
  fs.writeFileSync(frameFile(dir, n), data);
  return hash;
}

const KEYFRAMES = [
  { frame: 0,   slug: "VHS_NOISE" },
  { frame: 60,  slug: "SUN_RISE" },
  { frame: 120, slug: "GRID_FLY" },
  { frame: 165, slug: "TITLE_SLAM" },
  { frame: 225, slug: "FM_888" },
  { frame: 270, slug: "HOLD_VHS" },
];

function main() {
  const [mode, dir, a, b] = process.argv.slice(2);
  if (!dir) { console.error("usage: render.js full|batch|range <dir> [args]"); process.exit(2); }
  fs.mkdirSync(path.join(dir, "frames"), { recursive: true });
  let hashes = {};
  if (mode === "full") {
    fs.mkdirSync(path.join(dir, "keyframes"), { recursive: true });
    const manifest = [];
    for (let n = 0; n < FRAMES; n++) {
      hashes[n] = writeFrame(dir, n);
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
                       renderer: "synthwave-raster-js@1.0.0", hashes }, null, 2));
    fs.writeFileSync(path.join(dir, "keyframe_manifest.json"),
      JSON.stringify({ card: "04", slug: "10-synthwave", seed: SEED, fps: FPS, keyframes: manifest }, null, 2));
    console.log(JSON.stringify({ mode: "full", frames: FRAMES, keyframes: manifest.length, ok: true }));
  } else if (mode === "batch") {
    const list = a.split(",").map(Number);
    for (const n of list) hashes[n] = writeFrame(dir, n);
    console.log(JSON.stringify(hashes));
  } else if (mode === "range") {
    const lo = Number(a), hi = Number(b);
    for (let n = lo; n < hi; n++) hashes[n] = writeFrame(dir, n);
    console.log(JSON.stringify(hashes));
  } else { console.error("unknown mode " + mode); process.exit(2); }
}
if (require.main === module) main();

// Export the REAL shipped semantics for verify_style.js (verifier diffs the actual
// functions, not a copy, so renderer/schedule divergence is caught).
module.exports = {
  SEED, FPS, FRAMES, W, H, BEAT, HORIZON, SKIP_FRAME,
  MAGENTA, CYAN, DIM_CYAN, INK, GROUND, WHITE, CHROME, SKY, SUN,
  TITLE_BOX, TITLE_CHARS, FM_CELLS, FM_Y, FM_SC, FM_X,
  beatOf, state, semanticFrame, renderFrame, applyScanlines, applyRGBSplit,
  forbiddenHue, paletteViolations, eqColor, encodePNG, newBuf, setpx,
};
