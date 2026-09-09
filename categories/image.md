# 画像生成・編集・切り抜き

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**115件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [anime-segmentation](https://github.com/SkyTNT/anime-segmentation) · [詳細](#anime-segmentation) | アニメ絵のキャラクター領域を抽出し、背景除去や合成用マスクを作る。 | AIモデル・学習 / 比較・既存工程の参考 | 838 / 2025-05-21 |
| [krita-ai-diffusion](https://github.com/Acly/krita-ai-diffusion) · [詳細](#krita-ai-diffusion) | Kritaの描画工程へ画像生成・インペイント・アウトペイントを組み込む。 | AI連携 / 更新のある導入・評価候補 | 10,564 / 2026-08-28 |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image) · [詳細](#qwen-image) | テキスト描画と画像編集を扱う汎用画像モデル群。表紙・小物・宣伝画像の制作候補。 | AIモデル・学習 / 研究モデルの評価候補 | 8,294 / 2026-02-10 |
| [Z-Image](https://github.com/Tongyi-MAI/Z-Image) · [詳細](#z-image) | 6B級の汎用画像モデル群。Turboやベースモデルを用途に合わせて利用する。 | AIモデル・学習 / 研究モデルの評価候補 | 12,000 / 2026-02-09 |

<a id="anime-segmentation"></a>

## anime-segmentation

アニメ絵のキャラクター領域を抽出し、背景除去や合成用マスクを作る。

- **リポジトリ**: https://github.com/SkyTNT/anime-segmentation
- **分類**: model / AIモデル・学習 / 比較・既存工程の参考
- **入力**: アニメキャラクター画像
- **出力**: 背景除去画像・マスク
- **環境**: Python推論環境または公式リンクのデモ。
- **依存**: anime-seg重み
- **制約・未確認**: レイヤー分解や隠れた身体部位の補完ではない。最近の更新は少ない。
- **編集者評価**: 立ち絵の切り抜きと素材整理を支える専用基盤。
- **メトリクス**: ★838、fork 76、作成 2022-08-14、最終push 2025-05-21T02:00:35Z、archived=False
- **確認**: 2026-09-09 / コミット `55d874013a2811cdf59c365059174c7823acf5b4`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/SkyTNT/anime-segmentation/tree/55d874013a2811cdf59c365059174c7823acf5b4)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/SkyTNT/anime-segmentation/blob/55d874013a2811cdf59c365059174c7823acf5b4/README.md) / [GitHub API](https://api.github.com/repos/SkyTNT/anime-segmentation) / [固定ツリー](https://github.com/SkyTNT/anime-segmentation/tree/55d874013a2811cdf59c365059174c7823acf5b4)

### 制作に使う際の検討

キャラクターと背景の分離に用途を絞ると入力準備が簡単。多層PSDが必要な工程では追加処理が必要。

**次に確かめること（実施前）**: 細い髪、白い衣装、半透明小物、背景との同系色でマスク境界を評価する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [app.py](https://github.com/SkyTNT/anime-segmentation/blob/55d874013a2811cdf59c365059174c7823acf5b4/app.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-05-21T02:00:34Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [skytnt/anime-seg](https://huggingface.co/skytnt/anime-seg) — file_listing_checked、確認日 2026-09-09、revision `493cb60893f47441b26ec4fb9a306bce9e342982`。代表ファイル: `isnetis.ckpt`, `isnetis.onnx`, `model.safetensors`。gated=False。

<a id="krita-ai-diffusion"></a>

## krita-ai-diffusion

Kritaの描画工程へ画像生成・インペイント・アウトペイントを組み込む。

- **リポジトリ**: https://github.com/Acly/krita-ai-diffusion
- **分類**: integration / AI連携 / 更新のある導入・評価候補
- **入力**: Kritaのキャンバス、選択範囲、プロンプト
- **出力**: 編集レイヤー・生成画像
- **環境**: Kritaと対応する生成バックエンド。
- **依存**: Krita、ComfyUI等の対応生成環境
- **制約・未確認**: 生成モデルとサービスによって費用・実行環境が変わる。
- **編集者評価**: 画師が手で直しながらAIを使う工程に適している。
- **メトリクス**: ★10,564、fork 624、作成 2023-09-01、最終push 2026-08-28T20:55:10Z、archived=False
- **確認**: 2026-09-09 / コミット `dda58d1c63e361207ccec085efbc34dbd32f1654`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Acly/krita-ai-diffusion/tree/dda58d1c63e361207ccec085efbc34dbd32f1654)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Acly/krita-ai-diffusion/blob/dda58d1c63e361207ccec085efbc34dbd32f1654/README.md) / [GitHub API](https://api.github.com/repos/Acly/krita-ai-diffusion) / [固定ツリー](https://github.com/Acly/krita-ai-diffusion/tree/dda58d1c63e361207ccec085efbc34dbd32f1654)

### 制作に使う際の検討

キャンバス上で局所修正しながら生成する制作UI。プロンプト単独生成より修正回数とレイヤー管理を評価する。

**次に確かめること（実施前）**: 選択範囲の外側の保持、レイヤー復元、バックエンド切替、生成待ちからの復旧を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [ai_diffusion/backend/client.py](https://github.com/Acly/krita-ai-diffusion/blob/dda58d1c63e361207ccec085efbc34dbd32f1654/ai_diffusion/backend/client.py)

**最新GitHub Release**: [v1.53.0](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.53.0) / 2026-08-22T19:38:06Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-23T11:02:28Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: plugin_for → krita（公式説明に基づく関係、接続実行は未検証）

<a id="qwen-image"></a>

## Qwen-Image

テキスト描画と画像編集を扱う汎用画像モデル群。表紙・小物・宣伝画像の制作候補。

- **リポジトリ**: https://github.com/QwenLM/Qwen-Image
- **分類**: model / AIモデル・学習 / 研究モデルの評価候補
- **入力**: テキスト、編集対象画像
- **出力**: 生成・編集画像
- **環境**: モデル別の推論環境。公式READMEにdiffusersの例。
- **依存**: Qwen-Imageモデル、編集用モデル。モデル中核は外部Diffusers実装に依存。
- **制約・未確認**: 2.0の告知と公開重みの版を混同しない。本調査の重み候補は2512とEdit-2511。
- **編集者評価**: イラスト制作と文字入り素材の基盤として評価する。
- **メトリクス**: ★8,294、fork 542、作成 2025-08-03、最終push 2026-02-10T07:37:37Z、archived=False
- **確認**: 2026-09-09 / コミット `6b5e1f5cec987d404be5ac6657db3b9aacb56a89`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/QwenLM/Qwen-Image/tree/6b5e1f5cec987d404be5ac6657db3b9aacb56a89)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/README.md) / [GitHub API](https://api.github.com/repos/QwenLM/Qwen-Image) / [固定ツリー](https://github.com/QwenLM/Qwen-Image/tree/6b5e1f5cec987d404be5ac6657db3b9aacb56a89)

### 制作に使う際の検討

公式の配布案内とDiffusers呼出しデモとして読む。GitHub内のモデル独立実装と読み替えない。

**次に確かめること（実施前）**: 2512とEdit-2511を別々に固定し、日本語文字、参照編集、CPUオフロード時の時間を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。 GitHubは配布案内とDiffusers利用デモが中心。

**入口候補（固定ツリーで存在確認）**: [src/examples/demo.py](https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/src/examples/demo.py) / [src/examples/edit_demo.py](https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/src/examples/edit_demo.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-02-10T07:37:32Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

本文を確認した箇所:

- [src/examples/demo.py](https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/src/examples/demo.py): DiffusionPipeline.from_pretrainedを呼ぶデモ部分を確認。モデル中核の独立実装ではない。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Qwen/Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512) — file_listing_checked、確認日 2026-09-09、revision `25468b98e3276ca6700de15c6628e51b7de54a26`。代表ファイル: `text_encoder/model-00001-of-00004.safetensors`, `text_encoder/model-00002-of-00004.safetensors`, `text_encoder/model-00003-of-00004.safetensors`, `text_encoder/model-00004-of-00004.safetensors`。gated=False。
- [Qwen/Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) — file_listing_checked、確認日 2026-09-09、revision `6f3ccc0b56e431dc6a0c2b2039706d7d26f22cb9`。代表ファイル: `text_encoder/model-00001-of-00004.safetensors`, `text_encoder/model-00002-of-00004.safetensors`, `text_encoder/model-00003-of-00004.safetensors`, `text_encoder/model-00004-of-00004.safetensors`。gated=False。

<a id="z-image"></a>

## Z-Image

6B級の汎用画像モデル群。Turboやベースモデルを用途に合わせて利用する。

- **リポジトリ**: https://github.com/Tongyi-MAI/Z-Image
- **分類**: model / AIモデル・学習 / 研究モデルの評価候補
- **入力**: テキスト、モデルによって画像条件
- **出力**: 生成・編集画像
- **環境**: モデル推論環境または公式デモ。
- **依存**: 対応するZ-Imageモデル
- **制約・未確認**: アニメ専用ではない。Turbo・Base・Omni等の能力と公開範囲を分ける。
- **編集者評価**: 背景・素材・イラスト試作の生成基盤候補。
- **メトリクス**: ★12,000、fork 819、作成 2025-11-26、最終push 2026-02-09T12:49:43Z、archived=False
- **確認**: 2026-09-09 / コミット `26f23eda626ffadda020b04ff79488e1d72004cd`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Tongyi-MAI/Z-Image/tree/26f23eda626ffadda020b04ff79488e1d72004cd)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Tongyi-MAI/Z-Image/blob/26f23eda626ffadda020b04ff79488e1d72004cd/README.md) / [GitHub API](https://api.github.com/repos/Tongyi-MAI/Z-Image) / [固定ツリー](https://github.com/Tongyi-MAI/Z-Image/tree/26f23eda626ffadda020b04ff79488e1d72004cd)

### 制作に使う際の検討

Turboで試作速度、Baseで学習・制御の適性を分けて調べる。各派生の公開状況を推測で補完しない。

**次に確かめること（実施前）**: 同一プロンプトと解像度で速度・衣装保持・文字・追加学習の互換を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [inference.py](https://github.com/Tongyi-MAI/Z-Image/blob/26f23eda626ffadda020b04ff79488e1d72004cd/inference.py) / [src/config/inference.py](https://github.com/Tongyi-MAI/Z-Image/blob/26f23eda626ffadda020b04ff79488e1d72004cd/src/config/inference.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-02-09T12:49:08Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) — file_listing_checked、確認日 2026-09-09、revision `f332072aa78be7aecdf3ee76d5c247082da564a6`。代表ファイル: `text_encoder/model-00001-of-00003.safetensors`, `text_encoder/model-00002-of-00003.safetensors`, `text_encoder/model-00003-of-00003.safetensors`, `transformer/diffusion_pytorch_model-00001-of-00003.safetensors`。gated=False。
