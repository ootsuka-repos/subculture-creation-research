# アニメ・エンタメ向けAI研究 2026 — 公式コード・公開モデル

**公式コードと本研究の学習済み重みが両方公開されている研究**を、日本語の内容要約付きでまとめています。2026年を優先し、2026年大会がない・採択が未確定の会議は2025年を参照します。最終確認日: **2026-09-06**。

| 一覧 | 掲載数 | 内容・データ |
| --- | --- | --- |
| [SIGGRAPH 2026](#分野別一覧) | 66件 | 3D・モーション・画像・映像・音声など。 [JSON](papers.json) · [CSV](papers.csv) · [未掲載候補](reviewed-not-included.json) |
| [関連会議の2026年版／2025年補完](entertainment-research-2026.md) | 21件 | ICLR、CVPR、ICCV、ECCV、ICML、NeurIPS、SIGGRAPH Asia、SCA、ACM MM、ICASSP、Interspeech。 [JSON](entertainment-research-2026.json) · [CSV](entertainment-research-2026.csv) |

**66件と21件は調査範囲が異なるため、会議間の研究数の比較には使えません。** SIGGRAPHはTechnical Papersを広く調べた一覧で、CAD・製造などの周辺分野も含みます。関連会議の21件はアニメ・エンタメへの関連性から選定した候補で、各会議の公開コード・重み付き研究を網羅した件数ではありません。

中割り・彩色、ベクターアニメ、キャラクター演技、リグ付け、効果音など、用途から探す場合は[制作工程別の一覧](entertainment-research-2026.md#制作工程から探す)を参照してください。各研究に「何ができるか」、公式コード、重みの配布先、公開範囲を記載しています。

## SIGGRAPH 2026の掲載基準と確認範囲

- 以下の66件はConference / Journalトラックと、SIGGRAPH 2026で発表されたTOG論文が対象です。SIGGRAPH Asiaは[関連会議の一覧](entertainment-research-2026.md)に掲載し、この66件には含めません。ポスター、講習、非公式再実装はこの一覧の対象外です。
- 著者の公式実装が存在し、本研究で配布する学習済み重み・LoRA・ポリシー・同梱ネットワークにアクセスできることを確認しています。部分公開は備考で範囲を明示します。
- 登録や利用条件への同意を要する配布も含みます。「公開」は無条件利用や商用利用の許可を意味しません。コードの条件とモデルの条件はそれぞれのリンク先を確認してください。
- コードのファイル一覧、HFのモデルファイル一覧、GitHub Releases、外部配布ページ・ダウンロード応答を確認しました。重み全体のダウンロードや推論・再現実験は実施していません。
- セッション別一覧、会議録索引、TOG索引と著者の公開ページを突き合わせた確認時点の一覧です。未発見・未索引の公開物まで含めた完全網羅は保証しません。「Coming soon」や専用重みを確認できないものを公開済み件数に含めていません。

各項目の確認日、コードのコミット、モデルのリビジョン・確認ファイル・根拠URLは[JSON](papers.json)に記録しています。ファイル一覧での確認と実行検証を区別し、Git LFSのオブジェクトIDはモデル本体のチェックサムとして扱っていません。

## 分野別一覧

### 3D生成・CAD・幾何処理（18件）

| 論文 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- |
| [AniGen: Unified S³ Fields for Animatable 3D Asset Generation](https://doi.org/10.1145/3811297) | 1枚の画像から、形状・骨格・スキニングをそろえた、動かせる3Dアセットを生成する。 | [VAST-AI-Research/AniGen](https://github.com/VAST-AI-Research/AniGen) · [コード条件](https://github.com/VAST-AI-Research/AniGen/blob/main/LICENSE) | [モデル](https://huggingface.co/VAST-AI/AniGen) | DAE・Flowなどを配布。 |
| [B-repLer: Language-guided Editing of CAD Models](https://doi.org/10.1145/3799902.3811166) | 既存のCADモデルを自然言語の指示で編集し、CADで再利用できるB-rep形式の形状を出力する。 | [yilinliu77/Brepler](https://github.com/yilinliu77/Brepler) · 条件はREADME参照 | [モデル](https://www.dropbox.com/scl/fi/38klqe5hdomc6t9xbiv84/brepler_ckpt.zip?rlkey=ebo0oabf6p1zkxnt0eamkj976&dl=0) | 編集モデルとHoLa VAE。 |
| [CubePart: An Open-Vocabulary Part-Controllable 3D Generator](https://doi.org/10.1145/3799902.3811117) | 3Dメッシュと部品名の一覧から、指定した意味単位のパーツに分解する。公開版は部品分解と形状VAEが対象。 | [Roblox/cube](https://github.com/Roblox/cube/tree/main/cubepart) · [コード条件](https://github.com/Roblox/cube/blob/main/LICENSE) | [モデル](https://huggingface.co/Roblox/cubepart) | 公開部分はmulti-part mesh decompositionとshape VAE。 |
| [DeepMill++: Neural Guidance Meets Rasterization for Efficient Accessibility Analysis](https://doi.org/10.1145/3799902.3811091) | 3D形状に対して切削工具が届く場所を推定する。3軸加工の干渉・加工可能性を調べる製造向け手法。 | [YaoZhang-666/DeepMillPlusPlus](https://github.com/YaoZhang-666/DeepMillPlusPlus) · 条件はREADME参照 | [モデル](https://github.com/YaoZhang-666/DeepMillPlusPlus/tree/main/DeepM/pretrained) | DeepMモデル。Git LFS配布。 |
| [DualBrep: A Dual-Field Continuous Representation for B-rep Modelling](https://doi.org/10.1145/3799902.3811057) | CAD形状の表面と境界構造を連続的な場で表現し、B-repモデルを復元・生成する。 | [AutodeskAILab/DualBrep](https://github.com/AutodeskAILab/DualBrep) · 条件はREADME参照 | [モデル](https://huggingface.co/ADSKAILab/DualBrep) | checkpoints.zipにVAE・Flow・parametrizer。 |
| [InfiniteDiffusion: Bridging Learned Fidelity and Procedural Utility for Open-World Terrain Generation](https://doi.org/10.1145/3799902.3811080) | シードを保ちながら必要な場所の地形を順次生成する。広大なゲーム背景や地形のストリーミング向け。 | [xandergos/terrain-diffusion](https://github.com/xandergos/terrain-diffusion) · [コード条件](https://github.com/xandergos/terrain-diffusion/blob/master/LICENSE) | [モデル](https://huggingface.co/collections/xandergos/terrain-diffusion) | Terrain Diffusionのモデル群。論文の旧題との重複を統合。 |
| [MeshFlow: Mesh Generation with Equivariant Flow Matching](https://doi.org/10.1145/3799902.3811195) | 頂点・面を持つ3Dメッシュを直接生成する。公開重みは椅子・机・ランプ・ベンチの4カテゴリ。 | [qiisun/MeshFlow](https://github.com/qiisun/MeshFlow) · 条件はREADME参照 | [モデル](https://huggingface.co/datasets/qsun2001/meshflow/tree/main/v1) | ShapeNetの4カテゴリの重み。配布先はHF datasetリポジトリ。 |
| [Learning Laplacian Eigenspace with Mass-Aware Neural Operators on Point Clouds](https://doi.org/10.1145/3799902.3811185) | 点群から形状解析に使う低周波の固有空間を高速に推定する。形状の比較・対応付けなどの基盤処理向け。 | [Adversarr/NEO](https://github.com/Adversarr/NEO) · 条件はREADME参照 | [モデル](https://drive.google.com/drive/folders/12026qTECiGywESPz6WSbpgD8BPMd41Ha) | NEOの学習済み重み。 |
| [Neural Particle Automata: Learning Self-Organizing Particle Dynamics](https://doi.org/10.1145/3799902.3811052) | 粒子同士の局所的な相互作用を学習し、模様や形が自己組織化して変化する動きを作る。 | [TheDevilWillBeBee/NPA](https://github.com/TheDevilWillBeBee/NPA) · 条件はREADME参照 | [モデル](https://github.com/TheDevilWillBeBee/NPA/tree/main/data/pretrained) | lizard・polka_dottedの学習済みモデル。 |
| [NeuralSketch2Surf: Fast Neural Surfacing of Unoriented 3D Sketches](https://doi.org/10.1145/3799902.3811227) | 空間内に描いた疎な3D線画から、滑らかで閉じた立体表面を復元する。ラフな立体スケッチの造形支援。 | [Hongsheng-Y/NeuralSketch2Surf](https://github.com/Hongsheng-Y/NeuralSketch2Surf) · 条件はREADME参照 | [モデル](https://huggingface.co/HongshengY/S2V_Net) | TorchScript/PyTorchチェックポイント。 |
| [Pixal3D: Pixel-Aligned 3D Generation from Images](https://doi.org/10.1145/3799902.3811175) | 参照画像の細部に対応する3D形状とPBRテクスチャを生成する。公開最新版は複数視点入力にも対応。 | [TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D) · [コード条件](https://github.com/TencentARC/Pixal3D/blob/master/LICENSE) | [モデル](https://huggingface.co/TencentARC/Pixal3D) | 論文再現用は paper ブランチ。最新実装と区別。 |
| [Points as Tori: Fast Pointwise Signed Distance for Point Clouds](https://doi.org/10.1145/3811385) | 向き付き点群から、空間中の点が表面からどれだけ離れているかを高速に計算する。形状処理の基盤技術。 | [nzfeng/points-as-tori](https://github.com/nzfeng/points-as-tori) · [コード条件](https://github.com/nzfeng/points-as-tori/blob/main/LICENSE) | [モデル](https://github.com/nzfeng/points-as-tori/tree/main/src/pointsastori/models) | 小規模な学習済みネットワークを同梱。 |
| [Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction](https://doi.org/10.1145/3799902.3811124) | 画像になった間取り図を、部屋などの意味情報を持つポリゴン列へ変換する。室内レイアウトの構造化向け。 | [Cornell-VAILab/Raster2Seq](https://github.com/Cornell-VAILab/Raster2Seq) · [コード条件](https://github.com/Cornell-VAILab/Raster2Seq/blob/master/LICENSE) | [モデル](https://huggingface.co/haopt/Raster2Seq) | 床面図復元モデル。 |
| [SegviGen: Repurposing 3D Generative Model for Part Segmentation](https://doi.org/10.1145/3811399) | 3Dモデルを意味のある部位に分割する。クリック指定・全体分割・2Dの分割画像による誘導を扱う。 | [Nelipot-Lee/SegviGen](https://github.com/Nelipot-Lee/SegviGen) · [コード条件](https://github.com/Nelipot-Lee/SegviGen/blob/main/LICENSE) | [モデル](https://huggingface.co/fenghora/SegviGen) | 部分指定・全体分割・2D誘導の重みを配布。 |
| [SimArt: Decomposing Monolithic Meshes into Sim-ready Articulated Assets via MLLM](https://doi.org/10.1145/3799902.3811173) | 一体化した3Dメッシュを部品に分け、関節の動きも推定して、シミュレーション可能なアセットにする。 | [ByteDance-Seed/SimArt](https://github.com/ByteDance-Seed/SimArt) · [コード条件](https://github.com/ByteDance-Seed/SimArt/blob/main/LICENSE) | [モデル](https://huggingface.co/ByteDance-Seed/SimArt) | MLLMとVQ-VAEの重み。 |
| [SQuadGen: Generating Simple Quad Layouts via Chart Distance Fields](https://doi.org/10.1145/3811348) | 3D形状上にシンプルな四角形の区画構造を生成し、モデリングや編集に使いやすいクアッドメッシュ作成を支援する。 | [microsoft/SQuadGen](https://github.com/microsoft/SQuadGen) · [コード条件](https://github.com/microsoft/SQuadGen/blob/main/LICENSE) | [モデル](https://huggingface.co/microsoft/SQuadGen) | SQ-VAE・Geom-AE・SQDiffuse。 |
| [SuperSDF: Sparse SDF Super-Resolution for Surface Extraction](https://doi.org/10.1145/3799902.3811176) | 粗い符号付き距離場を高解像度化し、より細かな表面メッシュを復元する。低解像度形状の改善向け。 | [Sagar160/SSU](https://github.com/Sagar160/SSU) · [コード条件](https://github.com/Sagar160/SSU/blob/main/LICENSE) | [モデル](https://github.com/Sagar160/SSU/tree/main/run/data) | リポジトリ内にモデル重みを収録。 |
| [Generative 3D Gaussians with Learned Density Control](https://doi.org/10.1145/3799902.3811130) | 1枚の画像から3D Gaussianアセットを生成する。Gaussian数を変えて見た目と描画負荷を調整できる。 | [runjie-yan/TripoSplat-Training](https://github.com/runjie-yan/TripoSplat-Training) · [コード条件](https://github.com/runjie-yan/TripoSplat-Training/blob/master/LICENSE) | [モデル](https://huggingface.co/VAST-AI/TripoSplat) | TripoSplat。DINOv3等の依存モデルには別途アクセス条件あり。 |

### 3D復元・理解（7件）

| 論文 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- |
| [ArtiFixer: Enhancing and Extending 3D Reconstruction with Auto-Regressive Diffusion Models](https://doi.org/10.1145/3799902.3811060) | 3D復元結果のレンダリングに生じる欠損や破綻を動画拡散モデルで補い、復元の改善や視点範囲の拡張を行う。 | [nv-tlabs/ArtiFixer](https://github.com/nv-tlabs/ArtiFixer) · [コード条件](https://github.com/nv-tlabs/ArtiFixer/blob/main/LICENSE) | [モデル](https://huggingface.co/nvidia/ArtiFixer) | 1.3B・14B。Wanベースモデルが別途必要。 |
| [GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction](https://doi.org/10.1145/3799902.3811222) | 少数視点から復元した3Dシーンの新視点画像を、参照画像と幾何対応を使って修復する。 | [Xiaoc7/GeoQuery](https://github.com/Xiaoc7/GeoQuery) · [コード条件](https://github.com/Xiaoc7/GeoQuery/blob/main/LICENSE) | [モデル](https://huggingface.co/DIG-UESTC/GeoQuery) | 拡散refinerの重み。 |
| [MegaNorm: Local Patch Embeddings for Efficient and Robust Point Normal Orientation at Super-Large Scale](https://doi.org/10.1145/3799902.3811139) | 大規模な点群で表面の向きを局所・全体の両方からそろえる。スキャン形状のメッシュ化などの前処理向け。 | [zd-lee/MegaNorm](https://github.com/zd-lee/MegaNorm) · 条件はREADME参照 | [モデル](https://huggingface.co/wlbbbbb/meganorm) | patchnet等の重み。 |
| [Mix3R: Mixing Feed-forward Reconstruction and Generative 3D Priors for Joint Multi-view Aligned 3D Reconstruction and Pose Estimation](https://doi.org/10.1145/3799902.3811152) | 複数画像から、生成モデルの形状知識を利用して3D形状とカメラ姿勢を同時に推定する。 | [jsnln/mix3r](https://github.com/jsnln/mix3r) · 条件はREADME参照 | [モデル](https://modelscope.cn/models/jsnln00/mix3r) | V1が論文版、V2が会議後の更新版。 |
| [MTPano: Multi-Task Panoramic Scene Understanding via Label-Free Integration of Dense Prediction Priors](https://doi.org/10.1145/3799902.3811193) | 360度パノラマ画像から、物体・領域の分類、奥行き、表面の向きをまとめて推定する。 | [Evergreen0929/MTPano](https://github.com/Evergreen0929/MTPano) · 条件はREADME参照 | [モデル](https://huggingface.co/jdzhang0929/MTPano) | 140k・408kチェックポイント。 |
| [PointLLM-R: Enhancing 3D Point Cloud Reasoning via Chain-of-Thought](https://doi.org/10.1145/3799902.3811081) | 3D点群について自然言語で質問し、形状・用途などの説明や分類を得る。3D素材の理解・整理向け。 | [Xqle/PointLLM-R](https://github.com/Xqle/PointLLM-R) · [コード条件](https://github.com/Xqle/PointLLM-R/blob/master/LICENSE) | [モデル](https://huggingface.co/QileXu/PointLLM-R-7B) | 7Bモデル。 |
| [TrajVG: 3D Trajectory-Coupled Visual Geometry Learning](https://doi.org/10.1145/3799902.3811184) | 動画から点の3D軌跡、フレームごとの形状、カメラ姿勢を整合するように推定する。動的シーンの解析向け。 | [xingy038/TrajVG](https://github.com/xingy038/TrajVG) · [コード条件](https://github.com/xingy038/TrajVG/blob/main/LICENSE) | [モデル](https://drive.google.com/file/d/1vk27rkLPJrYVUgD7tCFw2ti5NQLYk2PK/view) | 3D軌跡と幾何復元の学習済みモデル。 |

### モーション・アニメーション（9件）

| 論文 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- |
| [Adaptive Interpolation-Synthesis for Motion In-Betweening on Keyframe-Based Animation](https://doi.org/10.1145/3799902.3811157) | 指定したキーフレーム間の3Dキャラクター動作を補完する。補間と学習による合成を組み合わせた中割り手法。 | [animaj-lab/mib-ais](https://github.com/animaj-lab/mib-ais) · [コード条件](https://github.com/animaj-lab/mib-ais/blob/main/LICENSE) | [モデル](https://huggingface.co/AnimajSAS/AIS_BI_LSTM_v0) | AIS-BiLSTMの学習済みモデル。 |
| [Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation](https://doi.org/10.1145/3811284) | テキスト、移動経路、キーポーズ、関節の制約から3D人体モーションを対話的に生成する。 | [nv-tlabs/ardy](https://github.com/nv-tlabs/ardy) · [コード条件](https://github.com/nv-tlabs/ardy/blob/main/LICENSE) | [1](https://huggingface.co/nvidia/ARDY-Core-RP-20FPS-Horizon40) / [2](https://huggingface.co/nvidia/ARDY-Core-RP-20FPS-Horizon8) / [3](https://huggingface.co/nvidia/ARDY-G1-RP-25FPS-Horizon52) / [4](https://huggingface.co/nvidia/ARDY-G1-RP-25FPS-Horizon8) | ARDY。テキストエンコーダーのLlamaは申請が必要。 |
| [GPC: Large-Scale Generative Pretraining for Transferable Motor Control](https://doi.org/10.1145/3799902.3811038) | 大量の動作から汎用的な運動制御の事前知識を学び、物理シミュレーション内のキャラクター制御に転用する。 | [NVlabs/ProtoMotions](https://github.com/NVlabs/ProtoMotions) · [コード条件](https://github.com/NVlabs/ProtoMotions/blob/main/LICENSE.md) | [モデル](https://github.com/NVlabs/ProtoMotions/tree/main/data/pretrained_models/gpc_prior/soma_bones) | GPC priorの学習済みモデル。 |
| [Matérn Noise for Triangulation-Agnostic Flow Matching on Meshes](https://doi.org/10.1145/3811309) | メッシュの三角形分割に左右されにくい生成モデルで、形状上の変形などを扱う。異なるメッシュでの生成処理向け。 | [kts707/Matern-FM](https://github.com/kts707/Matern-FM) · [コード条件](https://github.com/kts707/Matern-FM/blob/main/LICENSE) | [モデル](https://github.com/kts707/Matern-FM/releases/tag/v1.0.0) | 6つの.ckptをGitHub Releasesで配布。 |
| [MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives](https://doi.org/10.1145/3811334) | 動作の生成と接続を、速度・方向・キーポーズなどで制御する。公開プレビューはG1骨格のリアルタイムデモを含む。 | [NVlabs/GR00T-WholeBodyControl](https://github.com/NVlabs/GR00T-WholeBodyControl/tree/main/motionbricks) · [コード条件](https://github.com/NVlabs/GR00T-WholeBodyControl/blob/main/LICENSE) | [モデル](https://github.com/NVlabs/GR00T-WholeBodyControl/tree/main/motionbricks/out) | プレビュー版。VQVAE・pose・rootの重みとG1デモ。 |
| [MUSIC: Learning Muscle-Driven Dexterous Hand Control](https://doi.org/10.1145/3811402) | 筋肉・腱を模した手のモデルを物理制御し、指の動作追従や両手のピアノ演奏を学習する。 | [xupei0610/music](https://github.com/xupei0610/music) · 条件はREADME参照 | [モデル](https://github.com/xupei0610/music/tree/main/pretrained) | joint・muscle_trackingの学習済みポリシーを同梱。 |
| [R-DMesh: Video-Guided 3D Animation via Rectified Dynamic Mesh Flow](https://doi.org/10.1145/3799902.3811135) | 静的な3Dメッシュを参照動画の初期ポーズに合わせ、動画に沿って動くメッシュ列を生成する。 | [Tencent-Hunyuan/R-DMesh](https://github.com/Tencent-Hunyuan/R-DMesh) · 条件はREADME参照 | [モデル](https://huggingface.co/JarrentWu/R-DMesh) | DVAEとRectified Flow。Wan2.2を併用。 |
| [SMP: Reusable Score-Matching Motion Priors for Physics-Based Character Control](https://doi.org/10.1145/3811282) | 動作データから再利用できるモーション事前分布を学び、物理キャラクターの自然な動作制御に使う。 | [xbpeng/MimicKit](https://github.com/xbpeng/MimicKit) · [コード条件](https://github.com/xbpeng/MimicKit/blob/main/LICENSE) | [モデル](https://1sfu-my.sharepoint.com/:u:/g/personal/xbpeng_sfu_ca/EclKq9pwdOBAl-17SogfMW0Bved4sodZBQ_5eZCiz9O--w?e=bqXBaa) | 公式配布アーカイブ内のモデル。SMPの設定はMimicKitに収録。 |
| [TopoCap: Learning Topology-Agnostic Motion Priors for Monocular Video-to-Animation](https://doi.org/10.1145/3799902.3811159) | 単眼動画から動作を読み取り、骨格構造が異なる3Dキャラクターへ移す。人型以外の骨格も対象。 | [czpcf/TopoCap](https://github.com/czpcf/TopoCap) · 条件はREADME参照 | [モデル](https://huggingface.co/duckduckplz/TopoCap) | VAE・Flowのモーションモデル。DINOv3は別途申請。 |

### 人体・顔・アバター（7件）

| 論文 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- |
| [EchoAvatar: Real-time Generative Avatar Animation from Audio Streams](https://doi.org/10.1145/3799902.3811066) | 入力音声ストリームから顔と身体の動きを生成し、Unityのアバターをリアルタイムに動かす。 | [RobinWitch/EchoAvatar](https://github.com/RobinWitch/EchoAvatar) · 条件はREADME参照 | [モデル](https://huggingface.co/robinwitch/EchoAvatar) | 音声駆動モデルとUnityパッケージ。 |
| [EgoForce: Forearm-Guided Camera-Space 3D Hand Pose from a Monocular Egocentric Camera](https://doi.org/10.1145/3799902.3811047) | 頭部に付けた単眼カメラの画像から、前腕の情報を利用して手の3D位置・姿勢・形状を推定する。 | [dfki-av/EgoForce](https://github.com/dfki-av/EgoForce) · 条件はREADME参照 | [モデル](https://huggingface.co/chris10/EgoForce) | モデル配布元は公式ダウンロードスクリプトで確認。 |
| [EgoRelight: Egocentric Human Capture and Illumination Recovery for Relightable and Photoreal Avatar Rendering](https://doi.org/10.1145/3811346) | 一人称視点の人物撮影と照明推定を組み合わせ、照明を変更して描画できる写実的なアバターを構築する。 | [jcjackch/EgoRelight](https://github.com/jcjackch/EgoRelight) · [コード条件](https://github.com/jcjackch/EgoRelight/blob/main/LICENSE) | [モデル](https://gvv-assets.mpi-inf.mpg.de/EgoRelight) | 配布サイトに登録・ログインが必要。被写体別重み等を配布。static-lighting appearance networkは未配布。 |
| [OmniHands: Robust Motion Capture of Interactive Hands via A Versatile Transformer](https://doi.org/10.1145/3807943) | 画像・動画・複数視点の入力から、接触や重なりのある両手の3D形状と動きを復元する。 | [LinDixuan/OmniHands](https://github.com/LinDixuan/OmniHands) · 条件はREADME参照 | [1](https://drive.google.com/file/d/1ZoP4qmYE8MyXCfhGK5meWWfBOYpy1VZ7/view) / [2](https://drive.google.com/file/d/1jLo7cFIWeDXep_hhvumWdm90QIwy_HwB/view) / [3](https://drive.google.com/file/d/10EZF6qLQuTyrxS0glP23HFOAdiLQ9gy7/view) | 画像・動画・複数視点の重み。MANOは別途利用条件あり。 |
| [Learning a Delighting Prior for Facial Appearance Capture in the Wild](https://doi.org/10.1145/3811303) | 顔の見た目から撮影時の照明や影の影響を取り除く。別の照明で描画する顔アセットの準備向け。 | [yxuhan/OpenDelight](https://github.com/yxuhan/OpenDelight) · [コード条件](https://github.com/yxuhan/OpenDelight/blob/main/LICENSE) | [モデル](https://drive.google.com/file/d/1bCIKOGNlKcGgObg5AeErUHkRTMuv0HHZ/view) | OpenDelight。配布モデルと論文内モデルの一致を著者が説明。 |
| [PEAR: Pixel-aligned Expressive humAn mesh Recovery](https://doi.org/10.1145/3799902.3811096) | 人物画像から身体・手・顔を含む表情豊かな3D人体メッシュのパラメータを推定する。 | [Pixel-Talk/PEAR](https://github.com/Pixel-Talk/PEAR) · [コード条件](https://github.com/Pixel-Talk/PEAR/blob/main/LICENSE.txt) | [モデル](https://huggingface.co/BestWJH/PEAR_models) | SMPL・SMPL-X・FLAMEには別途利用条件あり。 |
| [VFAvatar: Feed-Forward 3D Avatar Reconstruction from Casual Image Collections](https://doi.org/10.1145/3799902.3811171) | 日常的に撮った複数の人物画像から、アニメーション可能な3Dデジタルヒューマンを復元する。 | [huangshuo200823/VFAvatar](https://github.com/huangshuo200823/VFAvatar) · 条件はREADME参照 | [モデル](https://drive.google.com/file/d/18ITE4nXa0eYQqZueqnnzcLJQyNhhyHW7/view) | 事前学習済みアバター復元モデル。 |

### 動画生成・編集・リライティング（8件）

| 論文 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- |
| [Go-with-the-Track: Video Compositing and Motion Control with Point Tracking](https://doi.org/10.1145/3799902.3811093) | 動画内の点の軌跡を指定し、被写体の動きの制御や別動画への合成を行う。 | [Eyeline-Labs/Go-with-the-Track](https://github.com/Eyeline-Labs/Go-with-the-Track) · [コード条件](https://github.com/Eyeline-Labs/Go-with-the-Track/blob/main/LICENSE) | [モデル](https://huggingface.co/Eyeline-Labs/Go-with-the-Track) | 動画合成・モーション制御のモデル。 |
| [LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models](https://doi.org/10.1145/3799902.3811151) | イベントカメラの疎な信号から動画を復元し、将来フレームの予測や中間フレーム生成も行う。通常のRGB動画専用ではない。 | [cdfan0627/LongE2V](https://github.com/cdfan0627/LongE2V) · 条件はREADME参照 | [モデル](https://huggingface.co/fansam39/LongE2V) | LoRA重み。 |
| [MACE-Dance: Motion-Appearance Cascaded Experts for Music-Driven Dance Video Generation](https://doi.org/10.1145/3799902.3811202) | 音楽に合う3Dダンスと見た目の生成を分担してダンス動画を作る。配布重みはAppearance Expertが対象。 | [AMAP-ML/MACE-Dance](https://github.com/AMAP-ML/MACE-Dance) · 条件はREADME参照 | [モデル](https://huggingface.co/GD-ML/MACE-Dance) | Appearance Expertの重み。配布範囲はモデルカード参照。 |
| [MV-S2V: Multi-View Subject-Consistent Video Generation](https://doi.org/10.1145/3799902.3811131) | 同じ被写体の複数方向の参照画像から、視点が変わっても外観を保ちやすい動画を生成する。 | [Szy-Young/MV-S2V](https://github.com/Szy-Young/MV-S2V) · 条件はREADME参照 | [モデル](https://huggingface.co/youngsong305/MV-S2V) | 14Bモデル。Wan2.1のVAE・T5を併用。 |
| [OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation](https://doi.org/10.1145/3799902.3811180) | カメラ移動を制御しながら長い360度パノラマ動画を生成する。仮想空間を歩き回る映像の作成向け。 | [yuhengliu02/OmniRoam](https://github.com/yuhengliu02/OmniRoam) · [コード条件](https://github.com/yuhengliu02/OmniRoam/blob/main/LICENSE) | [モデル](https://huggingface.co/Yuheng02/OmniRoam) | Preview・Self-forcing・Refineの3段階モデル。 |
| [Relit-LiVE: Relight Video by Jointly Learning Environment Video](https://doi.org/10.1145/3799902.3811200) | 動画の照明を変更する。環境側の照明動画も同時に生成し、時間方向のちらつきや不整合を抑える。 | [zhuxing0/Relit-LiVE](https://github.com/zhuxing0/Relit-LiVE) · [コード条件](https://github.com/zhuxing0/Relit-LiVE/blob/main/LICENSE) | [モデル](https://huggingface.co/weiqingXiao/Relit-LiVE) | 画像・動画用の複数チェックポイント。 |
| [UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors](https://doi.org/10.1145/3811304) | 動画の色・材質・照明に関わる成分やアルファを扱い、成分の推定と条件付き動画生成を行う。 | [houyuanchen111/UniVidX](https://github.com/houyuanchen111/UniVidX) · [コード条件](https://github.com/houyuanchen111/UniVidX/blob/main/LICENSE) | [モデル](https://huggingface.co/houyuanchen/UniVidX) | UniVid-Intrinsic・UniVid-Alpha。 |
| [VFXMaster: Unlocking Dynamic Visual Effect Generation via In-Context Learning](https://doi.org/10.1145/3799902.3811208) | 見本のエフェクト動画を手掛かりに、別の画像へ同様の動的エフェクトを付けた動画を生成する。 | [libaolu312/VFXMaster](https://github.com/libaolu312/VFXMaster) · 条件はREADME参照 | [モデル](https://huggingface.co/8ruceLi/VFXMaster) | In-Context ConditioningとOne-shot Adaptationの重み。 |

### 画像生成・編集・材質（11件）

| 論文 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- |
| [BFS: Back-to-Front Layered Image Synthesis via Knowledge Transfer](https://doi.org/10.1145/3799902.3811228) | 画像を奥から手前へ透明度付きのレイヤーとして合成・生成する。後から部品を扱える画像制作向け。 | [kkang831/BFS_Release](https://github.com/kkang831/BFS_Release) · 条件はREADME参照 | [1](https://drive.google.com/file/d/1u4ZIz_MRvVDeJ9Qv4E2zLTPxMldy_TGP/view) / [2](https://drive.google.com/file/d/1AgxztNBgi2vYW4FKA3VTXESNxGUKWf4-/view) | Transparency VAEとBFSの配布ファイルを確認。FLUX.1-Fill-devには条件同意が必要。 |
| [BoxCtrl: 3D-Aware Visual Prompting for Geometric Image Editing](https://doi.org/10.1145/3799902.3811169) | 画像内の物体に3Dボックスを指定し、位置・大きさ・向きを幾何的に制御して画像を編集する。 | [beaglew/BoxCtrl](https://github.com/beaglew/BoxCtrl) · [コード条件](https://github.com/beaglew/BoxCtrl/blob/main/LICENSE) | [モデル](https://huggingface.co/wakalaka/BoxCtrl) | LoRA。FLUX.1-Kontext-devは条件同意が必要。 |
| [ComboStoc: Combinatorial Stochasticity for Diffusion Generative Models](https://doi.org/10.1145/3811285) | 画像の各次元や条件の組合せを多様に学習する拡散モデルの手法。制御付き生成の基盤研究向け。 | [Xrvitd/ComboStoc](https://github.com/Xrvitd/ComboStoc) · [コード条件](https://github.com/Xrvitd/ComboStoc/blob/main/LICENSE) | [モデル](https://drive.google.com/drive/folders/1EgIIbiN1Xup_wgjh1ksL2UV8_Qj2O1Pq) | XL/2・UNSYNC_ALL・800Kのモデル。 |
| [Controllable Texture Tiling via Diffusion Transformers with Transformed Rotary Embeddings](https://doi.org/10.1145/3799902.3811172) | 模様の配置・反復を制御しながらタイル状テクスチャを生成する。背景素材や繰り返し材質の作成向け。 | [Junrongh/ControlTile](https://github.com/Junrongh/ControlTile) · 条件はREADME参照 | [モデル](https://modelscope.cn/models/heika94/control-tile/summary) | ControlTile LoRA。 |
| [FIT: A Large-Scale Dataset for Fit-Aware Virtual Try-On](https://doi.org/10.1145/3799902.3811168) | 身体と衣服のサイズ関係を扱う試着データセット。公開モデルはシミュレーション画像を写実化するデータ生成用LoRA。 | [HarryWang355/FIT-VTO](https://github.com/HarryWang355/FIT-VTO) · 条件はREADME参照 | [モデル](https://huggingface.co/Yuanhao-Harry-Wang/FIT-sim2real) | 公開モデルはデータ生成用Sim2Real LoRA。 |
| [HairPort: In-context 3D-aware Hair Import and Transfer for Images](https://doi.org/10.1145/3799902.3811046) | 参照する髪型を顔画像へ移す。3Dの向きと大きさを合わせ、公開LoRAで元の髪を除く前処理も行う。 | [deepmancer/HairPort](https://github.com/deepmancer/HairPort) · [コード条件](https://github.com/deepmancer/HairPort/blob/main/LICENSE) | [モデル](https://huggingface.co/deepmancer/bald_konverter) | Bald Converter LoRA。FLUX.1-Kontext等の依存モデルあり。 |
| [LUCID: Learning Unified Control for Image Deflaring and Exposure Mastery in Nighttime Photography](https://doi.org/10.1145/3799902.3811133) | 夜景写真の露出不足、光のフレア、ゴーストなどを調整する。照明表現を制御できる画像修復。 | [frakenation/LUCID](https://github.com/frakenation/LUCID) · 条件はREADME参照 | [モデル](https://huggingface.co/OpticAI/LUCID) | flare分離・restorationモデル。 |
| [MAOAM: Unified Object and Material Selection with Vision-Language Models](https://doi.org/10.1145/3799902.3811186) | テキストやクリックで画像中の物体・材質を選択し、マスクを作る。部分的な編集や材質変更の準備向け。 | [adobe-research/obj-and-mat-selection](https://github.com/adobe-research/obj-and-mat-selection) · [コード条件](https://github.com/adobe-research/obj-and-mat-selection/blob/master/LICENSE) | [モデル](https://huggingface.co/jpark677/maoam_ckpts) | 物体・材質選択モデル。 |
| [See-through: Single-image Layer Decomposition for Anime Characters](https://doi.org/10.1145/3799902.3811209) | 1枚のアニメ絵を髪・顔・目・服などの補完済みレイヤーに分け、重なり順を推定する。2.5Dアニメの素材準備向け。 | [shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through) · [コード条件](https://github.com/shitagaki-lab/see-through/blob/main/LICENSE) | [1](https://huggingface.co/layerdifforg/seethroughv0.0.2_layerdiff3d) / [2](https://huggingface.co/24yearsold/seethroughv0.0.1_marigold) / [3](https://huggingface.co/24yearsold/l2d_sam_iter2) | レイヤー生成・深度・部位分割モデル。 |
| [StyleID: A Perception-Aware Dataset and Metric for Stylization-Agnostic Facial Identity Recognition](https://doi.org/10.1145/3811360) | 画風が変わった顔同士でも同一人物らしさを測る特徴量を抽出する。キャラクター外観の比較・検索・評価向け。 | [kwanyun/StyleID](https://github.com/kwanyun/StyleID) · 条件はREADME参照 | [モデル](https://huggingface.co/kwanY/styleid) | 顔IDエンコーダー。 |
| [VeraRetouch: A Lightweight Fully Differentiable Framework for Multi-Task Reasoning Photo Retouching](https://doi.org/10.1145/3799902.3811065) | 画像の内容や指示に応じて色・明るさなどをレタッチする。軽量な処理で写真の仕上げを支援する。 | [OpenVeraTeam/VeraRetouch](https://github.com/OpenVeraTeam/VeraRetouch) · [コード条件](https://github.com/OpenVeraTeam/VeraRetouch/blob/main/LICENSE) | [1](https://huggingface.co/Gyh68/VeraRetouch) / [2](https://huggingface.co/Gyh68/VeraRetouch.Encoder_Renderer) | レタッチモデルとEncoder-Renderer。 |

### 光学・レンダリング・VFX（4件）

| 論文 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- |
| [8DNA: 8D Neural Asset Light Transport by Distribution Learning](https://doi.org/10.1145/3799902.3811094) | 3Dアセット内部の光の伝わり方を学習済みモデルで表し、複雑な光輸送の描画に利用する。 | [lwwu2/8dna26](https://github.com/lwwu2/8dna26) · 条件はREADME参照 | [モデル](https://drive.google.com/file/d/1WeYpquFoDTZzbwpHotiwIRwKdBskULcY/view) | アセット別の学習済みlight-transportモデル。 |
| [Guidestar-Free Adaptive Optics with Asymmetric Apertures](https://doi.org/10.1145/3809501) | 非対称な開口と学習モデルを使い、基準となる光点なしで光学収差を推定・補正する。撮像装置寄りの研究。 | [WeiyunJiang/guidestar-free-ao](https://github.com/WeiyunJiang/guidestar-free-ao) · [コード条件](https://github.com/WeiyunJiang/guidestar-free-ao/blob/main/LICENSE) | [モデル](https://drive.google.com/file/d/1e2GxutCBGbDSLIHtMcvRMSlsKAqJVtYH/view) | Places2で学習したモデル群。 |
| [Neural Quadrature Rule and Autoregressive Adaptive Sampling](https://doi.org/10.1145/3811318) | 数値積分の評価点や重みを学習し、照明・透過率などの計算を効率化する。レンダラー開発の基盤技術。 | [SuikaSibyl/nqr](https://github.com/SuikaSibyl/nqr) · 条件はREADME参照 | [モデル](https://drive.google.com/file/d/1gydL15reAH7DDNNiieg5VnS8oe0HqGDT/view) | 配布アーカイブにscenesとckpt。 |
| [VfxDB: A Visual Effects Volume Dataset and Benchmark for VDB-Native Generative Modeling](https://doi.org/10.1145/3799902.3811178) | 煙などのVFXボリュームを扱うデータセットと生成モデル。VDB形式を意識した立体エフェクト素材の生成向け。 | [VfxDB-Official/VfxDB](https://github.com/VfxDB-Official/VfxDB) · 条件はREADME参照 | [モデル](https://huggingface.co/ryogishiki/VfxDB-models) | 論文用EMAチェックポイントを配布。 |

### 音声・吹き替え（2件）

| 論文 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- |
| [Audio-Omni: Extending Multi-modal Understanding to Versatile Audio Generation and Editing](https://doi.org/10.1145/3799902.3811191) | 効果音・音楽・音声を対象に、内容の理解、生成、指示による編集を統一的に行う。 | [ZeyueT/Audio-Omni](https://github.com/ZeyueT/Audio-Omni) · [コード条件](https://github.com/ZeyueT/Audio-Omni/blob/main/LICENSE) | [モデル](https://huggingface.co/HKUSTAudio/Audio-Omni) | 音声生成・編集モデル。 |
| [Just-Dub-It: Video dubbing via Joint Audio-Visual Diffusion](https://doi.org/10.1145/3799902.3811061) | 元動画に別の発話音声を合わせ、口の動きと音声を整合させる吹き替え手法。 | [justdubit/just-dub-it](https://github.com/justdubit/just-dub-it) · [コード条件](https://github.com/justdubit/just-dub-it/blob/main/LICENSE) | [モデル](https://huggingface.co/justdubit/justdubit) | HFで条件への同意が必要。 旧実装はarchived。[LTX2.3対応の移行先](https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-pipelines#10-lipdubpipeline)あり。この行のモデル確認記録は既存の配布版。 |

## 未掲載候補の扱い

SATO、FLASHand、VideoNeuMat、HumanFlowなどは、コードまたは専用モデルの公開が確認できないため掲載していません。Prox-E、FreeOrbit4D、LayerInbetween、StudioRecon、GimmBOのような既存モデルを利用する手法は、本研究の学習済み重みの配布一覧には数えていません。これらの公式リンクと個別の理由は[確認した未掲載候補](reviewed-not-included.json)で参照できます。未掲載は「非公開である」と断定するものではありません。

## 照合に使った索引

- [SIGGRAPH 2026公式Technical Papers](https://s2026.siggraph.org/program/technical-papers/)
- [SIGGRAPH 2026公式スケジュール](https://s2026.conference-schedule.org/?filter1=sstype132)
- [ACM SIGGRAPH 2026 Conference Proceedings](https://doi.org/10.1145/3799902)
- [ACM TOG Volume 45 Issue 4](https://dl.acm.org/toc/tog/2026/45/4)
- [DBLP: SIGGRAPH 2026 Conference Paper Track](https://dblp.org/db/conf/siggraph/siggraph2026.html)
- [Jiong Chen: セッション別論文一覧](https://jiongchen.github.io/siggraph-2026-technical-papers/)
- [Ke-Sen Huang: SIGGRAPH 2026 papers](https://www.realtimerendering.com/kesen/sig2026.html)

掲載判断の根拠は索引だけでなく、各行の著者リポジトリ・モデル配布元を使用しています。このリポジトリはリンクとメタデータのみを収録し、論文本文・コード本体・モデル重みを転載していません。
