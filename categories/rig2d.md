# 2Dキャラクター・自動リギング

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-05。**175件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Anime2.5DRig](https://github.com/852wa/Anime2.5DRig) · [詳細](#anime2.5drig) | PSDからリグを自動構成し、目パチ・口パク・髪物理・顔追跡で動かす。 | AIは任意 / 導入候補 | 235 / 2026-09-23 |
| [PuppetLoom](https://github.com/CheshireMew/PuppetLoom) · [詳細](#puppetloom) | レイヤーPSDを自動バインドし、改訂履歴・検証を残して動く2Dキャラを制作する。 | AI連携 / 要再確認 | 244 / 2026-10-05 |
| [stretchystudio](https://github.com/MangoLion/stretchystudio) · [詳細](#stretchystudio) | PSDを読み込み、自動リギングとタイムライン上のメッシュ変形でアニメーションを編集する。 | AI連携 / 導入候補 | 498 / 2026-04-28 |
| [psd2live](https://github.com/tsunehimatoi/psd2live) · [詳細](#psd2live) | レイヤー分けしたPSDからLive2Dモデルを自動生成し、同じ作業画面で修形・リギング・物理・アニメーション・書き出しまで行うデスクトップツール。 | AIは任意 / 活発・候補 | 562 / 2026-10-05 |
| [live2d-py](https://github.com/EasyLive2D/live2d-py) · [詳細](#live2d-py) | Live2DモデルをPythonから直接読み込み・描画するC++拡張ライブラリ。Web Engineを挟まず、OpenGLコンテキストがあれば任意のOpenGLウィンドウに描画できる。 | 非AI制作 / 実運用段階のライブラリ | 576 / 2026-09-30 |
| [ayagami](https://github.com/AyagamiDev/ayagami) · [詳細](#ayagami) | Live2D（MOC3）互換の2Dパペット読み込み・描画SDK。Rust実装で、wgpuベースのリファレンスレンダラとGodotコンポーネントを備える。 | 非AI制作 / 初期評価候補 | 343 / 2026-09-14 |
| [Amahane-Hikari-Live2D](https://github.com/luomo66ccff/Amahane-Hikari-Live2D) · [詳細](#amahane-hikari-live2d) | AIエージェントと協働してLive2Dキャラクターを制作し、TypeScript/WebGLのWebランタイムで再生する制作プロジェクト。制作フローをSkillとして公開する。 | AI連携 / 活発な候補 | 109 / 2026-09-21 |
| [live2d-agent-kit](https://github.com/Ariakage/live2d-agent-kit) · [詳細](#live2d-agent-kit) | coding agentが参考図や分层PSDから.moc3を作るためのLive2D制作キット。psd2liveアダプタ、アニメ超分スクリプト、検証手順を含む。 | AI連携 / 小規模・初期評価候補 | 20 / 2026-09-12 |
| [iki](https://github.com/zeikar/iki) · [詳細](#iki) | MITの2Dパペットエンジン。AIエージェントが画像モデルでパーツを描き、役割名付きレイヤーから.iki形式へ自動リギングする。 | AI連携 / 初期評価候補 | 10 / 2026-10-05 |
| [spine-parts](https://github.com/firejune/spine-parts) · [詳細](#spine-parts) | 1枚のアニメ絵からSpine 2Dキャラのパーツを組み立てるCLI。See-throughのレイヤ分解結果を統合し、メッシュ・ボーン・ループidleをspine-rigc仕様で生成、書き出し前に数値で検査する。 | AI連携 / 小規模・初期評価候補 | 2 / 2026-10-05 |

<a id="anime2.5drig"></a>

## Anime2.5DRig

PSDからリグを自動構成し、目パチ・口パク・髪物理・顔追跡で動かす。

- **リポジトリ**: https://github.com/852wa/Anime2.5DRig
- **分類**: browser_tool / AIは任意 / 導入候補
- **入力**: パーツ分けPSD
- **出力**: リアルタイム2.5Dアバター、設定JSON、透過PNG、OBS表示
- **環境**: 通常利用はブラウザ。OBS中継はPython 3。日本語README・デモあり。
- **依存**: MediaPipe FaceMesh（顔追跡時）、分解済みPSD
- **制約・未確認**: 入力PSDのレイヤー構造に依存。動作品質は未検証。
- **編集者評価**: 2026年7月作成、9月更新。See-through出力と接続しやすいブラウザ実装。
- **メトリクス**: ★235、fork 40、作成 2026-07-04、最終push 2026-09-23T07:01:12Z、archived=False
- **確認**: 2026-09-09 / コミット `7450341934a8ff77bf05b90d9f708786e3eb3996`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/852wa/Anime2.5DRig/tree/7450341934a8ff77bf05b90d9f708786e3eb3996)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/852wa/Anime2.5DRig/blob/7450341934a8ff77bf05b90d9f708786e3eb3996/README.md) / [GitHub API](https://api.github.com/repos/852wa/Anime2.5DRig) / [固定ツリー](https://github.com/852wa/Anime2.5DRig/tree/7450341934a8ff77bf05b90d9f708786e3eb3996)

### 制作に使う際の検討

ブラウザでPSDから動く立ち絵を作る候補。衣装や髪のレイヤー構造を入力仕様として管理する。

**次に確かめること（実施前）**: 目・口・前後髪の対応、可動角度、JSON再読込、OBS透過を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [lib/app.js](https://github.com/852wa/Anime2.5DRig/blob/7450341934a8ff77bf05b90d9f708786e3eb3996/lib/app.js) / [obs_server.py](https://github.com/852wa/Anime2.5DRig/blob/7450341934a8ff77bf05b90d9f708786e3eb3996/obs_server.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-07T06:23:50Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: documented_input_compatibility → see-through（公式説明に基づく関係、接続実行は未検証）

<a id="puppetloom"></a>

## PuppetLoom

レイヤーPSDを自動バインドし、改訂履歴・検証を残して動く2Dキャラを制作する。

- **リポジトリ**: https://github.com/CheshireMew/PuppetLoom
- **分類**: desktop_tool / AI連携 / 要再確認
- **入力**: レイヤー付きPSD
- **出力**: リグ付きプロジェクト、Web/OBS表示、WebM、CMO3/MOC3等の直接出力経路
- **環境**: 作者の対象はWindows x64。ソース実行はNode.js24以上・npm11・WebGL2。
- **依存**: See-through（単画像分解時）
- **制約・未確認**: 専門的Live2D制作と同等ではない。現行中国語READMEとCLIにCubism直接出力経路があるが、実ファイル生成・互換性は未検証。英語・日本語READMEのApache表記がLICENSE/NOTICEのAGPLと不一致。
- **編集者評価**: エージェントによる制作と再現可能な修正履歴を組み合わせる設計が有望。
- **メトリクス**: ★244、fork 31、作成 2026-08-14、最終push 2026-10-05T10:27:40Z、archived=False
- **確認**: 2026-09-09 / コミット `f26c83dd31a48c644eb962971b9e21b9fa06f3f4`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/CheshireMew/PuppetLoom/tree/f26c83dd31a48c644eb962971b9e21b9fa06f3f4)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/README.md) / [GitHub API](https://api.github.com/repos/CheshireMew/PuppetLoom) / [固定ツリー](https://github.com/CheshireMew/PuppetLoom/tree/f26c83dd31a48c644eb962971b9e21b9fa06f3f4) / [追加一次資料 1](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/LICENSE-NOTICE.md) / [追加一次資料 2](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/README.en.md) / [追加一次資料 3](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/README.ja.md) / [追加一次資料 4](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/apps/cli/src/commands/cubism.ts) / [追加一次資料 5](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/LICENSE)

### 制作に使う際の検討

PSDから制作・校正の改訂履歴を残す自動化基盤。現行CLIのCubism直接出力も検証候補に含める。

**次に確かめること（実施前）**: 自作PSDで中立・転頭・閉眼を点検し、直接出力したcmo3/moc3を対象Editor/SDKで開いて視覚比較する。

**利用条件の確認メモ**: LICENSEはAGPLv3本文、LICENSE-NOTICEはAGPL-3.0-or-later。中国語READMEは一致するがREADME.en.md/README.ja.mdにはApache-2.0が残る。配布元の版宣言を記録し、商用利用・依存物の条件判断は別。

**入口候補（固定ツリーで存在確認）**: [apps/cli/src/commands/cubism.ts](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/apps/cli/src/commands/cubism.ts) / [packages/core/src/cubism-export.ts](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/packages/core/src/cubism-export.ts)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-09T15:56:36Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

本文を確認した箇所:

- [LICENSE-NOTICE.md](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/LICENSE-NOTICE.md): AGPL-3.0-or-laterの版宣言を確認。
- [README.en.md](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/README.en.md): Apache-2.0表記が残り中国語README・LICENSE-NOTICEと不一致。
- [README.ja.md](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/README.ja.md): Apache-2.0表記が残り中国語README・LICENSE-NOTICEと不一致。
- [apps/cli/src/commands/cubism.ts](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/apps/cli/src/commands/cubism.ts): cubism exportがexportNativeCubismを呼び、EditorとRuntimeの対象版オプションを受け取る部分を確認。生成成功・形式互換は未検証。
- [LICENSE](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/LICENSE): AGPLv3本文の冒頭を確認。法的な適用判断は行っていない。

関連: documented_upstream → see-through（公式説明に基づく関係、接続実行は未検証）

<a id="stretchystudio"></a>

## stretchystudio

PSDを読み込み、自動リギングとタイムライン上のメッシュ変形でアニメーションを編集する。

- **リポジトリ**: https://github.com/MangoLion/stretchystudio
- **分類**: browser_tool / AI連携 / 導入候補
- **入力**: See-through形式の分割PSD
- **出力**: メッシュ変形アニメーション
- **環境**: ブラウザエディタあり。DWPoseまたはヒューリスティックな自動リグ。
- **依存**: See-through形式PSD、DWPose（選択時）
- **制約・未確認**: 最終pushは2026年4月。最近の活発な更新とは扱わない。
- **編集者評価**: See-throughから演出・編集につなぐ公開ブラウザツール。
- **メトリクス**: ★498、fork 71、作成 2026-04-12、最終push 2026-04-28T03:53:09Z、archived=False
- **確認**: 2026-09-09 / コミット `24a83a27ba43e43e9d2e3de5e33994594e6199c2`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/MangoLion/stretchystudio/tree/24a83a27ba43e43e9d2e3de5e33994594e6199c2)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/MangoLion/stretchystudio/blob/24a83a27ba43e43e9d2e3de5e33994594e6199c2/README.md) / [GitHub API](https://api.github.com/repos/MangoLion/stretchystudio) / [固定ツリー](https://github.com/MangoLion/stretchystudio/tree/24a83a27ba43e43e9d2e3de5e33994594e6199c2)

### 制作に使う際の検討

分解済みPSDをメッシュ変形に使う候補。See-through互換はレイヤー名だけでなく位置と遮蔽を試す。

**次に確かめること（実施前）**: 前髪・耳・首の境界を大きく動かし、めくれ・透過・保存復元を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/mesh/generate.js](https://github.com/MangoLion/stretchystudio/blob/24a83a27ba43e43e9d2e3de5e33994594e6199c2/src/mesh/generate.js) / [eslint.config.js](https://github.com/MangoLion/stretchystudio/blob/24a83a27ba43e43e9d2e3de5e33994594e6199c2/eslint.config.js)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-04-28T03:53:06Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: documented_input_compatibility → see-through（公式説明に基づく関係、接続実行は未検証）

<a id="psd2live"></a>

## psd2live

レイヤー分けしたPSDからLive2Dモデルを自動生成し、同じ作業画面で修形・リギング・物理・アニメーション・書き出しまで行うデスクトップツール。

- **リポジトリ**: https://github.com/tsunehimatoi/psd2live
- **分類**: desktop_tool / AIは任意 / 活発・候補
- **入力**: パーツ別レイヤーのPSD、差分用の透明画像
- **出力**: .cmo3、.moc3と.model3.json等のランタイム一式、.psd2live工程ファイル
- **環境**: Windows 10/11またはLinuxの配布バイナリ、ソース実行はJDK 21。
- **依存**: Live2D Cubism SDKは同梱せず、公式SDKは任意。
- **制約・未確認**: 自動生成の品質はPSDのレイヤー分けに依存し、書き出し成功が全ランタイムでの同一挙動を保証しないとREADMEが明記。
- **編集者評価**: レイヤー名からパーツを認識してメッシュ・変形器・頭身パラメータ・待機/瞬き動作・髪物理を自動生成し、Cubism Editorで続きを編集できる形式で書き出せる点が実用的。
- **メトリクス**: ★562、fork 47、作成 2026-09-03、最終push 2026-10-05T10:35:30Z、archived=False
- **確認**: 2026-09-30 / コミット `a494c6e6d713640f7c07d2114998f80f638275cf`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/tsunehimatoi/psd2live/tree/a494c6e6d713640f7c07d2114998f80f638275cf)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/tsunehimatoi/psd2live/blob/a494c6e6d713640f7c07d2114998f80f638275cf/README.md) / [GitHub API](https://api.github.com/repos/tsunehimatoi/psd2live) / [固定ツリー](https://github.com/tsunehimatoi/psd2live/tree/a494c6e6d713640f7c07d2114998f80f638275cf)

### 制作に使う際の検討

Live2Dモデルの初期リギングと物理設定の工数削減。

**次に確かめること（実施前）**: 配布版でサンプルPSDを読み込み、.cmo3/.moc3を書き出してCubism Editorで開けるか確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/tsunehimatoi/psd2live/blob/a494c6e6d713640f7c07d2114998f80f638275cf/README.md)

**最新GitHub Release**: [v2.0.4](https://github.com/tsunehimatoi/psd2live/releases/tag/v2.0.4) / 2026-10-04T17:42:53Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-30T18:27:06Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="live2d-py"></a>

## live2d-py

Live2DモデルをPythonから直接読み込み・描画するC++拡張ライブラリ。Web Engineを挟まず、OpenGLコンテキストがあれば任意のOpenGLウィンドウに描画できる。

- **リポジトリ**: https://github.com/EasyLive2D/live2d-py
- **分類**: library / 非AI制作 / 実運用段階のライブラリ
- **入力**: Cubism 2.1／3.0以降のモデルファイル、モデルパラメータ、口パク用の音声
- **出力**: OpenGLウィンドウへの描画、パラメータ・透明度操作の結果
- **環境**: Python 3.11以上。whl配布またはPyPIから導入、もしくはCMake 3.26以上でソースビルド。Live2D Cubism Core/Frameworkはライセンスの都合で同梱されず、公式から別途取得が必要。
- **依存**: Live2D Cubism Native SDK、OpenGL対応のUIライブラリ
- **制約・未確認**: Cubism Coreを同梱できないため、ソースビルド時はSDKを自分で用意する必要がある。READMEにモーション編集やモデル制作機能の記載はない。
- **編集者評価**: Pygame／PyQt5／PySide6／GLFW等へ組み込めるため、自作VTuberやコンパニオンの描画層を自前実装する土台になる。
- **メトリクス**: ★576、fork 55、作成 2024-06-04、最終push 2026-09-30T11:50:34Z、archived=False
- **確認**: 2026-10-02 / コミット `35f686412470ea25718fa9c76ee4f1809f6a8506`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/EasyLive2D/live2d-py/tree/35f686412470ea25718fa9c76ee4f1809f6a8506)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/EasyLive2D/live2d-py/blob/35f686412470ea25718fa9c76ee4f1809f6a8506/README.md) / [GitHub API](https://api.github.com/repos/EasyLive2D/live2d-py) / [固定ツリー](https://github.com/EasyLive2D/live2d-py/tree/35f686412470ea25718fa9c76ee4f1809f6a8506)

### 制作に使う際の検討

デスクトップコンパニオン／VTuberアプリの描画・口パク・クリック判定。

**次に確かめること（実施前）**: 手元のLive2Dモデルで読み込み・視線追跡・口パク・パーツ単位クリック判定を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [tests/v2/main.cpp](https://github.com/EasyLive2D/live2d-py/blob/35f686412470ea25718fa9c76ee4f1809f6a8506/tests/v2/main.cpp)

**最新GitHub Release**: [v1.0.0](https://github.com/EasyLive2D/live2d-py/releases/tag/v1.0.0) / 2026-09-30T11:50:35Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-30T11:48:39Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="ayagami"></a>

## ayagami

Live2D（MOC3）互換の2Dパペット読み込み・描画SDK。Rust実装で、wgpuベースのリファレンスレンダラとGodotコンポーネントを備える。

- **リポジトリ**: https://github.com/AyagamiDev/ayagami
- **分類**: library / 非AI制作 / 初期評価候補
- **入力**: MOC3ファイル、テクスチャ、モデルパラメータ、ZIPアーカイブ（デモ）
- **出力**: ウィンドウ／テクスチャへの描画結果、任意パラメータでのポーズ
- **環境**: Rust/Cargo。Webデモはブラウザで動作しモデルはローカル処理。ネイティブはcargo run、Webはtrunkを使用。
- **依存**: wgpu、egui（デモ）、Godot（ayagami-gd）
- **制約・未確認**: API未安定・ドキュメント未整備で、表情ファイル／ポーズファイル／モーションの対応はTODOのまま。現状PRは受け付けておらず、crates.io公開も未実施。
- **編集者評価**: ブラックボックス解析のみで書かれた独立実装で、ゲーム組込みや自作VTuberソフトの描画基盤に使える。
- **メトリクス**: ★343、fork 17、作成 2026-07-11、最終push 2026-09-14T14:19:06Z、archived=False
- **確認**: 2026-10-02 / コミット `0d1d7aa3efe57b1b363b72e672e353c52a9c15d6`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/AyagamiDev/ayagami/tree/0d1d7aa3efe57b1b363b72e672e353c52a9c15d6)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/AyagamiDev/ayagami/blob/0d1d7aa3efe57b1b363b72e672e353c52a9c15d6/README.md) / [GitHub API](https://api.github.com/repos/AyagamiDev/ayagami) / [固定ツリー](https://github.com/AyagamiDev/ayagami/tree/0d1d7aa3efe57b1b363b72e672e353c52a9c15d6)

### 制作に使う際の検討

エンジンへ組み込みたい場合のLive2D描画層。

**次に確かめること（実施前）**: Webデモでモデル読込とパラメータ操作を行い、Godotコンポーネントがビルドできるか確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [ayagami-demo/src/app.rs](https://github.com/AyagamiDev/ayagami/blob/0d1d7aa3efe57b1b363b72e672e353c52a9c15d6/ayagami-demo/src/app.rs) / [ayagami-demo/src/main.rs](https://github.com/AyagamiDev/ayagami/blob/0d1d7aa3efe57b1b363b72e672e353c52a9c15d6/ayagami-demo/src/main.rs) / [ayagami-render/src/main.rs](https://github.com/AyagamiDev/ayagami/blob/0d1d7aa3efe57b1b363b72e672e353c52a9c15d6/ayagami-render/src/main.rs)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-14T14:15:47Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="amahane-hikari-live2d"></a>

## Amahane-Hikari-Live2D

AIエージェントと協働してLive2Dキャラクターを制作し、TypeScript/WebGLのWebランタイムで再生する制作プロジェクト。制作フローをSkillとして公開する。

- **リポジトリ**: https://github.com/luomo66ccff/Amahane-Hikari-Live2D
- **分類**: workflow_tool / AI連携 / 活発な候補
- **入力**: 参考画像・Photoshopレイヤー、Live2D Cubism SDK for Web 5-r.5
- **出力**: MOC3/MODEL3などのLive2Dモデル、WebGLプレビュー、制作Skill
- **環境**: Node.js 22.12+。完全なWeb表示にはLive2D Cubism SDK for Web 5-r.5を別途取得する必要がある。
- **依存**: Live2D Cubism SDK for Web（別途取得）、npm依存
- **制約・未確認**: キャラクター資産は自作のNo-AIライセンスで、AI/ML学習への利用が禁止。SDKは同梱されない。
- **編集者評価**: Live2Dモデルの制作からWeb表示までの手順と検証（70項目のSDK不要CIなど）が公開され、AI支援制作の再現に使いやすい。
- **メトリクス**: ★109、fork 0、作成 2026-09-10、最終push 2026-09-21T15:42:38Z、archived=False
- **確認**: 2026-10-03 / コミット `246bbd195bf260e6e35f11c0c1c24fdc1b3d097d`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/luomo66ccff/Amahane-Hikari-Live2D/tree/246bbd195bf260e6e35f11c0c1c24fdc1b3d097d)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/luomo66ccff/Amahane-Hikari-Live2D/blob/246bbd195bf260e6e35f11c0c1c24fdc1b3d097d/README.md) / [GitHub API](https://api.github.com/repos/luomo66ccff/Amahane-Hikari-Live2D) / [固定ツリー](https://github.com/luomo66ccff/Amahane-Hikari-Live2D/tree/246bbd195bf260e6e35f11c0c1c24fdc1b3d097d)

### 制作に使う際の検討

Live2D制作の手順テンプレートと検証手法の参照元として使える。

**次に確かめること（実施前）**: SDKを配置してビルド・再生し、README記載の検証スクリプトが通るか確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [web/src/main.ts](https://github.com/luomo66ccff/Amahane-Hikari-Live2D/blob/246bbd195bf260e6e35f11c0c1c24fdc1b3d097d/web/src/main.ts)

**最新GitHub Release**: [v2.1.0](https://github.com/luomo66ccff/Amahane-Hikari-Live2D/releases/tag/v2.1.0) / 2026-09-20T13:12:23Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-09-21T15:42:38Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="live2d-agent-kit"></a>

## live2d-agent-kit

coding agentが参考図や分层PSDから.moc3を作るためのLive2D制作キット。psd2liveアダプタ、アニメ超分スクリプト、検証手順を含む。

- **リポジトリ**: https://github.com/Ariakage/live2d-agent-kit
- **分類**: workflow_tool / AI連携 / 小規模・初期評価候補
- **入力**: 参考画像、分层PSD/PNGレイヤー、Live2D公式Core
- **出力**: PSD/CMO3/MOC3、図集、パラメータと物理、WebGLプレビュー、運行パッケージ
- **環境**: Git、Python 3.10+、JDK 21、Node.js 22+。Upscayl CLIとLive2D Coreは別途用意する。
- **依存**: psd2live、Upscayl CLI、Live2D Core（別途取得）
- **制約・未確認**: 肩・腕・指の独立绑定は実装範囲外。示例資産はCC BY 4.0で、作者はLive2D社と無関係と明記。
- **編集者評価**: Live2D制作の工程と検査をエージェント向けに文書化し、示例モデルと202項目の検証記録を公開している。
- **メトリクス**: ★20、fork 0、作成 2026-09-11、最終push 2026-09-12T16:28:19Z、archived=False
- **確認**: 2026-10-03 / コミット `94e79e3a94753ae1bd29204d3ed685a3c7b59022`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Ariakage/live2d-agent-kit/tree/94e79e3a94753ae1bd29204d3ed685a3c7b59022)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Ariakage/live2d-agent-kit/blob/94e79e3a94753ae1bd29204d3ed685a3c7b59022/README.md) / [GitHub API](https://api.github.com/repos/Ariakage/live2d-agent-kit) / [固定ツリー](https://github.com/Ariakage/live2d-agent-kit/tree/94e79e3a94753ae1bd29204d3ed685a3c7b59022)

### 制作に使う際の検討

Live2D绑定の初期検証と手順の型として使える。

**次に確かめること（実施前）**: 最小示例を実行し、Core/WebGL検証が再現するか確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [templates/web-preview/app.js](https://github.com/Ariakage/live2d-agent-kit/blob/94e79e3a94753ae1bd29204d3ed685a3c7b59022/templates/web-preview/app.js) / [templates/web-preview/server.py](https://github.com/Ariakage/live2d-agent-kit/blob/94e79e3a94753ae1bd29204d3ed685a3c7b59022/templates/web-preview/server.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-09-12T16:28:15Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="iki"></a>

## iki

MITの2Dパペットエンジン。AIエージェントが画像モデルでパーツを描き、役割名付きレイヤーから.iki形式へ自動リギングする。

- **リポジトリ**: https://github.com/zeikar/iki
- **分類**: engine / AI連携 / 初期評価候補
- **入力**: 役割名付きPNG/PSDレイヤー、画像生成モデル（Claude Codeプラグイン経由）
- **出力**: .ikiモデル（プレーンJSON）、WebGL2での動作
- **環境**: Node.js、npmパッケージ（@ikijs/engine等）。自動リギングには画像生成環境が必要。
- **依存**: 画像生成モデル（別途）、npm
- **制約・未確認**: 作者自身が早期と明記し、スキーマは流動的。Live2D/Inochi2Dより成熟度は低い。
- **編集者評価**: オープンなJSON形式と自動リギングで、エージェントによるLive2D代替制作を試せる。作者が0.xの早期と明記している。
- **メトリクス**: ★10、fork 1、作成 2026-06-04、最終push 2026-10-05T12:00:22Z、archived=False
- **確認**: 2026-10-03 / コミット `e0ebdd542212e60847ca3af37965c73e77301ad1`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/zeikar/iki/tree/e0ebdd542212e60847ca3af37965c73e77301ad1)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/zeikar/iki/blob/e0ebdd542212e60847ca3af37965c73e77301ad1/README.md) / [GitHub API](https://api.github.com/repos/zeikar/iki) / [固定ツリー](https://github.com/zeikar/iki/tree/e0ebdd542212e60847ca3af37965c73e77301ad1)

### 制作に使う際の検討

エージェント連携での2Dリギング自動化の検証に向く。

**次に確かめること（実施前）**: 自動リギングした.ikiをブラウザで再生し、瞬き・口パク・髪物理を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [examples/editor/src/main.tsx](https://github.com/zeikar/iki/blob/e0ebdd542212e60847ca3af37965c73e77301ad1/examples/editor/src/main.tsx) / [examples/playground/src/main.ts](https://github.com/zeikar/iki/blob/e0ebdd542212e60847ca3af37965c73e77301ad1/examples/playground/src/main.ts) / [packages/editor/src/auto-rig/index.ts](https://github.com/zeikar/iki/blob/e0ebdd542212e60847ca3af37965c73e77301ad1/packages/editor/src/auto-rig/index.ts)

**最新GitHub Release**: [@ikijs/mcp@0.16.0](https://github.com/zeikar/iki/releases/tag/%40ikijs/mcp%400.16.0) / 2026-10-05T00:14:30Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-10-03T13:47:20Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="spine-parts"></a>

## spine-parts

1枚のアニメ絵からSpine 2Dキャラのパーツを組み立てるCLI。See-throughのレイヤ分解結果を統合し、メッシュ・ボーン・ループidleをspine-rigc仕様で生成、書き出し前に数値で検査する。

- **リポジトリ**: https://github.com/firejune/spine-parts
- **分類**: pipeline / AI連携 / 小規模・初期評価候補
- **入力**: キャラ立ち絵PNG、See-throughのレイヤ（layers.json+PNGまたはPSD）、キャラ設定config.json
- **出力**: Spine 4.3のskeleton.json/atlas/packedページ、パーツPNG、idleのAPNG/GIF等
- **環境**: Node/Bun環境。See-throughの実行結果とspine-rigcが必要。MIT。
- **依存**: See-through、spine-rigc、入力の立ち絵とレイヤ分解結果
- **制約・未確認**: READMEは特定チェックポイント（Pony Diffusion V6 XL）と手作業編集を伴う例を記載。入力は正面・全身で縦長の1キャラに限定。
- **編集者評価**: エージェント向けに検査結果を数値で出す設計で、レイヤ分解からリグ生成まで再現性を重視。2Dキャラの自動リギング検証に有用。
- **メトリクス**: ★2、fork 0、作成 2026-09-27、最終push 2026-10-05T09:13:19Z、archived=False
- **確認**: 2026-10-05 / コミット `774ef0414fdb9e8b045803675d61664339965604`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/firejune/spine-parts/tree/774ef0414fdb9e8b045803675d61664339965604)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/firejune/spine-parts/blob/774ef0414fdb9e8b045803675d61664339965604/README.md) / [GitHub API](https://api.github.com/repos/firejune/spine-parts) / [固定ツリー](https://github.com/firejune/spine-parts/tree/774ef0414fdb9e8b045803675d61664339965604)

### 制作に使う際の検討

Spine/Live2D系の2Dリグ工程の自動化・検証の足がかりになる。

**次に確かめること（実施前）**: 自作の立ち絵とSee-through出力で、生成リグの品質とゲート通過率を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [cli.ts](https://github.com/firejune/spine-parts/blob/774ef0414fdb9e8b045803675d61664339965604/cli.ts) / [src/comfy/index.ts](https://github.com/firejune/spine-parts/blob/774ef0414fdb9e8b045803675d61664339965604/src/comfy/index.ts) / [src/raster/index.ts](https://github.com/firejune/spine-parts/blob/774ef0414fdb9e8b045803675d61664339965604/src/raster/index.ts)

**最新GitHub Release**: [v0.9.0](https://github.com/firejune/spine-parts/releases/tag/v0.9.0) / 2026-10-05T09:13:19Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-10-05T09:13:09Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
