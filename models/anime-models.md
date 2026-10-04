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

## Illustrious-XL-v2.0

アニメ特化のtext-to-imageモデル(ヴェースはSDXL系)。公式のv2系チェックポイントを公開している。

- **版の区別**: 単一safetensors(Illustrious-XL-v2.0.safetensors)を配布。コサインアニーリング後半のより安定したチェックポイントとの説明がある。
- **入力・設定**: モデルカードにプロンプト例や推奨設定・品質タグの記載はない。
- **必要構成**: カードに必要環境の記載はない。SDXL系の推論環境が前提。
- **制約**: モデルカードの記述が短く、学習データ・評価・推奨解像度は不明。
- **利用条件**: licenseはcreativeml-openrail-m。
- **編集者評価**: アニメ画像生成で広く派生している系統の公式版で、既存のアニメ系モデルと比較する基準として押さえる価値がある。
- **次の検証（未実施）**: 同一プロンプトで他のアニメ系SDXLと品質・構図追従・タグ反応を比較する。

確認日: 2026-09-30 / revision `69459c1fe6f46db41ab31e6114f05acc0e06bcaa` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `Illustrious-XL-v2.0.safetensors`

根拠: [固定モデルカード](https://huggingface.co/OnomaAIResearch/Illustrious-XL-v2.0/blob/69459c1fe6f46db41ab31e6114f05acc0e06bcaa/README.md) / [モデルAPI](https://huggingface.co/api/models/OnomaAIResearch/Illustrious-XL-v2.0)

## HDM-xut-340M-anime

独自バックボーンXUT(Cross-U-Transformer)を用いる約340Mのアニメ向けtext-to-imageベース。TREAD併用で家庭用ハード/格安サーバでの学習を狙う。

- **版の区別**: 512px/768px/1024pxの重み、diffusersフォルダ、学習用ckptを配布。解像度別にファイルが分かれる。
- **入力・設定**: カードはタグ/自然文の使い分けに触れていない。学習データはPixivとdanbooru系。
- **必要構成**: diffusersで実行可能。学習は民生クラスのGPU/格安サーバ想定と記載。
- **制約**: 「世界最小・最安のアニメ調T2Iベース」を掲げる小規模モデルで、ベースとしての品質は限定的と考えられる。
- **利用条件**: licenseはcc(具体的なCC種別はカードに明記されていない)。
- **編集者評価**: 低VRAM・低コストで回せるアニメ画像ベースとして、学習レシピ検証の土台になる。
- **次の検証（未実施）**: 512/768/1024px各重みで同一プロンプトを生成し、VRAM・速度・品質の差を記録する。

確認日: 2026-09-30 / revision `7c9e455a9722811bd9eec7eb38b4c8712a7ef290` / gated=False。ファイル名候補9件の一覧確認。代表ファイル: `hdm-xut-340M-1024px-note.safetensors`、`hdm-xut-340M-512px-note.safetensors`、`hdm-xut-340M-768px-note.safetensors`、`text_encoder/model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/KBlueLeaf/HDM-xut-340M-anime/blob/7c9e455a9722811bd9eec7eb38b4c8712a7ef290/README.md) / [モデルAPI](https://huggingface.co/api/models/KBlueLeaf/HDM-xut-340M-anime)

## anime-painter

SDXLベースのscribble ControlNet。ラフな線画からアニメ調画像を生成する。

- **版の区別**: diffusion_pytorch_model.safetensorsの1ファイル。アニメ系SDXLベースモデルと組み合わせて使う。
- **入力・設定**: danbooruタグで被写体を、自然文で状況を記述する併用を推奨。線の太さや種類を問わず対応すると記載。
- **必要構成**: diffusersのControlNetパイプライン。別途アニメ系SDXLベースモデルが必要。
- **制約**: カードは性能を強く宣伝するが数値根拠は示していない。ライセンスはapache-2.0。
- **利用条件**: licenseはapache-2.0。
- **編集者評価**: ラフ・走り書きからアニメ絵を作る定番候補で、下書き〜清書工程に組み込みやすい。
- **次の検証（未実施）**: 自作ラフ数枚でタグ併用時の構図一致と破綻率を確認する。

確認日: 2026-09-30 / revision `18185a73b6e7fe49f2f2de1bb9d7db0b74a41773` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `diffusion_pytorch_model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/xinsir/anime-painter/blob/18185a73b6e7fe49f2f2de1bb9d7db0b74a41773/README.md) / [モデルAPI](https://huggingface.co/api/models/xinsir/anime-painter)

## Galgame-Llasa-3B

Llasa-3B(HKUSTAudio)をベースに、ギャルゲー音声データセットで日本語向けに微調整したTTSモデル。

- **版の区別**: 3Bの重み(2シャード)。デモSpaceあり。1B/8Bなど姉妹サイズも別リポジトリで公開されている。
- **入力・設定**: カードにプロンプト仕様や話者指定の記載はない。
- **必要構成**: カードに必要環境や推論コードの記載はない。
- **制約**: モデルカードは概要のみで、評価・使い方の詳細がない。日本語のみ。
- **利用条件**: licenseはCC-BY-NC-4.0(非商用)。
- **編集者評価**: ギャルゲー調のキャラ音声生成の候補として、既存の日本語TTSと比較する余地がある。
- **次の検証（未実施）**: 同一台本で既存の日本語TTSと聞き比べ、感情表現・安定性・速度を確認する。

確認日: 2026-09-30 / revision `23134f66585fe17c0e72bdeb737c9f71bb89d0db` / gated=False。ファイル名候補3件の一覧確認。代表ファイル: `model-00001-of-00002.safetensors`、`model-00002-of-00002.safetensors`、`training_args.bin`

根拠: [固定モデルカード](https://huggingface.co/OmniAICreator/Galgame-Llasa-3B/blob/23134f66585fe17c0e72bdeb737c9f71bb89d0db/README.md) / [モデルAPI](https://huggingface.co/api/models/OmniAICreator/Galgame-Llasa-3B)

## Audio2Face-3D-v3.0

Hubert系エンコーダと拡散機構を組み合わせ、音声から3D顔モーション(肌・舌・顎・眼球)を生成する約1.8億パラメータのモデル。

- **版の区別**: ONNX(network.onnx)を配布。Audio2Face-SDK経由で利用し、TensorRTで高速化する。
- **入力・設定**: プロンプトではなく、16kHzにリサンプルした音声と感情ラベルを入力にする。
- **必要構成**: NVIDIA GPU、TensorRT/Audio2Face-SDK。OSはLinux/Windows。Ampere〜Blackwell等に対応。
- **制約**: 低品質音声では口形が不正確になり得るとカードが明記。アニメ特化ではなく写実的な3Dアバター向け。性能指標は口形精度・レイテンシ・スループット。
- **利用条件**: license_nameはnvidia-open-model-license。カードは商用/非商用利用可と記載。
- **編集者評価**: 3Dアバターのリップシンク生成を自前パイプラインへ組み込む部品として有用。
- **次の検証（未実施）**: 手持ち音声で口形精度とレイテンシを計測し、VRM等のアバターへの適用可否を確認する。

確認日: 2026-09-30 / revision `b74132732fd9a9d29b237bec193ded64c9745e91` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `network.onnx`

根拠: [固定モデルカード](https://huggingface.co/nvidia/Audio2Face-3D-v3.0/blob/b74132732fd9a9d29b237bec193ded64c9745e91/README.md) / [モデルAPI](https://huggingface.co/api/models/nvidia/Audio2Face-3D-v3.0)

## IndexTTS-2.5

GPTバックボーン＋フローマッチングの音声-to-メルデコーダ＋BigVGANボコーダで構成される自己回帰ゼロショットTTS。GPTバックボーンは約0.8B。出力は22.05kHz。

- **版の区別**: リポジトリ直下がフル精度重み（codec.pth、gpt.pth、s2mel.pth、qwen0.6bemo4-merge 等）。補助モデル(w2v-bert-2.0、MaskGCTセマンティックコーデック、CAMPPlus、BigVGAN)は同梱されず初回実行時にhf_cacheへ自動取得される。量子化版の記載はない。
- **入力・設定**: 参照音声1本で話者をクローンし、langで言語(EN/ZH/JA/ES/AR)を指定。8要素の感情ベクトル[happy, angry, sad, afraid, disgusted, melancholic, surprised, calm]で感情を制御でき、<word|reading>で読み（Pinyin/CMU/Kana）、duration_factor(0.5〜2.0)で話速を調整する。
- **必要構成**: Python 3.10〜3.11、NVIDIA GPU、推論におよそ6GBのVRAM。uvでセットアップし、webui.pyも用意される。
- **制約**: 長文は分割して無音を挟んで連結するため、セグメント境界をまたぐ韻律は扱わない。テキスト記述からの感情制御にはQwenEmotionモデルが必要で、use_qwen_emo=True時のみ読み込まれる。参照話者の同意確認は利用者の責任と明記。
- **利用条件**: licenseはother、license_nameはbilibili-model-license。公開重みを無条件の商用可として扱わない。
- **編集者評価**: 日本語を含む多言語のゼロショット声質クローンと、声質から切り離した感情制御を備え、キャラクター音声制作の候補になる。アニメ特化モデルではなく汎用のTTS。
- **次の検証（未実施）**: 同一の参照音声でIndexTTS-2と比較し、推論速度・感情ベクトルの追従・日本語の読みと句読点処理を記録する。

確認日: 2026-10-01 / revision `c39ce5ba981572cb187443877ff559dfb246ce63` / gated=False。ファイル名候補7件の一覧確認。代表ファイル: `codec.pth`、`feat1.pt`、`feat2.pt`、`gpt.pth`

根拠: [固定モデルカード](https://huggingface.co/IndexTeam/IndexTTS-2.5/blob/c39ce5ba981572cb187443877ff559dfb246ce63/README.md) / [モデルAPI](https://huggingface.co/api/models/IndexTeam/IndexTTS-2.5)

## Qwen2D-Anime-VAE

Qwen Image VAE(非テンポラル版)のデコーダを調整したVAE。ComfyUI用ノードパック(anzhc-qwen2d-comfyui)から使用する。

- **版の区別**: Qwen2D-Anime-dense-440k_ema_epoch_1.safetensors と Qwen2D-Anime-dense_epoch_1.safetensors の2ファイル。
- **入力・設定**: モデルカードにプロンプト記述はなく、対応ワークフローのVAEを差し替えて使う想定。カードの説明は過剰シャープの軽減、瞳など小さい要素の改善、ノイズ低減という位置づけ。
- **必要構成**: カードに必要環境・VRAMの記載はない。ComfyUI用ノードパックの導入が必要。
- **制約**: デコーダ調整のみで、カードには解像度・再現手順・比較条件の記載が少ない。効果は作者の比較画像に基づくもので、数値評価は無い。
- **利用条件**: apache-2.0。
- **編集者評価**: Qwen Image系のアニメ絵ワークフローで、過剰シャープや小物（瞳など）の破綻を抑える狙いのVAE候補。
- **次の検証（未実施）**: 同一シード・同一プロンプトで標準VAEと差し替え比較し、瞳や細部、全体のノイズ感の差を確認する。

確認日: 2026-10-01 / revision `d59c106b50524909ac660cd97a32fdf49b2f8f21` / gated=False。ファイル名候補2件の一覧確認。代表ファイル: `Qwen2D-Anime-dense-440k_ema_epoch_1.safetensors`、`Qwen2D-Anime-dense_epoch_1.safetensors`

根拠: [固定モデルカード](https://huggingface.co/Anzhc/Qwen2D-Anime-VAE/blob/d59c106b50524909ac660cd97a32fdf49b2f8f21/README.md) / [モデルAPI](https://huggingface.co/api/models/Anzhc/Qwen2D-Anime-VAE)

## ml-danbooru-onnx

ML-DanbooruのONNX変換版。Caformer-M36（畳み込み＋Transformer）とTResnet-D系の画像分類モデルで、Danbooru系タグを推定する。

- **版の区別**: 主モデルはml_caformer_m36_dec-5-97527.onnx。他にml_caformer_m36_dec-3-80000.onnx、caformer_m36-3-80000.onnx、TResnet-D-FLq系が複数。classes.json（簡易タグ1527件）とtags.csv（12547件）を同梱する。
- **入力・設定**: プロンプトではなく、dghs-imgutilsのget_mldanbooru_tagsに画像を渡す。threshold(既定0.7)・size(既定448)・keep_ratio・drop_overlapなどを指定してタグを得る。
- **必要構成**: pip install dghs-imgutils。ONNXランタイム上で動作。既定入力は448x448。
- **制約**: 2023年公開のモデルで、タグ体系は当時のDanbooruに準拠する。カードに精度の数値は記載されておらず、近年の作風やタグ語彙への追随は未確認。
- **利用条件**: mit。
- **編集者評価**: 手持ちイラストの自動タグ付けに使え、学習用データセット整備やキャラ・属性の下ごしらえに向く。
- **次の検証（未実施）**: 対象イラストでthresholdを変えてタグの妥当性を確認し、日本語のキャラ名や作品名がどの程度拾えるかを測る。

確認日: 2026-10-01 / revision `eb9058324a741f1b90d4db168f6e1d6b6cb7e63d` / gated=False。ファイル名候補7件の一覧確認。代表ファイル: `TResnet-D-FLq_ema_2-40000.onnx`、`TResnet-D-FLq_ema_4-10000.onnx`、`TResnet-D-FLq_ema_6-10000.onnx`、`TResnet-D-FLq_ema_6-30000.onnx`

根拠: [固定モデルカード](https://huggingface.co/deepghs/ml-danbooru-onnx/blob/eb9058324a741f1b90d4db168f6e1d6b6cb7e63d/README.md) / [モデルAPI](https://huggingface.co/api/models/deepghs/ml-danbooru-onnx)

## Irodori-TTS-500M-v2-Character-Voice-Tagger

Aratako/Irodori-TTS-500M-v2をベースに、SmilingWolf/wd-vit-tagger-v3を画像エンコーダとして条件付けに加えた日本語TTS。参照音声や声色キャプションの代わりにキャラクター画像の特徴を使い、ゼロショットでキャラの雰囲気に合う声を合成する。

- **版の区別**: Character Voice系は画像エンコーダ違いの2系統で、本モデルはTagger（wd-vit-tagger-v3）版、姉妹のSigLIP版はSigLIP-v2-B/16-512を使う。重みはmodel.safetensorsの1ファイル。
- **入力・設定**: 入力は日本語テキストとキャラクター画像。GitHubのCLIでは--hf-checkpoint p1atdev/Irodori-TTS-500M-v2-Character-Voice-Tagger と --character-image を指定する。カードにプロンプト文面やキャプション指定の記載はない。
- **必要構成**: 推論コード・インストール手順・CLI例はGitHubのp1atdev/Irodori-Character-Voice側。GradioデモSpaceも公開されている。モデルは約500M。必要VRAMや生成速度はカードに記載がない。
- **制約**: 日本語のみ。話者類似度・表現力の定量評価はカードになく、arXivはcoming soon。同じキャラ画像でも出力が安定するかは未確認。学習データの詳細も非公開。
- **利用条件**: MIT。ベースのIrodori-TTS-500M-v2および画像エンコーダ（Apache系）の条件は別途確認が必要。
- **編集者評価**: 参照音声を用意せずにキャラ絵から声を決められるため、キャラボイスの試作やキャスト当ての検討に向く。
- **次の検証（未実施）**: 同一テキストでキャラ画像だけを差し替え、声色の差と同一画像での再現性を比較する。

確認日: 2026-10-02 / revision `3fe62991c9e86d275a57e879ba62cff85c8cf18a` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/p1atdev/Irodori-TTS-500M-v2-Character-Voice-Tagger/blob/3fe62991c9e86d275a57e879ba62cff85c8cf18a/README.md) / [モデルAPI](https://huggingface.co/api/models/p1atdev/Irodori-TTS-500M-v2-Character-Voice-Tagger)

## Irodori-TTS-500M-v2-Character-Voice-SigLIP

Aratako/Irodori-TTS-500M-v2をベースに、timm/vit_base_patch16_siglip_512.v2_webliを画像エンコーダとして使う日本語TTS。キャラクター画像を条件に話者スタイルを制御する。

- **版の区別**: Character Voice系の画像エンコーダ違い2系統のうち本モデルがSigLIP版、姉妹のTagger版はwd-vit-tagger-v3を使う。重みはmodel.safetensorsの1ファイル。
- **入力・設定**: 日本語テキストとキャラクター画像を入力する。GitHubのCLIでは--hf-checkpoint p1atdev/Irodori-TTS-500M-v2-Character-Voice-SigLIP と --character-image を指定。キャプション指定の記載はない。
- **必要構成**: GitHubのp1atdev/Irodori-Character-Voiceの推論コードとデモSpaceを使用。モデルは約500M。VRAM要件はカードに記載がない。
- **制約**: 日本語のみ。Tagger版との品質差や使い分けはカードに記載がなく、定量評価も未掲載。
- **利用条件**: MIT。ベースモデルと画像エンコーダ側の条件は別途確認が必要。
- **編集者評価**: 同じ発想を別の画像エンコーダで実装した比較対象で、用途に応じてTagger版と聴き比べる価値がある。
- **次の検証（未実施）**: Tagger版と同じテキスト・同じ画像で生成し、声色と安定性を聴き比べる。

確認日: 2026-10-02 / revision `b5954e439b7b1a4a452d56ec6a15e079be56c99f` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/p1atdev/Irodori-TTS-500M-v2-Character-Voice-SigLIP/blob/b5954e439b7b1a4a452d56ec6a15e079be56c99f/README.md) / [モデルAPI](https://huggingface.co/api/models/p1atdev/Irodori-TTS-500M-v2-Character-Voice-SigLIP)

## Irodori-TTS-500M-v2-VoiceDesign

約500MのRectified Flow Diffusion Transformer（RF-DiT）による日本語TTS。v2系の参照音声エンコーダをキャプションエンコーダに置き換え、話者・感情・話し方をテキスト記述だけで設計できる。音声はSemantic-DACVAE-Japanese-32dimの32次元潜在で48kHz再構成。

- **版の区別**: VoiceDesign版として単一のmodel.safetensorsを配布。推論用のGradioデモSpaceがあり、mlx-communityによる量子化版も別途存在する。
- **入力・設定**: 台詞テキストと、「低い声の女性が苛立ちを隠せず焦って話す」のようなキャプションを指定する。テキスト中に絵文字を埋め込むと間・感情・効果音を追加制御でき、EMOJI_ANNOTATIONS.mdに一覧がある。
- **必要構成**: GitHubのAratako/Irodori-TTSの推論コードとデモSpaceを使用。必要VRAMや速度はカードに記載がない。
- **制約**: 日本語のみ。複雑または矛盾したキャプションでは声が不安定になる。漢字の読みが弱く、事前にひらがな・カタカナ化が必要な場合がある。絵文字制御は常に一貫しない。
- **利用条件**: MIT。加えて、実在人物の声の模倣や誤情報生成を禁じる倫理制限がカードに明記されている。キャプションには話者名は含まれない。
- **編集者評価**: 参照音声なしでキャラの声色と演技を言語で指定できるため、キャラ音声の設計・試作に向く。実在の声優の声を再現する用途は想定されていない。
- **次の検証（未実施）**: 同じ台詞でキャプションの記述だけを変え、声色・感情・話速の変化を確認する。

確認日: 2026-10-02 / revision `456e55708e7183f5c7faa1448209d54aa8991451` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/Aratako/Irodori-TTS-500M-v2-VoiceDesign/blob/456e55708e7183f5c7faa1448209d54aa8991451/README.md) / [モデルAPI](https://huggingface.co/api/models/Aratako/Irodori-TTS-500M-v2-VoiceDesign)

## anime-censorship-tagger-mnv3-384

MobileNetV3-Large（約4.2M）をEVA-02-Large教師から蒸留したONNX分類器。384×384のsquash入力を共有し、censored／bar／mosaicを独立シグモイドで出力する。

- **版の区別**: 配布は17MBのmodel.onnxと、infer.py・censor_infer_core.py・config.json・selected_tags.csv等の同梱スクリプト一式。
- **入力・設定**: プロンプトは使わない。カード記載の前処理（384×384へsquash、/255、(x-0.5)/0.5）と閾値（censored 0.47、bar 0.59、mosaic 0.53）を厳密に適用する必要があり、単純なsigmoid>0.5では誤る。
- **必要構成**: onnxruntimeとnumpy・Pillow。CPUでも動作し、バッチ推論の実装例も同梱されている。
- **制約**: アニメ・イラスト限定で写真や実写、AI生成画像では精度が落ちる。JPEG-q95前提のため圧縮条件が違うと分布外。ineffectiveヘッドは品質不足で無効化済み。判定は人手確認の代替ではなく、閾値は自前データで調整が必要と明記。
- **利用条件**: Apache-2.0（教師モデルwd-eva02-large-tagger-v3とバックボーンtimmもApache-2.0）。再配布時は帰属表示が必要。
- **編集者評価**: 学習データや納品物のフィルタリングを軽量に自動化できる検出専用モデルで、生成・改変は行わない。パイプラインへはほぼ追加コストなしで組み込める。
- **次の検証（未実施）**: 手元のデータセットに適用して閾値の妥当性と誤検出傾向を確認する。

確認日: 2026-10-02 / revision `b6c017a5c9ee4273f27db51b0fe96956184ffa0e` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `model.onnx`

根拠: [固定モデルカード](https://huggingface.co/Maltox/anime-censorship-tagger-mnv3-384/blob/b6c017a5c9ee4273f27db51b0fe96956184ffa0e/README.md) / [モデルAPI](https://huggingface.co/api/models/Maltox/anime-censorship-tagger-mnv3-384)

## asmr-trigger-audio-h3-lora

MiniMaxAI/MiniMax-H3をベースにしたLoRAアダプタ。囁き系ASMRの音響と、それに対応する映像（T2V/I2V）を生成する。

- **版の区別**: 配布はasmr_trigger_audio_h3_lora_v1_500.safetensorsの1ファイル（step500）。他のチェックポイントはカードに記載がない。
- **入力・設定**: 「she is holding mic in one hand, she leans her head close to the mic and whispers: '...'」のようなプロンプトを推奨。解像度720x1280、weight 0.6〜0.8、20〜30ステップ、9:16で30ステップが最適と記載されている。
- **必要構成**: MiniMax H3の推論環境。カードにはVRAM要件や実行手順の記載がない。
- **制約**: カードは設定値とデモ動画のみで、音質評価・多言語対応・失敗例の記載がない。特定話者の声を再現する設計ではなく、ベースモデル側の制約も受ける。
- **利用条件**: Apache-2.0。ベースのMiniMax H3およびその他アダプタの条件は別途確認が必要。
- **編集者評価**: 囁きASMRの音声つき映像を狙って調整されたLoRAで、ASMR作品の試作に使いやすい。
- **次の検証（未実施）**: 推奨設定で短文を生成し、囁きの明瞭度・音量・映像との同期を確認する。

確認日: 2026-10-02 / revision `9369cad86bc549caa9e0d8f6f1c812aad4fc2e33` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `asmr_trigger_audio_h3_lora_v1_500.safetensors`

根拠: [固定モデルカード](https://huggingface.co/vpakarinen/asmr-trigger-audio-h3-lora/blob/9369cad86bc549caa9e0d8f6f1c812aad4fc2e33/README.md) / [モデルAPI](https://huggingface.co/api/models/vpakarinen/asmr-trigger-audio-h3-lora)

## Galgame-Llasa-3B-v3

HKUSTAudio/Llasa-3Bを基に、ギャルゲー系の日本語音声データで微調整した日本語テキスト音声合成モデル。

- **版の区別**: 3B版にはv1/v2/v3があり、本項目はv3。v3は学習時のテキスト正規化を変更し一貫性を改善したと記載。1B版も別途公開されている。
- **入力・設定**: 日本語テキストを入力する。詳細なプロンプト書式はモデルカードに記載がない。
- **必要構成**: Llasa系列の推論環境が必要。具体的なVRAM要件はモデルカードに記載がない。3BのデモがHugging Face Spacesで公開されている。
- **制約**: cc-by-nc-4.0で商用利用は不可。日本語のみを対象とする。話者・感情制御の仕様はカードに記載がない。
- **利用条件**: metadataのlicenseはcc-by-nc-4.0。商用利用は不可として扱う。
- **編集者評価**: ギャルゲー/アニメ調の日本語音声合成をローカルで試す候補。既存の3B（v1）とは別のv3チェックポイント。
- **次の検証（未実施）**: 公開デモと同じテキストで3B-v3と1B-v3を比較し、読みと韻律・速度を記録する。

確認日: 2026-10-03 / revision `880454ae1697e6a397df39c7bdc0d16a3b21d543` / gated=False。ファイル名候補3件の一覧確認。代表ファイル: `model-00001-of-00003.safetensors`、`model-00002-of-00003.safetensors`、`model-00003-of-00003.safetensors`

根拠: [固定モデルカード](https://huggingface.co/OmniAICreator/Galgame-Llasa-3B-v3/blob/880454ae1697e6a397df39c7bdc0d16a3b21d543/README.md) / [モデルAPI](https://huggingface.co/api/models/OmniAICreator/Galgame-Llasa-3B-v3)

## Galgame-Llasa-1B-v3

HKUSTAudio/Llasa-1B-Multilingualを基に、ギャルゲー音声や日本語アニメ音声データで微調整した日本語テキスト音声合成モデル。

- **版の区別**: 1B版にはv1/v2/v3があり、本項目はv3。学習データにEmilia・ehehe-corpus・japanese-anime-speech等を追加したと記載。3B版も別途公開されている。
- **入力・設定**: 日本語テキストを入力する。詳細なプロンプト書式はモデルカードに記載がない。
- **必要構成**: Llasa系列の推論環境が必要。具体的なVRAM要件はモデルカードに記載がない。
- **制約**: cc-by-nc-4.0で商用利用は不可。日本語のみを対象とする。話者・感情制御の仕様はカードに記載がない。
- **利用条件**: metadataのlicenseはcc-by-nc-4.0。商用利用は不可として扱う。
- **編集者評価**: 軽量な1Bクラスで日本語キャラ音声を作る候補。3B版より小さいぶん試しやすい。
- **次の検証（未実施）**: 1B-v3と3B-v3で同一台詞を合成し、品質と速度の差を確認する。

確認日: 2026-10-03 / revision `e3f797a5a51bf6811e28b6e2be8650dba7322aa3` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/OmniAICreator/Galgame-Llasa-1B-v3/blob/e3f797a5a51bf6811e28b6e2be8650dba7322aa3/README.md) / [モデルAPI](https://huggingface.co/api/models/OmniAICreator/Galgame-Llasa-1B-v3)

## Manga-Bubble-YOLO

Manga109-sとMangadex由来画像で学習したYOLO26ベースのテキスト領域検出モデル。NMS不要のend-to-endヘッドを持つ。

- **版の区別**: yolo26nとyolo26sのPyTorch(.pt)とONNXを同梱。学習は英語・ベトナム語・日本語の混合データ（5,595画像）。
- **入力・設定**: 該当なし（検出モデル）。imgsz=1280、conf=0.25を推奨と記載。
- **必要構成**: ultralytics、またはONNX Runtime。推論はT4でn約11.0ms/画像、s約27.5ms/画像と記載。
- **制約**: データセットは著作権の都合で非公開。検出対象はテキスト領域/吹き出しに限る。
- **利用条件**: カード表記のlicenseはapache-2.0。学習元データのManga109-sには別途利用条件がある。
- **編集者評価**: 漫画翻訳パイプラインの吹き出し検出前段に組み込める軽量モデル。
- **次の検証（未実施）**: 実ページでnとsの再現率・誤検出を比較し、OCR前段としての実用性を確認する。

確認日: 2026-10-03 / revision `fb646500455e8a8a3a807fd27b855c8e4fc63766` / gated=False。ファイル名候補4件の一覧確認。代表ファイル: `onnx/yolo26n.onnx`、`onnx/yolo26s.onnx`、`weights/yolo26n.pt`、`weights/yolo26s.pt`

根拠: [固定モデルカード](https://huggingface.co/Kiuyha/Manga-Bubble-YOLO/blob/fb646500455e8a8a3a807fd27b855c8e4fc63766/README.md) / [モデルAPI](https://huggingface.co/api/models/Kiuyha/Manga-Bubble-YOLO)

## MiniMax-H3-Rough-2D-Cartoon-Illustration

MiniMax-H3をベースに、2Dカートゥーン風の動的イラスト動画データで学習したLoRAアダプタ。

- **版の区別**: チェックポイント1000/1200を推奨と記載。リポジトリには1000/1200のsafetensorsが置かれている。
- **入力・設定**: トリガーワード「rough 2D cartoon illustration」を用いる。
- **必要構成**: MiniMax-H3の推論環境。解像度は既定480x832で、映像フレーム数に応じて調整されると記載。
- **制約**: 作者が実験的でアーティファクトが出ると明記。学習データはPexelsの動画を素材にしている。
- **利用条件**: metadataはother、license_nameはminimax-h3-community-license。ベースモデルの条件に従う。
- **編集者評価**: 2Dカートゥーン調の動きを付与する実験的LoRA。既存のMiniMax-H3系項目とは別のスタイル。
- **次の検証（未実施）**: 同一シードでベースと比較し、動きの自由度と破綻の程度を確認する。

確認日: 2026-10-03 / revision `fc40d010a2b44fd4caa4b750b6f503eca5d61577` / gated=False。ファイル名候補2件の一覧確認。代表ファイル: `1000/minimax-h3-rough-2d-cartoon-illustration-1000.safetensors`、`minimax-h3-rough-2d-cartoon-illustration-1200.safetensors`

根拠: [固定モデルカード](https://huggingface.co/prithivMLmods/MiniMax-H3-Rough-2D-Cartoon-Illustration/blob/fc40d010a2b44fd4caa4b750b6f503eca5d61577/README.md) / [モデルAPI](https://huggingface.co/api/models/prithivMLmods/MiniMax-H3-Rough-2D-Cartoon-Illustration)

## AnimeBackgroundGAN-Shinkai

CartoonGAN（Chen et al., CVPR18）の新海誠スタイル学習済みモデル。PyTorch実装で重みを配布する。

- **版の区別**: 新海誠版のほか、細田守・今敏・宮崎駿版が別リポジトリで公開されている。重みは単一の.pthファイル。
- **入力・設定**: 該当なし（画像変換モデル）。実写写真を入力する。
- **必要構成**: PyTorch。README記載のTransform実装で読み込む。
- **制約**: 2022年公開のモデルで、実写写真をアニメ風背景へ変換する用途。最新の生成モデルに比べ表現力は限定的。
- **利用条件**: metadataのlicenseはmit。
- **編集者評価**: 実写写真から新海誠風の背景を作る古典的GANとして参照価値がある。
- **次の検証（未実施）**: 実写風景写真で変換し、背景素材として使える品質かを目視確認する。

確認日: 2026-10-03 / revision `d162ca947aab5aa943c3586bda550812831d5cf4` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `shinkai_makoto.pth`

根拠: [固定モデルカード](https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Shinkai/blob/d162ca947aab5aa943c3586bda550812831d5cf4/README.md) / [モデルAPI](https://huggingface.co/api/models/akiyamasho/AnimeBackgroundGAN-Shinkai)

## CharacterSheet

画像編集ベースのLoRA群。FLUX.2 Klein 9BとKrea 2向けに、参照キャラ画像からマルチビューのキャラクターシートを生成する。学習は約300例のキャラクターシートで、人間キャラ中心。

- **版の区別**: TripleView_klein9b（前/横/後）、QuadView_klein9b（顔クローズアップ追加）、QuadView_krea2、DynamicCharacterSheet_krea2（実験的）の計4ファイル。各ファイルで対応ベースモデルと同梱ワークフローJSONが異なる。
- **入力・設定**: レイアウトごとの定型キャプション（例: "Convert the character in the image to a Character Sheet showing front, side and back full body views"）を使う。Dynamic版は構造化ブラケットプロンプトが必要で、同梱のQwen3-VLノードで生成するのが推奨。
- **必要構成**: ComfyUI。LoRAをmodels/lorasへ配置し、同梱のworkflow JSONを開いて使用。既定は1536×1024・8〜10ステップ・CFG1。
- **制約**: 学習例は約300で人間キャラ中心のため、アニメ等の様式では一貫性が落ちる場合がある。Dynamic版はシート内文字の生成が未成熟で、ビュー間の一貫性も100%ではない。
- **利用条件**: metadataはother、license_nameはcivitai-model-license、license_linkはcivitai。無条件の商用利用可とは扱わない。
- **編集者評価**: 1枚のキャラ画像からターンアラウンドや資料シートを作る用途が具体的で、キャラ設定資料やデータセット準備に向く。
- **次の検証（未実施）**: アニメ調の参照画像でTripleView/QuadViewを回し、ビュー間の同一性・衣装保持・解像度別の破綻を確認する。

確認日: 2026-10-04 / revision `3dc4295163dacc924d213168d67bf16850fd954f` / gated=False。ファイル名候補4件の一覧確認。代表ファイル: `DynamicCharacterSheet_krea2_v1.safetensors`、`QuadView_klein9b_v1.safetensors`、`QuadView_krea2_v1.safetensors`、`TripleView_klein9b_v1.safetensors`

根拠: [固定モデルカード](https://huggingface.co/Alissonerdx/CharacterSheet/blob/3dc4295163dacc924d213168d67bf16850fd954f/README.md) / [モデルAPI](https://huggingface.co/api/models/Alissonerdx/CharacterSheet)

## Live2Diff

単方向テンポラルアテンションとマルチタイムステップKVキャッシュを用いた動画拡散モデル（Stable Diffusion系）。リアルタイムのストリーム翻訳（video-to-video）を目的とし、LCM-LoRAとStreamDiffusionで高速化する。

- **版の区別**: live2diff.ckpt（ckpt形式の1ファイル）。
- **入力・設定**: モデルカードにプロンプト仕様の記載はない。デモではWebカメラ入力（人の顔）やアニメキャラ映像のリアルタイム変換例が示される。
- **必要構成**: PyTorch 2.2.2。RTX 4090での速度評価で、2ステップdenoising時512×512はTensorRT有効で16.43FPS。TensorRT対応。
- **制約**: モデルカードは性能・制約の詳細を記述していない。リアルタイム実行にはWebカメラ等の入力と相応のGPUが必要。
- **利用条件**: Apache-2.0。
- **編集者評価**: 映像をリアルタイムにアニメ調へ変換でき、配信やVTuber的な映像演出の実験に向く。
- **次の検証（未実施）**: 入力映像を用意し、TensorRT有無でのFPS・構造一貫性・スタイルの安定性を比較する。

確認日: 2026-10-04 / revision `0e6801b3e805e37a6e27f99aa9e8ee6574d748c6` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `live2diff.ckpt`

根拠: [固定モデルカード](https://huggingface.co/Leoxing/Live2Diff/blob/0e6801b3e805e37a6e27f99aa9e8ee6574d748c6/README.md) / [モデルAPI](https://huggingface.co/api/models/Leoxing/Live2Diff)

## japanese_speecht5_tts

microsoft/speecht5_ttsをベースに、Open JTalk（pyopenjtalk）ベースの改修トークナイザを組み合わせた日本語TTS。JVSコーパス（100話者）でファインチューニングしている。

- **版の区別**: model.safetensors（1ファイル）と、改修トークナイザのPythonコード（speecht5_openjtalk_tokenizer.py）。
- **入力・設定**: プロンプトではなく入力テキストを渡す。16次元の話者埋め込みで声質を制御し、第1次元が男性寄り（-1.0）〜女性寄り（1.0）を表す。
- **必要構成**: transformers、sentencepiece、pyopenjtalk。改修トークナイザをダウンロードして使用。vocoderはmicrosoft/speecht5_hifigan。
- **制約**: 複数文を一度に入力すると後半が長い無音になる既知問題があり、文単位での分割生成が推奨されている。
- **利用条件**: モデルカードのlicenseは未設定。JVS Corpusのライセンスを継承すると記載され、商用利用可否は明記されていない。
- **編集者評価**: 日本語の読み上げ音声を作る軽量な選択肢で、キャラ音声の下地づくりに使える。
- **次の検証（未実施）**: 同一テキストで話者埋め込みを振り、声質変化と複数文入力時の無音問題を確認する。

確認日: 2026-10-04 / revision `21d6e52032f74123966ac8a3717e23fdfb7809b0` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/esnya/japanese_speecht5_tts/blob/21d6e52032f74123966ac8a3717e23fdfb7809b0/README.md) / [モデルAPI](https://huggingface.co/api/models/esnya/japanese_speecht5_tts)

## noob-sdxl-controlnet-lineart_anime

Laxhar/sdxl_noob（NoobAI-XL）をベースにしたSDXL向けlineart ControlNet。pipeline_tagはtext-to-imageで、controlnet形式の重みを含む。

- **版の区別**: diffusion_pytorch_model.safetensors と diffusion_pytorch_model.fp16.safetensors（diffusers形式）、および noob-sdxl-controlnet-lineart_anime.safetensors。
- **入力・設定**: モデルカードにプロンプト例・推奨設定の記載はない。
- **必要構成**: diffusersまたは対応するWebUI。fp16版が同梱。必要VRAMや推奨解像度はカードに記載がない。
- **制約**: モデルカードは記述がほぼ無く、性能・制約・推奨パラメータは不明。利用条件はFair AI Public License 1.0-SD。
- **利用条件**: metadataはother、license_nameはfair-ai-public-license-1.0-sd、license_linkはfreedevproject.org。無条件の商用利用可とは扱わない。
- **編集者評価**: アニメ調イラストの線画制御に使えるNoobAI系ControlNetで、既存のSDXLワークフローへ組み込みやすい。
- **次の検証（未実施）**: 線画を入力に、NoobAI-XL系チェックポイントと組み合わせて塗りの品質・構図保持・fp16精度の差を確認する。

確認日: 2026-10-04 / revision `61ed2d40710b32a5a1c9873f7dec89ff0af9f2a4` / gated=False。ファイル名候補3件の一覧確認。代表ファイル: `diffusion_pytorch_model.fp16.safetensors`、`diffusion_pytorch_model.safetensors`、`noob-sdxl-controlnet-lineart_anime.safetensors`

根拠: [固定モデルカード](https://huggingface.co/Eugeoter/noob-sdxl-controlnet-lineart_anime/blob/61ed2d40710b32a5a1c9873f7dec89ff0af9f2a4/README.md) / [モデルAPI](https://huggingface.co/api/models/Eugeoter/noob-sdxl-controlnet-lineart_anime)

## storyboard-sketch

SDXL Baseをベースに、60枚のグレースケール絵コンテスケッチとキャラクター肖像で学習したLoRA。21:9・16:9・1:1の比率を含む。

- **版の区別**: Storyboard_sketch.safetensors（1ファイル）。適用強度で抽象度と整合性が変わる。
- **入力・設定**: instance_promptは"storyboard sketch of"。強度1.0で最も抽象的、0.8で整合性が上がり、0.5でより詳細・写実寄りになる。
- **必要構成**: Stable Diffusion XL（diffusers）環境。21:9などの横長比率を想定。
- **制約**: 学習例は約60枚と小さく、作風はスケッチ調に限定される。ライセンスはotherで、ベースモデルの条件に従う。
- **利用条件**: metadataはother。ベースはstabilityai/stable-diffusion-xl-base-1.0。無条件の商用利用可とは扱わない。
- **編集者評価**: シーンやカット割りのラフスケッチを出す用途に向き、絵コンテ検討のたたき台づくりに使える。
- **次の検証（未実施）**: 同一カット指定で強度0.5/0.8/1.0を比較し、構図の読みやすさとプロンプト追従を確認する。

確認日: 2026-10-04 / revision `be328fecdfe3fb053a500376283013f34f99eebb` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `Storyboard_sketch.safetensors`

根拠: [固定モデルカード](https://huggingface.co/blink7630/storyboard-sketch/blob/be328fecdfe3fb053a500376283013f34f99eebb/README.md) / [モデルAPI](https://huggingface.co/api/models/blink7630/storyboard-sketch)
