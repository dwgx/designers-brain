# 发布前独立只读交叉审阅

## 裁决

Main `33b03c1f69e20b7418139c5309b5c26e9355e4b3` 相对 `e0cfe964ed8b326721115630faf1e05b00de3f23` 的有效实现，Root 已覆盖或以更严格实现替代。未发现需要整批合并 Main 分支或重新渲染的功能缺口。收尾只有三个具体文本／溯源 delta；主代理已接收前两项，第三项在本报告前单独通知。

| 最小 delta | 独立依据 | 建议处理 |
|---|---|---|
| 五份 UI 现行说明还保留 cloud socket block／Windows 待复验 | 已读当前 README 与矩阵；Root 实际浏览器回执现已存在 | 更新 `examples/ui/README.md`、`ui-01/README.md`、`ui-02/README.md`、`ui-03/README.md`、`ui-03/VERIFICATION_MATRIX.md`，只引用 Root 的实际验证结果；evidence_audit 已被主代理指派处理 |
| 32 份 consumer 历史材料的源字节与 Git LF 字节边界未说明 | 20 份原字节相同；12 份可精确证明仅 CRLF→LF；所有 32 份当前字节都等于 e0 Git；当前 44 条校验均正确 | 保留现行 checksum；保留历史 source pins，追加下面的 LF 映射及 current／historical 声明，不恢复与当前文件不符的旧 hash |
| xchylerdrenth 一条 build.py 原始 SHA 被现行 SHA 覆盖 | `ORIGIN.json` 仍保存 pre-patch `9026122a…`→current `cc3a554f…`；Root PACKAGE-MANIFEST 却记 original=current、transformation=none | 恢复该条历史 original pin 并标 `GEOMETRY-CHECK.patch`；或精确定义导入阶段并显式引用 ORIGIN 更早谱系。当前代码与 Main 一样，无源码修补遗漏 |

## 实际读取范围与版本边界

读取 Main `e0..33b03c1` 的五个提交和全部 254 个变更路径，并计算 Main Git blob 与 Root 工作文件 SHA；其中 177 个文件字节一致、2 个删除状态一致，75 个差异继续按语义审阅。完整阅读选定 19 份差异正文、Main 六份独有 Motion 工具／证据、seed 与 capability 元数据，以及本报告列出的保全对象。第一轮 Root 为 e0 HEAD 上尚未提交的 Root 独占整合；consumer 最后核查已观察到 Root `d2d0d7c1f7616a1f3b21f979388c105e7d42b001`。整项是连续读取窗口，不声称全部读数来自同一个原子工作树快照。

Main 同期另产生 `5cdb7c10fe4cae637267575f83ee657a9a2e8778`（checksum）和 `13ebeb839fabf276e625ad42bfd4f359382ac98c`（GOALS）。只补读了这两项的相关差异，没有追逐后续 HEAD。本轮没有渲染、测试、项目文件写入、合并或远端发布；SHA／源文本审阅不能代替主代理的最终 commit 和 fresh-clone gate。

## 保全结论

### 739 张图与中央 manifest

`knowledge/domains/painters/dossiers/_images` 中，SOURCE Git `f008952365a77e140cbda3f3959d43ef000f9a22`、SOURCE 当前工作目录、e0 Git、Root 工作目录四方均为同样 739 条图像路径；每张图像 SHA 完全相同，零遗漏／字节变更。排序后 `path + TAB + sha256 + LF` 的整体 SHA 四方均为：

`ed3fc1cda611a209114f25ac814fc6a1988153ce7557386e69cb52b6a0ba5848`

中央 `manifest.md` 的 SOURCE f008 Git、e0 Git、Root 当前文件字节完全一致：`0540d8df1c2597287b06e0664d3832c848f18bd5932d46dd5b8480b6c59da033`（467685 bytes）。SOURCE 当前工作文件是完全相同文本的 CRLF 版本：`5698124daf47c989fd26232a686ec54cda2658b623e1a302ddb5806ebf95b470`（470997 bytes，3312 CRLF）；精确归一化后相同，无表格内容修改。本轮未拿旧 SOURCE 工作目录 raw manifest 作时间前后对比，因此不将它表述成缺少基准的“历史 raw bytes 前后相同”。

### 五段既有 Motion MP4

直接比较 e0 Git MP4 blob 与 Root 当前 MP4，02／10／12／13／15 全部原字节一致，完整 SHA 在 `PRESERVATION-AND-LATEST-DELTA.json`。本轮未重做已成立的解码／浏览器／渲染测试。

### Consumer 32：精确 LF 投影

e0 checksum 文件包含 44 条（32 历史材料 + 12 份 fresh C2 日志）。以下 12 条历史文件的当前 SHA 与旧记录不同，但当前字节均与 e0 Git 完全相同，LF→CRLF 重建后又精确等于旧记录 SHA；其余 20 条直接保持旧 source SHA。完整 64 位映射见 `CONSUMER12-LF-PROJECTION.csv`；全部 32 条原始比对字段见 `CONSUMER32-PROJECTION.json`。

| 文件（相对 experiments/consumer_skill） | 历史 CRLF SHA 前缀 | e0／当前 LF SHA 前缀 |
|---|---|---|
| ./C1/A-SEAL.json | `6f75252a577a…` | `f61e47160d9c…` |
| ./C1/CUE.json | `4939c0917f6e…` | `d8e5c452b1db…` |
| ./C2/stage-A/check-output.json | `7fcb4e14904f…` | `8c69e0ae1b89…` |
| ./C2/stage-B/cases/neg_budget/layout.html | `767e9b2743ec…` | `fe9f83c85435…` |
| ./C2/stage-B/cases/neg_budget/layout.json | `86a02b915a56…` | `d20ca4a9578d…` |
| ./C2/stage-B/cases/neg_role/layout.html | `767e9b2743ec…` | `fe9f83c85435…` |
| ./C2/stage-B/cases/neg_role/layout.json | `3633d41f35f6…` | `2e808c8107e9…` |
| ./C2/stage-B/cases/positive/layout.json | `5938c6acf5ba…` | `5c12d8050c89…` |
| ./C2/stage-B/runs/_aa_decision1.txt | `f9a833bd708d…` | `9a16370a87d3…` |
| ./C2/stage-B/runs/_aa_decision2.txt | `f9a833bd708d…` | `9a16370a87d3…` |
| ./C3/stage-B/verify-output.json | `aef86bd33b6a…` | `313555f84bca…` |
| ./C3/stage-B/verify-stdout.txt | `b63f1288e7c7…` | `126ea19ee68e…` |

当前 44/44 checksum 都匹配现行字节。应精确更正的现行句为：

- `experiments/consumer_skill/README.md` 第 3 行 “Byte-identical copies of the non-private artifacts …”。
- `docs/skill/consumer-evidence.md` 第 21 行 “Byte-identical copies … now live …”。
- README 第 35 行、consumer-evidence 第 55 行的 staging／before-commit “32/32 identical”可保留为历史，并紧接 Git 发布时 12 项 LF 投影说明。
- consumer-evidence 第 36 行 A/A 的 `f9a833bd708dfa4810c248a6430d8c768652d624f74dca33a6e9a32f2dffa20b` ×2 属历史 CRLF；当前 LF 为 `9a16370a87d32501f66177a5bc3c8ed5a0d313197900d78dd1beb9a7ce65db81` ×2。两者在各自表示下均相等，无 A/A 不确定性回退。

## 不应带回的 Main 差异

1. **5cdb 的“45/45 OK”checksum 不可采用。** 直接以其不可变 Git blob 检查 45 条，21 条不匹配：20 条绑定 CRLF 工作字节而实际提交 LF，另 README 在绑定后被改写，既不匹配 LF 也非 CRLF 变体。Root 当前 44 条自洽；增加 README 并不是必要修复。
2. **Root UI 现行行为脚本保留。** Root UI01／02 使用每次独立 TemporaryDirectory；Root UI01 负控限定 exit 1 且匹配指定断言。Main 接受任意非零退出，不能覆盖更强 Root 检查器。
3. **Root Motion 当前严格路线保留。** Main `probe_all.py` 在 FFmpeg 缺失时仍可成功并硬编码 yuv420p；`encode_frames.py` 的描述超出实际检查；`check_determinism.py` 在受控异常前读取未提交的 `renders/.../frames/frame_hashes.json`，无法直接用于干净 checkout。Main BROWSER 的七卡四次 observed seek 全为 0，却标成功；Root strict12 已否决这份弱回执并替换。Main 的独有工具不是尚缺的有效修补。
4. **Root NOTICE／三语 PROTOCOLS／路径脱敏无遗漏。** 已实际比较 39 attribution／699 recognized labels／1 jurisdiction-dependent conditional 的语义以及 null 的保守解释。Root 另修正真实视频来源 URL 和误导性的全量 pass 说法。fresh consumer 日志双方都已脱敏，Root保留独立投影映射。
5. **Seed／capability 实现覆盖完整。** 七个 seed 共 202 个 manifest 路径相同、无丢失；四组 capability 共 294 个 state 完全一致。Root 为当前 LF 包装字节重绑 hash 并添加 path_base；原始 pin 唯一需解释的差异就是 xchylerdrenth build.py 上述一条。完整 ORIGIN 仍在，所以谱系没有丢失。
6. **GOALS 不拷贝 Main 的旧“done”。** Main 13eb 的 Z-10 是它的 D1–D7／R1 记录；Root 使用 `final_gate_recorded_separately` 指向自己的 FINAL-GATE，更符合 Root 实际发布版本。

## 证据文件

- `MAIN-DELTA-INVENTORY.json`：254 路径、提交列表、逐项字节比较。
- `MAIN-DIFFERENCES-READ.json`：实际审阅差异和 Main Motion 独有正文。
- `PRESERVATION-AND-LATEST-DELTA.json`：739 图、中央 manifest、旧 5 MP4、额外 Main 提交。
- `CONSUMER32-PROJECTION.json`／`CONSUMER12-LF-PROJECTION.csv`：完整 32 条与需投影 12 条的精确 SHA。
- `MAIN-METADATA-SEMANTIC-COMPARISON.json`：202 seed 路径与 294 capability state。
- `XCHYLER-SOURCE-LINEAGE.json`：Main、Root manifest 条目和原始 ORIGIN。

上述三个 delta 完成并由 Root 对最终版本执行其既定发布 gate 后，本轮分支交叉审阅没有额外功能修补要求。
