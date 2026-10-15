# i18n 監査 · ja ↔ EN（5 対ファイル）

> **For:** Designers_Brain · R-03（i18n ja 品質監査）、2026-10-15。
> **対象（5 対 / 10 ファイル）:** `README.md` ↔ `README.ja.md` ／ `docs/ARCHITECTURE.md` ↔ `docs/i18n/ja/ARCHITECTURE.md` ／ `docs/WORKFLOW.md` ↔ `docs/i18n/ja/WORKFLOW.md` ／ `docs/PROTOCOLS.md` ↔ `docs/i18n/ja/PROTOCOLS.md` ／ `docs/ROADMAP.md` ↔ `docs/i18n/ja/ROADMAP.md`
> **ベースライン:** 各 ja ファイル L4 の「Translation baseline: README/docs as of 2026-10-15 (commit 534924e+)」。監査時 HEAD は `a296b6f`。534924e 以降の EN 側変更（README のライセンス表記・バッジ、ARCHITECTURE のツリー 1 行）は ja に反映済みであることを確認（旧 `LICENSE-CONTENT.md` 参照の残存なし）。
> **方法:** 全文対読による逐句抽出 19 箇所（各ファイル 2 箇所以上）＋ 機械照合（コードブロックの SHA-256 バイト比較／インラインコード・リンク・太字・斜体のスパン比較／識別子・数値の出現数カウント／見出し・箇条書き・表の構造パリティ）。
> **証拠等級:** `[研究]`（直接対照）＋ `[归纳]`（修正提案・判断）。
> **声明:** 読み取り専用監査。被監査ファイルは未変更、本監査による追加は本ファイルのみ。

## 0. 結論サマリ

**判定: PASS-with-notes。**

- 逐句抽出 19 箇所（R 4 / A 5 / W 3 / P 4 / Ro 3）: 意味・強調・制限条件の漂流は検出されず、日本語としても自然。
- 用語 17 項目: 15 項目 OK、2 項目に軽微な指摘（ジャンクション初出注＝P-1、ドシエ注の 1 ファイル欠落＝P-4）。
- ゼロ翻訳・ゼロ改変 10 箇所: 全通過（コードブロック 5/5 バイト一致、識別子・リンク・コマンド完全保持）。
- 問題リスト: 4 件（低 ×3・極小 ×1）＋情報 1 件。すべて編集レベルで、リリースを阻害しない。

## 1. 抽出記録（逐句抽出 19 箇所 — 各ファイル 2 箇所以上）

判定は「意味／強調／制限条件の漂流」と「日本語技術文書としての自然さ」を確認した結果。位置は「EN 行 ↔ JA 行」。

### README（4 箇所）

**R1. タグライン**（`README.md:3` ↔ `README.ja.md:8`）
- EN: > **A brain for designers.** Deep-research distillation of artists' and designers' visual languages into composable, verifiable modules — packaged as an agent skill that **asks before it designs**.
- JA: > **デザイナーのための脳。** アーティストとデザイナーの視覚言語を、深いリサーチによって合成可能・検証可能なモジュールへと蒸留し、**設計する前に問いを立てる**エージェントスキルとしてパッケージ化したものです。
- 判定: 意味一致。強調（太字）位置対応（asks before it designs ↔ 設計する前に問いを立てる）。自然。漂流なし。

**R2. 収録内容① 画家ドシエ**（`README.md:16` ↔ `README.ja.md:19`）
- EN: - **11 painter dossiers** (da Vinci, Michelangelo, Van Gogh, Monet, Picasso, Cézanne, Matisse, Hokusai, Caravaggio, Vermeer, Dürer) — ~300 lines of evidence each, 126 sourced quotes, 33 public-domain artworks.
- JA: - **画家ドシエ（資料ファイル）11 件**（ダ・ヴィンチ、ミケランジェロ、ファン・ゴッホ、モネ、ピカソ、セザンヌ、マティス、北斎、カラヴァッジョ、フェルメール、デューラー）——各約 300 行のエビデンス、出典付き引用 126 件、パブリックドメイン作品 33 点。
- 判定: 数値（11 / 約 300 / 126 / 33）・人名 11 名の順序すべて一致。初出注「（資料ファイル）」は翻訳注の追加（他ファイルと同型、意味変更なし）。

**R3. 収録内容③ モジュール横断ルール**（`README.md:18` ↔ `README.ja.md:21`）
- EN: - **Cross-module rules**: 18 conflict entries (C-01–C-18) + composition rules N1–N9.
- JA: - **モジュール横断ルール**：コンフリクト項目 18 件（C-01–C-18）+ コンポジション（組み合わせ）ルール N1–N9。
- 判定: 識別子 C-01–C-18 / N1–N9 は原文のまま（en dash 含め文字同一）。件数 18 一致。「composition」初出注あり。漂流なし。

**R4. 仕組み① 等級タグ**（`README.md:54` ↔ `README.ja.md:57`）
- EN: 1. **Deep research** — primary sources per artist/domain; every claim carries an evidence grade (`[自述]/[史料]/[研究]/[归纳]/[推测]`).
- JA: 1. **深いリサーチ**——画家 / ドメインごとの一次資料。すべての主張にエビデンス等級（`[自述]/[史料]/[研究]/[归纳]/[推测]`＝本人の証言 / 史料 / 研究文献 / 帰納 / 推測。識別子は原文のまま）を付与します。
- 判定: 等級タグは原文保持＋読み注を追加（「識別子は原文のまま」）。意味・制限条件の漂流なし。

### ARCHITECTURE（5 箇所）

**A1. リード文**（`docs/ARCHITECTURE.md:3` ↔ `docs/i18n/ja/ARCHITECTURE.md:8`）
- EN: > Designers_Brain distills the working languages of artists and designers into composable, verifiable modules that AI agents can execute — and packages them as a skill any agent can load. Give the repo to an agent; it asks first, then designs and replaces with evidence.
- JA: > Designers_Brain は、アーティストとデザイナーの視覚言語を、AI エージェントが実行できる合成可能・検証可能なモジュールへと蒸留し、どのエージェントでも読み込めるスキルとしてパッケージ化します。リポジトリをエージェントに渡せば、まず問いを立て、それからエビデンスに基づいて設計・置換を行います。
- 判定: 意味一致（「working languages」→「視覚言語」は README の「visual languages」と語を統一した訳語選択。許容範囲。直訳なら「制作言語」等）。「any agent can load」「asks first, then designs and replaces with evidence」保持。漂流なし。

**A2. §1 蒸留**（`docs/ARCHITECTURE.md:9` ↔ `docs/i18n/ja/ARCHITECTURE.md:14`）
- EN: - **Distillation** — for each domain (starting with painters), we read primary sources (works, letters, treatises, scholarship), extract the *operational rules* behind a visual language, and compress them into **modules** that can be composed, tuned, and verified.
- JA: - **蒸留**——各ドメイン（まずは画家から）について一次資料（作品、書簡、論考、研究文献）を読み、視覚言語の背後にある*操作可能なルール*を抽出し、合成・調整・検証ができる**モジュール**へ圧縮します。
- 判定: 要素・強調（*操作可能なルール*／**モジュール**）対応。「composed, tuned, and verified」→「合成・調整・検証」。漂流なし。

**A3. §3.2 登録契約の制限条件**（`docs/ARCHITECTURE.md:60` ↔ `docs/i18n/ja/ARCHITECTURE.md:65`）
- EN: Domains are registered in `skills/designers-brain/domains.yaml`. A domain may be `active` only if it ships all of:
- JA: ドメインは `skills/designers-brain/domains.yaml` に登録されます。ドメインが `active` になれるのは、以下をすべて備えている場合のみです：
- 判定: 「only if … all of」の制限条件を「…場合のみです／すべて」で保持。続く 7 項目の数・順序も一致。漂流なし。

**A4. §4 アクティベーション（junction）**（`docs/ARCHITECTURE.md:79` ↔ `docs/i18n/ja/ARCHITECTURE.md:84`）
- EN: - **Activation (local)**: junction into the harness scan path (`~/.agents/skills`, `~/.claude/skills`, `~/.codex/skills`); project-level `.agents/skills/` for repo-local sessions.
- JA: - **アクティベーション（ローカル）**：ハーネスのスキャンパスへのジャンクション（`~/.agents/skills`、`~/.claude/skills`、`~/.codex/skills`）。リポジトリ内セッション用のプロジェクトレベル `.agents/skills/` もあります。
- 判定: パス 3 種・プロジェクトレベル `.agents/skills/` 保持。「ジャンクション」に初出注なし → §4 P-1 参照。

**A5. §4 対話プロトコル**（`docs/ARCHITECTURE.md:81` ↔ `docs/i18n/ja/ARCHITECTURE.md:86`）
- EN: - **Interaction protocol** (full text in the skill): first action is the **first-ask package** (business / audience / materials / style intent / replacement axis — 3+2 fill-in, defaults spoken aloud); ≤3 conversation rounds; visual decisions require *visible* candidates and stop after showing; a `design-brief.md` gate file records intent, assumptions, and approval scope.
- JA: - **対話プロトコル**（全文はスキル内）：最初のアクションは**初回質問パッケージ（first-ask package）**（ビジネス / オーディエンス / 素材 / スタイルの意図 / 置換軸——3+2 の記入式、デフォルトは口頭で明示）。会話は ≤3 ラウンド。視覚的な決定には*目に見える*候補が必要で、提示後は停止します。`design-brief.md` ゲートファイルに、意図・前提・承認範囲を記録します。
- 判定: 5 項目・3+2・≤3・*visible*・提示後停止・ゲートファイルの記録内容すべて一致。漂流なし。

### WORKFLOW（3 箇所）

**W1. §1 メインブレインの役割**（`docs/WORKFLOW.md:8` ↔ `docs/i18n/ja/WORKFLOW.md:13`）
- EN: - **Main brain** (the top-level agent session): sets direction, slices work, dispatches, accepts results (reads artifacts + runs acceptance), synthesizes, and maintains `ops/GOALS.md`, this file, and `docs/`.
- JA: - **メインブレイン**（最上位のエージェントセッション）：方向づけ、作業の切り分け、ディスパッチ、成果の受け入れ（成果物を読み、受け入れ条件を実行）、統合、そして `ops/GOALS.md`・本ファイル・`docs/` の維持管理を担当します。
- 判定: 全要素一致（役割 6 項目 + 維持対象 3 件）。漂流なし。

**W2. §3 LOOP 手順 4（自己レビュー 4 部構成）**（`docs/WORKFLOW.md:28` ↔ `docs/i18n/ja/WORKFLOW.md:33`）
- EN: 4. Self-review in four parts: **A early output** (land something first, then continue) → **B rebuttal** (try to overturn your 3–5 strongest claims; tag `CONFIRMED/WEAKENED/OVERTURNED` + the command run; delete overturned claims from artifacts) → **C mechanical verification** (name one checker; paste raw output) → **D ≤14-line summary** (established / overturned / unknown / next).
- JA: 4. 自己レビューは 4 部構成です：**A 早期アウトプット**（まず何かを着地させ、それから続けます） → **B 反論**（自分の最強の主張 3〜5 件を覆してみます。`CONFIRMED/WEAKENED/OVERTURNED` タグ + 実行したコマンドを記録。覆った主張は成果物から削除） → **C 機械検証**（チェッカーを 1 つ指定し、生の出力を貼ります） → **D ≤14 行のサマリ**（確定 / 覆った / 不明 / 次）。
- 判定: 4 部構成・「3–5」→「3〜5」・タグ・「≤14」すべて一致（数値範囲の波ダッシュ化は日本語表記の慣例）。漂流なし。

**W3. §5 エビデンス基準②**（`docs/WORKFLOW.md:41` ↔ `docs/i18n/ja/WORKFLOW.md:46`）
- EN: - Numbers carry denominator + date; "not found" ≠ "does not exist" (write "未找到（已查: …）").
- JA: - 数値には分母 + 日付を付けます。「見つからない」 ≠ 「存在しない」（「未找到（已查: …）」と書きます）。
- 判定: 中国語の定型句を原文のまま保持。意味一致。漂流なし。

### PROTOCOLS（4 箇所）

**P1. §1.1 書き手 1 人原則**（`docs/PROTOCOLS.md:7` ↔ `docs/i18n/ja/PROTOCOLS.md:12`）
- EN: 1. **One writer per path.** Any file has exactly one writer at a time (a person, an agent, or the main brain). Parallel writers coordinate via explicit handoff, never by both editing.
- JA: 1. **パスごとに書き手は 1 人。** どのファイルにも、同時点で書き手はちょうど 1 人だけです（人間、エージェント、またはメインブレイン）。並行する書き手は明示的なハンドオフで調整し、両者が同時に編集することはありません。
- 判定: 「exactly one … at a time」「never by both editing」の制限条件を保持。漂流なし。

**P2. §5 コンポジション完全プリチェック**（`docs/PROTOCOLS.md:40` ↔ `docs/i18n/ja/PROTOCOLS.md:45`）
- EN: - Composition of two modules requires the full pre-check, in order: conflict table scan → near-miss explicit values → N1 anti-constraint recompute → N3 axis-ownership (auxiliary conflict lines are **removed entirely**, never downgraded) → N4 split decision (same pixel statistic → pick one; separable regions → zoning table + mask) → N9 acceptance (main module full set + auxiliary non-conflict axes; "dual standards on a conflict axis" is a failure).
- JA: - 2 つのモジュールのコンポジション（組み合わせ）には、順序どおりの完全なプリチェックが必要です：コンフリクト表のスキャン → ニアミスの明示値 → N1 反制約の再計算 → N3 軸所有権（補助的なコンフリクト行は**完全に削除**し、決して降格させません） → N4 分割の判断（同一の画素統計 → 一方を選ぶ。分離可能な領域 → ゾーニング表 + マスク） → N9 受け入れ（メインモジュールのフルセット + 補助の非コンフリクト軸。「コンフリクト軸における二重基準」は失敗です）。
- 判定: 手順順序・識別子（N1/N3/N4/N9）・「**完全に削除**し、決して降格させません」・「二重基準は失敗」をすべて保持。漂流なし。

**P3. §4 決定論コントラクト**（`docs/PROTOCOLS.md:34` ↔ `docs/i18n/ja/PROTOCOLS.md:39`）
- EN: - **Determinism contracts** (animation/code output): C1–C10 in `templates/determinism_contract.md`, including the **out-of-order re-render check** — sequential re-renders can hide state bugs; always re-render a non-contiguous sample and compare frame hashes.
- JA: - **決定論コントラクト**（アニメーション / コード出力）：`templates/determinism_contract.md` の C1–C10。**順序を変えた再レンダーチェック**を含みます——連続した再レンダーは状態バグを隠し得るため、常に非連続のサンプルを再レンダーし、フレームハッシュを比較してください。
- 判定: C1–C10・非連続サンプルの再レンダー・フレームハッシュ比較を保持。漂流なし。

**P4. §6 画像チャネル（素のモデル名）**（`docs/PROTOCOLS.md:46` ↔ `docs/i18n/ja/PROTOCOLS.md:51`）
- EN: - Channel: direct gateway API; **bare model name** `grok-imagine-image-2.0` (a `buddyfarm/` prefix 404s on this path — opposite of the CLI). Request 1024×1536; actual return 768×1152.
- JA: - チャネル：ゲートウェイ直結 API。**素のモデル名** `grok-imagine-image-2.0`（このパスでは `buddyfarm/` プレフィックスを付けると 404 になります——CLI とは逆）。要求は 1024×1536、実際の返却は 768×1152。
- 判定: モデル名・プレフィックス挙動（404）・解像度 2 種を保持。漂流なし。

### ROADMAP（3 箇所）

**D1. 現在地・スキル行**（`docs/ROADMAP.md:7` ↔ `docs/i18n/ja/ROADMAP.md:12`）
- EN: - **Skill**: `designers-brain` v0.2 — built, activated (junctions + packaging), RED-GREEN blind test PASS, full walkthrough (café identity, 3 directions) with gate file and independent review.
- JA: - **スキル**：`designers-brain` v0.2——ビルド・アクティベート済み（ジャンクション + パッケージング）、RED-GREEN ブラインドテスト PASS、フルウォークスルー（カフェのアイデンティティ、3 案）をゲートファイル + 独立レビュー付きで実施。
- 判定: v0.2・RED-GREEN PASS・3 案・ゲートファイル／独立レビュー一致。「junctions」→「ジャンクション」は注なし（§4 P-1 関連、ROADMAP 内は 2 番目の出現箇所）。

**D2. フェーズ 1・E3 強度スイープ**（`docs/ROADMAP.md:14` ↔ `docs/i18n/ja/ROADMAP.md:19`）
- EN: - **E3** intensity sweep (30 / 50 / 75 / 100%) for painter modules — the "tunable strength" promise is currently `[UNVERIFIED]`.
- JA: - **E3** 画家モジュールの強度スイープ（30 / 50 / 75 / 100%）——「強度を調整できる」という約束は現在 `[UNVERIFIED]` です。
- 判定: パーセンテージ 4 種・`[UNVERIFIED]` を保持。漂流なし。

**D3. 原則・スタイル機構の書き直し**（`docs/ROADMAP.md:34` ↔ `docs/i18n/ja/ROADMAP.md:39`）
- EN: - Pipelines transfer across models; **style mechanisms must be rewritten with matching mechanical checks** (verified finding).
- JA: - パイプラインはモデル間で移行できる。**スタイルのメカニズムは書き直しと対応する機械チェックが必要**（検証済みの発見）。
- 判定: 強調位置対応。「must be rewritten」の義務を「書き直し…が必要」で保持。漂流なし。

## 2. 用語チェック表（17 項目）

出現数は部分文字列カウント（複合語を含む）。R=README.ja / A=ARCHITECTURE.ja / W=WORKFLOW.ja / P=PROTOCOLS.ja / Ro=ROADMAP.ja。

| 用語 | EN 対応語 | 出現数 R/A/W/P/Ro | 初出注・備考 | 判定 |
|---|---|---|---|---|
| ドシエ | dossier(s) | 1/3/1/1/2 | 初出注「（資料ファイル）」: R・A・W・Ro は初出に付与、**P のみ無し** | 概ね一貫（P-4） |
| モジュール | module(s) | 5/8/1/2/4 | 表記揺れなし | OK |
| モジュールカード | module card(s) | 1/1/1/0/1 | 「カード」系は「枚」で計数 | OK |
| スタイルカード | style card(s) | 1/1/0/1/1 | 同上 | OK |
| レーン | lane(s) | 0/0/4/0/0 | 見出し・表・本文で一貫 | OK |
| LOOP プロトコル | LOOP protocol | 0/0/2/0/0 | A は「LOOP」（EN 同様の使い分け） | OK |
| メインブレイン | main brain | 0/1/4/1/0 | 一貫 | OK |
| ワーカー | worker(s) | 0/0/4/0/0 | リサーチ／クロスハーネス／外部 の修飾で一貫 | OK |
| ゲートファイル | gate file | 0/1/0/1/1 | 一貫 | OK |
| ジャンクション | junction(s) | 0/1/0/0/1（+README コードブロック内 1） | **初出注なし**（zh-CN は「junction（目录联接）」と注記） | 要対応（P-1） |
| スキル | skill | 6/7/1/3/3 | 一貫 | OK |
| パイプライン | pipeline(s) | 3/3/1/0/3 | 一貫 | OK |
| 検証スクリプト | verifier (script) | 1/2/0/2/0 | EN の verifier / verifier script を「検証スクリプト」に統一 | OK |
| 受け入れ条件 | acceptance condition | 0/1/3/1/0 | 「受け入れゲート」「受け入れ」は EN の acceptance gate 等に対応させた使い分け | OK |
| コンフリクト軸 | conflict axis | 0/1/0/2/0 | 一貫 | OK |
| エビデンス等級 | evidence grade | 1/4/1/2/1 | タグ本体は原文保持。読み注の形式が R/W/P（「本人の証言 / 史料 / …」）と A（タグ別注）でやや異なるが内容は同一 | OK |
| 登録契約 | registry contract | 0/2/0/1/1 | 一貫 | OK |

補足: 初出注（借用語の意味・読み注）の付与状況 — ドシエ「（資料ファイル）」4/5 ファイル、コンポジション「（組み合わせ）」4/4 ファイル、ask-first / first-ask package の注 3 箇所、**ジャンクション 0/2 箇所（唯一の欠落）**。タグ読み注は 3 ファイルで「識別子は原文のまま」を明記。

## 3. ゼロ翻訳・ゼロ改変の対照（10 箇所）

コードブロックはフェンス内テキスト（UTF-8 / LF、フェンス記号を除く）の SHA-256 バイト比較。照合は読み取り専用の一時スクリプトで実施（リポジトリへの追加物なし）。

1. **README コードブロック①（bash / junction コマンド）** — `README.md:26–31` ↔ `README.ja.md:29–34`。**バイト一致**（212 B、SHA-256 `b00975ccd5af582f59ee7ded160fc4545f2271b9ecc598190d4253ce7a6ea873`）。`New-Item -ItemType Junction …` 以下、コメント含め原文のまま。
2. **README コードブロック②（bash / 検証コマンド）** — `README.md:44–50` ↔ `README.ja.md:47–53`。**バイト一致**（209 B、`3ae05f03f72c940f55a065a35cba6c2cf25d27ceec2d795fdab9fba270591ce0`）。`python …/_extract.py --check`・`cd experiments/E2_t1 && python _verify_e2.py` 保持。
3. **README コードブロック③（リポジトリ構成）** — `README.md:61–68` ↔ `README.ja.md:64–71`。**バイト一致**（450 B、`27a102a2cd5d4d8a8e262e0c86c28f021457fd63f8b8b03f960d06cb4f32677d`）。
4. **ARCHITECTURE コードブロック①（リポジトリツリー）** — `docs/ARCHITECTURE.md:18–40` ↔ `docs/i18n/ja/ARCHITECTURE.md:23–45`。**バイト一致**（2008 B、`8a054a84d15d61fc7403a80b7e4b5a34e27e91b6373feb610cf15a30f4118d11`）。パス・`—` 区切り・英語注記すべて原文のまま。
5. **ARCHITECTURE コードブロック②（レイヤー図）** — `docs/ARCHITECTURE.md:46–51` ↔ `docs/i18n/ja/ARCHITECTURE.md:51–56`。**バイト一致**（260 B、`f5dd96d01148e2f318c6e2d86c014a29c2b0cdafca999c83f723e7a8da48ea65`）。
6. **エビデンス等級タグ** — 連結形 `` `[自述]/[史料]/[研究]/[归纳]/[推测]` `` は R・A・W・P で文字列完全一致。個別タグの出現数も全ファイルで一致（`[自述]` 等: R 1/1・A 2/2・W 1/1・P 1/1）。`[UNVERIFIED]`: A 3/3・P 1/1・Ro 2/2。
7. **識別子 N1–N9 / C-01–C-18** — 出現数一致（R: C-01/C-18 1/1・N1/N9 1/1。A: 各 1/1。P: N1 3/3・N3/N4/N9 各 1/1・C-01/C-18 各 2/2）。P のチェック順序 `N1 → N3 → N4 → N9` も一致。範囲記号は en dash（U+2013）のまま文字同一。
8. **決定論系識別子 C1–C10 / C9 / P1 / P0** — 出現数一致（A: C1/C9/C10/P1 各 1/1。P: C1/C10/P1 各 1/1。Ro: P0 1/1・P1 2/2）。文字同一。
9. **リンク** — README 両版とも 12 本で、差分はスイッチャーのみ（EN「日本語」→ `README.ja.md` ／ JA「English」→ `README.md`、現言語は非リンクの慣例どおり）。docs は ja 側にスイッチャー 2 本（`[English](../../X.md)`・`[中文](../zh-CN/X.md)`）を追加。相対パスは全ターゲット実在（デッドリンク 0）、バッジ・本文の URL は完全一致。
10. **インラインコード** — 全 5 ペアでマルチセット完全一致（R 19/19・A 52/52・W 30/30・P 37/37・Ro 11/11）。例: `board.py close --verify`・`_verify*.py`・`grok-imagine-image-2.0`・`buddyfarm/`・`mg-styles-15`・`E1_t1b/c`・`~/.dwgx/ops/boards/`・`CONFIRMED/WEAKENED/OVERTURNED`。

補足（許容差として記録）: 数値範囲は EN の en dash を ja の波ダッシュに置換（`250–380`→`250〜380`、`3–5`→`3〜5`、`2–3`→`2〜3`。数値は不変、日本語表記の慣例）。識別子範囲（C-01–C-18 等）は置換していない。構造パリティも確認: 見出し数 11/13/8/12/7、箇条書き数 17/38/15/41/24、WORKFLOW の表 16 行 × 列数同一、太字 13/13・23/23・18/18・22/22・8/8、斜体 1/1・5/5・0/0・5/5・0/0。

## 4. 問題リスト（位置 + 証拠 + 修正案）

いずれも意味の漂流ではなく、表記統一・初出注・可読性に係る軽微な指摘。**本監査ではファイルを修正していない（提案のみ）。**

**P-1【低】ジャンクションの初出注が無い**
- 位置: `docs/i18n/ja/ARCHITECTURE.md:84`（初出）、`docs/i18n/ja/ROADMAP.md:12`（2 箇所目）。README.ja はコードブロック内の英語のみ（`README.ja.md:30` "activate via junction (no copy)"）。
- 証拠: zh-CN 版は同箇所で「junction（目录联接）」と注記（`docs/i18n/zh-CN/ARCHITECTURE.md:84`、`docs/i18n/zh-CN/ROADMAP.md:12`）。ja は他の借用語に初出注を付与する方針（ドシエ・コンポジション・first-ask package 等）だが、ジャンクションのみ注が無い。
- 修正案（例）: 初出の ARCHITECTURE §4 に「…スキャンパスへのジャンクション（コピーせずにディレクトリをリンクする Windows の仕組み）…」のように一言注を付す。

**P-2【低】「Entry」の訳語が揺れている（入口 / エントリ）**
- 位置: `docs/i18n/ja/WORKFLOW.md:8`（「入口：」） ↔ `docs/i18n/ja/ARCHITECTURE.md:83`（「**エントリ**：」）。
- 証拠: 同一 EN 語 "Entry"（`docs/WORKFLOW.md:3` / `docs/ARCHITECTURE.md:78`）に対する訳が 2 通り。「エントリ」は他に `ARCHITECTURE.md:73`・`115`・`WORKFLOW.md:23` でも使用（4 対 1）。
- 修正案: どちらかに統一（推奨: 多数派の「エントリ」。または両方を「入口」に）。混在の解消のみで意味は不変。

**P-3【低・可読性】「パス」の多義（pass / path）による誤読余地**
- 位置: `docs/i18n/ja/ARCHITECTURE.md:92`「…検証スクリプト（`_verify*.py`）が含まれ、そのパスが受け入れゲートとなります。」
- 証拠: EN 原文は "whose pass is the acceptance gate"。同一ファイル内で「パス」は path の意味で多用（成果物パス `:102`、スキャンパス `:84`、書き込みパス `WORKFLOW.md:15` 等）され、「そのパス」が一瞬 path と読める。
- 修正案（例）: 「検証にパスすることが受け入れゲートとなります」または「その合格が受け入れゲートとなります」。

**P-4【極小】ドシエの初出注が PROTOCOLS のみ欠落**
- 位置: `docs/i18n/ja/PROTOCOLS.md:30`「ドシエの各節は等級を明記します。」
- 証拠: 他 4 ファイルの初出は「（資料ファイル）」付き（`README.ja.md:19`・`ARCHITECTURE.md:58`・`WORKFLOW.md:21`・`ROADMAP.md:10`）。
- 修正案: 「ドシエ（資料ファイル）の各節は…」に揃えるか、ファイル単位初出注の適用範囲（初出が 1 回のみのファイルは省略可等）を明文化して許容とする。

**P-5【情報】EN 側 docs に言語スイッチャーが無い（翻訳からの片方向リンク）**
- 位置: `docs/ARCHITECTURE.md`・`WORKFLOW.md`・`PROTOCOLS.md`・`ROADMAP.md`（EN）。ja / zh-CN の各文書は L6 にスイッチャーを持つ（例: `docs/i18n/ja/ARCHITECTURE.md:6`）。
- 証拠: ja 4 文書 + zh 4 文書に `[English](…) · [中文](…) · 日本語/中文` 行あり。EN docs には相当行なし（README は EN 側にもスイッチャーあり）。
- 修正案: 次回同期時に (a) EN docs にもスイッチャーを追加する、(b) 翻訳専用の導線として現状維持とする、のいずれかを方針決定（EN 側の変更は本監査の対象外）。

## 5. 結論

**判定: PASS-with-notes**

- 逐句抽出 19 箇所（R 4 / A 5 / W 3 / P 4 / Ro 3）で、意味・強調・制限条件の漂流は検出されず。日本語技術文書としても自然（軽微な指摘は P-1〜P-4 の 4 件のみで、いずれも意味には影響しない）。
- ゼロ翻訳・ゼロ改変は達成: コードブロック 5/5 がバイト一致、インラインコード・識別子（N1–N9 / C-01–C-18 / 等級タグ / C1–C10 / P0–P1）・リンク・コマンドは完全保持。スイッチャー・翻訳バナー・baseline・用語注以外の追加・削除なし（構造パリティ一致）。
- 用語 17 項目: 15 項目 OK、2 項目に軽微な指摘（ジャンクションの初出注＝P-1、ドシエ注の 1 ファイル欠落＝P-4）。
- 推奨アクション: P-1〜P-4 を次回編集時に一括反映（例: ジャンクション注の追加、Entry 訳の統一、パス表現の言い換え、ドシエ注の追加）。P-5 は日英スイッチャー方針として判断。次回 EN 更新時は各 ja ファイル L4 の baseline（commit / 日付）更新を忘れないこと。
- 留意: 本監査は EN ↔ ja の対照（zh-CN は参照のみ）。監査時点の HEAD は `a296b6f`、ja はベースライン「534924e+」の内容と一致していることを確認済み。
