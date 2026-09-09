# ASMR・効果音・環境音

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ASMRify](https://github.com/ReactorcoreGames/ASMRify) · [詳細](#asmrify) | 音声に定位移動・残響・ピッチ等を加えて一括処理するASMR向け音声加工ツール。 | AI出力の後処理 / 小規模・初期評価候補 | 1 / 2026-06-18 |
| [FoleyCrafter](https://github.com/open-mmlab/FoleyCrafter) · [詳細](#foleycrafter) | 動画の内容とタイミングに合わせた効果音を生成する研究実装。 | AIモデル・学習 / 研究モデルの評価候補 | 663 / 2026-06-15 |
| [MMAudio](https://github.com/hkchengrex/MMAudio) · [詳細](#mmaudio) | 動画やテキストを条件に、時間的に対応する音声を生成する。 | AIモデル・学習 / 研究モデルの評価候補 | 2,268 / 2026-02-23 |
| [stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools) · [詳細](#stable-audio-tools) | 条件付き音声生成モデルの学習と推論を行うツール群。効果音や環境音素材を検討できる。 | AIモデル・学習 / 更新のある導入・評価候補 | 3,856 / 2026-09-09 |

<a id="asmrify"></a>

## ASMRify

音声に定位移動・残響・ピッチ等を加えて一括処理するASMR向け音声加工ツール。

- **リポジトリ**: https://github.com/ReactorcoreGames/ASMRify
- **分類**: desktop_tool / AI出力の後処理 / 小規模・初期評価候補
- **入力**: 録音またはTTS音声ファイル
- **出力**: 効果処理したWAV・MP3
- **環境**: Windows 10/11、FFmpeg。
- **依存**: FFmpeg、入力音声
- **制約・未確認**: 小規模で利用実績は未確認。AIによるささやき生成・実録バイノーラルの再現・効果効能は確認していない。
- **編集者評価**: AIのTTS出力をASMR風の音声演出へ加工する周辺候補。
- **メトリクス**: ★1、fork 0、作成 2026-06-18、最終push 2026-06-18T22:47:00Z、archived=False
- **確認**: 2026-09-09 / コミット `5f30fc61e6148a537cdc609173880e2d50ae3b53`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/ReactorcoreGames/ASMRify/blob/5f30fc61e6148a537cdc609173880e2d50ae3b53/README.md)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ReactorcoreGames/ASMRify/blob/5f30fc61e6148a537cdc609173880e2d50ae3b53/README.md) / [GitHub API](https://api.github.com/repos/ReactorcoreGames/ASMRify) / [固定ツリー](https://github.com/ReactorcoreGames/ASMRify/tree/5f30fc61e6148a537cdc609173880e2d50ae3b53)

<a id="foleycrafter"></a>

## FoleyCrafter

動画の内容とタイミングに合わせた効果音を生成する研究実装。

- **リポジトリ**: https://github.com/open-mmlab/FoleyCrafter
- **分類**: model / AIモデル・学習 / 研究モデルの評価候補
- **入力**: 無音動画、テキスト条件
- **出力**: 動画に合わせた効果音
- **環境**: Python/GPU環境、推論時のチェックポイント取得。
- **依存**: FoleyCrafterと基盤音声モデル
- **制約・未確認**: ASMR専用ではなく、距離感・耳元表現・立体音響は未検証。
- **編集者評価**: アニメ・ゲーム映像のフォーリー制作候補。
- **メトリクス**: ★663、fork 67、作成 2024-06-25、最終push 2026-06-15T04:39:18Z、archived=False
- **確認**: 2026-09-09 / コミット `b4526d1586aaf044140b359295504452297f8c13`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/open-mmlab/FoleyCrafter/blob/b4526d1586aaf044140b359295504452297f8c13/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/open-mmlab/FoleyCrafter/blob/b4526d1586aaf044140b359295504452297f8c13/README.md) / [GitHub API](https://api.github.com/repos/open-mmlab/FoleyCrafter) / [固定ツリー](https://github.com/open-mmlab/FoleyCrafter/tree/b4526d1586aaf044140b359295504452297f8c13)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [ymzhang319/FoleyCrafter](https://huggingface.co/ymzhang319/FoleyCrafter) — file_listing_checked、確認日 2026-09-09、revision `56c5ba7e052249a10bca6ebd12f9d5d8e6c26ae0`。代表ファイル: `semantic/semantic_adapter.bin`, `temporal_adapter.ckpt`, `vocoder/vocoder.pt`。gated=False。

<a id="mmaudio"></a>

## MMAudio

動画やテキストを条件に、時間的に対応する音声を生成する。

- **リポジトリ**: https://github.com/hkchengrex/MMAudio
- **分類**: model / AIモデル・学習 / 研究モデルの評価候補
- **入力**: 動画、テキスト
- **出力**: 同期音声
- **環境**: Python/GPU環境とチェックポイント。
- **依存**: MMAudio、音声VAE等
- **制約・未確認**: ASMRや日本語のセリフ生成専用ではない。音の同期と内容は素材ごとに評価する。
- **編集者評価**: 映像用の効果音・環境音を作る技術候補。
- **メトリクス**: ★2,268、fork 267、作成 2024-12-07、最終push 2026-02-23T06:09:19Z、archived=False
- **確認**: 2026-09-09 / コミット `974010a026c731054592d8f777218bd9d85a6c24`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/hkchengrex/MMAudio/blob/974010a026c731054592d8f777218bd9d85a6c24/LICENSE)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/hkchengrex/MMAudio/blob/974010a026c731054592d8f777218bd9d85a6c24/README.md) / [GitHub API](https://api.github.com/repos/hkchengrex/MMAudio) / [固定ツリー](https://github.com/hkchengrex/MMAudio/tree/974010a026c731054592d8f777218bd9d85a6c24)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [hkchengrex/MMAudio](https://huggingface.co/hkchengrex/MMAudio) — file_listing_checked、確認日 2026-09-09、revision `eb13a1a98fdbec91753775c57b074ccdfc60587c`。代表ファイル: `checkpoints/mmaudio_large_44k_ckpt.pth`, `checkpoints/mmaudio_medium_44k_ckpt.pth`, `checkpoints/mmaudio_small_16k_ckpt.pth`, `checkpoints/mmaudio_small_44k_ckpt.pth`。gated=False。

<a id="stable-audio-tools"></a>

## stable-audio-tools

条件付き音声生成モデルの学習と推論を行うツール群。効果音や環境音素材を検討できる。

- **リポジトリ**: https://github.com/Stability-AI/stable-audio-tools
- **分類**: model_toolkit / AIモデル・学習 / 更新のある導入・評価候補
- **入力**: テキスト条件、音声、モデル設定
- **出力**: 生成音声・学習済みモデル
- **環境**: Python、PyTorch。モデルごとに必要環境を確認。
- **依存**: Stable Audio Openなど対応モデル
- **制約・未確認**: ASMR専用モデルではない。空間音響・ささやきの品質は未検証。
- **編集者評価**: 音声素材の生成・追加学習を同じ基盤で扱う。
- **メトリクス**: ★3,856、fork 483、作成 2023-05-23、最終push 2026-09-09T09:50:41Z、archived=False
- **確認**: 2026-09-09 / コミット `3241adba4fc2a85cf5b29d9eb68d42f40a28e820`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Stability-AI/stable-audio-tools/blob/3241adba4fc2a85cf5b29d9eb68d42f40a28e820/LICENSE)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Stability-AI/stable-audio-tools/blob/3241adba4fc2a85cf5b29d9eb68d42f40a28e820/README.md) / [GitHub API](https://api.github.com/repos/Stability-AI/stable-audio-tools) / [固定ツリー](https://github.com/Stability-AI/stable-audio-tools/tree/3241adba4fc2a85cf5b29d9eb68d42f40a28e820)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [stabilityai/stable-audio-open-1.0](https://huggingface.co/stabilityai/stable-audio-open-1.0) — file_listing_checked、確認日 2026-09-09、revision `f21265c1e2710b3bd2386596943f0007f55f802e`。代表ファイル: `model.ckpt`, `model.safetensors`, `projection_model/diffusion_pytorch_model.safetensors`, `text_encoder/model.safetensors`。gated=auto。
