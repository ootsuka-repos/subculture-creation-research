# TTS・キャラクター音声

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-06。**185件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [CosyVoice](https://github.com/QwenAudio/CosyVoice) · [詳細](#cosyvoice) | ストリーミング対応の多言語音声合成。現行READMEはFun-CosyVoice3を案内。 | AIモデル・学習 / モデル・研究候補 | 23,851 / 2026-05-25 |
| [F5-TTS](https://github.com/SWivid/F5-TTS) · [詳細](#f5-tts) | 参照音声とテキストを使うフローマッチング音声合成・追加学習。 | AIモデル・学習 / モデル・研究候補 | 15,346 / 2026-09-21 |
| [fish-speech](https://github.com/fishaudio/fish-speech) · [詳細](#fish-speech) | Fish Audio S2系の表現豊かなTTS・音声クローンを扱う実装。 | AIモデル・学習 / 更新のある導入・評価候補 | 32,953 / 2026-10-05 |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) · [詳細](#gpt-sovits) | 少量音声を使うTTSと音声クローンをWebUIから扱う。 | AIモデル・学習 / 更新のある導入・評価候補 | 62,417 / 2026-10-06 |
| [IndexTTS](https://github.com/index-tts/index-tts) · [詳細](#index-tts) | 声質・感情の条件を扱う音声合成。現行2.5は日本語を含む5言語を案内。 | AIモデル・学習 / モデル・研究候補 | 24,332 / 2026-09-29 |
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) · [詳細](#qwen3-tts) | 声のデザイン、参照音声による合成、指示による話し方制御を扱う多言語TTS。 | AIモデル・学習 / 研究モデルの評価候補 | 13,668 / 2026-03-17 |
| [RVC WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) · [詳細](#retrieval-based-voice-conversion-webui) | 入力音声の発話内容を保ちながら学習した声へ変換する。 | AIモデル・学習 / モデル・研究候補 | 38,622 / 2026-08-04 |
| [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) · [詳細](#style-bert-vits2) | Bert-VITS2を基に音声スタイルの制御と学習を扱う日本語TTSツール。 | AIモデル・学習 / 比較・既存工程の参考 | 1,380 / 2025-12-07 |
| [voicevox](https://github.com/VOICEVOX/voicevox) · [詳細](#voicevox) | 日本語のキャラクター音声を編集して出力するVOICEVOXのエディタ。 | AI連携 / 定番の制作基盤 | 3,261 / 2026-10-03 |
| [Genie-TTS](https://github.com/High-Logic/Genie-TTS) · [詳細](#genie-tts) | GPT-SoVITS（V2/V2ProPlus）をONNX化してCPUで動かす軽量推論エンジン。TTS推論・モデル変換・FastAPIサーバーをまとめて提供する。 | AIモデル・学習 / 活発・実用段階 | 1,792 / 2026-08-30 |
| [TTS-WebUI](https://github.com/rsxdalv/TTS-WebUI) · [詳細](#tts-webui) | 多数のTTS/音声生成モデルを1つのGradio+React UIで扱うWebUI。GPT-SoVITS、XTTSv2、Kokoro、StyleTTS2、RVC、MusicGen、Demucs等の拡張を備える。 | AIモデル・学習 / 活発・実用段階 | 3,282 / 2026-09-07 |
| [vits-simple-api](https://github.com/Artrajz/vits-simple-api) · [詳細](#vits-simple-api) | VITS系TTSをHTTP APIとして提供するサーバー。VITS/Bert-VITS2/GPT-SoVITS/emotion-vits等の複数モデルを読み込み、GETで音声合成できる。 | AIモデル・学習 / 活発・実用段階 | 1,050 / 2026-05-18 |

<a id="cosyvoice"></a>

## CosyVoice

ストリーミング対応の多言語音声合成。現行READMEはFun-CosyVoice3を案内。

- **リポジトリ**: https://github.com/QwenAudio/CosyVoice
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: テキスト、参照音声、モデル別の制御指示
- **出力**: 合成音声、ストリーミング音声
- **環境**: Python、PyTorch。採用版の導入手順に従う。
- **依存**: Fun-CosyVoice3-0.5B-2512等、音声トークナイザ
- **制約・未確認**: FunAudioLLMからQwenAudioへ移転。作者の低遅延値は全システムの遅延ではない。
- **編集者評価**: 会話キャラの音声バックエンド候補。発話開始までの遅延を重視する場合に比較。
- **メトリクス**: ★23,851、fork 2,716、作成 2024-07-03、最終push 2026-05-25T18:15:40Z、archived=False
- **確認**: 2026-09-09 / コミット `074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/QwenAudio/CosyVoice/tree/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/README.md) / [GitHub API](https://api.github.com/repos/QwenAudio/CosyVoice) / [固定ツリー](https://github.com/QwenAudio/CosyVoice/tree/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc)

### 制作に使う際の検討

会話キャラの音声バックエンド候補。発話開始までの遅延を重視する場合に比較。

**次に確かめること（実施前）**: 日本語の最初の音が出る時間、文途中の区切り、参照声質の保持を計測する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [example.py](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/example.py) / [vllm_example.py](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/vllm_example.py) / [webui.py](https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/webui.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-05-25T18:15:40Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [FunAudioLLM/Fun-CosyVoice3-0.5B-2512](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512) — file_listing_checked、確認日 2026-09-09、revision `29e01c4e8d000f4bcd70751be16fa94bf3d85a18`。代表ファイル: `CosyVoice-BlankEN/model.safetensors`, `flow.pt`, `hift.pt`, `llm.pt`。gated=False。

<a id="f5-tts"></a>

## F5-TTS

参照音声とテキストを使うフローマッチング音声合成・追加学習。

- **リポジトリ**: https://github.com/SWivid/F5-TTS
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 参照音声と文字起こし、合成テキスト
- **出力**: 合成音声
- **環境**: Python/PyTorch、CLIまたはGradio。
- **依存**: F5-TTSチェックポイント、VocosまたはBigVGAN
- **制約・未確認**: コードはMIT、事前学習モデルはREADMEでCC BY-NCと明記。日本語の標準対応を推定しない。
- **編集者評価**: 音声参照を使う研究比較に適する。声の演技と日本語品質は別々に試す。
- **メトリクス**: ★15,346、fork 2,238、作成 2024-10-08、最終push 2026-09-21T14:21:15Z、archived=False
- **確認**: 2026-09-09 / コミット `9c614e9657089213efc6a7421b30630be138a3f5`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/SWivid/F5-TTS/tree/9c614e9657089213efc6a7421b30630be138a3f5)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/SWivid/F5-TTS/blob/9c614e9657089213efc6a7421b30630be138a3f5/README.md) / [GitHub API](https://api.github.com/repos/SWivid/F5-TTS) / [固定ツリー](https://github.com/SWivid/F5-TTS/tree/9c614e9657089213efc6a7421b30630be138a3f5)

### 制作に使う際の検討

音声参照を使う研究比較に適する。声の演技と日本語品質は別々に試す。

**次に確かめること（実施前）**: 参照の無音・雑音・読み誤りを変えて比較し、使用する言語モデルを特定する。

**利用条件の確認メモ**: READMEでコードMIT、事前学習重みCC BY-NCと区別。 商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/f5_tts/infer/infer_cli.py](https://github.com/SWivid/F5-TTS/blob/9c614e9657089213efc6a7421b30630be138a3f5/src/f5_tts/infer/infer_cli.py)

**最新GitHub Release**: [1.1.22](https://github.com/SWivid/F5-TTS/releases/tag/1.1.22) / 2026-07-23T09:20:37Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-23T09:19:55Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [SWivid/F5-TTS](https://huggingface.co/SWivid/F5-TTS) — file_listing_checked、確認日 2026-09-09、revision `84e5a410d9cead4de2f847e7c9369a6440bdfaca`。代表ファイル: `F5TTS_Base/model_1200000.pt`, `F5TTS_Base/model_1200000.safetensors`, `F5TTS_Base_bigvgan/model_1250000.pt`, `F5TTS_v1_Base/model_1250000.safetensors`。gated=False。

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
- **メトリクス**: ★32,953、fork 2,849、作成 2023-10-10、最終push 2026-10-05T20:25:09Z、archived=False
- **確認**: 2026-09-09 / コミット `befe4001745417f8c42131739d862b8a6fdbd15a`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/fishaudio/fish-speech/tree/befe4001745417f8c42131739d862b8a6fdbd15a)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/fishaudio/fish-speech/blob/befe4001745417f8c42131739d862b8a6fdbd15a/README.md) / [GitHub API](https://api.github.com/repos/fishaudio/fish-speech) / [固定ツリー](https://github.com/fishaudio/fish-speech/tree/befe4001745417f8c42131739d862b8a6fdbd15a)

### 制作に使う際の検討

現行S2-Proには小声など自由記述の表現タグが案内される。ASMR専用の耳元表現とは別に音声演技を評価する。

**次に確かめること（実施前）**: 通常声・小声を同じ台詞で比較し、息・子音・発音と長文の安定性を試聴する。

**利用条件の確認メモ**: 現行S2-Proのコード・重みはFISH AUDIO RESEARCH LICENSE。過去版の条件と分ける。 商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [tools/api_server.py](https://github.com/fishaudio/fish-speech/blob/befe4001745417f8c42131739d862b8a6fdbd15a/tools/api_server.py) / [tools/run_webui.py](https://github.com/fishaudio/fish-speech/blob/befe4001745417f8c42131739d862b8a6fdbd15a/tools/run_webui.py)

**最新GitHub Release**: [v1.5.1](https://github.com/fishaudio/fish-speech/releases/tag/v1.5.1) / 2025-05-31T12:15:00Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-22T08:55:48Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **メトリクス**: ★62,417、fork 6,691、作成 2024-01-14、最終push 2026-10-06T08:49:23Z、archived=False
- **確認**: 2026-09-09 / コミット `48b1a0169a28582a8984402f82cf438d3bfa6aca`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/RVC-Boss/GPT-SoVITS/tree/48b1a0169a28582a8984402f82cf438d3bfa6aca)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/RVC-Boss/GPT-SoVITS/blob/48b1a0169a28582a8984402f82cf438d3bfa6aca/README.md) / [GitHub API](https://api.github.com/repos/RVC-Boss/GPT-SoVITS) / [固定ツリー](https://github.com/RVC-Boss/GPT-SoVITS/tree/48b1a0169a28582a8984402f82cf438d3bfa6aca)

### 制作に使う際の検討

参照音声や少量学習でキャラ台詞を作る候補。短い参照例と長期運用する声モデルを区別する。

**次に確かめること（実施前）**: 日本語固有名詞、短文・長文、感情差、参照音の変更で再現性を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [api_v2.py](https://github.com/RVC-Boss/GPT-SoVITS/blob/48b1a0169a28582a8984402f82cf438d3bfa6aca/api_v2.py) / [webui.py](https://github.com/RVC-Boss/GPT-SoVITS/blob/48b1a0169a28582a8984402f82cf438d3bfa6aca/webui.py) / [install.sh](https://github.com/RVC-Boss/GPT-SoVITS/blob/48b1a0169a28582a8984402f82cf438d3bfa6aca/install.sh)

**最新GitHub Release**: [20250606v2pro](https://github.com/RVC-Boss/GPT-SoVITS/releases/tag/20250606v2pro) / 2025-06-06T03:04:27Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-18T09:16:25Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [lj1995/GPT-SoVITS](https://huggingface.co/lj1995/GPT-SoVITS) — file_listing_checked、確認日 2026-09-09、revision `336b2ec4e8d4ac74740798dd40af44e74659ecaf`。代表ファイル: `chinese-hubert-base/pytorch_model.bin`, `chinese-roberta-wwm-ext-large/pytorch_model.bin`, `gsv-v2final-pretrained/s1bert25hz-5kh-longer-epoch=12-step=369668.ckpt`, `gsv-v2final-pretrained/s2D2333k.pth`。gated=False。

<a id="index-tts"></a>

## IndexTTS

声質・感情の条件を扱う音声合成。現行2.5は日本語を含む5言語を案内。

- **リポジトリ**: https://github.com/index-tts/index-tts
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: テキスト、声質用参照、感情条件
- **出力**: 合成音声
- **環境**: uv管理環境、WebUIまたはCLI。版2と2.5でモデルディレクトリを分ける。
- **依存**: IndexTeam/IndexTTS-2.5、付随音声モデル
- **制約・未確認**: 2.5と2のPython API・モデルを混用しない。日本語対応は作者説明であり品質実測ではない。
- **編集者評価**: 日本語キャラクターの演技付き台詞に新しい比較対象。
- **メトリクス**: ★24,332、fork 2,884、作成 2025-02-06、最終push 2026-09-29T16:06:53Z、archived=False
- **確認**: 2026-09-09 / コミット `ee40fa7d6c6b8a2c7f06105f9f1e65775b74868c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/index-tts/index-tts/tree/ee40fa7d6c6b8a2c7f06105f9f1e65775b74868c)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/index-tts/index-tts/blob/ee40fa7d6c6b8a2c7f06105f9f1e65775b74868c/README.md) / [GitHub API](https://api.github.com/repos/index-tts/index-tts) / [固定ツリー](https://github.com/index-tts/index-tts/tree/ee40fa7d6c6b8a2c7f06105f9f1e65775b74868c)

### 制作に使う際の検討

日本語キャラクターの演技付き台詞に新しい比較対象。

**次に確かめること（実施前）**: 同じ台詞を平静・怒り・小声で生成し、感情の分離、固有名詞、長音を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [webui.py](https://github.com/index-tts/index-tts/blob/ee40fa7d6c6b8a2c7f06105f9f1e65775b74868c/webui.py) / [indextts/cli_v2.py](https://github.com/index-tts/index-tts/blob/ee40fa7d6c6b8a2c7f06105f9f1e65775b74868c/indextts/cli_v2.py)

**最新GitHub Release**: [v2.5.0](https://github.com/index-tts/index-tts/releases/tag/v2.5.0) / 2026-08-13T10:55:37Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-18T06:52:28Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [IndexTeam/IndexTTS-2.5](https://huggingface.co/IndexTeam/IndexTTS-2.5) — file_listing_checked、確認日 2026-09-09、revision `c39ce5ba981572cb187443877ff559dfb246ce63`。代表ファイル: `codec.pth`, `feat1.pt`, `feat2.pt`, `gpt.pth`。gated=False。

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
- **メトリクス**: ★13,668、fork 1,770、作成 2026-01-21、最終push 2026-03-17T06:38:41Z、archived=False
- **確認**: 2026-09-09 / コミット `022e286b98fbec7e1e916cb940cdf532cd9f488e`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/QwenLM/Qwen3-TTS/tree/022e286b98fbec7e1e916cb940cdf532cd9f488e)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/README.md) / [GitHub API](https://api.github.com/repos/QwenLM/Qwen3-TTS) / [固定ツリー](https://github.com/QwenLM/Qwen3-TTS/tree/022e286b98fbec7e1e916cb940cdf532cd9f488e)

### 制作に使う際の検討

声の設計・既定声・参照声のモデルを分けて選ぶ。会話キャラでは速度と日本語の自然さを両方見る。

**次に確かめること（実施前）**: CustomVoice/VoiceDesign/Base等から目的の版を選び、声の保持、指示追従、出力時間を比較する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [qwen_tts/cli/demo.py](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/cli/demo.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-03-17T06:38:41Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign) — file_listing_checked、確認日 2026-09-09、revision `5ecdb67327fd37bb2e042aab12ff7391903235d3`。代表ファイル: `model.safetensors`, `speech_tokenizer/model.safetensors`。gated=False。

<a id="retrieval-based-voice-conversion-webui"></a>

## RVC WebUI

入力音声の発話内容を保ちながら学習した声へ変換する。

- **リポジトリ**: https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 録音・歌声、対象声モデル、学習音声
- **出力**: 変換音声、声モデル
- **環境**: Python、CPU/CUDA別依存。
- **依存**: HuBERT等、音高推定器、別途用意する対象声モデル
- **制約・未確認**: TTSではなく声質変換。汎用の基盤ファイルだけでは任意の対象声が使えるわけではない。
- **編集者評価**: 自分で演じた台詞のタイミングを保持して声を変える工程に適する。
- **メトリクス**: ★38,622、fork 5,290、作成 2023-03-27、最終push 2026-08-04T07:47:32Z、archived=False
- **確認**: 2026-09-09 / コミット `81eed5e8f68b6bed1789f682fe78cdd324495afc`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/tree/81eed5e8f68b6bed1789f682fe78cdd324495afc)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/README.md) / [GitHub API](https://api.github.com/repos/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) / [固定ツリー](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/tree/81eed5e8f68b6bed1789f682fe78cdd324495afc)

### 制作に使う際の検討

自分で演じた台詞のタイミングを保持して声を変える工程に適する。

**次に確かめること（実施前）**: 無声音、息、歯擦音、歌の高音で変換前後を比較し、参照モデルの条件を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [infer/cli.py](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/infer/cli.py)

**最新GitHub Release**: [2.3.260718](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/releases/tag/2.3.260718) / 2026-07-21T02:28:49Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-04T07:47:05Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **メトリクス**: ★1,380、fork 220、作成 2023-12-01、最終push 2025-12-07T13:06:59Z、archived=False
- **確認**: 2026-09-09 / コミット `66de777e06392c0f313600be03c43ef96658b244`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/litagin02/Style-Bert-VITS2/tree/66de777e06392c0f313600be03c43ef96658b244)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/litagin02/Style-Bert-VITS2/blob/66de777e06392c0f313600be03c43ef96658b244/README.md) / [GitHub API](https://api.github.com/repos/litagin02/Style-Bert-VITS2) / [固定ツリー](https://github.com/litagin02/Style-Bert-VITS2/tree/66de777e06392c0f313600be03c43ef96658b244)

### 制作に使う際の検討

日本語の読みとスタイルを調整する制作用途。学習済み音源ごとの声の特徴と条件を保持する。

**次に確かめること（実施前）**: アクセント、長音、疑問文、スタイル混合を試し、辞書・設定と音声を保存する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [app.py](https://github.com/litagin02/Style-Bert-VITS2/blob/66de777e06392c0f313600be03c43ef96658b244/app.py)

**最新GitHub Release**: [2.7.0](https://github.com/litagin02/Style-Bert-VITS2/releases/tag/2.7.0) / 2025-08-24T03:01:47Z / prerelease=False

デフォルトブランチの確認コミット日時: 2025-08-24T03:04:16Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **メトリクス**: ★3,261、fork 377、作成 2021-07-27、最終push 2026-10-03T13:06:45Z、archived=False
- **確認**: 2026-09-09 / コミット `b7258250fe90c82f112d0f51e43f2a1b67992d36`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/VOICEVOX/voicevox/tree/b7258250fe90c82f112d0f51e43f2a1b67992d36)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/VOICEVOX/voicevox/blob/b7258250fe90c82f112d0f51e43f2a1b67992d36/README.md) / [GitHub API](https://api.github.com/repos/VOICEVOX/voicevox) / [固定ツリー](https://github.com/VOICEVOX/voicevox/tree/b7258250fe90c82f112d0f51e43f2a1b67992d36)

### 制作に使う際の検討

台詞をGUIで校正しやすい日本語音声編集の候補。UIのライセンスだけで話者の条件を判断しない。

**次に確かめること（実施前）**: 選んだ話者でアクセント・読み辞書・音声書き出しを試し、エンジン版と音源名を記録する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/main.ts](https://github.com/VOICEVOX/voicevox/blob/b7258250fe90c82f112d0f51e43f2a1b67992d36/src/main.ts)

**最新GitHub Release**: [0.25.2](https://github.com/VOICEVOX/voicevox/releases/tag/0.25.2) / 2026-04-30T08:12:22Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-07T10:12:56Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="genie-tts"></a>

## Genie-TTS

GPT-SoVITS（V2/V2ProPlus）をONNX化してCPUで動かす軽量推論エンジン。TTS推論・モデル変換・FastAPIサーバーをまとめて提供する。

- **リポジトリ**: https://github.com/High-Logic/Genie-TTS
- **分類**: model_toolkit / AIモデル・学習 / 活発・実用段階
- **入力**: テキスト、キャラクターのONNXモデル、参照音声
- **出力**: 合成音声、ONNXモデル、API応答
- **環境**: Python 3.10+、pip install genie-tts。初回に約391MBのリソースDL。モデル変換にはtorch。
- **依存**: GPT-SoVITSモデル、ONNXランタイム、torch（変換時）
- **制約・未確認**: READMEは対応モデルがV2/V2ProPlusで、V3/V4は未対応と記載。性能値は作者のCPU計測で環境依存。
- **編集者評価**: GPT-SoVITS系のキャラ音声を軽量に配備したいときに有用。日本語・英語・中国語・韓国語に対応とREADMEに記載。
- **メトリクス**: ★1,792、fork 123、作成 2025-08-25、最終push 2026-08-30T11:22:20Z、archived=False
- **確認**: 2026-10-06 / コミット `d347fd0f8683e9a362b69f59fa0a4799ddb5e828`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/High-Logic/Genie-TTS/tree/d347fd0f8683e9a362b69f59fa0a4799ddb5e828)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/High-Logic/Genie-TTS/blob/d347fd0f8683e9a362b69f59fa0a4799ddb5e828/README.md) / [GitHub API](https://api.github.com/repos/High-Logic/Genie-TTS) / [固定ツリー](https://github.com/High-Logic/Genie-TTS/tree/d347fd0f8683e9a362b69f59fa0a4799ddb5e828)

### 制作に使う際の検討

ローカル/サーバーでのキャラ音声合成API配備候補。

**次に確かめること（実施前）**: 手持ちのGPT-SoVITSモデルをONNX変換し、CPUでの生成速度と自然さを測る。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/High-Logic/Genie-TTS/blob/d347fd0f8683e9a362b69f59fa0a4799ddb5e828/README.md)

**最新GitHub Release**: [v2.0.2](https://github.com/High-Logic/Genie-TTS/releases/tag/v2.0.2) / 2025-12-12T08:17:20Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-30T11:22:20Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="tts-webui"></a>

## TTS-WebUI

多数のTTS/音声生成モデルを1つのGradio+React UIで扱うWebUI。GPT-SoVITS、XTTSv2、Kokoro、StyleTTS2、RVC、MusicGen、Demucs等の拡張を備える。

- **リポジトリ**: https://github.com/rsxdalv/TTS-WebUI
- **分類**: web_app / AIモデル・学習 / 活発・実用段階
- **入力**: テキスト、参照音声、音声ファイル
- **出力**: 合成音声、変換音声、生成音楽
- **環境**: インストーラまたはDocker、Colab。拡張ごとに個別の依存とモデルDL。
- **依存**: 各TTS/音楽モデル、Gradio、React、Docker（任意）
- **制約・未確認**: READMEはモデルごとに拡張が必要で、依存やライセンスは各モデルに従うと説明。動作はGPU/環境依存。
- **編集者評価**: 複数の音声系モデルを横断して試せるため、キャラ音声や歌声・音声変換の比較検討に使いやすい。
- **メトリクス**: ★3,282、fork 333、作成 2023-04-27、最終push 2026-09-07T08:54:58Z、archived=False
- **確認**: 2026-10-06 / コミット `2e5701387c423307d73972a45496bfdcb6a7d8e1`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/rsxdalv/TTS-WebUI/tree/2e5701387c423307d73972a45496bfdcb6a7d8e1)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/rsxdalv/TTS-WebUI/blob/2e5701387c423307d73972a45496bfdcb6a7d8e1/README.md) / [GitHub API](https://api.github.com/repos/rsxdalv/TTS-WebUI) / [固定ツリー](https://github.com/rsxdalv/TTS-WebUI/tree/2e5701387c423307d73972a45496bfdcb6a7d8e1)

### 制作に使う際の検討

音声制作の試作・比較環境の候補。

**次に確かめること（実施前）**: GPT-SoVITSとRVC拡張を有効化し、同一参照音声で生成品質と速度を比較する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [extensions/builtin/extension_conda_storage_optimizer/main.py](https://github.com/rsxdalv/TTS-WebUI/blob/2e5701387c423307d73972a45496bfdcb6a7d8e1/extensions/builtin/extension_conda_storage_optimizer/main.py) / [extensions/builtin/extension_custom_extensions_installer/main.py](https://github.com/rsxdalv/TTS-WebUI/blob/2e5701387c423307d73972a45496bfdcb6a7d8e1/extensions/builtin/extension_custom_extensions_installer/main.py) / [extensions/builtin/extension_decorator_save_ffmpeg/main.py](https://github.com/rsxdalv/TTS-WebUI/blob/2e5701387c423307d73972a45496bfdcb6a7d8e1/extensions/builtin/extension_decorator_save_ffmpeg/main.py)

**最新GitHub Release**: [v1.5.2](https://github.com/rsxdalv/TTS-WebUI/releases/tag/v1.5.2) / 2026-08-31T21:03:01Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-07T08:54:58Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="vits-simple-api"></a>

## vits-simple-api

VITS系TTSをHTTP APIとして提供するサーバー。VITS/Bert-VITS2/GPT-SoVITS/emotion-vits等の複数モデルを読み込み、GETで音声合成できる。

- **リポジトリ**: https://github.com/Artrajz/vits-simple-api
- **分類**: api_reference / AIモデル・学習 / 活発・実用段階
- **入力**: テキスト、モデルID、話者・感情パラメータ
- **出力**: 音声ファイル
- **環境**: Python 3.10推奨、requirements導入かDocker。モデルはdata/modelsに配置。
- **依存**: VITS系モデルファイル、BERT/感情モデル、Docker（任意）
- **制約・未確認**: ライセンスはAGPL-3.0。READMEはSSML対応が作業中と記載。モデルごとにクリーンアーと言語対応が異なる。
- **編集者評価**: 既存のVITS系キャラ音声モデルをAPI経由でアプリや配信に組み込みたいときに使いやすい。複数モデルの同時ロードと長文バッチ処理に対応。
- **メトリクス**: ★1,050、fork 134、作成 2023-03-13、最終push 2026-05-18T10:29:11Z、archived=False
- **確認**: 2026-10-06 / コミット `c3d179ffabff711e6697c6eb16298ac66a250406`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Artrajz/vits-simple-api/tree/c3d179ffabff711e6697c6eb16298ac66a250406)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Artrajz/vits-simple-api/blob/c3d179ffabff711e6697c6eb16298ac66a250406/README.md) / [GitHub API](https://api.github.com/repos/Artrajz/vits-simple-api) / [固定ツリー](https://github.com/Artrajz/vits-simple-api/tree/c3d179ffabff711e6697c6eb16298ac66a250406)

### 制作に使う際の検討

キャラ音声をAPIでサービス連携する工程の候補。

**次に確かめること（実施前）**: 手持ちVITSモデルを読み込み、複数話者でのAPI応答と言語処理を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [app.py](https://github.com/Artrajz/vits-simple-api/blob/c3d179ffabff711e6697c6eb16298ac66a250406/app.py) / [tts_app/static/js/index.js](https://github.com/Artrajz/vits-simple-api/blob/c3d179ffabff711e6697c6eb16298ac66a250406/tts_app/static/js/index.js)

**最新GitHub Release**: [v0.6.16](https://github.com/Artrajz/vits-simple-api/releases/tag/v0.6.16) / 2025-02-03T05:41:41Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-05-18T10:29:11Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
