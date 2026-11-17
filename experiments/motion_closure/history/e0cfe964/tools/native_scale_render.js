#!/usr/bin/env node
/*
 * Native-resolution geometry scaler for the low-resolution motion cards.
 *
 * PURPOSE / HONESTY
 * -----------------
 * The shipped sources/MOTION-XX/render.* files are the FROZEN original renderers,
 * byte-for-byte. Their pure renderFrame(n, seed) is called UNCHANGED. This wrapper
 * applies a single deterministic integer geometric scale S to the raster output:
 *
 *     x -> x*S ,  y -> y*S ,  every 1px stroke/pixel -> an S x S block.
 *
 * S is exact: 640x360 * 3 = 1920x1080 ; 960x540 * 2 = 1920x1080. No resampling,
 * no new colours, no interpolation, no frame duplication, no wall clock, no RNG.
 * Seed, beat/time schedule and drawing method are the ORIGINAL renderer's, so the
 * temporal behaviour is identical to the frozen card. This is a RASTER render with
 * uniformly SCALED GEOMETRY — NOT a browser/WebGL native 1920x1080 re-author and it
 * adds no finer native detail than the logical grid. See each card's NOTES.md.
 *
 * CLI
 *   node native_scale_render.js <renderer.js> <outdir> full   <srcW> <srcH> <palette|rgb>
 *   node native_scale_render.js <renderer.js> <outdir> batch  <srcW> <srcH> <palette|rgb> <n,n,..>
 *
 * <palette> is the literal JS array expression of the source palette (indexed
 * colour buffers), or the word 'rgb' for truecolor buffers.
 */
"use strict";
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");
const crypto = require("crypto");

const TARGET_W = 1920, TARGET_H = 1080, FRAMES = 300;

function crc32(buf) {
  let c = ~0;
  for (let i = 0; i < buf.length; i++) {
    c ^= buf[i];
    for (let k = 0; k < 8; k++) c = (c >>> 1) ^ (0xEDB88320 & -(c & 1));
  }
  return (~c) >>> 0;
}
function chunk(type, data) {
  const len = Buffer.alloc(4); len.writeUInt32BE(data.length, 0);
  const t = Buffer.from(type, "ascii");
  const crc = Buffer.alloc(4); crc.writeUInt32BE(crc32(Buffer.concat([t, data])), 0);
  return Buffer.concat([len, t, data, crc]);
}
/* deterministic truecolor RGB PNG (fixed filter=none, fixed zlib level) */
function encodePNG(rgb, w, h) {
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(w, 0); ihdr.writeUInt32BE(h, 4);
  ihdr[8] = 8; ihdr[9] = 2; ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0;
  const stride = w * 3;
  const raw = Buffer.alloc((stride + 1) * h);
  for (let y = 0; y < h; y++) {
    raw[y * (stride + 1)] = 0;
    rgb.copy(raw, y * (stride + 1) + 1, y * stride, (y + 1) * stride);
  }
  const sig = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
  return Buffer.concat([sig, chunk("IHDR", ihdr),
    chunk("IDAT", zlib.deflateSync(raw, { level: 6 })), chunk("IEND", Buffer.alloc(0))]);
}

/* Integer pixel-replication from src buffer to native 1920x1080 RGB.
 * indexed palette: 1 byte/pixel -> palette lookup. rgb: 3 bytes/pixel. */
function scaleToNative(buf, srcW, srcH, S, palette) {
  const out = Buffer.alloc(TARGET_W * TARGET_H * 3);
  const indexed = Array.isArray(palette);
  const stride = TARGET_W * 3;
  const oneRow = Buffer.alloc(stride);
  for (let sy = 0; sy < srcH; sy++) {
    oneRow.fill(0);
    for (let sx = 0; sx < srcW; sx++) {
      let r, g, b;
      if (indexed) {
        const idx = buf[sy * srcW + sx];
        const c = palette[idx]; r = c[0]; g = c[1]; b = c[2];
      } else {
        const i = (sy * srcW + sx) * 3; r = buf[i]; g = buf[i + 1]; b = buf[i + 2];
      }
      for (let k = 0; k < S; k++) {
        const p = (sx * S + k) * 3;
        oneRow[p] = r; oneRow[p + 1] = g; oneRow[p + 2] = b;
      }
    }
    for (let ky = 0; ky < S; ky++) oneRow.copy(out, (sy * S + ky) * stride, 0, stride);
  }
  return out;
}

function sha(buf) { return crypto.createHash("sha256").update(buf).digest("hex"); }

function main() {
  const args = process.argv.slice(2);
  const [rendererPath, outDir, mode, swArg, shArg, paletteArg] = args;
  const R = require(path.resolve(rendererPath));
  const srcW = parseInt(swArg, 10), srcH = parseInt(shArg, 10);
  const S = TARGET_W / srcW;
  if (!Number.isInteger(S) || srcW * S !== TARGET_W || srcH * S !== TARGET_H) {
    console.error("non-integer scale", { srcW, srcH, S }); process.exit(2);
  }
  let palette = null;
  if (paletteArg !== "rgb") palette = JSON.parse(paletteArg);
  const SEED = R.SEED;
  const framesDir = path.join(outDir, "frames");
  fs.mkdirSync(framesDir, { recursive: true });

  function renderOne(n) {
    const buf = R.renderFrame(n, SEED);       // FROZEN pure function, unchanged
    const native = scaleToNative(buf, srcW, srcH, S, palette);
    const png = encodePNG(native, TARGET_W, TARGET_H);
    const name = "f" + String(n).padStart(4, "0") + ".png";
    fs.writeFileSync(path.join(framesDir, name), png);
    return sha(png);
  }

  if (mode === "full") {
    const hashes = {};
    for (let n = 0; n < FRAMES; n++) hashes[String(n).padStart(4, "0")] = renderOne(n);
    fs.writeFileSync(path.join(framesDir, "frame_hashes.json"), JSON.stringify({
      seed: SEED, fps: 30, frames: FRAMES, resolution: [TARGET_W, TARGET_H],
      source_resolution: [srcW, srcH], geometry_scale: S,
      renderer: "frozen-original-renderFrame + integer-geometry-scale@1.0.0",
      hashes
    }, null, 1));
    console.log(JSON.stringify({ mode: "full", frames: FRAMES, resolution: [TARGET_W, TARGET_H], scale: S, ok: true }));
  } else if (mode === "batch") {
    const list = args[6].split(",").map(Number);
    const out = {};
    for (const n of list) out[n] = renderOne(n);
    console.log(JSON.stringify({ mode: "batch", scale: S, hashes: out }));
  } else {
    console.error("usage: native_scale_render.js <renderer.js> <outdir> full|batch <srcW> <srcH> <palette|rgb> [n,n,..]");
    process.exit(2);
  }
}
main();
