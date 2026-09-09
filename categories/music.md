# 音楽・歌声合成

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) · [詳細](#ace-step-1.5) | ローカルで楽曲を生成し、編集や追加学習につなげる音楽モデル。 | AIモデル・学習 / 更新のある導入・評価候補 | 12,616 / 2026-09-03 |
| [DiffSinger](https://github.com/openvpi/DiffSinger) · [詳細](#diffsinger) | 歌声合成の学習・推論と、ピッチ・エネルギー・息成分などの制御を扱う。 | AIモデル・学習 / 更新のある導入・評価候補 | 3,201 / 2026-09-07 |
| [OpenUtau](https://github.com/openutau/OpenUtau) · [詳細](#openutau) | UTAUコミュニティ向けの歌声編集・合成プラットフォーム。 | AIは任意 / 定番の制作基盤 | 4,281 / 2026-09-09 |

<a id="ace-step-1.5"></a>

## ACE-Step-1.5

ローカルで楽曲を生成し、編集や追加学習につなげる音楽モデル。

- **リポジトリ**: https://github.com/ace-step/ACE-Step-1.5
- **分類**: model / AIモデル・学習 / 更新のある導入・評価候補
- **入力**: 楽曲説明、歌詞、参照音声等
- **出力**: 楽曲・歌声を含む音声
- **環境**: モデル・端末別の実行手順あり。XL版などでGPU要件が異なる。
- **依存**: ACE-Stepのモデル群、任意のLoRA
- **制約・未確認**: 作者の速度・商用モデル比較は当カタログで再検証していない。
- **編集者評価**: ゲームBGM・キャラソング・映像用音楽の試作候補。
- **メトリクス**: ★12,616、fork 1,619、作成 2025-09-04、最終push 2026-09-03T02:46:44Z、archived=False
- **確認**: 2026-09-09 / コミット `ca1e85fe9430179831e6bc6be790c332190a3866`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/LICENSE)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/README.md) / [GitHub API](https://api.github.com/repos/ace-step/ACE-Step-1.5) / [固定ツリー](https://github.com/ace-step/ACE-Step-1.5/tree/ca1e85fe9430179831e6bc6be790c332190a3866)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [ACE-Step/acestep-v15-xl-turbo](https://huggingface.co/ACE-Step/acestep-v15-xl-turbo) — file_listing_checked、確認日 2026-09-09、revision `d4a0b288b83ebb7e25a8c0b32c573c22e134e8ee`。代表ファイル: `model-00001-of-00004.safetensors`, `model-00002-of-00004.safetensors`, `model-00003-of-00004.safetensors`, `model-00004-of-00004.safetensors`。gated=False。

<a id="diffsinger"></a>

## DiffSinger

歌声合成の学習・推論と、ピッチ・エネルギー・息成分などの制御を扱う。

- **リポジトリ**: https://github.com/openvpi/DiffSinger
- **分類**: model_toolkit / AIモデル・学習 / 更新のある導入・評価候補
- **入力**: 音符、歌詞、音声データ、表現パラメータ
- **出力**: 合成歌声・音声モデル
- **環境**: Python/GPU環境。使用する音源の設定に依存。
- **依存**: DiffSinger対応モデル・ボコーダ
- **制約・未確認**: 原論文実装の拡張版。OpenUtau等のエディタと音源の対応は別途確認。
- **編集者評価**: 歌声の細かな表現と独自音源制作を検討する基盤。
- **メトリクス**: ★3,201、fork 348、作成 2022-08-03、最終push 2026-09-07T11:30:33Z、archived=False
- **確認**: 2026-09-09 / コミット `336cf01b57f2ad44c6b37a79cf33993043291759`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/openvpi/DiffSinger/blob/336cf01b57f2ad44c6b37a79cf33993043291759/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/openvpi/DiffSinger/blob/336cf01b57f2ad44c6b37a79cf33993043291759/README.md) / [GitHub API](https://api.github.com/repos/openvpi/DiffSinger) / [固定ツリー](https://github.com/openvpi/DiffSinger/tree/336cf01b57f2ad44c6b37a79cf33993043291759)

<a id="openutau"></a>

## OpenUtau

UTAUコミュニティ向けの歌声編集・合成プラットフォーム。

- **リポジトリ**: https://github.com/openutau/OpenUtau
- **分類**: desktop_tool / AIは任意 / 定番の制作基盤
- **入力**: 音符、歌詞、音源ライブラリ
- **出力**: 合成歌声・歌唱プロジェクト
- **環境**: 対応する歌声音源と合成エンジン。
- **依存**: UTAU系音源、対応するDiffSinger等
- **制約・未確認**: エディタと音源・合成モデルの条件を分ける。公式リポジトリはopenutau/OpenUtauへ移転。
- **編集者評価**: キャラソングや同人音楽で、音符と発音を編集する入口。
- **メトリクス**: ★4,281、fork 546、作成 2014-11-27、最終push 2026-09-09T06:52:33Z、archived=False
- **確認**: 2026-09-09 / コミット `17bf25e7f78c5f88a6c5bce437bf6d592f012e46`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/openutau/OpenUtau/blob/17bf25e7f78c5f88a6c5bce437bf6d592f012e46/LICENSE.txt)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/openutau/OpenUtau/blob/17bf25e7f78c5f88a6c5bce437bf6d592f012e46/README.md) / [GitHub API](https://api.github.com/repos/openutau/OpenUtau) / [固定ツリー](https://github.com/openutau/OpenUtau/tree/17bf25e7f78c5f88a6c5bce437bf6d592f012e46)
