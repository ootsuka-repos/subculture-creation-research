# 制作ワークフロー・追加学習

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-02。**151件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) · [詳細](#comfyui) | 画像・動画などのモデルをノードで接続して制作工程を構成する。 | AI連携 / 更新のある導入・評価候補 | 135,880 / 2026-10-02 |
| [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) · [詳細](#comfyui-wanvideowrapper) | Wan系および関連動画モデルをComfyUIで使うためのラッパーノード。 | AI連携 / 連携の評価候補 | 6,719 / 2026-05-24 |
| [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) · [詳細](#diffsynth-studio) | 画像・動画の生成と追加学習を複数モデルで扱う統合実装。 | AIモデル・学習 / モデル・研究候補 | 13,200 / 2026-09-30 |
| [musubi-tuner](https://github.com/kohya-ss/musubi-tuner) · [詳細](#musubi-tuner) | 画像・動画モデル向けのLoRA学習スクリプト群。 | AIモデル・学習 / 更新のある導入・評価候補 | 2,077 / 2026-09-30 |
| [sd-scripts](https://github.com/kohya-ss/sd-scripts) · [詳細](#sd-scripts) | 画像生成モデルの追加学習・LoRAを扱うスクリプト群。 | AIモデル・学習 / 連携・制作ツール候補 | 7,242 / 2026-09-24 |
| [ComfyUI-Anime-Extensions](https://github.com/ootsuka-repos/ComfyUI-Anime-Extensions) · [詳細](#comfyui-anime-extensions) | ComfyUI向けのノード集で、音声合成、画像条件付きキャラクター音声、画像解析・切り抜き、音楽生成、動画生成、漫画ページ組み、VRM処理をまとめて扱う。 | AIモデル・学習 / 初期評価候補 | 1 / 2026-10-02 |
| [comfyui-stylebook](https://github.com/EnragedAntelope/comfyui-stylebook) · [詳細](#comfyui-stylebook) | ComfyUI向けの画風プリセット集。650以上のスタイルにレンダ済みプレビュー、1000以上の作家記述子、130以上のモディファイアを同梱する。 | AIは任意 / 小規模・初期評価候補 | 9 / 2026-10-02 |

<a id="comfyui"></a>

## ComfyUI

画像・動画などのモデルをノードで接続して制作工程を構成する。

- **リポジトリ**: https://github.com/Comfy-Org/ComfyUI
- **分類**: workflow_tool / AI連携 / 更新のある導入・評価候補
- **入力**: ノードグラフ、プロンプト、素材、モデル
- **出力**: 画像・動画・音声などの生成物とワークフローJSON
- **環境**: 対応GPU・実行環境は利用するモデルによる。
- **依存**: 各種生成モデル、任意のカスタムノード
- **制約・未確認**: カスタムノードとモデルの互換性は個別確認が必要。ワークフロー公開だけで再現済みとはしない。
- **編集者評価**: 複数分野のモデルと制作補助ノードを集約できる共通基盤。
- **メトリクス**: ★135,880、fork 16,110、作成 2023-01-17、最終push 2026-10-02T21:19:14Z、archived=False
- **確認**: 2026-09-09 / コミット `4989cdd95487531b50438c6a091dffa06e4af4b2`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Comfy-Org/ComfyUI/tree/4989cdd95487531b50438c6a091dffa06e4af4b2)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Comfy-Org/ComfyUI/blob/4989cdd95487531b50438c6a091dffa06e4af4b2/README.md) / [GitHub API](https://api.github.com/repos/Comfy-Org/ComfyUI) / [固定ツリー](https://github.com/Comfy-Org/ComfyUI/tree/4989cdd95487531b50438c6a091dffa06e4af4b2)

### 制作に使う際の検討

モデルやノードを工程として保存する制作基盤。ノード・重み・ワークフローの三者を固定すると引継ぎやすい。

**次に確かめること（実施前）**: 新規環境で固定グラフを読み、欠けたノード・モデル・出力形式を照合する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [main.py](https://github.com/Comfy-Org/ComfyUI/blob/4989cdd95487531b50438c6a091dffa06e4af4b2/main.py) / [nodes.py](https://github.com/Comfy-Org/ComfyUI/blob/4989cdd95487531b50438c6a091dffa06e4af4b2/nodes.py)

**最新GitHub Release**: [v0.38.0](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.38.0) / 2026-09-29T21:46:45Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T18:23:21Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="comfyui-wanvideowrapper"></a>

## ComfyUI-WanVideoWrapper

Wan系および関連動画モデルをComfyUIで使うためのラッパーノード。

- **リポジトリ**: https://github.com/kijai/ComfyUI-WanVideoWrapper
- **分類**: integration / AI連携 / 連携の評価候補
- **入力**: ComfyUIグラフ、Wan系モデル、素材
- **出力**: 生成動画と再利用可能なワークフロー
- **環境**: ComfyUIと対応モデル、GPU。
- **依存**: ComfyUI、Wan系モデル
- **制約・未確認**: 公式Wan実装ではない。対応版と既存ワークフローの互換性を確認する。
- **編集者評価**: 動画制作のモデル操作・省メモリ設定を工程に組み込める。
- **メトリクス**: ★6,719、fork 694、作成 2025-02-25、最終push 2026-05-24T13:07:20Z、archived=False
- **確認**: 2026-09-09 / コミット `088128b224242e110d3906c6750e9a3a348a659b`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/088128b224242e110d3906c6750e9a3a348a659b)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/088128b224242e110d3906c6750e9a3a348a659b/readme.md) / [GitHub API](https://api.github.com/repos/kijai/ComfyUI-WanVideoWrapper) / [固定ツリー](https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/088128b224242e110d3906c6750e9a3a348a659b)

### 制作に使う際の検討

Wan派生をComfyUIへ接続する第三者統合。公式重みそのままと変換済み配布を分ける。

**次に確かめること（実施前）**: 採用するWan系モデルの版・精度・ノードrevisionを固定してサンプルグラフを再現する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [nodes.py](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/088128b224242e110d3906c6750e9a3a348a659b/nodes.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-05-24T13:07:12Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: plugin_for → comfyui（公式説明に基づく関係、接続実行は未検証）

<a id="diffsynth-studio"></a>

## DiffSynth-Studio

画像・動画の生成と追加学習を複数モデルで扱う統合実装。

- **リポジトリ**: https://github.com/modelscope/DiffSynth-Studio
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 画像・動画・プロンプト・学習素材
- **出力**: 生成物、追加学習済み重み
- **環境**: Python/PyTorch。対象パイプライン別の環境とモデルが必要。
- **依存**: 対応する画像・動画基盤モデル
- **制約・未確認**: 一覧に載るモデルを同じ機能・VRAM条件で扱わない。モデル条件も別。
- **編集者評価**: 複数研究の再現・学習コードを追う制作技術基盤として有用。
- **メトリクス**: ★13,200、fork 1,309、作成 2023-12-07、最終push 2026-09-30T08:07:05Z、archived=False
- **確認**: 2026-09-09 / コミット `ce9f4541d0f4ae47a138337e59066dd633207aa7`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/modelscope/DiffSynth-Studio/tree/ce9f4541d0f4ae47a138337e59066dd633207aa7)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/modelscope/DiffSynth-Studio/blob/ce9f4541d0f4ae47a138337e59066dd633207aa7/README.md) / [GitHub API](https://api.github.com/repos/modelscope/DiffSynth-Studio) / [固定ツリー](https://github.com/modelscope/DiffSynth-Studio/tree/ce9f4541d0f4ae47a138337e59066dd633207aa7)

### 制作に使う際の検討

複数研究の再現・学習コードを追う制作技術基盤として有用。

**次に確かめること（実施前）**: 目的のモデル一つの公式exampleを選び、重みrevisionと入出力を固定して再現する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [diffsynth/__init__.py](https://github.com/modelscope/DiffSynth-Studio/blob/ce9f4541d0f4ae47a138337e59066dd633207aa7/diffsynth/__init__.py) / [diffsynth/version.py](https://github.com/modelscope/DiffSynth-Studio/blob/ce9f4541d0f4ae47a138337e59066dd633207aa7/diffsynth/version.py)

**最新GitHub Release**: [v1.1.9](https://github.com/modelscope/DiffSynth-Studio/releases/tag/v1.1.9) / 2025-11-18T02:32:52Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-08T10:46:42Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="musubi-tuner"></a>

## musubi-tuner

画像・動画モデル向けのLoRA学習スクリプト群。

- **リポジトリ**: https://github.com/kohya-ss/musubi-tuner
- **分類**: training_tool / AIモデル・学習 / 更新のある導入・評価候補
- **入力**: 画像・動画データセット、キャプション、基盤モデル
- **出力**: LoRA等の追加学習結果
- **環境**: Python、学習用GPU。要件は対象アーキテクチャ別。
- **依存**: Wan、Qwen-Image、Z-Image等の対応モデル
- **制約・未確認**: 各モデル作者による公式実装ではない。対応するモデル版と学習素材を確認する。
- **編集者評価**: 画風・キャラ・動作などを制作目的に合わせる学習基盤。
- **メトリクス**: ★2,077、fork 313、作成 2024-12-31、最終push 2026-09-30T12:27:12Z、archived=False
- **確認**: 2026-09-09 / コミット `e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/kohya-ss/musubi-tuner/tree/e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/kohya-ss/musubi-tuner/blob/e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1/README.md) / [GitHub API](https://api.github.com/repos/kohya-ss/musubi-tuner) / [固定ツリー](https://github.com/kohya-ss/musubi-tuner/tree/e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1)

### 制作に使う際の検討

動画等の追加学習をモデル別スクリプトで扱う。学習できる版と推論するUIのLoRA互換性を確認する。

**次に確かめること（実施前）**: 少数素材で学習を完走させ、別カットで過学習・キャラ保持・動画のちらつきを評価する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [wan_train_network.py](https://github.com/kohya-ss/musubi-tuner/blob/e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1/wan_train_network.py)

**最新GitHub Release**: [v0.3.6](https://github.com/kohya-ss/musubi-tuner/releases/tag/v0.3.6) / 2026-09-27T12:27:20Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-13T04:28:48Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="sd-scripts"></a>

## sd-scripts

画像生成モデルの追加学習・LoRAを扱うスクリプト群。

- **リポジトリ**: https://github.com/kohya-ss/sd-scripts
- **分類**: training_tool / AIモデル・学習 / 連携・制作ツール候補
- **入力**: 画像データ、キャプション、基盤モデル
- **出力**: 追加学習モデル・LoRA
- **環境**: Python/PyTorch、モデルごとの学習設定とGPU。
- **依存**: SD/SDXL等の対応する基盤重み
- **制約・未確認**: 生成UIではない。モデル版と学習方式の組み合わせを確認する。
- **編集者評価**: キャラ・画風の再現性を制作側で調整する学習基盤。
- **メトリクス**: ★7,242、fork 1,217、作成 2022-12-18、最終push 2026-09-24T10:35:53Z、archived=False
- **確認**: 2026-09-09 / コミット `4e624302e0088e39933b31cbc71f24212e900f5f`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/kohya-ss/sd-scripts/tree/4e624302e0088e39933b31cbc71f24212e900f5f)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/kohya-ss/sd-scripts/blob/4e624302e0088e39933b31cbc71f24212e900f5f/README.md) / [GitHub API](https://api.github.com/repos/kohya-ss/sd-scripts) / [固定ツリー](https://github.com/kohya-ss/sd-scripts/tree/4e624302e0088e39933b31cbc71f24212e900f5f)

### 制作に使う際の検討

キャラ・画風の再現性を制作側で調整する学習基盤。

**次に確かめること（実施前）**: 未学習のポーズ・衣装・背景で過学習とキャラ保持を評価し、固定検証画像を残す。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [sdxl_train_network.py](https://github.com/kohya-ss/sd-scripts/blob/4e624302e0088e39933b31cbc71f24212e900f5f/sdxl_train_network.py)

**最新GitHub Release**: [v0.12.0](https://github.com/kohya-ss/sd-scripts/releases/tag/v0.12.0) / 2026-09-24T10:35:53Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T13:32:35Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="comfyui-anime-extensions"></a>

## ComfyUI-Anime-Extensions

ComfyUI向けのノード集で、音声合成、画像条件付きキャラクター音声、画像解析・切り抜き、音楽生成、動画生成、漫画ページ組み、VRM処理をまとめて扱う。

- **リポジトリ**: https://github.com/ootsuka-repos/ComfyUI-Anime-Extensions
- **分類**: integration / AIモデル・学習 / 初期評価候補
- **入力**: テキスト、画像、参照音声、歌詞・スタイル
- **出力**: 音声、解析結果JSON、マスク、漫画ページ画像、VRM/Blenderシーン、動画
- **環境**: ComfyUIの最新Extension API、Python環境、VRM機能にはBlender+VRMアドオン。
- **依存**: Irodori-TTS、YuE2、Sol-H3-Spark、dghs-imgutils等。
- **制約・未確認**: モデルとランタイムは同梱されず別途準備。YuE2の重みは非商用ライセンスとREADMEが記載。
- **編集者評価**: Irodori-TTSの音声合成や画像条件付きキャラクター音声、VRMのダンス生成、漫画ページ組みなど制作寄りの機能を1パッケージで提供する点が特徴。
- **メトリクス**: ★1、fork 0、作成 2026-08-30、最終push 2026-10-02T19:20:22Z、archived=False
- **確認**: 2026-09-30 / コミット `aa21a682ea509bab0fa3f17ba877a3867647d4eb`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/ootsuka-repos/ComfyUI-Anime-Extensions/tree/aa21a682ea509bab0fa3f17ba877a3867647d4eb)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ootsuka-repos/ComfyUI-Anime-Extensions/blob/aa21a682ea509bab0fa3f17ba877a3867647d4eb/README.md) / [GitHub API](https://api.github.com/repos/ootsuka-repos/ComfyUI-Anime-Extensions) / [固定ツリー](https://github.com/ootsuka-repos/ComfyUI-Anime-Extensions/tree/aa21a682ea509bab0fa3f17ba877a3867647d4eb)

### 制作に使う際の検討

音声・画像解析・VRM・漫画ページ組みをComfyUI内で連携。

**次に確かめること（実施前）**: Irodori-TTSとVRM Danceノードを実環境で動かし、入出力と必要モデルを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/ootsuka-repos/ComfyUI-Anime-Extensions/blob/aa21a682ea509bab0fa3f17ba877a3867647d4eb/README.md)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-23T00:25:52Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="comfyui-stylebook"></a>

## comfyui-stylebook

ComfyUI向けの画風プリセット集。650以上のスタイルにレンダ済みプレビュー、1000以上の作家記述子、130以上のモディファイアを同梱する。

- **リポジトリ**: https://github.com/EnragedAntelope/comfyui-stylebook
- **分類**: integration / AIは任意 / 小規模・初期評価候補
- **入力**: 被写体プロンプト
- **出力**: スタイル/作家/モディファイアを合成したプロンプトとネガティブ
- **環境**: ComfyUI。依存ゼロ、ネット不要、APIキー不要。
- **依存**: ComfyUI
- **制約・未確認**: スタイルの実効はベースモデル依存。AIモデル自体は含まない。CFG1ではネガティブが効かない旨の注意あり。
- **編集者評価**: 650以上のスタイルにレンダ済みプレビューが付き、見て選べるため画風探索の試行錯誤を減らせる。
- **メトリクス**: ★9、fork 0、作成 2026-08-02、最終push 2026-10-02T12:52:09Z、archived=False
- **確認**: 2026-09-30 / コミット `3ccd87219d061fb549e481843be3c680de341e86`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/EnragedAntelope/comfyui-stylebook/tree/3ccd87219d061fb549e481843be3c680de341e86)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/EnragedAntelope/comfyui-stylebook/blob/3ccd87219d061fb549e481843be3c680de341e86/README.md) / [GitHub API](https://api.github.com/repos/EnragedAntelope/comfyui-stylebook) / [固定ツリー](https://github.com/EnragedAntelope/comfyui-stylebook/tree/3ccd87219d061fb549e481843be3c680de341e86)

### 制作に使う際の検討

画風の探索・統一、作品ごとのルック固定に。

**次に確かめること（実施前）**: 主要スタイルを自前モデルで試し、意図した画風と被写体保持の両立を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [tests/frontend/stubs/app.js](https://github.com/EnragedAntelope/comfyui-stylebook/blob/3ccd87219d061fb549e481843be3c680de341e86/tests/frontend/stubs/app.js)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-28T02:55:42Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
