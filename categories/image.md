# 画像生成・編集・切り抜き

[一覧へ](../README.md) · [機械可読データ](../catalog.json)

一覧更新日: 2026-10-02。**151件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

| リポジトリ | 何に使うか | 区分・評価 | ★ / 最終push |
| --- | --- | --- | --- |
| [anime-segmentation](https://github.com/SkyTNT/anime-segmentation) · [詳細](#anime-segmentation) | アニメ絵のキャラクター領域を抽出し、背景除去や合成用マスクを作る。 | AIモデル・学習 / 比較・既存工程の参考 | 845 / 2025-05-21 |
| [krita-ai-diffusion](https://github.com/Acly/krita-ai-diffusion) · [詳細](#krita-ai-diffusion) | Kritaの描画工程へ画像生成・インペイント・アウトペイントを組み込む。 | AI連携 / 更新のある導入・評価候補 | 10,662 / 2026-09-27 |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image) · [詳細](#qwen-image) | テキスト描画と画像編集を扱う汎用画像モデル群。表紙・小物・宣伝画像の制作候補。 | AIモデル・学習 / 研究モデルの評価候補 | 8,381 / 2026-02-10 |
| [Z-Image](https://github.com/Tongyi-MAI/Z-Image) · [詳細](#z-image) | 6B級の汎用画像モデル群。Turboやベースモデルを用途に合わせて利用する。 | AIモデル・学習 / 研究モデルの評価候補 | 12,058 / 2026-02-09 |
| [ComfyUI-Forbidden-Vision](https://github.com/luxdelux7/ComfyUI-Forbidden-Vision) · [詳細](#comfyui-forbidden-vision) | アニメ調・実写の両方に対応する顔の検出・セグメンテーション・補正を行うComfyUIカスタムノード群。ADetailerやFaceDetailerの代替を狙い、独自学習モデルを同梱する。 | AIモデル・学習 / 更新中の実装候補 | 103 / 2026-07-19 |
| [ComfyUI-Ultimate-Face-Fix](https://github.com/Merserk/ComfyUI-Ultimate-Face-Fix) · [詳細](#comfyui-ultimate-face-fix) | 顔を検出して切り出し、接続した生成モデルでimg2img修復し、意味マスクで顔だけを元画像に合成するComfyUIノード。 | AI出力の後処理 / 活発・候補 | 25 / 2026-07-21 |
| [Colortina](https://github.com/Amster-Ilvil/Colortina) · [詳細](#colortina) | manga-colorization-v2を基にしたローカル漫画自動彩色デスクトップツール。手動カラーヒント、区域ごとの再彩色、髪色補正、バッチ処理を備える。 | AIモデル・学習 / 小規模・初期評価候補 | 1 / 2026-08-23 |
| [ComfyUI-NeuralBooru](https://github.com/ChrisJohnson89/ComfyUI-NeuralBooru) · [詳細](#comfyui-neuralbooru) | 自然文のシーン記述をローカルLLMでDanbooruタグに変換するComfyUIノード。約14万件の実在タグ語彙で検証・別名変換・語形修正・並び替えを行い、テンプレートで包んでサンプラーへ渡す。 | AIモデル・学習 / 小規模・初期評価候補 | 19 / 2026-07-10 |

<a id="anime-segmentation"></a>

## anime-segmentation

アニメ絵のキャラクター領域を抽出し、背景除去や合成用マスクを作る。

- **リポジトリ**: https://github.com/SkyTNT/anime-segmentation
- **分類**: model / AIモデル・学習 / 比較・既存工程の参考
- **入力**: アニメキャラクター画像
- **出力**: 背景除去画像・マスク
- **環境**: Python推論環境または公式リンクのデモ。
- **依存**: anime-seg重み
- **制約・未確認**: レイヤー分解や隠れた身体部位の補完ではない。最近の更新は少ない。
- **編集者評価**: 立ち絵の切り抜きと素材整理を支える専用基盤。
- **メトリクス**: ★845、fork 75、作成 2022-08-14、最終push 2025-05-21T02:00:35Z、archived=False
- **確認**: 2026-09-09 / コミット `55d874013a2811cdf59c365059174c7823acf5b4`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/SkyTNT/anime-segmentation/tree/55d874013a2811cdf59c365059174c7823acf5b4)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/SkyTNT/anime-segmentation/blob/55d874013a2811cdf59c365059174c7823acf5b4/README.md) / [GitHub API](https://api.github.com/repos/SkyTNT/anime-segmentation) / [固定ツリー](https://github.com/SkyTNT/anime-segmentation/tree/55d874013a2811cdf59c365059174c7823acf5b4)

### 制作に使う際の検討

キャラクターと背景の分離に用途を絞ると入力準備が簡単。多層PSDが必要な工程では追加処理が必要。

**次に確かめること（実施前）**: 細い髪、白い衣装、半透明小物、背景との同系色でマスク境界を評価する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [app.py](https://github.com/SkyTNT/anime-segmentation/blob/55d874013a2811cdf59c365059174c7823acf5b4/app.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2025-05-21T02:00:34Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [skytnt/anime-seg](https://huggingface.co/skytnt/anime-seg) — file_listing_checked、確認日 2026-09-09、revision `493cb60893f47441b26ec4fb9a306bce9e342982`。代表ファイル: `isnetis.ckpt`, `isnetis.onnx`, `model.safetensors`。gated=False。

<a id="krita-ai-diffusion"></a>

## krita-ai-diffusion

Kritaの描画工程へ画像生成・インペイント・アウトペイントを組み込む。

- **リポジトリ**: https://github.com/Acly/krita-ai-diffusion
- **分類**: integration / AI連携 / 更新のある導入・評価候補
- **入力**: Kritaのキャンバス、選択範囲、プロンプト
- **出力**: 編集レイヤー・生成画像
- **環境**: Kritaと対応する生成バックエンド。
- **依存**: Krita、ComfyUI等の対応生成環境
- **制約・未確認**: 生成モデルとサービスによって費用・実行環境が変わる。
- **編集者評価**: 画師が手で直しながらAIを使う工程に適している。
- **メトリクス**: ★10,662、fork 636、作成 2023-09-01、最終push 2026-09-27T11:03:01Z、archived=False
- **確認**: 2026-09-09 / コミット `dda58d1c63e361207ccec085efbc34dbd32f1654`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Acly/krita-ai-diffusion/tree/dda58d1c63e361207ccec085efbc34dbd32f1654)。GitHub自動判定=GPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Acly/krita-ai-diffusion/blob/dda58d1c63e361207ccec085efbc34dbd32f1654/README.md) / [GitHub API](https://api.github.com/repos/Acly/krita-ai-diffusion) / [固定ツリー](https://github.com/Acly/krita-ai-diffusion/tree/dda58d1c63e361207ccec085efbc34dbd32f1654)

### 制作に使う際の検討

キャンバス上で局所修正しながら生成する制作UI。プロンプト単独生成より修正回数とレイヤー管理を評価する。

**次に確かめること（実施前）**: 選択範囲の外側の保持、レイヤー復元、バックエンド切替、生成待ちからの復旧を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [ai_diffusion/backend/client.py](https://github.com/Acly/krita-ai-diffusion/blob/dda58d1c63e361207ccec085efbc34dbd32f1654/ai_diffusion/backend/client.py)

**最新GitHub Release**: [v1.53.0](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.53.0) / 2026-08-22T19:38:06Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-23T11:02:28Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

関連: plugin_for → krita（公式説明に基づく関係、接続実行は未検証）

<a id="qwen-image"></a>

## Qwen-Image

テキスト描画と画像編集を扱う汎用画像モデル群。表紙・小物・宣伝画像の制作候補。

- **リポジトリ**: https://github.com/QwenLM/Qwen-Image
- **分類**: model / AIモデル・学習 / 研究モデルの評価候補
- **入力**: テキスト、編集対象画像
- **出力**: 生成・編集画像
- **環境**: モデル別の推論環境。公式READMEにdiffusersの例。
- **依存**: Qwen-Imageモデル、編集用モデル。モデル中核は外部Diffusers実装に依存。
- **制約・未確認**: 2.0の告知と公開重みの版を混同しない。本調査の重み候補は2512とEdit-2511。
- **編集者評価**: イラスト制作と文字入り素材の基盤として評価する。
- **メトリクス**: ★8,381、fork 559、作成 2025-08-03、最終push 2026-02-10T07:37:37Z、archived=False
- **確認**: 2026-09-09 / コミット `6b5e1f5cec987d404be5ac6657db3b9aacb56a89`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/QwenLM/Qwen-Image/tree/6b5e1f5cec987d404be5ac6657db3b9aacb56a89)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/README.md) / [GitHub API](https://api.github.com/repos/QwenLM/Qwen-Image) / [固定ツリー](https://github.com/QwenLM/Qwen-Image/tree/6b5e1f5cec987d404be5ac6657db3b9aacb56a89)

### 制作に使う際の検討

公式の配布案内とDiffusers呼出しデモとして読む。GitHub内のモデル独立実装と読み替えない。

**次に確かめること（実施前）**: 2512とEdit-2511を別々に固定し、日本語文字、参照編集、CPUオフロード時の時間を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。 GitHubは配布案内とDiffusers利用デモが中心。

**入口候補（固定ツリーで存在確認）**: [src/examples/demo.py](https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/src/examples/demo.py) / [src/examples/edit_demo.py](https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/src/examples/edit_demo.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-02-10T07:37:32Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

本文を確認した箇所:

- [src/examples/demo.py](https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/src/examples/demo.py): DiffusionPipeline.from_pretrainedを呼ぶデモ部分を確認。モデル中核の独立実装ではない。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Qwen/Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512) — file_listing_checked、確認日 2026-09-09、revision `25468b98e3276ca6700de15c6628e51b7de54a26`。代表ファイル: `text_encoder/model-00001-of-00004.safetensors`, `text_encoder/model-00002-of-00004.safetensors`, `text_encoder/model-00003-of-00004.safetensors`, `text_encoder/model-00004-of-00004.safetensors`。gated=False。
- [Qwen/Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) — file_listing_checked、確認日 2026-09-09、revision `6f3ccc0b56e431dc6a0c2b2039706d7d26f22cb9`。代表ファイル: `text_encoder/model-00001-of-00004.safetensors`, `text_encoder/model-00002-of-00004.safetensors`, `text_encoder/model-00003-of-00004.safetensors`, `text_encoder/model-00004-of-00004.safetensors`。gated=False。

<a id="z-image"></a>

## Z-Image

6B級の汎用画像モデル群。Turboやベースモデルを用途に合わせて利用する。

- **リポジトリ**: https://github.com/Tongyi-MAI/Z-Image
- **分類**: model / AIモデル・学習 / 研究モデルの評価候補
- **入力**: テキスト、モデルによって画像条件
- **出力**: 生成・編集画像
- **環境**: モデル推論環境または公式デモ。
- **依存**: 対応するZ-Imageモデル
- **制約・未確認**: アニメ専用ではない。Turbo・Base・Omni等の能力と公開範囲を分ける。
- **編集者評価**: 背景・素材・イラスト試作の生成基盤候補。
- **メトリクス**: ★12,058、fork 821、作成 2025-11-26、最終push 2026-02-09T12:49:43Z、archived=False
- **確認**: 2026-09-09 / コミット `26f23eda626ffadda020b04ff79488e1d72004cd`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。記載モデルのファイル一覧確認あり。
- **利用条件**: [配布元の条件](https://github.com/Tongyi-MAI/Z-Image/tree/26f23eda626ffadda020b04ff79488e1d72004cd)。GitHub自動判定=Apache-2.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Tongyi-MAI/Z-Image/blob/26f23eda626ffadda020b04ff79488e1d72004cd/README.md) / [GitHub API](https://api.github.com/repos/Tongyi-MAI/Z-Image) / [固定ツリー](https://github.com/Tongyi-MAI/Z-Image/tree/26f23eda626ffadda020b04ff79488e1d72004cd)

### 制作に使う際の検討

Turboで試作速度、Baseで学習・制御の適性を分けて調べる。各派生の公開状況を推測で補完しない。

**次に確かめること（実施前）**: 同一プロンプトと解像度で速度・衣装保持・文字・追加学習の互換を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定、モデルメタデータ、各素材の条件は別。商用可否の独立判定は未実施。

**入口候補（固定ツリーで存在確認）**: [inference.py](https://github.com/Tongyi-MAI/Z-Image/blob/26f23eda626ffadda020b04ff79488e1d72004cd/inference.py) / [src/config/inference.py](https://github.com/Tongyi-MAI/Z-Image/blob/26f23eda626ffadda020b04ff79488e1d72004cd/src/config/inference.py)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-02-09T12:49:08Z。公式説明と固定ツリーに基づく制作工程の検討。entry_pointsはファイルの存在確認。選択した本文確認はsource_inspectionsに限定し、全コード監査・起動・品質比較は未実施。

モデル配布確認（ファイル一覧のみ。代表モデルであり依存全体ではありません）:

- [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) — file_listing_checked、確認日 2026-09-09、revision `f332072aa78be7aecdf3ee76d5c247082da564a6`。代表ファイル: `text_encoder/model-00001-of-00003.safetensors`, `text_encoder/model-00002-of-00003.safetensors`, `text_encoder/model-00003-of-00003.safetensors`, `transformer/diffusion_pytorch_model-00001-of-00003.safetensors`。gated=False。

<a id="comfyui-forbidden-vision"></a>

## ComfyUI-Forbidden-Vision

アニメ調・実写の両方に対応する顔の検出・セグメンテーション・補正を行うComfyUIカスタムノード群。ADetailerやFaceDetailerの代替を狙い、独自学習モデルを同梱する。

- **リポジトリ**: https://github.com/luxdelux7/ComfyUI-Forbidden-Vision
- **分類**: integration / AIモデル・学習 / 更新中の実装候補
- **入力**: ComfyUIの画像または潜在、プロンプト、顔検出・マスク用モデル
- **出力**: 顔を修正した画像、顔マスク、トーン補正/アップスケール済み出力
- **環境**: ComfyUI（ComfyUI Managerまたは手動導入）。初回実行時にモデルをHuggingFaceから自動ダウンロード。
- **依存**: ComfyUI本体、luxdelux7の検出・セグメンテーションモデル（HuggingFace）
- **制約・未確認**: 強い様式化・遮蔽・特殊構図では検出失敗があり得るとREADMEに明記。モデル精度は未検証。
- **編集者評価**: 顔検出・マスク生成・コンテキスト対応インペイント・色調補正を単一ノードにまとめており、顔の修正工程を簡略化できる。
- **メトリクス**: ★103、fork 7、作成 2025-07-06、最終push 2026-07-19T14:34:33Z、archived=False
- **確認**: 2026-10-01 / コミット `b474d579c7749c8046d267c75512484120626b6d`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/luxdelux7/ComfyUI-Forbidden-Vision/tree/b474d579c7749c8046d267c75512484120626b6d)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/luxdelux7/ComfyUI-Forbidden-Vision/blob/b474d579c7749c8046d267c75512484120626b6d/README.md) / [GitHub API](https://api.github.com/repos/luxdelux7/ComfyUI-Forbidden-Vision) / [固定ツリー](https://github.com/luxdelux7/ComfyUI-Forbidden-Vision/tree/b474d579c7749c8046d267c75512484120626b6d)

### 制作に使う際の検討

生成イラストの顔修正・ディテール補正工程の候補。

**次に確かめること（実施前）**: アニメ調画像で検出・マスク精度とブレンド品質を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/luxdelux7/ComfyUI-Forbidden-Vision/blob/b474d579c7749c8046d267c75512484120626b6d/README.md)

**最新GitHub Release**: [v1.1.8](https://github.com/luxdelux7/ComfyUI-Forbidden-Vision/releases/tag/v1.1.8) / 2026-04-09T20:26:41Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-19T14:34:26Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="comfyui-ultimate-face-fix"></a>

## ComfyUI-Ultimate-Face-Fix

顔を検出して切り出し、接続した生成モデルでimg2img修復し、意味マスクで顔だけを元画像に合成するComfyUIノード。

- **リポジトリ**: https://github.com/Merserk/ComfyUI-Ultimate-Face-Fix
- **分類**: integration / AI出力の後処理 / 活発・候補
- **入力**: 元画像、生成モデル・VAE・プロンプト、顔検出/セグメンテーションモデル
- **出力**: 修復済み画像、顔クロップ、顔マスク、プレビュー
- **環境**: ComfyUI。ComfyUI Managerで依存と3つの顔解析モデルを自動導入。
- **依存**: 同梱の顔解析モデル、使用する生成チェックポイント。
- **制約・未確認**: 生成モデルと素材は利用者が用意。モデル重みは別途取得で上流ライセンスに従う。
- **編集者評価**: アニメ・イラスト・実写のチェックポイントに対応し、複数顔を順に処理して「修復」「再構成」などのデノイズプリセットで調整できる点が実用的。
- **メトリクス**: ★25、fork 6、作成 2026-07-20、最終push 2026-07-21T17:06:53Z、archived=False
- **確認**: 2026-09-30 / コミット `98a00ad332803f4adf9e2154a211e3641971d7ef`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Merserk/ComfyUI-Ultimate-Face-Fix/tree/98a00ad332803f4adf9e2154a211e3641971d7ef)。GitHub自動判定=AGPL-3.0。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Merserk/ComfyUI-Ultimate-Face-Fix/blob/98a00ad332803f4adf9e2154a211e3641971d7ef/README.md) / [GitHub API](https://api.github.com/repos/Merserk/ComfyUI-Ultimate-Face-Fix) / [固定ツリー](https://github.com/Merserk/ComfyUI-Ultimate-Face-Fix/tree/98a00ad332803f4adf9e2154a211e3641971d7ef)

### 制作に使う際の検討

ラフや生成画像の顔崩れを後処理で整える用途。

**次に確かめること（実施前）**: アニメ系チェックポイントで複数顔画像を処理し、継ぎ目と同一性の保持を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/Merserk/ComfyUI-Ultimate-Face-Fix/blob/98a00ad332803f4adf9e2154a211e3641971d7ef/README.md)

**最新GitHub Release**: APIにlatest Releaseなし。開発停止やモデル未公開を意味しません。

デフォルトブランチの確認コミット日時: 2026-07-21T17:06:53Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="colortina"></a>

## Colortina

manga-colorization-v2を基にしたローカル漫画自動彩色デスクトップツール。手動カラーヒント、区域ごとの再彩色、髪色補正、バッチ処理を備える。

- **リポジトリ**: https://github.com/Amster-Ilvil/Colortina
- **分類**: desktop_tool / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 白黒漫画画像、PDF、画像フォルダ
- **出力**: 彩色済み画像
- **環境**: Python/PySide6。Apple SiliconはMPS、NVIDIAはCUDA、不足時はCPU。初回にモデル重みを取得。
- **依存**: manga-colorization-v2のgenerator/denoiser重み、PyTorch、OpenCV等
- **制約・未確認**: モデル重みはリポジトリ非同梱。新規・小規模。第三者コード/モデルは各ライセンスに従う。
- **編集者評価**: 自動彩色に手動ガイドと部分再彩色を重ねられるため、下地づくりから修正までを1画面で回せる。
- **メトリクス**: ★1、fork 0、作成 2026-07-16、最終push 2026-08-23T09:47:19Z、archived=False
- **確認**: 2026-09-30 / コミット `056c6ed79609037605a6d5fdde9f0bda5176abac`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/Amster-Ilvil/Colortina/tree/056c6ed79609037605a6d5fdde9f0bda5176abac)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/Amster-Ilvil/Colortina/blob/056c6ed79609037605a6d5fdde9f0bda5176abac/README.md) / [GitHub API](https://api.github.com/repos/Amster-Ilvil/Colortina) / [固定ツリー](https://github.com/Amster-Ilvil/Colortina/tree/056c6ed79609037605a6d5fdde9f0bda5176abac)

### 制作に使う際の検討

ページ単位の彩色下地と手直しに。

**次に確かめること（実施前）**: 見開き数ページで自動彩色の品質と再彩色・髪色補正の手間を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [main.py](https://github.com/Amster-Ilvil/Colortina/blob/056c6ed79609037605a6d5fdde9f0bda5176abac/main.py)

**最新GitHub Release**: [v5.13.27](https://github.com/Amster-Ilvil/Colortina/releases/tag/v5.13.27) / 2026-08-10T08:33:51Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-08-23T09:44:36Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。

<a id="comfyui-neuralbooru"></a>

## ComfyUI-NeuralBooru

自然文のシーン記述をローカルLLMでDanbooruタグに変換するComfyUIノード。約14万件の実在タグ語彙で検証・別名変換・語形修正・並び替えを行い、テンプレートで包んでサンプラーへ渡す。

- **リポジトリ**: https://github.com/ChrisJohnson89/ComfyUI-NeuralBooru
- **分類**: integration / AIモデル・学習 / 小規模・初期評価候補
- **入力**: 英語のシーン説明文、system prompt、プロンプトテンプレート、ローカルLLMのモデル名
- **出力**: 検証済みのDanbooruタグ文字列、除外されたタグ一覧
- **環境**: ComfyUI本体と、LM Studio/Ollama等のOpenAI互換ローカルサーバ（READMEはQwen3-1.7Bを推奨）。ノード自体はPython標準ライブラリのみで追加依存なし。
- **依存**: ComfyUI、ローカルLLMサーバ（LM Studio/Ollama/llama.cpp/vLLM等）
- **制約・未確認**: READMEの想定はSDXL系チェックポイントと英語Danbooru語彙。日本語入力の扱いやタグ辞書の網羅性は記載されていない。fuzzy matchは既定で無効。
- **編集者評価**: タグ語彙を重みに焼き込まず、汎用LLMの提案を同梱のタグ辞書で検証する設計が特徴。LLMを差し替えても検証側が効く。
- **メトリクス**: ★19、fork 2、作成 2026-06-29、最終push 2026-07-10T03:25:47Z、archived=False
- **確認**: 2026-10-02 / コミット `e3376e5fcea10d38c52e8261f81f73fab6ef3352`
- **検証範囲**: README・ファイル構成確認。起動・推論なし。モデルファイル一覧は未確認。
- **利用条件**: [配布元の条件](https://github.com/ChrisJohnson89/ComfyUI-NeuralBooru/tree/e3376e5fcea10d38c52e8261f81f73fab6ef3352)。GitHub自動判定=MIT。独立レビュー・商用可否判定は未実施。

根拠: [固定README](https://github.com/ChrisJohnson89/ComfyUI-NeuralBooru/blob/e3376e5fcea10d38c52e8261f81f73fab6ef3352/README.md) / [GitHub API](https://api.github.com/repos/ChrisJohnson89/ComfyUI-NeuralBooru) / [固定ツリー](https://github.com/ChrisJohnson89/ComfyUI-NeuralBooru/tree/e3376e5fcea10d38c52e8261f81f73fab6ef3352)

### 制作に使う際の検討

大量のプロンプト作成・表記ゆれ統一をワークフロー内で自動化する用途。

**次に確かめること（実施前）**: 手元のワークフローに接続し、Qwen3-1.7Bで同じ日本語記述からタグが再現するか、dropped_tagsの傾向を確認する。

**利用条件の確認メモ**: コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。

**入口候補（固定ツリーで存在確認）**: [README.md](https://github.com/ChrisJohnson89/ComfyUI-NeuralBooru/blob/e3376e5fcea10d38c52e8261f81f73fab6ef3352/README.md)

**最新GitHub Release**: [v1.4.0](https://github.com/ChrisJohnson89/ComfyUI-NeuralBooru/releases/tag/v1.4.0) / 2026-07-10T03:25:57Z / prerelease=False

デフォルトブランチの確認コミット日時: 2026-07-10T03:15:04Z。AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。
