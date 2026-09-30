# 動画生成

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-30。**136件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [FramePack](https://github.com/lllyasviel/FramePack) · [詳細](#framepack) | 過去フレームの文脈を圧縮して動画を逐次生成する実装・デスクトップUI。 | AIモデル・学習 / モデル・研究候補 | 17,266 / 2025-10-16 |
| [Index-anisora](https://github.com/bilibili/Index-anisora) · [詳細](#index-anisora) | アニメ向け動画生成。版ごとに任意フレーム、マスク制御、スタイル変換等を提供。 | AIモデル・学習 / モデル・研究候補 | 2,519 / 2026-07-16 |
| [LTX-2](https://github.com/Lightricks/LTX-2) · [詳細](#ltx-2) | 音声・動画生成とLoRA学習を扱う公式実装。READMEはLTX-2.5の導入も案内する。 | AIモデル・学習 / 更新のある導入・評価候補 | 9,562 / 2026-09-30 |
| [LTX-Video](https://github.com/Lightricks/LTX-Video) · [詳細](#ltx-video) | LTXの旧世代動画生成実装。 | AIモデル・学習 / 旧版・履歴資料 | 10,997 / 2026-01-05 |
| [SCAIL-2](https://github.com/zai-org/SCAIL-2) · [詳細](#scail-2) | 参照キャラクターに動画の動きを移し、複数参照やキャラクター置換にも対応する。 | AIモデル・学習 / 研究・技術評価候補 | 1,238 / 2026-08-24 |
| [Wan-Move](https://github.com/ali-vilab/Wan-Move) · [詳細](#wan-move) | 動きの軌跡を条件に動画を生成するWan系実装。 | AIモデル・学習 / モデル・研究候補 | 658 / 2026-01-05 |
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) · [詳細](#wan2.2) | テキストや画像から動画を作るWan2.2公式モデル群。 | AIモデル・学習 / 研究モデルの評価候補 | 17,678 / 2026-09-21 |

<a id="framepack"></a>

## FramePack

過去フレームの文脈を圧縮して動画を逐次生成する実装・デスクトップUI。

- **リポジトリ**: https://github.com/lllyasviel/FramePack
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 開始画像、テキスト、長さ設定
- **出力**: 段階的に生成する動画
- **環境**: 作者は最低6GB GPUを案内。初回モデル取得は30GB超。
- **依存**: HunyuanVideo系、FramePack重み、PyTorch
- **制約・未確認**: 少ないVRAMは短い生成時間を保証しない。長尺の人物・背景一貫性は未評価。
- **編集者評価**: 個人GPUで長さを伸ばす実験候補。生成時間を含めて採用を決めたい。
- **メトリクス**: ★17,266、fork 1,733、作成 2025-04-12、最終push 2025-10-16T01:28:50Z、archived=False
- **確認**: 2026-09-09 / コミット `97fe5dbe06ac1f337ece08935b1076a35eefeeb9`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/lllyasviel/FramePack/tree/97fe5dbe06ac1f337ece08935b1076a35eefeeb9)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/lllyasviel/FramePack/blob/97fe5dbe06ac1f337ece08935b1076a35eefeeb9/README.md) / [GitHub API](https://api.github.com/repos/lllyasviel/FramePack) / [固定ツリー](https://github.com/lllyasviel/FramePack/tree/97fe5dbe06ac1f337ece08935b1076a35eefeeb9)

### 制作に使う際の検討

個人GPUで長さを伸ばす実験候補。生成時間を含めて採用を決めたい。

**次に確かめること（実施前）**: 同じ開始画像で10秒と60秒を生成し、総時間と後半の顔・背景の変化を記録する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [demo_gradio.py](https://github.com/lllyasviel/FramePack/blob/97fe5dbe06ac1f337ece08935b1076a35eefeeb9/demo_gradio.py)

**最新GitHub Release**: [windows](https://github.com/lllyasviel/FramePack/releases/tag/windows) / 2025-04-18T03:22:59Z / prerelease=False

デフォルトブランチの確認コミット日時: 2025-10-16T01:28:50Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) — file_listing_checked、確認日 2026-09-09、revision `86cef4396041b6002c957852daac4c91aaa47c79`。代表ファイル: `diffusion_pytorch_model-00001-of-00003.safetensors`, `diffusion_pytorch_model-00002-of-00003.safetensors`, `diffusion_pytorch_model-00003-of-00003.safetensors`。gated=False。

<a id="index-anisora"></a>

## Index-anisora

アニメ向け動画生成。版ごとに任意フレーム、マスク制御、スタイル変換等を提供。

- **リポジトリ**: https://github.com/bilibili/Index-anisora
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 画像、プロンプト、版に応じたマスクや中間フレーム
- **出力**: アニメ動画
- **環境**: V3.2はWan2.2系A14B、8ステップの推論例。
- **依存**: Wan系基盤、Index-anisoraの版別重み
- **制約・未確認**: V3.1の12GB配布パッケージをV3.2の一般要件としない。「3Dキャラ動画」は編集可能なメッシュではない。
- **編集者評価**: アニメ特化の比較対象として優先度が高い。汎用Wanと同じカットを比較すると価値を判断しやすい。
- **メトリクス**: ★2,519、fork 152、作成 2024-12-16、最終push 2026-07-16T08:14:26Z、archived=False
- **確認**: 2026-09-09 / コミット `6cdce3a17548d7ff0f2e05978469f134da25e68e`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/bilibili/Index-anisora/tree/6cdce3a17548d7ff0f2e05978469f134da25e68e)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/bilibili/Index-anisora/blob/6cdce3a17548d7ff0f2e05978469f134da25e68e/README.md) / [GitHub API](https://api.github.com/repos/bilibili/Index-anisora) / [固定ツリー](https://github.com/bilibili/Index-anisora/tree/6cdce3a17548d7ff0f2e05978469f134da25e68e)

### 制作に使う際の検討

アニメ特化の比較対象として優先度が高い。汎用Wanと同じカットを比較すると価値を判断しやすい。

**次に確かめること（実施前）**: V3.2の重みとコードを合わせ、顔・髪の保持、手、動きの大きさを汎用Wanと比較する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [anisoraV3.2/generate_txt_new.py](https://github.com/bilibili/Index-anisora/blob/6cdce3a17548d7ff0f2e05978469f134da25e68e/anisoraV3.2/generate_txt_new.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-07-16T08:07:36Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: based_on → wan2.2（公式説明に基づく関係、接続実行は未検証）

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [IndexTeam/Index-anisora](https://huggingface.co/IndexTeam/Index-anisora) — file_listing_checked、確認日 2026-09-09、revision `b134a8e677e4b22269827af7d596a4f2d9d3430a`。代表ファイル: `14B/Wan2.1_VAE.pth`, `14B/model_part1.safetensors`, `14B/model_part2.safetensors`, `14B/models_clip_open-clip-xlm-roberta-large-vit-huge-14.pth`。gated=False。

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
- **メトリクス**: ★9,562、fork 1,516、作成 2026-01-03、最終push 2026-09-30T14:51:06Z、archived=False
- **確認**: 2026-09-09 / コミット `a95ab856bf29407b6b066ede0abe1846050db56c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Lightricks/LTX-2/tree/a95ab856bf29407b6b066ede0abe1846050db56c)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Lightricks/LTX-2/blob/a95ab856bf29407b6b066ede0abe1846050db56c/README.md) / [GitHub API](https://api.github.com/repos/Lightricks/LTX-2) / [固定ツリー](https://github.com/Lightricks/LTX-2/tree/a95ab856bf29407b6b066ede0abe1846050db56c)

### 制作に使う際の検討

映像と音を同時に生成する短編候補。現READMEの2.5導線と既存2系重みの組み合わせを明記する。

**次に確かめること（実施前）**: 使用版・全依存重みを固定し、台詞の聞き取り、効果音同期、参照人物の保持を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [packages/ltx-pipelines/src/ltx_pipelines/ti2vid_two_stages.py](https://github.com/Lightricks/LTX-2/blob/a95ab856bf29407b6b066ede0abe1846050db56c/packages/ltx-pipelines/src/ltx_pipelines/ti2vid_two_stages.py)

**最新GitHub Release**: [v1.4.1](https://github.com/Lightricks/LTX-2/releases/tag/v1.4.1) / 2026-09-30T14:51:08Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-26T10:46:59Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **メトリクス**: ★10,997、fork 1,151、作成 2024-11-20、最終push 2026-01-05T22:37:07Z、archived=False
- **確認**: 2026-09-09 / コミット `4b2d053057623ddd4d0a1d3e9cd28890e9ef487f`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Lightricks/LTX-Video/tree/4b2d053057623ddd4d0a1d3e9cd28890e9ef487f)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Lightricks/LTX-Video/blob/4b2d053057623ddd4d0a1d3e9cd28890e9ef487f/README.md) / [GitHub API](https://api.github.com/repos/Lightricks/LTX-Video) / [固定ツリー](https://github.com/Lightricks/LTX-Video/tree/4b2d053057623ddd4d0a1d3e9cd28890e9ef487f)

### 制作に使う際の検討

既存ワークフロー再現のための前世代記録。新規制作は後継との入力・モデル差から比較する。

**次に確かめること（実施前）**: 保存済み旧ワークフローの再現性を確認し、同じ条件をLTX-2に移す際の変更点を記録する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [inference.py](https://github.com/Lightricks/LTX-Video/blob/4b2d053057623ddd4d0a1d3e9cd28890e9ef487f/inference.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-01-05T22:37:06Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: successor → ltx-2（公式説明に基づく関係、接続実行は未検証）

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
- **メトリクス**: ★1,238、fork 90、作成 2026-05-28、最終push 2026-08-24T13:30:59Z、archived=False
- **確認**: 2026-09-09 / コミット `78fe19576bb06be96c2375e088574a262a300edb`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/zai-org/SCAIL-2/tree/78fe19576bb06be96c2375e088574a262a300edb)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/zai-org/SCAIL-2/blob/78fe19576bb06be96c2375e088574a262a300edb/README.md) / [GitHub API](https://api.github.com/repos/zai-org/SCAIL-2) / [固定ツリー](https://github.com/zai-org/SCAIL-2/tree/78fe19576bb06be96c2375e088574a262a300edb)

### 制作に使う際の検討

動作動画とマスクを用いたキャラ置換の候補。マスク準備を含む工程全体の手間を評価する。

**次に確かめること（実施前）**: 全身・横向き・自己遮蔽でキャラ保持、背景漏れ、複数参照時の変化を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [generate.py](https://github.com/zai-org/SCAIL-2/blob/78fe19576bb06be96c2375e088574a262a300edb/generate.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-24T13:30:59Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [zai-org/SCAIL-2](https://huggingface.co/zai-org/SCAIL-2) — file_listing_checked、確認日 2026-09-09、revision `150cc0ca4e98e50e60b9295dacde39442fdccab2`。代表ファイル: `Wan2.1_VAE.pth`, `model/1/fsdp2_rank_0000_checkpoint.pt`, `model/bias-aware-dpo-lora.pt`, `model/relighting-lora.pt`。gated=False。

<a id="wan-move"></a>

## Wan-Move

動きの軌跡を条件に動画を生成するWan系実装。

- **リポジトリ**: https://github.com/ali-vilab/Wan-Move
- **分類**: model / AIモデル・学習 / モデル・研究候補
- **入力**: 開始画像、プロンプト、移動軌跡
- **出力**: 5秒・480P等の制御動画
- **環境**: 14B。公式例はオフロード等を併用して単一40GB GPU。
- **依存**: Wan-Move重み、Wan2.1系、CoTracker
- **制約・未確認**: 第三者の低VRAM統合と公式経路を分ける。軌跡制御で厳密な骨格アニメになるわけではない。
- **編集者評価**: キャラや小物の移動位置を狙った短いカットの候補。
- **メトリクス**: ★658、fork 37、作成 2025-12-06、最終push 2026-01-05T11:32:22Z、archived=False
- **確認**: 2026-09-09 / コミット `80c58a7d2ad175fa82a4d57f79f2a1415317dcfa`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/ali-vilab/Wan-Move/tree/80c58a7d2ad175fa82a4d57f79f2a1415317dcfa)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ali-vilab/Wan-Move/blob/80c58a7d2ad175fa82a4d57f79f2a1415317dcfa/README.md) / [GitHub API](https://api.github.com/repos/ali-vilab/Wan-Move) / [固定ツリー](https://github.com/ali-vilab/Wan-Move/tree/80c58a7d2ad175fa82a4d57f79f2a1415317dcfa)

### 制作に使う際の検討

キャラや小物の移動位置を狙った短いカットの候補。

**次に確かめること（実施前）**: 指定軌跡と画面上の追跡結果、遮蔽時の位置、見た目の保持を比較する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [generate.py](https://github.com/ali-vilab/Wan-Move/blob/80c58a7d2ad175fa82a4d57f79f2a1415317dcfa/generate.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-01-05T11:31:27Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: documented_integration → comfyui-wanvideowrapper（公式説明に基づく関係、接続実行は未検証）

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Ruihang/Wan-Move-14B-480P](https://huggingface.co/Ruihang/Wan-Move-14B-480P) — file_listing_checked、確認日 2026-09-09、revision `63a21fd3f4f1e6c6104e29f6b8d9b8ce3d635456`。代表ファイル: `Wan2.1_VAE.pth`, `diffusion_pytorch_model-00001-of-00007.safetensors`, `diffusion_pytorch_model-00002-of-00007.safetensors`, `diffusion_pytorch_model-00003-of-00007.safetensors`。gated=False。

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
- **メトリクス**: ★17,678、fork 2,280、作成 2025-07-28、最終push 2026-09-21T06:16:22Z、archived=False
- **確認**: 2026-09-09 / コミット `42bf4cfaa384bc21833865abc2f9e6c0e67233dc`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Wan-Video/Wan2.2/tree/42bf4cfaa384bc21833865abc2f9e6c0e67233dc)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Wan-Video/Wan2.2/blob/42bf4cfaa384bc21833865abc2f9e6c0e67233dc/README.md) / [GitHub API](https://api.github.com/repos/Wan-Video/Wan2.2) / [固定ツリー](https://github.com/Wan-Video/Wan2.2/tree/42bf4cfaa384bc21833865abc2f9e6c0e67233dc)

### 制作に使う際の検討

汎用動画基盤としてアニメ特化版の比較元にする。TI2V-5B、A14B、Animate等は別構成として扱う。

**次に確かめること（実施前）**: 一つの版に固定し、同じキャラと動作でAnisora等との画風・時間的一貫性を比較する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [generate.py](https://github.com/Wan-Video/Wan2.2/blob/42bf4cfaa384bc21833865abc2f9e6c0e67233dc/generate.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-03-17T10:48:41Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Wan-AI/Wan2.2-TI2V-5B](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B) — file_listing_checked、確認日 2026-09-09、revision `921dbaf3f1674a56f47e83fb80a34bac8a8f203e`。代表ファイル: `Wan2.2_VAE.pth`, `diffusion_pytorch_model-00001-of-00003.safetensors`, `diffusion_pytorch_model-00002-of-00003.safetensors`, `diffusion_pytorch_model-00003-of-00003.safetensors`。gated=False。
