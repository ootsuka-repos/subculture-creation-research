# ゲーム・ノベル・スプライト

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-30。**136件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ControlTile](https://github.com/Junrongh/ControlTile) · [詳細](#controltile) | 条件付きの画像タイル生成を扱う研究実装。 | AIモデル・学習 / 小規模・初期候補 | 12 / 2026-07-27 |
| [Godot](https://github.com/godotengine/godot) · [詳細](#godot) | 2D/3Dゲーム制作と複数プラットフォームへの出力を行うゲームエンジン。 | 非AI制作 / 定番の制作基盤 | 118,011 / 2026-09-30 |
| [LDtk](https://github.com/deepnight/ldtk) · [詳細](#ldtk) | 2Dレベルを設計するオープンソースのエディタ。 | 非AI制作 / 制作基盤として比較 | 4,283 / 2026-07-12 |
| [OpenGame](https://github.com/leigest519/OpenGame) · [詳細](#opengame) | 指示からWebゲームを制作するエージェント基盤。テンプレートとデバッグ手順を組み込む。 | AI連携 / 連携・制作ツール候補 | 2,960 / 2026-09-03 |
| [Pixelorama](https://github.com/Orama-Interactive/Pixelorama) · [詳細](#pixelorama) | ドット絵・タイル・アニメーションを編集する制作アプリ。 | 非AI制作 / 定番の制作基盤 | 10,431 / 2026-09-30 |
| [PNGAL](https://github.com/1mm-module/PNGAL) · [詳細](#pngal) | 顔差分生成・PSD分解・目パチと口パクの補間を組み合わせ、立ち絵アニメ素材を制作する。 | AI連携 / 導入経路の追加確認が必要 | 350 / 2026-09-01 |
| [RenPy](https://github.com/renpy/renpy) · [詳細](#renpy) | テキストとキャラクター素材を組み合わせたノベルゲームを制作する。 | 非AI制作 / 定番の制作基盤 | 6,876 / 2026-09-30 |
| [sprite-maker](https://github.com/JohnKinyanjui/sprite-maker) · [詳細](#sprite-maker) | AIエージェントと連携して素材を作り、関節・ボーンとRust描画で再現可能なアニメーションを生成する。 | AI連携 / 初期評価候補 | 414 / 2026-09-24 |
| [Terrain Diffusion](https://github.com/xandergos/terrain-diffusion) · [詳細](#terrain-diffusion) | 広域地形を拡散モデルで生成し、地図から地形への変換も扱う。 | AIモデル・学習 / モデル・研究候補 | 1,410 / 2026-08-12 |
| [Tiled](https://github.com/mapeditor/tiled) · [詳細](#tiled) | タイルとオブジェクトを配置して2Dゲームのマップを作る。 | 非AI制作 / 制作基盤として比較 | 12,932 / 2026-09-25 |

<a id="controltile"></a>

## ControlTile

条件付きの画像タイル生成を扱う研究実装。

- **リポジトリ**: https://github.com/Junrongh/ControlTile
- **分類**: model / AIモデル・学習 / 小規模・初期候補
- **入力**: タイル生成条件、参照データ
- **出力**: タイル画像
- **環境**: Python3.10、PyTorch Lightning系、作者設定。
- **依存**: ModelScope配布のmodel-lora.ckpt、データセット
- **制約・未確認**: 配布URLは確認したが、重みファイルの一覧・取得・推論は未検証。ゲームのマップ配置とは別。
- **編集者評価**: タイルの連続性と制御を研究したい場合の小規模候補。
- **メトリクス**: ★12、fork 2、作成 2026-05-01、最終push 2026-07-27T02:36:27Z、archived=False
- **確認**: 2026-09-09 / コミット `f3410e843742335ae3fa3298d2b335509da18893`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Junrongh/ControlTile/tree/f3410e843742335ae3fa3298d2b335509da18893)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Junrongh/ControlTile/blob/f3410e843742335ae3fa3298d2b335509da18893/README.md) / [GitHub API](https://api.github.com/repos/Junrongh/ControlTile) / [固定ツリー](https://github.com/Junrongh/ControlTile/tree/f3410e843742335ae3fa3298d2b335509da18893)

### 制作に使う際の検討

タイルの連続性と制御を研究したい場合の小規模候補。

**次に確かめること（実施前）**: 隣接タイルの境界、繰り返し時の継ぎ目、実際のタイルエディタへの取り込みを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [run.py](https://github.com/Junrongh/ControlTile/blob/f3410e843742335ae3fa3298d2b335509da18893/run.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-07-27T02:36:27Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="godot"></a>

## Godot

2D/3Dゲーム制作と複数プラットフォームへの出力を行うゲームエンジン。

- **リポジトリ**: https://github.com/godotengine/godot
- **分類**: engine / 非AI制作 / 定番の制作基盤
- **入力**: 2D/3D素材、シーン、スクリプト
- **出力**: 実行可能なゲーム
- **環境**: 各OS向けエディタ・エクスポート環境。
- **依存**: ゲーム用素材。AIモデルは必須でない
- **制約・未確認**: AI素材生成機能そのものではない。配布先ごとのビルド要件は別途確認。
- **編集者評価**: 生成素材を遊べる作品へ統合する定番基盤。
- **メトリクス**: ★118,011、fork 26,910、作成 2014-01-04、最終push 2026-09-30T19:42:59Z、archived=False
- **確認**: 2026-09-09 / コミット `9552dfb6859a1aaba1e570b8e0ef5c599b830f19`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/godotengine/godot/tree/9552dfb6859a1aaba1e570b8e0ef5c599b830f19)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/godotengine/godot/blob/9552dfb6859a1aaba1e570b8e0ef5c599b830f19/README.md) / [GitHub API](https://api.github.com/repos/godotengine/godot) / [固定ツリー](https://github.com/godotengine/godot/tree/9552dfb6859a1aaba1e570b8e0ef5c599b830f19)

### 制作に使う際の検討

完成素材を操作・勝敗・セーブを備えるゲームにする基盤。素材生成の品質とゲームとしての完成度を別評価する。

**次に確かめること（実施前）**: 1ステージで衝突、アニメ、音、セーブ、配布先での起動を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [main/main.cpp](https://github.com/godotengine/godot/blob/9552dfb6859a1aaba1e570b8e0ef5c599b830f19/main/main.cpp)

**最新GitHub Release**: [4.7.2-stable](https://github.com/godotengine/godot/releases/tag/4.7.2-stable) / 2026-08-18T16:12:28Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-08T16:54:40Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="ldtk"></a>

## LDtk

2Dレベルを設計するオープンソースのエディタ。

- **リポジトリ**: https://github.com/deepnight/ldtk
- **分類**: desktop_tool / 非AI制作 / 制作基盤として比較
- **入力**: タイル、エンティティ、レベル設計
- **出力**: レベルデータと配置情報
- **環境**: 配布アプリ。開発環境はHaxe等。
- **依存**: 対象エンジン側のインポータ
- **制約・未確認**: マップを作る道具で、ゲームロジックは生成しない。
- **編集者評価**: 小規模2Dゲームのレベル反復制作でTiledと比較したい。
- **メトリクス**: ★4,283、fork 288、作成 2020-05-29、最終push 2026-07-12T13:55:51Z、archived=False
- **確認**: 2026-09-09 / コミット `6d69bd1d6be92f01ac30778f6a934f0da8448b16`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/deepnight/ldtk/tree/6d69bd1d6be92f01ac30778f6a934f0da8448b16)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/deepnight/ldtk/blob/6d69bd1d6be92f01ac30778f6a934f0da8448b16/README.md) / [GitHub API](https://api.github.com/repos/deepnight/ldtk) / [固定ツリー](https://github.com/deepnight/ldtk/tree/6d69bd1d6be92f01ac30778f6a934f0da8448b16)

### 制作に使う際の検討

小規模2Dゲームのレベル反復制作でTiledと比較したい。

**次に確かめること（実施前）**: 隣接レベル、エンティティ参照、タイル更新時の再読み込みを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/electron.renderer/App.hx](https://github.com/deepnight/ldtk/blob/6d69bd1d6be92f01ac30778f6a934f0da8448b16/src/electron.renderer/App.hx) / [app/nwjs/electron-shim.js](https://github.com/deepnight/ldtk/blob/6d69bd1d6be92f01ac30778f6a934f0da8448b16/app/nwjs/electron-shim.js)

**最新GitHub Release**: [v1.5.3](https://github.com/deepnight/ldtk/releases/tag/v1.5.3) / 2024-01-15T15:18:29Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-12T13:55:51Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="opengame"></a>

## OpenGame

指示からWebゲームを制作するエージェント基盤。テンプレートとデバッグ手順を組み込む。

- **リポジトリ**: https://github.com/leigest519/OpenGame
- **分類**: pipeline / AI連携 / 連携・制作ツール候補
- **入力**: ゲーム仕様、素材条件、利用モデル設定
- **出力**: ゲームプロジェクトのコードと素材
- **環境**: Node.js20以上、ソースからの導入、モデルAPI設定。
- **依存**: LLMプロバイダ、画像・動画・音声の任意API
- **制約・未確認**: GameCoder-27Bは説明されるが本調査で公式重みは未特定。評価パイプラインはREADMEで公開予定。
- **編集者評価**: 遊べるゲームのコードを出す対象として、ゲーム風動画生成と区別して比較。
- **メトリクス**: ★2,960、fork 431、作成 2026-04-20、最終push 2026-09-03T17:11:09Z、archived=False
- **確認**: 2026-09-09 / コミット `c9bea37786af524bf3bbe802f2b67d23816fa5c0`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/leigest519/OpenGame/tree/c9bea37786af524bf3bbe802f2b67d23816fa5c0)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/leigest519/OpenGame/blob/c9bea37786af524bf3bbe802f2b67d23816fa5c0/README.md) / [GitHub API](https://api.github.com/repos/leigest519/OpenGame) / [固定ツリー](https://github.com/leigest519/OpenGame/tree/c9bea37786af524bf3bbe802f2b67d23816fa5c0)

### 制作に使う際の検討

遊べるゲームのコードを出す対象として、ゲーム風動画生成と区別して比較。

**次に確かめること（実施前）**: 小さな仕様でビルド、入力応答、勝敗、リスタート、ブラウザ互換を実操作で検証する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [scripts/start.js](https://github.com/leigest519/OpenGame/blob/c9bea37786af524bf3bbe802f2b67d23816fa5c0/scripts/start.js)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-03T17:11:09Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

本文を確認した箇所:

- [package.json](https://github.com/leigest519/OpenGame/blob/c9bea37786af524bf3bbe802f2b67d23816fa5c0/package.json): Node.js20以上、ワークスペースとCLI起動用scriptsを確認。ゲーム完成・評価再現の証明ではない。

<a id="pixelorama"></a>

## Pixelorama

ドット絵・タイル・アニメーションを編集する制作アプリ。

- **リポジトリ**: https://github.com/Orama-Interactive/Pixelorama
- **分類**: desktop_tool / 非AI制作 / 定番の制作基盤
- **入力**: ピクセルアート、フレーム、タイル素材
- **出力**: スプライト、タイル、アニメーション
- **環境**: Windows・Linux・macOS・Web。
- **依存**: 通常制作にAIモデル不要
- **制約・未確認**: AI画像生成モデルを内蔵するという意味ではない。
- **編集者評価**: 2Dゲーム素材の手直しと仕上げを担う定番候補。
- **メトリクス**: ★10,431、fork 551、作成 2019-08-18、最終push 2026-09-30T11:55:14Z、archived=False
- **確認**: 2026-09-09 / コミット `9263cf3636efc336aadbcc46c57dc614e57525b0`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Orama-Interactive/Pixelorama/tree/9263cf3636efc336aadbcc46c57dc614e57525b0)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Orama-Interactive/Pixelorama/blob/9263cf3636efc336aadbcc46c57dc614e57525b0/README.md) / [GitHub API](https://api.github.com/repos/Orama-Interactive/Pixelorama) / [固定ツリー](https://github.com/Orama-Interactive/Pixelorama/tree/9263cf3636efc336aadbcc46c57dc614e57525b0)

### 制作に使う際の検討

ピクセル境界・パレット・フレームを編集し、AI生成素材をドット絵として整える候補。

**次に確かめること（実施前）**: スプライトシートの余白、原点、フレーム時間、タイル境界をゲーム内で確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/Main.gd](https://github.com/Orama-Interactive/Pixelorama/blob/9263cf3636efc336aadbcc46c57dc614e57525b0/src/Main.gd)

**最新GitHub Release**: [v1.2.3](https://github.com/Orama-Interactive/Pixelorama/releases/tag/v1.2.3) / 2026-09-15T13:25:15Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-09T13:16:26Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="pngal"></a>

## PNGAL

顔差分生成・PSD分解・目パチと口パクの補間を組み合わせ、立ち絵アニメ素材を制作する。

- **リポジトリ**: https://github.com/1mm-module/PNGAL
- **分類**: desktop_tool / AI連携 / 導入経路の追加確認が必要
- **入力**: 透過PNG、Photoshop互換PSD
- **出力**: PSD、WebM、MP4、GIF、スプライトシート、JSON
- **環境**: Windows 10/11、NVIDIA CUDA。VRAM目安12GB以上、構成により24GB。
- **依存**: Qwen、See-through、RIFE、ComfyUI
- **制約・未確認**: 音声入力・顔追跡・マウス追従は非対応。正式配布ZIPのURLはREADMEに記載なし。
- **編集者評価**: 2026年8月作成、9月更新。素材制作からゲーム用出力まで一連の工程を扱う。
- **メトリクス**: ★350、fork 46、作成 2026-08-01、最終push 2026-09-01T15:53:21Z、archived=False
- **確認**: 2026-09-09 / コミット `7a00caec16e8e9d6734f3ee5264118f44aec157c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/1mm-module/PNGAL/tree/7a00caec16e8e9d6734f3ee5264118f44aec157c)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/1mm-module/PNGAL/blob/7a00caec16e8e9d6734f3ee5264118f44aec157c/README.md) / [GitHub API](https://api.github.com/repos/1mm-module/PNGAL) / [固定ツリー](https://github.com/1mm-module/PNGAL/tree/7a00caec16e8e9d6734f3ee5264118f44aec157c)

### 制作に使う際の検討

透過キャラの待機・ループをスプライトや映像素材にする用途。配信の顔追跡用途とは入力が異なる。

**次に確かめること（実施前）**: PSDレイヤー名・原点・透明度、スプライトJSON、ループの継ぎ目を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [layer-editor/app.js](https://github.com/1mm-module/PNGAL/blob/7a00caec16e8e9d6734f3ee5264118f44aec157c/layer-editor/app.js)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-01T15:52:57Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: documented_upstream → see-through（公式説明に基づく関係、接続実行は未検証）

<a id="renpy"></a>

## RenPy

テキストとキャラクター素材を組み合わせたノベルゲームを制作する。

- **リポジトリ**: https://github.com/renpy/renpy
- **分類**: engine / 非AI制作 / 定番の制作基盤
- **入力**: シナリオ、立ち絵、背景、音声
- **出力**: ビジュアルノベル・アドベンチャーゲーム
- **環境**: Ren’Py SDKと対応OS。
- **依存**: 台本、画像、音声。AIモデル不要
- **制約・未確認**: LLMシナリオ生成器ではない。生成した素材をゲームへ組み込むためのエンジン。
- **編集者評価**: 漫画・キャラ音声・背景など複数の生成素材を作品にまとめやすい。
- **メトリクス**: ★6,876、fork 941、作成 2012-06-28、最終push 2026-09-30T14:11:25Z、archived=False
- **確認**: 2026-09-09 / コミット `f6a68a3a77014eca58c799d6663ccae733e5e10f`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/renpy/renpy/tree/f6a68a3a77014eca58c799d6663ccae733e5e10f)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/renpy/renpy/blob/f6a68a3a77014eca58c799d6663ccae733e5e10f/README.rst) / [GitHub API](https://api.github.com/repos/renpy/renpy) / [固定ツリー](https://github.com/renpy/renpy/tree/f6a68a3a77014eca58c799d6663ccae733e5e10f)

### 制作に使う際の検討

台詞・選択肢・立ち絵・音声を組み合わせるノベル制作の出力先。生成素材をrpyとアセットへ確定する。

**次に確かめること（実施前）**: 分岐、既読、セーブ、台詞と音声の対応、日本語フォント、配布ビルドを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [main.py](https://github.com/renpy/renpy/blob/f6a68a3a77014eca58c799d6663ccae733e5e10f/main.py) / [run.sh](https://github.com/renpy/renpy/blob/f6a68a3a77014eca58c799d6663ccae733e5e10f/run.sh)

**最新GitHub Release**: [8.5.3.26051504](https://github.com/renpy/renpy/releases/tag/8.5.3.26051504) / 2026-05-16T02:09:49Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-08T03:48:10Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="sprite-maker"></a>

## sprite-maker

AIエージェントと連携して素材を作り、関節・ボーンとRust描画で再現可能なアニメーションを生成する。

- **リポジトリ**: https://github.com/JohnKinyanjui/sprite-maker
- **分類**: desktop_tool / AI連携 / 初期評価候補
- **入力**: スプライト画像、制作指示、関節設定
- **出力**: アニメーションフレーム、PNGシート、メタデータ
- **環境**: エージェントCLIとの連携環境が必要。詳細は公式README参照。
- **依存**: 外部エージェントCLI、生成経路に応じた画像モデル
- **制約・未確認**: 初期段階。全OSでの導入成功や生成品質は未検証。
- **編集者評価**: 2026年8月作成。エージェント操作とゲーム用素材出力を組み合わせる新規候補。
- **メトリクス**: ★414、fork 53、作成 2026-08-09、最終push 2026-09-24T22:57:34Z、archived=False
- **確認**: 2026-09-09 / コミット `336c7114f0fce7336ec17f6e9beb93980ed03b1d`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/JohnKinyanjui/sprite-maker/tree/336c7114f0fce7336ec17f6e9beb93980ed03b1d)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/JohnKinyanjui/sprite-maker/blob/336c7114f0fce7336ec17f6e9beb93980ed03b1d/README.md) / [GitHub API](https://api.github.com/repos/JohnKinyanjui/sprite-maker) / [固定ツリー](https://github.com/JohnKinyanjui/sprite-maker/tree/336c7114f0fce7336ec17f6e9beb93980ed03b1d)

### 制作に使う際の検討

関節やフレームを扱う初期のスプライト制作候補。完成画像の見た目に加えてエクスポート形式を確認したい。

**次に確かめること（実施前）**: 自作キャラでリグ、フレーム生成、PNGシート、原点メタデータの受け渡しを試す。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/routes/+page.svelte](https://github.com/JohnKinyanjui/sprite-maker/blob/336c7114f0fce7336ec17f6e9beb93980ed03b1d/src/routes/+page.svelte)

**最新GitHub Release**: [v0.3.3](https://github.com/JohnKinyanjui/sprite-maker/releases/tag/v0.3.3) / 2026-09-24T23:13:32Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-19T10:27:09Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="terrain-diffusion"></a>

## Terrain Diffusion

広域地形を拡散モデルで生成し、地図から地形への変換も扱う。

- **リポジトリ**: https://github.com/xandergos/terrain-diffusion
- **分類**: model_toolkit / AIモデル・学習 / モデル・研究候補
- **入力**: 地形条件、地図レイヤー、生成範囲
- **出力**: 標高・地形データ、TIFF等
- **環境**: Python/PyTorch、CLI・API・探索用UI。
- **依存**: 地形モデル、必要に応じAzgaar地図
- **制約・未確認**: 標高データの生成であり、完成したゲームレベル・衝突設定ではない。
- **編集者評価**: RPG世界地図や3D背景の地形案を作る補助工程。
- **メトリクス**: ★1,410、fork 91、作成 2024-10-08、最終push 2026-08-12T03:58:54Z、archived=False
- **確認**: 2026-09-09 / コミット `e8dcb4b1a834ab2f6b1a6f5256ed7c9f2f3e8230`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/xandergos/terrain-diffusion/tree/e8dcb4b1a834ab2f6b1a6f5256ed7c9f2f3e8230)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/xandergos/terrain-diffusion/blob/e8dcb4b1a834ab2f6b1a6f5256ed7c9f2f3e8230/README.md) / [GitHub API](https://api.github.com/repos/xandergos/terrain-diffusion) / [固定ツリー](https://github.com/xandergos/terrain-diffusion/tree/e8dcb4b1a834ab2f6b1a6f5256ed7c9f2f3e8230)

### 制作に使う際の検討

RPG世界地図や3D背景の地形案を作る補助工程。

**次に確かめること（実施前）**: TIFFの高さスケール、タイル境界、川、ゲーム内で歩ける傾斜を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [terrain_diffusion/__main__.py](https://github.com/xandergos/terrain-diffusion/blob/e8dcb4b1a834ab2f6b1a6f5256ed7c9f2f3e8230/terrain_diffusion/__main__.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-12T03:58:48Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [xandergos/terrain-diffusion-30m](https://huggingface.co/xandergos/terrain-diffusion-30m) — file_listing_checked、確認日 2026-09-09、revision `9ef8030cb805b433b98ec25c5dddefbac07a9e26`。代表ファイル: `base_model/diffusion_pytorch_model.safetensors`, `coarse_model/diffusion_pytorch_model.safetensors`, `decoder_model/diffusion_pytorch_model.safetensors`。gated=False。

<a id="tiled"></a>

## Tiled

タイルとオブジェクトを配置して2Dゲームのマップを作る。

- **リポジトリ**: https://github.com/mapeditor/tiled
- **分類**: desktop_tool / 非AI制作 / 制作基盤として比較
- **入力**: タイルセット、レイヤー、オブジェクト属性
- **出力**: TMX等のマップデータ
- **環境**: デスクトップエディタ。ソースビルドはQt等。
- **依存**: ゲーム側のマップローダー、素材
- **制約・未確認**: ゲームの実行エンジンは別。独自属性の読み込みをゲーム側で実装する。
- **編集者評価**: AI生成タイルを遊べる地形へ整理する工程の基盤。
- **メトリクス**: ★12,932、fork 1,973、作成 2011-02-27、最終push 2026-09-25T09:23:19Z、archived=False
- **確認**: 2026-09-09 / コミット `395619407b39a34fccf45dc9e6e7dd0c34b6feb5`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/mapeditor/tiled/tree/395619407b39a34fccf45dc9e6e7dd0c34b6feb5)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/mapeditor/tiled/blob/395619407b39a34fccf45dc9e6e7dd0c34b6feb5/README.md) / [GitHub API](https://api.github.com/repos/mapeditor/tiled) / [固定ツリー](https://github.com/mapeditor/tiled/tree/395619407b39a34fccf45dc9e6e7dd0c34b6feb5)

### 制作に使う際の検討

AI生成タイルを遊べる地形へ整理する工程の基盤。

**次に確かめること（実施前）**: 衝突、レイヤー順、タイルアニメ、独自属性がエンジンに渡るか確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/tiledapp/main.cpp](https://github.com/mapeditor/tiled/blob/395619407b39a34fccf45dc9e6e7dd0c34b6feb5/src/tiledapp/main.cpp)

**最新GitHub Release**: [v1.12.2](https://github.com/mapeditor/tiled/releases/tag/v1.12.2) / 2026-05-27T15:17:56Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-07T15:00:14Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。
