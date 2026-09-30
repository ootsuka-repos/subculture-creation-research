# 字幕・翻訳・ローカライズ

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-30。**126件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ASMR Dubber](https://github.com/EveningStudy/asmr-dubber) · [詳細](#asmr-dubber) | 日本語・英語の音声や動画を、校正可能な字幕・中国語吹替・二言語音声へ変換する制作ツール。 | AI連携 / 小規模・制作連携候補 | 215 / 2026-09-30 |
| [Manga OCR](https://github.com/kha-white/manga-ocr) · [詳細](#manga-ocr) | 日本語漫画の縦書き・横書き・ルビ付き文字を認識する。 | AIモデル・学習 / モデル・研究候補 | 2,792 / 2026-07-19 |
| [manga-image-translator](https://github.com/zyddnys/manga-image-translator) · [詳細](#manga-image-translator) | 画像内の文字を検出・認識・翻訳し、元の文字を修復して訳文を組版する。 | AIモデル・学習 / 比較・既存工程の参考 | 10,457 / 2026-09-25 |
| [mokuro](https://github.com/kha-white/mokuro) · [詳細](#mokuro) | 漫画ページの文字位置とOCR結果をまとめ、選択可能なテキストとして閲覧できる形式へ変換。 | AI連携 / 連携・制作ツール候補 | 1,738 / 2026-07-20 |
| [VoiceTransl](https://github.com/shinnpuru/VoiceTransl) · [詳細](#voicetransl) | 音声認識、字幕翻訳、字幕と動画の処理を組み合わせる。 | AI連携 / 連携の評価候補 | 1,298 / 2026-08-28 |
| [xianscan-rust](https://github.com/ArbenApura/xianscan-rust) · [詳細](#xianscan-rust) | 漫画・韓漫・国漫向けのローカル完結型翻訳スタジオ。吹き出し検出、多言語OCR、LLM翻訳、LaMaによるインペイント、組版までを単体バイナリで実行する。 | AIモデル・学習 / 更新が活発な実装候補 | 77 / 2026-09-29 |
| [BallonsTranslator-Pro](https://github.com/thomaswantstobeaskeleton/BallonsTranslator-Pro) · [詳細](#ballonstranslator-pro) | BallonsTranslatorを元にした漫画・コミック翻訳ツールキットで、検出・OCR・翻訳・インペイント・植字を組み替え可能なモジュール群で処理する。 | AIモデル・学習 / 活発・候補 | 96 / 2026-07-31 |
| [CarrotMangaTranslator](https://github.com/ucx0204/CarrotMangaTranslator) · [詳細](#carrotmangatranslator) | 漫画原稿のOCR→翻訳→原文消去→植字・検品→出力を扱うデスクトップアプリ。局所GemmaやOpenAI互換APIで翻訳する。 | AIモデル・学習 / 活発・候補 | 76 / 2026-09-30 |
| [Kites](https://github.com/Unheat/Kites) · [詳細](#kites) | ブラウザ拡張として動作し、WebGPU上でOCR・インペイント・翻訳を行って漫画をその場で翻訳表示するツール。 | AIモデル・学習 / 初期評価候補 | 30 / 2026-09-26 |

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
- **メトリクス**: ★215、fork 12、作成 2026-07-23、最終push 2026-09-30T16:16:58Z、archived=False
- **確認**: 2026-09-09 / コミット `bc088faceec743d51f2914e9f7efd98d7b19d9e3`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/EveningStudy/asmr-dubber/tree/bc088faceec743d51f2914e9f7efd98d7b19d9e3)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/EveningStudy/asmr-dubber/blob/bc088faceec743d51f2914e9f7efd98d7b19d9e3/README.md) / [GitHub API](https://api.github.com/repos/EveningStudy/asmr-dubber) / [固定ツリー](https://github.com/EveningStudy/asmr-dubber/tree/bc088faceec743d51f2914e9f7efd98d7b19d9e3)

### 制作に使う際の検討

ASMR作品の翻訳・台本校正・吹替・混音までを扱う具体的な連携候補。 生成音質だけでなく字幕と音声の手修正・再生成のしやすさを比較する。

**次に確かめること（実施前）**: 自作3分音声で小声・無音・息を含む字幕を校正し、中国語台詞の長さ、原声との重なり、キャッシュ再利用を確認する。

**利用条件の確認メモ**: コードはREADMEでMIT。モデル・サービス・入力作品・生成内容の条件は別と明記。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/asmr_dubber/cli.py](https://github.com/EveningStudy/asmr-dubber/blob/bc088faceec743d51f2914e9f7efd98d7b19d9e3/src/asmr_dubber/cli.py)

**最新GitHub Release**: [v1.6.2](https://github.com/EveningStudy/asmr-dubber/releases/tag/v1.6.2) / 2026-09-30T16:21:38Z / prerelease=False

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
- **メトリクス**: ★2,792、fork 142、作成 2022-01-15、最終push 2026-07-19T08:43:43Z、archived=False
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
- **メトリクス**: ★10,457、fork 1,067、作成 2021-02-18、最終push 2026-09-25T02:45:14Z、archived=False
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
- **メトリクス**: ★1,738、fork 121、作成 2022-04-16、最終push 2026-07-20T07:18:29Z、archived=False
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
- **メトリクス**: ★1,298、fork 53、作成 2024-03-15、最終push 2026-08-28T14:44:44Z、archived=False
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
- **メトリクス**: ★77、fork 12、作成 2026-08-16、最終push 2026-09-29T22:30:33Z、archived=False
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
- **メトリクス**: ★76、fork 16、作成 2026-04-20、最終push 2026-09-30T12:37:59Z、archived=False
- **確認**: 2026-09-30 / コミット `a6454549af83d424dc47d871d76734fb8a33187d`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/ucx0204/CarrotMangaTranslator/tree/a6454549af83d424dc47d871d76734fb8a33187d)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ucx0204/CarrotMangaTranslator/blob/a6454549af83d424dc47d871d76734fb8a33187d/README.md) / [GitHub API](https://api.github.com/repos/ucx0204/CarrotMangaTranslator) / [固定ツリー](https://github.com/ucx0204/CarrotMangaTranslator/tree/a6454549af83d424dc47d871d76734fb8a33187d)

### 制作に使う際の検討

漫画翻訳の制作パイプラインを1アプリで完結させやすい。

**次に確かめること（実施前）**: 1話を読み込み、OCR精度と原文消去・植字の編集しやすさを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [src/main/index.ts](https://github.com/ucx0204/CarrotMangaTranslator/blob/a6454549af83d424dc47d871d76734fb8a33187d/src/main/index.ts) / [src/preload/index.ts](https://github.com/ucx0204/CarrotMangaTranslator/blob/a6454549af83d424dc47d871d76734fb8a33187d/src/preload/index.ts) / [src/renderer/src/main.tsx](https://github.com/ucx0204/CarrotMangaTranslator/blob/a6454549af83d424dc47d871d76734fb8a33187d/src/renderer/src/main.tsx)

**最新GitHub Release**: [v3.0.1](https://github.com/ucx0204/CarrotMangaTranslator/releases/tag/v3.0.1) / 2026-09-30T12:38:00Z / prerelease=False

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
- **メトリクス**: ★30、fork 5、作成 2026-07-08、最終push 2026-09-26T16:09:40Z、archived=False
- **確認**: 2026-09-30 / コミット `420898820e9ac2d4e91eede871ce48087c411475`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Unheat/Kites/tree/420898820e9ac2d4e91eede871ce48087c411475)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Unheat/Kites/blob/420898820e9ac2d4e91eede871ce48087c411475/README.md) / [GitHub API](https://api.github.com/repos/Unheat/Kites) / [固定ツリー](https://github.com/Unheat/Kites/tree/420898820e9ac2d4e91eede871ce48087c411475)

### 制作に使う際の検討

ブラウザで読む漫画の下訳・確認作業を軽量化。

**次に確かめること（実施前）**: 対応サイトで実際に翻訳・植字結果と処理速度を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [site/js/main.js](https://github.com/Unheat/Kites/blob/420898820e9ac2d4e91eede871ce48087c411475/site/js/main.js) / [src/background/index.ts](https://github.com/Unheat/Kites/blob/420898820e9ac2d4e91eede871ce48087c411475/src/background/index.ts) / [src/content/index.tsx](https://github.com/Unheat/Kites/blob/420898820e9ac2d4e91eede871ce48087c411475/src/content/index.tsx)

**最新GitHub Release**: [v1.1.0](https://github.com/Unheat/Kites/releases/tag/v1.1.0) / 2026-09-24T22:03:13Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-26T16:09:39Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
