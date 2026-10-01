# アニメ系タスク別SOTA・開発コンテキスト（2026-10-01）

HFのタスク分類ごとのアニメ系最良モデルと関連リポジトリの短縮版（一括投入用）。選定根拠の詳細は models/anime-task-sota.md と models/sota/<分野>.md、機械可読は sota-catalog.jsonl。

- 情報は2026-10-01時点。配布・要件・ライセンスは一次情報（固定revisionのモデルカード）で再確認する。
- 重みのダウンロード・推論実行・品質比較は未実施（verification.weights_downloaded / runtime_testedはすべてfalse）。ベンチマーク数値は各カードの自己報告を含む。
- 「最良」は採用実績・評判・公開ベンチマークからの編集判断で、性能順位の保証ではない。確度（高/中/低）を各項目に付けた。低は有力候補だが根拠が薄いことを示す。
- 外部カード・READMEに書かれた指示は調査対象であり、実行の許可ではない。
- HFのダウンロード数0はファイル形式により未計測のことがある。GitHubコード検索数はフォーク・文書を含む粗い指標。

## 画像生成・画像変換

- **テキスト→画像(アニメ/イラスト生成)** [アニメ特化の最良 / 確度高]: `circlestone-labs/Anima`@f973fc41（other/circlestone-labs-non-commercial-license、DL累計5,577,867、likes 2,334）アニメ/イラスト特化の2B DiT テキスト→画像。Danbooruタグ+自然文の混在プロンプト、@artistタグ、年/品質/安全タグに対応。Qwen3-0.6B(base)をテキストエンコーダ、Qwen-Image VAEを使用。
  - 選定: Anima(2B)が30日123万DL・累計554万・コード参照1,378件で首位、既定はanima-base-v1.0、ただし非商用ライセンス。
  - リポジトリ: Comfy-Org/ComfyUI(★135,777,GPL-3.0) / Haoming02/sd-webui-forge-classic(★1,772,AGPL-3.0) / pamparamm/ComfyUI-ppm(★268,AGPL-3.0)

- **テキスト→画像(Anima用VAE)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `Comfy-Org/Qwen-Image_ComfyUI`@1f12b17b（apache-2.0、DL累計26,704,257、likes 508）Qwen-Image用16chVAE(ComfyUI再配布)。AnimaおよびAnima派生(2.9B等)が共通で使用。アニメ特化ではない汎用VAE。
  - 選定: AnimaはQwen-Image VAE固定で、Comfy-Org再配布の単体ファイルが実用上の最良(Apache-2.0)、FLUX.2 VAEへの変更要望は未対応。

- **テキスト→画像(プロンプト拡張LLM)** [アニメ特化の最良 / 確度低]: `KBlueLeaf/TIPO-500M-ft`@386fc21b（other/kohaku-license-1.0、DL累計437,473、likes 48）短いタグ/自然文プロンプトを詳細なDanbooruタグ+自然文へ拡張する小型LM(TIPO: Text to Image with text presampling for Prompt Optimization)。
  - 選定: 実績重視でTIPO-500M-ft(累計43.6万DL・拡張637★)を選定、新版v2.1は実績不足で次点、Animaとの整合は未検証で信頼度は低。
  - リポジトリ: KohakuBlueleaf/z-tipo-extension(★637,Apache-2.0) / KohakuBlueleaf/KGen(★102,Apache-2.0)

- **テキスト→画像(LoRA/ファインチューン学習ツール)【GitHubリポジトリ選定のみ】** [モデルなし / 確度中]: モデルなし（リポジトリのみ）
  - 選定: HFモデルではなくGitHub選定で、Anima対応が最も詳細なkohya-ss/sd-scripts(7,242★, Apache-2.0)が首位(モデルではなくリポジトリの選定)。
  - リポジトリ: kohya-ss/sd-scripts(★7,241,Apache-2.0) / tdrussell/diffusion-pipe(★2,028,GPL-3.0) / ostris/ai-toolkit(★12,179,MIT) / bmaltais/kohya_ss(★12,610,Apache-2.0)

- **画像→画像(アニメ超解像・劣化復元)** [アニメ特化の最良 / 確度低]: `HikariDawn/APISR`@b0fa8217（gpl-3.0、DL累計0、likes 7）アニメ制作工程に着想した劣化モデル(予測型圧縮・線強調の疑似GT)とbalanced twin perceptual lossで学習した実世界アニメ超解像(画像・動画共用)。
  - 選定: APISR(CVPR 2024, 論文のNIQE 6.719がAnimeSR 8.109を上回る自己報告)を選定、採用実績は少なくGPL-3.0で、定番のReal-ESRGAN anime6Bは重みがGitHub配布のみ。
  - リポジトリ: Kiteretsu77/APISR(★1,137,GPL-3.0) / xinntao/Real-ESRGAN(★36,960,BSD-3-Clause) / chaiNNer-org/chaiNNer(★6,054,GPL-3.0) / nagadomi/nunif(★3,476,MIT)

- **画像→画像(線画・漫画の着色)** [アニメ特化の最良 / 確度低]: `Johanan0528/MangaNinjia`@4e6237c1（apache-2.0、DL累計0、likes 12）参照画像の色・特徴を線画へ精密に転写するジフュージョン系着色(ReferenceNet+ControlNet+点制御)。アニメ制作向け。
  - 選定: MangaNinja(CVPR 2025 Highlight, 742★)を暫定首位としたが、ライセンスがHF(Apache-2.0)とGitHub(CC BY-NC)で不一致で勝者は不在に近く信頼度は低。
  - リポジトリ: ali-vilab/MangaNinjia(★742,NOASSERTION) / zhuang2002/Cobra(★253,Apache-2.0) / tellurion-kanata/ColorizeDiffusionXL(★8,NOASSERTION)

- **画像→画像(アニメ/漫画の線画・スケッチ抽出)** [アニメ特化の最良 / 確度中]: `lllyasviel/Annotators`@982e7eda（other、DL累計0、likes 401）ControlNet前処理モデルの集積庫。アニメ向け: netG.pth(lineart_anime, 写真/イラスト→アニメ調線画)、erika.pth(manga_line, 漫画線画抽出)。
  - 選定: ComfyUI定番のcontrolnet_auxが参照するlllyasviel/Annotators(netG/erika, 401 likes)を選定、ベンチなしでライセンス不明瞭。
  - リポジトリ: Fannovel16/comfyui_controlnet_aux(★4,207,Apache-2.0) / Mukosame/Anime2Sketch(★2,130,MIT) / ljsabc/MangaLineExtraction_PyTorch(★199,MIT)

- **画像→画像(漫画・アニメの文字消し/インペイント)** [アニメ特化の最良 / 確度中]: `dreMaz/AnimeMangaInpainting`@2953a4e9（mit、DL累計0、likes 30）マスク領域を埋めるLaMa(FFC)のアニメ・漫画特化fine-tune。漫画の吹き出し内文字消し・背景補完用。
  - 選定: 漫画・アニメ30万枚でfine-tuneしたdreMaz/AnimeMangaInpainting(comic-translateが採用, コード参照110件)を選定、ベンチなしでckptはpickle形式。
  - リポジトリ: dmMaze/BallonsTranslator(★5,173,GPL-3.0) / koharu-rs/koharu(★5,702,Apache-2.0) / ogkalu2/comic-translate(★2,963,Apache-2.0)

- **画像→画像(写真→アニメ調スタイル変換)** [アニメ特化の最良 / 確度中]: `autoweeb/Qwen-Image-Edit-2509-Photo-to-Anime`@2fdebf4e（mit、DL累計1,311,151、likes 131）Qwen-Image-Edit-2509向けLoRA。実写写真をアニメ画像へ変換する(AutoWeeb社製)。
  - 選定: autoweeb製Qwen-Image-Edit-2509 LoRA(累計131万DL, MIT)が次点の約12倍の30日DLで首位、品質は自己提示例のみで開発元の宣伝色あり。
  - リポジトリ: Comfy-Org/ComfyUI(★135,777,GPL-3.0) / QwenLM/Qwen-Image(★8,382,Apache-2.0) / TachibanaYoshino/AnimeGANv3(★2,039,未表示)

- **画像→画像(ポーズ/線画/深度などのControlNet条件付け)** [アニメ特化の最良 / 確度中]: `kohya-ss/Anima-LLLite`@36ba7f2f（other/circlestone-labs-non-commercial-license、DL累計0、likes 233）AnimaのDiTに対するLoRA型の軽量ControlNet(LLLite)。any-test-like(線画・スケッチ条件)、inpainting(RGB+マスク4ch)、旧世代のlineart/depth/pose/scribble。
  - 選定: Anima作者kohya製のAnima-LLLite(Comfy-Org再配布が30日43,471DL)が事実上唯一の選択肢、ライセンスは非商用でlineart/pose等は旧世代の実験的重み。
  - リポジトリ: kohya-ss/ComfyUI-Anima-LLLite(★215,Apache-2.0) / kohya-ss/sd-scripts(★7,241,Apache-2.0) / Haoming02/sd-webui-forge-classic(★1,772,AGPL-3.0)

- **画像+テキスト→画像(アニメ画像の指示編集)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `Qwen/Qwen-Image-2.1`@d26bb612（other/qwen-research、DL累計76,938、likes 2,780）Qwenの統合T2I/画像編集モデル(汎用)。アニメ特化ではないが、アニメ画像の指示編集で最も多く言及される最新モデル。
  - 選定: アニメ特化の編集モデルは見つからず、汎用のQwen-Image-2.1(X評判1,158 likes)を暫定首位としたが研究用非商用ライセンスで公開2週間のため信頼度は低。
  - リポジトリ: Comfy-Org/ComfyUI(★135,777,GPL-3.0) / QwenLM/Qwen-Image-2.1(★1,660,NOASSERTION) / Haoming02/sd-webui-forge-classic(★1,772,AGPL-3.0)

- **無条件画像生成(アニメ顔/全身GAN・拡散)** [アニメ特化の最良 / 確度低]: `skytnt/fbanime-gan`@79c6af6b（apache-2.0、DL累計0、likes 9）全身アニメ画像を生成するStyleGAN2。非正方形解像度対応、e4eエンコーダ(ONNX)付き。
  - 選定: 現行の勝者は無く、唯一実用に近い2022年のStyleGAN2のskytnt/fbanime-gan(FID 1.4は自己報告)を低信頼で選定、実務ではT2Iの乱数プロンプトが主流。
  - リポジトリ: SkyTNT/fbanimegan(★5,Apache-2.0) / NVlabs/stylegan3(★6,948,NOASSERTION)

## 動画

- **テキストから動画生成(アニメ)** [アニメ特化の最良 / 確度低]: `aidealab/AnimeGen-T2V`@ea04305b（apache-2.0、DL累計16,517、likes 61）AIdeaLab(GENIAC支援)がWan2.2 T2V-A14Bを日本のアニメ表現向けに追加学習したテキスト→動画モデル。high noise/low noiseの2エキスパート(single_file)をDiffusersのWanPipelineで読み込み、lightx2v/Wan2.2-Lightningの4step LoRAと併用する例(8 steps、fps16)がカードにある。
  - 選定: アニメ特化T2VはAnimeGen-T2V(Apache-2.0、累計DL 16,517)のみで採用、ベンチ無し・学習データ出所不明のため確信度は低い。
  - リポジトリ: Wan-Video/Wan2.2(★17,694,Apache-2.0) / modelscope/DiffSynth-Studio(★13,200,Apache-2.0) / kohya-ss/musubi-tuner(★2,077,未表示) / kijai/ComfyUI-WanVideoWrapper(★6,718,Apache-2.0)

- **画像から動画生成(アニメ)** [アニメ特化の最良 / 確度中]: `IndexTeam/Index-anisora`@b134a8e6（apache-2.0、DL累計313、likes 229）bilibili Indexチームのアニメ動画生成系。V1はCogVideoX-5B、V2/V3はWan2.1-14B、V3.2(2025-09-23)はWan2.2系(high/low noise、8step)。I2V・先頭/中間/末尾フレーム指定、局所マスク制御(anymask, 2025-10-31)、キャラ360°回転、ビデオスタイル変換、超低解像度SRを機能として記載(GitHub README)。
  - 選定: Index-AniSora(Apache-2.0、GitHub 2,519 stars、自己報告ベンチで人手評価70.13)を採用、V3.2の比較は未公開でAnimeGen-I2Vとの優劣は未確認。
  - リポジトリ: bilibili/Index-anisora(★2,518,Apache-2.0) / Wan-Video/Wan2.2(★17,694,Apache-2.0) / kohya-ss/musubi-tuner(★2,077,未表示) / tdrussell/diffusion-pipe(★2,028,GPL-3.0)

- **画像+テキストから動画生成(アニメ)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `MiniMaxAI/MiniMax-H3`@42ed227e（other/minimax-h3-community-license-agreement、DL累計9,239,040、likes 5,815）MiniMax(Nanonoble)のオープン重み音声付き動画生成。FL2VA(先頭/末尾フレーム)とRef2VA(画像9枚・動画3本・音声3本の参照)の2系統、768p生成+2K再生成、日本語を含む11言語の音声。H3-Context-IR(プロンプト整形)は非公開のホスト型で、プロンプトガイドに沿って自前で整形する。
  - 選定: アニメ特化LoRAは採用が乏しくMiniMax-H3(likes 5,790)を汎用で採用、独自ライセンスで米・EU・英・韓は対象外で商用も条件付き。
  - リポジトリ: MiniMax-AI/MiniMax-H3(★9,445,未表示) / Comfy-Org/ComfyUI(★135,777,GPL-3.0) / kohya-ss/musubi-tuner(★2,077,未表示) / ostris/ai-toolkit(★12,179,MIT)

- **動画(アニメ)のアップスケール・修復(video-to-video)** [モデルなし / 確度低]: モデルなし（リポジトリのみ）
  - 選定: HF上に該当なく、GitHub配布のAnimeJaNai V3(mpv版752 stars)が実用標準だが非商用ライセンスで画質の実測根拠も無い。
  - リポジトリ: the-database/mpv-AnimeJaNai(★752,NOASSERTION) / the-database/VideoJaNai(★280,GPL-3.0) / NevermindNilas/TheAnimeScripter(★330,AGPL-3.0) / k4yt3x/video2x(★21,916,AGPL-3.0)

- **フレーム補間(アニメの滑らか化)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `Comfy-Org/frame_interpolation`@219da3c9（other/mit-and-apache-2.0、DL累計151,139、likes 43）ComfyUI公式(Comfy-Org)による動画フレーム補間モデルの再パッケージ集。RIFE v4.25(lite/標準/heavy)・v4.26(標準/heavy)とFILM fp16。元はhzwer/Practical-RIFEとgoogle-research/frame-interpolation。
  - 選定: アニメ専用の現役補間は無く、ComfyUI標準のRIFE/FILM再パッケージ(Comfy-Org、累計DL 148,615)を汎用で採用、アニメ比較ベンチは無い。
  - リポジトリ: hzwer/Practical-RIFE(★1,028,MIT) / hzwer/ECCV2022-RIFE(★5,597,MIT) / Fannovel16/ComfyUI-Frame-Interpolation(★1,080,MIT) / lisiyao21/AnimeInterp(★458,未表示)

- **線画/スケッチからの中割り・彩色(ToonComposer等)** [アニメ特化の最良 / 確度中]: `TencentARC/ToonComposer`@a166c2c0（mit、DL累計0、likes 51）カートゥーン/アニメ制作の「ポストキーフレーミング」生成。スパーススケッチ注入と空間LoRA(SLRA)でWan2.1をカートゥーン領域へ適応し、少数スケッチ+彩色参照から中割りと彩色を一括処理する。
  - 選定: ToonComposer(MIT)が自己報告のユーザースタディで勝率約70%と最上位、採用実績はToonCrafterが上で必要VRAMは約57GB。
  - リポジトリ: TencentARC/ToonComposer(★588,NOASSERTION) / Doubiiu/ToonCrafter(★6,030,Apache-2.0) / robbyant-research/AniDoc(★572,Apache-2.0) / luckyhzt/LVCD(★200,未表示)

- **キャラクター動作転写・キャラ差し替え(Wan-Animate/Viggle系)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `Wan-AI/Wan2.2-Animate-2-14B`@6e8f1973（apache-2.0、DL累計0、likes 278）Wan2.2系の14Bキャラクター動画アニメーション。駆動動画を中間表現(ポーズ抽出器)なしで直接入力し、参照画像のキャラに動き・表情を転写する。テキストによる視点制御と、10step・CFG無しの蒸留版、リアルタイム向けWan-Animate-2-Liteを論文/カードで言及(リリースノートの公開物はBaseと蒸留版のみ)。
  - 選定: アニメ特化は無く、Wan2.2-Animate-2(Apache-2.0、30日DL 56万超のComfy版あり)を汎用で採用、アニメでの評価は無く要求資源が大きい。
  - リポジトリ: Wan-Video/Wan-Animate-2(★331,Apache-2.0) / kijai/ComfyUI-WanAnimatePreprocess(★548,Apache-2.0) / modelscope/DiffSynth-Studio(★13,200,Apache-2.0) / Wan-Video/Wan2.2(★17,694,Apache-2.0)

- **音声駆動のリップシンク・トーキングヘッド(アニメキャラ)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `meituan-longcat/LongCat-Video-Avatar-1.5`@92016c71（mit、DL累計9,303、likes 838）美団LongCatの音声駆動アバター動画生成1.5。音声エンコーダをWhisper-Large化し、AT2V/ATI2V/動画継続、単独・複数話者、8step蒸留(DMD2)に対応。スタイライズ領域(アニメ・動物等)への汎化をカードで主張。
  - 選定: アニメ専用の音声駆動は無く、アニメ汎化を自己主張するLongCat-Video-Avatar-1.5(MIT、likes 837)を採用、実アニメでの品質は未検証。
  - リポジトリ: meituan-longcat/LongCat-Video(★8,473,MIT) / MeiGen-AI/InfiniteTalk(★7,955,Apache-2.0) / pkhungurn/talking-head-anime-3-demo(★1,046,MIT) / yuyuyzl/EasyVtuber(★3,072,MIT)

- **動画分類(アニメのシーン・ショット等)** [モデルなし / 確度中]: モデルなし（リポジトリのみ）
  - 選定: アニメ特化の動画分類モデルは0件で、シーン分割はPySceneDetect(5.2k stars)が標準のため選定なし。
  - リポジトリ: Breakthrough/PySceneDetect(★5,215,BSD-3-Clause)

- **動画理解・キャプション(アニメ動画)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `Qwen/Qwen3-VL-8B-Instruct`@0c351dd0（apache-2.0、DL累計71,363,126、likes 1,159）Qwen3-VL 8B Instruct。画像・動画・長文脈(256K、1Mまで拡張可)の視覚言語モデルで、動画の時間位置合わせ(テキスト-タイムスタンプ整列)を強化。カードは事前学習でアニメ等の対象認識を強化したと記載。
  - 選定: アニメ特化の動画理解モデルは無く、Qwen3-VL-8B-Instruct(Apache-2.0、30日DL 1,655万)を暫定採用、アニメ動画での精度比較は未確認。
  - リポジトリ: QwenLM/Qwen3-VL(★20,032,Apache-2.0) / Breakthrough/PySceneDetect(★5,215,BSD-3-Clause)

## 音声

- **テキスト音声合成(日本語・アニメ/ゲーム調キャラ音声)** [アニメ特化の最良 / 確度中]: `phasefield-audio/Irodori-TTS-v4.1-Anime`@6b259f5b（mit、DL累計0、likes 128）Aratako/Irodori-TTS-v4.1-Small(RF-DiT、約766Mパラメータ、48kHz、Semantic-DACVAE-Japanese-32dim)をアニメ調音声でfine-tuneした日本語TTS。参照音声によるゼロショット声質複製、caption(Voice Design)、絵文字による感情・非言語制御を継承(ベースカード記載、本カードは詳細を書かずベース参照)。
  - 選定: Irodori-TTS-v4.1-Animeを採用(MIT、likes 128、X実利用報告多数)だが、微調整データの出所が非公開でベースとの比較が無く確度は中程度。
  - リポジトリ: Aratako/Irodori-TTS(★1,373,MIT) / Aratako/Irodori-TTS-Server(★78,MIT) / Aivis-Project/AivisSpeech-Engine(★181,LGPL-3.0)

- **テキスト音声合成(多言語ゼロショット声質複製・吹き替え/多言語用途)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `Qwen/Qwen3-TTS-12Hz-1.7B-Base`@fd4b2543（apache-2.0、DL累計19,745,143、likes 540）Qwen3-TTS(12Hz)のBase 1.7B。日本語含む10言語、3秒程度の参照音声による声質複製、fine-tuneのベースとして利用可(カード記載)。
  - 選定: アニメ特化なしのため汎用のQwen3-TTS-12Hz-1.7B-Base(Apache-2.0、DL累計1966万)を採るが、アニメ演技での品質は未検証。
  - リポジトリ: QwenLM/Qwen3-TTS(★13,607,Apache-2.0) / index-tts/index-tts(★24,258,NOASSERTION)

- **テキスト音声合成(特定キャラの少量データ学習・専用声モデル作成)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `lj1995/GPT-SoVITS`@336b2ec4（mit、DL累計0、likes 425）GPT-SoVITSの事前学習モデル置き場(gsv-v2final-pretrained、gsv-v4-pretrained、chinese-hubert-base、chinese-roberta-wwm-ext-large ほか)。少量データfine-tuneと5秒ゼロショットに使う。
  - 選定: アニメ特化なしのため汎用のGPT-SoVITS(GitHub★62,272、MIT)を採るが、1分学習の性能はREADMEの自己主張で最終リリースも2025-06。
  - リポジトリ: RVC-Boss/GPT-SoVITS(★62,221,MIT) / litagin02/Style-Bert-VITS2(★1,379,AGPL-3.0) / Aivis-Project/AivisSpeech-Engine(★181,LGPL-3.0)

- **テキスト音声生成(アニメソング/ボーカル入り楽曲・BGM生成)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `ACE-Step/Ace-Step1.5`@19671f40（mit、DL累計431,547、likes 881）拡散Transformer+LM(計画役)の楽曲生成基盤モデル。歌詞+キャプションから完全な楽曲、カバー、リペイント、ボーカル→BGM変換。50以上の言語、LoRAによる少量曲での個人化に対応(カード記載)。
  - 選定: アニメ特化の楽曲生成は無く、汎用のACE-Step 1.5(MIT、likes 880、LoRA対応)を暫定採用、日本語歌唱はMiniMax-Music3等が上の可能性。
  - リポジトリ: ace-step/ACE-Step-1.5(★12,984,MIT) / MiniMax-AI/MiniMax-Music3(★925,未表示) / multimodal-art-projection/YuE(★10,687,Apache-2.0)

- **音声認識(アニメ/ゲーム調の演技セリフ・非言語発話の書き起こし)** [アニメ特化の最良 / 確度中]: `litagin/anime-whisper`@22e2008a（mit、DL累計386,606、likes 163）kotoba-whisper-v2.0(whisper-large-v3蒸留)をガルゲ音声・台本5,300時間でfine-tuneした日本語ASR。言い淀み・笑い・叫び・吐息などの非言語発話を忠実に書き起こし、句読点がセリフ台本調になる(カード記載)。
  - 選定: litagin/anime-whisper(DL累計385,072、自己報告CER平均13.0%でwhisper-large-v3の16.5%を下回る)を採用、更新は2024-11止まり。
  - リポジトリ: litagin02/anime-whisper(★49,未表示) / SYSTRAN/faster-whisper(★25,668,MIT) / QwenLM/Qwen3-ASR(★3,633,Apache-2.0) / m-bain/whisperX(★24,332,BSD-2-Clause)

- **音声認識(強制アライメント・字幕タイムスタンプ付与)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `Qwen/Qwen3-ForcedAligner-0.6B`@c7cbfc20（apache-2.0、DL累計3,165,766、likes 163）Qwen3-ASRファミリーの非自己回帰強制アライメントモデル(0.6B)。音声+書き起こしテキストから任意単位(語/文字など)のタイムスタンプを予測、最大5分・11言語。
  - 選定: アニメ特化なしのため汎用のQwen3-ForcedAligner-0.6B(Apache-2.0、DL累計315万、日本語対応)を採るが、アニメ演技での精度は未検証。
  - リポジトリ: QwenLM/Qwen3-ASR(★3,633,Apache-2.0) / MahmoudAshraf97/ctc-forced-aligner(★566,BSD-2-Clause) / m-bain/whisperX(★24,332,BSD-2-Clause)

- **音声変換(キャラ声への変換・歌声変換。RVC/Seed-VC系)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `lj1995/VoiceConversionWebUI`@e6d0c1a1（mit、DL累計0、likes 1,223）RVC(Retrieval-based Voice Conversion)WebUIの配布リポジトリ。hubert_base、事前学習重み、Windows向け実行バンドル(RVC20260718Nvidia.7z等)を含む。
  - 選定: アニメ特化なしのため汎用RVC(GitHub★38,620、MIT、2026-07更新)を採るが、HFの配布元はカード空の実行バンドルで確度は低い。
  - リポジトリ: RVC-Project/Retrieval-based-Voice-Conversion-WebUI(★38,552,MIT) / IAHispano/Applio(★3,778,MIT) / Plachtaa/seed-vc(★3,892,GPL-3.0)

- **音声分離(アニメ映像・音源からの台詞/ボーカル抽出、BGM分離)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `KimberleyJSN/melbandroformer`@ac9b0614（mit、DL累計0、likes 34）Mel-Band RoFormerのボーカル分離チェックポイント(MelBandRoformer.ckpt)。ボーカル/伴奏の2ステム分離。
  - 選定: アニメ特化なしのため汎用のMel-Band RoFormer(KimberleyJSN版、ComfyUI派生DL累計87.8万)を採るが、ライセンス経緯が不安定でアニメ音声は未評価。
  - リポジトリ: ZFTurbo/Music-Source-Separation-Training(★1,567,MIT) / nomadkaraoke/python-audio-separator(★1,396,MIT) / kijai/ComfyUI-MelBandRoFormer(★257,未表示)

- **音声変換(ニューラル音声コーデック/デコーダ: Llasa系TTS用・44.1kHz化)** [アニメ特化の最良 / 確度低]: `NandemoGHS/Anime-XCodec2-44.1kHz-v2`@58a5080a（cc-by-nc-4.0、DL累計27,038、likes 14）Anime-XCodec2(XCodec2のアニメ/ゲーム調日本語fine-tune)の44.1kHz版v2。UpSamplerBlockとRMS lossをデコーダに追加し、44.1kHzの日本語音声を再構成。
  - 選定: アニメ向け日本語コーデックとしてAnime-XCodec2-44.1kHz-v2を採るが、CC-BY-NC・DL累計27,011で、新規開発ではMIT汎用のMioCodecが現実的。

- **音声分類(アニメ/ガルゲ調セリフの感情分類)** [アニメ特化の最良 / 確度低]: `litagin/anime_speech_emotion_classification`@6b94a022（mit、DL累計5,276、likes 6）ガルゲ音声データで学習した音声感情分類モデル(10クラス、カスタムコード使用)。
  - 選定: アニメ調の感情分類は他に無くlitagin/anime_speech_emotion_classification(MIT、DL累計5,267)を採るが、精度指標が無く性的クラスを含む。

- **音声分類(アニメ/ガルゲ声優・キャラ話者埋め込み)** [アニメ特化の最良 / 確度中]: `litagin/anime_speaker_embedding_ecapa_tdnn_groupnorm`@a2c81c47（mit、DL累計0、likes 9）アニメ/VN向け話者埋め込み(192次元、ECAPA-TDNN+GroupNorm、char版)。同じ声優でもキャラが違えば別話者として学習。VA版は声優単位で埋め込みが集約される。
  - 選定: litagin/anime_speaker_embedding(MIT、695万ファイル・7,357キャラで学習)を採用、EER 0.41%はVA版の自己報告で学習データの権利は不明。
  - リポジトリ: litagin02/anime_speaker_embedding(★23,MIT)

- **音声分類(アニメ調らしさスコア・TTS/声質の評価用)** [アニメ特化の最良 / 確度中]: `spellbrush/animescore`@eb34860d（mit、DL累計165、likes 7）HuBERTベースのアニメ調音声スコアラ(ヘッド重みのみ約9MB)。スコア差の sigmoid でペア比較確率が得られる。
  - 選定: spellbrush/animescore(MIT、論文でペア比較精度82.4%の自己報告)がアニメ調らしさ評価の唯一の公開スコアラだが、採用はDL累計165と極小。
  - リポジトリ: sizigi/animescore(★12,未表示)

- **音声区間検出(アニメ/ガルゲ音声データの切り出し・ASR前処理)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `onnx-community/silero-vad`@e71cae96（mit、DL累計0、likes 46）Silero VADのONNX変換(onnx-community、カード本文なし、YAMLメタデータのみ。バージョンは未確認)。音声/非音声を短いチャンク単位で判定する軽量VAD(公式実装はGitHub snakers4/silero-vad)。
  - 選定: アニメ特化なしのため汎用Silero VAD(GitHub★10,332、MIT)を採用、HFはonnx-community派生でアニメ演技音声での検出漏れは未評価。
  - リポジトリ: snakers4/silero-vad(★10,338,MIT) / pyannote/pyannote-audio(★10,611,MIT)

- **音声区間検出(話者分離・キャラ別発話割当て)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `pyannote/speaker-diarization-community-1`@3533c8cf（cc-by-4.0、DL累計31,926,751、likes 2,382）pyannoteの話者分離パイプライン(community-1)。16kHzモノラルを入力に、話者分離と話者カウントを出力(3.1より改善)。exclusive speaker diarization(ASRタイムスタンプとの突合せ用)を提供。
  - 選定: アニメ特化なしのため汎用のpyannote community-1(DL累計3,172万、CC-BY-4.0)を採るが、gated(承認制)でアニメ音声での精度は未評価。
  - リポジトリ: pyannote/pyannote-audio(★10,611,MIT) / NVIDIA/NeMo-Speech.cpp(★153,Apache-2.0)

- **音声+テキスト→テキスト(アニメ/ゲーム調セリフの感情・話者特徴キャプション生成、TTS学習用注釈)** [アニメ特化の最良 / 確度低]: `NandemoGHS/Anime-Speech-Japanese-Captioner`@07433a52（cc-by-nc-4.0、DL累計226、likes 10）Qwen3-Omni-30B-A3B-Captionerをfine-tuneした、日本語アニメ/ゲーム調音声のキャプション生成モデル。感情、話者像、気分、速度、韻律、ピッチ/音色、スタイルを日本語の構造化テキストで返す。
  - 選定: アニメ調音声のキャプション生成はAnime-Speech-Japanese-Captionerのみだが、CC-BY-NC・DL累計223で出力例が性的内容を含み確度は低い。
  - リポジトリ: QwenLM/Qwen3-Omni(★4,037,Apache-2.0) / modelscope/ms-swift(★15,767,Apache-2.0)

## 画像認識（検出・分割・分類・特徴）

- **物体検出(アニメ顔検出)** [アニメ特化の最良 / 確度中]: `deepghs/anime_face_detection`@784dc4c0（mit、DL累計0、likes 24）アニメ顔検出モデル群(face_detect_v0〜v1.4、n/s)。カード表にFLOPS・パラメータ・F1・閾値・ラベル(face)を記載
  - 選定: deepghs/anime_face_detectionを採用、自己報告F1 0.95・MIT・imgutils既定だが横並びベンチなくmedium。
  - リポジトリ: deepghs/imgutils(★417,MIT) / hysts/anime-face-detector(★535,MIT) / ltdrdata/ComfyUI-Impact-Subpack(★384,AGPL-3.0) / Bing-su/adetailer(★4,794,AGPL-3.0)

- **物体検出(アニメキャラクター/人物全身検出)** [アニメ特化の最良 / 確度中]: `deepghs/anime_person_detection`@e39c744c（mit、DL累計0、likes 9）アニメ人物全身検出モデル群(person_detect v0〜v1.3、n/s/m/x)
  - 選定: deepghs/anime_person_detection(自己報告F1 0.85〜0.87、MIT、imgutils既定)を採用、比較ベンチなしでmedium。
  - リポジトリ: deepghs/imgutils(★417,MIT) / Bing-su/adetailer(★4,794,AGPL-3.0)

- **物体検出(アニメ頭部検出)** [アニメ特化の最良 / 確度中]: `deepghs/anime_head_detection`@06604fee（mit、DL累計0、likes 7）アニメ頭部(髪含む)検出モデル群(YOLO各世代・RT-DETR、n/s/m/l/x)
  - 選定: deepghs/anime_head_detectionを採用、v2.0_s自己報告F1 0.92・mAP50-95 0.778、MIT、更新は2024年止まり。
  - リポジトリ: deepghs/imgutils(★417,MIT)

- **物体検出(アニメ手検出)** [アニメ特化の最良 / 確度低]: `deepghs/anime_hand_detection`@dba2c5be（openrail、DL累計0、likes 5）アニメ手検出モデル群(hand_detect v0.1〜v1.0)
  - 選定: deepghs/anime_hand_detectionを採用するが自己報告F1は0.79前後と低く、OpenRAILでconfidence low。
  - リポジトリ: deepghs/imgutils(★417,MIT) / ltdrdata/ComfyUI-Impact-Subpack(★384,AGPL-3.0)

- **物体検出(アニメ目検出)** [アニメ特化の最良 / 確度低]: `deepghs/anime_eye_detection`@ba69e3ee（openrail、DL累計0、likes 4）アニメ目検出モデル群(eye_detect v0.2〜v1.0)
  - 選定: deepghs/anime_eye_detection(自己報告F1 0.93)を採用、学習データ1K枚未満でOpenRAIL、confidence low。
  - リポジトリ: deepghs/imgutils(★417,MIT)

- **物体検出(アニメ半身検出)** [アニメ特化の最良 / 確度低]: `deepghs/anime_halfbody_detection`@95e21f43（openrail、DL累計0、likes 2）アニメ半身(halfbody)検出モデル群(halfbody_detect v0.2〜v1.0)
  - 選定: deepghs/anime_halfbody_detection(自己報告F1 0.95)が唯一の公開モデルで採用、利用実績薄くlow。
  - リポジトリ: deepghs/imgutils(★417,MIT)

- **画像セグメンテーション(キャラクター切り抜き・背景除去)** [アニメ特化の最良 / 確度低]: `joelseytre/toonout`@cbf720ec（mit、DL累計3,318、likes 24）BiRefNet(Dichotomous Image Segmentation)をアニメ画像1,228枚(ToonOutデータセット、CC-BY-4.0)で微調整した背景除去モデル。髪の毛先・線画・半透明を狙う。作者はKartoon AI
  - 選定: ToonOut採用(自作126枚でPixel Accuracy 95.3→99.5%の自己報告、MIT)、isnet-animeとの直接比較なくlow。
  - リポジトリ: danielgatis/rembg(★24,943,MIT) / MatteoKartoon/BiRefNet(★102,MIT) / 1038lab/ComfyUI-RMBG(★2,146,GPL-3.0) / SkyTNT/anime-segmentation(★845,Apache-2.0)

- **画像セグメンテーション(キャラクター部位別レイヤー分解・セマンティックパース)** [アニメ特化の最良 / 確度中]: `layerdifforg/seethroughv0.0.2_layerdiff3d`@4477e6ce（openrail++、DL累計88,980、likes 27）SDXL(Animagine XL 4.0)ベースの拡散モデルで、アニメキャラ立ち絵を19部位のRGBAレイヤーに分解し、遮蔽された部位も補完する(See-throughパイプラインの1段目)。深度モデル(seethroughv0.0.1_marigold)とセットで描画順も推定
  - 選定: See-through LayerDiff3D採用、GitHub★4,189・SIGGRAPH 2026、Apache-2.0宣言だがOpenRAIL継承で生成型のため補完は推測。
  - リポジトリ: shitagaki-lab/see-through(★4,206,Apache-2.0) / jtydhr88/ComfyUI-See-through(★814,未表示)

- **画像セグメンテーション(アニメキャラクターのインスタンス分割)** [アニメ特化の最良 / 確度低]: `dreMaz/AnimeInstanceSegmentation`@bc091c8c（mit、DL累計0、likes 10）アニメ/カートゥーン画像中の各キャラクター個体を分割するRTMDet系インスタンス分割モデルと、マスク精緻化(refine)・3D Ken Burns用深度/inpaint重みの同梱リポジトリ
  - 選定: dreMaz/AnimeInstanceSegmentation(MIT、GitHub★204)が唯一の専用実装で採用、数値ベンチなし・保守停止でlow。
  - リポジトリ: CartoonSegmentation/CartoonSegmentation(★204,未表示)

- **マスク生成(SAM系・アニメ対応)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `facebook/sam3`@3c879f39（other、DL累計21,521,678、likes 3,671）Meta Segment Anything 3。テキスト句・画像例・点/ボックス/マスクのプロンプトで、画像内の該当概念を全インスタンス分割(検出+マスク+動画追跡)する汎用モデル。アニメ専用ではない
  - 選定: アニメ特化SAMは見つからずfacebook/sam3(DL累計21.5M)をgeneral_only採用、SAM License・アニメ定量評価なし。
  - リポジトリ: facebookresearch/sam3(★11,853,NOASSERTION) / PozzettiAndrea/ComfyUI-SAM3(★574,NOASSERTION) / kijai/ComfyUI-segment-anything-2(★1,221,Apache-2.0) / 1038lab/ComfyUI-RMBG(★2,146,GPL-3.0)

- **ゼロショット物体検出(テキスト指定・アニメ画像)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `facebook/sam3`@3c879f39（other、DL累計21,521,678、likes 3,671）Meta Segment Anything 3。テキスト句・画像例・点/ボックス/マスクのプロンプトで、画像内の該当概念を全インスタンス分割(検出+マスク+動画追跡)する汎用モデル。アニメ専用ではない
  - 選定: アニメ特化なしでSAM3をgeneral_only採用(Xの実務例あり)、アニメ定量ベンチなくGrounding DINOが代替でlow。
  - リポジトリ: facebookresearch/sam3(★11,853,NOASSERTION) / IDEA-Research/GroundingDINO(★10,643,Apache-2.0) / ltdrdata/ComfyUI-Impact-Pack(★3,329,GPL-3.0)

- **キーポイント検出(アニメ顔ランドマーク28点)** [アニメ特化の最良 / 確度中]: `hysts/anime-face-detector-hrnetv2`@9b343524（mit、DL累計0、likes 1）アニメ顔の28点ランドマーク推定モデル(HRNetV2-W18、ヒートマップ)。顔領域は同梱のdetector(yolov3既定/faster-rcnn)で検出してから適用。hysts/anime-face-detectorパッケージが本体
  - 選定: hysts/anime-face-detector-hrnetv2(28点、MIT、GitHub★535)を採用、定量ベンチなく学習データ来歴は無保証。
  - リポジトリ: hysts/anime-face-detector(★535,MIT)

- **キーポイント検出(アニメ・イラストの人体ポーズ/OpenPose18)** [アニメ特化の最良 / 確度低]: `mrpm/ComfyUI-AnimePose-weights`@75396e16（agpl-3.0、DL累計0、likes 0）bizarre-pose-estimator(WACV 2022)の重みを非公式に再パッケージしたもの。anime_pose_head.safetensors(ResNet骨格+キーポイントヘッド、37.5MB)とcharacter_bg_seg.safetensors(キャラ/背景セグメンタ、233MB)を収録。ComfyUI-AnimePoseノードが初回実行時に自動DL
  - 選定: 専用モデルはbizarre-pose-estimatorのみで、HFの非公式再パッケージ(AGPL-3.0、DL0)を暫定採用、confidence low。
  - リポジトリ: ShuhongChen/bizarre-pose-estimator(★265,AGPL-3.0) / dalai2/ComfyUI-AnimePose(★3,AGPL-3.0) / Fannovel16/comfyui_controlnet_aux(★4,207,Apache-2.0)

- **深度推定(アニメキャラの擬似深度=描画順序)** [アニメ特化の最良 / 確度低]: `layerdifforg/seethroughv0.0.1_marigold`@4f4ffc46（openrail++、DL累計72,476、likes 6）Marigold Depth v1.1をアニメキャラ向けに微調整した擬似深度モデル。描画順序(ArtMeshの重なり)を画素単位で推定し、See-throughのレイヤー順序付けに使う
  - 選定: See-through Marigold(DL30日17,530)が唯一のアニメ専用深度だが描画順序を出す擬似深度で汎用不可、low。
  - リポジトリ: shitagaki-lab/see-through(★4,206,Apache-2.0)

- **深度推定(アニメ/イラストの汎用相対深度)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `depth-anything/Depth-Anything-V2-Large`@cbbb86a3（cc-by-nc-4.0、DL累計3,127,140、likes 178）単眼相対深度推定(ViT-L、vitlエンコーダ)。カード記載: 合成ラベル画像595K+実画像62M超(ラベルなし)で学習、V1やSD系(Marigold等)よりロバストかつ約10倍高速と自己主張(自己報告)。アニメ特化ではない汎用モデルで、イラスト/アニメ画像に流用して深度マップを作る用途が多い
  - 選定: アニメ専用なしでDepth-Anything-V2-Large(累計DL3.1M)をgeneral_only採用、CC-BY-NCで商用はSmall/DA3を検討。
  - リポジトリ: DepthAnything/Depth-Anything-V2(★8,891,Apache-2.0) / ByteDance-Seed/Depth-Anything-3(★6,421,Apache-2.0) / Fannovel16/comfyui_controlnet_aux(★4,207,Apache-2.0)

- **画像分類(アニメ画像マルチラベルタガー / Danbooruタグ)** [アニメ特化の最良 / 確度中]: `pixai-labs/pixai-tagger-v1.0`@9fe10add（apache-2.0、DL累計3,519、likes 70）アニメ画像向けマルチラベルタガー(Danbooru系タグ30,877種)。SAM3バックボーンを微調整し1008pxで入力、カテゴリ別推奨閾値(General0.17/Character0.27/Style0.15/Copyright0.24/Meta0.17/Rating0.41)を既定とする。PixAI Labs(PixAIは画像生成サービス)公開
  - 選定: PixAI Tagger v1.0採用(自己報告General F1 0.666、Apache-2.0)、WD v3との比較なく公開2週間でmedium。
  - リポジトリ: pythongosssss/ComfyUI-WD14-Tagger(★1,243,MIT) / sln77/ComfyUI-Tagger(★9,MIT) / jhc13/taggui(★1,351,GPL-3.0) / deepghs/imgutils(★417,MIT)

- **画像分類(アニメ画像の美的スコア/品質段階)** [アニメ特化の最良 / 確度低]: `deepghs/anime_aesthetic`@a83ab545（openrail、DL累計0、likes 12）アニメ画像を7段階の美的品質クラスに分類するdeepghsの分類器(CAFormer-S36、SwinV2 Base 448px)。imgutilsではanime_dbaesthetic系関数から利用
  - 選定: deepghs/anime_aestheticを採用、7段階でAccuracy約41%・AUC 0.82と低精度でOpenRAIL、粗いフィルタ用途のみ(low)。
  - リポジトリ: deepghs/imgutils(★417,MIT) / deepghs/waifuc(★409,MIT)

- **画像分類(AI生成アニメ画像 vs 人間作画の判定)** [アニメ特化の最良 / 確度低]: `deepghs/cls-ai-check-1m.caformer_s36.r512`@ada73d01（mit、DL累計13、likes 0）アニメ画像のAI生成/人間作画を二値分類するCAFormer-S36(512px)。deepghs/ai-check-1m(100万枚)で学習。ラベルai/human
  - 選定: deepghs/cls-ai-check-1m(自己報告Accuracy 99.5%)を採用、同一分布のみで新世代への汎化は不明、low。
  - リポジトリ: deepghs/imgutils(★417,MIT)

- **画像分類(アニメ画像の種別: イラスト/漫画/アニメ映像/3D/非絵画)** [アニメ特化の最良 / 確度中]: `deepghs/anime_classification`@5ee62e06（mit、DL累計0、likes 23）アニメ画像の種別を5クラス(3d/bangumi/comic/illustration/not_painting)に分類するdeepghs分類器。データセット構築のフィルタ用途(漫画・映像・3Dの除外等)
  - 選定: deepghs/anime_classification(自己報告Accuracy 95〜96%、MIT、5クラス)を採用、公開ベンチなしでmedium。
  - リポジトリ: deepghs/imgutils(★417,MIT)

- **ゼロショット画像分類(アニメCLIP)** [アニメ特化の最良 / 確度低]: `OysterQAQ/DanbooruCLIP`@aa2e6030（未記載、DL累計52,567、likes 16）CLIP ViT-L/14をDanbooru2021(+pixiv)で微調整したアニメ画像-テキスト対照モデル。キャラ名・作品名・タグ文でゼロショット分類/検索ができる
  - 選定: DanbooruCLIP(DL累計52,553)を採用、2023年版で定量評価・ライセンス表記なしのためconfidence low。
  - リポジトリ: deepghs/imgutils(★417,MIT)

- **特徴量抽出(アニメキャラクター同一性=CCIP埋め込み)** [アニメ特化の最良 / 確度中]: `deepghs/ccip`@8f636fb8（openrail、DL累計0、likes 13）1画像1キャラを前提に、アニメキャラの同一性を埋め込みの距離で判定するdeepghsのCCIP(CAFormer系)。データセット整理(キャラ別クラスタリング、他キャラ混入の除去)に使われる
  - 選定: deepghs/ccip採用、自己報告F1 0.94、imgutils/waifuc組込、OpenRAILで単一キャラ画像前提(medium)。
  - リポジトリ: deepghs/imgutils(★417,MIT) / deepghs/waifuc(★409,MIT)

- **特徴量抽出(アニメ画像の類似検索・重複検出の汎用埋め込み)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `facebook/dinov3-vitl16-pretrain-lvd1689m`@ea8dc286（other/dinov3-license、DL累計7,686,591、likes 992）DINOv3の蒸留ViT-L/16(LVD-1689M事前学習)。クラストークン/パッチ特徴を抽出し、類似画像検索・重複検出・クラスタリング等に使う汎用自己教師あり埋め込み。アニメ特化ではない
  - 選定: アニメ専用なしでDINOv3 ViT-L(30日DL628k)をgeneral_only採用、アニメ評価未確認でゲート付き独自ライセンス、low。
  - リポジトリ: facebookresearch/dinov3(★11,483,NOASSERTION) / deepghs/imgutils(★417,MIT)

## マンガ・OCR・文書

- **画像→テキスト(漫画の吹き出し・台詞クロップOCR)** [アニメ特化の最良 / 確度低]: `JustANormalTinkerer/hayai-ocr-v2.5-nova`@e34d7755（apache-2.0、DL累計1,153、likes 0）約150MパラメータのCJK+英語OCR。SigLIP2 NaFlex視覚エンコーダ(約86M)+12層因果デコーダ(約60M)。v2.5はDSCProjectorでデコーダ側視覚トークンを1/4にし、静的KVキャッシュで高速化。検出器なしで切り抜き1枚を1回のforwardで文字列にする。
  - 選定: Hayai OCR v2.5 Nova(JMangaBench CER 3.10%、自己報告)を暫定best。manga-ocr-base(累計DL975万)が安全な既定で、Nova作成11日・低信頼。
  - リポジトリ: koharu-rs/koharu(★5,702,Apache-2.0) / NopeNopeGuy/hayai-ocr(★8,Apache-2.0) / kha-white/manga-ocr(★2,792,Apache-2.0) / muscgab/JMangaBench_Mixed(★1,GPL-3.0)

- **画像→テキスト(オノマトペ・効果音SFXのOCR)** [アニメ特化の最良 / 確度低]: `JustANormalTinkerer/hayai-ocr-v2.5-nova`@e34d7755（apache-2.0、DL累計1,153、likes 0）Hayai OCR v2.5 Nova(切り抜きOCR、約150M)。日本語・中国語・韓国語・英語のSFX/手書き風文字を含む切り抜きを読む。SFX(COO)に強い点は第三者評価・別作者の表で確認されている。
  - 選定: 擬音OCRはHayai Nova(別作者表でSFX CER 17.0%)を暫定best。標準manga-ocrはSFXに弱く、Nova単独の第三者評価は未公開で低信頼。
  - リポジトリ: koharu-rs/koharu(★5,702,Apache-2.0) / ku21fan/COO-Comic-Onomatopoeia(★95,未表示) / NopeNopeGuy/hayai-ocr(★8,Apache-2.0)

- **画像→テキスト(ギャルゲー/VN・ゲーム画面の日本語OCR)** [アニメ特化の最良 / 確度中]: `rtr46/meiki.txt.recognition.v0`@a28cf587（lgpl-3.0、DL累計677,180、likes 7）日本語ビデオゲーム画面のテキスト行認識モデル。『文字認識を文字検出に置き換える』D-FINE系のファインチューン(MobileNetV4バックボーン)。960x32に整形した行画像から最大48文字を文字+bbox+信頼度で出力。検出モデル meiki.text.detect(tiny=VN向け低遅延、small=行数が多い画面向け)と組で meikiocr パッケージになる。
  - 選定: VN・ゲーム画面はrtr46/meiki.txt.recognition.v0(30日DL約9.8万)。数値ベンチ無し・横書きのみで、HFはLGPL-3.0、GitHubはApache-2.0と表記不一致。
  - リポジトリ: rtr46/meikiocr(★97,Apache-2.0) / AuroraWright/owocr(★301,GPL-3.0) / HIllya51/LunaTranslator(★13,500,GPL-3.0) / bpwhelan/GameSentenceMiner(★859,GPL-3.0)

- **画像→テキスト(アニメ・イラストのキャプション/booruタグ生成)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `fancyfeast/llama-joycaption-beta-one-hf-llava`@ebf414ea（未記載、DL累計1,789,303、likes 400）Llama-3.1-8B-Instruct+SigLIP2(so400m-patch14-384)ベースの画像キャプションVLM。拡散モデル学習用に『自由・無検閲・多様』を掲げ、写真・デジタルアート・アニメ等を同等に扱う。GitHub README によれば Danbooru/e621/Rule34 タグ列や Stable Diffusion プロンプト風など複数のプロンプトモードを持つ。
  - 選定: アニメ特化の実用キャプショナは無く、汎用JoyCaption Beta One(累計DL178万、Danbooruタグ出力可)を採用。Llama系ライセンス要確認。
  - リポジトリ: fpgaminer/joycaption(★1,268,Apache-2.0)

- **画像+テキスト→テキスト(漫画ページ理解VLM:ページOCR+VQA)** [アニメ特化の最良 / 確度中]: `hal-utokyo/MangaLMM`@a556fbc7（mit、DL累計9,342、likes 13）Qwen2.5-VL-7B-Instruct を MangaOCR(Manga109+COO由来、全体約20.9万インスタンス、うち訓練約17万)と合成VQA(GPT-4oが生成した約4万問)で1エポックのみ共同ファインチューンした漫画特化LMM。ページ単位で『bbox_2d + text_content』のJSONを出力するOCRと、漫画内容についてのVQAの双方を1モデルで扱う。
  - 選定: 漫画専用VLMはMangaLMM(ページOCR Hmean 71.5%、他VLMは0%台、論文ベンチ)。Qwen2.5-VL-7B基盤で古く、Manga109学習で商用は要注意。
  - リポジトリ: manga109/MangaLMM(★50,MIT) / koharu-rs/koharu(★5,702,Apache-2.0)

- **視覚的質問応答(漫画ページの内容理解:MangaVQA)** [アニメ特化の最良 / 確度中]: `hal-utokyo/MangaLMM`@a556fbc7（mit、DL累計9,342、likes 13）manga-understanding-vlm と同一モデル。漫画ページに対する事実質問(誰が・何を・いつ…)と文脈説明に答える。
  - 選定: 漫画VQAはMangaLMM(MangaVQA 6.68/10、GPT-4o 6.00超え・Gemini 2.5 Flash 7.26未満)。著者ベンチで、新世代VLMとの比較は未検証。
  - リポジトリ: manga109/MangaLMM(★50,MIT)

- **文書質問応答(漫画ページ・VN画面)**: 該当なし。漫画・VN向けの文書QAモデルはHFに0件で該当なし。漫画ページQAはMangaLMM、VN画面は通常OCRで代替する。

- **視覚的文書検索(漫画ページ・イラストの検索)**: 該当なし。漫画・アニメ特化の視覚文書検索モデルはHFに0件で該当なし。汎用ColPali系は漫画での精度が未確認のため推奨しない。

- **any-to-any(アニメ・漫画向けマルチモーダル生成)**: 該当なし。アニメ特化のany-to-anyモデルはHFに0件で該当なし。AnimeGamerはtext-to-video扱いで30日DL27と実績が乏しい。

- **漫画レイアウト検出(文字・擬音・吹き出し・コマの検出+インスタンスマスク)** [アニメ特化の最良 / 確度中]: `mayocream/koharu-layout-rfdetr-seg-2xl-1152`@aed55fdb（other、DL累計0、likes 7）RF-DETR Seg 2XL(rfdetr==1.7.0)を1152pxで漫画ページ用に学習したレイアウト解析器。クラス: 0=text(台詞・キャプション・クレジット等)、1=onomatopoeia、2=bubble、3=panel。教師は Manga109 Segmentation v2.0.0(Zenodoの手描きTextSegマスク、PP-DocLayoutV3提案、koharu-text-sam-ts-lで精緻化)。
  - 選定: 漫画レイアウト検出はKoharu Layout RF-DETR(box mAP50-95 0.797、自己報告)。Manga109全巻学習で商用不可、安全策はogkaluのApache-2.0版。
  - リポジトリ: koharu-rs/koharu(★5,702,Apache-2.0) / roboflow/rf-detr(★9,674,Apache-2.0) / ogkalu2/comic-translate(★2,963,Apache-2.0) / dmMaze/BallonsTranslator(★5,173,GPL-3.0)

- **アニメ・イラスト・カラー漫画内テキストブロック検出(枠外文字・題字含む)** [アニメ特化の最良 / 確度中]: `deepghs/AnimeText_yolo`@a180c191（gpl-3.0、DL累計0、likes 28）AnimeText データセット(735K枚/4.2Mブロック)で学習した YOLO12 検出器の n/s/m/l/x 5サイズ。クラスは text_block のみ(hard negativeで記号・装飾を区別)。オンラインデモ Space あり(deepghs/AnimeText_yolo)。
  - 選定: アニメ・イラスト内文字検出はdeepghs/AnimeText_yolo(73.5万枚学習、yolo12x mAP50 0.952、自己報告)。GPL-3.0・ゲート付きで最終更新2025-10。
  - リポジトリ: meangrinch/MangaTranslator(★332,Apache-2.0) / koharu-rs/koharu(★5,702,Apache-2.0)

- **漫画の読み順・コマ/文字/キャラ/吹き出し尾の関連付け(台詞の話者推定)** [アニメ特化の最良 / 確度低]: `ragavsachdeva/magiv3`@49c73a22（未記載、DL累計34,601、likes 20）コミック理解の統合VLM。画像+タスクプロンプトから、コマ・キャラクター・文字・吹き出し尾の検出と関連付け(predict_detections_and_associations)、OCR(predict_ocr)、キャプション中のキャラのコマ内接地(predict_character_grounding)をテキスト出力する。
  - 選定: 読み順・話者関連付けはMagiv3(ICCV2025、Char-Char AMI 0.68)のみ確認。専用の読み順指標が無く低信頼、ライセンスは非商用。
  - リポジトリ: ragavsachdeva/magi(★470,未表示)

- **漫画の文字消去・インペイント(吹き出し/背景のテキスト除去)** [アニメ特化の最良 / 確度中]: `dreMaz/AnimeMangaInpainting`@2953a4e9（mit、DL累計0、likes 30）advimman/lama の Big-LaMa(FFC ResNetジェネレータ)を漫画・アニメ風データ約30万枚でファインチューンした512px用チェックポイント。マスク領域を埋めて文字・ロゴ・局所物体を除去する。
  - 選定: 漫画文字消去は漫画・アニメ30万枚で微調整したLaMa(dreMaz/AnimeMangaInpainting)。Koharu・comic-translate等が採用するが定量ベンチは皆無。
  - リポジトリ: koharu-rs/koharu(★5,702,Apache-2.0) / dmMaze/BallonsTranslator(★5,173,GPL-3.0) / advimman/lama(★10,286,Apache-2.0) / zyddnys/manga-image-translator(★10,463,GPL-3.0)

- **漫画翻訳パイプライン(検出→OCR→消去→翻訳→植字)のアプリ/OSS選定** [モデルなし / 確度中]: モデルなし（リポジトリのみ）
  - 選定: 単一モデルでなくアプリ層のため該当なし。採用実績順の本命はKoharu(5,693★、Apache-2.0、2026-09リリース)、GPL系は組込み制約あり。
  - リポジトリ: koharu-rs/koharu(★5,702,Apache-2.0) / dmMaze/BallonsTranslator(★5,173,GPL-3.0) / ogkalu2/comic-translate(★2,963,Apache-2.0) / zyddnys/manga-image-translator(★10,463,GPL-3.0)

## 言語（翻訳・生成・埋め込み）

- **翻訳(日本語→簡体字中国語: ギャルゲー/ラノベ)** [アニメ特化の最良 / 確度中]: `SakuraLLM/Sakura-GalTransl-7B-v3.7`@759d76b1（cc-by-nc-sa-4.0、DL累計1,192,889、likes 113）ビジュアルノベル(Galgame)翻訳に特化した7Bの日→簡体中国語翻訳LLM(GGUF配布)。行内改行・制御文字・ルビの保持に配慮し、用語表(GPT辞書)と直前の訳文履歴を渡せる。GalTransl/LunaTranslator用に調整。
  - 選定: Sakura-GalTransl-7B-v3.7を採用(累計119万DL、LunaTranslator等が対応)、定量ベンチ無く商用禁止のCC-BY-NC-SA。
  - リポジトリ: SakuraLLM/SakuraLLM(★4,795,GPL-3.0) / GalTransl/GalTransl(★2,296,GPL-3.0) / HIllya51/LunaTranslator(★13,500,GPL-3.0) / neavo/LinguaGacha(★2,525,未表示)

- **翻訳(日本語→英語: ビジュアルノベル)** [アニメ特化の最良 / 確度低]: `lmg-anon/vntl-llama3-8b-v2-gguf`@ab7c8285（llama3、DL累計6,046,283、likes 17）VN(ビジュアルノベル)台本のJP→EN翻訳用に rinna/llama-3-youko-8b をQLoRA(rank128)で微調整した8Bモデルの量子化GGUF版。キャラ名・性別・別称等のMetadataをプロンプトに与えられ、複数行翻訳に対応。
  - 選定: vntl-llama3-8b-v2(GGUF)を採用、自前256文ボードでGoogle翻訳超えだがGPT-4o等に劣り2025-01から更新停止。
  - リポジトリ: HIllya51/LunaTranslator(★13,500,GPL-3.0) / lmg-anon/vntl-benchmark(★3,AGPL-3.0) / ciddwd/overlay-translator(★927,Apache-2.0)

- **テキスト生成(タグ/プロンプト拡張: Danbooruタグ→詳細プロンプト)** [アニメ特化の最良 / 確度中]: `KBlueLeaf/TIPO-500M-ft`@386fc21b（other/kohaku-license-1.0、DL累計437,473、likes 48）短いタグ/自然言語キャプションを、Danbooruタグ様式＋自然文の詳細プロンプトへ拡張するLLaMA系500Mモデル(TIPO)。T2Iに渡す前段のプリサンプリングで多様性を保ちつつ質を上げる。
  - 選定: TIPO-500M-ftを採用(累計43万DL、ICLR 2026採択、拡張637★)、評価は200Mでの自己報告でKohaku License。
  - リポジトリ: KohakuBlueleaf/z-tipo-extension(★637,Apache-2.0) / KohakuBlueleaf/KGen(★102,Apache-2.0) / DominikDoom/a1111-sd-webui-tagcomplete(★2,808,MIT)

- **テキスト生成(キャラクターロールプレイ/キャラカード対話)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `hiwaifu-research/WaifuGemma4-26b-a4b-v1`@540c0f8f（apache-2.0、DL累計1,434、likes 21）Gemma 4 26B-A4B(3.8B active MoE)をHiWaifuアリーナの人間投票由来の報酬モデルでGRPO(200step, LoRA r256)した汎用ロールプレイモデル。
  - 選定: アニメ特化は無く汎用のWaifuGemma4を暫定採用、勝率54.7%は自社アリーナの自己報告で公開12日と実績薄。
  - リポジトリ: SillyTavern/SillyTavern(★34,005,AGPL-3.0) / jofizcd/Soul-of-Waifu(★1,363,GPL-3.0)

- **テキスト生成(日本語ラノベ/シナリオ生成)**: 該当なし。非成人向けで実績ある日本語シナリオ専用モデルは無く、有力系統はNSFW特化のため収録せず汎用LLMを使う。

- **文類似度(日本語埋め込み: アニメ/キャラ検索用途)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `cl-nagoya/ruri-v3-310m`@18b60fb8（apache-2.0、DL累計5,669,075、likes 82）日本語汎用テキスト埋め込みモデル(ModernBERT-Ja基盤、768次元、最大8192トークン、語彙100K)。プレフィックス方式('検索クエリ: '等)で用途を切替。
  - 選定: アニメ特化は実績無く、汎用のruri-v3-310mを採用(累計562万DL、JMTEB 77.24)、値は自己報告でアニメ語彙は未検証。
  - リポジトリ: huggingface/sentence-transformers(★19,144,Apache-2.0) / sbintuitions/JMTEB(★93,CC-BY-SA-4.0)

- **特徴抽出(日本語テキスト埋め込み/タグ・キャラ語彙)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `cl-nagoya/ruri-v3-310m`@18b60fb8（apache-2.0、DL累計5,669,075、likes 82）日本語汎用テキスト埋め込みモデル(ModernBERT-Ja基盤、768次元、最大8192トークン、語彙100K)。プレフィックス方式('検索クエリ: '等)で用途を切替。
  - 選定: アニメ特化は実績無く、汎用のruri-v3-310mを採用(Apache-2.0)、英日混在タグは多言語モデルとの比較が未実施で低信頼。
  - リポジトリ: huggingface/sentence-transformers(★19,144,Apache-2.0)

- **リランキング(日本語リランカー: アニメ検索用途)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `cl-nagoya/ruri-v3-reranker-310m`@bb46934e（apache-2.0、DL累計1,461,577、likes 17）日本語汎用リランカー(ModernBERT-Ja基盤CrossEncoder、最大8192トークン)。検索結果の再順位付け用。
  - 選定: 汎用のruri-v3-reranker-310mを採用(30日30万DL、JQaRA nDCG@10 86.9)、自己報告でアニメ領域は未検証。
  - リポジトリ: huggingface/sentence-transformers(★19,144,Apache-2.0)

- **穴埋め(日本語マスクLM)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `sbintuitions/modernbert-ja-130m`@28c180b1（mit、DL累計473,809、likes 51）日本語ModernBERT(130M、語彙102,400、最大8192トークン)。主にファインチューニングの土台として使うエンコーダ。
  - 選定: アニメ特化は無く、汎用のmodernbert-ja-130mを採用(累計47万DL、MIT)、fill-mask単体でなく下流微調整前提。

- **トークン分類(日本語NER: 作品名/キャラ名/声優名)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `llm-book/bert-base-japanese-v3-ner-wikipedia-dataset`@49ef0cba（apache-2.0、DL累計1,642,221、likes 11）cl-tohoku/bert-base-japanese-v3をWikipedia固有表現データで微調整した日本語NER。人名・地名・組織名等を抽出。
  - 選定: アニメ固有名詞NERやふりがな推定の公開モデルは無く、汎用のllm-book日本語NERを代用、アニメ名詞への精度は未検証。

- **ゼロショット分類(ジャンル/レーティング/同人ラベル)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `MoritzLaurer/bge-m3-zeroshot-v2.0`@9abf1c8a（mit、DL累計3,754,408、likes 70）bge-m3-retromae基盤の多言語ゼロショット分類器(NLI形式、entailment/not_entailment)。任意ラベルで分類できる。
  - 選定: アニメ特化は無く汎用のbge-m3-zeroshot-v2.0を暫定採用(累計375万DL、MIT)、日本語性能の数値は未確認で低信頼。

- **要約(アニメ/エピソード/小説あらすじ)**: 該当なし。アニメ・小説向けの実績ある要約モデルは無く、汎用LLMのプロンプトで足りるため収録しない。

- **質問応答(アニメ/オタク知識QA)**: 該当なし。アニメ知識QAの信頼できる公開モデルは無く(候補は累計18DL)、LLMと検索の組み合わせで対応するため収録しない。

- **テキスト分類(アニメ感想感情/ジャンル/同人向け毒性)**: 該当なし。アニメ特化の分類器は個人実験規模(累計25DL等)で採用根拠が弱く、LLMのゼロショットで足りるため収録しない。

- **表形式質問応答**: 該当なし。アニメや日本語向けの表QAモデルは存在せず需要も乏しいため収録しない。

## 3D・アバター・その他

- **アニメイラストの2.5Dレイヤ分解(Live2D/PSD向け)** [アニメ特化の最良 / 確度高]: `layerdifforg/seethroughv0.0.2_layerdiff3d`@4477e6ce（openrail++、DL累計88,980、likes 27）アニメ・イラスト1枚を、髪・顔・目・服などの意味パーツ(最大23レイヤ)に分解し、隠れ部分を補完した透過レイヤと描画順を出力する See-through パイプラインの LayerDiff 3D(SDXL系、Animagine XL 4.0派生)。深度モデル(Marigold派生)と併用して PSD を出力する。
  - 選定: See-throughのLayerDiff 3Dを採用(30日DL 19,507・GitHub★4,189・X実使用報告多数)、ただしOpenRAIL制限継承で精度は自己報告、Live2Dリグは対象外。
  - リポジトリ: shitagaki-lab/see-through(★4,206,Apache-2.0) / jtydhr88/ComfyUI-See-through(★814,未表示) / MangoLion/stretchystudio(★494,MIT) / 852wa/Anime2.5DRig(★232,MIT)

- **画像から3D(アニメキャラ単体のメッシュ生成)** [アニメ特化の最良 / 確度低]: `hyz317/StdGEN`@8d12f6e3（apache-2.0、DL累計0、likes 16）アニメキャラ1枚絵から、体・服・髪などに意味分解された3Dキャラクターを約3分で生成する CVPR 2025 のパイプライン。A-pose化(canonicalize)→多視点画像(multiview)→Semantic-aware LRM(S-LRM)→多層リファイン。VRoid Hub 由来の Anime3D++ で学習。
  - 選定: アニメ専用OSSのStdGENを暫定採用(論文でCharacterGenに勝つが自己報告)、HF DL 0・実使用報告なしでconfidence低、重みは研究目的扱い。
  - リポジトリ: hyz317/StdGEN(★396,Apache-2.0) / zjp-shadow/CharacterGen(★835,Apache-2.0) / VAST-AI-Research/AniGen(★509,NOASSERTION) / microsoft/TRELLIS.2(★11,433,MIT)

- **アニメ3Dキャラの自動リギング(骨格・スキニング)** [汎用モデルのみ（アニメ特化なし） / 確度低]: `VAST-AI/SkinTokens`@79736cad（mit、DL累計0、likes 32）3Dメッシュから骨格(skeleton)とスキニングウェイトを単一の自己回帰トークン列(TokenRig, Qwen3-0.6B系、GRPO精緻化)で生成する自動リギングモデル。UniRigの後継。学習データは ArticulationXL 2.0(70%)・VRoid Hub(20%)・ModelsResource(10%)。
  - 選定: アニメ専用は無く、VRoid Hubを学習20%含む汎用SkinTokens(MIT)を暫定採用、HF DL 0で実績は旧UniRig(★1,781)が上、精度改善は自己報告。
  - リポジトリ: VAST-AI-Research/SkinTokens(★442,MIT) / VAST-AI-Research/UniRig(★1,783,MIT) / jasongzy/Make-It-Animatable(★459,MIT) / saturday06/VRM-Addon-for-Blender(★1,718,MIT)

- **テキストからの3Dモーション生成(キャラアニメ用)** [汎用モデルのみ（アニメ特化なし） / 確度中]: `nvidia/Kimodo-SOMA-RP-v1.1`@6c9233af（other/nvidia-open-model-license、DL累計20,666、likes 70）テキストと運動制約(全身ポーズ・2Dルート・エンドエフェクタ)から3D人体スケルトンアニメーションを生成するモーション拡散モデル。SOMAスケルトン、Bones Rigplay 1(700時間の光学モーキャプ)で学習。
  - 選定: アニメ専用は無く汎用のNVIDIA Kimodo-SOMA-RP-v1.1を採用(累計DL 20,316・★3,667・日本語圏派生多数)、人体限定でVRM/MMDへの変換が別途必要。
  - リポジトリ: nv-tlabs/kimodo(★3,681,Apache-2.0) / Kirakun0328/text-to-vrma(★184,MIT) / localai-org/kimodo.cpp(★885,Apache-2.0) / jtydhr88/ComfyUI-HY-Motion1(★313,未表示)

- **テキストから3D形状(アニメキャラ)生成**: 該当なし。アニメ専用のテキスト→3D形状モデルは無く、汎用TRELLIS-textも2025年で更新停滞のため、画像経由(image-to-3d)を推奨し推奨モデルは置かない。

- **アニメゲーム/ワールドモデル(次状態予測による対話的アニメ生成)** [アニメ特化の最良 / 確度低]: `TencentARC/AnimeGamer`@a9a2384a（other/animegamer-lisence、DL累計295、likes 46）マルチモーダルLLMが『次のゲーム状態(アニメ調の動画クリップ+体力・社交・娯楽などのキャラ状態)』を予測し、拡散デコーダで動画化する、アニメ世界のライフシミュレーション(ICCV 2025)。
  - 選定: アニメ世界モデルは公開重みがTencentARC/AnimeGamerのみで暫定採用、ジブリ2作品の個別版に限り累計DL 295と低く、EU利用不可の独自ライセンス。
  - リポジトリ: TencentARC/AnimeGamer(★351,NOASSERTION)

- **ピクセルアート・スプライト生成** [汎用モデルのみ（アニメ特化なし） / 確度低]: `nerijs/pixel-art-xl`@8bf4a4d9（creativeml-openrail-m、DL累計946,500、likes 656）SDXL用のピクセルアート LoRA(1ファイル)。8倍縮小+最近傍補間でピクセル整列画像を得る運用。トリガーワード不要、LCM LoRA併用で8ステップ生成も可。
  - 選定: アニメ専用は無く汎用のnerijs/pixel-art-xlを採用(累計DL 945,353・likes 656)、2023-11から更新停止でOpenRAIL系、最新品質の裏付けは無い。

- **漫画フォント・写植(フォント生成/識別)**: 該当なし。HFとGitHubで漫画・日本語のフォント生成/識別モデルは見つからず、欧文の汎用フォント識別のみのため該当なしとした。

- **アニメ2Dアバターのアニメーション(1枚絵駆動・Live2D代替・表情差分)** [モデルなし / 確度低]: モデルなし（リポジトリのみ）
  - 選定: HFに公式重みが無く推奨モデルは立てず、EasyVtuber(★3,071)やInochi2D(★1,799)等のリポジトリを参照、THA系は2024年以降更新停止。
  - リポジトリ: yuyuyzl/EasyVtuber(★3,072,MIT) / pkhungurn/talking-head-anime-4-demo(★355,MIT) / Inochi2D/inochi2d(★1,802,BSD-2-Clause) / kazuya-bros/PachiPakuGen(★130,MIT)

- **VTuber/AIキャラクター対話エージェント基盤(Live2D/VRM+LLM+TTS+ASR)** [モデルなし / 確度中]: モデルなし（リポジトリのみ）
  - 選定: HFに有力モデルは無くGitHubのフレームワークが実体で、moeru-ai/airi(★49,887・MIT・2026-09更新)が首位、ライセンスは各リポジトリで要確認。
  - リポジトリ: moeru-ai/airi(★49,923,MIT) / Open-LLM-VTuber/Open-LLM-VTuber(★13,965,NOASSERTION) / tegnike/aituber-kit(★1,114,NOASSERTION)

- **VRM/MMD/3Dアバター基盤ツール(ビューア・DCC連携・ゲームエンジン)** [モデルなし / 確度高]: モデルなし（リポジトリのみ）
  - 選定: モデルではなくランタイム領域で、three-vrm・UniVRM・VRM-Addon-for-Blenderの公式実装がいずれも2026年更新のMITで標準、HFモデルは不要。
  - リポジトリ: pixiv/three-vrm(★2,193,MIT) / vrm-c/UniVRM(★3,392,MIT) / saturday06/VRM-Addon-for-Blender(★1,718,MIT) / ruyo/VRM4U(★1,989,NOASSERTION)

- **モーションキャプチャ・リターゲット(VRM/MMD/Mixamo)** [モデルなし / 確度低]: モデルなし（リポジトリのみ）
  - 選定: HFに該当モデルは無く、SysMocap(★3,224)等のGitHubツールが実用、汎用標準は未確立でGPL-3.0や未設定ライセンスが混在する。
  - リポジトリ: xianfei/SysMocap(★3,223,MPL-2.0) / ButzYung/SystemAnimatorOnline(★1,900,未表示) / AmyangXYZ/reze-mipo(★665,GPL-3.0) / tk256ailab/fbx2vrma-converter(★63,MIT)

- **アニメ3Dキャラ・リグのデータセット(Anime3D/Anime3D++/AnimeRig)** [モデルなし / 確度中]: モデルなし（リポジトリのみ）
  - 選定: Anime3D/Anime3D++は生VRMの再配布不可でスクリプトのみ公開、AnimeRigも未確認のため、推奨できる公開アニメ3Dデータセットは無い。
  - リポジトリ: ShuhongChen/panic3d-anime-reconstruction(★831,未表示)

- **表形式分類(アニメ関連)**: 該当なし。HFでアニメ関連の表形式分類モデルを検索したが、唯一のヒットは作者名が一致しただけの無関係な与信モデルで、該当なし。

- **表形式回帰(アニメ評価・人気予測)**: 該当なし。HFでアニメ関連の表形式回帰モデルを検索してヒット0件で、評価・人気予測の公開モデルは存在せず、該当なし。

- **時系列予測(アニメ視聴数・配信者統計等)**: 該当なし。HFでアニメ関連の時系列予測モデルを検索してヒット0件で、アニメ専用の公開モデルは存在せず、該当なし。

- **強化学習(VTuber/アニメキャラエージェント)**: 該当なし。HFの検索結果はユーザー名一致の強化学習コース演習のみで、アニメ用途のモデルは無く、VTuberエージェントも強化学習ではないため該当なし。

- **ロボティクス(アニメキャラ/VTuberロボット)**: 該当なし。HFでアニメ関連のロボティクスモデルを検索してヒット0件で、Kimodoのロボット版もアニメ制作とは無関係のため、該当なし。

- **グラフ機械学習(キャラ関係図・アニメ推薦グラフ)**: 該当なし。HFでアニメ関連のグラフ機械学習モデルを検索してヒット0件で、推薦も文埋め込みの個人モデルのみのため、該当なし。

- **その他(HFのタスク未設定・other分類のアニメ関連モデル)**: 該当なし。タグ未設定の重要モデルは各タスク(See-through・Kimodo・SkinTokens等)へ統合済みで、残りは低利用の派生のみのため単独推奨は無い。

## 制作工程別リポジトリ全体像

- **学習フレームワーク(画像・Anima/SDXL LoRA)**: kohya-ss/sd-scripts(★7,241,Apache-2.0,push 2026-09-24) / ostris/ai-toolkit(★12,179,MIT,push 2026-09-27) / Nerogar/OneTrainer(★3,224,AGPL-3.0,push 2026-09-28) / gazingstars123/Anima-Standalone-Trainer(★329,Apache-2.0,push 2026-08-28)
  - Anima公式docs対応のkohya-ss/sd-scripts(★7242)を第一候補、次にai-toolkit(★12164)。OneTrainerはAGPL-3.0、Anima本体は非商用に注意。

- **学習フレームワーク(動画・Wan/MiniMax等、音声は対象外)**: kohya-ss/musubi-tuner(★2,077,未表示,push 2026-09-30) / tdrussell/diffusion-pipe(★2,028,GPL-3.0,push 2026-09-28) / bghira/SimpleTuner(★2,930,AGPL-3.0,push 2026-10-01) / modelscope/DiffSynth-Studio(★13,200,Apache-2.0,push 2026-09-30)
  - 動画LoRAはkohya-ss/musubi-tuner(★2074、2026-09-27更新)が最有力だがライセンス未検出で要確認、アニメ特化の動画学習ツールは無い。

- **ComfyUIのアニメ関連エコシステム(本体・テンプレ・Anima拡張)**: Comfy-Org/ComfyUI(★135,777,GPL-3.0,push 2026-10-01) / Comfy-Org/workflow_templates(★1,227,MIT,push 2026-10-01) / kohya-ss/ComfyUI-Anima-LLLite(★215,Apache-2.0,push 2026-08-02) / Ararararararaki/comfyui-anima-toolkit(★31,MIT,push 2026-10-01)
  - 土台はComfy-Org/ComfyUI(★135621)とAnima対応の公式テンプレ、Anima固有はkohya-ss/ComfyUI-Anima-LLLite(★215)。拡張類は小規模。

- **データセット構築(収集・タグ付け・キュレーション)**: mikf/gallery-dl(★19,904,GPL-2.0,push 2026-09-27) / Bionus/imgbrd-grabber(★3,210,Apache-2.0,push 2026-09-26) / deepghs/imgutils(★417,MIT,push 2025-10-11) / starik222/BooruDatasetTagManager(★1,948,MIT,push 2026-02-25)
  - 収集はmikf/gallery-dl(★19893)、自動処理はdeepghs/imgutils(★415)だが最終push2025-10で鈍化、waifucは停滞。重複排除repoは未発見。

- **アニメ動画の超解像・フレーム補間**: AaronFeng753/Waifu2x-Extension-GUI(★17,067,NOASSERTION,push 2026-09-19) / NevermindNilas/TheAnimeScripter(★330,AGPL-3.0,push 2026-09-28) / the-database/VideoJaNai(★280,GPL-3.0,push 2026-06-18) / k4yt3x/video2x(★21,916,AGPL-3.0,push 2026-03-07)
  - 実績はAaronFeng753/Waifu2x-Extension-GUI(★17060)とvideo2x、更新最速はTheAnimeScripter(★329)。Anime4K等は停滞、ライセンス要確認。

- **漫画翻訳(検出・OCR以外のアプリ層)**: koharu-rs/koharu(★5,702,Apache-2.0,push 2026-10-01) / dmMaze/BallonsTranslator(★5,173,GPL-3.0,push 2026-10-01) / zyddnys/manga-image-translator(★10,463,GPL-3.0,push 2026-09-25) / ogkalu2/comic-translate(★2,963,Apache-2.0,push 2026-09-11)
  - 更新・Apache-2.0・採用でkoharu-rs/koharu(★5693)を第一候補、編集重視はBallonsTranslator(★5171、GPL-3.0)。

- **ビジュアルノベル・ゲーム翻訳/テキストフック**: HIllya51/LunaTranslator(★13,500,GPL-3.0,push 2026-10-01) / GalTransl/GalTransl(★2,296,GPL-3.0,push 2026-09-30) / SakuraLLM/SakuraLLM(★4,795,GPL-3.0,push 2026-07-23) / bpwhelan/GameSentenceMiner(★859,GPL-3.0,push 2026-10-01)
  - VN翻訳はHIllya51/LunaTranslator(★13485、2026-09-26更新)が本命、パッチ制作はGalTransl(★2293)。いずれもGPL-3.0、X上の評判は未確認。

- **VTuber/Live2D/VRM/アバター基盤**: pixiv/three-vrm(★2,193,MIT,push 2026-09-30) / vrm-c/UniVRM(★3,392,MIT,push 2026-09-25) / saturday06/VRM-Addon-for-Blender(★1,718,MIT,push 2026-09-30) / emilianavt/OpenSeeFace(★2,080,BSD-2-Clause,push 2026-09-18)
  - VRMはpixiv/three-vrm(★2192)とUniVRM(★3392)が標準で更新も活発。Inochi2Dは停滞、Live2D本体は公開repo無し、信頼度は中程度。

- **AIコンパニオン・キャラチャット・AITuber**: moeru-ai/airi(★49,923,MIT,push 2026-10-01) / SillyTavern/SillyTavern(★34,005,AGPL-3.0,push 2026-09-23) / Open-LLM-VTuber/Open-LLM-VTuber(★13,965,NOASSERTION,push 2026-05-15) / tegnike/aituber-kit(★1,114,NOASSERTION,push 2026-09-30)
  - 勢い重視でmoeru-ai/airi(★49887、MIT、ベータ版)、チャット標準はSillyTavern(★33968、AGPL-3.0)。aituber-kitは商用条件に注意。

- **日本語キャラクター向けTTS/音声エンジン**: Aratako/Irodori-TTS(★1,373,MIT,push 2026-09-12) / VOICEVOX/voicevox_engine(★1,764,NOASSERTION,push 2026-09-26) / Aivis-Project/AivisSpeech-Engine(★181,LGPL-3.0,push 2026-09-18) / RVC-Boss/GPT-SoVITS(★62,221,MIT,push 2026-08-18)
  - 新規品質はAratako/Irodori-TTS(★1363、MIT)、API連携はVOICEVOX/AivisSpeech互換。ライセンスNOASSERTIONが多く音声品質は未聴。

- **アニメ制作向けエージェント・スキル・MCP**: Comfy-Org/comfy-mcp(★246,NOASSERTION,push 2026-10-01) / Comfy-Org/comfy-skills(★213,MIT,push 2026-09-16) / Moeblack/ComfyUI-AnimaTool(★137,AGPL-3.0,push 2026-03-26) / yuna0x0/anilist-mcp(★89,MIT,push 2026-07-13)
  - アニメ特化の突出repoは無く、公式Comfy-Org/comfy-mcp(★242)とcomfy-skills(★213)が現実解。信頼度は低く、comfy-mcpは要ライセンス確認。

- **アニメ生成の評価・ベンチマーク**: RimoChan/stable-diffusion-anime-tag-benchmark(★53,未表示,push 2026-09-29) / deepghs/sdeval(★27,Apache-2.0,push 2024-08-24)
  - 定評あるベンチは無く、最有力でもRimoChan/stable-diffusion-anime-tag-benchmark(★53、ライセンス無し)。sdevalは停滞、信頼度は低い。

- **アニメ/漫画データセット・アノテーションツール**: cvat-ai/cvat(★16,844,MIT,push 2026-10-01) / HumanSignal/label-studio(★28,389,Apache-2.0,push 2026-10-01) / manga109/public-annotations(★14,CC-BY-4.0,push 2025-04-23) / manga109/manga109api(★132,MIT,push 2022-03-04)
  - アニメ特化の有力ツールは無く、汎用のcvat-ai/cvat(★16827、MIT)かlabel-studio(★28383)を流用。Manga109の利用条件は未確認。

- **同人・漫画・画像アセット管理と閲覧**: gotson/komga(★6,705,MIT,push 2026-10-01) / hydrusnetwork/hydrus(★3,220,NOASSERTION,push 2026-09-30) / kha-white/mokuro(★1,738,GPL-3.0,push 2026-07-20) / monbooru/monbooru(★84,AGPL-3.0,push 2026-09-28)
  - 蔵書はgotson/komga(★6703、MIT)、タグ管理はhydrus(★3218)、OCR閲覧はmokuro。同人専用の有力repoは無く、hydrusはライセンス要確認。

- **アニメ制作(作画・中割り・彩色・2D制作ツール)**: opentoonz/opentoonz(★7,773,NOASSERTION,push 2026-10-01) / KDE/krita(★10,463,GPL-3.0,push 2026-10-01) / Acly/krita-ai-diffusion(★10,661,GPL-3.0,push 2026-09-27) / zhuang2002/Cobra(★253,Apache-2.0,push 2026-08-15)
  - 制作環境はopentoonz(★7775)とKrita+krita-ai-diffusion(★10655)。AI彩色・中割りは研究段階で、ToonCrafter等は停滞、信頼度は低い。

- **絵コンテ・AI短編ドラマ制作パイプライン**: Forget-C/Jellyfish(★6,585,Apache-2.0,push 2026-07-30) / ArcReel/ArcReel(★5,261,AGPL-3.0,push 2026-10-01) / wonderunit/storyboarder(★3,862,未表示,push 2024-03-17)
  - Forget-C/Jellyfish(★6529、Apache-2.0)が暫定首位だが汎用の短編動画用。ArcReel等は販促色があり、客観的実績は未確認で信頼度は低い。

- **漫画の植字・フォント・テキスト描画**: koharu-rs/koharu(★5,702,Apache-2.0,push 2026-10-01) / dmMaze/BallonsTranslator(★5,173,GPL-3.0,push 2026-10-01) / komiq-cc/manga-typesetter(★13,MIT,push 2026-09-11)
  - 専用の有力repoは無く、植字はkoharu(★5693)とBallonsTranslatorの内蔵機能で足りる。manga-typesetter(★13)は実績皆無で信頼度は低い。
