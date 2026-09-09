# 制作ワークフロー・追加学習

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) · [詳細](#comfyui) | 画像・動画などのモデルをノードで接続して制作工程を構成する。 | AI連携 / 更新のある導入・評価候補 | 132,241 / 2026-09-09 |
| [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) · [詳細](#comfyui-wanvideowrapper) | Wan系および関連動画モデルをComfyUIで使うためのラッパーノード。 | AI連携 / 連携の評価候補 | 6,687 / 2026-05-24 |
| [musubi-tuner](https://github.com/kohya-ss/musubi-tuner) · [詳細](#musubi-tuner) | 画像・動画モデル向けのLoRA学習スクリプト群。 | AIモデル・学習 / 更新のある導入・評価候補 | 2,033 / 2026-09-08 |

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
- **メトリクス**: ★132,241、fork 15,590、作成 2023-01-17、最終push 2026-09-09T18:24:58Z、archived=False
- **確認**: 2026-09-09 / コミット `4989cdd95487531b50438c6a091dffa06e4af4b2`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Comfy-Org/ComfyUI/blob/4989cdd95487531b50438c6a091dffa06e4af4b2/LICENSE)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Comfy-Org/ComfyUI/blob/4989cdd95487531b50438c6a091dffa06e4af4b2/README.md) / [GitHub API](https://api.github.com/repos/Comfy-Org/ComfyUI) / [固定ツリー](https://github.com/Comfy-Org/ComfyUI/tree/4989cdd95487531b50438c6a091dffa06e4af4b2)

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
- **メトリクス**: ★6,687、fork 691、作成 2025-02-25、最終push 2026-05-24T13:07:20Z、archived=False
- **確認**: 2026-09-09 / コミット `088128b224242e110d3906c6750e9a3a348a659b`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/088128b224242e110d3906c6750e9a3a348a659b/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/088128b224242e110d3906c6750e9a3a348a659b/readme.md) / [GitHub API](https://api.github.com/repos/kijai/ComfyUI-WanVideoWrapper) / [固定ツリー](https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/088128b224242e110d3906c6750e9a3a348a659b)

関連: plugin_for → comfyui（公式説明、接続実行は未検証）

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
- **メトリクス**: ★2,033、fork 308、作成 2024-12-31、最終push 2026-09-08T09:30:32Z、archived=False
- **確認**: 2026-09-09 / コミット `e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/kohya-ss/musubi-tuner/blob/e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1/README.md)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/kohya-ss/musubi-tuner/blob/e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1/README.md) / [GitHub API](https://api.github.com/repos/kohya-ss/musubi-tuner) / [固定ツリー](https://github.com/kohya-ss/musubi-tuner/tree/e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1)
