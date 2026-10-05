# 字幕・翻訳・ローカライズ

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-05。**175件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ASMR Dubber](https://github.com/EveningStudy/asmr-dubber) · [詳細](#asmr-dubber) | 日本語・英語の音声や動画を、校正可能な字幕・中国語吹替・二言語音声へ変換する制作ツール。 | AI連携 / 小規模・制作連携候補 | 226 / 2026-10-05 |
| [Manga OCR](https://github.com/kha-white/manga-ocr) · [詳細](#manga-ocr) | 日本語漫画の縦書き・横書き・ルビ付き文字を認識する。 | AIモデル・学習 / モデル・研究候補 | 2,798 / 2026-07-19 |
| [manga-image-translator](https://github.com/zyddnys/manga-image-translator) · [詳細](#manga-image-translator) | 画像内の文字を検出・認識・翻訳し、元の文字を修復して訳文を組版する。 | AIモデル・学習 / 比較・既存工程の参考 | 10,478 / 2026-09-25 |
| [mokuro](https://github.com/kha-white/mokuro) · [詳細](#mokuro) | 漫画ページの文字位置とOCR結果をまとめ、選択可能なテキストとして閲覧できる形式へ変換。 | AI連携 / 連携・制作ツール候補 | 1,739 / 2026-07-20 |
| [VoiceTransl](https://github.com/shinnpuru/VoiceTransl) · [詳細](#voicetransl) | 音声認識、字幕翻訳、字幕と動画の処理を組み合わせる。 | AI連携 / 連携の評価候補 | 1,300 / 2026-10-05 |
| [xianscan-rust](https://github.com/ArbenApura/xianscan-rust) · [詳細](#xianscan-rust) | 漫画・韓漫・国漫向けのローカル完結型翻訳スタジオ。吹き出し検出、多言語OCR、LLM翻訳、LaMaによるインペイント、組版までを単体バイナリで実行する。 | AIモデル・学習 / 更新が活発な実装候補 | 78 / 2026-10-03 |
| [BallonsTranslator-Pro](https://github.com/thomaswantstobeaskeleton/BallonsTranslator-Pro) · [詳細](#ballonstranslator-pro) | BallonsTranslatorを元にした漫画・コミック翻訳ツールキットで、検出・OCR・翻訳・インペイント・植字を組み替え可能なモジュール群で処理する。 | AIモデル・学習 / 活発・候補 | 96 / 2026-07-31 |
| [CarrotMangaTranslator](https://github.com/ucx0204/CarrotMangaTranslator) · [詳細](#carrotmangatranslator) | 漫画原稿のOCR→翻訳→原文消去→植字・検品→出力を扱うデスクトップアプリ。局所GemmaやOpenAI互換APIで翻訳する。 | AIモデル・学習 / 活発・候補 | 82 / 2026-10-05 |
| [Kites](https://github.com/Unheat/Kites) · [詳細](#kites) | ブラウザ拡張として動作し、WebGPU上でOCR・インペイント・翻訳を行って漫画をその場で翻訳表示するツール。 | AIモデル・学習 / 初期評価候補 | 30 / 2026-10-04 |
| [lumina](https://github.com/lumina-tl/lumina) · [詳細](#lumina) | 漫画・マンファ・マンファ翻訳の無料デスクトップアプリ。テキスト検出・OCR・翻訳・インペイント・組版の全工程を自動化しつつ、各結果を手で修正できる。 | AIモデル・学習 / 活発・候補 | 19 / 2026-09-22 |
| [yakuyomi-engine](https://github.com/joyeli/yakuyomi-engine) · [詳細](#yakuyomi-engine) | 端末上で動く漫画翻訳エンジン。検出・OCR・文字消去をNCNNでCPU実行し、翻訳のみネットワークLLMに投げる。読み手アプリYakuyomiに組み込まれる。 | AIモデル・学習 / 活発・候補 | 7 / 2026-10-05 |
| [translate-manga-br](https://github.com/marco0antonio0/translate-manga-br) · [詳細](#translate-manga-br) | ローカルファーストの漫画翻訳フルスタックアプリ。YOLOで吹き出し検出、PaddleOCRでOCR、翻訳、編集可能オーバーレイ付きリーダーまでを1本で提供する。 | AIモデル・学習 / 小規模・初期評価候補 | 31 / 2026-09-29 |
| [LingoVeil](https://github.com/Gerald-Ha/LingoVeil) · [詳細](#lingoveil) | 漫画・コミック向けのセルフホスト翻訳ツール。画像内のテキストを検出・翻訳し、翻訳ビューで読める。ブックマークや読書進捗も保持する。 | AIモデル・学習 / 小規模・初期評価候補 | 5 / 2026-09-30 |
| [OverTranslate](https://github.com/Hon-Lu/OverTranslate) · [詳細](#overtranslate) | Windows向けの画面翻訳ツール。スクリーンショット翻訳・リアルタイム翻訳・取詞翻訳・快速翻訳・文字翻訳の5機能を持ち、認識した訳文を元の画面上にそのまま重ねて表示する。 | AIは任意 / 活発・実用候補 | 97 / 2026-10-05 |
| [FumetoReaderPlus](https://github.com/fumetodev/FumetoReaderPlus) · [詳細](#fumetoreaderplus) | Android向け漫画リーダー。吹き出し検出・OCR・漫画向けLLM翻訳・風船内への再レタリングを端末上で行い、タップで原文に戻せる。 | AIモデル・学習 / 活発な候補 | 5 / 2026-10-04 |
| [Solar-Manga-Translator](https://github.com/soluna/Solar-Manga-Translator) · [詳細](#solar-manga-translator) | 中国語話者向けのローカル漫画翻訳・校正ワークベンチ。OCR、AI翻訳、擦字補修、自動嵌字、人手校正、導出を一流程にまとめる。 | AIモデル・学習 / 小規模・初期評価候補 | 4 / 2026-09-30 |
| [UGTLive](https://github.com/SethRobinson/UGTLive) · [詳細](#ugtlive) | Windows向けGUIツールで、画面や画像の文字を「ライブ」でOCR・翻訳する。縦書き日本語の漫画読み上げ、PDF/CBZ/画像の一括変換、音声読み上げ、リアルタイム字幕にも対応する。 | AIモデル・学習 / 稼働中・実運用候補 | 117 / 2026-09-03 |
| [manga-translator](https://github.com/cameronkinsella/manga-translator) · [詳細](#manga-translator) | Gio製GUIのデスクトップアプリで、画像内のテキストをOCRして翻訳する。検出した全テキストに色付きボックスを表示し、クリックで原文と訳文を確認・コピーできる。 | AI連携 / 稼働中 | 153 / 2026-02-01 |
| [AutoScanlate-AI](https://github.com/P4ST4S/AutoScanlate-AI) · [詳細](#autoscanlate-ai) | 完全ローカル・GPU加速の漫画翻訳パイプライン。YOLOv8で吹き出し検出、MangaOCRで縦書きOCR、Qwen 2.5 7Bで文脈翻訳、マスク付きインペイントと段組みで元画像に描き戻す。Goバックエンド+Next.js UI+Pythonワーカーの構成。 | AIモデル・学習 / 小規模・初期評価候補 | 35 / 2026-09-07 |

<a id="asmr-dubber"></a>

## ASMR Dubber

日本語・英語の音声や動画を、校正可能な字幕・中国語吹替・二言語音声へ変換する制作ツール。

- **リポジトリ**: https://github.com/EveningStudy/asmr-dubber
- **分類**: pipeline / AI連携 / 小規模・制作連携候補
- **入力**: 音声・動画、原文字幕、台本、声の参照
- **出力**: 字幕、中国語吹替、原声を残した二言語音声・ミックス
- **環境**: Windows10/11の配布ZIP、Linux x86_64/WSL2。ARM64/macOSは対象外。GPU要件は選択バックエンドごと。
- **依存**: Parakeet/Kotoba/Faster-Whisper等のASR、IndexTTS2/2.5または音声API、翻訳API、FFmpeg等。
- **制約・未確認**: 主な方向は日英から中国語への制作。ASMR専用生成モデルではない。IndexTTS2.5は任意追加で、基本パッケージへの同梱と混同しない。
- **編集者評価**: ASMR作品の翻訳・台本校正・吹替・混音までを扱う具体的な連携候補。
- **メトリクス**: ★226、fork 14、作成 2026-07-23、最終push 2026-10-05T19:38:15Z、archived=False
- **確認**: 2026-09-09 / コミット `bc088faceec743d51f2914e9f7efd98d7b19d9e3`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/EveningStudy/asmr-dubber/tree/bc088faceec743d51f2914e9f7efd98d7b19d9e3)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/EveningStudy/asmr-dubber/blob/bc088faceec743d51f2914e9f7efd98d7b19d9e3/README.md) / [GitHub API](https://api.github.com/repos/EveningStudy/asmr-dubber) / [固定ツリー](https://github.com/EveningStudy/asmr-dubber/tree/bc088faceec743d51f2914e9f7efd98d7b19d9e3)

### 制作に使う際の検討

ASMR作品の翻訳・台本校正・吹替・混音までを扱う具体的な連携候補。 生成音質だけでなく字幕と音声の手修正・再生成のしやすさを比較する。

**次に確かめること（実施前）**: 自作3分音声で小声・無音・息を含む字幕を校正し、中国語台詞の長さ、原声との重なり、キャッシュ再利用を確認する。

**利用条件の確認メモ**: コードはREADMEでMIT。モデル・サービス・入力作品・生成内容の条件は別と明記。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/asmr_dubber/cli.py](https://github.com/EveningStudy/asmr-dubber/blob/bc088faceec743d51f2914e9f7efd98d7b19d9e3/src/asmr_dubber/cli.py)

**最新GitHub Release**: [v2.0.1](https://github.com/EveningStudy/asmr-dubber/releases/tag/v2.0.1) / 2026-10-05T19:17:22Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-07T16:29:46Z。公式READMEと固定ファイル構成の確認。バックエンドの起動・生成・翻訳品質は未検証。

関連: documented_integration → index-tts（公式説明に基づく関係、接続実行は未検証）

<a id="manga-ocr"></a>

## Manga OCR

日本語漫画の縦書き・横書き・ルビ付き文字を認識する。

- **リポジトリ**: https://github.com/kha-white/manga-ocr
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 吹き出し等の文字画像
- **出力**: 日本語テキスト
- **環境**: Python3.9以上と対応PyTorch。CPU/GPU経路。
- **依存**: manga-ocr-base、Transformers、形態素関連依存
- **制約・未確認**: ページ内の文字領域検出や翻訳・組版は別工程。読み取り品質は素材依存。
- **編集者評価**: 漫画の校正・翻訳素材抽出を構成するOCR部品。
- **メトリクス**: ★2,798、fork 142、作成 2022-01-15、最終push 2026-07-19T08:43:43Z、archived=False
- **確認**: 2026-09-09 / コミット `c333b5d36e88d539d6b040b4c4cf90ad5ecd4f69`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/kha-white/manga-ocr/tree/c333b5d36e88d539d6b040b4c4cf90ad5ecd4f69)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/kha-white/manga-ocr/blob/c333b5d36e88d539d6b040b4c4cf90ad5ecd4f69/README.md) / [GitHub API](https://api.github.com/repos/kha-white/manga-ocr) / [固定ツリー](https://github.com/kha-white/manga-ocr/tree/c333b5d36e88d539d6b040b4c4cf90ad5ecd4f69)

### 制作に使う際の検討

漫画の校正・翻訳素材抽出を構成するOCR部品。

**次に確かめること（実施前）**: 縦書き、ルビ、装飾フォント、擬音を分けて文字誤りと脱落を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [manga_ocr/run.py](https://github.com/kha-white/manga-ocr/blob/c333b5d36e88d539d6b040b4c4cf90ad5ecd4f69/manga_ocr/run.py) / [manga_ocr_dev/data/generate_backgrounds.py](https://github.com/kha-white/manga-ocr/blob/c333b5d36e88d539d6b040b4c4cf90ad5ecd4f69/manga_ocr_dev/data/generate_backgrounds.py)

**最新GitHub Release**: [v0.1.16](https://github.com/kha-white/manga-ocr/releases/tag/v0.1.16) / 2026-07-19T08:44:54Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-19T08:35:53Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [kha-white/manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) — file_listing_checked、確認日 2026-09-09、revision `aa6573bd10b0d446cbf622e29c3e084914df9741`。代表ファイル: `pytorch_model.bin`。gated=False。

<a id="manga-image-translator"></a>

## manga-image-translator

画像内の文字を検出・認識・翻訳し、元の文字を修復して訳文を組版する。

- **リポジトリ**: https://github.com/zyddnys/manga-image-translator
- **分類**: pipeline / AIモデル・学習 / 比較・既存工程の参考
- **入力**: 漫画・イラスト画像
- **出力**: 文字除去・翻訳・組版後の画像
- **環境**: Python、OCR・修復モデル、翻訳バックエンド。
- **依存**: OCR、インペイント、翻訳モデルまたはAPI
- **制約・未確認**: 公式説明に公開Webデモの停止記載あり。縦書き・擬音・レイアウト保持の品質は素材で検証が必要。
- **編集者評価**: 漫画のローカライズと文字処理工程の技術候補。
- **メトリクス**: ★10,478、fork 1,068、作成 2021-02-18、最終push 2026-09-25T02:45:14Z、archived=False
- **確認**: 2026-09-09 / コミット `95227a2bb0fd306cd4f0c104d57284026f991b3a`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/zyddnys/manga-image-translator/tree/95227a2bb0fd306cd4f0c104d57284026f991b3a)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/zyddnys/manga-image-translator/blob/95227a2bb0fd306cd4f0c104d57284026f991b3a/README.md) / [GitHub API](https://api.github.com/repos/zyddnys/manga-image-translator) / [固定ツリー](https://github.com/zyddnys/manga-image-translator/tree/95227a2bb0fd306cd4f0c104d57284026f991b3a)

### 制作に使う際の検討

文字検出・除去・翻訳・組版の複合工程。各段階の中間結果を保存できる構成が評価しやすい。

**次に確かめること（実施前）**: 縦書き、ルビ、吹き出し外の文字、擬音を含む自作ページで誤りを段階ごとに点検する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [manga_translator/__main__.py](https://github.com/zyddnys/manga-image-translator/blob/95227a2bb0fd306cd4f0c104d57284026f991b3a/manga_translator/__main__.py)

**最新GitHub Release**: [beta-0.3](https://github.com/zyddnys/manga-image-translator/releases/tag/beta-0.3) / 2022-04-23T17:55:18Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-20T07:17:48Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="mokuro"></a>

## mokuro

漫画ページの文字位置とOCR結果をまとめ、選択可能なテキストとして閲覧できる形式へ変換。

- **リポジトリ**: https://github.com/kha-white/mokuro
- **分類**: pipeline / AI連携 / 連携・制作ツール候補
- **入力**: 漫画ページ画像
- **出力**: .mokuroデータ、互換用HTML
- **環境**: Python3.10以上、事前処理はオフライン。
- **依存**: comic-text-detector、manga-ocr、対応Webリーダー
- **制約・未確認**: 主目的は読書支援。ここでは自作漫画の校正・テキスト抽出用の前処理として掲載。翻訳器ではない。
- **編集者評価**: ページ単位で位置付き文字を得るため、OCR単体より制作後の校正に接続しやすい。
- **メトリクス**: ★1,739、fork 121、作成 2022-04-16、最終push 2026-07-20T07:18:29Z、archived=False
- **確認**: 2026-09-09 / コミット `9f79b1281066f953ec6e5d1e7086c401fa8da159`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/kha-white/mokuro/tree/9f79b1281066f953ec6e5d1e7086c401fa8da159)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/kha-white/mokuro/blob/9f79b1281066f953ec6e5d1e7086c401fa8da159/README.md) / [GitHub API](https://api.github.com/repos/kha-white/mokuro) / [固定ツリー](https://github.com/kha-white/mokuro/tree/9f79b1281066f953ec6e5d1e7086c401fa8da159)

### 制作に使う際の検討

ページ単位で位置付き文字を得るため、OCR単体より制作後の校正に接続しやすい。

**次に確かめること（実施前）**: 自作1話で読み順・文字位置・誤認識を点検し、翻訳工程へ取り出せるか確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [mokuro/run.py](https://github.com/kha-white/mokuro/blob/9f79b1281066f953ec6e5d1e7086c401fa8da159/mokuro/run.py) / [mokuro/__init__.py](https://github.com/kha-white/mokuro/blob/9f79b1281066f953ec6e5d1e7086c401fa8da159/mokuro/__init__.py)

**最新GitHub Release**: [v0.2.5](https://github.com/kha-white/mokuro/releases/tag/v0.2.5) / 2026-07-20T07:19:36Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-19T12:36:41Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: uses → manga-ocr（公式説明に基づく関係、接続実行は未検証）

<a id="voicetransl"></a>

## VoiceTransl

音声認識、字幕翻訳、字幕と動画の処理を組み合わせる。

- **リポジトリ**: https://github.com/shinnpuru/VoiceTransl
- **分類**: pipeline / AI連携 / 連携の評価候補
- **入力**: 音声、動画、字幕
- **出力**: 文字起こし、翻訳字幕、動画
- **環境**: 音声認識モデルと翻訳用のローカルモデルまたはAPI。
- **依存**: Whisper系、翻訳LLM、FFmpeg等
- **制約・未確認**: 同名forkと公式配布元を区別。声の生成機能ではない。
- **編集者評価**: ASMR・キャラ音声・映像の字幕付けとローカライズ候補。
- **メトリクス**: ★1,300、fork 53、作成 2024-03-15、最終push 2026-10-05T04:31:39Z、archived=False
- **確認**: 2026-09-09 / コミット `b5f7e5038763aeb3420ac872c0bd191112f92227`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/shinnpuru/VoiceTransl/tree/b5f7e5038763aeb3420ac872c0bd191112f92227)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/shinnpuru/VoiceTransl/blob/b5f7e5038763aeb3420ac872c0bd191112f92227/README.md) / [GitHub API](https://api.github.com/repos/shinnpuru/VoiceTransl) / [固定ツリー](https://github.com/shinnpuru/VoiceTransl/tree/b5f7e5038763aeb3420ac872c0bd191112f92227)

### 制作に使う際の検討

台詞や映像の字幕・翻訳をまとめる制作支援。音声生成とは別のローカライズ工程。

**次に確かめること（実施前）**: 日本語ASR、固有名詞辞書、字幕タイミング、翻訳改訂、動画再出力を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [app.py](https://github.com/shinnpuru/VoiceTransl/blob/b5f7e5038763aeb3420ac872c0bd191112f92227/app.py) / [i18n.py](https://github.com/shinnpuru/VoiceTransl/blob/b5f7e5038763aeb3420ac872c0bd191112f92227/i18n.py)

**最新GitHub Release**: [v1.30](https://github.com/shinnpuru/VoiceTransl/releases/tag/v1.30) / 2026-08-28T13:20:38Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-28T14:44:14Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="xianscan-rust"></a>

## xianscan-rust

漫画・韓漫・国漫向けのローカル完結型翻訳スタジオ。吹き出し検出、多言語OCR、LLM翻訳、LaMaによるインペイント、組版までを単体バイナリで実行する。

- **リポジトリ**: https://github.com/ArbenApura/xianscan-rust
- **分類**: pipeline / AIモデル・学習 / 更新が活発な実装候補
- **入力**: 漫画・ウェブトゥーンの画像、フォルダ、ブラウザ拡張で取り込んだページ
- **出力**: 翻訳・組版済みページ、Mihon/Tachiyomi拡張で読めるチャプター
- **環境**: x86_64(AVX2)またはApple Silicon、RAM 8GB以上。ソースからはRust 1.88+。GPUは任意。
- **依存**: 内蔵のONNXモデル/Skia。翻訳にOllama・LM Studio等のローカルLLMやGemini/OpenAI等のクラウドAPIを任意使用。
- **制約・未確認**: 翻訳品質やOCR精度はREADMEの主張で未検証。GPU無しではCPU推論となる。
- **編集者評価**: 検出→OCR→翻訳→インペイント→組版を1クリックで自動化し、ONNXモデルとUIを内蔵した単体実行ファイルで動かせる点が実用的。
- **メトリクス**: ★78、fork 13、作成 2026-08-16、最終push 2026-10-03T19:54:18Z、archived=False
- **確認**: 2026-10-01 / コミット `075d36f359cdcad1d08ea88d2f4d927640789c26`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/ArbenApura/xianscan-rust/tree/075d36f359cdcad1d08ea88d2f4d927640789c26)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ArbenApura/xianscan-rust/blob/075d36f359cdcad1d08ea88d2f4d927640789c26/README.md) / [GitHub API](https://api.github.com/repos/ArbenApura/xianscan-rust) / [固定ツリー](https://github.com/ArbenApura/xianscan-rust/tree/075d36f359cdcad1d08ea88d2f4d927640789c26)

### 制作に使う際の検討

既存の漫画翻訳・組版工程をローカルで自動化したい場合の候補。

**次に確かめること（実施前）**: 実際のページで吹き出し検出・OCR・組版の精度と日本語対応を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [docs-site/src/lib/components/ui/index.ts](https://github.com/ArbenApura/xianscan-rust/blob/075d36f359cdcad1d08ea88d2f4d927640789c26/docs-site/src/lib/components/ui/index.ts) / [src/main.rs](https://github.com/ArbenApura/xianscan-rust/blob/075d36f359cdcad1d08ea88d2f4d927640789c26/src/main.rs) / [web/src/lib/components/ui/index.ts](https://github.com/ArbenApura/xianscan-rust/blob/075d36f359cdcad1d08ea88d2f4d927640789c26/web/src/lib/components/ui/index.ts)

**最新GitHub Release**: [v0.5.0-beta.8](https://github.com/ArbenApura/xianscan-rust/releases/tag/v0.5.0-beta.8) / 2026-09-26T13:56:24Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-29T22:28:44Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="ballonstranslator-pro"></a>

## BallonsTranslator-Pro

BallonsTranslatorを元にした漫画・コミック翻訳ツールキットで、検出・OCR・翻訳・インペイント・植字を組み替え可能なモジュール群で処理する。

- **リポジトリ**: https://github.com/thomaswantstobeaskeleton/BallonsTranslator-Pro
- **分類**: desktop_tool / AIモデル・学習 / 活発・候補
- **入力**: 漫画・コミックの画像、翻訳先言語、各段階のモジュール設定
- **出力**: 翻訳・植字済みの画像、作業データ
- **環境**: Python 3.10+、Windows/macOS/Linux。GPU利用可。
- **依存**: 各種OCR・翻訳・インペイントのモデルやAPIキーは利用者が用意。
- **制約・未確認**: dmMaze/BallonsTranslatorのフォーク。公開時は機械翻訳の明示が要るとREADMEが注意喚起し、人手校正を推奨。
- **編集者評価**: 検出20以上・OCR30以上・翻訳25以上・インペイント15以上のモジュールを組み合わせられる点と、リアルタイム画面翻訳・バッチ処理・ローカルREST APIを備える点が具体的。
- **メトリクス**: ★96、fork 9、作成 2026-02-23、最終push 2026-07-31T00:24:49Z、archived=False
- **確認**: 2026-09-30 / コミット `1cb5af0ca9b87919ffdfe0626167612815baf030`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/thomaswantstobeaskeleton/BallonsTranslator-Pro/tree/1cb5af0ca9b87919ffdfe0626167612815baf030)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/thomaswantstobeaskeleton/BallonsTranslator-Pro/blob/1cb5af0ca9b87919ffdfe0626167612815baf030/README.md) / [GitHub API](https://api.github.com/repos/thomaswantstobeaskeleton/BallonsTranslator-Pro) / [固定ツリー](https://github.com/thomaswantstobeaskeleton/BallonsTranslator-Pro/tree/1cb5af0ca9b87919ffdfe0626167612815baf030)

### 制作に使う際の検討

漫画翻訳の一連の工程をGUIとAPIの両方から回せる。

**次に確かめること（実施前）**: 実際の1話で検出→OCR→翻訳→植字を通し、出力品質と処理時間を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [modules/textdetector/ctd/inference.py](https://github.com/thomaswantstobeaskeleton/BallonsTranslator-Pro/blob/1cb5af0ca9b87919ffdfe0626167612815baf030/modules/textdetector/ctd/inference.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-07-31T00:23:45Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="carrotmangatranslator"></a>

## CarrotMangaTranslator

漫画原稿のOCR→翻訳→原文消去→植字・検品→出力を扱うデスクトップアプリ。局所GemmaやOpenAI互換APIで翻訳する。

- **リポジトリ**: https://github.com/ucx0204/CarrotMangaTranslator
- **分類**: desktop_tool / AIモデル・学習 / 活発・候補
- **入力**: 漫画画像・ZIP/CBZ/RAR/PDF、用語・人物設定
- **出力**: 翻訳済み画像、PSD出力、作業データ
- **環境**: Windows 10/11、またはApple SiliconのmacOS 14以上。モデルとランタイムは別途ダウンロード。
- **依存**: Gemma/OCR/インペイントのモデル、OpenAI互換APIキーなど。
- **制約・未確認**: Intel Mac非対応。初回準備にネット接続と空き容量が必要。
- **編集者評価**: 翻訳エンジン・OCR・原文消去を個別に設定でき、MCP経由で外部AIアプリから編集や出力を依頼できる点が用途に合う。
- **メトリクス**: ★82、fork 16、作成 2026-04-20、最終push 2026-10-05T22:36:04Z、archived=False
- **確認**: 2026-09-30 / コミット `a6454549af83d424dc47d871d76734fb8a33187d`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/ucx0204/CarrotMangaTranslator/tree/a6454549af83d424dc47d871d76734fb8a33187d)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ucx0204/CarrotMangaTranslator/blob/a6454549af83d424dc47d871d76734fb8a33187d/README.md) / [GitHub API](https://api.github.com/repos/ucx0204/CarrotMangaTranslator) / [固定ツリー](https://github.com/ucx0204/CarrotMangaTranslator/tree/a6454549af83d424dc47d871d76734fb8a33187d)

### 制作に使う際の検討

漫画翻訳の制作パイプラインを1アプリで完結させやすい。

**次に確かめること（実施前）**: 1話を読み込み、OCR精度と原文消去・植字の編集しやすさを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [src/main/index.ts](https://github.com/ucx0204/CarrotMangaTranslator/blob/a6454549af83d424dc47d871d76734fb8a33187d/src/main/index.ts) / [src/preload/index.ts](https://github.com/ucx0204/CarrotMangaTranslator/blob/a6454549af83d424dc47d871d76734fb8a33187d/src/preload/index.ts) / [src/renderer/src/main.tsx](https://github.com/ucx0204/CarrotMangaTranslator/blob/a6454549af83d424dc47d871d76734fb8a33187d/src/renderer/src/main.tsx)

**最新GitHub Release**: [v3.2.0](https://github.com/ucx0204/CarrotMangaTranslator/releases/tag/v3.2.0) / 2026-10-05T22:36:05Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-30T11:15:16Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="kites"></a>

## Kites

ブラウザ拡張として動作し、WebGPU上でOCR・インペイント・翻訳を行って漫画をその場で翻訳表示するツール。

- **リポジトリ**: https://github.com/Unheat/Kites
- **分類**: browser_tool / AIモデル・学習 / 初期評価候補
- **入力**: Web上の漫画・コミック画像
- **出力**: 翻訳・植字済みのページ画像
- **環境**: Chrome（Manifest V3）とWebGPU。Chrome Web Storeまたは手動インストール。
- **依存**: ブラウザ、必要に応じて独自APIキー。
- **制約・未確認**: 翻訳はローカルLLM・共有プール・Google翻訳・独自APIから選択。WebGPU環境が前提。
- **編集者評価**: 画像を外部に送らず端末内でOCRと背景修復を行い、内蔵スタジオで修正・書き出しまでできる点が具体的。
- **メトリクス**: ★30、fork 5、作成 2026-07-08、最終push 2026-10-04T17:35:19Z、archived=False
- **確認**: 2026-09-30 / コミット `420898820e9ac2d4e91eede871ce48087c411475`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Unheat/Kites/tree/420898820e9ac2d4e91eede871ce48087c411475)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Unheat/Kites/blob/420898820e9ac2d4e91eede871ce48087c411475/README.md) / [GitHub API](https://api.github.com/repos/Unheat/Kites) / [固定ツリー](https://github.com/Unheat/Kites/tree/420898820e9ac2d4e91eede871ce48087c411475)

### 制作に使う際の検討

ブラウザで読む漫画の下訳・確認作業を軽量化。

**次に確かめること（実施前）**: 対応サイトで実際に翻訳・植字結果と処理速度を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [site/js/main.js](https://github.com/Unheat/Kites/blob/420898820e9ac2d4e91eede871ce48087c411475/site/js/main.js) / [src/background/index.ts](https://github.com/Unheat/Kites/blob/420898820e9ac2d4e91eede871ce48087c411475/src/background/index.ts) / [src/content/index.tsx](https://github.com/Unheat/Kites/blob/420898820e9ac2d4e91eede871ce48087c411475/src/content/index.tsx)

**最新GitHub Release**: [v1.1.1](https://github.com/Unheat/Kites/releases/tag/v1.1.1) / 2026-10-04T17:35:19Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-26T16:09:39Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="lumina"></a>

## lumina

漫画・マンファ・マンファ翻訳の無料デスクトップアプリ。テキスト検出・OCR・翻訳・インペイント・組版の全工程を自動化しつつ、各結果を手で修正できる。

- **リポジトリ**: https://github.com/lumina-tl/lumina
- **分類**: desktop_tool / AIモデル・学習 / 活発・候補
- **入力**: 漫画のページ画像、プロジェクトファイル(.lmi)
- **出力**: 翻訳済み画像(PNG/JPG)、プロジェクトファイル(.lmi)
- **環境**: Electron+Python FastAPIバックエンド。モデルは同梱されず個別DL。CUDA/DirectML/CPU。
- **依存**: ONNX Runtime、翻訳プロバイダのAPIキー、モデルファイル一式
- **制約・未確認**: 翻訳は外部AI APIキーが必要。モデルは自動同梱されず手動配置/DL。
- **編集者評価**: 翻訳だけ外部APIで、検出/OCR/インペイント/組版はローカルONNX実行という切り分けと、工程ごとの編集可能性が制作向き。
- **メトリクス**: ★19、fork 3、作成 2026-08-24、最終push 2026-09-22T01:17:53Z、archived=False
- **確認**: 2026-09-30 / コミット `bfbf042aff4c18290198f65c18f31430cd3f5a06`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/lumina-tl/lumina/tree/bfbf042aff4c18290198f65c18f31430cd3f5a06)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/lumina-tl/lumina/blob/bfbf042aff4c18290198f65c18f31430cd3f5a06/README.md) / [GitHub API](https://api.github.com/repos/lumina-tl/lumina) / [固定ツリー](https://github.com/lumina-tl/lumina/tree/bfbf042aff4c18290198f65c18f31430cd3f5a06)

### 制作に使う際の検討

同人・商業を問わない漫画翻訳ワークフローの中核候補。

**次に確かめること（実施前）**: 日本語漫画数ページで工程別の精度とGPU/CPU速度、モデル配置の手間を計測する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [python/main.py](https://github.com/lumina-tl/lumina/blob/bfbf042aff4c18290198f65c18f31430cd3f5a06/python/main.py) / [src/main/main.ts](https://github.com/lumina-tl/lumina/blob/bfbf042aff4c18290198f65c18f31430cd3f5a06/src/main/main.ts) / [src/renderer/lib/canvas/index.ts](https://github.com/lumina-tl/lumina/blob/bfbf042aff4c18290198f65c18f31430cd3f5a06/src/renderer/lib/canvas/index.ts)

**最新GitHub Release**: [v0.4.0](https://github.com/lumina-tl/lumina/releases/tag/v0.4.0) / 2026-09-13T05:39:34Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-22T01:17:40Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="yakuyomi-engine"></a>

## yakuyomi-engine

端末上で動く漫画翻訳エンジン。検出・OCR・文字消去をNCNNでCPU実行し、翻訳のみネットワークLLMに投げる。読み手アプリYakuyomiに組み込まれる。

- **リポジトリ**: https://github.com/joyeli/yakuyomi-engine
- **分類**: library / AIモデル・学習 / 活発・候補
- **入力**: 漫画ページのビットマップ
- **出力**: 翻訳済みページのビットマップ(translatePage/PageResult)
- **環境**: Kotlin/NCNN。arm64実機。モデルは自分で配置。翻訳は任意のLLM APIキー。
- **依存**: NCNNモデル(DBNet/OCR/AOT-GAN)一式、任意のLLM API
- **制約・未確認**: アプリではなくライブラリ本体。速度優先で画質は天井を取らない。GPU/NPUは使わずCPU実行とREADMEが明記。
- **編集者評価**: スマホでの待ち時間を基準に各段を速度優先で設計しており、ページ間並行処理まで作り込まれている。
- **メトリクス**: ★7、fork 2、作成 2026-06-01、最終push 2026-10-05T21:19:48Z、archived=False
- **確認**: 2026-09-30 / コミット `3d64c43380ff0fd38ead58a35949825ecd9edfcc`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/joyeli/yakuyomi-engine/tree/3d64c43380ff0fd38ead58a35949825ecd9edfcc)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/joyeli/yakuyomi-engine/blob/3d64c43380ff0fd38ead58a35949825ecd9edfcc/README.md) / [GitHub API](https://api.github.com/repos/joyeli/yakuyomi-engine) / [固定ツリー](https://github.com/joyeli/yakuyomi-engine/tree/3d64c43380ff0fd38ead58a35949825ecd9edfcc)

### 制作に使う際の検討

Android読書アプリへの翻訳機能組み込みに。

**次に確かめること（実施前）**: 手持ちページで検出・OCR・文字消去の所要時間と品質、翻訳併走時の挙動を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/joyeli/yakuyomi-engine/blob/3d64c43380ff0fd38ead58a35949825ecd9edfcc/README.md)

**最新GitHub Release**: [models-v5](https://github.com/joyeli/yakuyomi-engine/releases/tag/models-v5) / 2026-09-26T07:14:02Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-30T18:26:08Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="translate-manga-br"></a>

## translate-manga-br

ローカルファーストの漫画翻訳フルスタックアプリ。YOLOで吹き出し検出、PaddleOCRでOCR、翻訳、編集可能オーバーレイ付きリーダーまでを1本で提供する。

- **リポジトリ**: https://github.com/marco0antonio0/translate-manga-br
- **分類**: web_app / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 漫画ページ画像
- **出力**: 翻訳オーバーレイ付きページ、SQLite/ローカルファイル
- **環境**: DockerまたはNode.js/Next.js。AIはCPU実行。翻訳はGoogle翻訳かOpenRouter。
- **依存**: YOLO/PaddleOCRモデル、SQLite、任意の翻訳APIキー
- **制約・未確認**: 翻訳は外部サービスが必要。規模は小さめでAndroidアプリはベータ。
- **編集者評価**: 検出から閲覧までを自前ホストで完結させ、データをstorage/に残す設計が分かりやすい。
- **メトリクス**: ★31、fork 0、作成 2026-05-18、最終push 2026-09-29T02:40:51Z、archived=False
- **確認**: 2026-09-30 / コミット `cb6989b7a978bb3b87f4c6305d972c6d61811b3a`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/marco0antonio0/translate-manga-br/tree/cb6989b7a978bb3b87f4c6305d972c6d61811b3a)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/marco0antonio0/translate-manga-br/blob/cb6989b7a978bb3b87f4c6305d972c6d61811b3a/README.md) / [GitHub API](https://api.github.com/repos/marco0antonio0/translate-manga-br) / [固定ツリー](https://github.com/marco0antonio0/translate-manga-br/tree/cb6989b7a978bb3b87f4c6305d972c6d61811b3a)

### 制作に使う際の検討

自前サーバで漫画翻訳と閲覧を回す用途。

**次に確かめること（実施前）**: 日本語ページで吹き出し検出・OCR精度とDocker運用の負荷を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [lib/backend/shared/migrations/index.ts](https://github.com/marco0antonio0/translate-manga-br/blob/cb6989b7a978bb3b87f4c6305d972c6d61811b3a/lib/backend/shared/migrations/index.ts)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-01T04:11:43Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="lingoveil"></a>

## LingoVeil

漫画・コミック向けのセルフホスト翻訳ツール。画像内のテキストを検出・翻訳し、翻訳ビューで読める。ブックマークや読書進捗も保持する。

- **リポジトリ**: https://github.com/Gerald-Ha/LingoVeil
- **分類**: web_app / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 画像、PDF、対応漫画サイトの章ページ
- **出力**: 翻訳ビュー、履歴・ブックマーク
- **環境**: Docker等でセルフホスト。翻訳はSeamlessM4T v2 Large/Bergamot/LM Studio/Ollama。
- **依存**: 翻訳モデル(例:SeamlessM4T v2 Large、約8.7GiB)、任意でOllama/LM Studio
- **制約・未確認**: 翻訳エンジンごとに対応言語が異なる。新規・小規模。SeamlessM4TはRAM消費が大きいと記載。
- **編集者評価**: 読書体験と翻訳を一体化し、スマホから同じサーバにアクセスできる点が実用的。
- **メトリクス**: ★5、fork 0、作成 2026-08-07、最終push 2026-09-30T08:44:03Z、archived=False
- **確認**: 2026-09-30 / コミット `dc3e378a7199f7c746fa4a94d7556532885a5386`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Gerald-Ha/LingoVeil/tree/dc3e378a7199f7c746fa4a94d7556532885a5386)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Gerald-Ha/LingoVeil/blob/dc3e378a7199f7c746fa4a94d7556532885a5386/README.md) / [GitHub API](https://api.github.com/repos/Gerald-Ha/LingoVeil) / [固定ツリー](https://github.com/Gerald-Ha/LingoVeil/tree/dc3e378a7199f7c746fa4a94d7556532885a5386)

### 制作に使う際の検討

自宅サーバとスマホ閲覧を組み合わせた翻訳読書に。

**次に確かめること（実施前）**: 実ページでOCR品質とSeamlessM4TのRAM/速度、Ollama連携の設定負荷を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [web/app.js](https://github.com/Gerald-Ha/LingoVeil/blob/dc3e378a7199f7c746fa4a94d7556532885a5386/web/app.js)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-30T08:44:03Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="overtranslate"></a>

## OverTranslate

Windows向けの画面翻訳ツール。スクリーンショット翻訳・リアルタイム翻訳・取詞翻訳・快速翻訳・文字翻訳の5機能を持ち、認識した訳文を元の画面上にそのまま重ねて表示する。

- **リポジトリ**: https://github.com/Hon-Lu/OverTranslate
- **分類**: desktop_tool / AIは任意 / 活発・実用候補
- **入力**: 画面キャプチャ（スクリーン/ウィンドウ）、選択テキスト、入力テキスト
- **出力**: 画面にオーバーレイ表示された訳文、コピー可能なテキスト、朗読音声
- **環境**: Windows 10/11。インストーラに実行環境を同梱。DeepL/OpenAIを使う場合はAPIキー、ローカルLLMはOllamaを使用。
- **依存**: PP-OCRv6系ONNXモデル（RapidOcrNet）、Google/Bing/Microsoft/DeepL/OpenAI互換の翻訳サービス
- **制約・未確認**: 対応OSはWindowsのみ。OCRはRapidOcrNetのONNXモデルで、翻訳は外部サービスまたはローカルLLMに依存する。READMEに翻訳品質の数値評価の記載はない。
- **編集者評価**: 漫画・ゲーム・動画字幕のその場翻訳という用途が具体的で、OCRは端末内CPU処理、翻訳は複数サービスを自動で切り替える備援機構を持つ。
- **メトリクス**: ★97、fork 8、作成 2026-05-09、最終push 2026-10-05T15:49:37Z、archived=False
- **確認**: 2026-10-01 / コミット `2c9d1ab98e0327837a4df009f6f404fe5b494d18`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Hon-Lu/OverTranslate/tree/2c9d1ab98e0327837a4df009f6f404fe5b494d18)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Hon-Lu/OverTranslate/blob/2c9d1ab98e0327837a4df009f6f404fe5b494d18/README.md) / [GitHub API](https://api.github.com/repos/Hon-Lu/OverTranslate) / [固定ツリー](https://github.com/Hon-Lu/OverTranslate/tree/2c9d1ab98e0327837a4df009f6f404fe5b494d18)

### 制作に使う際の検討

漫画・ゲーム画面を読むための補助ツールとして試しやすい。

**次に確かめること（実施前）**: 漫画ページでOCR認識と訳文レイアウト（重なり・改行）を実測し、ローカルLLM使用時の速度を記録する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [docs/site/app.js](https://github.com/Hon-Lu/OverTranslate/blob/2c9d1ab98e0327837a4df009f6f404fe5b494d18/docs/site/app.js) / [src/OverTranslate.Launcher/src/main.rs](https://github.com/Hon-Lu/OverTranslate/blob/2c9d1ab98e0327837a4df009f6f404fe5b494d18/src/OverTranslate.Launcher/src/main.rs)

**最新GitHub Release**: [2.6.0](https://github.com/Hon-Lu/OverTranslate/releases/tag/2.6.0) / 2026-10-03T08:33:30Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-10-01T16:59:10Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="fumetoreaderplus"></a>

## FumetoReaderPlus

Android向け漫画リーダー。吹き出し検出・OCR・漫画向けLLM翻訳・風船内への再レタリングを端末上で行い、タップで原文に戻せる。

- **リポジトリ**: https://github.com/fumetodev/FumetoReaderPlus
- **分類**: desktop_tool / AIモデル・学習 / 活発な候補
- **入力**: CBZ/CBR/PDF/EPUB、Komga/Kavita/YACReaderLibraryServerのサーバ
- **出力**: 翻訳済みページ表示、翻訳CBZ
- **環境**: Android。ビルドにはJDK 21、Android SDK/NDK 29.0.13846066、Rust、Node 22/24/26が必要。
- **依存**: PP-OCR、Hy-MT2 1.8B漫画向けFT（ONNX Runtime/llama.cpp）、rtmdetレイアウトモデル
- **制約・未確認**: テスト・評価用コードとコーパスは非公開。デスクトップ版は実験的で未対応と明記。
- **編集者評価**: 端末内で完結する漫画翻訳リーダーで、レタリングや一括翻訳まで実装されている。
- **メトリクス**: ★5、fork 1、作成 2026-09-02、最終push 2026-10-04T18:01:39Z、archived=False
- **確認**: 2026-10-03 / コミット `a56a4c621b3b6a5a6eb89fa01e0a0a0526cdb677`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/fumetodev/FumetoReaderPlus/tree/a56a4c621b3b6a5a6eb89fa01e0a0a0526cdb677)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/fumetodev/FumetoReaderPlus/blob/a56a4c621b3b6a5a6eb89fa01e0a0a0526cdb677/README.md) / [GitHub API](https://api.github.com/repos/fumetodev/FumetoReaderPlus) / [固定ツリー](https://github.com/fumetodev/FumetoReaderPlus/tree/a56a4c621b3b6a5a6eb89fa01e0a0a0526cdb677)

### 制作に使う際の検討

権利を有する漫画の端末内翻訳・閲覧に使える。

**次に確かめること（実施前）**: 実機で1ページ翻訳を試し、風船内レタリングと所要時間（1ページ6〜16秒と記載）を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [src-tauri/llama-bridge/llama.cpp/tools/cli/cli.cpp](https://github.com/fumetodev/FumetoReaderPlus/blob/a56a4c621b3b6a5a6eb89fa01e0a0a0526cdb677/src-tauri/llama-bridge/llama.cpp/tools/cli/cli.cpp) / [src-tauri/llama-bridge/llama.cpp/tools/server/server.cpp](https://github.com/fumetodev/FumetoReaderPlus/blob/a56a4c621b3b6a5a6eb89fa01e0a0a0526cdb677/src-tauri/llama-bridge/llama.cpp/tools/server/server.cpp) / [src-tauri/llama-bridge/llama.cpp/tools/server/webui/.storybook/main.ts](https://github.com/fumetodev/FumetoReaderPlus/blob/a56a4c621b3b6a5a6eb89fa01e0a0a0526cdb677/src-tauri/llama-bridge/llama.cpp/tools/server/webui/.storybook/main.ts)

**最新GitHub Release**: [v0.7.3-vc7003](https://github.com/fumetodev/FumetoReaderPlus/releases/tag/v0.7.3-vc7003) / 2026-09-04T16:43:38Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-04T16:54:27Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="solar-manga-translator"></a>

## Solar-Manga-Translator

中国語話者向けのローカル漫画翻訳・校正ワークベンチ。OCR、AI翻訳、擦字補修、自動嵌字、人手校正、導出を一流程にまとめる。

- **リポジトリ**: https://github.com/soluna/Solar-Manga-Translator
- **分類**: desktop_tool / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 画像、画像フォルダ、ZIP、CBZ
- **出力**: 処理済み画像、アーカイブ、プロジェクト（スナップショット）
- **環境**: Python 3.10/3.11、Node.js 22.12以上、実翻訳にはWindows + NVIDIA GPU推奨。初回にモデル・依存をダウンロード。
- **依存**: FastAPI、Vue3+Vite、Electron、翻訳サービスAPIキー（Gemini/豆包Ark等）
- **制約・未確認**: 配布用インストーラ未公開、Windows打包は実験的。翻訳・補修結果は人手確認が必要と明記。
- **編集者評価**: 翻訳初稿を人がページ単位で校正できる作業台として構成されている。
- **メトリクス**: ★4、fork 0、作成 2026-07-02、最終push 2026-09-30T14:51:19Z、archived=False
- **確認**: 2026-10-03 / コミット `88864b95044b29ae9e4997594b2c61bc2f066c07`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/soluna/Solar-Manga-Translator/tree/88864b95044b29ae9e4997594b2c61bc2f066c07)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/soluna/Solar-Manga-Translator/blob/88864b95044b29ae9e4997594b2c61bc2f066c07/README.md) / [GitHub API](https://api.github.com/repos/soluna/Solar-Manga-Translator) / [固定ツリー](https://github.com/soluna/Solar-Manga-Translator/tree/88864b95044b29ae9e4997594b2c61bc2f066c07)

### 制作に使う際の検討

権利を有する画像の翻訳・校正に使える。

**次に確かめること（実施前）**: 合成素材で導入→OCR→翻訳→嵌字→導出を一通り実行し、再現性を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [backend/main.py](https://github.com/soluna/Solar-Manga-Translator/blob/88864b95044b29ae9e4997594b2c61bc2f066c07/backend/main.py) / [frontend-v3/src/main.js](https://github.com/soluna/Solar-Manga-Translator/blob/88864b95044b29ae9e4997594b2c61bc2f066c07/frontend-v3/src/main.js) / [frontend/src/main.js](https://github.com/soluna/Solar-Manga-Translator/blob/88864b95044b29ae9e4997594b2c61bc2f066c07/frontend/src/main.js)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-24T12:58:57Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="ugtlive"></a>

## UGTLive

Windows向けGUIツールで、画面や画像の文字を「ライブ」でOCR・翻訳する。縦書き日本語の漫画読み上げ、PDF/CBZ/画像の一括変換、音声読み上げ、リアルタイム字幕にも対応する。

- **リポジトリ**: https://github.com/SethRobinson/UGTLive
- **分類**: desktop_tool / AIモデル・学習 / 稼働中・実運用候補
- **入力**: 画面キャプチャ、画像、PDF/CBZファイル
- **出力**: 翻訳テキスト/オーバーレイ、音声読み上げ、HTMLエクスポート、翻訳済み画像
- **環境**: Windows、NVIDIA RTX 20〜50系、VRAM 8GB以上。OCRはEasyOCR/MangaOCR/PaddleOCR/docTR等をGPUサービスとして導入。
- **依存**: llama.cpp/Ollama、EasyOCR等のOCRサービス、任意でOpenAI/Gemini/OpenRouter等のAPI
- **制約・未確認**: Windows/NVIDIA前提でAMD/Intelは未検証。高品質翻訳や音声はOpenAI/Gemini/ElevenLabs等の外部APIキーが必要。ライセンスはBSD系の帰属表示。
- **編集者評価**: 漫画・ゲーム・ビジュアルノベルの翻訳を、ローカルGPUまたは任意のAPIで行える。26言語対応で、読み解き用途から下訳まで幅広く使える。
- **メトリクス**: ★117、fork 15、作成 2025-04-18、最終push 2026-09-03T13:15:24Z、archived=False
- **確認**: 2026-10-04 / コミット `f647679dcc384aba2ed9178172d227db8e79effd`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/SethRobinson/UGTLive/tree/f647679dcc384aba2ed9178172d227db8e79effd)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/SethRobinson/UGTLive/blob/f647679dcc384aba2ed9178172d227db8e79effd/README.md) / [GitHub API](https://api.github.com/repos/SethRobinson/UGTLive) / [固定ツリー](https://github.com/SethRobinson/UGTLive/tree/f647679dcc384aba2ed9178172d227db8e79effd)

### 制作に使う際の検討

漫画やゲーム画面の翻訳を手元で高速に回したいローカライズ作業に向く。

**次に確かめること（実施前）**: 縦書き漫画ページを読み込ませ、MangaOCRでの文字起こし精度とページ読み上げ・HTML出力の実用性を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [app/services/EasyOCR/server.py](https://github.com/SethRobinson/UGTLive/blob/f647679dcc384aba2ed9178172d227db8e79effd/app/services/EasyOCR/server.py) / [app/services/MangaOCR/server.py](https://github.com/SethRobinson/UGTLive/blob/f647679dcc384aba2ed9178172d227db8e79effd/app/services/MangaOCR/server.py) / [app/services/PaddleOCR/server.py](https://github.com/SethRobinson/UGTLive/blob/f647679dcc384aba2ed9178172d227db8e79effd/app/services/PaddleOCR/server.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-03T11:28:46Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="manga-translator"></a>

## manga-translator

Gio製GUIのデスクトップアプリで、画像内のテキストをOCRして翻訳する。検出した全テキストに色付きボックスを表示し、クリックで原文と訳文を確認・コピーできる。

- **リポジトリ**: https://github.com/cameronkinsella/manga-translator
- **分類**: desktop_tool / AI連携 / 稼働中
- **入力**: 画像ファイル、画像URL、クリップボードの画像
- **出力**: 原文/訳文テキスト（コピー可能）、複数画像のナビゲーション表示
- **環境**: Google Cloud Vision APIのサービスアカウントキーが必須。翻訳はGoogle Cloud TranslationまたはDeepLのAPIキーが必要。Windowsはバイナリ配布、他はgo install。
- **依存**: Google Cloud Vision API、Google Cloud Translation API または DeepL API
- **制約・未確認**: クラウドAPIキーが必須でローカル完結しない。OCR/翻訳はGoogle/DeepL依存。ライセンスはMIT。
- **編集者評価**: GUIで手軽に画像内文字を確認・翻訳でき、漫画の読解や用語確認の補助に向く。
- **メトリクス**: ★153、fork 10、作成 2021-09-04、最終push 2026-02-01T12:23:56Z、archived=False
- **確認**: 2026-10-04 / コミット `3b1139c8f446ef4e9e5b3776e415038ec2a73f4c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/cameronkinsella/manga-translator/tree/3b1139c8f446ef4e9e5b3776e415038ec2a73f4c)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/cameronkinsella/manga-translator/blob/3b1139c8f446ef4e9e5b3776e415038ec2a73f4c/README.md) / [GitHub API](https://api.github.com/repos/cameronkinsella/manga-translator) / [固定ツリー](https://github.com/cameronkinsella/manga-translator/tree/3b1139c8f446ef4e9e5b3776e415038ec2a73f4c)

### 制作に使う際の検討

大量処理よりも、数枚の画像を目視で確認しながら訳したい作業に向く。

**次に確かめること（実施前）**: 漫画ページ数枚でOCRボックスの検出精度と訳文のコピー動線を確認し、既存の漫画翻訳ツールとの差分を整理する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [cmd/manga-translator-setup/main.go](https://github.com/cameronkinsella/manga-translator/blob/3b1139c8f446ef4e9e5b3776e415038ec2a73f4c/cmd/manga-translator-setup/main.go) / [cmd/manga-translator/main.go](https://github.com/cameronkinsella/manga-translator/blob/3b1139c8f446ef4e9e5b3776e415038ec2a73f4c/cmd/manga-translator/main.go)

**最新GitHub Release**: [2.2.0](https://github.com/cameronkinsella/manga-translator/releases/tag/2.2.0) / 2026-02-01T12:23:56Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-02-01T12:15:54Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="autoscanlate-ai"></a>

## AutoScanlate-AI

完全ローカル・GPU加速の漫画翻訳パイプライン。YOLOv8で吹き出し検出、MangaOCRで縦書きOCR、Qwen 2.5 7Bで文脈翻訳、マスク付きインペイントと段組みで元画像に描き戻す。Goバックエンド+Next.js UI+Pythonワーカーの構成。

- **リポジトリ**: https://github.com/P4ST4S/AutoScanlate-AI
- **分類**: pipeline / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 漫画/コミックの画像またはZIP
- **出力**: 翻訳済みページ画像
- **環境**: GPU（READMEはRTX 2060 12GBで約29ページ/分と記載）、Docker、Go、Python。run.bat/run.shで起動。
- **依存**: YOLOv8(Manga109)、MangaOCR、Qwen2.5 7B(llama.cpp)、OpenCV、Redis
- **制約・未確認**: ライセンスはNOASSERTION。性能値はREADME記載の環境依存。WindowsではMangaOCRをCPU実行する等の制約がある。
- **編集者評価**: 外部API無しで検出→OCR→翻訳→描き戻しまで通せる構成が具体的で、下訳づくりに使いやすい。
- **メトリクス**: ★35、fork 3、作成 2025-12-07、最終push 2026-09-07T09:32:46Z、archived=False
- **確認**: 2026-10-05 / コミット `fa734c06add489479a306f5923726040a92a467b`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/P4ST4S/AutoScanlate-AI/tree/fa734c06add489479a306f5923726040a92a467b)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/P4ST4S/AutoScanlate-AI/blob/fa734c06add489479a306f5923726040a92a467b/README.md) / [GitHub API](https://api.github.com/repos/P4ST4S/AutoScanlate-AI) / [固定ツリー](https://github.com/P4ST4S/AutoScanlate-AI/tree/fa734c06add489479a306f5923726040a92a467b)

### 制作に使う際の検討

大量ページの下訳・たたき台作成に有効。最終校正は人手前提。

**次に確かめること（実施前）**: 日本語漫画で翻訳品質・描き戻しの破綻・処理速度を実測する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [ai-worker/main.py](https://github.com/P4ST4S/AutoScanlate-AI/blob/fa734c06add489479a306f5923726040a92a467b/ai-worker/main.py) / [backend-api/cmd/api/main.go](https://github.com/P4ST4S/AutoScanlate-AI/blob/fa734c06add489479a306f5923726040a92a467b/backend-api/cmd/api/main.go) / [backend-api/internal/adapters/queue/asynq/server.go](https://github.com/P4ST4S/AutoScanlate-AI/blob/fa734c06add489479a306f5923726040a92a467b/backend-api/internal/adapters/queue/asynq/server.go)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-07T09:32:45Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
