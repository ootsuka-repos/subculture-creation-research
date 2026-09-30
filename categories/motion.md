# モーション・身体演技

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-30。**136件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ARDY](https://github.com/nv-tlabs/ardy) · [詳細](#ardy) | テキストと運動学的制約から、対応骨格のモーションを生成する。 | AIモデル・学習 / モデル・研究候補 | 945 / 2026-07-10 |
| [EchoAvatar](https://github.com/RobinWitch/EchoAvatar) · [詳細](#echoavatar) | ストリーミング音声から顔・身体の動きを生成してUnityアバターへ送る。 | AIモデル・学習 / 小規模・初期候補 | 43 / 2026-06-17 |
| [Gelina](https://github.com/TGuichoux/Gelina) · [詳細](#gelina) | 音声とジェスチャーの生成・クローニング・音声から動作への変換を扱う。 | AIモデル・学習 / 小規模・初期候補 | 31 / 2026-04-28 |
| [HY-Motion 1.0](https://github.com/Tencent-Hunyuan/HY-Motion-1.0) · [詳細](#hy-motion-1-0) | テキストから人型キャラクターの3D動作を生成する。 | AIモデル・学習 / モデル・研究候補 | 2,577 / 2026-07-18 |
| [R-DMesh](https://github.com/Tencent-Hunyuan/R-DMesh) · [詳細](#r-dmesh) | 静的メッシュを参照動画に沿って動く4Dメッシュ列へ変換する。 | AIモデル・学習 / 小規模・初期候補 | 62 / 2026-08-11 |
| [VRM-Spacing-Animation-Baking](https://github.com/Meringue-Rouge/VRM-Spacing-Animation-Baking) · [詳細](#vrm-spacing-animation-baking) | VRM 1.0モデル向けBlenderアドオン。腕・脚・肩の間隔をMixamo風に調整し、髪やバストの物理ボーンをアニメへ焼き込み、ループ化する。 | 非AI制作 / 小規模・初期評価候補 | 10 / 2026-09-13 |

<a id="ardy"></a>

## ARDY

テキストと運動学的制約から、対応骨格のモーションを生成する。

- **リポジトリ**: https://github.com/nv-tlabs/ardy
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 動作記述、骨格別の制約
- **出力**: 対応骨格の動作列
- **環境**: PyTorch2.4以上、C++17/CMake。TensorRTは任意。
- **依存**: ARDY重み、アクセス申請が必要なLlama3-8B系テキストエンコーダ
- **制約・未確認**: CoreとG1で骨格・fps・予測長が異なる。テキストエンコーダのメモリを本体から分ける。
- **編集者評価**: 経路や姿勢制約を与えるキャラ動作生成として比較価値がある。
- **メトリクス**: ★945、fork 117、作成 2026-07-08、最終push 2026-07-10T14:13:31Z、archived=False
- **確認**: 2026-09-09 / コミット `693f74d13b3d04a0a22ce127ee79c929dd89756b`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/nv-tlabs/ardy/tree/693f74d13b3d04a0a22ce127ee79c929dd89756b)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/nv-tlabs/ardy/blob/693f74d13b3d04a0a22ce127ee79c929dd89756b/README.md) / [GitHub API](https://api.github.com/repos/nv-tlabs/ardy) / [固定ツリー](https://github.com/nv-tlabs/ardy/tree/693f74d13b3d04a0a22ce127ee79c929dd89756b)

### 制作に使う際の検討

経路や姿勢制約を与えるキャラ動作生成として比較価値がある。

**次に確かめること（実施前）**: ゲーム用骨格へ転送し、制約一致、足滑り、連続動作の接続を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [scripts/generate.py](https://github.com/nv-tlabs/ardy/blob/693f74d13b3d04a0a22ce127ee79c929dd89756b/scripts/generate.py) / [scripts/visualize.py](https://github.com/nv-tlabs/ardy/blob/693f74d13b3d04a0a22ce127ee79c929dd89756b/scripts/visualize.py) / [scripts/run_text_encoder_server.py](https://github.com/nv-tlabs/ardy/blob/693f74d13b3d04a0a22ce127ee79c929dd89756b/scripts/run_text_encoder_server.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-07-09T17:52:46Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [nvidia/ARDY-Core-RP-20FPS-Horizon40](https://huggingface.co/nvidia/ARDY-Core-RP-20FPS-Horizon40) — file_listing_checked、確認日 2026-09-09、revision `abe6c43beb28c867c950acb824b9c4ef3d63fb76`。代表ファイル: `denoiser.safetensors`, `tokenizer.safetensors`。gated=False。

<a id="echoavatar"></a>

## EchoAvatar

ストリーミング音声から顔・身体の動きを生成してUnityアバターへ送る。

- **リポジトリ**: https://github.com/RobinWitch/EchoAvatar
- **分類**: pipeline / AIモデル・学習 / 小規模・初期候補
- **入力**: 音声ストリーム、アバター
- **出力**: 顔と身体の動作、Unity表示
- **環境**: 推奨はUbuntu推論サーバーとWindows/Unity。顔・体同時は作者構成でRTX3090二枚。
- **依存**: 独自チェックポイント、音声エンコーダ、Unityパッケージ
- **制約・未確認**: 公開された音声エンコーダだけで顔・体全体のモデルが揃うとは言えない。複数マシン構成。
- **編集者評価**: 対話キャラクターの発話に身体演技を足す実験候補。
- **メトリクス**: ★43、fork 8、作成 2026-05-27、最終push 2026-06-17T09:31:29Z、archived=False
- **確認**: 2026-09-09 / コミット `174ca5dc6a535a557177cf6703cc9a5338a17bc7`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/RobinWitch/EchoAvatar/tree/174ca5dc6a535a557177cf6703cc9a5338a17bc7)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/RobinWitch/EchoAvatar/blob/174ca5dc6a535a557177cf6703cc9a5338a17bc7/readme.md) / [GitHub API](https://api.github.com/repos/RobinWitch/EchoAvatar) / [固定ツリー](https://github.com/RobinWitch/EchoAvatar/tree/174ca5dc6a535a557177cf6703cc9a5338a17bc7)

### 制作に使う際の検討

対話キャラクターの発話に身体演技を足す実験候補。

**次に確かめること（実施前）**: 発話から口・手が動くまでの遅延、通信切断、長時間のずれを計測する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [scripts/5_streaming_vllm_unity_30fps_bp_attn4_encodec2_multirvq_nbc512_motionexample_withface_ik.py](https://github.com/RobinWitch/EchoAvatar/blob/174ca5dc6a535a557177cf6703cc9a5338a17bc7/scripts/5_streaming_vllm_unity_30fps_bp_attn4_encodec2_multirvq_nbc512_motionexample_withface_ik.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-06-17T09:36:54Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="gelina"></a>

## Gelina

音声とジェスチャーの生成・クローニング・音声から動作への変換を扱う。

- **リポジトリ**: https://github.com/TGuichoux/Gelina
- **分類**: model_toolkit / AIモデル・学習 / 小規模・初期候補
- **入力**: テキスト・参照音声・動作条件
- **出力**: 音声と身体ジェスチャー
- **環境**: Python研究環境、モード別推論スクリプト。
- **依存**: Matcha系TTS、動作表現、作者Google Drive重み
- **制約・未確認**: Google Drive配布の中身・取得成功は未確認。モード別の入力と必要モデルが異なる。
- **編集者評価**: 音声と身振りの協調を調べる研究候補。
- **メトリクス**: ★31、fork 3、作成 2025-09-22、最終push 2026-04-28T08:52:34Z、archived=False
- **確認**: 2026-09-09 / コミット `bd50c64661498855b41300fa3d3b983819d0175a`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/TGuichoux/Gelina/tree/bd50c64661498855b41300fa3d3b983819d0175a)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/TGuichoux/Gelina/blob/bd50c64661498855b41300fa3d3b983819d0175a/README.md) / [GitHub API](https://api.github.com/repos/TGuichoux/Gelina) / [固定ツリー](https://github.com/TGuichoux/Gelina/tree/bd50c64661498855b41300fa3d3b983819d0175a)

### 制作に使う際の検討

音声と身振りの協調を調べる研究候補。

**次に確かめること（実施前）**: 同じ台詞の発話区間と身振りピーク、話者を変えたときの整合性を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [scripts/inference/clone_segments_cfm.py](https://github.com/TGuichoux/Gelina/blob/bd50c64661498855b41300fa3d3b983819d0175a/scripts/inference/clone_segments_cfm.py) / [scripts/preprocessing/tokenize_motion.py](https://github.com/TGuichoux/Gelina/blob/bd50c64661498855b41300fa3d3b983819d0175a/scripts/preprocessing/tokenize_motion.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-04-28T08:52:34Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="hy-motion-1-0"></a>

## HY-Motion 1.0

テキストから人型キャラクターの3D動作を生成する。

- **リポジトリ**: https://github.com/Tencent-Hunyuan/HY-Motion-1.0
- **分類**: model / AIモデル・学習 / モデル・研究候補
- **入力**: 動作テキスト
- **出力**: 人型モーション
- **環境**: 公式目安26GB、Lite24GB。短い指示・5秒未満・num_seeds=1等の条件。
- **依存**: HY-Motion重み、必要に応じ別のプロンプト書き換えモデル
- **制約・未確認**: 非人型・複数人・シームレスループ・in-placeは公式の非対応項目。追加LLMのVRAMは表に含まれない。
- **編集者評価**: 人型の単発演技を作る候補。ゲームの常時ループには追加編集が必要。
- **メトリクス**: ★2,577、fork 219、作成 2025-12-29、最終push 2026-07-18T15:13:36Z、archived=False
- **確認**: 2026-09-09 / コミット `4e426f5a1021cbcf7f375458c37b840ee7225229`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Tencent-Hunyuan/HY-Motion-1.0/tree/4e426f5a1021cbcf7f375458c37b840ee7225229)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Tencent-Hunyuan/HY-Motion-1.0/blob/4e426f5a1021cbcf7f375458c37b840ee7225229/README.md) / [GitHub API](https://api.github.com/repos/Tencent-Hunyuan/HY-Motion-1.0) / [固定ツリー](https://github.com/Tencent-Hunyuan/HY-Motion-1.0/tree/4e426f5a1021cbcf7f375458c37b840ee7225229)

### 制作に使う際の検討

人型の単発演技を作る候補。ゲームの常時ループには追加編集が必要。

**次に確かめること（実施前）**: ゲーム骨格への転送、足接地、開始終了姿勢、ループ化に必要な修正量を記録する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [local_infer.py](https://github.com/Tencent-Hunyuan/HY-Motion-1.0/blob/4e426f5a1021cbcf7f375458c37b840ee7225229/local_infer.py) / [gradio_app.py](https://github.com/Tencent-Hunyuan/HY-Motion-1.0/blob/4e426f5a1021cbcf7f375458c37b840ee7225229/gradio_app.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-07-18T15:13:36Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [tencent/HY-Motion-1.0](https://huggingface.co/tencent/HY-Motion-1.0) — file_listing_checked、確認日 2026-09-09、revision `620dd559f8d964aac2f82f1204fe6a35ad8ad14d`。代表ファイル: `HY-Motion-1.0-Lite/latest.ckpt`, `HY-Motion-1.0/latest.ckpt`。gated=False。

<a id="r-dmesh"></a>

## R-DMesh

静的メッシュを参照動画に沿って動く4Dメッシュ列へ変換する。

- **リポジトリ**: https://github.com/Tencent-Hunyuan/R-DMesh
- **分類**: model / AIモデル・学習 / 小規模・初期候補
- **入力**: 静的メッシュ、参照動画
- **出力**: 動的メッシュ列
- **環境**: Python/CUDA系研究環境、test_drive.pyによる推論。
- **依存**: R-DMeshチェックポイント、Wan2.2-TI2V-5B等
- **制約・未確認**: 4Dメッシュ列と再利用可能な骨格モーションは同一ではない。リグ転送は別問題。
- **編集者評価**: 骨格で表しにくい変形の映像制作に適する研究候補。
- **メトリクス**: ★62、fork 9、作成 2026-04-29、最終push 2026-08-11T01:56:44Z、archived=False
- **確認**: 2026-09-09 / コミット `467cb35a9f53f6d61a0b36a5aa4e171e4d40ad0f`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Tencent-Hunyuan/R-DMesh/tree/467cb35a9f53f6d61a0b36a5aa4e171e4d40ad0f)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Tencent-Hunyuan/R-DMesh/blob/467cb35a9f53f6d61a0b36a5aa4e171e4d40ad0f/README.md) / [GitHub API](https://api.github.com/repos/Tencent-Hunyuan/R-DMesh) / [固定ツリー](https://github.com/Tencent-Hunyuan/R-DMesh/tree/467cb35a9f53f6d61a0b36a5aa4e171e4d40ad0f)

### 制作に使う際の検討

骨格で表しにくい変形の映像制作に適する研究候補。

**次に確かめること（実施前）**: フレーム間の形状・テクスチャ保持、ファイルサイズ、DCCへの読み込みを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [test_drive.py](https://github.com/Tencent-Hunyuan/R-DMesh/blob/467cb35a9f53f6d61a0b36a5aa4e171e4d40ad0f/test_drive.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-11T01:56:43Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [JarrentWu/R-DMesh](https://huggingface.co/JarrentWu/R-DMesh) — file_listing_checked、確認日 2026-09-09、revision `a374a76866abf15d22b598f1d7f0a80764a4ba76`。代表ファイル: `ckpts/dvae/rdmeshvae/dvae_f.pth`, `ckpts/rf_model/rdmeshdit/rf_epoch_f.pth`。gated=False。

<a id="vrm-spacing-animation-baking"></a>

## VRM-Spacing-Animation-Baking

VRM 1.0モデル向けBlenderアドオン。腕・脚・肩の間隔をMixamo風に調整し、髪やバストの物理ボーンをアニメへ焼き込み、ループ化する。

- **リポジトリ**: https://github.com/Meringue-Rouge/VRM-Spacing-Animation-Baking
- **分類**: integration / 非AI制作 / 小規模・初期評価候補
- **入力**: VRM 1.0モデルとアクション(アニメーション)
- **出力**: 物理ベイク済み・ループ調整済みのアニメーション
- **環境**: Blender + VRM Add-on。VRM 1.0モデル。
- **依存**: BlenderのVRM Add-on
- **制約・未確認**: VRM 1.0限定。外部のVRM Add-onと併用が前提。AI機能は含まない。
- **編集者評価**: 外部ツールで再生する前提のVRMモーション作りを、間隔調整と物理ループという実際に困る点で補助する。
- **メトリクス**: ★10、fork 0、作成 2024-08-22、最終push 2026-09-13T13:14:33Z、archived=False
- **確認**: 2026-09-30 / コミット `dc2a4a4aabb741f2eb30683e6883c3e3dd399512`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Meringue-Rouge/VRM-Spacing-Animation-Baking/tree/dc2a4a4aabb741f2eb30683e6883c3e3dd399512)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Meringue-Rouge/VRM-Spacing-Animation-Baking/blob/dc2a4a4aabb741f2eb30683e6883c3e3dd399512/README.md) / [GitHub API](https://api.github.com/repos/Meringue-Rouge/VRM-Spacing-Animation-Baking) / [固定ツリー](https://github.com/Meringue-Rouge/VRM-Spacing-Animation-Baking/tree/dc2a4a4aabb741f2eb30683e6883c3e3dd399512)

### 制作に使う際の検討

VRMキャラのモーション最終調整や衣装・体型差の補正に。

**次に確かめること（実施前）**: Mixamo系クリップで間隔調整後のクリッピングとループ継ぎ目の品質を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/Meringue-Rouge/VRM-Spacing-Animation-Baking/blob/dc2a4a4aabb741f2eb30683e6883c3e3dd399512/README.md)

**最新GitHub Release**: [2.1.0](https://github.com/Meringue-Rouge/VRM-Spacing-Animation-Baking/releases/tag/2.1.0) / 2026-09-13T13:14:33Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-13T13:13:18Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
