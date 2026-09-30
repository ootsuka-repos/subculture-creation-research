# サブカルコンテンツ制作リポジトリ一覧

一覧更新日: 2026-09-30。**136件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

## 漫画・イラスト編集

[分野別詳細](categories/manga.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ai-comic-factory](https://github.com/jbilcke-hf/ai-comic-factory) | LLMと画像生成を連携してコマを作るAI漫画アプリの参考実装。 | AI連携 / 旧版・履歴資料 | 1,342 / 2025-10-30 |
| [DiffSensei](https://github.com/jianzongwu/DiffSensei) | 複数キャラ参照と配置を条件に白黒漫画のコマを生成する。 | AIモデル・学習 / モデル・研究候補 | 925 / 2025-02-05 |
| [krita](https://github.com/KDE/krita) | 漫画・イラスト制作に使うデジタルペイントアプリ。 | 非AI制作 / 定番の制作基盤 | 10,457 / 2026-09-30 |
| [manga-editor-desu](https://github.com/new-sankaku/manga-editor-desu) | ブラウザでコマ割り、吹き出し、縦書き、レイヤー編集とAI生成連携を行う。 | AIは任意 / 更新のある導入・評価候補 | 390 / 2026-08-30 |
| [MangaNinja](https://github.com/ali-vilab/MangaNinjia) | 参照画像と点対応を使い、線画のキャラクターに指定色を反映する。 | AIモデル・学習 / モデル・研究候補 | 742 / 2025-03-02 |
| [OpenKoma](https://github.com/Reuben-Sun/OpenKoma) | 手持ち画像をコマに配置し、複数ページの漫画に組み立てる編集ツール。 | 非AI制作 / 小規模・初期評価候補 | 14 / 2026-05-08 |
| [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) | キャラクターの一貫性を保つ注意機構で連続画像・漫画素材を生成する。 | AIモデル・学習 / モデル・研究候補 | 6,470 / 2024-09-26 |
| [Venera-SSR](https://github.com/Kiastr/Venera-SSR) | 複数の漫画源に対応する漫画ビューアに、ローカルの白黒漫画着色・Anime4K超解像・OCR翻訳を統合した改版リーダー。 | AIモデル・学習 / 初期評価候補 | 55 / 2026-08-02 |

## シナリオ・キャラクター・絵コンテ

[分野別詳細](categories/story.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [BlueFish](https://github.com/bluefish2026/BlueFish) | 複数のAIプロバイダを接続し、脚本から絵コンテ・動画制作まで管理する。 | AI連携 / 小規模・初期評価候補 | 8 / 2026-04-22 |
| [ink](https://github.com/inkle/ink) | 分岐する物語を書くスクリプト言語、コンパイラ、実行ランタイム。 | 非AI制作 / 制作基盤として比較 | 4,954 / 2026-05-05 |
| [SillyTavern](https://github.com/SillyTavern/SillyTavern) | キャラ設定とLorebookを使い、LLMとの対話や世界観の試作を行うフロントエンド。 | AI連携 / 更新のある導入・評価候補 | 33,971 / 2026-09-23 |
| [Yarn Spinner](https://github.com/YarnSpinnerTool/YarnSpinner) | ゲームの会話記述をコンパイル・実行する台詞制作基盤。 | 非AI制作 / 制作基盤として比較 | 2,850 / 2026-09-30 |

## ゲーム・ノベル・スプライト

[分野別詳細](categories/game.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ControlTile](https://github.com/Junrongh/ControlTile) | 条件付きの画像タイル生成を扱う研究実装。 | AIモデル・学習 / 小規模・初期候補 | 12 / 2026-07-27 |
| [Godot](https://github.com/godotengine/godot) | 2D/3Dゲーム制作と複数プラットフォームへの出力を行うゲームエンジン。 | 非AI制作 / 定番の制作基盤 | 118,011 / 2026-09-30 |
| [LDtk](https://github.com/deepnight/ldtk) | 2Dレベルを設計するオープンソースのエディタ。 | 非AI制作 / 制作基盤として比較 | 4,283 / 2026-07-12 |
| [OpenGame](https://github.com/leigest519/OpenGame) | 指示からWebゲームを制作するエージェント基盤。テンプレートとデバッグ手順を組み込む。 | AI連携 / 連携・制作ツール候補 | 2,960 / 2026-09-03 |
| [Pixelorama](https://github.com/Orama-Interactive/Pixelorama) | ドット絵・タイル・アニメーションを編集する制作アプリ。 | 非AI制作 / 定番の制作基盤 | 10,431 / 2026-09-30 |
| [PNGAL](https://github.com/1mm-module/PNGAL) | 顔差分生成・PSD分解・目パチと口パクの補間を組み合わせ、立ち絵アニメ素材を制作する。 | AI連携 / 導入経路の追加確認が必要 | 350 / 2026-09-01 |
| [RenPy](https://github.com/renpy/renpy) | テキストとキャラクター素材を組み合わせたノベルゲームを制作する。 | 非AI制作 / 定番の制作基盤 | 6,876 / 2026-09-30 |
| [sprite-maker](https://github.com/JohnKinyanjui/sprite-maker) | AIエージェントと連携して素材を作り、関節・ボーンとRust描画で再現可能なアニメーションを生成する。 | AI連携 / 初期評価候補 | 414 / 2026-09-24 |
| [Terrain Diffusion](https://github.com/xandergos/terrain-diffusion) | 広域地形を拡散モデルで生成し、地図から地形への変換も扱う。 | AIモデル・学習 / モデル・研究候補 | 1,410 / 2026-08-12 |
| [Tiled](https://github.com/mapeditor/tiled) | タイルとオブジェクトを配置して2Dゲームのマップを作る。 | 非AI制作 / 制作基盤として比較 | 12,932 / 2026-09-25 |

## アニメ制作・中割り・彩色・リップシンク

[分野別詳細](categories/animation.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AniDoc](https://github.com/robbyant-research/AniDoc) | 設定画を参照してスケッチ列を彩色するアニメ制作研究。 | AIモデル・学習 / モデル・研究候補 | 572 / 2025-04-15 |
| [AnimeColor](https://github.com/IamCreateAI/AnimeColor) | 設定画参照とスケッチ動画からアニメを彩色する拡散Transformer。 | AIモデル・学習 / 小規模・初期候補 | 9 / 2025-08-04 |
| [BasicPBC](https://github.com/ykdai/BasicPBC) | 閉領域の対応付けによってアニメ線画の塗りを支援するペイントバケット彩色。 | AIモデル・学習 / モデル・研究候補 | 307 / 2025-06-26 |
| [ECCV2022-RIFE](https://github.com/hzwer/ECCV2022-RIFE) | フレーム間の中間画像を推定する動画補間モデル。 | AIモデル・学習 / 比較・既存工程の参考 | 5,596 / 2025-09-10 |
| [LatentSync](https://github.com/bytedance/LatentSync) | 音声条件で口の動きを同期させる動画処理モデル。 | AIモデル・学習 / 比較・既存工程の参考 | 6,103 / 2025-06-20 |
| [opentoonz](https://github.com/opentoonz/opentoonz) | 作画、彩色、撮影を扱う2Dアニメ制作アプリ。 | 非AI制作 / 定番の制作基盤 | 7,775 / 2026-09-27 |
| [ToonComposer](https://github.com/TencentARC/ToonComposer) | キーフレーム後の中割りと彩色を生成AIでまとめて処理する。 | AIモデル・学習 / 研究・技術評価候補 | 586 / 2025-08-20 |
| [ToonCrafter](https://github.com/Doubiiu/ToonCrafter) | 二枚のアニメ画像の間を生成する補間モデル。 | AIモデル・学習 / モデル・研究候補 | 6,030 / 2025-03-19 |

## 2Dキャラクター・自動リギング

[分野別詳細](categories/rig2d.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Anime2.5DRig](https://github.com/852wa/Anime2.5DRig) | PSDからリグを自動構成し、目パチ・口パク・髪物理・顔追跡で動かす。 | AIは任意 / 導入候補 | 231 / 2026-09-23 |
| [PuppetLoom](https://github.com/CheshireMew/PuppetLoom) | レイヤーPSDを自動バインドし、改訂履歴・検証を残して動く2Dキャラを制作する。 | AI連携 / 要再確認 | 241 / 2026-09-28 |
| [stretchystudio](https://github.com/MangoLion/stretchystudio) | PSDを読み込み、自動リギングとタイムライン上のメッシュ変形でアニメーションを編集する。 | AI連携 / 導入候補 | 494 / 2026-04-28 |
| [psd2live](https://github.com/tsunehimatoi/psd2live) | レイヤー分けしたPSDからLive2Dモデルを自動生成し、同じ作業画面で修形・リギング・物理・アニメーション・書き出しまで行うデスクトップツール。 | AIは任意 / 活発・候補 | 514 / 2026-09-30 |

## レイヤー分解

[分野別詳細](categories/layer.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ComfyUI-See-through](https://github.com/jtydhr88/ComfyUI-See-through) | See-throughによる分解をComfyUIのノード工程へ接続する。 | AI連携 / ComfyUI利用者向け | 814 / 2026-08-20 |
| [Qwen-Image-Layered](https://github.com/QwenLM/Qwen-Image-Layered) | 画像を複数の編集可能なレイヤーに分解し、個別の色・位置・サイズ変更につなげる。 | AIモデル・学習 / 基盤技術候補 | 2,122 / 2025-12-31 |
| [see-through](https://github.com/shitagaki-lab/see-through) | 一枚絵を意味別パーツへ分解し、遮蔽部分を補完してPSDに出力する。 | AIモデル・学習 / 導入候補 | 4,192 / 2026-09-24 |
| [Stable Layers](https://github.com/Stability-AI/Stable-Layers) | Qwen-Image-Layered上のLoRAで、画像を背景と物体の編集用RGBA層へ分解する。 | AIモデル・学習 / レイヤー分解の研究候補 | 24 / 2026-07-23 |
| [loom-unravel](https://github.com/byeolki/loom-unravel) | 1枚のアニメキャラ立ち絵を顔パーツ単位のRGBAレイヤーと、階層・深度順・アンカー点を持つメタデータに分解するオフラインパイプライン。 | AIモデル・学習 / 初期評価候補 | 0 / 2026-09-11 |

## 画像生成・編集・切り抜き

[分野別詳細](categories/image.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [anime-segmentation](https://github.com/SkyTNT/anime-segmentation) | アニメ絵のキャラクター領域を抽出し、背景除去や合成用マスクを作る。 | AIモデル・学習 / 比較・既存工程の参考 | 844 / 2025-05-21 |
| [krita-ai-diffusion](https://github.com/Acly/krita-ai-diffusion) | Kritaの描画工程へ画像生成・インペイント・アウトペイントを組み込む。 | AI連携 / 更新のある導入・評価候補 | 10,655 / 2026-09-27 |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image) | テキスト描画と画像編集を扱う汎用画像モデル群。表紙・小物・宣伝画像の制作候補。 | AIモデル・学習 / 研究モデルの評価候補 | 8,385 / 2026-02-10 |
| [Z-Image](https://github.com/Tongyi-MAI/Z-Image) | 6B級の汎用画像モデル群。Turboやベースモデルを用途に合わせて利用する。 | AIモデル・学習 / 研究モデルの評価候補 | 12,057 / 2026-02-09 |
| [ComfyUI-Forbidden-Vision](https://github.com/luxdelux7/ComfyUI-Forbidden-Vision) | アニメ調・実写の両方に対応する顔の検出・セグメンテーション・補正を行うComfyUIカスタムノード群。ADetailerやFaceDetailerの代替を狙い、独自学習モデルを同梱する。 | AIモデル・学習 / 更新中の実装候補 | 103 / 2026-07-19 |
| [ComfyUI-Ultimate-Face-Fix](https://github.com/Merserk/ComfyUI-Ultimate-Face-Fix) | 顔を検出して切り出し、接続した生成モデルでimg2img修復し、意味マスクで顔だけを元画像に合成するComfyUIノード。 | AI出力の後処理 / 活発・候補 | 25 / 2026-07-21 |
| [Colortina](https://github.com/Amster-Ilvil/Colortina) | manga-colorization-v2を基にしたローカル漫画自動彩色デスクトップツール。手動カラーヒント、区域ごとの再彩色、髪色補正、バッチ処理を備える。 | AIモデル・学習 / 小規模・初期評価候補 | 1 / 2026-08-23 |

## 動画生成

[分野別詳細](categories/video.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [FramePack](https://github.com/lllyasviel/FramePack) | 過去フレームの文脈を圧縮して動画を逐次生成する実装・デスクトップUI。 | AIモデル・学習 / モデル・研究候補 | 17,266 / 2025-10-16 |
| [Index-anisora](https://github.com/bilibili/Index-anisora) | アニメ向け動画生成。版ごとに任意フレーム、マスク制御、スタイル変換等を提供。 | AIモデル・学習 / モデル・研究候補 | 2,519 / 2026-07-16 |
| [LTX-2](https://github.com/Lightricks/LTX-2) | 音声・動画生成とLoRA学習を扱う公式実装。READMEはLTX-2.5の導入も案内する。 | AIモデル・学習 / 更新のある導入・評価候補 | 9,562 / 2026-09-30 |
| [LTX-Video](https://github.com/Lightricks/LTX-Video) | LTXの旧世代動画生成実装。 | AIモデル・学習 / 旧版・履歴資料 | 10,997 / 2026-01-05 |
| [SCAIL-2](https://github.com/zai-org/SCAIL-2) | 参照キャラクターに動画の動きを移し、複数参照やキャラクター置換にも対応する。 | AIモデル・学習 / 研究・技術評価候補 | 1,238 / 2026-08-24 |
| [Wan-Move](https://github.com/ali-vilab/Wan-Move) | 動きの軌跡を条件に動画を生成するWan系実装。 | AIモデル・学習 / モデル・研究候補 | 658 / 2026-01-05 |
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) | テキストや画像から動画を作るWan2.2公式モデル群。 | AIモデル・学習 / 研究モデルの評価候補 | 17,678 / 2026-09-21 |

## 3D生成・モデリング・リギング

[分野別詳細](categories/3d.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AniGen](https://github.com/VAST-AI-Research/AniGen) | 一枚の画像から形状・骨格・スキンウェイトを一緒に生成する。 | AIモデル・学習 / モデル・研究候補 | 507 / 2026-07-15 |
| [Blender](https://github.com/blender/blender) | モデリング、リギング、アニメ、レンダリング、合成を扱う統合制作環境。 | 非AI制作 / 定番の制作基盤 | 20,617 / 2026-09-30 |
| [Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) | 画像から3D形状と材質を生成する公式実装。 | AIモデル・学習 / 比較・既存工程の参考 | 4,099 / 2025-10-17 |
| [Pixal3D](https://github.com/TencentARC/Pixal3D) | 画像からPBR付き3Dを生成。2026年9月に多視点推論経路を追加。 | AIモデル・学習 / モデル・研究候補 | 2,387 / 2026-09-01 |
| [Puppeteer](https://github.com/Seed3D/Puppeteer) | 3Dメッシュに骨格とウェイトを付け、動画誘導でアニメーションする。 | AIモデル・学習 / モデル・研究候補 | 423 / 2025-09-19 |
| [Roblox Cube / CubePart](https://github.com/Roblox/cube) | テキストからの形状生成に加え、メッシュと部品定義から構造を持つ部品群を生成する。 | AIモデル・学習 / モデル・研究候補 | 1,260 / 2026-05-28 |
| [SkinTokens](https://github.com/VAST-AI-Research/SkinTokens) | TokenRigで骨格とスキンウェイトを一つの系列として生成する自動リギング研究。 | AIモデル・学習 / 研究モデルの評価候補 | 440 / 2026-05-12 |
| [SQuadGen](https://github.com/microsoft/SQuadGen) | 3D形状上の単純な四角形レイアウトを生成する研究。 | AIモデル・学習 / 小規模・初期候補 | 32 / 2026-08-31 |
| [TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | 画像から形状・材質を備えた3Dアセットを生成する4Bモデル。 | AIモデル・学習 / 研究モデルの評価候補 | 11,413 / 2026-07-10 |
| [UniRig](https://github.com/VAST-AI-Research/UniRig) | 形状から骨格推定とスキニングを行う自動リギング研究。 | AIモデル・学習 / 比較・既存工程の参考 | 1,781 / 2026-06-04 |
| [SekaiBlender](https://github.com/ShiJieWorld/SekaiBlender) | MMD向けに特化したBlenderブランチ。PMX/VMDのネイティブ入出力、CCD IKソルバ、Bullet物理、FSR拡大を統合する。 | 非AI制作 / 小規模・初期評価候補 | 17 / 2026-09-18 |

## TTS・キャラクター音声

[分野別詳細](categories/tts.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [CosyVoice](https://github.com/QwenAudio/CosyVoice) | ストリーミング対応の多言語音声合成。現行READMEはFun-CosyVoice3を案内。 | AIモデル・学習 / モデル・研究候補 | 23,815 / 2026-05-25 |
| [F5-TTS](https://github.com/SWivid/F5-TTS) | 参照音声とテキストを使うフローマッチング音声合成・追加学習。 | AIモデル・学習 / モデル・研究候補 | 15,316 / 2026-09-21 |
| [fish-speech](https://github.com/fishaudio/fish-speech) | Fish Audio S2系の表現豊かなTTS・音声クローンを扱う実装。 | AIモデル・学習 / 更新のある導入・評価候補 | 32,901 / 2026-09-16 |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 少量音声を使うTTSと音声クローンをWebUIから扱う。 | AIモデル・学習 / 更新のある導入・評価候補 | 62,274 / 2026-08-18 |
| [IndexTTS](https://github.com/index-tts/index-tts) | 声質・感情の条件を扱う音声合成。現行2.5は日本語を含む5言語を案内。 | AIモデル・学習 / モデル・研究候補 | 24,240 / 2026-09-29 |
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | 声のデザイン、参照音声による合成、指示による話し方制御を扱う多言語TTS。 | AIモデル・学習 / 研究モデルの評価候補 | 13,597 / 2026-03-17 |
| [RVC WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | 入力音声の発話内容を保ちながら学習した声へ変換する。 | AIモデル・学習 / モデル・研究候補 | 38,620 / 2026-08-04 |
| [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) | Bert-VITS2を基に音声スタイルの制御と学習を扱う日本語TTSツール。 | AIモデル・学習 / 比較・既存工程の参考 | 1,378 / 2025-12-07 |
| [voicevox](https://github.com/VOICEVOX/voicevox) | 日本語のキャラクター音声を編集して出力するVOICEVOXのエディタ。 | AI連携 / 定番の制作基盤 | 3,254 / 2026-09-30 |

## ASMR・効果音・環境音

[分野別詳細](categories/sound.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ASMRify](https://github.com/ReactorcoreGames/ASMRify) | 音声に定位移動・残響・ピッチ等を加えて一括処理するASMR向け音声加工ツール。 | AI出力の後処理 / 小規模・初期評価候補 | 1 / 2026-06-18 |
| [Audacity](https://github.com/audacity/audacity) | 録音とマルチトラック編集を行う音声制作アプリ。 | 非AI制作 / 制作基盤として比較 | 18,609 / 2026-09-30 |
| [Binaural Speech Synthesis](https://github.com/facebookresearch/BinauralSpeechSynthesis) | モノラル音声を空間条件に従うバイノーラル音声へ変換する研究。 | AIモデル・学習 / アーカイブ済み資料 | 190 / 2022-05-19 |
| [ControlFoley](https://github.com/xiaomi-research/controlfoley) | 動画・テキスト・参照音を条件に、効果音とそのタイミングを制御する。 | AIモデル・学習 / 小規模・初期候補 | 153 / 2026-08-28 |
| [FoleyCrafter](https://github.com/open-mmlab/FoleyCrafter) | 動画の内容とタイミングに合わせた効果音を生成する研究実装。 | AIモデル・学習 / 研究モデルの評価候補 | 665 / 2026-06-15 |
| [MMAudio](https://github.com/hkchengrex/MMAudio) | 動画やテキストを条件に、時間的に対応する音声を生成する。 | AIモデル・学習 / 研究モデルの評価候補 | 2,270 / 2026-02-23 |
| [stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools) | 条件付き音声生成モデルの学習と推論を行うツール群。効果音や環境音素材を検討できる。 | AIモデル・学習 / 更新のある導入・評価候補 | 3,871 / 2026-09-18 |
| [Steam Audio](https://github.com/ValveSoftware/steam-audio) | ゲーム空間に合わせた音の定位・伝播を扱う空間音響SDK。 | 非AI制作 / 制作基盤として比較 | 2,955 / 2026-03-25 |
| [Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui) | 音源分離モデルをGUIで使い、歌・伴奏等を分離する。 | AI連携 / 連携・制作ツール候補 | 26,449 / 2025-03-13 |

## 音楽・歌声合成

[分野別詳細](categories/music.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | ローカルで楽曲を生成し、編集や追加学習につなげる音楽モデル。 | AIモデル・学習 / 更新のある導入・評価候補 | 12,959 / 2026-09-03 |
| [Basic Pitch](https://github.com/spotify/basic-pitch) | 音声を音高ベンド付きMIDIへ変換する軽量な採譜モデル。 | AIモデル・学習 / 連携・制作ツール候補 | 5,655 / 2025-11-13 |
| [DiffSinger](https://github.com/openvpi/DiffSinger) | 歌声合成の学習・推論と、ピッチ・エネルギー・息成分などの制御を扱う。 | AIモデル・学習 / 更新のある導入・評価候補 | 3,210 / 2026-09-26 |
| [OpenUtau](https://github.com/openutau/OpenUtau) | UTAUコミュニティ向けの歌声編集・合成プラットフォーム。 | AIは任意 / 定番の制作基盤 | 4,346 / 2026-09-30 |
| [SOFA](https://github.com/qiuqiao/SOFA) | 歌声向けの強制アラインメントで歌詞・音素の時間位置を求める。 | AIモデル・学習 / モデル・研究候補 | 239 / 2026-09-02 |
| [YuE2](https://github.com/multimodal-art-projection/YuE) | 歌詞と曲調から編集可能な旋律・和音計画を作り、歌と伴奏へ展開する。 | AIモデル・学習 / モデル・研究候補 | 10,648 / 2026-09-29 |

## VTuber・AIキャラクター・VRM

[分野別詳細](categories/vtuber.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AIRI](https://github.com/moeru-ai/airi) | 会話するバーチャルキャラクターを構築する環境。 | AI連携 / 更新のある導入・評価候補 | 49,892 / 2026-09-30 |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) | Babylon.jsでMMDモデル・モーションを読み込み、物理・IK・モーフを再生する。 | 非AI制作 / 制作基盤として比較 | 256 / 2026-09-09 |
| [inochi-creator](https://github.com/Inochi2D/inochi-creator) | レイヤー画像を変形させ、ゲームやVTuberで動かす2Dモデルを作るエディタ。 | 非AI制作 / 比較・既存工程の参考 | 1,230 / 2025-06-16 |
| [OBS Studio](https://github.com/obsproject/obs-studio) | 画面・カメラ・音声を合成して録画・配信する。 | 非AI制作 / 制作基盤として比較 | 76,825 / 2026-09-30 |
| [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | 音声会話・視覚認識・Live2D表示を組み合わせるAIキャラクター環境。 | AI連携 / 連携の評価候補 | 13,963 / 2026-05-15 |
| [OpenSeeFace](https://github.com/emilianavt/OpenSeeFace) | Webカメラから顔のランドマークを推定し、アバター駆動へ渡す。 | AIモデル・学習 / 連携・制作ツール候補 | 2,080 / 2026-09-18 |
| [PersonaLive](https://github.com/GVCLab/PersonaLive) | 参照人物の画像を動作入力に従ってストリーミングでアニメーションする。 | AIモデル・学習 / モデル・研究候補 | 3,877 / 2026-08-28 |
| [three-vrm](https://github.com/pixiv/three-vrm) | three.jsでVRMアバターを読み込み表示するライブラリ。 | 非AI制作 / 制作基盤として比較 | 2,192 / 2026-09-30 |
| [UniVRM](https://github.com/vrm-c/UniVRM) | Unity用のVRM形式実装。3Dアバターの読み込み・書き出しを扱う。 | 非AI制作 / 定番の制作基盤 | 3,392 / 2026-09-25 |
| [VTubeStudio](https://github.com/DenchiSoft/VTubeStudio) | VTube Studioを外部から制御する公式API文書・開発資料。 | AI連携 / 連携用文書資料 | 1,304 / 2026-09-28 |
| [prometheus-avatar](https://github.com/myths-labs/prometheus-avatar) | LLM出力でLive2D/3Dアバターを動かすオープンソースSDK。口パク、感情表現、リアルタイム音声、TTS、VTuberモード、MCPサーバをまとめる。 | AI連携 / 小規模・初期評価候補 | 17 / 2026-09-30 |

## 制作ワークフロー・追加学習

[分野別詳細](categories/workflow.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 画像・動画などのモデルをノードで接続して制作工程を構成する。 | AI連携 / 更新のある導入・評価候補 | 135,649 / 2026-09-30 |
| [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) | Wan系および関連動画モデルをComfyUIで使うためのラッパーノード。 | AI連携 / 連携の評価候補 | 6,716 / 2026-05-24 |
| [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) | 画像・動画の生成と追加学習を複数モデルで扱う統合実装。 | AIモデル・学習 / モデル・研究候補 | 13,200 / 2026-09-30 |
| [musubi-tuner](https://github.com/kohya-ss/musubi-tuner) | 画像・動画モデル向けのLoRA学習スクリプト群。 | AIモデル・学習 / 更新のある導入・評価候補 | 2,074 / 2026-09-30 |
| [sd-scripts](https://github.com/kohya-ss/sd-scripts) | 画像生成モデルの追加学習・LoRAを扱うスクリプト群。 | AIモデル・学習 / 連携・制作ツール候補 | 7,242 / 2026-09-24 |
| [ComfyUI-Anime-Extensions](https://github.com/ootsuka-repos/ComfyUI-Anime-Extensions) | ComfyUI向けのノード集で、音声合成、画像条件付きキャラクター音声、画像解析・切り抜き、音楽生成、動画生成、漫画ページ組み、VRM処理をまとめて扱う。 | AIモデル・学習 / 初期評価候補 | 1 / 2026-09-23 |
| [comfyui-stylebook](https://github.com/EnragedAntelope/comfyui-stylebook) | ComfyUI向けの画風プリセット集。650以上のスタイルにレンダ済みプレビュー、1000以上の作家記述子、130以上のモディファイアを同梱する。 | AIは任意 / 小規模・初期評価候補 | 9 / 2026-09-28 |

## 字幕・翻訳・ローカライズ

[分野別詳細](categories/localization.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ASMR Dubber](https://github.com/EveningStudy/asmr-dubber) | 日本語・英語の音声や動画を、校正可能な字幕・中国語吹替・二言語音声へ変換する制作ツール。 | AI連携 / 小規模・制作連携候補 | 215 / 2026-09-30 |
| [Manga OCR](https://github.com/kha-white/manga-ocr) | 日本語漫画の縦書き・横書き・ルビ付き文字を認識する。 | AIモデル・学習 / モデル・研究候補 | 2,792 / 2026-07-19 |
| [manga-image-translator](https://github.com/zyddnys/manga-image-translator) | 画像内の文字を検出・認識・翻訳し、元の文字を修復して訳文を組版する。 | AIモデル・学習 / 比較・既存工程の参考 | 10,457 / 2026-09-25 |
| [mokuro](https://github.com/kha-white/mokuro) | 漫画ページの文字位置とOCR結果をまとめ、選択可能なテキストとして閲覧できる形式へ変換。 | AI連携 / 連携・制作ツール候補 | 1,738 / 2026-07-20 |
| [VoiceTransl](https://github.com/shinnpuru/VoiceTransl) | 音声認識、字幕翻訳、字幕と動画の処理を組み合わせる。 | AI連携 / 連携の評価候補 | 1,298 / 2026-08-28 |
| [xianscan-rust](https://github.com/ArbenApura/xianscan-rust) | 漫画・韓漫・国漫向けのローカル完結型翻訳スタジオ。吹き出し検出、多言語OCR、LLM翻訳、LaMaによるインペイント、組版までを単体バイナリで実行する。 | AIモデル・学習 / 更新が活発な実装候補 | 77 / 2026-09-29 |
| [BallonsTranslator-Pro](https://github.com/thomaswantstobeaskeleton/BallonsTranslator-Pro) | BallonsTranslatorを元にした漫画・コミック翻訳ツールキットで、検出・OCR・翻訳・インペイント・植字を組み替え可能なモジュール群で処理する。 | AIモデル・学習 / 活発・候補 | 96 / 2026-07-31 |
| [CarrotMangaTranslator](https://github.com/ucx0204/CarrotMangaTranslator) | 漫画原稿のOCR→翻訳→原文消去→植字・検品→出力を扱うデスクトップアプリ。局所GemmaやOpenAI互換APIで翻訳する。 | AIモデル・学習 / 活発・候補 | 76 / 2026-09-30 |
| [Kites](https://github.com/Unheat/Kites) | ブラウザ拡張として動作し、WebGPU上でOCR・インペイント・翻訳を行って漫画をその場で翻訳表示するツール。 | AIモデル・学習 / 初期評価候補 | 30 / 2026-09-26 |
| [lumina](https://github.com/lumina-tl/lumina) | 漫画・マンファ・マンファ翻訳の無料デスクトップアプリ。テキスト検出・OCR・翻訳・インペイント・組版の全工程を自動化しつつ、各結果を手で修正できる。 | AIモデル・学習 / 活発・候補 | 19 / 2026-09-22 |
| [yakuyomi-engine](https://github.com/joyeli/yakuyomi-engine) | 端末上で動く漫画翻訳エンジン。検出・OCR・文字消去をNCNNでCPU実行し、翻訳のみネットワークLLMに投げる。読み手アプリYakuyomiに組み込まれる。 | AIモデル・学習 / 活発・候補 | 7 / 2026-09-30 |
| [translate-manga-br](https://github.com/marco0antonio0/translate-manga-br) | ローカルファーストの漫画翻訳フルスタックアプリ。YOLOで吹き出し検出、PaddleOCRでOCR、翻訳、編集可能オーバーレイ付きリーダーまでを1本で提供する。 | AIモデル・学習 / 小規模・初期評価候補 | 31 / 2026-09-29 |
| [LingoVeil](https://github.com/Gerald-Ha/LingoVeil) | 漫画・コミック向けのセルフホスト翻訳ツール。画像内のテキストを検出・翻訳し、翻訳ビューで読める。ブックマークや読書進捗も保持する。 | AIモデル・学習 / 小規模・初期評価候補 | 5 / 2026-09-30 |

## モーション・身体演技

[分野別詳細](categories/motion.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ARDY](https://github.com/nv-tlabs/ardy) | テキストと運動学的制約から、対応骨格のモーションを生成する。 | AIモデル・学習 / モデル・研究候補 | 945 / 2026-07-10 |
| [EchoAvatar](https://github.com/RobinWitch/EchoAvatar) | ストリーミング音声から顔・身体の動きを生成してUnityアバターへ送る。 | AIモデル・学習 / 小規模・初期候補 | 43 / 2026-06-17 |
| [Gelina](https://github.com/TGuichoux/Gelina) | 音声とジェスチャーの生成・クローニング・音声から動作への変換を扱う。 | AIモデル・学習 / 小規模・初期候補 | 31 / 2026-04-28 |
| [HY-Motion 1.0](https://github.com/Tencent-Hunyuan/HY-Motion-1.0) | テキストから人型キャラクターの3D動作を生成する。 | AIモデル・学習 / モデル・研究候補 | 2,577 / 2026-07-18 |
| [R-DMesh](https://github.com/Tencent-Hunyuan/R-DMesh) | 静的メッシュを参照動画に沿って動く4Dメッシュ列へ変換する。 | AIモデル・学習 / 小規模・初期候補 | 62 / 2026-08-11 |
| [VRM-Spacing-Animation-Baking](https://github.com/Meringue-Rouge/VRM-Spacing-Animation-Baking) | VRM 1.0モデル向けBlenderアドオン。腕・脚・肩の間隔をMixamo風に調整し、髪やバストの物理ボーンをアニメへ焼き込み、ループ化する。 | 非AI制作 / 小規模・初期評価候補 | 10 / 2026-09-13 |

## VFX・材質・ベクター演出

[分野別詳細](categories/vfx.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Effekseer](https://github.com/effekseer/Effekseer) | ゲーム向けのパーティクル効果を編集し、ランタイムで再生する。 | 非AI制作 / 制作基盤として比較 | 1,778 / 2026-09-14 |
| [GenCompositor](https://github.com/TencentARC/GenCompositor) | 前景・背景と制御条件を用いて動画を生成合成する。 | AIモデル・学習 / 小規模・初期候補 | 157 / 2026-06-30 |
| [Material Maker](https://github.com/RodZill4/material-maker) | ノードで手続き的なテクスチャを作り、3Dモデルへのペイントも行う。 | 非AI制作 / 制作基盤として比較 | 5,956 / 2026-09-20 |
| [OmniLottie](https://github.com/OpenVGLab/OmniLottie) | テキスト・画像等から編集可能なLottieベクターアニメーションを生成する。 | AIモデル・学習 / モデル・研究候補 | 795 / 2026-04-06 |
| [VfxDB](https://github.com/VfxDB-Official/VfxDB) | OpenVDB由来の疎な3Dボリューム効果を学習・生成する。 | AIモデル・学習 / 小規模・初期候補 | 7 / 2026-08-19 |
| [VFXMaster](https://github.com/libaolu312/VFXMaster) | 効果の参照映像を条件に動的なVFX動画を生成する。 | AIモデル・学習 / 小規模・初期候補 | 67 / 2026-04-07 |
| [cHiDeScaler-Neo](https://github.com/animeojisan/cHiDeScaler-Neo) | Windowsの任意ウィンドウをリアルタイムキャプチャし、GLSL/ONNXでAI拡大とRIFE系フレーム補間をかけるポータブルアプリ。Anime4K等のシェーダ資産を利用できる。 | AIモデル・学習 / 小規模・初期評価候補 | 18 / 2026-09-28 |

## 絵コンテ・制作管理・評価

[分野別詳細](categories/production.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Kitsu](https://github.com/cgwire/kitsu) | アニメ・VFX・ゲーム制作の成果物、レビュー、進行を管理するWebアプリ。 | 非AI制作 / 制作基盤として比較 | 725 / 2026-09-30 |
| [Storyboarder](https://github.com/wonderunit/storyboarder) | 絵コンテを描き、ショットの順序と時間を試すアニマティクス制作ツール。 | 非AI制作 / 既存研究・制作の参考 | 3,860 / 2024-03-17 |
| [StyleID](https://github.com/kwanyun/StyleID) | 画風変化に強い顔の同一性特徴を計算し、比較・検索・評価に使う。 | AIモデル・学習 / 小規模・初期候補 | 34 / 2026-08-16 |
| [Nomi](https://github.com/aqm857886159/Nomi) | ローカル優先のAI動画制作スタジオ。エージェントがショット分割・キーフレーム生成・動画化・タイムライン配置を支援する。 | AIモデル・学習 / 活発・候補 | 534 / 2026-09-30 |
