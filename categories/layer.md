# レイヤー分解

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ComfyUI-See-through](https://github.com/jtydhr88/ComfyUI-See-through) · [詳細](#comfyui-see-through) | See-throughによる分解をComfyUIのノード工程へ接続する。 | AI連携 / ComfyUI利用者向け | 766 / 2026-08-20 |
| [Qwen-Image-Layered](https://github.com/QwenLM/Qwen-Image-Layered) · [詳細](#qwen-image-layered) | 画像を複数の編集可能なレイヤーに分解し、個別の色・位置・サイズ変更につなげる。 | AIモデル・学習 / 基盤技術候補 | 2,093 / 2025-12-31 |
| [see-through](https://github.com/shitagaki-lab/see-through) · [詳細](#see-through) | 一枚絵を意味別パーツへ分解し、遮蔽部分を補完してPSDに出力する。 | AIモデル・学習 / 導入候補 | 3,868 / 2026-08-05 |

<a id="comfyui-see-through"></a>

## ComfyUI-See-through

See-throughによる分解をComfyUIのノード工程へ接続する。

- **リポジトリ**: https://github.com/jtydhr88/ComfyUI-See-through
- **分類**: integration / AI連携 / ComfyUI利用者向け
- **入力**: アニメイラスト
- **出力**: 分解レイヤー、PSD
- **環境**: ComfyUIとSee-through用の依存環境・モデルが必要。
- **依存**: ComfyUI、See-through
- **制約・未確認**: 独立した分解モデルではない。GitHub APIはルートのライセンスを判定できていない。
- **編集者評価**: See-through公式が紹介する周辺実装で、既存ComfyUI工程へ組み込みやすい。
- **メトリクス**: ★766、fork 68、作成 2026-03-31、最終push 2026-08-20T03:16:42Z、archived=False
- **確認**: 2026-09-09 / コミット `98d754bf04f668647919ab750eccb0e0640faa81`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/jtydhr88/ComfyUI-See-through/blob/98d754bf04f668647919ab750eccb0e0640faa81/README.md)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/jtydhr88/ComfyUI-See-through/blob/98d754bf04f668647919ab750eccb0e0640faa81/README.md) / [GitHub API](https://api.github.com/repos/jtydhr88/ComfyUI-See-through) / [固定ツリー](https://github.com/jtydhr88/ComfyUI-See-through/tree/98d754bf04f668647919ab750eccb0e0640faa81)

関連: integration_of → see-through（公式説明、接続実行は未検証）

<a id="qwen-image-layered"></a>

## Qwen-Image-Layered

画像を複数の編集可能なレイヤーに分解し、個別の色・位置・サイズ変更につなげる。

- **リポジトリ**: https://github.com/QwenLM/Qwen-Image-Layered
- **分類**: model / AIモデル・学習 / 基盤技術候補
- **入力**: 汎用画像
- **出力**: 複数RGBAレイヤー、PSD、ZIP、PPTX
- **環境**: モデル推論環境または公式デモ。
- **依存**: Qwen-Image-Layered、編集にはQwen-Image-Edit
- **制約・未確認**: アニメ専用の可動パーツ分解ではない。最終pushは2025年12月。
- **編集者評価**: イラスト・背景・小物を編集可能な素材に変える基盤として有用。
- **メトリクス**: ★2,093、fork 170、作成 2025-12-18、最終push 2025-12-31T11:40:35Z、archived=False
- **確認**: 2026-09-09 / コミット `54c4fe47e76d745775e03fc66ee38457280ed9ea`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/QwenLM/Qwen-Image-Layered/blob/54c4fe47e76d745775e03fc66ee38457280ed9ea/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/QwenLM/Qwen-Image-Layered/blob/54c4fe47e76d745775e03fc66ee38457280ed9ea/README.md) / [GitHub API](https://api.github.com/repos/QwenLM/Qwen-Image-Layered) / [固定ツリー](https://github.com/QwenLM/Qwen-Image-Layered/tree/54c4fe47e76d745775e03fc66ee38457280ed9ea)

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Qwen/Qwen-Image-Layered](https://huggingface.co/Qwen/Qwen-Image-Layered) — file_listing_checked、確認日 2026-09-09、revision `8f0ca708dfff6ba1dd5f2d85d78f8c108a040bcf`。代表ファイル: `text_encoder/model-00001-of-00004.safetensors`, `text_encoder/model-00002-of-00004.safetensors`, `text_encoder/model-00003-of-00004.safetensors`, `text_encoder/model-00004-of-00004.safetensors`。gated=False。

<a id="see-through"></a>

## see-through

一枚絵を意味別パーツへ分解し、遮蔽部分を補完してPSDに出力する。

- **リポジトリ**: https://github.com/shitagaki-lab/see-through
- **分類**: model / AIモデル・学習 / 導入候補
- **入力**: アニメキャラクターの一枚絵
- **出力**: 最大23レイヤーのPSD、深度・マスク
- **環境**: オンラインデモあり。READMEの目安は1280解像度でVRAM 12〜16GB、量子化で約8GB。
- **依存**: LayerDiff、Marigold、各種セグメンテーションモデル
- **制約・未確認**: 分解が対象であり、リギングや専門家による可動構造設計は別工程。
- **編集者評価**: PuppetLoomを含む複数の制作ツールが採用する上流基盤。
- **メトリクス**: ★3,868、fork 348、作成 2026-03-31、最終push 2026-08-05T13:31:48Z、archived=False
- **確認**: 2026-09-09 / コミット `7f139bb25c46a0c8ac720d95ddab185fcda5451c`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/shitagaki-lab/see-through/blob/7f139bb25c46a0c8ac720d95ddab185fcda5451c/LICENSE)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/shitagaki-lab/see-through/blob/7f139bb25c46a0c8ac720d95ddab185fcda5451c/README.md) / [GitHub API](https://api.github.com/repos/shitagaki-lab/see-through) / [固定ツリー](https://github.com/shitagaki-lab/see-through/tree/7f139bb25c46a0c8ac720d95ddab185fcda5451c)
