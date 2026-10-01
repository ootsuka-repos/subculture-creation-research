# 絵コンテ・制作管理・評価

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-01。**143件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Kitsu](https://github.com/cgwire/kitsu) · [詳細](#kitsu) | アニメ・VFX・ゲーム制作の成果物、レビュー、進行を管理するWebアプリ。 | 非AI制作 / 制作基盤として比較 | 726 / 2026-09-30 |
| [Storyboarder](https://github.com/wonderunit/storyboarder) · [詳細](#storyboarder) | 絵コンテを描き、ショットの順序と時間を試すアニマティクス制作ツール。 | 非AI制作 / 既存研究・制作の参考 | 3,862 / 2024-03-17 |
| [StyleID](https://github.com/kwanyun/StyleID) · [詳細](#styleid) | 画風変化に強い顔の同一性特徴を計算し、比較・検索・評価に使う。 | AIモデル・学習 / 小規模・初期候補 | 34 / 2026-08-16 |
| [Nomi](https://github.com/aqm857886159/Nomi) · [詳細](#nomi) | ローカル優先のAI動画制作スタジオ。エージェントがショット分割・キーフレーム生成・動画化・タイムライン配置を支援する。 | AIモデル・学習 / 活発・候補 | 537 / 2026-10-01 |

<a id="kitsu"></a>

## Kitsu

アニメ・VFX・ゲーム制作の成果物、レビュー、進行を管理するWebアプリ。

- **リポジトリ**: https://github.com/cgwire/kitsu
- **分類**: web_app / 非AI制作 / 制作基盤として比較
- **入力**: アセット、ショット、タスク、レビュー素材
- **出力**: 制作管理画面と進行情報
- **環境**: Webフロントエンド。運用には対応バックエンド環境が必要。
- **依存**: CGWireの制作管理構成、ユーザー認証・保存先
- **制約・未確認**: このフロントエンドだけで全サービスが完結するとは扱わない。画像生成器ではない。
- **編集者評価**: 素材数・改訂数が増えた制作の受け渡しとレビュー整理に向く。
- **メトリクス**: ★726、fork 183、作成 2017-03-26、最終push 2026-09-30T15:18:12Z、archived=False
- **確認**: 2026-09-09 / コミット `6cf2e8e77b1172dff970286ea6098502579239f2`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/cgwire/kitsu/tree/6cf2e8e77b1172dff970286ea6098502579239f2)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/cgwire/kitsu/blob/6cf2e8e77b1172dff970286ea6098502579239f2/README.md) / [GitHub API](https://api.github.com/repos/cgwire/kitsu) / [固定ツリー](https://github.com/cgwire/kitsu/tree/6cf2e8e77b1172dff970286ea6098502579239f2)

### 制作に使う際の検討

素材数・改訂数が増えた制作の受け渡しとレビュー整理に向く。

**次に確かめること（実施前）**: キャラ・ショット・版を一つずつ登録し、レビューと権限、バックアップを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/main.js](https://github.com/cgwire/kitsu/blob/6cf2e8e77b1172dff970286ea6098502579239f2/src/main.js) / [src/App.vue](https://github.com/cgwire/kitsu/blob/6cf2e8e77b1172dff970286ea6098502579239f2/src/App.vue)

**最新GitHub Release**: [v1.0.68](https://github.com/cgwire/kitsu/releases/tag/v1.0.68) / 2026-09-29T11:51:32Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T13:11:45Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="storyboarder"></a>

## Storyboarder

絵コンテを描き、ショットの順序と時間を試すアニマティクス制作ツール。

- **リポジトリ**: https://github.com/wonderunit/storyboarder
- **分類**: desktop_tool / 非AI制作 / 既存研究・制作の参考
- **入力**: ラフ画、ショット、台詞・時間
- **出力**: 絵コンテ・アニマティクス
- **環境**: デスクトップアプリ、Electron系開発環境。
- **依存**: 作画素材、外部編集ツールとの受け渡し
- **制約・未確認**: 最終push2024年。最新OS・配布版の導入状態は再確認が必要。
- **編集者評価**: 生成回数を増やす前にカット割りを固定する道具として有用。
- **メトリクス**: ★3,862、fork 395、作成 2016-12-22、最終push 2024-03-17T12:03:55Z、archived=False
- **確認**: 2026-09-09 / コミット `8b81a25c71d5f7ca46e8d5b8e3d4f7b3968f95c2`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/wonderunit/storyboarder/tree/8b81a25c71d5f7ca46e8d5b8e3d4f7b3968f95c2)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/wonderunit/storyboarder/blob/8b81a25c71d5f7ca46e8d5b8e3d4f7b3968f95c2/README.md) / [GitHub API](https://api.github.com/repos/wonderunit/storyboarder) / [固定ツリー](https://github.com/wonderunit/storyboarder/tree/8b81a25c71d5f7ca46e8d5b8e3d4f7b3968f95c2)

### 制作に使う際の検討

生成回数を増やす前にカット割りを固定する道具として有用。

**次に確かめること（実施前）**: 10ショットの台詞タイミングと編集ソフトへの書き出しを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/js/main.js](https://github.com/wonderunit/storyboarder/blob/8b81a25c71d5f7ca46e8d5b8e3d4f7b3968f95c2/src/js/main.js) / [src/js/express-app/app.js](https://github.com/wonderunit/storyboarder/blob/8b81a25c71d5f7ca46e8d5b8e3d4f7b3968f95c2/src/js/express-app/app.js)

**最新GitHub Release**: [v2.1.0](https://github.com/wonderunit/storyboarder/releases/tag/v2.1.0) / 2020-09-03T19:48:35Z / prerelease=False

デフォルトブランチの確認コミット日時: 2022-06-30T17:42:04Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="styleid"></a>

## StyleID

画風変化に強い顔の同一性特徴を計算し、比較・検索・評価に使う。

- **リポジトリ**: https://github.com/kwanyun/StyleID
- **分類**: model / AIモデル・学習 / 小規模・初期候補
- **入力**: 一人の顔を含む画像
- **出力**: 正規化された特徴ベクトル・類似度
- **環境**: PyTorch、Transformers4.52、CLIPModel。
- **依存**: kwanY/styleidチェックポイント
- **制約・未確認**: 複数顔には不適、顔の中央クロップを推奨。非商用研究用と記載。画像生成器ではない。
- **編集者評価**: 絵柄を跨ぐキャラの一貫性評価を補助する候補。自動合否の唯一の指標にはしない。
- **メトリクス**: ★34、fork 3、作成 2026-04-23、最終push 2026-08-16T08:18:40Z、archived=False
- **確認**: 2026-09-09 / コミット `bbb917dcc350d24456be6cb7dbb9fe5f4aa05c00`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/kwanyun/StyleID/tree/bbb917dcc350d24456be6cb7dbb9fe5f4aa05c00)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/kwanyun/StyleID/blob/bbb917dcc350d24456be6cb7dbb9fe5f4aa05c00/README.md) / [GitHub API](https://api.github.com/repos/kwanyun/StyleID) / [固定ツリー](https://github.com/kwanyun/StyleID/tree/bbb917dcc350d24456be6cb7dbb9fe5f4aa05c00)

### 制作に使う際の検討

絵柄を跨ぐキャラの一貫性評価を補助する候補。自動合否の唯一の指標にはしない。

**次に確かめること（実施前）**: 同一キャラの別表情と似た別キャラを分けた評価集合で誤判定を確認する。

**利用条件の確認メモ**: READMEは非商用研究用途を明記。 商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [example.py](https://github.com/kwanyun/StyleID/blob/bbb917dcc350d24456be6cb7dbb9fe5f4aa05c00/example.py) / [full_train_clip-checkpoint.py](https://github.com/kwanyun/StyleID/blob/bbb917dcc350d24456be6cb7dbb9fe5f4aa05c00/full_train_clip-checkpoint.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-16T08:18:40Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

本文を確認した箇所:

- [example.py](https://github.com/kwanyun/StyleID/blob/bbb917dcc350d24456be6cb7dbb9fe5f4aa05c00/example.py): CLIPModelのget_image_featuresと正規化を確認。画像を生成するコードではない。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [kwanY/styleid](https://huggingface.co/kwanY/styleid) — file_listing_checked、確認日 2026-09-09、revision `1967c354f339a636e5b3e16ecab3d0075aa27ab1`。代表ファイル: `model.safetensors`, `pytorch_model.bin`。gated=False。

<a id="nomi"></a>

## Nomi

ローカル優先のAI動画制作スタジオ。エージェントがショット分割・キーフレーム生成・動画化・タイムライン配置を支援する。

- **リポジトリ**: https://github.com/aqm857886159/Nomi
- **分類**: desktop_tool / AIモデル・学習 / 活発・候補
- **入力**: 作りたい内容のテキスト、参照カード、接続した動画・画像生成モデル
- **出力**: 生成されたキーフレームと動画クリップ、タイムライン、MP4書き出し、プロジェクトフォルダ
- **環境**: macOS(arm64/x64)またはWindows x64。外部モデルAPIキーまたはローカルComfyUI。
- **依存**: 各種モデルプロバイダ（APIMart/Kie.ai等）、OpenAI互換中継、ローカルComfyUI。
- **制約・未確認**: LinuxやWindows arm64のインストーラは未配布。macOSビルドは署名・公証なし。モデル利用は提供元への課金。
- **編集者評価**: 絵コンテ画面でショットごとにモデルと尺を管理し、キャラクター参照カードで一貫性を保ち、MCPでClaude Code等から操作できる点が具体的。
- **メトリクス**: ★537、fork 121、作成 2026-05-04、最終push 2026-10-01T20:02:50Z、archived=False
- **確認**: 2026-09-30 / コミット `2094010c4b840314b0fffaea030d8b97e32ff275`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/aqm857886159/Nomi/tree/2094010c4b840314b0fffaea030d8b97e32ff275)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/aqm857886159/Nomi/blob/2094010c4b840314b0fffaea030d8b97e32ff275/README.md) / [GitHub API](https://api.github.com/repos/aqm857886159/Nomi) / [固定ツリー](https://github.com/aqm857886159/Nomi/tree/2094010c4b840314b0fffaea030d8b97e32ff275)

### 制作に使う際の検討

絵コンテから動画素材の初稿作成までの流れをローカルで管理。

**次に確かめること（実施前）**: 短い題材でショット分割からMP4書き出しまで通し、参照一貫性を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [docs/design/mockups/capability-system/app.js](https://github.com/aqm857886159/Nomi/blob/2094010c4b840314b0fffaea030d8b97e32ff275/docs/design/mockups/capability-system/app.js) / [electron/main.ts](https://github.com/aqm857886159/Nomi/blob/2094010c4b840314b0fffaea030d8b97e32ff275/electron/main.ts) / [electron/shared/modelArchetypes/index.ts](https://github.com/aqm857886159/Nomi/blob/2094010c4b840314b0fffaea030d8b97e32ff275/electron/shared/modelArchetypes/index.ts)

**最新GitHub Release**: [v0.22.5](https://github.com/aqm857886159/Nomi/releases/tag/v0.22.5) / 2026-09-30T08:42:21Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-30T16:15:30Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
