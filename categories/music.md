# 音楽・歌声合成

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-04。**167件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) · [詳細](#ace-step-1.5) | ローカルで楽曲を生成し、編集や追加学習につなげる音楽モデル。 | AIモデル・学習 / 更新のある導入・評価候補 | 13,033 / 2026-10-01 |
| [Basic Pitch](https://github.com/spotify/basic-pitch) · [詳細](#basic-pitch) | 音声を音高ベンド付きMIDIへ変換する軽量な採譜モデル。 | AIモデル・学習 / 連携・制作ツール候補 | 5,663 / 2025-11-13 |
| [DiffSinger](https://github.com/openvpi/DiffSinger) · [詳細](#diffsinger) | 歌声合成の学習・推論と、ピッチ・エネルギー・息成分などの制御を扱う。 | AIモデル・学習 / 更新のある導入・評価候補 | 3,216 / 2026-09-26 |
| [OpenUtau](https://github.com/openutau/OpenUtau) · [詳細](#openutau) | UTAUコミュニティ向けの歌声編集・合成プラットフォーム。 | AIは任意 / 定番の制作基盤 | 4,369 / 2026-10-04 |
| [SOFA](https://github.com/qiuqiao/SOFA) · [詳細](#sofa) | 歌声向けの強制アラインメントで歌詞・音素の時間位置を求める。 | AIモデル・学習 / モデル・研究候補 | 240 / 2026-09-02 |
| [YuE2](https://github.com/multimodal-art-projection/YuE) · [詳細](#yue) | 歌詞と曲調から編集可能な旋律・和音計画を作り、歌と伴奏へ展開する。 | AIモデル・学習 / モデル・研究候補 | 10,815 / 2026-10-02 |
| [OpenUtauMobile](https://github.com/vocoder712/OpenUtauMobile) · [詳細](#openutaumobile) | モバイル向けのオープンソース歌声合成エディタ。OpenUtau CoreをベースにUSTXプロジェクトファイルを扱い、DiffSinger／UTAU／Vogenの音源を読み込める。 | AI連携 / 初期評価候補 | 328 / 2026-10-03 |
| [SoulX-Singer](https://github.com/Soul-AILab/SoulX-Singer) · [詳細](#soulx-singer) | 未見の歌声を生成するゼロショット歌声合成（SVS）モデルの公式推論コード。メロディ（F0）条件と楽譜（MIDI）条件に対応し、歌声変換（SVC）版も提供する。 | AIモデル・学習 / モデル候補 | 979 / 2026-05-29 |
| [DiffSinger](https://github.com/MoonInTheRiver/DiffSinger) · [詳細](#moonintheriver-diffsinger) | Shallow Diffusion機構を用いた歌声合成（DiffSinger）と音声合成（DiffSpeech）の公式PyTorch実装。歌詞+MIDI/F0からメルへ、メルから波形へ変換する複数構成を提供する。 | AIモデル・学習 / 確立した参照実装 | 4,875 / 2026-07-24 |

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
- **メトリクス**: ★13,033、fork 1,672、作成 2025-09-04、最終push 2026-10-01T09:56:56Z、archived=False
- **確認**: 2026-09-09 / コミット `ca1e85fe9430179831e6bc6be790c332190a3866`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/ace-step/ACE-Step-1.5/tree/ca1e85fe9430179831e6bc6be790c332190a3866)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/README.md) / [GitHub API](https://api.github.com/repos/ace-step/ACE-Step-1.5) / [固定ツリー](https://github.com/ace-step/ACE-Step-1.5/tree/ca1e85fe9430179831e6bc6be790c332190a3866)

### 制作に使う際の検討

歌詞付き楽曲を試作する候補。編集可能な音符を重視するなら歌声エディタやYuE2の計画機構とも比較する。

**次に確かめること（実施前）**: 日本語歌詞の脱落、サビの繰り返し、参照音の反映、長さ指定、書き出しを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [acestep/api_server.py](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api_server.py) / [profile_inference.py](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/profile_inference.py)

**最新GitHub Release**: [v0.1.8](https://github.com/ace-step/ACE-Step-1.5/releases/tag/v0.1.8) / 2026-05-18T14:04:34Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-29T08:25:18Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [ACE-Step/acestep-v15-xl-turbo](https://huggingface.co/ACE-Step/acestep-v15-xl-turbo) — file_listing_checked、確認日 2026-09-09、revision `d4a0b288b83ebb7e25a8c0b32c573c22e134e8ee`。代表ファイル: `model-00001-of-00004.safetensors`, `model-00002-of-00004.safetensors`, `model-00003-of-00004.safetensors`, `model-00004-of-00004.safetensors`。gated=False。

<a id="basic-pitch"></a>

## Basic Pitch

音声を音高ベンド付きMIDIへ変換する軽量な採譜モデル。

- **リポジトリ**: https://github.com/spotify/basic-pitch
- **分類**: library / AIモデル・学習 / 連携・制作ツール候補
- **入力**: 楽器等の音声
- **出力**: MIDI、音符・音高情報
- **環境**: Python対応版、TensorFlow/ONNX等のランタイム。
- **依存**: 同梱・配布モデル、音声処理ライブラリ
- **制約・未確認**: 作者は単一楽器での利用を推奨。全楽曲から完全な編曲譜が取れるわけではない。
- **編集者評価**: 作った旋律をノート編集や再演奏へ戻す補助工程に向く。
- **メトリクス**: ★5,663、fork 519、作成 2022-05-03、最終push 2025-11-13T14:40:46Z、archived=False
- **確認**: 2026-09-09 / コミット `fa5997af0a8210982619003269994a1be25eddf3`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/spotify/basic-pitch/tree/fa5997af0a8210982619003269994a1be25eddf3)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/README.md) / [GitHub API](https://api.github.com/repos/spotify/basic-pitch) / [固定ツリー](https://github.com/spotify/basic-pitch/tree/fa5997af0a8210982619003269994a1be25eddf3)

### 制作に使う際の検討

作った旋律をノート編集や再演奏へ戻す補助工程に向く。

**次に確かめること（実施前）**: 単音と和音で音高・開始時刻・長さを比較し、ボーカル分離の有無も試す。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [basic_pitch/inference.py](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/basic_pitch/inference.py) / [setup.py](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/setup.py)

**最新GitHub Release**: [v0.4.0](https://github.com/spotify/basic-pitch/releases/tag/v0.4.0) / 2024-08-16T17:16:26Z / prerelease=False

デフォルトブランチの確認コミット日時: 2025-11-13T14:40:45Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **メトリクス**: ★3,216、fork 352、作成 2022-08-03、最終push 2026-09-26T15:16:51Z、archived=False
- **確認**: 2026-09-09 / コミット `336cf01b57f2ad44c6b37a79cf33993043291759`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/openvpi/DiffSinger/tree/336cf01b57f2ad44c6b37a79cf33993043291759)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/openvpi/DiffSinger/blob/336cf01b57f2ad44c6b37a79cf33993043291759/README.md) / [GitHub API](https://api.github.com/repos/openvpi/DiffSinger) / [固定ツリー](https://github.com/openvpi/DiffSinger/tree/336cf01b57f2ad44c6b37a79cf33993043291759)

### 制作に使う際の検討

音符と歌詞に沿って歌わせる制作モデル群。自動作曲・歌詞付き音源の一括生成とは制御粒度が異なる。

**次に確かめること（実施前）**: 対応音源とエディタでピッチ、ビブラート、音素長、ブレスの反映を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [scripts/infer.py](https://github.com/openvpi/DiffSinger/blob/336cf01b57f2ad44c6b37a79cf33993043291759/scripts/infer.py) / [utils/infer_utils.py](https://github.com/openvpi/DiffSinger/blob/336cf01b57f2ad44c6b37a79cf33993043291759/utils/infer_utils.py)

**最新GitHub Release**: [v2.5.1](https://github.com/openvpi/DiffSinger/releases/tag/v2.5.1) / 2026-01-08T09:03:01Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-03T08:32:45Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **メトリクス**: ★4,369、fork 558、作成 2014-11-27、最終push 2026-10-04T14:05:53Z、archived=False
- **確認**: 2026-09-09 / コミット `17bf25e7f78c5f88a6c5bce437bf6d592f012e46`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/openutau/OpenUtau/tree/17bf25e7f78c5f88a6c5bce437bf6d592f012e46)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/openutau/OpenUtau/blob/17bf25e7f78c5f88a6c5bce437bf6d592f012e46/README.md) / [GitHub API](https://api.github.com/repos/openutau/OpenUtau) / [固定ツリー](https://github.com/openutau/OpenUtau/tree/17bf25e7f78c5f88a6c5bce437bf6d592f012e46)

### 制作に使う際の検討

音符と発音を人が編集する歌声制作の中心。音源とレンダラーの互換性を明示して使う。

**次に確かめること（実施前）**: 音源形式を固定し、日本語歌詞、音素境界、ピッチ修正、wav書き出しを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [OpenUtau/App.axaml.cs](https://github.com/openutau/OpenUtau/blob/17bf25e7f78c5f88a6c5bce437bf6d592f012e46/OpenUtau/App.axaml.cs)

**最新GitHub Release**: [0.1.565](https://github.com/openutau/OpenUtau/releases/tag/0.1.565) / 2025-09-14T03:17:06Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T04:00:03Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="sofa"></a>

## SOFA

歌声向けの強制アラインメントで歌詞・音素の時間位置を求める。

- **リポジトリ**: https://github.com/qiuqiao/SOFA
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 歌声音声、歌詞・発音辞書
- **出力**: 音素境界等のアラインメント
- **環境**: READMEはPython3.8。infer.pyとONNX推論経路。
- **依存**: 配布チェックポイント、対象言語の辞書
- **制約・未確認**: 歌声生成器ではない。辞書と歌唱発音の差が結果に影響する。
- **編集者評価**: DiffSinger等の学習データ準備と歌詞タイミングの整備に有用。
- **メトリクス**: ★240、fork 34、作成 2023-09-15、最終push 2026-09-02T12:39:58Z、archived=False
- **確認**: 2026-09-09 / コミット `9549c6a86d16019c817eefe4bb8183405da524cc`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/qiuqiao/SOFA/tree/9549c6a86d16019c817eefe4bb8183405da524cc)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/qiuqiao/SOFA/blob/9549c6a86d16019c817eefe4bb8183405da524cc/README.MD) / [GitHub API](https://api.github.com/repos/qiuqiao/SOFA) / [固定ツリー](https://github.com/qiuqiao/SOFA/tree/9549c6a86d16019c817eefe4bb8183405da524cc)

### 制作に使う際の検討

DiffSinger等の学習データ準備と歌詞タイミングの整備に有用。

**次に確かめること（実施前）**: 伸ばす母音、促音、子音先行を含む歌で境界を人手注釈と比較する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [infer.py](https://github.com/qiuqiao/SOFA/blob/9549c6a86d16019c817eefe4bb8183405da524cc/infer.py) / [binarize.py](https://github.com/qiuqiao/SOFA/blob/9549c6a86d16019c817eefe4bb8183405da524cc/binarize.py) / [train.py](https://github.com/qiuqiao/SOFA/blob/9549c6a86d16019c817eefe4bb8183405da524cc/train.py)

**最新GitHub Release**: [v1.0.3](https://github.com/qiuqiao/SOFA/releases/tag/v1.0.3) / 2024-08-04T07:11:15Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-02T12:39:57Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="yue"></a>

## YuE2

歌詞と曲調から編集可能な旋律・和音計画を作り、歌と伴奏へ展開する。

- **リポジトリ**: https://github.com/multimodal-art-projection/YuE
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 歌詞、曲調、任意の楽譜・参照録音
- **出力**: 楽曲計画、48kHzステレオ楽曲
- **環境**: Linux、Python3.12、BF16対応NVIDIA24GBを作者が案内。
- **依存**: YuE2-3B、YuE2-Vae、カバー用途ではSheetSage2等
- **制約・未確認**: 現在のmainはYuE2で、コード・重みCC BY-NC 4.0。YuE-v1の旧条件を引き継がない。日本語は今回確認したカードの記載言語外。
- **編集者評価**: 生成前に旋律・和音を編集する曲作りの候補。歌声エディタとは出力制御が異なる。
- **メトリクス**: ★10,815、fork 1,238、作成 2025-01-23、最終push 2026-10-02T16:29:34Z、archived=False
- **確認**: 2026-09-09 / コミット `6332efcafa5f792df81812acc3b0f20b80b855cf`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/multimodal-art-projection/YuE/tree/6332efcafa5f792df81812acc3b0f20b80b855cf)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/multimodal-art-projection/YuE/blob/6332efcafa5f792df81812acc3b0f20b80b855cf/README.md) / [GitHub API](https://api.github.com/repos/multimodal-art-projection/YuE) / [固定ツリー](https://github.com/multimodal-art-projection/YuE/tree/6332efcafa5f792df81812acc3b0f20b80b855cf)

### 制作に使う際の検討

生成前に旋律・和音を編集する曲作りの候補。歌声エディタとは出力制御が異なる。

**次に確かめること（実施前）**: 和音・旋律だけを変更した時の音の反映、歌詞対応、同じ計画の再生成差を比較する。

**利用条件の確認メモ**: 現在のYuE2はコード・重みCC BY-NC 4.0。旧YuE-v1は別ブランチ・別条件。 商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [examples/generate.py](https://github.com/multimodal-art-projection/YuE/blob/6332efcafa5f792df81812acc3b0f20b80b855cf/examples/generate.py)

**最新GitHub Release**: [yue2-v0.1.6](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-v0.1.6) / 2026-09-09T19:10:05Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T19:38:47Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: editorial_comparison → ace-step-1.5（編集者による比較候補、接続実行は未検証）

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [m-a-p/YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B) — file_listing_checked、確認日 2026-09-09、revision `1a96eca688d6ae5d7f0feb88573fec89920fcd19`。代表ファイル: `model.safetensors`。gated=False。

<a id="openutaumobile"></a>

## OpenUtauMobile

モバイル向けのオープンソース歌声合成エディタ。OpenUtau CoreをベースにUSTXプロジェクトファイルを扱い、DiffSinger／UTAU／Vogenの音源を読み込める。

- **リポジトリ**: https://github.com/vocoder712/OpenUtauMobile
- **分類**: desktop_tool / AI連携 / 初期評価候補
- **入力**: USTXプロジェクト、歌声音源（ZIP）、歌詞と音符
- **出力**: 歌声の合成結果、USTXファイル
- **環境**: Android 5.0以上。iOSは.NET 9 SDK・MAUI・Xcode 15以降を備えたmacOSでの自前ビルドが必要。音源は別途入手する。
- **依存**: OpenUtau Core、DiffSinger／UTAU／Vogen音源
- **制約・未確認**: READMEは現状かなり不安定でメモリ管理問題が起きうるとして頻繁な保存を推奨。非公式アプリであり、公式OpenUtauを名乗ってはいけない。他音源形式の動作は非保証。
- **編集者評価**: スマートフォンでDiffSinger系音源を使える点が実用的。V2書き換え中でmasterはlegacy扱いとの注意がある。
- **メトリクス**: ★328、fork 68、作成 2025-10-14、最終push 2026-10-03T08:13:09Z、archived=False
- **確認**: 2026-10-02 / コミット `17a86f602e054c345841684224903004eff1f536`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/vocoder712/OpenUtauMobile/tree/17a86f602e054c345841684224903004eff1f536)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/vocoder712/OpenUtauMobile/blob/17a86f602e054c345841684224903004eff1f536/README.md) / [GitHub API](https://api.github.com/repos/vocoder712/OpenUtauMobile) / [固定ツリー](https://github.com/vocoder712/OpenUtauMobile/tree/17a86f602e054c345841684224903004eff1f536)

### 制作に使う際の検討

外出先での歌わせ調整・プレビュー。

**次に確かめること（実施前）**: Android版にDiffSinger音源を入れ、USTXを開いて保存・書き出しまで通るか確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/vocoder712/OpenUtauMobile/blob/17a86f602e054c345841684224903004eff1f536/README.md)

**最新GitHub Release**: [1.1.7](https://github.com/vocoder712/OpenUtauMobile/releases/tag/1.1.7) / 2025-12-31T16:25:36Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-08T02:05:39Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="soulx-singer"></a>

## SoulX-Singer

未見の歌声を生成するゼロショット歌声合成（SVS）モデルの公式推論コード。メロディ（F0）条件と楽譜（MIDI）条件に対応し、歌声変換（SVC）版も提供する。

- **リポジトリ**: https://github.com/Soul-AILab/SoulX-Singer
- **分類**: model_toolkit / AIモデル・学習 / モデル候補
- **入力**: 歌詞、メロディまたはMIDI、話者プロンプト音声（SVCは変換元の歌声波形とF0）
- **出力**: 歌声波形（wav）
- **環境**: Python 3.10のConda環境、PyTorch。Hugging FaceからSVS/SVCモデルと前処理モデルを取得。SVS/SVCそれぞれのWebUIを同梱。
- **依存**: F5-TTS、Amphion、RMVPE、Parakeet、前処理モデル群（SoulX-Singer-Preprocess）
- **制約・未確認**: 自動前処理のメタデータは歌唱音声と歌詞・音符の対応がずれることがあり、MIDIエディタでの手修正を推奨。ライセンスはApache-2.0。
- **編集者評価**: キャラクターの歌声づくりに向く。SVSとSVCの両方、歌声編集、クロスリンガル合成まで扱う点が特徴的。
- **メトリクス**: ★979、fork 147、作成 2026-02-06、最終push 2026-05-29T03:46:36Z、archived=False
- **確認**: 2026-10-04 / コミット `81aeb3ae772c70093c3de74dc23c92d983801ae4`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Soul-AILab/SoulX-Singer/tree/81aeb3ae772c70093c3de74dc23c92d983801ae4)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Soul-AILab/SoulX-Singer/blob/81aeb3ae772c70093c3de74dc23c92d983801ae4/README.md) / [GitHub API](https://api.github.com/repos/Soul-AILab/SoulX-Singer) / [固定ツリー](https://github.com/Soul-AILab/SoulX-Singer/tree/81aeb3ae772c70093c3de74dc23c92d983801ae4)

### 制作に使う際の検討

キャラクターソングや歌声素材を、話者ごとの追加学習なしで試作したい用途に向く。

**次に確かめること（実施前）**: 任意キャラの話者プロンプトでSVSとSVCを回し、声質保持・音程/リズム整合・クロスリンガル時の自然さを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [cli/inference.py](https://github.com/Soul-AILab/SoulX-Singer/blob/81aeb3ae772c70093c3de74dc23c92d983801ae4/cli/inference.py) / [preprocess/tools/midi_editor/src/main.tsx](https://github.com/Soul-AILab/SoulX-Singer/blob/81aeb3ae772c70093c3de74dc23c92d983801ae4/preprocess/tools/midi_editor/src/main.tsx) / [preprocess/tools/note_transcription/modules/pe/rmvpe/inference.py](https://github.com/Soul-AILab/SoulX-Singer/blob/81aeb3ae772c70093c3de74dc23c92d983801ae4/preprocess/tools/note_transcription/modules/pe/rmvpe/inference.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-05-29T03:46:12Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="moonintheriver-diffsinger"></a>

## DiffSinger

Shallow Diffusion機構を用いた歌声合成（DiffSinger）と音声合成（DiffSpeech）の公式PyTorch実装。歌詞+MIDI/F0からメルへ、メルから波形へ変換する複数構成を提供する。

- **リポジトリ**: https://github.com/MoonInTheRiver/DiffSinger
- **分類**: model_toolkit / AIモデル・学習 / 確立した参照実装
- **入力**: 歌詞、F0またはMIDI、テキスト（TTS構成）
- **出力**: 音声波形（wav）、音響特徴量（メル）
- **環境**: Python 3.8。GPU別のrequirements（2080Ti/CUDA10.2、3090/CUDA11.4）を用意。学習・推論のドキュメントを同梱。
- **依存**: PyTorch Lightning、HiFiGAN/NSF-HiFiGAN、ParallelWaveGAN等
- **制約・未確認**: 公開データセット（PopCS/OpenCpop/Ljspeech）ベースで、任意キャラの歌声には追加学習が必要。環境はやや古め。ライセンスはMIT。
- **編集者評価**: 歌声合成の代表的な参照実装で、派生プロジェクト（openvpi版DiffSinger等）の土台にもなっている。研究・実装の出発点として価値が高い。
- **メトリクス**: ★4,875、fork 831、作成 2021-12-17、最終push 2026-07-24T07:22:44Z、archived=False
- **確認**: 2026-10-04 / コミット `4662c53a27a5ac662821eae23a7d71cfcff7356d`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/MoonInTheRiver/DiffSinger/tree/4662c53a27a5ac662821eae23a7d71cfcff7356d)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/MoonInTheRiver/DiffSinger/blob/4662c53a27a5ac662821eae23a7d71cfcff7356d/README.md) / [GitHub API](https://api.github.com/repos/MoonInTheRiver/DiffSinger) / [固定ツリー](https://github.com/MoonInTheRiver/DiffSinger/tree/4662c53a27a5ac662821eae23a7d71cfcff7356d)

### 制作に使う際の検討

歌声合成モデルを自作・追加学習する際の参照基盤として使える。

**次に確かめること（実施前）**: OpenCpop構成で推論を再現し、環境構築の難易度と生成音質、追加学習の所要を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [tasks/run.py](https://github.com/MoonInTheRiver/DiffSinger/blob/4662c53a27a5ac662821eae23a7d71cfcff7356d/tasks/run.py)

**最新GitHub Release**: [pretrain-model](https://github.com/MoonInTheRiver/DiffSinger/releases/tag/pretrain-model) / 2022-01-17T03:30:08Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-24T07:22:43Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
