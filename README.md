# サブカルコンテンツ制作リサーチ

一覧更新日: 2026-09-09。**115件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

漫画・ゲーム・アニメ・3D・ASMR／音声・TTS・画像生成・動画生成・VTuberに加え、歌声合成、シナリオ、リギング、翻訳、追加学習などを集約しています。AIを使わない二次元・キャラクター制作ツールも対象です。将来のモデルへのコンテキストと追加調査の引き継ぎに使えます。

## 収録データ

| データ | 内容 | 機械可読 |
| --- | --- | --- |
| 制作系リポジトリ（分野別ページ） | 固定コミット・入出力・根拠つきの詳細調査。115件 / 18分野 | [catalog.jsonl](catalog.jsonl) |
| [会話できるアニメ系AIキャラクター](categories/companion.md) | Live2D/VRM/AI VTuberなど60件。一覧レベルの記録 | [companion-catalog.jsonl](companion-catalog.jsonl) |
| [公式コード＋公開重みのある研究](research/papers.md) | SIGGRAPH 2026ほか87件、12分野 | [research/papers.jsonl](research/papers.jsonl) |
| [タスク別アニメ系SOTAモデル・リポジトリ](models/anime-task-sota.md) | HFタスク別の最良モデル（108タスク・最良あり82）と制作工程別の代表リポジトリ193件（2026-10-01） | [sota-catalog.jsonl](sota-catalog.jsonl) |

AIエージェントは先に [AGENTS.md](AGENTS.md) と [llms.txt](llms.txt) を読むと、質問別に必要なファイルだけを取得できます。

## 読み方

| 目的 | ファイル |
| --- | --- |
| 全件の日本語一覧 | [catalog.md](catalog.md) |
| 分野横断の深掘り比較・優先候補・公開範囲 | [詳細リサーチ](research/deep-dive-2026-09-09.md) |
| GitHub以外のアニメ画像モデル4系統 | [モデル比較](models/anime-models.md) / [モデル正本JSON](model-catalog.json) / [JSONL](model-catalog.jsonl) |
| タスク別のアニメ系最良モデル（開発で迷ったとき） | [一覧](models/anime-task-sota.md) / [短縮版](SOTA_CONTEXT.md) / [リポジトリ全体像](models/anime-repositories.md) / [正本JSON](sota-catalog.json) |
| モデルに一括で渡す短縮資料 | [MODEL_CONTEXT.md](MODEL_CONTEXT.md) |
| 入出力・環境・依存・根拠・モデル配布・コミットの正本 | [catalog.json](catalog.json) |
| RAGなどで1件ずつ取り込む | [catalog.jsonl](catalog.jsonl) |
| 表計算・絞り込み | [catalog.csv](catalog.csv) |
| 制作目的に沿った組み合わせ | [WORKFLOWS.md](WORKFLOWS.md) |
| 調査範囲・追加調査の方向 | [RESEARCH_NOTES.md](RESEARCH_NOTES.md) |
| 追記ルールとデータ仕様 | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 保留・未掲載候補 | [reviewed-not-included.json](reviewed-not-included.json) |

## 分野から探す

| 分野 | 件数 | 掲載項目 |
| --- | --- | --- |
| [漫画・イラスト編集](categories/manga.md) | 7 | ai-comic-factory、DiffSensei、krita、manga-editor-desu、MangaNinja、OpenKoma、StoryDiffusion |
| [シナリオ・キャラクター・絵コンテ](categories/story.md) | 4 | BlueFish、ink、SillyTavern、Yarn Spinner |
| [ゲーム・ノベル・スプライト](categories/game.md) | 10 | ControlTile、Godot、LDtk、OpenGame、Pixelorama、PNGAL、RenPy、sprite-maker、Terrain Diffusion、Tiled |
| [アニメ制作・中割り・彩色・リップシンク](categories/animation.md) | 8 | AniDoc、AnimeColor、BasicPBC、ECCV2022-RIFE、LatentSync、opentoonz、ToonComposer、ToonCrafter |
| [2Dキャラクター・自動リギング](categories/rig2d.md) | 3 | Anime2.5DRig、PuppetLoom、stretchystudio |
| [レイヤー分解](categories/layer.md) | 4 | ComfyUI-See-through、Qwen-Image-Layered、see-through、Stable Layers |
| [画像生成・編集・切り抜き](categories/image.md) | 4 | anime-segmentation、krita-ai-diffusion、Qwen-Image、Z-Image |
| [動画生成](categories/video.md) | 7 | FramePack、Index-anisora、LTX-2、LTX-Video、SCAIL-2、Wan-Move、Wan2.2 |
| [3D生成・モデリング・リギング](categories/3d.md) | 10 | AniGen、Blender、Hunyuan3D-2.1、Pixal3D、Puppeteer、Roblox Cube / CubePart、SkinTokens、SQuadGen、TRELLIS.2、UniRig |
| [TTS・キャラクター音声](categories/tts.md) | 9 | CosyVoice、F5-TTS、fish-speech、GPT-SoVITS、IndexTTS、Qwen3-TTS、RVC WebUI、Style-Bert-VITS2、voicevox |
| [ASMR・効果音・環境音](categories/sound.md) | 9 | ASMRify、Audacity、Binaural Speech Synthesis、ControlFoley、FoleyCrafter、MMAudio、stable-audio-tools、Steam Audio、Ultimate Vocal Remover |
| [音楽・歌声合成](categories/music.md) | 6 | ACE-Step-1.5、Basic Pitch、DiffSinger、OpenUtau、SOFA、YuE2 |
| [VTuber・AIキャラクター・VRM](categories/vtuber.md) | 10 | AIRI、babylon-mmd、inochi-creator、OBS Studio、Open-LLM-VTuber、OpenSeeFace、PersonaLive、three-vrm、UniVRM、VTubeStudio |
| [制作ワークフロー・追加学習](categories/workflow.md) | 5 | ComfyUI、ComfyUI-WanVideoWrapper、DiffSynth-Studio、musubi-tuner、sd-scripts |
| [字幕・翻訳・ローカライズ](categories/localization.md) | 5 | ASMR Dubber、Manga OCR、manga-image-translator、mokuro、VoiceTransl |
| [モーション・身体演技](categories/motion.md) | 5 | ARDY、EchoAvatar、Gelina、HY-Motion 1.0、R-DMesh |
| [VFX・材質・ベクター演出](categories/vfx.md) | 6 | Effekseer、GenCompositor、Material Maker、OmniLottie、VfxDB、VFXMaster |
| [絵コンテ・制作管理・評価](categories/production.md) | 3 | Kitsu、Storyboarder、StyleID |

## 最初に見る候補

- **一枚絵から動くキャラ**: See-through → Anime2.5DRig / PuppetLoom。ゲーム素材ならPNGALも比較。
- **漫画・画像**: DiffSensei / StoryDiffusionでキャラ参照、Manga Editor Desu / Kritaで原稿編集。Anima等は別のモデル一覧へ。
- **アニメ彩色**: BasicPBC / AniDoc / AnimeColor。中間フレームはToonCrafter、アニメ特化動画はIndex-anisora。
- **音声・キャラソング**: IndexTTS 2.5 / Qwen3-TTS / GPT-SoVITS、歌声編集にはOpenUtau / DiffSinger、楽曲案にはACE-Step / YuE2。
- **3Dキャラ**: AniGenの形状・リグ同時生成、Pixal3Dの多視点入力、既存メッシュにはSkinTokens、手直しにはBlender。
- **動画と音・ASMR制作**: LTX-2 / Wan2.2、効果音にはControlFoley / MMAudio。空間音響はSteam Audio、翻訳制作はASMR Dubber。
- **ゲーム・周辺制作**: OpenGame / Godot / RenPy、マップにはTiled / LDtk、効果にはEffekseer、制作管理にはKitsu。
- **AIキャラクター**: AIRI / Open-LLM-VTuber。VTube Studioへの接続は公式API資料。

上記は制作工程から選んだ編集者の候補で、接続実行・品質比較を実施したランキングではありません。各項目の制約は分野別ページへ記録しています。

## モデルへの渡し方

MODEL_CONTEXT.mdを添付し、例えば次のように依頼できます。

> この資料を参考に、Windows・VRAM 12GBで、漫画の立ち絵と音声付き短編ノベルを制作する工程を比較してください。確認日と未検証事項を保持し、導入前に公式情報を再確認してください。

分野を絞る場合はcategories/の対応ページ、機械検索にはcatalog.jsonlを使用します。id・sources・checked_on・code_revisionを保持してください。

## 更新と検証

Python標準ライブラリだけで再生成できます。

```sh
python3 scripts/export.py
python3 scripts/export.py --check
python3 scripts/validate.py
```

catalog.jsonを正本として、一覧・CSV・JSONL・分野別詳細・モデル用資料を同期します。最初のメトリクスは[data/github-snapshot-2026-09-09.json](data/github-snapshot-2026-09-09.json)に保存しています。更新時は新しいスナップショットを追加してください。

## 参考と公開条件の扱い

研究コレクション（[research/papers.md](research/papers.md)）の日本語要約・構造化データ・確認根拠を残す構成を参考にしました。本カタログは研究、制作アプリ、連携実装、API文書を含むため、全件に独自の学習済み重みを要求しません。

コード・重み・音声ライブラリ・キャラ素材の条件は個別です。商用利用可否は独立して判定していません。PuppetLoomはLICENSE/NOTICEと中国語READMEにAGPL表記、英語・日本語READMEにApache表記が残る不一致を確認しました。モデルカード本文の追加条件も別途記録しています。第三者のコードやモデル本体は収録していません。

## 深掘り版の収録範囲

全115件に制作での用途、入口候補、次の検証項目、GitHub Release情報を追加しました。別枠で4系統のアニメ画像モデルを収録。ASMR専用モデル等の公開範囲が不明な候補は保留に残しています。

[全件再確認時のスナップショット](data/github-snapshot-2026-09-09-deep.json) · [選択した本文の確認記録](data/source-checks-2026-09-09.json) · [モデル配布の確認記録](data/model-hub-snapshot-2026-09-09.json)
