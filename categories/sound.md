# ASMR・効果音・環境音

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-01。**117件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ASMRify](https://github.com/ReactorcoreGames/ASMRify) · [詳細](#asmrify) | 音声に定位移動・残響・ピッチ等を加えて一括処理するASMR向け音声加工ツール。 | AI出力の後処理 / 小規模・初期評価候補 | 1 / 2026-06-18 |
| [Audacity](https://github.com/audacity/audacity) · [詳細](#audacity) | 録音とマルチトラック編集を行う音声制作アプリ。 | 非AI制作 / 制作基盤として比較 | 18,609 / 2026-09-30 |
| [Binaural Speech Synthesis](https://github.com/facebookresearch/BinauralSpeechSynthesis) · [詳細](#binauralspeechsynthesis) | モノラル音声を空間条件に従うバイノーラル音声へ変換する研究。 | AIモデル・学習 / アーカイブ済み資料 | 190 / 2022-05-19 |
| [ControlFoley](https://github.com/xiaomi-research/controlfoley) · [詳細](#controlfoley) | 動画・テキスト・参照音を条件に、効果音とそのタイミングを制御する。 | AIモデル・学習 / 小規模・初期候補 | 153 / 2026-08-28 |
| [FoleyCrafter](https://github.com/open-mmlab/FoleyCrafter) · [詳細](#foleycrafter) | 動画の内容とタイミングに合わせた効果音を生成する研究実装。 | AIモデル・学習 / 研究モデルの評価候補 | 665 / 2026-06-15 |
| [MMAudio](https://github.com/hkchengrex/MMAudio) · [詳細](#mmaudio) | 動画やテキストを条件に、時間的に対応する音声を生成する。 | AIモデル・学習 / 研究モデルの評価候補 | 2,270 / 2026-02-23 |
| [stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools) · [詳細](#stable-audio-tools) | 条件付き音声生成モデルの学習と推論を行うツール群。効果音や環境音素材を検討できる。 | AIモデル・学習 / 更新のある導入・評価候補 | 3,871 / 2026-09-18 |
| [Steam Audio](https://github.com/ValveSoftware/steam-audio) · [詳細](#steam-audio) | ゲーム空間に合わせた音の定位・伝播を扱う空間音響SDK。 | 非AI制作 / 制作基盤として比較 | 2,955 / 2026-03-25 |
| [Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui) · [詳細](#ultimatevocalremovergui) | 音源分離モデルをGUIで使い、歌・伴奏等を分離する。 | AI連携 / 連携・制作ツール候補 | 26,449 / 2025-03-13 |

<a id="asmrify"></a>

## ASMRify

音声に定位移動・残響・ピッチ等を加えて一括処理するASMR向け音声加工ツール。

- **リポジトリ**: https://github.com/ReactorcoreGames/ASMRify
- **分類**: desktop_tool / AI出力の後処理 / 小規模・初期評価候補
- **入力**: 録音またはTTS音声ファイル
- **出力**: 効果処理したWAV・MP3
- **環境**: Windows 10/11、FFmpeg。
- **依存**: FFmpeg、入力音声
- **制約・未確認**: 小規模で利用実績は未確認。AIによるささやき生成・実録バイノーラルの再現・効果効能は確認していない。
- **編集者評価**: AIのTTS出力をASMR風の音声演出へ加工する周辺候補。
- **メトリクス**: ★1、fork 0、作成 2026-06-18、最終push 2026-06-18T22:47:00Z、archived=False
- **確認**: 2026-09-09 / コミット `5f30fc61e6148a537cdc609173880e2d50ae3b53`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/ReactorcoreGames/ASMRify/tree/5f30fc61e6148a537cdc609173880e2d50ae3b53)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ReactorcoreGames/ASMRify/blob/5f30fc61e6148a537cdc609173880e2d50ae3b53/README.md) / [GitHub API](https://api.github.com/repos/ReactorcoreGames/ASMRify) / [固定ツリー](https://github.com/ReactorcoreGames/ASMRify/tree/5f30fc61e6148a537cdc609173880e2d50ae3b53)

### 制作に使う際の検討

既存録音・TTSへフィルタや空間処理を加える後処理候補。ささやき声の生成成功と呼ばない。

**次に確かめること（実施前）**: 同じ音声で処理前後のノイズ、クリップ、左右差、モノラル互換を試聴する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [main.py](https://github.com/ReactorcoreGames/ASMRify/blob/5f30fc61e6148a537cdc609173880e2d50ae3b53/main.py) / [gui/app.py](https://github.com/ReactorcoreGames/ASMRify/blob/5f30fc61e6148a537cdc609173880e2d50ae3b53/gui/app.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-06-18T22:47:00Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="audacity"></a>

## Audacity

録音とマルチトラック編集を行う音声制作アプリ。

- **リポジトリ**: https://github.com/audacity/audacity
- **分類**: desktop_tool / 非AI制作 / 制作基盤として比較
- **入力**: 録音、TTS、効果音、楽曲
- **出力**: 編集済み音声プロジェクト・書き出し音声
- **環境**: Windows/macOS/Linux。安定配布と開発ブランチを区別。
- **依存**: 音声入出力機器、任意のプラグイン
- **制約・未確認**: 現masterはAudacity4への構造変更中。3.x用の導入・開発手順と混用しない。
- **編集者評価**: ASMR・台詞・効果音を実際に仕上げる録音編集工程。
- **メトリクス**: ★18,609、fork 2,675、作成 2015-03-26、最終push 2026-09-30T16:14:17Z、archived=False
- **確認**: 2026-09-09 / コミット `7c667777427b0e80c177caa6d3c46367901fc775`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/audacity/audacity/tree/7c667777427b0e80c177caa6d3c46367901fc775)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/audacity/audacity/blob/7c667777427b0e80c177caa6d3c46367901fc775/README.md) / [GitHub API](https://api.github.com/repos/audacity/audacity) / [固定ツリー](https://github.com/audacity/audacity/tree/7c667777427b0e80c177caa6d3c46367901fc775)

### 制作に使う際の検討

ASMR・台詞・効果音を実際に仕上げる録音編集工程。

**次に確かめること（実施前）**: クリップ境界、ノイズ、左右バランス、ピーク、書き出し後の長さを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/app/main.cpp](https://github.com/audacity/audacity/blob/7c667777427b0e80c177caa6d3c46367901fc775/src/app/main.cpp) / [tools/translations/run_lupdate.sh](https://github.com/audacity/audacity/blob/7c667777427b0e80c177caa6d3c46367901fc775/tools/translations/run_lupdate.sh)

**最新GitHub Release**: [Audacity-4.0.1](https://github.com/audacity/audacity/releases/tag/Audacity-4.0.1) / 2026-09-30T11:59:48Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T16:05:35Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="binauralspeechsynthesis"></a>

## Binaural Speech Synthesis

モノラル音声を空間条件に従うバイノーラル音声へ変換する研究。

- **リポジトリ**: https://github.com/facebookresearch/BinauralSpeechSynthesis
- **分類**: model_toolkit / AIモデル・学習 / アーカイブ済み資料
- **入力**: モノ音声、話者と聴取者の幾何情報
- **出力**: 左右2chの空間音声
- **環境**: 研究用Python/PyTorch環境。学習・評価コードを掲載。
- **依存**: 作者データセットとモデル設定
- **制約・未確認**: 2021年研究、最終push2022年。現在の主流TTSやASMR専用モデルではない。READMEに非商用条件。
- **編集者評価**: 耳元表現の学習型レンダリングを理解する比較基準として残す。
- **メトリクス**: ★190、fork 21、作成 2021-03-09、最終push 2022-05-19T20:44:09Z、archived=True
- **確認**: 2026-09-09 / コミット `81d0765ae590e8f69d3d26dc03f8a2e9c02b7d03`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/facebookresearch/BinauralSpeechSynthesis/tree/81d0765ae590e8f69d3d26dc03f8a2e9c02b7d03)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/facebookresearch/BinauralSpeechSynthesis/blob/81d0765ae590e8f69d3d26dc03f8a2e9c02b7d03/README.md) / [GitHub API](https://api.github.com/repos/facebookresearch/BinauralSpeechSynthesis) / [固定ツリー](https://github.com/facebookresearch/BinauralSpeechSynthesis/tree/81d0765ae590e8f69d3d26dc03f8a2e9c02b7d03)

### 制作に使う際の検討

耳元表現の学習型レンダリングを理解する比較基準として残す。

**次に確かめること（実施前）**: 幾何情報を固定して左右移動を評価し、汎用ステレオ拡張との違いを試聴する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [evaluate.py](https://github.com/facebookresearch/BinauralSpeechSynthesis/blob/81d0765ae590e8f69d3d26dc03f8a2e9c02b7d03/evaluate.py) / [train.py](https://github.com/facebookresearch/BinauralSpeechSynthesis/blob/81d0765ae590e8f69d3d26dc03f8a2e9c02b7d03/train.py)

**最新GitHub Release**: [video_v1.0](https://github.com/facebookresearch/BinauralSpeechSynthesis/releases/tag/video_v1.0) / 2021-06-21T16:43:12Z / prerelease=False

デフォルトブランチの確認コミット日時: 2022-05-19T20:44:00Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="controlfoley"></a>

## ControlFoley

動画・テキスト・参照音を条件に、効果音とそのタイミングを制御する。

- **リポジトリ**: https://github.com/xiaomi-research/controlfoley
- **分類**: model / AIモデル・学習 / 小規模・初期候補
- **入力**: 動画、文章、任意の参照音声
- **出力**: 効果音、音声付き動画
- **環境**: Python/PyTorch、demo.py。モデルと外部特徴抽出重みが必要。
- **依存**: ControlFoley、音声・映像特徴抽出器
- **制約・未確認**: コードApache-2.0、重みCC BY-NC 4.0。ASMR専用・台詞合成モデルではない。
- **編集者評価**: 接触音や環境音を映像の動きに合わせる工程でMMAudioと比較したい。
- **メトリクス**: ★153、fork 5、作成 2026-04-14、最終push 2026-08-28T01:54:55Z、archived=False
- **確認**: 2026-09-09 / コミット `b6c902888d45d75f022e253e3db29836360a3f82`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/xiaomi-research/controlfoley/tree/b6c902888d45d75f022e253e3db29836360a3f82)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/xiaomi-research/controlfoley/blob/b6c902888d45d75f022e253e3db29836360a3f82/README.md) / [GitHub API](https://api.github.com/repos/xiaomi-research/controlfoley) / [固定ツリー](https://github.com/xiaomi-research/controlfoley/tree/b6c902888d45d75f022e253e3db29836360a3f82)

### 制作に使う際の検討

接触音や環境音を映像の動きに合わせる工程でMMAudioと比較したい。

**次に確かめること（実施前）**: 同じ映像で参照音・時刻条件を変え、音の種類と発音タイミングを独立評価する。

**利用条件の確認メモ**: READMEでコードApache-2.0、重みCC BY-NC 4.0と区別。 商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [demo.py](https://github.com/xiaomi-research/controlfoley/blob/b6c902888d45d75f022e253e3db29836360a3f82/demo.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-28T01:54:52Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

本文を確認した箇所:

- [demo.py](https://github.com/xiaomi-research/controlfoley/blob/b6c902888d45d75f022e253e3db29836360a3f82/demo.py): video/audio/prompt/durationを受け取り推論設定へ渡すCLI部分を確認。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [YJX-Xiaomi/ControlFoley](https://huggingface.co/YJX-Xiaomi/ControlFoley) — file_listing_checked、確認日 2026-09-09、revision `cde633f5c3f5ccbedf07994ad6dc124b761df22f`。代表ファイル: `weights/controlfoley.pth`。gated=False。

<a id="foleycrafter"></a>

## FoleyCrafter

動画の内容とタイミングに合わせた効果音を生成する研究実装。

- **リポジトリ**: https://github.com/open-mmlab/FoleyCrafter
- **分類**: model / AIモデル・学習 / 研究モデルの評価候補
- **入力**: 無音動画、テキスト条件
- **出力**: 動画に合わせた効果音
- **環境**: Python/GPU環境、推論時のチェックポイント取得。
- **依存**: FoleyCrafterと基盤音声モデル
- **制約・未確認**: ASMR専用ではなく、距離感・耳元表現・立体音響は未検証。
- **編集者評価**: アニメ・ゲーム映像のフォーリー制作候補。
- **メトリクス**: ★665、fork 67、作成 2024-06-25、最終push 2026-06-15T04:39:18Z、archived=False
- **確認**: 2026-09-09 / コミット `b4526d1586aaf044140b359295504452297f8c13`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/open-mmlab/FoleyCrafter/tree/b4526d1586aaf044140b359295504452297f8c13)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/open-mmlab/FoleyCrafter/blob/b4526d1586aaf044140b359295504452297f8c13/README.md) / [GitHub API](https://api.github.com/repos/open-mmlab/FoleyCrafter) / [固定ツリー](https://github.com/open-mmlab/FoleyCrafter/tree/b4526d1586aaf044140b359295504452297f8c13)

### 制作に使う際の検討

無音動画の効果音を作る比較基準。台詞やBGMの制作は別工程に分ける。

**次に確かめること（実施前）**: 打撃・足音・環境音の短い動画で、音の種類、開始時刻、映像外の余計な音を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [inference.py](https://github.com/open-mmlab/FoleyCrafter/blob/b4526d1586aaf044140b359295504452297f8c13/inference.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-06-15T04:39:17Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [ymzhang319/FoleyCrafter](https://huggingface.co/ymzhang319/FoleyCrafter) — file_listing_checked、確認日 2026-09-09、revision `56c5ba7e052249a10bca6ebd12f9d5d8e6c26ae0`。代表ファイル: `semantic/semantic_adapter.bin`, `temporal_adapter.ckpt`, `vocoder/vocoder.pt`。gated=False。

<a id="mmaudio"></a>

## MMAudio

動画やテキストを条件に、時間的に対応する音声を生成する。

- **リポジトリ**: https://github.com/hkchengrex/MMAudio
- **分類**: model / AIモデル・学習 / 研究モデルの評価候補
- **入力**: 動画、テキスト
- **出力**: 同期音声
- **環境**: Python/GPU環境とチェックポイント。
- **依存**: MMAudio、音声VAE等
- **制約・未確認**: ASMRや日本語のセリフ生成専用ではない。音の同期と内容は素材ごとに評価する。
- **編集者評価**: 映像用の効果音・環境音を作る技術候補。
- **メトリクス**: ★2,270、fork 268、作成 2024-12-07、最終push 2026-02-23T06:09:19Z、archived=False
- **確認**: 2026-09-09 / コミット `974010a026c731054592d8f777218bd9d85a6c24`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/hkchengrex/MMAudio/tree/974010a026c731054592d8f777218bd9d85a6c24)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/hkchengrex/MMAudio/blob/974010a026c731054592d8f777218bd9d85a6c24/README.md) / [GitHub API](https://api.github.com/repos/hkchengrex/MMAudio) / [固定ツリー](https://github.com/hkchengrex/MMAudio/tree/974010a026c731054592d8f777218bd9d85a6c24)

### 制作に使う際の検討

映像と文章から効果音を合わせる候補。参照音や時刻制御を重視する場合はControlFoleyとも比較する。

**次に確かめること（実施前）**: 同じ動画・同じ文章を複数seedで生成し、同期、音質、不要な声の混入を評価する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [demo.py](https://github.com/hkchengrex/MMAudio/blob/974010a026c731054592d8f777218bd9d85a6c24/demo.py) / [batch_eval.py](https://github.com/hkchengrex/MMAudio/blob/974010a026c731054592d8f777218bd9d85a6c24/batch_eval.py)

**最新GitHub Release**: [v0.1](https://github.com/hkchengrex/MMAudio/releases/tag/v0.1) / 2024-12-07T19:33:18Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-02-23T06:09:17Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [hkchengrex/MMAudio](https://huggingface.co/hkchengrex/MMAudio) — file_listing_checked、確認日 2026-09-09、revision `eb13a1a98fdbec91753775c57b074ccdfc60587c`。代表ファイル: `checkpoints/mmaudio_large_44k_ckpt.pth`, `checkpoints/mmaudio_medium_44k_ckpt.pth`, `checkpoints/mmaudio_small_16k_ckpt.pth`, `checkpoints/mmaudio_small_44k_ckpt.pth`。gated=False。

<a id="stable-audio-tools"></a>

## stable-audio-tools

条件付き音声生成モデルの学習と推論を行うツール群。効果音や環境音素材を検討できる。

- **リポジトリ**: https://github.com/Stability-AI/stable-audio-tools
- **分類**: model_toolkit / AIモデル・学習 / 更新のある導入・評価候補
- **入力**: テキスト条件、音声、モデル設定
- **出力**: 生成音声・学習済みモデル
- **環境**: Python、PyTorch。モデルごとに必要環境を確認。
- **依存**: Stable Audio Openなど対応モデル
- **制約・未確認**: ASMR専用モデルではない。空間音響・ささやきの品質は未検証。
- **編集者評価**: 音声素材の生成・追加学習を同じ基盤で扱う。
- **メトリクス**: ★3,871、fork 486、作成 2023-05-23、最終push 2026-09-18T22:33:51Z、archived=False
- **確認**: 2026-09-09 / コミット `3241adba4fc2a85cf5b29d9eb68d42f40a28e820`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Stability-AI/stable-audio-tools/tree/3241adba4fc2a85cf5b29d9eb68d42f40a28e820)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Stability-AI/stable-audio-tools/blob/3241adba4fc2a85cf5b29d9eb68d42f40a28e820/README.md) / [GitHub API](https://api.github.com/repos/Stability-AI/stable-audio-tools) / [固定ツリー](https://github.com/Stability-AI/stable-audio-tools/tree/3241adba4fc2a85cf5b29d9eb68d42f40a28e820)

### 制作に使う際の検討

音声生成と学習の基盤。Toolsのコード条件と使用する音声モデルの公開条件は別管理する。

**次に確かめること（実施前）**: 対象チェックポイントを一つ選び、長さ・サンプルレート・ループ境界・プロンプト追従を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [run_gradio.py](https://github.com/Stability-AI/stable-audio-tools/blob/3241adba4fc2a85cf5b29d9eb68d42f40a28e820/run_gradio.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-05-26T23:34:41Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [stabilityai/stable-audio-open-1.0](https://huggingface.co/stabilityai/stable-audio-open-1.0) — file_listing_checked、確認日 2026-09-09、revision `f21265c1e2710b3bd2386596943f0007f55f802e`。代表ファイル: `model.ckpt`, `model.safetensors`, `projection_model/diffusion_pytorch_model.safetensors`, `text_encoder/model.safetensors`。gated=auto。

<a id="steam-audio"></a>

## Steam Audio

ゲーム空間に合わせた音の定位・伝播を扱う空間音響SDK。

- **リポジトリ**: https://github.com/ValveSoftware/steam-audio
- **分類**: library / 非AI制作 / 制作基盤として比較
- **入力**: 音源、リスナー位置、シーン形状
- **出力**: 空間化された音声出力
- **環境**: Windows/Linux/macOS/モバイル。Unity/Unreal等の統合。
- **依存**: ホストエンジン、シーン・音響設定
- **制約・未確認**: ニューラルASMR生成や収録音声の声質生成ではない。HRTFと再生環境で印象が変わる。
- **編集者評価**: VR・耳元会話・環境音の位置制御に接続しやすい非AI基盤。
- **メトリクス**: ★2,955、fork 257、作成 2017-01-26、最終push 2026-03-25T17:13:21Z、archived=False
- **確認**: 2026-09-09 / コミット `480dd64f513cc8a6437e7d5b9eb0d3f1d30c2fac`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/ValveSoftware/steam-audio/tree/480dd64f513cc8a6437e7d5b9eb0d3f1d30c2fac)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ValveSoftware/steam-audio/blob/480dd64f513cc8a6437e7d5b9eb0d3f1d30c2fac/README.md) / [GitHub API](https://api.github.com/repos/ValveSoftware/steam-audio) / [固定ツリー](https://github.com/ValveSoftware/steam-audio/tree/480dd64f513cc8a6437e7d5b9eb0d3f1d30c2fac)

### 制作に使う際の検討

VR・耳元会話・環境音の位置制御に接続しやすい非AI基盤。

**次に確かめること（実施前）**: 音源の前後・左右・距離を動かし、ヘッドホンで定位と遮蔽・残響の変化を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [core/src/core/api_binaural_effect.cpp](https://github.com/ValveSoftware/steam-audio/blob/480dd64f513cc8a6437e7d5b9eb0d3f1d30c2fac/core/src/core/api_binaural_effect.cpp)

**最新GitHub Release**: [v4.8.1](https://github.com/ValveSoftware/steam-audio/releases/tag/v4.8.1) / 2026-02-11T18:43:55Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-03-25T17:13:21Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="ultimatevocalremovergui"></a>

## Ultimate Vocal Remover

音源分離モデルをGUIで使い、歌・伴奏等を分離する。

- **リポジトリ**: https://github.com/Anjok07/ultimatevocalremovergui
- **分類**: desktop_tool / AI連携 / 連携・制作ツール候補
- **入力**: ミックス音源
- **出力**: 分離された音声・伴奏
- **環境**: OS別配布あり。READMEのGPU最低目安6GB、推奨8GB以上。
- **依存**: UVR系モデル、選択によりDemucs
- **制約・未確認**: 分離は完全ではなく、残響や楽器の漏れが残る可能性。2025年からコード更新が少ない。
- **編集者評価**: 歌唱分析、台詞の抽出、既存音の整理の前処理候補。
- **メトリクス**: ★26,449、fork 2,019、作成 2020-07-20、最終push 2025-03-13T21:44:03Z、archived=False
- **確認**: 2026-09-09 / コミット `5517e0cf0d1acd16a1618eeedec596957523f9e1`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Anjok07/ultimatevocalremovergui/tree/5517e0cf0d1acd16a1618eeedec596957523f9e1)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Anjok07/ultimatevocalremovergui/blob/5517e0cf0d1acd16a1618eeedec596957523f9e1/README.md) / [GitHub API](https://api.github.com/repos/Anjok07/ultimatevocalremovergui) / [固定ツリー](https://github.com/Anjok07/ultimatevocalremovergui/tree/5517e0cf0d1acd16a1618eeedec596957523f9e1)

### 制作に使う際の検討

歌唱分析、台詞の抽出、既存音の整理の前処理候補。

**次に確かめること（実施前）**: ボーカル残り、打楽器の欠落、位相感を試聴し、分離前後の長さも照合する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [UVR.py](https://github.com/Anjok07/ultimatevocalremovergui/blob/5517e0cf0d1acd16a1618eeedec596957523f9e1/UVR.py) / [gui_data/app_size_values.py](https://github.com/Anjok07/ultimatevocalremovergui/blob/5517e0cf0d1acd16a1618eeedec596957523f9e1/gui_data/app_size_values.py)

**最新GitHub Release**: [v5.6](https://github.com/Anjok07/ultimatevocalremovergui/releases/tag/v5.6) / 2023-09-26T02:29:28Z / prerelease=False

デフォルトブランチの確認コミット日時: 2025-03-13T21:44:03Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。
