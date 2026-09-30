# アニメ系モデルの配布・制作条件比較

[一覧へ](../README.md) · [正本JSON](../model-catalog.json)

GitHub中心の一覧を補うアニメ系モデル（画像・音声など）。当初の4系統は人手で調査、以降はAIが毎日自動追加（人の確認なし）。全派生を網羅した一覧ではない。具体的な配布リポジトリとrevisionを記録する。

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

## manga-panel-detector-yolo26n

Ultralytics YOLO26-nano（2.57Mパラメータ）を、Manga109-sでパネルとテキストの2クラス検出にファインチューニングしたモデル。入力は640x640。

- **版の区別**: FP32のPyTorch重み（manga_panel_detector_fp32.pt、約15MB、追加学習・再エクスポート向け）と、Android/LiteRT向けINT8 TFLite（manga_panel_detector_int8.tflite、2.71MB）の2ファイル。READMEにFP32とINT8のmAP差はごく小さいと記載。
- **入力・設定**: プロンプトは不要。推論時の推奨confidence閾値は0.25。クラスは0=panel、1=text。
- **必要構成**: Pythonではultralyticsで推論、モバイルではTFLite/LiteRTランタイム。READM EはCPUで約100〜180ms/枚と記載。学習元はManga109-s（87作品・約18kページ）。
- **制約**: 検出はコマ枠とテキスト領域の2クラスのみで、セリフの文字起こし・話者・読み順は扱わない。学習は日本語漫画中心。重みはAGPL-3.0で、ネットワーク経由のサービス提供時は完全なソース公開が必要と作者が明記。Manga109-sの利用条件も追加適用され出典表示が必要。
- **利用条件**: 重みはAGPL-3.0（Ultralytics YOLO26由来）。以前はApache-2.0と表示していたが誤りだったと作者が訂正。クローズドな商用製品にはUltralytics Enterprise Licenseが必要と記載。
- **編集者評価**: 漫画ページのコマ・テキスト領域検出を軽量・オンデバイスで回せるため、翻訳・組版・字幕付けの前段処理として組み込みやすい。
- **次の検証（未実施）**: 手元の漫画ページでコマ検出・吹き出し検出の取りこぼしを確認し、AndroidのTFLiteでの速度とメモリを実測する。

確認日: 2026-10-01 / revision `40a2854663d537563cfb95c370288a84c6505b9a` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `manga_panel_detector_fp32.pt`

根拠: [固定モデルカード](https://huggingface.co/leoxs22/manga-panel-detector-yolo26n/blob/40a2854663d537563cfb95c370288a84c6505b9a/README.md) / [モデルAPI](https://huggingface.co/api/models/leoxs22/manga-panel-detector-yolo26n)

## Hy-MT2-1.8B-JP-Manga-Finetune-v5-GGUF

tencent/Hy-MT2-1.8Bを日本語→英語の漫画セリフ翻訳向けにファインチューニングしたモデル（HunYuanDenseV1ForCausalLM）。Q4_K_MのGGUFとマージ済みbf16重みの両方を同梱。

- **版の区別**: manga-v5-Q4_K_M.gguf（約1.13GB、llama.cpp想定）と、config・tokenizer・chat_template付きのbf16 model.safetensors。作者はv4の後継で日英ペアの推奨版と説明。他言語向けはv3-multilingualを案内。
- **入力・設定**: 用語ブロック→指示→訳す行、の順で英語プロンプトを渡す。用語集をプロンプトに含めると効くと作者が説明。生成はtemperature 0.15、top_k 20、top_p 0.6、repeat_penalty 1.05、min_p 0。
- **必要構成**: llama.cpp（GGUF）またはtransformers（bf16、trust_remote_code=True）。READMEは変換時にeos_token_idを120020にするよう注意を促している（3だと生成が止まらない）。
- **制約**: 対象は日本語→英語のみ。漫画向けの短い1行単位の翻訳に特化し、切り詰められた入力を補完してしまう傾向、実在の固有名詞や専門用語が弱い、ページ文脈を見ない、出力がv4より約7%長い、といった制約を作者が明記。
- **利用条件**: Apache-2.0（baseモデル tencent/Hy-MT2-1.8B に準拠）。
- **編集者評価**: 漫画の吹き出し単位の日英翻訳をローカル（スマホ含む）で回せる専門モデルで、翻訳ツールのバックエンドとして試す価値がある。
- **次の検証（未実施）**: 実際の漫画ページでv5とv4を比較し、固有名詞・擬音・吹き出し内の文字数に収まるかを確認する。

確認日: 2026-10-01 / revision `e17bc6a8dd92ddf930bd7858ceb916117ee5f916` / gated=False。ファイル名候補2件の一覧確認。代表ファイル: `manga-v5-Q4_K_M.gguf`、`model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/fumetodev/Hy-MT2-1.8B-JP-Manga-Finetune-v5-GGUF/blob/e17bc6a8dd92ddf930bd7858ceb916117ee5f916/README.md) / [モデルAPI](https://huggingface.co/api/models/fumetodev/Hy-MT2-1.8B-JP-Manga-Finetune-v5-GGUF)
