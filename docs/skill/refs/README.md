# refs — skill 生态调研 · 关键原文留档

> 调研日期: 2026-10-15 · 方法: GitHub API + raw.githubusercontent.com 直读（web_search 限流，未用）
> 主报告: [`../skill_ecosystem.md`](../skill_ecosystem.md)
> 用途: 保留少量关键文件的原文/摘录，供 Designers_Brain 后续建「设计顾问 skill」时逐字对照。

## 索引

| 文件 | 来源 | 内容 | 类型 |
|---|---|---|---|
| `spec/agentskills_specification.md` | https://agentskills.io/specification.md | Agent Skills 官方格式规范 | 全文 |
| `spec/anthropic_skill_best_practices.md` | obra/superpowers `skills/writing-skills/anthropic-best-practices.md` | 官方 skill 写作最佳实践（渐进披露三模式、description 写法） | 全文 |
| `spec/progressive_disclosure_client_guide_excerpt.md` | https://agentskills.io/client-implementation/adding-skills-support.md | 加载机制：三层披露 / 发现路径 / 激活方式 | 摘录 |
| `spec/claude-code_plugin_manifest_excerpt.md` | https://code.claude.com/docs/en/plugins-reference.md | Claude Code plugin.json `skills` 字段语义（加扫 / 默认发现） | 摘录 |
| `spec/codex_plugin_manifest_spec.md` | openai/plugins `.agents/skills/plugin-creator/references/plugin-json-spec.md` | Codex `.codex-plugin/plugin.json` + `.agents/plugins/marketplace.json` 规范 | 全文 |
| `superpowers/brainstorming_SKILL.md` | obra/superpowers `skills/brainstorming/` | 现行 brainstorming（提问协议核心） | 全文 |
| `superpowers/brainstorming_rebuild_spec.md` | obra/superpowers `docs/superpowers/specs/2026-10-05-*.md` | 2026-10 重写的设计意图（含原始 40 词 prompt 与反目标） | 全文 |
| `superpowers/using-superpowers_SKILL.md` | obra/superpowers `skills/using-superpowers/` | bootstrap skill（1% 规则、优先级、红线表） | 全文 |
| `superpowers/writing-skills_SKILL.md` | obra/superpowers `skills/writing-skills/` | skill 写作指南（frontmatter 规则 / SDO / 反合理化 / TDD 流程） | 全文 |
| `superpowers/session-start_hook.sh` | obra/superpowers `hooks/session-start` | SessionStart 注入脚本（bootstrap 物证） | 全文 |
| `superpowers/builder-check-prompt.md` | obra/superpowers `skills/brainstorming/` | builder-check 子代理提示词（文档"完备性"验收） | 全文 |
| `superpowers/porting_across_harnesses_excerpt.md` | obra/superpowers `docs/porting-to-a-new-harness.md` | 跨 harness 三组件模型 / 硬性要求 / 验收标准（Part 1-3） | 摘录 |
| `superpowers/visual-companion.md` | obra/superpowers `skills/brainstorming/visual-companion.md` | 视觉伴侣机制（何时用浏览器 / 何时留终端 / server 用法） | 全文 |
| `superpowers/manifest_samples.md` | obra/superpowers 三份清单 | `.claude-plugin` / `.codex-plugin` / `.agents` 市场 实样 | 全文 |
| `community/brainstorming_v2.2_SKILL.md` | obra/superpowers-skills `skills/collaboration/brainstorming/` | 社区版旧 brainstorming（Socratic 三阶段版） | 全文 |
| `zh/brainstorming_SKILL.zh-CN.md` | jnMetaCode/superpowers-zh `skills/brainstorming/` | 中文翻译版（三路径版，含 HARD-GATE 中译） | 全文 |
| `zh/upstream-sync.json` | jnMetaCode/superpowers-zh 根目录 | 上游同步基线（翻译审计机制） | 全文 |
| `waza/RESOLVER.md` | tw93/Waza `skills/RESOLVER.md` | 技能路由表 + 歧义消解 + 串联规则 | 全文 |
| `waza/skills_excerpts.md` | tw93/Waza `plugins/waza/skills/ui|think/SKILL.md` + `rules/waza-routing.md` | infer-first 提问 / 方向锁定 / 评价模式 | 摘录 |
| `design-packs/huashu-design_consultant_excerpts.md` | alchaincyf/huashu-design `SKILL.md` | 设计方向顾问模式 / 三方向硬门 / 提问与异常处理 / Gate 文件 | 摘录 |
| `design-packs/oil-ui_direction_excerpt.md` | oil-oil/oil-ui `SKILL.md` | 「先文字问一次、再决定做几个」两步方向收敛协议 | 摘录 |
| `design-packs/grill-me_SKILL.md` | plugin87/ux-ui-agent-skills `.claude/skills/grill-me/` | 审问式提问 skill（七问一轮 / assumption 留档） | 全文 |

## 说明

- 全文 = 原样保留；摘录 = 保留关键节 + 来源 URL + 省略标记，均在文件头部注明。
- **历史路径对照**：调研期抓取缓存 `refs/_raw/` 已精选归档并移除；`refs/_raw/sp_skills_brainstorming_SKILL.md` → `refs/superpowers/brainstorming_SKILL.md`（内容相同，即旧引用的新路径）。
- 许可：各文件归属原仓库（superpowers / superpowers-zh / Waza / huashu-design / ux-ui-agent-skills / oil-ui 均为 MIT；agentskills.io 为公开规范文档）。仅作研究留档。
- 更新方式：重跑各来源 URL 直读即可刷新（命令示例见主报告 §6）。
