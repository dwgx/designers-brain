# Claude Code plugin.json — `skills` 字段语义摘录

> 来源: https://code.claude.com/docs/en/plugins-reference.md（官方 Plugins reference）
> 摘录日期: 2026-10-15。只摘 `skills` 字段与技能加载相关行。

---

> Save the manifest at `.claude-plugin/plugin.json` under the plugin root. Put every other plugin file at the plugin root, not inside `.claude-plugin/`. That includes `skills/`, `commands/`, and `hooks/`.

> | `skills` | Path, or array of paths | Directories to scan for skills, each a directory of `<name>/SKILL.md` folders or one folder holding `SKILL.md` directly. `"."` names the plugin root. Adds to the default `skills/` scan |

> `agents`, `skills`, `outputStyles`, `workflows`, and `experimental.themes` take one path or an array of paths. `agents` entries must be `.md` files, and `skills` entries must be directories. The other three accept a directory or a file.

> Every component path in a manifest is relative to the plugin root and must start with `./`. A path such as `commands/foo.md` fails validation. `skills` and `mcpServers` each accept one form outside that rule:

> * **`skills`**: also accepts `"."`. Both `"."` and `"./"` denote the plugin root. Before v2.1.221, `"."` failed manifest validation, so use `"./"` when the plugin must load on earlier versions

> * **Adds to the default**: `skills`. The `skills/` directory is still scanned, and the listed directories load alongside it

> | Skills | `skills/` | One `<name>/SKILL.md` per skill. A plugin with `SKILL.md` at its root, no `skills/`, and no `skills` key loads as a single skill |

> When a [marketplace entry whose `source` is the marketplace root](/docs/en/plugins/marketplace-reference) lists specific `skills` subdirectories, only those subdirectories load, and the plugin's default `skills/` directory isn't scanned. A `skills` key in the manifest instead [adds to the default](#how-each-key-combines-with-its-default-location).

## 语境补充（同文档）

- 插件组件默认位置：`skills/`（每个子目录一个 `<name>/SKILL.md`）、`commands/`、`hooks/` 等，均在插件根目录下自动发现。
- 清单文件放 `.claude-plugin/plugin.json`；其余文件放插件根，**不要**放进 `.claude-plugin/` 里。
- `skills` 字段（可选）：路径或路径数组，指向要扫描的技能目录；`"."` / `"./"` 表示插件根；**加扫**（adds to the default），默认 `skills/` 仍会被扫描。
- 特例：插件根有 `SKILL.md`、没有 `skills/` 目录、且清单无 `skills` 键 → 整个插件按单个 skill 加载。
