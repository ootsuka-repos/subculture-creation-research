# VFX・材質・ベクター演出

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-03。**158件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Effekseer](https://github.com/effekseer/Effekseer) · [詳細](#effekseer) | ゲーム向けのパーティクル効果を編集し、ランタイムで再生する。 | 非AI制作 / 制作基盤として比較 | 1,783 / 2026-09-14 |
| [GenCompositor](https://github.com/TencentARC/GenCompositor) · [詳細](#gencompositor) | 前景・背景と制御条件を用いて動画を生成合成する。 | AIモデル・学習 / 小規模・初期候補 | 157 / 2026-06-30 |
| [Material Maker](https://github.com/RodZill4/material-maker) · [詳細](#material-maker) | ノードで手続き的なテクスチャを作り、3Dモデルへのペイントも行う。 | 非AI制作 / 制作基盤として比較 | 5,962 / 2026-10-03 |
| [OmniLottie](https://github.com/OpenVGLab/OmniLottie) · [詳細](#omnilottie) | テキスト・画像等から編集可能なLottieベクターアニメーションを生成する。 | AIモデル・学習 / モデル・研究候補 | 797 / 2026-04-06 |
| [VfxDB](https://github.com/VfxDB-Official/VfxDB) · [詳細](#vfxdb) | OpenVDB由来の疎な3Dボリューム効果を学習・生成する。 | AIモデル・学習 / 小規模・初期候補 | 7 / 2026-08-19 |
| [VFXMaster](https://github.com/libaolu312/VFXMaster) · [詳細](#vfxmaster) | 効果の参照映像を条件に動的なVFX動画を生成する。 | AIモデル・学習 / 小規模・初期候補 | 67 / 2026-04-07 |
| [cHiDeScaler-Neo](https://github.com/animeojisan/cHiDeScaler-Neo) · [詳細](#chidescaler-neo) | Windowsの任意ウィンドウをリアルタイムキャプチャし、GLSL/ONNXでAI拡大とRIFE系フレーム補間をかけるポータブルアプリ。Anime4K等のシェーダ資産を利用できる。 | AIモデル・学習 / 小規模・初期評価候補 | 19 / 2026-09-28 |

<a id="effekseer"></a>

## Effekseer

ゲーム向けのパーティクル効果を編集し、ランタイムで再生する。

- **リポジトリ**: https://github.com/effekseer/Effekseer
- **分類**: desktop_tool / 非AI制作 / 制作基盤として比較
- **入力**: テクスチャ、メッシュ、効果の時間・発生設定
- **出力**: 編集可能なエフェクトとランタイム再生
- **環境**: エディタと対象エンジン用ランタイム・プラグイン。
- **依存**: ゲームエンジン、エフェクト素材
- **制約・未確認**: 動画生成型VFXとは出力が異なる。実機での描画負荷とシェーダ互換性は別途確認。
- **編集者評価**: 魔法・攻撃・演出をゲームに組み込む実用候補。
- **メトリクス**: ★1,783、fork 279、作成 2013-10-19、最終push 2026-09-14T13:05:28Z、archived=False
- **確認**: 2026-09-09 / コミット `6cf1cb853383765153219ba5ce9b47eff5ad8398`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/effekseer/Effekseer/tree/6cf1cb853383765153219ba5ce9b47eff5ad8398)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/effekseer/Effekseer/blob/6cf1cb853383765153219ba5ce9b47eff5ad8398/README.md) / [GitHub API](https://api.github.com/repos/effekseer/Effekseer) / [固定ツリー](https://github.com/effekseer/Effekseer/tree/6cf1cb853383765153219ba5ce9b47eff5ad8398)

### 制作に使う際の検討

魔法・攻撃・演出をゲームに組み込む実用候補。

**次に確かめること（実施前）**: 対象端末で大量発生時の負荷、透過順序、画面解像度差を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [Dev/Editor/Effekseer/Program.cs](https://github.com/effekseer/Effekseer/blob/6cf1cb853383765153219ba5ce9b47eff5ad8398/Dev/Editor/Effekseer/Program.cs)

**最新GitHub Release**: [1807](https://github.com/effekseer/Effekseer/releases/tag/1807) / 2026-08-07T08:02:55Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-05T06:39:43Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="gencompositor"></a>

## GenCompositor

前景・背景と制御条件を用いて動画を生成合成する。

- **リポジトリ**: https://github.com/TencentARC/GenCompositor
- **分類**: model / AIモデル・学習 / 小規模・初期候補
- **入力**: 前景動画、背景、マスク・動き条件
- **出力**: 合成動画
- **環境**: Python/CUDA、infer配下のスクリプト。
- **依存**: CogVideoX-5B系、GenCompositor重み
- **制約・未確認**: 従来の合成ソフトと同じ画素保持を保証しない。マスクと参照条件が必要。
- **編集者評価**: キャラを背景へ自然に馴染ませる短編映像の研究候補。
- **メトリクス**: ★157、fork 7、作成 2025-09-01、最終push 2026-06-30T12:41:01Z、archived=False
- **確認**: 2026-09-09 / コミット `a2aedd619fac71c9420a56ce7b8885f98a29c612`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/TencentARC/GenCompositor/tree/a2aedd619fac71c9420a56ce7b8885f98a29c612)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/TencentARC/GenCompositor/blob/a2aedd619fac71c9420a56ce7b8885f98a29c612/README.md) / [GitHub API](https://api.github.com/repos/TencentARC/GenCompositor) / [固定ツリー](https://github.com/TencentARC/GenCompositor/tree/a2aedd619fac71c9420a56ce7b8885f98a29c612)

### 制作に使う際の検討

キャラを背景へ自然に馴染ませる短編映像の研究候補。

**次に確かめること（実施前）**: 輪郭・影・接地・前景の同一性を、通常のアルファ合成と比較する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [infer/usr.py](https://github.com/TencentARC/GenCompositor/blob/a2aedd619fac71c9420a56ce7b8885f98a29c612/infer/usr.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-06-30T12:41:01Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [TencentARC/GenCompositor](https://huggingface.co/TencentARC/GenCompositor) — file_listing_checked、確認日 2026-09-09、revision `d499350f7aa952e43c2b342092e96b3725d8469e`。代表ファイル: `branch/diffusion_pytorch_model.safetensors`, `model/pytorch_model/mp_rank_00_model_states.pt`, `model/scheduler.bin`, `model/transformer/diffusion_pytorch_model-00001-of-00002.safetensors`。gated=False。

<a id="material-maker"></a>

## Material Maker

ノードで手続き的なテクスチャを作り、3Dモデルへのペイントも行う。

- **リポジトリ**: https://github.com/RodZill4/material-maker
- **分類**: desktop_tool / 非AI制作 / 制作基盤として比較
- **入力**: ノードグラフ、画像、3D素材
- **出力**: 材質用テクスチャ・ペイント結果
- **環境**: Godotベース。OS別の配布経路あり。
- **依存**: Godot、任意のユーザー素材
- **制約・未確認**: 生成AIモデルではない。出力先のPBRチャンネルと色空間を合わせる必要がある。
- **編集者評価**: ゲーム・背景・トゥーン素材の反復制作に向く。
- **メトリクス**: ★5,962、fork 380、作成 2018-07-22、最終push 2026-10-03T02:59:03Z、archived=False
- **確認**: 2026-09-09 / コミット `ad19fcf0ee34a7caf74df709dc4de7112f0d467d`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/RodZill4/material-maker/tree/ad19fcf0ee34a7caf74df709dc4de7112f0d467d)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/RodZill4/material-maker/blob/ad19fcf0ee34a7caf74df709dc4de7112f0d467d/README.md) / [GitHub API](https://api.github.com/repos/RodZill4/material-maker) / [固定ツリー](https://github.com/RodZill4/material-maker/tree/ad19fcf0ee34a7caf74df709dc4de7112f0d467d)

### 制作に使う際の検討

ゲーム・背景・トゥーン素材の反復制作に向く。

**次に確かめること（実施前）**: タイル境界、法線向き、粗さ、色空間を実際のエンジンで確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [material_maker/main_window.gd](https://github.com/RodZill4/material-maker/blob/ad19fcf0ee34a7caf74df709dc4de7112f0d467d/material_maker/main_window.gd) / [material_maker/main_window_layout.gd](https://github.com/RodZill4/material-maker/blob/ad19fcf0ee34a7caf74df709dc4de7112f0d467d/material_maker/main_window_layout.gd)

**最新GitHub Release**: [1.7](https://github.com/RodZill4/material-maker/releases/tag/1.7) / 2026-07-14T07:34:27Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-14T08:37:15Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="omnilottie"></a>

## OmniLottie

テキスト・画像等から編集可能なLottieベクターアニメーションを生成する。

- **リポジトリ**: https://github.com/OpenVGLab/OmniLottie
- **分類**: model / AIモデル・学習 / モデル・研究候補
- **入力**: テキスト、画像等の視覚条件
- **出力**: Lottie JSON、ベクターアニメーション
- **環境**: Python、公開推論スクリプト、HF重み。
- **依存**: VLM系モデル、Lottieの描画・変換環境
- **制約・未確認**: ラスタ動画やLive2Dリグとは別形式。重みのライセンスメタデータは未設定。
- **編集者評価**: 配信画面の動くアイコンやゲームUIの短い演出に新しい選択肢。
- **メトリクス**: ★797、fork 40、作成 2026-01-15、最終push 2026-04-06T04:01:50Z、archived=False
- **確認**: 2026-09-09 / コミット `26131278e7b46bc2f64f989b25bb816f9e07c528`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/OpenVGLab/OmniLottie/tree/26131278e7b46bc2f64f989b25bb816f9e07c528)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/OpenVGLab/OmniLottie/blob/26131278e7b46bc2f64f989b25bb816f9e07c528/README.md) / [GitHub API](https://api.github.com/repos/OpenVGLab/OmniLottie) / [固定ツリー](https://github.com/OpenVGLab/OmniLottie/tree/26131278e7b46bc2f64f989b25bb816f9e07c528)

### 制作に使う際の検討

配信画面の動くアイコンやゲームUIの短い演出に新しい選択肢。

**次に確かめること（実施前）**: JSONが対象プレーヤーで再生できるか、編集しやすさとパス数・負荷を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [inference_hf.py](https://github.com/OpenVGLab/OmniLottie/blob/26131278e7b46bc2f64f989b25bb816f9e07c528/inference_hf.py) / [app_hf.py](https://github.com/OpenVGLab/OmniLottie/blob/26131278e7b46bc2f64f989b25bb816f9e07c528/app_hf.py) / [inference.py](https://github.com/OpenVGLab/OmniLottie/blob/26131278e7b46bc2f64f989b25bb816f9e07c528/inference.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-03-20T10:02:47Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [OmniLottie/OmniLottie](https://huggingface.co/OmniLottie/OmniLottie) — file_listing_checked、確認日 2026-09-09、revision `10b0d6bb443a2c70eb6a6fae6400f571d9df29d6`。代表ファイル: `model-00001-of-00002.safetensors`, `model-00002-of-00002.safetensors`, `pytorch_model.bin`。gated=False。

<a id="vfxdb"></a>

## VfxDB

OpenVDB由来の疎な3Dボリューム効果を学習・生成する。

- **リポジトリ**: https://github.com/VfxDB-Official/VfxDB
- **分類**: model_toolkit / AIモデル・学習 / 小規模・初期候補
- **入力**: 条件ボリューム、設定、学習データ
- **出力**: 密度ボリューム、推論のNPZ等
- **環境**: Linux/NVIDIA、Python3.10、PyTorch2.5.1/cu124、vdb_ext。
- **依存**: 公開EMAチェックポイント、必要に応じ大規模VfxDBデータ
- **制約・未確認**: データ・重みはCC BY-NC 4.0。動画VFXと違い体積データ。全データは作者表記4.6TB。
- **編集者評価**: 煙などを3Dシーンで扱う研究候補。まず小規模サンプルで形式変換を評価。
- **メトリクス**: ★7、fork 3、作成 2026-04-27、最終push 2026-08-19T15:23:04Z、archived=False
- **確認**: 2026-09-09 / コミット `eaf0530af2067e9d0ffcdfc4fdbb114499037cf8`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/VfxDB-Official/VfxDB/tree/eaf0530af2067e9d0ffcdfc4fdbb114499037cf8)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/VfxDB-Official/VfxDB/blob/eaf0530af2067e9d0ffcdfc4fdbb114499037cf8/README.md) / [GitHub API](https://api.github.com/repos/VfxDB-Official/VfxDB) / [固定ツリー](https://github.com/VfxDB-Official/VfxDB/tree/eaf0530af2067e9d0ffcdfc4fdbb114499037cf8)

### 制作に使う際の検討

煙などを3Dシーンで扱う研究候補。まず小規模サンプルで形式変換を評価。

**次に確かめること（実施前）**: NPZからDCCでのボリューム表示まで確認し、密度スケールと時間方向の連続性を評価する。

**利用条件の確認メモ**: データ・チェックポイントは作者READMEでCC BY-NC 4.0。 商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [infer_one_stage_hf.py](https://github.com/VfxDB-Official/VfxDB/blob/eaf0530af2067e9d0ffcdfc4fdbb114499037cf8/infer_one_stage_hf.py)

**最新GitHub Release**: [prebuilt-v1](https://github.com/VfxDB-Official/VfxDB/releases/tag/prebuilt-v1) / 2026-06-26T04:48:07Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-19T15:23:00Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

本文を確認した箇所:

- [infer_one_stage_hf.py](https://github.com/VfxDB-Official/VfxDB/blob/eaf0530af2067e9d0ffcdfc4fdbb114499037cf8/infer_one_stage_hf.py): ローカルまたはHFチェックポイントとrevisionから推論バンドルを読み込む部分を確認。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [ryogishiki/VfxDB-models](https://huggingface.co/ryogishiki/VfxDB-models) — file_listing_checked、確認日 2026-09-09、revision `126f05c502b6527fc9ea679ded49593081827140`。代表ファイル: `checkpoints/paper-v1/static-conditional-32/diffusion_pytorch_model.safetensors`, `checkpoints/paper-v1/static-unconditional-32/diffusion_pytorch_model.safetensors`, `checkpoints/paper-v1/temporal-conditional-32/diffusion_pytorch_model.safetensors`。gated=False。

<a id="vfxmaster"></a>

## VFXMaster

効果の参照映像を条件に動的なVFX動画を生成する。

- **リポジトリ**: https://github.com/libaolu312/VFXMaster
- **分類**: model_toolkit / AIモデル・学習 / 小規模・初期候補
- **入力**: 参照効果動画、対象条件
- **出力**: 効果を伴う動画
- **環境**: 公式は最低34GB GPU、A800 80GBで検証。
- **依存**: 独自重み、CogVideoX系、推論・適応用スクリプト
- **制約・未確認**: エフェクトごとのLoRA方式との比較研究。ゲーム用パーティクルデータは出力しない。
- **編集者評価**: 短い映像へ未知の効果を移す研究候補。VRAM要件は個人環境での障壁。
- **メトリクス**: ★67、fork 4、作成 2025-10-24、最終push 2026-04-07T15:56:15Z、archived=False
- **確認**: 2026-09-09 / コミット `0632c5a9979586adc1d4f96632e5b808ee11712f`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/libaolu312/VFXMaster/tree/0632c5a9979586adc1d4f96632e5b808ee11712f)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/libaolu312/VFXMaster/blob/0632c5a9979586adc1d4f96632e5b808ee11712f/README.md) / [GitHub API](https://api.github.com/repos/libaolu312/VFXMaster) / [固定ツリー](https://github.com/libaolu312/VFXMaster/tree/0632c5a9979586adc1d4f96632e5b808ee11712f)

### 制作に使う際の検討

短い映像へ未知の効果を移す研究候補。VRAM要件は個人環境での障壁。

**次に確かめること（実施前）**: 未見の効果を参照させ、対象保持と効果転写、元映像の混入を評価する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [scripts/inference_tta.sh](https://github.com/libaolu312/VFXMaster/blob/0632c5a9979586adc1d4f96632e5b808ee11712f/scripts/inference_tta.sh) / [scripts/train.sh](https://github.com/libaolu312/VFXMaster/blob/0632c5a9979586adc1d4f96632e5b808ee11712f/scripts/train.sh)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-04-07T15:56:15Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [8ruceLi/VFXMaster](https://huggingface.co/8ruceLi/VFXMaster) — file_listing_checked、確認日 2026-09-09、revision `63d976c76bfd62bb8b991f97f5e753c6d9716c81`。代表ファイル: `In-Context-Conditioning/checkpoint-40000/diffusion_pytorch_model-00001-of-00002.safetensors`, `In-Context-Conditioning/checkpoint-40000/diffusion_pytorch_model-00002-of-00002.safetensors`, `In-Context-Conditioning/checkpoint-40000/scheduler.bin`, `One-shot-Adaptation/Acid/checkpoint-200/pytorch_model.pt`。gated=False。

<a id="chidescaler-neo"></a>

## cHiDeScaler-Neo

Windowsの任意ウィンドウをリアルタイムキャプチャし、GLSL/ONNXでAI拡大とRIFE系フレーム補間をかけるポータブルアプリ。Anime4K等のシェーダ資産を利用できる。

- **リポジトリ**: https://github.com/animeojisan/cHiDeScaler-Neo
- **分類**: desktop_tool / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 任意のWindowsウィンドウ映像(リアルタイムキャプチャ)
- **出力**: 拡大・フレーム補間された映像出力
- **環境**: Windows 10/11、Rust/MSVCビルド。DirectML/NeoAMD/TensorRTバックエンド。
- **依存**: ONNXモデル、mpv互換GLSLシェーダ、RIFE/DRBA
- **制約・未確認**: HDR非対応でSDR前提。一部同梱モデル/シェーダのライセンス情報は整理中と明記。
- **編集者評価**: アニメ向けシェーダ/ONNXモデルを前提に、DirectML・NeoAMD・TensorRTを選べる構成で、既存のmpv系資産を流用できる。
- **メトリクス**: ★19、fork 0、作成 2026-08-08、最終push 2026-09-28T03:56:36Z、archived=False
- **確認**: 2026-09-30 / コミット `1e8fb3e7378b7df99709393087578ea7bc55d209`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/animeojisan/cHiDeScaler-Neo/tree/1e8fb3e7378b7df99709393087578ea7bc55d209)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/animeojisan/cHiDeScaler-Neo/blob/1e8fb3e7378b7df99709393087578ea7bc55d209/README.md) / [GitHub API](https://api.github.com/repos/animeojisan/cHiDeScaler-Neo) / [固定ツリー](https://github.com/animeojisan/cHiDeScaler-Neo/tree/1e8fb3e7378b7df99709393087578ea7bc55d209)

### 制作に使う際の検討

映像素材のアップスケールや補間、視聴環境の画質底上げに。

**次に確かめること（実施前）**: 手元のアニメ映像でバックエンド別の速度と画質、フレーム補間の破綻を比較する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [src/main.rs](https://github.com/animeojisan/cHiDeScaler-Neo/blob/1e8fb3e7378b7df99709393087578ea7bc55d209/src/main.rs)

**最新GitHub Release**: [v0.99.4](https://github.com/animeojisan/cHiDeScaler-Neo/releases/tag/v0.99.4) / 2026-09-28T03:56:37Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-28T03:48:09Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
