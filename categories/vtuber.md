# VTuber・AIキャラクター・VRM

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-05。**175件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AIRI](https://github.com/moeru-ai/airi) · [詳細](#airi) | 会話するバーチャルキャラクターを構築する環境。 | AI連携 / 更新のある導入・評価候補 | 50,066 / 2026-10-05 |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) · [詳細](#babylon-mmd) | Babylon.jsでMMDモデル・モーションを読み込み、物理・IK・モーフを再生する。 | 非AI制作 / 制作基盤として比較 | 256 / 2026-09-09 |
| [inochi-creator](https://github.com/Inochi2D/inochi-creator) · [詳細](#inochi-creator) | レイヤー画像を変形させ、ゲームやVTuberで動かす2Dモデルを作るエディタ。 | 非AI制作 / 比較・既存工程の参考 | 1,236 / 2025-06-16 |
| [OBS Studio](https://github.com/obsproject/obs-studio) · [詳細](#obs-studio) | 画面・カメラ・音声を合成して録画・配信する。 | 非AI制作 / 制作基盤として比較 | 77,006 / 2026-10-05 |
| [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) · [詳細](#open-llm-vtuber) | 音声会話・視覚認識・Live2D表示を組み合わせるAIキャラクター環境。 | AI連携 / 連携の評価候補 | 13,991 / 2026-05-15 |
| [OpenSeeFace](https://github.com/emilianavt/OpenSeeFace) · [詳細](#openseeface) | Webカメラから顔のランドマークを推定し、アバター駆動へ渡す。 | AIモデル・学習 / 連携・制作ツール候補 | 2,082 / 2026-09-18 |
| [PersonaLive](https://github.com/GVCLab/PersonaLive) · [詳細](#personalive) | 参照人物の画像を動作入力に従ってストリーミングでアニメーションする。 | AIモデル・学習 / モデル・研究候補 | 3,926 / 2026-08-28 |
| [three-vrm](https://github.com/pixiv/three-vrm) · [詳細](#three-vrm) | three.jsでVRMアバターを読み込み表示するライブラリ。 | 非AI制作 / 制作基盤として比較 | 2,199 / 2026-10-02 |
| [UniVRM](https://github.com/vrm-c/UniVRM) · [詳細](#univrm) | Unity用のVRM形式実装。3Dアバターの読み込み・書き出しを扱う。 | 非AI制作 / 定番の制作基盤 | 3,391 / 2026-10-02 |
| [VTubeStudio](https://github.com/DenchiSoft/VTubeStudio) · [詳細](#vtubestudio) | VTube Studioを外部から制御する公式API文書・開発資料。 | AI連携 / 連携用文書資料 | 1,309 / 2026-09-28 |
| [prometheus-avatar](https://github.com/myths-labs/prometheus-avatar) · [詳細](#prometheus-avatar) | LLM出力でLive2D/3Dアバターを動かすオープンソースSDK。口パク、感情表現、リアルタイム音声、TTS、VTuberモード、MCPサーバをまとめる。 | AI連携 / 小規模・初期評価候補 | 17 / 2026-09-30 |
| [VMagicMirror](https://github.com/malaybaku/VMagicMirror) · [詳細](#vmagicmirror) | WindowsでVRMモデルを読み込み、追加デバイスなしにキーボードとマウス操作をモーションとしてアバターの上半身に反映するアプリ。可変クロマキーに対応し、配信・ライブコーディング・デスクトップマスコットに使える。 | 非AI制作 / 確立済み | 544 / 2026-10-01 |
| [gaussian-vrm](https://github.com/naruya/gaussian-vrm) · [詳細](#gaussian-vrm) | three.js上でVRM形式のスキニング付きガウシアンアバター(GVRM)を扱う実装。three-vrmとgaussian-splats-3dを基盤に、VRMの操作（移動やアニメーション）をそのまま再利用できる。 | 非AI制作 / 研究実装・活発 | 425 / 2026-09-29 |
| [Cortico](https://github.com/Pal-AI-Lab/Cortico) · [詳細](#cortico) | イベントストリームを中心に設計したエージェント基盤。ペルソナbot・AI配信者・ロールプレイ・コンパニオン向けで、Core/Persona/Memory/World/Botの4層構成と、外部環境を隔離して接続するWorld拡張機構を持つ。 | AIモデル・学習 / 活発・pre-release | 183 / 2026-10-04 |
| [Anima](https://github.com/Yun-0000/Anima) · [詳細](#anima) | ブラウザで動くVRMキャラクタースタジオ。テキストまたはリアルタイム音声でキャラと対話し、表情・リップシンク・身体モーションを付けて演技させる。 | AIモデル・学習 / 小規模・初期評価候補 | 3 / 2026-05-09 |
| [open-vt](https://github.com/erodozer/open-vt) · [詳細](#open-vt) | Godotで作られたオープンソースの2D VTuberソフト。OpenSeeFaceとVTubeStudioのトラッカーに対応し、OBSで取り込みやすい透過ウィンドウや複数ウィンドウのポップアウト操作を持つ。 | 非AI制作 / 実運用候補 | 281 / 2026-09-25 |
| [A.R.I.A](https://github.com/NekoUnix/A.R.I.A) · [詳細](#a-r-i-a) | Live2D・VRM・GLB・PNG/GIFアバターをまとめて扱うクロスプラットフォームのアバタースタジオ。顔トラッキング、物理、ライティング、視覚アクション、複数アバターのOBS出力に対応する。 | 非AI制作 / Alpha・初期評価候補 | 9 / 2026-10-05 |
| [Seidr-Smidja](https://github.com/hrabanazviking/Seidr-Smidja) · [詳細](#seidr-smidja) | AIエージェントがYAML仕様からVRMアバターを設計・構築・検証・レンダリングするヘッドレスなパイプライン。VRoidベーステンプレートにBlenderをヘッドレスで適用し、VRChat/VTube Studio互換を検査して.vrmを出力する。 | AI連携 / Genesis・初期評価候補 | 21 / 2026-10-05 |
| [vrm-studio](https://github.com/vucinatim/vrm-studio) · [詳細](#vrm-studio) | ブラウザで動くVTubingアプリ。Google MediaPipe Holisticで顔・手・全身をトラッキングし、Three.jsでVRMアバターを動かす。グリーンスクリーン、OBS連携、カルマンフィルタによる平滑化を備える。 | AIは任意 / 小規模・実用候補 | 21 / 2025-12-09 |

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
- **メトリクス**: ★50,066、fork 5,000、作成 2024-12-01、最終push 2026-10-05T19:02:50Z、archived=False
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
- **メトリクス**: ★256、fork 19、作成 2023-03-24、最終push 2026-09-09T07:00:36Z、archived=False
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
- **メトリクス**: ★1,236、fork 91、作成 2020-11-19、最終push 2025-06-16T20:39:43Z、archived=False
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
- **メトリクス**: ★77,006、fork 10,457、作成 2013-10-01、最終push 2026-10-05T21:50:19Z、archived=False
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
- **メトリクス**: ★13,991、fork 1,674、作成 2023-11-24、最終push 2026-05-15T07:18:04Z、archived=False
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
- **メトリクス**: ★2,082、fork 209、作成 2020-01-01、最終push 2026-09-18T17:30:40Z、archived=False
- **確認**: 2026-09-09 / コミット `85aa70fc67582d046e771ea73625182a0d8f7475`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/emilianavt/OpenSeeFace/tree/85aa70fc67582d046e771ea73625182a0d8f7475)。GitHub自動判定=BSD-2-Clause。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/emilianavt/OpenSeeFace/blob/85aa70fc67582d046e771ea73625182a0d8f7475/README.md) / [GitHub API](https://api.github.com/repos/emilianavt/OpenSeeFace) / [固定ツリー](https://github.com/emilianavt/OpenSeeFace/tree/85aa70fc67582d046e771ea73625182a0d8f7475)

### 制作に使う際の検討

生成モデルを増やす前に安定した表情入力を作る候補。

**次に確かめること（実施前）**: 眼鏡、横顔、暗所、口を閉じた状態で誤検出と受信側の表情を評価する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [facetracker.py](https://github.com/emilianavt/OpenSeeFace/blob/85aa70fc67582d046e771ea73625182a0d8f7475/facetracker.py)

**最新GitHub Release**: [v1.20.5](https://github.com/emilianavt/OpenSeeFace/releases/tag/v1.20.5) / 2026-09-14T10:29:18Z / prerelease=False

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
- **メトリクス**: ★3,926、fork 587、作成 2025-11-25、最終push 2026-08-28T04:01:07Z、archived=False
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
- **メトリクス**: ★2,199、fork 191、作成 2019-06-04、最終push 2026-10-02T10:33:21Z、archived=False
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
- **メトリクス**: ★3,391、fork 490、作成 2018-04-16、最終push 2026-10-02T08:22:37Z、archived=False
- **確認**: 2026-09-09 / コミット `928b30e96439c1c11a49b172efb72eb96d2cad8b`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/vrm-c/UniVRM/tree/928b30e96439c1c11a49b172efb72eb96d2cad8b)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/vrm-c/UniVRM/blob/928b30e96439c1c11a49b172efb72eb96d2cad8b/README.md) / [GitHub API](https://api.github.com/repos/vrm-c/UniVRM) / [固定ツリー](https://github.com/vrm-c/UniVRM/tree/928b30e96439c1c11a49b172efb72eb96d2cad8b)

### 制作に使う際の検討

UnityとVRMの入出力基盤。リグや生成モデルと別に形式互換を担当する。

**次に確かめること（実施前）**: VRM0.xと1.0の素材を分け、表情、揺れ物、材質、再エクスポートを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [Packages/VRM10/Runtime/IO/Vrm10.cs](https://github.com/vrm-c/UniVRM/blob/928b30e96439c1c11a49b172efb72eb96d2cad8b/Packages/VRM10/Runtime/IO/Vrm10.cs)

**最新GitHub Release**: [v0.131.3](https://github.com/vrm-c/UniVRM/releases/tag/v0.131.3) / 2026-10-02T12:08:42Z / prerelease=False

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
- **メトリクス**: ★1,309、fork 145、作成 2019-11-11、最終push 2026-09-28T23:12:53Z、archived=False
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

<a id="prometheus-avatar"></a>

## prometheus-avatar

LLM出力でLive2D/3Dアバターを動かすオープンソースSDK。口パク、感情表現、リアルタイム音声、TTS、VTuberモード、MCPサーバをまとめる。

- **リポジトリ**: https://github.com/myths-labs/prometheus-avatar
- **分類**: library / AI連携 / 小規模・初期評価候補
- **入力**: LLMのテキスト/音声、Live2Dモデル
- **出力**: 発話・表情付きのアバター表示
- **環境**: npm (@prometheusavatar/core)。Live2D Cubism 2/4。リアルタイム音声はGemini Live API。
- **依存**: PIXI.js、Live2D Cubism SDK、TTS/LLMプロバイダ
- **制約・未確認**: 音声/一部生成はホステッドAPIやマーケットプレイス前提の機能がある。比較的新しくv0.x系。
- **編集者評価**: 数行のコードでアバターに感情付き発話と口パクを与えられ、MCP経由で任意のAIエージェントから駆動できる点が実装向き。
- **メトリクス**: ★17、fork 8、作成 2026-03-07、最終push 2026-09-30T12:35:32Z、archived=False
- **確認**: 2026-09-30 / コミット `7cb8e6d6a8e7d03ae4a08cede07c9d9585edcbb0`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/myths-labs/prometheus-avatar/tree/7cb8e6d6a8e7d03ae4a08cede07c9d9585edcbb0)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/myths-labs/prometheus-avatar/blob/7cb8e6d6a8e7d03ae4a08cede07c9d9585edcbb0/README.md) / [GitHub API](https://api.github.com/repos/myths-labs/prometheus-avatar) / [固定ツリー](https://github.com/myths-labs/prometheus-avatar/tree/7cb8e6d6a8e7d03ae4a08cede07c9d9585edcbb0)

### 制作に使う際の検討

Webアプリや自作エージェントへのアバター組込みに。

**次に確かめること（実施前）**: 自作Live2Dモデルでの口パク同期と感情→表情マッピングの精度を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [docs/api/assets/main.js](https://github.com/myths-labs/prometheus-avatar/blob/7cb8e6d6a8e7d03ae4a08cede07c9d9585edcbb0/docs/api/assets/main.js) / [packages/mcp-server/src/index.ts](https://github.com/myths-labs/prometheus-avatar/blob/7cb8e6d6a8e7d03ae4a08cede07c9d9585edcbb0/packages/mcp-server/src/index.ts) / [packages/openclaw-plugin/src/index.ts](https://github.com/myths-labs/prometheus-avatar/blob/7cb8e6d6a8e7d03ae4a08cede07c9d9585edcbb0/packages/openclaw-plugin/src/index.ts)

**最新GitHub Release**: [v1.0.0](https://github.com/myths-labs/prometheus-avatar/releases/tag/v1.0.0) / 2026-03-09T13:02:01Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-27T07:57:45Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="vmagicmirror"></a>

## VMagicMirror

WindowsでVRMモデルを読み込み、追加デバイスなしにキーボードとマウス操作をモーションとしてアバターの上半身に反映するアプリ。可変クロマキーに対応し、配信・ライブコーディング・デスクトップマスコットに使える。

- **リポジトリ**: https://github.com/malaybaku/VMagicMirror
- **分類**: desktop_tool / 非AI制作 / 確立済み
- **入力**: VRMモデル、キーボード/マウス（および対応デバイス）の入力
- **出力**: アバターの描画（配信・録画向け、クロマキー合成可能）
- **環境**: Windows 10/11。配布版はBOOTHから入手。ソースからのビルドはUnity 6.3系とVisual Studio 2022、FinalIK等の別途アセットが必要。
- **依存**: UniVRM、MediaPipeUnityPlugin、Oculus LipSync Unity Integration、FinalIK（有償）、KlakSpout等
- **制約・未確認**: 同梱されないプリセット資産（サブキャラのVRM等）があるため、ソースからはダミー差し替え等の追加作業が必要。AI/対話機能は含まず、別途連携が前提。
- **編集者評価**: 配信準備を軽くしたい用途に特化した定番のVRMアプリで、比較的高頻度に更新されている。
- **メトリクス**: ★544、fork 53、作成 2019-03-06、最終push 2026-10-01T02:30:59Z、archived=False
- **確認**: 2026-10-01 / コミット `0f65276abb017015b9f6c5bbcfed428645050169`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/malaybaku/VMagicMirror/tree/0f65276abb017015b9f6c5bbcfed428645050169)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/malaybaku/VMagicMirror/blob/0f65276abb017015b9f6c5bbcfed428645050169/README.md) / [GitHub API](https://api.github.com/repos/malaybaku/VMagicMirror) / [固定ツリー](https://github.com/malaybaku/VMagicMirror/tree/0f65276abb017015b9f6c5bbcfed428645050169)

### 制作に使う際の検討

VRMアバターの配信・キャラ表示基盤として組み合わせやすい。

**次に確かめること（実施前）**: 手持ちのVRMで表示・モーション反映・クロマキー合成・外部ツール連携（OSC等）を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/malaybaku/VMagicMirror/blob/0f65276abb017015b9f6c5bbcfed428645050169/README.md)

**最新GitHub Release**: [v5.0.0](https://github.com/malaybaku/VMagicMirror/releases/tag/v5.0.0) / 2026-06-06T01:39:00Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-30T08:37:20Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="gaussian-vrm"></a>

## gaussian-vrm

three.js上でVRM形式のスキニング付きガウシアンアバター(GVRM)を扱う実装。three-vrmとgaussian-splats-3dを基盤に、VRMの操作（移動やアニメーション）をそのまま再利用できる。

- **リポジトリ**: https://github.com/naruya/gaussian-vrm
- **分類**: library / 非AI制作 / 研究実装・活発
- **入力**: GVRMファイル、FBXアニメーション（Mixamo等）
- **出力**: Web/モバイル/VR上にレンダリングされるアバター
- **環境**: JavaScript（three.js）。サンプルアバターはGoogle Driveから取得。
- **依存**: three-vrm、GaussianSplats3D、Mixamoのアニメーション（任意）
- **制約・未確認**: assets/ 配下のファイルはMIT対象外で研究用途のみ。制作パイプラインへの組み込み手順や性能の記載はREADMEにない。
- **編集者評価**: SUI 2025 Demo Trackの公式実装で、サンプルアバターとスキャンデータが公開されている。SMPL等の制約ライセンスを使わない構成。
- **メトリクス**: ★425、fork 29、作成 2025-10-08、最終push 2026-09-29T08:00:26Z、archived=False
- **確認**: 2026-10-01 / コミット `f6f552a24f7c2b7fb0d8c73f9c0b5581273b1e4c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/naruya/gaussian-vrm/tree/f6f552a24f7c2b7fb0d8c73f9c0b5581273b1e4c)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/naruya/gaussian-vrm/blob/f6f552a24f7c2b7fb0d8c73f9c0b5581273b1e4c/README.md) / [GitHub API](https://api.github.com/repos/naruya/gaussian-vrm) / [固定ツリー](https://github.com/naruya/gaussian-vrm/tree/f6f552a24f7c2b7fb0d8c73f9c0b5581273b1e4c)

### 制作に使う際の検討

Web向けアバター表現の選択肢として検討できる。

**次に確かめること（実施前）**: サンプルGVRMの読み込みとFBXアニメーション適用、描画負荷を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [apps/avatarworld/main.js](https://github.com/naruya/gaussian-vrm/blob/f6f552a24f7c2b7fb0d8c73f9c0b5581273b1e4c/apps/avatarworld/main.js) / [apps/test/main.js](https://github.com/naruya/gaussian-vrm/blob/f6f552a24f7c2b7fb0d8c73f9c0b5581273b1e4c/apps/test/main.js) / [main.js](https://github.com/naruya/gaussian-vrm/blob/f6f552a24f7c2b7fb0d8c73f9c0b5581273b1e4c/main.js)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-29T08:00:21Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="cortico"></a>

## Cortico

イベントストリームを中心に設計したエージェント基盤。ペルソナbot・AI配信者・ロールプレイ・コンパニオン向けで、Core/Persona/Memory/World/Botの4層構成と、外部環境を隔離して接続するWorld拡張機構を持つ。

- **リポジトリ**: https://github.com/Pal-AI-Lab/Cortico
- **分類**: engine / AIモデル・学習 / 活発・pre-release
- **入力**: LLMプロバイダ設定、外部環境からのイベント、ツール定義
- **出力**: botの応答・行動、Webコンソール上の管理・監視ログ
- **環境**: Node 22+、pnpm。モデルは各種LLM APIまたはローカルのllama.cpp実行を利用。
- **依存**: Node.js/pnpm、外部LLMプロバイダ、cortico-world-vtuber（任意）
- **制約・未確認**: READMEにpre-releaseと明記されている。VTuber向けWorldは本体と別ライセンス(AGPL-3.0+CLA)の別リポジトリで配布される。
- **編集者評価**: Live2D(VTube Studio)・配信TTS・字幕・OBS連携を行うcortico-world-vtuberが別リポジトリで公開されており、AI VTuber構築の土台として具体性がある。
- **メトリクス**: ★183、fork 15、作成 2026-09-13、最終push 2026-10-04T22:43:04Z、archived=False
- **確認**: 2026-10-01 / コミット `02f2936c89ac783675645f95cd87ff8c25305d46`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Pal-AI-Lab/Cortico/tree/02f2936c89ac783675645f95cd87ff8c25305d46)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Pal-AI-Lab/Cortico/blob/02f2936c89ac783675645f95cd87ff8c25305d46/README.md) / [GitHub API](https://api.github.com/repos/Pal-AI-Lab/Cortico) / [固定ツリー](https://github.com/Pal-AI-Lab/Cortico/tree/02f2936c89ac783675645f95cd87ff8c25305d46)

### 制作に使う際の検討

配信・コンパニオン系エージェントの実装基盤として検討できる。

**次に確かめること（実施前）**: ローカルモデルで起動し、コンソールからの対話とWorld拡張の追加手順を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [bots/cormini/index.ts](https://github.com/Pal-AI-Lab/Cortico/blob/02f2936c89ac783675645f95cd87ff8c25305d46/bots/cormini/index.ts) / [bots/corti-soulmate/index.ts](https://github.com/Pal-AI-Lab/Cortico/blob/02f2936c89ac783675645f95cd87ff8c25305d46/bots/corti-soulmate/index.ts) / [bots/corti-soulmate/persona/index.ts](https://github.com/Pal-AI-Lab/Cortico/blob/02f2936c89ac783675645f95cd87ff8c25305d46/bots/corti-soulmate/persona/index.ts)

**最新GitHub Release**: [v0.1.6](https://github.com/Pal-AI-Lab/Cortico/releases/tag/v0.1.6) / 2026-10-04T03:43:53Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-10-01T17:10:50Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="anima"></a>

## Anima

ブラウザで動くVRMキャラクタースタジオ。テキストまたはリアルタイム音声でキャラと対話し、表情・リップシンク・身体モーションを付けて演技させる。

- **リポジトリ**: https://github.com/Yun-0000/Anima
- **分類**: web_app / AIモデル・学習 / 小規模・初期評価候補
- **入力**: テキスト入力、音声（BYOKのOpenAI realtime）、VRMモデル、Mixamo互換FBXアニメーション（任意）
- **出力**: 画面上のVRM演技（表情・モーション）、TTS音声のデータURL
- **環境**: Python 3.12のバックエンド(FastAPI)とNodeのフロントエンド。音声モードはOPENAI_API_KEY、テキストのTTSは任意でELEVENLABS_API_KEY。
- **依存**: React、Three.js、three-vrm、FastAPI、OpenAI realtime / ElevenLabs（任意）
- **制約・未確認**: Mixamoの.fbxは再配布されず、フル動作には各自でアニメーションを用意する必要がある。同梱VRMは本リポジトリの公開デモ用途と明記されている。
- **編集者評価**: キー不要のテキストモードから試せ、音声・リップシンクは実音声に追従、表情とモーションの計画を /api/motion-plan に分離した設計が分かりやすい。
- **メトリクス**: ★3、fork 1、作成 2026-05-03、最終push 2026-05-09T21:04:39Z、archived=False
- **確認**: 2026-10-01 / コミット `9cdfb5eabe4230a34bd1d879053a1abb0baff76a`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Yun-0000/Anima/tree/9cdfb5eabe4230a34bd1d879053a1abb0baff76a)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Yun-0000/Anima/blob/9cdfb5eabe4230a34bd1d879053a1abb0baff76a/README.md) / [GitHub API](https://api.github.com/repos/Yun-0000/Anima) / [固定ツリー](https://github.com/Yun-0000/Anima/tree/9cdfb5eabe4230a34bd1d879053a1abb0baff76a)

### 制作に使う際の検討

VRMキャラの対話・演技の試作に使える。

**次に確かめること（実施前）**: 同梱の2体のVRMでテキストモードとモーション適用、リップシンクの追従を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [backend/app/main.py](https://github.com/Yun-0000/Anima/blob/9cdfb5eabe4230a34bd1d879053a1abb0baff76a/backend/app/main.py) / [frontend/src/main.tsx](https://github.com/Yun-0000/Anima/blob/9cdfb5eabe4230a34bd1d879053a1abb0baff76a/frontend/src/main.tsx)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-05-09T21:04:17Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="open-vt"></a>

## open-vt

Godotで作られたオープンソースの2D VTuberソフト。OpenSeeFaceとVTubeStudioのトラッカーに対応し、OBSで取り込みやすい透過ウィンドウや複数ウィンドウのポップアウト操作を持つ。

- **リポジトリ**: https://github.com/erodozer/open-vt
- **分類**: desktop_tool / 非AI制作 / 実運用候補
- **入力**: Live2Dモデルとアセット、フェイストラッキング入力（OpenSeeFace／VTubeStudio）
- **出力**: 配信・録画向けのアバター表示
- **環境**: Godot。thirdparty/のサブモジュールをbuild_dependencies.shでビルドする必要があり、OpenSeeFaceは別途実行ファイルを用意する。
- **依存**: Ayagami、OpenSeeFace、VTubeStudio（任意）
- **制約・未確認**: VTSのプラグイン互換やVNetは対象外。AI対話や音声合成などは含まず、アバター表示に限定される。
- **編集者評価**: VTube Studio互換のアセット運用を掲げ、Linuxネイティブ対応とピクセルアート向けのスケーリング調整を特徴とする。
- **メトリクス**: ★281、fork 9、作成 2025-01-12、最終push 2026-09-25T02:18:59Z、archived=False
- **確認**: 2026-10-02 / コミット `89f2f0f4119a21c96a8b9e1222850b558ffcb62e`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/erodozer/open-vt/tree/89f2f0f4119a21c96a8b9e1222850b558ffcb62e)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/erodozer/open-vt/blob/89f2f0f4119a21c96a8b9e1222850b558ffcb62e/README.md) / [GitHub API](https://api.github.com/repos/erodozer/open-vt) / [固定ツリー](https://github.com/erodozer/open-vt/tree/89f2f0f4119a21c96a8b9e1222850b558ffcb62e)

### 制作に使う際の検討

Live2Dアバターでの配信運用と、透過合成を含むキャプチャ。

**次に確かめること（実施前）**: 手元のモデルでOpenSeeFace入力の追従と透過ウィンドウ出力を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/erodozer/open-vt/blob/89f2f0f4119a21c96a8b9e1222850b558ffcb62e/README.md)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-25T02:18:47Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="a-r-i-a"></a>

## A.R.I.A

Live2D・VRM・GLB・PNG/GIFアバターをまとめて扱うクロスプラットフォームのアバタースタジオ。顔トラッキング、物理、ライティング、視覚アクション、複数アバターのOBS出力に対応する。

- **リポジトリ**: https://github.com/NekoUnix/A.R.I.A
- **分類**: desktop_tool / 非AI制作 / Alpha・初期評価候補
- **入力**: Live2Dモデル（.model3.json/.moc3等）、VRMファイル、スキン済みGLB、PNG/GIF画像、カメラやiPhone等のトラッキング入力
- **出力**: OBS向けの複数アバター表示、配信画面
- **環境**: Windows/macOS/Linux。プラットフォーム別のバイナリを配布。Live2D/VRMなどのモデル素材は別途用意。グラフィックドライバが必要。
- **依存**: 各アバター形式のモデル素材、トラッキングアプリ（iPhone利用時はiFacialMocap等）
- **制約・未確認**: Alpha版で一部のデバイス組合せは検証不足。VTube Studio/VBridger/VRC・GLBインポートや生成スプリングチェーンは実験的。モデル素材の利用規約は別途。ライセンスMIT。
- **編集者評価**: 形式の異なる複数アバターを同じ画面に並べてOBSへ出せる点が実用的。Live2Dは独自のRustコアで評価し、別途Cubismランタイムを要さないと記載。
- **メトリクス**: ★9、fork 0、作成 2026-09-11、最終push 2026-10-05T10:58:52Z、archived=False
- **確認**: 2026-10-04 / コミット `14973e63e85d4b590ab104ba51dd1acdee24ffb9`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/NekoUnix/A.R.I.A/tree/14973e63e85d4b590ab104ba51dd1acdee24ffb9)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/NekoUnix/A.R.I.A/blob/14973e63e85d4b590ab104ba51dd1acdee24ffb9/README.md) / [GitHub API](https://api.github.com/repos/NekoUnix/A.R.I.A) / [固定ツリー](https://github.com/NekoUnix/A.R.I.A/tree/14973e63e85d4b590ab104ba51dd1acdee24ffb9)

### 制作に使う際の検討

複数アバターを1配信画面にまとめたいVTuber/配信者に向く。

**次に確かめること（実施前）**: Live2DとVRMを同時に読み込み、トラッキング共有・物理挙動・OBS出力の安定性を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [apps/aria-cli/src/main.rs](https://github.com/NekoUnix/A.R.I.A/blob/14973e63e85d4b590ab104ba51dd1acdee24ffb9/apps/aria-cli/src/main.rs) / [apps/aria-desktop/src/app.rs](https://github.com/NekoUnix/A.R.I.A/blob/14973e63e85d4b590ab104ba51dd1acdee24ffb9/apps/aria-desktop/src/app.rs) / [apps/aria-desktop/src/main.rs](https://github.com/NekoUnix/A.R.I.A/blob/14973e63e85d4b590ab104ba51dd1acdee24ffb9/apps/aria-desktop/src/main.rs)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-29T00:29:50Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="seidr-smidja"></a>

## Seidr-Smidja

AIエージェントがYAML仕様からVRMアバターを設計・構築・検証・レンダリングするヘッドレスなパイプライン。VRoidベーステンプレートにBlenderをヘッドレスで適用し、VRChat/VTube Studio互換を検査して.vrmを出力する。

- **リポジトリ**: https://github.com/hrabanazviking/Seidr-Smidja
- **分類**: pipeline / AI連携 / Genesis・初期評価候補
- **入力**: アバター仕様のYAML（身長・髪・服・表情・ライセンス情報等）、VRoidベーステンプレート
- **出力**: .vrmファイル、プレビューPNG（正面・斜め・横・顔クローズアップ・Tポーズ・表情）
- **環境**: Python 3.10+。ヘッドレス経路はBlender+VRM Add-on for Blender、VRoid操作経路はVRoid Studio（Tailscale越しも可）。
- **依存**: Blender、VRM Add-on for Blender、VRoid Studio、pyautogui等（VRoid操作時）
- **制約・未確認**: 人間向けGUIは無くagent/CLI専用。VRM以外の形式は対象外。READMEのステータスバッジはGenesis Phaseで、ライセンスバッジはTBD表記だがリポジトリ表記はApache-2.0。
- **編集者評価**: 人手を介さずVRMを反復生成し、互換チェックとレンダリングまで行う発想が特徴的。MCP/CLI/REST/スキルの4経路で操作できる。
- **メトリクス**: ★21、fork 3、作成 2026-05-06、最終push 2026-10-05T03:37:54Z、archived=False
- **確認**: 2026-10-04 / コミット `482c8f0032b28c4ceb323478e7854adae3715f72`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/hrabanazviking/Seidr-Smidja/tree/482c8f0032b28c4ceb323478e7854adae3715f72)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/hrabanazviking/Seidr-Smidja/blob/482c8f0032b28c4ceb323478e7854adae3715f72/README.md) / [GitHub API](https://api.github.com/repos/hrabanazviking/Seidr-Smidja) / [固定ツリー](https://github.com/hrabanazviking/Seidr-Smidja/tree/482c8f0032b28c4ceb323478e7854adae3715f72)

### 制作に使う際の検討

VRMアバターの量産や、エージェント主導の反復的なアバター制作を試したい用途に向く。

**次に確かめること（実施前）**: 最小仕様のYAMLでビルドし、出力.vrmの互換チェック結果とレンダリング品質、再現性を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [src/seidr_smidja/bridges/mjoll/server.py](https://github.com/hrabanazviking/Seidr-Smidja/blob/482c8f0032b28c4ceb323478e7854adae3715f72/src/seidr_smidja/bridges/mjoll/server.py) / [src/seidr_smidja/bridges/runstafr/cli.py](https://github.com/hrabanazviking/Seidr-Smidja/blob/482c8f0032b28c4ceb323478e7854adae3715f72/src/seidr_smidja/bridges/runstafr/cli.py) / [src/seidr_smidja/brunhand/daemon/app.py](https://github.com/hrabanazviking/Seidr-Smidja/blob/482c8f0032b28c4ceb323478e7854adae3715f72/src/seidr_smidja/brunhand/daemon/app.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-17T10:48:08Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="vrm-studio"></a>

## vrm-studio

ブラウザで動くVTubingアプリ。Google MediaPipe Holisticで顔・手・全身をトラッキングし、Three.jsでVRMアバターを動かす。グリーンスクリーン、OBS連携、カルマンフィルタによる平滑化を備える。

- **リポジトリ**: https://github.com/vucinatim/vrm-studio
- **分類**: web_app / AIは任意 / 小規模・実用候補
- **入力**: Webカメラ映像、VRMモデル
- **出力**: トラッキング済みアバター表示（OBSのウィンドウキャプチャ経由で合成）
- **環境**: Webカメラと対応ブラウザ。ローカル実行はpnpm/Next.js。
- **依存**: Google MediaPipe、Three.js/react-three-fiber、VRMモデル
- **制約・未確認**: ライセンス表記なし。トラッキングはMediaPipe Holisticに依存。READMEの計測はM1で30-50ms/フレーム。
- **編集者評価**: インストール不要でVRMアバターの配信環境を組める。AI生成ではなくトラッキング中心の構成。
- **メトリクス**: ★21、fork 3、作成 2025-06-29、最終push 2025-12-09T08:30:59Z、archived=False
- **確認**: 2026-10-05 / コミット `30af4abcd417039b4f3d9615a1427402f6d04a2c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/vucinatim/vrm-studio/tree/30af4abcd417039b4f3d9615a1427402f6d04a2c)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/vucinatim/vrm-studio/blob/30af4abcd417039b4f3d9615a1427402f6d04a2c/README.md) / [GitHub API](https://api.github.com/repos/vucinatim/vrm-studio) / [固定ツリー](https://github.com/vucinatim/vrm-studio/tree/30af4abcd417039b4f3d9615a1427402f6d04a2c)

### 制作に使う際の検討

手軽なVTuber配信・アバター確認に使える。商用条件は未記載で要確認。

**次に確かめること（実施前）**: 代表的なVRMでトラッキング精度・遅延・OBS合成の実用性を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/vucinatim/vrm-studio/blob/30af4abcd417039b4f3d9615a1427402f6d04a2c/README.md)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-12-09T08:30:52Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
