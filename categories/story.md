# シナリオ・キャラクター・絵コンテ

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [BlueFish](https://github.com/bluefish2026/BlueFish) · [詳細](#bluefish) | 複数のAIプロバイダを接続し、脚本から絵コンテ・動画制作まで管理する。 | AI連携 / 小規模・初期評価候補 | 8 / 2026-04-22 |
| [SillyTavern](https://github.com/SillyTavern/SillyTavern) · [詳細](#sillytavern) | キャラ設定とLorebookを使い、LLMとの対話や世界観の試作を行うフロントエンド。 | AI連携 / 更新のある導入・評価候補 | 33,188 / 2026-09-07 |

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
- **メトリクス**: ★8、fork 9、作成 2026-04-17、最終push 2026-04-22T04:11:49Z、archived=False
- **確認**: 2026-09-09 / コミット `8b409c1332e46bc1211d2ffc6d45fe1f01492eca`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/bluefish2026/BlueFish/blob/8b409c1332e46bc1211d2ffc6d45fe1f01492eca/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/bluefish2026/BlueFish/blob/8b409c1332e46bc1211d2ffc6d45fe1f01492eca/README.md) / [GitHub API](https://api.github.com/repos/bluefish2026/BlueFish) / [固定ツリー](https://github.com/bluefish2026/BlueFish/tree/8b409c1332e46bc1211d2ffc6d45fe1f01492eca)

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
- **メトリクス**: ★33,188、fork 6,250、作成 2023-02-09、最終push 2026-09-07T21:09:17Z、archived=False
- **確認**: 2026-09-09 / コミット `8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/SillyTavern/SillyTavern/blob/8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8/LICENSE)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/SillyTavern/SillyTavern/blob/8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8/.github/readme.md) / [GitHub API](https://api.github.com/repos/SillyTavern/SillyTavern) / [固定ツリー](https://github.com/SillyTavern/SillyTavern/tree/8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8)
