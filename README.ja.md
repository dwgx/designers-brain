# Designers_Brain

> 本ファイルは翻訳版です。英語正本が優先されます（最新変更に遅れる場合があります）。
Translation baseline: README/docs as of 2026-10-15 (commit 534924e+)

[English](README.md) · [中文](README.zh-CN.md) · 日本語

> **デザイナーのための脳。** アーティストとデザイナーの視覚言語を、深いリサーチによって合成可能・検証可能なモジュールへと蒸留し、**設計する前に問いを立てる**エージェントスキルとしてパッケージ化したものです。

[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE-CODE)

## これは何か

このリポジトリを AI エージェントに渡すと、設計コンサルタントになります。まず適切な質問をし、蒸留済みライブラリからスタイルを推薦し、組み合わせる前にコンフリクトをチェックし、エビデンス付きで成果物を出力します——画像プロンプト、10 秒の Web アニメーション、または Blender ブリーフです。

収録内容：

- **画家ドシエ（資料ファイル）11 件**（ダ・ヴィンチ、ミケランジェロ、ファン・ゴッホ、モネ、ピカソ、セザンヌ、マティス、北斎、カラヴァッジョ、フェルメール、デューラー）——各約 300 行のエビデンス、出典付き引用 126 件、パブリックドメイン作品 33 点。
- **合成可能なモジュールカード 11 枚** + **モーショングラフィックスのスタイルカード 15 枚**（10 秒アニメーションの骨格）。
- **モジュール横断ルール**：コンフリクト項目 18 件（C-01–C-18）+ コンポジション（組み合わせ）ルール N1–N9。
- **スキル**（`skills/designers-brain/`）——ask-first（まず問いを立てる）コンサルタントプロトコルを実装。
- **機械チェック付きの実験**：スタイル転写マトリクス（E シリーズ）と 3 本のエンドツーエンド・アニメーションパイプライン（Web ×2、Blender ×1）。

## クイックスタート

### 1. スキルを読み込む

```bash
# Claude Code / Codex / omp — activate via junction (no copy):
# (Windows PowerShell)
New-Item -ItemType Junction -Path "$HOME\.claude\skills\designers-brain" `
  -Target "<path-to-repo>\skills\designers-brain"
```

あとは設計作業を頼むだけです：*「スタイルを選んでポスターを作ってほしい。対象は …」*——スキルは設計 / 置換のリクエストで発動します。パッケージング用のプラグインマニフェストも同梱されています（`.claude-plugin/`、`.codex-plugin/`、`.agents/plugins/`）。

### 2. ナレッジを見る

- まず [`knowledge/INDEX.md`](knowledge/INDEX.md)（ソースの全インデックス）から。
- 画家モジュール：[`knowledge/domains/painters/modules/`](knowledge/domains/painters/modules/)——各カードはそのままプロンプトに合成できます。
- モーションスタイル：[`knowledge/domains/motion-graphics/`](knowledge/domains/motion-graphics/)。
- コンポジションルール：[`knowledge/cross/conflicts.md`](knowledge/cross/conflicts.md)。

### 3. 実験を再現する

```bash
# module-card verbatim check (33 checks)
python knowledge/domains/painters/modules/_extract.py --check

# image experiment verification (example: composition batch)
cd experiments/E2_t1 && python _verify_e2.py
```

## 仕組み

1. **深いリサーチ**——画家 / ドメインごとの一次資料。すべての主張にエビデンス等級（`[自述]/[史料]/[研究]/[归纳]/[推测]`＝本人の証言 / 史料 / 研究文献 / 帰納 / 推測。識別子は原文のまま）を付与します。
2. **蒸留**——エビデンスは操作可能なルールへ圧縮されます：合成・調整・機械チェックができるモジュールです。
3. **検証**——主張する前に、すべての能力をエンドツーエンドで実行します。検証スクリプトは成果物とともに配布されます。
4. **AI 運用**——リポジトリは明示的なプロトコル（`docs/WORKFLOW.md`、`docs/PROTOCOLS.md`）の下で AI エージェントが運用しています。作業状態は `ops/GOALS.md` にあります。

## リポジトリ構成

```
knowledge/    distilled product (domains, cross rules, agent-art pipelines, index)
experiments/  evidence runs (E-series, animation tests) with scripts & verifiers
skills/       designers-brain — the consumable agent skill
docs/         architecture, workflow, protocols, roadmap (+ zh-CN / ja translations)
ops/          GOALS.md (work queue) · OPS-LOG.md (append-only log)
templates/    module / style-card / determinism / design-brief templates
```

## デモ成果物

- アニメーションパイプライン：`experiments/anim_test_01/out.mp4` · `anim_test_02/out.mp4` · `anim_test_03_blender/out.mp4`
- スタイル分離の比較：`experiments/E1_t1b/compare_all_t1b.png`
- コンポジションシート：`experiments/E2_t1/sheet_all_e2.png`
- スキル・ウォークスルー（カフェのアイデンティティ、3 案）：`docs/skill/walkthrough_01/candidates/compare_candidates.png`

## ステータス

**PRE マイルストーン完了**（2026-10）：最初の 2 ドメインを蒸留し、スキルを構築してブラインドテストし、3 本のパイプラインをエンドツーエンドで検証しました。次はドメイン拡張、強度スイープ、人手スコアリング——[`docs/ROADMAP.md`](docs/ROADMAP.md) を参照。

## ライセンス

コンテンツとドキュメント：[CC BY 4.0](LICENSE)。コード：[MIT](LICENSE-CODE)。サードパーティ：[NOTICE.md](NOTICE.md) を参照。
