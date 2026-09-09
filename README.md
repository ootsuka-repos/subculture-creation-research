# サブカルコンテンツ制作リサーチ

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

漫画・ゲーム・アニメ・3D・ASMR／音声・TTS・画像生成・動画生成・VTuberに加え、歌声合成、シナリオ、リギング、翻訳、追加学習などを集約しています。AIを使わない二次元・キャラクター制作ツールも対象です。将来のモデルへのコンテキストと追加調査の引き継ぎに使えます。

## 読み方

| 目的 | ファイル |
| --- | --- |
| 全件の日本語一覧 | [catalog.md](catalog.md) |
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
| [漫画・イラスト編集](categories/manga.md) | 4 | ai-comic-factory、krita、manga-editor-desu、OpenKoma |
| [シナリオ・キャラクター・絵コンテ](categories/story.md) | 2 | BlueFish、SillyTavern |
| [ゲーム・ノベル・スプライト](categories/game.md) | 5 | Godot、Pixelorama、PNGAL、RenPy、sprite-maker |
| [アニメ制作・中割り・彩色・リップシンク](categories/animation.md) | 4 | ECCV2022-RIFE、LatentSync、opentoonz、ToonComposer |
| [2Dキャラクター・自動リギング](categories/rig2d.md) | 3 | Anime2.5DRig、PuppetLoom、stretchystudio |
| [レイヤー分解](categories/layer.md) | 3 | ComfyUI-See-through、Qwen-Image-Layered、see-through |
| [画像生成・編集・切り抜き](categories/image.md) | 4 | anime-segmentation、krita-ai-diffusion、Qwen-Image、Z-Image |
| [動画生成](categories/video.md) | 4 | LTX-2、LTX-Video、SCAIL-2、Wan2.2 |
| [3D生成・モデリング・リギング](categories/3d.md) | 5 | Blender、Hunyuan3D-2.1、SkinTokens、TRELLIS.2、UniRig |
| [TTS・キャラクター音声](categories/tts.md) | 5 | fish-speech、GPT-SoVITS、Qwen3-TTS、Style-Bert-VITS2、voicevox |
| [ASMR・効果音・環境音](categories/sound.md) | 4 | ASMRify、FoleyCrafter、MMAudio、stable-audio-tools |
| [音楽・歌声合成](categories/music.md) | 3 | ACE-Step-1.5、DiffSinger、OpenUtau |
| [VTuber・AIキャラクター・VRM](categories/vtuber.md) | 5 | AIRI、inochi-creator、Open-LLM-VTuber、UniVRM、VTubeStudio |
| [制作ワークフロー・追加学習](categories/workflow.md) | 3 | ComfyUI、ComfyUI-WanVideoWrapper、musubi-tuner |
| [字幕・翻訳・ローカライズ](categories/localization.md) | 2 | manga-image-translator、VoiceTransl |

## 最初に見る候補

- **一枚絵から動くキャラ**: See-through → Anime2.5DRig / PuppetLoom。ゲーム素材ならPNGALも比較。
- **漫画**: Manga Editor Desuでコマ・吹き出しを編集、Krita + Krita AI Diffusionで素材を制作。
- **音声・キャラソング**: Qwen3-TTS / GPT-SoVITS、歌声編集にはOpenUtau / DiffSinger、楽曲生成にはACE-Step。
- **3Dキャラ**: TRELLIS.2 / Hunyuan3D-2.1、リグにはSkinTokens、手直しにはBlender。
- **動画と音**: LTX-2 / Wan2.2、別工程で効果音を付ける場合はMMAudio / FoleyCrafter。
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

[entertainment-ai-2026-code-models](https://github.com/ootsuka-repos/entertainment-ai-2026-code-models)の日本語要約・構造化データ・確認根拠を残す構成を参考にしました。本カタログは研究、制作アプリ、連携実装、API文書を含むため、全件に独自の学習済み重みを要求しません。

コード・重み・音声ライブラリ・キャラ素材の条件は個別です。商用利用可否は独立して判定していません。PuppetLoomのREADME表記とGitHubの自動ライセンス判定には不一致があり、要再確認として残しています。第三者のコードやモデル本体は収録していません。
