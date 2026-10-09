# サブカルコンテンツ制作リポジトリ一覧

一覧更新日: 2026-10-09。**208件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

## 漫画・イラスト編集

[分野別詳細](categories/manga.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ai-comic-factory](https://github.com/jbilcke-hf/ai-comic-factory) | LLMと画像生成を連携してコマを作るAI漫画アプリの参考実装。 | AI連携 / 旧版・履歴資料 | 1,341 / 2025-10-30 |
| [DiffSensei](https://github.com/jianzongwu/DiffSensei) | 複数キャラ参照と配置を条件に白黒漫画のコマを生成する。 | AIモデル・学習 / モデル・研究候補 | 925 / 2025-02-05 |
| [krita](https://github.com/KDE/krita) | 漫画・イラスト制作に使うデジタルペイントアプリ。 | 非AI制作 / 定番の制作基盤 | 10,509 / 2026-10-09 |
| [manga-editor-desu](https://github.com/new-sankaku/manga-editor-desu) | ブラウザでコマ割り、吹き出し、縦書き、レイヤー編集とAI生成連携を行う。 | AIは任意 / 更新のある導入・評価候補 | 391 / 2026-10-08 |
| [MangaNinja](https://github.com/ali-vilab/MangaNinjia) | 参照画像と点対応を使い、線画のキャラクターに指定色を反映する。 | AIモデル・学習 / モデル・研究候補 | 742 / 2025-03-02 |
| [OpenKoma](https://github.com/Reuben-Sun/OpenKoma) | 手持ち画像をコマに配置し、複数ページの漫画に組み立てる編集ツール。 | 非AI制作 / 小規模・初期評価候補 | 14 / 2026-05-08 |
| [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) | キャラクターの一貫性を保つ注意機構で連続画像・漫画素材を生成する。 | AIモデル・学習 / モデル・研究候補 | 6,473 / 2024-09-26 |
| [Venera-SSR](https://github.com/Kiastr/Venera-SSR) | 複数の漫画源に対応する漫画ビューアに、ローカルの白黒漫画着色・Anime4K超解像・OCR翻訳を統合した改版リーダー。 | AIモデル・学習 / 初期評価候補 | 57 / 2026-08-02 |
| [Manga-AI-detector](https://github.com/nonillion-studios/Manga-AI-detector) | 漫画・マンファ・コミックページ向けに追加学習したYOLOv11インスタンスセグメンテーションモデル。コマ枠(panels)・吹き出し(bubbles)・本文テキスト(text)・効果音(SFX)の4要素を検出する。 | AIモデル・学習 / 小規模・初期評価候補 | 4 / 2026-08-17 |
| [manga-colorizer](https://github.com/Mobai0z0/manga-colorizer) | 白黒漫画（网点含む）の意味ベース自動彩色ツール。ONNXのSAM誘導ジェネレータで髪/肌/瞳/背景を配色し、Windowsデスクトップ（Tauri 2+Python）、ブラウザ、Dartエンジンで動作する。 | AIモデル・学習 / 小規模・初期評価候補 | 0 / 2026-10-09 |
| [ColorComic](https://github.com/vikast908/ColorComic) | 白黒の漫画・マンファPDFを、領域ごとに色を割り当てる「ガイド付き彩色」で手塗り風に彩色するローカルWebアプリ。Auto／参照画像／LLMの3モードを持ち、任意でテキスト専用LLMが配色を指示する。 | AIモデル・学習 / 中規模・実用候補 | 21 / 2026-07-10 |
| [manga-colorizer](https://github.com/FlamboyantEntertainment/manga-colorizer) | 白黒漫画を丸ごと（PDF/EPUB/CBZ）色付けするセルフホストWebアプリ。Docker一行で導入でき、読書中にその場で色付けするブラウザ拡張も同梱。線画を保持したまま色だけを元解像度ページへ転送する。 | AIモデル・学習 / 小規模・初期評価候補 | 6 / 2026-10-02 |
| [MangaFlow](https://github.com/coffe01-10/MangaFlow) | 小説テキストから漫画ページを作るローカル優先の単一ユーザー向けワークベンチ。原作・キャラ/衣装参照・絵コンテ・ページ候補を追跡可能な形でまとめ、AIは補助し人間が承認して進める。 | AIモデル・学習 / 小規模・初期評価候補（Windows v1.0.0-rc2） | 2 / 2026-10-05 |
| [AI-Comic-Generator](https://github.com/Dapeng960208/AI-Comic-Generator) | テキストの物語から、絵コンテ生成・キャラクター設定（三面図）・キャラ一貫性チェック・ビジュアル編集まで行うオープンソースの漫画制作ツール。Google Geminiモデルを利用し、全体をJSONで管理する。 | AIモデル・学習 / 小規模・初期評価候補 | 14 / 2026-01-28 |

## シナリオ・キャラクター・絵コンテ

[分野別詳細](categories/story.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [BlueFish](https://github.com/bluefish2026/BlueFish) | 複数のAIプロバイダを接続し、脚本から絵コンテ・動画制作まで管理する。 | AI連携 / 小規模・初期評価候補 | 8 / 2026-04-22 |
| [ink](https://github.com/inkle/ink) | 分岐する物語を書くスクリプト言語、コンパイラ、実行ランタイム。 | 非AI制作 / 制作基盤として比較 | 4,964 / 2026-05-05 |
| [SillyTavern](https://github.com/SillyTavern/SillyTavern) | キャラ設定とLorebookを使い、LLMとの対話や世界観の試作を行うフロントエンド。 | AI連携 / 更新のある導入・評価候補 | 34,266 / 2026-10-02 |
| [Yarn Spinner](https://github.com/YarnSpinnerTool/YarnSpinner) | ゲームの会話記述をコンパイル・実行する台詞制作基盤。 | 非AI制作 / 制作基盤として比較 | 2,855 / 2026-10-01 |
| [YumingScroll](https://github.com/tansuanyl/YumingScroll) | 物語テキストから世界観・人物・分鏡・画像/動画資産をひとつのプロジェクトにまとめるセルフホスト型AI漫劇制作ワークベンチ。Flow Mapで人物・場景・画風・15秒台本を接続する。 | AI連携 / 早期開発 | 1 / 2026-10-06 |

## ゲーム・ノベル・スプライト

[分野別詳細](categories/game.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ControlTile](https://github.com/Junrongh/ControlTile) | 条件付きの画像タイル生成を扱う研究実装。 | AIモデル・学習 / 小規模・初期候補 | 12 / 2026-07-27 |
| [Godot](https://github.com/godotengine/godot) | 2D/3Dゲーム制作と複数プラットフォームへの出力を行うゲームエンジン。 | 非AI制作 / 定番の制作基盤 | 118,168 / 2026-10-09 |
| [LDtk](https://github.com/deepnight/ldtk) | 2Dレベルを設計するオープンソースのエディタ。 | 非AI制作 / 制作基盤として比較 | 4,309 / 2026-10-09 |
| [OpenGame](https://github.com/leigest519/OpenGame) | 指示からWebゲームを制作するエージェント基盤。テンプレートとデバッグ手順を組み込む。 | AI連携 / 連携・制作ツール候補 | 2,974 / 2026-09-03 |
| [Pixelorama](https://github.com/Orama-Interactive/Pixelorama) | ドット絵・タイル・アニメーションを編集する制作アプリ。 | 非AI制作 / 定番の制作基盤 | 10,488 / 2026-10-08 |
| [PNGAL](https://github.com/1mm-module/PNGAL) | 顔差分生成・PSD分解・目パチと口パクの補間を組み合わせ、立ち絵アニメ素材を制作する。 | AI連携 / 導入経路の追加確認が必要 | 356 / 2026-09-01 |
| [RenPy](https://github.com/renpy/renpy) | テキストとキャラクター素材を組み合わせたノベルゲームを制作する。 | 非AI制作 / 定番の制作基盤 | 6,900 / 2026-10-09 |
| [sprite-maker](https://github.com/JohnKinyanjui/sprite-maker) | AIエージェントと連携して素材を作り、関節・ボーンとRust描画で再現可能なアニメーションを生成する。 | AI連携 / 初期評価候補 | 426 / 2026-09-24 |
| [Terrain Diffusion](https://github.com/xandergos/terrain-diffusion) | 広域地形を拡散モデルで生成し、地図から地形への変換も扱う。 | AIモデル・学習 / モデル・研究候補 | 1,427 / 2026-08-12 |
| [Tiled](https://github.com/mapeditor/tiled) | タイルとオブジェクトを配置して2Dゲームのマップを作る。 | 非AI制作 / 制作基盤として比較 | 12,952 / 2026-09-25 |
| [character-animation-creator-skill](https://github.com/tachikomared/character-animation-creator-skill) | Codex（OpenAI）およびGPT Web Agent向けのスキル。テキスト指定や参照画像から64×64ピクセルアートのキャラクタースプライトシートを、8方向×idle/walk/attackのアニメーション込みで生成し、パレット量子化や検証まで行う。 | AIモデル・学習 / 小規模・初期評価候補 | 343 / 2026-05-08 |
| [spritebrew](https://github.com/GAlbanese09/spritebrew) | テキストや既存画像からピクセルアートのキャラクターを生成し、アニメーション化・スライス・プレビュー・エクスポートまで一貫して行うWebツール。21種のスタイルと複数エンジン向け書き出しに対応する。 | AIモデル・学習 / 稼働中・実運用候補 | 61 / 2026-10-07 |

## アニメ制作・中割り・彩色・リップシンク

[分野別詳細](categories/animation.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AniDoc](https://github.com/robbyant-research/AniDoc) | 設定画を参照してスケッチ列を彩色するアニメ制作研究。 | AIモデル・学習 / モデル・研究候補 | 573 / 2025-04-15 |
| [AnimeColor](https://github.com/IamCreateAI/AnimeColor) | 設定画参照とスケッチ動画からアニメを彩色する拡散Transformer。 | AIモデル・学習 / 小規模・初期候補 | 9 / 2025-08-04 |
| [BasicPBC](https://github.com/ykdai/BasicPBC) | 閉領域の対応付けによってアニメ線画の塗りを支援するペイントバケット彩色。 | AIモデル・学習 / モデル・研究候補 | 307 / 2025-06-26 |
| [ECCV2022-RIFE](https://github.com/hzwer/ECCV2022-RIFE) | フレーム間の中間画像を推定する動画補間モデル。 | AIモデル・学習 / 比較・既存工程の参考 | 5,604 / 2025-09-10 |
| [LatentSync](https://github.com/bytedance/LatentSync) | 音声条件で口の動きを同期させる動画処理モデル。 | AIモデル・学習 / 比較・既存工程の参考 | 6,123 / 2025-06-20 |
| [opentoonz](https://github.com/opentoonz/opentoonz) | 作画、彩色、撮影を扱う2Dアニメ制作アプリ。 | 非AI制作 / 定番の制作基盤 | 7,806 / 2026-10-09 |
| [ToonComposer](https://github.com/TencentARC/ToonComposer) | キーフレーム後の中割りと彩色を生成AIでまとめて処理する。 | AIモデル・学習 / 研究・技術評価候補 | 591 / 2025-08-20 |
| [ToonCrafter](https://github.com/Doubiiu/ToonCrafter) | 二枚のアニメ画像の間を生成する補間モデル。 | AIモデル・学習 / モデル・研究候補 | 6,032 / 2025-03-19 |
| [comic-manga-narrator](https://github.com/MushiSenpai/comic-manga-narrator) | 漫画/コミックページを、コマ検出・セリフの音声化・ナレーション・Ken Burnsと2.5Dパララックスで演出したナレーション付きMP4に変換するローカルパイプライン。 | AIモデル・学習 / 小規模・初期評価候補 | 0 / 2026-07-12 |
| [vedGen](https://github.com/HarisUmer/vedGen) | 一行のあらすじから絵コンテ→ショット別I2V→結合までをローカルGPUで回すアニメ風短編動画生成ライブラリ。ComfyUIをヘッドレスでAPI駆動し、Pythonライブラリとして呼び出す。 | AIモデル・学習 / 小規模・初期評価候補 | 1 / 2026-07-22 |

## 2Dキャラクター・自動リギング

[分野別詳細](categories/rig2d.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Anime2.5DRig](https://github.com/852wa/Anime2.5DRig) | PSDからリグを自動構成し、目パチ・口パク・髪物理・顔追跡で動かす。 | AIは任意 / 導入候補 | 238 / 2026-09-23 |
| [PuppetLoom](https://github.com/CheshireMew/PuppetLoom) | レイヤーPSDを自動バインドし、改訂履歴・検証を残して動く2Dキャラを制作する。 | AI連携 / 要再確認 | 245 / 2026-10-05 |
| [stretchystudio](https://github.com/MangoLion/stretchystudio) | PSDを読み込み、自動リギングとタイムライン上のメッシュ変形でアニメーションを編集する。 | AI連携 / 導入候補 | 503 / 2026-04-28 |
| [psd2live](https://github.com/tsunehimatoi/psd2live) | レイヤー分けしたPSDからLive2Dモデルを自動生成し、同じ作業画面で修形・リギング・物理・アニメーション・書き出しまで行うデスクトップツール。 | AIは任意 / 活発・候補 | 598 / 2026-10-09 |
| [live2d-py](https://github.com/EasyLive2D/live2d-py) | Live2DモデルをPythonから直接読み込み・描画するC++拡張ライブラリ。Web Engineを挟まず、OpenGLコンテキストがあれば任意のOpenGLウィンドウに描画できる。 | 非AI制作 / 実運用段階のライブラリ | 576 / 2026-09-30 |
| [ayagami](https://github.com/AyagamiDev/ayagami) | Live2D（MOC3）互換の2Dパペット読み込み・描画SDK。Rust実装で、wgpuベースのリファレンスレンダラとGodotコンポーネントを備える。 | 非AI制作 / 初期評価候補 | 350 / 2026-09-14 |
| [Amahane-Hikari-Live2D](https://github.com/luomo66ccff/Amahane-Hikari-Live2D) | AIエージェントと協働してLive2Dキャラクターを制作し、TypeScript/WebGLのWebランタイムで再生する制作プロジェクト。制作フローをSkillとして公開する。 | AI連携 / 活発な候補 | 112 / 2026-09-21 |
| [live2d-agent-kit](https://github.com/Ariakage/live2d-agent-kit) | coding agentが参考図や分层PSDから.moc3を作るためのLive2D制作キット。psd2liveアダプタ、アニメ超分スクリプト、検証手順を含む。 | AI連携 / 小規模・初期評価候補 | 25 / 2026-09-12 |
| [iki](https://github.com/zeikar/iki) | MITの2Dパペットエンジン。AIエージェントが画像モデルでパーツを描き、役割名付きレイヤーから.iki形式へ自動リギングする。 | AI連携 / 初期評価候補 | 14 / 2026-10-09 |
| [spine-parts](https://github.com/firejune/spine-parts) | 1枚のアニメ絵からSpine 2Dキャラのパーツを組み立てるCLI。See-throughのレイヤ分解結果を統合し、メッシュ・ボーン・ループidleをspine-rigc仕様で生成、書き出し前に数値で検査する。 | AI連携 / 小規模・初期評価候補 | 2 / 2026-10-09 |
| [still2rig-psd](https://github.com/shinshin86/still2rig-psd) | 1枚のアニメキャラ画像をSee-throughで意味的にレイヤー分解し、構造チェック付きのPSDへ組み立てるワークフロー。組み込みWebUIでまばたき・口・髪/体のモーションをプレビューできる。 | AIモデル・学習 / 小規模・初期評価候補（READMEはv0.1 alphaと明記） | 130 / 2026-09-29 |

## レイヤー分解

[分野別詳細](categories/layer.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ComfyUI-See-through](https://github.com/jtydhr88/ComfyUI-See-through) | See-throughによる分解をComfyUIのノード工程へ接続する。 | AI連携 / ComfyUI利用者向け | 832 / 2026-08-20 |
| [Qwen-Image-Layered](https://github.com/QwenLM/Qwen-Image-Layered) | 画像を複数の編集可能なレイヤーに分解し、個別の色・位置・サイズ変更につなげる。 | AIモデル・学習 / 基盤技術候補 | 2,129 / 2025-12-31 |
| [see-through](https://github.com/shitagaki-lab/see-through) | 一枚絵を意味別パーツへ分解し、遮蔽部分を補完してPSDに出力する。 | AIモデル・学習 / 導入候補 | 4,497 / 2026-10-05 |
| [Stable Layers](https://github.com/Stability-AI/Stable-Layers) | Qwen-Image-Layered上のLoRAで、画像を背景と物体の編集用RGBA層へ分解する。 | AIモデル・学習 / レイヤー分解の研究候補 | 24 / 2026-07-23 |
| [loom-unravel](https://github.com/byeolki/loom-unravel) | 1枚のアニメキャラ立ち絵を顔パーツ単位のRGBAレイヤーと、階層・深度順・アンカー点を持つメタデータに分解するオフラインパイプライン。 | AIモデル・学習 / 初期評価候補 | 0 / 2026-09-11 |
| [see-through-portable](https://github.com/iamtie34/see-through-portable) | アニメキャラのイラスト1枚を最大23の意味レイヤー（前髪/後ろ髪・目・眉・衣装・小物など）に分解し、各レイヤーを補完して深度順に並べ、多層PSDとして書き出すWindows向けワンクリック配布版。ベースはSee-through（Apache-2.0）。 | AIモデル・学習 / 小規模・初期評価候補 | 2 / 2026-06-06 |

## 画像生成・編集・切り抜き

[分野別詳細](categories/image.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [anime-segmentation](https://github.com/SkyTNT/anime-segmentation) | アニメ絵のキャラクター領域を抽出し、背景除去や合成用マスクを作る。 | AIモデル・学習 / 比較・既存工程の参考 | 847 / 2025-05-21 |
| [krita-ai-diffusion](https://github.com/Acly/krita-ai-diffusion) | Kritaの描画工程へ画像生成・インペイント・アウトペイントを組み込む。 | AI連携 / 更新のある導入・評価候補 | 10,683 / 2026-10-03 |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image) | テキスト描画と画像編集を扱う汎用画像モデル群。表紙・小物・宣伝画像の制作候補。 | AIモデル・学習 / 研究モデルの評価候補 | 8,390 / 2026-02-10 |
| [Z-Image](https://github.com/Tongyi-MAI/Z-Image) | 6B級の汎用画像モデル群。Turboやベースモデルを用途に合わせて利用する。 | AIモデル・学習 / 研究モデルの評価候補 | 12,073 / 2026-02-09 |
| [ComfyUI-Forbidden-Vision](https://github.com/luxdelux7/ComfyUI-Forbidden-Vision) | アニメ調・実写の両方に対応する顔の検出・セグメンテーション・補正を行うComfyUIカスタムノード群。ADetailerやFaceDetailerの代替を狙い、独自学習モデルを同梱する。 | AIモデル・学習 / 更新中の実装候補 | 104 / 2026-07-19 |
| [ComfyUI-Ultimate-Face-Fix](https://github.com/Merserk/ComfyUI-Ultimate-Face-Fix) | 顔を検出して切り出し、接続した生成モデルでimg2img修復し、意味マスクで顔だけを元画像に合成するComfyUIノード。 | AI出力の後処理 / 活発・候補 | 26 / 2026-07-21 |
| [Colortina](https://github.com/Amster-Ilvil/Colortina) | manga-colorization-v2を基にしたローカル漫画自動彩色デスクトップツール。手動カラーヒント、区域ごとの再彩色、髪色補正、バッチ処理を備える。 | AIモデル・学習 / 小規模・初期評価候補 | 1 / 2026-08-23 |
| [ComfyUI-NeuralBooru](https://github.com/ChrisJohnson89/ComfyUI-NeuralBooru) | 自然文のシーン記述をローカルLLMでDanbooruタグに変換するComfyUIノード。約14万件の実在タグ語彙で検証・別名変換・語形修正・並び替えを行い、テンプレートで包んでサンプラーへ渡す。 | AIモデル・学習 / 小規模・初期評価候補 | 20 / 2026-07-10 |
| [ComfyUI-AnimeRembg](https://github.com/mincad/ComfyUI-AnimeRembg) | アニメキャラ動画のアルファマットを抽出するComfyUIカスタムノード集。既知背景の差分マッティングとデスピルを実装する。 | AI出力の後処理 / 小規模・初期評価候補（beta） | 1 / 2026-08-04 |
| [CYKSM](https://github.com/Nigh/CYKSM) | realesrgan-x4plus-animeモデルを手軽に使うためのGUIツール。画像を左側にドラッグ&ドロップしてボタンを押すと超解像し、結果を右側にプレビューする。 | AIモデル・学習 / 小規模・初期評価候補 | 102 / 2026-08-21 |
| [Caelum](https://github.com/yumenana/Caelum) | アニメイラスト専用の×4超解像・圧縮劣化復元ツール（Windows GUI）。Pixiv/X/Facebook等の再アップロードで劣化した画像の復元を狙い、PPBUNetという独自構成を採る。 | AIモデル・学習 / 小規模・初期評価候補 | 16 / 2026-09-05 |
| [ComfyUI_LayerStyle](https://github.com/chflame163/ComfyUI_LayerStyle) | ComfyUIにPhotoshop風のレイヤー合成・マスク処理ノード群を追加するカスタムノード。合成・マスク・切り抜き・プロンプト補助などのノードをまとめて提供する。 | AIは任意 / 活発・実用段階 | 3,181 / 2026-09-16 |
| [QualityScaler](https://github.com/Djdefrag/QualityScaler) | 画像・動画をAIで拡大・ノイズ除去するWindows向けGUIアプリ。タイル分割でVRAM制限を回避し、動画の停止再開や補間、マルチGPUにも対応。 | AIモデル・学習 / 活発・実用段階 | 3,205 / 2026-08-27 |
| [abg-comfyui](https://github.com/kwaroran/abg-comfyui) | アニメ画像の背景除去を行うComfyUIノード。skytntのanime-remove-background系スペースを土台にしている。 | AIモデル・学習 / 公開済み | 25 / 2024-05-22 |
| [upscalejs](https://github.com/gqgs/upscalejs) | ブラウザ内でONNX Runtime Webを使い超解像モデルで画像を拡大するJSライブラリ。Real-ESRGAN anime 4x等をWeb Workerで実行する。 | AIモデル・学習 / 公開済み（v2） | 24 / 2026-04-15 |
| [Xyether-Anime-Upscaler](https://github.com/XYETHER/Xyether-Anime-Upscaler) | アニメ・イラスト向けの2倍超解像モデル。SRVGGアーキテクチャで、線画・色・キャラディテールの保持を狙う。GitHub Releaseで重みを配布。 | AIモデル・学習 / 小規模・初期評価候補 | 7 / 2026-08-30 |

## 動画生成

[分野別詳細](categories/video.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [FramePack](https://github.com/lllyasviel/FramePack) | 過去フレームの文脈を圧縮して動画を逐次生成する実装・デスクトップUI。 | AIモデル・学習 / モデル・研究候補 | 17,278 / 2025-10-16 |
| [Index-anisora](https://github.com/bilibili/Index-anisora) | アニメ向け動画生成。版ごとに任意フレーム、マスク制御、スタイル変換等を提供。 | AIモデル・学習 / モデル・研究候補 | 2,526 / 2026-07-16 |
| [LTX-2](https://github.com/Lightricks/LTX-2) | 音声・動画生成とLoRA学習を扱う公式実装。READMEはLTX-2.5の導入も案内する。 | AIモデル・学習 / 更新のある導入・評価候補 | 9,633 / 2026-10-02 |
| [LTX-Video](https://github.com/Lightricks/LTX-Video) | LTXの旧世代動画生成実装。 | AIモデル・学習 / 旧版・履歴資料 | 11,057 / 2026-01-05 |
| [SCAIL-2](https://github.com/zai-org/SCAIL-2) | 参照キャラクターに動画の動きを移し、複数参照やキャラクター置換にも対応する。 | AIモデル・学習 / 研究・技術評価候補 | 1,251 / 2026-08-24 |
| [Wan-Move](https://github.com/ali-vilab/Wan-Move) | 動きの軌跡を条件に動画を生成するWan系実装。 | AIモデル・学習 / モデル・研究候補 | 659 / 2026-01-05 |
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) | テキストや画像から動画を作るWan2.2公式モデル群。 | AIモデル・学習 / 研究モデルの評価候補 | 17,819 / 2026-09-21 |
| [vlog2anime-kit](https://github.com/mincad/vlog2anime-kit) | 実写動画の人物を参照画像のアニメキャラへ置換し、元人物を露出させずに実写背景へ戻すComfyUIワークフロー集。Wan2.2 Animate/SCAIL-2で変換し、SAM3追跡＋MatAnyone2でマットを作る。 | AIモデル・学習 / 小規模・初期評価候補 | 2 / 2026-08-04 |
| [video-regen-recipes](https://github.com/Shenrui-Ma/video-regen-recipes) | Agentに指示してローカルMiniMax H3でMAD・手書・鬼畜等の二創動画を再現するためのテンプレート集（20件）とSkills。参考図生成・音声クローン・後期編集まで手順書と検証プロンプトを同梱する。 | AIモデル・学習 / 小規模・初期評価候補 | 10 / 2026-09-18 |
| [NijiLucid](https://github.com/chenmozhijin/NijiLucid) | WebGPUでブラウザ上のアニメ動画をリアルタイムに超解像する拡張。動画プレイヤーに「超分」ボタンを出し、2x/4x/8xや目標解像度で拡大する。快速/均衡/質量/極致の性能档位とカスタム効果合成を備える。 | AIモデル・学習 / 活発・実用候補 | 239 / 2026-09-10 |

## 3D生成・モデリング・リギング

[分野別詳細](categories/3d.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AniGen](https://github.com/VAST-AI-Research/AniGen) | 一枚の画像から形状・骨格・スキンウェイトを一緒に生成する。 | AIモデル・学習 / モデル・研究候補 | 518 / 2026-07-15 |
| [Blender](https://github.com/blender/blender) | モデリング、リギング、アニメ、レンダリング、合成を扱う統合制作環境。 | 非AI制作 / 定番の制作基盤 | 20,790 / 2026-10-09 |
| [Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) | 画像から3D形状と材質を生成する公式実装。 | AIモデル・学習 / 比較・既存工程の参考 | 4,154 / 2025-10-17 |
| [Pixal3D](https://github.com/TencentARC/Pixal3D) | 画像からPBR付き3Dを生成。2026年9月に多視点推論経路を追加。 | AIモデル・学習 / モデル・研究候補 | 2,440 / 2026-09-01 |
| [Puppeteer](https://github.com/Seed3D/Puppeteer) | 3Dメッシュに骨格とウェイトを付け、動画誘導でアニメーションする。 | AIモデル・学習 / モデル・研究候補 | 428 / 2025-09-19 |
| [Roblox Cube / CubePart](https://github.com/Roblox/cube) | テキストからの形状生成に加え、メッシュと部品定義から構造を持つ部品群を生成する。 | AIモデル・学習 / モデル・研究候補 | 1,267 / 2026-05-28 |
| [SkinTokens](https://github.com/VAST-AI-Research/SkinTokens) | TokenRigで骨格とスキンウェイトを一つの系列として生成する自動リギング研究。 | AIモデル・学習 / 研究モデルの評価候補 | 463 / 2026-05-12 |
| [SQuadGen](https://github.com/microsoft/SQuadGen) | 3D形状上の単純な四角形レイアウトを生成する研究。 | AIモデル・学習 / 小規模・初期候補 | 35 / 2026-08-31 |
| [TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | 画像から形状・材質を備えた3Dアセットを生成する4Bモデル。 | AIモデル・学習 / 研究モデルの評価候補 | 11,644 / 2026-07-10 |
| [UniRig](https://github.com/VAST-AI-Research/UniRig) | 形状から骨格推定とスキニングを行う自動リギング研究。 | AIモデル・学習 / 比較・既存工程の参考 | 1,805 / 2026-06-04 |
| [SekaiBlender](https://github.com/ShiJieWorld/SekaiBlender) | MMD向けに特化したBlenderブランチ。PMX/VMDのネイティブ入出力、CCD IKソルバ、Bullet物理、FSR拡大を統合する。 | 非AI制作 / 小規模・初期評価候補 | 17 / 2026-09-18 |
| [godot-vrm](https://github.com/V-Sekai/godot-vrm) | Godot 4.1+/3.2+向けにVRMアバターとMToonシェーダのインポート/エクスポートを提供するプラグイン。Asset Libraryから入手できる。 | 非AI制作 / 活発・実用段階 | 475 / 2026-07-08 |
| [awesome-astra-blender-characters](https://github.com/icesixgod/awesome-astra-blender-characters) | 人物参考図から編集可能なBlenderキャラクターを作るAIエージェント向けスキル。九方向ビュー作成、顔・髪の制作、部分修正、多視点検収を手順化する。 | AI連携 / 小規模・初期評価候補（指示書のみ） | 117 / 2026-09-10 |

## TTS・キャラクター音声

[分野別詳細](categories/tts.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [CosyVoice](https://github.com/QwenAudio/CosyVoice) | ストリーミング対応の多言語音声合成。現行READMEはFun-CosyVoice3を案内。 | AIモデル・学習 / モデル・研究候補 | 23,903 / 2026-05-25 |
| [F5-TTS](https://github.com/SWivid/F5-TTS) | 参照音声とテキストを使うフローマッチング音声合成・追加学習。 | AIモデル・学習 / モデル・研究候補 | 15,363 / 2026-09-21 |
| [fish-speech](https://github.com/fishaudio/fish-speech) | Fish Audio S2系の表現豊かなTTS・音声クローンを扱う実装。 | AIモデル・学習 / 更新のある導入・評価候補 | 32,978 / 2026-10-05 |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 少量音声を使うTTSと音声クローンをWebUIから扱う。 | AIモデル・学習 / 更新のある導入・評価候補 | 62,587 / 2026-10-08 |
| [IndexTTS](https://github.com/index-tts/index-tts) | 声質・感情の条件を扱う音声合成。現行2.5は日本語を含む5言語を案内。 | AIモデル・学習 / モデル・研究候補 | 24,379 / 2026-09-29 |
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | 声のデザイン、参照音声による合成、指示による話し方制御を扱う多言語TTS。 | AIモデル・学習 / 研究モデルの評価候補 | 13,709 / 2026-03-17 |
| [RVC WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | 入力音声の発話内容を保ちながら学習した声へ変換する。 | AIモデル・学習 / モデル・研究候補 | 38,663 / 2026-08-04 |
| [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) | Bert-VITS2を基に音声スタイルの制御と学習を扱う日本語TTSツール。 | AIモデル・学習 / 比較・既存工程の参考 | 1,382 / 2025-12-07 |
| [voicevox](https://github.com/VOICEVOX/voicevox) | 日本語のキャラクター音声を編集して出力するVOICEVOXのエディタ。 | AI連携 / 定番の制作基盤 | 3,264 / 2026-10-07 |
| [Genie-TTS](https://github.com/High-Logic/Genie-TTS) | GPT-SoVITS（V2/V2ProPlus）をONNX化してCPUで動かす軽量推論エンジン。TTS推論・モデル変換・FastAPIサーバーをまとめて提供する。 | AIモデル・学習 / 活発・実用段階 | 1,796 / 2026-08-30 |
| [TTS-WebUI](https://github.com/rsxdalv/TTS-WebUI) | 多数のTTS/音声生成モデルを1つのGradio+React UIで扱うWebUI。GPT-SoVITS、XTTSv2、Kokoro、StyleTTS2、RVC、MusicGen、Demucs等の拡張を備える。 | AIモデル・学習 / 活発・実用段階 | 3,287 / 2026-09-07 |
| [vits-simple-api](https://github.com/Artrajz/vits-simple-api) | VITS系TTSをHTTP APIとして提供するサーバー。VITS/Bert-VITS2/GPT-SoVITS/emotion-vits等の複数モデルを読み込み、GETで音声合成できる。 | AIモデル・学習 / 活発・実用段階 | 1,050 / 2026-05-18 |
| [sukasuka-vocal-dataset-builder](https://github.com/Hecate2/sukasuka-vocal-dataset-builder) | アニメ本編やドラマCDと字幕から、役柄ごとの音声を切り出してデータセット化するスクリプト群。TTS/SVC学習用のキャラクター音声データ作成を想定。 | 非AI制作 / コミュニティ運用中 | 54 / 2026-09-20 |

## ASMR・効果音・環境音

[分野別詳細](categories/sound.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ASMRify](https://github.com/ReactorcoreGames/ASMRify) | 音声に定位移動・残響・ピッチ等を加えて一括処理するASMR向け音声加工ツール。 | AI出力の後処理 / 小規模・初期評価候補 | 1 / 2026-06-18 |
| [Audacity](https://github.com/audacity/audacity) | 録音とマルチトラック編集を行う音声制作アプリ。 | 非AI制作 / 制作基盤として比較 | 18,682 / 2026-10-09 |
| [Binaural Speech Synthesis](https://github.com/facebookresearch/BinauralSpeechSynthesis) | モノラル音声を空間条件に従うバイノーラル音声へ変換する研究。 | AIモデル・学習 / アーカイブ済み資料 | 191 / 2022-05-19 |
| [ControlFoley](https://github.com/xiaomi-research/controlfoley) | 動画・テキスト・参照音を条件に、効果音とそのタイミングを制御する。 | AIモデル・学習 / 小規模・初期候補 | 155 / 2026-08-28 |
| [FoleyCrafter](https://github.com/open-mmlab/FoleyCrafter) | 動画の内容とタイミングに合わせた効果音を生成する研究実装。 | AIモデル・学習 / 研究モデルの評価候補 | 666 / 2026-06-15 |
| [MMAudio](https://github.com/hkchengrex/MMAudio) | 動画やテキストを条件に、時間的に対応する音声を生成する。 | AIモデル・学習 / 研究モデルの評価候補 | 2,276 / 2026-02-23 |
| [stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools) | 条件付き音声生成モデルの学習と推論を行うツール群。効果音や環境音素材を検討できる。 | AIモデル・学習 / 更新のある導入・評価候補 | 3,876 / 2026-10-09 |
| [Steam Audio](https://github.com/ValveSoftware/steam-audio) | ゲーム空間に合わせた音の定位・伝播を扱う空間音響SDK。 | 非AI制作 / 制作基盤として比較 | 2,963 / 2026-03-25 |
| [Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui) | 音源分離モデルをGUIで使い、歌・伴奏等を分離する。 | AI連携 / 連携・制作ツール候補 | 26,544 / 2026-10-06 |
| [agent-audio](https://github.com/AIEGOBOT/agent-audio) | コーディングエージェント（Codex/Claude Code/Cursor）から呼び出せるローカル音声生成のMCPサーバー兼Agent Skill。Stable Audio 3 Mediumで効果音や音楽を生成し、ComfyUIや有料APIを不要にする。 | AIモデル・学習 / 小規模・初期評価候補 | 39 / 2026-10-05 |

## 音楽・歌声合成

[分野別詳細](categories/music.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | ローカルで楽曲を生成し、編集や追加学習につなげる音楽モデル。 | AIモデル・学習 / 更新のある導入・評価候補 | 13,322 / 2026-10-05 |
| [Basic Pitch](https://github.com/spotify/basic-pitch) | 音声を音高ベンド付きMIDIへ変換する軽量な採譜モデル。 | AIモデル・学習 / 連携・制作ツール候補 | 5,828 / 2025-11-13 |
| [DiffSinger](https://github.com/openvpi/DiffSinger) | 歌声合成の学習・推論と、ピッチ・エネルギー・息成分などの制御を扱う。 | AIモデル・学習 / 更新のある導入・評価候補 | 3,218 / 2026-10-08 |
| [OpenUtau](https://github.com/openutau/OpenUtau) | UTAUコミュニティ向けの歌声編集・合成プラットフォーム。 | AIは任意 / 定番の制作基盤 | 4,391 / 2026-10-09 |
| [SOFA](https://github.com/qiuqiao/SOFA) | 歌声向けの強制アラインメントで歌詞・音素の時間位置を求める。 | AIモデル・学習 / モデル・研究候補 | 242 / 2026-09-02 |
| [YuE2](https://github.com/multimodal-art-projection/YuE) | 歌詞と曲調から編集可能な旋律・和音計画を作り、歌と伴奏へ展開する。 | AIモデル・学習 / モデル・研究候補 | 11,049 / 2026-10-06 |
| [OpenUtauMobile](https://github.com/vocoder712/OpenUtauMobile) | モバイル向けのオープンソース歌声合成エディタ。OpenUtau CoreをベースにUSTXプロジェクトファイルを扱い、DiffSinger／UTAU／Vogenの音源を読み込める。 | AI連携 / 初期評価候補 | 334 / 2026-10-09 |
| [SoulX-Singer](https://github.com/Soul-AILab/SoulX-Singer) | 未見の歌声を生成するゼロショット歌声合成（SVS）モデルの公式推論コード。メロディ（F0）条件と楽譜（MIDI）条件に対応し、歌声変換（SVC）版も提供する。 | AIモデル・学習 / モデル候補 | 994 / 2026-05-29 |
| [DiffSinger](https://github.com/MoonInTheRiver/DiffSinger) | Shallow Diffusion機構を用いた歌声合成（DiffSinger）と音声合成（DiffSpeech）の公式PyTorch実装。歌詞+MIDI/F0からメルへ、メルから波形へ変換する複数構成を提供する。 | AIモデル・学習 / 確立した参照実装 | 4,873 / 2026-07-24 |
| [yinyue](https://github.com/yishui111/yinyue) | 楽曲の原声を二次元キャラの声へ置き換えるローカルGPU向けシステム。RVC・GPT-SoVITS・so-vits-svc・DiffSingerを総控えページと端末間パイプラインで束ねる。 | AIモデル・学習 / 小規模・初期評価候補（作者の自作物のみ公開） | 0 / 2026-10-03 |

## VTuber・AIキャラクター・VRM

[分野別詳細](categories/vtuber.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AIRI](https://github.com/moeru-ai/airi) | 会話するバーチャルキャラクターを構築する環境。 | AI連携 / 更新のある導入・評価候補 | 50,220 / 2026-10-09 |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) | Babylon.jsでMMDモデル・モーションを読み込み、物理・IK・モーフを再生する。 | 非AI制作 / 制作基盤として比較 | 256 / 2026-09-09 |
| [inochi-creator](https://github.com/Inochi2D/inochi-creator) | レイヤー画像を変形させ、ゲームやVTuberで動かす2Dモデルを作るエディタ。 | 非AI制作 / 比較・既存工程の参考 | 1,240 / 2025-06-16 |
| [OBS Studio](https://github.com/obsproject/obs-studio) | 画面・カメラ・音声を合成して録画・配信する。 | 非AI制作 / 制作基盤として比較 | 77,200 / 2026-10-09 |
| [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | 音声会話・視覚認識・Live2D表示を組み合わせるAIキャラクター環境。 | AI連携 / 連携の評価候補 | 14,026 / 2026-05-15 |
| [OpenSeeFace](https://github.com/emilianavt/OpenSeeFace) | Webカメラから顔のランドマークを推定し、アバター駆動へ渡す。 | AIモデル・学習 / 連携・制作ツール候補 | 2,083 / 2026-09-18 |
| [PersonaLive](https://github.com/GVCLab/PersonaLive) | 参照人物の画像を動作入力に従ってストリーミングでアニメーションする。 | AIモデル・学習 / モデル・研究候補 | 3,955 / 2026-08-28 |
| [three-vrm](https://github.com/pixiv/three-vrm) | three.jsでVRMアバターを読み込み表示するライブラリ。 | 非AI制作 / 制作基盤として比較 | 2,210 / 2026-10-02 |
| [UniVRM](https://github.com/vrm-c/UniVRM) | Unity用のVRM形式実装。3Dアバターの読み込み・書き出しを扱う。 | 非AI制作 / 定番の制作基盤 | 3,392 / 2026-10-06 |
| [VTubeStudio](https://github.com/DenchiSoft/VTubeStudio) | VTube Studioを外部から制御する公式API文書・開発資料。 | AI連携 / 連携用文書資料 | 1,312 / 2026-09-28 |
| [prometheus-avatar](https://github.com/myths-labs/prometheus-avatar) | LLM出力でLive2D/3Dアバターを動かすオープンソースSDK。口パク、感情表現、リアルタイム音声、TTS、VTuberモード、MCPサーバをまとめる。 | AI連携 / 小規模・初期評価候補 | 17 / 2026-10-09 |
| [VMagicMirror](https://github.com/malaybaku/VMagicMirror) | WindowsでVRMモデルを読み込み、追加デバイスなしにキーボードとマウス操作をモーションとしてアバターの上半身に反映するアプリ。可変クロマキーに対応し、配信・ライブコーディング・デスクトップマスコットに使える。 | 非AI制作 / 確立済み | 545 / 2026-10-01 |
| [gaussian-vrm](https://github.com/naruya/gaussian-vrm) | three.js上でVRM形式のスキニング付きガウシアンアバター(GVRM)を扱う実装。three-vrmとgaussian-splats-3dを基盤に、VRMの操作（移動やアニメーション）をそのまま再利用できる。 | 非AI制作 / 研究実装・活発 | 426 / 2026-10-06 |
| [Cortico](https://github.com/Pal-AI-Lab/Cortico) | イベントストリームを中心に設計したエージェント基盤。ペルソナbot・AI配信者・ロールプレイ・コンパニオン向けで、Core/Persona/Memory/World/Botの4層構成と、外部環境を隔離して接続するWorld拡張機構を持つ。 | AIモデル・学習 / 活発・pre-release | 194 / 2026-10-09 |
| [Anima](https://github.com/Yun-0000/Anima) | ブラウザで動くVRMキャラクタースタジオ。テキストまたはリアルタイム音声でキャラと対話し、表情・リップシンク・身体モーションを付けて演技させる。 | AIモデル・学習 / 小規模・初期評価候補 | 3 / 2026-05-09 |
| [open-vt](https://github.com/erodozer/open-vt) | Godotで作られたオープンソースの2D VTuberソフト。OpenSeeFaceとVTubeStudioのトラッカーに対応し、OBSで取り込みやすい透過ウィンドウや複数ウィンドウのポップアウト操作を持つ。 | 非AI制作 / 実運用候補 | 282 / 2026-09-25 |
| [A.R.I.A](https://github.com/NekoUnix/A.R.I.A) | Live2D・VRM・GLB・PNG/GIFアバターをまとめて扱うクロスプラットフォームのアバタースタジオ。顔トラッキング、物理、ライティング、視覚アクション、複数アバターのOBS出力に対応する。 | 非AI制作 / Alpha・初期評価候補 | 10 / 2026-10-05 |
| [Seidr-Smidja](https://github.com/hrabanazviking/Seidr-Smidja) | AIエージェントがYAML仕様からVRMアバターを設計・構築・検証・レンダリングするヘッドレスなパイプライン。VRoidベーステンプレートにBlenderをヘッドレスで適用し、VRChat/VTube Studio互換を検査して.vrmを出力する。 | AI連携 / Genesis・初期評価候補 | 21 / 2026-10-07 |
| [vrm-studio](https://github.com/vucinatim/vrm-studio) | ブラウザで動くVTubingアプリ。Google MediaPipe Holisticで顔・手・全身をトラッキングし、Three.jsでVRMアバターを動かす。グリーンスクリーン、OBS連携、カルマンフィルタによる平滑化を備える。 | AIは任意 / 小規模・実用候補 | 21 / 2025-12-09 |
| [CharacterStudio](https://github.com/M3-org/CharacterStudio) | ブラウザ上でglTF/VRMアバターを組み立てるオープンソースの3Dアバター制作スタジオ。パーツのドラッグ＆ドロップ配置、色変更、VRM最適化、glb/VRM書き出しに対応。 | 非AI制作 / 活発・実用段階 | 354 / 2026-08-11 |
| [ndmf-vrm-exporter](https://github.com/hkrn/ndmf-vrm-exporter) | NDMFベースでVRChatアバターをVRM 1.0として書き出すUnityプラグイン。PhysBone→SpringBone、Constraint→VRM Constraint、lilToon→MToon互換設定の自動変換に対応。 | 非AI制作 / 活発・実用段階 | 77 / 2026-09-29 |
| [app](https://github.com/vcamapp/app) | macOSでVRMアバターを仮想カメラとして表示するアプリ。ZoomやGoogle Meetなどでアバターを映像として映せる。 | 非AI制作 / 活発・実用段階 | 278 / 2026-10-08 |
| [VTubeStudio.Client](https://github.com/Agash/VTubeStudio.Client) | VTube Studio公開API（WebSocket）向けの.NET 10/C# 14クライアントライブラリ。型付きメッセージとイベントハブ、DI対応パッケージを提供する。 | 非AI制作 / 公開済み（NuGet） | 1 / 2026-10-05 |
| [KuroBlob-AI](https://github.com/eykicuihb/KuroBlob-AI) | HTML5 Canvasで動く手続き生成のゼリー型3D風アバターエンジン。ベジェばね物理、表情タイムライン、Web VTuber面追従、LLM対話、MP4書き出しを備える。 | AIモデル・学習 / 小規模・初期評価候補 | 26 / 2026-09-16 |

## 制作ワークフロー・追加学習

[分野別詳細](categories/workflow.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 画像・動画などのモデルをノードで接続して制作工程を構成する。 | AI連携 / 更新のある導入・評価候補 | 136,628 / 2026-10-09 |
| [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) | Wan系および関連動画モデルをComfyUIで使うためのラッパーノード。 | AI連携 / 連携の評価候補 | 6,726 / 2026-05-24 |
| [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) | 画像・動画の生成と追加学習を複数モデルで扱う統合実装。 | AIモデル・学習 / モデル・研究候補 | 13,214 / 2026-10-09 |
| [musubi-tuner](https://github.com/kohya-ss/musubi-tuner) | 画像・動画モデル向けのLoRA学習スクリプト群。 | AIモデル・学習 / 更新のある導入・評価候補 | 2,090 / 2026-09-30 |
| [sd-scripts](https://github.com/kohya-ss/sd-scripts) | 画像生成モデルの追加学習・LoRAを扱うスクリプト群。 | AIモデル・学習 / 連携・制作ツール候補 | 7,242 / 2026-09-24 |
| [ComfyUI-Anime-Extensions](https://github.com/ootsuka-repos/ComfyUI-Anime-Extensions) | ComfyUI向けのノード集で、音声合成、画像条件付きキャラクター音声、画像解析・切り抜き、音楽生成、動画生成、漫画ページ組み、VRM処理をまとめて扱う。 | AIモデル・学習 / 初期評価候補 | 1 / 2026-10-03 |
| [comfyui-stylebook](https://github.com/EnragedAntelope/comfyui-stylebook) | ComfyUI向けの画風プリセット集。650以上のスタイルにレンダ済みプレビュー、1000以上の作家記述子、130以上のモディファイアを同梱する。 | AIは任意 / 小規模・初期評価候補 | 10 / 2026-10-02 |
| [comfyui-imgutils](https://github.com/xiaden/comfyui-imgutils) | deepghs/imgutilsをComfyUI V3 APIでラップしたノード集。アニメ画像のタグ付け・検出・姿勢推定・分割など34ノードを提供する。 | AI連携 / 小規模・初期評価候補 | 1 / 2026-07-05 |
| [BooruDatasetTagManagerPlus](https://github.com/storyAura/BooruDatasetTagManagerPlus) | LoRA/キャラ画像データセット用のWindows打標ツール。booruタグ編集、WD14/PixAI/CL/OppaiOracleのONNX自動タグ付け、LLMキャプション、キャラタグ審査、RMBG背景除去、画像編集、動画フレーム抽出を備える。 | AI連携 / 活発・実用候補 | 18 / 2026-10-02 |
| [ComfyUI-BatchAnimeTimm](https://github.com/zzczzcx1/ComfyUI-BatchAnimeTimm) | フォルダ内の画像を一括でAnimeTimmタグ付けし、1画像につき1つの.txtキャプションを書き出すComfyUI出力ノード。モデルは1回ロードして使い回す。 | AI出力の後処理 / 公開済み | 3 / 2026-09-01 |
| [Anima-Portable-Standalone-Trainer](https://github.com/official-imvoiid/Anima-Portable-Standalone-Trainer) | Anima拡散アーキテクチャ（DiT + Qwen3テキストエンコーダ + VAE）向けのLoRA/ファインチューン用スタンドアロン学習UI。kohya-ssの学習スクリプトを改変し、ブラウザUIで操作する。 | AIモデル・学習 / v1.0.0（初期） | 1 / 2026-05-19 |
| [tag-skill](https://github.com/1756141021/tag-skill) | 役柄・動作・構図・環境・画風の要件から画像生成プロンプトを組み立てるエージェント向けスキル。SD/NovelAI/Anima/Krea 2など形式別の出力規則をまとめる。 | AI連携 / 小規模・初期評価候補（指示書のみ） | 14 / 2026-10-06 |

## 字幕・翻訳・ローカライズ

[分野別詳細](categories/localization.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ASMR Dubber](https://github.com/EveningStudy/asmr-dubber) | 日本語・英語の音声や動画を、校正可能な字幕・中国語吹替・二言語音声へ変換する制作ツール。 | AI連携 / 小規模・制作連携候補 | 228 / 2026-10-05 |
| [Manga OCR](https://github.com/kha-white/manga-ocr) | 日本語漫画の縦書き・横書き・ルビ付き文字を認識する。 | AIモデル・学習 / モデル・研究候補 | 2,800 / 2026-07-19 |
| [manga-image-translator](https://github.com/zyddnys/manga-image-translator) | 画像内の文字を検出・認識・翻訳し、元の文字を修復して訳文を組版する。 | AIモデル・学習 / 比較・既存工程の参考 | 10,490 / 2026-09-25 |
| [mokuro](https://github.com/kha-white/mokuro) | 漫画ページの文字位置とOCR結果をまとめ、選択可能なテキストとして閲覧できる形式へ変換。 | AI連携 / 連携・制作ツール候補 | 1,744 / 2026-07-20 |
| [VoiceTransl](https://github.com/shinnpuru/VoiceTransl) | 音声認識、字幕翻訳、字幕と動画の処理を組み合わせる。 | AI連携 / 連携の評価候補 | 1,305 / 2026-10-09 |
| [xianscan-rust](https://github.com/ArbenApura/xianscan-rust) | 漫画・韓漫・国漫向けのローカル完結型翻訳スタジオ。吹き出し検出、多言語OCR、LLM翻訳、LaMaによるインペイント、組版までを単体バイナリで実行する。 | AIモデル・学習 / 更新が活発な実装候補 | 82 / 2026-10-07 |
| [BallonsTranslator-Pro](https://github.com/thomaswantstobeaskeleton/BallonsTranslator-Pro) | BallonsTranslatorを元にした漫画・コミック翻訳ツールキットで、検出・OCR・翻訳・インペイント・植字を組み替え可能なモジュール群で処理する。 | AIモデル・学習 / 活発・候補 | 97 / 2026-07-31 |
| [CarrotMangaTranslator](https://github.com/ucx0204/CarrotMangaTranslator) | 漫画原稿のOCR→翻訳→原文消去→植字・検品→出力を扱うデスクトップアプリ。局所GemmaやOpenAI互換APIで翻訳する。 | AIモデル・学習 / 活発・候補 | 84 / 2026-10-07 |
| [Kites](https://github.com/Unheat/Kites) | ブラウザ拡張として動作し、WebGPU上でOCR・インペイント・翻訳を行って漫画をその場で翻訳表示するツール。 | AIモデル・学習 / 初期評価候補 | 33 / 2026-10-04 |
| [lumina](https://github.com/lumina-tl/lumina) | 漫画・マンファ・マンファ翻訳の無料デスクトップアプリ。テキスト検出・OCR・翻訳・インペイント・組版の全工程を自動化しつつ、各結果を手で修正できる。 | AIモデル・学習 / 活発・候補 | 19 / 2026-09-22 |
| [yakuyomi-engine](https://github.com/joyeli/yakuyomi-engine) | 端末上で動く漫画翻訳エンジン。検出・OCR・文字消去をNCNNでCPU実行し、翻訳のみネットワークLLMに投げる。読み手アプリYakuyomiに組み込まれる。 | AIモデル・学習 / 活発・候補 | 7 / 2026-10-08 |
| [translate-manga-br](https://github.com/marco0antonio0/translate-manga-br) | ローカルファーストの漫画翻訳フルスタックアプリ。YOLOで吹き出し検出、PaddleOCRでOCR、翻訳、編集可能オーバーレイ付きリーダーまでを1本で提供する。 | AIモデル・学習 / 小規模・初期評価候補 | 31 / 2026-09-29 |
| [LingoVeil](https://github.com/Gerald-Ha/LingoVeil) | 漫画・コミック向けのセルフホスト翻訳ツール。画像内のテキストを検出・翻訳し、翻訳ビューで読める。ブックマークや読書進捗も保持する。 | AIモデル・学習 / 小規模・初期評価候補 | 5 / 2026-09-30 |
| [OverTranslate](https://github.com/Hon-Lu/OverTranslate) | Windows向けの画面翻訳ツール。スクリーンショット翻訳・リアルタイム翻訳・取詞翻訳・快速翻訳・文字翻訳の5機能を持ち、認識した訳文を元の画面上にそのまま重ねて表示する。 | AIは任意 / 活発・実用候補 | 111 / 2026-10-09 |
| [FumetoReaderPlus](https://github.com/fumetodev/FumetoReaderPlus) | Android向け漫画リーダー。吹き出し検出・OCR・漫画向けLLM翻訳・風船内への再レタリングを端末上で行い、タップで原文に戻せる。 | AIモデル・学習 / 活発な候補 | 5 / 2026-10-04 |
| [Solar-Manga-Translator](https://github.com/soluna/Solar-Manga-Translator) | 中国語話者向けのローカル漫画翻訳・校正ワークベンチ。OCR、AI翻訳、擦字補修、自動嵌字、人手校正、導出を一流程にまとめる。 | AIモデル・学習 / 小規模・初期評価候補 | 4 / 2026-09-30 |
| [UGTLive](https://github.com/SethRobinson/UGTLive) | Windows向けGUIツールで、画面や画像の文字を「ライブ」でOCR・翻訳する。縦書き日本語の漫画読み上げ、PDF/CBZ/画像の一括変換、音声読み上げ、リアルタイム字幕にも対応する。 | AIモデル・学習 / 稼働中・実運用候補 | 118 / 2026-09-03 |
| [manga-translator](https://github.com/cameronkinsella/manga-translator) | Gio製GUIのデスクトップアプリで、画像内のテキストをOCRして翻訳する。検出した全テキストに色付きボックスを表示し、クリックで原文と訳文を確認・コピーできる。 | AI連携 / 稼働中 | 154 / 2026-02-01 |
| [AutoScanlate-AI](https://github.com/P4ST4S/AutoScanlate-AI) | 完全ローカル・GPU加速の漫画翻訳パイプライン。YOLOv8で吹き出し検出、MangaOCRで縦書きOCR、Qwen 2.5 7Bで文脈翻訳、マスク付きインペイントと段組みで元画像に描き戻す。Goバックエンド+Next.js UI+Pythonワーカーの構成。 | AIモデル・学習 / 小規模・初期評価候補 | 35 / 2026-09-07 |
| [manga-translator-android](https://github.com/jedzqer/manga-translator-android) | Android向けの漫画翻訳アプリ。ローカルで气泡・文字検出とOCRを行い、OpenAI互換APIで翻訳。翻訳气泡を原画上に重ね、位置をドラッグで調整できる。屏幕翻訳/悬浮窗にも対応。 | AIモデル・学習 / 活発に開発中 | 476 / 2026-10-09 |
| [local_anime_dubber](https://github.com/Bugsbunnydev2000/local_anime_dubber) | 日本語動画と短い声サンプルから英語吹き替えをローカル生成するパイプライン。声質をクローンし、BGM/効果音を残したままセリフのタイミングを映像に合わせる。 | AIモデル・学習 / 試作（prototype） | 3 / 2026-09-30 |
| [manhua](https://github.com/aklid01/manhua) | 中国語マンガ（manhua）ページを英語へ翻訳するローカル向けPythonパイプライン。吹き出し検出・OCR・翻訳・言い換え・描画・QA・梱包を段階別に実行する。 | AIモデル・学習 / 小規模・初期評価候補 | 5 / 2026-10-05 |
| [manga-image-translator-android](https://github.com/Yuu18id/manga-image-translator-android) | zyddnys/manga-image-translatorを基にしたAndroid向けオンデバイス漫画翻訳アプリ。日本語漫画をONNX Runtime Mobileで検出・OCR・インペイントし、LLMで翻訳する。 | AIモデル・学習 / 小規模・初期評価候補 | 4 / 2026-10-08 |

## モーション・身体演技

[分野別詳細](categories/motion.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ARDY](https://github.com/nv-tlabs/ardy) | テキストと運動学的制約から、対応骨格のモーションを生成する。 | AIモデル・学習 / モデル・研究候補 | 967 / 2026-07-10 |
| [EchoAvatar](https://github.com/RobinWitch/EchoAvatar) | ストリーミング音声から顔・身体の動きを生成してUnityアバターへ送る。 | AIモデル・学習 / 小規模・初期候補 | 48 / 2026-10-07 |
| [Gelina](https://github.com/TGuichoux/Gelina) | 音声とジェスチャーの生成・クローニング・音声から動作への変換を扱う。 | AIモデル・学習 / 小規模・初期候補 | 31 / 2026-10-01 |
| [HY-Motion 1.0](https://github.com/Tencent-Hunyuan/HY-Motion-1.0) | テキストから人型キャラクターの3D動作を生成する。 | AIモデル・学習 / モデル・研究候補 | 2,588 / 2026-07-18 |
| [R-DMesh](https://github.com/Tencent-Hunyuan/R-DMesh) | 静的メッシュを参照動画に沿って動く4Dメッシュ列へ変換する。 | AIモデル・学習 / 小規模・初期候補 | 62 / 2026-08-11 |
| [VRM-Spacing-Animation-Baking](https://github.com/Meringue-Rouge/VRM-Spacing-Animation-Baking) | VRM 1.0モデル向けBlenderアドオン。腕・脚・肩の間隔をMixamo風に調整し、髪やバストの物理ボーンをアニメへ焼き込み、ループ化する。 | 非AI制作 / 小規模・初期評価候補 | 10 / 2026-09-13 |
| [fbx2vrma-app](https://github.com/tk256ailab/fbx2vrma-app) | ヒューマノイドFBXアニメーションを.vrmaへ変換し、VRMモデルでプレビューできるブラウザベースのWebアプリ。複数ファイル一括変換とZIP一括DL、英日UI切り替えに対応。 | 非AI制作 / 小規模・初期評価候補 | 2 / 2026-06-06 |

## VFX・材質・ベクター演出

[分野別詳細](categories/vfx.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Effekseer](https://github.com/effekseer/Effekseer) | ゲーム向けのパーティクル効果を編集し、ランタイムで再生する。 | 非AI制作 / 制作基盤として比較 | 1,796 / 2026-09-14 |
| [GenCompositor](https://github.com/TencentARC/GenCompositor) | 前景・背景と制御条件を用いて動画を生成合成する。 | AIモデル・学習 / 小規模・初期候補 | 157 / 2026-06-30 |
| [Material Maker](https://github.com/RodZill4/material-maker) | ノードで手続き的なテクスチャを作り、3Dモデルへのペイントも行う。 | 非AI制作 / 制作基盤として比較 | 5,973 / 2026-10-07 |
| [OmniLottie](https://github.com/OpenVGLab/OmniLottie) | テキスト・画像等から編集可能なLottieベクターアニメーションを生成する。 | AIモデル・学習 / モデル・研究候補 | 798 / 2026-04-06 |
| [VfxDB](https://github.com/VfxDB-Official/VfxDB) | OpenVDB由来の疎な3Dボリューム効果を学習・生成する。 | AIモデル・学習 / 小規模・初期候補 | 8 / 2026-08-19 |
| [VFXMaster](https://github.com/libaolu312/VFXMaster) | 効果の参照映像を条件に動的なVFX動画を生成する。 | AIモデル・学習 / 小規模・初期候補 | 67 / 2026-04-07 |
| [cHiDeScaler-Neo](https://github.com/animeojisan/cHiDeScaler-Neo) | Windowsの任意ウィンドウをリアルタイムキャプチャし、GLSL/ONNXでAI拡大とRIFE系フレーム補間をかけるポータブルアプリ。Anime4K等のシェーダ資産を利用できる。 | AIモデル・学習 / 小規模・初期評価候補 | 21 / 2026-10-05 |
| [ComfyUI-CustomNodePacks](https://github.com/Code2Collapse/ComfyUI-CustomNodePacks) | ComfyUI向けの大規模カスタムノード群（142ノード）。SAM2.1/SAM3セグメンテーション、alpha matting、inpaintのcrop/stitch、動画マスク伝搬、EXR入出力・LUT等のVFXツールを含む。 | AI連携 / 活発・実用候補 | 58 / 2026-10-09 |

## 絵コンテ・制作管理・評価

[分野別詳細](categories/production.md)

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Kitsu](https://github.com/cgwire/kitsu) | アニメ・VFX・ゲーム制作の成果物、レビュー、進行を管理するWebアプリ。 | 非AI制作 / 制作基盤として比較 | 733 / 2026-10-09 |
| [Storyboarder](https://github.com/wonderunit/storyboarder) | 絵コンテを描き、ショットの順序と時間を試すアニマティクス制作ツール。 | 非AI制作 / 既存研究・制作の参考 | 3,871 / 2024-03-17 |
| [StyleID](https://github.com/kwanyun/StyleID) | 画風変化に強い顔の同一性特徴を計算し、比較・検索・評価に使う。 | AIモデル・学習 / 小規模・初期候補 | 34 / 2026-08-16 |
| [Nomi](https://github.com/aqm857886159/Nomi) | ローカル優先のAI動画制作スタジオ。エージェントがショット分割・キーフレーム生成・動画化・タイムライン配置を支援する。 | AIモデル・学習 / 活発・候補 | 556 / 2026-10-09 |
