# 動画生成

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [LTX-2](https://github.com/Lightricks/LTX-2) · [詳細](#ltx-2) | 音声・動画生成とLoRA学習を扱う公式実装。READMEはLTX-2.5の導入も案内する。 | AIモデル・学習 / 更新のある導入・評価候補 | 9,380 / 2026-08-26 |
| [LTX-Video](https://github.com/Lightricks/LTX-Video) · [詳細](#ltx-video) | LTXの旧世代動画生成実装。 | AIモデル・学習 / 旧版・履歴資料 | 10,941 / 2026-01-05 |
| [SCAIL-2](https://github.com/zai-org/SCAIL-2) · [詳細](#scail-2) | 参照キャラクターに動画の動きを移し、複数参照やキャラクター置換にも対応する。 | AIモデル・学習 / 研究・技術評価候補 | 1,177 / 2026-08-24 |
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) · [詳細](#wan2.2) | テキストや画像から動画を作るWan2.2公式モデル群。 | AIモデル・学習 / 研究モデルの評価候補 | 17,444 / 2026-03-17 |

<a id="ltx-2"></a>

## LTX-2

音声・動画生成とLoRA学習を扱う公式実装。READMEはLTX-2.5の導入も案内する。

- **リポジトリ**: https://github.com/Lightricks/LTX-2
- **分類**: model / AIモデル・学習 / 更新のある導入・評価候補
- **入力**: テキスト、参照画像・制御条件
- **出力**: 音声と映像を伴う動画
- **環境**: モデル別のGPU環境。READMEの2.5取得例は約66GiBのモデル群。
- **依存**: LTXモデル、テキストエンコーダ、VAE、アップスケーラ
- **制約・未確認**: LTX-2と2.5の版・必要モデル・利用条件を分ける。全環境での動作は未検証。
- **編集者評価**: 音と映像を一緒に制作する候補。旧LTX-Videoから開発の主軸が移った。
- **メトリクス**: ★9,380、fork 1,484、作成 2026-01-03、最終push 2026-08-26T10:47:10Z、archived=False
- **確認**: 2026-09-09 / コミット `a95ab856bf29407b6b066ede0abe1846050db56c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Lightricks/LTX-2/blob/a95ab856bf29407b6b066ede0abe1846050db56c/LICENSE)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Lightricks/LTX-2/blob/a95ab856bf29407b6b066ede0abe1846050db56c/README.md) / [GitHub API](https://api.github.com/repos/Lightricks/LTX-2) / [固定ツリー](https://github.com/Lightricks/LTX-2/tree/a95ab856bf29407b6b066ede0abe1846050db56c)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) — file_listing_checked、確認日 2026-09-09、revision `5e6e71018ee1756ed329b697a7b4aedc934dfce9`。代表ファイル: `diffusion_models/ltx-2.5-22b-dev-transformer-bf16.safetensors`, `diffusion_models/ltx-2.5-22b-dev-transformer-comfy-int8-convrot.safetensors`, `diffusion_models/ltx-2.5-22b-distilled-transformer-bf16.safetensors`, `diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors`。gated=auto。

<a id="ltx-video"></a>

## LTX-Video

LTXの旧世代動画生成実装。

- **リポジトリ**: https://github.com/Lightricks/LTX-Video
- **分類**: model / AIモデル・学習 / 旧版・履歴資料
- **入力**: テキスト、参照画像
- **出力**: 動画
- **環境**: 旧LTX-Videoモデルと対応Python環境。
- **依存**: LTX-Videoモデル
- **制約・未確認**: 公式READMEはLTX-2への移行を案内。現在の主開発先として推薦しない。
- **編集者評価**: 既存ワークフローの保守・比較資料として残す。
- **メトリクス**: ★10,941、fork 1,130、作成 2024-11-20、最終push 2026-01-05T22:37:07Z、archived=False
- **確認**: 2026-09-09 / コミット `4b2d053057623ddd4d0a1d3e9cd28890e9ef487f`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Lightricks/LTX-Video/blob/4b2d053057623ddd4d0a1d3e9cd28890e9ef487f/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Lightricks/LTX-Video/blob/4b2d053057623ddd4d0a1d3e9cd28890e9ef487f/README.md) / [GitHub API](https://api.github.com/repos/Lightricks/LTX-Video) / [固定ツリー](https://github.com/Lightricks/LTX-Video/tree/4b2d053057623ddd4d0a1d3e9cd28890e9ef487f)

関連: successor → ltx-2（公式説明、接続実行は未検証）

<a id="scail-2"></a>

## SCAIL-2

参照キャラクターに動画の動きを移し、複数参照やキャラクター置換にも対応する。

- **リポジトリ**: https://github.com/zai-org/SCAIL-2
- **分類**: model / AIモデル・学習 / 研究・技術評価候補
- **入力**: 参照画像、動作動画、対応マスク、プロンプト
- **出力**: キャラクター動画、キャラ置換動画
- **環境**: 14Bモデルと前処理環境が必要。Python 3.10〜3.12。
- **依存**: SCAIL-2重み、Wan VAE、T5、前処理モデル
- **制約・未確認**: アニメ専用ではない。入力マスクが重要で、複数参照は品質低下の場合がある。
- **編集者評価**: 2026年6月に推論コード・モデル、8月に学習コード公開。ComfyUI連携あり。
- **メトリクス**: ★1,177、fork 89、作成 2026-05-28、最終push 2026-08-24T13:30:59Z、archived=False
- **確認**: 2026-09-09 / コミット `78fe19576bb06be96c2375e088574a262a300edb`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/zai-org/SCAIL-2/blob/78fe19576bb06be96c2375e088574a262a300edb/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/zai-org/SCAIL-2/blob/78fe19576bb06be96c2375e088574a262a300edb/README.md) / [GitHub API](https://api.github.com/repos/zai-org/SCAIL-2) / [固定ツリー](https://github.com/zai-org/SCAIL-2/tree/78fe19576bb06be96c2375e088574a262a300edb)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [zai-org/SCAIL-2](https://huggingface.co/zai-org/SCAIL-2) — file_listing_checked、確認日 2026-09-09、revision `150cc0ca4e98e50e60b9295dacde39442fdccab2`。代表ファイル: `Wan2.1_VAE.pth`, `model/1/fsdp2_rank_0000_checkpoint.pt`, `model/bias-aware-dpo-lora.pt`, `model/relighting-lora.pt`。gated=False。

<a id="wan2.2"></a>

## Wan2.2

テキストや画像から動画を作るWan2.2公式モデル群。

- **リポジトリ**: https://github.com/Wan-Video/Wan2.2
- **分類**: model / AIモデル・学習 / 研究モデルの評価候補
- **入力**: テキスト、画像等の条件
- **出力**: 生成動画
- **環境**: モデル規模と設定に応じたGPU環境。
- **依存**: Wan2.2の対応モデル
- **制約・未確認**: アニメ専用ではない。5BとA14B等の機能・メモリ要件を一括りにしない。
- **編集者評価**: 短編アニメ・背景動画・動作素材の生成基盤候補。
- **メトリクス**: ★17,444、fork 2,235、作成 2025-07-28、最終push 2026-03-17T10:48:41Z、archived=False
- **確認**: 2026-09-09 / コミット `42bf4cfaa384bc21833865abc2f9e6c0e67233dc`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Wan-Video/Wan2.2/blob/42bf4cfaa384bc21833865abc2f9e6c0e67233dc/LICENSE.txt)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Wan-Video/Wan2.2/blob/42bf4cfaa384bc21833865abc2f9e6c0e67233dc/README.md) / [GitHub API](https://api.github.com/repos/Wan-Video/Wan2.2) / [固定ツリー](https://github.com/Wan-Video/Wan2.2/tree/42bf4cfaa384bc21833865abc2f9e6c0e67233dc)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Wan-AI/Wan2.2-TI2V-5B](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B) — file_listing_checked、確認日 2026-09-09、revision `921dbaf3f1674a56f47e83fb80a34bac8a8f203e`。代表ファイル: `Wan2.2_VAE.pth`, `diffusion_pytorch_model-00001-of-00003.safetensors`, `diffusion_pytorch_model-00002-of-00003.safetensors`, `diffusion_pytorch_model-00003-of-00003.safetensors`。gated=False。
