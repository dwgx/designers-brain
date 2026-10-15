# Designers_Brain

> 本文件为翻译版；以英文正本为准（可能滞后于最新改动）。
Translation baseline: README/docs as of 2026-10-15 (commit 534924e+)

[English](README.md) · 中文 · [日本語](README.ja.md)

> **为设计师而生的大脑。** 把艺术家与设计师的视觉语言，经深度研究蒸馏为可组合、可验证的模块——并打包成一个**先问再设计**的 agent skill（技能包）。

[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE-CODE)

## 这是什么

把这个仓库交给一个 AI agent，它就会变成一位设计顾问：先问对问题，从已蒸馏的库中推荐风格，组合前先查冲突，产出带证据的结果——图像提示词、10 秒网页动画，或 Blender 任务书。

内容一览：

- **11 份画家档案**（达·芬奇、米开朗基罗、梵高、莫奈、毕加索、塞尚、马蒂斯、葛饰北斋、卡拉瓦乔、维米尔、丢勒）——每份约 300 行证据、126 条带来源引文、33 件公有领域作品。
- **11 张可组合模块卡** + **15 张动态图形风格卡**（10 秒动画骨架）。
- **跨模块规则**：18 条冲突条目（C-01–C-18）+ 组合规则 N1–N9。
- **一个 skill**（`skills/designers-brain/`），实现「先问再设计」的顾问协议。
- **带机械检查的实验**：风格迁移矩阵（E 系列）与三条端到端动画管线（网页 ×2、Blender ×1）。

## 快速开始

### 1. 加载 skill

```bash
# Claude Code / Codex / omp — activate via junction (no copy):
# (Windows PowerShell)
New-Item -ItemType Junction -Path "$HOME\.claude\skills\designers-brain" `
  -Target "<path-to-repo>\skills\designers-brain"
```

然后直接提设计需求即可：*「帮我挑一种风格，做一张……的海报」*——skill 会在设计/替换类请求上触发。打包用的插件清单也已随附（`.claude-plugin/`、`.codex-plugin/`、`.agents/plugins/`）。

### 2. 浏览知识

- 从 [`knowledge/INDEX.md`](knowledge/INDEX.md) 开始（完整来源索引）。
- 画家模块：[`knowledge/domains/painters/modules/`](knowledge/domains/painters/modules/)——每张卡都可直接组合进提示词。
- 动态风格：[`knowledge/domains/motion-graphics/`](knowledge/domains/motion-graphics/)。
- 组合规则：[`knowledge/cross/conflicts.md`](knowledge/cross/conflicts.md)。

### 3. 复现一个实验

```bash
# module-card verbatim check (33 checks)
python knowledge/domains/painters/modules/_extract.py --check

# image experiment verification (example: composition batch)
cd experiments/E2_t1 && python _verify_e2.py
```

## 工作原理

1. **深度研究**——每位艺术家、每个领域都以一手来源为准；每条论断都带证据分级（`[自述]/[史料]/[研究]/[归纳]/[推测]`）。
2. **蒸馏**——证据压缩为可执行的操作规则：可组合、可调节、可机械检查的模块。
3. **验证**——每项能力都端到端跑通后才对外声称；验证器随产物一起交付。
4. **AI 运维**——仓库由 AI agent 在明确的协议下运维（`docs/WORKFLOW.md`、`docs/PROTOCOLS.md`）；工作状态放在 `ops/GOALS.md`。

## 仓库地图

```
knowledge/    distilled product (domains, cross rules, agent-art pipelines, index)
experiments/  evidence runs (E-series, animation tests) with scripts & verifiers
skills/       designers-brain — the consumable agent skill
docs/         architecture, workflow, protocols, roadmap (+ zh-CN / ja translations)
ops/          GOALS.md (work queue) · OPS-LOG.md (append-only log)
templates/    module / style-card / determinism / design-brief templates
```

## 演示产物

- 动画管线：`experiments/anim_test_01/out.mp4` · `anim_test_02/out.mp4` · `anim_test_03_blender/out.mp4`
- 风格分离对照：`experiments/E1_t1b/compare_all_t1b.png`
- 组合总表：`experiments/E2_t1/sheet_all_e2.png`
- skill 走查（咖啡馆形象，3 个方向）：`docs/skill/walkthrough_01/candidates/compare_candidates.png`

## 状态

**PRE 里程碑完成**（2026-10）：前两个领域已蒸馏，skill 已构建并通过盲测，三条管线端到端验证通过。下一步：领域扩展、强度扫描、人工打分——见 [`docs/ROADMAP.md`](docs/ROADMAP.md)。

## 许可

内容与文档：[CC BY 4.0](LICENSE)。代码：[MIT](LICENSE-CODE)。第三方：见 [NOTICE.md](NOTICE.md)。
