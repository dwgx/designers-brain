# superpowers 插件清单实样（打包参考）

> 来源: https://github.com/obra/superpowers（v7.0.0, main 分支），2026-10-15 直读。
> 用途: wave9 打包件设计的「实样」对照（Claude Code / Codex / .agents 市场三件套）。

## 1. `.claude-plugin/plugin.json`（全文）

```json
{
  "name": "superpowers",
  "description": "Core skills library for Claude Code: TDD, debugging, collaboration patterns, and proven techniques",
  "version": "7.0.0",
  "author": {
    "name": "Jesse Vincent",
    "email": "jesse@fsck.com"
  },
  "homepage": "https://github.com/obra/superpowers",
  "repository": "https://github.com/obra/superpowers",
  "license": "MIT",
  "keywords": [
    "skills",
    "tdd",
    "debugging",
    "collaboration",
    "best-practices",
    "workflows"
  ]
}
```

> 注：不带 `skills` 字段——Claude Code 默认扫描插件根 `skills/`，字段只是「加扫」。

## 2. `.codex-plugin/plugin.json`（全文）

```json
{
  "name": "superpowers",
  "version": "7.0.0",
  "description": "An agentic skills framework & software development methodology that works: planning, TDD, debugging, and collaboration workflows.",
  "author": {
    "name": "Jesse Vincent",
    "email": "jesse@fsck.com",
    "url": "https://github.com/obra"
  },
  "homepage": "https://github.com/obra/superpowers",
  "repository": "https://github.com/obra/superpowers",
  "license": "MIT",
  "keywords": [
    "brainstorming",
    "subagent-driven-development",
    "skills",
    "planning",
    "tdd",
    "debugging",
    "code-review",
    "workflow"
  ],
  "skills": "./skills/",
  "hooks": {},
  "interface": {
    "displayName": "Superpowers",
    "shortDescription": "Planning, TDD, debugging, and delivery workflows for coding agents",
    "longDescription": "Use Superpowers to guide agent work through brainstorming, implementation planning, test-driven development, systematic debugging, parallel execution, code review, and finish-the-branch workflows.",
    "developerName": "Jesse Vincent",
    "category": "Developer Tools",
    "capabilities": [
      "Interactive",
      "Read",
      "Write"
    ],
    "defaultPrompt": [
      "I've got an idea for something I'd like to build.",
      "Let's add a feature to this project."
    ],
    "websiteURL": "https://github.com/obra/superpowers",
    "privacyPolicyURL": "https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement",
    "termsOfServiceURL": "https://docs.github.com/en/site-policy/github-terms/github-terms-of-service",
    "brandColor": "#F59E0B",
    "composerIcon": "./assets/superpowers-small.svg",
    "logo": "./assets/app-icon.png",
    "screenshots": []
  }
}
```

> 注：`"skills": "./skills/"`（加扫）+ `"hooks": {}`（空对象，刻意抑制 Codex 对 hooks/hooks.json 的自动发现——Codex 原生展示 skills、无 session-start hook）+ `interface` UI 块。

## 3. `.agents/plugins/marketplace.json`（全文）

```json
{
  "name": "superpowers-dev",
  "interface": {
    "displayName": "Superpowers Dev"
  },
  "plugins": [
    {
      "name": "superpowers",
      "source": {
        "source": "url",
        "url": "./"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Developer Tools"
    }
  ]
}
```

> 注：跨客户端（.agents 系）市场条目格式：`name / source{source:url} / policy{installation,authentication} / category`。
