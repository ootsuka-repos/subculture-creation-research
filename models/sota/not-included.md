# 検討したが選ばなかったもの（2026-10-01）

[一覧へ](../anime-task-sota.md)

最良に選ばなかった理由の記録。成人向け専用モデル、ライセンス・由来が不明なもの、停滞、用途違いなど。

## 画像生成・画像変換

| 対象 | 理由 |
| --- | --- |
| `Noctaluna/Noct-Q-Anime-Uncensored-Qwen-Image-2.1` | Qwen-Image-2.1基盤のアニメ・無検閲(成人向け)特化T2I。2026-09-28公開で30日6,195DL、X(2026-09-29, 284 likes ほか)で急拡散。成人向け特化のためbestから除外。同種派生(0xSojalSec/Anime-Uncensored-Qwen-Image-2.1)も同様。 |
| `ShinoharaHare/Waifu-Inpaint-XL` | アニメ特化SDXLインペイント(52 likes, 累計11,670DL)。基盤がWAI-NSFW-illustrious-SDXL-V14(NSFW寄りマージ)のため、汎用ベストとしては見送り。創作的インペイントの代替として人間判断に委ねる。 |
| `John6666/janku-v5-nsfw-trained-noobai-rou-wei-illustrious-xl-v50-sdxl` | NoobAI/Illustrious系NSFW学習マージのSDXL(30日89,292DL)。成人向け特化のため除外(SDXL系の採用量を示す参考)。 |
| `duongve/NetaYume-Lumina-Image-2.0` | Lumina-Image-2.0系のアニメ特化T2I。累計680,638DL/Apache-2.0表記だが最終更新2025-12-09、30日19,698DLでAnimaに置換が進行。商用ライセンス重視の代替候補として要確認(基盤Neta-Luminaの条件は未確認)。 |
| `NewBie-AI/NewBie-image-Exp0.1` | Next-DiT 3.5Bアニメ特化T2I(2025-11)。300 likesだが30日255DL/累計3,186で採用が極小、ライセンスnewbie-nc-1.0(非商用)。 |
| `cagliostrolab/animagine-xl-4.0` | SDXL系で累計3,595,591DL(30日366,672)。最終更新2025-02で世代が古い。Animaとの直接比較は未確認。SDXL資産を使う場合の既存標準。 |
| `lylogummy/Anima-3.8B` | Anima層拡張の別派生(117 likes)だがDL計測0・作者非公式・定量ベンチなし。Forge Neo READMEは3.8Bにも対応と記載。 |
| `KBlueLeaf/HDM-xut-340M-anime` | 340M小型アニメ生成(139 likes, 30日917DL, 2025-08)。研究寄りで評価データ未確認、採用も小さい。 |

## 動画

| 対象 | 理由 |
| --- | --- |
| `Muapi/ltx-2.3-2d-nsfw-motion-enhancer` | text-to-videoで「2d/anime」検索の上位(30日DL 786)だが、NSFW動作強化専用のLTX-2.3 LoRAのため best から除外。人間が判断する場合のみ検討。 |
| `kabachuha/ltx2-big-anime-breasts` | image-to-videoで「anime」検索の上位(likes 8、30日DL 22)だが、成人向け特化のLTX-2 LoRAのため除外。 |
| `Muapi/ltx-2.3-blowjob-animation-i2v` | 成人向け特化のLTX-2.3 I2V LoRA(30日DL 469)。アニメ検索で上位に出るが best 対象外。 |
| `UnifiedHorusRA/WAN_2.2_Anime_Cumshot_Aesthetics_Precision_Load_I2V_Beta_version` | Wan2.2向けの成人向けアニメ特化LoRA。best 対象外。 |
| `TenStrip/LTX2.3-10Eros` | LTX-2.3系の成人向け/無検閲派生(likes 580)。アニメ特化でも成人特化でもあり best 対象外。LTX系でlikesが高いが用途が成人向け中心のため除外。 |
| `Baberg/ltx-2.5-22b-ic-lora-cel-character` | 実写→2Dセルアニメ人物(中心キャラのみ)のLTX-2.5 IC-LoRA(video-to-video)。累計DL 43・likes 5と採用実績が乏しく、日本アニメ特化とは言えず(合成20ペアで学習)、ライセンスは「other」で名称なし(Discussion #1が明確化を質問)。video-to-video の実写→アニメ調変換枠の候補として保留。 |
| `lovis93/studio-1939-old-animation-lora-minimax-h3` | 1930年代風の西洋旧アニメ調のH3 LoRA(likes 74)。日本アニメ向けではないため除外。 |
| `TencentARC/AnimeGamer` | アニメ世界のゲームプレイ動画生成(累計295DL、独自ライセンス animegamer-lisence)。汎用T2V/I2Vではないため除外。 |
| `KBlueLeaf/TTVidT` | video-classificationタグの新着(2026-09-30)だが動き特化の自己教師エンコーダで、アニメ向けの検証なし。 |
| `Muapi/* の各種アニメLoRA(例: Muapi/anime-style-ltx-2, Muapi/anime-style-lora-m3-wan2.1-t2v-14b)` | Civitai等からの再アップロード集約リポジトリ。30日DLは数十程度で出所・ライセンス確認が困難なため除外。 |

## 音声

| 対象 | 理由 |
| --- | --- |
| `swdq/galgame-oral-tts` | GalGameの口淫シーン音声のみのコーパスでIrodori-TTS v4.1-SmallとDACVAEをfine-tuneした成人向け特化モデル(カード記載)。likes 0、DL 0。方針によりbestにしない。 |
| `swdq/Visual-novel-whisper` | kotoba-whisper-v1.1を「アダルト用語を認識できるように」再学習したASR(カード記載、likes 19、DL累計419)。成人向け語彙への特化が目的のため除外。anime-whisperが汎用のアニメ調ASRとして上位。 |
| `NandemoGHS/Galgame-Orpheus-3B` | ガルゲ音声で学習したOrpheus系TTS(2025-08、likes 4、DL累計146、カードなし・ライセンス未設定)。後継のAnime-Llasa-3B系に対して採用・情報とも劣る。学習データにR18ゲーム音声を含む(同作者のJapanese-Eroge-Voiceデータセット名から示唆)。 |
| `OmniAICreator/Galgame-Llasa-3B-v3` | Anime-Llasa-3Bの旧版(CC-BY-NC、DL累計393)。Anime-Llasa-3B(33,000時間)に置き換え済み。 |
| `NandemoGHS/Anime-Llasa-3B` | 最有力の対抗だがbestにしない: CC-BY-NC(商用不可)、採用指標が低く(DL 30日335/累計24,301、likes 30)、多音字誤読報告あり、学習データの権利処理に懸念の投稿。アニメ特化の大規模学習(33,000時間)は評価できるため、商用・権利が問題にならない研究用途の代替としてrunner-up記載。 |
| `m-a-p/YuE2-3B` | 楽曲生成でCC-BY-NC-4.0のためbest不採用(runner-up記載)。日本語ボーカル対応の報道あり。人間が商用要否で判断すること。 |
| `litagin/anime_speech_emotion_classification` | bestに採用したが、Sexual1/Sexual2(喘ぎ・口淫SE)クラスを含む。成人向け特化ではなく汎用10クラス感情分類のため採用、人間確認用に注記。 |
| `ryanontheinside/j_pop-acestep1.5-xl-v1` | ACE-Step 1.5 XL用J-Pop LoRA(プロンプトに"anime-style melody"を含む)。DL累計149、likes 0、ライセンス未設定で採用実績なし。アニメソング特化の唯一の候補だが推奨しない。 |
| `NandemoGHS/Anime-Speech-Japanese-Refiner` | Captionerと同系統の音声+書き起こし→修正書き起こし/記述モデル(CC-BY-NC、likes 12)。出力例が性的内容を含みうる点もCaptionerと同じ。キャプション用途ではCaptionerで足りるためrunner-up扱い。 |

## 画像認識（検出・分割・分類・特徴）

| 対象 | 理由 |
| --- | --- |
| `deepghs/anime_censor_detection` | アニメ画像の検閲(モザイク)対象部位検出で、成人向け用途に特化(likes14、MIT)。成人向け専用モデルのためbestにしない。人間が判断する場合の候補としてのみ記録 |
| `Anzhc/Anzhcs_YOLOs` | 30日DL78,985・likes184でADetailer系アニメ用途に広く使われる顔/目/頭髪セグメンテーション集。ただし同一repoに胸部セグメンテーション/サイズ分類など成人向けモデルを含む混在repo、顔モデルは『illustration+real』でアニメ特化ではなく、学習データ非公開(約500〜1,030枚)、ベンチはmAP50 0.835(box)/mAP50-95 0.537(v4、自己報告)。bestにしない |
| `Bingsu/adetailer` | ADetailerの標準重み(HF DL累計352M、30日9.9M、likes794、Apache-2.0)。ただし『2D/realistic』混在でWIDER FACE・COCO・DeepFashion2を含みアニメ特化ではない。顔検出でアニメ特化のdeepghsを選び、こちらは汎用の実務標準として併記 |
| `cella110n/cl_tagger_v2` | X(2026-09-27 Explorer_EX99)で『cl-tagger-v2の検出力は凄い、導入難易度は高い』との投稿。SigLIP2 so400mベースのONNX、likes30、gated auto、独自ライセンス(cl-tagger-v2-model-license-v1.0)でカード本文が取得できず(HTTP 403)、性能・条件を確認できないため選定不可 |
| `animetimm/caformer_b36.dbv4-full` | AnimeTIMM(dbv4、12,476タグ)系のタガー群(EVA02/ConvNeXtV2/SigLIP Giant等)。PixAIカードの比較表ではGeneral micro F1 0.6362〜0.6435、Character micro F1 0.9069〜0.9265と上位(自己報告)。GPL-3.0・gated auto・HFカード取得403で条件を確認できず、PixAI v1.0より下位と報告されるため不採用 |
| `Camais03/camie-tagger-v2` | 70,527タグ・GPL-3.0・自己テスト20,116枚でmicro F1 0.673。PixAIカードの共有タグ比較ではGeneral micro F1 0.5775で8モデル中最下位(自己報告)。語彙の広さ(アーティスト・年タグ)は独自の利点 |
| `Zarxrax/BiRefNet-Real_Anime` | BiRefNet_lite微調整(MIT)、アニメ映像スクショ向けと記載。2026-09-22公開でDL0・likes0・ベンチなし。実アニメ映像フレームの背景除去用途の新顔として要追跡 |
| `Civitai/Age-Classification-SigLIP2-anime-finetune` | アニメキャラの年齢区分分類(SigLIP2微調整、2026-03-13、30日DL262)。安全/年齢確認系でカードを精査しておらず、用途が未成年判定に関わるため選定対象外(未評価) |
| `deepghs/idolsankaku-eva02-large-tagger-v1` | アイドル(実写)画像用タガー。アニメ対象外のため対象外 |
| `ogkalu/comic-text-and-bubble-detector` | 漫画の吹き出し/文字検出はmanga側スライス(SotaManga)で扱うため本スライスでは評価しない(object-detection/image-segmentationの漫画用途は重複させない) |

## マンガ・OCR・文書

| 対象 | 理由 |
| --- | --- |
| `Kellenok/PP-OCRv6_manga` | 検出0.9MB+認識10MBの軽量CPU漫画OCRパイプライン(Apache-2.0、v0.2=2026-09-28)。842ページ end-to-end CER 11.34%、漫画/webtoon/イラスト切り抜きCER 5.72%(総合、自己報告)で、Hayai Nova より webtoon/希少漢字に強い。しかし作成2026-09-02、30日DL0・likes1、第三者検証なし。エッジ/CPU用途の有力候補として記録。 |
| `muscgab/manga-ocr-nar-preview` | JMangaBench作者の非自己回帰OCRプレビュー(2026-09-14)。Manga109-s v2026の実クロップ123,212枚で exact 75.03%・micro-CER 4.79%(Baberu 72.48%/4.94%、自己報告、Manga109-sは学習に未使用と明記)。ただしDL23・likes1、Hayai/manga-ocrとの比較なし、重みは CC BY-NC-SA 4.0。 |
| `JustANormalTinkerer/hayai-ocr-v2` | Koharuが同梱しているHayai版(DL累計7,920、likes8)。カード冒頭に『outdated、Novaへ移行』と記載されるため、同一作者の Nova を採用。 |
| `sorryhyun/paddleocr-vl-1.6-manga-lora` | PaddleOCR-VL-1.6 の漫画SFX/台詞LoRA+視覚タワー(Apache-2.0、2026-09)。COO SFX exact 83.9%(自己報告)だがDL473・likes0。SFXの専用候補として onomatopoeia-ocr の次点に記録。 |
| `jzhang533/PaddleOCR-VL-For-Manga` | likes136・BallonsTranslator対応のManga109-sファインチューン版。JMangaBench CER 2.91%だがManga109-s学習のため同ベンチで漏洩リスク。dialogue-ocr の次点に記録。 |
| `mayocream/koharu-text-sam-ts-l` | Hi-SAM派生のテキスト画素マスク分割(Apache-2.0表記)。テスト40ページ(未知4冊)で HR IoU 0.6285(元TextSeg 0.3461)、自己報告。30日DL81。学習に Manga109 画像(Zenodoマスク+認可画像)を使用。消去用マスクの精緻化に有用だがDL・採用が乏しく独立エントリは見送り。 |
| `monkeyslikebananas/Qwen3-VL-8B-NSFW-Caption-V4.5` | 成人向け画像のキャプション専用モデル群(同名の mradermacher/Qwen3-VL-8B-NSFW-Caption-V4.5-GGUF は30日DL13,540、bartowski/thesby_Qwen2.5-VL-7B-NSFW-Caption-V3-GGUF は9,971)。『キャプション』検索の派生DLで上位だが、成人向け特化のため best 対象外。人間判断用に記録。 |
| `prithivMLmods/Qwen3-VL-8B-Abliterated-Caption-it 系` | 汎用VLMのabliterated(安全機構除去)キャプション派生。アニメ特化の根拠なし。 |
| `TencentARC/AnimeGamer` | アニメ世界シミュレーション(pipeline_tag=text-to-video、license other、likes46、30日DL27)。any-to-anyではなく動画スライスの範囲。 |
| `YSGforMTL/YSGYoloDetector` | 日本語漫画/CG内の擬音を除外して検出する検出器(MIT、BallonsTranslatorがDL案内)。HF DLカウンタ0・likes20、ベンチなしで比較不能。 |

## 言語（翻訳・生成・埋め込み）

| 対象 | 理由 |
| --- | --- |
| `Elizezen/Berghof-NSFW-7B` | 日本語小説/ERP特化の7B(NSFW/ERP向けとして公開)。成人向け専用のため日本語シナリオ生成のbestから除外。人間判断用に記録 |
| `Elizezen/Berghof-ERP-7B` | 日本語ERP特化。成人向け専用のため除外 |
| `Local-Novel-LLM-project/Ninja-v1-NSFW-GGUF` | 日本語小説生成のNSFW特化系統(Ninja-v1)。成人向け専用のため除外 |
| `mradermacher/Qwen3.8-27B-Heretic-JP-Roleplay-NSFW-DanbooruTags-i1-GGUF` | 2026-09公開でJPロールプレイ＋Danbooruタグ出力を謳うが、名称上NSFW/検閲解除(Heretic)特化の派生・量子化。30日6,694DLで成人向け専用のため除外 |
| `Aratako/Qwen3-8B-ERP-v0.1` | ERP専用の日本語ロールプレイ微調整(30日438DL)。成人向け専用のため除外 |
| `SakuraLLM/Sakura-14B-Qwen2.5-v1.0-GGUF` | ラノベ/漫画/Galgame汎用のJA→ZH翻訳14B(累計389,138DL、likes 95)。VN特化のGalTransl系を優先したため非採用だが、ラノベ・漫画用途ではこちらが正式v1.0版。CC-BY-NC-SA 4.0 |
| `Oxygavz/Manga-Translator-9B` | 漫画翻訳を名乗るQwen3系9B(2026-04公開)だが累計62DL・カード/ベンチ未確認で実績なし |
| `mradermacher/Deepseek-Light-Novel-Translator-1-i1-GGUF` | ラノベ翻訳GGUF(30日1,177DL)。元モデル・評価が不明で採用根拠が弱い |
| `kujirahand/anime_llm_qwen3_14b` | アニメ知識LLMを名乗るが累計18DL・ライセンス/評価未記載 |
| `Lorg0n/hikka-forge2vec` | アニメ/マンガ作品メタデータの専用埋め込み(Apache-2.0)。2026-09-05公開・累計112DLで未実績。今後の監視対象 |

## 3D・アバター・その他

| 対象 | 理由 |
| --- | --- |
| `VAST-AI/AniGen` | リグ付き3D一括生成(TRELLIS-image-large派生、MIT表記、2026-04)。汎用アセット向けでアニメ専用ではなく、GitHubライセンスはNOASSERTION。HF DL 0・likes 15。image-to-3dの次点として記載 |
| `tencent/HY-Motion-1.0` | text-to-3dのHFタグで最有力の汎用モーションモデル(likes 441)。ライセンスがEU・英国・韓国を対象外、月間1M MAU超は別契約のため次点 |
| `Hydrilla/BlueFox3D-character-shape512` | 2026-09公開のキャラ向けimage-to-3d。ただしObjaverse-LVISの149メッシュで1000ステップ微調整しただけ(カード自身が『新製品モデルではない』と記載)、likes 1、アニメ学習ではない |
| `LordLiang/DrawingSpinUp` | キャラクター素描→3Dアニメ(SIGGRAPH Asia 2024、★658、GitHubライセンス未設定)。対象は手描きキャラの単一画像で、HFはcamenduruの再配布(likes 0、DL 0)のみ。アニメ専用評価・リギング標準ではなく収録外 |
| `Tripo / Meshy / Hi3D(クローズドサービス)` | 日本語圏のX実務報告(2026-07〜09、4,349/816/631/611 likes等)ではアニメキャラ→3Dはこれらのサービスが多数派。重みが非公開のため対象外(Genshiというローカル/自動Live2Dメッシュ化ツールもXで言及されるが公開リポジトリ・重みは確認できず、未検証のリード) |
| `Wan-AI/Wan-Dancer-14B` | ダンス動画生成(image-to-video、likes 187)。動画生成スライスの管轄でありスケルトンモーションではないため本スライスでは対象外 |

## 制作工程別リポジトリ全体像

| 対象 | 理由 |
| --- | --- |
| `Anime4K (bloc97/Anime4K)` | ★21448(MIT)でmpv等のシェーダ標準だが最終push 2024-08-17でリリースも2021-09。停滞のためbestにせず、利用は許容。 |
| `nagadomi/waifu2x, xinntao/Real-ESRGAN, nihui/realcugan-ncnn-vulkan` | 最終push 2023-05/2024-08/2023-03でメンテ停止。モデル資産としてVideo2X等が内包。 |
| `deepghs/waifuc` | ★409(MIT)の収集→加工パイプラインだが最終push 2024-08-24で停滞。imgutilsとgallery-dlで代替。 |
| `jhc13/taggui` | ★1351(GPL-3.0)。最終push 2025-10-11で12か月手前、BooruDatasetTagManagerを優先。 |
| `perfectgf/lora-dataset-studio` | ★283、2026-09-29更新だが新しく、作者自身の宣伝文言があり実績不足。 |
| `Artikash/Textractor` | ★2698だが最終push 2024-03-15で停滞、LunaTranslatorが内蔵フックで代替。 |
| `litagin02/Style-Bert-VITS2` | catalog収録(style-bert-vits2)。★1378、AGPL-3.0、最終リリース2025-08、push 2025-12-07で更新停滞。 |
| `artokun/comfyui-mcp` | ★774だがREADMEがメンテ終了・2026-10-09アーカイブ予定と明記。公式comfy-mcpへ。 |
| `Kareadita/Kavita` | ★11784(GPL-3.0)、Komgaと同格の漫画サーバ。枠の都合で除外、好みで選択可。 |
| `dramaclaw/dramaclaw, waooAI/waoowaoo` | ★6612/★14338と大きいがライセンスNOASSERTION・READMEが販促/思想色で実績の客観根拠なし。 |
| `Inochi2D/inochi-creator` | catalog収録。最終push 2025-06-16で停滞(SDKのinochi2dは2026-09-15まで更新)。 |
| `ltdrdata/ComfyUI-Manager` | ★16316だがアニメ特化でないためComfyUI枠の対象外。導入には事実上必須。 |
| `ToonCrafter/ToonComposer/BasicPBC(中割り・彩色)` | 最終push 2025-03/2025-08/2025-06で停滞、ライセンス条件は個別確認。研究参照にとどめる。 |
| `lllyasviel/Fooocus, AUTOMATIC1111/stable-diffusion-webui, lllyasviel/stable-diffusion-webui-forge` | 最終push 2025-12/2026-03/2025-07。後継Haoming02/sd-webui-forge-classic(★1772、READMEにAnima対応明記)のほうが活発。 |
