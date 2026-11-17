# Designers_Brain

> 本ファイルは翻訳版です。英語正本が優先されます（最新変更に遅れる場合があります）。
Translation update: 2026-11-15 — learning navigation, capability scope and host-specific loading; historical counts retained.

[English](README.md) · [中文](README.zh-CN.md) · 日本語

> **デザイナーのための脳。** アーティストとデザイナーの視覚言語を、深いリサーチによって合成可能・検証可能なモジュールへと蒸留し、**設計する前に問いを立てる**エージェントスキルとしてパッケージ化したものです。

[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE-CODE)

## これは何か

このリポジトリを AI エージェントに渡すと、設計コンサルタントになります。まず適切な質問をし、蒸留済みライブラリからスタイルを推薦し、組み合わせる前にコンフリクトをチェックし、エビデンス付きで成果物を出力します——画像プロンプト、10 秒の Web アニメーション、または Blender ブリーフです。

収録内容：

- **画家ドシエ（資料ファイル）76 件**（ダ・ヴィンチ、ミケランジェロ、ファン・ゴッホ、モネ、ピカソ、セザンヌ、マティス、北斎、カラヴァッジョ、フェルメール、デューラーほか）——各約 300〜600 行のエビデンス、出典付き引用 2044 件、出典付き作品画像 739 点：**パブリックドメイン / CC0 が 701 点 ＋ 帰属表示が必要なオープンライセンス画像 38 点**（[NOTICE.md](NOTICE.md) 参照）。*（PRE マイルストーン時点の数値も記録として保持：62 件 / 1613 件 / 618 点——「画像はすべてパブリックドメイン」という従来の記述は、うち 38 点については正しくありません。）*
- **合成可能なモジュールカード 76 枚** + **モーショングラフィックスのスタイルカード 15 枚**（10 秒アニメーションの骨格）。*（PRE：62 枚。）*
- **モジュール横断ルール**：コンフリクト項目 18 件（C-01–C-18）+ コンポジション（組み合わせ）ルール N1–N9。
- **スキル**（`skills/designers-brain/`）——ask-first（まず問いを立てる）コンサルタントプロトコルを実装。
- **機械チェック付きの実験**：スタイル転写マトリクス（E シリーズ）と 3 本のエンドツーエンド・アニメーションパイプライン（Web ×2、Blender ×1）。

- **76 件の学習パスと 65 件の新しいスタイル候補**。出典、反例、[具体的な読書ルート](knowledge/domains/painters/learning/INDEX.md)を含み、既存の 11 節は元のカードへリンクしています。
- **エビデンスの範囲を示す[能力マトリクス](knowledge/CAPABILITIES.md)**。画像、Web アニメーション、Blender を個別に評価し、過去の成果、部分的な実装、未検証を区別します。

## クイックスタート

### 1. スキルを読み込む

リポジトリを開き、エージェントに [`skills/designers-brain/SKILL.md`](skills/designers-brain/SKILL.md) を読ませます。参照先を読む前に、実際のスキルからリポジトリのルートを解決してください。

```text
python -X utf8 -B skills/designers-brain/resolve_repo.py --json
python -X utf8 -B docs/skill/_selfcheck.py --repo-only
```

OMP では `skills.customDirectories` を、この checkout の **`skills` 親ディレクトリ**に設定します。設定と `skill://` の読み取り確認は[ローカル利用ガイド](docs/skill/local-usage.md)を参照してください。他のホストには固有の検出・インストール方法があり、一つの junction を共通のインストールとは扱いません。

具体的なデザインの依頼を入力すると、スキルは不足する要件を確認し、出力経路を約束する前に能力マトリクスを読みます。ホストでの検出、自動選択、実際のレンダリングは別々に検証します。

### 2. ナレッジを見る

- まず [`knowledge/INDEX.md`](knowledge/INDEX.md)（ソースの全インデックス）から。
- 画家モジュール：[`knowledge/domains/painters/modules/`](knowledge/domains/painters/modules/)——各カードはそのままプロンプトに合成できます。
- モーションスタイル：[`knowledge/domains/motion-graphics/`](knowledge/domains/motion-graphics/)。
- コンポジションルール：[`knowledge/cross/conflicts.md`](knowledge/cross/conflicts.md)。

### 3. 実験を再現する

```bash
# module-card verbatim check (228 checks — 76 枚 × §8.1/§8.2/§4)
python knowledge/domains/painters/modules/_extract.py --check

# image experiment verification (example: composition batch)
cd experiments/E2_t1 && python _verify_e2.py
```

## 仕組み

1. **深いリサーチ**——画家 / ドメインごとの一次資料。すべての主張にエビデンス等級（`[自述]/[史料]/[研究]/[归纳]/[推测]`＝本人の証言 / 史料 / 研究文献 / 帰納 / 推測。識別子は原文のまま）を付与します。
2. **蒸留**——エビデンスは操作可能なルールへ圧縮されます：合成・調整・機械チェックができるモジュールです。
3. **検証**——出力経路、実装、確認項目と制限を記録します。能力マトリクスは supported、conditional、unsupported、untested を区別し、過去の検証結果は元の範囲を保持します。
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

2026 年 11 月の研究更新では、学習パス、スタイル候補、出典付きナビゲーション、出力別の能力状態を統合しています。既存の証拠が支える範囲は[能力マトリクス](knowledge/CAPABILITIES.md)を参照してください。練習案やスタイルの文章だけでは、画像生成、ブラウザ描画、Blender の実行、学習効果を実証できません。

10 月の PRE マイルストーンは過去の記録として保持します。現在のリリースの正式な受け入れは、正確なバージョンを紐付けたリリースノートで確認します。作業ツリーやローカルコミット自体は公開済みの証明ではありません。今後の研究方向は [`docs/ROADMAP.md`](docs/ROADMAP.md) を参照してください。

## ライセンス

コンテンツとドキュメント：[CC BY 4.0](LICENSE)。コード：[MIT](LICENSE-CODE)。サードパーティ：[NOTICE.md](NOTICE.md) を参照。

画像ライセンスは**一様ではありません**：出典付き作品画像 739 点のうち 701 点がパブリックドメインまたは CC0、38 点がオープンライセンス（CC BY 3.0/4.0、CC BY-SA 3.0/4.0、ColBase 利用規約、台北国立故宮博物院オープンデータ）で、再配布時には**画像ごとのクレジット表示が必須**です。区分と帰属要件は [NOTICE.md](NOTICE.md#images-not-pdcc0-38) を参照。
