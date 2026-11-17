# Designers_Brain

> 本文件为翻译版；以英文正本为准（可能滞后于最新改动）。
Translation update: 2026-11-15 — learning navigation, capability scope and host-specific loading; historical counts retained.

[English](README.md) · 中文 · [日本語](README.ja.md)

> **为设计师而生的大脑。** 把艺术家与设计师的视觉语言，经深度研究蒸馏为可组合、可验证的模块——并打包成一个**先问再设计**的 agent skill（技能包）。

[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE-CODE)

## 这是什么

把这个仓库交给一个 AI agent，它就会变成一位设计顾问：先问对问题，从已蒸馏的库中推荐风格，组合前先查冲突，产出带证据的结果——图像提示词、10 秒网页动画，或 Blender 任务书。

内容一览：

- **76 份画家档案**（达·芬奇、米开朗基罗、梵高、莫奈、毕加索、塞尚、马蒂斯、葛饰北斋、卡拉瓦乔、维米尔、丢勒等）——每份约 300–600 行证据、2044 条带来源引文、739 件来源图像：**701 件公有领域 / CC0 ＋ 38 件开放许可、须逐张署名**（见 [NOTICE.md](NOTICE.md)）。*（PRE 里程碑口径，保留备查：62 份 / 1613 条 / 618 件——原先「图像全部为公有领域」的说法对其中 38 件不成立。）*
- **76 张可组合模块卡** + **15 张动态图形风格卡**（10 秒动画骨架）。*（PRE：62 张。）*
- **跨模块规则**：18 条冲突条目（C-01–C-18）+ 组合规则 N1–N9。
- **一个 skill**（`skills/designers-brain/`），实现「先问再设计」的顾问协议。
- **带机械检查的实验**：风格迁移矩阵（E 系列）与三条端到端动画管线（网页 ×2、Blender ×1）。

- **76 条学习路径与 65 份新增纯风格候选**，包含来源声明、反例与[具体阅读路线](knowledge/domains/painters/learning/INDEX.md)；另链接 11 个既有风格章节，保留原卡为正本。
- **按证据范围划分的[能力矩阵](knowledge/CAPABILITIES.md)**：图像、网页动画、Blender 分开判断，区分历史成果、局部实现和未验证项。

## 快速开始

### 1. 加载 skill

打开仓库，让 agent 读取 [`skills/designers-brain/SKILL.md`](skills/designers-brain/SKILL.md)。使用实际 skill 的解析器定位仓库，再读取引用：

```text
python -X utf8 -B skills/designers-brain/resolve_repo.py --json
python -X utf8 -B docs/skill/_selfcheck.py --repo-only
```

OMP 使用 `skills.customDirectories` 指向这份 checkout 的 **`skills` 父目录**。具体配置、`skill://` 读取与来源核对见[本地加载说明](docs/skill/local-usage.md)。其他宿主使用各自的发现/安装机制；一个宿主的 junction 不等于为所有宿主安装。

随后给出具体需求，例如：「帮我选风格并准备一张……的海报」。skill 会补齐必要信息，并先读能力矩阵再承诺输出路线。宿主发现、自动选择和实际渲染分别记录验证结果。

### 2. 浏览知识

- 从 [`knowledge/INDEX.md`](knowledge/INDEX.md) 开始（完整来源索引）。
- 画家模块：[`knowledge/domains/painters/modules/`](knowledge/domains/painters/modules/)——每张卡都可直接组合进提示词。
- 动态风格：[`knowledge/domains/motion-graphics/`](knowledge/domains/motion-graphics/)。
- 组合规则：[`knowledge/cross/conflicts.md`](knowledge/cross/conflicts.md)。

### 3. 复现一个实验

```bash
# module-card verbatim check (228 checks — 76 张卡 × §8.1/§8.2/§4)
python knowledge/domains/painters/modules/_extract.py --check

# image experiment verification (example: composition batch)
cd experiments/E2_t1 && python _verify_e2.py
```

## 工作原理

1. **深度研究**——每位艺术家、每个领域都以一手来源为准；每条论断都带证据分级（`[自述]/[史料]/[研究]/[归纳]/[推测]`）。
2. **蒸馏**——证据压缩为可执行的操作规则：可组合、可调节、可机械检查的模块。
3. **验证**——记录具体输出路线、实现、检查与限制。能力矩阵区分 supported、conditional、unsupported、untested；历史验证器保留原范围。
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

2026 年 11 月研究更新已整合学习路径、纯风格候选、带来源的导航，以及逐输出能力状态。已有证据能支持什么，见[能力矩阵](knowledge/CAPABILITIES.md)。练习建议和风格文字本身不能证明图像生成、浏览器渲染、Blender 执行或实际学习收益。

10 月 PRE 里程碑作为历史记录保留。当前发布的正式接受以发布说明中绑定的准确版本为准；工作树或本地提交本身不代表已发布。后续研究方向见 [`docs/ROADMAP.md`](docs/ROADMAP.md)。

## 许可

内容与文档：[CC BY 4.0](LICENSE)。代码：[MIT](LICENSE-CODE)。第三方：见 [NOTICE.md](NOTICE.md)。

图像许可**并不统一**：739 件来源图像中 701 件为公有领域或 CC0，38 件为开放许可（CC BY 3.0/4.0、CC BY-SA 3.0/4.0、ColBase 规约、台北故宫开放资料），再分发时**必须保留逐张署名行**。类别与署名要求见 [NOTICE.md](NOTICE.md#images-not-pdcc0-38)。
