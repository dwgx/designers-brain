# video-shotcraft 深拆手册（B-16）

> 归属：GOALS B-16（VideoShotcraftDeep）｜状态 v0.1（2026-10-15）｜前置调研：`video_shotcraft.md`（B-14，元数据级）
> 兄弟文档：`mg-styles-15_handbook.md`（B-13，同作者另一条路线逐文件拆解）· `review_rubric.md`（B-11）· `templates/determinism_contract.md`（B-11）
> 对象：GitHub 仓 `Vincentwei1021/video-shotcraft`（Apache-2.0，11,994★，2026-10-15 API 实测），默认分支 `main`。
> **本次实读方式**：`git clone --depth 1 --filter=blob:none --no-checkout` + `git sparse-checkout`（cone 模式，23 MB，只检出本手册用到的目录）到 `%TEMP%/vsc2`；克隆 HEAD = `13c74a7 docs(readme): add sponsors and animated workflow (#101)`（2026-10-13T15:09:40+08:00）。全文引用均来自该克隆或 raw 直读，`路径:行号` 与原文引号可复核。
> 证据分级：`[实测]`=本次实读/实跑；`[自述]`=仓库文档自述；`[归纳]`=本次总结；`[推测]`=推断；`[UNVERIFIED]`=未跑未核。

---

## 0. 结论速览

1. **三层卡库，不是一层文档**：`references/shots/*.md`（124 张卡，人读）→ `gallery/api/library.json`（机读索引，124 卡 / 150 style）→ `demos/**/*.tsx`（152 个参考实现，参数真相）。三层之间由 `gallery/sync-from-cards.py` + CI 漂移门强制同步 `[实测]`。
2. **判例式规则是全部方法论的写法**：`aesthetic-rules.md` 27 条（R1–R4 / Q1–Q11 / S1–S5 / C1–C3 / P1–P4），每条 = 规则 + 用户原话判例 + 自检问题；编号只追加不重排；验收时逐条输出 `编号 ✓` / `编号 ✗(位置)` `[实测]`。
3. **验收机制可以整段搬走**：每镜头在分镜计划里**写死 2 个验收帧号**（`npx remotion still --frame=N` 肉眼验收，产物归档 `out/qa/`）+ 交付前**干净上下文 subagent** 按 17 项输入清单出**带帧号证据**报告（P/F/V/S/B/D/A/Q 八组）`[实测]`。
4. **工作台契约是本仓最独特的一块**：成片工程写一份 `src/workbench.ts` 清单（`WORKBENCH` 常量），浏览器里把成片拆成多轨编辑；「语境参数 → props + schema，节奏命门保持常量」，`npm run parity` 用逐像素比对证明拆解无损（退出码 0/1/2，绝不假绿）`[实测]`。
5. **与我们路线的接口**：卡格式的**机读层 + 参考实现指针**、规则的**判例三要素**、验收的**帧号证据**三样可直接进 B-11/B-13/B-08/B-17；而 Remotion 依赖、真实页面截图路线、Mixkit 音频、工作台整包属**不抄清单**（理由见 §5.2）。
6. **口径警告**：仓库简介「152 cards / 209 previews」是旧值，`llms.txt` 写「six-stage methodology」而 `pipeline.md` 标题是**八阶段 0–7**——本手册一律以克隆实读为准 `[实测]`。

---

## 1. 仓库地图

### 1.1 顶层（git trees API `recursive=1`，`truncated: false`；1,648 条 entry = **1,358 blob + 290 tree**，blob 合计 64.77 MB）[实测]

> 下表「blob 数」为**只计文件**（不含目录）；早先按 entry 计的口径（如 demos 484、template 81）含 tree，勿混用。

| 路径 | blob 数 | 内容 | 本手册实读程度 |
|---|---|---|---|
| `demos/` | 280（204 个目录） | 每卡一个 Remotion 参考实现（10 类目录共 152 个 `.tsx`）+ `_fixtures/` 6 + `_textures/` 25 + `_legacy/` 96（68 tsx，已下架）；`.tsx` 全量 226 | 目录级 + `README.md` 全文 + 1 个 TSX 头部 |
| `shot-polish/` | 376 | **作者内部打磨工作区**：`notes/` 216 + `final-notes/` 150 + `decisions.json` + `BRIEF.md` + `BRAND-BRIEF.md` + 7 个工具文件（`build-compare.py` / `build-final.py` / `serve.py` / `sheet.py` / `tsc-demos.sh` + 2 个 html 模板） | `BRIEF.md` 头部 + `decisions.json` summary |
| `assets/` | 193 | `lib/` 12（7 组件 + helpers 4 + 单测）· `scripts/` 3（capture / smoke / readme-cover）· `audio/` 156（149 SFX 16 类 + 5 BGM + 2 说明文件）· `brand/` 7 · `readme/` 15 | `lib`/`scripts` 实读，音频只读目录计数 |
| `gallery/` | 196 | `api/library.json`（206,605 B 机读索引）· `source/` 124（卡的副本）· `media/` 54（**全部 .jpg**，mp4 另存 release）· `app.js` 24.5 KB · `translations.js` 50 KB · `sync-from-cards.py` · `build-seo.py` · `assemble-media.py` · `fetch-media.sh` · `llms.txt` · `showcase.*` | `library.json` 机读全量解析 + `sync-from-cards.py` 全文 + `app.js` 头部 |
| `references/` | 136 | 9 个方法论文档（下表）+ `shots/` 125（124 卡 + ATTRIBUTION）+ `sequences/` 2 | 7 篇实读（pipeline / aesthetic-rules / final-review / workbench / guided-free-creation 全文；sound-design、music-beat-sync 未读） |
| `workbench/` | 73 | Vite + Remotion Player 浏览器工作台：`src/` 41（cards/ timeline/ panels/ preview/ remotion/）· `scripts/` 7（open / gen-index / parity / render-demos / check-demo / test-themes / test-legacy）· `i18n/` 4 · `docs/` 9 张截图 | `manifest.ts` + `parity.mjs` + `zodFromCard.ts` + `GUIDE.md` 头部 |
| `template/` | 70 | 已验收成片模板 Ink Press（36.2 s / 1085 f / 10 镜头）：`src/` 22（aifl/ 含 Main + 6 场景 + 4 组件 + live-layout.json；themes/）· `public/` 38（textures/live 27 图 + audio 11 mp3）· `remotion.config.ts` | `TEMPLATE.md` + `workbench.ts` + `package.json` + `remotion.config.ts` 实读 |
| `videos/` | 12 | `videos/readme-workflow/`：README 动效工作流的独立小工程（`hyperframes.json` / `shot-plan.json` / `index.motion.json` / `BRIEF.md`） | **未读** [UNVERIFIED] |
| `.github/` | 5 | 3 workflow（pr-checks / deploy-pages / showcase-publish）+ showcase issue 模板 + 发布脚本 | `pr-checks.yml` 全文 |
| `jianying-export/` | 5 | 剪映工程导出（`mac_draft.py` / `windows_draft.py` / `aifl_promo.py` / `smoke_test.py`） | 未读 |
| `publish/` | 2 | Upload-Post 社交发布（纯标准库）+ 单测 | 未读 |
| `.claude-plugin/` `agents/` | 1+1 | Claude Code 插件清单（`"skills": "./"`）+ Codex UI 元数据 `openai.yaml` | B-14 已实读 plugin.json |
| 根 | 8 | `SKILL.md` 20,853 B · `README.md` / `_CN` / `_JA` · `package.json`（仅 vitest）· `LICENSE`(Apache-2.0) · `.gitignore` · `package-lock.json` | `SKILL.md` 全文 + README Install/Use 段 |

### 1.2 九篇方法论文档（字节数为 tree API 实测）[实测]

| 文档 | 字节 | 职责（本手册实读程度） |
|---|---|---|
| `references/pipeline.md` | 25,226 | 八阶段 0–7 主流水线（**全文实读**） |
| `references/aesthetic-rules.md` | 27,528 | 判例式审美准则 27 条（**全文实读**） |
| `references/sound-design.md` | 27,677 | 声音设计（未读；本手册音频结论来自 pipeline/SKILL/aesthetic-rules 的转述） |
| `references/music-beat-sync.md` | 13,019 | 卡点方法论（未读，同上） |
| `references/workbench.md` | 13,212 | 工作台接入契约（**全文实读**） |
| `references/guided-free-creation.md` | 10,874 | 共同创作引导流程（**全文实读**） |
| `references/jianying-export.md` | 9,348 | 剪映导出（未读） |
| `references/final-review.md` | 7,095 | 独立终检清单（**全文实读**） |
| `references/publish-upload-post.md` | 6,596 | 社交平台发布（未读） |

### 1.3 关键文件一句话职责 [归纳]（均实读）

- `SKILL.md` — agent 入口：frontmatter 双语触发词 + 三模式判别（模板/自主/共同）+ 两例外 + 9 条核心理念 + 「何时读哪个文件」路由表 + 资产使用方式 + 交付收尾 1-2-3。
- `gallery/api/library.json` — **机读真相源**：卡名/一句话/适用/时长/能量/意图/style 列表/media URL，gallery 页面与 llms.txt 的数字全部读它。
- `gallery/sync-from-cards.py` — 卡 → 索引的同步器 + 漂移门：卡改了不同步，CI 直接红。
- `references/shots/<类别>/<卡名>.md` — 卡本体：YAML frontmatter（机读）+ 五段正文（人读）。
- `demos/<类别>/<卡名>/<组件>.tsx` — 参考实现：`export const <Stem>: React.FC` + `<大写蛇形>_DURATION`，copy 即跑。
- `template/src/workbench.ts` — 成片 → 工作台的拆解清单（`WORKBENCH` 常量），所有时间表从 `Main.tsx` import，不存第二份。
- `workbench/scripts/parity.mjs` — 拆解无损证明：`ProjImported` vs `ProjOriginal` 同帧 PNG 逐像素比对。
- `assets/scripts/capture-template.mjs` — 真实页面 → 素材三件套（整页 2x / 元素抠图 / layout.json）的采集模板，只改顶部 CONFIG。
- `.github/workflows/pr-checks.yml` — 4 个 job：单测 / 产物同步 + 媒体存在性 / 工作台构建 + 主题回归 / demo 首帧冒烟。

---

## 2. 镜头卡系统

### 2.1 三层结构与数据流 [实测]

```text
references/shots/<类别>/<卡名>.md          124 张，人工撰写（frontmatter + 五段正文）
        │  sync-from-cards.py（写 gallery/source/ 副本 + 刷新 library.json 文本字段 + 重算 stats）
        ▼
gallery/api/library.json                   cards[124] / stats{cardCount 124, styleCount 150, previewCount 150}
        │  app.js 渲染画廊（搜索/筛选/多选复制卡名）+ llms.txt 生成
        ▼
demos/<类别>/<卡名>/<组件>.tsx             152 个参考实现（卡的「参考实现」段指向它）
```

**样式（style）≠ 卡（card）**：19 张卡带多个 `styles[]` 条目，150 = 124 卡里多出的 26 个变体 `[实测]`。多变体卡在正文里用「三式选型」表列出变体差异（例：`chart-live-moves` = oscilloscope-stream / unit-dot-swarm-regroup / axis-rescale-shock），实现文件也是多文件（`AxisRescaleShockV2.tsx / OscilloscopeStreamV2.tsx / UnitDotSwarmRegroupV2.tsx`）`[实测]`。

### 2.2 frontmatter 机读层（124/124 全量机读解析）[实测]

**字段频次**（本次用脚本解析 124 个卡的 frontmatter）：

| 键 | 出现次数 | 含义 |
|---|---|---|
| `name` | 124 | 卡名（= 文件名 = library.json `cards[].name` = demo 目录名） |
| `一句话` | 124 | 摘要（→ library.json `summary`） |
| `适用` | 124 | 使用场景（→ `use`） |
| `时长` | 124 | 建议时长，含分段（→ `duration`） |
| `能量` | 124 | 能量档（→ `energy`） |
| `标签` | 50 | 追加类别标签（→ `tags`，用于跨类筛选） |

**键序**：74 张卡为 `(name, 一句话, 适用, 时长, 能量)`，49 张尾部带 `标签`，1 张 `标签` 插在 `时长` 前——**解析器不依赖键序**（`sync-from-cards.py` 逐行 split `:`）`[实测]`。

**样例（`references/shots/opening/text-as-mask.md:1-9` 原样）**：

```yaml
---
name: text-as-mask
一句话: 文字视频遮罩——瓷白舞台上切出超粗大标题字，字内部透出缓慢平移的暗色实时产品面板，结尾吸一口气后字形指数冲入放大 46 倍溢出、内部画面接管全屏
适用: 品牌词/口号与产品画面二合一的开场或章节卡；字是门、产品在门里
时长: 165f（入场 18f + 字内漂移 78f + 吸气 8f + 冲入接管 24f + 落定/hold 37f）
能量: 中高（漂移段沉稳，接管段一次爆发）
标签: typography
---
```

> 对照：B-14 §3.3 引的同一张卡 frontmatter 与本次实读有出入（`一句话` 少了「瓷白舞台上切出」等描述）——**以本手册的 raw 实读为准**（§7.3 已贴全文）。`[实测]`

### 2.3 正文五段（结构恒定）[实测]

`意图 → 动效核心 → 参数表 → 已知坑 → 参考实现`，其中：

- **意图**：为什么存在 + 同族/不并用关系（`sync-from-cards.py` 用正则 `^## 意图\n(.*?)(?=\n## )` 抽它进 `library.json.intention`）。
- **动效核心**：逐条物理参数（缓动、时值、遮罩时机、transform 分离），带**为什么**。
- **参数表**：三列 `| 参数 | 典型值 | 调节手感 |`——「调节手感」列写的是**调坏的方向**（例：`放大倍率 | 46× | 不足则接管帧还看得到字边残影`）。
- **已知坑**：每条都是踩过的坑 + 原因/后果（例：「别给字形做描边高光：system-ui 等可变字体的字形由重叠轮廓拼成，描边会画出 A 的横杠/顶角等内部轮廓线」）。
- **参考实现**：目录 + 文件名（`demos/opening/text-as-mask/（TextAsMask.tsx）`）——**卡的语义层与 demo 的参数层显式分离**。

### 2.4 library.json schema（机读全量）[实测]

**顶层**：`generatedAt` / `revision` / `stats` / `cards[124]` / `staticExport` / `categories{10}`。

**card 条目**（`cards[0]` 原样，节选）：

```json
{
 "name": "assemble-then-type-flyin",
 "summary": "空的暗底网格上，无文字的组件骨架先从四面八方飞入贴合；随后各处文字逐字从 3D 空间旋转着飞来落位……",
 "use": "页面/海报\"自己长出来\"的开场；排版类产品的能力展示；从骨架到成稿的两段式叙事",
 "duration": "约5.6s（168f@30fps）",
 "energy": "中高（骨架段稀疏、文字段密集，能量单调上升到收尾）",
 "intention": "把\"页面生成\"拆成两个语义清楚的阶段：先立骨架……",
 "source": "references/shots/effects/assemble-then-type-flyin.md",
 "updatedAt": "2026-10-02T21:01:48.000Z",
 "styles": [{ "key": "assemble-then-type-flyin", "label": "...", "description": "...",
              "media": { "url": "./media/assemble-then-type-flyin.mp4?v=1790980736765", "type": "mp4" } }],
 "sourceUrl": "./source/assemble-then-type-flyin.md",
 "category": "effects", "tags": ["effects"],
 "addedAt": "2026-08-07T04:03:34.000Z"
}
```

**style 条目键集合（150 条全量取并集）**：`key / label / description / media / use`——另有一个**预留但当前为空**的 `implementationStatus`（`sync-from-cards.py` 的 `STYLE_STATUS` 字典，源码注释：「Variants with a recipe/sample but no reusable demo source get 'reference-only' here so the workflow does not recommend them by default. **Currently empty: every style has demo source.**」）`[实测]`。
→ 也就是说 SKILL/pipeline 反复提到的两种降级标记（「仅供参考，需要自定义实现」「缺少预览」）**机制存在、当下 0 条命中**（本次在 124 个卡 md 里 grep `仅供参考`/`缺少预览` 均 0 命中，150 个 style 里 `implementationStatus` 0 条）`[实测]`。

**stats**（由脚本重算，不手写）：`{"cardCount":124,"styleCount":150,"previewCount":150,"mediaCount":150,"newest":"2026-10-02T21:01:48.000Z"}`。
**分类卡数 vs style 数**（本次全量统计）[实测]：

| category | cards | styles |
|---|---|---|
| typography | 22 | 25 |
| ui-entrance | 21 | 22 |
| transition | 15 | 19 |
| effects | 15 | 23 |
| opening | 11 | 11 |
| interaction | 11 | 13 |
| camera | 10 | 13 |
| rhythm | 8 | 8 |
| outro | 6 | 7 |
| data | 5 | 9 |
| **合计** | **124** | **150** |

→ README 图集里「Camera · 13 shots」「Transitions · 19」「Typography · 25」用的是 **style 口径**，而「Opening & Brand · 11」是 card 口径——**两个口径混用**，引用时必须写清分母 `[实测]`。

### 2.5 同步器与漂移门（`sync-from-cards.py` + `pr-checks.yml`）[实测]

`sync-from-cards.py` 的硬规则（源码实读）：

1. 卡删了 → `gallery/source/` 副本删；`library.json` 里还有孤儿条目 → `raise SystemExit`（**硬失败**，注释：「Gallery 会渲染一张 source 链接指向虚空的卡」）。
2. 卡的 `标签` 值必须在 `CATEGORIES` 里，否则 `SystemExit`（「unknown 标签 …」）。
3. `card['tags'] = [主类别] + [其他标签]`——**目录名永远是主类别**，标签只扩大筛选命中面。
4. `stats` 全部从卡重算（不信任旧值）；`addedAt` 首入时写死（画廊 NEW 徽标数据源，14 天窗口），之后只动 `updatedAt`。
5. 卡的 md 字节变了 → 该卡 `updatedAt` 置为本次同步时刻（sitemap lastmod 跟着走）。

CI 门（`pr-checks.yml`，4 个 job）`[实测]`：

- `unit-tests`：`npm ci && npm test`（vitest，覆盖 helpers 的 mulberry32 / velocityAt / lagged / dampedSettle / handheld）。
- `verify` ①：跑 `sync-from-cards.py` + `build-seo.py` 后 **`git status --porcelain -- gallery` 必须为空**——「产物与卡不同步」直接红（注释解释为何不用 `diff --exit-code`：新卡的重生成副本是 **untracked**，diff 看不见）。
- `verify` ②：`library.json` 每个 `media.url` 必须匹配正则 `^\./media/[a-z0-9-]+\.(mp4|gif)(\?v=\d+)?$`（因为 `app.js` 把 URL 插进 `innerHTML` 不做转义）**且**文件存在于 gallery-media release。
- `verify` ③：`find demos -name '*.tsx'` 全量 `tsc --noEmit --strict`（含 `assets/lib` 里只依赖 remotion 的 9 个文件）。
- `workbench-build`：工作台 `tsc -b && vite build` + 模板（含 `workbench.ts`）用工作台工具链编译 + 主题/旧卡回归测试。
- `demo-smoke`：`smoke-render-demos.py` 渲每个 demo 首帧。

### 2.6 判例式规则体系（`aesthetic-rules.md` 27 条全量）[实测]

**格式三要素**（文件开头原文）：

```
**使用方式**：
- 每条 = 规则（一句可执行的话）+ 判例（用户原话 / 返工经过）+ 自检问题，三要素缺一不可。
- pipeline.md 阶段 7 验收时**逐条过一遍**，输出自检报告，格式：`编号 ✓` 或 `编号 ✗(位置)`（位置 = 镜头名/帧号）。
- 准则可以有意识违反（风格需要时），但每次违反必须写进该项目的说明文档（写明违反了哪条、为什么）。
- 编号体系：R(节奏) / Q(质感·运镜·构图) / S(声音) / C(文案) / P(流程)，编号一经发布不重排，新增条目只追加。
```

**条目清单**（本次逐条读毕）：R1–R4 · Q1–Q11 · S1–S5 · C1–C3 · P1–P4 = **27 条**。

**逐字样例三条**（判断力在「判例」段）：

- **R3（节奏宁慢勿快）**——判例是可证伪的统计：「全片六次独立反馈全部指向"放慢/停留"，**从未有一次"太慢了"的反向反馈**。用户："第一个镜头还是太快了，放慢到3秒"……开场几经放慢到 3s macro opening，交互段落改成不慌不忙的 type-and-filter。」自检：「把每个镜头当第一次看：哪里没看清？交互段落自己能不能跟着操作一遍？」
- **Q2（文字发糊先查纹理链路）**——判例是三轮追打 + 根因：「用户三轮追打："明显卡片变得模糊了"、"还是不够高清……有像素点的方块"……先调 DoF 治标无效，改成按原生尺寸 rasterize 拿到真正 4x 锐度，最后把 CSS zoom 推广到全部 3D 页面层根治。」技法展开给出**排查顺序**：文字糊 → 先查纹理源分辨率链路（截图倍率→栅格化路径→缩放方式），最后才考虑相机；「DoF 只做氛围，永远不是清晰度的解法（实证无效）」。
- **S5（音画对齐两项偏移）**——判例带**实测数字**：「AiflPromo 实测 click 滞后 2032 samples、impact 2066 samples（≈1.27–1.29f），与 AAC priming 指纹吻合……promo-ink 时代实测过 4f（≈133ms，远超 priming 量级，根因未验证）——**常数不可跨管线搬运**。」规则要求按渲染管线（Remotion 版本 + codec + sample rate + 容器）实测记档，补偿在渲染层 from 计算式统一扣。

**规则的自我修正痕迹**（同类最值钱的信号）：Q1/Q4 都带 2026-07-13 用户澄清的**约束收窄**（「否决针对的是"实现的版本不好看"，不代表技术路径不可行」），R4 的计数口径补了「计数单位是一次手法/set-piece 使用，不按内部子事件数」——**判例被后续裁决改写时，原条不删，改写进同条** `[实测]`。

### 2.7 卡的来源与授权（`references/shots/ATTRIBUTION.md`）[实测]

- 现存 **38 张卡**记录为「研究自公开发布的产品宣传片与开源项目主页」，实现**从零重写**：「仓库不包含任何原片片段、截图、美术资产或品牌元素；实现中的文案、配色、UI 内容均为中性占位模板。原作者未参与本项目，卡片标注来源仅为致敬与研究溯源」。
- 法律边界自述：「来源作品"公开发布"**不等于**授予复刻或衍生的许可。本表记录的是研究溯源，不是授权凭证；对未获明确许可的来源，我们依赖的是"手法参考 + 独立重写、无原素材"这一实践」。
- 已知精确度限制：「X / 抖音来源当时以账号主页为单位记录，未逐条留存具体帖子 URL」。
- 逐卡映射示例：`anime.js 官网演示 → radial-wave / value-stagger-gradient`；`x.com/Jerrythe2d → bezier-source-converge-merge 等 6 张`；`用户参考图定制（brand-scan）→ assemble-then-type-flyin / scanline-annotate-focus / scanline-assemble-flyin`。
→ 对我们是**可直接引用的方法论**：卡库允许「手法参考 + 独立重写 + 去品牌化」，但要在库内明写来源批次与边界 `[归纳]`。

---

## 3. 工作流与工作台

### 3.1 三模式入口（`SKILL.md`）[实测]

| 模式 | 读什么 | 确认节奏 |
|---|---|---|
| ① 直接使用模板 | `template/TEMPLATE.md` 全文 | 按模板自带替换流程走 |
| ② 自主自由创作 | `references/pipeline.md` | 阶段 0–7 连续推进，**不逐阶段等待确认** |
| ③ 共同创作 | `references/guided-free-creation.md` | 阶段 0–3 逐级确认（产品简报→需求决策→视觉方向→镜头映射→分镜），放行后从阶段 4 继续 |

**两例外**：点名 Ink Press = 模式①已选；点名镜头卡 = 镜头约束已定（只问②/③）。模式未定先做**最小只读产品检查**（不修改业务项目、不采集敏感数据、不写视频代码），再给推荐并问一句「要按这个模式继续吗？」。

### 3.2 八阶段流水线（`pipeline.md` 全文实读）[实测]

| 阶段 | 关键机制（可直接借的部分） |
|---|---|
| 0 产品理解 | 只读检查 → 产品简报 + **需求到执行决策表**（每行：已确认需求 / 项目依据 / 受影响执行范围 / Agent 推荐 / 需确认项）；敏感数据先冻结/脱敏 |
| 1 视觉方向 | **不渲染视频、不写 Remotion**，纯 HTML/CSS styleframe（2–3 张 1920×1080）+ **品牌→动效参数两轴推导表**（能量轴×调性轴 → 6 预设：主时长/easing/过冲/squash）+ 参考片 ffmpeg 抽帧 motion breakdown |
| 2 功能→镜头映射 | 扫 `references/shots/` **全部卡 frontmatter**（用途/能量/时长/限制）选卡；一种手法全片只当一次主角 |
| 3 分镜与放行 | 先查 `sequences/`（`promo-energy-arc` 四段位）；**帧预算先划 hold**（字标 ≥30f、批量收尾 15f、开场主体 ≥3s）；帧级时间轴 `\| shot \| from \| duration \| 内容 \|`，**每镜头指定源文件与验收帧号** |
| 4 素材采集 | 采集三件套（§3.3） |
| 5 逐镜头实现 | 三读硬规则 + 2 验收帧号 + 整片重渲 + 确定性铁律 + 为工作台留接口（§3.4） |
| 6 声音设计 | **画面锁定后才开始**；16 类 SFX 先类别后音色；**钉帧表用相对表达式**（`SHOTS.x.from + offset`，卡点片 `beatF(n)`），绝不写裸数字帧号；长样本（>5s，21 个）显式 `durationInFrames`；BGM 用布尔 inputProp 出两版 |
| 7 验收 | 独立终检 subagent + 内容级自查 + 音画对齐回测 + 修复回流阶段 3/5/6（§3.5） |

**能量骨架 `sequences/promo-energy-arc.md`**（实读）：四段位（品牌开场 8–12% / 单主角立传 12–15% / 功能爬升 55–65% / 发布会收场 13–16%）+ 呼吸字卡（每 1–2 个功能镜头后一张，50–55f，全片 2–4 张）+ 填空流程五步（列功能数 N → 先扣首尾与字卡预算 → 高/稳能量交替 → 逐槽位扫 frontmatter 挑卡 → 逐接缝选转场）。骨架自述是「**默认项，不是令**」，偏离写进项目 spec。

### 3.3 素材采集三件套（`assets/scripts/capture-template.mjs`）[实测]

脚本头注释原文（文件 1-19 行）列出「前置条件三条都是硬前提」，其中第三条是**红线**：

```
//   3. 【红线】假数据先注入 —— 截图前页面必须已填充"虚构但真实感"的演示数据。
//      空库/lorem ipsum 截出来的图直接废片；真实客户数据则不能出片。
```

CONFIG 结构（实读）：`BASE`（本地地址）/ `OUT_DIR`（默认指向 Remotion 项目 `public/textures/live`）/ `LAYOUT_JSON` / `VIEWPORT {width:1920, height:1080, deviceScaleFactor:2}` / `SETTLE_MS:600` / `PAGES[]`，每页含：

- `boxes`（只记坐标，`all:true` 记匹配元素数组 → `layout.<name>.boxes`）；
- `cutouts`（元素级截图 + bbox，`omitBackground:true` 出透明底「浮起的 UI 芯片」，`parent:true` 截父元素）；
- `hideForEmptyPlate`（把某元素设为 `visibility:hidden` 后再截一张 → `<name>-empty.png`，供「元素飞入」镜头当空底板）；
- `interact`（截图前在页面里执行交互，如点开某个 tab，之后补一张 `<name>-after.png`）；
- `waitMs` / `interactWaitMs`（实时同步页额外等待）。

采集逻辑通用部分：先 `document.fonts.ready` + settle（「避免截到 FOUT/骨架屏」），元素 bbox 换算到整页坐标系（与 `fullPage` 截图同系），输出 `layout.json {pageW, pages{…}}`。

### 3.4 逐镜 QA：**2 个验收帧号**机制（`pipeline.md` 阶段 5）[实测]

阶段 5 第 3 条原文：

> **静帧验收（最高频动作）**：每镜头在计划里写死 2 个验收帧号，完成即跑
> `npx remotion still src/index.ts <Comp> out/qa/<name>.png --frame=<N>`，自己肉眼检查构图/穿帮/文字锐度后才算完成。静帧产物按迭代版本归档 `out/qa/`，用户贴帧反馈时可直接对号。

配套四条：

1. **三读硬规则（不可跳）**：`library.json` 校验卡名与 style-key → 读卡全文 → 按「参考实现」读**准确 demo TSX 全文** → copy `assets/lib/` 组件；同时保存 Gallery 参考样片路径供终检对照。「配方卡"已知坑/命门"标注的参数**不得降档**，质量标准只升不降。凭卡名和理解新写＝放弃全部调校积累，实测质感差一档。」
2. **每轮修改后整片渲染**：`npx remotion render …` 后用 `ffmpeg -i out/promo.mp4 -vf "select=eq(n,…)"` 从成片抽帧回看；实际形态是「改哪个镜头就 still 哪几帧，然后整片重渲」。
3. **像素级自检小工具**：crop 放大看文字锐度、两帧像素 diff、量元素 bbox 对构图。
4. **确定性渲染铁律**：禁 `Date.now()` / `Math.random()` / 无参 `new Date()`；伪随机用固定种子（mulberry32/哈希，**seed 从 index 派生**），tween 全部 clamp。

> 模板文档 `template/TEMPLATE.md` 给的验收口径是**三帧**：「每镜头至少入场中/动作峰值/落定后三帧」，验收静帧示例 `npx remotion still src/index.ts AiflPromo out/qa/f150.png --frame=150`——**「2 个写死帧号」是计划纪律，「至少三帧」是模板的抽帧口径**，两者不冲突，引用时别混 `[实测]`。

### 3.5 干净上下文 subagent 终检（`final-review.md` 全文实读）[实测]

**交接原则**原文：「审查 Agent 必须处于干净上下文，不参与制作；**不要给它制作过程中的理由、辩解、修改历史或预期结论**。」

**审查输入（17 项）**：最新成片 MP4 + 每镜头关键帧；创作模式；产品简报与必须展示的功能；需求到执行决策表；视觉方向/tokens/styleframe（模板模式给原模板结构与替换记录）；功能到镜头映射；Gallery 卡名与具体变体；`library.json` 中对应卡片与 style-key 记录；卡定位到的**准确 demo TSX**；Gallery 参考样片或抽帧；最终分镜/字幕/页面状态/SFX 计划；选中的 `references/shots/*.md`；`aesthetic-rules.md`；数据合规口径。**缺输入标「无法验证」，不许猜**；索引/卡/demo/样片互相冲突时**报告冲突来源，不自行挑一个当真相**。

**检查项八组**：P（产品目标 P1–P4）/ F（功能完整性 F1–F3）/ V（视觉方向 V1–V4）/ S（镜头卡与变体 S1–S6）/ B（分镜一致性 B1–B4）/ D（数据与素材安全 D1–D5）/ A（音频与节奏 A1–A9）/ Q（视觉技术质量，完整执行 aesthetic-rules）。

**报告格式**（原文代码块）：

```text
P1 ✓ 产品定位和核心卖点清楚。
F2 ✗ 第 340 帧：已确认的知识图谱功能没有出现在成片。
V3 ✗ 第 420 帧：大面积琥珀纸张材质偏离已确认的深蓝科技方向。
S2 ✗ 第 515 帧：用户选择 whip-pan，实际实现为 flash-cut。
Q2 ✗ 第 615 帧：3D 推近后正文文字发糊，见关键帧 f615.png。
```

末段原文：「最后按严重程度列出必须修复项、建议优化项和无法验证项。**不要用没有证据的"整体不错"代替逐项检查，也不要为了报告好看而全部标记通过。**」

**修复回流**：方案/分镜偏差 → 阶段 3；画面实现 → 阶段 5；声音 → 阶段 6；checklist 通过后终渲（配 BGM 的片子交付带 BGM / 无 BGM 两版，无 BGM 版靠 `--props=props-nobgm.json` 从同一时间线渲出；Windows 内联 JSON 会被 shell 剥引号，必须走文件）。

### 3.6 Remotion 渲染管线（实读配置）[实测]

- **版本与规格**：`template/package.json` → `remotion 4.0.484` / `@remotion/cli 4.0.484` / `react 19.2.7` / `typescript 6.0.3`；1920×1080@30fps，模板片 1085 帧。
- **`template/remotion.config.ts` 全文**：

```ts
import { Config } from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
Config.setChromiumOpenGlRenderer('angle');
Config.setConcurrency(4);
```

- **三条命令**（`package.json` scripts）：`npm run dev`（studio）/ `npm run render`（`remotion render src/index.ts AiflPromo out/promo.mp4`）/ `npm run still`。
- **交付前 parity**（`workbench/scripts/parity.mjs` 实读）：bundle 一次、渲多帧（默认 `--frames 150,240,470,1000`，容差 `--tolerance 2`），比对 `ProjImported`（按清单导入、未改动）与 `ProjOriginal`（工程自己的 Main）；前置先查 Pillow（「别渲完一堆帧才发现比不了」），`public/` 先 `rsync -aL` 解引用（「Remotion 静态服务器拒绝服务符号链接」）；**退出码 0 一致 / 1 有差异 / 2 无法得出结论（缺前置或比对未执行）——「绝不假绿」**。
- **工作台导出**：顶栏「导出成片」→ dev server 内起 Remotion CLI 渲当前工程到 `workbench/exports/`；`remotion.config.ts` 与 template 同口径（jpeg 帧、ANGLE GL、并发 4）。

### 3.7 浏览器工作台（`references/workbench.md` + `workbench/GUIDE.md`）[实测]

**启动**（`SKILL.md` 交付收尾第一条，主动做不等问）：

```bash
node workbench/scripts/open.mjs <成片工程目录>   # 链接工程 src/ 与 public/ → 生成索引 → dev server 5198 → 浏览器自动导入
```

首启自动 `npm install`（约 1 分钟）；`kill $(cat workbench/.dev.pid)` 停；talkcraft 5199 / shotcraft 5198 两端口错开可同开。所有改动存 localStorage；成片清单内容哈希变了才重新导入，旧改动压进撤销栈。

**三层可编辑度**（原文表）：

| 层 | 用户能改什么 | 对动效代码的要求 |
|---|---|---|
| 时间与图层（所有 clip） | 起点/时长（超出原长尾帧定格）/变速 0.25×–4×/裁入点/不透明度/缩放/位移/换轨/隐藏 | 组件是 `useCurrentFrame()` 的纯函数、tween 全部 clamp、无 `Date.now`/`Math.random` |
| 内容与样式（属性面板） | 文案/颜色/字号/位置/开关/枚举 | 语境级参数暴露为**带默认值的 props** + `schema`；顶部 `CONFIG` 常量不改就不可调 |
| 拆解导入（一键成多轨） | 每镜头/转场/字幕/音效各成一段，单独挪删复制 | 工程提供 `src/workbench.ts` 清单，时间表与 Main.tsx **同源** |

**清单契约**（`workbench/src/cards/manifest.ts` 类型 + `template/src/workbench.ts` 实例）：`WORKBENCH = { name, fps, width, height, total, background, revision?, shots[], transitions[], captions[], overlays[], sfx[], bgm[], order[], original }`；单元字段 `{ id, label, from, duration, component, props, schema, durationProp, cardId, cardName, accent }`；**时间量一律绝对帧**，与 `<Sequence from durationInFrames>` 一一对应。
模板实例的写法要点（实读）：`scene()` 工厂从 `AIFL_SHOTS[key]` 取 `from/duration`；`title()` 工厂把四张字卡合成**同一张卡**（`cardId:'title-card'`）；`schema` 的 `default` 直接引用场景导出的 `*_DEFAULTS` 对象（「属性面板里改的就是屏幕上的值，缓动/时值/相机键不暴露」）；`sfx` 从 `SFX.map(...)` 派生。

**同源与版本**：清单里每张表都从 `Main.tsx` import（「不要手抄第二份」）；`manifestKey(m) = ${name}@${total}f#${revision ?? fnv1a(canonical(m))}`——未写 `revision` 时用**清单内容哈希**（时间表/label/props/分组拓扑/组件 displayName/音效表）；组件引用变化靠**卡 id 拓扑**体现（`.name` 会被 HMR/压缩改写，纳入会误判新版本）。

**schema → Studio Inspector**：`workbench/src/remotion/zodFromCard.ts` 把 `PropField` 转 Zod（`text/textarea→z.string`，`number/slider→z.number().min().max()`，`color→zColor()`，`select→z.enum`，`boolean→z.boolean`），官方 Inspector 据此渲染表单控件。

**demo 入库**：`scripts/gen-index.mjs` 扫 `demos/<类别>/<卡>/<组件>.tsx`，凡导出 `<组件>: React.FC`（无必填 props）即接入为一张卡（**152 个 tsx 里接入 150 个**，跳过需要真实 mp4 的 `ClipCardLooping` 与辅助组件 `VerticalTicker`）；时长取值链 = demo 导出的 `*_DURATION|*_DUR` → 卡 md「时长:」的 `NNNf` → 文件内 `const *DUR*` → 缺省 150f（来源写在 `DEMO_MODULES[].durationSource`）。

**已知边界（实读 §6）**：同轨允许 clip 重叠；变速是匀速重映射；卡片库按 30fps 编排，工程 fps 不同时拖卡上轨会换算时长并反向变速；`open.mjs` 只重启自己启动的 dev server（`.dev.pid` + 进程命令行核实）；工程 `src/` 以符号链接打包，`react`/`remotion` 落到工作台 node_modules，工程用了 `three` 等额外包要先在工作台装同版本。

### 3.8 确定性实现（本仓的可复制件）[实测]

`assets/lib/helpers/rand.ts` 全文（391 B）：

```ts
// origin: 模板片源仓库 helpers
/** Deterministic PRNG — same seed always yields the same sequence. */
export const mulberry32 = (seed: number) => {
  let a = seed | 0;
  return () => {
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
};
```

同目录 `helpers/__tests__/helpers.test.ts` 是 vitest 确定性断言（覆盖 mulberry32 / velocityAt / lagged / dampedSettle / handheld）——**「确定性」在本仓有单测兜底，不只是一句纪律** `[实测]`（测试文件存在与覆盖名单来自 `SKILL.md` 与 `pr-checks.yml` 自述，未逐行读）。

---

## 4. 与 mg-styles-15 路线对比（同作者两条线）

数据来源：本手册实读 + B-13 `mg-styles-15_handbook.md`（逐文件拆解，2026-10-15）+ B-14 §2.2。`[实测]`=两侧均有文件级证据。

| 维度 | **video-shotcraft**（本仓） | **mg-styles-15**（我们 15 卡的来源） |
|---|---|---|
| 时间/规模/许可 | created 2026-07-19；11,994★；**Apache-2.0**（音频逐文件 Mixkit；Remotion 独立许可） | created 2026-10-02；868★；**MIT** |
| 定位 | agent 技能包（Claude Code / Codex 可装）——「把产品做成一支宣传片」 | 展示仓（15 风格 × 单提示词），给模型当提示词素材 |
| 渲染器 | **Remotion 4.0.484**（React 19 组件逐帧）；`remotion.config.ts`：jpeg 帧 / ANGLE GL / 并发 4 | 单文件 HTML/Canvas/WebGL + `window.renderAt(t)`；`harness/render.mjs` 用 puppeteer-core **headless Chrome 逐帧截图 → ffmpeg**（image2pipe） |
| 素材 | **真实页面截图三件套**（整页 2x + 元素抠图 + layout.json），`capture-template.mjs` | 纯代码作画（SVG/Canvas/WebGL/Three.js）；3D 片用 Blender 渲 PNG 序列后回网页合成 |
| 音频 | 录制音效库：149 SFX（16 类）+ 5 BGM（Mixkit），卡点用 librosa 分析 | **代码合成**：`audio.py` + mgaudio（numpy+numba，seeded）+ VCSL 采样 102 flac；母带链到 −14 LUFS |
| 卡/配方系统 | **124 卡 + 150 style + 152 demo**；三层（md → library.json → tsx）+ sync 脚本 + CI 漂移门 | 15 个 `prompts/*.md`（任务头/画风/内容/别做成四段）+ `demos/NN/` 三件套（index.html + audio.py + cues.json） |
| 规则体系 | `aesthetic-rules.md` **27 条判例式**（规则+判例+自检），编号只追加 | `rubric.md` 两段式评审提示词（评审 → 修改），无判例库 |
| 评审 | **干净上下文 subagent** 按 17 输入 + 八组检查项出**带帧号**报告（`final-review.md`） | 另开 AI 会话按 7 维打分（终评 7.57–8.21，均值 ≈7.86）→ 修改 → 再评审 |
| 逐镜验收 | **每镜头写死 2 个验收帧号** → `remotion still` 肉眼验收 → `out/qa/` 归档 | **先 6 关键帧**（`--stills 0,1.5,3,5,7.5,9.5`）通过后才做全片 |
| 确定性机制 | 禁 `Date.now`/`Math.random`；mulberry32 seed 从 index 派生；**helpers 有 vitest 单测** | 禁壁钟；播种随机；CSS/WAAPI `pause()+currentTime=t*1000` seek；`harness` 契约 `renderAt(t)` |
| 交付后编辑 | **浏览器工作台**（多轨/属性面板/parity 无损校验）+ 剪映工程导出 + 社交发布 | 无（产物即 mp4 + 源码） |
| CI | 4 job：单测 / 产物同步 + 媒体存在性 / 工作台构建 + 主题回归 / demo 首帧冒烟 | 无 CI（仓库未见 workflow） |
| 面向 | 产品宣传片（30–60s，功能叙事，真实 UI） | 10s MG 展示片（风格即内容，无真实产品） |
| 共同 DNA | 代码作画 · 帧 = 时间的纯函数 · 卡库 + 参考实现分离 · 独立评审两轮制 · 中文优先文档 | 同左（作者同一人，两仓互不引用 `[实测]`） |

**一句话对照** `[归纳]`：mg-styles-15 是「**单卡质量**的实验室」（一卡一提示词，做满 10s，评审打分），video-shotcraft 是「**卡库工程**的产品化」（124 卡索引化 + 工作台 + CI + 交付收尾）。我们要的两样东西恰好各在一侧：卡文本格式与判例规则在 mg-styles 侧更纯（我们的 15 卡就是它），而**索引层 / 验收工程 / 工作台契约**只有 vsc 侧有。

---

## 5. 可复用清单与不抄清单

### 5.1 可复用（逐条映射 B-11 / B-13 / B-08 / B-17）

| # | 仓库件（路径） | 抄什么 | 映射 |
|---|---|---|---|
| 1 | `references/aesthetic-rules.md` | **判例三要素**（规则 + 用户原话判例 + 自检问题）+ 编号只追加 + 「违反必须写进项目文档」+ 验收输出 `编号 ✓` / `编号 ✗(位置)` | **B-11**（style_card 的「别做成」段升级为判例格式；review_rubric 增「违反须记录」条款）· **B-13**（手册收录判例原文） |
| 2 | `references/shots/*.md` frontmatter + `gallery/api/library.json` + `sync-from-cards.py` + `pr-checks.yml` 漂移门 | **机读层**（一句话/适用/时长/能量/标签）+ 索引（stats 全量重算）+ 「产物必须与源同步」的 CI 门 | **B-11**（style_card v0.3 加 frontmatter 与「参考实现」指针）· **B-13**（给 15 卡建 library.json 式索引） |
| 3 | `pipeline.md` 阶段 5 三读硬规则 | **「索引校验 → 卡全文 → 准确 demo 源码」优先级链** + 「命门参数不得降档」+「凭卡名新写 = 放弃全部调校积累」 | **B-13**（写成章）· **B-08**（证明调校积累应落代码资产而非模型记忆） |
| 4 | `pipeline.md` 阶段 5.3 + `template/TEMPLATE.md` | **每镜头 2 个写死验收帧号** + `still` 静帧肉眼验收 + `out/qa/` 版本归档 + 「至少入场中/动作峰值/落定后三帧」抽帧口径 | **B-11**（制作侧硬要求）· **B-17**（anim_test_02 的逐镜自查清单） |
| 5 | `references/final-review.md` | **17 项审查输入清单 + 八组检查项 + 帧号证据报告格式 + 「缺输入标无法验证」+「不许全部标记通过」**；以及「制作者确认偏差 → 首检永不交给用户」的纪律 | **B-11**（评审 prompt 附件）· **B-08**（把「自查」变成 stop 条件） |
| 6 | `pipeline.md` 阶段 1 品牌→动效参数表 | **两轴推导（能量×调性）→ 6 预设**（主时长/easing/过冲/squash 全给数）+ 自检两条（三词能否对上品牌词；一套 tokens 管入场/转场/hold） | **B-11**（「控制参数（弱/中/强）」升级为两轴推导 + 预设表） |
| 7 | `references/sequences/promo-energy-arc.md` | **四段位骨架 + 呼吸字卡规则 + 填空流程五步**（先扣首尾与字卡预算 → 能量交替 → 逐槽位扫 frontmatter 挑卡） | **B-11**（10s 片骨架模板，压缩段位比例）· **B-13** |
| 8 | `assets/lib/helpers/rand.ts` + vitest 单测 | **mulberry32 + seed 从 index 派生 + tween clamp + 纯函数**，并**给确定性写单测** | **B-11**（determinism_contract 补实现级条款）· **B-17**（第二支片的确定性回归） |
| 9 | `references/workbench.md` §1–3 + `template/src/workbench.ts` + `workbench/scripts/parity.mjs` | **可编辑度分层**（语境参数开放 / 节奏命门锁死）+ **时间表唯一事实源**（派生并 export）+ `durationProp` 让拉长跟着走 + **parity 逐像素证明拆解无损**（退出码 0/1/2 不假绿） | **B-13**（「确定性管线」章收「可编辑度分层」原则）· **B-17**（若第二支片要做参数化/变速实验） |
| 10 | `SKILL.md` + `.claude-plugin/plugin.json` + `agents/openai.yaml` | **技能包四件套**：frontmatter 双语触发词（「当用户要求 X/Y/Z 时使用」）+「何时读哪个文件」路由表（渐进披露）+ 整仓即插件 + 跨 harness UI 元数据 | **B-08**（我们的「画家模块 + 代码艺术工作流」未来打包范式） |
| 11 | `assets/scripts/capture-template.mjs` + `pipeline.md` 阶段 4 | **三件套采集**（整页 2x / 元素抠图含透明底与空底板 / layout.json 坐标表）+ **「假数据先注入」红线**（空库截图直接废片、真实客户数据不能出片） | **B-17**（若第二支片改用真实页面素材）· **B-13** |
| 12 | `shot-polish/decisions.json` + `BRIEF.md` | **「卡库不是写出来的，是裁出来的」**：216 个候选逐个三选一（原版 8 / 第一版 50 / 第二版 92），砍掉 66 → 落成 150 镜；改版简报明写「只保留手法识别度，其余全部可重做」+「不许新增依赖 / 不许改导出签名 / 确定性铁律」 | **B-13**（工艺证据）· **B-11**（卡库评审口径） |
| 13 | `pipeline.md` 阶段 6 + `aesthetic-rules.md` S2/S4 | **SFX 钉帧表机制**：`{from, src, volume}` 声明式 + **from 一律相对表达式**（时间线平移自动跟随）+ 长样本显式 `durationInFrames` + **音量按素材实测峰值给**（轻音素材 7 个须换/归一化/给 >1 增益并以渲染产物验峰） | **B-13**（音频章） |
| 14 | `SKILL.md` 交付收尾 1-2-3 | **产品化叙事写成 agent 行为规范**（主动开工作台；三件事每件只说一次，用户拒绝就不再提） | **B-08**（可选，属分发与增长动作） |

### 5.2 不抄 / 要改 [归纳，理由带证据]

1. **Remotion 依赖**：Remotion 有**独立许可**（SKILL 自述「个人与小团队免费、公司可能需要付费」），Apache-2.0 只覆盖本仓代码。我们的 mg-styles 路线（headless Chrome + ffmpeg）无此依赖，**不为借卡而换渲染栈**。
2. **真实页面截图路线**：需要目标产品可本地运行 + puppeteer 采集 + 数据脱敏流程，属「复刻既有页面」专用；我们的 10s 片实验是纯代码作画，引入它只会增加前置条件。
3. **音频资产**：149 SFX + 5 BGM 是 Mixkit **逐文件授权**，不进我们的 CC0/MIT 账；我们已有 mgaudio 代码合成路线（`audio.py` + VCSL CC0），**不搬音频文件**。
4. **系统字体依赖**：`demos/README.md` 明写「少数 demo 按本机 SF Pro 实测写死了字宽/字心坐标……换字体或字号要按注释重测」——macOS 系统字体栈在 Windows 上必失效，**只借「写死坐标要重测」这条纪律**。
5. **demo 组件代码**：Apache-2.0 允许借用，但需保留版权与许可声明；本项目**不建 git、纯研究**，直接 copy 会引入授权记账负担，且会与 mg-styles 路线的实现重复。**借格式与参数结论，不借文件**。
6. **工作台整包**：Vite + React + Remotion Player 的大型前端（73 文件 + i18n），维护成本远超研究收益。**只借契约（清单结构 / 可编辑度分层 / parity 判据），不借代码**。
7. **gallery / showcase 展示层**：营销与增长设施（SEO、sitemap、NEW 徽标、提交表单），与研究无关。
8. **平台路径默认**：`MG_CHROME` 式 macOS 默认路径、`/tmp` 约定、`kill $(cat …)`——Windows 下都要改（B-13 §6.2 同款坑）。
9. **品牌资产**：`demos/_fixtures/Brand.tsx`（镜刻标志/字标/文案库 `PITCH`）与 `assets/brand/`——授权允许但含商标属性，且与我们的实验无关。
10. **文档里的旧口径**：README 图集「152 shots / 209 previews」、`llms.txt`「six-stage」——**引用前先查 `library.json` 与 `pipeline.md` 标题**，不抄数字。

---

## 6. 缺口

### 6.1 没跑（全部「行为」结论来自静态阅读）[UNVERIFIED]

- **未安装 skill、未渲染任何帧、未启动工作台、未跑 `npm test` / `tsc` / `smoke-render-demos.py` / `parity`**。本手册所有性能、时长、成本、听感结论均为**代码里的常数与文档自述**，非本机测量。
- 具体：`npx remotion still/render` 未跑（未装 template 依赖）；`capture-template.mjs` 未跑（无目标产品 dev server）；`open.mjs` 未跑（未装工作台依赖）；`sync-from-cards.py` 未跑（只读源码，未执行以验证其幂等性）。
- 因此 §3 的一切「机制描述」是**契约级**证据（源码/文档原文），不是**运行级**证据。

### 6.2 读不到 / 只抽样

1. **124 张卡只全文读了 2 张**（`opening/text-as-mask.md`、`data/chart-live-moves.md`）+ 1 张 sequence；其余 122 张只做了 frontmatter 的机读解析（键频次与键序）。**卡与卡之间的写法一致性未逐张核**。
2. **150 个 style 的 `media` 语义未逐项核**：只验证了「150 条全部有 url」与「url 形如 `./media/<name>.mp4?v=N`」（后者来自 CI 正则，非我实测）。
3. **未读的方法论文档**：`sound-design.md`（27.7 KB）、`music-beat-sync.md`（13 KB）、`jianying-export.md`、`publish-upload-post.md`、`shot-polish/BRIEF.md` 全文、`template/TEMPLATE.md` 之外的 template 源码、`workbench/GUIDE.md` 全文（只读头部）、`videos/readme-workflow/`（12 文件，未检出）。
4. **音频未听**：149 SFX / 5 BGM 只做了目录计数（16 类：transition 23 / ui 18 / impact 14 / data 13 / text 13 / camera 10 / light 10 / paper 10 / film 8 / mech 8 / fluid 5 / scifi 5 / counter 4 / glass 4 / crowd 3 / riser 1 = 149）；「长样本 21 个 / 轻音素材 7 个」两条名单来自文档自述，**未逐文件量峰值与时长**。
5. **demo TSX 只读了 1 个文件的头部 70 行**（`TextAsMask.tsx`）；`_fixtures/`（6 个共享件）未读；`_legacy/`（96 文件）未读。
6. **`gallery/media/` 54 个文件全部是 `.jpg`**（本次实测扩展名分布）——推断为画廊占位/海报图，**mp4 预览存于 GitHub release**（该机制来自 `fetch-media.sh` 与 `pr-checks.yml` 的自述，未实跑拉取）`[推测]`。

### 6.3 未做验证的推断

1. **「同源两仓互不引用」**：B-14 已实测（vsc README/README_CN/SKILL 中 `mg-styles` 命中 0）。本次**未复验**。
2. **「skill 装进 Claude Code / Codex 后的实际行为」**：未装、未跑，一切模式判别与触发词效果均为文档级 `[UNVERIFIED]`。
3. **「工作台 parity 真能证明无损」**：只读了脚本（渲染 `ProjImported` vs `ProjOriginal`、Pillow 逐像素、容差 2、差异 <0.1% 视为一致），**未跑**。

### 6.4 授权未做法律解读

Apache-2.0（代码/文档，需保留版权与许可声明 + 变更声明）、Mixkit 逐文件音频授权、Remotion 独立许可、`ATTRIBUTION.md` 自述的「手法参考 + 独立重写」实践——四者边界**本手册只做转述，不做法律结论**。若未来要借用卡文本或组件代码，须按 Apache-2.0 记账。

### 6.5 文档漂移（引用时注意）

1. `gallery/llms.txt` 写「a **six-stage** production methodology」，`references/pipeline.md` 标题是「**八阶段**制作流水线」（阶段 0–7）——本次实测 `[实测]`。
2. README 图集每类「NN shots」是 **style 口径**（camera 13 / transition 19 / typography 25），与卡数（10 / 15 / 22）不同——本次实测 `[实测]`。
3. B-14 报告的两处漂移（`demos/README.md` 与 `workbench.md` 中的「152」遗留引用）本次**未复验**；本次实测 `demos/` 下 `.tsx` = 226（含 `_legacy/` 68、`_fixtures/` 6），**非 legacy 且非 fixtures 的 demo tsx = 152**，与 `workbench.md` 的「152 个 tsx 里接入 150 个」一致。

### 6.6 建议下一步

1. **B-13 增补**：把 §2.6（判例三要素）与 §5.1 的 #3/#5 写进 mg-styles-15 手册的对应章（两仓共用一套验收语言）。
2. **B-11 修订**：`style_card.md` 加 frontmatter 机读层 + 「参考实现」指针（借 2）；「别做成」段升级为判例格式（借 1）；`review_rubric.md` 增「违反须记录」+ 帧号证据格式（借 5）。
3. **B-17 采纳**：anim_test_02 的逐镜自查用「2 个写死验收帧号 + out/qa 归档」（借 4），并给确定性回归加一条乱序重渲（与 `determinism_contract` ①b 呼应）。
4. **可选实验**：跑一次 `template/` 首帧（`npm install && npx remotion still`）把 §3.6 从契约级升到运行级——成本 = 一次 npm 安装 + 一次 still，可与 AnimTest02 的收尾合并做。

---

## 7. 机械验证（read 原样输出，2026-10-15）

**检查器**：`read` 工具直读 `raw.githubusercontent.com`（2026-10-15 实测可达）。抽 2 条：

**URL 1：`https://raw.githubusercontent.com/Vincentwei1021/video-shotcraft/main/references/shots/opening/text-as-mask.md`**

````
URL: https://raw.githubusercontent.com/Vincentwei1021/video-shotcraft/main/references/shots/opening/text-as-mask.md
Content-Type: text/plain
Method: text

---

---
name: text-as-mask
一句话: 文字视频遮罩——瓷白舞台上切出超粗大标题字，字内部透出缓慢平移的暗色实时产品面板，结尾吸一口气后字形指数冲入放大 46 倍溢出、内部画面接管全屏
适用: 品牌词/口号与产品画面二合一的开场或章节卡；字是门、产品在门里
时长: 165f（入场 18f + 字内漂移 78f + 吸气 8f + 冲入接管 24f + 落定/hold 37f）
能量: 中高（漂移段沉稳，接管段一次爆发）
标签: typography
---

## 意图
标题和产品画面抢屏幕是老问题——先字后画慢，画上压字挤。这一式让
两者同体：字形就是遮罩，产品只透过笔画显形，观众同时读到词和画面
质感；结尾字形胀开溢出画幅，产品自然接管全屏——"从品牌词走进产品"
一条镜头说完，兼任章节转场（与 transition-travel A 字腔穿越同族：
那边是镜头钻进字腔，这边是字形自己胀开，前者相机动、后者门动）。

## 动效核心
- 亮场舞台（porcelain 冷白 + 主光 + 暗角）+ SVG 白字黑底 data-URI 交给 CSS `mask-image`，遮罩层套住产品画面；
  字形下垫一层同字形、带色相的模糊投影（同样走 data-URI 图片），字像被"挖"进舞台的窗
- 窗里的内容要有大块饱和色与亮线：demo 是 video-shotcraft 的暗色渲染看板（钴蓝→青流式面积图持续向左流、渲染帧数计数、渲染队列柱状图呼吸；眉题是 video-shotcraft 字标，副题 From one prompt to a finished launch film.），
  漂移期面板上移 110px 让亮线正好穿过字的腰线、面积渐变铺满字的下半截——白卡/浅色 UI 透进白底字里会读成普通字
- 入场：遮罩从基线向上擦出（clip-path 底边收起，16f）+ 1.04→1 落定；眉题字距收拢、副题升起
- 字内漂移：产品层 scale 1.32 + translateX +150→-150（f18–96，bezier(0.3,0,0.7,1) 两端轻缓）——
  字形静止、内容流动，"窗外有世界"的错觉即手法本体
- 吸气：f96–104 字 1→0.965（swift），眉题/副题 ease-in 退场——大动作前的预备
- 冲入 24f（f104–128）：mask wrapper `scale(0.965→46)`，对数空间里按 t^1.8 插值
  （`S = s0·(46/s0)^(t^1.8)`，每帧放大比例越来越大 = 越冲越快）；
  **transform-origin 必须钉在实心笔画内**（demo 取 L 竖笔中线 1236,546）——钉在字腔空洞里则放大后透出的是底色；
  冲入同时 wrapper 平移 `(960−Ox, 540−Oy)·t`，把竖笔拉回画面中线（否则偏右的竖笔要到 30× 才盖住左缘）
- 内容层反向补偿：套一层 `scale(1/S) translate(−d)`（同一 origin）抵消 wrapper 的放大与平移，产品画面
  不随遮罩几何畸变；面板同时 1.32→1、漂移归零（expo-out，f104–132，比冲入晚 4f 收敛 = 跟随）
- 接管保险：另叠一个共享同一 translate/scale 变换的无遮罩全屏层，只在竖笔已撑满全屏（t^1.8 ∈ [0.86, 0.95]，S≈24×）
  之后淡入——更早淡入会在亮底上叠出一层半透明灰纱
- 收尾：f132–165 全屏面板 hold，流式图仍缓慢流动（产品活着，不是死帧）
## 参数表
| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 字号/字重 | 470px / 900（system-ui Black，字距 −22） | 笔画就是视口——细字重等于把产品塞进门缝；字宽占画幅 ~72% |
| 漂移速度 | ~3.8px/f（300px/78f） | 快了字内画面读不清；漂移方向选画面信息密的轴 |
| 吸气 | 8f，1→0.965 | 没有吸气的冲入读作"突然胀开"；>0.94 读作字在缩小退场 |
| 放大倍率 | 46×（按竖笔宽/画幅比配：88px 竖笔需 ≥24× 才撑满） | 不足则接管帧还看得到字边残影 |
| 冲入曲线 | 对数空间 t^1.8，24f | 线性对数 = 匀速冲入；指数 >2.5 前半段几乎不动、最后 3f 猛胀 |
| 收尾 | 接管后 hold ≥30f | R1；接管完成帧产品应落在标准构图 |
## 已知坑
- demo 用的是为镜头设计的 video-shotcraft 渲染看板（Render throughput，侧栏是品牌标志）——实战换真实截图时先看笔画里透出的是不是大块色与亮线，
  浅色页面要先调暗或换暗色主题，否则字读不出"窗"
- 别给字形做描边高光：system-ui 等可变字体的字形由重叠轮廓拼成，描边会画出 A 的横杠/顶角等内部轮廓线
- 字内透出的产品画面全程被特写盯着看——真实素材先过
  审美准则 Q2 的高分辨率栅格化技法，低倍截图在笔画里糊成一片
- 换词/换字体后 origin 手推值必失效——渲后看放大方向，洞不对中就微调
  origin（同 transition-travel A 字腔穿越的腔心漂移坑）
- 与 transition-travel A 字腔穿越同片不并用——同为"字里长出世界"，
  观众读作同一招使两次（P4）
- mask 层与内容层的 transform 必须分离驱动（wrapper 放大/内容反向补偿），
  合在一层则产品跟着字形一起胀成 26 倍废片

## 参考实现
demos/opening/text-as-mask/
（TextAsMask.tsx）
````

**URL 2：`https://raw.githubusercontent.com/Vincentwei1021/video-shotcraft/main/references/sequences/promo-energy-arc.md`**

````
URL: https://raw.githubusercontent.com/Vincentwei1021/video-shotcraft/main/references/sequences/promo-energy-arc.md
Content-Type: text/plain
Method: text

---

---
name: promo-energy-arc
一句话: 全片能量骨架——低开品牌 → 单主角立传 → 字卡呼吸间隔的功能爬升段 → 发布会峰值收场
适用: 30–60s 多功能 web 产品宣传片的默认全片结构（分镜阶段先填骨架再挑卡）
段数: 4 段位 + 2–4 张呼吸字卡
---

## 意图

把散落在 R1–R3/Q5/Q8/P4 的节奏规则合成一条可直接填空的全片曲线。
模板片成片（1085f）与两次独立复现（各 900f）三次成表均收敛到同一
骨架——它是默认项，不是令：逐项目可有意识偏离，偏离写进项目 spec。

## 段位表

| 段位 | 时长占比 | 能量 | 职责 | 候选配方卡 |
|------|----------|------|------|------------|
| ① 品牌开场 | 8–12%（30s 片）；开场+立传合计可达 20%（模板片） | 低 | 字标压印 + hold ≥1s（R1），交棒产品页面 | brand-ink-open |
| ② 单主角立传 | 12–15% | 中（质感最高、节奏最慢） | 一个主角、一条完整动作弧 ≥3s（Q5/R3），立出产品原子单位 | spotlight-hero-card（+aesthetic-rules.md Q2 高清 rasterize 技法） |
| ③ 功能爬升段 | 55–65% | 中高⇄低交替 | 每镜绑一个独特功能、一种手法只当一次主角（P4）；镜与镜之间按需插呼吸字卡 | deck-deal-flyin / type-and-filter / list-stack-press / row-embed / document-typewriter-reveal |
| ④ 发布会收场 | 13–16% | 峰值（全片最高） | 已展示功能各出代表元素合影围住字标（Q8），sign-off hold ≥1s（R1） | outro-group-photo-launch |

呼吸字卡（paper-title-card）规则：每 1–2 个功能镜头后插一张，单张
50–55f（≈1.8s），全片 2–4 张；重要功能出场前用作引导字卡（C2）。
模板片 10 镜里字卡占 4 席，两次复现各 2 席——密度按功能镜头数取。

## 填空流程（替代 ad-hoc 推导）

1. 列产品功能清单（P4），数出功能镜头数 N。
2. 按段位表分配总帧数：先扣 ①②④ 与字卡的预算，剩余给 ③ 均分。
   每镜预算内**先划走 hold/rest 帧**（R1 落定 ≥30f、批量收尾 15f，R3）
   再排动效——不是排完动效再找空隙。
3. ③ 段能量交替：高能量镜（发牌/堆叠）与稳节奏镜（交互/读字段）
   间隔排列，信息密度最高的镜头（文档/报告类）放在峰值收场之前——
   模板片与两次复现均把文档/报告类镜头排在倒数第 2–3 位。
4. 逐槽位扫 shots/ frontmatter 挑卡，选中的卡读全文。
5. 镜头排定后逐接缝选转场式（shot-transitions 技法卡三式选型），
   写进分镜表"关键动效"列——转场帧从相邻镜头预算划走。

## 已知坑

- 骨架当风格令全局硬套：段位占比是模板片单例实证（标注：单例判例），
  15s 短片或单功能产品应大胆合并段位，但 ①hold/④峰值两端不可省。
- ③ 段只堆高能量镜：连续高能量读作嘈杂，交替与字卡就是节奏本身。
- 呼吸字卡写成第二遍 tagline：字卡与 outro 文案重复即删（P4 判例：
  outro tagline 去重）。

## 参考实现

template/src/aifl/Main.tsx AIFL_SHOTS 段位表（sum=1085f）。
````

**附加机械校验**（sha256，2026-10-15）：克隆文件与 raw main 逐字节一致（本地 CRLF 归一化后比对；本机 `core.autocrlf=true` 造成 checkout 换行差异）：

```
references/shots/opening/text-as-mask.md      local-normalized 75fcfe12effe6508 == raw 75fcfe12effe6508  MATCH
references/sequences/promo-energy-arc.md      local-normalized 0bad18a5661a24ec == raw 0bad18a5661a24ec  MATCH
gallery/api/library.json                      local-normalized 1adcdf77a3681eac == raw 1adcdf77a3681eac  MATCH
```

---

## 自审四段（LOOP 协议）

**A · 早产出**：先读 B-14 前置卡与项目 AGENTS/GOALS → 稀疏克隆（HEAD `13c74a7`）→ 按 §1→§7 逐节填充；§2.2/§2.4/§2.6 的数字均为**全量机读**（124 卡 frontmatter 解析、150 style 键并集、27 条规则逐条），不是抽样；§7 的两条 raw URL 为 read 工具原样输出。

**B · 反驳（5 条最强结论试推翻）**：

1. **「三层结构（md → library.json → tsx）由脚本 + CI 强制同步」** → 推翻尝试：读 `sync-from-cards.py` 全文 + `pr-checks.yml` 全文。结果：脚本确有 `SystemExit` 硬失败路径与 stats 重算；CI 用 `git status --porcelain -- gallery` 而非 diff（注释解释了 untracked 新卡副本的盲区）。**CONFIRMED**（机制层面；未实跑脚本）。
2. **「每镜头 2 个验收帧号是硬要求」** → 推翻尝试：对照 `template/TEMPLATE.md`（「每镜头至少入场中/动作峰值/落定后三帧」）与 `pipeline.md` 阶段 5.3（「写死 2 个验收帧号」）。结果：**数字不一致但机制同源**——计划纪律是 2 个、模板抽帧口径是 ≥3 个。结论**WEAKENED**（已在 §3.4 加口径注记，不写成单一数字）。
3. **「150 style 全部有实现、无降级标记」** → 推翻尝试：grep 124 卡 `仅供参考`/`缺少预览` = 0；150 style 的 `implementationStatus` = 0 条；`STYLE_STATUS` 源码注释「Currently empty: every style has demo source」。**CONFIRMED**（并纠正了 B-14 转述 SKILL 时易误读为「库里存在这类标记」的印象）。
4. **「克隆 == 当前 raw main」** → 推翻尝试：先直接比 sha256 → 3/3 DIFF；再查换行（本机 `core.autocrlf=true`）→ 归一化后 3/3 MATCH。**CONFIRMED**（且证明首次 DIFF 是环境假象，不是内容漂移）。
5. **「demo tsx = 152」** → 推翻尝试：tree 全量计数 tsx = 226，含 `_legacy/` 68 + `_fixtures/` 6 → 226−68−6 = **152**。**CONFIRMED**（`workbench.md` 的「152 个 tsx」口径成立；B-14 未给分母，本手册已补）。

**C · 机械验证（原样输出，2026-10-15）**：见 §7（两条 raw URL 的 read 原样输出 + 三条 sha256 归一化比对）。另：§2.2 的 frontmatter 键频次、§2.4 的分类卡/style 计数、§2.6 的 27 条规则标题、§1.2 的文档字节数，均由本次会话内的 python/bash 全量统计产生，命令与结果已在对话中留档（可复跑：`python -c "…frontmatter 解析…"` / `grep -c '^### [A-Z]' references/aesthetic-rules.md`）。

**D · 小结**（≤14 行）
1. 本手册 = vsc 的第一份**文件级**拆解：§1 仓库地图（1648 entry 全量分类）、§2 卡系统三层 + library.json 机读 schema + 27 条判例规则、§3 八阶段 + 2 帧号 QA + 干净上下文终检 + 工作台契约 + parity、§4 两路线对照、§5 14 条可复用 + 10 条不抄、§6 缺口。
2. 最值钱三样：**判例三要素**、**机读层 + 漂移门**、**帧号证据验收链**——都能不依赖 Remotion 直接搬。
3. 已纠正 B-14 的三处口径：卡 frontmatter 原文（§2.2 注）、style 降级标记当前为空、152 tsx 的分母。
4. 未跑任何渲染/工作台/测试：全部机制为契约级证据，性能与听感结论缺席（§6.1）。
5. 下一步：B-11 按 §5.1 的 #1/#2/#5/#6 修订模板与评审表；B-13 增补判例章；B-17 采纳 2 帧号自查；可选跑 template 首帧把 §3.6 升到运行级。
