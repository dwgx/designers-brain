# C1 Stage A — 自主公共文本检索记录

## 边界与时序

- attempt：C1-CLOSURE-20261118-001；case：C1；consumer版本：C1-CLOSURE-v1。
- 起始实测UTC：2026-11-17T22:39:50.632479+00:00。Windows快照验证完成UTC见原始工具回执：2026-11-17T22:51:33.994418+00:00。
- binding SHA-256：`5e0bdad6fad5c3186a97b5ca0cb0f7c70aa06c36cbbf8cb4f0e2e8e045aa8744`，本消费者先自行读取并核对。
- Windows route 每次明确指定 link_id/deviceId；只运行消费者编写的只读 git/hash/text 命令，GIT_OPTIONAL_LOCKS=0；没有运行仓库源码，没有读取图片、其他会话或旧消费者。
- `rev-parse --show-toplevel` 和 `--absolute-git-dir` 确认是输入目录自身仓库，不借父目录；HEAD、tree、status及六入口字节全部符合binding。每份被读取文本还与 `git show HEAD:path` 原字节相等。
- 原始代码和工具返回完整保留在本A目录。完整blob SHA、大小和阅读范围见 `source-read-ledger.json`。

## 实际导航

1. 读 `knowledge/INDEX.md` L1–96。L83的实际相对链接 `domains/painters/learning/INDEX.md` 引向学习导航。
2. 读 `knowledge/domains/painters/learning/INDEX.md` L1–133。L7–13给出明暗/边缘、三级灰阶、非人物替代分支。由此选择da_vinci；Bada和Caravaggio只作为入口级备选，未深入它们的路径。
3. 同时读公共入口 `skills/designers-brain/references/painter-modules.md` L1–20，看到模块README的指针。读 `knowledge/domains/painters/modules/README.md` L1–80，L11确认da_vinci卡的实际相对链接。
4. 从学习导航的 `da_vinci/learning_path.md#db-source-line-78` 进入，读 `knowledge/domains/painters/learning/da_vinci/learning_path.md` L1–162。依据L87–91三级起稿，L142非人物分支，以及L148–154限制。
5. 从学习导航L13和模块README L11的实际相对链接读 `knowledge/domains/painters/modules/da_vinci.md` L1–98。L9–12的无描边/中间调/边缘，L41–57场景迁移文本，L75中档“暗侧化开、亮部保结构”支持本次取舍。
6. public-read-2输出在会话展示中间截断；从同一已缓存原始返回再次显示学习路径L60–80后才用其中机制行。未发生另一个输入版本的读取。

## 原字节SHA与阅读范围

| 路径 | SHA-256 | 模型实际文本范围 |
| --- | --- | --- |
| knowledge/INDEX.md | d4688562f5975fae9b4366b26dc536379f5db55bc0923f1bbdd224f58a91533e | L1–96 |
| knowledge/LEARNING-INDEX.json | e6f801219dc3ab08a05b5a3b6a68a7e967f2d1dc3a2bc53e7c3fea3c5c74de73 | 仅核字节，未展现内容 |
| knowledge/domains/painters/learning/INDEX.md | c24e16e7cbdca9b44bdc9143979ec9e18785a961b05d6fa3c92e3e95b8eb80fd | L1–133 |
| knowledge/domains/painters/modules/README.md | e98da3bceeda223521c52592ffa0c4e4a2d30ccc8c63d98bf75ba8c18a3663a3 | L1–80 |
| skills/designers-brain/SKILL.md | 5043ac6f7daeaa6d067a26866efbc20c3bed79226573106f89d8253e41cf5362 | 仅核字节，未展现内容 |
| skills/designers-brain/references/painter-modules.md | 96a83b91abed8cde77e26bd77b1328f2f810f5f5b8304f84f3c98f4ce46a0787 | L1–20 |
| knowledge/domains/painters/learning/da_vinci/learning_path.md | 00a7010818682d14c14003f8e2ef06949ff25fb1bcc4ef1deca76986dde22730 | L1–162 |
| knowledge/domains/painters/modules/da_vinci.md | e6ad4d1b24b25994bfc4cc467677d1f323545e28bba17f1efd7428f8dcc88cc3 | L1–98 |

## 提示暴露与解释边界

公共学习路径本身提供了球体/面部局部、三级起稿、对照练习、数值阈值及常见失败；模块提供人物完整prompt、纯风格prompt及负向词。均已读，不能称“零提示”试验。纯风格段仍保留圆锥岩石和浅绿水，因此本次避开这些场景。具体题材改为种子库布袋；“未作为示例”只覆盖实际阅读范围。

来源的数值是项目归纳规则。本次只消费三级起稿和边缘关系；SVG仍有三值形块边界，未实现完整连续渐变，不声称通过全部sfumato规则。视觉焦点与边缘的因果取舍是本消费者的设计解释，需后续实际观察，不能以文件或元数据存在宣称审美有效。

先写 `unaided-selection.json` 和 `01-focus-plan.json/.svg` 标注焦点，再写 `02-three-value-sketch.svg` 和规格。Stage A无栅格渲染目检，留待有效CUE后。READY一旦生成，本A目录永久不修改。
