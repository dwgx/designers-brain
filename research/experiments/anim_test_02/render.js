/* =============================================================================
   render.js —— 逐帧捕获驱动（B-17 / anim_test_02）
   契约：页面暴露 window.seek(frame) 纯函数；本脚本只做「seek(f) → screenshot」。
   用法：
     node render.js --keys             # 6 张关键帧 0/50/100/150/200/250 -> key/
     node render.js --frames           # 全片 300 帧 -> frames/
     node render.js --probe 0,150,299  # 指定帧 -> checks/probe/
     node render.js --rerun 299,150,0  # 重渲同帧（乱序）-> checks/rerun/（确定性 P0）
   ============================================================================= */
"use strict";
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const ROOT = __dirname;
const EXE = process.env.CHROME_BIN ||
  'C:/Users/dwgx1/.cache/puppeteer/chrome-headless-shell/win64-153.0.8010.36/chrome-headless-shell-win64/chrome-headless-shell.exe';
const KEY_FRAMES = [0, 50, 100, 150, 200, 250];

const argv = process.argv.slice(2);
function argVal(name, def){
  const i = argv.indexOf(name);
  return (i >= 0 && argv[i+1] && !argv[i+1].startsWith('--')) ? argv[i+1] : def;
}
const MODE =
  argv.includes('--keys')   ? 'keys'   :
  argv.includes('--frames') ? 'frames' :
  argv.includes('--probe')  ? 'probe'  :
  argv.includes('--rerun')  ? 'rerun'  : null;

function frameList(){
  if (MODE === 'keys')  return { list: KEY_FRAMES, dir: 'key', prefix: 'k' };
  if (MODE === 'frames'){ const l = []; for (let f=0; f<300; f++) l.push(f); return { list: l, dir: 'frames', prefix: 'f' }; }
  if (MODE === 'probe') return { list: argVal('--probe','0').split(',').map(Number), dir: 'checks/probe', prefix: 'p' };
  if (MODE === 'rerun') return { list: argVal('--rerun','0').split(',').map(Number), dir: 'checks/rerun', prefix: 'f' };
  return null;
}
function pad(f){ return String(f).padStart(4, '0'); }

(async () => {
  const job = frameList();
  if (!job){ console.error('usage: node render.js --keys | --frames | --probe a,b,c | --rerun a,b,c'); process.exit(2); }
  const outDir = path.join(ROOT, job.dir);
  fs.mkdirSync(outDir, { recursive: true });

  const t0 = Date.now();
  const browser = await puppeteer.launch({
    executablePath: EXE,
    headless: 'shell',
    args: [
      '--force-color-profile=srgb',
      '--hide-scrollbars',
      '--disable-gpu',
      '--disable-lcd-text',
      '--force-device-scale-factor=1',
      '--disable-extensions',
      '--mute-audio'
    ],
    defaultViewport: { width: 1920, height: 1080, deviceScaleFactor: 1 }
  });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });

  const url = 'file:///' + path.join(ROOT, 'index.html').replace(/\\/g, '/');
  await page.goto(url, { waitUntil: 'load' });
  await page.waitForFunction('window.__ready === true', { timeout: 15000 });
  const meta = await page.evaluate(() => window.__meta);
  const selftest = await page.evaluate(() => window.__selftest);
  const speed = await page.evaluate(() => window.__speed);

  for (const f of job.list){
    await page.evaluate(fr => window.seek(fr), f);
    await page.screenshot({
      path: path.join(outDir, `${job.prefix}${pad(f)}.png`),
      type: 'png',
      captureBeyondViewport: false
    });
  }
  await browser.close();
  const dt = ((Date.now() - t0)/1000).toFixed(1);
  console.log(JSON.stringify({
    mode: MODE, frames: job.list.length, dir: job.dir,
    first: job.list[0], last: job.list[job.list.length-1],
    meta, selftest, speed, errors, seconds: Number(dt)
  }));
  if (errors.length) process.exit(1);
})();
