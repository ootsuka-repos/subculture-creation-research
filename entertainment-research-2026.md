# アニメ・エンタメ向けAI研究 — 2026年版（未確定の会議は2025年）

確認日: **2026-09-06**。**公式コードと本研究の学習済み重みが両方公開されているものだけ**を掲載しています。[SIGGRAPH 2026の既存66件](README.md)に加え、関連会議から**21件**を選びました。全採択論文の網羅リストではありません。 SIGGRAPHの66件とは調査範囲が異なり、この件数から他会議の該当研究が少ないとは判断できません。

[検証根拠付きJSON](entertainment-research-2026.json) · [CSV](entertainment-research-2026.csv)

## どの会議を見るとよいか

アニメ・エンタメへの近さを重視するなら、まず **SIGGRAPH / SIGGRAPH Asia と CVPR / ICCV / ECCV**。生成モデルの新しい手法には **ICLR / NeurIPS / ICML**、キャラクター動作には **SCA / MIG**、音声・効果音には **ACM MM / ICASSP / Interspeech**を加えると探しやすくなります。これは本調査の用途別の見方で、会議間の品質順位ではありません。

「2026年」は採択・発表先の年です。プレプリントが2025年初出でもICLR 2026採択なら2026年に分類し、2025年会議のコードが2026年に更新された場合は公開版を備考で区別しています。

| 会議 | 採用年 | 件数 | 年度・確認状況 |
| --- | --- | --- | --- |
| SIGGRAPH | 2026 | 66 | 既存Technical Papers集。各項目に日本語要約を追加。 |
| ICLR | 2026 | 3 | 2026年採択作から選定。 [根拠](https://iclr.cc/virtual/2026/papers.html) |
| CVPR | 2026 | 4 | うちSCAIL 1件はFindings。本会議採択作と区別する。 |
| ECCV | 2026 | 1 | 2026年採択告知を著者公式情報で確認。 |
| ICCV | 2025 | 2 | 隔年開催で2026年大会がないため、直近2025年。GEMの公開コード・重みは2026年版を確認。 [根拠](https://tc.computer.org/tcpami/iccv/) |
| ICML | 2026 | 1 | 2026年採択告知を著者公式情報で確認。 |
| NeurIPS | 2025 | 2 | 2026年の採択通知は9月24日。確認日9月6日時点では2025年を使用。 [根拠](https://neurips.cc/Conferences/2026/Dates) |
| SIGGRAPH Asia | 2026 | 1 | PActの著者READMEに採択告知あり。開催前・会議録未確認として区別する。 [著者の告知](https://github.com/Mobiuslqm/PAct) · [会議の状況](https://asia.siggraph.org/2026/submissions/technical-papers/) |
| SCA | 2026 | 1 | MotionPyramidのSCA 2026 / CGF掲載を著者所属機関のページで確認。 [根拠](https://igl.ethz.ch/projects/MotionPyramid/) |
| MIG | 2025 | 0 | 2026年は開催前で発表論文一覧を確認できず、2025年も調査。調査候補内でコード・重みの両方を確認できたものがなく、掲載は0件。該当研究が世界に存在しないという意味ではない。 [公式2026](https://mig.siggraph.org/2026/) · [公式2025](https://mig.siggraph.org/2025/program/) |
| ACM MM | 2026 | 1 | 2026年採択告知を著者公式情報で確認。 |
| ICASSP | 2026 | 2 | 2026年採択・発表情報を著者公式情報で確認。 |
| Interspeech | 2026 | 3 | 2026年論文の著者公式実装・配布ページを確認。 |

SIGGRAPHの66件は既存集、残り21件はこのページの追加分です。SCAILのFindings、PActの開催前採択告知は、開催済みの本会議発表と同一扱いにしていません。

## 制作工程から探す

まず内容を見たい場合は、**中割り・彩色ならToonComposer、編集可能なベクター演出ならOmniLottie、3Dリグ付けならPuppeteer、話すキャラの身振りならGELINA、効果音ならControlFoley**が用途を把握しやすい例です。導入の容易さや画質を実測して順位付けしたものではありません。

既存SIGGRAPH集にも、[See-through](https://github.com/shitagaki-lab/see-through)や[ARDY](https://github.com/nv-tlabs/ardy)などがあります。各リポジトリの説明は[既存66件の一覧](README.md#分野別一覧)を参照してください。

### 作画・映像・ベクターアニメ（8件）

| 研究・論文 | 会議 | 何ができるか | 公式コード・重み | 公開範囲・実用上の補足 |
| --- | --- | --- | --- | --- |
| [ToonComposer](https://arxiv.org/abs/2508.10881) | ICLR 2026 | 色付きの参照画像と少数のキーフレーム線画から、中割りと彩色をまとめて行い、アニメ映像を生成する。 | [コード](https://github.com/TencentARC/ToonComposer) · [重み](https://huggingface.co/TencentARC/ToonComposer) | 480p・608pの専用チェックポイント。Wan2.1-I2V-14B-480Pも必要。 公式目安は480p・61フレームで約57GB VRAM。会議年はICLR 2026、プレプリント初出は2025年。 |
| [GenCompositor](https://openreview.net/forum?id=ynim5u2N4i) | ICLR 2026 | 前景の被写体動画を背景動画へ合成する。位置・大きさ・移動経路を指定し、背景に合う見た目の映像を生成する。 | [コード](https://github.com/TencentARC/GenCompositor) · [重み](https://huggingface.co/TencentARC/GenCompositor) | 合成用branch・transformerの重みと推論・学習コード。CogVideoX-5B-I2V等も必要。 |
| [SCAIL](https://arxiv.org/abs/2512.05905) | CVPR 2026 Findings | キャラクター画像と姿勢の動きから、そのキャラクターが演技する動画を生成する。3Dの整合性を持つ姿勢表現を利用する。 | [コード](https://github.com/zai-org/SCAIL) · [重み](https://huggingface.co/zai-org/SCAIL-Preview) | SCAIL-Preview 14Bの推論コードと専用重み。 CVPRのFindingsトラック。著者READMEにComfyUI対応とBlenderリグ利用へのリンクあり。連携の実機検証は未実施。 |
| [One-to-All Animation](https://arxiv.org/abs/2511.22940) | CVPR 2026 | 参照キャラクターと姿勢指定から、画像のポーズ変更やアニメーションを生成する。参照画像との事前の位置合わせを省く設計。 | [コード](https://github.com/ssj9596/One-to-All-Animation) · [重み](https://huggingface.co/MochunniaN1/One-to-All-1.3b_2) | 動画生成用1.3B v2の2分割safetensorsを確認。 他のモデル版も著者が案内しているが、本一覧の重み確認対象は1.3B v2。 |
| [OmniLottie](https://arxiv.org/abs/2603.02138) | CVPR 2026 | 文章・画像・動画から、編集可能なLottie形式のベクターアニメーションを生成する。UI演出や動く図形・アイコン向け。 | [コード](https://github.com/OpenVGLab/OmniLottie) · [重み](https://huggingface.co/OmniLottie/OmniLottie) | 4Bモデルと推論コード。出力はLottie JSON。 ラスター動画とは異なり、ベクター要素と時間変化を扱う。 |
| [PersonaLive](https://arxiv.org/abs/2512.11253) | CVPR 2026 | 1枚の肖像画像を、入力映像の表情・頭部の動きに合わせて動かす。長い映像を逐次処理する配信向けポートレートアニメーション。 | [コード](https://github.com/GVCLab/PersonaLive) · [重み](https://huggingface.co/huaichang/PersonaLive) | 専用UNet・motion encoder等の重みとオンライン／オフライン推論コード。 著者READMEはacademic research onlyと明記。2026-08-28に後継[EditaLive](https://github.com/GVCLab/EditaLive)への案内あり。本項目はCVPR採択のPersonaLive版。 |
| [PhysRVG](https://arxiv.org/abs/2601.11087) | ECCV 2026 | 入力動画内の対象を点で指定し、落下・衝突などの物理的な動きを改善した動画を生成する。強化学習で動画モデルを調整する研究。 | [コード](https://github.com/ant-research/PhysRVG) · [重み](https://huggingface.co/HappyP4nda/PhysRVG) | 専用DiT・LoRAの重みと推論・学習コード。Wan2.2-TI2V-5Bベース。 物理シミュレータとしての数値的正確性を保証するものではない。 |
| [Wan-Move](https://arxiv.org/abs/2512.08765) | NeurIPS 2025 | 画像と点の移動軌跡を指定し、被写体の動きを制御した動画を生成する。動線を決めた映像演出向け。 | [コード](https://github.com/ali-vilab/Wan-Move) · [重み](https://huggingface.co/Ruihang/Wan-Move-14B-480P) | 14B・480pモデルの7分割safetensors。公式例は5秒の動画。 NeurIPS 2026は確認日時点で採択通知前のため、2025年を採用。 |

### 3Dモーション・キャラクター演技（6件）

| 研究・論文 | 会議 | 何ができるか | 公式コード・重み | 公開範囲・実用上の補足 |
| --- | --- | --- | --- | --- |
| [LIGHT](https://arxiv.org/abs/2603.25734) | ICLR 2026 | 人物が物を持つ・運ぶなど、人と物体が接触して動く3Dアニメーションを生成する。人と物体の動きを別々の速さで整えていく。 | [コード](https://github.com/wzyabcas/LIGHT) · [重み](https://drive.google.com/file/d/142UBxI1XyGVeopk0_azD_B_FDE_HPS8J/view) | 著者リンクのpretrained_checkpoints.zipと推論・学習コード。 SMPL系モデルやデータの準備は別途必要。 |
| [MotionPyramid](https://igl.ethz.ch/projects/MotionPyramid/) | SCA 2026 | 文章から3Dの人物動作を生成し、動作内容・周期や速さ・スタイルを調整する。Unityで生成結果を確認できる。 | [コード](https://github.com/Lee-abcde/MotionPyramid) · [重み1](https://drive.google.com/drive/folders/1w977lVQIOYd5FNONwmRtoLqpXjhOxHLE) · [重み2](https://drive.google.com/drive/folders/1GIFQUfyG46N563jkb8-Rdwxm__UznHad) · [重み3](https://drive.google.com/drive/folders/1Tp0WtckZh7XXVBRQaE6z3QTvBoTG0n2P) | VQ位相表現、phase-to-motion、text-to-phaseの学習済み重みとPython／Unityコード。 配布フォルダのdiffusion重みはmodel001680000.pt。READMEのphase-to-motion例はmodel001480000.ptなので、実行時には配布ファイル名への調整が必要。 |
| [GEM](https://arxiv.org/abs/2505.01425) | ICCV 2025 | 映像や文章などを条件に3Dの人体動作を復元・生成する。公開GEM-SMPLのデモは動画と文章を組み合わせた入力に対応する。 | [コード](https://github.com/NVlabs/GENMO) · [重み](https://huggingface.co/nvidia/GEM-X) | 2026年3月公開のGEM-SMPLコードとgem_smpl.ckpt。配布先名はGEM-X。 会議年はICCV 2025。GEM-Xの他の重みまでこの論文の公開範囲に含めない。コードはNVIDIA OneWay Noncommercial。 |
| [Ponimator](https://arxiv.org/abs/2510.14976) | ICCV 2025 | 2人が触れ合うポーズなどを起点に、抱擁や対人動作の3Dアニメーションを生成する。人物同士の接触を伴う演技向け。 | [コード](https://github.com/stevenlsw/ponimator) · [重み](https://huggingface.co/shaoweiliu/ponimator) | contactpose.ckpt・contactmotion.ckptと生成コード。 人体モデルや入力ポーズ推定などの依存物は別途必要。 |
| [GELINA](https://arxiv.org/abs/2510.12834) | ICASSP 2026 | 文章から音声と、それに同期した3Dジェスチャーを生成する。話すキャラクターの声と身振りを一緒に作る用途。 | [コード](https://github.com/TGuichoux/Gelina) · [重み](https://drive.google.com/file/d/1JnfyYCH0TQ6JpQl1duL6XN4hlj07iYmd/view) | 著者リンクのcheckpoints.zipと推論コード。 音声条件からのジェスチャー生成も扱う。 |
| [Being-H0](https://arxiv.org/abs/2507.15597) | ICML 2026 | 画像と作業の文章から、物を扱う手指・手首の動きを生成する。主目的はロボット学習で、手と物体の演技研究への応用候補。 | [コード](https://github.com/BeingBeyond/Being-H0) · [重み1](https://huggingface.co/BeingBeyond/Being-H0-GRVQ-8K) · [重み2](https://huggingface.co/BeingBeyond/Being-H0-1B-2508) | GRVQ手指・手首モデルと1B VLAの重みを確認。 全身アニメ制作ツールではない。MANO等が別途必要。後続Being-H0.5／H0.7は本項目の検証範囲外。 |

### 動かせる3Dアセット（2件）

| 研究・論文 | 会議 | 何ができるか | 公式コード・重み | 公開範囲・実用上の補足 |
| --- | --- | --- | --- | --- |
| [PAct](https://arxiv.org/abs/2602.14965) | SIGGRAPH Asia 2026（採択告知・開催前） | 1枚の画像から、部品と関節を持つ3D物体を生成する。扉・家具などの可動小物を、動かせるアセットへ変換する用途。 | [コード](https://github.com/Mobiuslqm/PAct) · [重み](https://huggingface.co/PAct000/PAct) | パーツ構造・関節推定等の5モデルと推論・学習コード。 重みはCC BY-NC-SA 4.0。著者READMEの採択告知に基づく掲載で、SIGGRAPH Asia 2026は開催前。 |
| [Puppeteer](https://arxiv.org/abs/2508.10898) | NeurIPS 2025 | 静的な3Dメッシュに骨格とスキニングを付ける。さらに参照動画を使って動きを最適化し、モデルをアニメーション化する。 | [コード](https://github.com/Seed3D/Puppeteer) · [重み](https://huggingface.co/Seed3D/Puppeteer) | 公開重みは骨格生成・スキニング用。動画からの動作付けは最適化処理。 NeurIPS 2026は確認日時点で採択通知前のため、2025年を採用。 |

### 効果音・音声・音響（5件）

| 研究・論文 | 会議 | 何ができるか | 公式コード・重み | 公開範囲・実用上の補足 |
| --- | --- | --- | --- | --- |
| [ControlFoley](https://arxiv.org/abs/2604.15086) | ACM MM 2026 | 動画に合う効果音を生成する。文章・参照音・発音タイミングも使って、足音や物音などの内容と出る時刻を調整する。 | [コード](https://github.com/xiaomi-research/controlfoley) · [重み](https://huggingface.co/YJX-Xiaomi/ControlFoley) | controlfoley.pthと推論コード。補助モデルも配布。 コードApache-2.0、モデルCC BY-NC 4.0。公開済みでも商用利用可とは限らない。 |
| [OV-InstructTTS](https://arxiv.org/abs/2601.01459) | ICASSP 2026 | 読み上げる文章に、感情や話し方の自然言語指示を添えて音声を生成する。台詞の演技指定に関係する研究。 | [コード](https://github.com/y-ren16/OV-InstructTTS) · [重み](https://huggingface.co/y-ren16/OV-InstructTTS) | 専用モデル2分割safetensorsとtoken2wavの重み。 公開推論コードはOV-InstructTTS-TEP。日本語での演技品質は未検証。 |
| [MSpoofTTS](https://arxiv.org/abs/2603.05373) | Interspeech 2026 | 音声合成中の複数候補を学習済み判別器で評価し、より自然な読み上げを選ぶ。既存TTSの推論を改善する手法。 | [コード](https://github.com/Danny-NUS/MSpoofTTS) · [重み](https://huggingface.co/Chanson-0803/MSpoofTTS) | 本研究の判別器5チェックポイントとNeuTTSに組み込む推論コード。 独立したTTS基盤モデルの新規配布ではない。NeuTTSの重みと利用条件も適用される。 |
| [UR-BERT](https://arxiv.org/abs/2606.11681) | Interspeech 2026 | 文字を共通のローマ字表現に変換し、多言語の音声合成に使うテキストエンコーダを学習する。多言語吹き替えの基盤研究。 | [コード](https://github.com/sanghyang00/ur-bert) · [重み](https://huggingface.co/Sanghyang00/urbert-256) | UR-BERTエンコーダと複数言語のVITS微調整チェックポイント。 495言語はエンコーダの対象範囲であり、495言語分の完成TTS重みの公開を意味しない。 |
| [HARP](https://arxiv.org/abs/2607.16657) | Interspeech 2026 | 音声を低ビットレートのトークンへ圧縮・復元する。倍音情報を考慮した音響コーデックで、音素材の伝送や圧縮の基盤向け。 | [コード](https://github.com/QiaoyuYang/harp-codec) · [重み](https://huggingface.co/KelvinYang/harp-codec) | harp.ckptと圧縮・復元コード。 楽曲や効果音そのものを指示から生成するモデルではない。 |

## 必須条件を満たさず掲載しなかった候補

公開予定やデータ配布を、学習済み重みの公開と取り違えないための記録です。公開状況は確認日以降に変わる可能性があります。

| 候補 | 未掲載の理由 |
| --- | --- |
| [UVFaceFusion](https://github.com/grignarder/UVFaceFusion) | 本研究の専用学習済み重みの配布を確認できない。依存する他研究の重みだけでは条件を満たさない。 |
| [World-R1](https://github.com/microsoft/World-R1) | 学習・報酬計算コードとデータセットの公開は確認したが、本研究の学習済みチェックポイントを確認できない。 |
| [OmniShow](https://github.com/Correr-Zhou/OmniShow) | READMEに内部方針によりチェックポイントを含めないと明記。 |
| [gnochi](https://github.com/GonzaloGNogales/gnochi) | 重み用READMEがComing soon。メインREADMEにローカル配置手順があっても公開済みとは数えない。 |
| [SiGnature_model](https://github.com/Adirosenthal540/SiGnature_model) | 公式ダウンロードスクリプトの重み配布先がHTTP 404。取得可能な公開重みを確認できない。 |
| [Earthbender](https://github.com/danial-barazandeh/Earthbender) | MIG 2025の実装とデータ配布は確認したが、学習済み重みの配布を確認できない。 |

## 確認方法と限界

- 公式GitHubのコミットを固定し、推論・モデル等の実装ファイルが読み取れることを確認しました。READMEだけの空リポジトリは含めません。
- HF配布の18研究では、匿名アクセスによるモデルファイル一覧と、研究固有のサンプル重みへのHEAD 200を確認しました。Being-H0は2つのモデルリポジトリを確認しています。
- LIGHT・GELINAは著者リンクの重みアーカイブ配布ページ、MotionPyramidは重みファイル名が見えるGoogle Driveフォルダを確認しました。アーカイブ全体の取得・内容検査はしていません。
- 全重みのダウンロード、GPU推論、再現性・生成品質・ComfyUI/Blender連携は未検証です。これらの結果を保証する一覧ではありません。
- コードと重みが公開されていても、商用利用が許可されているとは限りません。公開範囲の制約を表に記し、判別器・LoRA・一部モデルのみの公開も明示しています。
- モデルのリビジョン、確認ファイル、HTTP応答、コードのコミット・ファイル、採択情報の根拠は[JSON](entertainment-research-2026.json)に保存しています。既存SIGGRAPH 66件のモデル配布確認記録は[papers.json](papers.json)に保持し、今回その著者READMEを読み直して日本語要約を追加しました。
