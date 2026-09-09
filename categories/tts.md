# TTS・キャラクター音声

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [fish-speech](https://github.com/fishaudio/fish-speech) · [詳細](#fish-speech) | Fish Audio S2系の表現豊かなTTS・音声クローンを扱う実装。 | AIモデル・学習 / 更新のある導入・評価候補 | 32,627 / 2026-09-07 |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) · [詳細](#gpt-sovits) | 少量音声を使うTTSと音声クローンをWebUIから扱う。 | AIモデル・学習 / 更新のある導入・評価候補 | 61,660 / 2026-08-18 |
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) · [詳細](#qwen3-tts) | 声のデザイン、参照音声による合成、指示による話し方制御を扱う多言語TTS。 | AIモデル・学習 / 研究モデルの評価候補 | 13,328 / 2026-03-17 |
| [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) · [詳細](#style-bert-vits2) | Bert-VITS2を基に音声スタイルの制御と学習を扱う日本語TTSツール。 | AIモデル・学習 / 比較・既存工程の参考 | 1,370 / 2025-12-07 |
| [voicevox](https://github.com/VOICEVOX/voicevox) · [詳細](#voicevox) | 日本語のキャラクター音声を編集して出力するVOICEVOXのエディタ。 | AI連携 / 定番の制作基盤 | 3,236 / 2026-09-09 |

<a id="fish-speech"></a>

## fish-speech

Fish Audio S2系の表現豊かなTTS・音声クローンを扱う実装。

- **リポジトリ**: https://github.com/fishaudio/fish-speech
- **分類**: model / AIモデル・学習 / 更新のある導入・評価候補
- **入力**: テキスト、参照音声
- **出力**: 合成音声
- **環境**: モデル規模に対応した推論環境。
- **依存**: Fish Audio S2-Pro等の対応モデル
- **制約・未確認**: READMEはFISH AUDIO RESEARCH LICENSEと記載。過去版のライセンスを現在版へ適用しない。
- **編集者評価**: 多言語キャラ音声と会話音声の生成候補。
- **メトリクス**: ★32,627、fork 2,816、作成 2023-10-10、最終push 2026-09-07T19:20:34Z、archived=False
- **確認**: 2026-09-09 / コミット `befe4001745417f8c42131739d862b8a6fdbd15a`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/fishaudio/fish-speech/blob/befe4001745417f8c42131739d862b8a6fdbd15a/LICENSE)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/fishaudio/fish-speech/blob/befe4001745417f8c42131739d862b8a6fdbd15a/README.md) / [GitHub API](https://api.github.com/repos/fishaudio/fish-speech) / [固定ツリー](https://github.com/fishaudio/fish-speech/tree/befe4001745417f8c42131739d862b8a6fdbd15a)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [fishaudio/s2-pro](https://huggingface.co/fishaudio/s2-pro) — file_listing_checked、確認日 2026-09-09、revision `1de9996b6be38b745688de084d87a5633f714e4e`。代表ファイル: `codec.pth`, `model-00001-of-00002.safetensors`, `model-00002-of-00002.safetensors`。gated=False。

<a id="gpt-sovits"></a>

## GPT-SoVITS

少量音声を使うTTSと音声クローンをWebUIから扱う。

- **リポジトリ**: https://github.com/RVC-Boss/GPT-SoVITS
- **分類**: model_toolkit / AIモデル・学習 / 更新のある導入・評価候補
- **入力**: テキスト、参照音声、学習音声
- **出力**: 音声合成・追加学習モデル
- **環境**: Pythonまたは配布環境。モデル版に応じたGPU要件。
- **依存**: GPT-SoVITS、音声前処理モデル
- **制約・未確認**: 参照音声の長さと品質で結果が変わる。作者の少量学習品質は未再現。
- **編集者評価**: 独自キャラ音声を作るための学習・推論環境候補。
- **メトリクス**: ★61,660、fork 6,649、作成 2024-01-14、最終push 2026-08-18T09:16:25Z、archived=False
- **確認**: 2026-09-09 / コミット `48b1a0169a28582a8984402f82cf438d3bfa6aca`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/RVC-Boss/GPT-SoVITS/blob/48b1a0169a28582a8984402f82cf438d3bfa6aca/LICENSE)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/RVC-Boss/GPT-SoVITS/blob/48b1a0169a28582a8984402f82cf438d3bfa6aca/README.md) / [GitHub API](https://api.github.com/repos/RVC-Boss/GPT-SoVITS) / [固定ツリー](https://github.com/RVC-Boss/GPT-SoVITS/tree/48b1a0169a28582a8984402f82cf438d3bfa6aca)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [lj1995/GPT-SoVITS](https://huggingface.co/lj1995/GPT-SoVITS) — file_listing_checked、確認日 2026-09-09、revision `336b2ec4e8d4ac74740798dd40af44e74659ecaf`。代表ファイル: `chinese-hubert-base/pytorch_model.bin`, `chinese-roberta-wwm-ext-large/pytorch_model.bin`, `gsv-v2final-pretrained/s1bert25hz-5kh-longer-epoch=12-step=369668.ckpt`, `gsv-v2final-pretrained/s2D2333k.pth`。gated=False。

<a id="qwen3-tts"></a>

## Qwen3-TTS

声のデザイン、参照音声による合成、指示による話し方制御を扱う多言語TTS。

- **リポジトリ**: https://github.com/QwenLM/Qwen3-TTS
- **分類**: model / AIモデル・学習 / 研究モデルの評価候補
- **入力**: テキスト、声の説明、参照音声
- **出力**: 合成音声
- **環境**: Python推論環境。0.6B/1.7Bなどのモデル別に機能が異なる。
- **依存**: Qwen3-TTS、音声トークナイザ
- **制約・未確認**: 通常TTSの表現制御とASMR専用性能を同一視しない。
- **編集者評価**: 日本語を含むキャラ音声・ナレーション制作の新しい基盤候補。
- **メトリクス**: ★13,328、fork 1,727、作成 2026-01-21、最終push 2026-03-17T06:38:41Z、archived=False
- **確認**: 2026-09-09 / コミット `022e286b98fbec7e1e916cb940cdf532cd9f488e`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/README.md) / [GitHub API](https://api.github.com/repos/QwenLM/Qwen3-TTS) / [固定ツリー](https://github.com/QwenLM/Qwen3-TTS/tree/022e286b98fbec7e1e916cb940cdf532cd9f488e)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign) — file_listing_checked、確認日 2026-09-09、revision `5ecdb67327fd37bb2e042aab12ff7391903235d3`。代表ファイル: `model.safetensors`, `speech_tokenizer/model.safetensors`。gated=False。

<a id="style-bert-vits2"></a>

## Style-Bert-VITS2

Bert-VITS2を基に音声スタイルの制御と学習を扱う日本語TTSツール。

- **リポジトリ**: https://github.com/litagin02/Style-Bert-VITS2
- **分類**: model_toolkit / AIモデル・学習 / 比較・既存工程の参考
- **入力**: テキスト、音声スタイル、学習音声
- **出力**: 読み上げ音声・追加学習モデル
- **環境**: Python、音声モデル、推論用ライブラリまたはエディタ。
- **依存**: Style-Bert-VITS2モデル、BERT、音声素材
- **制約・未確認**: コードとデフォルト音声モデルの利用条件を分ける。最近の更新は少ない。
- **編集者評価**: キャラの声色・話し方を調整する候補。
- **メトリクス**: ★1,370、fork 215、作成 2023-12-01、最終push 2025-12-07T13:06:59Z、archived=False
- **確認**: 2026-09-09 / コミット `66de777e06392c0f313600be03c43ef96658b244`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/litagin02/Style-Bert-VITS2/blob/66de777e06392c0f313600be03c43ef96658b244/LICENSE)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/litagin02/Style-Bert-VITS2/blob/66de777e06392c0f313600be03c43ef96658b244/README.md) / [GitHub API](https://api.github.com/repos/litagin02/Style-Bert-VITS2) / [固定ツリー](https://github.com/litagin02/Style-Bert-VITS2/tree/66de777e06392c0f313600be03c43ef96658b244)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [litagin/Style-Bert-VITS2-2.0-base-JP-Extra](https://huggingface.co/litagin/Style-Bert-VITS2-2.0-base-JP-Extra) — file_listing_checked、確認日 2026-09-09、revision `a731761009f3c96d104487be6ad332bf1bb5a3a5`。代表ファイル: `D_0.safetensors`, `G_0.safetensors`, `WD_0.safetensors`。gated=False。

<a id="voicevox"></a>

## voicevox

日本語のキャラクター音声を編集して出力するVOICEVOXのエディタ。

- **リポジトリ**: https://github.com/VOICEVOX/voicevox
- **分類**: desktop_tool / AI連携 / 定番の制作基盤
- **入力**: 日本語テキスト、話者・抑揚設定
- **出力**: 読み上げ音声
- **環境**: VOICEVOXアプリと音声エンジン。
- **依存**: VOICEVOX ENGINE、音声ライブラリ
- **制約・未確認**: このリポジトリはエディタ。エンジン・音声ライブラリ・キャラの条件は別。
- **編集者評価**: セリフ・説明動画・ゲーム用音声の制作入口。
- **メトリクス**: ★3,236、fork 373、作成 2021-07-27、最終push 2026-09-09T11:18:27Z、archived=False
- **確認**: 2026-09-09 / コミット `b7258250fe90c82f112d0f51e43f2a1b67992d36`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/VOICEVOX/voicevox/blob/b7258250fe90c82f112d0f51e43f2a1b67992d36/LICENSE)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/VOICEVOX/voicevox/blob/b7258250fe90c82f112d0f51e43f2a1b67992d36/README.md) / [GitHub API](https://api.github.com/repos/VOICEVOX/voicevox) / [固定ツリー](https://github.com/VOICEVOX/voicevox/tree/b7258250fe90c82f112d0f51e43f2a1b67992d36)
