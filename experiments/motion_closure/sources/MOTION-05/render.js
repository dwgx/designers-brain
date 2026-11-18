#!/usr/bin/env node
/*
 * MOTION-05 / 08-morph — deterministic JS scene rasterizer with bound Pillow font rendering (形变 / MORPH).
 *
 * Card rules honored (origin/提示词全文.md L104-108):
 *   - 一个形状连续变成另一个: ONE analytic star-shaped outline r(theta)>0 per frame,
 *     NOT a crossfade. The outline geometry is recomputed every frame.
 *   - 轮廓从头到尾连着、不打结: r(theta)>0 for ALL theta => the polygon
 *     (cx + r cos t, cy - r sin t) with strictly increasing t is a SIMPLE closed
 *     star-shaped curve (connected, non-self-intersecting). Squash/rotation are
 *     affine transforms that preserve simplicity.
 *   - 中间每一帧都是干净的形状: every intermediate frame is a single clean shape.
 *   - 两个复杂形状之间先收成圆或胶囊，再展开: each A->B morph goes
 *     A -> CIRCLE (mediator, r=0.60R) -> B.
 *   - 变的时候带一点挤压拉伸和小角度旋转，像有弹性: sx/sy + small rot, all
 *     vanish at morph endpoints so each morph starts/ends on a clean shape.
 *   - 每次变形卡在拍子上完成: every morph is 60 frames (4 beats) and completes
 *     exactly on a beat boundary (90/165/240); 120 BPM = 15 frames/beat.
 *   - 背景色跟着换: flat full-frame color block changes at beat boundaries
 *     30/105/180/270 (BG0..BG4), a clean color-block change, not a dissolve.
 *   - 前后两个形状在意思上有关系: BULB->BUBBLE->PENCIL->STAR (idea->speak->
 *     write->spark), the card's literal 内容 chain.
 *
 * renderFrame(n) is a PURE function of n. No wall clock, no RNG stream, no
 * inter-frame mutable state. Frames 270..299 are clamped to the frame-270
 * FINALE state (single true freeze plateau — avoids the MOTION-06 r1 defect).
 *
 * Modes: full | batch <list> | range <lo> <hi>; <dir> is the first arg in the
 * pilot's determinism.js protocol (fresh `node render.js <mode> <dir> ...`).
 */
"use strict";
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");
const crypto = require("crypto");
const {loadGlyphs,drawIndexed,drawRGB} = require("../cjk_text.js");
const CJK_FONT = loadGlyphs([{"id": "title", "text": "灵感", "size": 120}]);
// CJK text uses a bound existing font at native pixel size; no font is bundled.


const SEED = 20261115;
const FPS = 30;
const FRAMES = 300;
const W = 1920, H = 1080;   // native raster allocation; no low-res image exists
const BEAT = 15;            // 120 BPM at 30 fps
const CX = 960, CY = 540;
const R = 276;              // 92 logical units, mapped before rasterization
const N = 288;              // denser angular geometry, unchanged analytic shape
const MEDIATOR = 0.60 * R;  // circle mediator radius
const FREEZE_AT = 270;

// ---- palette (indexed color, 1 byte/pixel) --------------------------------
// 5 flat background blocks + shape cream + dark rim + glyph accent.
const COL = { BG0: 0, BG1: 1, BG2: 2, BG3: 3, BG4: 4,
              SHAPE: 5, OUTLINE: 6, ACCENT: 7 };
const RGB = [
  [26, 26, 58],    // BG0 deep indigo
  [14, 77, 92],    // BG1 teal
  [138, 75, 30],   // BG2 amber
  [91, 42, 107],   // BG3 plum
  [16, 26, 58],    // BG4 midnight (finale)
  [244, 234, 210], // SHAPE cream
  [40, 30, 50],    // OUTLINE dark rim
  [240, 190, 60],  // ACCENT gold (灵感 glyphs)
];

// ---- deterministic pixel buffer helpers ----------------------------------
function newBuf(fill) { const b = new Uint8Array(W * H); b.fill(fill); return b; }
function px(buf, x, y, c) { if (x >= 0 && x < W && y >= 0 && y < H) buf[y * W + x] = c; }
function hline(buf, x0, x1, y, c) { for (let x = x0; x <= x1; x++) px(buf, x, y, c); }

// Even-odd scanline fill of a simple polygon (integer vertex coords).
// A star-shaped polygon (r>0, monotone angle) crosses each scanline exactly
// twice, so this yields ONE connected filled region (a "clean shape").
function fillPolygon(buf, pts, c) {
  const n = pts.length;
  let minY = Infinity, maxY = -Infinity;
  for (const p of pts) { if (p.y < minY) minY = p.y; if (p.y > maxY) maxY = p.y; }
  const y0 = Math.max(0, Math.floor(minY)), y1 = Math.min(H - 1, Math.ceil(maxY));
  for (let y = y0; y <= y1; y++) {
    const xs = [];
    for (let i = 0; i < n; i++) {
      const a = pts[i], b = pts[(i + 1) % n];
      const sampleY = y + 0.5;
      if ((a.y <= sampleY && b.y > sampleY) || (b.y <= sampleY && a.y > sampleY)) {
        const t = (sampleY - a.y) / (b.y - a.y);
        xs.push(a.x + t * (b.x - a.x));
      }
    }
    xs.sort((p, q) => p - q);
    for (let k = 0; k + 1 < xs.length; k += 2) {
      hline(buf, Math.ceil(xs[k] - 0.5), Math.floor(xs[k + 1] - 0.5), y, c);
    }
  }
}

// ---- analytic shapes: r(theta) > 0 for all theta -------------------------
function angDiff(a, b) {
  let d = Math.abs(a - b) % (2 * Math.PI);
  if (d > Math.PI) d = 2 * Math.PI - d;
  return d;
}
function baseRadius(kind, th) {
  const s = Math.sin(th), c = Math.cos(th);
  switch (kind) {
    case "BULB":   return R * (0.72 + 0.20 * s);                 // big round top, narrow neck
    case "BUBBLE": return R * (0.66 + 0.06 * Math.cos(2 * th)
                       + 0.30 * Math.exp(-Math.pow(angDiff(th, -Math.PI / 4), 2) / 0.05));
    case "PENCIL": return R * (0.30 + 0.55 * Math.abs(Math.cos(th - Math.PI / 4)));
    case "STAR":   return R * (0.50 + 0.34 * Math.cos(5 * th - Math.PI / 2));
    case "CIRCLE": return MEDIATOR;
    default:       return MEDIATOR;
  }
}
function lerpR(a, b, t) { return a + (b - a) * t; }

// A -> CIRCLE -> B, UNIFORM (linear) radial speed. The card's 别做成 explicitly
// bans 变形忽快忽慢 (morph speeding up / slowing down), so there is NO easing on
// the radial interpolation: t is linear in the frame index. Elastic feel comes
// only from squash/stretch + rotation below (as the card prescribes), not from
// the morph timing. Returns 96 radii; min radius is > 0 for every frame.
function morphRadii(from, to, t) {
  const out = new Float64Array(N);
  for (let i = 0; i < N; i++) {
    const th = i * 2 * Math.PI / N;
    const rF = baseRadius(from, th), rT = baseRadius(to, th);
    out[i] = (t < 0.5)
      ? lerpR(rF, MEDIATOR, t * 2)
      : lerpR(MEDIATOR, rT, (t - 0.5) * 2);
  }
  return out;
}
function singleRadii(kind) {
  const out = new Float64Array(N);
  for (let i = 0; i < N; i++) out[i] = baseRadius(kind, i * 2 * Math.PI / N);
  return out;
}

// ---- pre-registered beat schedule (exported; verifier diffs the REAL shipped
//      schedule, so a renderer/verifier divergence is caught) ----------------
// All boundaries are multiples of BEAT=15. bg changes at 30/105/180/270.
const MORPH_WINDOWS = [
  { from: "BULB",   to: "BUBBLE", start: 30,  end: 90,  dir: +1, label: "MORPH_A" },
  { from: "BUBBLE", to: "PENCIL", start: 105, end: 165, dir: -1, label: "MORPH_B" },
  { from: "PENCIL", to: "STAR",   start: 180, end: 240, dir: +1, label: "MORPH_C" },
];
function bgOf(m) {
  if (m < 30) return COL.BG0;
  if (m < 105) return COL.BG1;
  if (m < 180) return COL.BG2;
  if (m < 270) return COL.BG3;
  return COL.BG4;
}
function scheduleOf(m) {
  // m is already freeze-clamped by the caller.
  for (const w of MORPH_WINDOWS) {
    if (m >= w.start && m < w.end) {
      const t = (m - w.start) / (w.end - w.start);   // in [0,1)
      const s = Math.sin(2 * Math.PI * t);
      return {
        phase: w.label, bg: bgOf(m), morph: true,
        from: w.from, to: w.to, t, dir: w.dir,
        sx: 1 + 0.10 * s, sy: 1 - 0.10 * s,
        rot: (7 * Math.PI / 180) * Math.sin(Math.PI * t) * w.dir,
        scale: 1, glyphs: false, kind: null,
      };
    }
  }
  if (m < 30) {                 // INTRO: BULB scale-in 0.90 -> 1.00 over 15f
    return { phase: "INTRO", bg: bgOf(m), morph: false, from: null, to: null,
      t: 0, dir: 0, sx: 1, sy: 1, rot: 0,
      scale: 0.90 + 0.10 * Math.min(1, m / 15), glyphs: false, kind: "BULB" };
  }
  if (m < 105) {                // HOLD_A: BUBBLE clean
    return { phase: "HOLD_A", bg: bgOf(m), morph: false, from: null, to: null,
      t: 0, dir: 0, sx: 1, sy: 1, rot: 0, scale: 1, glyphs: false, kind: "BUBBLE" };
  }
  if (m < 180) {                // HOLD_B: PENCIL clean
    return { phase: "HOLD_B", bg: bgOf(m), morph: false, from: null, to: null,
      t: 0, dir: 0, sx: 1, sy: 1, rot: 0, scale: 1, glyphs: false, kind: "PENCIL" };
  }
  if (m < 270) {                // SETTLE: STAR, elastic wobble vanishing at 240 AND 270
    // sin(2*pi*u) is 0 at u=0 (frame 240, clean morph-C endpoint) and u=1
    // (frame 270, clean finale). No hard snap at either seam.
    const u = (m - 240) / 30;
    const w = 0.04 * Math.sin(2 * Math.PI * u);
    return { phase: "SETTLE", bg: bgOf(m), morph: false, from: null, to: null,
      t: 0, dir: 0, sx: 1 + w, sy: 1 - w, rot: 0,
      scale: 1, glyphs: false, kind: "STAR" };
  }
  // FINALE (m == 270 due to clamp): STAR + 灵感, background BG4, freeze.
  return { phase: "FINALE", bg: bgOf(m), morph: false, from: null, to: null,
    t: 0, dir: 0, sx: 1, sy: 1, rot: 0, scale: 1, glyphs: true, kind: "STAR" };
}

function shapeRadii(n) {
  const m = (n >= FREEZE_AT) ? FREEZE_AT : n;
  const s = scheduleOf(m);
  const radii = s.morph ? morphRadii(s.from, s.to, s.t) : singleRadii(s.kind);
  let minR = Infinity, maxR = -Infinity;
  for (let i = 0; i < N; i++) { if (radii[i] < minR) minR = radii[i]; if (radii[i] > maxR) maxR = radii[i]; }
  return { m, schedule: s, radii, minR, maxR };
}

// ---- historical abstract arrays; current title uses CJK_FONT ----------------
const G_LING = [
  "..######..", "..#....#..", "..######..", "....##....",
  "..######..", "..#....#..", ".#..##..#.", ".#.####.#.",
  "#..#..#..#", "#........#", "....##....", "..#....#..",
];
const G_GAN = [
  ".########.", "..#....#..", "..#....#..", ".########.",
  "..#....#..", ".########.", "..#....#..", ".#..##..#.",
  "..######..", "..#....#..", ".#......#.", "#...##...#",
];
function drawGlyph(buf, rows, ox, oy, sc) {
  for (let r = 0; r < rows.length; r++) {
    const row = rows[r];
    for (let c = 0; c < row.length; c++) {
      if (row[c] === "#") {
        const x0 = ox + c * sc, y0 = oy + r * sc;
        for (let y = y0; y < y0 + sc; y++) for (let x = x0; x < x0 + sc; x++) px(buf, x, y, COL.ACCENT);
      }
    }
  }
}
function drawGlyphs(buf) {
  const title=CJK_FONT.glyphs.title;
  drawIndexed(buf,W,H,title,Math.round((W-title.width)/2),870,COL.ACCENT);
}

// ---- the pure frame function ----------------------------------------------
function renderFrame(n) {
  const { m, schedule: s, radii } = shapeRadii(n);
  const buf = newBuf(s.bg);
  const cr = Math.cos(s.rot), sr = Math.sin(s.rot);
  const pts = new Array(N);
  for (let i = 0; i < N; i++) {
    const th = i * 2 * Math.PI / N;
    // start on the radial outline, then affine: squash -> rotate -> scale -> center
    let x = radii[i] * Math.cos(th);
    let y = -radii[i] * Math.sin(th);
    x *= s.sx; y *= s.sy;
    const xr = x * cr - y * sr, yr = x * sr + y * cr;
    // Keep floating geometry until native scan conversion; do not quantize
    // vertices on the old logical pixel lattice.
    pts[i] = { x: CX + xr * s.scale, y: CY + yr * s.scale };
  }
  // dark rim (slightly larger) then the clean cream fill
  const rim = pts.map(p => ({
    x: CX + (p.x - CX) * 1.045,
    y: CY + (p.y - CY) * 1.045,
  }));
  fillPolygon(buf, rim, COL.OUTLINE);
  fillPolygon(buf, pts, COL.SHAPE);
  if (s.glyphs) drawGlyphs(buf);
  return buf;
}

// ---- minimal deterministic PNG encoder (indexed color, no dependencies) ----
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
  ihdr[8] = 8; ihdr[9] = 3; ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0;
  const plte = Buffer.alloc(RGB.length * 3);
  RGB.forEach((rgb, i) => { plte[i * 3] = rgb[0]; plte[i * 3 + 1] = rgb[1]; plte[i * 3 + 2] = rgb[2]; });
  const raw = Buffer.alloc((W + 1) * H);
  for (let y = 0; y < H; y++) {
    raw[y * (W + 1)] = 0;
    for (let x = 0; x < W; x++) raw[y * (W + 1) + 1 + x] = buf[y * W + x];
  }
  const sig = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
  return Buffer.concat([
    sig, chunk("IHDR", ihdr), chunk("PLTE", plte),
    chunk("IDAT", zlib.deflateSync(raw, { level: 9 })), chunk("IEND", Buffer.alloc(0)),
  ]);
}

const KEYFRAMES = [
  { frame: 0,   slug: "INTRO_BULB" },
  { frame: 60,  slug: "MORPH_A_MEDIATOR" },
  { frame: 135, slug: "MORPH_B_MEDIATOR" },
  { frame: 210, slug: "MORPH_C_MEDIATOR" },
  { frame: 240, slug: "STAR_SETTLED" },
  { frame: 270, slug: "FINALE_LINGGAN_FREEZE" },
];
function frameFile(dir, n) { return path.join(dir, "frames", "f_" + String(n).padStart(4, "0") + ".png"); }
function writeFrame(dir, n) {
  const data = encodePNG(renderFrame(n));
  const hash = crypto.createHash("sha256").update(data).digest("hex");
  fs.writeFileSync(frameFile(dir, n), data);
  return hash;
}

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
      hashes[n] = writeFrame(dir, n);
      const kf = KEYFRAMES.find(k => k.frame === n);
      if (kf) {
        const src = fs.readFileSync(frameFile(dir, n));
        fs.writeFileSync(path.join(dir, "keyframes", "kf_" + String(n).padStart(4, "0") + ".png"), src);
        manifest.push({ keyframe: kf.slug, frame: n, t_seconds: n / FPS,
          path: "keyframes/kf_" + String(n).padStart(4, "0") + ".png",
          sha256: crypto.createHash("sha256").update(src).digest("hex") });
      }
    }
    fs.writeFileSync(path.join(dir, "frames", "frame_hashes.json"),
      JSON.stringify({ seed: SEED, fps: FPS, frames: FRAMES, resolution: [W, H],
        renderer: "morph-native-raster-js@2.0.0-review", hashes }, null, 2));
    fs.writeFileSync(path.join(dir, "keyframe_manifest.json"),
      JSON.stringify({ card: "05", slug: "08-morph", seed: SEED, fps: FPS, keyframes: manifest }, null, 2));
    console.log(JSON.stringify({ mode: "full", frames: FRAMES, keyframes: manifest.length, ok: true }));
  } else if (mode === "batch") {
    for (const n of a.split(",").map(Number)) hashes[n] = writeFrame(dir, n);
    console.log(JSON.stringify(hashes));
  } else if (mode === "range") {
    for (let n = Number(a); n < Number(b); n++) hashes[n] = writeFrame(dir, n);
    console.log(JSON.stringify(hashes));
  } else { console.error("unknown mode " + mode); process.exit(2); }
}
if (require.main === module) main();

module.exports = {
  SEED, FPS, FRAMES, W, H, BEAT, N, R, MEDIATOR, FREEZE_AT, CX, CY, COL, RGB,
  MORPH_WINDOWS, bgOf, scheduleOf, shapeRadii, renderFrame, encodePNG,
  baseRadius, morphRadii, singleRadii, KEYFRAMES, frameFile,
};
