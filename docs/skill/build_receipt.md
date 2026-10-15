# build_receipt — S-03 建包落地与激活（`skills/designers-brain`）

> 日期：2026-10-15｜执行：SkillBuild（S-03 / wave10）｜规格：`docs/skill/skill_spec.md` v0.2（§1.2 布局 / §1.3 激活 / §1.4 打包件 / §5.3 域注册表 / §1.6 自检）
> 口径：本回执只记事实与跑过的命令**原样输出**；未跑过的不写。完成情况以本文件为准（ops/GOALS.md 归主脑，未动）。
> 纪律：4 条 junction **逐条先核「目标不存在」再创建**（本次均不存在，无覆盖）；draft 保留为历史草案，定稿在 `skills/designers-brain/SKILL.md`。

## 1. 产物清单

| # | 产物 | 路径 | 说明 |
|---|---|---|---|
| 1 | skill 入口 | `skills/designers-brain/SKILL.md` | 106 行（<500）；frontmatter `name=designers-brain` 与目录同名；「⏳ 规划」字样已改实路径、落位行已更新（与草案仅 2 处差异，见 2.1） |
| 2 | 指针 ×9 | `skills/designers-brain/references/` | painter-modules / mg-cards / conflicts / output-forms / pipelines / evidence / review / question-bank / direction-protocol（各只写「去哪读什么」+ REPO 相对路径，不复制内容） |
| 3 | 域注册表 | `skills/designers-brain/domains.yaml` | painter(11) + mg-motion(15)；含 count 计数规则注记 |
| 4 | 技能级 UI 元数据 | `skills/designers-brain/agents/openai.yaml` | 按规格 §1.4 格式（display_name / short_description / default_prompt） |
| 5 | 打包件 ×3（仓库级） | `.claude-plugin/plugin.json`、`.codex-plugin/plugin.json`、`.agents/plugins/marketplace.json` | 按规格 §1.4 样例骨架；安装路径未在本机验证 [UNVERIFIED] |
| 6 | junction ×4 | `.agents/skills/designers-brain`（仓库内）+ `~/.agents/skills/designers-brain`、`~/.claude/skills/designers-brain`、`~/.codex/skills/designers-brain`（用户级） | 全部 → `D:\Project\Designers_Brain\skills\designers-brain`；PowerShell `New-Item -ItemType Junction` |
| 7 | gate 文件模板 | `templates/design_brief.md` | 意图 / 非目标 / 约束 / 用户选择原话 / 假设清单（内容+默认+错了的代价）/ 批准范围 |
| 8 | 自检扩展 | `docs/skill/_selfcheck.py` | + junction 解析校验 + domains.yaml 校验；原功能（引用路径存在性 + frontmatter）保留 |

## 2. 验证输出（原样）

### 2.1 定稿差异（draft → 落位版；`diff` 输出，仅 2 处）

```diff
13c13
< > 草案 v0.2（2026-10-15；v0.1 初稿 + R1 并入 SkillEcosystem）｜落位目标：`D:/Project/Designers_Brain/skills/designers-brain/SKILL.md`（⏳ 规划）｜规格：`D:/Project/Designers_Brain/docs/skill/skill_spec.md`
---
> > v0.2（2026-10-15；v0.1 初稿 + R1 并入 SkillEcosystem）｜落位：`D:/Project/Designers_Brain/skills/designers-brain/SKILL.md`｜规格：`D:/Project/Designers_Brain/docs/skill/skill_spec.md`
100c100
< （打包后：以上经由 `references/` 指针文件路由，指针清单见规格 §5.2；新域（非画家）插拔按规格 §5.3 契约登记 `domains.yaml`——两者均 ⏳ 规划。）
---
> （以上经由本包 `references/` 的 9 个指针文件路由，指针清单见规格 §5.2；新域（非画家）插拔按规格 §5.3 契约登记 `domains.yaml`——两者均已落位。）
```

### 2.2 包文件清单 + 格式校验

```
== 包文件清单（skills/designers-brain）==
  skills/designers-brain/SKILL.md  (9223 B)
  skills/designers-brain/domains.yaml  (1428 B)
  skills/designers-brain/agents/openai.yaml  (186 B)
  skills/designers-brain/references/conflicts.md  (498 B)
  skills/designers-brain/references/direction-protocol.md  (740 B)
  skills/designers-brain/references/evidence.md  (892 B)
  skills/designers-brain/references/mg-cards.md  (744 B)
  skills/designers-brain/references/output-forms.md  (700 B)
  skills/designers-brain/references/painter-modules.md  (856 B)
  skills/designers-brain/references/pipelines.md  (601 B)
  skills/designers-brain/references/question-bank.md  (523 B)
  skills/designers-brain/references/review.md  (398 B)

JSON OK: .claude-plugin/plugin.json
JSON OK: .codex-plugin/plugin.json
JSON OK: .agents/plugins/marketplace.json
YAML OK: skills/designers-brain/domains.yaml
YAML OK: skills/designers-brain/agents/openai.yaml
SKILL.md 行数 = 106 (<500)
```

```
$ ls -l templates/design_brief.md .claude-plugin/plugin.json .codex-plugin/plugin.json .agents/plugins/marketplace.json docs/skill/_selfcheck.py
-rwxrwxrwx 1 somebody somegroup   388 Oct 15 21:15 .agents/plugins/marketplace.json
-rwxrwxrwx 1 somebody somegroup   201 Oct 15 21:15 .claude-plugin/plugin.json
-rwxrwxrwx 1 somebody somegroup   355 Oct 15 21:15 .codex-plugin/plugin.json
-rwxrwxrwx 1 somebody somegroup 14273 Oct 15 21:16 docs/skill/_selfcheck.py
-rwxrwxrwx 1 somebody somegroup  1303 Oct 15 21:15 templates/design_brief.md
```

### 2.3 junction ×4（创建 + 实况 + 元数据）

创建命令（PowerShell；每条先 `Test-Path` 核目标不存在，已存在则停、不覆盖——本次 4 条均不存在）：

```powershell
New-Item -ItemType Junction -Path "<目标>" -Target "D:\Project\Designers_Brain\skills\designers-brain"
```

实况（`ls -ld` + 经 junction 读 `SKILL.md`，原样）：

```
lrwxrwxrwx 1 somebody somegroup 0 Oct 15 21:15 .agents/skills/designers-brain -> D:\Project\Designers_Brain\skills\designers-brain
-rwxrwxrwx 1 somebody somegroup 9223 Oct 15 21:14 .agents/skills/designers-brain/SKILL.md
lrwxrwxrwx 1 somebody somegroup 0 Oct 15 21:15 C:\Users\dwgx1/.agents/skills/designers-brain -> D:\Project\Designers_Brain\skills\designers-brain
-rwxrwxrwx 1 somebody somegroup 9223 Oct 15 21:14 C:\Users\dwgx1/.agents/skills/designers-brain/SKILL.md
lrwxrwxrwx 1 somebody somegroup 0 Oct 15 21:15 C:\Users\dwgx1/.claude/skills/designers-brain -> D:\Project\Designers_Brain\skills\designers-brain
-rwxrwxrwx 1 somebody somegroup 9223 Oct 15 21:14 C:\Users\dwgx1/.claude/skills/designers-brain/SKILL.md
lrwxrwxrwx 1 somebody somegroup 0 Oct 15 21:15 C:\Users\dwgx1/.codex/skills/designers-brain -> D:\Project\Designers_Brain\skills\designers-brain
-rwxrwxrwx 1 somebody somegroup 9223 Oct 15 21:14 C:\Users\dwgx1/.codex/skills/designers-brain/SKILL.md
```

Windows 元数据（PowerShell `Get-Item -Force`，原样）：

```
FullName : D:\Project\Designers_Brain\.agents\skills\designers-brain
LinkType : Junction
Target   : D:\Project\Designers_Brain\skills\designers-brain

FullName : C:\Users\dwgx1\.agents\skills\designers-brain
LinkType : Junction
Target   : D:\Project\Designers_Brain\skills\designers-brain

FullName : C:\Users\dwgx1\.claude\skills\designers-brain
LinkType : Junction
Target   : D:\Project\Designers_Brain\skills\designers-brain

FullName : C:\Users\dwgx1\.codex\skills\designers-brain
LinkType : Junction
Target   : D:\Project\Designers_Brain\skills\designers-brain
```

### 2.4 回归：`python knowledge/domains/painters/modules/_extract.py --check`（期望 33/33）

```
[da_vinci] §8.1 ok (1418c) · §8.2 ok (513c) · §4 ok (593c)
[michelangelo] §8.1 ok (1236c) · §8.2 ok (527c) · §4 ok (579c)
[van_gogh] §8.1 ok (1084c) · §8.2 ok (602c) · §4 ok (666c)
[monet] §8.1 ok (915c) · §8.2 ok (577c) · §4 ok (626c)
[picasso] §8.1 ok (1084c) · §8.2 ok (551c) · §4 ok (694c)
[cezanne] §8.1 ok (1290c) · §8.2 ok (618c) · §4 ok (651c)
[matisse] §8.1 ok (1006c) · §8.2 ok (1057c) · §4 ok (1023c)
[hokusai] §8.1 ok (1207c) · §8.2 ok (450c) · §4 ok (745c)
[caravaggio] §8.1 ok (1424c) · §8.2 ok (685c) · §4 ok (1257c)
[vermeer] §8.1 ok (1487c) · §8.2 ok (919c) · §4 ok (1152c)
[durer] §8.1 ok (1519c) · §8.2 ok (684c) · §4 ok (870c)
checks=33 ok=33 fail=0   # 11 卡 × §8.1/§8.2/§4 逐字比对
```

### 2.5 扩展后 `python docs/skill/_selfcheck.py`（期望 PASS）

```
== 文件 ==
  docs/skill/skill_spec.md  refs(unique)=59
  docs/skill/draft/SKILL.md  refs(unique)=16
  skills/designers-brain/SKILL.md  refs(unique)=16
  skills/designers-brain/domains.yaml  refs(unique)=9
  skills/designers-brain/agents/openai.yaml  refs(unique)=0
  templates/design_brief.md  refs(unique)=3
  skills/designers-brain/references/painter-modules.md  refs(unique)=5
  skills/designers-brain/references/mg-cards.md  refs(unique)=4
  skills/designers-brain/references/conflicts.md  refs(unique)=2
  skills/designers-brain/references/output-forms.md  refs(unique)=3
  skills/designers-brain/references/pipelines.md  refs(unique)=3
  skills/designers-brain/references/evidence.md  refs(unique)=7
  skills/designers-brain/references/review.md  refs(unique)=1
  skills/designers-brain/references/question-bank.md  refs(unique)=1
  skills/designers-brain/references/direction-protocol.md  refs(unique)=3

== 路径核验（仓库既有 + 包内）==
  checked=54 ok=54 fail=0
  （目录 13 / 文件 38 / 通配符 3）
    ok   agents/openai.yaml  [file]
    ok   domains.yaml  [file]
    ok   references/*.md  [glob(9)]
    ok   references/conflicts.md  [file]
    ok   references/direction-protocol.md  [file]
    ok   references/evidence.md  [file]
    ok   references/mg-cards.md  [file]
    ok   references/output-forms.md  [file]
    ok   references/painter-modules.md  [file]
    ok   references/pipelines.md  [file]
    ok   references/question-bank.md  [file]
    ok   references/review.md  [file]
    ok   knowledge/agent-art/blender/workflow.md  [file]
    ok   knowledge/domains/motion-graphics/cards/author_tutorial.md  [file]
    ok   knowledge/cross/image_channel.md  [file]
    ok   knowledge/domains/motion-graphics/cards/mg-styles-15_handbook.md  [file]
    ok   knowledge/cross/review_rubric.md  [file]
    ok   knowledge/domains/motion-graphics/cards/structure.md  [file]
    ok   knowledge/cross/conflicts.md  [file]
    ok   knowledge/agent-art/html/workflow.md  [file]
    ok   knowledge/cross/transfer_guide.md  [file]
    ok   knowledge/domains/painters/dossiers/  [dir]
    ok   experiments/  [dir]
    ok   experiments/E1_t1b/  [dir]
    ok   experiments/E1_t1c/  [dir]
    ok   experiments/E2_t1/  [dir]
    ok   experiments/anim_test_01/  [dir]
    ok   experiments/anim_test_02/  [dir]
    ok   experiments/anim_test_03_blender/  [dir]
    ok   experiments/design.md  [file]
    ok   knowledge/domains/motion-graphics/origin/  [dir]
    ok   knowledge/domains/motion-graphics/origin/提示词全文.md  [file]
    ok   knowledge/domains/painters/modules/  [dir]
    ok   knowledge/domains/painters/modules/*.md  [glob(12)]
    ok   knowledge/domains/painters/modules/README.md  [file]
    ok   knowledge/domains/painters/modules/_extract.py  [file]
    ok   docs/skill/_selfcheck.py  [file]
    ok   docs/skill/draft/SKILL.md  [file]
    ok   docs/skill/refs/design-packs/huashu-design_consultant_excerpts.md  [file]
    ok   docs/skill/refs/spec/  [dir]
    ok   docs/skill/refs/spec/claude-code_plugin_manifest_excerpt.md  [file]
    ok   docs/skill/refs/spec/codex_plugin_manifest_spec.md  [file]
    ok   docs/skill/refs/superpowers/brainstorming_SKILL.md  [file]
    ok   docs/skill/refs/superpowers/manifest_samples.md  [file]
    ok   docs/skill/skill_ecosystem.md  [file]
    ok   docs/skill/skill_spec.md  [file]
    ok   skills/*/SKILL.md  [glob(1)]
    ok   skills/designers-brain  [dir]
    ok   skills/designers-brain/  [dir]
    ok   skills/designers-brain/SKILL.md  [file]
    ok   skills/designers-brain/agents/openai.yaml  [file]
    ok   templates/design_brief.md  [file]
    ok   templates/determinism_contract.md  [file]
    ok   templates/style_card.md  [file]

== 规划路径（备选布局，不计失败）== planned=1
    ⏳ docs/skill/designers-brain/

== 机器级/打包件路径（状态核对）== ok=13 design-only=1 skip=1 fail=0
      ok .agents/plugins/marketplace.json  [file]
      ok .agents/skills  [dir]
      ok .agents/skills/  [dir]
      ok .agents/skills/designers-brain  [dir]
      ok .claude-plugin/plugin.json  [file]
      ok .claude/skills/*/SKILL.md  [glob(8)]
      ok .codex-plugin/plugin.json  [file]
       · ~/.agents/plugins/marketplace.json  [设计稿（未创建；非本包产物）]
      ok ~/.agents/skills  [dir]
      ok ~/.agents/skills/  [dir]
      ok ~/.agents/skills/designers-brain  [dir]
       ~ ~/.claude/skills/<name>/SKILL.md  [占位符]
      ok ~/.claude/skills/designers-brain  [dir]
      ok ~/.codex/skills  [dir]
      ok ~/.codex/skills/designers-brain  [dir]

== 示意形态（占位符，跳过）== schematic=6
    ~ references/...
    ~ research/...
    ~ experiments/<E-id>/design-brief.md
    ~ skills/...
    ~ skills/<name>/SKILL.md
    ~ templates/...

== frontmatter ==
  -- 落位版（skills/designers-brain/SKILL.md）--
  OK: name='designers-brain' (len=15, 小写/连字符=True, 首尾/连续连字符=True)
  OK: name 与父目录同名：'designers-brain' vs 'designers-brain' = True
  OK: description 长度=294 (≤1024)
  -- 草案（docs/skill/draft/SKILL.md；临时位，父目录同名要求以落位版为准）--
  OK: name='designers-brain' (len=15, 小写/连字符=True, 首尾/连续连字符=True)
  OK: description 长度=294 (≤1024)

== junction 解析（4 条；realpath == REPO/skills/designers-brain）== 4/4 ok
      ok .agents/skills/designers-brain  [realpath=D:\Project\Designers_Brain\skills\designers-brain]
      ok ~/.agents/skills/designers-brain  [realpath=D:\Project\Designers_Brain\skills\designers-brain]
      ok ~/.claude/skills/designers-brain  [realpath=D:\Project\Designers_Brain\skills\designers-brain]
      ok ~/.codex/skills/designers-brain  [realpath=D:\Project\Designers_Brain\skills\designers-brain]

== domains.yaml 校验（count == cards 目录实际数）==
      ok [painter] count=11 actual=11（knowledge/domains/painters/modules/*.md − README.md）
      ok [mg-motion] count=15 actual=15（knowledge/domains/motion-graphics/origin/ 01–15 号卡截图）

RESULT: PASS  (checked=54 fail=0 planned=1 · junctions=4/4 · domains=ok · harness_fail=0)
```

## 3. 复跑命令

```bash
python knowledge/domains/painters/modules/_extract.py --check   # 期望 checks=33 ok=33 fail=0
python docs/skill/_selfcheck.py                          # 期望 RESULT: PASS（含 junction 4/4 + domains ok）
ls ~/.agents/skills/designers-brain/SKILL.md                 # 其余 3 条 junction 同型（.claude / .codex / 仓库内）
```

## 4. 备注（边界与 [UNVERIFIED]）

- **打包件安装路径未在本机验证**（无 git；marketplace 分发暂不适用——规格 §1.4 口径）；三件套为「文件就位」设计。`~/.agents/plugins/marketplace.json`（个人级）为规格语义说明，未创建、非本包产物（自检以 `design-only` 列出）。
- **junction 激活口径**：本回执验证 = `realpath == REPO/skills/designers-brain`（规格 §1.6-1，逐条）；harness 实机「被发现」观察留待 S-04 盲测。
- **未动**：ops/GOALS.md / ops/OPS-LOG.md / 机器板 / draft（历史草案）/ 其它既有产物；本任务只新增/扩展 §1 清单所列文件。
