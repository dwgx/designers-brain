// MOTION-02 / card 02 "液态 (LIQUID)" / slug 07-liquid
// Procedural, dependency-free, deterministic per-pixel software renderer.
// Implements the card's mechanism: a fused metaball distance field (smooth-min SDF),
// rounded necks when blobs merge, thinning filaments when they split, fling-out
// easing (fast start / slow stop), landing squash+recover, secondary droplets that
// arrive 2-3 frames late, and metallic specular + rim reflection to show thickness.
//
// Determinism contract: output is a PURE FUNCTION of (frameIndex, constants below).
// No Date, no Math.random, no wall-clock, no accumulation across frames. Any frame
// can be rendered in any order, in a fresh process, or after a killed process and
// will produce byte-identical output.
//
// Usage:
//   node render.mjs --frames 0..299 --out frames/         (render a range, sequential)
//   node render.mjs --frames 17,88,150,211,290 --out frames/  (arbitrary order)
//   node render.mjs --frames 0..299 --out frames/ --stop-after 137  (pause test)
// Output: PNG frames f%04d.png via the pinned ffmpeg binary (image2 muxer).

import { execFileSync } from 'node:child_process';
import { mkdirSync, writeFileSync, readFileSync, unlinkSync } from 'node:fs';
import { join, resolve } from 'node:path';

// ---- fixed, versioned constants (single source of truth for the whole film) ----
export const SPEC = {
  renderer: 'metaball-sdf-software',
  renderer_version: '1.0.0',
  seed: 20261115,
  fps: 30,
  frames: 300,
  duration_seconds: 10,
  width: 1920,
  height: 1080,
  // ffmpeg pinned binary (n7.0.2); sha256 recorded in plan.md / RESULT.md
  ffmpeg_sha256: 'b2495c9ab7bec4ba5f9e34fcabc70f778cdb70730ed32b627b9f51f6c7f384ad',
  ffmpeg_version: 'n7.0.2',
  card: '02',
  slug: '07-liquid',
};

const FFMPEG = 'C:/Program Files/Virtual Desktop Streamer/ffmpeg.exe';
const W = SPEC.width, H = SPEC.height;
const CX = W / 2, CY = H / 2;
const FR = SPEC.frames; // 300

// ---- small deterministic math helpers (no Math.random anywhere) ----
function smoothstep(a, b, x) {
  if (b === a) return x < a ? 0 : 1;
  const t = Math.min(1, Math.max(0, (x - a) / (b - a)));
  return t * t * (3 - 2 * t);
}
function clamp(x, a, b) { return x < a ? a : (x > b ? b : x); }
function mix(a, b, t) { return a + (b - a) * t; }
// deterministic hash noise (no seed drift; pure integer function)
function hash2(ix, iy) {
  let h = (ix * 374761393 + iy * 668265263 + SPEC.seed * 1274126177) | 0;
  h = (h ^ (h >>> 13)) * 1274126177 | 0;
  h = h ^ (h >>> 16);
  return (h >>> 0) / 4294967295;
}
// polynomial smooth-min (the "rounded neck" / metaball fusion kernel)
function smin(a, b, k) {
  const h = clamp(0.5 + 0.5 * (b - a) / k, 0, 1);
  return mix(b, a, h) - k * h * (1 - h);
}
// easing: "起步快、停得慢" (fast start, slow stop)
function flingEase(t) { return 1 - Math.pow(1 - clamp(t, 0, 1), 3); }

// ---- time / narrative (6 keyframes from card §rules + 内容分镜) ----
// t in [0,1] over 10s (300 frames). Keyframes at 0,0.2,0.4,0.6,0.8,1.0.
// Story: 一滴液态金属落在黑色台面溅开 → 几团金属融合 → 拉丝 → 断开 →
//        聚成一个「合」字 → 再落下一滴荡开一圈涟漪.
// Each blob: {x, y, r, ax, ay} where ax/ay are the anisotropic (squash) factors.
function keyframeState(k) {
  // positions in pixels; r in pixels. Six narrative states.
  const K = [
    // K0 f0: single drop just above the dark table, about to land
    { blobs: [{ x: CX, y: CY - 260, r: 70, ax: 1, ay: 1 }], ripple: 0, letter: 0, trails: [] },
    // K1 f60: impact splash — main flattened body + 3 flung lobes
    { blobs: [
      { x: CX, y: CY + 40, r: 120, ax: 1.25, ay: 0.62 },
      { x: CX - 250, y: CY - 70, r: 62, ax: 1, ay: 1 },
      { x: CX + 270, y: CY - 30, r: 58, ax: 1, ay: 1 },
      { x: CX + 40, y: CY - 220, r: 52, ax: 1, ay: 1 },
    ], ripple: 0.15, letter: 0, trails: [0, 1, 2] },
    // K2 f120: fusion — lobes pulled back toward center, rounded neck via smin
    { blobs: [
      { x: CX - 30, y: CY + 10, r: 132, ax: 1, ay: 1 },
      { x: CX + 90, y: CY - 40, r: 96, ax: 1, ay: 1 },
      { x: CX + 150, y: CY + 80, r: 64, ax: 1, ay: 1 },
    ], ripple: 0.05, letter: 0, trails: [0] },
    // K3 f180: stretching / filament — two large masses pulling apart, thin bridge
    { blobs: [
      { x: CX - 200, y: CY, r: 118, ax: 1.15, ay: 0.9 },
      { x: CX + 200, y: CY - 10, r: 110, ax: 1.15, ay: 0.9 },
      { x: CX, y: CY, r: 20, ax: 3.5, ay: 0.22 }, // the stretching filament
    ], ripple: 0, letter: 0.15, trails: [] },
    // K4 f240: gathered into the glyph 「合」 (approximated by a compact ring+bar cluster)
    { blobs: [
      { x: CX, y: CY - 110, r: 96, ax: 1.5, ay: 0.55 }, // top 人 roof
      { x: CX, y: CY - 10, r: 110, ax: 1.25, ay: 0.45 }, // 一 bar
      { x: CX, y: CY + 90, r: 84, ax: 1, ay: 1 }, // 口 box
      { x: CX - 70, y: CY + 90, r: 30, ax: 1, ay: 1 },
      { x: CX + 70, y: CY + 90, r: 30, ax: 1, ay: 1 },
    ], ripple: 0, letter: 1, trails: [] },
    // K5 f299: a fresh drop has fallen; concentric ripple expands
    { blobs: [
      { x: CX, y: CY - 110, r: 96, ax: 1.5, ay: 0.55 },
      { x: CX, y: CY - 10, r: 110, ax: 1.25, ay: 0.45 },
      { x: CX, y: CY + 90, r: 84, ax: 1, ay: 1 },
      { x: CX - 70, y: CY + 90, r: 30, ax: 1, ay: 1 },
      { x: CX + 70, y: CY + 90, r: 30, ax: 1, ay: 1 },
      { x: CX + 220, y: CY + 160, r: 54, ax: 1, ay: 1 }, // new droplet
    ], ripple: 0.85, letter: 1, trails: [5] },
  ];
  return K[k];
}

// Interpolate blob sets across keyframes with deterministic per-frame easing.
// Secondary droplets (trails) are delayed by 2-3 frames: we sample their
// trajectory at (t - delay) so they visibly arrive late (card rule).
function sceneAt(f) {
  const t = f / (FR - 1); // 0..1
  const seg = Math.min(4, Math.floor(t * 5));
  const lt = (t * 5) - seg; // local 0..1 within the 5 segments (K0..K5)
  const e = flingEase(lt); // fast-start / slow-stop motion
  const A = keyframeState(seg), B = keyframeState(seg + 1);

  // Build a unified blob list by index (max blobs across A and B); missing blobs
  // in one keyframe are represented by a radius-0 blob at the other's position.
  const n = Math.max(A.blobs.length, B.blobs.length);
  const blobs = [];
  for (let i = 0; i < n; i++) {
    const a = A.blobs[i] || { x: B.blobs[i].x, y: B.blobs[i].y, r: 0, ax: 1, ay: 1 };
    const b = B.blobs[i] || { x: A.blobs[i].x, y: A.blobs[i].y, r: 0, ax: 1, ay: 1 };
    blobs.push({
      x: mix(a.x, b.x, e),
      y: mix(a.y, b.y, e),
      r: mix(a.r, b.r, e),
      ax: mix(a.ax, b.ax, e),
      ay: mix(a.ay, b.ay, e),
    });
  }
  let ripple = mix(A.ripple, B.ripple, e);
  const letter = mix(A.letter, B.letter, e);

  // Card rule: "主体后面跟几颗小液滴，晚 2-3 帧到". For blobs flagged as trails,
  // offset their position toward the previous keyframe by a 2-3 frame delay.
  const trailIdx = B.trails.length ? B.trails : A.trails;
  for (const ti of trailIdx) {
    const delayFrames = 2 + (ti % 2); // deterministic 2 or 3 frames
    const tf = Math.max(0, f - delayFrames);
    const ts = sceneAtDelayed(tf);
    if (ts.blobs[ti]) {
      blobs[ti].x = ts.blobs[ti].x;
      blobs[ti].y = ts.blobs[ti].y;
      blobs[ti].r = Math.min(blobs[ti].r, ts.blobs[ti].r);
    }
  }
  return { blobs, ripple, letter };
}

// delayed-scene evaluator WITHOUT trail recursion (avoids infinite recursion)
function sceneAtDelayed(f) {
  const t = f / (FR - 1);
  const seg = Math.min(4, Math.floor(t * 5));
  const lt = (t * 5) - seg;
  const e = flingEase(lt);
  const A = keyframeState(seg), B = keyframeState(seg + 1);
  const n = Math.max(A.blobs.length, B.blobs.length);
  const blobs = [];
  for (let i = 0; i < n; i++) {
    const a = A.blobs[i] || { x: B.blobs[i].x, y: B.blobs[i].y, r: 0, ax: 1, ay: 1 };
    const b = B.blobs[i] || { x: A.blobs[i].x, y: A.blobs[i].y, r: 0, ax: 1, ay: 1 };
    blobs.push({ x: mix(a.x, b.x, e), y: mix(a.y, b.y, e), r: mix(a.r, b.r, e),
      ax: mix(a.ax, b.ax, e), ay: mix(a.ay, b.ay, e) });
  }
  return { blobs };
}

// ---- signed distance field with smooth-min fusion ----
// Returns { d, nx, ny } where d<0 inside liquid. Uses polynomial smin so
// merging blobs form a rounded neck (card: "接口是圆润的颈，不是硬折").
function field(px, py, blobs) {
  let d = 1e9;
  const K = 46; // fusion kernel strength (controls neck roundness)
  let gx = 0, gy = 0;
  for (const b of blobs) {
    if (b.r <= 0.01) continue;
    const dx = (px - b.x) / b.ax, dy = (py - b.y) / b.ay;
    const dist = Math.sqrt(dx * dx + dy * dy) - b.r;
    d = smin(d, dist, K);
  }
  // gradient via finite differences (deterministic)
  const eps = 1.5;
  const dxp = fieldRaw(px + eps, py, blobs), dxm = fieldRaw(px - eps, py, blobs);
  const dyp = fieldRaw(px, py + eps, blobs), dym = fieldRaw(px, py - eps, blobs);
  gx = dxp - dxm; gy = dyp - dym;
  const gl = Math.sqrt(gx * gx + gy * gy) || 1;
  return { d, nx: gx / gl, ny: gy / gl };
}
function fieldRaw(px, py, blobs) {
  let d = 1e9;
  const K = 46;
  for (const b of blobs) {
    if (b.r <= 0.01) continue;
    const dx = (px - b.x) / b.ax, dy = (py - b.y) / b.ay;
    const dist = Math.sqrt(dx * dx + dy * dy) - b.r;
    d = smin(d, dist, K);
  }
  return d;
}

// ---- shading: metallic liquid (厚度 via specular + fresnel rim + highlight) ----
// Card: "表面有高光和边缘反光，看得出厚度"; avoid "没有高光的平涂".
function shade(d, nx, ny, px, py, ripple) {
  // background: dark table with a subtle vertical gradient (not flat fill)
  let r = 10 + 8 * (py / H), g = 10 + 8 * (py / H), b = 16 + 12 * (py / H);

  // ripple rings (card: "荡开一圈涟漪")
  if (ripple > 0.01) {
    const rr = Math.hypot(px - (CX + 220), py - (CY + 160));
    const ring = Math.sin(rr * 0.035 - ripple * 22) * Math.exp(-Math.abs(rr - ripple * 520) / 90);
    const amt = clamp(ring * 0.5 + 0.5, 0, 1) * ripple * 0.35;
    r += 30 * amt; g += 40 * amt; b += 70 * amt;
  }

  if (d < 0) {
    // inside the metaball: treat as a 3D chrome blob; derive a fake height
    // from the field value so thickness is visible via specular rolloff.
    const depth = clamp(-d / 90, 0, 1);
    const hgt = Math.sqrt(Math.max(0, 1 - depth * depth)); // dome profile
    // light direction (upper-left, fixed)
    const Lx = -0.55, Ly = -0.62, Lz = 0.56;
    const Nx = nx * (1 - hgt), Ny = ny * (1 - hgt), Nz = hgt + 0.15;
    const Nl = Math.sqrt(Nx * Nx + Ny * Ny + Nz * Nz) || 1;
    const nX = Nx / Nl, nY = Ny / Nl, nZ = Nz / Nl;
    const diff = Math.max(0, nX * Lx + nY * Ly + nZ * Lz);
    // Blinn-Phong specular (sharp highlight)
    const Vx = 0, Vy = 0, Vz = 1;
    const Hx = Lx + Vx, Hy = Ly + Vy, Hz = Lz + Vz;
    const Hl = Math.sqrt(Hx * Hx + Hy * Hy + Hz * Hz) || 1;
    let spec = Math.max(0, (nX * Hx + nY * Hy + nZ * Hz) / Hl);
    spec = Math.pow(spec, 48) * 1.4;
    // fresnel-like rim reflection (边缘反光)
    const fres = Math.pow(1 - Math.max(0, nZ), 3);
    // metal base: cool silver/chrome with a warm gold tint in raised center
    const base = 120 + 90 * diff;
    r = base + 30 * hgt; g = base + 26 * hgt; b = base + 10 * hgt;
    r += 255 * spec + 90 * fres;
    g += 250 * spec + 110 * fres;
    b += 235 * spec + 150 * fres;
    // subtle deterministic grain so the surface isn't a flat fill
    const grain = (hash2(px | 0, py | 0) - 0.5) * 6;
    r += grain; g += grain; b += grain;
  } else {
    // anti-aliased soft edge: blend chrome rim into background over ~2px
    const edge = Math.exp(-d / 2.2);
    r += 60 * edge; g += 70 * edge; b += 110 * edge;
  }
  return [clamp(r, 0, 255) | 0, clamp(g, 0, 255) | 0, clamp(b, 0, 255) | 0];
}

// ---- render one frame to an RGB24 raw buffer (pure function of f) ----
export function renderFrame(f) {
  const { blobs, ripple, letter } = sceneAt(f);
  const buf = Buffer.alloc(W * H * 3);
  for (let y = 0; y < H; y++) {
    for (let x = 0; x < W; x++) {
      const { d, nx, ny } = field(x, y, blobs);
      const [r, g, b] = shade(d, nx, ny, x, y, ripple);
      const o = (y * W + x) * 3;
      buf[o] = r; buf[o + 1] = g; buf[o + 2] = b;
    }
  }
  return buf;
}

// ---- write a frame as PNG via pinned ffmpeg (lossless) ----
// FIX (repair_round=2, M02-RGB-HEADER): feed ffmpeg EXACTLY W*H*3 raw RGB bytes
// with NO PPM header. rawvideo rgb24 does not parse a PPM header: the previous
// version prepended 18 header bytes, so ffmpeg consumed them as the first 6
// pixels and dropped the trailing 6 pixels. A hard length assertion guarantees
// the transport can never silently re-introduce a header/offset.
function writePNG(f, outDir) {
  const raw = renderFrame(f);
  if (raw.length !== W * H * 3) {
    throw new Error(`raw frame length ${raw.length} != expected ${W * H * 3}`);
  }
  const rawPath = join(outDir, `_tmp_${String(f).padStart(4, '0')}.rgb`);
  const pngPath = join(outDir, `f${String(f).padStart(4, '0')}.png`);
  writeFileSync(rawPath, raw); // exactly W*H*3 bytes, no header, no padding
  try {
    execFileSync(FFMPEG, [
      '-hide_banner', '-loglevel', 'error', '-nostdin', '-y',
      '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', `${W}x${H}`, '-i', rawPath,
      '-frames:v', '1', '-update', '1', pngPath,
    ], { stdio: 'pipe' });
  } finally {
    try { unlinkSync(rawPath); } catch (_) {}
  }
  return pngPath;
}

// ---- CLI ----
function parseFrameList(spec) {
  const out = [];
  for (const part of spec.split(',')) {
    const m = part.match(/^(\d+)\.\.(\d+)$/);
    if (m) { for (let i = +m[1]; i <= +m[2]; i++) out.push(i); }
    else if (/^\d+$/.test(part)) out.push(+part);
  }
  return out;
}

function main() {
  const args = process.argv.slice(2);
  const get = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
  const framesSpec = get('--frames', '0..299');
  const outDir = resolve(get('--out', 'frames'));
  const stopAfter = args.includes('--stop-after') ? +get('--stop-after', '0') : null;
  mkdirSync(outDir, { recursive: true });
  const frames = parseFrameList(framesSpec);
  let written = 0;
  for (const f of frames) {
    if (f < 0 || f >= FR) { console.error('frame out of range: ' + f); process.exit(2); }
    writePNG(f, outDir);
    written++;
    if (stopAfter !== null && written >= stopAfter) {
      // Simulated pause: exit cleanly after a partial write (child will be killed
      // in the real pause test; here we just stop so resume can continue).
      console.log(`STOPPED_AFTER ${written} (last f=${f})`);
      return;
    }
  }
  console.log(`WROTE ${written} frames to ${outDir}`);
}

if (import.meta.url === `file://${process.argv[1]}` ||
    process.argv[1] && process.argv[1].replace(/\\/g, '/').endsWith('render.mjs')) {
  main();
}
