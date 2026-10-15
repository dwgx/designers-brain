/* =============================================================================
   render_audio.js —— 在 headless Chrome 里跑 OfflineAudioContext 合成音轨 -> wav
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
    executablePath: EXE, headless: 'shell',
    args: ['--mute-audio', '--disable-gpu', '--disable-extensions']
  });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  await page.goto('file:///' + path.join(ROOT, 'audio.html').replace(/\\/g, '/'), { waitUntil: 'load' });
  const res = await page.evaluate(() => window.synthScore());
  await browser.close();
  fs.mkdirSync(path.join(ROOT, 'audio'), { recursive: true });
  const out = path.join(ROOT, 'audio', 'score.wav');
  fs.writeFileSync(out, Buffer.from(res.b64, 'base64'));
  console.log(JSON.stringify({
    wav: out, bytes: fs.statSync(out).size, samples: res.samples,
    sampleRate: res.sampleRate, channels: res.channels,
    peakBeforeLimit: res.peak, limitGain: res.gain,
    errors, seconds: Number(((Date.now()-t0)/1000).toFixed(1))
  }));
  if (errors.length) process.exit(1);
})();
