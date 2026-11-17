#!/usr/bin/env node
/*
 * MOTION-07 / card 07 科幻 HUD (`22-hud`) — deterministic pure-JS raster renderer.
 *
 * Implements the PRE-REGISTERED contract in schedule.md (read it first).
 * renderFrame(n, seed) is a PURE function of n (via t=floor(n/5), clamped to 54)
 * and the frozen seed. No wall clock, no RNG stream, no inter-frame mutable
 * state, no alpha, no gradients, no filled bright blocks. Every visible change
 * happens only at a frame divisible by TICK=5.
 *
 * Palette (indexed color type 3, 4 entries):
 *   0 BG        #04171C  near-black cyan-tint ground (the 近黑偏青的底)
 *   1 BG_SCAN   #071F26  scanline rows (same hue, background texture only)
 *   2 CYAN      #00E5FF  cold state linework (t < 48)
 *   3 ORANGE    #FF6A00  warm state linework (t >= 48)
 * Exactly ONE of {2,3} is used in any given frame ("状态一变整体换成一种暖色，
 * 只用这两种色"). The two dark indices are the ground, never state colors.
 *
 * Renderer: hud-raster-js@1.0.0 (web frame-by-frame, realized as a deterministic
 * pure-JS frame server because puppeteer is NOT installed on this host — same
 * choice as the MOTION-06 pilot; stronger for determinism: no compositor/GPU).
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
const TICK = 5;          // 60 ticks over 300 frames
const FREEZE_T = 54;     // t>=54 pinned to the final poster (frames 270..299)

const PAL = [
  [0x04, 0x17, 0x1C],  // 0 BG
  [0x07, 0x1F, 0x26],  // 1 BG_SCAN
  [0x00, 0xE5, 0xFF],  // 2 CYAN
  [0xFF, 0x6A, 0x00],  // 3 ORANGE
];
const BG = 0, BG_SCAN = 1, CYAN = 2, ORANGE = 3;

// ---- deterministic pixel buffer -------------------------------------------
function newBuf() {
  const b = new Uint8Array(W * H);
  for (let y = 0; y < H; y++)          // 近黑偏青的底 — the ONLY area fill
    for (let x = 0; x < W; x++) b[y * W + x] = (y % 3 === 0) ? BG_SCAN : BG;
  return b;
}
function px(buf, x, y, c) { if (x >= 0 && x < W && y >= 0 && y < H) buf[y * W + x] = c; }
function hline(buf, x0, x1, y, c) { for (let x = x0; x <= x1; x++) px(buf, x, y, c); }
function vline(buf, x, y0, y1, c) { for (let y = y0; y <= y1; y++) px(buf, x, y, c); }
// stroked rectangle outline (never a filled block of state color)
function outline(buf, x0, y0, x1, y1, c) {
  hline(buf, x0, x1, y0, c); hline(buf, x0, x1, y1, c);
  vline(buf, x0, y0, y1, c); vline(buf, x1, y0, y1, c);
}
// corner bracket (L-shape), length L, stroke 1-2px
function bracket(buf, x, y, sx, sy, L, c) {
  hline(buf, x, x + sx * L, y, c);
  vline(buf, x, y, y + sy * L, c);
  hline(buf, x, x + sx * (L - 1), y + 1, c); // 2px weight
}

// ---- 5x7 bitmap font (documented; no bundled font dependency) -------------
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
  "A":["01110","10001","10001","11111","10001","10001","10001"],
  "C":["01111","10000","10000","10000","10000","10000","01111"],
  "D":["11110","10001","10001","10001","10001","10001","11110"],
  "E":["11111","10000","10000","11110","10000","10000","11111"],
  "G":["01111","10000","10000","10111","10001","10001","01111"],
  "I":["11111","00100","00100","00100","00100","00100","11111"],
  "L":["10000","10000","10000","10000","10000","10000","11111"],
  "M":["10001","11011","10101","10101","10001","10001","10001"],
  "N":["10001","11001","10101","10011","10001","10001","10001"],
  "O":["01110","10001","10001","10001","10001","10001","01110"],
  "S":["01111","10000","10000","01110","00001","00001","11110"],
  "T":["11111","00100","00100","00100","00100","00100","00100"],
  "U":["10001","10001","10001","10001","10001","10001","01110"],
  "V":["10001","10001","10001","10001","10001","01010","00100"],
  " ":["00000","00000","00000","00000","00000","00000","00000"],
  ".":["00000","00000","00000","00000","00000","01100","01100"],
  "/":["00001","00001","00010","00100","01000","10000","10000"],
  ":":["00000","01100","01100","00000","01100","01100","00000"],
  "m":["00000","00000","11010","10101","10101","10101","10101"],
  "s":["00000","00000","01111","10000","01110","00001","11110"],
};
// scale>=2 everywhere (card forbids 看不清的小字). Text is drawn WITHOUT glow.
function drawText(buf, str, ox, oy, scale, c) {
  const adv = 5 * scale + 2;
  for (let i = 0; i < str.length; i++) {
    const g = FONT[str[i]] || FONT[" "];
    for (let r = 0; r < 7; r++) for (let q = 0; q < 5; q++) {
      if (g[r][q] === "1")
        for (let dy = 0; dy < scale; dy++) for (let dx = 0; dx < scale; dx++)
          px(buf, ox + i * adv + q * scale + dx, oy + r * scale + dy, c);
    }
  }
}

// ---- 4 abstract geometric CJK bitmaps (着陆成功) --------------------------
// No CJK font is bundled. These are DOCUMENTED abstract 9x9 geometric glyphs
// (same honest pattern the MOTION-06 pilot used for 「3 分」), NOT a real
// typeface and NOT gibberish: the literal legible content is carried by the
// typed latin words "LANDING SUCCESS" above them.
const CJK = [
  ["..#####..",".#..#..#.","..#####..",".#..#..#.","##.###.##","..#####..",".#..#..#.","..#####..","....#...."],
  ["#####.###","..#...#..","#####.###","..#...#..","#####.###","....#....",".#######.","....#....","...###..."],
  ["...###...","..#...#..",".#######.","..#...#..","...###...","..#####..",".#.....#.","#.......#",".#######."],
  ["..#####..",".#.....#.",".#.###.#.",".#.###.#.",".#.....#.",".#######.","..#...#..",".#.....#.","..#####.."],
];
function drawCJK(buf, idx, ox, oy, scale, c) {
  const g = CJK[idx];
  for (let r = 0; r < 9; r++) for (let q = 0; q < 9; q++) {
    if (g[r][q] === "#")
      for (let dy = 0; dy < scale; dy++) for (let dx = 0; dx < scale; dx++)
        px(buf, ox + q * scale + dx, oy + r * scale + dy, c);
  }
}

// ---- outer perimeter path (stroke reveal = extending path, never a fade) ---
function perimeter(x0, y0, x1, y1) {
  const p = [];
  for (let x = x0; x <= x1; x++) p.push([x, y0]);
  for (let y = y0 + 1; y <= y1; y++) p.push([x1, y]);
  for (let x = x1 - 1; x >= x0; x--) p.push([x, y1]);
  for (let y = y1 - 1; y > y0; y--) p.push([x0, y]);
  return p;
}
function glowStroke(buf, pts, count, c, seed) {
  for (let i = 0; i < count && i < pts.length; i++) {
    const x = pts[i][0], y = pts[i][1];
    px(buf, x, y, c);
    // 一点辉光: sparse 1px stipple in the SAME state color (no new hue, no alpha)
    if ((x * 3 + y * 5 + seed) % 3 === 0) px(buf, x, y + 1, c);
  }
}

// ---- seeded closed-form telemetry noise (no RNG stream) -------------------
// Deterministic speckle derived from seed: guarantees every frame's bytes are
// seed-bound (so a wrong-seed independent process is detectable), and reads as
// faint HUD sensor noise. Uses the ACTIVE state color only.
function speckle(buf, c, seed) {
  for (let i = 0; i < 34; i++) {
    const x = (seed * 13 + i * 197 + 7) % W;
    const y = (seed * 29 + i * 83 + 11) % H;
    px(buf, x, y, c);
  }
}
// jitter digit, pure closed form of (seed, tick, position)
function jd(seed, t, k) { return (seed * 7 + t * 131 + k * 977 + 3) % 10; }

// ---- PRE-REGISTERED tick -> state (shipped; verify.js requires THIS fn) ----
function hudState(t) {
  const color = (t >= 48) ? ORANGE : CYAN;
  const outer = Math.min(1, (t + 1) * 0.25);        // t0=.25 t1=.5 t2=.75 t3+=1
  const inner = Math.min(4, Math.max(0, t - 3));      // t4=1 t5=2 t6=3 t7+=4
  const chrome = t >= 8;                             // ticks + numbering
  const telemetry = t >= 9;                          // labels + reading
  let scanStep = 0;
  if (t >= 10) scanStep = 1;
  if (t >= 11) scanStep = 2;
  if (t >= 19) scanStep = 3;
  if (t >= 20) scanStep = 4;
  if (t >= 21) scanStep = 5;
  if (t >= 22) scanStep = 6;
  const jitter = (t >= 12 && t <= 17) ? (t - 11) : 0; // 1..6
  const settled = t >= 18;
  const contour = t >= 23;
  const reticle = t >= 24;
  const lockOn = t >= 25;
  const lockScale = lockOn ? (t <= 36 ? 1.40 - (t - 25) * (0.40 / 11) : 1.00) : 0;
  const lockVisible = lockOn && !(t === 42 || t === 44);
  const flashes = (t >= 43 ? 1 : 0) + (t >= 45 ? 1 : 0);
  const typed = t >= 48 ? Math.min(15, (t - 47) * 3) : 0;
  const cjk = t >= 48 ? Math.min(4, t - 47) : 0;
  const cursor = t >= 48 && t <= 53;
  const blink = (t === 53);
  return { t, color, outer, inner, chrome, telemetry, scanStep, jitter, settled,
           contour, reticle, lockOn, lockScale, lockVisible, flashes, typed, cjk,
           cursor, blink };
}

// ---- deterministic frame function -----------------------------------------
function renderFrame(n, seed) {
  const t = Math.min(Math.floor(n / TICK), FREEZE_T);
  const s = hudState(t);
  const c = s.color;
  const buf = newBuf();

  // (0) seeded sensor speckle — active color, present in EVERY frame
  speckle(buf, c, seed);

  // (R4) outer ring REVEAL by extending stroke (not a fade); glow on outer only
  const OP = perimeter(40, 40, 600, 320);
  glowStroke(buf, OP, Math.floor(s.outer * OP.length), c, seed);

  // (R3) 4 corner brackets once the outer ring is complete
  if (s.outer >= 1) {
    bracket(buf, 40, 40, 1, 1, 26, c);
    bracket(buf, 600, 40, -1, 1, 26, c);
    bracket(buf, 40, 320, 1, -1, 26, c);
    bracket(buf, 600, 320, -1, -1, 26, c);
  }

  // (R3) ruler ticks + corner numbering 01..04 (chrome, t>=8)
  if (s.chrome) {
    for (let x = 80; x <= 560; x += 40) { vline(buf, x, 40, 46, c); vline(buf, x, 314, 320, c); }
    for (let y = 80; y <= 280; y += 40) { hline(buf, 40, 46, y, c); hline(buf, 594, 600, y, c); }
    drawText(buf, "01", 52, 52, 2, c);
    drawText(buf, "02", 548, 52, 2, c);
    drawText(buf, "03", 52, 292, 2, c);
    drawText(buf, "04", 548, 292, 2, c);
  }

  // (R4) inner panels revealed one per tick, AFTER the outer ring (外圈先出、里圈后出)
  const PANELS = [[60, 55, 250, 120], [390, 55, 580, 120],
                  [60, 250, 250, 315], [390, 250, 580, 315]];
  for (let i = 0; i < s.inner; i++) { const p = PANELS[i]; outline(buf, p[0], p[1], p[2], p[3], c); }

  // (R5) telemetry: labels + ALT/VEL readings (static -> jitter -> settled)
  if (s.telemetry) {
    drawText(buf, "ALT", 70, 68, 2, c);
    drawText(buf, "SCAN", 400, 68, 2, c);
    drawText(buf, "VEL", 70, 258, 2, c);
    let alt, vel;
    if (s.settled) { alt = "0000"; vel = "00.0"; }
    else if (s.jitter > 0) {
      alt = "" + jd(seed, t, 0) + jd(seed, t, 1) + jd(seed, t, 2) + jd(seed, t, 3);
      vel = "" + jd(seed, t, 4) + jd(seed, t, 5) + "." + jd(seed, t, 6);
    } else { alt = "0200"; vel = "08.9"; }
    drawText(buf, alt + "m", 70, 90, 2, c);
    drawText(buf, vel + "m/s", 70, 280, 2, c);
  }

  // (content) terrain scan sweep, then contour, then target reticle
  if (s.scanStep > 0) {
    const sy = 150 + s.scanStep * 12;
    hline(buf, 250, 390, sy, c);
    for (let x = 250; x <= 390; x += 20) vline(buf, x, sy - 3, sy, c);
  }
  if (s.contour) {
    // deterministic jagged terrain polyline (pure function, no RNG)
    let prevY = 232;
    for (let x = 250; x <= 390; x += 4) {
      const y = 232 + ((x * 7 + seed) % 17) - 8;
      vline(buf, x, Math.min(prevY, y), Math.max(prevY, y), c);
      prevY = y;
    }
  }
  if (s.reticle) {
    const cx = 320, cy = 200;
    hline(buf, cx - 14, cx + 14, cy, c); vline(buf, cx, cy - 14, cy + 14, c);
    // small target circle (stroked, 1px)
    for (let a = 0; a < 360; a += 12) {
      const rad = a * Math.PI / 180;
      px(buf, Math.round(cx + 9 * Math.cos(rad)), Math.round(cy + 9 * Math.sin(rad)), c);
    }
    drawText(buf, "TARGET", 285, 214, 2, c);
  }

  // (R7) lock-on bracket scale 1.40 -> 1.00, two flashes on landing
  if (s.lockOn && s.lockVisible) {
    const half = Math.round(40 * s.lockScale);
    const cx = 320, cy = 200;
    const x0 = cx - half, x1 = cx + half, y0 = cy - half, y1 = cy + half;
    bracket(buf, x0, y0, 1, 1, 14, c);
    bracket(buf, x1, y0, -1, 1, 14, c);
    bracket(buf, x0, y1, 1, -1, 14, c);
    bracket(buf, x1, y1, -1, -1, 14, c);
  }

  // (R6) typed status words + per-tick CJK glyphs + cursor (WITHOUT glow)
  if (s.typed > 0) {
    drawText(buf, "LANDING SUCCESS".slice(0, s.typed), 200, 92, 2, c);
    if (s.cursor && !s.blink) {
      const cx = 200 + s.typed * 12;
      vline(buf, cx, 92, 106, c);
    }
  }
  for (let i = 0; i < s.cjk; i++) drawCJK(buf, i, 250 + i * 34, 120, 2, c);

  return buf;
}

// ---- minimal deterministic indexed-PNG encoder (no dependencies) ----------
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
  const plte = Buffer.alloc(PAL.length * 3);
  PAL.forEach((rgb, i) => { plte[i * 3] = rgb[0]; plte[i * 3 + 1] = rgb[1]; plte[i * 3 + 2] = rgb[2]; });
  const raw = Buffer.alloc((W + 1) * H);
  for (let y = 0; y < H; y++) {
    raw[y * (W + 1)] = 0; // filter: none
    for (let x = 0; x < W; x++) raw[y * (W + 1) + 1 + x] = buf[y * W + x];
  }
  const sig = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
  return Buffer.concat([sig, chunk("IHDR", ihdr), chunk("PLTE", plte),
    chunk("IDAT", zlib.deflateSync(raw, { level: 9 })), chunk("IEND", Buffer.alloc(0))]);
}
function pngFor(n, seed) { return encodePNG(renderFrame(n, seed)); }
function frameFile(dir, n) { return path.join(dir, "frames", "f_" + String(n).padStart(4, "0") + ".png"); }
function writeFrame(dir, n, seed) {
  const data = pngFor(n, seed);
  const hash = crypto.createHash("sha256").update(data).digest("hex");
  fs.writeFileSync(frameFile(dir, n), data);
  return hash;
}

const KEYFRAMES = [
  { frame: 0,   slug: "OUTER_RING" },
  { frame: 60,  slug: "SCAN" },
  { frame: 90,  slug: "SETTLED" },
  { frame: 180, slug: "LOCK" },
  { frame: 240, slug: "WARM" },
  { frame: 270, slug: "POSTER" },
];

function main() {
  const [mode, dir, a, b] = process.argv.slice(2);
  if (!dir) { console.error("usage: render.js full|batch|range <dir> [args]"); process.exit(2); }
  if (mode === "full") {
    fs.mkdirSync(path.join(dir, "frames"), { recursive: true });
    fs.mkdirSync(path.join(dir, "keyframes"), { recursive: true });
    const hashes = {}, manifest = [];
    for (let n = 0; n < FRAMES; n++) {
      hashes[n] = writeFrame(dir, n, SEED);
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
      JSON.stringify({ seed: SEED, fps: FPS, frames: FRAMES, resolution: [W, H], tick: TICK,
        renderer: "hud-raster-js@1.0.0", hashes }, null, 2));
    fs.writeFileSync(path.join(dir, "keyframe_manifest.json"),
      JSON.stringify({ card: "07", slug: "22-hud", seed: SEED, fps: FPS, keyframes: manifest }, null, 2));
    console.log(JSON.stringify({ mode: "full", frames: FRAMES, keyframes: manifest.length, ok: true }));
  } else if (mode === "batch") {
    // in-memory only: NEVER overwrite baseline frames (determinism helper)
    const h = {};
    for (const n of a.split(",").map(Number))
      h[n] = crypto.createHash("sha256").update(pngFor(n, SEED)).digest("hex");
    console.log(JSON.stringify(h));
  } else if (mode === "range") {
    const h = {};
    for (let n = Number(a); n < Number(b); n++)
      h[n] = crypto.createHash("sha256").update(pngFor(n, SEED)).digest("hex");
    console.log(JSON.stringify(h));
  } else { console.error("unknown mode " + mode); process.exit(2); }
}
if (require.main === module) main();
module.exports = { SEED, FPS, FRAMES, TICK, FREEZE_T, PAL, CYAN, ORANGE,
                   hudState, renderFrame, pngFor };
