# アニメ制作・中割り・彩色・リップシンク

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ECCV2022-RIFE](https://github.com/hzwer/ECCV2022-RIFE) · [詳細](#eccv2022-rife) | フレーム間の中間画像を推定する動画補間モデル。 | AIモデル・学習 / 比較・既存工程の参考 | 5,574 / 2025-09-10 |
| [LatentSync](https://github.com/bytedance/LatentSync) · [詳細](#latentsync) | 音声条件で口の動きを同期させる動画処理モデル。 | AIモデル・学習 / 比較・既存工程の参考 | 6,059 / 2025-06-20 |
| [opentoonz](https://github.com/opentoonz/opentoonz) · [詳細](#opentoonz) | 作画、彩色、撮影を扱う2Dアニメ制作アプリ。 | 非AI制作 / 定番の制作基盤 | 7,691 / 2026-09-09 |
| [ToonComposer](https://github.com/TencentARC/ToonComposer) · [詳細](#tooncomposer) | キーフレーム後の中割りと彩色を生成AIでまとめて処理する。 | AIモデル・学習 / 研究・技術評価候補 | 585 / 2025-08-20 |

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
- **メトリクス**: ★5,574、fork 566、作成 2020-11-12、最終push 2025-09-10T06:32:03Z、archived=False
- **確認**: 2026-09-09 / コミット `5d8adbdd40e12c2c8f91930eff838aebe561c086`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/hzwer/ECCV2022-RIFE/blob/5d8adbdd40e12c2c8f91930eff838aebe561c086/LICENSE)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/hzwer/ECCV2022-RIFE/blob/5d8adbdd40e12c2c8f91930eff838aebe561c086/README.md) / [GitHub API](https://api.github.com/repos/hzwer/ECCV2022-RIFE) / [固定ツリー](https://github.com/hzwer/ECCV2022-RIFE/tree/5d8adbdd40e12c2c8f91930eff838aebe561c086)

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
- **メトリクス**: ★6,059、fork 976、作成 2024-12-11、最終push 2025-06-20T07:36:58Z、archived=False
- **確認**: 2026-09-09 / コミット `a229c3948406bc2cf6eaf4873e662e70c6a04746`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/bytedance/LatentSync/blob/a229c3948406bc2cf6eaf4873e662e70c6a04746/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/bytedance/LatentSync/blob/a229c3948406bc2cf6eaf4873e662e70c6a04746/README.md) / [GitHub API](https://api.github.com/repos/bytedance/LatentSync) / [固定ツリー](https://github.com/bytedance/LatentSync/tree/a229c3948406bc2cf6eaf4873e662e70c6a04746)

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
- **メトリクス**: ★7,691、fork 872、作成 2016-03-18、最終push 2026-09-09T07:31:50Z、archived=False
- **確認**: 2026-09-09 / コミット `1ef22259b9cf64c9d8710daebc131b401932e81b`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/opentoonz/opentoonz/blob/1ef22259b9cf64c9d8710daebc131b401932e81b/LICENSE.txt)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/opentoonz/opentoonz/blob/1ef22259b9cf64c9d8710daebc131b401932e81b/README.md) / [GitHub API](https://api.github.com/repos/opentoonz/opentoonz) / [固定ツリー](https://github.com/opentoonz/opentoonz/tree/1ef22259b9cf64c9d8710daebc131b401932e81b)

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
- **メトリクス**: ★585、fork 59、作成 2025-08-12、最終push 2025-08-20T06:21:56Z、archived=False
- **確認**: 2026-09-09 / コミット `53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/TencentARC/ToonComposer/blob/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c/LICENSE)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/TencentARC/ToonComposer/blob/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c/README.md) / [GitHub API](https://api.github.com/repos/TencentARC/ToonComposer) / [固定ツリー](https://github.com/TencentARC/ToonComposer/tree/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [TencentARC/ToonComposer](https://huggingface.co/TencentARC/ToonComposer) — file_listing_checked、確認日 2026-09-09、revision `a166c2c0f0755af6b1876586739e818e92e5c44f`。代表ファイル: `480p/tooncomposer.ckpt`, `608p/tooncomposer.ckpt`。gated=False。
