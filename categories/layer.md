# レイヤー分解

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-09-09。**115件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [ComfyUI-See-through](https://github.com/jtydhr88/ComfyUI-See-through) · [詳細](#comfyui-see-through) | See-throughによる分解をComfyUIのノード工程へ接続する。 | AI連携 / ComfyUI利用者向け | 766 / 2026-08-20 |
| [Qwen-Image-Layered](https://github.com/QwenLM/Qwen-Image-Layered) · [詳細](#qwen-image-layered) | 画像を複数の編集可能なレイヤーに分解し、個別の色・位置・サイズ変更につなげる。 | AIモデル・学習 / 基盤技術候補 | 2,093 / 2025-12-31 |
| [see-through](https://github.com/shitagaki-lab/see-through) · [詳細](#see-through) | 一枚絵を意味別パーツへ分解し、遮蔽部分を補完してPSDに出力する。 | AIモデル・学習 / 導入候補 | 3,868 / 2026-08-05 |
| [Stable Layers](https://github.com/Stability-AI/Stable-Layers) · [詳細](#stable-layers) | Qwen-Image-Layered上のLoRAで、画像を背景と物体の編集用RGBA層へ分解する。 | AIモデル・学習 / レイヤー分解の研究候補 | 19 / 2026-07-23 |

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
- **利用条件**: [配布元の条件](https://github.com/jtydhr88/ComfyUI-See-through/tree/98d754bf04f668647919ab750eccb0e0640faa81)。GitHub自動判定=None。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/jtydhr88/ComfyUI-See-through/blob/98d754bf04f668647919ab750eccb0e0640faa81/README.md) / [GitHub API](https://api.github.com/repos/jtydhr88/ComfyUI-See-through) / [固定ツリー](https://github.com/jtydhr88/ComfyUI-See-through/tree/98d754bf04f668647919ab750eccb0e0640faa81)

### 制作に使う際の検討

分解処理をComfyUIの前後工程へ接続するラッパー。本家モデルの能力とノード側の互換性を分けて評価する。

**次に確かめること（実施前）**: 固定版ノードで本家と同じ画像を分解し、レイヤー名・画布座標・PSDの一致を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [nodes.py](https://github.com/jtydhr88/ComfyUI-See-through/blob/98d754bf04f668647919ab750eccb0e0640faa81/nodes.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-20T03:16:22Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: integration_of → see-through（公式説明に基づく関係、接続実行は未検証）

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
- **利用条件**: [配布元の条件](https://github.com/QwenLM/Qwen-Image-Layered/tree/54c4fe47e76d745775e03fc66ee38457280ed9ea)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/QwenLM/Qwen-Image-Layered/blob/54c4fe47e76d745775e03fc66ee38457280ed9ea/README.md) / [GitHub API](https://api.github.com/repos/QwenLM/Qwen-Image-Layered) / [固定ツリー](https://github.com/QwenLM/Qwen-Image-Layered/tree/54c4fe47e76d745775e03fc66ee38457280ed9ea)

### 制作に使う際の検討

背景や物体をRGBA層に分ける汎用編集用途。キャラ関節用のパーツ分解はSee-through等と比較する。

**次に確かめること（実施前）**: 重ね直したときの原画像との差、遮蔽物の補完、PPTX/PSDの透明度を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [src/app.py](https://github.com/QwenLM/Qwen-Image-Layered/blob/54c4fe47e76d745775e03fc66ee38457280ed9ea/src/app.py) / [src/tool/combine_layers.py](https://github.com/QwenLM/Qwen-Image-Layered/blob/54c4fe47e76d745775e03fc66ee38457280ed9ea/src/tool/combine_layers.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-12-31T11:40:35Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

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
- **利用条件**: [配布元の条件](https://github.com/shitagaki-lab/see-through/tree/7f139bb25c46a0c8ac720d95ddab185fcda5451c)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/shitagaki-lab/see-through/blob/7f139bb25c46a0c8ac720d95ddab185fcda5451c/README.md) / [GitHub API](https://api.github.com/repos/shitagaki-lab/see-through) / [固定ツリー](https://github.com/shitagaki-lab/see-through/tree/7f139bb25c46a0c8ac720d95ddab185fcda5451c)

### 制作に使う際の検討

一枚のキャラ絵をリグ工程へ渡す入口。隠れた箇所の分解結果は作画として人が確認する。

**次に確かめること（実施前）**: PSDを再合成し原画と比較、目・手・髪の欠損、リグ側での位置合わせを確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [inference/scripts/inference_psd.py](https://github.com/shitagaki-lab/see-through/blob/7f139bb25c46a0c8ac720d95ddab185fcda5451c/inference/scripts/inference_psd.py) / [inference/scripts/heuristic_partseg.py](https://github.com/shitagaki-lab/see-through/blob/7f139bb25c46a0c8ac720d95ddab185fcda5451c/inference/scripts/heuristic_partseg.py) / [inference/scripts/inference_psd_quantized.py](https://github.com/shitagaki-lab/see-through/blob/7f139bb25c46a0c8ac720d95ddab185fcda5451c/inference/scripts/inference_psd_quantized.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-08-05T13:31:47Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

<a id="stable-layers"></a>

## Stable Layers

Qwen-Image-Layered上のLoRAで、画像を背景と物体の編集用RGBA層へ分解する。

- **リポジトリ**: https://github.com/Stability-AI/Stable-Layers
- **分類**: model_toolkit / AIモデル・学習 / レイヤー分解の研究候補
- **入力**: 単一RGB画像、画像ディレクトリ
- **出力**: 再合成画像、背景・物体レイヤーPNG。実アルファには--transparent指定。
- **環境**: 作者はtorch2.11、diffusers0.37等で検証。bf16基盤約40GB、80GB級GPUを余裕ある構成として案内。
- **依存**: Qwen/Qwen-Image-Layered、Stable Layers LoRA、PEFT等。
- **制約・未確認**: 推論のみの公開。READMEは./model同梱と記すが確認GitHubツリー4ファイルにmodel/はない。HFにはアダプタを確認。既定PNGは白背景で、アルファ出力にはフラグが必要。
- **編集者評価**: 画像全体の物体分離と再合成に向く候補。キャラ可動部の分解はSee-throughと目的が異なる。
- **メトリクス**: ★19、fork 3、作成 2026-07-19、最終push 2026-07-23T22:10:50Z、archived=False
- **確認**: 2026-09-09 / コミット `b826314b34b12d7c7cce9f0de7f49a330bd8e011`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Stability-AI/Stable-Layers/blob/b826314b34b12d7c7cce9f0de7f49a330bd8e011/LICENSE.md)。GitHub自動判定=NOASSERTION。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Stability-AI/Stable-Layers/blob/b826314b34b12d7c7cce9f0de7f49a330bd8e011/README.md) / [GitHub API](https://api.github.com/repos/Stability-AI/Stable-Layers) / [固定ツリー](https://github.com/Stability-AI/Stable-Layers/tree/b826314b34b12d7c7cce9f0de7f49a330bd8e011)

### 制作に使う際の検討

画像全体の物体分離と再合成に向く候補。キャラ可動部の分解はSee-throughと目的が異なる。

**次に確かめること（実施前）**: HFからアダプタを配置し、作者推奨のHeun50ステップ・CFG1・640px・4層で分解。再合成の差と透過出力を確認する。

**利用条件の確認メモ**: Stability AI Community LicenseをREADMEとモデルカードが案内。基盤Qwenの条件は別。適用・商用可否の独立判断は未実施。

**入口候補（固定ツリーで存在確認）**: [decompose.py](https://github.com/Stability-AI/Stable-Layers/blob/b826314b34b12d7c7cce9f0de7f49a330bd8e011/decompose.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-07-23T22:10:48Z。README・固定ツリー・HFファイル一覧の確認。コード全体の監査、起動、品質比較は未実施。

関連: based_on → qwen-image-layered（公式説明に基づく関係、接続実行は未検証）

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [StabilityLabs/Stable-Layers](https://huggingface.co/StabilityLabs/Stable-Layers) — file_listing_checked、確認日 2026-09-09、revision `41b2f7692d2bc6be496f1de1f5dd349e93aa090f`。代表ファイル: `model/adapter_model.safetensors`。gated=False。
