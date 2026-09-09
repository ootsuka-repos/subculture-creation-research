# 字幕・翻訳・ローカライズ

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [manga-image-translator](https://github.com/zyddnys/manga-image-translator) · [詳細](#manga-image-translator) | 画像内の文字を検出・認識・翻訳し、元の文字を修復して訳文を組版する。 | AIモデル・学習 / 比較・既存工程の参考 | 10,401 / 2026-07-20 |
| [VoiceTransl](https://github.com/shinnpuru/VoiceTransl) · [詳細](#voicetransl) | 音声認識、字幕翻訳、字幕と動画の処理を組み合わせる。 | AI連携 / 連携の評価候補 | 1,271 / 2026-08-28 |

<a id="manga-image-translator"></a>

## manga-image-translator

画像内の文字を検出・認識・翻訳し、元の文字を修復して訳文を組版する。

- **リポジトリ**: https://github.com/zyddnys/manga-image-translator
- **分類**: pipeline / AIモデル・学習 / 比較・既存工程の参考
- **入力**: 漫画・イラスト画像
- **出力**: 文字除去・翻訳・組版後の画像
- **環境**: Python、OCR・修復モデル、翻訳バックエンド。
- **依存**: OCR、インペイント、翻訳モデルまたはAPI
- **制約・未確認**: 公式説明に公開Webデモの停止記載あり。縦書き・擬音・レイアウト保持の品質は素材で検証が必要。
- **編集者評価**: 漫画のローカライズと文字処理工程の技術候補。
- **メトリクス**: ★10,401、fork 1,060、作成 2021-02-18、最終push 2026-07-20T07:17:48Z、archived=False
- **確認**: 2026-09-09 / コミット `95227a2bb0fd306cd4f0c104d57284026f991b3a`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/zyddnys/manga-image-translator/blob/95227a2bb0fd306cd4f0c104d57284026f991b3a/LICENSE)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/zyddnys/manga-image-translator/blob/95227a2bb0fd306cd4f0c104d57284026f991b3a/README.md) / [GitHub API](https://api.github.com/repos/zyddnys/manga-image-translator) / [固定ツリー](https://github.com/zyddnys/manga-image-translator/tree/95227a2bb0fd306cd4f0c104d57284026f991b3a)

<a id="voicetransl"></a>

## VoiceTransl

音声認識、字幕翻訳、字幕と動画の処理を組み合わせる。

- **リポジトリ**: https://github.com/shinnpuru/VoiceTransl
- **分類**: pipeline / AI連携 / 連携の評価候補
- **入力**: 音声、動画、字幕
- **出力**: 文字起こし、翻訳字幕、動画
- **環境**: 音声認識モデルと翻訳用のローカルモデルまたはAPI。
- **依存**: Whisper系、翻訳LLM、FFmpeg等
- **制約・未確認**: 同名forkと公式配布元を区別。声の生成機能ではない。
- **編集者評価**: ASMR・キャラ音声・映像の字幕付けとローカライズ候補。
- **メトリクス**: ★1,271、fork 52、作成 2024-03-15、最終push 2026-08-28T14:44:44Z、archived=False
- **確認**: 2026-09-09 / コミット `b5f7e5038763aeb3420ac872c0bd191112f92227`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/shinnpuru/VoiceTransl/blob/b5f7e5038763aeb3420ac872c0bd191112f92227/LICENSE)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/shinnpuru/VoiceTransl/blob/b5f7e5038763aeb3420ac872c0bd191112f92227/README.md) / [GitHub API](https://api.github.com/repos/shinnpuru/VoiceTransl) / [固定ツリー](https://github.com/shinnpuru/VoiceTransl/tree/b5f7e5038763aeb3420ac872c0bd191112f92227)
