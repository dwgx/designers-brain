/*
 * UI-03 executable checks — run with:  node fixture/run_checks.js
 *
 * Produces JSON on stdout: { behavior: [...], semantics: [...], summary: {...} }
 * Exit 0 iff every check passes; nonzero otherwise.
 *
 * Layer discipline:
 *   - "behavior"  checks the reducer (click increments / keyboard activates /
 *                  disabled blocks). This is FUNCTIONAL correctness, in the
 *                  WebArena sense (a programmatic property of resulting state),
 *                  NOT visual similarity and NOT human satisfaction.
 *   - "semantics" checks the static HTML contract (role / aria-pressed /
 *                  accessible name) mechanically via parsing, NOT by eyeballing
 *                  a screenshot.
 * Neither layer claims aesthetic quality, user-goal completion of a user goal, or
 * human validation. Those are separate rows in the verification matrix.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');
const CB = require('./component.js');

const results = { behavior: [], semantics: [], summary: {} };
function rec(layer, id, ok, detail) {
  results[layer].push({ id, ok: !!ok, detail });
}

/* ---------------- Behavior layer ---------------- */
// B1: pointer activation increments count by exactly 1 and toggles pressed.
{
  let s = CB.initialState();
  const before = s.count;
  s = CB.reduce(s, { type: 'activate', via: 'pointer' });
  rec('behavior', 'B1_pointer_click_increments',
      s.count === before + 1 && s.pressed === true,
      `count ${before}->${s.count}, pressed=${s.pressed}`);
}
// B2: keyboard activation (Enter/Space path) increments by exactly 1 too.
{
  let s = CB.initialState();
  s = CB.reduce(s, { type: 'activate', via: 'keyboard' });
  rec('behavior', 'B2_keyboard_activates',
      s.count === 1 && s.pressed === true,
      `count=${s.count}, pressed=${s.pressed}`);
}
// B3: disabled state blocks BOTH pointer and keyboard activation.
{
  let s = CB.initialState({ disabled: true });
  const snap = JSON.stringify(s);
  s = CB.reduce(s, { type: 'activate', via: 'pointer' });
  s = CB.reduce(s, { type: 'activate', via: 'keyboard' });
  rec('behavior', 'B3_disabled_blocks_activation',
      JSON.stringify(s) === snap && s.count === 0 && s.pressed === false,
      `state unchanged=${JSON.stringify(s) === snap}, count=${s.count}`);
}
// B4: re-enabling restores activation; disabled is not a permanent latch.
{
  let s = CB.initialState({ disabled: true });
  s = CB.reduce(s, { type: 'setDisabled', value: false });
  s = CB.reduce(s, { type: 'activate', via: 'pointer' });
  rec('behavior', 'B4_reenable_restores_activation',
      s.count === 1 && s.disabled === false,
      `count=${s.count}, disabled=${s.disabled}`);
}
// B5: unknown/invalid action is a no-op (guards against false positives).
{
  let s = CB.initialState();
  const snap = JSON.stringify(s);
  s = CB.reduce(s, { type: 'activate', via: 'telepathy' });
  rec('behavior', 'B5_invalid_action_noop',
      JSON.stringify(s) === snap,
      `unchanged=${JSON.stringify(s) === snap}`);
}

/* ---------------- Semantics layer (parsed static target) ---------------- */
// Python's stdlib HTMLParser ignores comments and treats script/style as raw
// text. This fixture-level static parse is not an HTML5 accessibility tree;
// run_visual.py separately checks the browser's real DOM and input path.
const arg = process.argv.indexOf('--html');
const htmlPath = arg >= 0 ? process.argv[arg + 1] : path.join(__dirname, 'index.html');
const html = fs.readFileSync(htmlPath, 'utf8');
const parser = String.raw`
import json,sys
from html.parser import HTMLParser
class P(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True); self.stack=[]; self.nodes=[]
 def handle_starttag(self,tag,attrs):
  n={'tag':tag,'attrs':dict(attrs),'text':''}; self.nodes.append(n)
  if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}: self.stack.append(n)
 def handle_startendtag(self,tag,attrs):
  self.handle_starttag(tag,attrs); self.handle_endtag(tag)
 def handle_endtag(self,tag):
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i]['tag']==tag: del self.stack[i:]; break
 def handle_data(self,data):
  if any(n['tag'] in {'script','style','template'} for n in self.stack): return
  for n in self.stack: n['text']+=data
p=P(); p.feed(sys.stdin.read()); p.close()
print(json.dumps({k:[n for n in p.nodes if n['attrs'].get('id')==k] for k in ['counter','count']}))
`;
const parsed = spawnSync(process.env.UI_PYTHON || 'python', ['-c', parser],
                         { input: html, encoding: 'utf8', timeout: 15000 });
let dom = {};
try {
  if (parsed.error || parsed.status !== 0) throw new Error(parsed.error || parsed.stderr);
  dom = JSON.parse(parsed.stdout);
} catch (e) { results.static_parse_error = String(e); }
const controls = dom.counter || [], outputs = dom.count || [];
const button = controls.length === 1 ? controls[0] : null;
const output = outputs.length === 1 ? outputs[0] : null;
const a = button ? button.attrs : {};
rec('semantics', 'S1_role_button',
    !!button && button.tag === 'button' && a.type === 'button',
    `unique #counter count=${controls.length}, tag=${button?.tag}, type=${a.type}`);
rec('semantics', 'S2_aria_pressed_present', a['aria-pressed'] === 'false',
    `target aria-pressed=${a['aria-pressed']}`);
rec('semantics', 'S3_accessible_name_present',
    a['aria-label'] === CB.ACCESSIBLE_NAME && !!a['aria-label']?.trim(),
    `target aria-label=${a['aria-label']}`);
rec('semantics', 'S4_live_output_present',
    !!output && output.tag === 'output' && output.attrs['aria-live'] === 'polite',
    `unique #count count=${outputs.length}, tag=${output?.tag}`);
rec('semantics', 'S5_visible_text_label',
    !!button && button.tag === 'button' && button.text.trim() === 'Add one',
    `parsed target text=${button?.text.trim()}`);

/* ---------------- Summary ---------------- */
const all = [...results.behavior, ...results.semantics];
results.summary = {
  total: all.length,
  passed: all.filter(r => r.ok).length,
  failed: all.filter(r => !r.ok).length,
  behavior_total: results.behavior.length,
  behavior_passed: results.behavior.filter(r => r.ok).length,
  semantics_total: results.semantics.length,
  semantics_passed: results.semantics.filter(r => r.ok).length,
  node: process.version,
  cwd: '.' // portable public result; exact command cwd belongs in the local run log
};

process.stdout.write(JSON.stringify(results, null, 2) + '\n');
process.exit(results.summary.failed === 0 ? 0 : 1);
