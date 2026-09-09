# VTuber・AIキャラクター・VRM

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**115件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AIRI](https://github.com/moeru-ai/airi) · [詳細](#airi) | 会話するバーチャルキャラクターを構築する環境。 | AI連携 / 更新のある導入・評価候補 | 48,986 / 2026-09-09 |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) · [詳細](#babylon-mmd) | Babylon.jsでMMDモデル・モーションを読み込み、物理・IK・モーフを再生する。 | 非AI制作 / 制作基盤として比較 | 253 / 2026-09-09 |
| [inochi-creator](https://github.com/Inochi2D/inochi-creator) · [詳細](#inochi-creator) | レイヤー画像を変形させ、ゲームやVTuberで動かす2Dモデルを作るエディタ。 | 非AI制作 / 比較・既存工程の参考 | 1,217 / 2025-06-16 |
| [OBS Studio](https://github.com/obsproject/obs-studio) · [詳細](#obs-studio) | 画面・カメラ・音声を合成して録画・配信する。 | 非AI制作 / 制作基盤として比較 | 76,008 / 2026-09-09 |
| [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) · [詳細](#open-llm-vtuber) | 音声会話・視覚認識・Live2D表示を組み合わせるAIキャラクター環境。 | AI連携 / 連携の評価候補 | 13,686 / 2026-05-15 |
| [OpenSeeFace](https://github.com/emilianavt/OpenSeeFace) · [詳細](#openseeface) | Webカメラから顔のランドマークを推定し、アバター駆動へ渡す。 | AIモデル・学習 / 連携・制作ツール候補 | 2,046 / 2025-12-28 |
| [PersonaLive](https://github.com/GVCLab/PersonaLive) · [詳細](#personalive) | 参照人物の画像を動作入力に従ってストリーミングでアニメーションする。 | AIモデル・学習 / モデル・研究候補 | 3,690 / 2026-08-28 |
| [three-vrm](https://github.com/pixiv/three-vrm) · [詳細](#three-vrm) | three.jsでVRMアバターを読み込み表示するライブラリ。 | 非AI制作 / 制作基盤として比較 | 2,158 / 2026-09-09 |
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
- **メトリクス**: ★48,986、fork 4,849、作成 2024-12-01、最終push 2026-09-09T16:31:39Z、archived=False
- **確認**: 2026-09-09 / コミット `dfc6951a55bf4fdd66a68a0c881ae880ddd95f77`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/moeru-ai/airi/tree/dfc6951a55bf4fdd66a68a0c881ae880ddd95f77)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/moeru-ai/airi/blob/dfc6951a55bf4fdd66a68a0c881ae880ddd95f77/README.md) / [GitHub API](https://api.github.com/repos/moeru-ai/airi) / [固定ツリー](https://github.com/moeru-ai/airi/tree/dfc6951a55bf4fdd66a68a0c881ae880ddd95f77)

### 制作に使う際の検討

会話・表示・ゲーム接続を組み合わせるAIキャラ統合。READMEの対応先だけで目的の構成が動くとは断定しない。

**次に確かめること（実施前）**: 使うOSと2D/3D表示を固定し、STT→LLM→TTS、割込み、ゲーム入力の遅延を測る。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [apps/stage-web/src/main.ts](https://github.com/moeru-ai/airi/blob/dfc6951a55bf4fdd66a68a0c881ae880ddd95f77/apps/stage-web/src/main.ts)

**最新GitHub Release**: [v0.12.0-beta.5](https://github.com/moeru-ai/airi/releases/tag/v0.12.0-beta.5) / 2026-08-29T18:40:52Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T16:31:37Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="babylon-mmd"></a>

## babylon-mmd

Babylon.jsでMMDモデル・モーションを読み込み、物理・IK・モーフを再生する。

- **リポジトリ**: https://github.com/noname0310/babylon-mmd
- **分類**: library / 非AI制作 / 制作基盤として比較
- **入力**: PMX/PMD、VMD/VPD
- **出力**: Web上のMMDアニメーション
- **環境**: TypeScript、Babylon.js、ブラウザ。
- **依存**: MMDモデル・モーション、物理ランタイム
- **制約・未確認**: 読み込み成功と元MMDでの完全な見た目・挙動一致は別。素材条件は個別。
- **編集者評価**: MMD資産をWeb作品やキャラ表示に展開する具体的な接続先。
- **メトリクス**: ★253、fork 18、作成 2023-03-24、最終push 2026-09-09T07:00:36Z、archived=False
- **確認**: 2026-09-09 / コミット `ccb750db2998ed1067017eaf67f3fc987cfba6f8`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/noname0310/babylon-mmd/tree/ccb750db2998ed1067017eaf67f3fc987cfba6f8)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/noname0310/babylon-mmd/blob/ccb750db2998ed1067017eaf67f3fc987cfba6f8/README.md) / [GitHub API](https://api.github.com/repos/noname0310/babylon-mmd) / [固定ツリー](https://github.com/noname0310/babylon-mmd/tree/ccb750db2998ed1067017eaf67f3fc987cfba6f8)

### 制作に使う際の検討

MMD資産をWeb作品やキャラ表示に展開する具体的な接続先。

**次に確かめること（実施前）**: モーフ、足IK、剛体、カメラ曲線、音との同期を元作品と比較する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/Runtime/mmdRuntime.ts](https://github.com/noname0310/babylon-mmd/blob/ccb750db2998ed1067017eaf67f3fc987cfba6f8/src/Runtime/mmdRuntime.ts)

**最新GitHub Release**: [v1.3.0](https://github.com/noname0310/babylon-mmd/releases/tag/v1.3.0) / 2026-07-23T12:40:23Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T07:00:31Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **利用条件**: [配布元の条件](https://github.com/Inochi2D/inochi-creator/tree/dba60811cff224f8cc9ce367b1d9291bfa5f7640)。GitHub自動判定=BSD-2-Clause。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Inochi2D/inochi-creator/blob/dba60811cff224f8cc9ce367b1d9291bfa5f7640/README.md) / [GitHub API](https://api.github.com/repos/Inochi2D/inochi-creator) / [固定ツリー](https://github.com/Inochi2D/inochi-creator/tree/dba60811cff224f8cc9ce367b1d9291bfa5f7640)

### 制作に使う際の検討

独立した2Dリグ形式でモデルを編集する非AI制作候補。Cubismと同一形式とは扱わない。

**次に確かめること（実施前）**: 表情・変形・物理を作り、対応プレーヤーへ渡して保存・再生の一致を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [source/app.d](https://github.com/Inochi2D/inochi-creator/blob/dba60811cff224f8cc9ce367b1d9291bfa5f7640/source/app.d) / [genpot.sh](https://github.com/Inochi2D/inochi-creator/blob/dba60811cff224f8cc9ce367b1d9291bfa5f7640/genpot.sh)

**最新GitHub Release**: [v0.8.6](https://github.com/Inochi2D/inochi-creator/releases/tag/v0.8.6) / 2024-09-18T01:36:44Z / prerelease=False

デフォルトブランチの確認コミット日時: 2025-03-12T11:18:25Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="obs-studio"></a>

## OBS Studio

画面・カメラ・音声を合成して録画・配信する。

- **リポジトリ**: https://github.com/obsproject/obs-studio
- **分類**: desktop_tool / 非AI制作 / 制作基盤として比較
- **入力**: 映像ソース、アバター表示、マイク、音声
- **出力**: 配信・録画映像
- **環境**: Windows/macOS/Linux、利用するエンコーダに応じたGPU/CPU。
- **依存**: 各配信先、アバター表示アプリ、任意プラグイン
- **制約・未確認**: 顔追跡やモデル生成は別アプリ。プラグインの対応版を確認する。
- **編集者評価**: VTuber制作物を実際の配信画面へまとめる基本工程。
- **メトリクス**: ★76,008、fork 10,098、作成 2013-10-01、最終push 2026-09-09T01:05:38Z、archived=False
- **確認**: 2026-09-09 / コミット `012c6c23c73283ee5591ae00d08af14d9eeb8279`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/obsproject/obs-studio/tree/012c6c23c73283ee5591ae00d08af14d9eeb8279)。GitHub自動判定=GPL-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/obsproject/obs-studio/blob/012c6c23c73283ee5591ae00d08af14d9eeb8279/README.rst) / [GitHub API](https://api.github.com/repos/obsproject/obs-studio) / [固定ツリー](https://github.com/obsproject/obs-studio/tree/012c6c23c73283ee5591ae00d08af14d9eeb8279)

### 制作に使う際の検討

VTuber制作物を実際の配信画面へまとめる基本工程。

**次に確かめること（実施前）**: 30分の録画で映像と音声のずれ、透過、フレーム落ち、シーン切替を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [frontend/obs-main.cpp](https://github.com/obsproject/obs-studio/blob/012c6c23c73283ee5591ae00d08af14d9eeb8279/frontend/obs-main.cpp)

**最新GitHub Release**: [32.2.2](https://github.com/obsproject/obs-studio/releases/tag/32.2.2) / 2026-08-14T22:43:31Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-08T21:14:40Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **利用条件**: [配布元の条件](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/tree/992309c0aa19845960228f880013d4685fde93b5)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/README.md) / [GitHub API](https://api.github.com/repos/Open-LLM-VTuber/Open-LLM-VTuber) / [固定ツリー](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/tree/992309c0aa19845960228f880013d4685fde93b5)

### 制作に使う際の検討

音声会話とLive2D表示を組み合わせる導入候補。音声認識・LLM・TTSの構成を明記して評価する。

**次に確かめること（実施前）**: 日本語の認識、応答開始、割込み、口形、視覚入力を実際の会話で確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [run_server.py](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/run_server.py) / [scripts/run_bilibili_live.py](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/scripts/run_bilibili_live.py)

**最新GitHub Release**: [v1.2.1](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/releases/tag/v1.2.1) / 2025-08-26T08:47:08Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-05-15T07:18:03Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="openseeface"></a>

## OpenSeeFace

Webカメラから顔のランドマークを推定し、アバター駆動へ渡す。

- **リポジトリ**: https://github.com/emilianavt/OpenSeeFace
- **分類**: library / AIモデル・学習 / 連携・制作ツール候補
- **入力**: 顔カメラ映像
- **出力**: 顔特徴・トラッキング情報
- **環境**: Python、ONNX Runtime。CPU経路を用意。
- **依存**: 同梱・配布ONNXモデル、別途アバター描画ソフト
- **制約・未確認**: 単体のアバター表示ソフトではない。作者の30〜60fpsは環境依存。
- **編集者評価**: 生成モデルを増やす前に安定した表情入力を作る候補。
- **メトリクス**: ★2,046、fork 208、作成 2020-01-01、最終push 2025-12-28T11:52:30Z、archived=False
- **確認**: 2026-09-09 / コミット `85aa70fc67582d046e771ea73625182a0d8f7475`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/emilianavt/OpenSeeFace/tree/85aa70fc67582d046e771ea73625182a0d8f7475)。GitHub自動判定=BSD-2-Clause。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/emilianavt/OpenSeeFace/blob/85aa70fc67582d046e771ea73625182a0d8f7475/README.md) / [GitHub API](https://api.github.com/repos/emilianavt/OpenSeeFace) / [固定ツリー](https://github.com/emilianavt/OpenSeeFace/tree/85aa70fc67582d046e771ea73625182a0d8f7475)

### 制作に使う際の検討

生成モデルを増やす前に安定した表情入力を作る候補。

**次に確かめること（実施前）**: 眼鏡、横顔、暗所、口を閉じた状態で誤検出と受信側の表情を評価する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [facetracker.py](https://github.com/emilianavt/OpenSeeFace/blob/85aa70fc67582d046e771ea73625182a0d8f7475/facetracker.py)

**最新GitHub Release**: [v1.20.4](https://github.com/emilianavt/OpenSeeFace/releases/tag/v1.20.4) / 2021-09-17T20:20:39Z / prerelease=False

デフォルトブランチの確認コミット日時: 2025-12-28T11:52:30Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: documented_use_by → vtubestudio（公式説明に基づく関係、接続実行は未検証）

<a id="personalive"></a>

## PersonaLive

参照人物の画像を動作入力に従ってストリーミングでアニメーションする。

- **リポジトリ**: https://github.com/GVCLab/PersonaLive
- **分類**: model / AIモデル・学習 / モデル・研究候補
- **入力**: 参照画像、駆動映像・動作
- **出力**: 人物動画
- **環境**: READMEは12GB VRAMを案内。オンライン・オフライン経路。
- **依存**: 独自重み、SD image variations、VAE等
- **制約・未確認**: 出力は動画であり編集可能なLive2D・VRMモデルではない。二次元適性は未評価。
- **編集者評価**: 画像ベースの配信アバターを試す研究候補。
- **メトリクス**: ★3,690、fork 520、作成 2025-11-25、最終push 2026-08-28T04:01:07Z、archived=False
- **確認**: 2026-09-09 / コミット `abdd112e01dcf7d89122c2e5efa29fcff0669740`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/GVCLab/PersonaLive/tree/abdd112e01dcf7d89122c2e5efa29fcff0669740)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/GVCLab/PersonaLive/blob/abdd112e01dcf7d89122c2e5efa29fcff0669740/README.md) / [GitHub API](https://api.github.com/repos/GVCLab/PersonaLive) / [固定ツリー](https://github.com/GVCLab/PersonaLive/tree/abdd112e01dcf7d89122c2e5efa29fcff0669740)

### 制作に使う際の検討

画像ベースの配信アバターを試す研究候補。

**次に確かめること（実施前）**: 顔の保持、表情、輪郭、遅延、背景のちらつきを実際の配信条件で確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [inference_offline.py](https://github.com/GVCLab/PersonaLive/blob/abdd112e01dcf7d89122c2e5efa29fcff0669740/inference_offline.py) / [torch2trt.py](https://github.com/GVCLab/PersonaLive/blob/abdd112e01dcf7d89122c2e5efa29fcff0669740/torch2trt.py) / [inference_online.py](https://github.com/GVCLab/PersonaLive/blob/abdd112e01dcf7d89122c2e5efa29fcff0669740/inference_online.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-28T04:01:07Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [huaichang/PersonaLive](https://huggingface.co/huaichang/PersonaLive) — file_listing_checked、確認日 2026-09-09、revision `b247581c0361b8bee0aa7232eea6e3fdd6e38e60`。代表ファイル: `pretrained_weights/personalive/denoising_unet.pth`, `pretrained_weights/personalive/motion_encoder.pth`, `pretrained_weights/personalive/motion_extractor.pth`, `pretrained_weights/personalive/pose_guider.pth`。gated=False。

<a id="three-vrm"></a>

## three-vrm

three.jsでVRMアバターを読み込み表示するライブラリ。

- **リポジトリ**: https://github.com/pixiv/three-vrm
- **分類**: library / 非AI制作 / 制作基盤として比較
- **入力**: VRMモデル、アニメーション・表情値
- **出力**: ブラウザ内3Dアバター表示
- **環境**: JavaScript/TypeScript、three.js、GLTFLoader。
- **依存**: VRM素材、ブラウザWebGL
- **制約・未確認**: アバター生成や顔追跡は含まない。VRM・three.jsの対応版を確認する。
- **編集者評価**: WebのAIキャラクターUIへ既存VRMを組み込む基盤。
- **メトリクス**: ★2,158、fork 190、作成 2019-06-04、最終push 2026-09-09T00:46:32Z、archived=False
- **確認**: 2026-09-09 / コミット `1b4fc0cc7ef39a49d62bb7a66dcfeca8f65316f7`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/pixiv/three-vrm/tree/1b4fc0cc7ef39a49d62bb7a66dcfeca8f65316f7)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/pixiv/three-vrm/blob/1b4fc0cc7ef39a49d62bb7a66dcfeca8f65316f7/README.md) / [GitHub API](https://api.github.com/repos/pixiv/three-vrm) / [固定ツリー](https://github.com/pixiv/three-vrm/tree/1b4fc0cc7ef39a49d62bb7a66dcfeca8f65316f7)

### 制作に使う際の検討

WebのAIキャラクターUIへ既存VRMを組み込む基盤。

**次に確かめること（実施前）**: 対象VRMの表情、髪の揺れ、透明材質、モバイルのfpsを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [packages/three-vrm-core/examples/humanoidAnimation/main.js](https://github.com/pixiv/three-vrm/blob/1b4fc0cc7ef39a49d62bb7a66dcfeca8f65316f7/packages/three-vrm-core/examples/humanoidAnimation/main.js) / [packages/three-vrm/examples/humanoidAnimation/main.js](https://github.com/pixiv/three-vrm/blob/1b4fc0cc7ef39a49d62bb7a66dcfeca8f65316f7/packages/three-vrm/examples/humanoidAnimation/main.js)

**最新GitHub Release**: [v3.5.5](https://github.com/pixiv/three-vrm/releases/tag/v3.5.5) / 2026-07-09T07:49:21Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T00:46:30Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **利用条件**: [配布元の条件](https://github.com/vrm-c/UniVRM/tree/928b30e96439c1c11a49b172efb72eb96d2cad8b)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/vrm-c/UniVRM/blob/928b30e96439c1c11a49b172efb72eb96d2cad8b/README.md) / [GitHub API](https://api.github.com/repos/vrm-c/UniVRM) / [固定ツリー](https://github.com/vrm-c/UniVRM/tree/928b30e96439c1c11a49b172efb72eb96d2cad8b)

### 制作に使う際の検討

UnityとVRMの入出力基盤。リグや生成モデルと別に形式互換を担当する。

**次に確かめること（実施前）**: VRM0.xと1.0の素材を分け、表情、揺れ物、材質、再エクスポートを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [Packages/VRM10/Runtime/IO/Vrm10.cs](https://github.com/vrm-c/UniVRM/blob/928b30e96439c1c11a49b172efb72eb96d2cad8b/Packages/VRM10/Runtime/IO/Vrm10.cs)

**最新GitHub Release**: [v0.131.2](https://github.com/vrm-c/UniVRM/releases/tag/v0.131.2) / 2026-07-24T15:46:04Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-20T07:40:06Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **利用条件**: [配布元の条件](https://github.com/DenchiSoft/VTubeStudio/tree/0f46ef44b487fa17c8120db572ebd925924b93a3)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/DenchiSoft/VTubeStudio/blob/0f46ef44b487fa17c8120db572ebd925924b93a3/README.md) / [GitHub API](https://api.github.com/repos/DenchiSoft/VTubeStudio) / [固定ツリー](https://github.com/DenchiSoft/VTubeStudio/tree/0f46ef44b487fa17c8120db572ebd925924b93a3)

### 制作に使う際の検討

既存VTube Studioアプリへ外部AIや演出からパラメータを送るAPI資料。アプリのOSS実装とは数えない。

**次に確かめること（実施前）**: 認証、ホットキー、口形・表情値、接続切れ後の復旧を外部クライアントで確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [Files/EffectConfigs.cs](https://github.com/DenchiSoft/VTubeStudio/blob/0f46ef44b487fa17c8120db572ebd925924b93a3/Files/EffectConfigs.cs) / [Files/Effects.cs](https://github.com/DenchiSoft/VTubeStudio/blob/0f46ef44b487fa17c8120db572ebd925924b93a3/Files/Effects.cs)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-02T08:39:55Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。
