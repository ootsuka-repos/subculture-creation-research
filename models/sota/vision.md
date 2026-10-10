# 画像認識（検出・分割・分類・特徴）のアニメ系SOTA（2026-10-01）

[一覧へ](../anime-task-sota.md) · [リポジトリ全体像](../anime-repositories.md) · [正本JSON](../../sota-catalog.json)

選定基準・注意は[一覧ページ](../anime-task-sota.md)。各項目の「最良」は確度付きの編集判断で、重み取得・推論実行は未実施。

### 物体検出(アニメ顔検出)

<a id="object-detection--face"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [deepghs/anime_face_detection](https://huggingface.co/deepghs/anime_face_detection/tree/784dc4c0bb692351ddcdbe6131a050b17d3025d5)（revision `784dc4c0` / 作成 2023-06-04 / 更新 2024-09-24）
- **利用条件**: mit。MIT(メタデータ)。カード本文に追加条件の記載なし。学習データ出所の説明もカードになし(データセットdeepghs/anime_face_detectionはMIT表記・1K〜10K枚)。Ultralytics(AGPL-3.0)系で学習した可能性があるがカード未記載のため未確認。商用可とは断定しない
- **選定根拠**: 事実: deepghs/anime_face_detectionはface_detect_v0〜v1.4のn/sを収録し、カード表の自己報告F1は0.93〜0.97(v1.4_s 0.95/閾値0.307、v1.4_n 0.94)。評価データはバージョンごとに異なる可能性があり同一条件比較ではない。HF DL数は0(ONNX/ptのみでカウント対象外の可能性)、likes23、Space6、discussions2。MITライセンス。loaderのdeepghs/imgutilsは★415、既定値はdetect_faces(level='s', version='v1.4')。競合: Fuyucchi/yolov8_animeface(自己データmAP50 0.955/mAP50-95 0.534、safebooru由来10,000枚を手動アノテ、DL累計94,121だがAGPL-3.0・yolov8x6/1280pxで重い)、hysts/anime-face-detector(MIT、28点ランドマーク付き、GitHub★535・コード参照234)。評価: 同一データでの横並び比較が見つからないため精度の優劣は未決着。汎用性(顔・頭・人物・手・目・半身を同一流儀で供給)、MIT、ONNX+pt両方、imgutils経由の実績で選定。未解決: モデル更新が2024-09-24で止まっている、学習データ詳細がカード本文にない。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 24 / Spaces 6
- **概要**: アニメ顔検出モデル群(face_detect_v0〜v1.4、n/s)。カード表にFLOPS・パラメータ・F1・閾値・ラベル(face)を記載
- **入力**: RGB画像(任意サイズ。imgutilsは内部でリサイズ)
- **出力**: 顔のバウンディングボックス+信頼度(ラベル'face')。推奨閾値はthreshold.json
- **必要環境**: ONNX(model.onnx)とYOLO形式(model.pt)を同梱。推奨ローダはdghs-imgutils(onnxruntime)。速度・VRAMは未測定(カードはFLOPS/パラメータ数のみ記載)
- **制約**: 単一クラス(face)のみ。F1はカード自己報告で評価データの規模・構成は本文に記載なし。実写顔はWIDER等を含むBingsu/adetailer系の方が想定内。ランドマークは出せない(hysts参照)
- **使う版・派生**: 推奨: face_detect_v1.4_s/model.onnx (imgutilsの既定)。軽量: face_detect_v1.4_n。派生: Library-Mutsumi/anime_face_detection(2026-06-09のミラー、likes1)。同系統のYOLO系pt互換でADetailer/Impact-Subpackにも利用可能(model.ptあり)
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/deepghs/anime_face_detection/blob/784dc4c0bb692351ddcdbe6131a050b17d3025d5/README.md)
- **次点**: `Fuyucchi/yolov8_animeface`（自己データ(safebooru手動10,000枚)mAP50 0.955・yolov5_animeに勝つ比較あり、DL累計94k。ただしAGPL-3.0、yolov8x6/1280pxで推論約82ms、顔以外のクラスなし、2024-10-14以降更新なし） / `hysts/anime-face-detector-yolov3`（MIT・公式ミラー(2026-07-05作成、重みは2021年版)。ベンチ数値なし。顔ボックス+28点ランドマークが目的ならこちら(keypoint-detectionで採用)） / `Bingsu/adetailer`（ADetailer標準(DL累計352M、30日9.9M、likes794)だが'2D/realistic'混在でWIDER FACE等を含む汎用。face_yolov9c mAP50 0.748/mAP50-95 0.433(自己報告)。アニメ特化ではない）

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)
- [hysts/anime-face-detector](https://github.com/hysts/anime-face-detector) — 顔検出+28点ランドマーク(faster-rcnn/yolov3+hrnetv2)（★536 / MIT / 最終push 2026-07-05 / release v0.0.5 (2021-11-15) / 確認コミット [`98a9fb48`](https://github.com/hysts/anime-face-detector/blob/98a9fb480fa04bdd96acbe4d98da191a898267f3/README.md)）
  - MIT。★535、最終push 2026-07-05(HF公式ミラー作成に伴う更新)。リリースは2021-11の0.0.5止まり。GitHubコード検索'hysts/anime-face-detector'234件(シード)
- [ltdrdata/ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack) — ComfyUIでYOLO系.ptを検出器として使う(UltralyticsDetectorProvider)（★387 / AGPL-3.0 / 最終push 2025-07-22 / 確認コミット [`50c7b71a`](https://github.com/ltdrdata/ComfyUI-Impact-Subpack/blob/50c7b71a6a224734cc9b21963c6d1926816a97f1/README.md)）
  - ★384・AGPL-3.0、最終push 2025-07-22。Impact-Pack本体(GPL-3.0、★3,329、push 2026-04-19)の検出器プロバイダ。model.ptを配置して使う(READMEに記載)
- [Bing-su/adetailer](https://github.com/Bing-su/adetailer) — SD WebUIのADetailer(face/hand/personのYOLOで自動補正)（★4,792 / AGPL-3.0 / 最終push 2026-10-05 / 確認コミット [`3a599f5d`](https://github.com/Bing-su/adetailer/blob/3a599f5d4607d8f9d8b9fc5a15526197418dae1a/README.md)）
  - AGPL-3.0、★4,793、push 2026-09-28。Bingsu/adetailerのHF DL累計352Mが普及の証拠。アニメ特化ではなく汎用2D/実写混在

### 物体検出(アニメキャラクター/人物全身検出)

<a id="object-detection--person"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [deepghs/anime_person_detection](https://huggingface.co/deepghs/anime_person_detection/tree/e39c744c22432ad01f91dd254fe2b02c8d878b8c)（revision `e39c744c` / 作成 2023-06-07 / 更新 2024-09-24）
- **利用条件**: mit。MIT(メタデータ)。カード本文に追加条件なし。学習データ出所の説明なし。商用可とは断定しない
- **選定根拠**: 事実: deepghs/anime_person_detectionはperson_detect v0〜v1.3(n/s/m/x)を収録。カード表の自己報告F1は0.85〜0.87(v1.1_m 0.87/閾値0.348、v1.3_s 0.86、v1.1_n 0.85)で、imgutilsの既定はdetect_person(level='m', version='v1.1')。MIT、likes9、Space4、discussions0、DL統計0(ONNX/pt主体でカウント外の可能性)。データセットdeepghs/anime_person_detectionは1K〜10K枚・MIT表記。競合: 2024-10-28追加のanime_person_detection_remake(カード未確認・ライセンス表記なし・likes0)、Bingsu/adetailerのperson_yolov8m-seg(COCO人物+AniSegを混ぜた2D/実写、bbox mAP50 0.849/mAP50-95 0.636=自己報告)。評価: アニメ専用でこの粒度のバージョン管理・F1表があるのはdeepghsのみで選定。未解決: 横並びベンチなし、更新2024-09-24で停止。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 9 / Spaces 4
- **概要**: アニメ人物全身検出モデル群(person_detect v0〜v1.3、n/s/m/x)
- **入力**: RGB画像(任意サイズ。imgutilsは内部でリサイズ)
- **出力**: 人物(キャラクター)ボックス+信頼度(ラベル'person')
- **必要環境**: ONNX(model.onnx)とYOLO形式(model.pt)を同梱。推奨ローダはdghs-imgutils(onnxruntime)。速度・VRAMは未測定(カードはFLOPS/パラメータ数のみ記載)
- **制約**: 単一クラス。F1はカード自己報告のみで評価データ規模は記載なし。複数人の重なり・小さなキャラでの性能は未測定
- **使う版・派生**: 推奨: person_detect_v1.1_m(imgutils既定)または軽量person_detect_v1.3_s。派生: Library-Mutsumi/anime_person_detection(ミラー)
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/deepghs/anime_person_detection/blob/e39c744c22432ad01f91dd254fe2b02c8d878b8c/README.md)
- **次点**: `deepghs/anime_person_detection_remake`（2024-10-28追加の再学習版。ライセンス・カード情報が乏しくlikes0。imgutilsの既定にも入っていない） / `Bingsu/adetailer`（person_yolov8m-seg(2D/実写混在、bbox mAP50 0.849/マスクmAP50 0.831=自己報告)。マスクが要る場合の選択肢だがアニメ特化ではない）

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)
- [Bing-su/adetailer](https://github.com/Bing-su/adetailer) — SD WebUIでperson等をYOLO検出して再描画（★4,792 / AGPL-3.0 / 最終push 2026-10-05 / 確認コミット [`3a599f5d`](https://github.com/Bing-su/adetailer/blob/3a599f5d4607d8f9d8b9fc5a15526197418dae1a/README.md)）
  - AGPL-3.0、★4,793、push 2026-09-28。ADetailerはBingsu/adetailerの重みを標準採用

### 物体検出(アニメ頭部検出)

<a id="object-detection--head"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [deepghs/anime_head_detection](https://huggingface.co/deepghs/anime_head_detection/tree/06604feee81983792a57c21081e539c0ae229833)（revision `06604fee` / 作成 2023-06-07 / 更新 2024-10-19）
- **利用条件**: mit。MIT(メタデータ)。カード本文に追加条件なし。学習データ出所の説明なし。ultralytics形式のログ(labels.jpg・tfevents)を含む。商用可とは断定しない
- **選定根拠**: 事実: deepghs/anime_head_detectionはhead_detect v0〜v2.0(YOLOv8/v9/v10/v11/RT-DETR、n〜x)をカード表に列挙し、precision/recall/mAPまで自己報告。v2.0_x_yv11はF1 0.93・mAP50 0.969・mAP50-95 0.789、imgutils既定のhead_detect_v2.0_sはF1 0.92・mAP50 0.958・mAP50-95 0.778。旧v1.0_xはmAP50-95 0.815で数値上は上だが評価セットがバージョンで異なる可能性。MIT、likes7、Space5、データセットは10K〜100K枚・MIT表記、repoのファイル数786。評価: 頭部検出でこの規模の系統的なモデル表を持つアニメ特化は他にない(nyuuzyou/AnimeHeads、sophic00/animehead等は個人の小規模モデルでカード数値の裏付けが薄い)。未解決: 更新2024-10-19で停止、一部ファイル数が多くモデル選択が煩雑。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 7 / Spaces 5
- **概要**: アニメ頭部(髪含む)検出モデル群(YOLO各世代・RT-DETR、n/s/m/l/x)
- **入力**: RGB画像(任意サイズ。imgutilsは内部でリサイズ)
- **出力**: 頭部ボックス+信頼度(ラベル'head')
- **必要環境**: ONNX(model.onnx)とYOLO形式(model.pt)を同梱。推奨ローダはdghs-imgutils(onnxruntime)。速度・VRAMは未測定(カードはFLOPS/パラメータ数のみ記載)
- **制約**: 単一クラス。評価指標は自己報告でデータはバージョン間で同一でない可能性。顔(face)との差は『髪を含む頭全体』だが定義の詳細はカード未確認
- **使う版・派生**: 推奨: head_detect_v2.0_s(imgutils既定)。高精度: head_detect_v2.0_x_yv11。派生: Library-Mutsumi/anime_head_detection(ミラー)
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/deepghs/anime_head_detection/blob/06604feee81983792a57c21081e539c0ae229833/README.md)
- **次点**: `nyuuzyou/AnimeHeads`（2023-04-15の個人モデル(likes9)。ベンチ・更新の裏付けが薄い） / `sophic00/animehead`（2025-06-18作、30日DL310、likes0。カードの定量評価を確認していない）

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)

### 物体検出(アニメ手検出)

<a id="object-detection--hand"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [deepghs/anime_hand_detection](https://huggingface.co/deepghs/anime_hand_detection/tree/dba2c5bec15fcee9ac4909b244a84e8783cf46a2)（revision `dba2c5be` / 作成 2023-07-21 / 更新 2024-09-24）
- **利用条件**: openrail。メタデータはopenrail(CreativeML Open RAIL系、用途制限あり)。カード本文に追加条件なし。学習データ出所が不明。商用可とは断定しない
- **選定根拠**: 事実: deepghs/anime_hand_detectionはhand_detect v0.1〜v1.0(n/s)を収録。自己報告F1は0.70〜0.799(v1.0_s 0.79/閾値0.395、v0.6_s 0.799、v1.0_n 0.75)で顔・頭より明確に低い。ライセンスはopenrail、likes5、Space5、データセットdeepghs/anime_hand_detectionはDL累計108でライセンス未記載、カードにデータ説明なし。競合: Bingsu/adetailerのhand_yolov9c(2D/実写混在、mAP50 0.810/mAP50-95 0.550=自己報告、DL累計352M)は指標が異なり直接比較不能。評価: 『アニメ特化』で手を出す公開モデルとしてはdeepghsが唯一体系的だが、F1 0.8前後と手のラベル定義が難しく、ADetailer系の汎用版と使い分けが必要。自信度はlowとした。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 5 / Spaces 5
- **概要**: アニメ手検出モデル群(hand_detect v0.1〜v1.0)
- **入力**: RGB画像(任意サイズ。imgutilsは内部でリサイズ)
- **出力**: 手のボックス+信頼度(ラベル'hand')
- **必要環境**: ONNX(model.onnx)とYOLO形式(model.pt)を同梱。推奨ローダはdghs-imgutils(onnxruntime)。速度・VRAMは未測定(カードはFLOPS/パラメータ数のみ記載)
- **制約**: F1 0.8前後と低め。手の重なり・小さな手・持ち物との区別は未測定。データ出所・規模がカードに記載なし
- **使う版・派生**: 推奨: hand_detect_v1.0_s(imgutils既定)。派生: Library-Mutsumi/anime_hand_detection(ミラー)、kiriyamaX/ghs-anime-hand-detection(2026-01-17のコピー、内容未確認)
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/deepghs/anime_hand_detection/blob/dba2c5bec15fcee9ac4909b244a84e8783cf46a2/README.md)
- **次点**: `Bingsu/adetailer`（hand_yolov9c等(2D/実写混在、mAP50 0.810=自己報告)。ADetailerの標準でDL実績は桁違いだがアニメ特化ではなくAGPL系ツール前提）

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)
- [ltdrdata/ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack) — ComfyUIでhand検出器を使うUltralyticsDetectorProvider（★387 / AGPL-3.0 / 最終push 2025-07-22 / 確認コミット [`50c7b71a`](https://github.com/ltdrdata/ComfyUI-Impact-Subpack/blob/50c7b71a6a224734cc9b21963c6d1926816a97f1/README.md)）
  - ★384・AGPL-3.0。model.ptをmodels/ultralytics/bboxに置いて使う(READMEの記載)

### 物体検出(アニメ目検出)

<a id="object-detection--eye"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [deepghs/anime_eye_detection](https://huggingface.co/deepghs/anime_eye_detection/tree/ba69e3ee3b0b23e7c948994e182f06cd46e534f1)（revision `ba69e3ee` / 作成 2023-09-18 / 更新 2024-09-24）
- **利用条件**: openrail。メタデータはopenrail(用途制限あり)。データセット側はcc-by-4.0。カード本文に追加条件なし。商用可とは断定しない
- **選定根拠**: 事実: deepghs/anime_eye_detectionはeye_detect v0.2〜v1.0(n/s)を収録。自己報告F1は0.84〜0.94(v1.0_s 0.93/閾値0.228、v1.0_n 0.91、v0.4_s 0.94)。ライセンスはopenrail、likes4、Space5。データセットdeepghs/anime_eye_detectionはn<1K枚・cc-by-4.0で小規模。競合: killjoyelite/anime-eye-yolov8(2026-09-07作、30日DL332、likes1)は新しいがカード数値を未確認。評価: アニメ目検出として数値付きで体系化されている公開モデルはdeepghsのみで選定。学習データが1K枚未満のため汎化性は疑わしく、自信度low。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 4 / Spaces 5
- **概要**: アニメ目検出モデル群(eye_detect v0.2〜v1.0)
- **入力**: RGB画像(任意サイズ。imgutilsは内部でリサイズ)
- **出力**: 目のボックス+信頼度(ラベル'eye')
- **必要環境**: ONNX(model.onnx)とYOLO形式(model.pt)を同梱。推奨ローダはdghs-imgutils(onnxruntime)。速度・VRAMは未測定(カードはFLOPS/パラメータ数のみ記載)
- **制約**: 学習データn<1Kの小規模データセット。左右の区別なし、閉じ目・横顔・極端にデフォルメした目は未測定
- **使う版・派生**: 推奨: eye_detect_v1.0_s(imgutils既定)。派生: Library-Mutsumi/anime_eye_detection(ミラー)
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/deepghs/anime_eye_detection/blob/ba69e3ee3b0b23e7c948994e182f06cd46e534f1/README.md)
- **次点**: `killjoyelite/anime-eye-yolov8`（2026-09-07公開の新顔(30日DL332、likes1)。カードの定量評価・データ出所を確認していない）

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)

### 物体検出(アニメ半身検出)

<a id="object-detection--halfbody"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [deepghs/anime_halfbody_detection](https://huggingface.co/deepghs/anime_halfbody_detection/tree/95e21f43f13403930a78a87002f63b6d94c829e8)（revision `95e21f43` / 作成 2023-08-25 / 更新 2024-09-24）
- **利用条件**: openrail。メタデータはopenrail(用途制限あり)。カード本文に追加条件なし。学習データ出所が不明。商用可とは断定しない
- **選定根拠**: 事実: deepghs/anime_halfbody_detectionはhalfbody_detect v0.2〜v1.0(n/s)を収録。自己報告F1は0.92〜0.95(v1.0_s 0.95/閾値0.577、v1.0_n 0.94)。openrail、likes2、Space4、データセットは100K〜1M枚のopenrail表記(774DL)。半身(バストアップ〜腰)検出を公開しているのはdeepghsのみで、競合が見つからず選定。評価: 他の公開モデルが確認できないためデフォルト採用だが、likes2・利用例の裏付けが薄く自信度low。用途は立ち絵のクロップ判定(顔/半身/全身の振り分け)。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 2 / Spaces 4
- **概要**: アニメ半身(halfbody)検出モデル群(halfbody_detect v0.2〜v1.0)
- **入力**: RGB画像(任意サイズ。imgutilsは内部でリサイズ)
- **出力**: 半身のボックス+信頼度(ラベル'halfbody')
- **必要環境**: ONNX(model.onnx)とYOLO形式(model.pt)を同梱。推奨ローダはdghs-imgutils(onnxruntime)。速度・VRAMは未測定(カードはFLOPS/パラメータ数のみ記載)
- **制約**: 定義(どこまでが半身か)はカードに記載なし。単一クラスのため全身・顔との振り分けはperson/faceモデルと組み合わせる前提
- **使う版・派生**: 推奨: halfbody_detect_v1.0_s(imgutils既定)。派生: なし確認
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/deepghs/anime_halfbody_detection/blob/95e21f43f13403930a78a87002f63b6d94c829e8/README.md)

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)

### 画像セグメンテーション(キャラクター切り抜き・背景除去)

<a id="image-segmentation--character-matting"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [joelseytre/toonout](https://huggingface.co/joelseytre/toonout/tree/cbf720eca394edcde66b861a8a8c20fbabe9c748)（revision `cbf720ec` / 作成 2025-09-09 / 更新 2026-06-12）
- **利用条件**: mit。メタデータMIT。データセットはCC-BY 4.0(joelseytre/toonout、帰属表示が必要)。学習画像はSDXL系アニメチェックポイント(Yamer's Anime)生成物で、そのモデルの利用条件は未確認。商用可とは断定しない
- **選定根拠**: 事実: 決め手は『アニメ画像での実測があるか』。joelseytre/toonout(BiRefNet微調整、MIT)は論文arXiv:2509.06839で自作テスト126枚(SDXL系アニメモデルYamer's Animeの生成画像、BiRefNetが苦手な例を優先収録)にてPixel Accuracy 95.3→99.5%、Mean Boundary IoU 88.5→95.6%、Weighted F 97.8→99.4%(自己報告。比較相手はPhotoroom[99.2/95.2/99.3]・Bria RMBG-2.0[97.8/92.4/98.8]・無改造BiRefNet)。skytnt/anime-remove-background(ISNet-anime)は図1の定性比較のみ(Komikoは序論で言及のみ)で、表の数値比較はない。採用実績はskytnt側が圧倒: rembgの既定アニメ用isnet-anime(rembg★24,932)、HF Space100、コード検索'isnet-anime'2,352件・'skytnt/anime-seg'549件(シード)。ToonOutはHF DL累計3,304・likes23・Space2・コード参照33件(シード)、ただしComfyUI-RMBG(★2,127)がBiRefNet_toonOutを搭載、GGUF/ONNX派生あり、X上の実務者評価は乏しい(isnet-animeの方が実アニメキャラに良いとの個別投稿1件)。評価: 量的証拠はToonOutのみ・skytnt側は量的証拠ゼロで採用実績のみ。ライセンス面もToonOut(MIT・CC-BY-4.0のAI生成データ)がskytnt(学習データにdanbooru収集画像、ウェイトApache-2.0は作者が2026-08-17にHF議論で言及)より明快。よってToonOutを暫定1位としたが、両者の直接比較(同一テストセット)は未確認でlow。実アニメ映像フレームにはZarxrax/BiRefNet-Real_Anime_lite(2026-09-22公開、DL0)という新顔があるが未検証。
- **指標（確認日時点）**: DL累計 3,463 / 直近30日 522 / likes 24 / Spaces 2
- **概要**: BiRefNet(Dichotomous Image Segmentation)をアニメ画像1,228枚(ToonOutデータセット、CC-BY-4.0)で微調整した背景除去モデル。髪の毛先・線画・半透明を狙う。作者はKartoon AI
- **入力**: アニメ/イラスト画像(1024px前後、RGB)
- **出力**: 前景アルファマスク(0〜1のグレースケール)→RGBA切り抜き
- **必要環境**: BiRefNet実装(GitHub MatteoKartoon/BiRefNetのデモノートブック)で推論。PyTorch重み birefnet_finetuned_toonout.pth。VRAM・速度は未測定(カード記載なし)
- **制約**: 評価データは自作126枚でAI生成アニメ画像のみ。実写/手描き/アニメ映像フレームでの性能は未評価。小物(items)はPA 96.6%と弱い。isnet-animeとの直接比較なし
- **使う版・派生**: 重み: birefnet_finetuned_toonout.pth。派生: Acly/BiRefNet-toonout-GGUF、sprited/birefnet-toonout-onnx、Replicate sprited/birefnet-toonout、ComfyUI-RMBGのBiRefNet_toonOutノード
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/joelseytre/toonout/blob/cbf720eca394edcde66b861a8a8c20fbabe9c748/README.md) / [論文: データ・指標・Photoroom/Bria/BiRefNet比較(自己報告)](https://arxiv.org/abs/2509.06839) / [学習データセット(1,228枚、CC-BY-4.0)](https://huggingface.co/datasets/joelseytre/toonout)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `ZhengPeng7/BiRefNet` — 汎用BiRefNet(MIT、HF DL累計19.9M・30日784k・likes647)。アニメ特化ではないがToonOutの母体。ToonOut論文の表ではアニメ生成画像でPixel Accuracy 95.3%
- **次点**: `skytnt/anime-seg`（ISNet-anime。rembg既定・HF Space100・コード参照2,352件(シード)の事実上標準で、ウェイトApache-2.0は作者が2026-08-17にHF議論#4で回答。定量ベンチなし、論文の図1でToonOutに劣る旨の定性比較、2022年版(HF repo更新は2026-08-17)、学習データにdanbooru収集画像。deepghs/imgutilsもsegment/isnetis.pyで同系モデルを使用(GitHub APIで確認)） / `Zarxrax/BiRefNet-Real_Anime`（BiRefNet_lite微調整(MIT、アニメ映像フレーム向け、2026-09-22公開)。DL0・likes0・ベンチなしで未検証） / `suzukimain/AnimeSeg`（背景除去はanime-segmentation(isnet)委譲のラッパー。ライセンス未記載、DL 30日6,636はあるがlikes1・ベンチなし）

関連リポジトリ:

- [danielgatis/rembg](https://github.com/danielgatis/rembg) — 背景除去CLI/ライブラリ(isnet-animeセッション標準搭載)（★25,013 / MIT / 最終push 2026-10-10 / release v2.0.85 (2026-09-20) / 確認コミット [`202e4264`](https://github.com/danielgatis/rembg/blob/202e42649a8492a7c49f808de36608a7d1cbbfe3/README.md)）
  - MIT、★24,932、v2.0.85(2026-09-20)。README記載: isnet-anime=アニメキャラ向け高精度、isnet-general-use等。最も普及した呼び出し口
- [MatteoKartoon/BiRefNet](https://github.com/MatteoKartoon/BiRefNet) — ToonOutの学習・推論コード(BiRefNetフォーク、デモノートブック)（★105 / MIT / 最終push 2026-06-12 / 確認コミット [`ba5d19a7`](https://github.com/MatteoKartoon/BiRefNet/blob/ba5d19a7bf16b1ea7746bb9e9bec83d97dad9709/README.md)）
  - MIT、★101、最終push 2026-06-12。論文・重み・データセットを一括公開。リリースタグなし
- [1038lab/ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG) — ComfyUIの背景除去ノード集(BiRefNet_toonOut、SAM3等)（★2,176 / GPL-3.0 / 最終push 2026-10-01 / 確認コミット [`58f1947a`](https://github.com/1038lab/ComfyUI-RMBG/blob/58f1947a11567a9f8b707223185570850e773856/README.md)）
  - GPL-3.0、★2,127、push 2026-08-21。READMEにBiRefNet_toonOut追加の記載(v2.9.2)
- [SkyTNT/anime-segmentation](https://github.com/SkyTNT/anime-segmentation) — ISNet-anime等の学習コード・デモ(HF skytnt/anime-seg)（★848 / Apache-2.0 / 最終push 2025-05-21 / 確認コミット [`55d87401`](https://github.com/SkyTNT/anime-segmentation/blob/55d874013a2811cdf59c365059174c7823acf5b4/README.md) / 制作カタログ: [anime-segmentation](../../categories/image.md#anime-segmentation)）
  - Apache-2.0、★844、最終push 2025-05-21(約16か月更新なし)。READMEの学習済みモデルは'skytnt/anime-seg'に掲載

### 画像セグメンテーション(キャラクター部位別レイヤー分解・セマンティックパース)

<a id="image-segmentation--body-part-layers"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [layerdifforg/seethroughv0.0.2_layerdiff3d](https://huggingface.co/layerdifforg/seethroughv0.0.2_layerdiff3d/tree/4477e6ce529bc6a141732e1a55a4932176db3b89)（revision `4477e6ce` / 作成 2026-03-09 / 更新 2026-09-28）
- **利用条件**: openrail++。Apache-2.0(作者は自リポジトリ準拠と議論#1で2026-04-07回答)かつ継承元ライセンスも適用: Animagine XL 4.0/SDXL=CreativeML Open RAIL++-M、LayerDiffuse=Open RAIL-M、VAE=MIT。カードは『商用利用可・ただしRAILの用途制限(paragraph 5/Attachment A)を再配布・ホスティング時に利用条項へ明記』と記載。メタデータ表記はopenrail++。これを踏まえても商用可とは断定しない
- **選定根拠**: 事実: layerdifforg/seethroughv0.0.2_layerdiff3dは、論文『See-through』(arXiv:2602.03749、SIGGRAPH 2026 Conference Papers採択)の中核で、1枚のアニメ立ち絵を19部位の半透明RGBAレイヤー(隠れ部補完つき)に分解する。Live2Dモデル由来の9,102体(学習7,404/検証851/テスト847)で学習。論文Table1(自己報告、自作2.5Dテスト)はマスクDice loss 0.3855・Mask MSE 0.0354・LPIPS 0.1549・PSNR 18.30で、SAM+LaMa(Dice loss 0.4336・MSE 0.1020・LPIPS 0.2880)より良い。SAM3は部位プロンプトで『髪やズボンの欠落・マスク重複』が多いとの定性比較(数値はSAM+LaMa行のみ)。採用実績: GitHub shitagaki-lab/see-through ★4,189(push 2026-09-24)、ComfyUI-See-through ★814、HF DL 30日19,507/累計88,354、likes27、Space17、NF4/GGUF派生あり。評価: 部位レベルのアニメ専用パーサとしては実測・採用とも突出。対抗のsuzukimain/AnimeSeg(12クラス顔部位+服、Mask2Former、DL30日6,636)はベンチなし・ライセンス未記載。疑い: 出力は生成モデルなので元画素を保存するセグメンテーションではなく、SDXL級のVRAMが必要(数値は未測定)。論文はCC BY-NC-SA 4.0表記だがコード・重みはApache-2.0宣言。
- **指標（確認日時点）**: DL累計 96,480 / 直近30日 21,039 / likes 29 / Spaces 17
- **概要**: SDXL(Animagine XL 4.0)ベースの拡散モデルで、アニメキャラ立ち絵を19部位のRGBAレイヤーに分解し、遮蔽された部位も補完する(See-throughパイプラインの1段目)。深度モデル(seethroughv0.0.1_marigold)とセットで描画順も推定
- **入力**: アニメキャラ立ち絵1枚(推奨解像度は公式未確認。ggml派生実装は1280px未満・30ステップ未満を拒否と説明)
- **出力**: 部位別の透過RGBA画像(19部位、ALPHA=部位マスク)。深度モデルと合わせてPSD書き出し
- **必要環境**: diffusers形式(SDXL系)。CUDA GPU前提。VRAM・速度は未測定。省メモリ用にNF4版あり。手順はGitHub shitagaki-lab/see-through(Python3.12/PyTorch 2.8+cu128等)
- **制約**: 生成モデルのため隠れ部は『推測』(論文図でもワイングラス重複などの失敗例を明記)。セグメンテーションのみの軽量用途には過剰。テスト・数値は論文著者の自作セットで外部再現なし。全身立ち絵が前提(背景再構成なし)
- **使う版・派生**: 本体: layerdifforg/seethroughv0.0.2_layerdiff3d。NF4: 24yearsold/seethroughv0.0.2_layerdiff3d_nf4、GGUF: icefog72/seethroughv0.0.2_layerdiff3d_gguf。旧版の部位定義とは'new tag definition'で非互換の可能性(カード記載)
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/layerdifforg/seethroughv0.0.2_layerdiff3d/blob/4477e6ce529bc6a141732e1a55a4932176db3b89/README.md) / [論文(SIGGRAPH 2026): 19部位・Live2D 9,102体・Table1 SAM+LaMa比較・SAM3との定性比較](https://arxiv.org/abs/2602.03749) / [公式実装(Apache-2.0)](https://github.com/shitagaki-lab/see-through)
- **次点**: `suzukimain/AnimeSeg`（Mask2Former+DINOv2/U-Net++(LoRA)の12クラス部位パーサ(肌・顔・髪・目・眉・鼻・口・服・小物)。DL30日6,636だがlikes1・ライセンス未記載・ベンチ記載なし。生成なしの軽量マスクが欲しい場合の候補） / `facebook/sam3`（汎用SAM3(テキスト/ビジュアルプロンプト)。See-through論文では部位プロンプトで欠落・重複が多いと報告(定性)。ゲート付きSAM License）

関連リポジトリ:

- [shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through) — 公式実装(レイヤー分解+擬似深度+PSD出力、ComfyUI/Live2D向け)（★4,520 / Apache-2.0 / 最終push 2026-10-05 / 確認コミット [`a25a5498`](https://github.com/shitagaki-lab/see-through/blob/a25a5498e031dc7fe01232d05dadaf67736277fb/README.md) / 制作カタログ: [see-through](../../categories/layer.md#see-through)）
  - Apache-2.0、★4,189、push 2026-09-24、SIGGRAPH 2026採択。リリースタグなし
- [jtydhr88/ComfyUI-See-through](https://github.com/jtydhr88/ComfyUI-See-through) — See-throughのComfyUIプラグイン（★834 / ライセンス未表示 / 最終push 2026-08-20 / 確認コミット [`98d754bf`](https://github.com/jtydhr88/ComfyUI-See-through/blob/98d754bf04f668647919ab750eccb0e0640faa81/README.md) / 制作カタログ: [comfyui-see-through](../../categories/layer.md#comfyui-see-through)）
  - ★814、push 2026-08-20。ライセンス未表示(GitHub上null)

### 画像セグメンテーション(アニメキャラクターのインスタンス分割)

<a id="image-segmentation--instance-segmentation"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [dreMaz/AnimeInstanceSegmentation](https://huggingface.co/dreMaz/AnimeInstanceSegmentation/tree/bc091c8cd74e234001eeacece6dd45038521254f)（revision `bc091c8c` / 作成 2023-03-09 / 更新 2023-12-23）
- **利用条件**: mit。メタデータMIT。同梱のZoeD_M12_N.pt(ZoeDepth)・kenburns系ckpt等は別ライセンスのため個別確認が必要。学習データの出所はデータセットカード側(未精査)。商用可とは断定しない
- **選定根拠**: 事実: dreMaz/AnimeInstanceSegmentation(MIT、2023-03-09作成・最終更新2023-12-23)は論文『Instance-guided Cartoon Editing with a Large-scale Dataset』(arXiv:2312.01943)のRTMDet-L系インスタンス分割(rtmdetl_e60.ckpt等)+refine重みで、アニメ/カートゥーンキャラを個体ごとに分割する。likes10・Space6・HF DL統計0(ckptのみ)、GitHub CartoonSegmentation/CartoonSegmentation ★204(push 2025-04-29)、データセットdreMaz/AnimeInstanceSegmentationDataset公開。See-throughのREADMEはアニメインスタンス分割(mmdet/mmcv)をオプション依存として記載(CartoonSegmentation由来かは[INFERENCE])。評価: アニメ専用のインスタンス分割の公開実装が他に見つからず選定。カードに数値ベンチがなく(論文本文の数値は未確認)、保守は2025-04で停止、mmdet/mmcv依存で導入が重い。自信度low。背景除去ならToonOut、部位分解ならSee-throughを使う。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 10 / Spaces 6
- **概要**: アニメ/カートゥーン画像中の各キャラクター個体を分割するRTMDet系インスタンス分割モデルと、マスク精緻化(refine)・3D Ken Burns用深度/inpaint重みの同梱リポジトリ
- **入力**: アニメ画像(複数キャラ可)
- **出力**: キャラ個体ごとのインスタンスマスク+ボックス
- **必要環境**: GitHub CartoonSegmentationの手順(mmdet/mmcv依存、git-lfsでHF repoをclone)。VRAM・速度は未測定
- **制約**: HFカードは論文リンクのみで数値・データ詳細なし。2023年のモデルで新しい生成系画風への汎化は未評価。重みにZoeDepth等の第三者ckptを含む(ライセンス個別確認が必要)
- **使う版・派生**: 重み: rtmdetl_e60.ckpt、refine_f3loss.ckpt/refine_last.ckpt、ZoeD_M12_N.pt等。派生: OS-Software/CartoonSegmentation-Base-ONNX、-Refiner-ONNX、text4555/CartoonSegmentation-Base-ONNX、Jakaline/CartoonSegmentationOnnx
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/dreMaz/AnimeInstanceSegmentation/blob/bc091c8cd74e234001eeacece6dd45038521254f/README.md) / [論文: アニメインスタンス分割データセットと手法](https://arxiv.org/abs/2312.01943)
- **次点**: `joelseytre/toonout`（背景除去(前景/背景の2値)でキャラ個体は分けられない。用途が別）

関連リポジトリ:

- [CartoonSegmentation/CartoonSegmentation](https://github.com/CartoonSegmentation/CartoonSegmentation) — 公式実装(インスタンス分割・Ken Burns等の応用)（★204 / ライセンス未表示 / 最終push 2025-04-29 / 確認コミット [`3dbf06ce`](https://github.com/CartoonSegmentation/CartoonSegmentation/blob/3dbf06ce0dc714dbd1980e9883c4bebcba947410/README.md)）
  - ★204、push 2025-04-29、ライセンス未表示(GitHub上null)。READMEでHF重み・データセット・CPU Spaceを案内

### マスク生成(SAM系・アニメ対応)

<a id="mask-generation"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [facebook/sam3](https://huggingface.co/facebook/sam3/tree/3c879f39826c281e95690f02c7821c4de09afae7)（revision `3c879f39` / 作成 2025-11-07 / 更新 2025-11-20）
- **利用条件**: other / gated。SAM License(2025-11-19版、独自): 使用・複製・配布は許諾されるが、制裁・輸出管理法規および軍事/戦争、核、スパイ活動、銃器等の用途は禁止、再配布には同ライセンス添付が必要(LICENSE本文を確認)。HFはmanualゲート。商用可とは断定しない(HFゲート: manual)
- **選定根拠**: 事実: HFのmask-generationでアニメ特化の微調整SAMは見つからず(HF検索 anime/manga/illustration/danbooru 等でヒット0)。論文See-throughは『SAMはアニメ画像でドメインギャップがある』とし、自前でSAM-HQの多デコーダ微調整を行って部位セグメンタを作った。汎用の最有力はfacebook/sam3(HF DL累計21.45M・30日2.17M・likes3,629、ComfyUI/ISAT/AnyLabeling等が対応)。日本語X(2026-01〜03)ではComfyUIのSAM3を組み込んだワークフロー(顔補正等)やアニメ用切り抜きに使う投稿があり(例: onsen_hphp 2026-03-17『アニメ用の切り抜きに普通に精度よくて驚く』)、実務で使われている。評価: アニメ専用版がないためsam3をgeneral_onlyで採用。SAM 3.1は動画追跡向けで静止画の優位は未確認。未解決: SAM License(独自・ゲート)とアニメでの定量ベンチの欠如。
- **指標（確認日時点）**: DL累計 22,085,166 / 直近30日 2,128,836 / likes 3,998 / Spaces 100
- **概要**: Meta Segment Anything 3。テキスト句・画像例・点/ボックス/マスクのプロンプトで、画像内の該当概念を全インスタンス分割(検出+マスク+動画追跡)する汎用モデル。アニメ専用ではない
- **入力**: RGB画像(+テキスト句/例示/点・ボックス・マスクのプロンプト)
- **出力**: インスタンスマスク・ボックス・スコア
- **必要環境**: 公式sam3パッケージ(PyTorch)で推論。HF Transformers統合の有無はカードに明記なし。VRAM・速度は未測定。ComfyUIはPozzettiAndrea/ComfyUI-SAM3やyolain/ComfyUI-Easy-Sam3で利用
- **制約**: アニメ特化ではない。See-through論文はSAM系に『アニメ画像でのドメインギャップ』があり、SAM3の部位プロンプトは髪・ズボンの欠落や重複が出ると報告(定性)。アニメでのベンチは未確認
- **使う版・派生**: sam3(画像中心、DL累計21.5M)。後継facebook/sam3.1(2026-03-26、動画マルチオブジェクト追跡7倍高速化が主眼、DL累計745k)。ComfyUI用Comfy-Org/sam3.1、軽量vil-uob/sam3-litetext-s0
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/facebook/sam3/blob/3c879f39826c281e95690f02c7821c4de09afae7/README.md) / [SAM 3論文(SA-CO、人間性能の75-80%を自己報告)](https://arxiv.org/abs/2511.16719)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `facebook/sam2.1-hiera-large` — 未確認(本調査では精査せず)。SAM2系はImpact-Pack(V8.18〜)・kijai/ComfyUI-segment-anything-2(Apache-2.0)で使える。ライセンスが緩い選択肢として検討余地
- **次点**: `facebook/sam3.1`（SAM3に動画用Object Multiplexを追加した後継(2026-03-26、gated manual、DL累計745k)。静止画アニメ用途での優位は確認できず） / `vil-uob/sam3-litetext-s0`（SAM3の軽量テキストエンコーダ版(DL30日18k)。精度・アニメ適性は未確認）

関連リポジトリ:

- [facebookresearch/sam3](https://github.com/facebookresearch/sam3) — 公式実装・学習コード(SAM 3)（★11,911 / NOASSERTION / 最終push 2026-10-07 / 確認コミット [`2345a4ad`](https://github.com/facebookresearch/sam3/blob/2345a4ad109ac29c569da749c91d84f10dc08c40/README.md)）
  - ★11,850、push 2026-09-18。ライセンスはGitHub上NOASSERTION(SAM License)
- [PozzettiAndrea/ComfyUI-SAM3](https://github.com/PozzettiAndrea/ComfyUI-SAM3) — ComfyUI向けSAM3ラッパー（★576 / NOASSERTION / 最終push 2026-08-24 / 確認コミット [`de0ff5d2`](https://github.com/PozzettiAndrea/ComfyUI-SAM3/blob/de0ff5d2c2ea435d29f800abfa568cffdfb94773/README.md)）
  - ★575、push 2026-08-24。ライセンスはNOASSERTION
- [kijai/ComfyUI-segment-anything-2](https://github.com/kijai/ComfyUI-segment-anything-2) — ComfyUI向けSAM2(Apache-2.0)（★1,222 / Apache-2.0 / 最終push 2025-09-28 / 確認コミット [`0c35fff5`](https://github.com/kijai/ComfyUI-segment-anything-2/blob/0c35fff5f382803e2310103357b5e985f5437f32/README.md)）
  - ★1,221、push 2025-09-28。SAM3のライセンス・ゲートを避けたい場合の代替
- [1038lab/ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG) — ComfyUIのSAM3/背景除去ノード集（★2,176 / GPL-3.0 / 最終push 2026-10-01 / 確認コミット [`58f1947a`](https://github.com/1038lab/ComfyUI-RMBG/blob/58f1947a11567a9f8b707223185570850e773856/README.md)）
  - GPL-3.0、★2,127、push 2026-08-21。READMEにSAM3 Segmentation追加(v2.9.4, 2025-11-24)の記載

### ゼロショット物体検出(テキスト指定・アニメ画像)

<a id="zero-shot-object-detection"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [facebook/sam3](https://huggingface.co/facebook/sam3/tree/3c879f39826c281e95690f02c7821c4de09afae7)（revision `3c879f39` / 作成 2025-11-07 / 更新 2025-11-20）
- **利用条件**: other / gated。SAM License(2025-11-19版、独自): 使用・複製・配布は許諾されるが、制裁・輸出管理法規および軍事/戦争、核、スパイ活動、銃器等の用途は禁止、再配布には同ライセンス添付が必要(LICENSE本文を確認)。HFはmanualゲート。商用可とは断定しない(HFゲート: manual)
- **選定根拠**: 事実: HFのzero-shot-object-detectionにアニメ特化モデルは見つからず(anime/manga等でヒット0)。アニメでの定量ベンチも見つからない。汎用ではIDEA-Research/grounding-dino-base(HF DL累計33.6M)がタスク内の標準だが、2026年の日本語X投稿ではComfyUIでSAM3(テキスト句プロンプトで検出+分割)をアニメ制作の検出・切り抜きに使う例が目立つ(onsen_hphp 2026-03-17、hyperboleonのSAM3ワークフロー等、いずれも実務者の個別投稿で定量ではない)。評価: SAM3はテキストでボックスとマスクを同時に得られ、PixAI Tagger v1.0がSAM3バックボーンを流用して精度を出した点からもアニメ画像への転移性が示唆されるが、ゼロショット検出としてのアニメ精度は[INFERENCE]。固定クラスが使えるならdeepghsの検出器(顔/頭/手/目/半身/人物)の方が実績的に確実。自信度low。
- **指標（確認日時点）**: DL累計 22,085,166 / 直近30日 2,128,836 / likes 3,998 / Spaces 100
- **概要**: Meta Segment Anything 3。テキスト句・画像例・点/ボックス/マスクのプロンプトで、画像内の該当概念を全インスタンス分割(検出+マスク+動画追跡)する汎用モデル。アニメ専用ではない
- **入力**: RGB画像(+テキスト句/例示/点・ボックス・マスクのプロンプト)
- **出力**: インスタンスマスク・ボックス・スコア
- **必要環境**: 公式sam3パッケージ(PyTorch)で推論。HF Transformers統合の有無はカードに明記なし。VRAM・速度は未測定。ComfyUIはPozzettiAndrea/ComfyUI-SAM3やyolain/ComfyUI-Easy-Sam3で利用
- **制約**: アニメ特化ではない。See-through論文はSAM系に『アニメ画像でのドメインギャップ』があり、SAM3の部位プロンプトは髪・ズボンの欠落や重複が出ると報告(定性)。アニメでのベンチは未確認
- **使う版・派生**: sam3(画像中心、DL累計21.5M)。後継facebook/sam3.1(2026-03-26、動画マルチオブジェクト追跡7倍高速化が主眼、DL累計745k)。ComfyUI用Comfy-Org/sam3.1、軽量vil-uob/sam3-litetext-s0
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/facebook/sam3/blob/3c879f39826c281e95690f02c7821c4de09afae7/README.md) / [SAM 3論文(SA-CO、人間性能の75-80%を自己報告)](https://arxiv.org/abs/2511.16719)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `IDEA-Research/grounding-dino-base` — 汎用Grounding DINO(Apache-2.0、HF DL累計33.6M・30日1.53M・likes211、ungated、HF transformers対応)。アニメ検出のベンチは未確認。ゲート/SAM Licenseを避けたい場合の代替
- **次点**: `IDEA-Research/grounding-dino-base`（Apache-2.0・ungatedで統合が容易だが、アニメでの優位性を示す資料が見つからず、テキスト指定のアニメ用途の実例(X)がSAM3に偏っていた）

関連リポジトリ:

- [facebookresearch/sam3](https://github.com/facebookresearch/sam3) — 公式実装(テキスト句プロンプト検出・分割)（★11,911 / NOASSERTION / 最終push 2026-10-07 / 確認コミット [`2345a4ad`](https://github.com/facebookresearch/sam3/blob/2345a4ad109ac29c569da749c91d84f10dc08c40/README.md)）
  - ★11,850、push 2026-09-18、ライセンスNOASSERTION(SAM License)
- [IDEA-Research/GroundingDINO](https://github.com/IDEA-Research/GroundingDINO) — Grounding DINO公式実装(Apache-2.0)（★10,660 / Apache-2.0 / 最終push 2024-08-12 / release v0.1.0-alpha2 (2023-04-07) / 確認コミット [`856dde20`](https://github.com/IDEA-Research/GroundingDINO/blob/856dde20aee659246248e20734ef9ba5214f5e44/README.md)）
  - ★10,640、最終push 2024-08-12(約2年更新なし)。リリースはv0.1.0-alpha2(2023-04-07)
- [ltdrdata/ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) — ComfyUIのDetailer・SAM連携(SAM2対応V8.18〜)（★3,334 / GPL-3.0 / 最終push 2026-04-19 / 確認コミット [`429d0159`](https://github.com/ltdrdata/ComfyUI-Impact-Pack/blob/429d0159ad429e64d2b3916e6e7be9c22d025c3c/README.md)）
  - GPL-3.0、★3,329、push 2026-04-19。READMEにSAM2対応の記載。SAM3対応は未確認

### キーポイント検出(アニメ顔ランドマーク28点)

<a id="keypoint-detection--face-landmarks"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [hysts/anime-face-detector-hrnetv2](https://huggingface.co/hysts/anime-face-detector-hrnetv2/tree/9b3435248b26aeb82e2a8578fe9d86d5d57158af)（revision `9b343524` / 作成 2026-07-05 / 更新 2026-07-05）
- **利用条件**: mit。MIT(メタデータ)。カード本文は『学習データの来歴は無保証(as-is)』と明記。商用可とは断定しない
- **選定根拠**: 事実: hysts/anime-face-detector-hrnetv2は『アニメ顔28点ランドマーク』(HRNetV2-W18+ヒートマップヘッド、flip test・DARKデコード)で、hystsが2021年にmmposeで訓練した公式重みを2026-07-05にHFへ移した(mmpose_anime-face_hrnetv2.pthのsafetensors化、v0.1.0以降はmmpose不要でPure PyTorch)。MIT、likes1、HF DL統計0(新規ミラー)。GitHub hysts/anime-face-detector ★535、コード参照234件(シード計測)、companion検出器はyolov3(既定)/faster-rcnn(高精度)。評価: 公開されているアニメ顔ランドマーク実装として最も利用例が多く、他の候補(public-data/anime_face_landmark_detection 2022、ライセンス不明)は実績が薄いため選定。疑い: 定量ベンチ(NME等)がカードにない、学習データの出所は『保証しない』とカードが明記、最新の画風(AI生成)での精度は未測定。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 1 / Spaces 0
- **概要**: アニメ顔の28点ランドマーク推定モデル(HRNetV2-W18、ヒートマップ)。顔領域は同梱のdetector(yolov3既定/faster-rcnn)で検出してから適用。hysts/anime-face-detectorパッケージが本体
- **入力**: 顔検出器が出した顔領域(RGB画像全体を渡せばパッケージが検出→ランドマークまで実行)
- **出力**: 顔ごとのバウンディングボックス+28点ランドマーク
- **必要環境**: pip install anime-face-detector(v0.1.0以降はPyTorchのみ、mmpose/mmdet不要)。速度・VRAMは未測定
- **制約**: ベンチ数値なし。正面寄りの顔が対象(yolov3側カードが'near-frontal'と記載)。学習データの来歴はカードが保証しないと明記
- **使う版・派生**: 本体: hysts/anime-face-detector-hrnetv2。検出器: hysts/anime-face-detector-yolov3(既定)、hysts/anime-face-detector-faster-rcnn(高精度・重い)。旧: public-data/anime_face_landmark_detection
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/hysts/anime-face-detector-hrnetv2/blob/9b3435248b26aeb82e2a8578fe9d86d5d57158af/README.md) / [公式実装(MIT): 顔検出+28点ランドマーク](https://github.com/hysts/anime-face-detector)
- **次点**: `public-data/anime_face_landmark_detection`（2022年の別実装(checkpoint_landmark_191116.pth)。ライセンス不明・更新停止・likes0）

関連リポジトリ:

- [hysts/anime-face-detector](https://github.com/hysts/anime-face-detector) — 顔検出+28点ランドマーク(PyTorch単体動作)（★536 / MIT / 最終push 2026-07-05 / release v0.0.5 (2021-11-15) / 確認コミット [`98a9fb48`](https://github.com/hysts/anime-face-detector/blob/98a9fb480fa04bdd96acbe4d98da191a898267f3/README.md)）
  - MIT、★535、push 2026-07-05。リリースは0.0.5(2021-11)でタグ更新なし。コード参照234件(シード)

### キーポイント検出(アニメ・イラストの人体ポーズ/OpenPose18)

<a id="keypoint-detection--body-pose"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [mrpm/ComfyUI-AnimePose-weights](https://huggingface.co/mrpm/ComfyUI-AnimePose-weights/tree/75396e167075ba8ab740635d0a8d58cd0ba8b30f)（revision `75396e16` / 作成 2026-08-08 / 更新 2026-08-08）
- **利用条件**: agpl-3.0。AGPL-3.0(原典から継承、誘導物・ネットワークサービス提供時はソース開示義務=AGPL section 13)とカードが明記。商用利用は制約が大きい。商用可とは断定しない
- **選定根拠**: 事実: イラスト人体ポーズはbizarre-pose-estimator(Chen & Zwicker、WACV 2022、arXiv:2108.01819、AGPL-3.0、GitHub ShuhongChen/bizarre-pose-estimator ★265・最終push 2025-02-03)が唯一の専用学習モデルで、『イラスト向けの転移学習+新データセット』を論文が提示。公式重みはGoogle Driveのみで、HF上の公式ミラーはない。HFにあるmrpm/ComfyUI-AnimePose-weights(2026-08-08作成、DL0、likes0、AGPL-3.0)はdalai2/ComfyUI-AnimePose(★3)の作者が重みを再パッケージ(ckpt→safetensors化、rcnn枝を除去、カードはbit同一と主張=こちらで未検証)したもの。そのリポジトリのREADMEは『写真用の人物検出器はイラストで発火しない』と説明し、8枚で検証した信頼度ゲート付きOpenPose-18を出力する。評価: 公開された専用モデルが他にないためbest扱いだが、HFの当該repoは非公式ミラーで、採用実績はごく小さい。自信度low。汎用DWPose(yzd-v/DWPose)はイラスト・デフォルメで不発の報告があるが本調査では未検証。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 0 / Spaces 0
- **概要**: bizarre-pose-estimator(WACV 2022)の重みを非公式に再パッケージしたもの。anime_pose_head.safetensors(ResNet骨格+キーポイントヘッド、37.5MB)とcharacter_bg_seg.safetensors(キャラ/背景セグメンタ、233MB)を収録。ComfyUI-AnimePoseノードが初回実行時に自動DL
- **入力**: アニメ/イラストのキャラ画像(ComfyUI-AnimePoseはOpenPose系前処理として使用)
- **出力**: OpenPose-18形式の骨格(信頼度ゲート・シルエットゲート付き、ControlNet OpenPose用)
- **必要環境**: ComfyUI(torch/torchvision/kornia/opencv/safetensors)。DetectronのRCNN枝はtorchvisionのkeypointrcnn_resnet50_fpnで代替と記載。VRAM・速度は未測定
- **制約**: 非公式の再パッケージ(原典はGoogle Drive配布)。カードのbit同一性(336/336 pose tensors、690/690 seg tensors)は作者の検証スクリプトによる主張で未確認。全身が写らない構図では関節が捏造されやすい(READMEも注意)。論文は2021年の学習
- **使う版・派生**: 原典: github.com/ShuhongChen/bizarre-pose-estimator(Google Drive配布)。HF上の公式ミラーなし。ComfyUIノード: dalai2/ComfyUI-AnimePose。実装は他にrealding/animepose(2024、safetensors 1ファイル、出所不明)
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/mrpm/ComfyUI-AnimePose-weights/blob/75396e167075ba8ab740635d0a8d58cd0ba8b30f/README.md) / [論文: イラスト向けポーズ推定の転移学習とデータセット](https://arxiv.org/abs/2108.01819) / [利用ノード(再パッケージの経緯・検証方法の記載)](https://github.com/dalai2/ComfyUI-AnimePose)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `yzd-v/DWPose` — 汎用DWPose(comfyui_controlnet_aux等で標準)。アニメ特化ではなく、イラストでの検出失敗の有無は未検証
- **次点**: `yzd-v/DWPose`（汎用の全身ポーズ(ControlNet標準)。アニメでの優劣は本調査で未検証(ComfyUI-AnimePoseのREADMEは写真用検出器がイラストで発火しないと主張)）

関連リポジトリ:

- [ShuhongChen/bizarre-pose-estimator](https://github.com/ShuhongChen/bizarre-pose-estimator) — 原典の学習・推論コード(AGPL-3.0)（★265 / AGPL-3.0 / 最終push 2025-02-03 / 確認コミット [`b72005c2`](https://github.com/ShuhongChen/bizarre-pose-estimator/blob/b72005c2521c42c34df5c91c3660abab4a86a00c/README.md)）
  - ★265、最終push 2025-02-03。重み・データセットはGoogle Drive配布(READMEの記載)
- [dalai2/ComfyUI-AnimePose](https://github.com/dalai2/ComfyUI-AnimePose) — ComfyUIのOpenPose前処理ノード(AGPL-3.0)（★6 / AGPL-3.0 / 最終push 2026-08-09 / 確認コミット [`315e758b`](https://github.com/dalai2/ComfyUI-AnimePose/blob/315e758b17a578a7efb9b3eb95fdf4061d256866/README.md)）
  - ★3、2026-08-08作成、push 2026-08-09。検証の薄い新規ラッパー(READMEで8枚検証と記載)
- [Fannovel16/comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) — ComfyUI標準のControlNet前処理集(DWPose・Anime Lineart等)（★4,219 / Apache-2.0 / 最終push 2026-09-28 / 確認コミット [`0cd29047`](https://github.com/Fannovel16/comfyui_controlnet_aux/blob/0cd290477128d42cdc3e76a826a402d866e8c684/README.md)）
  - Apache-2.0、★4,207、push 2026-09-28。アニメ専用ポーズはなく、汎用DWPose等。READMEにAnime Lineart等あり

### 深度推定(アニメキャラの擬似深度=描画順序)

<a id="depth-estimation--anime-character-pseudo-depth"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [layerdifforg/seethroughv0.0.1_marigold](https://huggingface.co/layerdifforg/seethroughv0.0.1_marigold/tree/4f4ffc46050b6feb764b628859968a26e76e6b6a)（revision `4f4ffc46` / 作成 2026-02-03 / 更新 2026-09-28）
- **利用条件**: openrail++。Apache-2.0(作者主張)+継承元ライセンス: Marigold Depth v1.1=Open RAIL++-M、Stable Diffusion 2系=CreativeML Open RAIL++-M(Attachment Aの用途制限が適用)。メタデータはopenrail++。商用可とは断定しない
- **選定根拠**: 事実: layerdifforg/seethroughv0.0.1_marigoldは、論文『See-through』(SIGGRAPH 2026)が分解レイヤーの重なり順を決めるために、Marigold Depth v1.1をアニメキャラ向けに微調整した擬似深度モデル(学習ラベルはLive2D ArtMeshの描画順を0〜1に正規化したもの)。HF DL 30日17,530/累計71,920、likes6、Space17、NF4/GGUF派生あり、GitHub本体★4,189。論文は一貫性モジュールによるAbsRel・δ1の改善を報告(数値は本文抽出で欠落、未確認)し、汎用DA/Marigoldとの定量比較は確認できない。評価: アニメキャラ専用の深度モデルはこれのみ。ただし出力は『描画順序』であり現実の距離ではないため、ControlNet深度や3D化の汎用用途には向かない。汎用の相対深度はDepth Anything V2系を使う(別項)。自信度low。
- **指標（確認日時点）**: DL累計 78,764 / 直近30日 18,283 / likes 6 / Spaces 17
- **概要**: Marigold Depth v1.1をアニメキャラ向けに微調整した擬似深度モデル。描画順序(ArtMeshの重なり)を画素単位で推定し、See-throughのレイヤー順序付けに使う
- **入力**: アニメキャラ立ち絵(See-throughパイプライン経由で部位レイヤーと併用)
- **出力**: 画素ごとの擬似深度マップ(0〜1の描画順序、現実距離ではない)
- **必要環境**: diffusers形式(Marigold/SD2系)。NF4版あり。VRAM・速度は未測定(論文は4090での所要秒数を記載するが本文抽出で数値欠落)
- **制約**: 実世界の深度ではなく『描画順序』を学習。外部ベンチ・汎用深度との比較なし。立ち絵キャラ前提で背景・風景には非対応の可能性
- **使う版・派生**: 本体: layerdifforg/seethroughv0.0.1_marigold。NF4: 24yearsold/seethroughv0.0.1_marigold_nf4、GGUF: icefog72/seethroughv0.0.1_marigold_gguf
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/layerdifforg/seethroughv0.0.1_marigold/blob/4f4ffc46050b6feb764b628859968a26e76e6b6a/README.md) / [論文: 擬似深度の学習ラベル(ArtMesh描画順)・一貫性モジュールによる改善](https://arxiv.org/abs/2602.03749)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `depth-anything/Depth-Anything-V2-Large` — アニメ立ち絵の相対深度を『現実的な奥行き』として使いたい場合の汎用選択(別項目general-relative-depth参照)
- **次点**: `prs-eth/marigold-depth-v1-1`（母体のMarigold汎用(Open RAIL++-M、DL累計159k)。アニメ微調整は行っていない汎用版）

関連リポジトリ:

- [shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through) — 深度モデルを含むSee-through公式実装（★4,520 / Apache-2.0 / 最終push 2026-10-05 / 確認コミット [`a25a5498`](https://github.com/shitagaki-lab/see-through/blob/a25a5498e031dc7fe01232d05dadaf67736277fb/README.md) / 制作カタログ: [see-through](../../categories/layer.md#see-through)）
  - Apache-2.0、★4,189、push 2026-09-24

### 深度推定(アニメ/イラストの汎用相対深度)

<a id="depth-estimation--general-relative-depth"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [depth-anything/Depth-Anything-V2-Large](https://huggingface.co/depth-anything/Depth-Anything-V2-Large/tree/cbbb86a30ce19b5684b7a05155dc7e6cbc7685b9)（revision `cbbb86a3` / 作成 2024-06-13 / 更新 2024-07-08）
- **利用条件**: cc-by-nc-4.0。CC-BY-NC-4.0(非商用)。商用ならSmall-hf(Apache-2.0)やDA3MONO-LARGE(Apache-2.0)を別途確認
- **選定根拠**: 事実: アニメ画像向けの汎用(風景・背景を含む)深度モデルはHFで見つからず(anime depth等でヒット0)。汎用ではdepth-anything/Depth-Anything-V2-Large(HF DL累計3.12M・30日147k・likes177、CC-BY-NC-4.0)とSmall-hf(Apache-2.0、DL累計23.8M・30日2.68M・Space100)が標準。2026年のX投稿ではアニメ/イラスト制作でDepth Anything V2が実用されている(oohiro35 2026-03-03『niji画像の動画化にDepth Anything V2で深度マップ→AEでフォーカスシフト』likes1,313、ryo05m/yachimat_mangaも実写→深度→アニメ映像生成に使用)が個別の実務投稿で定量ではない。DA3(DA3MONO-LARGE、Apache-2.0、2025-11、30日DL208k)は『DA2より幾何精度が高い』とカードが自己主張するが、アニメでの利用例・評価は未確認。評価: アニメ適性の一次証拠が弱いため選定はlow。品質優先でV2-Largeをbestにしたが、ライセンスがNCのため商用利用ならSmall-hf(Apache-2.0)またはDA3MONO-LARGEを検討する必要がある。
- **指標（確認日時点）**: DL累計 3,148,450 / 直近30日 69,582 / likes 179 / Spaces 24
- **概要**: 単眼相対深度推定(ViT-L、vitlエンコーダ)。カード記載: 合成ラベル画像595K+実画像62M超(ラベルなし)で学習、V1やSD系(Marigold等)よりロバストかつ約10倍高速と自己主張(自己報告)。アニメ特化ではない汎用モデルで、イラスト/アニメ画像に流用して深度マップを作る用途が多い
- **入力**: RGB画像
- **出力**: 相対深度(視差型)マップ
- **必要環境**: 公式Depth-Anything-V2(PyTorch、depth_anything_v2_vitl.pth)。ComfyUIはcomfyui_controlnet_auxが前処理として提供。VRAM・速度は未測定
- **制約**: アニメ画像での定量評価は未確認。輪郭線・べた塗りが多く、キャラが平面的な絵では奥行きが曖昧になりうる。出力は視差型相対深度で計量できない。Largeは非商用ライセンス
- **使う版・派生**: V2-Large(本選定)、Base/Small。Small-hfのみApache-2.0。後継: depth-anything/DA3MONO-LARGE(DA3、Apache-2.0)、DA3-LARGE-1.1
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/depth-anything/Depth-Anything-V2-Large/blob/cbbb86a30ce19b5684b7a05155dc7e6cbc7685b9/README.md) / [DA3は幾何精度向上を自己主張(Apache-2.0)](https://huggingface.co/depth-anything/DA3MONO-LARGE)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `depth-anything/Depth-Anything-V2-Small-hf` — 商用を見据えるならApache-2.0の軽量版
- **次点**: `depth-anything/DA3MONO-LARGE`（Apache-2.0・2025-11・30日DL208kで新しく、カードは『DA2より幾何精度が高い』と自己主張。アニメでの実例・評価を確認できずV2を優先） / `depth-anything/Depth-Anything-V2-Small-hf`（Apache-2.0で商用検討向け・DL累計23.8M。精度はLargeより低い）

関連リポジトリ:

- [DepthAnything/Depth-Anything-V2](https://github.com/DepthAnything/Depth-Anything-V2) — 公式実装(NeurIPS 2024)（★8,930 / Apache-2.0 / 最終push 2026-03-24 / 確認コミット [`a561b849`](https://github.com/DepthAnything/Depth-Anything-V2/blob/a561b849ebae10a6f5ef49e26c83cbbcd36c71bf/README.md)）
  - Apache-2.0(コード)、★8,887、push 2026-03-24
- [ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3) — DA3公式実装（★6,452 / Apache-2.0 / 最終push 2026-07-27 / 確認コミット [`3d835ec1`](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/3d835ec1a5802d64a8b8b15f817a1ab54809bfe4/README.md)）
  - Apache-2.0、★6,414、push 2026-07-27
- [Fannovel16/comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) — ComfyUI前処理(Depth Anything V2等)（★4,219 / Apache-2.0 / 最終push 2026-09-28 / 確認コミット [`0cd29047`](https://github.com/Fannovel16/comfyui_controlnet_aux/blob/0cd290477128d42cdc3e76a826a402d866e8c684/README.md)）
  - Apache-2.0、★4,207、push 2026-09-28。READMEにDepth Anything/V2の記載

### 画像分類(アニメ画像マルチラベルタガー / Danbooruタグ)

<a id="image-classification--tagger"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [pixai-labs/pixai-tagger-v1.0](https://huggingface.co/pixai-labs/pixai-tagger-v1.0/tree/9fe10addf9326e292da8a85a98ea74cd91b41771)（revision `9fe10add` / 作成 2026-09-15 / 更新 2026-09-22）
- **利用条件**: apache-2.0。Apache-2.0(メタデータ)。v0.9のカードは『Danbooru content has its own licenses』と注記しており、学習データ由来の権利は別。v1.0カードに追加の使用条件は見当たらない(確認範囲)。商用可とは断定しない
- **選定根拠**: 事実: pixai-labs/pixai-tagger-v1.0(2026-09-15公開、Apache-2.0、SAM3微調整バックボーン486.3M・入力1008px・30,877タグ[general15,043/character8,308/style4,917/copyright2,460/meta145/rating4]、知識カットオフ2026-05)のカード自己報告ベンチ(PixAI自社の2026-06〜08画像99,999枚、共有タグのみ、7モデル比較): General micro F1 0.6660(2位AnimeTIMM CAFormer B36 0.6435)、Character micro F1 0.9242(1位はAnimeTIMM SigLIP Giant 0.9265)、Style 0.8143(比較相手Camie v2は0.3764)。全カテゴリ完全語彙では総合micro F1 0.723。v0.9比でGeneral +6.8pt/Character +10.44pt。注意: 比較表にWD Tagger v3は含まれない(主張は『評価した8モデル内』に限定)。採用実績: HF DL 30日3,348/累計3,348(公開2週間)、likes66、Space2、discussions0。ComfyUIノード(sln77/ComfyUI-Tagger ★9)が生まれ始め、Xでもtoyxyz3(2026-09-24、likes102)が試験投稿。旧v0.9はlikes215・コード参照'pixai-tagger'299件(シード/本調査)。対するSmilingWolf/wd-*-tagger-v3は事実上の標準: swinv2は30日762k・累計3.25M・Space100・コード参照996件、eva02-largeは累計698k・likes218・コード参照778件、Apache-2.0。ただしデータは2024-02-28で停止、検証マクロF1 0.4772(自社検証)。評価: 品質・鮮度・タグ語彙はPixAI v1.0が上、互換性・安定度・導入容易性はWD v3が上。WDとの直接比較が未公開という未解決点があるため選定はmedium。互換性重視ならWD EVA02 Large v3/SwinV2 v3を既定に。
- **指標（確認日時点）**: DL累計 16,595 / 直近30日 16,595 / likes 97 / Spaces 2
- **概要**: アニメ画像向けマルチラベルタガー(Danbooru系タグ30,877種)。SAM3バックボーンを微調整し1008pxで入力、カテゴリ別推奨閾値(General0.17/Character0.27/Style0.15/Copyright0.24/Meta0.17/Rating0.41)を既定とする。PixAI Labs(PixAIは画像生成サービス)公開
- **入力**: アニメ/イラスト画像(縦横比維持で1008×1008にリサイズ+パディング)
- **出力**: カテゴリ別(general/character/style/copyright/meta/rating)のタグと確信度
- **必要環境**: PyTorch・torchvision・Transformers・timm・NumPy・Pillow。transformers.pipeline(trust_remote_code=True)で読み込み。H100 80GBでバッチ16・48.3枚/秒、B1レイテンシ24.95ms(カード記載、BF16+FP32シグモイド、前処理除外)。その他の環境は未測定。tagger_pipeline.py(リポジトリ内コード)をtrust_remote_codeで実行
- **制約**: アニメイラストが対象(他は未測定)。知識は2026-05まで。欠落・誤タグあり、安全審査・年齢確認に使用不可(カード明記)。ベンチはPixAIの自社データで自己報告、WD Tagger v3を比較対象に含まない。trust_remote_codeでリポジトリ内コードを実行する必要(安全性は未監査)
- **使う版・派生**: v1.0本体。ONNX等の派生: noaione/pixai-tagger-v1.0-onnx(2026-09-24)、DraconicDragon/pixai-tagger-v1.0-mixed-bf16(2026-09-19)。旧v0.9: pixai-labs/pixai-tagger-v0.9(gated auto)、deepghs/pixai-tagger-v0.9-onnx(likes50、imgutils対応)、Bedovyy/pixai-tagger-v0.9-timm。ComfyUI: sln77/ComfyUI-Tagger
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/pixai-labs/pixai-tagger-v1.0/blob/9fe10addf9326e292da8a85a98ea74cd91b41771/README.md) / [ベンチ図表データ(同一リビジョン)](https://huggingface.co/pixai-labs/pixai-tagger-v1.0/blob/9fe10addf9326e292da8a85a98ea74cd91b41771/figures/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `SmilingWolf/wd-eva02-large-tagger-v3` — アニメ特化(汎用ではない)。エコシステム互換の安全な既定。gated/trust_remote_code不要・ONNX+timm両対応
- **次点**: `SmilingWolf/wd-eva02-large-tagger-v3`（事実上の標準(Apache-2.0、likes218、累計698k、コード参照778件)。EVA02-L/448px・データは2024-02-28まで・検証F1 0.4772(P=R点、カードはマクロF1基準と記載、自社)。互換性重視の既定。PixAI v1.0とのベンチ直接比較なし） / `SmilingWolf/wd-swinv2-tagger-v3`（最も使われている軽量版(30日762k・累計3.25M・Space100・コード参照996件)。EVA02版との精度差はカード未確認） / `ashen-sensored/wd-eva02-tagger-2026-canary`（WD EVA02を2026-05-18データで追加学習(タグ16,473、+5,999新規)したドロップイン(Apache-2.0、likes24、30日4,292)。カードに作者情報・比較がほぼなく、検証F1 0.5416(P=R点、自社)のみ。鮮度は魅力だが実績が浅い）

関連リポジトリ:

- [pythongosssss/ComfyUI-WD14-Tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger) — ComfyUIのWD14タガーノード(WD v1.4系の流儀)（★1,244 / MIT / 最終push 2025-07-11 / 確認コミット [`9e0a6e70`](https://github.com/pythongosssss/ComfyUI-WD14-Tagger/blob/9e0a6e700299182fc05c58b62e7ad9f72182a78b/README.md)）
  - MIT、★1,243、最終push 2025-07-11。READMEはWD 1.4ベース。PixAI v1.0は直接非対応(sln77/ComfyUI-Tagger等を使う)
- [sln77/ComfyUI-Tagger](https://github.com/sln77/ComfyUI-Tagger) — ComfyUIでPixAI v1.0・Camie・Taggerineを使うノード（★15 / MIT / 最終push 2026-09-20 / 確認コミット [`0094e546`](https://github.com/sln77/ComfyUI-Tagger/blob/0094e546d6c90022fb3247bc679b683cdd134581/README.md)）
  - MIT、★9、push 2026-09-20。PixAI v1.0対応が確認できる数少ないノードだが新規で実績は薄い
- [jhc13/taggui](https://github.com/jhc13/taggui) — 画像キャプション/タグ編集GUI(WD系タガー含む)（★1,355 / GPL-3.0 / 最終push 2025-10-11 / release v1.34.0 (2025-10-11) / 確認コミット [`cb8cca71`](https://github.com/jhc13/taggui/blob/cb8cca712c066cf3d7f4248a21322187f8eae63e/README.md)）
  - GPL-3.0、★1,351、v1.34.0(2025-10-11)。READMEにWD Taggerモデルのタグ除外設定の記載
- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs系タガーのローダ(imgutils.tagging)。PixAI v0.9 ONNX、WD v3、Camie等に対応(v0.9カード記載)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)。PixAI v1.0への対応は未確認。imgutils/tagging/にpixai.py・wd14.py・camie.pyが存在(GitHub APIで確認)

### 画像分類(アニメ画像の美的スコア/品質段階)

<a id="image-classification--aesthetic"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [deepghs/anime_aesthetic](https://huggingface.co/deepghs/anime_aesthetic/tree/a83ab545e1d2a869f1180b99b2a7dee22ec3b97e)（revision `a83ab545` / 作成 2024-03-05 / 更新 2024-03-24）
- **利用条件**: openrail。メタデータはopenrail(用途制限のあるRAIL系)。学習データの出所・ライセンスはカード未記載。商用可とは断定しない
- **選定根拠**: 事実: deepghs/anime_aestheticは7段階(masterpiece/best/great/good/normal/low/worst)分類で、自己報告の最良はswinv2pv3_v0_448_ls0.2_x(Accuracy 40.88%、AUC 0.8214)、caformer_s36_v0_ls0.2は34.68%/0.7725。openrail、likes12、Space8。deepghs imgutilsから呼べ、discussion#1に『学習データは何か』が質問されたまま学習データはカード未記載。競合: skytnt/anime-aesthetic(2022、ONNX/ckpt、Space100だがHFカード欠落・ライセンス未記載)、shadowlilac/aesthetic-shadow(1.1Bパラメータ・1024px ViT、likes36、累計DL11k、ライセンスunknown、ベンチなし)とそのv2ミラー(RE-N-Y/aesthetic-shadow-v2は累計134,815DLだがカード空、NeoChen1024版はcc-by-nc-4.0)、kawaimasa/kawai-aesthetic-scorer-convnextv2(2025-12、約6万枚の作者主観5段階、Apache-2.0、DL累計2,129)。評価: 美的スコアは主観的でモデル間の比較ベンチ自体がない。数値(Accuracy/AUC)付きで体系的に管理されているのはdeepghsのみ。精度は7段階で40%程度と低く、データ選別の粗いフィルタ用途に限る。自信度low。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 12 / Spaces 8
- **概要**: アニメ画像を7段階の美的品質クラスに分類するdeepghsの分類器(CAFormer-S36、SwinV2 Base 448px)。imgutilsではanime_dbaesthetic系関数から利用
- **入力**: アニメ画像(448px前後)
- **出力**: 7クラス(masterpiece〜worst)の確率
- **必要環境**: ONNX/pytorch(ファイル一式)。推奨ローダdghs-imgutils。FLOPS: CAFormer-S36 22.1G/37.2M、SwinV2 46.2G/65.9M(カード記載)。速度は未測定
- **制約**: Accuracy約41%(7クラス)と低く絶対値は信頼しにくい。『美しさ』の定義・学習データはカード未記載(discussion#1で質問あり)。画風偏り・個人の好みの反映度は不明
- **使う版・派生**: swinv2pv3_v0_448_ls0.2_x(最良報告)、caformer_s36_v0_ls0.2。関連: deepghs/anime_dbrating(2024-03-06)
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/deepghs/anime_aesthetic/blob/a83ab545e1d2a869f1180b99b2a7dee22ec3b97e/README.md)
- **次点**: `shadowlilac/aesthetic-shadow`（1.1Bパラメータ1024px ViT(LAION系とは別のアニメ専用)。カードは用途説明のみでベンチなし、ライセンスunknown、最終更新2023-11-18。v2系は原本が確認できずミラー(RE-N-Y等)のみ） / `kawaimasa/kawai-aesthetic-scorer-convnextv2`（2025-12、Apache-2.0、約6万枚の作者主観で学習した5段階(SS〜C)。データ選別用途に明確だが主観モデルで、DL累計2,129、likes4） / `skytnt/anime-aesthetic`（Space100で古くから使われたが2022-11・2023-01以降更新なし、カード/ライセンス欠落）

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs分類器・検出器のローダ(imgutils.metrics.dbaesthetic等)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)。imgutils/metrics/dbaesthetic.pyの存在をGitHub APIで確認
- [deepghs/waifuc](https://github.com/deepghs/waifuc) — アニメ画像データセット収集パイプライン(フィルタにdeepghs分類器を利用)（★412 / MIT / 最終push 2024-08-24 / 確認コミット [`efe5c491`](https://github.com/deepghs/waifuc/blob/efe5c49171a94a6441a79b7d7b595d4b3a4eb51f/README.md)）
  - MIT、★409、最終push 2024-08-24(約2年更新なし)。READMEに'Efficient Train Data Collector for Anime Waifu'、『PyPI版は未整備でソースからインストール』と記載

### 画像分類(AI生成アニメ画像 vs 人間作画の判定)

<a id="image-classification--ai-generated-detection"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [deepghs/cls-ai-check-1m.caformer_s36.r512](https://huggingface.co/deepghs/cls-ai-check-1m.caformer_s36.r512/tree/ada73d0101e481e21918c0550c9e94e021a1eaa1)（revision `ada73d01` / 作成 2025-11-06 / 更新 2025-11-06）
- **利用条件**: mit。MIT(メタデータ)。学習データdeepghs/ai-check-1mはlicense:other・出所詳細はカード未記載。商用可とは断定しない
- **選定根拠**: 事実: deepghs/cls-ai-check-1m.caformer_s36.r512(2025-11-06、MIT、CAFormer-S36/512px、37.3M)はaiとhumanの二値で、自己報告のテストAccuracy 99.52%(F1/P/R 0.995、AUC 0.999)。学習・評価は同作者のdeepghs/ai-check-1m(AI50万/人間50万、min辺640px以下、ライセンスother)で同一分布。likes0・HF DL累計13。旧deepghs/anime_ai_check(2023、MIT)、より大きい画像向けcls-ai-check-500k-plus.caformer_s36.r640(累計16DL)もある。競合: legekka/AI-Anime-Image-Detector-ViT(2024-08、Apache-2.0、DL累計34,691・30日176、自己小規模評価5,000枚で94.68%、比較した汎用検出器は36〜80%)、saltacc/anime-ai-detect(2023-01、Space100、累計37,583DL)。評価: 分布内99.5%は有望だが、2026年の新世代(Anima/Z-Image/GPT系画像)への汎化は検証不能で、AI検出器は一般に世代ずれに弱い[INFERENCE]。採用実績も極小。自信度low。判定を法的・倫理的根拠に使わないこと。
- **指標（確認日時点）**: DL累計 13 / 直近30日 0 / likes 0 / Spaces 0
- **概要**: アニメ画像のAI生成/人間作画を二値分類するCAFormer-S36(512px)。deepghs/ai-check-1m(100万枚)で学習。ラベルai/human
- **入力**: アニメ/イラスト画像(512px)
- **出力**: ai/humanの確率
- **必要環境**: timm/Transformers(trust_remote_code=True)+dghs-imgutils>=0.19.0。FLOPs 78.8G/MACs 39.3G(カード)。速度は未測定。リポジトリ内のtimm_model.py等を読み込むためtrust_remote_code=Trueが必要(外部コード実行・未監査)
- **制約**: 自己データ分布内の評価のみ。リサイズ後画像(min辺640以下)で学習。最新の生成モデルや加工・再圧縮後の画像への頑健性は未評価。誤判定は人間作画の権利・信用問題になり得るため単独判断に使わない
- **使う版・派生**: 本体r512。関連: cls-ai-check-1m.caformer_s36(別解像度)、cls-ai-check-500k-plus.caformer_s36.r640、cls-ai-check-10k.mobilenetv4_conv_aa_large(軽量)。旧: deepghs/anime_ai_check
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/deepghs/cls-ai-check-1m.caformer_s36.r512/blob/ada73d0101e481e21918c0550c9e94e021a1eaa1/README.md) / [学習データ(100万枚、ai/human各50万、ライセンスother)](https://huggingface.co/datasets/deepghs/ai-check-1m)
- **次点**: `legekka/AI-Anime-Image-Detector-ViT`（Apache-2.0、PoC(ViT、実画像100万+AI21.7万)。自己評価5,000枚で94.68%。2024-08以降更新なし） / `saltacc/anime-ai-detect`（2023-01の先駆。Space100・累計37,583DLだが古く、現行生成モデルには不向きの可能性）

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)

### 画像分類(アニメ画像の種別: イラスト/漫画/アニメ映像/3D/非絵画)

<a id="image-classification--image-type"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [deepghs/anime_classification](https://huggingface.co/deepghs/anime_classification/tree/5ee62e06f5f4cd68a1c2f3bc5dc9805e827d37df)（revision `5ee62e06` / 作成 2023-06-02 / 更新 2024-10-31）
- **利用条件**: mit。MIT(メタデータ)。データセットdeepghs/anime_classificationのライセンス・出所はカード未記載。商用可とは断定しない
- **選定根拠**: 事実: deepghs/anime_classificationは『3d・bangumi(アニメ映像スクショ)・comic(漫画)・illustration・not_painting』の5分類で、自己報告の最新caformer_s36_v1.5_focalはAccuracy 95.06%/AUC 0.9957、v1.4_focal_fixedは96.21%/AUC 0.9971、mobilenetv3_v1.5_distは94.56%/AUC 0.9946(ラベル数が異なる版で同一条件ではない)。MIT、likes23、Space4、discussions0。アニメ/実写の二値はdeepghs/anime_real_cls(caformer_s36_v1.4 Accuracy 99.14%/AUC 0.9991、openrail、likes11、discussions3: 学習コード・データの提供要望あり)。競合: Mitchins/anime-style-classifier-v5/v6(2026、MIT、30日DL54〜62、likes0〜1)は画風分類で数値未確認、prithivMLmods/Anime-Classification-v1.0(2025-04、likes1)。評価: データセット作りの前処理(絵柄種別フィルタ)で実績が最も厚いのはdeepghs(waifuc/imgutils経由)。未解決: 評価データが自作で公開ベンチがない、実写判定は別モデルが必要。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 23 / Spaces 4
- **概要**: アニメ画像の種別を5クラス(3d/bangumi/comic/illustration/not_painting)に分類するdeepghs分類器。データセット構築のフィルタ用途(漫画・映像・3Dの除外等)
- **入力**: アニメ/イラスト系画像
- **出力**: 5クラス確率(3d, bangumi, comic, illustration, not_painting)
- **必要環境**: ONNX/ptファイル+dghs-imgutils。CAFormer-S36 22.1G FLOPs/37.2M、MobileNetV3 0.63G/4.18M(カード)。速度は未測定
- **制約**: 自己データでの精度(約95%)。5クラス版(v1.5)は旧4クラス版と直接比較できない。『not_painting』の境界(ゲーム画面・宣伝画像等)は曖昧。実写判定は別モデル(anime_real_cls)
- **使う版・派生**: 推奨: caformer_s36_v1.5_focal(最新)。軽量: mobilenetv3_v1.5_dist。実写/アニメ二値: deepghs/anime_real_cls(caformer_s36_v1.4)
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/deepghs/anime_classification/blob/5ee62e06f5f4cd68a1c2f3bc5dc9805e827d37df/README.md)
- **次点**: `deepghs/anime_real_cls`（anime/realの二値(Accuracy 99.14%)に特化した別モデル(openrail)。種別細分が要らなければこちらが簡単） / `Mitchins/anime-style-classifier-v6`（画風分類(2026-03-23、MIT、likes1、30日DL54)。カードの定量評価を未確認・実績なし）

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)

### ゼロショット画像分類(アニメCLIP)

<a id="zero-shot-image-classification"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [OysterQAQ/DanbooruCLIP](https://huggingface.co/OysterQAQ/DanbooruCLIP/tree/aa2e603035bdf3e414e349f98ab2f9d3f6b43c5d)（revision `aa2e6030` / 作成 2023-05-18 / 更新 2023-07-17）
- **利用条件**: 未記載。ライセンス表記なし(メタデータ空)。学習データはDanbooru2021とpixiv(権利は投稿者に帰属し利用条件は別途)。ベースのOpenAI CLIPの条件はカード未記載(要確認)。商用可とは断定しない
- **選定根拠**: 事実: OysterQAQ/DanbooruCLIPはOpenAI CLIP ViT-L/14をDanbooru2021(2023-07-17更新でpixivデータを追加)で微調整し、キャラ名・作品名・一般タグを含む英文キャプションで学習(カードに前処理コード)。HF DL 30日1,234/累計52,553、likes16、Space1、discussions1(safetensors要望)。ライセンス表記なし、ベンチ数値なし。競合: deepghs/siglip_beta(2025-05、Apache-2.0、カード冒頭が『本番利用不可』と明記、WD SwinV2タガーを凍結したSigLIT風、Space1)、dudcjs2779/anime-style-tag-clip(EVA02 base、学習2.9万枚・検証R@1 0.877、DL累計550)、aki-0421/clip-anime-patch400-10k-v1(日本語のキャラ検索用、Apache-2.0、DL累計697)。評価: アニメ専用のCLIP系ゼロショット分類で最も普及しているのがDanbooruCLIPだが、2年以上前で定量評価がなく、ライセンス不明・Danbooru由来データの権利が曖昧。汎用SigLIP2はアニメ細部に弱い可能性があるが検証未了。自信度low。
- **指標（確認日時点）**: DL累計 52,635 / 直近30日 201 / likes 16 / Spaces 1
- **概要**: CLIP ViT-L/14をDanbooru2021(+pixiv)で微調整したアニメ画像-テキスト対照モデル。キャラ名・作品名・タグ文でゼロショット分類/検索ができる
- **入力**: アニメ画像+候補テキスト(英語タグ・キャラ名)
- **出力**: 画像-テキスト類似度(ロジット)
- **必要環境**: transformers(CLIPModel)。pytorch_model.bin(pickle形式。safetensors化はdiscussion#1で要望中)。VRAM・速度は未測定
- **制約**: 定量ベンチなし。データはDanbooru2021+pixivで2021年以降の新キャラ・新画風は未知。ライセンス未表記。pytorch_model.binはpickle形式のため信頼できる入手元を確認すること
- **使う版・派生**: pytorch_model.bin(2023-07-17版)、pytorch_model_2023-05-24.bin(旧版)。派生: なし確認
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/OysterQAQ/DanbooruCLIP/blob/aa2e603035bdf3e414e349f98ab2f9d3f6b43c5d/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `google/siglip2-so400m-patch14-384` — 汎用SigLIP2(Apache-2.0、DL累計11.6M・30日1.09M)。アニメ特化ではなく、アニメでの比較は未確認
- **次点**: `deepghs/siglip_beta`（SigLIP/SigLIT風の新しい試み(2025-05、Apache-2.0、imgutils>=0.17対応)だがカードが『本番利用不可』と明記。DL統計0・likes11） / `dudcjs2779/anime-style-tag-clip`（EVA02 base CLIP、29,187枚で学習、検証R@1 0.877(自己報告・小規模)。DL累計550、likes4）

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)。siglip_predict(imgutils.generic)でdeepghs/siglip_betaを呼べる(カードの使用例)

### 特徴量抽出(アニメキャラクター同一性=CCIP埋め込み)

<a id="image-feature-extraction--character-identity"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [deepghs/ccip](https://huggingface.co/deepghs/ccip/tree/8f636fb81a9f4342dfe220a16144525c2bece2a1)（revision `8f636fb8` / 作成 2023-05-15 / 更新 2024-09-09）
- **利用条件**: openrail。メタデータはopenrail(用途制限のあるRAIL系)。学習データの出所・権利はカード未記載(キャラ画像はdanbooru等の二次創作が含まれる可能性があるがカード未確認)。商用可とは断定しない
- **選定根拠**: 事実: deepghs/ccip(Contrastive Anime Character Image Pre-Training)は『2枚の画像のキャラが同一か』の類似度を出す埋め込みモデルで、カード表の自己報告は最良のccip-caformer_b36-24がF1 0.9409(精度0.9383/再現0.9436/閾値0.2132)、クラスタ評価Cluster_2 0.895・Cluster_Free 0.957。次点ccip-caformer-24-randaug-pruned F1 0.9172、ccip-v2-caformer_s36-10 F1 0.9064。openrail、likes13(onnx版10)、Space3、discussions1。データはdeepghs/character_similarity・character_index(カードのメタデータ)。GitHubコード検索'deepghs/ccip'82件、deepghs/imgutils(metrics.ccip・★415)とwaifuc(★409)が組み込み。競合: nebulette/ccip-anime-character-id(2026-06-29、Apache-2.0、最大6,000の女性キャラ、DL0・likes0、数値なし)。HFで他のアニメキャラ再識別モデルは検索でヒットなし。評価: 同一キャラ判定の公開専用モデルとして唯一体系的なベンチ表を持つ。単一キャラ画像が前提で、2024以降の更新なし。自信度medium。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 13 / Spaces 3
- **概要**: 1画像1キャラを前提に、アニメキャラの同一性を埋め込みの距離で判定するdeepghsのCCIP(CAFormer系)。データセット整理(キャラ別クラスタリング、他キャラ混入の除去)に使われる
- **入力**: 単一キャラが写るアニメ画像(複数キャラは前提外)
- **出力**: キャラ埋め込み(画像対の差分は0に近いほど同一キャラ)。推奨閾値はモデルごと(b36-24は約0.213)
- **必要環境**: ckpt/onnxを同梱、推奨ローダdghs-imgutils(ccip_batch_differences等)。FLOPs・速度は未測定
- **制約**: カードの条件『単一キャラのみ』。ベンチは自己データ・F1基準。新キャラ・新画風への汎化と髪型・衣装差分への頑健性は不明。2024-09-09以降更新なし。カードでアーキテクチャの質問(discussion#1)が未解決
- **使う版・派生**: 推奨: ccip-caformer_b36-24(カード最良)。ONNX版: deepghs/ccip_onnx(likes10)。派生: Library-Mutsumi/ccip・ccip_onnx(ミラー)、nebulette/ccip-anime-character-id(別実装)
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/deepghs/ccip/blob/8f636fb81a9f4342dfe220a16144525c2bece2a1/README.md) / [ONNX版(likes10)](https://huggingface.co/deepghs/ccip_onnx)
- **次点**: `nebulette/ccip-anime-character-id`（2026-06-29の別実装(Apache-2.0、6,000キャラ程度、DL0・likes0)。ベンチなし・実績なし）

関連リポジトリ:

- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)。imgutils/metrics/ccip.pyの存在をGitHub APIで確認
- [deepghs/waifuc](https://github.com/deepghs/waifuc) — キャラ別データセット作成パイプライン(CCIP等)（★412 / MIT / 最終push 2024-08-24 / 確認コミット [`efe5c491`](https://github.com/deepghs/waifuc/blob/efe5c49171a94a6441a79b7d7b595d4b3a4eb51f/README.md)）
  - MIT、★409、最終push 2024-08-24(約2年更新なし)。READMEは『PyPI版未整備、ソースからインストール』

### 特徴量抽出(アニメ画像の類似検索・重複検出の汎用埋め込み)

<a id="image-feature-extraction--general-retrieval"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [facebook/dinov3-vitl16-pretrain-lvd1689m](https://huggingface.co/facebook/dinov3-vitl16-pretrain-lvd1689m/tree/ea8dc2863c51be0a264bab82070e3e8836b02d51)（revision `ea8dc286` / 作成 2025-08-06 / 更新 2025-08-19）
- **利用条件**: other/dinov3-license / gated。DINOv3 License(独自、gated manual)。条件の細部は本文(LICENSE)未精査。商用可とは断定しない(HFゲート: manual)
- **選定根拠**: 事実: HFのimage-feature-extractionにアニメ特化の汎用埋め込み(illustration2vec系)は見つからず(anime/illustration embedding/danbooru embedding/anime dinov2等のHF検索でヒット0)。アニメ画像のタグ空間埋め込みを出すdeepghs/wd14_tagger_with_embeddings(2024-05、likes26)やdeepghs/anime_sites_indices(検索用インデックスと推測)が存在するが汎用ベンチはない。汎用ではfacebook/dinov3-vitl16-pretrain-lvd1689m(HF DL30日628k・累計7.65M・likes967、ViT-L/16)がタスク内で最多級で、カードは『専門SOTAを微調整なしで上回る』と自己主張。アニメでの評価は未確認。評価: 完全一致/近似重複はpHash・LPIPS(imgutils.metrics)で足りるが、意味的類似検索にはDINOv3/SigLIP2の選択肢があり、アニメでの優劣は検証未了。ライセンスはDINOv3独自(gated manual)で、緩さ重視ならSigLIP2(Apache-2.0)。自信度low。
- **指標（確認日時点）**: DL累計 7,988,710 / 直近30日 738,059 / likes 1,150 / Spaces 82
- **概要**: DINOv3の蒸留ViT-L/16(LVD-1689M事前学習)。クラストークン/パッチ特徴を抽出し、類似画像検索・重複検出・クラスタリング等に使う汎用自己教師あり埋め込み。アニメ特化ではない
- **入力**: RGB画像(16の倍数サイズ。224でcls1+register4+patch196トークン)
- **出力**: クラストークン・パッチトークン埋め込み
- **必要環境**: transformers/timm(timm/vit_large_patch16_dinov3.lvd1689mもあり)。VRAM・速度は未測定
- **制約**: アニメ専用ではなく、イラスト・線画での検索精度・キャラ同一性の区別は未確認(キャラ同一性はCCIPを使う)。ゲート付き
- **使う版・派生**: ViT-S/B/L/H+/7B、ConvNeXt版。timmミラー: timm/vit_base_patch16_dinov3.lvd1689m等。アニメ用タグ空間埋め込み: deepghs/wd14_tagger_with_embeddings
- **根拠**: [モデルカード(リビジョン固定): 用途・条件・自己報告ベンチ・ライセンス記載](https://huggingface.co/facebook/dinov3-vitl16-pretrain-lvd1689m/blob/ea8dc2863c51be0a264bab82070e3e8836b02d51/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `google/siglip2-so400m-patch14-384` — ゲートなし・Apache-2.0の汎用埋め込み。ライセンス重視ならこちら
- **次点**: `google/siglip2-so400m-patch14-384`（Apache-2.0・DL累計11.6M。画像-テキスト共通空間でアニメ検索に流用できるが、アニメでの比較は未確認）

関連リポジトリ:

- [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) — DINOv3公式実装（★11,515 / NOASSERTION / 最終push 2026-07-15 / 確認コミット [`6876159a`](https://github.com/facebookresearch/dinov3/blob/6876159a11b4df116f30f667f8c9888617df0751/README.md)）
  - ★11,471、push 2026-07-15、ライセンスNOASSERTION(DINOv3 License)
- [deepghs/imgutils](https://github.com/deepghs/imgutils) — deepghs全モデルのローダ(detect_faces等・CCIP・タグ付け・キャラ抽出を同梱)（★422 / MIT / 最終push 2025-10-11 / release v0.19.0 (2025-09-10) / 確認コミット [`46df848d`](https://github.com/deepghs/imgutils/blob/46df848dc4d20ac93f4919a40e2636d5f7c19766/README.md)）
  - MIT。★415、最新リリースv0.19.0(2025-09-10)、最終push 2025-10-11(約1年更新なし=保守停滞の懸念)。READMEに物体検出・CCIP・画像タグ付け・キャラ抽出を記載。GitHubコード検索'imgutils.detect'232件(シード計測)。imgutils/metrics(lpips_clustering等)で差分・重複検出を提供
