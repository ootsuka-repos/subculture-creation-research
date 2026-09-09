# 制作目的から組み合わせる

以下は公式に説明された入出力に基づく**編集者の工程案**です。当カタログで接続・推論・作品制作を実行したものではありません。フォーマット変換、パーツ分け、手直しが必要になる場合があります。

| 作りたいもの | 工程案 | 確認する点・詳細 |
| --- | --- | --- |
| 動く2Dキャラ | 一枚絵 → See-through → PSD → Anime2.5DRig / PuppetLoom / Stretchy Studio | 分解と自動リギングは別。レイヤー構造と不足表情を確認。[分解](categories/layer.md)・[リグ](categories/rig2d.md) |
| ノベルゲーム | シナリオ → 画像・音声制作 → PNGAL等で立ち絵 → Ren’Pyへ組み込み | 画像形式・音声長・ループ・ゲーム内制御を確認。[ゲーム](categories/game.md)・[TTS](categories/tts.md) |
| 漫画 | キャラ設定 → Krita / Krita AI Diffusionで素材 → Manga Editor Desu / OpenKomaでコマ編集 | キャラの一貫性と文字・コマ割りは人の確認が必要。[漫画](categories/manga.md)・[画像](categories/image.md) |
| 短編アニメ | 絵コンテ・原画 → ToonComposer / Wan2.2 / SCAIL-2等を目的別選択 → 編集 | 中割り・画像から動画・動作転送は入力条件が異なる。[アニメ](categories/animation.md)・[動画](categories/video.md) |
| 3Dキャラ・小物 | 画像 → TRELLIS.2 / Hunyuan3D-2.1 → Blenderで修正 → 必要ならSkinTokens | トポロジー・材質・リグ・ゲーム用最適化は個別工程。[3D](categories/3d.md) |
| AI VTuber | キャラ素材 → AIRI / Open-LLM-VTuber → LLM・ASR・TTSの接続 | キャラ制作と会話システムを区別。表示形式・遅延を検証。[VTuber](categories/vtuber.md) |
| 音声付き映像 | LTX-2の音声動画生成、または映像 → MMAudio / FoleyCrafter | セリフTTSと効果音は別。映像と音の同期を検証。[動画](categories/video.md)・[効果音](categories/sound.md) |
| ASMR風音声作品 | 台本 → TTSまたは録音 → ASMRify等で加工 → 編集・試聴 | 声の生成と音響加工は別。ASMR専用品質や効果を保証しない。[音声](categories/sound.md) |
| キャラソング | 歌詞・楽曲案 → ACE-Stepで楽曲試作、または音符・歌詞 → OpenUtau / DiffSinger | 自動楽曲生成と音符に沿った歌唱を区別。[音楽](categories/music.md) |
| 翻訳版・字幕版 | 原稿画像 → Manga Image Translator、音声・動画 → VoiceTransl | OCR、翻訳、組版、字幕タイミングを確認。[ローカライズ](categories/localization.md) |
| 独自画風・キャラの学習 | 素材整理 → musubi-tuner → 対応モデルのLoRA → ComfyUI等で利用 | 基盤モデルの版と学習・推論双方の対応を確認。[制作ワークフロー](categories/workflow.md) |

一枚絵→See-through→対応リグツールの接続は各公式READMEで説明があります。他の工程案は入出力からの編集者の推論を含み、公式に一括動作を保証された構成ではありません。
