# SIGGRAPH 2026 — 論文・公式コード・公開モデル

SIGGRAPH 2026のTechnical Papersから、**公式実装と学習済みモデルの配布を確認した66件**をまとめたリンク集です。最終確認日: **2026-09-06**。

[JSON](papers.json) · [CSV](papers.csv) · [確認した未掲載候補](reviewed-not-included.json)

## 掲載基準と確認範囲

- Conference / Journalトラックと、SIGGRAPH 2026で発表されたTOG論文を対象とします。SIGGRAPH Asia、ポスター、講習、非公式再実装は対象外です。
- 著者の公式実装が存在し、本研究で配布する学習済み重み・LoRA・ポリシー・同梱ネットワークにアクセスできることを確認しています。部分公開は備考で範囲を明示します。
- 登録や利用条件への同意を要する配布も含みます。「公開」は無条件利用や商用利用の許可を意味しません。コードの条件とモデルの条件はそれぞれのリンク先を確認してください。
- コードのファイル一覧、HFのモデルファイル一覧、GitHub Releases、外部配布ページ・ダウンロード応答を確認しました。重み全体のダウンロードや推論・再現実験は実施していません。
- セッション別一覧、会議録索引、TOG索引と著者の公開ページを突き合わせた確認時点の一覧です。未発見・未索引の公開物まで含めた完全網羅は保証しません。「Coming soon」や専用重みを確認できないものを公開済み件数に含めていません。

各項目の確認日、コードのコミット、モデルのリビジョン・確認ファイル・根拠URLは[JSON](papers.json)に記録しています。ファイル一覧での確認と実行検証を区別し、Git LFSのオブジェクトIDはモデル本体のチェックサムとして扱っていません。

## 分野別一覧

### 3D生成・CAD・幾何処理（18件）

| 論文 | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- |
| [AniGen: Unified S³ Fields for Animatable 3D Asset Generation](https://doi.org/10.1145/3811297) | [VAST-AI-Research/AniGen](https://github.com/VAST-AI-Research/AniGen) · [コード条件](https://github.com/VAST-AI-Research/AniGen/blob/main/LICENSE) | [モデル](https://huggingface.co/VAST-AI/AniGen) | DAE・Flowなどを配布。 |
| [B-repLer: Language-guided Editing of CAD Models](https://doi.org/10.1145/3799902.3811166) | [yilinliu77/Brepler](https://github.com/yilinliu77/Brepler) · 条件はREADME参照 | [モデル](https://www.dropbox.com/scl/fi/38klqe5hdomc6t9xbiv84/brepler_ckpt.zip?rlkey=ebo0oabf6p1zkxnt0eamkj976&dl=0) | 編集モデルとHoLa VAE。 |
| [CubePart: An Open-Vocabulary Part-Controllable 3D Generator](https://doi.org/10.1145/3799902.3811117) | [Roblox/cube](https://github.com/Roblox/cube/tree/main/cubepart) · [コード条件](https://github.com/Roblox/cube/blob/main/LICENSE) | [モデル](https://huggingface.co/Roblox/cubepart) | 公開部分はmulti-part mesh decompositionとshape VAE。 |
| [DeepMill++: Neural Guidance Meets Rasterization for Efficient Accessibility Analysis](https://doi.org/10.1145/3799902.3811091) | [YaoZhang-666/DeepMillPlusPlus](https://github.com/YaoZhang-666/DeepMillPlusPlus) · 条件はREADME参照 | [モデル](https://github.com/YaoZhang-666/DeepMillPlusPlus/tree/main/DeepM/pretrained) | DeepMモデル。Git LFS配布。 |
| [DualBrep: A Dual-Field Continuous Representation for B-rep Modelling](https://doi.org/10.1145/3799902.3811057) | [AutodeskAILab/DualBrep](https://github.com/AutodeskAILab/DualBrep) · 条件はREADME参照 | [モデル](https://huggingface.co/ADSKAILab/DualBrep) | checkpoints.zipにVAE・Flow・parametrizer。 |
| [InfiniteDiffusion: Bridging Learned Fidelity and Procedural Utility for Open-World Terrain Generation](https://doi.org/10.1145/3799902.3811080) | [xandergos/terrain-diffusion](https://github.com/xandergos/terrain-diffusion) · [コード条件](https://github.com/xandergos/terrain-diffusion/blob/master/LICENSE) | [モデル](https://huggingface.co/collections/xandergos/terrain-diffusion) | Terrain Diffusionのモデル群。論文の旧題との重複を統合。 |
| [MeshFlow: Mesh Generation with Equivariant Flow Matching](https://doi.org/10.1145/3799902.3811195) | [qiisun/MeshFlow](https://github.com/qiisun/MeshFlow) · 条件はREADME参照 | [モデル](https://huggingface.co/datasets/qsun2001/meshflow/tree/main/v1) | ShapeNetの4カテゴリの重み。配布先はHF datasetリポジトリ。 |
| [Learning Laplacian Eigenspace with Mass-Aware Neural Operators on Point Clouds](https://doi.org/10.1145/3799902.3811185) | [Adversarr/NEO](https://github.com/Adversarr/NEO) · 条件はREADME参照 | [モデル](https://drive.google.com/drive/folders/12026qTECiGywESPz6WSbpgD8BPMd41Ha) | NEOの学習済み重み。 |
| [Neural Particle Automata: Learning Self-Organizing Particle Dynamics](https://doi.org/10.1145/3799902.3811052) | [TheDevilWillBeBee/NPA](https://github.com/TheDevilWillBeBee/NPA) · 条件はREADME参照 | [モデル](https://github.com/TheDevilWillBeBee/NPA/tree/main/data/pretrained) | lizard・polka_dottedの学習済みモデル。 |
| [NeuralSketch2Surf: Fast Neural Surfacing of Unoriented 3D Sketches](https://doi.org/10.1145/3799902.3811227) | [Hongsheng-Y/NeuralSketch2Surf](https://github.com/Hongsheng-Y/NeuralSketch2Surf) · 条件はREADME参照 | [モデル](https://huggingface.co/HongshengY/S2V_Net) | TorchScript/PyTorchチェックポイント。 |
| [Pixal3D: Pixel-Aligned 3D Generation from Images](https://doi.org/10.1145/3799902.3811175) | [TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D) · [コード条件](https://github.com/TencentARC/Pixal3D/blob/master/LICENSE) | [モデル](https://huggingface.co/TencentARC/Pixal3D) | 論文再現用は paper ブランチ。最新実装と区別。 |
| [Points as Tori: Fast Pointwise Signed Distance for Point Clouds](https://doi.org/10.1145/3811385) | [nzfeng/points-as-tori](https://github.com/nzfeng/points-as-tori) · [コード条件](https://github.com/nzfeng/points-as-tori/blob/main/LICENSE) | [モデル](https://github.com/nzfeng/points-as-tori/tree/main/src/pointsastori/models) | 小規模な学習済みネットワークを同梱。 |
| [Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction](https://doi.org/10.1145/3799902.3811124) | [Cornell-VAILab/Raster2Seq](https://github.com/Cornell-VAILab/Raster2Seq) · [コード条件](https://github.com/Cornell-VAILab/Raster2Seq/blob/master/LICENSE) | [モデル](https://huggingface.co/haopt/Raster2Seq) | 床面図復元モデル。 |
| [SegviGen: Repurposing 3D Generative Model for Part Segmentation](https://doi.org/10.1145/3811399) | [Nelipot-Lee/SegviGen](https://github.com/Nelipot-Lee/SegviGen) · [コード条件](https://github.com/Nelipot-Lee/SegviGen/blob/main/LICENSE) | [モデル](https://huggingface.co/fenghora/SegviGen) | 部分指定・全体分割・2D誘導の重みを配布。 |
| [SimArt: Decomposing Monolithic Meshes into Sim-ready Articulated Assets via MLLM](https://doi.org/10.1145/3799902.3811173) | [ByteDance-Seed/SimArt](https://github.com/ByteDance-Seed/SimArt) · [コード条件](https://github.com/ByteDance-Seed/SimArt/blob/main/LICENSE) | [モデル](https://huggingface.co/ByteDance-Seed/SimArt) | MLLMとVQ-VAEの重み。 |
| [SQuadGen: Generating Simple Quad Layouts via Chart Distance Fields](https://doi.org/10.1145/3811348) | [microsoft/SQuadGen](https://github.com/microsoft/SQuadGen) · [コード条件](https://github.com/microsoft/SQuadGen/blob/main/LICENSE) | [モデル](https://huggingface.co/microsoft/SQuadGen) | SQ-VAE・Geom-AE・SQDiffuse。 |
| [SuperSDF: Sparse SDF Super-Resolution for Surface Extraction](https://doi.org/10.1145/3799902.3811176) | [Sagar160/SSU](https://github.com/Sagar160/SSU) · [コード条件](https://github.com/Sagar160/SSU/blob/main/LICENSE) | [モデル](https://github.com/Sagar160/SSU/tree/main/run/data) | リポジトリ内にモデル重みを収録。 |
| [Generative 3D Gaussians with Learned Density Control](https://doi.org/10.1145/3799902.3811130) | [runjie-yan/TripoSplat-Training](https://github.com/runjie-yan/TripoSplat-Training) · [コード条件](https://github.com/runjie-yan/TripoSplat-Training/blob/master/LICENSE) | [モデル](https://huggingface.co/VAST-AI/TripoSplat) | TripoSplat。DINOv3等の依存モデルには別途アクセス条件あり。 |

### 3D復元・理解（7件）

| 論文 | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- |
| [ArtiFixer: Enhancing and Extending 3D Reconstruction with Auto-Regressive Diffusion Models](https://doi.org/10.1145/3799902.3811060) | [nv-tlabs/ArtiFixer](https://github.com/nv-tlabs/ArtiFixer) · [コード条件](https://github.com/nv-tlabs/ArtiFixer/blob/main/LICENSE) | [モデル](https://huggingface.co/nvidia/ArtiFixer) | 1.3B・14B。Wanベースモデルが別途必要。 |
| [GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction](https://doi.org/10.1145/3799902.3811222) | [Xiaoc7/GeoQuery](https://github.com/Xiaoc7/GeoQuery) · [コード条件](https://github.com/Xiaoc7/GeoQuery/blob/main/LICENSE) | [モデル](https://huggingface.co/DIG-UESTC/GeoQuery) | 拡散refinerの重み。 |
| [MegaNorm: Local Patch Embeddings for Efficient and Robust Point Normal Orientation at Super-Large Scale](https://doi.org/10.1145/3799902.3811139) | [zd-lee/MegaNorm](https://github.com/zd-lee/MegaNorm) · 条件はREADME参照 | [モデル](https://huggingface.co/wlbbbbb/meganorm) | patchnet等の重み。 |
| [Mix3R: Mixing Feed-forward Reconstruction and Generative 3D Priors for Joint Multi-view Aligned 3D Reconstruction and Pose Estimation](https://doi.org/10.1145/3799902.3811152) | [jsnln/mix3r](https://github.com/jsnln/mix3r) · 条件はREADME参照 | [モデル](https://modelscope.cn/models/jsnln00/mix3r) | V1が論文版、V2が会議後の更新版。 |
| [MTPano: Multi-Task Panoramic Scene Understanding via Label-Free Integration of Dense Prediction Priors](https://doi.org/10.1145/3799902.3811193) | [Evergreen0929/MTPano](https://github.com/Evergreen0929/MTPano) · 条件はREADME参照 | [モデル](https://huggingface.co/jdzhang0929/MTPano) | 140k・408kチェックポイント。 |
| [PointLLM-R: Enhancing 3D Point Cloud Reasoning via Chain-of-Thought](https://doi.org/10.1145/3799902.3811081) | [Xqle/PointLLM-R](https://github.com/Xqle/PointLLM-R) · [コード条件](https://github.com/Xqle/PointLLM-R/blob/master/LICENSE) | [モデル](https://huggingface.co/QileXu/PointLLM-R-7B) | 7Bモデル。 |
| [TrajVG: 3D Trajectory-Coupled Visual Geometry Learning](https://doi.org/10.1145/3799902.3811184) | [xingy038/TrajVG](https://github.com/xingy038/TrajVG) · [コード条件](https://github.com/xingy038/TrajVG/blob/main/LICENSE) | [モデル](https://drive.google.com/file/d/1vk27rkLPJrYVUgD7tCFw2ti5NQLYk2PK/view) | 3D軌跡と幾何復元の学習済みモデル。 |

### モーション・アニメーション（9件）

| 論文 | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- |
| [Adaptive Interpolation-Synthesis for Motion In-Betweening on Keyframe-Based Animation](https://doi.org/10.1145/3799902.3811157) | [animaj-lab/mib-ais](https://github.com/animaj-lab/mib-ais) · [コード条件](https://github.com/animaj-lab/mib-ais/blob/main/LICENSE) | [モデル](https://huggingface.co/AnimajSAS/AIS_BI_LSTM_v0) | AIS-BiLSTMの学習済みモデル。 |
| [Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation](https://doi.org/10.1145/3811284) | [nv-tlabs/ardy](https://github.com/nv-tlabs/ardy) · [コード条件](https://github.com/nv-tlabs/ardy/blob/main/LICENSE) | [1](https://huggingface.co/nvidia/ARDY-Core-RP-20FPS-Horizon40) / [2](https://huggingface.co/nvidia/ARDY-Core-RP-20FPS-Horizon8) / [3](https://huggingface.co/nvidia/ARDY-G1-RP-25FPS-Horizon52) / [4](https://huggingface.co/nvidia/ARDY-G1-RP-25FPS-Horizon8) | ARDY。テキストエンコーダーのLlamaは申請が必要。 |
| [GPC: Large-Scale Generative Pretraining for Transferable Motor Control](https://doi.org/10.1145/3799902.3811038) | [NVlabs/ProtoMotions](https://github.com/NVlabs/ProtoMotions) · [コード条件](https://github.com/NVlabs/ProtoMotions/blob/main/LICENSE.md) | [モデル](https://github.com/NVlabs/ProtoMotions/tree/main/data/pretrained_models/gpc_prior/soma_bones) | GPC priorの学習済みモデル。 |
| [Matérn Noise for Triangulation-Agnostic Flow Matching on Meshes](https://doi.org/10.1145/3811309) | [kts707/Matern-FM](https://github.com/kts707/Matern-FM) · [コード条件](https://github.com/kts707/Matern-FM/blob/main/LICENSE) | [モデル](https://github.com/kts707/Matern-FM/releases/tag/v1.0.0) | 6つの.ckptをGitHub Releasesで配布。 |
| [MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives](https://doi.org/10.1145/3811334) | [NVlabs/GR00T-WholeBodyControl](https://github.com/NVlabs/GR00T-WholeBodyControl/tree/main/motionbricks) · [コード条件](https://github.com/NVlabs/GR00T-WholeBodyControl/blob/main/LICENSE) | [モデル](https://github.com/NVlabs/GR00T-WholeBodyControl/tree/main/motionbricks/out) | プレビュー版。VQVAE・pose・rootの重みとG1デモ。 |
| [MUSIC: Learning Muscle-Driven Dexterous Hand Control](https://doi.org/10.1145/3811402) | [xupei0610/music](https://github.com/xupei0610/music) · 条件はREADME参照 | [モデル](https://github.com/xupei0610/music/tree/main/pretrained) | joint・muscle_trackingの学習済みポリシーを同梱。 |
| [R-DMesh: Video-Guided 3D Animation via Rectified Dynamic Mesh Flow](https://doi.org/10.1145/3799902.3811135) | [Tencent-Hunyuan/R-DMesh](https://github.com/Tencent-Hunyuan/R-DMesh) · 条件はREADME参照 | [モデル](https://huggingface.co/JarrentWu/R-DMesh) | DVAEとRectified Flow。Wan2.2を併用。 |
| [SMP: Reusable Score-Matching Motion Priors for Physics-Based Character Control](https://doi.org/10.1145/3811282) | [xbpeng/MimicKit](https://github.com/xbpeng/MimicKit) · [コード条件](https://github.com/xbpeng/MimicKit/blob/main/LICENSE) | [モデル](https://1sfu-my.sharepoint.com/:u:/g/personal/xbpeng_sfu_ca/EclKq9pwdOBAl-17SogfMW0Bved4sodZBQ_5eZCiz9O--w?e=bqXBaa) | 公式配布アーカイブ内のモデル。SMPの設定はMimicKitに収録。 |
| [TopoCap: Learning Topology-Agnostic Motion Priors for Monocular Video-to-Animation](https://doi.org/10.1145/3799902.3811159) | [czpcf/TopoCap](https://github.com/czpcf/TopoCap) · 条件はREADME参照 | [モデル](https://huggingface.co/duckduckplz/TopoCap) | VAE・Flowのモーションモデル。DINOv3は別途申請。 |

### 人体・顔・アバター（7件）

| 論文 | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- |
| [EchoAvatar: Real-time Generative Avatar Animation from Audio Streams](https://doi.org/10.1145/3799902.3811066) | [RobinWitch/EchoAvatar](https://github.com/RobinWitch/EchoAvatar) · 条件はREADME参照 | [モデル](https://huggingface.co/robinwitch/EchoAvatar) | 音声駆動モデルとUnityパッケージ。 |
| [EgoForce: Forearm-Guided Camera-Space 3D Hand Pose from a Monocular Egocentric Camera](https://doi.org/10.1145/3799902.3811047) | [dfki-av/EgoForce](https://github.com/dfki-av/EgoForce) · 条件はREADME参照 | [モデル](https://huggingface.co/chris10/EgoForce) | モデル配布元は公式ダウンロードスクリプトで確認。 |
| [EgoRelight: Egocentric Human Capture and Illumination Recovery for Relightable and Photoreal Avatar Rendering](https://doi.org/10.1145/3811346) | [jcjackch/EgoRelight](https://github.com/jcjackch/EgoRelight) · [コード条件](https://github.com/jcjackch/EgoRelight/blob/main/LICENSE) | [モデル](https://gvv-assets.mpi-inf.mpg.de/EgoRelight) | 配布サイトに登録・ログインが必要。被写体別重み等を配布。static-lighting appearance networkは未配布。 |
| [OmniHands: Robust Motion Capture of Interactive Hands via A Versatile Transformer](https://doi.org/10.1145/3807943) | [LinDixuan/OmniHands](https://github.com/LinDixuan/OmniHands) · 条件はREADME参照 | [1](https://drive.google.com/file/d/1ZoP4qmYE8MyXCfhGK5meWWfBOYpy1VZ7/view) / [2](https://drive.google.com/file/d/1jLo7cFIWeDXep_hhvumWdm90QIwy_HwB/view) / [3](https://drive.google.com/file/d/10EZF6qLQuTyrxS0glP23HFOAdiLQ9gy7/view) | 画像・動画・複数視点の重み。MANOは別途利用条件あり。 |
| [Learning a Delighting Prior for Facial Appearance Capture in the Wild](https://doi.org/10.1145/3811303) | [yxuhan/OpenDelight](https://github.com/yxuhan/OpenDelight) · [コード条件](https://github.com/yxuhan/OpenDelight/blob/main/LICENSE) | [モデル](https://drive.google.com/file/d/1bCIKOGNlKcGgObg5AeErUHkRTMuv0HHZ/view) | OpenDelight。配布モデルと論文内モデルの一致を著者が説明。 |
| [PEAR: Pixel-aligned Expressive humAn mesh Recovery](https://doi.org/10.1145/3799902.3811096) | [Pixel-Talk/PEAR](https://github.com/Pixel-Talk/PEAR) · [コード条件](https://github.com/Pixel-Talk/PEAR/blob/main/LICENSE.txt) | [モデル](https://huggingface.co/BestWJH/PEAR_models) | SMPL・SMPL-X・FLAMEには別途利用条件あり。 |
| [VFAvatar: Feed-Forward 3D Avatar Reconstruction from Casual Image Collections](https://doi.org/10.1145/3799902.3811171) | [huangshuo200823/VFAvatar](https://github.com/huangshuo200823/VFAvatar) · 条件はREADME参照 | [モデル](https://drive.google.com/file/d/18ITE4nXa0eYQqZueqnnzcLJQyNhhyHW7/view) | 事前学習済みアバター復元モデル。 |

### 動画生成・編集・リライティング（8件）

| 論文 | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- |
| [Go-with-the-Track: Video Compositing and Motion Control with Point Tracking](https://doi.org/10.1145/3799902.3811093) | [Eyeline-Labs/Go-with-the-Track](https://github.com/Eyeline-Labs/Go-with-the-Track) · [コード条件](https://github.com/Eyeline-Labs/Go-with-the-Track/blob/main/LICENSE) | [モデル](https://huggingface.co/Eyeline-Labs/Go-with-the-Track) | 動画合成・モーション制御のモデル。 |
| [LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models](https://doi.org/10.1145/3799902.3811151) | [cdfan0627/LongE2V](https://github.com/cdfan0627/LongE2V) · 条件はREADME参照 | [モデル](https://huggingface.co/fansam39/LongE2V) | LoRA重み。 |
| [MACE-Dance: Motion-Appearance Cascaded Experts for Music-Driven Dance Video Generation](https://doi.org/10.1145/3799902.3811202) | [AMAP-ML/MACE-Dance](https://github.com/AMAP-ML/MACE-Dance) · 条件はREADME参照 | [モデル](https://huggingface.co/GD-ML/MACE-Dance) | Appearance Expertの重み。配布範囲はモデルカード参照。 |
| [MV-S2V: Multi-View Subject-Consistent Video Generation](https://doi.org/10.1145/3799902.3811131) | [Szy-Young/MV-S2V](https://github.com/Szy-Young/MV-S2V) · 条件はREADME参照 | [モデル](https://huggingface.co/youngsong305/MV-S2V) | 14Bモデル。Wan2.1のVAE・T5を併用。 |
| [OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation](https://doi.org/10.1145/3799902.3811180) | [yuhengliu02/OmniRoam](https://github.com/yuhengliu02/OmniRoam) · [コード条件](https://github.com/yuhengliu02/OmniRoam/blob/main/LICENSE) | [モデル](https://huggingface.co/Yuheng02/OmniRoam) | Preview・Self-forcing・Refineの3段階モデル。 |
| [Relit-LiVE: Relight Video by Jointly Learning Environment Video](https://doi.org/10.1145/3799902.3811200) | [zhuxing0/Relit-LiVE](https://github.com/zhuxing0/Relit-LiVE) · [コード条件](https://github.com/zhuxing0/Relit-LiVE/blob/main/LICENSE) | [モデル](https://huggingface.co/weiqingXiao/Relit-LiVE) | 画像・動画用の複数チェックポイント。 |
| [UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors](https://doi.org/10.1145/3811304) | [houyuanchen111/UniVidX](https://github.com/houyuanchen111/UniVidX) · [コード条件](https://github.com/houyuanchen111/UniVidX/blob/main/LICENSE) | [モデル](https://huggingface.co/houyuanchen/UniVidX) | UniVid-Intrinsic・UniVid-Alpha。 |
| [VFXMaster: Unlocking Dynamic Visual Effect Generation via In-Context Learning](https://doi.org/10.1145/3799902.3811208) | [libaolu312/VFXMaster](https://github.com/libaolu312/VFXMaster) · 条件はREADME参照 | [モデル](https://huggingface.co/8ruceLi/VFXMaster) | In-Context ConditioningとOne-shot Adaptationの重み。 |

### 画像生成・編集・材質（11件）

| 論文 | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- |
| [BFS: Back-to-Front Layered Image Synthesis via Knowledge Transfer](https://doi.org/10.1145/3799902.3811228) | [kkang831/BFS_Release](https://github.com/kkang831/BFS_Release) · 条件はREADME参照 | [1](https://drive.google.com/file/d/1u4ZIz_MRvVDeJ9Qv4E2zLTPxMldy_TGP/view) / [2](https://drive.google.com/file/d/1AgxztNBgi2vYW4FKA3VTXESNxGUKWf4-/view) | Transparency VAEとBFSの配布ファイルを確認。FLUX.1-Fill-devには条件同意が必要。 |
| [BoxCtrl: 3D-Aware Visual Prompting for Geometric Image Editing](https://doi.org/10.1145/3799902.3811169) | [beaglew/BoxCtrl](https://github.com/beaglew/BoxCtrl) · [コード条件](https://github.com/beaglew/BoxCtrl/blob/main/LICENSE) | [モデル](https://huggingface.co/wakalaka/BoxCtrl) | LoRA。FLUX.1-Kontext-devは条件同意が必要。 |
| [ComboStoc: Combinatorial Stochasticity for Diffusion Generative Models](https://doi.org/10.1145/3811285) | [Xrvitd/ComboStoc](https://github.com/Xrvitd/ComboStoc) · [コード条件](https://github.com/Xrvitd/ComboStoc/blob/main/LICENSE) | [モデル](https://drive.google.com/drive/folders/1EgIIbiN1Xup_wgjh1ksL2UV8_Qj2O1Pq) | XL/2・UNSYNC_ALL・800Kのモデル。 |
| [Controllable Texture Tiling via Diffusion Transformers with Transformed Rotary Embeddings](https://doi.org/10.1145/3799902.3811172) | [Junrongh/ControlTile](https://github.com/Junrongh/ControlTile) · 条件はREADME参照 | [モデル](https://modelscope.cn/models/heika94/control-tile/summary) | ControlTile LoRA。 |
| [FIT: A Large-Scale Dataset for Fit-Aware Virtual Try-On](https://doi.org/10.1145/3799902.3811168) | [HarryWang355/FIT-VTO](https://github.com/HarryWang355/FIT-VTO) · 条件はREADME参照 | [モデル](https://huggingface.co/Yuanhao-Harry-Wang/FIT-sim2real) | 公開モデルはデータ生成用Sim2Real LoRA。 |
| [HairPort: In-context 3D-aware Hair Import and Transfer for Images](https://doi.org/10.1145/3799902.3811046) | [deepmancer/HairPort](https://github.com/deepmancer/HairPort) · [コード条件](https://github.com/deepmancer/HairPort/blob/main/LICENSE) | [モデル](https://huggingface.co/deepmancer/bald_konverter) | Bald Converter LoRA。FLUX.1-Kontext等の依存モデルあり。 |
| [LUCID: Learning Unified Control for Image Deflaring and Exposure Mastery in Nighttime Photography](https://doi.org/10.1145/3799902.3811133) | [frakenation/LUCID](https://github.com/frakenation/LUCID) · 条件はREADME参照 | [モデル](https://huggingface.co/OpticAI/LUCID) | flare分離・restorationモデル。 |
| [MAOAM: Unified Object and Material Selection with Vision-Language Models](https://doi.org/10.1145/3799902.3811186) | [adobe-research/obj-and-mat-selection](https://github.com/adobe-research/obj-and-mat-selection) · [コード条件](https://github.com/adobe-research/obj-and-mat-selection/blob/master/LICENSE) | [モデル](https://huggingface.co/jpark677/maoam_ckpts) | 物体・材質選択モデル。 |
| [See-through: Single-image Layer Decomposition for Anime Characters](https://doi.org/10.1145/3799902.3811209) | [shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through) · [コード条件](https://github.com/shitagaki-lab/see-through/blob/main/LICENSE) | [1](https://huggingface.co/layerdifforg/seethroughv0.0.2_layerdiff3d) / [2](https://huggingface.co/24yearsold/seethroughv0.0.1_marigold) / [3](https://huggingface.co/24yearsold/l2d_sam_iter2) | レイヤー生成・深度・部位分割モデル。 |
| [StyleID: A Perception-Aware Dataset and Metric for Stylization-Agnostic Facial Identity Recognition](https://doi.org/10.1145/3811360) | [kwanyun/StyleID](https://github.com/kwanyun/StyleID) · 条件はREADME参照 | [モデル](https://huggingface.co/kwanY/styleid) | 顔IDエンコーダー。 |
| [VeraRetouch: A Lightweight Fully Differentiable Framework for Multi-Task Reasoning Photo Retouching](https://doi.org/10.1145/3799902.3811065) | [OpenVeraTeam/VeraRetouch](https://github.com/OpenVeraTeam/VeraRetouch) · [コード条件](https://github.com/OpenVeraTeam/VeraRetouch/blob/main/LICENSE) | [1](https://huggingface.co/Gyh68/VeraRetouch) / [2](https://huggingface.co/Gyh68/VeraRetouch.Encoder_Renderer) | レタッチモデルとEncoder-Renderer。 |

### 光学・レンダリング・VFX（4件）

| 論文 | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- |
| [8DNA: 8D Neural Asset Light Transport by Distribution Learning](https://doi.org/10.1145/3799902.3811094) | [lwwu2/8dna26](https://github.com/lwwu2/8dna26) · 条件はREADME参照 | [モデル](https://drive.google.com/file/d/1WeYpquFoDTZzbwpHotiwIRwKdBskULcY/view) | アセット別の学習済みlight-transportモデル。 |
| [Guidestar-Free Adaptive Optics with Asymmetric Apertures](https://doi.org/10.1145/3809501) | [WeiyunJiang/guidestar-free-ao](https://github.com/WeiyunJiang/guidestar-free-ao) · [コード条件](https://github.com/WeiyunJiang/guidestar-free-ao/blob/main/LICENSE) | [モデル](https://drive.google.com/file/d/1e2GxutCBGbDSLIHtMcvRMSlsKAqJVtYH/view) | Places2で学習したモデル群。 |
| [Neural Quadrature Rule and Autoregressive Adaptive Sampling](https://doi.org/10.1145/3811318) | [SuikaSibyl/nqr](https://github.com/SuikaSibyl/nqr) · 条件はREADME参照 | [モデル](https://drive.google.com/file/d/1gydL15reAH7DDNNiieg5VnS8oe0HqGDT/view) | 配布アーカイブにscenesとckpt。 |
| [VfxDB: A Visual Effects Volume Dataset and Benchmark for VDB-Native Generative Modeling](https://doi.org/10.1145/3799902.3811178) | [VfxDB-Official/VfxDB](https://github.com/VfxDB-Official/VfxDB) · 条件はREADME参照 | [モデル](https://huggingface.co/ryogishiki/VfxDB-models) | 論文用EMAチェックポイントを配布。 |

### 音声・吹き替え（2件）

| 論文 | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- |
| [Audio-Omni: Extending Multi-modal Understanding to Versatile Audio Generation and Editing](https://doi.org/10.1145/3799902.3811191) | [ZeyueT/Audio-Omni](https://github.com/ZeyueT/Audio-Omni) · [コード条件](https://github.com/ZeyueT/Audio-Omni/blob/main/LICENSE) | [モデル](https://huggingface.co/HKUSTAudio/Audio-Omni) | 音声生成・編集モデル。 |
| [Just-Dub-It: Video dubbing via Joint Audio-Visual Diffusion](https://doi.org/10.1145/3799902.3811061) | [justdubit/just-dub-it](https://github.com/justdubit/just-dub-it) · [コード条件](https://github.com/justdubit/just-dub-it/blob/main/LICENSE) | [モデル](https://huggingface.co/justdubit/justdubit) | HFで条件への同意が必要。 |

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
