# アニメ画像モデルの配布・制作条件比較

[一覧へ](../README.md) · [正本JSON](../model-catalog.json)

GitHub中心の一覧を補うアニメ画像モデル4系統。最新版や全派生を網羅した一覧ではない。具体的な配布リポジトリとrevisionを記録する。

モデルカードとファイル一覧を確認。重み取得・起動・品質比較は未実施。公開日はリポジトリ・ファイル・モデル版で異なります。

## Anima

Cosmos-Predict2-2Bを基にした2B画像モデル。Qwen系テキストエンコーダとQwen-Image VAEを組み合わせる。

- **版の区別**: Baseは追加学習向け、Aestheticは画風調整、Turboは蒸留版。配布には複数のv1.xファイルがあり、系統と具体的なファイル名を固定する。
- **入力・設定**: タグと自然文を併用。Turboは作者推奨CFG1・8〜12ステップ。BaseとAestheticでは品質タグの推奨が異なる。
- **必要構成**: ComfyUIの本体・エンコーダ・VAEを別配置。READMEは512²〜1536²の解像度範囲を案内。全構成の必要VRAMは今回未測定。
- **制約**: 写実と長文の画像内文字は苦手と作者が明記。既存SDXL向けLoRAの互換を仮定しない。
- **利用条件**: metadataはother、license_nameはcirclestone-labs-non-commercial-license。公開重みを無条件商用可と扱わない。
- **編集者評価**: アニメ絵専用の新しい基盤として、従来SDXL系と比較する価値がある。
- **次の検証（未実施）**: 同じキャラ設定と解像度でBase/Aesthetic/Turboを比較し、速度・衣装保持・学習互換を記録する。

確認日: 2026-09-09 / revision `f973fc41ec7545364ac9776c2440285f43ff2a30` / gated=False。ファイル名候補11件の一覧確認。代表ファイル: `split_files/diffusion_models/anima-aesthetic-v1.0.safetensors`、`split_files/diffusion_models/anima-aesthetic-v1.0b.safetensors`、`split_files/diffusion_models/anima-aesthetic-v1.1.safetensors`、`split_files/diffusion_models/anima-base-v1.0.safetensors`

根拠: [固定モデルカード](https://huggingface.co/circlestone-labs/Anima/blob/f973fc41ec7545364ac9776c2440285f43ff2a30/README.md) / [モデルAPI](https://huggingface.co/api/models/circlestone-labs/Anima)

## Animagine XL 4.0 / Opt

Stable Diffusion XL1.0から学習したアニメ向け画像モデル。

- **版の区別**: 4.0とOptを同一配布内で提供。Optの改善は作者評価であり、このカタログの実測順位ではない。
- **入力・設定**: キャラ・作品・画風・一般タグの順序を使う。品質タグを含む作者推奨設定はモデルカードを参照。
- **必要構成**: ComfyUI、WebUI、Diffusers等。使用実装と解像度で必要GPUが変わる。
- **制約**: キャラ名の知識と、新規の自作キャラの連続画像一貫性は別。編集用PSDやリグは出力しない。
- **利用条件**: CreativeML Open RAIL++-Mをモデルカードが案内。利用制限と派生モデル条件は原文を参照。
- **編集者評価**: SDXLの制作環境で比較しやすいアニメ特化の基準候補。
- **次の検証（未実施）**: 4.0とOptを同一seed群で比較し、手・彩度・文字・多人数の混線を確認する。

確認日: 2026-09-09 / revision `2b7c1b397761bf5bd3cc42e5b39ec99314a75a96` / gated=False。ファイル名候補6件の一覧確認。代表ファイル: `animagine-xl-4.0-opt.safetensors`、`animagine-xl-4.0.safetensors`、`unet/diffusion_pytorch_model.safetensors`、`vae/diffusion_pytorch_model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/cagliostrolab/animagine-xl-4.0/blob/2b7c1b397761bf5bd3cc42e5b39ec99314a75a96/README.md) / [モデルAPI](https://huggingface.co/api/models/cagliostrolab/animagine-xl-4.0)

## Illustrious XL early release v0

SDXL系のイラスト生成基盤。カードのbase_modelはKohaku XL beta5。

- **版の区別**: リポジトリ名v0と配布ファイルv0.1/GUIDEDを区別。この項目はIllustrious全派生の一覧ではない。
- **入力・設定**: タグ指示を中心に扱う。派生の推奨品質タグや予測方式を本体へ逆輸入しない。
- **必要構成**: SDXL対応推論環境と具体的チェックポイント。GPU要件は実装ごとに確認。
- **制約**: 配布ページの名称だけで最新版・派生との性能順位を決めない。原稿組版や動画生成は別。
- **利用条件**: metadataはfair-ai-public-license-1.0-sd。派生モデルが追加条件を持つ場合は別途確認する。
- **編集者評価**: NoobAI等の基盤関係を理解し、派生モデルの条件を追跡するために有用。
- **次の検証（未実施）**: 配布ファイル名・予測方式・推奨設定を固定し、自作キャラのLoRA候補との互換を確認する。

確認日: 2026-09-09 / revision `dca0dac303e6dc4b0c31d8001bc685b89b5d0204` / gated=False。ファイル名候補10件の一覧確認。代表ファイル: `Illustrious-XL-v0.1-GUIDED.safetensors`、`Illustrious-XL-v0.1.safetensors`、`unet/diffusion_pytorch_model.bin`、`unet/diffusion_pytorch_model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0/blob/dca0dac303e6dc4b0c31d8001bc685b89b5d0204/README.md) / [モデルAPI](https://huggingface.co/api/models/OnomaAIResearch/Illustrious-xl-early-release-v0)

## NoobAI XL 1.1

Illustrious系のアニメ画像モデル。直接のbase_modelはNoobAI XL1.0。

- **版の区別**: この項目は1.1の配布を対象とし、同名のV-prediction版やコミュニティマージを混ぜない。
- **入力・設定**: 作者はEuler a、25〜30ステップ、CFG5〜6、1024²程度の面積を案内。ネイティブタグを使う。
- **必要構成**: SDXL対応の推論環境。重みの予測方式とワークフローの一致を確認する。
- **制約**: 同じ基盤でも派生の利用条件・プロンプトは同一ではない。多人数や衣装保持は未評価。
- **利用条件**: HFメタデータのFAIPL表記に加え、モデルカード本文にモデル・派生・生成物を含む商用禁止と共有条件を記載。本文の追加条件を見落とさない。
- **編集者評価**: アニメ画像の比較対象として記録するが、公開配布と制作物の利用条件を明確に分ける。
- **次の検証（未実施）**: 同じプロンプトのキャラ・人体・画風を比較し、用途に照らしてカード本文の追加条件を確認する。

確認日: 2026-09-09 / revision `814a274af2b8097c0828819d561ec74c7d0c6cea` / gated=False。ファイル名候補5件の一覧確認。代表ファイル: `NoobAI-XL-v1.1.safetensors`、`unet/diffusion_pytorch_model.safetensors`、`vae/diffusion_pytorch_model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/Laxhar/noobai-XL-1.1/blob/814a274af2b8097c0828819d561ec74c7d0c6cea/README.md) / [モデルAPI](https://huggingface.co/api/models/Laxhar/noobai-XL-1.1)
