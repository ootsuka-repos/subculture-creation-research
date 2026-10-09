# アニメ・サブカル制作のリポジトリ全体像（2026-10-01）

[SOTA一覧へ](anime-task-sota.md) · [正本JSON](../sota-catalog.json)

制作工程ごとに、採用実績・更新状況・ライセンスを確認して選んだ代表リポジトリ。星数は累計。更新状況は確認コミットと最終pushを併記し、12か月以上更新がないものは停滞として注記。起動・動作検証は未実施。

## 学習フレームワーク(画像・Anima/SDXL LoRA)

<a id="repos-training-image"></a>
- **判定**: アニメ特化の最良 / 確度 高
- **選定基準と順位の根拠**: 事実: 各READMEを確認。kohya-ss/sd-scriptsはAnimaのLoRA/LLLite学習を公式docs(anima_train_network.md等)で対応(★7242、v0.12.0=2026-09-24、Apache-2.0)。ostris/ai-toolkitはREADMEにcirclestone-labs/Anima-Base-v1.0-Diffusersを明記(★12164、MIT)。Nerogar/OneTrainerはmodules/modelSetupにAnimaLoRASetup.py/AnimaFineTuneSetup.pyを持つ(★3220、AGPL-3.0)。gazingstars123/Anima-Standalone-Trainer(★329、Apache-2.0)はsd-scripts系のAnima専用GUIで、Anima-2.9B対応をREADMEが記載。X(2026-08-15の日本語投稿、likes76)でもAnima-2.9B学習にsd-scripts系フォークが言及、別投稿(2026-09-01)でOneTrainerによるAnima LoRA作成例。評価: 採用実績と公式Anima対応の明確さでsd-scripts→ai-toolkit→OneTrainerの順。sd-scriptsをまず選べば迷わない。bmaltais/kohya_ss(★12609、GUI、2026-08-01push)とAkegarasu/lora-scripts(★6155、AGPL、最新コミット2025-09)はGUIラッパで次点。ライセンスはAGPL-3.0(OneTrainer)に注意、Anima本体のライセンス(非商用)も別途確認。SimpleTunerもAnima行あり(次点)。

関連リポジトリ:

- [kohya-ss/sd-scripts](https://github.com/kohya-ss/sd-scripts) — SDXL/Anima/FLUX等のLoRA・LLLite学習CLI(標準的存在)（★7,242 / Apache-2.0 / 最終push 2026-09-24 / release v0.12.0 (2026-09-24) / 確認コミット [`690ea7f9`](https://github.com/kohya-ss/sd-scripts/blob/690ea7f96c23182352ec63def76d431c6120bd2f/README.md) / 制作カタログ: [sd-scripts](../categories/workflow.md#sd-scripts)）
  - 公式docsにAnima LoRA/LLLite学習ガイド、torch.compile対応の更新履歴がREADMEにある。v0.12.0=2026-09-24。【catalog.json収録: id=sd-scripts】
- [ostris/ai-toolkit](https://github.com/ostris/ai-toolkit) — 多モデル対応のLoRA学習(GUI/CLI)（★12,243 / MIT / 最終push 2026-10-09 / 確認コミット [`ecee894e`](https://github.com/ostris/ai-toolkit/blob/ecee894ed2b1f3716d9d7326693061ec1a3105bb/README.md)）
  - ★12164で本スライス最大の学習ツール。READMEがAnima-Base-v1.0-Diffusersを対応モデルとして列挙。リリースタグ無し(mainを追う)。MIT。【catalog.json未収録(新規)】
- [Nerogar/OneTrainer](https://github.com/Nerogar/OneTrainer) — GUI中心の学習(LoRA/FineTune/Embedding)（★3,233 / AGPL-3.0 / 最終push 2026-10-05 / 確認コミット [`23df3832`](https://github.com/Nerogar/OneTrainer/blob/23df3832e8f213d64c337e39f9365ba46e99fed0/README.md)）
  - modules/modelSetupにAnima用Setupが存在。最新コミット2026-08-19、リリースタグ無し。AGPL-3.0で組み込み配布時は注意。【catalog.json未収録(新規)】
- [gazingstars123/Anima-Standalone-Trainer](https://github.com/gazingstars123/Anima-Standalone-Trainer) — Anima/Anima-2.9B専用LoRA学習GUI(sd-scripts派生)（★332 / Apache-2.0 / 最終push 2026-08-28 / release v2.2.0 (2026-04-30) / 確認コミット [`7f5c336f`](https://github.com/gazingstars123/Anima-Standalone-Trainer/blob/7f5c336f3c61802e9b7a64fb4a4492d50362a90f/README.md)）
  - READMEでAnima 2.9B LoRA学習対応を明記。v2.2.0=2026-04-30、個人プロジェクトで★329と小規模。Anima専用で手軽だが保守体制は小さい。【catalog.json未収録(新規)】

## 学習フレームワーク(動画・Wan/MiniMax等、音声は対象外)

<a id="repos-training-video-audio"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **選定基準と順位の根拠**: 事実: kohya-ss/musubi-tuner(★2074、v0.3.6=2026-09-27)はdocsにwan.md・qwen_image.md・zimage.md・minimax_h3.md等を持つがAnima用docは無い(docs一覧で確認)。tdrussell/diffusion-pipe(★2028、GPL-3.0)はREADMEの対応モデルにWan2.1/2.2・Qwen-Image等を列挙し、更新履歴に『Support Anima』あり。SimpleTuner(★2930、AGPL-3.0、v4.9.2=2026-09-07)は『image/video/audio』対応を標榜。modelscope/DiffSynth-Studio(★13200、Apache-2.0)は推論/学習両対応の基盤(リリースv1.1.9は2025-11)。X(2026-08-21、likes68)でmusubi-tunerのH3ワンショットLoRA作成への言及。評価: 動画LoRA(Wan2.2/AnimeGen-I2V系)はmusubi-tuner→diffusion-pipeが標準。アニメ特化の動画学習ツールは見つからず汎用。音声(TTS)学習フレームワークはここでは該当が弱く、TTS側カテゴリに記載。musubi-tunerはGitHubライセンス未検出(None)なので利用前にLICENSEファイルを確認。

関連リポジトリ:

- [kohya-ss/musubi-tuner](https://github.com/kohya-ss/musubi-tuner) — Wan/Qwen-Image/H3等の動画・画像LoRA学習（★2,090 / ライセンス未表示 / 最終push 2026-09-30 / release v0.3.6 (2026-09-27) / 確認コミット [`f8a1b037`](https://github.com/kohya-ss/musubi-tuner/blob/f8a1b03794a49239a3539015075f5123d6c07d66/README.md) / 制作カタログ: [musubi-tuner](../categories/workflow.md#musubi-tuner)）
  - 2026-09-30push、v0.3.6=2026-09-27と最も更新が速い。ライセンスはGitHub APIで未検出のため要確認。【catalog.json収録: id=musubi-tuner】
- [tdrussell/diffusion-pipe](https://github.com/tdrussell/diffusion-pipe) — パイプライン並列のdiffusion学習(Wan2.2等)（★2,029 / GPL-3.0 / 最終push 2026-09-28 / 確認コミット [`334106c2`](https://github.com/tdrussell/diffusion-pipe/blob/334106c2d0e29131b53d504b80e211942dac147e/README.md)）
  - ★2028。Wan2.2対応、更新履歴にAnima対応。2026-09-28push。GPL-3.0。リリースタグ無し。【catalog.json未収録(新規)】
- [bghira/SimpleTuner](https://github.com/bghira/SimpleTuner) — image/video/audio対応の汎用学習キット（★2,934 / AGPL-3.0 / 最終push 2026-10-09 / release v4.9.3 (2026-10-01) / 確認コミット [`f1cb3800`](https://github.com/bghira/SimpleTuner/blob/f1cb3800c9d32b888d5e391ab74b6101ecb4acd8/README.md)）
  - ★2930、v4.9.2=2026-09-07。READMEにAnimaのライセンス行(非商用)が載る。AGPL-3.0。【catalog.json未収録(新規)】
- [modelscope/DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) — Wan等の推論+学習基盤（★13,214 / Apache-2.0 / 最終push 2026-10-09 / release v1.1.9 (2025-11-18) / 確認コミット [`974cfa37`](https://github.com/modelscope/DiffSynth-Studio/blob/974cfa37f27ac55eba3b6d10efa21f876900572d/README.md) / 制作カタログ: [diffsynth-studio](../categories/workflow.md#diffsynth-studio)）
  - ★13200、2026-09-30push。最新リリースは2025-11-18で、mainが先行。【catalog.json収録: id=diffsynth-studio】

## ComfyUIのアニメ関連エコシステム(本体・テンプレ・Anima拡張)

<a id="repos-comfyui-anime"></a>
- **判定**: アニメ特化の最良 / 確度 高
- **選定基準と順位の根拠**: 事実: Comfy-Org/ComfyUI(★135621、v0.38.0=2026-09-29、GPL-3.0)のREADME対応モデル一覧にAnimaが含まれる。Comfy-Org/workflow_templates(★1217、MIT、v0.11.73=2026-09-30)が公式テンプレ集。kohya-ss/ComfyUI-Anima-LLLite(★215、Apache-2.0、2026-08-02)はsd-scripts作者によるAnima ControlNet-LLLite用ノード。Ararararararaki/comfyui-anima-toolkit(★31、MIT、v2.15.1=2026-09-18)はLoRA一括・Danbooruタグ検索/ギャラリー等(READMEは中国語)。評価: 土台は公式ComfyUIとテンプレで確定、Anima固有はkohya版が信頼性高、toolkitは小規模個人開発で採用実績は薄い。ComfyUI-Manager(★16316、GPL-3.0)は導入に事実上必須だがアニメ特化ではないため枠外。ComfyUI-Impact-Pack(2026-04-19)やkijai/WanVideoWrapper(2026-05-24)はpushが4〜5か月前で更新鈍化。ローカルのComfyUI-Anime-Extensions(Irodori-TTS・imgutils・YuE2・Sol-H3-Spark・VRM・Comic Page等)とは役割が重ならない(READMEで確認)。

関連リポジトリ:

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) — ノードベース生成UI/エンジン本体（★136,628 / GPL-3.0 / 最終push 2026-10-09 / release v0.39.0 (2026-10-05) / 確認コミット [`83071e1a`](https://github.com/Comfy-Org/ComfyUI/blob/83071e1aec311d31e773d64d6872181b3bad0fe2/README.md) / 制作カタログ: [comfyui](../categories/workflow.md#comfyui)）
  - READMEがAnimaを対応モデルとして列挙、v0.38.0=2026-09-29。ComfyUIはcatalog収録の本体。【catalog.json収録: id=comfyui】
- [Comfy-Org/workflow_templates](https://github.com/Comfy-Org/workflow_templates) — 公式ワークフロー雛形（★1,278 / MIT / 最終push 2026-10-09 / release v0.11.78 (2026-10-07) / 確認コミット [`0bfbbbfa`](https://github.com/Comfy-Org/workflow_templates/blob/0bfbbbfa260e76f69137f5aa37b7553199c73bc0/README.md)）
  - v0.11.73=2026-09-30と更新が頻繁。Animaテンプレの有無は個別に未確認。【catalog.json未収録(新規)】
- [kohya-ss/ComfyUI-Anima-LLLite](https://github.com/kohya-ss/ComfyUI-Anima-LLLite) — Anima用ControlNet-LLLiteノード（★221 / Apache-2.0 / 最終push 2026-08-02 / 確認コミット [`b7495bd8`](https://github.com/kohya-ss/ComfyUI-Anima-LLLite/blob/b7495bd8eb876e334509976896702484ed19cdbb/README.md)）
  - sd-scripts側のLLLite学習(docs/anima_train_control_net_lllite.md)と対。★215、最終push 2026-08-02。【catalog.json未収録(新規)】
- [Ararararararaki/comfyui-anima-toolkit](https://github.com/Ararararararaki/comfyui-anima-toolkit) — Anima向けLoRA管理・Danbooruタグ・出力ギャラリー（★34 / MIT / 最終push 2026-10-09 / release v2.30.0 (2026-10-07) / 確認コミット [`d95f5b50`](https://github.com/Ararararararaki/comfyui-anima-toolkit/blob/d95f5b50c224ab5d7f01a7cac7164f06bf212213/README.md)）
  - 2026-09-30pushで更新活発だが★31と小規模。中国語中心。MIT。【catalog.json未収録(新規)】

## データセット構築(収集・タグ付け・キュレーション)

<a id="repos-dataset-building"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **選定基準と順位の根拠**: 事実: mikf/gallery-dl(★19893、GPL-2.0、v1.32.14=2026-09-27)は多サイトのbooru/Pixiv等ダウンローダの事実上標準。Bionus/imgbrd-grabber(★3210、Apache-2.0、v7.14.0=2026-08-14)はbooru特化GUI/CLI。deepghs/imgutils(★415、MIT、v0.19.0=2025-09-10、最終push 2025-10-11)はWD14タグ付け・顔/頭検出・キャラ切り出しの共通ライブラリでローカルComfyUI-Anime-Extensionsも依存。starik222/BooruDatasetTagManager(★1947、MIT、v2.6.3=2026-02-25)は学習用タグ編集GUI。評価: 収集はgallery-dl、タグ編集はBooruDatasetTagManager、自動処理はimgutils。deepghs/waifuc(★409)は収集→加工パイプラインの本命だが最終push 2024-08で停滞(reviewedへ)。重複排除専用の有力repoは検索では見つからず(未確認)。jhc13/taggui(★1351、GPL-3.0、2025-10-11)も12か月手前で停滞気味。新顔のperfectgf/lora-dataset-studio(★283、2026-09-29)は作者自身がai-toolkit+ComfyUI連携を謳うが新しく実績不足。

関連リポジトリ:

- [mikf/gallery-dl](https://github.com/mikf/gallery-dl) — booru/Pixiv等の一括ダウンロード（★19,999 / GPL-2.0 / 最終push 2026-10-09 / release v1.32.16 (2026-10-09) / 確認コミット [`8b9a56d6`](https://github.com/mikf/gallery-dl/blob/8b9a56d6b1a53bc13a80894625fd58b24de3063a/README.md)）
  - ★19893、リリース2026-09-27。ライセンスGPL-2.0。【catalog.json未収録(新規)】
- [Bionus/imgbrd-grabber](https://github.com/Bionus/imgbrd-grabber) — booruクライアント兼ダウンローダ（★3,223 / Apache-2.0 / 最終push 2026-09-26 / release v7.14.0 (2026-08-14) / 確認コミット [`56f673c6`](https://github.com/Bionus/imgbrd-grabber/blob/56f673c6e821567e5a8af5361bf8004c62a55052/README.md)）
  - ★3210、Apache-2.0、リリース2026-08-14。【catalog.json未収録(新規)】
- [deepghs/imgutils](https://github.com/deepghs/imgutils) — アニメ画像の検出・タグ付け・切り出し共通ライブラリ（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - ★415。最終push 2025-10-11で更新は鈍化(12か月手前)。ローカルComfyUI-Anime-Extensionsが依存(READMEの要件に記載)。【catalog.json未収録(新規)】
- [starik222/BooruDatasetTagManager](https://github.com/starik222/BooruDatasetTagManager) — LoRA用タグ編集GUI（★1,949 / MIT / 最終push 2026-02-25 / release v2.6.3 (2026-02-25) / 確認コミット [`953e1856`](https://github.com/starik222/BooruDatasetTagManager/blob/953e1856caa846ae0b4a62a81a24219d8df4b50b/README.md)）
  - ★1947、MIT、2026-02-25リリース。【catalog.json未収録(新規)】

## アニメ動画の超解像・フレーム補間

<a id="repos-video-upscale-interpolation"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **選定基準と順位の根拠**: 事実: AaronFeng753/Waifu2x-Extension-GUI(★17060、v3.141.01=2026-09-02、ライセンスNOASSERTION)は画像/動画/GIFの超解像+補間GUIで最大級。k4yt3x/video2x(★21897、AGPL-3.0)はREADME/X投稿(2026-07-25)でAnime4K v4/Real-ESRGAN/Real-CUGAN/RIFE対応と説明、ただし最新リリース6.4.0=2025-01、最終push 2026-03-07。NevermindNilas/TheAnimeScripter(★329、AGPL-3.0、v2.10.0=2026-09-20)は超解像+RIFE補間+復元で更新が最も活発。the-database/VideoJaNai(★280、GPL-3.0、2.1.0=2026-06-18)はTensorRT/VapourSynthによる高速変換GUI。X上の使用例は主にVideo2X(2026-06〜08、likes50〜69、Grok生成動画の後処理)。評価: 動画制作の現場利用はVideo2XとGUI系、活発度ではTAS。mpv内リアルタイムはthe-database/mpv-AnimeJaNai(★752)。Anime4K(★21448、MIT)は最終push 2024-08でライブラリ型の標準だが停滞(reviewedへ)、waifu2x(2023-05)・Real-ESRGAN(2024-08)・realcugan-ncnn-vulkan(2023-03)は事実上メンテ停止。

関連リポジトリ:

- [AaronFeng753/Waifu2x-Extension-GUI](https://github.com/AaronFeng753/Waifu2x-Extension-GUI) — 超解像+補間の総合GUI（★17,102 / NOASSERTION / 最終push 2026-10-02 / release v3.142.01 (2026-10-02) / 確認コミット [`f73d2415`](https://github.com/AaronFeng753/Waifu2x-Extension-GUI/blob/f73d24156e843807cb99d5d4f8d4c595479c690a/README.md)）
  - ★17060、2026-09-02リリース。ライセンスはAPI上NOASSERTION(カスタム)なので要確認。【catalog.json未収録(新規)】
- [NevermindNilas/TheAnimeScripter](https://github.com/NevermindNilas/TheAnimeScripter) — 超解像・RIFE補間・復元のCLI/GUI（★332 / AGPL-3.0 / 最終push 2026-10-07 / release v2.10.0 (2026-09-20) / 確認コミット [`a4913ca9`](https://github.com/NevermindNilas/TheAnimeScripter/blob/a4913ca99e0ef4a8d7253f11f2ee6735752664b4/README.md)）
  - v2.10.0=2026-09-20、2026-09-28push。★329と小規模だが更新最速。AGPL-3.0。【catalog.json未収録(新規)】
- [the-database/VideoJaNai](https://github.com/the-database/VideoJaNai) — ONNX/TensorRT超解像+RIFE補間GUI（★281 / GPL-3.0 / 最終push 2026-06-18 / release 2.1.0 (2026-06-18) / 確認コミット [`68f6060c`](https://github.com/the-database/VideoJaNai/blob/68f6060c3971dfc0f2423b5702f2d259013eca60/README.md)）
  - 2026-06-18リリース。GPL-3.0。Windows GUI。【catalog.json未収録(新規)】
- [k4yt3x/video2x](https://github.com/k4yt3x/video2x) — Anime4K/Real-ESRGAN/RIFE統合フレームワーク（★22,111 / AGPL-3.0 / 最終push 2026-03-07 / release 6.4.0 (2025-01-24) / 確認コミット [`7db9c18d`](https://github.com/k4yt3x/video2x/blob/7db9c18d6278bbad9c3eda0e4e4ae210f9a688eb/README.md)）
  - ★21897でX上の実利用例も多いが、最新リリース6.4.0は2025-01-24で、最終push 2026-03-07と鈍化。AGPL-3.0。【catalog.json未収録(新規)】

## 漫画翻訳(検出・OCR以外のアプリ層)

<a id="repos-manga-translation"></a>
- **判定**: アニメ特化の最良 / 確度 高
- **選定基準と順位の根拠**: 事実: koharu-rs/koharu(★5693、Apache-2.0、0.83.5=2026-09-22)はRust製で日中英のローカル翻訳、X投稿(2026-09-25)で紹介あり。dmMaze/BallonsTranslator(★5171、GPL-3.0、v1.5.17=2026-09-27)は編集機能付きの定番。zyddnys/manga-image-translator(★10457、GPL-3.0、最新コミット2026-09-25、ただしリリースタグbeta-0.3は2022-04)はcatalog収録の老舗で、READMEが公式Web版は終了と記載。ogkalu2/comic-translate(★2959、Apache-2.0、v2.8.9=2026-09-11)。評価: 新規導入の第一候補は更新・ライセンス(Apache-2.0)・採用の3点でkoharu(検出モデルの詳細は他担当)。編集重視ならBallonsTranslator、既存資産・APIならmanga-image-translator。派生のhgmzhn/manga-translator-ui(★2895、2026-09-30push)とmeangrinch/MangaTranslator(★331)は次点。読書側はdoujin-asset-managementのmokuroを参照。

関連リポジトリ:

- [koharu-rs/koharu](https://github.com/koharu-rs/koharu) — ローカル完結の漫画翻訳(検出→OCR→消去→翻訳→植字)（★5,903 / Apache-2.0 / 最終push 2026-10-09 / release 0.83.5 (2026-09-22) / 確認コミット [`45b4cae1`](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md)）
  - ★5693、2026-09-22リリース、Apache-2.0。【catalog.json未収録(新規)】
- [dmMaze/BallonsTranslator](https://github.com/dmMaze/BallonsTranslator) — 編集UI付き漫画翻訳支援（★5,199 / GPL-3.0 / 最終push 2026-10-04 / release v1.5.19 (2026-10-04) / 確認コミット [`9c7863c1`](https://github.com/dmMaze/BallonsTranslator/blob/9c7863c1e10c5bd927312eca0a0860177b0e5539/README.md)）
  - ★5171、v1.5.17=2026-09-27。GPL-3.0。【catalog.json未収録(新規)】
- [zyddnys/manga-image-translator](https://github.com/zyddnys/manga-image-translator) — バッチ/API向け自動翻訳パイプライン（★10,490 / GPL-3.0 / 最終push 2026-09-25 / release beta-0.3 (2022-04-23) / 確認コミット [`441d07c5`](https://github.com/zyddnys/manga-image-translator/blob/441d07c59a735c7db3db2e7bb8b07920afd8a9cc/README.md) / 制作カタログ: [manga-image-translator](../categories/localization.md#manga-image-translator)）
  - ★10457で最大。リリースタグは2022-04止まりだがコミットは2026-09-25。GPL-3.0。【catalog.json収録: id=manga-image-translator】
- [ogkalu2/comic-translate](https://github.com/ogkalu2/comic-translate) — 多言語コミック翻訳デスクトップアプリ（★2,970 / Apache-2.0 / 最終push 2026-09-11 / release v2.8.9 (2026-09-11) / 確認コミット [`8977b91a`](https://github.com/ogkalu2/comic-translate/blob/8977b91a4f7a40c3917c5a268e9e7d78e1d818da/README.md)）
  - ★2959、v2.8.9=2026-09-11、Apache-2.0。【catalog.json未収録(新規)】

## ビジュアルノベル・ゲーム翻訳/テキストフック

<a id="repos-vn-game-translation"></a>
- **判定**: アニメ特化の最良 / 確度 高
- **選定基準と順位の根拠**: 事実: HIllya51/LunaTranslator(★13485、GPL-3.0、v10.17.1.12=2026-09-26)はVN翻訳のテキストフック+OCR+翻訳統合の本命。GalTransl/GalTransl(★2293、GPL-3.0、8.1.0=2026-09-27)はLLMでGalgameを自動翻訳し翻訳パッチ作成まで行う。SakuraLLM/SakuraLLM(★4793、GPL-3.0、v1.1.0=2024-05-10、最終push 2026-07-23)は軽小説/Galgame向け日中翻訳モデル。bpwhelan/GameSentenceMiner(★859、GPL-3.0、v2026.9.4=2026-09-26)は日本語学習向けゲーム文抽出。評価: 実用はLunaTranslator一択、パッチ制作はGalTransl。Artikash/Textractor(★2698)は最終push 2024-03で停滞(reviewedへ)。リアルタイムOCR型のkmonkeyhead/MORT(★1777、MIT)・thanhkeke97/RSTGameTranslation(★656)は次点。X上の実使用評判は取得できず(未確認)。

関連リポジトリ:

- [HIllya51/LunaTranslator](https://github.com/HIllya51/LunaTranslator) — VN向けフック/OCR/翻訳オーバーレイ（★13,650 / GPL-3.0 / 最終push 2026-10-09 / release v12.0.1 (2026-10-06) / 確認コミット [`363de635`](https://github.com/HIllya51/LunaTranslator/blob/363de6354ef9d085403f78f325cff5d69b97eda8/README.md)）
  - ★13485、2026-09-26リリース。GPL-3.0。【catalog.json未収録(新規)】
- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl) — LLMによるGalgame翻訳パッチ自動化（★2,312 / GPL-3.0 / 最終push 2026-10-09 / release 8.3.0 (2026-10-08) / 確認コミット [`ad04d23e`](https://github.com/GalTransl/GalTransl/blob/ad04d23e187dbc37db2de588e99a13b785127a3e/README.md)）
  - ★2293、8.1.0=2026-09-27、README中国語。【catalog.json未収録(新規)】
- [SakuraLLM/SakuraLLM](https://github.com/SakuraLLM/SakuraLLM) — Galgame/軽小説向け日中翻訳LLM（★4,811 / GPL-3.0 / 最終push 2026-07-23 / release v1.1.0 (2024-05-10) / 確認コミット [`0ff69116`](https://github.com/SakuraLLM/SakuraLLM/blob/0ff69116222ca66c7a15dcff00fd4f9f86b18d5c/README.md)）
  - ★4793。リリースは2024-05だがpushは2026-07。モデル重みはHF側。【catalog.json未収録(新規)】
- [bpwhelan/GameSentenceMiner](https://github.com/bpwhelan/GameSentenceMiner) — ゲーム文のAnki連携・学習ツール（★866 / GPL-3.0 / 最終push 2026-10-07 / release v2026.10.0 (2026-10-04) / 確認コミット [`7dac58bc`](https://github.com/bpwhelan/GameSentenceMiner/blob/7dac58bc1a54b2f2b953787f36d587a2aedeb176/README.md)）
  - ★859、v2026.9.4=2026-09-26。翻訳ではなく学習用途。【catalog.json未収録(新規)】

## VTuber/Live2D/VRM/アバター基盤

<a id="repos-vtuber-avatar"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **選定基準と順位の根拠**: 事実: pixiv/three-vrm(★2192、MIT、v3.5.5=2026-07-09)はWebのVRM標準ライブラリ。vrm-c/UniVRM(★3392、MIT、v0.131.2=2026-07-24)はUnity側の仕様実装。saturday06/VRM-Addon-for-Blender(★1716、MIT、v4.7.2=2026-09-23)はBlenderのVRM入出力(ローカルVRM Starter/Danceの編集経路に近い)。emilianavt/OpenSeeFace(★2080、BSD-2-Clause、v1.20.5=2026-09-14)は顔トラッキング。評価: いずれも公式/標準系で更新が活発。Inochi2D/inochi-creator(★1230)は最終push 2025-06で停滞、Live2D Cubism本体は公開リポジトリ無し。XR Animator(ButzYung/SystemAnimatorOnline ★1897、ライセンス未検出)はモーキャプ用の次点。AI対話統合は別カテゴリ(repos-ai-companion-chat)。

関連リポジトリ:

- [pixiv/three-vrm](https://github.com/pixiv/three-vrm) — Three.jsでVRMを扱う（★2,210 / MIT / 最終push 2026-10-02 / release v3.5.5 (2026-07-09) / 確認コミット [`1b4fc0cc`](https://github.com/pixiv/three-vrm/blob/1b4fc0cc7ef39a49d62bb7a66dcfeca8f65316f7/README.md) / 制作カタログ: [three-vrm](../categories/vtuber.md#three-vrm)）
  - ★2192、MIT。【catalog.json収録: id=three-vrm】
- [vrm-c/UniVRM](https://github.com/vrm-c/UniVRM) — Unity VRM実装（★3,392 / MIT / 最終push 2026-10-06 / release v0.131.3 (2026-10-02) / 確認コミット [`9750dadc`](https://github.com/vrm-c/UniVRM/blob/9750dadc592f421c356bf0376c73e61abbe323e3/README.md) / 制作カタログ: [univrm](../categories/vtuber.md#univrm)）
  - ★3392、MIT。【catalog.json収録: id=univrm】
- [saturday06/VRM-Addon-for-Blender](https://github.com/saturday06/VRM-Addon-for-Blender) — BlenderでのVRM入出力（★1,722 / MIT / 最終push 2026-10-09 / release v4.7.2 (2026-09-23) / 確認コミット [`6502ad98`](https://github.com/saturday06/VRM-Addon-for-Blender/blob/6502ad9852816ec2a391ed321a4932d45711c105/README.md)）
  - ★1716、v4.7.2=2026-09-23、MIT。【catalog.json未収録(新規)】
- [emilianavt/OpenSeeFace](https://github.com/emilianavt/OpenSeeFace) — CPU顔トラッキング（★2,083 / BSD-2-Clause / 最終push 2026-09-18 / release v1.20.5 (2026-09-14) / 確認コミット [`50c09741`](https://github.com/emilianavt/OpenSeeFace/blob/50c09741897010faad721a218b2bbe14ecad6251/README.md) / 制作カタログ: [openseeface](../categories/vtuber.md#openseeface)）
  - ★2080、v1.20.5=2026-09-14、BSD-2-Clause。【catalog.json収録: id=openseeface】

## AIコンパニオン・キャラチャット・AITuber

<a id="repos-ai-companion-chat"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **選定基準と順位の根拠**: 事実: moeru-ai/airi(★49887、MIT、v0.12.0-beta.5=2026-08-29)は自己ホスト型AIコンパニオン(VRM/Live2D)でX投稿が2026-07-26(likes4840)と2026-09-27/28(likes3000超)に拡散。SillyTavern/SillyTavern(★33968、AGPL-3.0、1.19.0=2026-09-14)はキャラチャットUIの標準。Open-LLM-VTuber(★13961、ライセンスNOASSERTION、最新コミット2026-05-15、v1.2.1=2025-08)は音声対話+Live2Dだが更新が鈍化。tegnike/aituber-kit(★1114、v2.78.1=2026-09-13、v2.0.0以降カスタムライセンスで商用条件あり)は日本語圏AITuber向け。評価: 新規はairiが勢い・MIT・更新で優先、チャット/ロールプレイはSillyTavern、日本語配信/商用はaituber-kitの規約確認が必要。人気の高い星数にはプロモ由来の可能性があり、airiの実利用品質は未検証。LingChat(★2288、AGPL-3.0)・uezo/aiavatarkit(★682、Apache-2.0)は次点。

関連リポジトリ:

- [moeru-ai/airi](https://github.com/moeru-ai/airi) — VRM/Live2D対応の自己ホスト型AIコンパニオン（★50,220 / MIT / 最終push 2026-10-09 / release v0.12.0-beta.5 (2026-08-29) / 確認コミット [`da2bcbd4`](https://github.com/moeru-ai/airi/blob/da2bcbd46f56c1c6ecb40d44fb60694e6599f11b/README.md) / 制作カタログ: [airi](../categories/vtuber.md#airi)）
  - ★49887。v0.12.0-beta.5=2026-08-29(ベータ)。MIT。【catalog.json収録: id=airi】
- [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) — キャラクターカード/ロールプレイチャットUI（★34,266 / AGPL-3.0 / 最終push 2026-10-02 / release 1.19.0 (2026-09-14) / 確認コミット [`06bde939`](https://github.com/SillyTavern/SillyTavern/blob/06bde939fb1e9c4c8d8641d810f0a916b5bce127/README.md) / 制作カタログ: [sillytavern](../categories/story.md#sillytavern)）
  - ★33968、1.19.0=2026-09-14、AGPL-3.0。【catalog.json収録: id=sillytavern】
- [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) — 音声対話+Live2Dの自己ホストVTuber（★14,026 / NOASSERTION / 最終push 2026-05-15 / release v1.2.1 (2025-08-26) / 確認コミット [`992309c0`](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/README.md) / 制作カタログ: [open-llm-vtuber](../categories/vtuber.md#open-llm-vtuber)）
  - ★13961。最終push 2026-05-15と約4.5か月停滞、ライセンスは独自(NOASSERTION)。【catalog.json収録: id=open-llm-vtuber】
- [tegnike/aituber-kit](https://github.com/tegnike/aituber-kit) — 日本語圏AITuber構築キット（★1,119 / NOASSERTION / 最終push 2026-10-04 / release v2.79.0 (2026-10-04) / 確認コミット [`c7ea2b65`](https://github.com/tegnike/aituber-kit/blob/c7ea2b65f99ac68bf0621c626b9dedf9c30e2c32/README.md)）
  - ★1114、2026-09-30push。v2.0.0以降カスタムライセンスで商用は利用規約確認が必須。【catalog.json未収録(新規)】

## 日本語キャラクター向けTTS/音声エンジン

<a id="repos-japanese-tts-voice"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **選定基準と順位の根拠**: 事実: Aratako/Irodori-TTS(★1363、MIT、2026-09-12push、タグ無し)は最近の日本語TTS話題作(Irodori-TTS v4.1はローカルComfyUI-Anime-Extensionsが採用)。VOICEVOX/voicevox_engine(★1764、2026-09-26push、0.25.2=2026-04-30、ライセンスNOASSERTION=独自規約、各音声の利用規約は別)。Aivis-Project/AivisSpeech-Engine(★181、LGPL-3.0、1.2.0=2026-04-30)はStyle-Bert-VITS2系でVOICEVOX互換API。RVC-Boss/GPT-SoVITS(★62272、MIT、v2pro=2025-06-06リリース、最終push 2026-08-18)は少数ショット声クローンの最大手。評価: 新規品質はIrodori、アプリ連携APIはVOICEVOX/AivisSpeech互換が標準、クローンはGPT-SoVITS。litagin02/Style-Bert-VITS2(★1378、AGPL-3.0、2.7.0=2025-08、最終push 2025-12-07)はcatalog収録の基盤だが更新停止気味(reviewedへ)。fish-speech(★32898)・index-tts(★24238)はライセンスNOASSERTION(独自)のため商用条件要確認。音声品質は未聴。

関連リポジトリ:

- [Aratako/Irodori-TTS](https://github.com/Aratako/Irodori-TTS) — 日本語TTS(キャラ声・VoiceDesign対応)（★1,417 / MIT / 最終push 2026-09-12 / 確認コミット [`89f9d8fb`](https://github.com/Aratako/Irodori-TTS/blob/89f9d8fbd4d51ea019867ee1197725ede1df13c5/README.md)）
  - ★1363、MIT、2026-09-12push。ローカルのComfyUI-Anime-Extensionsが利用。【catalog.json未収録(新規)】
- [VOICEVOX/voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) — HTTP APIの日本語音声合成エンジン（★1,768 / NOASSERTION / 最終push 2026-10-02 / release 0.25.2 (2026-04-30) / 確認コミット [`bfa93039`](https://github.com/VOICEVOX/voicevox_engine/blob/bfa9303947090b5e91e9917a43b997a5e27683a8/README.md)）
  - ★1764、2026-09-26push。ライセンスは独自(NOASSERTION)で音声ごとの規約を要確認。【catalog.json未収録(新規)】
- [Aivis-Project/AivisSpeech-Engine](https://github.com/Aivis-Project/AivisSpeech-Engine) — VOICEVOX互換APIのSBV2系エンジン（★182 / LGPL-3.0 / 最終push 2026-10-07 / release 1.2.0 (2026-04-30) / 確認コミット [`0cf0635d`](https://github.com/Aivis-Project/AivisSpeech-Engine/blob/0cf0635d5f74de4cf07e5fb87b25c4c1d0c8a331/README.md)）
  - ★181と小規模だが2026-09-18push、LGPL-3.0。【catalog.json未収録(新規)】
- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) — 少数ショット声クローンTTS(多言語)（★62,587 / MIT / 最終push 2026-10-08 / release 20250606v2pro (2025-06-06) / 確認コミット [`48b1a016`](https://github.com/RVC-Boss/GPT-SoVITS/blob/48b1a0169a28582a8984402f82cf438d3bfa6aca/README.md) / 制作カタログ: [gpt-sovits](../categories/tts.md#gpt-sovits)）
  - ★62272、MIT。最終リリース2025-06だがpush 2026-08-18。【catalog.json収録: id=gpt-sovits】

## アニメ制作向けエージェント・スキル・MCP

<a id="repos-agents-skills-mcp"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **選定基準と順位の根拠**: 事実: Comfy-Org/comfy-mcp(★242、2026-09-20push、v0.10.0=2026-08-10、ライセンスNOASSERTION)とComfy-Org/comfy-skills(★213、MIT)は公式。artokun/comfyui-mcp(★774)はREADME冒頭で『メンテ終了、公式Comfy Agent/MCPへ移行、2026-10-09にアーカイブ』と明記(reviewedへ)。Moeblack/ComfyUI-AnimaTool(★137、AGPL-3.0、最終push 2026-03-26)はAnima専用のツール呼び出しAPI。yuna0x0/anilist-mcp(★89、MIT、v1.4.0=2025-11-28、push 2026-07-13)はAniListデータ用MCP。評価: アニメ特化のAgent/Skill/MCPは小規模で突出したものは無く、制作実務は公式ComfyUI MCP+Animaワークフローが現実的。Danbooru検索MCP(echo-xianyu/danbooru-MCP ★12、ライセンス無し)は実績不足で不採用。

関連リポジトリ:

- [Comfy-Org/comfy-mcp](https://github.com/Comfy-Org/comfy-mcp) — ComfyUI公式ローカルMCPサーバ（★268 / NOASSERTION / 最終push 2026-10-09 / release v0.10.0 (2026-08-10) / 確認コミット [`e5f768d3`](https://github.com/Comfy-Org/comfy-mcp/blob/e5f768d31de21ea32829381cebdda5336492a8ac/README.md)）
  - 公式、★242、2026-09-20push。ライセンスはAPI上NOASSERTIONで要確認。【catalog.json未収録(新規)】
- [Comfy-Org/comfy-skills](https://github.com/Comfy-Org/comfy-skills) — ComfyUI公式スキル(Comfy Cloud向け)（★219 / MIT / 最終push 2026-10-08 / 確認コミット [`d50722a5`](https://github.com/Comfy-Org/comfy-skills/blob/d50722a53585d0ab4fd1909fd59294b978aad449/README.md)）
  - 公式、★213、MIT。タグ無し。Comfy Cloud向けでローカル用途とは異なる可能性。【catalog.json未収録(新規)】
- [Moeblack/ComfyUI-AnimaTool](https://github.com/Moeblack/ComfyUI-AnimaTool) — Anima画像生成のツール呼び出しAPI（★139 / AGPL-3.0 / 最終push 2026-03-26 / 確認コミット [`2a9c5fcb`](https://github.com/Moeblack/ComfyUI-AnimaTool/blob/2a9c5fcbbb5349956f93b16b74cfe94214e78b44/README.md)）
  - ★137。最終push 2026-03-26(約6か月前)、AGPL-3.0。【catalog.json未収録(新規)】
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) — AniList作品情報MCP（★90 / MIT / 最終push 2026-07-13 / release v1.4.0 (2025-11-28) / 確認コミット [`7c5cf1e3`](https://github.com/yuna0x0/anilist-mcp/blob/7c5cf1e374c09e3ddbd9c68f92c4c08a43e65477/README.md)）
  - ★89、MIT。作品メタデータ取得用で生成用途ではない。【catalog.json未収録(新規)】

## アニメ生成の評価・ベンチマーク

<a id="repos-evaluation-benchmarks"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **選定基準と順位の根拠**: 事実: RimoChan/stable-diffusion-anime-tag-benchmark(★53、2026-09-29push、ライセンス未設定)は各モデルがDanbooruタグを正しく描けるかを自動評価するツールで、READMEが結果と手法を掲載(中国語)。deepghs/sdeval(★27、Apache-2.0、v0.0.4=2024-01)は最終push 2024-08で停滞。smilingzerotwo/WorldCharBench(★0、パイロット)は作品世界との整合を診断するが実績なし。評価: 定評ある標準ベンチは見つからず、最有力でも★53と弱い。選定は暫定で、Animaの評価は実画像比較に頼るのが現実的。論文側ではAnime-2026データセット(ACM)が検索で見つかったがコード/ライセンス未確認。

関連リポジトリ:

- [RimoChan/stable-diffusion-anime-tag-benchmark](https://github.com/RimoChan/stable-diffusion-anime-tag-benchmark) — タグ理解度の自動評価（★53 / ライセンス未表示 / 最終push 2026-09-29 / 確認コミット [`66b12afb`](https://github.com/RimoChan/stable-diffusion-anime-tag-benchmark/blob/66b12afbcb081e1075711f4c09cb11b99f85c8c0/README.md)）
  - ★53と小規模。ライセンス未設定のため再利用条件不明。【catalog.json未収録(新規)】
- [deepghs/sdeval](https://github.com/deepghs/sdeval) — SD出力の評価ユーティリティ（★27 / Apache-2.0 / 最終push 2024-08-24 / release v0.0.4 (2024-01-26) / 確認コミット [`d66c5db4`](https://github.com/deepghs/sdeval/blob/d66c5db4a18dfa3ee1e065129a20f472e55fd0f8/README.md)）
  - Apache-2.0だが最終push 2024-08-24で停滞。【catalog.json未収録(新規)】 【要注意: pushed_atが12か月超で停滞】

## アニメ/漫画データセット・アノテーションツール

<a id="repos-dataset-annotation"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **選定基準と順位の根拠**: 事実: cvat-ai/cvat(★16827、MIT、v2.77.0=2026-09-28)とHumanSignal/label-studio(★28383、Apache-2.0、1.23.2=2026-09-29)は汎用だが活発なアノテーション基盤で、吹き出し/コマ検出ラベル付けに流用可能。manga109/public-annotations(★14、CC-BY-4.0、2025-04-23)はManga109の注釈、manga109/manga109api(★132、MIT、最終push 2022-03)は読み込みAPIだが停滞。評価: アニメ/漫画特化のアノテーションツールで有力なものは見つからず、CVATまたはLabel Studioを使うのが安全。Manga109画像本体は学術・非商用条件があるため各自で利用条件を確認すること(本調査では原文未確認)。HumanSignal/labelImgはアーカイブ済み。

関連リポジトリ:

- [cvat-ai/cvat](https://github.com/cvat-ai/cvat) — 画像アノテーション基盤(BBox/ポリゴン)（★16,888 / MIT / 最終push 2026-10-09 / release v2.78.0 (2026-10-06) / 確認コミット [`fadcbac2`](https://github.com/cvat-ai/cvat/blob/fadcbac254ba83436afefe7dbeff8c752d83608d/README.md)）
  - ★16827、MIT、2026-09-28リリース。【catalog.json未収録(新規)】
- [HumanSignal/label-studio](https://github.com/HumanSignal/label-studio) — 汎用アノテーション(画像/テキスト/音声)（★28,430 / Apache-2.0 / 最終push 2026-10-09 / release 1.23.2 (2026-09-29) / 確認コミット [`a6387435`](https://github.com/HumanSignal/label-studio/blob/a63874354e5fd18f4613d59c47dee136f8b29b5f/README.md)）
  - ★28383、Apache-2.0。【catalog.json未収録(新規)】
- [manga109/public-annotations](https://github.com/manga109/public-annotations) — Manga109注釈データ（★14 / CC-BY-4.0 / 最終push 2025-04-23 / 確認コミット [`fd20965a`](https://github.com/manga109/public-annotations/blob/fd20965a079c309deeb4f44bbed5d2ebabb2b493/README.md)）
  - ★14、CC-BY-4.0。画像自体の条件は別。【catalog.json未収録(新規)】 【要注意: pushed_atが12か月超で停滞】
- [manga109/manga109api](https://github.com/manga109/manga109api) — Manga109読み込みAPI（★132 / MIT / 最終push 2022-03-04 / 確認コミット [`94aaa1a8`](https://github.com/manga109/manga109api/blob/94aaa1a8d81266bdecc420eb9151f2924087d151/README.md)）
  - ★132、MIT。最終push 2022-03-04で停滞。【catalog.json未収録(新規)】 【要注意: pushed_atが12か月超で停滞】

## 同人・漫画・画像アセット管理と閲覧

<a id="repos-doujin-asset-management"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **選定基準と順位の根拠**: 事実: gotson/komga(★6703、MIT、1.28.0=2026-09-29)は漫画/コミックのメディアサーバ(OPDS対応)。hydrusnetwork/hydrus(★3218、v688=2026-09-23、ライセンスNOASSERTION)は個人booru型タグ管理。kha-white/mokuro(★1738、GPL-3.0、v0.2.5=2026-07-20)はOCR付き漫画読書用HTML生成でcatalog収録。monbooru/monbooru(★82、AGPL-3.0、v1.22.0=2026-09-28)はAI生成画像向けのローカルbooru、WD14等のONNXタグ付け対応をREADMEが記載。評価: 蔵書はKomga、画像タグ管理はHydrus、日本語学習/OCR閲覧はmokuro、AI生成物整理はmonbooru(小規模で新しい)。Kavita(★11784、GPL-3.0)も同格で、好みで選択(reviewedへ)。同人誌専用の有力管理repoは見つからず。

関連リポジトリ:

- [gotson/komga](https://github.com/gotson/komga) — 漫画・コミックサーバ（★6,727 / MIT / 最終push 2026-10-08 / release 1.28.1 (2026-10-02) / 確認コミット [`4fbcb1aa`](https://github.com/gotson/komga/blob/4fbcb1aa8a4990421f58b953c7aec3ba68b4de6f/README.md)）
  - ★6703、2026-09-29リリース、MIT。【catalog.json未収録(新規)】
- [hydrusnetwork/hydrus](https://github.com/hydrusnetwork/hydrus) — ローカル画像のタグ管理(booru型)（★3,234 / NOASSERTION / 最終push 2026-10-08 / release v689 (2026-09-30) / 確認コミット [`48194310`](https://github.com/hydrusnetwork/hydrus/blob/4819431092ed000c13011f17272c5222aec4ed2d/README.md)）
  - ★3218、リリース頻繁(v688=2026-09-23)。ライセンスはAPI上NOASSERTIONで要確認。【catalog.json未収録(新規)】
- [kha-white/mokuro](https://github.com/kha-white/mokuro) — OCR付き漫画リーダ生成（★1,744 / GPL-3.0 / 最終push 2026-07-20 / release v0.2.5 (2026-07-20) / 確認コミット [`9f79b128`](https://github.com/kha-white/mokuro/blob/9f79b1281066f953ec6e5d1e7086c401fa8da159/README.md) / 制作カタログ: [mokuro](../categories/localization.md#mokuro)）
  - ★1738、v0.2.5=2026-07-20、GPL-3.0。【catalog.json収録: id=mokuro】
- [monbooru/monbooru](https://github.com/monbooru/monbooru) — AI生成画像対応のセルフホストbooru（★93 / AGPL-3.0 / 最終push 2026-09-28 / release v1.22.0 (2026-09-28) / 確認コミット [`f49d97e4`](https://github.com/monbooru/monbooru/blob/f49d97e45de899e4413bc5239c4efe3e799fdf2d/README.md)）
  - ★82と小規模、AGPL-3.0、2026-09-28リリース。【catalog.json未収録(新規)】

## アニメ制作(作画・中割り・彩色・2D制作ツール)

<a id="repos-animation-production"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **選定基準と順位の根拠**: 事実: opentoonz/opentoonz(★7775、v1.8.0=2026-06-19、ライセンスNOASSERTION、2D制作ソフト)。KDE/krita(★10456、GPL-3.0)はペイント本体で、Acly/krita-ai-diffusion(★10655、GPL-3.0、v1.53.0=2026-08-22)がAI生成を統合。zhuang2002/Cobra(★253、Apache-2.0、SIGGRAPH 2025、線画彩色、2026-08-15push)とMarkMoHR/LayerInbetween(★12、GPL-3.0、SIGGRAPH 2026、中割り研究コード)は研究実装。評価: 制作環境はOpenToonz+Krita、AI彩色/中割りは研究コード段階で実運用の定番は未確立。ToonCrafter(★6030、2025-03)、ToonComposer(2025-08)、BasicPBC(2025-06)は12か月前後以上停滞(reviewedへ)。アニメ向けAI中割りの決定版は見つからず。

関連リポジトリ:

- [opentoonz/opentoonz](https://github.com/opentoonz/opentoonz) — 2Dアニメ制作ソフト（★7,806 / NOASSERTION / 最終push 2026-10-09 / release v1.8.0 (2026-06-19) / 確認コミット [`58f2ed14`](https://github.com/opentoonz/opentoonz/blob/58f2ed1413ee1041f6f643cd91c807318a323009/README.md) / 制作カタログ: [opentoonz](../categories/animation.md#opentoonz)）
  - ★7775、v1.8.0=2026-06-19。GitHub API上ライセンスはNOASSERTION(要確認)。【catalog.json収録: id=opentoonz】
- [KDE/krita](https://github.com/KDE/krita) — デジタルペイント本体（★10,509 / GPL-3.0 / 最終push 2026-10-09 / 確認コミット [`4216dd34`](https://github.com/KDE/krita/blob/4216dd347f843d59ca51c1e097a0dc8af7c753aa/README.md) / 制作カタログ: [krita](../categories/manga.md#krita)）
  - ★10456、GPL-3.0。catalog収録。【catalog.json収録: id=krita】
- [Acly/krita-ai-diffusion](https://github.com/Acly/krita-ai-diffusion) — KritaのAI生成プラグイン（★10,683 / GPL-3.0 / 最終push 2026-10-03 / release v1.53.0 (2026-08-22) / 確認コミット [`26aec6c6`](https://github.com/Acly/krita-ai-diffusion/blob/26aec6c6d8e1b7c1a3cf63880fda84360f6d5b0d/README.md) / 制作カタログ: [krita-ai-diffusion](../categories/image.md#krita-ai-diffusion)）
  - ★10655、v1.53.0=2026-08-22、GPL-3.0。【catalog.json収録: id=krita-ai-diffusion】
- [zhuang2002/Cobra](https://github.com/zhuang2002/Cobra) — 線画の参照ベース自動彩色(研究)（★254 / Apache-2.0 / 最終push 2026-08-15 / 確認コミット [`48d61688`](https://github.com/zhuang2002/Cobra/blob/48d6168838e05fbb707f393441219069aa33733b/README.md)）
  - ★253、Apache-2.0。研究コードで運用品質は未検証。【catalog.json未収録(新規)】

## 絵コンテ・AI短編ドラマ制作パイプライン

<a id="repos-storyboard-pipeline"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **選定基準と順位の根拠**: 事実: Forget-C/Jellyfish(★6529、Apache-2.0、v0.3.2=2026-04-17、日本語README有)は脚本→絵コンテ→画像/動画生成→書き出しを統合するAI短編制作ワークスペース。ArcReel/ArcReel(★5253、AGPL-3.0、v0.31.0=2026-09-23)はREADME冒頭にスポンサー広告(動画API)があり、商用誘導の要素あり。評価: アニメ特化ではなく汎用の短編動画制作で、いずれも中国圏中心。実績の客観根拠(ベンチ・第三者評価)は未確認でスター数の一部は宣伝由来の可能性がある。wonderunit/storyboarder(★3859)は最終push 2024-03で停滞(catalog収録)。dramaclaw・waoowaooは宣伝色が強く不採用(reviewedへ)。

関連リポジトリ:

- [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) — 脚本→絵コンテ→動画のAI短編制作ワークスペース（★6,640 / Apache-2.0 / 最終push 2026-07-30 / release v0.3.2 (2026-04-17) / 確認コミット [`a9678194`](https://github.com/Forget-C/Jellyfish/blob/a9678194ddf2d9be3ccbe78d4287d87d5089e123/README.md)）
  - ★6529、Apache-2.0。最終push 2026-07-30。【catalog.json未収録(新規)】
- [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) — 小説/脚本→動画のセルフホスト制作台（★5,404 / AGPL-3.0 / 最終push 2026-10-09 / release v0.33.0 (2026-10-08) / 確認コミット [`ff809bca`](https://github.com/ArcReel/ArcReel/blob/ff809bcab6480892cf135a5951b011201bb1e3d6/README.md)）
  - ★5253、2026-09-30push。READMEにスポンサー/販促あり、AGPL-3.0。【catalog.json未収録(新規)】
- [wonderunit/storyboarder](https://github.com/wonderunit/storyboarder) — 絵コンテ作成ソフト（★3,871 / ライセンス未表示 / 最終push 2024-03-17 / release v2.1.0 (2020-09-03) / 確認コミット [`8b81a25c`](https://github.com/wonderunit/storyboarder/blob/8b81a25c71d5f7ca46e8d5b8e3d4f7b3968f95c2/README.md) / 制作カタログ: [storyboarder](../categories/production.md#storyboarder)）
  - ★3859だが最終push 2024-03-17で停滞。catalog収録のため参照用。【catalog.json収録: id=storyboarder】 【要注意: pushed_atが12か月超で停滞】

## 漫画の植字・フォント・テキスト描画

<a id="repos-manga-typesetting"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **選定基準と順位の根拠**: 事実: 専用の有力リポジトリは見つからず。koharuは検出→消去→翻訳→植字を一体化(READMEの処理手順をX投稿2026-09-25も説明)、BallonsTranslatorはテキスト編集UIを持つ。komiq-cc/manga-typesetter(★13、MIT、v0.3.1=2026-09-11)は吹き出し配置に特化したTauriアプリで新しいが実績は皆無。評価: 植字は翻訳アプリ内機能で足りるのが現状。フォント選定は専用repoではなく各自でライセンス確認が必要(調査で該当リポジトリ未発見)。

関連リポジトリ:

- [koharu-rs/koharu](https://github.com/koharu-rs/koharu) — 翻訳一体型の植字（★5,903 / Apache-2.0 / 最終push 2026-10-09 / release 0.83.5 (2026-09-22) / 確認コミット [`45b4cae1`](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md)）
  - 植字機能を含む。★5693、Apache-2.0、2026-09-22リリース。【catalog.json未収録(新規)】
- [dmMaze/BallonsTranslator](https://github.com/dmMaze/BallonsTranslator) — テキスト編集UI付き植字（★5,199 / GPL-3.0 / 最終push 2026-10-04 / release v1.5.19 (2026-10-04) / 確認コミット [`9c7863c1`](https://github.com/dmMaze/BallonsTranslator/blob/9c7863c1e10c5bd927312eca0a0860177b0e5539/README.md)）
  - ★5171、v1.5.17=2026-09-27、GPL-3.0。【catalog.json未収録(新規)】
- [komiq-cc/manga-typesetter](https://github.com/komiq-cc/manga-typesetter) — 吹き出し内レタリング専用デスクトップアプリ（★13 / MIT / 最終push 2026-09-11 / release v0.3.1 (2026-09-11) / 確認コミット [`ef961771`](https://github.com/komiq-cc/manga-typesetter/blob/ef9617719babb664e62e6f151501030701217a99/README.md)）
  - ★13と極小規模、MIT、v0.3.1=2026-09-11。【catalog.json未収録(新規)】
