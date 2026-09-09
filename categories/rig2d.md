# 2Dキャラクター・自動リギング

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [Anime2.5DRig](https://github.com/852wa/Anime2.5DRig) · [詳細](#anime2.5drig) | PSDからリグを自動構成し、目パチ・口パク・髪物理・顔追跡で動かす。 | AIは任意 / 導入候補 | 204 / 2026-09-07 |
| [PuppetLoom](https://github.com/CheshireMew/PuppetLoom) · [詳細](#puppetloom) | PSDから初期リグを作成し、外部エージェントとCLIで検証・調整しながら動く2Dキャラクターを制作する。 | AI連携 / 要再確認 | 215 / 2026-09-09 |
| [stretchystudio](https://github.com/MangoLion/stretchystudio) · [詳細](#stretchystudio) | PSDを読み込み、自動リギングとタイムライン上のメッシュ変形でアニメーションを編集する。 | AI連携 / 導入候補 | 472 / 2026-04-28 |

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
- **メトリクス**: ★204、fork 36、作成 2026-07-04、最終push 2026-09-07T06:23:57Z、archived=False
- **確認**: 2026-09-09 / コミット `7450341934a8ff77bf05b90d9f708786e3eb3996`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/852wa/Anime2.5DRig/blob/7450341934a8ff77bf05b90d9f708786e3eb3996/LICENSE)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/852wa/Anime2.5DRig/blob/7450341934a8ff77bf05b90d9f708786e3eb3996/README.md) / [GitHub API](https://api.github.com/repos/852wa/Anime2.5DRig) / [固定ツリー](https://github.com/852wa/Anime2.5DRig/tree/7450341934a8ff77bf05b90d9f708786e3eb3996)

関連: documented_input_compatibility → see-through（公式説明、接続実行は未検証）

<a id="puppetloom"></a>

## PuppetLoom

PSDから初期リグを作成し、外部エージェントとCLIで検証・調整しながら動く2Dキャラクターを制作する。

- **リポジトリ**: https://github.com/CheshireMew/PuppetLoom
- **分類**: desktop_tool / AI連携 / 要再確認
- **入力**: レイヤー付きPSD
- **出力**: リグ付きプロジェクト、Web/OBS用出力、WebM
- **環境**: Windows x64。ソース実行はNode.js 24以上。単画像の分解には外部See-throughを利用。
- **依存**: See-through（単画像分解時）
- **制約・未確認**: 専門的Live2D制作と同等ではない。moc3はCubism Editorでの出力が必要。READMEのApache-2.0表記とGitHub APIのAGPL-3.0判定が不一致のため利用条件は要再確認。
- **編集者評価**: エージェントによる制作と再現可能な修正履歴を組み合わせる設計が有望。
- **メトリクス**: ★215、fork 26、作成 2026-08-14、最終push 2026-09-09T15:56:36Z、archived=False
- **確認**: 2026-09-09 / コミット `f26c83dd31a48c644eb962971b9e21b9fa06f3f4`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/LICENSE)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/README.md) / [GitHub API](https://api.github.com/repos/CheshireMew/PuppetLoom) / [固定ツリー](https://github.com/CheshireMew/PuppetLoom/tree/f26c83dd31a48c644eb962971b9e21b9fa06f3f4)

関連: documented_upstream → see-through（公式説明、接続実行は未検証）

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
- **メトリクス**: ★472、fork 66、作成 2026-04-12、最終push 2026-04-28T03:53:09Z、archived=False
- **確認**: 2026-09-09 / コミット `24a83a27ba43e43e9d2e3de5e33994594e6199c2`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/MangoLion/stretchystudio/blob/24a83a27ba43e43e9d2e3de5e33994594e6199c2/LICENSE)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/MangoLion/stretchystudio/blob/24a83a27ba43e43e9d2e3de5e33994594e6199c2/README.md) / [GitHub API](https://api.github.com/repos/MangoLion/stretchystudio) / [固定ツリー](https://github.com/MangoLion/stretchystudio/tree/24a83a27ba43e43e9d2e3de5e33994594e6199c2)

関連: documented_input_compatibility → see-through（公式説明、接続実行は未検証）
