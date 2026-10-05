# シナリオ・キャラクター・絵コンテ

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-05。**175件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [BlueFish](https://github.com/bluefish2026/BlueFish) · [詳細](#bluefish) | 複数のAIプロバイダを接続し、脚本から絵コンテ・動画制作まで管理する。 | AI連携 / 小規模・初期評価候補 | 8 / 2026-04-22 |
| [ink](https://github.com/inkle/ink) · [詳細](#ink) | 分岐する物語を書くスクリプト言語、コンパイラ、実行ランタイム。 | 非AI制作 / 制作基盤として比較 | 4,959 / 2026-05-05 |
| [SillyTavern](https://github.com/SillyTavern/SillyTavern) · [詳細](#sillytavern) | キャラ設定とLorebookを使い、LLMとの対話や世界観の試作を行うフロントエンド。 | AI連携 / 更新のある導入・評価候補 | 34,118 / 2026-10-02 |
| [Yarn Spinner](https://github.com/YarnSpinnerTool/YarnSpinner) · [詳細](#yarnspinner) | ゲームの会話記述をコンパイル・実行する台詞制作基盤。 | 非AI制作 / 制作基盤として比較 | 2,854 / 2026-10-01 |

<a id="bluefish"></a>

## BlueFish

複数のAIプロバイダを接続し、脚本から絵コンテ・動画制作まで管理する。

- **リポジトリ**: https://github.com/bluefish2026/BlueFish
- **分類**: web_app / AI連携 / 小規模・初期評価候補
- **入力**: 脚本、参照キャラ・背景
- **出力**: 絵コンテ、生成動画、編集用素材
- **環境**: React/FastAPI、生成用API。mockモードあり。
- **依存**: 外部LLM、画像・動画・TTS API
- **制約・未確認**: 小規模な初期候補。mock動作と実際の生成完了を区別する。ローカルUIはローカル推論を意味しない。
- **編集者評価**: シナリオ・キャラ素材・生成履歴を同じ場所で扱う構成が参考になる。
- **メトリクス**: ★8、fork 10、作成 2026-04-17、最終push 2026-04-22T04:11:49Z、archived=False
- **確認**: 2026-09-09 / コミット `8b409c1332e46bc1211d2ffc6d45fe1f01492eca`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/bluefish2026/BlueFish/tree/8b409c1332e46bc1211d2ffc6d45fe1f01492eca)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/bluefish2026/BlueFish/blob/8b409c1332e46bc1211d2ffc6d45fe1f01492eca/README.md) / [GitHub API](https://api.github.com/repos/bluefish2026/BlueFish) / [固定ツリー](https://github.com/bluefish2026/BlueFish/tree/8b409c1332e46bc1211d2ffc6d45fe1f01492eca)

### 制作に使う際の検討

脚本から複数工程を管理する統合UIの初期候補。APIの実処理とデモ表示の差を評価する。

**次に確かめること（実施前）**: mockを切った1ショットで課金対象API、ジョブ完了、失敗復旧、素材保存先を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [bluefish-server/app/main.py](https://github.com/bluefish2026/BlueFish/blob/8b409c1332e46bc1211d2ffc6d45fe1f01492eca/bluefish-server/app/main.py) / [bluefish-client/eslint.config.js](https://github.com/bluefish2026/BlueFish/blob/8b409c1332e46bc1211d2ffc6d45fe1f01492eca/bluefish-client/eslint.config.js)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-04-22T04:11:22Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="ink"></a>

## ink

分岐する物語を書くスクリプト言語、コンパイラ、実行ランタイム。

- **リポジトリ**: https://github.com/inkle/ink
- **分類**: library / 非AI制作 / 制作基盤として比較
- **入力**: ink形式の会話・分岐シナリオ
- **出力**: コンパイル済み物語と進行状態
- **環境**: C#/.NET。対象環境の統合ライブラリ。
- **依存**: ゲームエンジンまたはWebランタイム
- **制約・未確認**: LLMではない。画面演出・音声・立ち絵表示はホスト側で実装する。
- **編集者評価**: 生成したシナリオを分岐・変数・セーブ可能な構造へ落とす工程に適する。
- **メトリクス**: ★4,959、fork 542、作成 2016-01-23、最終push 2026-05-05T11:24:42Z、archived=False
- **確認**: 2026-09-09 / コミット `35c63e52f1d36060930dc7ed3cfba38ea224b528`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/inkle/ink/tree/35c63e52f1d36060930dc7ed3cfba38ea224b528)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/inkle/ink/blob/35c63e52f1d36060930dc7ed3cfba38ea224b528/README.md) / [GitHub API](https://api.github.com/repos/inkle/ink) / [固定ツリー](https://github.com/inkle/ink/tree/35c63e52f1d36060930dc7ed3cfba38ea224b528)

### 制作に使う際の検討

生成したシナリオを分岐・変数・セーブ可能な構造へ落とす工程に適する。

**次に確かめること（実施前）**: 選択肢の到達性、ループ、変数保存、翻訳後の分岐ずれを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [inklecate/CommandLineTool.cs](https://github.com/inkle/ink/blob/35c63e52f1d36060930dc7ed3cfba38ea224b528/inklecate/CommandLineTool.cs) / [ink-engine-runtime/Story.cs](https://github.com/inkle/ink/blob/35c63e52f1d36060930dc7ed3cfba38ea224b528/ink-engine-runtime/Story.cs)

**最新GitHub Release**: [v1.2.1](https://github.com/inkle/ink/releases/tag/v1.2.1) / 2026-05-05T11:24:42Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-05-05T11:19:29Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="sillytavern"></a>

## SillyTavern

キャラ設定とLorebookを使い、LLMとの対話や世界観の試作を行うフロントエンド。

- **リポジトリ**: https://github.com/SillyTavern/SillyTavern
- **分類**: web_app / AI連携 / 更新のある導入・評価候補
- **入力**: キャラクター設定、世界設定、会話
- **出力**: キャラ会話、設定・ログ、連携した画像や音声
- **環境**: Node.js環境と外部またはローカルのLLM。
- **依存**: LLM、任意の画像生成・TTSバックエンド
- **制約・未確認**: 完成シナリオの整合性を自動保証するものではない。独自LLM重みは提供しない。
- **編集者評価**: キャラクター設計やシナリオの対話試作に使う候補。
- **メトリクス**: ★34,118、fork 6,415、作成 2023-02-09、最終push 2026-10-02T22:05:54Z、archived=False
- **確認**: 2026-09-09 / コミット `8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/SillyTavern/SillyTavern/tree/8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/SillyTavern/SillyTavern/blob/8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8/.github/readme.md) / [GitHub API](https://api.github.com/repos/SillyTavern/SillyTavern) / [固定ツリー](https://github.com/SillyTavern/SillyTavern/tree/8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8)

### 制作に使う際の検討

キャラ設定・世界設定の試演に使い、確定シナリオは別形式へ書き出して管理する。

**次に確かめること（実施前）**: 長い会話で設定の保持、記憶の参照、ログの再利用、外部TTS接続の条件を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [server.js](https://github.com/SillyTavern/SillyTavern/blob/8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8/server.js)

**最新GitHub Release**: [1.19.0](https://github.com/SillyTavern/SillyTavern/releases/tag/1.19.0) / 2026-09-14T18:05:11Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-07T17:36:20Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="yarnspinner"></a>

## Yarn Spinner

ゲームの会話記述をコンパイル・実行する台詞制作基盤。

- **リポジトリ**: https://github.com/YarnSpinnerTool/YarnSpinner
- **分類**: library / 非AI制作 / 制作基盤として比較
- **入力**: Yarn会話スクリプト、変数、コマンド
- **出力**: 分岐会話の実行と台詞データ
- **環境**: C#/.NET、エンジン別統合。
- **依存**: Unity等のホスト、音声・ローカライズ資産
- **制約・未確認**: コアとUnity向け商品・統合の公開条件を分ける。AI脚本モデルではない。
- **編集者評価**: 声付きNPC会話をエンジンの演出と結び付ける候補。
- **メトリクス**: ★2,854、fork 235、作成 2015-10-03、最終push 2026-10-01T00:03:23Z、archived=False
- **確認**: 2026-09-09 / コミット `c39241c573167ea0157e48d8380c36920c5e50d8`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/YarnSpinnerTool/YarnSpinner/tree/c39241c573167ea0157e48d8380c36920c5e50d8)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/YarnSpinnerTool/YarnSpinner/blob/c39241c573167ea0157e48d8380c36920c5e50d8/README.md) / [GitHub API](https://api.github.com/repos/YarnSpinnerTool/YarnSpinner) / [固定ツリー](https://github.com/YarnSpinnerTool/YarnSpinner/tree/c39241c573167ea0157e48d8380c36920c5e50d8)

### 制作に使う際の検討

声付きNPC会話をエンジンの演出と結び付ける候補。

**次に確かめること（実施前）**: 台詞ID、翻訳表、音声ファイル、カスタムコマンドの対応を小シーンで確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [YarnSpinner/Program.cs](https://github.com/YarnSpinnerTool/YarnSpinner/blob/c39241c573167ea0157e48d8380c36920c5e50d8/YarnSpinner/Program.cs) / [antlr.sh](https://github.com/YarnSpinnerTool/YarnSpinner/blob/c39241c573167ea0157e48d8380c36920c5e50d8/antlr.sh)

**最新GitHub Release**: [v3.2.1](https://github.com/YarnSpinnerTool/YarnSpinner/releases/tag/v3.2.1) / 2026-05-05T02:37:44Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-07T03:49:07Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。
