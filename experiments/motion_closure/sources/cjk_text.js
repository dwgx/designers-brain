"use strict";
const path = require("path");
const {spawnSync} = require("child_process");
const crypto = require("crypto");
const fs = require("fs");
function loadGlyphs(requests) {
  const p = spawnSync(process.env.MOTION_PYTHON || "python",
    ["-B", path.join(__dirname, "cjk_text.py")],
    {input: JSON.stringify(requests), encoding: "utf8", maxBuffer: 4*1024*1024});
  if (p.error || p.status !== 0) throw new Error("CJK font rasterization failed: " + (p.error || p.stderr));
  const result = JSON.parse(p.stdout);
  result.evidence.js_helper_sha256 = crypto.createHash("sha256").update(fs.readFileSync(__filename)).digest("hex");
  for (const glyph of Object.values(result.glyphs)) {
    glyph.alpha = Buffer.from(glyph.alpha, "base64");
    if (glyph.alpha.length !== glyph.width*glyph.height) throw new Error("Invalid text alpha mask");
  }
  return result;
}
function drawIndexed(buf, width, height, glyph, ox, oy, color) {
  ox=Math.round(ox); oy=Math.round(oy);
  for(let y=0;y<glyph.height;y++) for(let x=0;x<glyph.width;x++) {
    const xx=ox+x, yy=oy+y;
    // Preserve the scene's exact finite palette; text is thresholded at native resolution.
    if(xx>=0&&xx<width&&yy>=0&&yy<height&&glyph.alpha[y*glyph.width+x]>=128) buf[yy*width+xx]=color;
  }
}
function drawRGB(buf, width, height, glyph, ox, oy, color, opacity=1) {
  ox=Math.round(ox); oy=Math.round(oy);
  for(let y=0;y<glyph.height;y++) for(let x=0;x<glyph.width;x++) {
    const xx=ox+x, yy=oy+y, a=glyph.alpha[y*glyph.width+x]/255*opacity;
    if(xx<0||xx>=width||yy<0||yy>=height||a<=0) continue;
    const rgb=typeof color==="function"?color(x,y,glyph.width,glyph.height):color;
    const at=(yy*width+xx)*3;
    for(let k=0;k<3;k++) buf[at+k]=Math.round(buf[at+k]*(1-a)+rgb[k]*a);
  }
}
module.exports={loadGlyphs,drawIndexed,drawRGB};
