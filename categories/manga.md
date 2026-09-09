# 漫画・イラスト編集

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ai-comic-factory](https://github.com/jbilcke-hf/ai-comic-factory) · [詳細](#ai-comic-factory) | LLMと画像生成を連携してコマを作るAI漫画アプリの参考実装。 | AI連携 / 旧版・履歴資料 | 1,345 / 2025-10-30 |
| [krita](https://github.com/KDE/krita) · [詳細](#krita) | 漫画・イラスト制作に使うデジタルペイントアプリ。 | 非AI制作 / 定番の制作基盤 | 10,341 / 2026-09-09 |
| [manga-editor-desu](https://github.com/new-sankaku/manga-editor-desu) · [詳細](#manga-editor-desu) | ブラウザでコマ割り、吹き出し、縦書き、レイヤー編集とAI生成連携を行う。 | AIは任意 / 更新のある導入・評価候補 | 384 / 2026-08-30 |
| [OpenKoma](https://github.com/Reuben-Sun/OpenKoma) · [詳細](#openkoma) | 手持ち画像をコマに配置し、複数ページの漫画に組み立てる編集ツール。 | 非AI制作 / 小規模・初期評価候補 | 12 / 2026-05-08 |

<a id="ai-comic-factory"></a>

## ai-comic-factory

LLMと画像生成を連携してコマを作るAI漫画アプリの参考実装。

- **リポジトリ**: https://github.com/jbilcke-hf/ai-comic-factory
- **分類**: web_app / AI連携 / 旧版・履歴資料
- **入力**: ストーリー指示
- **出力**: コミックページ
- **環境**: Webアプリ環境と推論バックエンド。
- **依存**: LLM、SDXL等の設定された画像バックエンド
- **制約・未確認**: GitHubでarchived=true。現在の活発な開発候補には含めない。
- **編集者評価**: ストーリーからコマ生成への構成を学ぶ資料として残す。
- **メトリクス**: ★1,345、fork 312、作成 2023-08-25、最終push 2025-10-30T19:17:30Z、archived=True
- **確認**: 2026-09-09 / コミット `c5dc3c7dafeb593efa3b7c95431ee982965bb524`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/jbilcke-hf/ai-comic-factory/blob/c5dc3c7dafeb593efa3b7c95431ee982965bb524/README.md)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/jbilcke-hf/ai-comic-factory/blob/c5dc3c7dafeb593efa3b7c95431ee982965bb524/README.md) / [GitHub API](https://api.github.com/repos/jbilcke-hf/ai-comic-factory) / [固定ツリー](https://github.com/jbilcke-hf/ai-comic-factory/tree/c5dc3c7dafeb593efa3b7c95431ee982965bb524)

<a id="krita"></a>

## krita

漫画・イラスト制作に使うデジタルペイントアプリ。

- **リポジトリ**: https://github.com/KDE/krita
- **分類**: desktop_tool / 非AI制作 / 定番の制作基盤
- **入力**: ラフ、筆入力、画像素材
- **出力**: イラスト・漫画用デジタル原稿
- **環境**: Windows・macOS・Linux向け配布。
- **依存**: 通常の描画にはAIモデル不要
- **制約・未確認**: GitHubは公式ミラーで、開発元はKDE。標準アプリをAI生成モデルとして扱わない。
- **編集者評価**: 生成結果の手直しや原稿制作を担う定番基盤。
- **メトリクス**: ★10,341、fork 849、作成 2015-10-09、最終push 2026-09-09T15:31:07Z、archived=False
- **確認**: 2026-09-09 / コミット `75db0d95e142c9251dc27483180148f77d4de014`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/KDE/krita/blob/75db0d95e142c9251dc27483180148f77d4de014/COPYING)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/KDE/krita/blob/75db0d95e142c9251dc27483180148f77d4de014/README.md) / [GitHub API](https://api.github.com/repos/KDE/krita) / [固定ツリー](https://github.com/KDE/krita/tree/75db0d95e142c9251dc27483180148f77d4de014)

<a id="manga-editor-desu"></a>

## manga-editor-desu

ブラウザでコマ割り、吹き出し、縦書き、レイヤー編集とAI生成連携を行う。

- **リポジトリ**: https://github.com/new-sankaku/manga-editor-desu
- **分類**: browser_tool / AIは任意 / 更新のある導入・評価候補
- **入力**: 画像、セリフ、コマ割り、生成指示
- **出力**: 漫画ページ・複数ページの編集プロジェクト
- **環境**: ブラウザ。AI生成には対応するローカルバックエンド等。
- **依存**: 画像素材、任意の画像生成バックエンド
- **制約・未確認**: 文字・吹き出しやページ切り替え時の編集履歴などは実作業で確認が必要。
- **編集者評価**: 漫画固有の編集操作と画像生成をつなぐ有力候補。
- **メトリクス**: ★384、fork 54、作成 2023-08-14、最終push 2026-08-30T17:00:19Z、archived=False
- **確認**: 2026-09-09 / コミット `04e0cf3de1f3677682f6d1831f2713db70e441ba`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/new-sankaku/manga-editor-desu/blob/04e0cf3de1f3677682f6d1831f2713db70e441ba/LICENSE)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/new-sankaku/manga-editor-desu/blob/04e0cf3de1f3677682f6d1831f2713db70e441ba/README.md) / [GitHub API](https://api.github.com/repos/new-sankaku/manga-editor-desu) / [固定ツリー](https://github.com/new-sankaku/manga-editor-desu/tree/04e0cf3de1f3677682f6d1831f2713db70e441ba)

<a id="openkoma"></a>

## OpenKoma

手持ち画像をコマに配置し、複数ページの漫画に組み立てる編集ツール。

- **リポジトリ**: https://github.com/Reuben-Sun/OpenKoma
- **分類**: browser_tool / 非AI制作 / 小規模・初期評価候補
- **入力**: キャラ画像、背景、セリフ
- **出力**: 漫画ページPNG、PDF、プロジェクトJSON
- **環境**: ブラウザ、ソース実行はNode.js。
- **依存**: 入力する画像・テキスト素材
- **制約・未確認**: 小規模な新規候補。AI画像モデルそのものは含まない。
- **編集者評価**: 生成画像を編集可能な漫画ページへまとめる用途が具体的。
- **メトリクス**: ★12、fork 2、作成 2026-04-05、最終push 2026-05-08T08:27:39Z、archived=False
- **確認**: 2026-09-09 / コミット `aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Reuben-Sun/OpenKoma/blob/aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Reuben-Sun/OpenKoma/blob/aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c/README.md) / [GitHub API](https://api.github.com/repos/Reuben-Sun/OpenKoma) / [固定ツリー](https://github.com/Reuben-Sun/OpenKoma/tree/aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c)
