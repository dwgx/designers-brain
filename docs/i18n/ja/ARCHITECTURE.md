# アーキテクチャ

> 本ファイルは翻訳版です。英語正本が優先されます（最新変更に遅れる場合があります）。
Translation baseline: README/docs as of 2026-10-15 (commit 534924e+)

[English](../../ARCHITECTURE.md) · [中文](../zh-CN/ARCHITECTURE.md) · 日本語

> Designers_Brain は、アーティストとデザイナーの視覚言語を、AI エージェントが実行できる合成可能・検証可能なモジュールへと蒸留し、どのエージェントでも読み込めるスキルとしてパッケージ化します。リポジトリをエージェントに渡せば、まず問いを立て、それからエビデンスに基づいて設計・置換を行います。

## 1. アイデア

ほとんどの「スタイルプロンプト」は雰囲気でしかありません。本プロジェクトはそれを**エンジニアリング成果物**に変えます：

- **蒸留**——各ドメイン（まずは画家から）について一次資料（作品、書簡、論考、研究文献）を読み、視覚言語の背後にある*操作可能なルール*を抽出し、合成・調整・検証ができる**モジュール**へ圧縮します。
- **エビデンス等級**——すべての主張にはタグを付けます：`[自述]`（本人の証言 / 一次引用）、`[史料]`（史料）、`[研究]`（研究文献）、`[归纳]`（本プロジェクトによる帰納）、`[推测]`（推測）。等級は主張とともに、下流のあらゆる成果物へ引き継がれます。
- **実験**——すべてのモジュールは、機械チェック付きでエンドツーエンドに実行されます（画像生成、Web アニメーション、Blender シーン）。裏付けのない主張は `[UNVERIFIED]` のままです。
- **スキル**——蒸留されたナレッジはエージェントスキル（`skills/designers-brain/`）としてパッケージ化され、あらゆる有能なエージェントを設計コンサルタントに変えます：まず適切な質問をし、コンフリクトのプリチェック付きでモジュールを推薦し、3 つの形式（画像プロンプト / 10 秒の Web アニメーション / Blender ブリーフ）のいずれかで出力します。

プロジェクト名はその野心を表しています：*デザイナーのための脳*——ドメインごとに深いリサーチを行い、外へ広げていきます。

## 2. リポジトリ構成

```
designers-brain/
├── README.md · README.zh-CN.md · README.ja.md   — public face (EN primary + translations)
├── LICENSE · LICENSE-CODE · NOTICE.md            — CC BY 4.0 (content) + MIT (code) + third-party notices
├── AGENTS.md · CLAUDE.md                         — entry points for AI agents
├── CONTRIBUTING.md                               — how to contribute (domains, cards, fixes)
├── docs/
│   ├── ARCHITECTURE.md · WORKFLOW.md · PROTOCOLS.md · ROADMAP.md
│   ├── MIGRATION.md                              — layout history (old → new paths)
│   ├── skill/                                    — skill design research: ecosystem study, spec, tests, walkthrough
│   └── i18n/zh-CN/ · i18n/ja/                    — translations of the four docs above
├── knowledge/                                    — the distilled product
│   ├── INDEX.md                                  — full source/image index
│   ├── domains/
│   │   ├── painters/       (dossiers/ + modules/) — domain #1: 62 painters
│   │   └── motion-graphics/ (cards/ + origin/ + sources/) — domain #2: 15 MG style cards
│   ├── cross/                                    — cross-domain rules: conflicts, transfer guide, review rubric, image channel
│   └── agent-art/                                — how agents make art with code: HTML/Blender pipelines, prompt corpus, evidence
├── skills/designers-brain/                       — the consumable skill (SKILL.md + references/ + domains.yaml)
├── experiments/                                  — evidence runs (E-series + animation tests), scripts included
├── templates/                                    — reusable templates (module, style card, determinism contract, design brief)
└── ops/                                          — AI-ops state: GOALS.md (work queue) · OPS-LOG.md (append-only log)
```

## 3. ナレッジモデル

### 3.1 レイヤー

```
sources ──▶ dossiers ──▶ modules / cards ──▶ skill (pointers only)
(quotes,     (full evidence    (operational,      (routing + protocols,
 images,      per artist,       composable)        never copies content)
 literature)  ~300–600 lines each)
```

- **ドシエ（資料ファイル）**（`knowledge/domains/painters/dossiers/`）——画家ごとのエビデンスファイル：視覚的フィンガープリント、技法ルール、制作原則、制御パラメータ、出典付き引用、画像マニフェスト。画家 62 名、各約 300〜600 行。
- **モジュール**（`.../modules/`）——画家ごとの*モジュールカード*：画像プロンプトのセグメント（§8.1 / §8.1b スタイル専用）、コードアートのルール（§8.2）、制御パラメータ（§4）、コンフリクトの注記。カードはドシエから機械的に抽出されます（`_extract.py`、逐語チェック 186 件）。
- **横断ルール**（`knowledge/cross/`）——モジュール間のコンフリクト（C-01–C-18）、コンポジション（組み合わせ）ルール（N1–N9）、モデル転移ガイド、レビュールーブリック、画像チャネルのドキュメント。
- **スキル**（`skills/designers-brain/`）——ポインタによって上記へルーティングします。コンテンツを複製しないため、ナレッジの更新にスキルの編集は不要です。

### 3.2 ドメインと登録契約

ドメインは `skills/designers-brain/domains.yaml` に登録されます。ドメインが `active` になれるのは、以下をすべて備えている場合のみです：

1. カードディレクトリ（1 カードにつき 1 ファイル、インデックスと整合）。
2. インデックス（ケイパビリティマップ + コンポジションの注記）。
3. コンフリクト一覧（または汎用ルール + ドメイン差分の明示的な再利用）。
4. 出力形式のマッピング（画像プロンプト / Web アニメーション / Blender——どれがサポートされ、フィールドがどう異なるか）。
5. 強度メカニズム（または明示的なギャップマーカー）。
6. エビデンス（実験）または `[UNVERIFIED]` ステータス。
7. レジストリエントリ + セルフチェックのカバレッジ。

アクティブなドメイン：`painter`（モジュール 62 件）、`mg-motion`（スタイルカード 15 枚）。新しいドメイン（写真、タイポグラフィなど）は、同じ契約を満たすことで組み込めます。

### 3.3 エビデンス等級

`[自述]` 本人の証言（出典必須） · `[史料]` 史料 · `[研究]` 研究文献 · `[归纳]` 本プロジェクトによる帰納 · `[推测]` 推測。検証されていない能力は `[UNVERIFIED]` とマークされ、提供済みとして約束されることはありません。

## 4. スキル

- **入口**：`skills/designers-brain/SKILL.md`（段階的開示：カタログ → 本文 → リファレンス）。
- **アクティベーション（ローカル）**：ハーネスのスキャンパスへのジャンクション（ディレクトリ結合。`~/.agents/skills`、`~/.claude/skills`、`~/.codex/skills`）。リポジトリ内セッション用のプロジェクトレベル `.agents/skills/` もあります。
- **配布**：プラグインマニフェスト（`.claude-plugin/plugin.json`、`.codex-plugin/plugin.json`、`.agents/plugins/marketplace.json`）。
- **対話プロトコル**（全文はスキル内）：最初のアクションは**初回質問パッケージ（first-ask package）**（ビジネス / オーディエンス / 素材 / スタイルの意図 / 置換軸——3+2 の記入式、デフォルトは口頭で明示）。会話は ≤3 ラウンド。視覚的な決定には*目に見える*候補が必要で、提示後は停止します。`design-brief.md` ゲートファイルに、意図・前提・承認範囲を記録します。
- **置換セマンティクス**：コンテンツを変える（骨格は維持）/ スタイルを変える（コンテンツは維持）/ 強度を調整する——モードごとに明示的なロック区間を伴います。
- **出力形式**：画像プロンプト（チャネル：ゲートウェイ直結の `grok-imagine-image-2.0`。ネガティブプロンプトのチャネルなし。768×1152）、10 秒の Web アニメーション・ブリーフ（決定論コントラクト C1–C10 + 順序を変えた再実行チェック）、Blender ブリーフ（C9 + P1 決定論の注記）。

## 5. 実験

`experiments/` にエビデンスがあります。各実験ディレクトリには、スクリプト、生のリクエスト / レスポンスのアーカイブ、出力、そして検証スクリプト（`_verify*.py`）が含まれ、その PASS が受け入れゲートとなります。

- `E1_t1*`——12 セルのスタイル転写マトリクス：ベースライン、題材バイアスの診断、スタイル専用セグメントの分割（7/7 解消）。
- `E2_t1`——最初のコンポジション・バッチ（モネ×ファン・ゴッホ、ダ・ヴィンチ×カラヴァッジョ、モネ×セザンヌ）：融合は成立し、コンフリクト軸は二者択一またはゾーニングで解決。
- `anim_test_01/02/03`——非フロンティアモデルで検証された 3 本のエンドツーエンド・パイプライン：ピクセルカード（Web）、一筆書きカード（Web）、3D テクスチャカード（Blender）。主要な発見：*パイプラインは移行できるが、スタイルのメカニズムは書き直しと対応する機械チェックが必要*。

## 6. 運用（AI 運用）

本リポジトリは **AI エージェントによって運用**されており、ops レイヤーは第一級の要素です：

- `ops/GOALS.md`——作業状態の唯一の情報源（各項目：ステータス / 目標 / 成果物パス / 担当 + 受け入れ条件の行）。
- `ops/OPS-LOG.md`——追記専用：チャネル状態、インシデント、教訓、承認記録。
- **LOOP**：目標を取る → 深いリサーチ → 成果物を着地（エビデンス等級付き） → 自己レビュー → メインブレインの受け入れ → 新しい手がかりをキューへ。詳細は `docs/WORKFLOW.md`、ハードルールは `docs/PROTOCOLS.md`。
- マシンレベルのディスパッチボードはリポジトリ外（`~/.dwgx/ops/boards/`）にあります——ボードはスナップショットであり、情報源にはなりません。

## 7. ドキュメントと i18n

- `docs/` は英語で書かれています（正本）。`docs/i18n/zh-CN/` と `docs/i18n/ja/` は `ARCHITECTURE / WORKFLOW / PROTOCOLS / ROADMAP` をミラーしています。ルートの README 3 言語版は GitHub の慣例に従います。
- 翻訳は用語の一貫性の観点でレビューされます。英語原本が実質的に変更された場合、翻訳は更新されるか、明示的に stale としてマークされます。
- 生のリサーチノート（ドシエ、ログ）の作業言語は引き続き中国語です。公開インターフェースは 3 言語です。

## 8. 拡張ポイント

- **新しいドメイン** → 登録契約（§3.2）+ `domains.yaml` エントリ + セルフチェックのカバレッジ。
- **新しい出力形式**（例：印刷用ポスター、動画） → 出力形式のマッピングに、必須フィールド + 決定論 / 検証の注記とともに追加。
- **新しいパイプライン**（例：Blender → Web） → プローブと検証スクリプトとともに `knowledge/agent-art/` に文書化。
- **新しい言語** → `docs/i18n/<lang>/` + README の言語版をミラーし、言語スイッチャーに追加。

## 9. 非目標

- モデル訓練のプロジェクトではありません（ファインチューニングなし、LoRA 訓練なし——蒸留されたナレッジはプロンプト / コードのレベルです）。
- サードパーティメディアの再配布は行いません（動画・リファレンスクリップは除外。`.gitignore` と `NOTICE.md` を参照）。
- エビデンス等級のない主張はしません。実行可能なチェックのない「完了」はありません。
