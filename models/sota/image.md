# 画像生成・画像変換のアニメ系SOTA（2026-10-01）

[一覧へ](../anime-task-sota.md) · [リポジトリ全体像](../anime-repositories.md) · [正本JSON](../../sota-catalog.json)

選定基準・注意は[一覧ページ](../anime-task-sota.md)。各項目の「最良」は確度付きの編集判断で、重み取得・推論実行は未実施。

### テキスト→画像(アニメ/イラスト生成)

<a id="text-to-image"></a>
- **判定**: アニメ特化の最良 / 確度 高
- **最良**: [circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima/tree/f973fc41ec7545364ac9776c2440285f43ff2a30)（revision `f973fc41` / 作成 2026-01-29 / 更新 2026-08-24）
- **利用条件**: other/circlestone-labs-non-commercial-license。HFメタデータは other/circlestone-labs-non-commercial-license。カード・LICENSE.md: モデルと派生物は非商用のみ、NVIDIA Open Model License(Cosmos-Predict2派生)も適用。出力画像の商用利用は可だが、有料生成サービス/APIでのホスト、商用ゲームへの重み同梱、商用目的でのモデル蒸留・学習は不可。個人による派生重みの販売のみ例外。商用ライセンスはメール申請。商用可とは断定できない。
- **選定根拠**: 【事実】circlestone-labs/Anima(2B, Cosmos-Predict2-2B派生, CircleStone×Comfy Org)は DL 30日1,228,812/累計5,537,017、likes 2,329、Discussions 240、GitHubコード参照1,378件。同時計測の比較対象は Anima-2.9B 122件、Z-Anime 148件、noobai-XL 245件。HF上の30日DLは noobai-XL-1.1 135,958(最終更新2025-09)、animagine-xl-4.0 366,672(最終更新2025-02)、Z-Anime 2,265、NetaYume-Lumina 19,698(最終更新2025-12)、NewBie-image-Exp0.1 255、Anima-2.9B 32,068。第三者の定量ベンチは見つからず、カードも自己比較用ワークフロー(anima_comparison.json)のみ。【評価】採用量が次点より1桁以上大きく、ComfyUI/Forge Neo/sd-scripts/ai-toolkit/diffusion-pipe が揃って対応するため首位。X(2026-09-22, javawock7618, 1,158 likes)は『アニメ画像=Anima aesthetic 1.1』、shimotti_ai(2026-08-29, 427 likes)は『Anima=構図理解・自然言語に強い/Illustrious=LoRA・ControlNet・量産に強い』と使い分けを提示。一方 mr_290000000000(2026-08-12)は形状・色調の正確さはIllustrious系より劣ると批判しており、用途で分かれる。【版の選択】既定は anima-base-v1.0.safetensors(作者がLoRA学習はBase版で行うよう指示、最大の柔軟性/画風追従、HF討議214でAesthetic 1.1は『AI感が強い』『1.0b/Baseを使う理由しかない』との声)。高速反復は anima-turbo-v1.1(CFG1・8〜12step、作者が開始点として推奨、ただし討議210/236で画風崩れ・ネガ無効の指摘)。標準の見た目重視は anima-aesthetic-v1.1(Xで高評価、HFは賛否)。最終更新は2026-08-24(turbo-v1.1追加)。次世代(Anima 2)については、討議232に『作者は資金不足で自己資金では出せないと発言』との第三者書込みがあるのみで一次確認不可。【未解決】非商用ライセンス、Qwen-Image VAEの再構成損失への不満(討議200)。NovelAI V5はクローズドで重み非公開のため対象外。
- **指標（確認日時点）**: DL累計 5,537,017 / 直近30日 1,228,812 / likes 2,329 / Spaces 60
- **概要**: アニメ/イラスト特化の2B DiT テキスト→画像。Danbooruタグ+自然文の混在プロンプト、@artistタグ、年/品質/安全タグに対応。Qwen3-0.6B(base)をテキストエンコーダ、Qwen-Image VAEを使用。
- **入力**: テキストプロンプト(Danbooruタグ・自然文・混在、先頭に品質/年/安全タグ)。512²〜1536²。
- **出力**: 画像(PNG/JPEG等)。
- **必要環境**: カード記載: ComfyUIネイティブ対応。diffusion_models/anima-*.safetensors(約4.18GB/ファイル)、text_encoders/qwen_3_06b_base.safetensors、vae/qwen_image_vae.safetensors。30〜50step・CFG4〜5(Turboはstep 8〜12・CFG1)。VRAM要件はカードに記載なし(未測定)。
- **制約**: リアル画は不得手(意図的)。短いプロンプトで意図しない内容が出る。文字描画は単語レベル。Baseは素の画風が地味。Turboは多様性低下・ネガティブ無効。LLMアダプタ(text conditioner)は学習で劣化しやすく、学習時はlr=0推奨。
- **使う版・派生**: 原本: split_files/diffusion_models/ の anima-base-v1.0(LoRA学習/汎用既定), anima-aesthetic-v1.1(v1.0=スタイルLoRAマージ版, v1.0b=純aesthetic全FT), anima-turbo-v1.1(蒸留高速), anima-preview/preview2/preview3-base(旧)。Diffusers形式: circlestone-labs/Anima-Base-v1.0-Diffusers(30日18,509DL)。派生: Gazingstars123/Anima-2.9B(層拡張preview v1)、INT8 Bedovyy/Anima-INT8(30日8,933)、GGUF vanes430/Anima-Turbo-V1.1-GGUF 等。
- **根拠**: [モデル概要(2B, 数百万枚のアニメ画像+約80万枚の非アニメ画像、知識カットオフ2025-09)、Base/Aesthetic/Turbo各版の説明と推奨、対応ツール・推奨設定・ライセンス。](https://huggingface.co/circlestone-labs/Anima/blob/f973fc41ec7545364ac9776c2440285f43ff2a30/README.md) / [CircleStone Labs Non-Commercial License v1.2(モデル・派生は非商用のみ、出力は商用利用可、有料API/商用ゲーム同梱は不可)](https://huggingface.co/circlestone-labs/Anima/blob/f973fc41ec7545364ac9776c2440285f43ff2a30/LICENSE.md) / [版の更新履歴(aesthetic-v1.1=2026-07-13, turbo-v1.1=2026-08-24)](https://huggingface.co/circlestone-labs/Anima/commits/main) / [Aesthetic 1.1/1.0の画風への不満とBase・1.0b継続利用の声](https://huggingface.co/circlestone-labs/Anima/discussions/214) / [turbo-v1.1の評価(1.0より安定・解剖学改善、素の画風は粗い)](https://huggingface.co/circlestone-labs/Anima/discussions/233) / [2026-09-22: ローカルのアニメ画像ベストは Anima aesthetic 1.1(1,158 likes)](https://x.com/javawock7618/status/2102314466444775605) / [2026-08-29: Anima=構図理解・自然言語、Illustrious=LoRA/ControlNet/量産、NovelAI V5=手軽さ(427 likes)](https://x.com/shimotti_ai/status/2093662209704677545)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `Qwen/Qwen-Image-2.1` — アニメ特化ではない汎用T2I/編集統合(7B, 2026-09-14公開)。アニメも出せるとのX報告はあるが研究用ライセンス(非商用)。
- **次点**: `Gazingstars123/Anima-2.9B`（Animaの非公式層拡張(28→40層, 追加新層のみ学習のpreview v1)。30日32,068DL/累計81,037/393 likes/参照122件で、採用・評価は原本の3%未満。カードに定量ベンチなし。討議229でも知識量は他の微調整に劣るとの声。ただしForge Neo/ComfyUI対応で多くのマージが2.9Bへ移行中(X 2026-09)。有望だが未成熟。） / `Laxhar/noobai-XL-1.1`（SDXL系の事実上標準(30日135,958DL/累計896,846)。LoRA/ControlNet資産は最大だが最終更新2025-09、ライセンスfair-ai-public-license-1.0-sd。新規開発は世代的にAnimaが優勢(X/HF討議)。） / `SeeSee21/Z-Anime`（Z-Image Base(6B)の全FT。Apache-2.0表記で商用を見据える場合の有力候補(作者が討議10で追加制限なしと回答)。ただし30日2,265DL/累計28,408、参照148件、最終更新2026-04-27で採用は桁違いに小さい。）

関連リポジトリ:

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) — Animaの標準実行基盤(カードがComfyUIネイティブ対応と明記、ワークフローPNG同梱)（★135,624 / GPL-3.0 / 最終push 2026-09-30 / release v0.38.0 (2026-09-29) / 確認コミット [`83071e1a`](https://github.com/Comfy-Org/ComfyUI/blob/83071e1aec311d31e773d64d6872181b3bad0fe2/README.md) / 制作カタログ: [comfyui](../../categories/workflow.md#comfyui)）
  - 135,621★/GPL-3.0/v0.38.0(2026-09-29)。Comfy OrgがAnimaの共同開発元。
- [Haoming02/sd-webui-forge-classic](https://github.com/Haoming02/sd-webui-forge-classic) — Forge Neo: WebUI系でAnima 2B/2.9B/3.8B、Anima-LLLite、Anima Edit(要LoRA)を対応（★1,772 / AGPL-3.0 / 最終push 2026-09-30 / release 2.29.1 (2026-09-21) / 確認コミット [`0b1783c7`](https://github.com/Haoming02/sd-webui-forge-classic/blob/0b1783c79b397e73818c3d8432b25cc3cbb5ca50/README.md)）
  - README記載でAnima各版・ControlNet-LLLite対応。1,772★/AGPL-3.0/2.29.1(2026-09-21)。
- [pamparamm/ComfyUI-ppm](https://github.com/pamparamm/ComfyUI-ppm) — Anima/SDXL向け Attention Couple(多人数の領域指定)、NegPiP（★268 / AGPL-3.0 / 最終push 2026-08-09 / 確認コミット [`6c6c3601`](https://github.com/pamparamm/ComfyUI-ppm/blob/6c6c360155cace9d7091306c1b8e26d9c7438620/README.md)）
  - 268★/AGPL-3.0、pushed 2026-08-09。HF討議218/202で問題になる多人物・スタイル混入の対策ノード。

### テキスト→画像(Anima用VAE)

<a id="text-to-image--vae"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/1f12b17be14c89b026c51a91d67c32f84bb047bc)（revision `1f12b17b` / 作成 2025-08-05 / 更新 2026-09-23）
- **利用条件**: apache-2.0。メタデータはapache-2.0(元のQwen/Qwen-ImageもApache-2.0)。Anima本体は非商用ライセンスで別。VAE単体の利用条件のみ。
- **選定根拠**: 【事実】AnimaはQwen-Image VAE固定(Animaカード: vae/qwen_image_vae.safetensors、kohya-ss/Anima-LLLiteカードもVAE=Qwen-Image VAEと明記)。アニメ専用VAEで採用されているものは確認できず、Comfy-Org/Qwen-Image_ComfyUIは30日2,655,340DL/累計26,618,324/507 likes(リポジトリ全体の合算でVAE単体ではない)、Apache-2.0。HF討議200(2026-06-24)でFLUX.2 VAEへの変更要望があり『QwenVAEは再構成損失がある』との意見が出たが、作者の対応は未確認(Anima 2026-08-24版もQwen VAEのまま)。【評価】別VAEへの差し替えは再学習が必要なためAnimaでは選択肢がなく、ComfyUI配布の単体ファイルが実用上の最良。SDXL系(Illustrious/NoobAI)は別VAEで本項目の対象外。
- **指標（確認日時点）**: DL累計 26,618,324 / 直近30日 2,655,340 / likes 507 / Spaces 23
- **概要**: Qwen-Image用16chVAE(ComfyUI再配布)。AnimaおよびAnima派生(2.9B等)が共通で使用。アニメ特化ではない汎用VAE。
- **入力**: 潜在表現(生成時)/画像(エンコード時)。
- **出力**: 画像/潜在表現。
- **必要環境**: ComfyUI/models/vae/qwen_image_vae.safetensors に配置。VRAM要件は未測定(約254MB)。
- **制約**: アニメ専用ではない。細部の再構成損失がありAnimaの上限を下げるとのコミュニティ指摘(討議200)。差し替え不可。
- **使う版・派生**: 原本: Qwen/Qwen-Image の vae/ サブフォルダ(30日277,333DL, Apache-2.0)。ComfyUI用単体ファイルが本エントリ。
- **根拠**: [ComfyUI用再パッケージ。split_files/vae/qwen_image_vae.safetensors(253,806,246B)を含み、Anima標準の配置先(ComfyUI/models/vae)と一致。](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/1f12b17be14c89b026c51a91d67c32f84bb047bc/README.md) / [AnimaがQwen-Image VAEを使うとカードに明記](https://huggingface.co/circlestone-labs/Anima/blob/f973fc41ec7545364ac9776c2440285f43ff2a30/README.md) / [FLUX.2 VAE変更要望とQwen VAEの再構成損失への指摘](https://huggingface.co/circlestone-labs/Anima/discussions/200)
- **次点**: `Qwen/Qwen-Image`（VAEの原本だが全パイプライン(テキストエンコーダ含む)の巨大リポジトリ。VAEだけ欲しい用途にはComfy-Org再配布が実用的。）

### テキスト→画像(プロンプト拡張LLM)

<a id="text-to-image--prompt-expansion"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [KBlueLeaf/TIPO-500M-ft](https://huggingface.co/KBlueLeaf/TIPO-500M-ft/tree/386fc21b10c810c0c1c8f182695e28fbbd45597c)（revision `386fc21b` / 作成 2025-01-10 / 更新 2025-01-22）
- **利用条件**: other/kohaku-license-1.0。HFメタデータはother。カードはKohaku License 1.0(条文はHF/LICENSE参照)。商用可否は未確認のため断定しない。
- **選定根拠**: 【事実】KBlueLeaf/TIPO-500M-ft(LLaMA系500M, Danbooru2023+GBC10M+Coyo11M, 技術報告 arXiv 2411.08127)は30日59,247DL/累計436,120/48 likes/spaces 18、GitHubコード参照61件。実行拡張 KohakuBlueleaf/z-tipo-extension(637★, Apache-2.0, 2026-08-23更新)がWebUI/Forge/ComfyUIで動き、KGen(101★)のモデル一覧に収録。より新しい TIPO-v2.1-1B-A200M(2026-08-22, 30日10,909DL/23 likes, 4096ctx)はKGenのtipo_model_list先頭だが、カードに比較ベンチがなく実績も5週間分のみ。【評価】旧式でも実績のあるTIPO-500M-ftを首位とし、v2.1は次点。【未検証】TIPOの学習データはDanbooru2023までで、Animaのタグ(@artist・年/品質タグ等)との整合は未確認。Anima専用のプロンプト拡張モデルはHF上で見つからず、汎用LLM(Qwen/Gemma)で自然文を書く運用が別途必要。
- **指標（確認日時点）**: DL累計 436,120 / 直近30日 59,247 / likes 48 / Spaces 18
- **概要**: 短いタグ/自然文プロンプトを詳細なDanbooruタグ+自然文へ拡張する小型LM(TIPO: Text to Image with text presampling for Prompt Optimization)。
- **入力**: 短いタグ列または自然文、メタ指定(品質・レーティング・長さ等)。
- **出力**: 拡張されたタグ列/自然文プロンプト。
- **必要環境**: カード記載: z-tipo-extension経由でGGUF(F16)をllama-cppで実行可能。VRAM/速度は未測定。
- **制約**: 学習データはDanbooru2023までで最新タグ(2025以降)に弱い可能性。Anima専用ではない(整合は未検証)。
- **使う版・派生**: 同リポジトリ TIPO-500M-ft-F16.gguf。新版: KBlueLeaf/TIPO-v2.1-1B-A200M(gguf/ 同梱)、TIPOv2-1B-A200M。量子化: mradermacher/TIPO-500M-ft-i1-GGUF。
- **根拠**: [TIPOの概要、z-tipo-extensionでの利用方法(WebUI/Forge/ComfyUI)、200M/500M系の学習データ表、Kohaku License 1.0の明記、技術報告リンク。](https://huggingface.co/KBlueLeaf/TIPO-500M-ft/blob/386fc21b10c810c0c1c8f182695e28fbbd45597c/README.md) / [TIPO技術報告(ベンチは著者自己報告)](https://arxiv.org/abs/2411.08127) / [KGenのtipo_model_list(v2.1が先頭、TIPO-500M-ftも収録)](https://github.com/KohakuBlueleaf/KGen/blob/fecfe05341f021f916f9b23e1c93f23b4c50d9bb/src/kgen/models.py) / [v2.1のカード(メタデータ修正・4096ctx、比較ベンチなし、Kohaku License 1.0)](https://huggingface.co/KBlueLeaf/TIPO-v2.1-1B-A200M/blob/f5a318524a4ab30cdbbf51816cf406170f454e65/README.md)
- **次点**: `KBlueLeaf/TIPO-v2.1-1B-A200M`（同作者の最新(2026-08-22, 1B-A200Mの疎モデル, データ欠陥修正済み, KGen一覧の先頭)。30日10,909DL/累計13,087/23 likes、ベンチなし。実績不足で次点。今後逆転しうる。） / `KBlueLeaf/DanTagGen-delta-rev2`（前世代(2024-04)。30日18,175DLだが、TIPOに置換済みで新規採用の理由がない。）

関連リポジトリ:

- [KohakuBlueleaf/z-tipo-extension](https://github.com/KohakuBlueleaf/z-tipo-extension) — TIPO実行用拡張(SD-WebUI/Forge/ComfyUI)（★637 / Apache-2.0 / 最終push 2026-08-23 / 確認コミット [`61328629`](https://github.com/KohakuBlueleaf/z-tipo-extension/blob/6132862978021727284215bc2d5fe5257a872709/README.md)）
  - 637★/Apache-2.0、pushed 2026-08-23。TIPO各版をGGUFで読み込むUI/ノードを提供。
- [KohakuBlueleaf/KGen](https://github.com/KohakuBlueleaf/KGen) — TIPO/DanTagGenの推論ライブラリ(tag拡張・サンプリング)（★101 / Apache-2.0 / 最終push 2026-08-22 / 確認コミット [`fecfe053`](https://github.com/KohakuBlueleaf/KGen/blob/fecfe05341f021f916f9b23e1c93f23b4c50d9bb/README.md)）
  - 101★/Apache-2.0、2026-08-22更新、tipo_model_listにv2.1を追加済み。

### テキスト→画像(LoRA/ファインチューン学習ツール)【GitHubリポジトリ選定のみ】

<a id="text-to-image--lora-training-tool"></a>
- **判定**: モデルなし / 確度 中
- **選定根拠**: 【注意】HFモデルではなくGitHubツールの選定で、best=nullのまま関連リポジトリが本体。【事実】Animaカードは学習に作者自身のdiffusion-pipe(llm_adapter_lr=0が既定)とsd-scriptsを挙げる。kohya-ss/sd-scripts(7,242★, Apache-2.0, v0.12.0=2026-09-24)はREADMEにAnima LoRA/LLLite学習・torch.compile対応を記載。ostris/ai-toolkit(12,164★, MIT)はAnima-Base-v1.0-Diffusersを対応モデルに列挙。bmaltais/kohya_ss(12,609★, v26.0.0)はAnima LoRA・全FT・LLLite・LoHa/LoKrをGUIで提供。Nerogar/OneTrainer(3,220★, AGPL-3.0)とkohya-ss/musubi-tunerのREADMEにはAnimaの記載なし(未対応の可能性、未検証)。【評価】最良はsd-scripts(Anima対応が最も詳細・最新、Apache-2.0、Forge/ComfyUI/LLLiteと同系)。複数GPU・作者推奨設定を使うならdiffusion-pipe(GPL-3.0)。

関連リポジトリ:

- [kohya-ss/sd-scripts](https://github.com/kohya-ss/sd-scripts) — Anima LoRA/全FT/ControlNet-LLLite学習の基準実装(docs/anima_train_network.md)（★7,242 / Apache-2.0 / 最終push 2026-09-24 / release v0.12.0 (2026-09-24) / 確認コミット [`690ea7f9`](https://github.com/kohya-ss/sd-scripts/blob/690ea7f96c23182352ec63def76d431c6120bd2f/README.md) / 制作カタログ: [sd-scripts](../../categories/workflow.md#sd-scripts)）
  - 7,242★/Apache-2.0/v0.12.0(2026-09-24)。READMEがAnima LoRA・torch.compile・LLLite学習を記載。
- [tdrussell/diffusion-pipe](https://github.com/tdrussell/diffusion-pipe) — Anima作者自身の学習スクリプト(パイプライン並列)（★2,028 / GPL-3.0 / 最終push 2026-09-28 / 確認コミット [`334106c2`](https://github.com/tdrussell/diffusion-pipe/blob/334106c2d0e29131b53d504b80e211942dac147e/README.md)）
  - 2,028★/GPL-3.0、pushed 2026-09-28。READMEに『Support Anima』。Animaカードがllm_adapter_lr=0を既定と説明。
- [ostris/ai-toolkit](https://github.com/ostris/ai-toolkit) — GUI付き汎用LoRA学習(Anima-Base-v1.0-Diffusers対応)（★12,164 / MIT / 最終push 2026-09-27 / 確認コミット [`ecee894e`](https://github.com/ostris/ai-toolkit/blob/ecee894ed2b1f3716d9d7326693061ec1a3105bb/README.md)）
  - 12,164★/MIT、pushed 2026-09-27。READMEの対応モデルにAnimaを記載。
- [bmaltais/kohya_ss](https://github.com/bmaltais/kohya_ss) — sd-scriptsのGUIラッパー(Anima LoRA/全FT/LLLite/LoHa・LoKr)（★12,609 / Apache-2.0 / 最終push 2026-08-01 / release v26.0.0 (2026-07-09) / 確認コミット [`45088f04`](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/README.md)）
  - 12,609★/Apache-2.0/v26.0.0(2026-07-09)。READMEでAnima対応を明記。

### 画像→画像(アニメ超解像・劣化復元)

<a id="image-to-image--upscaling"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [HikariDawn/APISR](https://huggingface.co/HikariDawn/APISR/tree/b0fa82171d75218f538f61f66c18f41c6e61111c)（revision `b0fa8217` / 作成 2024-04-05 / 更新 2024-04-05）
- **利用条件**: gpl-3.0。HFメタデータはgpl-3.0(GitHubもGPL-3.0)。学習データ(API dataset: アニメ動画フレーム)の権利関係はカード未記載。商用可とは断定しない。
- **選定根拠**: 【事実】HikariDawn/APISR(CVPR 2024, arXiv 2403.01598, Kiteretsu77/APISR 1,136★)はアニメ制作工程に合わせた劣化モデルで学習した実世界アニメSR。論文Table1(AVC-RealLQ 46クリップ, 4倍, 無参照指標・著者自己報告)で APISR: NIQE 6.719/MANIQA 0.514/CLIPIQA 0.711、AnimeSR 8.109/0.462/0.539、VQD-SR 8.202/0.464/0.567(Real-ESRGAN*等は動画データでfine-tuneした版でanime6B本体ではない)。公式HFにx2(RRDB)/x4(RRDB, GRL, DAT)重みあり。【弱点】HF側のDL計測は0(.pth)、likes 7、GitHubコード参照12件、ライセンスGPL-3.0、最終push 2025-10。採用実績は乏しい。【実務の既定】xinntao/Real-ESRGAN(36,952★, BSD-3-Clause)のRealESRGAN_x4plus_anime_6B/animevideov3は最も広く知られた標準的選択肢で(採用数は未計測)、GitHubリリース配布のみ(HF公式なし)。ライセンス・ツール互換を優先するならこちら。品質優先・単体画像の劣化復元でAPISR、という使い分け。評価が無参照指標・自己報告のため信頼度は低。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 7 / Spaces 0
- **概要**: アニメ制作工程に着想した劣化モデル(予測型圧縮・線強調の疑似GT)とbalanced twin perceptual lossで学習した実世界アニメ超解像(画像・動画共用)。
- **入力**: 低画質アニメ画像/動画フレーム。
- **出力**: 2倍/4倍拡大画像。
- **必要環境**: リポジトリ記載の推論はPyTorch(Python 3.10, torch 2.1.1)。GRLは約6.5MBと小型。VRAM・速度は未測定。
- **制約**: 評価は無参照指標のみ(著者自己報告)。採用実績が少なく、ComfyUI/chaiNNer等への標準搭載は確認できていない。GPL-3.0。
- **使う版・派生**: ONNX: Xenova/4x_APISR_GRL_GAN_generator-onnx(30日573DL)、Xenova/2x_APISR_RRDB_GAN_generator-onnx。デモ: spaces/HikariDawn/APISR。
- **根拠**: [APISRモデルカード(論文・コード・デモへのリンク、要旨)。重みファイル一覧で2x_RRDB/4x_RRDB/4x_GRL/4x_DATを確認。](https://huggingface.co/HikariDawn/APISR/blob/b0fa82171d75218f538f61f66c18f41c6e61111c/README.md) / [APISR論文(AVC-RealLQでNIQE/MANIQA/CLIPIQAの比較, 自己報告)](https://arxiv.org/abs/2403.01598) / [推論・学習手順、API/AVCデータセット、Model Zoo](https://github.com/Kiteretsu77/APISR/blob/c0c0407ba68c0bc5026e43da05f0e7c1cf7b9b95/README.md)
- **次点**: `xinntao/Real-ESRGAN (RealESRGAN_x4plus_anime_6B / realesr-animevideov3)`（最も広く知られた選択肢(36,952★, BSD-3-Clause)。重みはGitHubリリース配布のみでHF公式リポジトリなし(hlky/RealESRGAN_x4plus_anime_6B等は非公式ミラー)。定量ベンチなし、最終push 2024-08。ライセンス/互換性重視ならこちらを使う。） / `Kim2091/2x-AnimeSharpV4`（HF 57 likes(2025-01公開)のRCAN 2倍。ライセンスCC-BY-NC-SA-4.0、定量評価なし(slow.pics比較のみ)。） / `bilibili/ailab (Real-CUGAN)`（Real-CUGANの公式(5,872★)。ライセンス表記なし、最終push 2023-08。）

関連リポジトリ:

- [Kiteretsu77/APISR](https://github.com/Kiteretsu77/APISR) — APISR公式(推論・学習・データ収集)（★1,136 / GPL-3.0 / 最終push 2025-10-16 / release v0.3.0 (2024-04-03) / 確認コミット [`c0c0407b`](https://github.com/Kiteretsu77/APISR/blob/c0c0407ba68c0bc5026e43da05f0e7c1cf7b9b95/README.md)）
  - 1,136★/GPL-3.0、最終push 2025-10-16。CVPR 2024。
- [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) — anime6B/animevideov3の公式実装と重み配布（★36,952 / BSD-3-Clause / 最終push 2024-08-06 / release v0.3.0 (2022-09-20) / 確認コミット [`a4abfb29`](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/README.md)）
  - 36,952★/BSD-3-Clause、最終push 2024-08-06(v0.3.0)。docs/anime_model.mdがanime6Bの使い方とwaifu2x比較を掲載(定性のみ)。実務の既定候補。
- [chaiNNer-org/chaiNNer](https://github.com/chaiNNer-org/chaiNNer) — 超解像モデルを連鎖実行する汎用ノードGUI(アニメ専用ではない。READMEのモデル対応範囲は未精読)（★6,054 / GPL-3.0 / 最終push 2026-09-30 / release v0.25.1 (2025-10-23) / 確認コミット [`b3ca7ff5`](https://github.com/chaiNNer-org/chaiNNer/blob/b3ca7ff586d4071dbe8601bc4000493560503f21/README.md)）
  - 6,054★/GPL-3.0、pushed 2026-09-30、v0.25.1。
- [nagadomi/nunif](https://github.com/nagadomi/nunif) — waifu2x最新版(MIT)を含むnunif（★3,471 / MIT / 最終push 2026-09-18 / release 0.0.0 (2022-11-09) / 確認コミット [`d23721f1`](https://github.com/nagadomi/nunif/blob/d23721f1b5f0a4c92c3ee1be013180bf298730c5/README.md)）
  - 3,471★/MIT、pushed 2026-09-18。waifu2x元祖(28,230★)の後継実装。

### 画像→画像(線画・漫画の着色)

<a id="image-to-image--colorization"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [Johanan0528/MangaNinjia](https://huggingface.co/Johanan0528/MangaNinjia/tree/4e6237c1d22415272bf98426616fe478cd3202a0)（revision `4e6237c1` / 作成 2025-01-14 / 更新 2025-01-14）
- **利用条件**: apache-2.0。HFメタデータはapache-2.0だが、公式GitHub READMEはCC BY-NC 4.0バッジで不一致。基盤にSD1.5・CLIP系を用いるため各ライセンスも影響。商用可とは断定しない(非商用前提で扱う)。
- **選定根拠**: 【事実】Johanan0528/MangaNinjia(MangaNinja, CVPR 2025 Highlight, 論文upvotes 62, ali-vilab/MangaNinjia 742★)は参照画像+線画からの着色で、点指定による対応付け制御を持つ。論文は自作ベンチでDINO/CLIP/PSNR/MS-SSIM/LPIPSを報告(自己報告)。HF: likes 12/spaces 5、DL計測0(.pth)、GitHubコード参照9件。【ライセンス不一致】HFメタデータはapache-2.0だがGitHub READMEバッジはCC BY-NC 4.0。【対抗】tellurion/ColorizeDiffusionXL(2026-03, arXiv 2603.05971)は50K-FIDで自身8.28、MangaNinja 42.85(512px), 著者自己評価のためMangaNinjaより大差だが、GitHub 8★/HF 0 likes/CC-BY-NC-SA-4.0で実績ゼロ。Cobra(SIGGRAPH 2025, Apache-2.0, 253★, HF 33 likes)は200枚超の参照に対応するコミック向けで、ColorizeDiffusionXL論文ではスケッチ様式が変わると劣化と評価されている(競合著者の評価)。【評価】実績と査読済みの根拠でMangaNinjaを暫定首位。3系統とも自己/競合著者評価のみで、標準といえる勝者は不在。FLUX.2-klein-9B用の漫画着色LoRA(thedeoxen, 累計4,965DL, Apache-2.0だが基盤はflux-non-commercial)もあり、汎用編集モデル流用が最近の流れ。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 12 / Spaces 5
- **概要**: 参照画像の色・特徴を線画へ精密に転写するジフュージョン系着色(ReferenceNet+ControlNet+点制御)。アニメ制作向け。
- **入力**: 線画(または白黒漫画)+参照カラー画像、任意で対応点。
- **出力**: 着色画像(公式実装は512px固定)。
- **必要環境**: SD1.5ベースの4ネットワーク(controlnet/denoising_unet/point_net/reference_unet)。VRAM等は未測定。
- **制約**: 512px固定。背景が複雑な着色に弱いとColorizeDiffusionXL論文が指摘(競合著者)。点制御は任意。ライセンス不一致。
- **使う版・派生**: CoreML: VioletXF/manganinja-coreml(2026-09-26, 30日68DL)。デモ: spaces/fffiloni/MangaNinja-demo。
- **根拠**: [カードは`license: apache-2.0`のみで本文なし(重み4本: controlnet/denoising_unet/point_net/reference_unet)。詳細は公式GitHub/論文。](https://huggingface.co/Johanan0528/MangaNinjia/blob/4e6237c1d22415272bf98426616fe478cd3202a0/README.md) / [MangaNinja論文(参照付き線画着色、自作ベンチで既存手法より高い、自己報告)](https://arxiv.org/abs/2501.08332) / [重みの配置(本HFリポジトリ)とCC BY-NC 4.0バッジ、HFスペースdemo](https://github.com/ali-vilab/MangaNinjia/blob/6363c81aaedab0a435d18cba9209a7e842881ad7/README.md) / [ColorizeDiffusionXL論文のTable1(MangaNinja FID 42.85は512px, 自身8.28, 競合著者による比較)](https://arxiv.org/abs/2603.05971)
- **次点**: `tellurion/ColorizeDiffusionXL`（SDXL 1024px、2026-03。自己評価で50K-FID 8.28(MangaNinja 42.85)と最良だが、GitHub 8★/HF 0 likes、CC-BY-NC-SA-4.0で実績不足。今後の首位候補。） / `JunhaoZhuang/Cobra`（コミック頁向け、200枚超の参照、Apache-2.0、33 likes・253★。DL計測0、Cobra-Benchは自己評価。スケッチ様式依存と指摘(競合著者)。） / `thedeoxen/FLUX.2-klein-9B-manga-colorization-by-reference-LORA`（基盤FLUX.2-klein-base-9B(flux-non-commercial)のLoRA。累計4,965DL/56 likes、2026-06公開。評価ベンチなし。）

関連リポジトリ:

- [ali-vilab/MangaNinjia](https://github.com/ali-vilab/MangaNinjia) — MangaNinja公式(推論・デモ)（★742 / NOASSERTION / 最終push 2025-03-02 / 確認コミット [`6363c81a`](https://github.com/ali-vilab/MangaNinjia/blob/6363c81aaedab0a435d18cba9209a7e842881ad7/README.md) / 制作カタログ: [manganinjia](../../categories/manga.md#manganinjia)）
  - 742★、ライセンス表記なし(READMEはCC BY-NC 4.0バッジ)、最終push 2025-03-02。CVPR 2025 Highlight。
- [zhuang2002/Cobra](https://github.com/zhuang2002/Cobra) — Cobra公式(コミック向け多参照着色)（★253 / Apache-2.0 / 最終push 2026-08-15 / 確認コミット [`48d61688`](https://github.com/zhuang2002/Cobra/blob/48d6168838e05fbb707f393441219069aa33733b/README.md)）
  - 253★/Apache-2.0、pushed 2026-08-15。
- [tellurion-kanata/ColorizeDiffusionXL](https://github.com/tellurion-kanata/ColorizeDiffusionXL) — ColorizeDiffusion XL(1024px参照付きスケッチ着色)（★8 / NOASSERTION / 最終push 2026-04-09 / 確認コミット [`40db2f4e`](https://github.com/tellurion-kanata/ColorizeDiffusionXL/blob/40db2f4e1cec81e60551e2f76bf1b9cdf26584d8/README.md)）
  - 8★、pushed 2026-04-09。2026年論文の実装。採用はまだ小さい。

### 画像→画像(アニメ/漫画の線画・スケッチ抽出)

<a id="image-to-image--lineart-extraction"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [lllyasviel/Annotators](https://huggingface.co/lllyasviel/Annotators/tree/982e7edaec38759d914a963c48c4726685de7d96)（revision `982e7eda` / 作成 2023-03-14 / 更新 2023-08-27）
- **利用条件**: other。メタデータはother、カード本文なし。各重みの個別ライセンスは未確認(商用可と断定不可)。
- **選定根拠**: 【事実】lllyasviel/Annotators(401 likes, 25ファイル, 最終更新2023-08)はComfyUIのcontrolnet_aux(4,207★, Apache-2.0, 2026-09-28更新)が参照する重みの集積庫で、READMEの対応表: lineart_anime=netG.pth、manga_line=erika.pth(ノード名『Manga Lineart (aka lineart_anime_denoise)』)。別の抽出専用モデルとしては p1atdev/MangaLineExtraction-hf(MIT, 30日982DL/累計4,218, ljsabc/MangaLineExtraction_PyTorchの変換)、Mukosame/Anime2Sketch(2,130★, MIT)がある。定量ベンチはどれも無く、採用量(ComfyUIの定番カスタムノード(controlnet_aux)が採用)で判断。【評価】ControlNet前処理としてはAnnotators内のnetG/erikaが事実上標準。【未確認】netG.pthの出自(Anime2Sketch系か)はREADME上で断定できず。Annotatorsカードは実質空でライセンス明記なし(メタデータother)、HFのDL計測は0。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 401 / Spaces 100
- **概要**: ControlNet前処理モデルの集積庫。アニメ向け: netG.pth(lineart_anime, 写真/イラスト→アニメ調線画)、erika.pth(manga_line, 漫画線画抽出)。
- **入力**: アニメ・イラスト・漫画画像。
- **出力**: 線画(白地に黒線)画像。
- **必要環境**: controlnet_auxのLineartAnimeDetector/LineartMangaDetectorからfrom_pretrained()で取得。VRAM未測定。
- **制約**: リポジトリ自体は汎用(25ファイル中アニメ向けは一部)。2023年の重みで更新なし。出自・ライセンス不明瞭。
- **使う版・派生**: 抽出専用: p1atdev/MangaLineExtraction-hf(transformers形式, MIT)。ControlNet本体: lllyasviel/control_v11p_sd15s2_lineart_anime(30日4,816DL, SD1.5)、Eugeoter/noob-sdxl-controlnet-lineart_anime(30日7,418DL/累計143,030, NoobAI用)。Anima用はkohya-ss/Anima-LLLiteのlineart-1(Preview3世代)。
- **根拠**: [カード本文は空(23B)。ファイル一覧にnetG.pth(217MB), erika.pth(173MB), sk_model(2).pth, latest_net_G.pth等を確認。](https://huggingface.co/lllyasviel/Annotators/blob/982e7edaec38759d914a963c48c4726685de7d96/README.md) / [lineart_anime=lllyasviel/Annotators/netG.pth、manga_line=erika.pth という対応表](https://github.com/Fannovel16/comfyui_controlnet_aux/blob/0cd290477128d42cdc3e76a826a402d866e8c684/README.md) / [netG.pth/erika.pthの存在(アニメ線画・漫画線画抽出用)](https://huggingface.co/lllyasviel/Annotators/tree/main)
- **次点**: `p1atdev/MangaLineExtraction-hf`（漫画線画抽出のtransformers化(MIT, 30日982DL)。ComfyUIでの標準採用は確認できず。） / `Mukosame/Anime2Sketch`（スケッチ抽出の公式実装(2,130★, MIT, 2026-09更新)。重みの配布先がHFではなくGitHub/Drive系(本セッションでは未確認)。）

関連リポジトリ:

- [Fannovel16/comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) — ComfyUIの前処理ノード(AnimeLineArt/Manga Lineart)（★4,207 / Apache-2.0 / 最終push 2026-09-28 / 確認コミット [`0cd29047`](https://github.com/Fannovel16/comfyui_controlnet_aux/blob/0cd290477128d42cdc3e76a826a402d866e8c684/README.md)）
  - 4,207★/Apache-2.0、pushed 2026-09-28。lineart_anime/manga_lineの対応をREADMEで明示。
- [Mukosame/Anime2Sketch](https://github.com/Mukosame/Anime2Sketch) — アニメ/イラスト→スケッチ抽出の公式実装（★2,130 / MIT / 最終push 2026-09-08 / 確認コミット [`50a6a128`](https://github.com/Mukosame/Anime2Sketch/blob/50a6a128c5f66d3a25cf2a7aa67d1cb9669affd8/README.md)）
  - 2,130★/MIT、pushed 2026-09-08。
- [ljsabc/MangaLineExtraction_PyTorch](https://github.com/ljsabc/MangaLineExtraction_PyTorch) — 漫画線画抽出の元実装(erika.pth系との対応は推測)（★199 / MIT / 最終push 2025-01-10 / release v1 (2021-09-05) / 確認コミット [`6ec136d5`](https://github.com/ljsabc/MangaLineExtraction_PyTorch/blob/6ec136d5332180b65476e62c2558f2873d5d936a/README.md)）
  - 199★/MIT、最終push 2025-01。p1atdev版の元。

### 画像→画像(漫画・アニメの文字消し/インペイント)

<a id="image-to-image--inpainting"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [dreMaz/AnimeMangaInpainting](https://huggingface.co/dreMaz/AnimeMangaInpainting/tree/2953a4e935bf01ad1471f6cbfd26ab81abeeb92d)（revision `2953a4e9` / 作成 2023-11-10 / 更新 2023-11-10）
- **利用条件**: mit。HFメタデータはmit。カードにデータ由来・学習データ構成の記載なし(30万枚の出典不明)。コードはLaMa(Apache-2.0)由来。商用可否は学習データ不明のため断定しない。
- **選定根拠**: 【事実】dreMaz/AnimeMangaInpainting(lama_large_512px.ckpt, Big-LaMaを漫画・アニメ調30万枚でfine-tune, MIT)はcomic-translate(2,959★)が名指しで採用し、BallonsTranslator(5,171★)もfine-tune版lama(lama*)を搭載(dreMaz=BallonsTranslator作者dmMazeかは未確認)。30 likes/spaces 8、GitHubコード参照110件、HFのDL計測0(.ckpt)。Koharu(5,693★)は同系統のmayocream/lama-manga(安全なsafetensors変換, MIT, 30日407DL)とAOT GAN、さらにFLUX.2 Klein/RORem(生成型)を選択肢として提供。定量ベンチは無し(カードは『lama_mpeより大幅に良い』と主張のみ)。【評価】原本かつ主要翻訳ツール2本が採用しているためdreMaz版を首位。.ckptはpickleのため、安全性重視ならmayocream/lama-manga(safetensors)を使う。創造的なイラスト補完はAnima-LLLite inpainting-v2(Anima専用, 非商用)やWaifu-Inpaint-XL(基盤がNSFW特化のWAI-NSFW, 要判断)が別系統。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 30 / Spaces 8
- **概要**: マスク領域を埋めるLaMa(FFC)のアニメ・漫画特化fine-tune。漫画の吹き出し内文字消し・背景補完用。
- **入力**: 画像+二値マスク(512px系)。
- **出力**: マスク領域が補完された画像。
- **必要環境**: チェックポイント1ファイル(lama_large_512px.ckpt)。BallonsTranslator/comic-translateから読込。VRAM・速度は未測定。
- **制約**: 512px学習。ckptはpickle形式(読込時の安全性に注意)。ベンチなし。複雑な絵柄の大領域補完は不得手とみられる(未検証)。
- **使う版・派生**: safetensors変換: mayocream/lama-manga(MIT, Koharu同梱)。ONNX: ogkalu/lama-manga-onnx-dynamic、mayocream/lama-manga-onnx。AOT GAN: mayocream/aot-inpainting(30日919DL)。元ckpt: Sanster/models releasesのanime-manga-big-lama.pt。
- **根拠**: [BallonsTranslatorがlama*(fine-tune版lama)を選択肢に搭載(dreMaz版との同一性は未確認)](https://huggingface.co/dreMaz/AnimeMangaInpainting/blob/2953a4e935bf01ad1471f6cbfd26ab81abeeb92d/README.md) / [BallonsTranslatorがlama*(fine-tune版lama)を選択肢に搭載](https://github.com/dmMaze/BallonsTranslator/blob/9c7863c1e10c5bd927312eca0a0860177b0e5539/README.md) / [comic-translateがdreMaz/AnimeMangaInpainting(manga/anime fine-tune lama)を採用と記載](https://github.com/ogkalu2/comic-translate/blob/8977b91a4f7a40c3917c5a268e9e7d78e1d818da/README.md) / [KoharuのInpainting選択肢(LaMa=mayocream/lama-manga, AOT GAN, FLUX.2 Klein, RORem)](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md) / [同モデルのsafetensors変換(出典: Sanster anime-manga-big-lama.pt)](https://huggingface.co/mayocream/lama-manga/blob/f91c85b26913b3e83f9877867b4c336da3675238/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `black-forest-labs/FLUX.2-klein-9B` — Koharuが生成型インペイント候補に採用(FLUX.2 Klein)。アニメ特化ではなくflux-non-commercial。
- **次点**: `mayocream/lama-manga`（同モデルの安全なsafetensors変換(MIT, 30日407DL/累計503, 2026-07更新)。Koharuが採用。性能は同一で実質これを使うのが安全。原本ではないため次点。） / `kohya-ss/Anima-LLLite`（inpainting-v2(4ch RGB+mask)はAnima専用の生成型補完。非商用、ComfyUI実験ノード。文字消しでなく創作補完向け。） / `mayocream/aot-inpainting`（AOT GAN(Koharu搭載)、30日919DL。文字消しではLaMa系と比較未確認。）

関連リポジトリ:

- [dmMaze/BallonsTranslator](https://github.com/dmMaze/BallonsTranslator) — 漫画翻訳GUI(lama*/AOT/PatchMatchインペイント搭載)（★5,171 / GPL-3.0 / 最終push 2026-09-27 / release v1.5.17 (2026-09-27) / 確認コミット [`9c7863c1`](https://github.com/dmMaze/BallonsTranslator/blob/9c7863c1e10c5bd927312eca0a0860177b0e5539/README.md)）
  - 5,171★/GPL-3.0/v1.5.17(2026-09-27)。
- [koharu-rs/koharu](https://github.com/koharu-rs/koharu) — Rust製漫画翻訳(LaMa/AOT/FLUX.2 Klein/RORemを選択式で提供)（★5,693 / Apache-2.0 / 最終push 2026-09-30 / release 0.83.5 (2026-09-22) / 確認コミット [`45b4cae1`](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md)）
  - 5,693★/Apache-2.0/0.83.5(2026-09-22)。READMEが各インペイントモデルのHFリンクを列挙。
- [ogkalu2/comic-translate](https://github.com/ogkalu2/comic-translate) — 翻訳アプリ(AnimeMangaInpaintingのlamaを採用)（★2,959 / Apache-2.0 / 最終push 2026-09-11 / release v2.8.9 (2026-09-11) / 確認コミット [`8977b91a`](https://github.com/ogkalu2/comic-translate/blob/8977b91a4f7a40c3917c5a268e9e7d78e1d818da/README.md)）
  - 2,959★/Apache-2.0/v2.8.9(2026-09-11)。

### 画像→画像(写真→アニメ調スタイル変換)

<a id="image-to-image--photo-to-anime"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [autoweeb/Qwen-Image-Edit-2509-Photo-to-Anime](https://huggingface.co/autoweeb/Qwen-Image-Edit-2509-Photo-to-Anime/tree/2fdebf4e0c1ea04ef3037ff531bc5a4a3a842396)（revision `2fdebf4e` / 作成 2025-11-07 / 更新 2025-11-11）
- **利用条件**: mit。LoRA側はMIT。基盤Qwen/Qwen-Image-Edit-2509(Apache-2.0表記)のライセンスに従う。学習データはカード未記載。商用可と断定しない。
- **選定根拠**: 【事実】autoweeb/Qwen-Image-Edit-2509-Photo-to-Anime(Qwen-Image-Edit-2509用LoRA, MIT)は DL 30日55,981/累計1,309,813、likes 130、spaces 100(上限値の可能性)、GitHubコード参照31件。prithivMLmods/Qwen-Image-Edit-2511-Anime(Apache-2.0, 新しい2511基盤)は30日4,675/累計31,974/56 likes。定量ベンチはどちらも無し。古典GAN系 AnimeGANv3(TachibanaYoshino, 2,037★)は最終push 2025-08・重みGitHub配布で、拡散編集系に比べ採用の流れが薄い。【評価】採用量で autoweeb が圧倒(次点の約12倍)。『transform into anime』の一言で動き、Phr00t/Qwen-Image-Edit-Rapid-AIOとの併用が推奨される。【疑い】LoRAは商用サービス(AutoWeeb)向けに作られた宣伝色あり。品質は自己提示の例画像のみ。基盤は2025-09のEdit-2509で、2511/Qwen-Image-2.1世代への追随は未確認。
- **指標（確認日時点）**: DL累計 1,309,813 / 直近30日 55,981 / likes 130 / Spaces 100
- **概要**: Qwen-Image-Edit-2509向けLoRA。実写写真をアニメ画像へ変換する(AutoWeeb社製)。
- **入力**: 写真(高解像度が推奨)+プロンプト『transform into anime』。
- **出力**: アニメ調に変換された画像。
- **必要環境**: 基盤Qwen-Image-Edit-2509+LoRA(rank等はカード未記載)。ComfyUI workflow.json同梱。VRAM未測定。
- **制約**: 単純なプロンプトと高解像度写真で良好とのみ記載。ベンチなし。開発元のサービス宣伝あり。
- **使う版・派生**: LoRA: Qwen-Image-Edit-2509-Photo-to-Anime_000001000.safetensors。2511版: prithivMLmods/Qwen-Image-Edit-2511-Anime。Space: akhaliq/Qwen-Image-Edit-2509-Photo-to-Anime。
- **根拠**: [LoRAの概要(写真→アニメ)、推奨プロンプト『transform into anime』、ComfyUI workflow.json、Phr00t Rapid-AIO併用の推奨、ライセンスMIT。](https://huggingface.co/autoweeb/Qwen-Image-Edit-2509-Photo-to-Anime/blob/2fdebf4e0c1ea04ef3037ff531bc5a4a3a842396/README.md) / [2511基盤の代替LoRA(アニメ調フラットセル, 4step lightning併用)](https://huggingface.co/prithivMLmods/Qwen-Image-Edit-2511-Anime/blob/977f8c2ed22c8581c8750370bfce34058b253598/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `Qwen/Qwen-Image-Edit-2511` — LoRAなしでも『Transform into anime』程度の指示編集が可能な汎用編集モデル(Apache-2.0)。
- **次点**: `prithivMLmods/Qwen-Image-Edit-2511-Anime`（新しい2511基盤・Apache-2.0。ただし30日4,675DL/累計31,974と採用は1/40以下。ベンチなし。） / `TachibanaYoshino/AnimeGANv3`（GAN系の軽量変換。2,037★だが最終push 2025-08、重みはGitHub配布。拡散編集系との品質比較は未検証。）

関連リポジトリ:

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) — Qwen-Image-Edit LoRAの実行基盤(READMEがQwen Image Edit対応を明記)（★135,624 / GPL-3.0 / 最終push 2026-09-30 / release v0.38.0 (2026-09-29) / 確認コミット [`83071e1a`](https://github.com/Comfy-Org/ComfyUI/blob/83071e1aec311d31e773d64d6872181b3bad0fe2/README.md) / 制作カタログ: [comfyui](../../categories/workflow.md#comfyui)）
  - 135,621★/GPL-3.0/v0.38.0。
- [QwenLM/Qwen-Image](https://github.com/QwenLM/Qwen-Image) — Qwen-Image/Edit-2511の公式実装（★8,385 / Apache-2.0 / 最終push 2026-02-10 / 確認コミット [`6b5e1f5c`](https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/README.md) / 制作カタログ: [qwen-image](../../categories/image.md#qwen-image)）
  - 8,385★/Apache-2.0、pushed 2026-02-10。
- [TachibanaYoshino/AnimeGANv3](https://github.com/TachibanaYoshino/AnimeGANv3) — GAN系写真→アニメ変換(旧来手法)（★2,037 / ライセンス未表示 / 最終push 2025-08-23 / release v1.1.0 (2023-11-23) / 確認コミット [`73ada391`](https://github.com/TachibanaYoshino/AnimeGANv3/blob/73ada3910dafa87b4cc972bcd80ebfebce9f3abe/README.md)）
  - 2,037★、ライセンス表記なし、pushed 2025-08-23。

### 画像→画像(ポーズ/線画/深度などのControlNet条件付け)

<a id="image-to-image--controlnet-conditioning"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [kohya-ss/Anima-LLLite](https://huggingface.co/kohya-ss/Anima-LLLite/tree/36ba7f2f498a1ca63cc77fc7a1298652f72d4524)（revision `36ba7f2f` / 作成 2026-04-27 / 更新 2026-08-02）
- **利用条件**: other/circlestone-labs-non-commercial-license。HFメタデータはother/circlestone-labs-non-commercial-license(Anima本体と同じ非商用)。リポジトリ内にLICENSEあり。商用可と断定しない。Sen-sou版はApache-2.0表記だが基盤Animaは非商用。
- **選定根拠**: 【事実】kohya-ss/Anima-LLLite(Anima用ControlNet-LLLite, 233 likes, spaces 16, 最終更新2026-08-02)はsd-scriptsの公式学習スクリプトで作られ、Anima-Base v1.0向けに any-test-like-v2(線画/スケッチ/グレースケール混合)とinpainting-v2を提供。lineart/depth/pose/scribbleはPreview3世代(Base v1.0でも品質低下つきで動作、討議8で再学習要望)。ComfyUI公式再配布 Comfy-Org/Anima-LLLite は30日43,471DL/累計89,945(原本リポジトリはDL計測0)でワークフローテンプレートあり。Forge Neo(1,772★)も対応。定量ベンチなし(サンプル画像のみ)。【評価】AnimaのControlNet相当としては作者本人(kohya)製で代替が実質なし→首位。【疑い】討議6『OpenPoseがlineart/scribble扱いになる』、討議10『品質が悪い』の報告あり。Sen-sou/Anima-LLLite-Regional-Controlnet(49 likes, Apache-2.0, 実験的な領域指定)、Temp1k/Anima-Control-Pose(Preview-2, 0 likes, 作者自身が未完成と注記)は未成熟。SDXL系(Illustrious/NoobAI)ではEugeoter/noob-sdxl-controlnet-lineart_anime(30日7,418DL/累計143,030)などの資産が厚く、ControlNetの成熟度はSDXL側が上。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 233 / Spaces 16
- **概要**: AnimaのDiTに対するLoRA型の軽量ControlNet(LLLite)。any-test-like(線画・スケッチ条件)、inpainting(RGB+マスク4ch)、旧世代のlineart/depth/pose/scribble。
- **入力**: 条件画像(線画・スケッチ等)またはRGB+マスク、プロンプト。
- **出力**: 条件に沿ったAnima生成画像。
- **必要環境**: Anima-Base v1.0+Qwen3-0.6B+Qwen-Image VAE。ComfyUIのmodel_patchesフォルダに配置。学習はRTX PRO 6000 Blackwellで実施とカード記載、推論VRAMは未測定。
- **制約**: サンプル重みで実験的。lineart/depth/pose/scribbleはPreview3世代で品質低下。OpenPoseの誤解釈報告あり。
- **使う版・派生**: ComfyUI再配布: Comfy-Org/Anima-LLLite(model_patches/に10ファイル)。領域指定: Sen-sou/Anima-LLLite-Regional-Controlnet。ポーズ: Temp1k/Anima-Control-Pose(Preview-2)。
- **根拠**: [Anima-Base v1.0向けサンプル重み(any-test-like-v2, inpainting-v2)、Preview3世代のlineart/depth/pose/scribbleの扱い、学習データ(Animaで生成した4,000枚)、ComfyUI実験ノードへのリンク。](https://huggingface.co/kohya-ss/Anima-LLLite/blob/36ba7f2f498a1ca63cc77fc7a1298652f72d4524/README.md) / [ComfyUI用再配布(30日43,471DL)とワークフロー(Any Control/Depth/Inpainting)](https://huggingface.co/Comfy-Org/Anima-LLLite/blob/57973aa5c824df58d9f8217b031f96a148f9b349/README.md) / [OpenPose入力がLineart/Scribble扱いになる報告](https://huggingface.co/kohya-ss/Anima-LLLite/discussions/6) / [Anima LLLite学習スクリプト対応の明記](https://github.com/kohya-ss/sd-scripts/blob/690ea7f96c23182352ec63def76d431c6120bd2f/README.md)
- **次点**: `Sen-sou/Anima-LLLite-Regional-Controlnet`（領域カラーマスクで多人数配置。Apache-2.0表記、49 likes、DL計測0、実験的。kohya版の拡張で単独の代替ではない。） / `Temp1k/Anima-Control-Pose`（Anima v1.0向けネイティブ・ポーズ制御(Preview-2, 2026-09-28公開)。作者自身が手指崩れなど未完成と注記、0 likes。）

関連リポジトリ:

- [kohya-ss/ComfyUI-Anima-LLLite](https://github.com/kohya-ss/ComfyUI-Anima-LLLite) — Anima-LLLiteのComfyUIノード(実験的)（★215 / Apache-2.0 / 最終push 2026-08-02 / 確認コミット [`b7495bd8`](https://github.com/kohya-ss/ComfyUI-Anima-LLLite/blob/b7495bd8eb876e334509976896702484ed19cdbb/README.md)）
  - 215★/Apache-2.0、pushed 2026-08-02。
- [kohya-ss/sd-scripts](https://github.com/kohya-ss/sd-scripts) — LLLite学習スクリプト(anima_train_control_net_lllite.py)（★7,242 / Apache-2.0 / 最終push 2026-09-24 / release v0.12.0 (2026-09-24) / 確認コミット [`690ea7f9`](https://github.com/kohya-ss/sd-scripts/blob/690ea7f96c23182352ec63def76d431c6120bd2f/README.md) / 制作カタログ: [sd-scripts](../../categories/workflow.md#sd-scripts)）
  - 7,242★/Apache-2.0/v0.12.0。READMEがAnima LLLite学習を記載。
- [Haoming02/sd-webui-forge-classic](https://github.com/Haoming02/sd-webui-forge-classic) — Forge Neo: Anima-LLLite・Regional Controlnetを対応（★1,772 / AGPL-3.0 / 最終push 2026-09-30 / release 2.29.1 (2026-09-21) / 確認コミット [`0b1783c7`](https://github.com/Haoming02/sd-webui-forge-classic/blob/0b1783c79b397e73818c3d8432b25cc3cbb5ca50/README.md)）
  - 1,772★/AGPL-3.0、READMEにAnima-LLLiteリンク。

### 画像+テキスト→画像(アニメ画像の指示編集)

<a id="image-text-to-image"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1/tree/d26bb61231c349cf6b7896fa83353113880e1ba3)（revision `d26bb612` / 作成 2026-09-14 / 更新 2026-09-30）
- **利用条件**: other/qwen-research。Qwen RESEARCH LICENSE AGREEMENT(2026-09-20): 非商用・研究/評価のみ。商用は別途ライセンス要。学習/改良したモデルの公開時『Built with Qwen』表示義務。HFメタデータはother。商用利用不可として扱う。
- **選定根拠**: 【事実】HFのimage-text-to-imageタグで検索したアニメ系は実質RunningHubAI系の新着(0 likes)のみ。アニメ専用の編集基盤モデルは見つからず、Forge Neoが対応する『Anima Edit』はCivitAI上のLoRA(HF不在, 未検証)。汎用の最有力は Qwen/Qwen-Image-2.1(2026-09-14公開, T2I+編集統合7B, likes 2,706, 30日70,687DL, 10参照画像・マスク/丸囲み編集)。X: javawock7618(2026-09-22, 1,158 likes)『編集=Qwen-Image 2.1』、sep_is_heim(2026-09-22)三面図でキャラLoRA代替を検証、ai_hakase_(2026-09-25)が修正用途で紹介。一方 PSueoka55133(2026-09-24)はT2Iのイラストはさほどでもないが編集能力は高いと評価。ライセンスはQwen RESEARCH LICENSE(非商用, 2026-09-20)。商用・安全側なら Qwen/Qwen-Image-Edit-2511(Apache-2.0, 30日292,995DL/累計1,914,682, likes 1,432)。anime LoRA(photo-to-anime等)は2509/2511基盤が主流で2.1用は新規。【評価】アニメ専用評価ベンチは無く、Xの評判と採用で暫定首位。信頼度低(公開2週間、個別の定量比較なし)。
- **指標（確認日時点）**: DL累計 70,687 / 直近30日 70,687 / likes 2,706 / Spaces 100
- **概要**: Qwenの統合T2I/画像編集モデル(汎用)。アニメ特化ではないが、アニメ画像の指示編集で最も多く言及される最新モデル。
- **入力**: 画像(最大10枚)+編集指示、任意でマスク/丸囲み/ペイント注釈。
- **出力**: 編集後画像(RGBA透過も可)。
- **必要環境**: diffusers(QwenImage21Pipeline, transformers>=5.17)。VRAM要件はカード確認範囲では不明(未測定)。Xでは12GB VRAM動作の報告(派生)。
- **制約**: 研究ライセンス(非商用)。アニメ絵のT2Iが平凡との評価も。公開直後で実績が浅い。
- **使う版・派生**: 編集指示書き換え用: Qwen/Qwen-Image-2.1-PE-I2I(30日10,325DL)。旧世代: Qwen/Qwen-Image-Edit-2511(Apache-2.0), Qwen-Image-Edit-2509。アダルト特化の派生(Noct-Q等)は対象外。
- **根拠**: [T2I+編集統合(視覚生成部7B・32層Single-Stream DiT)。透明度(RGBA)生成、最大10参照画像、丸囲み/ペイント/マスク指定編集。ライセンスLICENSE同梱。](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/d26bb61231c349cf6b7896fa83353113880e1ba3/README.md) / [Qwen RESEARCH LICENSE(非商用のみ, 商用は別契約, 派生モデル公開時『Built with Qwen』表示)](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/d26bb61231c349cf6b7896fa83353113880e1ba3/LICENSE) / [2026-09-22: 編集=Qwen-Image 2.1(1,158 likes)](https://x.com/javawock7618/status/2102314466444775605) / [2026-09-24: T2Iイラストは平凡だが編集能力は高いとの評価](https://x.com/PSueoka55133/status/2102935008399044779)
- **次点**: `Qwen/Qwen-Image-Edit-2511`（Apache-2.0、30日292,995DL/累計1,914,682/1,432 likes、アニメ向けLoRA資産が最多(autoweeb等)。2.1との直接比較は未確認。ライセンス重視ならこちらが本命。） / `black-forest-labs/FLUX.2-klein-9B`（30日190,875DL/1,585 likes、Koharuがインペイントに採用。flux-non-commercial。アニメ用LoRAは漫画着色等(thedeoxen)が少数。） / `circlestone-labs/Anima`（編集モデルではない。Anima Edit(CivitAI LoRA)は未検証。Anima-LLLiteのinpainting-v2が最も近い公式資産。）

関連リポジトリ:

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) — 編集モデルの実行基盤(READMEがQwen Image Edit・Flux.2 Klein編集等を対応と記載)（★135,624 / GPL-3.0 / 最終push 2026-09-30 / release v0.38.0 (2026-09-29) / 確認コミット [`83071e1a`](https://github.com/Comfy-Org/ComfyUI/blob/83071e1aec311d31e773d64d6872181b3bad0fe2/README.md) / 制作カタログ: [comfyui](../../categories/workflow.md#comfyui)）
  - 135,621★/GPL-3.0/v0.38.0。
- [QwenLM/Qwen-Image-2.1](https://github.com/QwenLM/Qwen-Image-2.1) — Qwen-Image-2.1公式実装（★1,652 / NOASSERTION / 最終push 2026-09-30 / 確認コミット [`6627d87c`](https://github.com/QwenLM/Qwen-Image-2.1/blob/6627d87c6433151463ec4b48b8945a24fcf16a35/README.md)）
  - 1,651★、ライセンス表記なし(NOASSERTION)、pushed 2026-09-30。
- [Haoming02/sd-webui-forge-classic](https://github.com/Haoming02/sd-webui-forge-classic) — Forge Neo: Qwen-Image-Edit・Anima Edit(要LoRA)対応（★1,772 / AGPL-3.0 / 最終push 2026-09-30 / release 2.29.1 (2026-09-21) / 確認コミット [`0b1783c7`](https://github.com/Haoming02/sd-webui-forge-classic/blob/0b1783c79b397e73818c3d8432b25cc3cbb5ca50/README.md)）
  - 1,772★/AGPL-3.0。

### 無条件画像生成(アニメ顔/全身GAN・拡散)

<a id="unconditional-image-generation"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [skytnt/fbanime-gan](https://huggingface.co/skytnt/fbanime-gan/tree/79c6af6b789fb18533eb9885fc21680ee29d235e)（revision `79c6af6b` / 作成 2022-08-10 / 更新 2022-12-12）
- **利用条件**: apache-2.0。メタデータはapache-2.0。学習データ(fbanimehq: アニメ全身画像)の権利・出典は未確認で商用可と断定不可。NVIDIA StyleGAN3コードのライセンスもNOASSERTION。
- **選定根拠**: 【事実】HFのunconditional-image-generationタグでアニメ関連は、チュートリアル規模のDDPM(64px, 30日10〜130DL: LittleNyima/ddpm-anime-faces-64, xchuan/ddpm-fewshot_anime_face等)と、2022年のGAN(skytnt/fbanime-gan 9 likes/spaces 4、huggan/stylegan_animeface512 3 likes)のみ。skytnt/fbanime-gan(StyleGAN2, 非正方形対応, 全身アニメ, 学習データ fbanimehq v2.0, カード記載FID 1.4=自己報告)が実用に最も近く、ONNX(mapping/synthesis/encoder)とe4e系エンコーダ付き。DL計測0、最終更新2022-12、GitHub SkyTNT/fbanimegan 5★(2022-11)。【評価】本タスクに現行の勝者は無い。現在の実務では無条件サンプリングの代わりにAnima等のテキスト→画像で乱数プロンプト生成を使うのが主流。fbanime-ganは潜在空間編集/エンコーダ用途の保守的な選択肢に限る。ライセンスはApache-2.0表記だがデータセット(fbanimehq)の権利は未確認。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 9 / Spaces 4
- **概要**: 全身アニメ画像を生成するStyleGAN2。非正方形解像度対応、e4eエンコーダ(ONNX)付き。
- **入力**: 潜在ベクトル(またはエンコーダ経由で画像)。
- **出力**: 全身アニメ画像。
- **必要環境**: カード記載: fbanime.pkl(fp16はGPUのみ)、fbanime_fp32.pkl(GPU/CPU)、ONNX版。VRAM未測定。
- **制約**: 2022年のモデルで解像度・品質は現行T2Iに遠く及ばない。更新なし。条件制御なし。
- **使う版・派生**: fbanime.pkl(fp16), fbanime_fp32.pkl, g_mapping.onnx, g_synthesis.onnx, encoder.onnx, waifu_dect.onnx。顔用: huggan/stylegan_animeface512。
- **根拠**: [StyleGAN2(StyleGAN3コード改変)で学習、FID 1.4(カード記載・自己報告)、ONNX(g_mapping/g_synthesis/encoder/waifu_dect)、データセットfbanimehq v2.0。](https://huggingface.co/skytnt/fbanime-gan/blob/79c6af6b789fb18533eb9885fc21680ee29d235e/README.md) / [学習データfbanimehq(権利関係は未確認)](https://huggingface.co/datasets/skytnt/fbanimehq)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `circlestone-labs/Anima` — 無条件生成の代替として、乱数プロンプトのT2Iで多様なアニメ画像を量産するのが実務的(非商用ライセンス)。
- **次点**: `huggan/stylegan_animeface512`（アニメ顔512px StyleGAN(2022-04)。3 likes、DL計測0。全身ではなく顔のみ、更新停止。） / `LittleNyima/ddpm-anime-faces-64`（64px DDPM(2024-06)で30日102DL。学習用チュートリアル規模で実用画質ではない。）

関連リポジトリ:

- [SkyTNT/fbanimegan](https://github.com/SkyTNT/fbanimegan) — fbanime-ganの学習コード(StyleGAN2改変)（★5 / Apache-2.0 / 最終push 2022-11-21 / 確認コミット [`636c128b`](https://github.com/SkyTNT/fbanimegan/blob/636c128bbeed5095af84ef524cbb1b7db1175bfb/README.md)）
  - 5★/Apache-2.0、pushed 2022-11-21。
- [NVlabs/stylegan3](https://github.com/NVlabs/stylegan3) — StyleGAN2/3公式実装(fbanimeの学習基盤)（★6,948 / NOASSERTION / 最終push 2023-09-12 / 確認コミット [`c233a919`](https://github.com/NVlabs/stylegan3/blob/c233a919a6faee6e36a316ddd4eddababad1adf9/README.md)）
  - 6,948★、ライセンス表記NOASSERTION、最終push 2023-09-12(アーカイブ状態ではない)。
