# アニメ制作・中割り・彩色・リップシンク

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-10。**218件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [AniDoc](https://github.com/robbyant-research/AniDoc) · [詳細](#anidoc) | 設定画を参照してスケッチ列を彩色するアニメ制作研究。 | AIモデル・学習 / モデル・研究候補 | 573 / 2025-04-15 |
| [AnimeColor](https://github.com/IamCreateAI/AnimeColor) · [詳細](#animecolor) | 設定画参照とスケッチ動画からアニメを彩色する拡散Transformer。 | AIモデル・学習 / 小規模・初期候補 | 9 / 2025-08-04 |
| [BasicPBC](https://github.com/ykdai/BasicPBC) · [詳細](#basicpbc) | 閉領域の対応付けによってアニメ線画の塗りを支援するペイントバケット彩色。 | AIモデル・学習 / モデル・研究候補 | 307 / 2025-06-26 |
| [ECCV2022-RIFE](https://github.com/hzwer/ECCV2022-RIFE) · [詳細](#eccv2022-rife) | フレーム間の中間画像を推定する動画補間モデル。 | AIモデル・学習 / 比較・既存工程の参考 | 5,605 / 2025-09-10 |
| [LatentSync](https://github.com/bytedance/LatentSync) · [詳細](#latentsync) | 音声条件で口の動きを同期させる動画処理モデル。 | AIモデル・学習 / 比較・既存工程の参考 | 6,127 / 2025-06-20 |
| [opentoonz](https://github.com/opentoonz/opentoonz) · [詳細](#opentoonz) | 作画、彩色、撮影を扱う2Dアニメ制作アプリ。 | 非AI制作 / 定番の制作基盤 | 7,806 / 2026-10-09 |
| [ToonComposer](https://github.com/TencentARC/ToonComposer) · [詳細](#tooncomposer) | キーフレーム後の中割りと彩色を生成AIでまとめて処理する。 | AIモデル・学習 / 研究・技術評価候補 | 591 / 2025-08-20 |
| [ToonCrafter](https://github.com/Doubiiu/ToonCrafter) · [詳細](#tooncrafter) | 二枚のアニメ画像の間を生成する補間モデル。 | AIモデル・学習 / モデル・研究候補 | 6,031 / 2025-03-19 |
| [comic-manga-narrator](https://github.com/MushiSenpai/comic-manga-narrator) · [詳細](#comic-manga-narrator) | 漫画/コミックページを、コマ検出・セリフの音声化・ナレーション・Ken Burnsと2.5Dパララックスで演出したナレーション付きMP4に変換するローカルパイプライン。 | AIモデル・学習 / 小規模・初期評価候補 | 0 / 2026-07-12 |
| [vedGen](https://github.com/HarisUmer/vedGen) · [詳細](#vedgen) | 一行のあらすじから絵コンテ→ショット別I2V→結合までをローカルGPUで回すアニメ風短編動画生成ライブラリ。ComfyUIをヘッドレスでAPI駆動し、Pythonライブラリとして呼び出す。 | AIモデル・学習 / 小規模・初期評価候補 | 1 / 2026-07-22 |
| [vocaloid-style-mv-pipeline](https://github.com/EGSECDA/vocaloid-style-mv-pipeline) · [詳細](#vocaloid-style-mv-pipeline) | 楽曲と歌詞からボカロ風の手書きリリックMVを作る制作パイプライン。各フレームをCanvas2D/WebGL2で決定論的に描画し、Playwrightとffmpegで1080pマスターと9:16版を書き出す。 | AI連携 / 活発・実用候補 | 92 / 2026-10-04 |
| [AIComics](https://github.com/chfr19820610-cell/AIComics) · [詳細](#aicomics) | 物語から分鏡・作画・配音・公開までをローカルで回すAI漫劇の制作システム。LLMで脚本と分鏡、ComfyUI+SDXLでキーフレーム、TTSで音声を作り、動画生成や投稿までモジュール化する。 | AIモデル・学習 / 小規模・初期評価候補 | 24 / 2026-09-26 |

<a id="anidoc"></a>

## AniDoc

設定画を参照してスケッチ列を彩色するアニメ制作研究。

- **リポジトリ**: https://github.com/robbyant-research/AniDoc
- **分類**: model / AIモデル・学習 / モデル・研究候補
- **入力**: 参照カラー画像、スケッチ列
- **出力**: 彩色動画
- **環境**: Linux、PyTorch。作者測定で推論約14GB VRAM、14フレームを扱う。
- **依存**: SVD、独自UNet/ControlNet、CoTracker2
- **制約・未確認**: 環境構築に複数モデルが必要。長いカットや作画の線の保持は未評価。
- **編集者評価**: 完成画像から自由な動画を作る用途より、既存原画を使う彩色工程で比較したい。
- **メトリクス**: ★573、fork 46、作成 2024-12-18、最終push 2025-04-15T06:21:33Z、archived=False
- **確認**: 2026-09-09 / コミット `77e0696cea9df7bb1cd2c254ba21639d3a6ab8f8`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/robbyant-research/AniDoc/tree/77e0696cea9df7bb1cd2c254ba21639d3a6ab8f8)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/robbyant-research/AniDoc/blob/77e0696cea9df7bb1cd2c254ba21639d3a6ab8f8/README.md) / [GitHub API](https://api.github.com/repos/robbyant-research/AniDoc) / [固定ツリー](https://github.com/robbyant-research/AniDoc/tree/77e0696cea9df7bb1cd2c254ba21639d3a6ab8f8)

### 制作に使う際の検討

完成画像から自由な動画を作る用途より、既存原画を使う彩色工程で比較したい。

**次に確かめること（実施前）**: 同じ14枚の線画と色指定で、服の色、目、遮蔽後の再出現を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [scripts_infer/anidoc_inference.sh](https://github.com/robbyant-research/AniDoc/blob/77e0696cea9df7bb1cd2c254ba21639d3a6ab8f8/scripts_infer/anidoc_inference.sh) / [install.sh](https://github.com/robbyant-research/AniDoc/blob/77e0696cea9df7bb1cd2c254ba21639d3a6ab8f8/install.sh)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-04-15T06:21:33Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Yhmeng1106/anidoc](https://huggingface.co/Yhmeng1106/anidoc) — file_listing_checked、確認日 2026-09-09、revision `cd1d29fcab5e86fefb3d12d090f9630465f05185`。代表ファイル: `anidoc/controlnet/diffusion_pytorch_model.safetensors`, `anidoc/scaler.pt`, `anidoc/scheduler.bin`, `anidoc/unet/diffusion_pytorch_model.safetensors`。gated=False。

<a id="animecolor"></a>

## AnimeColor

設定画参照とスケッチ動画からアニメを彩色する拡散Transformer。

- **リポジトリ**: https://github.com/IamCreateAI/AnimeColor
- **分類**: model / AIモデル・学習 / 小規模・初期候補
- **入力**: 参照カラー画像、スケッチ動画、キャプション
- **出力**: 彩色動画
- **環境**: Python3.10。test_msketch.py内の入出力設定を編集する。
- **依存**: CogVideoX-Fun系、AnimeColorの参照網・Transformer
- **制約・未確認**: コードに低メモリ設定はあるが、任意GPUでの動作保証はない。動画全体の色一貫性は未評価。
- **編集者評価**: AniDoc・BasicPBCと同じ線画で比較したい彩色候補。
- **メトリクス**: ★9、fork 2、作成 2025-06-17、最終push 2025-08-04T07:04:34Z、archived=False
- **確認**: 2026-09-09 / コミット `76fb1f83628fa420fbab73967af7e6b74712ebbc`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/IamCreateAI/AnimeColor/tree/76fb1f83628fa420fbab73967af7e6b74712ebbc)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/IamCreateAI/AnimeColor/blob/76fb1f83628fa420fbab73967af7e6b74712ebbc/README.md) / [GitHub API](https://api.github.com/repos/IamCreateAI/AnimeColor) / [固定ツリー](https://github.com/IamCreateAI/AnimeColor/tree/76fb1f83628fa420fbab73967af7e6b74712ebbc)

### 制作に使う際の検討

AniDoc・BasicPBCと同じ線画で比較したい彩色候補。

**次に確かめること（実施前）**: 同じ線画46フレームで色漏れ、線の変化、衣装色の持続、処理時間を測る。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [test_msketch.py](https://github.com/IamCreateAI/AnimeColor/blob/76fb1f83628fa420fbab73967af7e6b74712ebbc/test_msketch.py) / [extract_sketch_from_vid.py](https://github.com/IamCreateAI/AnimeColor/blob/76fb1f83628fa420fbab73967af7e6b74712ebbc/extract_sketch_from_vid.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-08-04T07:04:21Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

本文を確認した箇所:

- [test_msketch.py](https://github.com/IamCreateAI/AnimeColor/blob/76fb1f83628fa420fbab73967af7e6b74712ebbc/test_msketch.py): CogVideoX-Fun系モデル・参照網と動画長46、入力設定を記述する冒頭部分を確認。

関連: editorial_comparison → anidoc（編集者による比較候補、接続実行は未検証）

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [rainbowow/AnimeColor](https://huggingface.co/rainbowow/AnimeColor) — file_listing_checked、確認日 2026-09-09、revision `1672912547093795e8a9d2b9590ddb8fea6aa233`。代表ファイル: `referencenet/diffusion_pytorch_model.safetensors`, `transformer/diffusion_pytorch_model.safetensors`。gated=False。

<a id="basicpbc"></a>

## BasicPBC

閉領域の対応付けによってアニメ線画の塗りを支援するペイントバケット彩色。

- **リポジトリ**: https://github.com/ykdai/BasicPBC
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 線画、参照の彩色領域
- **出力**: 対応領域と彩色結果
- **環境**: Python/PyTorch。basicsr/test.pyと設定YAMLを使用。
- **依存**: BasicSR、作者配布チェックポイント
- **制約・未確認**: 実写ではなく線画の領域対応が中心。手描きデータの一部は非公開。配布重みの取得は未検証。
- **編集者評価**: 線の輪郭を保ちながら塗り分けたい工程で、拡散モデルによる再描画との違いが明確。
- **メトリクス**: ★307、fork 28、作成 2024-03-29、最終push 2025-06-26T23:11:03Z、archived=False
- **確認**: 2026-09-09 / コミット `223bf783dea63770fcced4612ecf153883ce91cf`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/ykdai/BasicPBC/tree/223bf783dea63770fcced4612ecf153883ce91cf)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ykdai/BasicPBC/blob/223bf783dea63770fcced4612ecf153883ce91cf/README.md) / [GitHub API](https://api.github.com/repos/ykdai/BasicPBC) / [固定ツリー](https://github.com/ykdai/BasicPBC/tree/223bf783dea63770fcced4612ecf153883ce91cf)

### 制作に使う際の検討

線の輪郭を保ちながら塗り分けたい工程で、拡散モデルによる再描画との違いが明確。

**次に確かめること（実施前）**: 開いた線、細い髪、領域の分裂・結合を含む連番で塗り漏れ数を数える。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [basicsr/test.py](https://github.com/ykdai/BasicPBC/blob/223bf783dea63770fcced4612ecf153883ce91cf/basicsr/test.py) / [scripts/dist_train.sh](https://github.com/ykdai/BasicPBC/blob/223bf783dea63770fcced4612ecf153883ce91cf/scripts/dist_train.sh)

**最新GitHub Release**: [v0.1.0](https://github.com/ykdai/BasicPBC/releases/tag/v0.1.0) / 2024-05-26T12:42:57Z / prerelease=False

デフォルトブランチの確認コミット日時: 2025-06-26T23:11:03Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="eccv2022-rife"></a>

## ECCV2022-RIFE

フレーム間の中間画像を推定する動画補間モデル。

- **リポジトリ**: https://github.com/hzwer/ECCV2022-RIFE
- **分類**: model / AIモデル・学習 / 比較・既存工程の参考
- **入力**: 前後の画像・動画フレーム
- **出力**: 補間フレーム・高フレームレート動画
- **環境**: Python/GPU環境または対応する外部実装。
- **依存**: RIFEモデル
- **制約・未確認**: 作者がアニメ向けモデルを案内。原画の演技設計やタイミングを自動で正しく決めるものではない。
- **編集者評価**: 少枚数アニメや生成動画の補間を検討する基盤。
- **メトリクス**: ★5,605、fork 570、作成 2020-11-12、最終push 2025-09-10T06:32:03Z、archived=False
- **確認**: 2026-09-09 / コミット `5d8adbdd40e12c2c8f91930eff838aebe561c086`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/hzwer/ECCV2022-RIFE/tree/5d8adbdd40e12c2c8f91930eff838aebe561c086)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/hzwer/ECCV2022-RIFE/blob/5d8adbdd40e12c2c8f91930eff838aebe561c086/README.md) / [GitHub API](https://api.github.com/repos/hzwer/ECCV2022-RIFE) / [固定ツリー](https://github.com/hzwer/ECCV2022-RIFE/tree/5d8adbdd40e12c2c8f91930eff838aebe561c086)

### 制作に使う際の検討

フレーム補間の比較基準。補間と演技の設計を分け、意図的なコマ打ちは保持する。

**次に確かめること（実施前）**: パン・口・髪・フラッシュを含む動画で、残像とタイミング変化を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [inference_video.py](https://github.com/hzwer/ECCV2022-RIFE/blob/5d8adbdd40e12c2c8f91930eff838aebe561c086/inference_video.py) / [inference_img.py](https://github.com/hzwer/ECCV2022-RIFE/blob/5d8adbdd40e12c2c8f91930eff838aebe561c086/inference_img.py) / [benchmark/UCF101.py](https://github.com/hzwer/ECCV2022-RIFE/blob/5d8adbdd40e12c2c8f91930eff838aebe561c086/benchmark/UCF101.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-09-10T06:32:03Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="latentsync"></a>

## LatentSync

音声条件で口の動きを同期させる動画処理モデル。

- **リポジトリ**: https://github.com/bytedance/LatentSync
- **分類**: model / AIモデル・学習 / 比較・既存工程の参考
- **入力**: 顔が映った動画、音声
- **出力**: リップシンク済み動画
- **環境**: GPU推論環境とモデル。
- **依存**: LatentSyncモデル、Whisper等
- **制約・未確認**: READMEにアニメ例はあるが、任意の二次元顔への適合性は未検証。更新は2025年中心。
- **編集者評価**: アニメやキャラクター動画のセリフ同期を試す候補。
- **メトリクス**: ★6,127、fork 982、作成 2024-12-11、最終push 2025-06-20T07:36:58Z、archived=False
- **確認**: 2026-09-09 / コミット `a229c3948406bc2cf6eaf4873e662e70c6a04746`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/bytedance/LatentSync/tree/a229c3948406bc2cf6eaf4873e662e70c6a04746)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/bytedance/LatentSync/blob/a229c3948406bc2cf6eaf4873e662e70c6a04746/README.md) / [GitHub API](https://api.github.com/repos/bytedance/LatentSync) / [固定ツリー](https://github.com/bytedance/LatentSync/tree/a229c3948406bc2cf6eaf4873e662e70c6a04746)

### 制作に使う際の検討

台詞に口を合わせる後処理候補。人間の顔を前提とする検出が二次元絵で成立するかが入口になる。

**次に確かめること（実施前）**: 正面・横顔・大きなアニメ目で顔検出、歯や口の描き換え、音とのずれを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [scripts/inference.py](https://github.com/bytedance/LatentSync/blob/a229c3948406bc2cf6eaf4873e662e70c6a04746/scripts/inference.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-06-20T07:36:51Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [ByteDance/LatentSync-1.6](https://huggingface.co/ByteDance/LatentSync-1.6) — file_listing_checked、確認日 2026-09-09、revision `c42c7e6c8e9c213626389fa7d9a3c444b8536353`。代表ファイル: `auxiliary/i3d_torchscript.pt`, `auxiliary/sfd_face.pth`, `auxiliary/vgg16-397923af.pth`, `auxiliary/vit_g_hybrid_pt_1200e_ssv2_ft.pth`。gated=False。

<a id="opentoonz"></a>

## opentoonz

作画、彩色、撮影を扱う2Dアニメ制作アプリ。

- **リポジトリ**: https://github.com/opentoonz/opentoonz
- **分類**: desktop_tool / 非AI制作 / 定番の制作基盤
- **入力**: 線画、画像素材、タイムシート
- **出力**: 2Dアニメーション作品
- **環境**: Windows・macOSなど。配布とビルドの対応状況は公式参照。
- **依存**: 通常制作にAIモデル不要
- **制約・未確認**: 生成AIモデルそのものではない。既存の制作工程への適合性を確認する。
- **編集者評価**: AI生成素材を手で仕上げる制作基盤として有用。
- **メトリクス**: ★7,806、fork 886、作成 2016-03-18、最終push 2026-10-09T21:44:07Z、archived=False
- **確認**: 2026-09-09 / コミット `1ef22259b9cf64c9d8710daebc131b401932e81b`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/opentoonz/opentoonz/tree/1ef22259b9cf64c9d8710daebc131b401932e81b)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/opentoonz/opentoonz/blob/1ef22259b9cf64c9d8710daebc131b401932e81b/README.md) / [GitHub API](https://api.github.com/repos/opentoonz/opentoonz) / [固定ツリー](https://github.com/opentoonz/opentoonz/tree/1ef22259b9cf64c9d8710daebc131b401932e81b)

### 制作に使う際の検討

原画・中割り・彩色結果をタイムシートに載せて仕上げる。AI動画をそのまま完成カットと扱わない制作経路。

**次に確かめること（実施前）**: 彩色連番の読込、線の透明度、コマ打ち、カメラ、音付き出力を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [toonz/sources/toonz/main.cpp](https://github.com/opentoonz/opentoonz/blob/1ef22259b9cf64c9d8710daebc131b401932e81b/toonz/sources/toonz/main.cpp)

**最新GitHub Release**: [v1.8.0](https://github.com/opentoonz/opentoonz/releases/tag/v1.8.0) / 2026-06-19T06:16:15Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T07:31:50Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="tooncomposer"></a>

## ToonComposer

キーフレーム後の中割りと彩色を生成AIでまとめて処理する。

- **リポジトリ**: https://github.com/TencentARC/ToonComposer
- **分類**: model / AIモデル・学習 / 研究・技術評価候補
- **入力**: キーフレーム・スケッチ等の制作条件
- **出力**: 彩色されたアニメーション動画
- **環境**: Python環境、モデル取得、Gradio UI。
- **依存**: ToonComposer重みと基盤モデル。配布条件は公式参照
- **制約・未確認**: 最終pushは2025年8月。最近の開発活発度は低く、研究上の有望性と区別する。
- **編集者評価**: 原画以降の制作工程への関連が高い。READMEはICLR 2026と記載。
- **メトリクス**: ★591、fork 62、作成 2025-08-12、最終push 2025-08-20T06:21:56Z、archived=False
- **確認**: 2026-09-09 / コミット `53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/TencentARC/ToonComposer/tree/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/TencentARC/ToonComposer/blob/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c/README.md) / [GitHub API](https://api.github.com/repos/TencentARC/ToonComposer) / [固定ツリー](https://github.com/TencentARC/ToonComposer/tree/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c)

### 制作に使う際の検討

決定したキーフレームとスケッチを使う制作制御の候補。自由生成動画より入力作画の保持を重視して比較する。

**次に確かめること（実施前）**: 指定した線・色・キーフレームが保持されるか、同じ素材をAniDoc等へ渡して比較する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [app.py](https://github.com/TencentARC/ToonComposer/blob/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c/app.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-08-20T06:21:47Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [TencentARC/ToonComposer](https://huggingface.co/TencentARC/ToonComposer) — file_listing_checked、確認日 2026-09-09、revision `a166c2c0f0755af6b1876586739e818e92e5c44f`。代表ファイル: `480p/tooncomposer.ckpt`, `608p/tooncomposer.ckpt`。gated=False。

<a id="tooncrafter"></a>

## ToonCrafter

二枚のアニメ画像の間を生成する補間モデル。

- **リポジトリ**: https://github.com/Doubiiu/ToonCrafter
- **分類**: model / AIモデル・学習 / モデル・研究候補
- **入力**: 始点・終点画像、任意のスケッチ制御
- **出力**: 中間フレームの動画
- **環境**: 公式経路は512×320・最大16フレーム。READMEの利用報告で24〜27GB VRAM。
- **依存**: 独自チェックポイント、PyTorch、Gradio
- **制約・未確認**: 第三者の軽量化版と公式実装の必要メモリを混同しない。2025年から更新が少ない。
- **編集者評価**: 二枚の決定原画の間を試作する比較基準。完成カットのタイミングは編集で決める。
- **メトリクス**: ★6,031、fork 532、作成 2024-05-28、最終push 2025-03-19T06:43:54Z、archived=False
- **確認**: 2026-09-09 / コミット `b0c47ff339c5e5ec45b84d0c6587850f242d41ef`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Doubiiu/ToonCrafter/tree/b0c47ff339c5e5ec45b84d0c6587850f242d41ef)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Doubiiu/ToonCrafter/blob/b0c47ff339c5e5ec45b84d0c6587850f242d41ef/README.md) / [GitHub API](https://api.github.com/repos/Doubiiu/ToonCrafter) / [固定ツリー](https://github.com/Doubiiu/ToonCrafter/tree/b0c47ff339c5e5ec45b84d0c6587850f242d41ef)

### 制作に使う際の検討

二枚の決定原画の間を試作する比較基準。完成カットのタイミングは編集で決める。

**次に確かめること（実施前）**: 大きな姿勢差と遮蔽のある2枚で、輪郭崩れ・勝手な中間動作を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [scripts/run.sh](https://github.com/Doubiiu/ToonCrafter/blob/b0c47ff339c5e5ec45b84d0c6587850f242d41ef/scripts/run.sh) / [configs/training_1024_v1.0/run.sh](https://github.com/Doubiiu/ToonCrafter/blob/b0c47ff339c5e5ec45b84d0c6587850f242d41ef/configs/training_1024_v1.0/run.sh)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-03-19T06:43:54Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Doubiiu/ToonCrafter](https://huggingface.co/Doubiiu/ToonCrafter) — file_listing_checked、確認日 2026-09-09、revision `7c56c5a23d9f8a9d99398e2a2491fff4bd6cffaf`。代表ファイル: `model.ckpt`, `sketch_encoder.ckpt`, `sketch_extractor.pth`。gated=False。

<a id="comic-manga-narrator"></a>

## comic-manga-narrator

漫画/コミックページを、コマ検出・セリフの音声化・ナレーション・Ken Burnsと2.5Dパララックスで演出したナレーション付きMP4に変換するローカルパイプライン。

- **リポジトリ**: https://github.com/MushiSenpai/comic-manga-narrator
- **分類**: pipeline / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 漫画ページ画像、PDF（章単位）
- **出力**: ナレーション付きMP4、中間ファイル（page.json / script.json / cast.json / timing.json）
- **環境**: Nemotron NIM(vLLM :8000)、音声ゲートウェイ+Fish Speech 1.5(:9000)、FFmpeg 6.x以上。READMEはRTX 5090/Ubuntu 24.04で検証と記載。
- **依存**: Nemotron-3-Nano-Omni、Fish Speech 1.5、ACE-Step、DepthFlow(Depth-Anything-V2)、Freesound、ffmpeg
- **制約・未確認**: 特定の自前スタック（Mushishi）を前提とした構成で、公開モデルへの差し替えはREADMEの範囲では未検証。Freesound APIキーは任意。READMEはライセンス表記がなく、権利条件は未確認。
- **編集者評価**: 権利クリーンなサンプル（Pepper & Carrot）で通しで生成した出力が同梱され、漫画→動画の制作フローとして具体的。
- **メトリクス**: ★0、fork 0、作成 2026-06-10、最終push 2026-07-12T17:50:47Z、archived=False
- **確認**: 2026-10-01 / コミット `38bac4fad34da68273de278a3fa85abc334b8308`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/MushiSenpai/comic-manga-narrator/tree/38bac4fad34da68273de278a3fa85abc334b8308)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/MushiSenpai/comic-manga-narrator/blob/38bac4fad34da68273de278a3fa85abc334b8308/README.md) / [GitHub API](https://api.github.com/repos/MushiSenpai/comic-manga-narrator) / [固定ツリー](https://github.com/MushiSenpai/comic-manga-narrator/tree/38bac4fad34da68273de278a3fa85abc334b8308)

### 制作に使う際の検討

漫画の読み聞かせ・二創動画化の実験パイプラインとして試せる。

**次に確かめること（実施前）**: 権利クリーンな自前ページで通し実行し、VRAM使用量と所要時間、音声同期を記録する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [serving/indextts2/server.py](https://github.com/MushiSenpai/comic-manga-narrator/blob/38bac4fad34da68273de278a3fa85abc334b8308/serving/indextts2/server.py)

**最新GitHub Release**: [v0.7.0](https://github.com/MushiSenpai/comic-manga-narrator/releases/tag/v0.7.0) / 2026-06-11T16:02:35Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-12T17:50:36Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="vedgen"></a>

## vedGen

一行のあらすじから絵コンテ→ショット別I2V→結合までをローカルGPUで回すアニメ風短編動画生成ライブラリ。ComfyUIをヘッドレスでAPI駆動し、Pythonライブラリとして呼び出す。

- **リポジトリ**: https://github.com/HarisUmer/vedGen
- **分類**: pipeline / AIモデル・学習 / 小規模・初期評価候補
- **入力**: あらすじ（premise）文、YAML設定、Comfy API形式のワークフローJSON
- **出力**: ショット別キーフレーム画像、ショット別クリップ、結合済みstory.mp4
- **環境**: READMEの想定はRTX 3060 12GB＋32GB RAM。CUDA版PyTorch、requirements.txt、vendor/ComfyUIのrequirements、重みDL時はCIVITAI_API_TOKEN。
- **依存**: ComfyUI（headless）とカスタムノード、Animagine XL、Wan 2.1 I2V、ffmpeg、Civitai/HF
- **制約・未確認**: 既定ではインストールも重みDLも行わない。リポジトリは小規模・初期段階で、READMEにLICENSEファイルの実体はない。finalはT5をCPU/RAMへ逃がす構成を含む。
- **編集者評価**: plan_story→render_keyframes→animate_shots→assembleの一貫APIと、fast/finalの二段構成＋OOM時フォールバックで12GB GPUを狙う設計。
- **メトリクス**: ★1、fork 0、作成 2026-07-22、最終push 2026-07-22T05:34:37Z、archived=False
- **確認**: 2026-10-02 / コミット `596f32ade8967725a3f8c54ba00d0f7ab288112d`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/HarisUmer/vedGen/tree/596f32ade8967725a3f8c54ba00d0f7ab288112d)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/HarisUmer/vedGen/blob/596f32ade8967725a3f8c54ba00d0f7ab288112d/README.md) / [GitHub API](https://api.github.com/repos/HarisUmer/vedGen) / [固定ツリー](https://github.com/HarisUmer/vedGen/tree/596f32ade8967725a3f8c54ba00d0f7ab288112d)

### 制作に使う際の検討

短編のプリビズ／キーフレーム検討から動画化までの試作。

**次に確かめること（実施前）**: plan_storyのみ実行し、ショット分割の妥当性と再現性を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/HarisUmer/vedGen/blob/596f32ade8967725a3f8c54ba00d0f7ab288112d/README.md)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-07-22T05:34:31Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="vocaloid-style-mv-pipeline"></a>

## vocaloid-style-mv-pipeline

楽曲と歌詞からボカロ風の手書きリリックMVを作る制作パイプライン。各フレームをCanvas2D/WebGL2で決定論的に描画し、Playwrightとffmpegで1080pマスターと9:16版を書き出す。

- **リポジトリ**: https://github.com/EGSECDA/vocaloid-style-mv-pipeline
- **分類**: pipeline / AI連携 / 活発・実用候補
- **入力**: song.wav、公式歌詞（任意で人声分離・強制アラインメント）、キャラ設定・参照素材
- **出力**: 1920x1080マスター、1080x1920縦版、共有用エンコード、JIZURAマークアップ付きLRC
- **環境**: Playwright/Node.js、ffmpeg、librosa等の解析、トゥーン3D使用時はBlender 5.x。READMEはRTX 3080で4分MVを約4分と記載。
- **依存**: Claude Code等のエージェント、ffmpeg、librosa、faster-whisper、Blender（任意）
- **制約・未確認**: 速度・作例は作者環境での値。AI画像生成はCodex CLI経由の例として示され、任意の画像モデルに置換可能と記載。
- **編集者評価**: 曲解析・歌詞タイミング・シーンライブラリ・レビューまで工程が文書化され、コードとして再現できる点が特徴。
- **メトリクス**: ★92、fork 6、作成 2026-10-04、最終push 2026-10-04T11:38:15Z、archived=False
- **確認**: 2026-10-10 / コミット `13b380dab077d4c8ea956825c9693c720e0c2b91`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/EGSECDA/vocaloid-style-mv-pipeline/tree/13b380dab077d4c8ea956825c9693c720e0c2b91)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/EGSECDA/vocaloid-style-mv-pipeline/blob/13b380dab077d4c8ea956825c9693c720e0c2b91/README.md) / [GitHub API](https://api.github.com/repos/EGSECDA/vocaloid-style-mv-pipeline) / [固定ツリー](https://github.com/EGSECDA/vocaloid-style-mv-pipeline/tree/13b380dab077d4c8ea956825c9693c720e0c2b91)

### 制作に使う際の検討

楽曲のリリックMVをコード管理で量産・修正したい制作に向く。

**次に確かめること（実施前）**: 短い楽曲でテンプレートを複製し、1シーンのみレンダリングして9:16再組版と歌詞同期を確認。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [skills/vocaloid-style-mv/template/engine/core/main.js](https://github.com/EGSECDA/vocaloid-style-mv-pipeline/blob/13b380dab077d4c8ea956825c9693c720e0c2b91/skills/vocaloid-style-mv/template/engine/core/main.js)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-10-04T11:38:12Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="aicomics"></a>

## AIComics

物語から分鏡・作画・配音・公開までをローカルで回すAI漫劇の制作システム。LLMで脚本と分鏡、ComfyUI+SDXLでキーフレーム、TTSで音声を作り、動画生成や投稿までモジュール化する。

- **リポジトリ**: https://github.com/chfr19820610-cell/AIComics
- **分類**: pipeline / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 物語/小説テキスト、キャラ設定、スタイル設定
- **出力**: 分鏡済みの動画、字幕、サムネイル、公開用ファイル
- **環境**: Python 3.12以上、ComfyUI、FFmpeg。動画生成はKling/Seedance/Wan等の外部プロバイダ。Electronデスクトップあり。
- **依存**: ComfyUI+SDXL、LLM API、Piper TTS、FFmpeg、social-auto-upload
- **制約・未確認**: READMEが主張する多数のモジュールとテスト数は第三者検証が未確認。商用ハンドブックへの導線がある。
- **編集者評価**: 脚本→分鏡→画像→動画→品質チェック→投稿までをモジュールとAPIで分けた構成が具体的。READMEは販売導線の記述が多い。
- **メトリクス**: ★24、fork 8、作成 2026-07-18、最終push 2026-09-26T06:31:23Z、archived=False
- **確認**: 2026-10-10 / コミット `e0862d048552d19f4d136a3e16dd98cabf72bbd2`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/chfr19820610-cell/AIComics/tree/e0862d048552d19f4d136a3e16dd98cabf72bbd2)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/chfr19820610-cell/AIComics/blob/e0862d048552d19f4d136a3e16dd98cabf72bbd2/README.md) / [GitHub API](https://api.github.com/repos/chfr19820610-cell/AIComics) / [固定ツリー](https://github.com/chfr19820610-cell/AIComics/tree/e0862d048552d19f4d136a3e16dd98cabf72bbd2)

### 制作に使う際の検討

縦型漫劇やショート動画を一人で量産する実験に向く。

**次に確かめること（実施前）**: 短編1本をNovelインポート→分鏡→1話分だけ画像/動画/音声を通し、品質ゲートの挙動を確認。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [desktop/main.js](https://github.com/chfr19820610-cell/AIComics/blob/e0862d048552d19f4d136a3e16dd98cabf72bbd2/desktop/main.js) / [main.py](https://github.com/chfr19820610-cell/AIComics/blob/e0862d048552d19f4d136a3e16dd98cabf72bbd2/main.py) / [src/aicomic/cli/main.py](https://github.com/chfr19820610-cell/AIComics/blob/e0862d048552d19f4d136a3e16dd98cabf72bbd2/src/aicomic/cli/main.py)

**最新GitHub Release**: [v5.1.0](https://github.com/chfr19820610-cell/AIComics/releases/tag/v5.1.0) / 2026-09-25T04:22:44Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-26T06:25:12Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
