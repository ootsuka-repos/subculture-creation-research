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

## visual_novel_tts

Style-Bert_VITS2をベースにした日本語TTSモデル。ビジュアルノベル（Senren*Banka、Café Stella and the Reaper's Butterflies、Riddle Joker等）のキャラ音声を対象に学習している。

- **版の区別**: 公開重みは visual_novel/visual_novel.safetensors の1件。対象キャラとしてムラサメ、茉子、芳乃、レナ、千咲、芦花、愛衣、栞那、ナツメ、希、涼音、あやせ、七海、羽月、茉優、小春が挙げられている。
- **入力・設定**: テキスト入力のみ（キャラ選択はモデル/話者単位）。Style-Bert_VITS2のAPIサーバ経由で他アプリと連携できると記載されている。
- **必要構成**: Style-Bert_VITS2の実行環境。詳細な導入手順はStyle-Bert_VITS2のリポジトリを参照する旨のみ記載。
- **制約**: 研究・個人利用のみで商用不可と明記。カードにはアクセント/感情制御の詳細や評価数値は無い。
- **利用条件**: licenseはcc-by-nc-4.0。READMEも研究目的・個人利用限定・商用不可と明記している。
- **編集者評価**: 特定のビジュアルノベルキャラ音声を再現する用途が具体的で、ノベル/二次創作の音声試作に使いやすい。
- **次の検証（未実施）**: 対象キャラの参照音声と比較し、読み上げの自然さ・固有名詞の読み・キャラらしさを確認する。

確認日: 2026-10-05 / revision `e66a75464838470fce23457b9c216a929420237d` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `visual_novel/visual_novel.safetensors`

根拠: [固定モデルカード](https://huggingface.co/spow12/visual_novel_tts/blob/e66a75464838470fce23457b9c216a929420237d/README.md) / [モデルAPI](https://huggingface.co/api/models/spow12/visual_novel_tts)

## Visual-novel-transcriptor

distil-whisper/distil-large-v2をファインチューニングした日本語ASR（Seq2Seq）。ビジュアルノベルの音声の文字起こしを目的とする。

- **版の区別**: 配布はmodel.safetensorsの1件。ベースはdistil-large-v2。関連として同作者のvisual_novel_ttsやChatWaifuが挙げられている。
- **入力・設定**: AutoProcessorでlanguage=\"ja\"、task=\"transcribe\"を指定する推論例が示されている。
- **必要構成**: transformers、librosa（16kHz）。カードにCUDA前提の記載がある。
- **制約**: 学習データにNSFWのビジュアルノベルが含まれると明記。評価数値は未記載。カードは現状は非商用のみと述べている。
- **利用条件**: metadata上のlicenseはnull。モデルカードは「現在は非商用利用のみ」と記載しており、商用可とは扱わない。
- **編集者評価**: ギャルゲー/ノベル音声の文字起こしに特化した軽量ASRとして、字幕・解析の下処理に使える。
- **次の検証（未実施）**: 自作のノベル音声でCERと誤変換傾向（固有名詞・非言語発話）を確認する。

確認日: 2026-10-05 / revision `0a51fa1107b6ef36276e33de5d5f6600012e85c8` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/spow12/Visual-novel-transcriptor/blob/0a51fa1107b6ef36276e33de5d5f6600012e85c8/README.md) / [モデルAPI](https://huggingface.co/api/models/spow12/Visual-novel-transcriptor)

## bg-visualnovel-v03

Anything-V3をベースにしたStable Diffusion系のテキストto画像モデル。ビジュアルノベル背景の生成を目的とする。

- **版の区別**: bg-visualnovel-v03（v3）。同名モデルのv02系列も存在する。diffusers形式の重み（unet/vae/text_encoder）を含む。
- **入力・設定**: 短いプロンプトでの背景生成を想定（例: \"a classroom\"、\"a hospital building, two trees\"、\"a street at night with nobody around\"）。
- **必要構成**: diffusersのStableDiffusionPipeline。例は512x512で、1920x1080も生成可能とのコメントがある（VRAM依存）。
- **制約**: 2022年公開の旧世代SDモデル。READMEは評価数値や厳密な解像度上限を明記していない。
- **利用条件**: licenseはcreativeml-openrail-m。商用利用や再配布は同ライセンスの制限を引き継ぐ条件付き。
- **編集者評価**: ノベル/ゲームの背景素材を少数プロンプトで量産する用途に合うが、旧世代モデルのため画質は要検証。
- **次の検証（未実施）**: 教室・街などの背景を同一条件で生成し、解像度・破綻・スタイルの安定性を比較する。

確認日: 2026-10-05 / revision `4fe98d1d8d6b0b518fe40023e1c5c06e171edaa6` / gated=False。ファイル名候補8件の一覧確認。代表ファイル: `safety_checker/model.safetensors`、`safety_checker/pytorch_model.bin`、`text_encoder/model.safetensors`、`text_encoder/pytorch_model.bin`

根拠: [固定モデルカード](https://huggingface.co/vinesmsuic/bg-visualnovel-v03/blob/4fe98d1d8d6b0b518fe40023e1c5c06e171edaa6/README.md) / [モデルAPI](https://huggingface.co/api/models/vinesmsuic/bg-visualnovel-v03)

## Manga109-panel-balloon-text-yolov26-segmentation

Ultralytics YOLO26sのインスタンスセグメンテーションモデル。frame/text/balloonの3クラスを検出・分割する。ベースはyolo26s-seg.pt。

- **版の区別**: best.pt と last.pt（約23.4MB、パラメータ約11.4M）。クラス順は 0:frame、1:text、2:balloon。
- **入力・設定**: テキストプロンプトではなく画像入力。推論例はimgsz=1280、conf=0.25、retina_masks=True。
- **必要構成**: ultralytics、pillow、opencv-python。学習データはMangaSegmentationとManga109_RegionLevelTextSegmentation。
- **制約**: OCR/翻訳モデルではなく可視領域の分割のみ。カードはOCR・読み順・翻訳品質は対象外と明記。データセットのライセンスは別途適用。
- **利用条件**: モデルリポジトリのlicenseはmit。ただし学習データ（Manga109系）のライセンス/アクセス条件は別途適用されると記載。
- **編集者評価**: 漫画翻訳パイプラインの領域検出（フレーム/吹き出し/テキスト）を担う部品として前処理の再利用価値が高い。
- **次の検証（未実施）**: 自作の漫画ページでクラス別マスク精度と、読み順・OCR前処理への効果を確認する。

確認日: 2026-10-05 / revision `3a860269ee0beb43ce9f31d82c7851441eb178ae` / gated=False。ファイル名候補2件の一覧確認。代表ファイル: `best.pt`、`last.pt`

根拠: [固定モデルカード](https://huggingface.co/ShadowB/Manga109-panel-balloon-text-yolov26-segmentation/blob/3a860269ee0beb43ce9f31d82c7851441eb178ae/README.md) / [モデルAPI](https://huggingface.co/api/models/ShadowB/Manga109-panel-balloon-text-yolov26-segmentation)

## controlnet-lineart-anime-sdxl-fp16

SDXL用のControlNet（lineart、anime向け）。fp16のdiffusion_pytorch_modelを配布する。

- **版の区別**: 配布はdiffusion_pytorch_model.fp16.safetensorsの1件（variant=fp16）。
- **入力・設定**: ControlNetModel.from_pretrainedでvariant=fp16を指定して読み込む例のみが示される。プロンプト指示の記載は薄い。
- **必要構成**: diffusersのControlNetModel。SDXL系ベースモデルと組み合わせる想定。
- **制約**: モデルカードは読み込み例のみで、学習データ・評価・適用解像度の記載は無い。
- **利用条件**: licenseはcreativeml-openrail-m。商用可否は同ラインモデルの制限に従う。
- **編集者評価**: 線画からのアニメ画像生成・彩色のControlとして使えるが、情報が少なく出自は要確認。
- **次の検証（未実施）**: 線画入力でSDXLアニメベースと組み合わせ、構図保持と破綻を確認する。

確認日: 2026-10-05 / revision `e02330c836049b89f122aa18625ae027537ea143` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `diffusion_pytorch_model.fp16.safetensors`

根拠: [固定モデルカード](https://huggingface.co/r3gm/controlnet-lineart-anime-sdxl-fp16/blob/e02330c836049b89f122aa18625ae027537ea143/README.md) / [モデルAPI](https://huggingface.co/api/models/r3gm/controlnet-lineart-anime-sdxl-fp16)

## Z-Image_Anime_VAE

Z-Image（Flux）のAEをアニメイラストデータでデコーダ微調整したVAE。既存パイプラインのae.safetensorsの代わりに読み込む。

- **版の区別**: 重みは「FLUX Anime VAE B2.safetensors」を1本配布。ComfyUI用にはAnzhcのノードパックが案内されている。
- **入力・設定**: プロンプトは対象外。VAE差し替えとして使い、生成側のプロンプトはそのまま。
- **必要構成**: diffusers形式で読み込み、Z-Image/Flux系パイプラインへ組み込む。カードに必要VRAMの記載はない。
- **制約**: カードは「現時点であまり有用ではない（アニメ用ベースが未整備）」と作者が明記。高周波圧縮アーティファクトと過剰シャープの低減を狙うもので、生成品質そのものを保証しない。
- **利用条件**: licenseはapache-2.0。base_modelはTongyi-MAI/Z-Image-Turboと記載。
- **編集者評価**: アニメ生成のVAE差し替え候補として試す価値があるが、効果は限定的と作者が述べている。
- **次の検証（未実施）**: 同一プロンプト・シードで標準AEと差し替え比較し、瞳孔など小部位と高周波ノイズの変化を確認する。

確認日: 2026-10-06 / revision `7272e1c80536d207cc294968eb09c8d44e46b3a6` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `FLUX Anime VAE B2.safetensors`

根拠: [固定モデルカード](https://huggingface.co/Anzhc/Z-Image_Anime_VAE/blob/7272e1c80536d207cc294968eb09c8d44e46b3a6/README.md) / [モデルAPI](https://huggingface.co/api/models/Anzhc/Z-Image_Anime_VAE)

## AnimeBackgroundGAN-Miyazaki

CartoonGAN（Chen et al., CVPR18）を宮崎駿作品の背景で学習した画像変換モデル。PyTorch実装で構成される。

- **版の区別**: 監督別に4種類（Shinkai/Hosoda/Kon/Miyazaki）があり、本リポジトリは宮崎駿版の「miyazaki_hayao.pth」。他作風は別リポジトリ。
- **入力・設定**: プロンプトは不要。実写写真を入力し、アニメ背景風へ変換する。
- **必要構成**: PyTorchで実行。Hugging Face Spacesのデモあり。必要VRAM等の記載はない。
- **制約**: 2022年公開。カードに学習データや性能の定量評価はなく、出力品質は非公開。対象は写真→背景の変換に限られる。
- **利用条件**: licenseはMIT。モデル/Spacesの再パッケージはShō Akiyama。
- **編集者評価**: 実写素材をアニメ背景調に寄せる用途が明確だが、古いモデルで評価情報が少ない。
- **次の検証（未実施）**: 背景写真数枚で変換し、作品ごとの4モデルの作風差と破綻の有無を比較する。

確認日: 2026-10-06 / revision `c93786c4e4766e43afd2949ca7314ccad61f1d79` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `miyazaki_hayao.pth`

根拠: [固定モデルカード](https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Miyazaki/blob/c93786c4e4766e43afd2949ca7314ccad61f1d79/README.md) / [モデルAPI](https://huggingface.co/api/models/akiyamasho/AnimeBackgroundGAN-Miyazaki)

## girl-style-bert-vits2-JPExtra-models

Style-Bert-VITS2 2.1 JP-Extraをベースにした多話者TTS。5人の日本語話者（女性4・男性1）と25種の感情スタイルを持つ。

- **版の区別**: 重みは「NotAnimeJPManySpeaker_e120_s22200.safetensors」1つ。config.jsonとstyle_vectors.npyを併用する。
- **入力・設定**: プロンプトではなくspeaker_idとstyle（例: amazinGood(lol), calmCloud(sad)）で話者と感情を指定。APIではstyle_weight等のパラメータを渡す。
- **必要構成**: Style-Bert-VITS2環境（model_assets配下に3ファイル配置）またはserver_fastapi.pyで使用。languageタグはen/zh、日本語タグも付く。
- **制約**: 2024年公開。カードは「成人済み」「悪用禁止」等を明記し、音声の品質指標は示していない。
- **利用条件**: licenseはmit（カードにlicence FREE(MIT)と記載）。
- **編集者評価**: 感情スタイル付きの日本語キャラ音声を手早く試せる。多話者・多スタイルの切り替えが用途に合う。
- **次の検証（未実施）**: 同一テキストで複数話者・複数スタイルを生成し、感情表現の再現性と安定性を確認する。

確認日: 2026-10-06 / revision `bb4f103fa602e4c5b59226b3466e62b6cb09e3f9` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `NotAnimeJPManySpeaker_e120_s22200.safetensors`

根拠: [固定モデルカード](https://huggingface.co/Mofa-Xingche/girl-style-bert-vits2-JPExtra-models/blob/bb4f103fa602e4c5b59226b3466e62b6cb09e3f9/README.md) / [モデルAPI](https://huggingface.co/api/models/Mofa-Xingche/girl-style-bert-vits2-JPExtra-models)

## style_bert_vits2_jp_extra_asmr_original

Style-Bert-VITS2 JP-Extraを作者本人の音声で学習した日本語TTS。ささやき演技向けのASMR版。

- **版の区別**: 重みは「rikka_botan_asmr.safetensors」。sweet/cool/english/chinese等の姉妹版が別リポジトリで公開されている。
- **入力・設定**: プロンプトは不要。テキストを入力して合成する。感情や話し方は姉妹モデル側で切り替える。
- **必要構成**: Style-Bert-VITS2環境にconfig.json/safetensors/style_vectors.npyの3ファイルを配置。推論はCUDAまたはCPU。
- **制約**: 2024年公開。カードは音声モデルの二次配布禁止・ゾーニング必須などの利用条件を列挙。自然性の数値評価はない。
- **利用条件**: licenseはcc-by-sa-4.0。カードは商用・非商用問わず利用可とするが、二次配布禁止・ゾーニング必須などの条件があり、商用可否は断定しない。
- **編集者評価**: ささやき演技のキャラ音声を手軽に生成でき、ASMRやボイスドラマの試作に向く。
- **次の検証（未実施）**: ささやきテキストで生成し、声質・ノイズ・長文での安定性を確認する。

確認日: 2026-10-06 / revision `1feb9152f9974062d5a32a12aab725e4600c945c` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `rikka_botan_asmr.safetensors`

根拠: [固定モデルカード](https://huggingface.co/RikkaBotan/style_bert_vits2_jp_extra_asmr_original/blob/1feb9152f9974062d5a32a12aab725e4600c945c/README.md) / [モデルAPI](https://huggingface.co/api/models/RikkaBotan/style_bert_vits2_jp_extra_asmr_original)

## best-comic-panel-detection

YOLOv12xをベースに、コミックページのコマ（Comic Panel）検出用にファインチューニングした物体検出モデル。クラスはComic Panelの1種。

- **版の区別**: 配布はbest.ptとlast.ptの2ファイル。学習はCOCO事前学習のYOLOv12xからの転移学習で、640x640・AdamW・200エポック。
- **入力・設定**: プロンプトは不要。ultralyticsのYOLOで画像を入力して予測する。READMEは推論時の閾値等の指定を必須としていない。
- **必要構成**: ultralytics（PyTorch）。READMEは推論に必要なVRAMを明記していない。
- **制約**: 矩形バウンディングボックス前提で、不規則・重なり合うコマ形状は苦手と明記。検証セットは自作のRoboflowデータセット由来で、公開ベンチマークではない。
- **利用条件**: metadataはapache-2.0。学習データはRoboflowのカスタムデータセット。
- **編集者評価**: コマ分割を前処理に使う漫画翻訳・構造化の入り口として有用。
- **次の検証（未実施）**: 日本語漫画ページでコマ検出の再現率と、非矩形レイアウトでの破綻を確認する。

確認日: 2026-10-07 / revision `bbab11504194d0b341ac3f6099f3592aa0604ae3` / gated=False。ファイル名候補2件の一覧確認。代表ファイル: `best.pt`、`last.pt`

根拠: [固定モデルカード](https://huggingface.co/mosesb/best-comic-panel-detection/blob/bbab11504194d0b341ac3f6099f3592aa0604ae3/README.md) / [モデルAPI](https://huggingface.co/api/models/mosesb/best-comic-panel-detection)

## Waifu-Inpaint-XL

SDXLベースのインペインティング用モデル。unet/text_encoder/text_encoder_2/vaeのdiffusers構成と単一safetensorsを配布する。

- **版の区別**: Waifu-Inpaint-XL.safetensorsのほか、text_encoder/text_encoder_2/unet/vaeのdiffusersサブフォルダを配布する。
- **入力・設定**: モデルカードに本文がなくプロンプト記述はない。利用時はインペイント範囲（マスク）とプロンプトを指定する一般的なSDXLインペイント手順に従う。
- **必要構成**: diffusers環境。モデルカードにVRAM要件の記載はない。
- **制約**: モデルカードに本文がなく、学習データや評価の記載がない。gated（auto承認）のため利用には同意が必要。
- **利用条件**: metadataはopenrail++。
- **編集者評価**: イラストの修正・消し込み用途でSDXL系のインペイントを選ぶ際の候補。
- **次の検証（未実施）**: アニメ絵の一部修正で、マスク境界のなじみと再現性を確認する。

確認日: 2026-10-07 / revision `a33e08f2ce957d0bd9974edddbe70fcd9b8f1680` / gated=auto。ファイル名候補5件の一覧確認。代表ファイル: `Waifu-Inpaint-XL.safetensors`、`text_encoder/model.safetensors`、`text_encoder_2/model.safetensors`、`unet/diffusion_pytorch_model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/ShinoharaHare/Waifu-Inpaint-XL/blob/a33e08f2ce957d0bd9974edddbe70fcd9b8f1680/README.md) / [モデルAPI](https://huggingface.co/api/models/ShinoharaHare/Waifu-Inpaint-XL)

## Qwen3.5-4B-Danbooru-Prompt-Generator

Qwen3.5-4B系テキスト専用LLMをマージしたモデル。Danbooruタグ列を入力に、タグ列のプロンプトへ展開する。ComfyUIノードからHTTPでモデルサーバー（LM Studio等）に問い合わせる構成。

- **版の区別**: model/にBF16のsafetensors（2分割）、gguf/Qwen3.5-4B-anime.gguf（約2.7GB）、comfyui-prompt-generator/のComfyUIノードを配布する。
- **入力・設定**: カンマ区切り・アンダースコアのDanbooruタグをユーザーメッセージで渡す。`-nude`のように先頭`-`で否定、`rating:general`/`rating:explicit`でレーティング指定。thinkingはオフで使う。
- **必要構成**: transformers>=5.5.0等、またはLM Studioの互換サーバー + ComfyUI。BF16は約8.4GBの重み + KVキャッシュ。
- **制約**: テキスト専用で画像入力は不可。学習データが主にNSFWで、指定してもSFW出力は保証されないとREADMEが注意。ローカル推論の要件やプライバシーは今回未検証。
- **利用条件**: metadataはapache-2.0。上流Qwen3.5-4Bのライセンスにも従う。
- **編集者評価**: Danbooruタグの補完・拡張をローカルで回し、ComfyUIへ直結できる点が制作フローに合う。
- **次の検証（未実施）**: SFW指定（rating:general + 否定タグ）で生成タグの安全性と再現性を確認する。

確認日: 2026-10-07 / revision `d54023fefd8433c0b27356c146f34d58395001ac` / gated=False。ファイル名候補3件の一覧確認。代表ファイル: `gguf/Qwen3.5-4B-anime.gguf`、`model/model-00001-of-00002.safetensors`、`model/model-00002-of-00002.safetensors`

根拠: [固定モデルカード](https://huggingface.co/TRYZER01/Qwen3.5-4B-Danbooru-Prompt-Generator/blob/d54023fefd8433c0b27356c146f34d58395001ac/README.md) / [モデルAPI](https://huggingface.co/api/models/TRYZER01/Qwen3.5-4B-Danbooru-Prompt-Generator)

## waifu-scorer-v3

CLIP特徴量にMLPを重ねた美観スコアラ。アニメ風画像を0〜10で採点する。

- **版の区別**: model.safetensorsとmodel.pthの2ファイル。
- **入力・設定**: プロンプトは不要。画像を入力してスコアを得る。
- **必要構成**: CLIP系の推論環境。モデルカードにVRAM等の記載はない。
- **制約**: スコアは学習分布に依存し、モデルカードは用途や評価データを詳述していない。精度は今回未検証。
- **利用条件**: metadataはopenrailだが、カード本文はApache 2.0と記載され両者で表記が一致しない。商用利用の可否を断定しない。
- **編集者評価**: アニメ画像の選別・データセット品質管理の補助指標として使える。
- **次の検証（未実施）**: 手元画像でスコアのばらつきと主観評価との相関を確認する。

確認日: 2026-10-07 / revision `c2a747fd61d310a90e9cbbf8fc590c522f234424` / gated=False。ファイル名候補2件の一覧確認。代表ファイル: `model.pth`、`model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/Eugeoter/waifu-scorer-v3/blob/c2a747fd61d310a90e9cbbf8fc590c522f234424/README.md) / [モデルAPI](https://huggingface.co/api/models/Eugeoter/waifu-scorer-v3)

## Sakura-13B-Galgame

複数のオープンLLM（Baichuan2-13B、Qwen/Qwen1.5系）を日中ACGN語料で継続事前学習・微調整したテキスト生成モデル。軽小説・Galgame領域の日中翻訳向け。

- **版の区別**: カードにはv0.1〜v0.7の複数重み（Baichuan2-13B系、Qwen14B系、4bit/8bit量子化）を同リポジトリに収録。別リポジトリで7B/14B/32BのGGUF版も案内。使用系統とファイル名を固定する。
- **入力・設定**: カードにシステムプロンプト例があり、軽小説調で日本語を行単位の配列として入力し簡体字中国語へ訳す形式。他プロジェクトが提供する独自プロンプトでは品質を保証しないと明記。
- **必要構成**: カードはllama.cpp GGUFでの量子化別VRAM目安（Q4_K_Mで16G等）を掲載。llama.cpp/vllm/OpenAI互換API経由の運用が想定される。
- **制約**: 作者は人称代名詞の誤りや文脈理解の問題が残ると明記。機械翻訳のため公開時は機翻表示を求める。カードはPPL/BLEU/人手評価をTBDとしている。
- **利用条件**: メタデータはapache-2.0だが、本文はCC BY-NC-SA 4.0と明記し、Sakura全モデルと派生モデルの商用を禁止。公開重みを無条件に商用可と扱わない。
- **編集者評価**: 軽小説・Galgameの日中翻訳向けに広く使われてきた系統で、漫画・小説のローカライズ検証の比較対象になる。
- **次の検証（未実施）**: 同一の日本語台本でSakura系と汎用LLMを翻訳比較し、人称・用語一貫性・制御記号の保持を記録する。

確認日: 2026-10-08 / revision `86ebbf223c466c97aaeb503f82d63a49fe341df7` / gated=False。ファイル名候補11件の一覧確認。代表ファイル: `pytorch_model-00001-of-00003.bin`、`pytorch_model-00002-of-00003.bin`、`pytorch_model-00003-of-00003.bin`、`sakura_13b_model_v0.1/sakura-13b-2epoch-260k-0826-v0.1.bin`

根拠: [固定モデルカード](https://huggingface.co/sakuraumi/Sakura-13B-Galgame/blob/86ebbf223c466c97aaeb503f82d63a49fe341df7/README.md) / [モデルAPI](https://huggingface.co/api/models/sakuraumi/Sakura-13B-Galgame)

## Baikal-Anime-Upscaler

アニメ・イラスト向けの2倍超解像モデル。Baikal LoopSR と SwinFIR v31（Transformer系）の2系統を配布する。

- **版の区別**: Baikal_LoopSR_x2.safetensors と Baikal_SwinFIR_Anime_x2_v31.safetensors。LoopSRはloops 1〜4に対応。
- **入力・設定**: テキストプロンプトはなし。ComfyUIノード（Baikal/Upscale）でモデル読込→拡大→保存の順に接続する。
- **必要構成**: ComfyUI-Baikal-Animeノードを導入し、重みをComfyUI/models/anime_upscale/に配置。LoopSRの既定タイル/オーバーラップ/ハローは256/32/96。
- **制約**: 2倍固定。カードは品質を定量比較で示しておらず、入力の劣化具合で結果が変わる。
- **利用条件**: MIT。カードにMIT表記あり。
- **編集者評価**: アニメ特化の2倍拡大をComfyUIで扱える実装つきで、生成イラストの仕上げに組み込みやすい。
- **次の検証（未実施）**: 同一イラストでLoopSR（loops1〜4）とSwinFIRを比較し、速度と線・テクスチャの保持を記録する。

確認日: 2026-10-08 / revision `37a73e6ce75b90fe2103ec95cc2e18115857b723` / gated=False。ファイル名候補2件の一覧確認。代表ファイル: `Baikal_LoopSR_x2.safetensors`、`Baikal_SwinFIR_Anime_x2_v31.safetensors`

根拠: [固定モデルカード](https://huggingface.co/SnJake/Baikal-Anime-Upscaler/blob/37a73e6ce75b90fe2103ec95cc2e18115857b723/README.md) / [モデルAPI](https://huggingface.co/api/models/SnJake/Baikal-Anime-Upscaler)

## Anima-Control-Pose

Anima v1.0画像モデル向けのネイティブなpose制御アダプタ。凍結したAnima DiTにチャネル連結のcontrol-LoRA（rank16）とzero初期化のControlEmbedderを加える。

- **版の区別**: Preview-2（anima_pose_preview2.safetensors、512/768/1024対応）とPreview-1（512のみ）。併せて姿勢検出用ONNX（rtmw-dw-x-l、yolox_m）を配布。
- **入力・設定**: 参照写真から姿勢を検出し骨格を描画して条件にする。READMEは黒背景の細い骨格が学習条件で最良の既定と説明。strength 0でベース相当、1で骨格追従、範囲0〜2。
- **必要構成**: ComfyUIにcomfyui/内の2ノード（Anima Control Lora と ComfyUI-anima-pose-control）を配置し、rtmlib/OpenCV/ONNX Runtimeを用意。初回に検出モデル約316MBを取得。
- **制約**: Preview-2は実験段階で、姿勢を外す・手の融合・体の破綻が残るとカードが明記。動的ポーズが最も不安定で、短いプロンプトでは画風が平坦化する。
- **利用条件**: metadataはother、license_nameはcirclestone-labs-non-commercial-license。Anima派生としてNVIDIA Open Model Licenseも継承し、非商用のみ。
- **編集者評価**: Anima系で姿勢を制御する数少ない公開実装で、ポーズ指定の検証候補になる。
- **次の検証（未実施）**: 同一キャラ・同一プロンプトでcontrol on/offとstrengthを変え、姿勢一致と破綻の頻度を記録する。

確認日: 2026-10-08 / revision `8f559771d5a49a02fa03f7df2a05ccb7eecb3a2a` / gated=False。ファイル名候補4件の一覧確認。代表ファイル: `adapter_model.safetensors`、`anima_pose_preview2.safetensors`、`detector/rtmw-dw-x-l_simcc-cocktail14_270e-256x192_20231122.onnx`、`detector/yolox_m_8xb8-300e_humanart-c2c7a14a.onnx`

根拠: [固定モデルカード](https://huggingface.co/Claquasse/Anima-Control-Pose/blob/8f559771d5a49a02fa03f7df2a05ccb7eecb3a2a/README.md) / [モデルAPI](https://huggingface.co/api/models/Claquasse/Anima-Control-Pose)

## H3_Ref2V_Anime_Slider_v1

MiniMax-H3をベースにしたスライダーLoRA。正の強度で2Dアニメ寄り、負で写実寄りに全体スタイルを動かす。

- **版の区別**: H3_Ref2V_Anime_Slider_v1.safetensors の単一ファイル。Ref2VとT2Vの両ワークフローに適用。
- **入力・設定**: 推奨強度は-5〜5で、通常は3または-3でスタイルが定まるとカードが説明。プロンプトや参照画像により調整が必要。
- **必要構成**: MiniMax-H3ワークフロー上でLoRAとして適用。必要VRAMや手順の詳細はカードに記載なし。
- **制約**: 主要目的は2Dアニメ寄せで、写実化は主目的ではない。強度は参照画像とプロンプト依存で調整が要る。
- **利用条件**: カードにライセンス表記なし（metadataはnull）。MiniMax-H3の条件に従う必要があり、商用可否は未確認。
- **編集者評価**: H3の2Dアニメが3D寄りになる問題への対処として、スタイル寄せの検証に使える。
- **次の検証（未実施）**: 同一参照画像・プロンプトで強度-3/0/3を比較し、平面感とキャラ保持の差を記録する。

確認日: 2026-10-08 / revision `5a55012c837819edcd1e2f9b67c73ea46921875f` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `H3_Ref2V_Anime_Slider_v1.safetensors`

根拠: [固定モデルカード](https://huggingface.co/adf99/H3_Ref2V_Anime_Slider_v1/blob/5a55012c837819edcd1e2f9b67c73ea46921875f/README.md) / [モデルAPI](https://huggingface.co/api/models/adf99/H3_Ref2V_Anime_Slider_v1)

## Anima-3.8B

Anima 2.9BのDiTを52ブロックへ拡張した約3.8Bのアニメ/イラスト向け画像モデル。timestep-awareなSemantic Connector v2を拡散チェックポイントへ統合し、別途Qwen3.5 4BとネイティブQwen3 0.6Bのテキストエンコーダを併用する。

- **版の区別**: 推論用バンドルはAnima-3.8B-v1.1（旧Anima-3.8Bとpreview素材、expanded_adapterも同梱）。テキストエンコーダはqwen35_4b.safetensorsとqwen_3_06b_base.safetensors、VAEはqwen_image_vae.safetensorsを別途配置する。
- **入力・設定**: 自然文・Danbooru/Gelbooruタグ・混合に対応。複数キャラは主語を明示し代名詞を避けるよう案内。解像度832x1216（1MP程度）、CFG4〜7、28〜50steps、res_multistep+Betaが推奨の出発点。
- **必要構成**: ComfyUIはcomfyui-anima-3-8B、Forge Neoはforge-anima-3-8Bの拡張を導入。テキストエンコーダはプロンプト符号化時のみ読み込み、その後解放する構成でピークVRAMを抑える。
- **制約**: 作者は実験的な拡張リリースと位置づける。低VRAMではプロンプト符号化中にQwen3.5の分だけVRAM使用が一時的に増えると説明。正確なメモリ量は解像度・attention・offload設定依存。
- **利用条件**: CircleStone Labs Non-Commercial License（派生物カテゴリ）。Cosmos-Predict2由来のNVIDIA Open Model Licenseも関係する。無条件の商用利用可ではない。
- **編集者評価**: Anima系の最新拡張として、プロンプト追従と複数キャラの属性束縛の改善を狙った構成が具体的。
- **次の検証（未実施）**: Anima-2.9Bと同一プロンプト・解像度で生成し、複数キャラの属性混線と構図の差を比較する。

確認日: 2026-10-09 / revision `3ef641256377dc4e7efbf35d426ca31c1fe5180b` / gated=False。ファイル名候補4件の一覧確認。代表ファイル: `difussion_models/Anima-3.8B-v1.1.safetensors`、`difussion_models/Anima-3.8B.safetensors`、`text_encoders/Anima-3.8B-expanded_adapter.safetensors`、`text_encoders/qwen35_4b.safetensors`

根拠: [固定モデルカード](https://huggingface.co/lylogummy/Anima-3.8B/blob/3ef641256377dc4e7efbf35d426ca31c1fe5180b/README.md) / [モデルAPI](https://huggingface.co/api/models/lylogummy/Anima-3.8B)

## Anima-InContext-Character

Anima 2B（Cosmos-Predict2 DiT + Qwen3-0.6Bテキストエンコーダ + WanVAE）向けのin-context参照LoRA（DiT rank64）とComfyUIノード。参照画像をVAE潜在のまま時間軸のフレームとして連結し、self-attention経由で同一性を流し込む。

- **版の区別**: 重みはanima-incontext-character.safetensors。ベースのAnima各ファイルと、同梱のカスタムノードcomfyui-anima-incontext・ワークフローJSONを併用する。
- **入力・設定**: 参照は全身1枚＋顔アップ1枚を推奨。外見タグも併記し、プロンプトはポーズ/シーン、参照は同一性を担う。strength1.0が中立、効きが弱い場合1.2〜1.5。er_sde/simple、30steps、CFG4、discrete_flow_shift3.0が推奨。
- **必要構成**: ComfyUIにカスタムノードを配置し、LoRAはmodels/loras、Animaベース一式をdiffusion_models/text_encoders/vaeへ。参照はマスクで白背景合成するのが推奨。
- **制約**: 細かな装飾・柄は揺れることがあるとREADMEが明記。参照を強くすると背景が薄まることがある。学習データはアニメイラスト領域。
- **利用条件**: ベースAnimaはCircleStone Labs非商用ライセンスで、本LoRAも派生物として非商用配布。商用利用・再配布前に最新LICENSEの確認が必要と記載。
- **編集者評価**: キャラ毎の学習なしで未知キャラを別ポーズ・別シーンに展開できる点が、制作実務の一貫性維持に効く。
- **次の検証（未実施）**: 全身＋顔アップの参照で数シーンを生成し、髪飾りや服の柄の保持度とstrengthの効きを確認する。

確認日: 2026-10-09 / revision `e084c88c02dcaa55806c56b22a43461d4c32be85` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `anima-incontext-character.safetensors`

根拠: [固定モデルカード](https://huggingface.co/darask0/Anima-InContext-Character/blob/e084c88c02dcaa55806c56b22a43461d4c32be85/README.md) / [モデルAPI](https://huggingface.co/api/models/darask0/Anima-InContext-Character)

## z-image-modern-anime

Tongyi-MAIのZ-Imageを日本語モダンアニメ調にフルファインチューンした実験モデル。作者はQuality Tuningのみで学習したと記載。diffusersのZImagePipelineでfrom_pretrainedできる形式で配布。

- **版の区別**: modern_anime_z_image.safetensorsの単一チェックポイント。diffusers一式（text_encoder/transformer/vae）も同梱。
- **入力・設定**: トリガーは「Japanese modern anime style, 」。negative promptは「photo, cg, 3d, blurry」を例示。1280x720、CFG4、30steps、cfg_normalization=Falseのコード例が示されている。
- **必要構成**: ComfyUIでモデルを所定フォルダへ置くか、diffusersのZImagePipelineで読み込む。README記載の再現設定以外の条件は未記載。
- **制約**: 作者がexperimental（実験的）と明記。解像度・ステップ等は例示の1条件のみで、広い条件での検証は示されていない。
- **利用条件**: apache-2.0。
- **編集者評価**: Z-Image系のアニメ専用ファインチューンとして、既存SDXL系のアニメモデルと比較する候補になる。
- **次の検証（未実施）**: 同一プロンプトでZ-Imageベースと比較し、画風の寄り方と解像度安定性を確認する。

確認日: 2026-10-09 / revision `c5e91f527e19f68ce9e941922dce5e7ed0af3849` / gated=False。ファイル名候補5件の一覧確認。代表ファイル: `modern_anime_z_image.safetensors`、`text_encoder/model.safetensors`、`transformer/diffusion_pytorch_model-00001-of-00002.safetensors`、`transformer/diffusion_pytorch_model-00002-of-00002.safetensors`

根拠: [固定モデルカード](https://huggingface.co/alfredplpl/z-image-modern-anime/blob/c5e91f527e19f68ce9e941922dce5e7ed0af3849/README.md) / [モデルAPI](https://huggingface.co/api/models/alfredplpl/z-image-modern-anime)

## Irodori-TTS-600M-v3-VoiceDesign

Rectified Flow Diffusion Transformer（RF-DiT）による約600Mの日本語TTS。テキスト・参照音声・キャプションを同時に条件に使うMulti-modal Voice Designで、32次元DACVAE潜在から48kHz波形を再構成する。Duration Predictorを内蔵。

- **版の区別**: 重みはルートのmodel.safetensors。ベースはAratako/Irodori-TTS-500M-v2系で、推論・学習コードはGitHubのAratako/Irodori-TTSを参照する。
- **入力・設定**: テキストに絵文字を埋めて笑い・咳・吐息などを制御（EMOJI_ANNOTATIONS.md）。キャプションで感情・話し方を指定し、参照音声で話者同一性を保持する。サンプルは同一シードでキャプション差のみを見せる。
- **必要構成**: GitHubのIrodori-TTSの推論手順に従う。モデルカードに追加のVRAM要件は明記なし。
- **制約**: 言語は日本語（language: ja）中心。キャプション・絵文字の効きは学習データの注釈パイプラインに依存する。
- **利用条件**: MIT。生成音声にはSilentCipherによる不可聴ウォーターマークを付与すると記載。
- **編集者評価**: 参照音声＋キャプション＋絵文字で演技を細かく指定できる点が、キャラ音声制作で使い分けやすい。
- **次の検証（未実施）**: 同一参照音声でキャプションと絵文字を変え、感情表現の振れ幅と声質保持を聴き比べる。

確認日: 2026-10-09 / revision `e863a3a93e652e09afeff3e84823a206a0a60314` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/Aratako/Irodori-TTS-600M-v3-VoiceDesign/blob/e863a3a93e652e09afeff3e84823a206a0a60314/README.md) / [モデルAPI](https://huggingface.co/api/models/Aratako/Irodori-TTS-600M-v3-VoiceDesign)

## manga-ocr-2025-onnx

日本語漫画OCR（kha-white/manga-ocr系）のVision Encoder DecoderをOptimumでONNX出力したもの。縦書き・横書き、ルビ、画像上の文字、低品質スキャンなど漫画特有の条件に頑健とされる。

- **版の区別**: encoder_model.onnxとdecoder_model.onnxの2ファイル構成。jzhang533/manga-ocr-base-2025の改良を反映。元モデルはmanga109-sと合成データで学習。
- **入力・設定**: TrOCRProcessorとORTModelForVision2Seq（optimum[onnxruntime]）で画像をRGB読み込みし、pixel_valuesからテキストを生成する。
- **必要構成**: optimum[onnxruntime]。ONNXランタイムでCPU推論できる構成。
- **制約**: モデルカードに性能評価や対応範囲の記載はなく、実装は元モデルと派生改良に依存。リポジトリのライセンスは未記載（null）。
- **利用条件**: ライセンスは明示されていない。元実装manga-ocrの条件を確認してから利用する。
- **編集者評価**: ONNX化により漫画OCRをローカル配信やアプリ組み込みへ載せやすくする配布。
- **次の検証（未実施）**: 手元の漫画画像でOCR精度と推論速度を、元のmanga-ocrと比較する。

確認日: 2026-10-09 / revision `e8b27bbd3f424fe3877e0bda704d6a920e4f0a33` / gated=False。ファイル名候補2件の一覧確認。代表ファイル: `decoder_model.onnx`、`encoder_model.onnx`

根拠: [固定モデルカード](https://huggingface.co/l0wgear/manga-ocr-2025-onnx/blob/e8b27bbd3f424fe3877e0bda704d6a920e4f0a33/README.md) / [モデルAPI](https://huggingface.co/api/models/l0wgear/manga-ocr-2025-onnx)

## character_turnaround_sheet_qwen_image_edit_2509

Qwen-Image-Edit-2509向けのLoRA。入力キャラ画像から多角度を合成したターンアラウンドシートを生成する。

- **版の区別**: 単一のsafetensors（character_turnaround_sheet_v2_...）を配布。トリガー語は「Character turnaround sheet」，学習データセットは別リポジトリ。
- **入力・設定**: トリガー語「Character turnaround sheet」を使用。READMEは入力解像度600x1080、出力解像度2600x1080を推奨。
- **必要構成**: Qwen-Image-Edit-2509とdiffusers。実行ワークフローや追加ノードの詳細はカードに記載なし。
- **制約**: カードの記述は簡潔で、対応解像度や失敗例の詳細は限られる。
- **利用条件**: licenseはapache-2.0。Qwen-Image-Edit-2509側の条件も別途確認が必要。
- **編集者評価**: キャラ設定画を多角度で揃える用途に絞ったLoRAで、設定資料づくりに使いやすい。
- **次の検証（未実施）**: 自作キャラ1体で推奨解像度どおりに生成し、角度ごとの同一性を確認。

確認日: 2026-10-10 / revision `bb3bcbf61c75b79a182d6a58f601fcdfc7b4e0ab` / gated=False。ファイル名候補1件の一覧確認。代表ファイル: `character_turnaround_sheet_v2_qwen_image_edit_000000760.safetensors`

根拠: [固定モデルカード](https://huggingface.co/tarn59/character_turnaround_sheet_qwen_image_edit_2509/blob/bb3bcbf61c75b79a182d6a58f601fcdfc7b4e0ab/README.md) / [モデルAPI](https://huggingface.co/api/models/tarn59/character_turnaround_sheet_qwen_image_edit_2509)

## flux-2-klein-4b-spritesheet-lora

FLUX.2-Klein 4BをベースにしたLoRA。1枚のオブジェクト画像から2x2のマルチビュー・スプライトシート（アイソメ2面・側面・トップダウン）を作る。

- **版の区別**: fal.ai用とComfyUI用の2ファイルを配布。トリガーは「2x2 sprite sheet」、推奨LoRAスケールは1.1。
- **入力・設定**: プロンプトは「2x2 sprite sheet」。出力は左上がアイソメ(右下向き)、右上がアイソメ(左下向き)、左下が左向き横顔、右下が上向きトップダウンの固定レイアウト。
- **必要構成**: FLUX.2-Klein 4Bと画像編集LoRAを扱える環境（fal.ai SDKまたはComfyUI）。
- **制約**: 出力背景は赤一色（設計上）。学習データは乗り物やオブジェクト中心の48組（120生成から人手選別）。
- **利用条件**: licenseはapache-2.0。
- **編集者評価**: ゲーム用に多方向の参照/アセットを短い手数で作れる候補。作例はキャラクターよりオブジェクト中心。
- **次の検証（未実施）**: 自キャラ画像で4方向の一貫性と背景除去のしやすさを確認。

確認日: 2026-10-10 / revision `6d3128f9223f585251ad3a02dd0d8082c9b5ca3f` / gated=False。ファイル名候補2件の一覧確認。代表ファイル: `flux-spritesheet-lora.safetensors`、`mFtSubaAlDqtHyKk6eIPi_pytorch_lora_weights_comfy_converted.safetensors`

根拠: [固定モデルカード](https://huggingface.co/fal/flux-2-klein-4b-spritesheet-lora/blob/6d3128f9223f585251ad3a02dd0d8082c9b5ca3f/README.md) / [モデルAPI](https://huggingface.co/api/models/fal/flux-2-klein-4b-spritesheet-lora)

## pixel_spritesheet_4walk_combat_32x48_v1

Qwen-Image-Edit-2511をベースにしたピクセルアート用LoRA。32x48のキャラについて4方向の歩行3フレーム・攻撃2フレーム・被弾1フレームを6x4グリッドで出す。

- **版の区別**: 単一リポジトリに複数ステップのLoRAを配布。専用トリガー語はなく、プロンプトでグリッド構成を指定する。
- **入力・設定**: READMEの例文どおり、行ごとに下/左/右/上の向きで「歩行3・攻撃2・被弾1」フレームを指定する。
- **必要構成**: ComfyUIのQwen Image Edit 2511ワークフローにLoRAロードノードを追加。入力は学習時と同じ768x768。
- **制約**: ピクセルパーフィットには4分の1（768→192）へダウンスケールする必要があると注記。k-centroid縮小を推奨。
- **利用条件**: licenseはapache-2.0。ベースのQwen-Image-Edit-2511側の条件も別途確認が必要。
- **編集者評価**: ドット絵ゲームのキャラスプライト一式を1枚で作る用途が明確。
- **次の検証（未実施）**: 768x768で生成し、k-centroid縮小後に各コマの位置ずれと行構成を確認。

確認日: 2026-10-10 / revision `9e3fafee0a2e49cbec23b7b54a8b03ce1ae0cad1` / gated=False。ファイル名候補4件の一覧確認。代表ファイル: `pixel_4walk_32x48_qwen_image_edit_2511_v1.safetensors`、`pixel_4walk_32x48_qwen_image_edit_2511_v1_000001750.safetensors`、`pixel_4walk_32x48_qwen_image_edit_2511_v1_000002000.safetensors`、`pixel_4walk_32x48_qwen_image_edit_2511_v1_000002500.safetensors`

根拠: [固定モデルカード](https://huggingface.co/svntax-dev/pixel_spritesheet_4walk_combat_32x48_v1/blob/9e3fafee0a2e49cbec23b7b54a8b03ce1ae0cad1/README.md) / [モデルAPI](https://huggingface.co/api/models/svntax-dev/pixel_spritesheet_4walk_combat_32x48_v1)

## Anima-Lightning

CircleStone LabsのAnimaとNVIDIA Cosmos-Predict2-2Bを基にした蒸留版。付属の専用transformerがK=4条件付けを持ち、標準のCosmosTransformer3DModelでは全チェックポイントを正しく読めないと明記。

- **版の区別**: 単一リポジトリにtext_encoder/text_conditioner/transformer/vaeと専用Pythonモジュールを同梱。旧checkpointとshift-1レシピを置き換える更新版。
- **入力・設定**: READMEは「anime illustration, a lighthouse above a calm sea, sunset」のような自然文例を示す。旧shift-1レシピや標準の全ステップCFG5推論は使わず、4ステップ・CFG1・scheduler shift3・raw sigmas[1,.75,.5,.25]で使うよう明記。
- **必要構成**: CUDA/BF16のPyTorch、Anima modular対応のDiffusers。検証環境はdiffusers 0.39.0、transformers 5.7.0、PyTorch 2.12.1+cu130。
- **制約**: 解剖・複雑な構図・文字描画は不完全と注記。保存transformerはBF16のためFP32や他サンプラ実装と結果が異なり得ると記載。
- **利用条件**: licenseはother、license_nameはcirclestone-labs-non-commercial-license。上流のCircleStone条項とNVIDIA Open Model Licenseが適用。
- **編集者評価**: Anima系を4ステップで回す高速版として、試作やバッチ生成の候補になる。
- **次の検証（未実施）**: 同一プロンプトでAnima本体と4ステップ生成を比較し、速度・構図・破綻の差を記録。

確認日: 2026-10-10 / revision `9dbb6e1a0f94eda0a1e523836d32355fb961cc7a` / gated=False。ファイル名候補4件の一覧確認。代表ファイル: `text_conditioner/diffusion_pytorch_model.safetensors`、`text_encoder/model.safetensors`、`transformer/diffusion_pytorch_model.safetensors`、`vae/diffusion_pytorch_model.safetensors`

根拠: [固定モデルカード](https://huggingface.co/aina-tech/Anima-Lightning/blob/9dbb6e1a0f94eda0a1e523836d32355fb961cc7a/README.md) / [モデルAPI](https://huggingface.co/api/models/aina-tech/Anima-Lightning)
