# サブカルコンテンツ制作リポジトリ一覧

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

## 漫画・イラスト編集

[分野別詳細](categories/manga.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ai-comic-factory](https://github.com/jbilcke-hf/ai-comic-factory) | LLMと画像生成を連携してコマを作るAI漫画アプリの参考実装。 | AI連携 / 旧版・履歴資料 | 1,345 / 2025-10-30 |
| [krita](https://github.com/KDE/krita) | 漫画・イラスト制作に使うデジタルペイントアプリ。 | 非AI制作 / 定番の制作基盤 | 10,341 / 2026-09-09 |
| [manga-editor-desu](https://github.com/new-sankaku/manga-editor-desu) | ブラウザでコマ割り、吹き出し、縦書き、レイヤー編集とAI生成連携を行う。 | AIは任意 / 更新のある導入・評価候補 | 384 / 2026-08-30 |
| [OpenKoma](https://github.com/Reuben-Sun/OpenKoma) | 手持ち画像をコマに配置し、複数ページの漫画に組み立てる編集ツール。 | 非AI制作 / 小規模・初期評価候補 | 12 / 2026-05-08 |

## シナリオ・キャラクター・絵コンテ

[分野別詳細](categories/story.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [BlueFish](https://github.com/bluefish2026/BlueFish) | 複数のAIプロバイダを接続し、脚本から絵コンテ・動画制作まで管理する。 | AI連携 / 小規模・初期評価候補 | 8 / 2026-04-22 |
| [SillyTavern](https://github.com/SillyTavern/SillyTavern) | キャラ設定とLorebookを使い、LLMとの対話や世界観の試作を行うフロントエンド。 | AI連携 / 更新のある導入・評価候補 | 33,188 / 2026-09-07 |

## ゲーム・ノベル・スプライト

[分野別詳細](categories/game.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Godot](https://github.com/godotengine/godot) | 2D/3Dゲーム制作と複数プラットフォームへの出力を行うゲームエンジン。 | 非AI制作 / 定番の制作基盤 | 116,882 / 2026-09-08 |
| [Pixelorama](https://github.com/Orama-Interactive/Pixelorama) | ドット絵・タイル・アニメーションを編集する制作アプリ。 | 非AI制作 / 定番の制作基盤 | 10,272 / 2026-09-09 |
| [PNGAL](https://github.com/1mm-module/PNGAL) | 顔差分生成・PSD分解・目パチと口パクの補間を組み合わせ、立ち絵アニメ素材を制作する。 | AI連携 / 導入経路の追加確認が必要 | 340 / 2026-09-01 |
| [RenPy](https://github.com/renpy/renpy) | テキストとキャラクター素材を組み合わせたノベルゲームを制作する。 | 非AI制作 / 定番の制作基盤 | 6,805 / 2026-09-08 |
| [sprite-maker](https://github.com/JohnKinyanjui/sprite-maker) | AIエージェントと連携して素材を作り、関節・ボーンとRust描画で再現可能なアニメーションを生成する。 | AI連携 / 初期評価候補 | 347 / 2026-08-19 |

## アニメ制作・中割り・彩色・リップシンク

[分野別詳細](categories/animation.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ECCV2022-RIFE](https://github.com/hzwer/ECCV2022-RIFE) | フレーム間の中間画像を推定する動画補間モデル。 | AIモデル・学習 / 比較・既存工程の参考 | 5,574 / 2025-09-10 |
| [LatentSync](https://github.com/bytedance/LatentSync) | 音声条件で口の動きを同期させる動画処理モデル。 | AIモデル・学習 / 比較・既存工程の参考 | 6,059 / 2025-06-20 |
| [opentoonz](https://github.com/opentoonz/opentoonz) | 作画、彩色、撮影を扱う2Dアニメ制作アプリ。 | 非AI制作 / 定番の制作基盤 | 7,691 / 2026-09-09 |
| [ToonComposer](https://github.com/TencentARC/ToonComposer) | キーフレーム後の中割りと彩色を生成AIでまとめて処理する。 | AIモデル・学習 / 研究・技術評価候補 | 585 / 2025-08-20 |

## 2Dキャラクター・自動リギング

[分野別詳細](categories/rig2d.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Anime2.5DRig](https://github.com/852wa/Anime2.5DRig) | PSDからリグを自動構成し、目パチ・口パク・髪物理・顔追跡で動かす。 | AIは任意 / 導入候補 | 204 / 2026-09-07 |
| [PuppetLoom](https://github.com/CheshireMew/PuppetLoom) | PSDから初期リグを作成し、外部エージェントとCLIで検証・調整しながら動く2Dキャラクターを制作する。 | AI連携 / 要再確認 | 215 / 2026-09-09 |
| [stretchystudio](https://github.com/MangoLion/stretchystudio) | PSDを読み込み、自動リギングとタイムライン上のメッシュ変形でアニメーションを編集する。 | AI連携 / 導入候補 | 472 / 2026-04-28 |

## レイヤー分解

[分野別詳細](categories/layer.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ComfyUI-See-through](https://github.com/jtydhr88/ComfyUI-See-through) | See-throughによる分解をComfyUIのノード工程へ接続する。 | AI連携 / ComfyUI利用者向け | 766 / 2026-08-20 |
| [Qwen-Image-Layered](https://github.com/QwenLM/Qwen-Image-Layered) | 画像を複数の編集可能なレイヤーに分解し、個別の色・位置・サイズ変更につなげる。 | AIモデル・学習 / 基盤技術候補 | 2,093 / 2025-12-31 |
| [see-through](https://github.com/shitagaki-lab/see-through) | 一枚絵を意味別パーツへ分解し、遮蔽部分を補完してPSDに出力する。 | AIモデル・学習 / 導入候補 | 3,868 / 2026-08-05 |

## 画像生成・編集・切り抜き

[分野別詳細](categories/image.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [anime-segmentation](https://github.com/SkyTNT/anime-segmentation) | アニメ絵のキャラクター領域を抽出し、背景除去や合成用マスクを作る。 | AIモデル・学習 / 比較・既存工程の参考 | 838 / 2025-05-21 |
| [krita-ai-diffusion](https://github.com/Acly/krita-ai-diffusion) | Kritaの描画工程へ画像生成・インペイント・アウトペイントを組み込む。 | AI連携 / 更新のある導入・評価候補 | 10,564 / 2026-08-28 |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image) | テキスト描画と画像編集を扱う汎用画像モデル群。表紙・小物・宣伝画像の制作候補。 | AIモデル・学習 / 研究モデルの評価候補 | 8,294 / 2026-02-10 |
| [Z-Image](https://github.com/Tongyi-MAI/Z-Image) | 6B級の汎用画像モデル群。Turboやベースモデルを用途に合わせて利用する。 | AIモデル・学習 / 研究モデルの評価候補 | 11,999 / 2026-02-09 |

## 動画生成

[分野別詳細](categories/video.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [LTX-2](https://github.com/Lightricks/LTX-2) | 音声・動画生成とLoRA学習を扱う公式実装。READMEはLTX-2.5の導入も案内する。 | AIモデル・学習 / 更新のある導入・評価候補 | 9,380 / 2026-08-26 |
| [LTX-Video](https://github.com/Lightricks/LTX-Video) | LTXの旧世代動画生成実装。 | AIモデル・学習 / 旧版・履歴資料 | 10,941 / 2026-01-05 |
| [SCAIL-2](https://github.com/zai-org/SCAIL-2) | 参照キャラクターに動画の動きを移し、複数参照やキャラクター置換にも対応する。 | AIモデル・学習 / 研究・技術評価候補 | 1,177 / 2026-08-24 |
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) | テキストや画像から動画を作るWan2.2公式モデル群。 | AIモデル・学習 / 研究モデルの評価候補 | 17,444 / 2026-03-17 |

## 3D生成・モデリング・リギング

[分野別詳細](categories/3d.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Blender](https://github.com/blender/blender) | モデリング、リギング、アニメ、レンダリング、合成を扱う統合制作環境。 | 非AI制作 / 定番の制作基盤 | 20,204 / 2026-09-09 |
| [Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) | 画像から3D形状と材質を生成する公式実装。 | AIモデル・学習 / 比較・既存工程の参考 | 3,998 / 2025-10-17 |
| [SkinTokens](https://github.com/VAST-AI-Research/SkinTokens) | TokenRigで骨格とスキンウェイトを一つの系列として生成する自動リギング研究。 | AIモデル・学習 / 研究モデルの評価候補 | 375 / 2026-05-12 |
| [TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | 画像から形状・材質を備えた3Dアセットを生成する4Bモデル。 | AIモデル・学習 / 研究モデルの評価候補 | 11,134 / 2026-07-10 |
| [UniRig](https://github.com/VAST-AI-Research/UniRig) | 形状から骨格推定とスキニングを行う自動リギング研究。 | AIモデル・学習 / 比較・既存工程の参考 | 1,741 / 2026-06-04 |

## TTS・キャラクター音声

[分野別詳細](categories/tts.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [fish-speech](https://github.com/fishaudio/fish-speech) | Fish Audio S2系の表現豊かなTTS・音声クローンを扱う実装。 | AIモデル・学習 / 更新のある導入・評価候補 | 32,627 / 2026-09-07 |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 少量音声を使うTTSと音声クローンをWebUIから扱う。 | AIモデル・学習 / 更新のある導入・評価候補 | 61,660 / 2026-08-18 |
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | 声のデザイン、参照音声による合成、指示による話し方制御を扱う多言語TTS。 | AIモデル・学習 / 研究モデルの評価候補 | 13,328 / 2026-03-17 |
| [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) | Bert-VITS2を基に音声スタイルの制御と学習を扱う日本語TTSツール。 | AIモデル・学習 / 比較・既存工程の参考 | 1,370 / 2025-12-07 |
| [voicevox](https://github.com/VOICEVOX/voicevox) | 日本語のキャラクター音声を編集して出力するVOICEVOXのエディタ。 | AI連携 / 定番の制作基盤 | 3,236 / 2026-09-09 |

## ASMR・効果音・環境音

[分野別詳細](categories/sound.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ASMRify](https://github.com/ReactorcoreGames/ASMRify) | 音声に定位移動・残響・ピッチ等を加えて一括処理するASMR向け音声加工ツール。 | AI出力の後処理 / 小規模・初期評価候補 | 1 / 2026-06-18 |
| [FoleyCrafter](https://github.com/open-mmlab/FoleyCrafter) | 動画の内容とタイミングに合わせた効果音を生成する研究実装。 | AIモデル・学習 / 研究モデルの評価候補 | 663 / 2026-06-15 |
| [MMAudio](https://github.com/hkchengrex/MMAudio) | 動画やテキストを条件に、時間的に対応する音声を生成する。 | AIモデル・学習 / 研究モデルの評価候補 | 2,268 / 2026-02-23 |
| [stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools) | 条件付き音声生成モデルの学習と推論を行うツール群。効果音や環境音素材を検討できる。 | AIモデル・学習 / 更新のある導入・評価候補 | 3,856 / 2026-09-09 |

## 音楽・歌声合成

[分野別詳細](categories/music.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | ローカルで楽曲を生成し、編集や追加学習につなげる音楽モデル。 | AIモデル・学習 / 更新のある導入・評価候補 | 12,616 / 2026-09-03 |
| [DiffSinger](https://github.com/openvpi/DiffSinger) | 歌声合成の学習・推論と、ピッチ・エネルギー・息成分などの制御を扱う。 | AIモデル・学習 / 更新のある導入・評価候補 | 3,201 / 2026-09-07 |
| [OpenUtau](https://github.com/openutau/OpenUtau) | UTAUコミュニティ向けの歌声編集・合成プラットフォーム。 | AIは任意 / 定番の制作基盤 | 4,281 / 2026-09-09 |

## VTuber・AIキャラクター・VRM

[分野別詳細](categories/vtuber.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AIRI](https://github.com/moeru-ai/airi) | 会話するバーチャルキャラクターを構築する環境。 | AI連携 / 更新のある導入・評価候補 | 48,985 / 2026-09-09 |
| [inochi-creator](https://github.com/Inochi2D/inochi-creator) | レイヤー画像を変形させ、ゲームやVTuberで動かす2Dモデルを作るエディタ。 | 非AI制作 / 比較・既存工程の参考 | 1,217 / 2025-06-16 |
| [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | 音声会話・視覚認識・Live2D表示を組み合わせるAIキャラクター環境。 | AI連携 / 連携の評価候補 | 13,686 / 2026-05-15 |
| [UniVRM](https://github.com/vrm-c/UniVRM) | Unity用のVRM形式実装。3Dアバターの読み込み・書き出しを扱う。 | 非AI制作 / 定番の制作基盤 | 3,378 / 2026-08-20 |
| [VTubeStudio](https://github.com/DenchiSoft/VTubeStudio) | VTube Studioを外部から制御する公式API文書・開発資料。 | AI連携 / 連携用文書資料 | 1,287 / 2026-09-02 |

## 制作ワークフロー・追加学習

[分野別詳細](categories/workflow.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 画像・動画などのモデルをノードで接続して制作工程を構成する。 | AI連携 / 更新のある導入・評価候補 | 132,241 / 2026-09-09 |
| [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) | Wan系および関連動画モデルをComfyUIで使うためのラッパーノード。 | AI連携 / 連携の評価候補 | 6,687 / 2026-05-24 |
| [musubi-tuner](https://github.com/kohya-ss/musubi-tuner) | 画像・動画モデル向けのLoRA学習スクリプト群。 | AIモデル・学習 / 更新のある導入・評価候補 | 2,033 / 2026-09-08 |

## 字幕・翻訳・ローカライズ

[分野別詳細](categories/localization.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [manga-image-translator](https://github.com/zyddnys/manga-image-translator) | 画像内の文字を検出・認識・翻訳し、元の文字を修復して訳文を組版する。 | AIモデル・学習 / 比較・既存工程の参考 | 10,401 / 2026-07-20 |
| [VoiceTransl](https://github.com/shinnpuru/VoiceTransl) | 音声認識、字幕翻訳、字幕と動画の処理を組み合わせる。 | AI連携 / 連携の評価候補 | 1,271 / 2026-08-28 |
