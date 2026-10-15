/* =============================================================================
   render_audio.js —— 驱动 audio.html：OfflineAudioContext 离线渲染 → audio/score.wav
   用法：node render_audio.js
   ============================================================================= */
"use strict";
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const ROOT = __dirname;
const EXE = process.env.CHROME_BIN ||
  'C:/Users/dwgx1/.cache/puppeteer/chrome-headless-shell/win64-153.0.8010.36/chrome-headless-shell-win64/chrome-headless-shell.exe';

(async () => {
  const t0 = Date.now();
  const browser = await puppeteer.launch({
    executablePath: EXE,
    headless: 'shell',
    args: ['--force-color-profile=srgb', '--disable-gpu', '--mute-audio'],
    defaultViewport: { width: 800, height: 600 }
  });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });

  await page.goto('file:///' + path.join(ROOT, 'audio.html').replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForFunction('window.__ready === true', { timeout: 15000 });
  const res = await page.evaluate(async () => await window.renderScore());
  await browser.close();

  fs.mkdirSync(path.join(ROOT, 'audio'), { recursive: true });
  const out = path.join(ROOT, 'audio', 'score.wav');
  fs.writeFileSync(out, Buffer.from(res.base64, 'base64'));
  const dt = ((Date.now() - t0)/1000).toFixed(1);
  console.log(JSON.stringify({
    wav: out, bytes: res.bytes, seconds: res.seconds,
    peakBeforeNormalize: res.peak, gainApplied: res.gain, errors: errors, seconds_run: Number(dt)
  }));
  if (errors.length) process.exit(1);
})();
