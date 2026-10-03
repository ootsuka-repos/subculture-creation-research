# 3D・アバター・その他のアニメ系SOTA（2026-10-01）

[一覧へ](../anime-task-sota.md) · [リポジトリ全体像](../anime-repositories.md) · [正本JSON](../../sota-catalog.json)

選定基準・注意は[一覧ページ](../anime-task-sota.md)。各項目の「最良」は確度付きの編集判断で、重み取得・推論実行は未実施。

### アニメイラストの2.5Dレイヤ分解(Live2D/PSD向け)

<a id="live2d-layer-decomposition"></a>
- **判定**: アニメ特化の最良 / 確度 高
- **最良**: [layerdifforg/seethroughv0.0.2_layerdiff3d](https://huggingface.co/layerdifforg/seethroughv0.0.2_layerdiff3d/tree/4477e6ce529bc6a141732e1a55a4932176db3b89)（revision `4477e6ce` / 作成 2026-03-09 / 更新 2026-09-28）
- **利用条件**: openrail++。メタデータは openrail++。カード本文: 自作部分はApache-2.0、ただしAnimagine XL 4.0/SDXL(CreativeML Open RAIL++-M)・LayerDiffuse(Open RAIL-M)・SDXL-VAE-FP16-Fix(MIT)のライセンスを継承し、Open RAILの使用制限(para.5・Attachment A)が全利用に及ぶ。『商用利用は許可』とカードは書くが、配布・サービス提供時は制限条項の転記義務あり。論文本文は CC BY-NC-SA 4.0 表記(arXiv HTML)。学習データは商用Live2Dモデルのレイヤから生成したと論文が記述しており、データ権利の扱いは未確認。コード(GitHub)はApache-2.0。
- **選定根拠**: 【事実】アニメ専用・単一画像→最大23意味レイヤ(補完済み)+描画順→PSD。SIGGRAPH 2026論文。自己報告(論文・自作2.5Dテストセット): Ours Full LPIPS 0.1549/PSNR 18.30/SSIM 0.923/Mask Dice 0.3855/FID 18.37、ベースラインSAM+LaMa LPIPS 0.2880/PSNR 12.28/FID 81.14。Qwen-Image-Layeredとは定性比較のみで数値比較なし。採用指標: HF 30日DL 19,507/累計88,354/likes 27/spaces 17、GitHub ★4,189(Apache-2.0)、コード参照92件、Xで2026-03〜09に2,638/2,213/1,088/831 likes級の実使用報告(ComfyUI・WebUI・PSD→Live2D/2.5Dリグ連携)。【評価】アニメ向けレイヤ分解ではOSSの事実上の標準で対抗馬なし。【疑い】Live2Dリグまでは自動化されない(公式が明言)、学習データが商用Live2Dモデル由来でデータ権利は不明、ライセンスはOpenRAIL制限継承。
- **指標（確認日時点）**: DL累計 90,402 / 直近30日 19,705 / likes 27 / Spaces 17
- **概要**: アニメ・イラスト1枚を、髪・顔・目・服などの意味パーツ(最大23レイヤ)に分解し、隠れ部分を補完した透過レイヤと描画順を出力する See-through パイプラインの LayerDiff 3D(SDXL系、Animagine XL 4.0派生)。深度モデル(Marigold派生)と併用して PSD を出力する。
- **入力**: アニメ調キャラクター1枚絵(GitHub READMEの例は1280解像度)
- **出力**: 意味パーツ別の補完済み透過レイヤ、擬似深度による描画順、レイヤ付きPSD(パイプライン全体の出力。GitHub README記載)
- **必要環境**: モデルカードに要件記載なし。GitHub README: bf16・1280解像度で約12〜16GB VRAM、group offloadで約10GB、NF4で約8GB。いずれもREADME記載値で未測定。
- **制約**: 公式READMEが『Image-to-Live2Dではない』と明記(変形メッシュ・物理・リギングは対象外、Live2D用のレイヤ分割とは設計判断が異なる)。頭部と胴体は2段階処理で遅い。READMEはV3(23レイヤ)を最新とし、HFカード(v0.0.2)は『new tag definition』と記載するのみで、v0.0.2とV3の対応関係はカード上明示なし[INFERENCE: 同一重みを指す]。
- **使う版・派生**: 本体: layerdifforg/seethroughv0.0.2_layerdiff3d(v0.0.1は旧タグ定義)。必須の併用モデル: layerdifforg/seethroughv0.0.1_marigold(30日DL 17,530/累計71,920、深度)。低VRAM版: 24yearsold/seethroughv0.0.2_layerdiff3d_nf4(30日DL 7,810)・24yearsold/seethroughv0.0.1_marigold_nf4、GGUF再配布: icefog72/seethroughv0.0.2_layerdiff3d_gguf(30日DL 485、第三者)。デモSpace: 24yearsold/see-through-demo(ZeroGPU)。
- **根拠**: [LayerDiff 3D のカード。ライセンス節(Apache-2.0自作部分+OpenRAIL継承)、NF4版リンク、論文引用](https://huggingface.co/layerdifforg/seethroughv0.0.2_layerdiff3d/blob/4477e6ce529bc6a141732e1a55a4932176db3b89/README.md) / [論文(2026-02-03): 商用Live2Dモデルから教師データを生成、Body Part Consistency Module、擬似深度による描画順](https://arxiv.org/abs/2602.03749) / [GitHub README: 23レイヤPSD出力、VRAM目安、ComfyUI/StretchyStudio/Anime2.5DRig等の派生列挙、『Image-to-Live2Dではない』議論](https://github.com/shitagaki-lab/see-through/blob/main/README.md) / [X(2026-04-05, 2,638 likes): WebUI化の拡散](https://x.com/BeamManP/status/2040610228371329033) / [X(2026-04-01, 2,213 likes): ComfyUI+RTX5090で1280px約2分、Live2D化まで15〜20分との実使用報告](https://x.com/8co28/status/2039267460327887219)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `Qwen/Qwen-Image-Layered` — 汎用のテキスト指定レイヤ分解。背景・オブジェクト層の分離向きで、キャラの意味パーツ分解には See-through が適する(収録外)
- **次点**: `Qwen/Qwen-Image-Layered`（汎用(likes 1,168)。レイヤ意味は単一テキストプロンプトで指定し、パーツ意味・描画順を出さない(See-through論文の比較記述)。アニメ専用評価なし）

関連リポジトリ:

- [shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through) — 公式実装・学習スクリプト・PSD出力パイプライン（★4,290 / Apache-2.0 / 最終push 2026-09-24 / 確認コミット [`a25a5498`](https://github.com/shitagaki-lab/see-through/blob/a25a5498e031dc7fe01232d05dadaf67736277fb/README.md) / 制作カタログ: [see-through](../../categories/layer.md#see-through)）
  - ★4,189、Apache-2.0、最終push 2026-09-24。SIGGRAPH 2026論文の公式実装で、学習コード/データパイプラインは2026-04-14公開(READMEのChangelog)。リリースタグなし。
- [jtydhr88/ComfyUI-See-through](https://github.com/jtydhr88/ComfyUI-See-through) — ComfyUIノード(PSD出力、ネイティブレイヤエディタ対応)（★816 / ライセンス未表示 / 最終push 2026-08-20 / 確認コミット [`98d754bf`](https://github.com/jtydhr88/ComfyUI-See-through/blob/98d754bf04f668647919ab750eccb0e0640faa81/README.md) / 制作カタログ: [comfyui-see-through](../../categories/layer.md#comfyui-see-through)）
  - ★814、最終push 2026-08-20。公式READMEが推奨派生として掲載、Xでも753/355 likesの告知。ライセンス未設定(GitHub上null)のため再利用条件は要確認。
- [MangoLion/stretchystudio](https://github.com/MangoLion/stretchystudio) — See-through PSDを自動リグするブラウザ2Dパペット工具（★496 / MIT / 最終push 2026-04-28 / 確認コミット [`24a83a27`](https://github.com/MangoLion/stretchystudio/blob/24a83a27ba43e43e9d2e3de5e33994594e6199c2/README.md) / 制作カタログ: [stretchystudio](../../categories/rig2d.md#stretchystudio)）
  - ★494、MIT、最終push 2026-04-28。公式READMEが『PSD出力をドロップするだけで動く』派生として掲載。
- [852wa/Anime2.5DRig](https://github.com/852wa/Anime2.5DRig) — レイヤPSD→2.5D VTuber風アバター(瞬き・リップシンク・髪物理)のブラウザ工具（★234 / MIT / 最終push 2026-09-23 / 確認コミット [`7ddbd994`](https://github.com/852wa/Anime2.5DRig/blob/7ddbd9943ea3152561b3dc8348fd752c850f3e95/README.md) / 制作カタログ: [anime2.5drig](../../categories/rig2d.md#anime2.5drig)）
  - ★231、MIT、最終push 2026-09-23。公式READMEが派生として掲載(レイヤ命名がSee-through準拠)。

### 画像から3D(アニメキャラ単体のメッシュ生成)

<a id="image-to-3d--anime-character-mesh"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [hyz317/StdGEN](https://huggingface.co/hyz317/StdGEN/tree/8d12f6e3e279a2aac9bb957236c1e8e3c13549c0)（revision `8d12f6e3` / 作成 2025-03-04 / 更新 2025-03-12）
- **利用条件**: apache-2.0。メタデータは apache-2.0 だが、GitHub Disclaimer は『公開チェックポイントは研究目的』と記載(矛盾あり→研究用途として扱う)。推論コードは InstantMesh/Unique3D/Era3D/CharacterGen 由来部分を含む(各ライセンス要確認)。学習データの VRoid Hub モデルは『ポリシー上、生VRMは再配布不可』とREADMEが述べ、Anime3D++ の権利は制約あり。商用可とは断定しない。
- **選定根拠**: 【事実】アニメ専用(VRoid Hub 10,811体で学習)のオープン重みは StdGEN(CVPR 2025)と CharacterGen(SIGGRAPH'24)が実質2本。StdGEN論文Table 1(自己報告、自作Anime3D++テスト)で、A-pose入力 SSIM 0.937/LPIPS 0.066 に対し CharacterGen 0.880/0.124、任意ポーズでも 0.916/0.084 対 0.869/0.134 と上回り、体・服・髪に分解した出力も持つため選定。【採用の弱さ】HF DLは両者とも0(集計対象外で判定不能)、likes 16(StdGEN)対25(CharacterGen)、GitHub ★395対★835、コード参照21対28と利用は小さい。X検索(StdGEN/CharacterGen/UniRig等×anime/VRM)で実使用報告は見つからず、日本語圏の実務はTripo・Meshy・Hi3D等のクローズドサービスとOSS汎用のTRELLIS.2(Krea経由)が中心(X 2026-07〜09)。【評価】アニメ専用OSSでは最有力だが、実用品質は未検証でconfidence=low。ライセンスは『研究目的』注記あり。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 16 / Spaces 5
- **概要**: アニメキャラ1枚絵から、体・服・髪などに意味分解された3Dキャラクターを約3分で生成する CVPR 2025 のパイプライン。A-pose化(canonicalize)→多視点画像(multiview)→Semantic-aware LRM(S-LRM)→多層リファイン。VRoid Hub 由来の Anime3D++ で学習。
- **入力**: 全身のキャラクター画像(READMEは半身入力で品質低下と注記)
- **出力**: 意味分解された3Dキャラクターメッシュ(body/clothes/hair等)。分解なし出力も可
- **必要環境**: モデルカードに要件記載なし。GitHub README: Python 3.9、torch 2.1.0(cu118)、xformers 0.0.22、torch-scatter、ViT-H SAM重みが別途必要、`--low_vram` オプションあり。VRAM量は記載なし・未測定。
- **制約**: 学習データが全身像のため半身入力に弱い(README)。2.5D・実写風では背景除去(rm_anime_bg)が効きにくい(README)。生成後のリギング・VRM化は別工程。HF DLは0(重みがカスタム構成で未集計、利用実績は判定不能)。Xでの実使用報告は今回の検索で見つからず。
- **使う版・派生**: HF内に3モデル同梱: StdGEN-canonicalize-1024、StdGEN-multiview-1024、StdGEN-mesh-slrm(カード記載、合計48ファイル)。量子化・ONNX派生は未確認。デモSpaceあり(spaces 5)。
- **根拠**: [モデルカード: 3モデル構成(canonicalize/multiview/S-LRM)、論文・CVPR 2025](https://huggingface.co/hyz317/StdGEN/blob/8d12f6e3e279a2aac9bb957236c1e8e3c13549c0/README.md) / [GitHub README: 推論手順、Anime3D++データセット(VRoid由来、再配布不可)、Disclaimer(研究目的)、半身入力の注意](https://github.com/hyz317/StdGEN/blob/main/README.md) / [論文: Anime3D++(VRoid-Hub約14,000体→10,811体に選別)。Table 1(A-pose入力): StdGEN SSIM 0.937/LPIPS 0.066/FID 0.010/CLIP 0.941 vs CharacterGen 0.880/0.124/0.081/0.905、Unique3D 0.889/0.136/0.030/0.919、InstantMesh 0.888/0.126/0.107/0.906(自己報告・自作Anime3D++テスト)](https://arxiv.org/abs/2411.05738)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `microsoft/TRELLIS.2-4B` — 汎用image-to-3Dの実質標準(HF likes 1,266、30日DL 1.66M規模)。アニメ専用ではないが、日本語圏の実務でもイラスト→3Dに使われている(X 2026-09)。アニメの顔・髪の忠実度は未検証(収録外)
- **次点**: `zjpshadow/CharacterGen`（先行作(2024)。GitHub ★835・likes 25で知名度は上だが、StdGEN論文比較で全指標劣後(自己報告)、意味分解なし、最終push 2025-04-11） / `VAST-AI/AniGen`（リグ付き3D一括生成(2026-04、MIT表記)。ただしアニメ専用ではなく汎用アセット向け、GitHubライセンスNOASSERTION、18GB以上のGPU要）

関連リポジトリ:

- [hyz317/StdGEN](https://github.com/hyz317/StdGEN) — 公式実装(canonicalize→multiview→S-LRM→refine)とAnime3D++レンダリング手順（★396 / Apache-2.0 / 最終push 2026-04-17 / 確認コミット [`f1b0c822`](https://github.com/hyz317/StdGEN/blob/f1b0c822689dc2539c774bb73090a67c66e2e766/README.md)）
  - ★395、Apache-2.0、最終push 2026-04-17。CVPR 2025公式。リリースタグなし。
- [zjp-shadow/CharacterGen](https://github.com/zjp-shadow/CharacterGen) — 前世代のアニメキャラ3D生成(VRMレンダリングスクリプト同梱)（★835 / Apache-2.0 / 最終push 2025-04-11 / 確認コミット [`f329a835`](https://github.com/zjp-shadow/CharacterGen/blob/f329a835dbd5003060a5653eafd83d4d8868b043/README.md)）
  - ★835、Apache-2.0、最終push 2025-04-11。Blender/three-vrm用VRMレンダリングスクリプトを公開(READMEのAnime3Dデータ準備手順)。更新は停滞。
- [VAST-AI-Research/AniGen](https://github.com/VAST-AI-Research/AniGen) — リグ付き3Dアセットを1枚から生成(汎用)（★509 / NOASSERTION / 最終push 2026-07-15 / 確認コミット [`c49db3d6`](https://github.com/VAST-AI-Research/AniGen/blob/c49db3d6b466537a02ccf2286688903d77af7e4f/README.md) / 制作カタログ: [anigen](../../categories/3d.md#anigen)）
  - ★506、最終push 2026-07-15。SIGGRAPH 2026。汎用でありアニメ専用ではない。GitHubライセンスはNOASSERTION、HF側はMIT表記で不一致。
- [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) — 汎用image-to-3d(実務の比較基準)（★11,445 / MIT / 最終push 2026-07-10 / 確認コミット [`75fbf018`](https://github.com/microsoft/TRELLIS.2/blob/75fbf0183001ed9876c8dbb35de6b68552ee08bd/README.md) / 制作カタログ: [trellis.2](../../categories/3d.md#trellis.2)）
  - ★11,411、MIT、最終push 2026-07-10。アニメ専用ではないが日本語圏の実例が多い。

### アニメ3Dキャラの自動リギング(骨格・スキニング)

<a id="anime-3d-rigging"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [VAST-AI/SkinTokens](https://huggingface.co/VAST-AI/SkinTokens/tree/79736cad0fd84de384d5eede659b4ebd24effe33)（revision `79736cad` / 作成 2026-04-20 / 更新 2026-04-20）
- **利用条件**: mit。メタデータ・GitHubともMIT。ただし学習データに VRoid Hub モデルや ModelsResource(ゲーム由来アセット)を含み、個別モデルの権利は未確認。商用可とは断定しない。
- **選定根拠**: 【事実】アニメ専用の自動リギングモデルは見つからず(HF・GitHub・論文検索)。汎用で VRoid Hub を学習に20%混ぜたものが VAST-AI/SkinTokens(2026-02論文、2026-04-20 HF公開、MIT)。カード自己報告: 既存手法比でスキニング精度 +98〜133%、ボーン予測 +17〜22%(評価データはカード本文に明示なし)。UniRigの公開ckptは Articulation-XL2.0のみで VRoid版は未公開のため、VRoid学習を含む公開重みとしては SkinTokens が上。【採用の弱さ】HF DL 0(集計対象外)、likes 31(UniRig 92)、GitHub ★440(UniRig ★1,781)、UniRigはコード参照92件と利用は旧UniRigが上。SkinTokensの実使用報告はXで未確認。【評価】精度は新しい方、実績はUniRigが上のため confidence=low。アニメ専用ではない。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 32 / Spaces 12
- **概要**: 3Dメッシュから骨格(skeleton)とスキニングウェイトを単一の自己回帰トークン列(TokenRig, Qwen3-0.6B系、GRPO精緻化)で生成する自動リギングモデル。UniRigの後継。学習データは ArticulationXL 2.0(70%)・VRoid Hub(20%)・ModelsResource(10%)。
- **入力**: 3Dメッシュ(GitHub READMEの例は .glb。UniRig側は .obj/.fbx/.glb/.vrm 対応と記載)
- **出力**: 骨格階層+頂点ごとのスキニングウェイトを持つリグ付き3Dアセット(glb等)
- **必要環境**: モデルカードに要件記載なし。GitHub README: 推論にNVIDIA GPU 14GB以上、Python>=3.11、CUDA>=12.1、flash-attn。未測定。
- **制約**: アニメ専用ではなく汎用(VRoid Hubは学習の20%)。VRM(ヒューマノイドボーン規約)への直接出力は未確認で、VRM化はBlender等で別途必要。学習データ(ArticulationXL splits)は『後日公開』とカードが記載。HF DLは0(集計対象外)、likes 31。ベンチ値は論文・カードの自己報告。
- **使う版・派生**: 推奨ckpt: experiments/articulation_xl_quantization_256_token_4/grpo_1400.ckpt(TokenRig)+ experiments/skin_vae_2_10_32768/last.ckpt(FSQ-CVAE)。派生: LocalAI-io/SkinTokens-GGUF(30日DL 790)、mlx-community/SkinTokens-bf16、fernandotonon/QtMeshEditor-skintokens-onnx(いずれも第三者)。旧世代: VAST-AI/UniRig(ckptはArticulation-XL2.0のみ、VRoid/Rig-XL版は『近日公開』のまま)。
- **根拠**: [モデルカード: UniRig後継、recommended checkpoint、データ構成 ArticulationXL 2.0(70%)/VRoid Hub(20%)/ModelsResource(10%)、『98〜133%スキニング精度向上』の自己報告](https://huggingface.co/VAST-AI/SkinTokens/blob/79736cad0fd84de384d5eede659b4ebd24effe33/README.md) / [論文(2026-02-04): SkinTokens/TokenRig。データ構成(Articulation2.0 70%、VRoid Hub 20%、ModelsResource 10%)](https://arxiv.org/abs/2602.04805) / [GitHub README: 14GB GPU要件、recommended checkpoint、MIT](https://github.com/VAST-AI-Research/SkinTokens/blob/main/README.md) / [旧UniRigカード: 公開ckptはArticulation-XL2.0のみで、VRoid/Rig-XL版は未公開(Discussion #3『Any news on full checkpoints?』がopen)](https://huggingface.co/VAST-AI/UniRig/blob/36842e2b5947e9e60f89275b83208c8e74071c63/README.md)
- **次点**: `VAST-AI/UniRig`（実績は上(likes 92、★1,781、コード参照92、.vrm入出力対応)。ただし公開ckptはArticulation-XL2.0のみでVRoid版は未公開、SkinTokens論文が後継として精度改善を主張） / `jasongzy/Make-It-Animatable`（Mixamo互換のヒューマノイド向け(CVPR 2025 Highlight、★458、MIT)。HFの登録はimage-to-video誤タグ、likes 9、アニメ評価は未確認）

関連リポジトリ:

- [VAST-AI-Research/SkinTokens](https://github.com/VAST-AI-Research/SkinTokens) — 骨格+スキニング統合リギングの公式実装（★447 / MIT / 最終push 2026-05-12 / 確認コミット [`273b691d`](https://github.com/VAST-AI-Research/SkinTokens/blob/273b691d35989d71cd17ff2895fdc735097b92d1/README.md) / 制作カタログ: [skintokens](../../categories/3d.md#skintokens)）
  - ★440、MIT、最終push 2026-05-12。UniRigの後継と明記。
- [VAST-AI-Research/UniRig](https://github.com/VAST-AI-Research/UniRig) — 先行する自動リギング(.vrm入出力とBlender VRMアドオン改造版を同梱)（★1,785 / MIT / 最終push 2026-06-04 / 確認コミット [`6793c664`](https://github.com/VAST-AI-Research/UniRig/blob/6793c6640ff01c8fb389f3993434124bb43d2933/README.md) / 制作カタログ: [unirig](../../categories/3d.md#unirig)）
  - ★1,781、MIT、最終push 2026-06-04。READMEが後継SkinTokensを告知。
- [jasongzy/Make-It-Animatable](https://github.com/jasongzy/Make-It-Animatable) — ヒューマノイド向けの高速リギング(Mixamo互換)（★459 / MIT / 最終push 2026-09-08 / 確認コミット [`8fb51382`](https://github.com/jasongzy/Make-It-Animatable/blob/8fb51382ff6da556cdb95cc03a48200603f3a493/README.md)）
  - ★458、MIT、最終push 2026-09-08。CVPR 2025 Highlight。
- [saturday06/VRM-Addon-for-Blender](https://github.com/saturday06/VRM-Addon-for-Blender) — リグ結果をVRMへ変換・書き出しするBlenderアドオン（★1,720 / MIT / 最終push 2026-10-03 / release v4.7.2 (2026-09-23) / 確認コミット [`6502ad98`](https://github.com/saturday06/VRM-Addon-for-Blender/blob/6502ad9852816ec2a391ed321a4932d45711c105/README.md)）
  - ★1,716、MIT、最終push 2026-09-30、最新リリース v4.7.2(2026-09-23)。UniRig/CharacterGen/StdGENの手順が依拠するVRM入出力。

### テキストからの3Dモーション生成(キャラアニメ用)

<a id="text-to-3d--text-to-motion"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [nvidia/Kimodo-SOMA-RP-v1.1](https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1.1/tree/6c9233af1180b8151e3c4703477104af5dce9dd5)（revision `6c9233af` / 作成 2026-04-07 / 更新 2026-04-10）
- **利用条件**: other/nvidia-open-model-license。メタデータは other/nvidia-open-model-license。カードは『商用利用可(ready for commercial use)』と記述するが、NVIDIA Open Model License の条項は別途確認が必要(商用可と断定しない)。SMPLX版は別の研究用ライセンス。
- **選定根拠**: 【事実】アニメ専用のtext-to-motionモデルはHF・GitHubで未確認。HFでtext-to-3dに分類されるモーションモデルは tencent/HY-Motion-1.0(likes 441、累計DL 4,683)。実務での採用はNVIDIA Kimodoが上: nvidia/Kimodo-SOMA-RP-v1.1 は累計DL 20,316/30日4,857/likes 67、GitHub ★3,667(Apache-2.0、最終push 2026-09-22)、派生(kimodo.cpp ★883、ComfyUI/Blender/Unity橋渡し、MMD用VMD版、Text-To-VRMA ★183)が2026-07〜09に日本語圏Xで多数(1,944/1,094/671 likes)。HY-Motionは Tencent Hunyuan Community License で EU・英国・韓国が対象外(LICENSE.txt)なのに対し、Kimodoは『商用利用可』とカードに記載。ベンチマーク: Kimodoは公開ベンチマーク(BONES-SEED)を同梱、HY-Motionは自社比較図のみ(いずれも自己報告)。【評価】Kimodo採用。アニメ専用でなく人体モーションで、VRM/MMDへはリターゲット必要。音楽→ダンス専用の有力OSSは未確認(HF上はedge-dance-generation/EDGEがDL 0、GitHubのOdoriVRMは★0)。
- **指標（確認日時点）**: DL累計 21,260 / 直近30日 5,291 / likes 70 / Spaces 11
- **概要**: テキストと運動制約(全身ポーズ・2Dルート・エンドエフェクタ)から3D人体スケルトンアニメーションを生成するモーション拡散モデル。SOMAスケルトン、Bones Rigplay 1(700時間の光学モーキャプ)で学習。
- **入力**: テキストプロンプト(英語)、任意でキーフレーム/ルート/手足の制約
- **出力**: SOMAスケルトンの関節回転・ルート並進(VRM・MMD・Mixamo等へは別途リターゲットが必要)
- **必要環境**: モデルカードには要件の記載が乏しい。GitHub README: 約17GB VRAMでGPU単独実行、TEXT_ENCODER_DEVICE=cpu で3GB未満。3090/4090/A100で検証、Linux開発(Windowsはdocker推奨)。未測定。
- **制約**: 人体(ヒューマノイド)限定。アニメ的な誇張モーション・デフォルメ体型・表情/指は対象外。スケルトンはカードが30関節、GitHub READMEが77関節(somaskel77)と記載し不一致(要確認)。訓練データはBones Rigplayの独占データで内容は非公開。
- **使う版・派生**: 同系: Kimodo-SOMA-SEED-v1.1(公開データBONES-SEED 288時間、累計DL 1,184、性能は下と明記)、Kimodo-SMPLX-RP-v1(研究用ライセンス)、Kimodo-G1-*(Unitree G1ロボット用)。第三者派生: localai-org/kimodo.cpp(C++/GGML)、LocalAI-io/Kimodo-SOMA-RP-v1.1-GGML(30日DL 8,257)、Aero-Ex/KIMODO-Meta3_llm2vec_NF4(30日DL 14,900、テキストエンコーダ量子化)。後継的な実時間版: nvidia/ARDY-*(2026-07公開)。
- **根拠**: [モデルカード: SOMA/Rigplay、700時間モーキャプ、v1.1の変更点、NVIDIA Open Model License、『商用利用可』の記載](https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1.1/blob/6c9233af1180b8151e3c4703477104af5dce9dd5/README.md) / [GitHub README: モデル一覧、推奨はRP(700h)、17GB VRAM、ベンチマーク(BONES-SEED)、2026-07-10にARDY公開](https://github.com/nv-tlabs/kimodo/blob/main/README.md) / [X(2026-09-30, 1,094 likes): Kimodoを制作パイプラインに組み込んだ日本語圏の実例](https://x.com/KanaWorks_AI/status/2105242419403149583) / [X(2026-08-23, 1,944 likes): kimodo.cpp(CPU/Vulkan)の告知](https://x.com/Stefan_3D_AI/status/2091531702183350276) / [X(2026-09-12, 251 likes): MMD用VMD対応版Kimodoの公開告知](https://x.com/errno_mmd/status/2098760419104227507)
- **次点**: `tencent/HY-Motion-1.0`（HFのtext-to-3dタグ(likes 441、コード参照274件)でComfyUIノード(★313)もあるが、ライセンスがEU/英国/韓国を対象外とし月間1M MAU超は別契約、累計DLはKimodoの約1/4） / `nvidia/ARDY-Core-RP-20FPS-Horizon40`（実時間・自己回帰版(2026-07、累計DL 5,801、likes 45)。Text-To-VRMAが対応エンジンに採用するが、新しく実績はKimodo本体が上）

関連リポジトリ:

- [nv-tlabs/kimodo](https://github.com/nv-tlabs/kimodo) — Kimodo公式実装(CLI・対話デモ・ベンチマーク)（★3,708 / Apache-2.0 / 最終push 2026-09-22 / 確認コミット [`58e78189`](https://github.com/nv-tlabs/kimodo/blob/58e781898b3d7e328a676a75d3e338c45dce3ad9/README.md)）
  - ★3,667、Apache-2.0、最終push 2026-09-22。ARDY公開(2026-07-10)もREADMEに記載。
- [Kirakun0328/text-to-vrma](https://github.com/Kirakun0328/text-to-vrma) — テキスト→VRMA(VRMアニメーション)生成ツール(VRM特化)（★186 / MIT / 最終push 2026-09-05 / release v1.1.8 (2026-09-05) / 確認コミット [`b8081875`](https://github.com/Kirakun0328/text-to-vrma/blob/b8081875916c8621c7ec226b4adcb2c70e7b13b7/README.md)）
  - ★183、MIT、最終push 2026-09-05、最新 v1.1.8。ARDY/OpenAI/Claudeエンジン対応、ローカルHTTP API。X告知 671 likes(2026-07-16)。
- [localai-org/kimodo.cpp](https://github.com/localai-org/kimodo.cpp) — Kimodoを C++/GGML 化(CPU/Vulkan、PyTorch・CUDA不要)（★891 / Apache-2.0 / 最終push 2026-09-17 / 確認コミット [`5679ff19`](https://github.com/localai-org/kimodo.cpp/blob/5679ff19ba0a522c0b0516e9a9d402fe1af2c027/README.md)）
  - ★883、Apache-2.0、最終push 2026-09-17。X告知 1,944 likes。
- [jtydhr88/ComfyUI-HY-Motion1](https://github.com/jtydhr88/ComfyUI-HY-Motion1) — HY-Motion 1.0 の ComfyUIノード（★312 / ライセンス未表示 / 最終push 2026-08-20 / 確認コミット [`60843a4d`](https://github.com/jtydhr88/ComfyUI-HY-Motion1/blob/60843a4d631efa3989b5c512ae547f996c30dcc3/README.md)）
  - ★313、最終push 2026-08-20、ライセンス未設定。HY-Motionを使う場合の実用経路(ライセンス制限は本体に従う)。

### アニメゲーム/ワールドモデル(次状態予測による対話的アニメ生成)

<a id="anime-game-world-model"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [TencentARC/AnimeGamer](https://huggingface.co/TencentARC/AnimeGamer/tree/a9a2384ac0aae03d32df2b1c6ce6e9c3291baa26)（revision `a9a2384a` / 作成 2025-03-30 / 更新 2025-04-10）
- **利用条件**: other/animegamer-lisence。メタデータは other/animegamer-lisence。ライセンス条項0に『EUでの利用は想定しない(NOT INTENDED FOR USE WITHIN THE EUROPEAN UNION)』とあり領土制限つき。学習データは商業アニメ映画由来で著作権の扱いは明記なし。商用可とは断定しない。
- **選定根拠**: 【事実】アニメ世界を対象にした公開重みのゲーム/ワールドモデルは TencentARC/AnimeGamer が唯一(HF検索 anime game/world model/interactive anime で他に該当なし)。累計DL 295/30日27/likes 46/spaces 0、GitHub ★350(ライセンスNOASSERTION)、論文はHF papers upvotes 70。公開重みは『魔女の宅急便』『崖の上のポニョ』個別版のみで、混合版・学習コードは未公開。ジブリ作品IP前提のためオリジナルキャラの制作には転用不可。【評価】比較対象がないため暫定選定。実用採用の証拠は乏しく(Xでも実使用報告は未確認)、アニメ制作の開発基盤としては研究参考に留まる。
- **指標（確認日時点）**: DL累計 295 / 直近30日 20 / likes 46 / Spaces 0
- **概要**: マルチモーダルLLMが『次のゲーム状態(アニメ調の動画クリップ+体力・社交・娯楽などのキャラ状態)』を予測し、拡散デコーダで動画化する、アニメ世界のライフシミュレーション(ICCV 2025)。
- **入力**: 自然言語の行動指示、キャラ/シーンの参照、履歴(過去のゲーム状態表現)
- **出力**: 動画クリップ(アニメーションショット)とキャラクターステータスの更新
- **必要環境**: モデルカードに要件記載なし。GitHub README: Mistral-7B と CogVideoX の3D-VAE が別途必要、低VRAM版は2GPU(各24GB以上)、単一GPUなら60GB以上。未測定。
- **制約**: 公開重みは『魔女の宅急便(Qiqi)』『崖の上のポニョ(Sosuke)』ごとの個別学習版のみ(スタジオジブリ作品IP)。論文設定の複数アニメ映画混合版・学習コード・データ処理は未公開(READMEのTODO未チェック)。任意のオリジナルキャラへは使えない。最終更新 2025-04。
- **使う版・派生**: MLLM-Qiqi/MLLM-Sosuke と VDM_Decoder-Qiqi/VDM_Decoder-Sosuke を同梱。量子化・派生は未確認。
- **根拠**: [モデルカード: 概要とLICENSE(EU除外)。HFのtext-to-videoタグ](https://huggingface.co/TencentARC/AnimeGamer/blob/a9a2384ac0aae03d32df2b1c6ce6e9c3291baa26/README.md) / [GitHub README: 公開重みは2作品別、混合版・学習コード未公開、Gradio要件(2×24GB/60GB)](https://github.com/TencentARC/AnimeGamer/blob/main/README.md) / [論文 AnimeGamer(2025-04-01)、HF papers upvotes 70](https://arxiv.org/abs/2504.01014)

関連リポジトリ:

- [TencentARC/AnimeGamer](https://github.com/TencentARC/AnimeGamer) — 公式推論コード・Gradioデモ（★352 / NOASSERTION / 最終push 2025-04-09 / 確認コミット [`59711149`](https://github.com/TencentARC/AnimeGamer/blob/5971114910913cdb5837418dc42aacccbb408a6d/README.md)）
  - ★350、最終push 2025-04-09(以降更新なし)。ICCV 2025。訓練コード・混合版重みはREADMEのTODOが未完了。

### ピクセルアート・スプライト生成

<a id="pixel-art-sprite"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [nerijs/pixel-art-xl](https://huggingface.co/nerijs/pixel-art-xl/tree/8bf4a4d9ea283e00a51fafda8e0539f8248ea037)（revision `8bf4a4d9` / 作成 2023-08-03 / 更新 2023-11-09）
- **利用条件**: creativeml-openrail-m。メタデータは creativeml-openrail-m(SDXL baseのOpenRAIL系)。使用制限条項は適用される。商用可とは断定しない。
- **選定根拠**: 【事実】アニメ専用のスプライト/ピクセルアート生成モデルは見つからず(HF検索 sprite・pixel art・tachie・character sheet・visual novel 等。歩行スプライトLoRAは汎用ゲーム向け)。汎用では nerijs/pixel-art-xl が累計DL 945,353/30日32,460/likes 656/spaces 100/討議23件で突出し、tarn59のZ-Image-Turbo版(累計935,604/30日11,118/likes 56)が並ぶ。【評価】利用実績で nerijs を選ぶが、2023-11から更新がなく『老舗の事実上標準』であって最新品質の裏付けはない。ベンチ比較は見つからず、ピクセルアートはアニメ固有でもないため confidence=low。立ち絵の表情差分(瞬き・口形)はレイヤ分解+PachiPakuGen系の別経路が現実的。
- **指標（確認日時点）**: DL累計 948,411 / 直近30日 34,068 / likes 656 / Spaces 100
- **概要**: SDXL用のピクセルアート LoRA(1ファイル)。8倍縮小+最近傍補間でピクセル整列画像を得る運用。トリガーワード不要、LCM LoRA併用で8ステップ生成も可。
- **入力**: テキストプロンプト(SDXL系パイプライン、固定VAE推奨)
- **出力**: ピクセルアート調の画像(ドット整列には8倍縮小が必要)
- **必要環境**: SDXL base 1.0 + LoRA。VRAM要件はカードに記載なし・未測定。
- **制約**: アニメ専用ではなくピクセルアート汎用。16×16/32×32等の小ドット指定は安定しない(Discussion #21で質問がopen)。スプライトシート(歩行アニメ等)専用の設計ではない。2023-11以降更新なし。
- **使う版・派生**: Z-Image-Turbo版: tarn59/pixel_art_style_lora_z_image_turbo(累計DL 935,604/30日11,118、Apache-2.0)。スプライトシート系: svntax-dev/pixel_spritesheet_4walk_small_lora_v1(likes 45)、fal/flux-2-klein-4b-spritesheet-lora(2×2多視点、物体向けでキャラ歩行ではない)。
- **根拠**: [モデルカード: 使い方(8倍縮小・最近傍補間・固定VAE・LCM LoRA併用)、トリガー不要](https://huggingface.co/nerijs/pixel-art-xl/blob/8bf4a4d9ea283e00a51fafda8e0539f8248ea037/README.md) / [次点: Z-Image-Turbo用LoRA(累計DL 935,604、Apache-2.0)](https://huggingface.co/tarn59/pixel_art_style_lora_z_image_turbo/blob/0a5092d1619664d94a5a36784f92db84b3ae62bd/README.md)
- **次点**: `tarn59/pixel_art_style_lora_z_image_turbo`（累計DL 935,604とnerijsに並ぶがlikes 56・30日DLは約1/3。新世代ベース(Z-Image-Turbo)向けで、こちらを選ぶ余地あり） / `svntax-dev/pixel_spritesheet_4walk_small_lora_v1`（4方向歩行スプライトシート専用(likes 45)。30日DL 768と小規模、アニメ向けではない）

### アニメ2Dアバターのアニメーション(1枚絵駆動・Live2D代替・表情差分)

<a id="anime-2d-avatar-animation"></a>
- **判定**: モデルなし / 確度 低
- **選定根拠**: 【事実】HF上にはpkhungurn『Talking Head Anime』系の再配布(OktayAlpk/talking-head-anime-3等、DL 0)しかなく、公式重みはGitHub側配布でHF推奨モデルは立てられない。リポジトリ側の実績: EasyVtuber(THA3ベース、★3,071、MIT、最終push 2026-02-12)、talking-head-anime-3-demo ★1,044、-4-demo ★355(MIT、2024-03以降更新なし)。Inochi2D(オープンなLive2D代替、★1,799、BSD-2-Clause、最終リリースv0.8.7は2024-10)。See-throughのPSD出力から瞬き・口形を作る PachiPakuGen(★130、MIT、2026-09-21に v0.4.1)がSee-through公式READMEの派生に掲載。【評価】一枚絵を直接動かす学習モデルの新世代は確認できず、2026年の実務はSee-throughレイヤ分解→2.5Dリグ(live2d-layer-decompositionのリポジトリ)へ移っている(X 2026-03〜09)。THA系は2024年以降更新停止。

関連リポジトリ:

- [yuyuyzl/EasyVtuber](https://github.com/yuyuyzl/EasyVtuber) — Talking-head-anime-3 を使ったVTuber配信ツール(Vtube Studio相当)（★3,071 / MIT / 最終push 2026-02-12 / 確認コミット [`f7dd2de4`](https://github.com/yuyuyzl/EasyVtuber/blob/f7dd2de4df93c878b0171f47346ff66414a863e6/README.md)）
  - ★3,071、MIT、最終push 2026-02-12。THA3の実用フロントエンドとして最大。
- [pkhungurn/talking-head-anime-4-demo](https://github.com/pkhungurn/talking-head-anime-4-demo) — 1枚絵から表情・頭部を駆動する研究実装(THA4)（★355 / MIT / 最終push 2024-03-01 / 確認コミット [`32064011`](https://github.com/pkhungurn/talking-head-anime-4-demo/blob/320640116abd604de22d7b56faec85b4d95770e0/README.md)）
  - ★355、MIT、最終push 2024-03-01。更新停止。重みはGitHub側手順で取得(HF公式なし)。
- [Inochi2D/inochi2d](https://github.com/Inochi2D/inochi2d) — オープンソースの2Dパペット/Live2D代替SDK(リギング・配信アプリinochi-creator/sessionと連携)（★1,803 / BSD-2-Clause / 最終push 2026-10-03 / release v0.8.7 (2024-10-02) / 確認コミット [`ba2b1413`](https://github.com/Inochi2D/inochi2d/blob/ba2b1413c68d9f7bf575fef790ba0c35715558db/README.md)）
  - ★1,799、BSD-2-Clause、最終push 2026-09-15、最新リリース v0.8.7(2024-10-02)。
- [kazuya-bros/PachiPakuGen](https://github.com/kazuya-bros/PachiPakuGen) — See-through PSDから瞬き・リップシンク口形の素材を生成するデスクトップ工具（★131 / MIT / 最終push 2026-09-21 / release v0.4.1 (2026-09-21) / 確認コミット [`629e6346`](https://github.com/kazuya-bros/PachiPakuGen/blob/629e63461bb076ca9275b5640026ffff022d1f32/README.md)）
  - ★130、MIT、最終push 2026-09-21、最新 v0.4.1。See-through公式READMEが派生として掲載。

### VTuber/AIキャラクター対話エージェント基盤(Live2D/VRM+LLM+TTS+ASR)

<a id="vtuber-agent-framework"></a>
- **判定**: モデルなし / 確度 中
- **選定根拠**: 【事実】HFにはVTuber専用の有力モデルがなく(vtuber検索: LLM微調整GGUF等、30日DL 500未満が最大級)、実体はGitHubのフレームワーク。moeru-ai/airi ★49,887(MIT、最終push 2026-09-30、v0.12.0-beta.5=2026-08-29、VRM/Live2D・Minecraft連携、WebGPU/CUDA)、Open-LLM-VTuber ★13,961(ライセンスNOASSERTION、最終push 2026-05-15、最新v1.2.1=2025-08-26、Live2D+音声対話)、tegnike/aituber-kit ★1,114(ライセンスNOASSERTION、最終push 2026-09-30、v2.78.1)。【評価】更新頻度・規模でAIRIが首位、日本語圏実務のAITuber系はaituber-kit。Open-LLM-VTuberは2026-05以降push停止でリリースも2025-08止まり。ライセンス条件はリポジトリごとに異なり、Open-LLM-VTuberはLive2Dサンプルモデルが別ライセンス(商用は追加条件)と明記。

関連リポジトリ:

- [moeru-ai/airi](https://github.com/moeru-ai/airi) — 自己ホスト型AIコンパニオン/VTuber基盤(VRM・Live2D・音声・Minecraft)（★49,976 / MIT / 最終push 2026-10-03 / release v0.12.0-beta.5 (2026-08-29) / 確認コミット [`da2bcbd4`](https://github.com/moeru-ai/airi/blob/da2bcbd46f56c1c6ecb40d44fb60694e6599f11b/README.md) / 制作カタログ: [airi](../../categories/vtuber.md#airi)）
  - ★49,887、MIT、最終push 2026-09-30、最新 v0.12.0-beta.5(2026-08-29)。規模・更新とも首位。
- [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) — 音声対話+Live2Dの定番ローカルVTuber(割り込み・ハンズフリー)（★13,977 / NOASSERTION / 最終push 2026-05-15 / release v1.2.1 (2025-08-26) / 確認コミット [`992309c0`](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/README.md) / 制作カタログ: [open-llm-vtuber](../../categories/vtuber.md#open-llm-vtuber)）
  - ★13,961、最終push 2026-05-15、最新 v1.2.1(2025-08-26)。GitHubライセンスはNOASSERTION(READMEはMITと別の第三者ライセンスを併記、Live2Dサンプルは別条件)。更新は鈍化。
- [tegnike/aituber-kit](https://github.com/tegnike/aituber-kit) — 日本語圏で使われるAITuber向けWebアプリ(VRM/Live2D・多数のLLM/TTS)（★1,114 / NOASSERTION / 最終push 2026-10-03 / release v2.78.1 (2026-09-13) / 確認コミット [`c7ea2b65`](https://github.com/tegnike/aituber-kit/blob/c7ea2b65f99ac68bf0621c626b9dedf9c30e2c32/README.md)）
  - ★1,114、最終push 2026-09-30、v2.78.1(2026-09-13)。ライセンスNOASSERTION(要確認)。

### VRM/MMD/3Dアバター基盤ツール(ビューア・DCC連携・ゲームエンジン)

<a id="vrm-avatar-tooling"></a>
- **判定**: モデルなし / 確度 高
- **選定根拠**: 【事実】モデルではなくフォーマット/ランタイム領域。各ランタイムの公式実装が標準で、いずれも更新が新しい: pixiv/three-vrm(★2,192、MIT、最終push 2026-09-30、v3.5.5=2026-07-09)、vrm-c/UniVRM(Unity、★3,392、MIT、v0.131.2=2026-07-24、最終push 2026-09-25)、saturday06/VRM-Addon-for-Blender(★1,716、MIT、v4.7.2=2026-09-23)、ruyo/VRM4U(UE5、★1,989、ライセンスNOASSERTION、v1.2026.09.12)。UniRig・CharacterGen・StdGENの手順もBlenderアドオンとthree-vrmに依拠している。【評価】該当は『モデルなし・公式ランタイムを採用』で確定。MMD(PMX/VMD)用は単独で突出した公式実装を確認できず(SekaiBlender ★17等は小規模)、本タスクではVRM系を標準とする。

関連リポジトリ:

- [pixiv/three-vrm](https://github.com/pixiv/three-vrm) — Three.js用VRMローダ・ビューア(Web/ComfyUI/AITuber系の標準)（★2,196 / MIT / 最終push 2026-10-02 / release v3.5.5 (2026-07-09) / 確認コミット [`1b4fc0cc`](https://github.com/pixiv/three-vrm/blob/1b4fc0cc7ef39a49d62bb7a66dcfeca8f65316f7/README.md) / 制作カタログ: [three-vrm](../../categories/vtuber.md#three-vrm)）
  - ★2,192、MIT、最終push 2026-09-30、最新 v3.5.5(2026-07-09)。CharacterGenのVRMレンダリング手順も使用。
- [vrm-c/UniVRM](https://github.com/vrm-c/UniVRM) — Unity用VRMインポート/エクスポート(VRM仕様の参照実装)（★3,392 / MIT / 最終push 2026-10-02 / release v0.131.3 (2026-10-02) / 確認コミット [`9750dadc`](https://github.com/vrm-c/UniVRM/blob/9750dadc592f421c356bf0376c73e61abbe323e3/README.md) / 制作カタログ: [univrm](../../categories/vtuber.md#univrm)）
  - ★3,392、MIT、最終push 2026-09-25、最新 v0.131.2(2026-07-24)。
- [saturday06/VRM-Addon-for-Blender](https://github.com/saturday06/VRM-Addon-for-Blender) — BlenderのVRM入出力(リギング/レンダリング系論文の手順が依拠)（★1,720 / MIT / 最終push 2026-10-03 / release v4.7.2 (2026-09-23) / 確認コミット [`6502ad98`](https://github.com/saturday06/VRM-Addon-for-Blender/blob/6502ad9852816ec2a391ed321a4932d45711c105/README.md)）
  - ★1,716、MIT、最終push 2026-09-30、最新 v4.7.2(2026-09-23)。Blender 2.93〜5.2対応。
- [ruyo/VRM4U](https://github.com/ruyo/VRM4U) — Unreal Engine 5用VRMランタイムローダ（★1,988 / NOASSERTION / 最終push 2026-09-23 / release v1.2026.09.12 (2026-09-11) / 確認コミット [`615e6323`](https://github.com/ruyo/VRM4U/blob/615e6323d445961b7b0628807fbfd1db3acd2450/README.md)）
  - ★1,989、最終push 2026-09-23、最新 v1.2026.09.12。GitHubライセンスNOASSERTION(要確認)。

### モーションキャプチャ・リターゲット(VRM/MMD/Mixamo)

<a id="motion-capture-retargeting"></a>
- **判定**: モデルなし / 確度 低
- **選定根拠**: 【事実】HFに該当モデルなし(mmd・vmd・bvh・mixamo検索で実用モデル0)。実用はGitHubのツール。xianfei/SysMocap(★3,224、MPL-2.0、v0.8.0=2026-06-10、リアルタイムモーキャプ→3Dキャラ)、ButzYung/SystemAnimatorOnline(XR Animator、★1,897、ライセンス未設定、v0.35.0=2026-09-20)、AmyangXYZ/reze-mipo(MMD用ブラウザモーキャプ、★665、GPL-3.0、v5.0.0=2026-08-28)、tk256ailab/fbx2vrma-converter(FBX→VRMA、★63)。【評価】生成系モーションのVRM/MMD連携は text-to-motion のリポジトリ(Text-To-VRMA等)側にあり、リターゲットの汎用標準は確立していない。ライセンスはGPL-3.0やライセンス未設定が混在するため用途ごとに確認が必要。

関連リポジトリ:

- [xianfei/SysMocap](https://github.com/xianfei/SysMocap) — リアルタイムモーキャプ→3Dキャラ(VRM/MMD等)（★3,223 / MPL-2.0 / 最終push 2026-06-10 / release v0.8.0 (2026-06-10) / 確認コミット [`1472b082`](https://github.com/xianfei/SysMocap/blob/1472b082ad034cde6351c629cabad0f6020eaf7a/README.md)）
  - ★3,224、MPL-2.0、最終push 2026-06-10、v0.8.0。
- [ButzYung/SystemAnimatorOnline](https://github.com/ButzYung/SystemAnimatorOnline) — XR Animator: AIベース全身モーキャプ+VRM/MMDモデル駆動（★1,907 / ライセンス未表示 / 最終push 2026-09-20 / release XR-Animator_v0.35.0 (2026-09-20) / 確認コミット [`53c20eb9`](https://github.com/ButzYung/SystemAnimatorOnline/blob/53c20eb91517d2807d142c122a868ca9157c3016/README.md)）
  - ★1,897、ライセンス未設定、最終push 2026-09-20、v0.35.0(2026-09-20)。
- [AmyangXYZ/reze-mipo](https://github.com/AmyangXYZ/reze-mipo) — ブラウザ上のMMDリアルタイムモーキャプ(VMD出力)（★666 / GPL-3.0 / 最終push 2026-09-08 / release v5.0.0 (2026-08-28) / 確認コミット [`2eb21c09`](https://github.com/AmyangXYZ/reze-mipo/blob/2eb21c09ec563259e20e4edcbb9060ff47ddcf0d/README.md)）
  - ★665、GPL-3.0(コピーレフトに注意)、最終push 2026-09-08、v5.0.0。
- [tk256ailab/fbx2vrma-converter](https://github.com/tk256ailab/fbx2vrma-converter) — FBXアニメーション→VRMA(VRMアニメーション)変換（★63 / MIT / 最終push 2026-02-23 / 確認コミット [`c6454417`](https://github.com/tk256ailab/fbx2vrma-converter/blob/c6454417ae44a721ba25671adecda9dce8fda938/README.md)）
  - ★63、最終push 2026-02-23。小規模だが用途特化。

### アニメ3Dキャラ・リグのデータセット(Anime3D/Anime3D++/AnimeRig)

<a id="anime-3d-datasets"></a>
- **判定**: モデルなし / 確度 中
- **選定根拠**: 【事実】Anime3D(CharacterGen)・Anime3D++(StdGEN、VRoid Hub 10,811体)は『ポリシー上、生VRMは再配布不可』とREADMEが明記し、レンダリングスクリプトのみ公開(HF/GitHubに実データなし)。HFデータセット検索(anime3d・vroid・live2d・anime motion)でも大規模な該当なし(Mitsua/vroid-image-dataset-lite はlikes 11・30日DL 20の画像集のみ)。AnimeRigという名称のデータセットはHF・GitHubとも未確認。モーションはbones-studio/seed(BONES-SEED、likes 271、30日DL 5,063、人体モーキャプでアニメ専用ではない)のみ突出。【評価】利用可能な公開アニメ3Dデータはなく、各自がVRoid Hubの規約に従って収集する前提。推奨データセットは置かない。

関連リポジトリ:

- [ShuhongChen/panic3d-anime-reconstruction](https://github.com/ShuhongChen/panic3d-anime-reconstruction) — PAniC-3D(CVPR 2023): VRoid由来データ取得手順の出典(CharacterGen・StdGENが参照)（★831 / ライセンス未表示 / 最終push 2023-06-04 / 確認コミット [`ed49f931`](https://github.com/ShuhongChen/panic3d-anime-reconstruction/blob/ed49f931b0fbd7b73f484d10f723d9455a943793/README.md)）
  - ★831、ライセンス未設定、最終push 2023-06-04(更新停止)。データ入手手順の一次情報として参照される。
