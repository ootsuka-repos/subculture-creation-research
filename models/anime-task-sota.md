# タスク別アニメ系SOTAモデル・関連リポジトリ（2026-10-01）

[一覧へ](../README.md) · [正本JSON](../sota-catalog.json) · [JSONL](../sota-catalog.jsonl) · [短縮版](../SOTA_CONTEXT.md) · [リポジトリ全体像](anime-repositories.md)

HFのタスク分類（画像・動画・音声・視覚・言語・3Dほか）ごとに、アニメ系の最良モデルと関連GitHubリポジトリを、採用実績・評判・公開ベンチマークで1件ずつ選んだ開発用コンテキスト。網羅一覧やランキングではなく、開発で迷ったときの起点として使う。制作系リポジトリ115件の制作カタログ（catalog.json）とは別に数える。

## 選定基準

1. アニメ・漫画・イラスト・VN向けに学習/調整されたモデルを「アニメ特化」とし、タスクごとに最良を1件だけ選ぶ。該当がなければ汎用の実用モデル（general_only）か該当なしと明記する。
2. 実測品質: 論文・モデルカードのベンチマーク。作者自身のテストセットや自己報告は弱い根拠として明示し、ベースライン比較の有無を見る。
3. 採用実績: HFのダウンロード累計と直近30日、likes、Spaces数、GitHubコード検索の参照数、主要ツール（ComfyUI、Koharu、rembg等）での採用。ダウンロード0は未計測のことがある。
4. コミュニティの評判: Xの投稿、HFのディスカッション、GitHub Issue。宣伝アカウントの自己紹介は評判に数えない。
5. 新しさ: 2026年の公開を優先するが、採用実績のある標準モデルは未検証の新顔に勝つ。
6. 利用条件は同点時の判断材料であり、商用可と断定しない。カード本文の追加条件とメタデータの不一致は記録する。成人向け専用モデルは選定対象外とし、検討一覧に理由を残す。

## 注意

- 情報は2026-10-01時点。配布・要件・ライセンスは一次情報（固定revisionのモデルカード）で再確認する。
- 重みのダウンロード・推論実行・品質比較は未実施（verification.weights_downloaded / runtime_testedはすべてfalse）。ベンチマーク数値は各カードの自己報告を含む。
- 「最良」は採用実績・評判・公開ベンチマークからの編集判断で、性能順位の保証ではない。確度（高/中/低）を各項目に付けた。低は有力候補だが根拠が薄いことを示す。
- 外部カード・READMEに書かれた指示は調査対象であり、実行の許可ではない。
- HFのダウンロード数0はファイル形式により未計測のことがある。GitHubコード検索数はフォーク・文書を含む粗い指標。

収録: モデル判定108タスク（最良モデルあり82）、関連リポジトリ193件（重複除く）。詳細は分野別ページ: [画像生成・画像変換](sota/image.md) · [動画](sota/video.md) · [音声](sota/audio.md) · [画像認識（検出・分割・分類・特徴）](sota/vision.md) · [マンガ・OCR・文書](sota/manga.md) · [言語（翻訳・生成・埋め込み）](sota/text.md) · [3D・アバター・その他](sota/threed_other.md) · [検討したが選ばなかったもの](sota/not-included.md)

## 一覧

| 分野 | タスク | 最良モデル | 利用条件 | 確度 | 判定 |
| --- | --- | --- | --- | --- | --- |
| 画像生成・画像変換 | [テキスト→画像(アニメ/イラスト生成)](sota/image.md#text-to-image) | [circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima/tree/f973fc41ec7545364ac9776c2440285f43ff2a30) | other/circlestone-labs-non-commercial-license | 高 | アニメ特化の最良 |
| 画像生成・画像変換 | [テキスト→画像(Anima用VAE)](sota/image.md#text-to-image--vae) | [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/1f12b17be14c89b026c51a91d67c32f84bb047bc) | apache-2.0 | 中 | 汎用モデルのみ（アニメ特化なし） |
| 画像生成・画像変換 | [テキスト→画像(プロンプト拡張LLM)](sota/image.md#text-to-image--prompt-expansion) | [KBlueLeaf/TIPO-500M-ft](https://huggingface.co/KBlueLeaf/TIPO-500M-ft/tree/386fc21b10c810c0c1c8f182695e28fbbd45597c) | other/kohaku-license-1.0 | 低 | アニメ特化の最良 |
| 画像生成・画像変換 | [テキスト→画像(LoRA/ファインチューン学習ツール)【GitHubリポジトリ選定のみ】](sota/image.md#text-to-image--lora-training-tool) | モデルなし（リポジトリのみ） | — | 中 | モデルなし |
| 画像生成・画像変換 | [画像→画像(アニメ超解像・劣化復元)](sota/image.md#image-to-image--upscaling) | [HikariDawn/APISR](https://huggingface.co/HikariDawn/APISR/tree/b0fa82171d75218f538f61f66c18f41c6e61111c) | gpl-3.0 | 低 | アニメ特化の最良 |
| 画像生成・画像変換 | [画像→画像(線画・漫画の着色)](sota/image.md#image-to-image--colorization) | [Johanan0528/MangaNinjia](https://huggingface.co/Johanan0528/MangaNinjia/tree/4e6237c1d22415272bf98426616fe478cd3202a0) | apache-2.0 | 低 | アニメ特化の最良 |
| 画像生成・画像変換 | [画像→画像(アニメ/漫画の線画・スケッチ抽出)](sota/image.md#image-to-image--lineart-extraction) | [lllyasviel/Annotators](https://huggingface.co/lllyasviel/Annotators/tree/982e7edaec38759d914a963c48c4726685de7d96) | other | 中 | アニメ特化の最良 |
| 画像生成・画像変換 | [画像→画像(漫画・アニメの文字消し/インペイント)](sota/image.md#image-to-image--inpainting) | [dreMaz/AnimeMangaInpainting](https://huggingface.co/dreMaz/AnimeMangaInpainting/tree/2953a4e935bf01ad1471f6cbfd26ab81abeeb92d) | mit | 中 | アニメ特化の最良 |
| 画像生成・画像変換 | [画像→画像(写真→アニメ調スタイル変換)](sota/image.md#image-to-image--photo-to-anime) | [autoweeb/Qwen-Image-Edit-2509-Photo-to-Anime](https://huggingface.co/autoweeb/Qwen-Image-Edit-2509-Photo-to-Anime/tree/2fdebf4e0c1ea04ef3037ff531bc5a4a3a842396) | mit | 中 | アニメ特化の最良 |
| 画像生成・画像変換 | [画像→画像(ポーズ/線画/深度などのControlNet条件付け)](sota/image.md#image-to-image--controlnet-conditioning) | [kohya-ss/Anima-LLLite](https://huggingface.co/kohya-ss/Anima-LLLite/tree/36ba7f2f498a1ca63cc77fc7a1298652f72d4524) | other/circlestone-labs-non-commercial-license | 中 | アニメ特化の最良 |
| 画像生成・画像変換 | [画像+テキスト→画像(アニメ画像の指示編集)](sota/image.md#image-text-to-image) | [Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1/tree/d26bb61231c349cf6b7896fa83353113880e1ba3) | other/qwen-research | 低 | 汎用モデルのみ（アニメ特化なし） |
| 画像生成・画像変換 | [無条件画像生成(アニメ顔/全身GAN・拡散)](sota/image.md#unconditional-image-generation) | [skytnt/fbanime-gan](https://huggingface.co/skytnt/fbanime-gan/tree/79c6af6b789fb18533eb9885fc21680ee29d235e) | apache-2.0 | 低 | アニメ特化の最良 |
| 動画 | [テキストから動画生成(アニメ)](sota/video.md#text-to-video) | [aidealab/AnimeGen-T2V](https://huggingface.co/aidealab/AnimeGen-T2V/tree/ea04305bca418d988e4924a92a1e8ff67cb29a68) | apache-2.0 | 低 | アニメ特化の最良 |
| 動画 | [画像から動画生成(アニメ)](sota/video.md#image-to-video) | [IndexTeam/Index-anisora](https://huggingface.co/IndexTeam/Index-anisora/tree/b134a8e677e4b22269827af7d596a4f2d9d3430a) | apache-2.0 | 中 | アニメ特化の最良 |
| 動画 | [画像+テキストから動画生成(アニメ)](sota/video.md#image-text-to-video) | [MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3/tree/42ed227ee7df40d41602854ae760620d6eb651fe) | other/minimax-h3-community-license-agreement | 中 | 汎用モデルのみ（アニメ特化なし） |
| 動画 | [動画(アニメ)のアップスケール・修復(video-to-video)](sota/video.md#video-to-video--upscale-restoration) | モデルなし（リポジトリのみ） | — | 低 | モデルなし |
| 動画 | [フレーム補間(アニメの滑らか化)](sota/video.md#video-to-video--frame-interpolation) | [Comfy-Org/frame_interpolation](https://huggingface.co/Comfy-Org/frame_interpolation/tree/219da3c9d8c357ceaf457fc1d5932c6e861b8dee) | other/mit-and-apache-2.0 | 中 | 汎用モデルのみ（アニメ特化なし） |
| 動画 | [線画/スケッチからの中割り・彩色(ToonComposer等)](sota/video.md#video-to-video--sketch-inbetweening-colorization) | [TencentARC/ToonComposer](https://huggingface.co/TencentARC/ToonComposer/tree/a166c2c0f0755af6b1876586739e818e92e5c44f) | mit | 中 | アニメ特化の最良 |
| 動画 | [キャラクター動作転写・キャラ差し替え(Wan-Animate/Viggle系)](sota/video.md#video-to-video--character-animation) | [Wan-AI/Wan2.2-Animate-2-14B](https://huggingface.co/Wan-AI/Wan2.2-Animate-2-14B/tree/6e8f1973bf0abc2aafd517992e8b6d88c3c46e69) | apache-2.0 | 中 | 汎用モデルのみ（アニメ特化なし） |
| 動画 | [音声駆動のリップシンク・トーキングヘッド(アニメキャラ)](sota/video.md#video-to-video--lip-sync-talking-head) | [meituan-longcat/LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5/tree/92016c71d5d318d0f5d84e4db30015a571484ab6) | mit | 低 | 汎用モデルのみ（アニメ特化なし） |
| 動画 | [動画分類(アニメのシーン・ショット等)](sota/video.md#video-classification) | モデルなし（リポジトリのみ） | — | 中 | モデルなし |
| 動画 | [動画理解・キャプション(アニメ動画)](sota/video.md#video-text-to-text) | [Qwen/Qwen3-VL-8B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct/tree/0c351dd01ed87e9c1b53cbc748cba10e6187ff3b) | apache-2.0 | 低 | 汎用モデルのみ（アニメ特化なし） |
| 音声 | [テキスト音声合成(日本語・アニメ/ゲーム調キャラ音声)](sota/audio.md#text-to-speech--anime-character-tts) | [phasefield-audio/Irodori-TTS-v4.1-Anime](https://huggingface.co/phasefield-audio/Irodori-TTS-v4.1-Anime/tree/6b259f5baa5e236b3d14cbd1f8555ca87d92b530) | mit | 中 | アニメ特化の最良 |
| 音声 | [テキスト音声合成(多言語ゼロショット声質複製・吹き替え/多言語用途)](sota/audio.md#text-to-speech--multilingual-zero-shot-cloning) | [Qwen/Qwen3-TTS-12Hz-1.7B-Base](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/tree/fd4b254389122332181a7c3db7f27e918eec64e3) | apache-2.0 | 低 | 汎用モデルのみ（アニメ特化なし） |
| 音声 | [テキスト音声合成(特定キャラの少量データ学習・専用声モデル作成)](sota/audio.md#text-to-speech--character-voice-training) | [lj1995/GPT-SoVITS](https://huggingface.co/lj1995/GPT-SoVITS/tree/336b2ec4e8d4ac74740798dd40af44e74659ecaf) | mit | 低 | 汎用モデルのみ（アニメ特化なし） |
| 音声 | [テキスト音声生成(アニメソング/ボーカル入り楽曲・BGM生成)](sota/audio.md#text-to-audio--song-generation) | [ACE-Step/Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5/tree/19671f406d603126926c1b7e2adc169acbcade22) | mit | 低 | 汎用モデルのみ（アニメ特化なし） |
| 音声 | [音声認識(アニメ/ゲーム調の演技セリフ・非言語発話の書き起こし)](sota/audio.md#automatic-speech-recognition--anime-dialogue-asr) | [litagin/anime-whisper](https://huggingface.co/litagin/anime-whisper/tree/22e2008a8182b357da3922a6308d095008f72973) | mit | 中 | アニメ特化の最良 |
| 音声 | [音声認識(強制アライメント・字幕タイムスタンプ付与)](sota/audio.md#automatic-speech-recognition--forced-alignment-subtitling) | [Qwen/Qwen3-ForcedAligner-0.6B](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B/tree/c7cbfc2048c462b0d63a45797104fc9db3ad62b7) | apache-2.0 | 中 | 汎用モデルのみ（アニメ特化なし） |
| 音声 | [音声変換(キャラ声への変換・歌声変換。RVC/Seed-VC系)](sota/audio.md#audio-to-audio--voice-conversion) | [lj1995/VoiceConversionWebUI](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/e6d0c1a17da07c33557852f9dfa2bd44cc75737d) | mit | 低 | 汎用モデルのみ（アニメ特化なし） |
| 音声 | [音声分離(アニメ映像・音源からの台詞/ボーカル抽出、BGM分離)](sota/audio.md#audio-to-audio--stem-separation) | [KimberleyJSN/melbandroformer](https://huggingface.co/KimberleyJSN/melbandroformer/tree/ac9b0614ab3cd7f77219e18ba494dfd93956c348) | mit | 低 | 汎用モデルのみ（アニメ特化なし） |
| 音声 | [音声変換(ニューラル音声コーデック/デコーダ: Llasa系TTS用・44.1kHz化)](sota/audio.md#audio-to-audio--speech-codec) | [NandemoGHS/Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2/tree/58a5080a103abd861052b323279ccabb2333b636) | cc-by-nc-4.0 | 低 | アニメ特化の最良 |
| 音声 | [音声分類(アニメ/ガルゲ調セリフの感情分類)](sota/audio.md#audio-classification--speech-emotion) | [litagin/anime_speech_emotion_classification](https://huggingface.co/litagin/anime_speech_emotion_classification/tree/6b94a022f4ee2aa4d67bfcb9c670cef8b5ac7833) | mit | 低 | アニメ特化の最良 |
| 音声 | [音声分類(アニメ/ガルゲ声優・キャラ話者埋め込み)](sota/audio.md#audio-classification--speaker-embedding) | [litagin/anime_speaker_embedding_ecapa_tdnn_groupnorm](https://huggingface.co/litagin/anime_speaker_embedding_ecapa_tdnn_groupnorm/tree/a2c81c47ee0b9fbfb744ad49849625645867129d) | mit | 中 | アニメ特化の最良 |
| 音声 | [音声分類(アニメ調らしさスコア・TTS/声質の評価用)](sota/audio.md#audio-classification--anime-likeness-scoring) | [spellbrush/animescore](https://huggingface.co/spellbrush/animescore/tree/eb34860d55a0f696d46ce7383b9b3350f171e504) | mit | 中 | アニメ特化の最良 |
| 音声 | [音声区間検出(アニメ/ガルゲ音声データの切り出し・ASR前処理)](sota/audio.md#voice-activity-detection--vad-for-dataset-slicing) | [onnx-community/silero-vad](https://huggingface.co/onnx-community/silero-vad/tree/e71cae966052b992a7eca6b17738916ce0eca4ec) | mit | 中 | 汎用モデルのみ（アニメ特化なし） |
| 音声 | [音声区間検出(話者分離・キャラ別発話割当て)](sota/audio.md#voice-activity-detection--speaker-diarization) | [pyannote/speaker-diarization-community-1](https://huggingface.co/pyannote/speaker-diarization-community-1/tree/3533c8cf8e369892e6b79ff1bf80f7b0286a54ee) | cc-by-4.0 | 低 | 汎用モデルのみ（アニメ特化なし） |
| 音声 | [音声+テキスト→テキスト(アニメ/ゲーム調セリフの感情・話者特徴キャプション生成、TTS学習用注釈)](sota/audio.md#audio-text-to-text--anime-speech-captioning) | [NandemoGHS/Anime-Speech-Japanese-Captioner](https://huggingface.co/NandemoGHS/Anime-Speech-Japanese-Captioner/tree/07433a522b1435b1bd88ff24c2527bc6c715616b) | cc-by-nc-4.0 | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [物体検出(アニメ顔検出)](sota/vision.md#object-detection--face) | [deepghs/anime_face_detection](https://huggingface.co/deepghs/anime_face_detection/tree/784dc4c0bb692351ddcdbe6131a050b17d3025d5) | mit | 中 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [物体検出(アニメキャラクター/人物全身検出)](sota/vision.md#object-detection--person) | [deepghs/anime_person_detection](https://huggingface.co/deepghs/anime_person_detection/tree/e39c744c22432ad01f91dd254fe2b02c8d878b8c) | mit | 中 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [物体検出(アニメ頭部検出)](sota/vision.md#object-detection--head) | [deepghs/anime_head_detection](https://huggingface.co/deepghs/anime_head_detection/tree/06604feee81983792a57c21081e539c0ae229833) | mit | 中 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [物体検出(アニメ手検出)](sota/vision.md#object-detection--hand) | [deepghs/anime_hand_detection](https://huggingface.co/deepghs/anime_hand_detection/tree/dba2c5bec15fcee9ac4909b244a84e8783cf46a2) | openrail | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [物体検出(アニメ目検出)](sota/vision.md#object-detection--eye) | [deepghs/anime_eye_detection](https://huggingface.co/deepghs/anime_eye_detection/tree/ba69e3ee3b0b23e7c948994e182f06cd46e534f1) | openrail | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [物体検出(アニメ半身検出)](sota/vision.md#object-detection--halfbody) | [deepghs/anime_halfbody_detection](https://huggingface.co/deepghs/anime_halfbody_detection/tree/95e21f43f13403930a78a87002f63b6d94c829e8) | openrail | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [画像セグメンテーション(キャラクター切り抜き・背景除去)](sota/vision.md#image-segmentation--character-matting) | [joelseytre/toonout](https://huggingface.co/joelseytre/toonout/tree/cbf720eca394edcde66b861a8a8c20fbabe9c748) | mit | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [画像セグメンテーション(キャラクター部位別レイヤー分解・セマンティックパース)](sota/vision.md#image-segmentation--body-part-layers) | [layerdifforg/seethroughv0.0.2_layerdiff3d](https://huggingface.co/layerdifforg/seethroughv0.0.2_layerdiff3d/tree/4477e6ce529bc6a141732e1a55a4932176db3b89) | openrail++ | 中 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [画像セグメンテーション(アニメキャラクターのインスタンス分割)](sota/vision.md#image-segmentation--instance-segmentation) | [dreMaz/AnimeInstanceSegmentation](https://huggingface.co/dreMaz/AnimeInstanceSegmentation/tree/bc091c8cd74e234001eeacece6dd45038521254f) | mit | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [マスク生成(SAM系・アニメ対応)](sota/vision.md#mask-generation) | [facebook/sam3](https://huggingface.co/facebook/sam3/tree/3c879f39826c281e95690f02c7821c4de09afae7) | other | 中 | 汎用モデルのみ（アニメ特化なし） |
| 画像認識（検出・分割・分類・特徴） | [ゼロショット物体検出(テキスト指定・アニメ画像)](sota/vision.md#zero-shot-object-detection) | [facebook/sam3](https://huggingface.co/facebook/sam3/tree/3c879f39826c281e95690f02c7821c4de09afae7) | other | 低 | 汎用モデルのみ（アニメ特化なし） |
| 画像認識（検出・分割・分類・特徴） | [キーポイント検出(アニメ顔ランドマーク28点)](sota/vision.md#keypoint-detection--face-landmarks) | [hysts/anime-face-detector-hrnetv2](https://huggingface.co/hysts/anime-face-detector-hrnetv2/tree/9b3435248b26aeb82e2a8578fe9d86d5d57158af) | mit | 中 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [キーポイント検出(アニメ・イラストの人体ポーズ/OpenPose18)](sota/vision.md#keypoint-detection--body-pose) | [mrpm/ComfyUI-AnimePose-weights](https://huggingface.co/mrpm/ComfyUI-AnimePose-weights/tree/75396e167075ba8ab740635d0a8d58cd0ba8b30f) | agpl-3.0 | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [深度推定(アニメキャラの擬似深度=描画順序)](sota/vision.md#depth-estimation--anime-character-pseudo-depth) | [layerdifforg/seethroughv0.0.1_marigold](https://huggingface.co/layerdifforg/seethroughv0.0.1_marigold/tree/4f4ffc46050b6feb764b628859968a26e76e6b6a) | openrail++ | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [深度推定(アニメ/イラストの汎用相対深度)](sota/vision.md#depth-estimation--general-relative-depth) | [depth-anything/Depth-Anything-V2-Large](https://huggingface.co/depth-anything/Depth-Anything-V2-Large/tree/cbbb86a30ce19b5684b7a05155dc7e6cbc7685b9) | cc-by-nc-4.0 | 低 | 汎用モデルのみ（アニメ特化なし） |
| 画像認識（検出・分割・分類・特徴） | [画像分類(アニメ画像マルチラベルタガー / Danbooruタグ)](sota/vision.md#image-classification--tagger) | [pixai-labs/pixai-tagger-v1.0](https://huggingface.co/pixai-labs/pixai-tagger-v1.0/tree/9fe10addf9326e292da8a85a98ea74cd91b41771) | apache-2.0 | 中 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [画像分類(アニメ画像の美的スコア/品質段階)](sota/vision.md#image-classification--aesthetic) | [deepghs/anime_aesthetic](https://huggingface.co/deepghs/anime_aesthetic/tree/a83ab545e1d2a869f1180b99b2a7dee22ec3b97e) | openrail | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [画像分類(AI生成アニメ画像 vs 人間作画の判定)](sota/vision.md#image-classification--ai-generated-detection) | [deepghs/cls-ai-check-1m.caformer_s36.r512](https://huggingface.co/deepghs/cls-ai-check-1m.caformer_s36.r512/tree/ada73d0101e481e21918c0550c9e94e021a1eaa1) | mit | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [画像分類(アニメ画像の種別: イラスト/漫画/アニメ映像/3D/非絵画)](sota/vision.md#image-classification--image-type) | [deepghs/anime_classification](https://huggingface.co/deepghs/anime_classification/tree/5ee62e06f5f4cd68a1c2f3bc5dc9805e827d37df) | mit | 中 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [ゼロショット画像分類(アニメCLIP)](sota/vision.md#zero-shot-image-classification) | [OysterQAQ/DanbooruCLIP](https://huggingface.co/OysterQAQ/DanbooruCLIP/tree/aa2e603035bdf3e414e349f98ab2f9d3f6b43c5d) | 未記載 | 低 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [特徴量抽出(アニメキャラクター同一性=CCIP埋め込み)](sota/vision.md#image-feature-extraction--character-identity) | [deepghs/ccip](https://huggingface.co/deepghs/ccip/tree/8f636fb81a9f4342dfe220a16144525c2bece2a1) | openrail | 中 | アニメ特化の最良 |
| 画像認識（検出・分割・分類・特徴） | [特徴量抽出(アニメ画像の類似検索・重複検出の汎用埋め込み)](sota/vision.md#image-feature-extraction--general-retrieval) | [facebook/dinov3-vitl16-pretrain-lvd1689m](https://huggingface.co/facebook/dinov3-vitl16-pretrain-lvd1689m/tree/ea8dc2863c51be0a264bab82070e3e8836b02d51) | other/dinov3-license | 低 | 汎用モデルのみ（アニメ特化なし） |
| マンガ・OCR・文書 | [画像→テキスト(漫画の吹き出し・台詞クロップOCR)](sota/manga.md#image-to-text--manga-dialogue-ocr) | [JustANormalTinkerer/hayai-ocr-v2.5-nova](https://huggingface.co/JustANormalTinkerer/hayai-ocr-v2.5-nova/tree/e34d7755ed11e626c5ba39544af5d66f20ee57cc) | apache-2.0 | 低 | アニメ特化の最良 |
| マンガ・OCR・文書 | [画像→テキスト(オノマトペ・効果音SFXのOCR)](sota/manga.md#image-to-text--onomatopoeia-ocr) | [JustANormalTinkerer/hayai-ocr-v2.5-nova](https://huggingface.co/JustANormalTinkerer/hayai-ocr-v2.5-nova/tree/e34d7755ed11e626c5ba39544af5d66f20ee57cc) | apache-2.0 | 低 | アニメ特化の最良 |
| マンガ・OCR・文書 | [画像→テキスト(ギャルゲー/VN・ゲーム画面の日本語OCR)](sota/manga.md#image-to-text--game-vn-screen-ocr) | [rtr46/meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0/tree/a28cf5874dc2438ebb1c86336be26bcec51e3375) | lgpl-3.0 | 中 | アニメ特化の最良 |
| マンガ・OCR・文書 | [画像→テキスト(アニメ・イラストのキャプション/booruタグ生成)](sota/manga.md#image-to-text--illustration-captioning) | [fancyfeast/llama-joycaption-beta-one-hf-llava](https://huggingface.co/fancyfeast/llama-joycaption-beta-one-hf-llava/tree/ebf414ea497a020da0f82df3913e5b6cb8e9663a) | 未記載 | 中 | 汎用モデルのみ（アニメ特化なし） |
| マンガ・OCR・文書 | [画像+テキスト→テキスト(漫画ページ理解VLM:ページOCR+VQA)](sota/manga.md#image-text-to-text--manga-understanding-vlm) | [hal-utokyo/MangaLMM](https://huggingface.co/hal-utokyo/MangaLMM/tree/a556fbc7edc256fbd6d3b4d8d3418dd5d68f7c27) | mit | 中 | アニメ特化の最良 |
| マンガ・OCR・文書 | [視覚的質問応答(漫画ページの内容理解:MangaVQA)](sota/manga.md#visual-question-answering--manga-vqa) | [hal-utokyo/MangaLMM](https://huggingface.co/hal-utokyo/MangaLMM/tree/a556fbc7edc256fbd6d3b4d8d3418dd5d68f7c27) | mit | 中 | アニメ特化の最良 |
| マンガ・OCR・文書 | [漫画レイアウト検出(文字・擬音・吹き出し・コマの検出+インスタンスマスク)](sota/manga.md#manga-layout-detection--text-bubble-panel-detection) | [mayocream/koharu-layout-rfdetr-seg-2xl-1152](https://huggingface.co/mayocream/koharu-layout-rfdetr-seg-2xl-1152/tree/aed55fdb8ca953c6bec33cf6ed6dd52a9b72bfa2) | other | 中 | アニメ特化の最良 |
| マンガ・OCR・文書 | [アニメ・イラスト・カラー漫画内テキストブロック検出(枠外文字・題字含む)](sota/manga.md#manga-layout-detection--anime-scene-text-detection) | [deepghs/AnimeText_yolo](https://huggingface.co/deepghs/AnimeText_yolo/tree/a180c191bfdb9f0e31b57e7de567e7b6bac50f84) | gpl-3.0 | 中 | アニメ特化の最良 |
| マンガ・OCR・文書 | [漫画の読み順・コマ/文字/キャラ/吹き出し尾の関連付け(台詞の話者推定)](sota/manga.md#manga-reading-order) | [ragavsachdeva/magiv3](https://huggingface.co/ragavsachdeva/magiv3/tree/49c73a225122d53adbaa26d53868be81a57706e2) | 未記載 | 低 | アニメ特化の最良 |
| マンガ・OCR・文書 | [漫画の文字消去・インペイント(吹き出し/背景のテキスト除去)](sota/manga.md#manga-text-inpainting) | [dreMaz/AnimeMangaInpainting](https://huggingface.co/dreMaz/AnimeMangaInpainting/tree/2953a4e935bf01ad1471f6cbfd26ab81abeeb92d) | mit | 中 | アニメ特化の最良 |
| マンガ・OCR・文書 | [漫画翻訳パイプライン(検出→OCR→消去→翻訳→植字)のアプリ/OSS選定](sota/manga.md#manga-translation-pipeline) | モデルなし（リポジトリのみ） | — | 中 | モデルなし |
| 言語（翻訳・生成・埋め込み） | [翻訳(日本語→簡体字中国語: ギャルゲー/ラノベ)](sota/text.md#translation--ja-zh-galgame-ln) | [SakuraLLM/Sakura-GalTransl-7B-v3.7](https://huggingface.co/SakuraLLM/Sakura-GalTransl-7B-v3.7/tree/759d76b1745f4428308de6564c5ab710d4358b2e) | cc-by-nc-sa-4.0 | 中 | アニメ特化の最良 |
| 言語（翻訳・生成・埋め込み） | [翻訳(日本語→英語: ビジュアルノベル)](sota/text.md#translation--ja-en-visual-novel) | [lmg-anon/vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf/tree/ab7c8285d386fab7cd89e951f62e129085df6372) | llama3 | 低 | アニメ特化の最良 |
| 言語（翻訳・生成・埋め込み） | [テキスト生成(タグ/プロンプト拡張: Danbooruタグ→詳細プロンプト)](sota/text.md#text-generation--danbooru-prompt-expansion) | [KBlueLeaf/TIPO-500M-ft](https://huggingface.co/KBlueLeaf/TIPO-500M-ft/tree/386fc21b10c810c0c1c8f182695e28fbbd45597c) | other/kohaku-license-1.0 | 中 | アニメ特化の最良 |
| 言語（翻訳・生成・埋め込み） | [テキスト生成(キャラクターロールプレイ/キャラカード対話)](sota/text.md#text-generation--character-roleplay) | [hiwaifu-research/WaifuGemma4-26b-a4b-v1](https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1/tree/540c0f8f2c33683041f227507eaab4f9f6cb17a6) | apache-2.0 | 低 | 汎用モデルのみ（アニメ特化なし） |
| 言語（翻訳・生成・埋め込み） | [文類似度(日本語埋め込み: アニメ/キャラ検索用途)](sota/text.md#sentence-similarity) | [cl-nagoya/ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m/tree/18b60fb8c2b9df296fb4212bb7d23ef94e579cd3) | apache-2.0 | 中 | 汎用モデルのみ（アニメ特化なし） |
| 言語（翻訳・生成・埋め込み） | [特徴抽出(日本語テキスト埋め込み/タグ・キャラ語彙)](sota/text.md#feature-extraction) | [cl-nagoya/ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m/tree/18b60fb8c2b9df296fb4212bb7d23ef94e579cd3) | apache-2.0 | 低 | 汎用モデルのみ（アニメ特化なし） |
| 言語（翻訳・生成・埋め込み） | [リランキング(日本語リランカー: アニメ検索用途)](sota/text.md#text-ranking) | [cl-nagoya/ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m/tree/bb46934ee9ed09f850b9fcff17501b3ef7ddb2b3) | apache-2.0 | 中 | 汎用モデルのみ（アニメ特化なし） |
| 言語（翻訳・生成・埋め込み） | [穴埋め(日本語マスクLM)](sota/text.md#fill-mask) | [sbintuitions/modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m/tree/28c180b16463ba6f3fa79b48756fbf21586fe23e) | mit | 中 | 汎用モデルのみ（アニメ特化なし） |
| 言語（翻訳・生成・埋め込み） | [トークン分類(日本語NER: 作品名/キャラ名/声優名)](sota/text.md#token-classification) | [llm-book/bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset/tree/49ef0cbab94d38498d0c088f73549c22a59def1b) | apache-2.0 | 低 | 汎用モデルのみ（アニメ特化なし） |
| 言語（翻訳・生成・埋め込み） | [ゼロショット分類(ジャンル/レーティング/同人ラベル)](sota/text.md#zero-shot-classification) | [MoritzLaurer/bge-m3-zeroshot-v2.0](https://huggingface.co/MoritzLaurer/bge-m3-zeroshot-v2.0/tree/9abf1c8aaeb82a2447809c20753ed0b106b76652) | mit | 低 | 汎用モデルのみ（アニメ特化なし） |
| 3D・アバター・その他 | [アニメイラストの2.5Dレイヤ分解(Live2D/PSD向け)](sota/threed_other.md#live2d-layer-decomposition) | [layerdifforg/seethroughv0.0.2_layerdiff3d](https://huggingface.co/layerdifforg/seethroughv0.0.2_layerdiff3d/tree/4477e6ce529bc6a141732e1a55a4932176db3b89) | openrail++ | 高 | アニメ特化の最良 |
| 3D・アバター・その他 | [画像から3D(アニメキャラ単体のメッシュ生成)](sota/threed_other.md#image-to-3d--anime-character-mesh) | [hyz317/StdGEN](https://huggingface.co/hyz317/StdGEN/tree/8d12f6e3e279a2aac9bb957236c1e8e3c13549c0) | apache-2.0 | 低 | アニメ特化の最良 |
| 3D・アバター・その他 | [アニメ3Dキャラの自動リギング(骨格・スキニング)](sota/threed_other.md#anime-3d-rigging) | [VAST-AI/SkinTokens](https://huggingface.co/VAST-AI/SkinTokens/tree/79736cad0fd84de384d5eede659b4ebd24effe33) | mit | 低 | 汎用モデルのみ（アニメ特化なし） |
| 3D・アバター・その他 | [テキストからの3Dモーション生成(キャラアニメ用)](sota/threed_other.md#text-to-3d--text-to-motion) | [nvidia/Kimodo-SOMA-RP-v1.1](https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1.1/tree/6c9233af1180b8151e3c4703477104af5dce9dd5) | other/nvidia-open-model-license | 中 | 汎用モデルのみ（アニメ特化なし） |
| 3D・アバター・その他 | [アニメゲーム/ワールドモデル(次状態予測による対話的アニメ生成)](sota/threed_other.md#anime-game-world-model) | [TencentARC/AnimeGamer](https://huggingface.co/TencentARC/AnimeGamer/tree/a9a2384ac0aae03d32df2b1c6ce6e9c3291baa26) | other/animegamer-lisence | 低 | アニメ特化の最良 |
| 3D・アバター・その他 | [ピクセルアート・スプライト生成](sota/threed_other.md#pixel-art-sprite) | [nerijs/pixel-art-xl](https://huggingface.co/nerijs/pixel-art-xl/tree/8bf4a4d9ea283e00a51fafda8e0539f8248ea037) | creativeml-openrail-m | 低 | 汎用モデルのみ（アニメ特化なし） |
| 3D・アバター・その他 | [アニメ2Dアバターのアニメーション(1枚絵駆動・Live2D代替・表情差分)](sota/threed_other.md#anime-2d-avatar-animation) | モデルなし（リポジトリのみ） | — | 低 | モデルなし |
| 3D・アバター・その他 | [VTuber/AIキャラクター対話エージェント基盤(Live2D/VRM+LLM+TTS+ASR)](sota/threed_other.md#vtuber-agent-framework) | モデルなし（リポジトリのみ） | — | 中 | モデルなし |
| 3D・アバター・その他 | [VRM/MMD/3Dアバター基盤ツール(ビューア・DCC連携・ゲームエンジン)](sota/threed_other.md#vrm-avatar-tooling) | モデルなし（リポジトリのみ） | — | 高 | モデルなし |
| 3D・アバター・その他 | [モーションキャプチャ・リターゲット(VRM/MMD/Mixamo)](sota/threed_other.md#motion-capture-retargeting) | モデルなし（リポジトリのみ） | — | 低 | モデルなし |
| 3D・アバター・その他 | [アニメ3Dキャラ・リグのデータセット(Anime3D/Anime3D++/AnimeRig)](sota/threed_other.md#anime-3d-datasets) | モデルなし（リポジトリのみ） | — | 中 | モデルなし |

## 該当なし（アニメ特化モデルも実用的な汎用モデルも見つからなかったタスク）

| タスク | 確認した範囲と理由 |
| --- | --- |
| 文書質問応答(漫画ページ・VN画面) | 漫画・VN向けの文書QAモデルはHFに0件で該当なし。漫画ページQAはMangaLMM、VN画面は通常OCRで代替する。 |
| 視覚的文書検索(漫画ページ・イラストの検索) | 漫画・アニメ特化の視覚文書検索モデルはHFに0件で該当なし。汎用ColPali系は漫画での精度が未確認のため推奨しない。 |
| any-to-any(アニメ・漫画向けマルチモーダル生成) | アニメ特化のany-to-anyモデルはHFに0件で該当なし。AnimeGamerはtext-to-video扱いで30日DL27と実績が乏しい。 |
| テキスト生成(日本語ラノベ/シナリオ生成) | 非成人向けで実績ある日本語シナリオ専用モデルは無く、有力系統はNSFW特化のため収録せず汎用LLMを使う。 |
| 要約(アニメ/エピソード/小説あらすじ) | アニメ・小説向けの実績ある要約モデルは無く、汎用LLMのプロンプトで足りるため収録しない。 |
| 質問応答(アニメ/オタク知識QA) | アニメ知識QAの信頼できる公開モデルは無く(候補は累計18DL)、LLMと検索の組み合わせで対応するため収録しない。 |
| テキスト分類(アニメ感想感情/ジャンル/同人向け毒性) | アニメ特化の分類器は個人実験規模(累計25DL等)で採用根拠が弱く、LLMのゼロショットで足りるため収録しない。 |
| 表形式質問応答 | アニメや日本語向けの表QAモデルは存在せず需要も乏しいため収録しない。 |
| テキストから3D形状(アニメキャラ)生成 | アニメ専用のテキスト→3D形状モデルは無く、汎用TRELLIS-textも2025年で更新停滞のため、画像経由(image-to-3d)を推奨し推奨モデルは置かない。 |
| 漫画フォント・写植(フォント生成/識別) | HFとGitHubで漫画・日本語のフォント生成/識別モデルは見つからず、欧文の汎用フォント識別のみのため該当なしとした。 |
| 表形式分類(アニメ関連) | HFでアニメ関連の表形式分類モデルを検索したが、唯一のヒットは作者名が一致しただけの無関係な与信モデルで、該当なし。 |
| 表形式回帰(アニメ評価・人気予測) | HFでアニメ関連の表形式回帰モデルを検索してヒット0件で、評価・人気予測の公開モデルは存在せず、該当なし。 |
| 時系列予測(アニメ視聴数・配信者統計等) | HFでアニメ関連の時系列予測モデルを検索してヒット0件で、アニメ専用の公開モデルは存在せず、該当なし。 |
| 強化学習(VTuber/アニメキャラエージェント) | HFの検索結果はユーザー名一致の強化学習コース演習のみで、アニメ用途のモデルは無く、VTuberエージェントも強化学習ではないため該当なし。 |
| ロボティクス(アニメキャラ/VTuberロボット) | HFでアニメ関連のロボティクスモデルを検索してヒット0件で、Kimodoのロボット版もアニメ制作とは無関係のため、該当なし。 |
| グラフ機械学習(キャラ関係図・アニメ推薦グラフ) | HFでアニメ関連のグラフ機械学習モデルを検索してヒット0件で、推薦も文埋め込みの個人モデルのみのため、該当なし。 |
| その他(HFのタスク未設定・other分類のアニメ関連モデル) | タグ未設定の重要モデルは各タスク(See-through・Kimodo・SkinTokens等)へ統合済みで、残りは低利用の派生のみのため単独推奨は無い。 |
