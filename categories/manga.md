# 漫画・イラスト編集

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-07。**194件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ai-comic-factory](https://github.com/jbilcke-hf/ai-comic-factory) · [詳細](#ai-comic-factory) | LLMと画像生成を連携してコマを作るAI漫画アプリの参考実装。 | AI連携 / 旧版・履歴資料 | 1,341 / 2025-10-30 |
| [DiffSensei](https://github.com/jianzongwu/DiffSensei) · [詳細](#diffsensei) | 複数キャラ参照と配置を条件に白黒漫画のコマを生成する。 | AIモデル・学習 / モデル・研究候補 | 924 / 2025-02-05 |
| [krita](https://github.com/KDE/krita) · [詳細](#krita) | 漫画・イラスト制作に使うデジタルペイントアプリ。 | 非AI制作 / 定番の制作基盤 | 10,492 / 2026-10-07 |
| [manga-editor-desu](https://github.com/new-sankaku/manga-editor-desu) · [詳細](#manga-editor-desu) | ブラウザでコマ割り、吹き出し、縦書き、レイヤー編集とAI生成連携を行う。 | AIは任意 / 更新のある導入・評価候補 | 391 / 2026-10-07 |
| [MangaNinja](https://github.com/ali-vilab/MangaNinjia) · [詳細](#manganinjia) | 参照画像と点対応を使い、線画のキャラクターに指定色を反映する。 | AIモデル・学習 / モデル・研究候補 | 742 / 2025-03-02 |
| [OpenKoma](https://github.com/Reuben-Sun/OpenKoma) · [詳細](#openkoma) | 手持ち画像をコマに配置し、複数ページの漫画に組み立てる編集ツール。 | 非AI制作 / 小規模・初期評価候補 | 14 / 2026-05-08 |
| [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) · [詳細](#storydiffusion) | キャラクターの一貫性を保つ注意機構で連続画像・漫画素材を生成する。 | AIモデル・学習 / モデル・研究候補 | 6,471 / 2024-09-26 |
| [Venera-SSR](https://github.com/Kiastr/Venera-SSR) · [詳細](#venera-ssr) | 複数の漫画源に対応する漫画ビューアに、ローカルの白黒漫画着色・Anime4K超解像・OCR翻訳を統合した改版リーダー。 | AIモデル・学習 / 初期評価候補 | 55 / 2026-08-02 |
| [Manga-AI-detector](https://github.com/nonillion-studios/Manga-AI-detector) · [詳細](#manga-ai-detector) | 漫画・マンファ・コミックページ向けに追加学習したYOLOv11インスタンスセグメンテーションモデル。コマ枠(panels)・吹き出し(bubbles)・本文テキスト(text)・効果音(SFX)の4要素を検出する。 | AIモデル・学習 / 小規模・初期評価候補 | 4 / 2026-08-17 |
| [manga-colorizer](https://github.com/Mobai0z0/manga-colorizer) · [詳細](#manga-colorizer) | 白黒漫画（网点含む）の意味ベース自動彩色ツール。ONNXのSAM誘導ジェネレータで髪/肌/瞳/背景を配色し、Windowsデスクトップ（Tauri 2+Python）、ブラウザ、Dartエンジンで動作する。 | AIモデル・学習 / 小規模・初期評価候補 | 0 / 2026-10-07 |

<a id="ai-comic-factory"></a>

## ai-comic-factory

LLMと画像生成を連携してコマを作るAI漫画アプリの参考実装。

- **リポジトリ**: https://github.com/jbilcke-hf/ai-comic-factory
- **分類**: web_app / AI連携 / 旧版・履歴資料
- **入力**: ストーリー指示
- **出力**: コミックページ
- **環境**: Webアプリ環境と推論バックエンド。
- **依存**: LLM、SDXL等の設定された画像バックエンド
- **制約・未確認**: GitHubでarchived=true。現在の活発な開発候補には含めない。
- **編集者評価**: ストーリーからコマ生成への構成を学ぶ資料として残す。
- **メトリクス**: ★1,341、fork 310、作成 2023-08-25、最終push 2025-10-30T19:17:30Z、archived=True
- **確認**: 2026-09-09 / コミット `c5dc3c7dafeb593efa3b7c95431ee982965bb524`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/jbilcke-hf/ai-comic-factory/tree/c5dc3c7dafeb593efa3b7c95431ee982965bb524)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/jbilcke-hf/ai-comic-factory/blob/c5dc3c7dafeb593efa3b7c95431ee982965bb524/README.md) / [GitHub API](https://api.github.com/repos/jbilcke-hf/ai-comic-factory) / [固定ツリー](https://github.com/jbilcke-hf/ai-comic-factory/tree/c5dc3c7dafeb593efa3b7c95431ee982965bb524)

### 制作に使う際の検討

ページ全体を生成する過去のWebアプリ構成の参考。新規導入はアーカイブ状態と外部API依存を先に確認する。

**次に確かめること（実施前）**: サンプルのAPI設定が現在利用できるかを確認し、ページ生成が完了する最小例を再現する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/app/interface/page/index.tsx](https://github.com/jbilcke-hf/ai-comic-factory/blob/c5dc3c7dafeb593efa3b7c95431ee982965bb524/src/app/interface/page/index.tsx)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-10-30T19:17:19Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="diffsensei"></a>

## DiffSensei

複数キャラ参照と配置を条件に白黒漫画のコマを生成する。

- **リポジトリ**: https://github.com/jianzongwu/DiffSensei
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: キャラ参照、コマ説明、配置条件
- **出力**: 白黒漫画コマ
- **環境**: Python3.11、PyTorch/CUDA。MLLMなし版は小〜中サイズ・batch1で24GB4090の作者例。
- **依存**: 画像生成器、必要に応じMLLM、対応チェックポイント
- **制約・未確認**: 学習コードは調整が必要と作者が明記。漫画データは画像本体の一括配布ではない。台詞は別編集。
- **編集者評価**: 多人数の顔と配置を制御する漫画研究として優先比較したい。
- **メトリクス**: ★924、fork 101、作成 2024-12-03、最終push 2025-02-05T03:02:38Z、archived=False
- **確認**: 2026-09-09 / コミット `9fed2ab50c89f19da12d7796edfa6a41eebf23c8`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/jianzongwu/DiffSensei/tree/9fed2ab50c89f19da12d7796edfa6a41eebf23c8)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/jianzongwu/DiffSensei/blob/9fed2ab50c89f19da12d7796edfa6a41eebf23c8/README.md) / [GitHub API](https://api.github.com/repos/jianzongwu/DiffSensei) / [固定ツリー](https://github.com/jianzongwu/DiffSensei/tree/9fed2ab50c89f19da12d7796edfa6a41eebf23c8)

### 制作に使う際の検討

多人数の顔と配置を制御する漫画研究として優先比較したい。

**次に確かめること（実施前）**: 二人の見た目の混線、位置・表情指定、吹き出し領域、MLLM有無の差を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [scripts/demo/gradio_wo_mllm.py](https://github.com/jianzongwu/DiffSensei/blob/9fed2ab50c89f19da12d7796edfa6a41eebf23c8/scripts/demo/gradio_wo_mllm.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-02-05T03:02:02Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [jianzongwu/DiffSensei](https://huggingface.co/jianzongwu/DiffSensei) — file_listing_checked、確認日 2026-09-09、revision `d862c11da74705eab282f6543ede76be9331c586`。代表ファイル: `image_generator/clip_image_encoder/model.safetensors`, `image_generator/image_proj_model/pytorch_model.bin`, `image_generator/magi_image_encoder/pytorch_model.bin`, `image_generator/unet/pytorch_model.bin`。gated=False。

<a id="krita"></a>

## krita

漫画・イラスト制作に使うデジタルペイントアプリ。

- **リポジトリ**: https://github.com/KDE/krita
- **分類**: desktop_tool / 非AI制作 / 定番の制作基盤
- **入力**: ラフ、筆入力、画像素材
- **出力**: イラスト・漫画用デジタル原稿
- **環境**: Windows・macOS・Linux向け配布。
- **依存**: 通常の描画にはAIモデル不要
- **制約・未確認**: GitHubは公式ミラーで、開発元はKDE。標準アプリをAI生成モデルとして扱わない。
- **編集者評価**: 生成結果の手直しや原稿制作を担う定番基盤。
- **メトリクス**: ★10,492、fork 875、作成 2015-10-09、最終push 2026-10-07T09:40:12Z、archived=False
- **確認**: 2026-09-09 / コミット `75db0d95e142c9251dc27483180148f77d4de014`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/KDE/krita/tree/75db0d95e142c9251dc27483180148f77d4de014)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/KDE/krita/blob/75db0d95e142c9251dc27483180148f77d4de014/README.md) / [GitHub API](https://api.github.com/repos/KDE/krita) / [固定ツリー](https://github.com/KDE/krita/tree/75db0d95e142c9251dc27483180148f77d4de014)

### 制作に使う際の検討

線・文字・トーンを人が確定する原稿の中心に置く。AI連携は別プラグインで選べる。

**次に確かめること（実施前）**: 縦書き、トーン、印刷解像度、レイヤー保持、PDF等の入稿経路を自作1ページで確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [krita/main.cc](https://github.com/KDE/krita/blob/75db0d95e142c9251dc27483180148f77d4de014/krita/main.cc)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-09T01:54:43Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="manga-editor-desu"></a>

## manga-editor-desu

ブラウザでコマ割り、吹き出し、縦書き、レイヤー編集とAI生成連携を行う。

- **リポジトリ**: https://github.com/new-sankaku/manga-editor-desu
- **分類**: browser_tool / AIは任意 / 更新のある導入・評価候補
- **入力**: 画像、セリフ、コマ割り、生成指示
- **出力**: 漫画ページ・複数ページの編集プロジェクト
- **環境**: ブラウザ。AI生成には対応するローカルバックエンド等。
- **依存**: 画像素材、任意の画像生成バックエンド
- **制約・未確認**: 文字・吹き出しやページ切り替え時の編集履歴などは実作業で確認が必要。
- **編集者評価**: 漫画固有の編集操作と画像生成をつなぐ有力候補。
- **メトリクス**: ★391、fork 58、作成 2023-08-14、最終push 2026-10-07T18:34:59Z、archived=False
- **確認**: 2026-09-09 / コミット `04e0cf3de1f3677682f6d1831f2713db70e441ba`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/new-sankaku/manga-editor-desu/tree/04e0cf3de1f3677682f6d1831f2713db70e441ba)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/new-sankaku/manga-editor-desu/blob/04e0cf3de1f3677682f6d1831f2713db70e441ba/README.md) / [GitHub API](https://api.github.com/repos/new-sankaku/manga-editor-desu) / [固定ツリー](https://github.com/new-sankaku/manga-editor-desu/tree/04e0cf3de1f3677682f6d1831f2713db70e441ba)

### 制作に使う際の検討

生成済み素材を編集可能なページへ配置する用途。画像生成器の選定とコマ編集UIの評価を分ける。

**次に確かめること（実施前）**: 複数ページを保存・再読込し、縦書き・吹き出し・履歴・出力解像度が維持されるか確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [99_server.py](https://github.com/new-sankaku/manga-editor-desu/blob/04e0cf3de1f3677682f6d1831f2713db70e441ba/99_server.py) / [service-worker.js](https://github.com/new-sankaku/manga-editor-desu/blob/04e0cf3de1f3677682f6d1831f2713db70e441ba/service-worker.js)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-30T17:00:13Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="manganinjia"></a>

## MangaNinja

参照画像と点対応を使い、線画のキャラクターに指定色を反映する。

- **リポジトリ**: https://github.com/ali-vilab/MangaNinjia
- **分類**: model / AIモデル・学習 / モデル・研究候補
- **入力**: 線画、カラー参照、対応点
- **出力**: 彩色画像
- **環境**: Python/PyTorch、infer.pyまたはrun_gradio.py。
- **依存**: SD1.5系、CLIP、線画ControlNet、独自重み
- **制約・未確認**: GitHub READMEはCC BY-NC 4.0表記、HFメタデータはApache-2.0で不一致。6GB案内は第三者Windows版。
- **編集者評価**: 服・髪・小物の色を指定したいときの候補。ページ作成や台詞組版は別工程。
- **メトリクス**: ★742、fork 60、作成 2024-12-23、最終push 2025-03-02T07:20:37Z、archived=False
- **確認**: 2026-09-09 / コミット `6363c81aaedab0a435d18cba9209a7e842881ad7`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/ali-vilab/MangaNinjia/tree/6363c81aaedab0a435d18cba9209a7e842881ad7)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ali-vilab/MangaNinjia/blob/6363c81aaedab0a435d18cba9209a7e842881ad7/README.md) / [GitHub API](https://api.github.com/repos/ali-vilab/MangaNinjia) / [固定ツリー](https://github.com/ali-vilab/MangaNinjia/tree/6363c81aaedab0a435d18cba9209a7e842881ad7)

### 制作に使う際の検討

服・髪・小物の色を指定したいときの候補。ページ作成や台詞組版は別工程。

**次に確かめること（実施前）**: 点を追加する前後で色の混線と元線画の変化を比較し、利用条件の不一致を配布元で確認する。

**利用条件の確認メモ**: README/バッジCC BY-NC 4.0とHFメタデータApache-2.0が不一致。寛容な方を採用せず配布元で確認する。 商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [infer.py](https://github.com/ali-vilab/MangaNinjia/blob/6363c81aaedab0a435d18cba9209a7e842881ad7/infer.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-03-02T07:20:37Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Johanan0528/MangaNinjia](https://huggingface.co/Johanan0528/MangaNinjia) — file_listing_checked、確認日 2026-09-09、revision `4e6237c1d22415272bf98426616fe478cd3202a0`。代表ファイル: `controlnet.pth`, `denoising_unet.pth`, `point_net.pth`, `reference_unet.pth`。gated=False。

<a id="openkoma"></a>

## OpenKoma

手持ち画像をコマに配置し、複数ページの漫画に組み立てる編集ツール。

- **リポジトリ**: https://github.com/Reuben-Sun/OpenKoma
- **分類**: browser_tool / 非AI制作 / 小規模・初期評価候補
- **入力**: キャラ画像、背景、セリフ
- **出力**: 漫画ページPNG、PDF、プロジェクトJSON
- **環境**: ブラウザ、ソース実行はNode.js。
- **依存**: 入力する画像・テキスト素材
- **制約・未確認**: 小規模な新規候補。AI画像モデルそのものは含まない。
- **編集者評価**: 生成画像を編集可能な漫画ページへまとめる用途が具体的。
- **メトリクス**: ★14、fork 2、作成 2026-04-05、最終push 2026-05-08T08:27:39Z、archived=False
- **確認**: 2026-09-09 / コミット `aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Reuben-Sun/OpenKoma/tree/aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Reuben-Sun/OpenKoma/blob/aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c/README.md) / [GitHub API](https://api.github.com/repos/Reuben-Sun/OpenKoma) / [固定ツリー](https://github.com/Reuben-Sun/OpenKoma/tree/aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c)

### 制作に使う際の検討

PNG/PDFとプロジェクトJSONを併用し、画像だけの成果物から編集情報を保持する候補。

**次に確かめること（実施前）**: 3ページで保存・復元、台詞修正、フォント欠落、PDFのページ順を点検する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/main.tsx](https://github.com/Reuben-Sun/OpenKoma/blob/aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c/src/main.tsx) / [src/App.tsx](https://github.com/Reuben-Sun/OpenKoma/blob/aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c/src/App.tsx)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-05-08T08:27:22Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="storydiffusion"></a>

## StoryDiffusion

キャラクターの一貫性を保つ注意機構で連続画像・漫画素材を生成する。

- **リポジトリ**: https://github.com/HVision-NKU/StoryDiffusion
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: シーン記述、キャラクター指定・参照
- **出力**: 連続画像、漫画素材
- **環境**: 低VRAM例でも24GB GPU・30GB RAMで作者検証、20GB超を想定。
- **依存**: SDXL、版・経路によりPhotoMaker等
- **制約・未確認**: 動画モデルのソースと重みは現READMEのTODOで未公開。画像生成と動画研究の公開範囲を区別する。
- **編集者評価**: 画像の連続性を比較する既存研究。動画公開済み候補としては使わない。
- **メトリクス**: ★6,471、fork 645、作成 2024-04-21、最終push 2024-09-26T02:17:52Z、archived=False
- **確認**: 2026-09-09 / コミット `8de45e424887766fdd84dc917436ff8605f00149`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/HVision-NKU/StoryDiffusion/tree/8de45e424887766fdd84dc917436ff8605f00149)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/HVision-NKU/StoryDiffusion/blob/8de45e424887766fdd84dc917436ff8605f00149/README.md) / [GitHub API](https://api.github.com/repos/HVision-NKU/StoryDiffusion) / [固定ツリー](https://github.com/HVision-NKU/StoryDiffusion/tree/8de45e424887766fdd84dc917436ff8605f00149)

### 制作に使う際の検討

画像の連続性を比較する既存研究。動画公開済み候補としては使わない。

**次に確かめること（実施前）**: 服・顔・小物を固定した6コマで、一貫性とプロンプト追従を別々に採点する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [gradio_app_sdxl_specific_id_low_vram.py](https://github.com/HVision-NKU/StoryDiffusion/blob/8de45e424887766fdd84dc917436ff8605f00149/gradio_app_sdxl_specific_id_low_vram.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2024-09-26T02:17:52Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="venera-ssr"></a>

## Venera-SSR

複数の漫画源に対応する漫画ビューアに、ローカルの白黒漫画着色・Anime4K超解像・OCR翻訳を統合した改版リーダー。

- **リポジトリ**: https://github.com/Kiastr/Venera-SSR
- **分類**: desktop_tool / AIモデル・学習 / 初期評価候補
- **入力**: ローカルまたはネットワークの漫画画像・漫画源
- **出力**: 着色・高解像度化・翻訳表示されたページ
- **環境**: FlutterとRustのツールチェーンでビルド。
- **依存**: Anime4K、OCR・翻訳モデル。
- **制約・未確認**: 着色機能はテスト中の分支で追加モデルを検証中とREADMEが記載。権利面の注意も明記。
- **編集者評価**: 読みながら端末内で着色と超解像、埋め込み文字の翻訳を行える点が特徴的で、Flutter/Rustでビルドする。
- **メトリクス**: ★55、fork 4、作成 2026-02-28、最終push 2026-08-02T14:11:49Z、archived=False
- **確認**: 2026-09-30 / コミット `07ac77fcbd6c9050a5313f327e28d617eb602488`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Kiastr/Venera-SSR/tree/07ac77fcbd6c9050a5313f327e28d617eb602488)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Kiastr/Venera-SSR/blob/07ac77fcbd6c9050a5313f327e28d617eb602488/README.md) / [GitHub API](https://api.github.com/repos/Kiastr/Venera-SSR) / [固定ツリー](https://github.com/Kiastr/Venera-SSR/tree/07ac77fcbd6c9050a5313f327e28d617eb602488)

### 制作に使う際の検討

漫画制作・確認時のラフな着色や文字置換の検討に利用。

**次に確かめること（実施前）**: 代表的なページで着色とAnime4K、OCR翻訳の精度・速度を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [windows/runner/main.cpp](https://github.com/Kiastr/Venera-SSR/blob/07ac77fcbd6c9050a5313f327e28d617eb602488/windows/runner/main.cpp)

**最新GitHub Release**: [v2.1.5](https://github.com/Kiastr/Venera-SSR/releases/tag/v2.1.5) / 2026-08-01T05:16:58Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-02T14:11:49Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="manga-ai-detector"></a>

## Manga-AI-detector

漫画・マンファ・コミックページ向けに追加学習したYOLOv11インスタンスセグメンテーションモデル。コマ枠(panels)・吹き出し(bubbles)・本文テキスト(text)・効果音(SFX)の4要素を検出する。

- **リポジトリ**: https://github.com/nonillion-studios/Manga-AI-detector
- **分類**: model / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 漫画/コミックのページ画像（ファイルまたはbase64）
- **出力**: クラス名・confidence・bounding box・中心座標を含むJSON、可視化画像
- **環境**: Python 3.8+、ultralytics。推論はCPU可、GPU任意。学習推奨はRTX 3060/4060以上・8GB+ VRAM、CUDA 11.8/12.x。
- **依存**: Ultralytics YOLOv11、PyTorch、OpenCV、best.pt（同梱の学習済み重み）
- **制約・未確認**: 学習データの規模や精度指標（mAP等）はREADMEに記載がなく検出精度は未確認。REST API化のコードはREADME内のサンプル記載で、そのまま動く形では同梱されていない。
- **編集者評価**: 翻訳や読み上げパイプラインの前段（コマ・吹き出し検出）として用途が明確で、重みbest.ptと推論/学習スクリプトを同梱する。
- **メトリクス**: ★4、fork 0、作成 2026-07-30、最終push 2026-08-17T20:32:39Z、archived=False
- **確認**: 2026-10-01 / コミット `becb02ca3f2e5e01df4822045d001443442cf4ff`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/nonillion-studios/Manga-AI-detector/tree/becb02ca3f2e5e01df4822045d001443442cf4ff)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/nonillion-studios/Manga-AI-detector/blob/becb02ca3f2e5e01df4822045d001443442cf4ff/readme.md) / [GitHub API](https://api.github.com/repos/nonillion-studios/Manga-AI-detector) / [固定ツリー](https://github.com/nonillion-studios/Manga-AI-detector/tree/becb02ca3f2e5e01df4822045d001443442cf4ff)

### 制作に使う際の検討

漫画翻訳のコマ・吹き出し検出の候補として試せる。

**次に確かめること（実施前）**: 実際の日本語漫画ページで4クラスの検出再現率と誤検出を測り、既存の検出器と比較する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [inference.py](https://github.com/nonillion-studios/Manga-AI-detector/blob/becb02ca3f2e5e01df4822045d001443442cf4ff/inference.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-17T20:32:39Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="manga-colorizer"></a>

## manga-colorizer

白黒漫画（网点含む）の意味ベース自動彩色ツール。ONNXのSAM誘導ジェネレータで髪/肌/瞳/背景を配色し、Windowsデスクトップ（Tauri 2+Python）、ブラウザ、Dartエンジンで動作する。

- **リポジトリ**: https://github.com/Mobai0z0/manga-colorizer
- **分類**: desktop_tool / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 白黒漫画ページ画像、任意のヒント点や参照カラー画像
- **出力**: 彩色済み画像（Labのa/bのみ変更し、Lは原稿を保持）
- **環境**: Windowsデスクトップ（Tauri 2+Python）またはブラウザ。DirectML/CUDA、無ければCPUにフォールバック。
- **依存**: ONNX彩色モデル（SAM誘導generator）、Tauri/Python sidecar、WebCanvas
- **制約・未確認**: モデル重みはCC BY-NC-SA 4.0でリポジトリ非同梱、別途ダウンロードが必要。コードはApache-2.0。
- **編集者評価**: 网点や長尺ページ（1024px超はタイル推論）に対応し、明度を保存する設計が漫画彩色の用途に合う。
- **メトリクス**: ★0、fork 0、作成 2026-09-23、最終push 2026-10-07T13:58:13Z、archived=False
- **確認**: 2026-10-05 / コミット `f1bbf26d434be05f66a0a5f66ab821a1fd10c78d`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Mobai0z0/manga-colorizer/tree/f1bbf26d434be05f66a0a5f66ab821a1fd10c78d)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Mobai0z0/manga-colorizer/blob/f1bbf26d434be05f66a0a5f66ab821a1fd10c78d/readme.md) / [GitHub API](https://api.github.com/repos/Mobai0z0/manga-colorizer) / [固定ツリー](https://github.com/Mobai0z0/manga-colorizer/tree/f1bbf26d434be05f66a0a5f66ab821a1fd10c78d)

### 制作に使う際の検討

漫画の彩色補助・ラフ彩色に使えるが、モデルの商用条件に注意。

**次に確かめること（実施前）**: 网点の多いページで色滲みや破綻、タイル境界の連続性を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [src-tauri/src/main.rs](https://github.com/Mobai0z0/manga-colorizer/blob/f1bbf26d434be05f66a0a5f66ab821a1fd10c78d/src-tauri/src/main.rs) / [web/dist/app.js](https://github.com/Mobai0z0/manga-colorizer/blob/f1bbf26d434be05f66a0a5f66ab821a1fd10c78d/web/dist/app.js)

**最新GitHub Release**: [v0.5.12](https://github.com/Mobai0z0/manga-colorizer/releases/tag/v0.5.12) / 2026-10-07T14:08:53Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-24T04:40:21Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
