# VTuber・AIキャラクター・VRM

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AIRI](https://github.com/moeru-ai/airi) · [詳細](#airi) | 会話するバーチャルキャラクターを構築する環境。 | AI連携 / 更新のある導入・評価候補 | 48,985 / 2026-09-09 |
| [inochi-creator](https://github.com/Inochi2D/inochi-creator) · [詳細](#inochi-creator) | レイヤー画像を変形させ、ゲームやVTuberで動かす2Dモデルを作るエディタ。 | 非AI制作 / 比較・既存工程の参考 | 1,217 / 2025-06-16 |
| [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) · [詳細](#open-llm-vtuber) | 音声会話・視覚認識・Live2D表示を組み合わせるAIキャラクター環境。 | AI連携 / 連携の評価候補 | 13,686 / 2026-05-15 |
| [UniVRM](https://github.com/vrm-c/UniVRM) · [詳細](#univrm) | Unity用のVRM形式実装。3Dアバターの読み込み・書き出しを扱う。 | 非AI制作 / 定番の制作基盤 | 3,378 / 2026-08-20 |
| [VTubeStudio](https://github.com/DenchiSoft/VTubeStudio) · [詳細](#vtubestudio) | VTube Studioを外部から制御する公式API文書・開発資料。 | AI連携 / 連携用文書資料 | 1,287 / 2026-09-02 |

<a id="airi"></a>

## AIRI

会話するバーチャルキャラクターを構築する環境。

- **リポジトリ**: https://github.com/moeru-ai/airi
- **分類**: web_app / AI連携 / 更新のある導入・評価候補
- **入力**: 音声、キャラ設定、ゲーム等の入力
- **出力**: 会話音声、2D/3Dキャラ表示、対応ゲーム操作
- **環境**: ブラウザまたは対応デスクトップ環境、推論バックエンド。
- **依存**: LLM、TTS、ASR、キャラモデル
- **制約・未確認**: 対応機能はプラットフォームとプロバイダに依存。全ゲームで自律動作するという意味ではない。
- **編集者評価**: キャラ表示・会話・ゲーム操作の接続を扱う活動的な候補。
- **メトリクス**: ★48,985、fork 4,849、作成 2024-12-01、最終push 2026-09-09T16:31:39Z、archived=False
- **確認**: 2026-09-09 / コミット `dfc6951a55bf4fdd66a68a0c881ae880ddd95f77`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/moeru-ai/airi/blob/dfc6951a55bf4fdd66a68a0c881ae880ddd95f77/LICENSE)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/moeru-ai/airi/blob/dfc6951a55bf4fdd66a68a0c881ae880ddd95f77/README.md) / [GitHub API](https://api.github.com/repos/moeru-ai/airi) / [固定ツリー](https://github.com/moeru-ai/airi/tree/dfc6951a55bf4fdd66a68a0c881ae880ddd95f77)

<a id="inochi-creator"></a>

## inochi-creator

レイヤー画像を変形させ、ゲームやVTuberで動かす2Dモデルを作るエディタ。

- **リポジトリ**: https://github.com/Inochi2D/inochi-creator
- **分類**: desktop_tool / 非AI制作 / 比較・既存工程の参考
- **入力**: レイヤー付き2Dキャラ素材
- **出力**: Inochi2Dのリグ付きモデル
- **環境**: Inochi2D対応環境。配信用にはInochi Session等を併用。
- **依存**: Inochi2D、キャラ素材
- **制約・未確認**: 最終pushは2025年6月。Live2D Cubism形式と同じものではない。
- **編集者評価**: AIなしでも使える2Dリギングの比較基盤。
- **メトリクス**: ★1,217、fork 85、作成 2020-11-19、最終push 2025-06-16T20:39:43Z、archived=False
- **確認**: 2026-09-09 / コミット `dba60811cff224f8cc9ce367b1d9291bfa5f7640`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Inochi2D/inochi-creator/blob/dba60811cff224f8cc9ce367b1d9291bfa5f7640/LICENSE)。GitHub自動判定=BSD-2-Clause。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Inochi2D/inochi-creator/blob/dba60811cff224f8cc9ce367b1d9291bfa5f7640/README.md) / [GitHub API](https://api.github.com/repos/Inochi2D/inochi-creator) / [固定ツリー](https://github.com/Inochi2D/inochi-creator/tree/dba60811cff224f8cc9ce367b1d9291bfa5f7640)

<a id="open-llm-vtuber"></a>

## Open-LLM-VTuber

音声会話・視覚認識・Live2D表示を組み合わせるAIキャラクター環境。

- **リポジトリ**: https://github.com/Open-LLM-VTuber/Open-LLM-VTuber
- **分類**: web_app / AI連携 / 連携の評価候補
- **入力**: マイク入力、視覚情報、キャラ設定
- **出力**: 音声応答とLive2Dアバター表示
- **環境**: Windows・macOS・Linux。LLM・TTS・ASR環境。
- **依存**: LLM、TTS、ASR、Live2D素材
- **制約・未確認**: ローカル完結はバックエンドの選択に依存。Live2Dモデル制作機能とは別。
- **編集者評価**: 会話するVTuberやデスクトップキャラの実装候補。
- **メトリクス**: ★13,686、fork 1,630、作成 2023-11-24、最終push 2026-05-15T07:18:04Z、archived=False
- **確認**: 2026-09-09 / コミット `992309c0aa19845960228f880013d4685fde93b5`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/LICENSE)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/README.md) / [GitHub API](https://api.github.com/repos/Open-LLM-VTuber/Open-LLM-VTuber) / [固定ツリー](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/tree/992309c0aa19845960228f880013d4685fde93b5)

<a id="univrm"></a>

## UniVRM

Unity用のVRM形式実装。3Dアバターの読み込み・書き出しを扱う。

- **リポジトリ**: https://github.com/vrm-c/UniVRM
- **分類**: library / 非AI制作 / 定番の制作基盤
- **入力**: VRM・glTFアバター
- **出力**: Unityで読み書きできるアバター
- **環境**: Unityと対応するUniVRM版。
- **依存**: Unity、VRM素材
- **制約・未確認**: VRM 0.x/1.0等の互換性は個別確認。モデル生成・自動リギング機能ではない。
- **編集者評価**: 生成・制作した3DキャラをVTuberやゲームへ接続する基盤。
- **メトリクス**: ★3,378、fork 490、作成 2018-04-16、最終push 2026-08-20T07:40:06Z、archived=False
- **確認**: 2026-09-09 / コミット `928b30e96439c1c11a49b172efb72eb96d2cad8b`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/vrm-c/UniVRM/blob/928b30e96439c1c11a49b172efb72eb96d2cad8b/LICENSE.txt)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/vrm-c/UniVRM/blob/928b30e96439c1c11a49b172efb72eb96d2cad8b/README.md) / [GitHub API](https://api.github.com/repos/vrm-c/UniVRM) / [固定ツリー](https://github.com/vrm-c/UniVRM/tree/928b30e96439c1c11a49b172efb72eb96d2cad8b)

<a id="vtubestudio"></a>

## VTubeStudio

VTube Studioを外部から制御する公式API文書・開発資料。

- **リポジトリ**: https://github.com/DenchiSoft/VTubeStudio
- **分類**: api_reference / AI連携 / 連携用文書資料
- **入力**: 外部プログラムのAPI要求
- **出力**: VTube Studioのパラメータ制御・状態取得
- **環境**: VTube Studioアプリ、API対応クライアント。
- **依存**: VTube Studio、Live2Dモデル
- **制約・未確認**: アプリ本体のソース公開ではない。文書リポジトリとして掲載。
- **編集者評価**: AI会話や演出制御を既存のLive2D配信へ接続する参考。
- **メトリクス**: ★1,287、fork 141、作成 2019-11-11、最終push 2026-09-02T08:39:56Z、archived=False
- **確認**: 2026-09-09 / コミット `0f46ef44b487fa17c8120db572ebd925924b93a3`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/DenchiSoft/VTubeStudio/blob/0f46ef44b487fa17c8120db572ebd925924b93a3/LICENSE)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/DenchiSoft/VTubeStudio/blob/0f46ef44b487fa17c8120db572ebd925924b93a3/README.md) / [GitHub API](https://api.github.com/repos/DenchiSoft/VTubeStudio) / [固定ツリー](https://github.com/DenchiSoft/VTubeStudio/tree/0f46ef44b487fa17c8120db572ebd925924b93a3)
