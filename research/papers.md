# アニメ・エンタメ向けAI研究 — 公式コード＋公開重み（87件）

最終確認日: 2026-09-06。[制作系リポジトリ一覧](../README.md) · [papers.json](papers.json) · [papers.jsonl](papers.jsonl)

アニメ・エンタメ制作に使える、または参考になるAI研究のうち、著者の公式コードと本研究の学習済み重みが両方公開されているもの。SIGGRAPH 2026 Technical Papers（広く調査、CAD・製造などの周辺分野を含む）と、関連会議の用途別選定（網羅ではない）の2範囲を含む。SIGGRAPHと関連会議は調査範囲が異なるため、会議間の件数比較に使わない。

## 掲載条件

- 著者の公式実装が公開され、実装ソースを読み取れる。
- 本研究で配布する学習済み重みが公開され、HFのファイル一覧・サンプル配布応答または著者リンクの外部配布ページで確認できる。
- 専用重みの公開予定、第三者再実装、データセットのみ、既存ベースモデルの重みだけを掲載件数に含めない。
- モデルの一部や判別器・LoRAのみ公開の場合は、その範囲を明記する。

## 分野

| 分野 | 件数 | 論文 |
| --- | --- | --- |
| [3D生成・CAD・幾何処理](papers/3d-generation.md) | 18 | AniGen、B-repLer、CubePart、DeepMill++、DualBrep、InfiniteDiffusion、MeshFlow、NEO、Neural Particle Automata、NeuralSketch2Surf、Pixal3D、Points as Tori、Raster2Seq、SegviGen、SimArt、SQuadGen、SuperSDF、TripoSplat |
| [3D復元・理解](papers/3d-reconstruction.md) | 7 | ArtiFixer、GeoQuery、MegaNorm、Mix3R、MTPano、PointLLM-R、TrajVG |
| [モーション・アニメーション](papers/motion-animation.md) | 9 | AIS-BiLSTM、ARDY、GPC、Matérn-FM、MotionBricks、MUSIC、R-DMesh、SMP、TopoCap |
| [人体・顔・アバター](papers/human-avatar.md) | 7 | EchoAvatar、EgoForce、EgoRelight、OmniHands、OpenDelight、PEAR、VFAvatar |
| [動画生成・編集・リライティング](papers/video.md) | 8 | Go-with-the-Track、LongE2V、MACE-Dance、MV-S2V、OmniRoam、Relit-LiVE、UniVidX、VFXMaster |
| [画像生成・編集・材質](papers/image-material.md) | 11 | BFS、BoxCtrl、ComboStoc、ControlTile、FIT、HairPort、LUCID、MAOAM、See-through、StyleID、VeraRetouch |
| [光学・レンダリング・VFX](papers/rendering-vfx.md) | 4 | 8DNA、Guidestar-Free、NQR、VfxDB |
| [音声・吹き替え](papers/speech-dubbing.md) | 2 | Audio-Omni、Just-Dub-It |
| [作画・映像・ベクターアニメ](papers/drawing-vector-anime.md) | 8 | ToonComposer、GenCompositor、SCAIL、One-to-All Animation、OmniLottie、PersonaLive、PhysRVG、Wan-Move |
| [3Dモーション・キャラクター演技](papers/character-motion.md) | 6 | LIGHT、MotionPyramid、GEM、Ponimator、GELINA、Being-H0 |
| [動かせる3Dアセット](papers/animatable-3d.md) | 2 | PAct、Puppeteer |
| [効果音・音声・音響](papers/sound-audio.md) | 5 | ControlFoley、OV-InstructTTS、MSpoofTTS、UR-BERT、HARP |

## 会議と年度

年は採択・発表先の年。2026年大会がない、または採択未確定の会議は2025年を参照。本会議・Findings・Journal/TOG・開催前の採択告知を区別する。

| 会議 | 採用年 | 件数 | 年度・確認状況 |
| --- | --- | --- | --- |
| SIGGRAPH | 2026 | 66 | 既存Technical Papers集。各項目に日本語要約を追加。 |
| ICLR | 2026 | 3 | 2026年採択作から選定。 [根拠](https://iclr.cc/virtual/2026/papers.html) |
| CVPR | 2026 | 4 | うちSCAIL 1件はFindings。本会議採択作と区別する。 |
| ECCV | 2026 | 1 | 2026年採択告知を著者公式情報で確認。 |
| ICCV | 2025 | 2 | 隔年開催で2026年大会がないため、直近2025年。GEMの公開コード・重みは2026年版を確認。 [根拠](https://tc.computer.org/tcpami/iccv/) |
| ICML | 2026 | 1 | 2026年採択告知を著者公式情報で確認。 |
| NeurIPS | 2025 | 2 | 2026年の採択通知は9月24日。確認日9月6日時点では2025年を使用。 [根拠](https://neurips.cc/Conferences/2026/Dates) |
| SIGGRAPH Asia | 2026 | 1 | PActの著者READMEに採択告知あり。開催前・会議録未確認として区別する。 [根拠](https://asia.siggraph.org/2026/submissions/technical-papers/) |
| SCA | 2026 | 1 | MotionPyramidのSCA 2026 / CGF掲載を著者所属機関のページで確認。 [根拠](https://igl.ethz.ch/projects/MotionPyramid/) |
| MIG | 2025 | 0 | 2026年は開催前で発表論文一覧を確認できず、2025年も調査。調査候補内でコード・重みの両方を確認できたものがなく、掲載は0件。該当研究が世界に存在しないという意味ではない。 |
| ACM MM | 2026 | 1 | 2026年採択告知を著者公式情報で確認。 |
| ICASSP | 2026 | 2 | 2026年採択・発表情報を著者公式情報で確認。 |
| Interspeech | 2026 | 3 | 2026年論文の著者公式実装・配布ページを確認。 |

## 確認範囲と限界

- Release availability and file listings/headers were checked; model binaries were not fully downloaded or executed. Gated distributions are marked. This is a verified discovery snapshot, not a proof of exhaustive coverage.
- 重み全体のダウンロード、アーカイブ内の検査、GPU推論、品質・再現性・ツール連携の実機検証は未実施。
- HFでは匿名APIのファイル一覧と研究固有のサンプル重み1ファイルへのHEAD 200を確認。分割モデルの全シャード本体を取得したわけではない。
- Google Driveは著者の配布説明と匿名閲覧できる配布ページ／ファイル名を確認。全ファイルのダウンロードを保証するものではない。
- 会議情報は公式会議・著者機関の情報を優先し、著者READMEのみで確認した採択情報も区別して記録。
- 公開と商用利用可は別。ライセンスmetadataは記録値であり、本文・依存物の条件を含む法的判断ではない。

## 必須条件を満たさず掲載しなかった候補

| 候補 | 理由 | 範囲 | 確認日 |
| --- | --- | --- | --- |
| [SATO](https://github.com/Xrvitd/SATO) | トークナイザーのみ公開。推論コードとモデル重みは確認できず。 | SIGGRAPH 2026 | 2026-09-06 |
| [FLASHand](https://github.com/IGLICT/FLASHand) | 推論コードは公開済み。チェックポイントの配布リンクはComing soon。 | SIGGRAPH 2026 | 2026-09-06 |
| [VideoNeuMat](https://github.com/bowenxueai/VideoNeuMat) | モデル重みは公開済み。実装コードはComing soon。 | SIGGRAPH 2026 | 2026-09-06 |
| [HumanFlow](https://github.com/wenzhuofanfan/HumanFlow) | 推論コード・チェックポイントともに公開予定。 | SIGGRAPH 2026 | 2026-09-06 |
| [CasLayout](https://github.com/YingruiWoo/CasLayout) | 公式READMEはコード・データの公開予定のみ。 | SIGGRAPH 2026 | 2026-09-06 |
| [ShapeUP](https://github.com/inbar-2344/ShapeUp) | 公式READMEはComing soon。 | SIGGRAPH 2026 | 2026-09-06 |
| [MOCHI](https://github.com/jiyewise/MOCHI) | README・付随ファイルのみで、実装と重みは確認できず。 | SIGGRAPH 2026 | 2026-09-06 |
| [ParaCAD](https://github.com/dafei-qin/ParaCAD) | 実装とモデル重みの公開を確認できず。 | SIGGRAPH 2026 | 2026-09-06 |
| [GMT](https://github.com/xing-yuu/GMT) | READMEに公開データと学習済みチェックポイントを含まない旨が明記。 | SIGGRAPH 2026 | 2026-09-06 |
| [GR3EN](https://github.com/google-deepmind/gr3en) | コードは公開済み。専用重みの有効な配布リンクを確認できず。 | SIGGRAPH 2026 | 2026-09-06 |
| [STyMo](https://github.com/facebookresearch/STyMo) | 学習コードとモーションデータを配布。学習済み重みは確認できず。 | SIGGRAPH 2026 | 2026-09-06 |
| [EasyVFX](https://github.com/mayuelala/EasyVFX) | コードとベースモデルへのリンクは存在。EasyVFX固有の学習済み重みは確認できず。 | SIGGRAPH 2026 | 2026-09-06 |
| [Prox-E](https://github.com/etaisella/Prox-E) | 学習不要手法。公式実装は公開済みだが、本一覧の専用重み配布の対象外。 | SIGGRAPH 2026 | 2026-09-06 |
| [FreeOrbit4D](https://github.com/VVeiCao/FreeOrbit4D) | 学習不要手法。既存の公開モデルを組み合わせるため専用重み配布の対象外。 | SIGGRAPH 2026 | 2026-09-06 |
| [LayerInbetween](https://github.com/MarkMoHR/LayerInbetween) | 既存の光学フロー・深度・SAM2モデルを利用。専用重み配布の対象外。 | SIGGRAPH 2026 | 2026-09-06 |
| [StudioRecon](https://github.com/sisyphm/StudioRecon) | 公式ドキュメントは既存の上流モデルの取得方法を案内。専用重み配布の対象外。 | SIGGRAPH 2026 | 2026-09-06 |
| [GimmBO](https://github.com/squidrice21/gimmbo) | 既存のLoRAを探索・結合する手法。専用重み配布の対象外。 | SIGGRAPH 2026 | 2026-09-06 |
| [HairGPT](https://haiminluo.github.io/hairgpt/) | プロジェクトページのCode/Dataは配布先への有効なリンクになっていない。 | SIGGRAPH 2026 | 2026-09-06 |
| [UVFaceFusion](https://github.com/grignarder/UVFaceFusion) | 本研究の専用学習済み重みの配布を確認できない。依存する他研究の重みだけでは条件を満たさない。 | 関連会議 | 2026-09-06 |
| [World-R1](https://github.com/microsoft/World-R1) | 学習・報酬計算コードとデータセットの公開は確認したが、本研究の学習済みチェックポイントを確認できない。 | 関連会議 | 2026-09-06 |
| [OmniShow](https://github.com/Correr-Zhou/OmniShow) | READMEに内部方針によりチェックポイントを含めないと明記。 | 関連会議 | 2026-09-06 |
| [gnochi](https://github.com/GonzaloGNogales/gnochi) | 重み用READMEがComing soon。メインREADMEにローカル配置手順があっても公開済みとは数えない。 | 関連会議 | 2026-09-06 |
| [SiGnature_model](https://github.com/Adirosenthal540/SiGnature_model) | 公式ダウンロードスクリプトの重み配布先がHTTP 404。取得可能な公開重みを確認できない。 | 関連会議 | 2026-09-06 |
| [Earthbender](https://github.com/danial-barazandeh/Earthbender) | MIG 2025の実装とデータ配布は確認したが、学習済み重みの配布を確認できない。 | 関連会議 | 2026-09-06 |
