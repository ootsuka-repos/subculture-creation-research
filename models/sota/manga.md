# マンガ・OCR・文書のアニメ系SOTA（2026-10-01）

[一覧へ](../anime-task-sota.md) · [リポジトリ全体像](../anime-repositories.md) · [正本JSON](../../sota-catalog.json)

選定基準・注意は[一覧ページ](../anime-task-sota.md)。各項目の「最良」は確度付きの編集判断で、重み取得・推論実行は未実施。

### 画像→テキスト(漫画の吹き出し・台詞クロップOCR)

<a id="image-to-text--manga-dialogue-ocr"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [JustANormalTinkerer/hayai-ocr-v2.5-nova](https://huggingface.co/JustANormalTinkerer/hayai-ocr-v2.5-nova/tree/e34d7755ed11e626c5ba39544af5d66f20ee57cc)（revision `e34d7755` / 作成 2026-09-20 / 更新 2026-09-21）
- **利用条件**: apache-2.0。メタデータは apache-2.0。カードの datasets に hal-utokyo/Manga109-s が列挙されている。Manga109-s は学習結果の商用利用を許すが、事前学習済みモデルを公開する際に Manga109-s の利用を明記すること等の条件がある(manga109 公式サイトの License 節)。ほかに学習へ使った非公開の約1Mサンプル OCR コーパス、約1.82k 枚の手選別漫画クロップ、Wikipedia・青空文庫・独自の Japanese-Dialogue-Dataset(デコーダ用)の権利関係はカードに記載がなく未確認。視覚エンコーダ siglip2-base-patch16-naflex のライセンスは本調査で未確認。商用可とは断定しない。
- **選定根拠**: 【事実】JMangaBench_Mixed(第三者 muscgab 作。3,286クロップ=Manga109-s実画像1,286+合成2,000)で Hayai v2.5 Nova(patch512)は CER 3.10%/完全一致80.68%、manga-ocr は4.68%/73.52%、Baberu 4.59%/72.25%、PaddleOCR-VL-For-Manga 2.91%/78.91%(Nova数値はカード自己報告。別作者 Kellenok/PP-OCRv6_manga のカードも同ベンチで Nova 3.11% と再現)。第三者 sorryhyun は HF 議論でゼロショット評価を公開: Manga109-s∩COO test で台詞 exact が manga-ocr 62.1%、PaddleOCR-VL-1.6 63.4%、Hayai v2.1 78.4%(Novaではなくv2.1)。Baberu 作者の Manga109-v2026(n=2000)でも Baberu lCER 0.0345 < manga-ocr 0.0422(自己報告)。新世代が2022年の標準を上回る結果は4系統で一致。採用: manga-ocr-base は HF DL 累計9,750,174・30日1,134,204・likes183・spaces42、GH 2,791★で BallonsTranslator/comic-translate/MangaTranslator/manga-translator-ui/Lumina(既定)が採用。一方 Koharu(5.7k★)は既定を汎用 PaddleOCR-VL 1.6 に移し、0.79.0(2026-08-26)で Hayai(v2)を追加、Baberu も選択可能で、manga-ocr 一強ではなくなった。Nova 自体は作成2026-09-20・likes0・DL1,125と未成熟。X上の言及は Baberu 作者の自己宣伝のみで Hayai の評判は確認できない。【評価】精度優先なら Hayai Nova、互換性・実績優先なら manga-ocr-base。Hayai は Manga109-s を学習セット列挙しており JMangaBench 実画像部分への漏洩可否が未確認、訓練コーパス非公開のため暫定best・低信頼とする。
- **指標（確認日時点）**: DL累計 1,125 / 直近30日 1,125 / likes 0 / Spaces 1
- **概要**: 約150MパラメータのCJK+英語OCR。SigLIP2 NaFlex視覚エンコーダ(約86M)+12層因果デコーダ(約60M)。v2.5はDSCProjectorでデコーダ側視覚トークンを1/4にし、静的KVキャッシュで高速化。検出器なしで切り抜き1枚を1回のforwardで文字列にする。
- **入力**: 吹き出し・SFX・テキスト行の切り抜き画像(ページ全体は不可)。max_num_patches は 256(速度)/384(既定)/512(最高品質)から選ぶ。
- **出力**: 認識文字列(greedy、repetition_penalty=1.0 推奨)。
- **必要環境**: カード記載: transformers の AutoModel を trust_remote_code=True で読み込み(独自の block-causal attention と2D mRoPE)、プロセッサは google/siglip2-base-patch16-naflex。v2カードには FP16 で約300MB VRAM の記載があるがNovaの値ではない。本調査では未測定。
- **制約**: 切り抜き専用で別途テキスト検出器が必要。作成から11日・likes 0。訓練データは非公開(約1Mの私的OCRコーパス+手選別1.82k漫画クロップ)。Kellenok のカード表では SFX(加重CER 17.01 vs PP-OCRv6_manga v0.2 26.14)は強いが、webtoon では CER 13.03(PP-OCRv6_manga 4.43)と弱く、ランダム文字列の合成希少漢字も弱い。Koharu が同梱するのは hayai-ocr-v2 で Nova ではない。カード既知事項: trust_remote_code 必須。
- **使う版・派生**: 同リポジトリに ONNX/TFLite はなし(ファイル8点)。旧版 hayai-ocr-v2(Koharu同梱、カードに『outdated』、DL累計7,920)、v2-onnx / v2-tflite(JustANormalTinkerer)、vadik82/hayai-ocr-v2-onnx・hayai-ocr-v25-onnx(第三者ONNX)。ヘルパーライブラリ NopeNopeGuy/hayai-ocr(Apache-2.0)。
- **根拠**: [JMangaBench_Mixed でのCER/完全一致(patch別)、アーキテクチャ、訓練手順、Manga109-s の datasets 列挙、既知制約(自己報告)](https://huggingface.co/JustANormalTinkerer/hayai-ocr-v2.5-nova/blob/e34d7755ed11e626c5ba39544af5d66f20ee57cc/README.md) / [第三者ベンチ作者による基準結果: MangaOCR 4.683%、Baberu 4.589%、PaddleOCR-VL-0.9B-For-Manga 2.910%(RTX4090, n=3,286)](https://github.com/muscgab/JMangaBench_Mixed/blob/9b8396a6191597c4ed58e05d35bf9f116a1e2d81/README.md) / [別作者の表2: JMangaBench で hayai v2.5 nova(p512) 3.11%、SFX 17.01% が最良、webtoon/漫画ページ/希少漢字では PP-OCRv6_manga v0.2 が上(自己報告)](https://huggingface.co/Kellenok/PP-OCRv6_manga/blob/ba1d479e8a61a20e8318c9758c73fbbbd290b98d/README.md) / [第三者 sorryhyun による Hayai v2.1 / manga-ocr / PaddleOCR-VL-1.6 のゼロショット比較(Manga109-s∩COO test と同人誌OOD)](https://huggingface.co/sorryhyun/paddleocr-vl-1.6-manga-lora/discussions/1) / [Koharu 0.79.0(2026-08-26)で Hayai OCR 追加(#988)](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/CHANGELOG.md) / [Baberu 作者の Manga109-v2026(n=2000) 比較: lCER Baberu 0.0345 / PaddleOCR-VL 0.0368 / manga-ocr 0.0422](https://huggingface.co/genshiai-daichi/baberu-ocr/blob/d9cc13153e9a1cd8fdfa3b7b1cc329da2020aeae/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `PaddlePaddle/PaddleOCR-VL-1.6` — 汎用VLM OCR(Koharu既定、likes509、30日DL41,057、Apache-2.0)。漫画では stock が台詞exact 63.4%・暴走91件・SFX 30.2%(sorryhyun評価)と弱い。多言語・文書系は強い。
- **次点**: `kha-white/manga-ocr-base`（採用は圧倒的(DL累計9,750,174、30日1,134,204、likes183、spaces42、Apache-2.0、GH 2,791★)で互換性・安定性の既定。ただし最終更新2022-06。JMangaBench CER 4.68%、同人誌OODのSFXは6/619(第三者評価)。精度より互換性を取るなら本命。） / `jzhang533/PaddleOCR-VL-For-Manga`（JMangaBench CER 2.91%・exact78.91%と数値は最良だが、Manga109-s クロップで学習(カード)しておりベンチ実画像部分への漏洩が疑われる(Baberu作者も同様に除外)。0.9Bで遅い(RTX4090 p50 211.8ms vs manga-ocr 74.8ms)。likes136、最終更新2025-11、手書き漢字弱点の議論あり。） / `genshiai-daichi/baberu-ocr`（115M・日中英・ONNX対応でKoharu/Lumina対応。Manga109-v2026 lCER 0.0345(自己報告)だが、JMangaBenchでは manga-ocr と同等(4.59 vs 4.68)。manga-ocr/PaddleOCR-VL からの蒸留。DL累計2,062・likes12。ONNX量子化版で約64字切れの既知issue。）

関連リポジトリ:

- [koharu-rs/koharu](https://github.com/koharu-rs/koharu) — 検出→OCR→消去→翻訳→植字の統合アプリ。OCRに PaddleOCR-VL 1.6/Manga OCR/Baberu/Hayai を選択可（★5,693 / Apache-2.0 / 最終push 2026-09-30 / release 0.83.5 (2026-09-22) / 確認コミット [`45b4cae1`](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md)）
  - 最も活発な漫画翻訳アプリ(リリース0.83.5、2026-09-22)。OCRモデルを選択式で比較運用できる
- [NopeNopeGuy/hayai-ocr](https://github.com/NopeNopeGuy/hayai-ocr) — Hayai OCR 公式ヘルパーライブラリ（★8 / Apache-2.0 / 最終push 2026-09-21 / release v2.3.0 (2026-09-21) / 確認コミット [`54c2771e`](https://github.com/NopeNopeGuy/hayai-ocr/blob/54c2771e11424f2c732cf32be22d616220ad8c4c/README.md)）
  - v2.3.0(2026-09-21)。★8と小規模だがNova対応の唯一の配布経路
- [kha-white/manga-ocr](https://github.com/kha-white/manga-ocr) — 標準manga-ocr Python/CLI。互換性の基準（★2,792 / Apache-2.0 / 最終push 2026-07-19 / release v0.1.16 (2026-07-19) / 確認コミット [`c333b5d3`](https://github.com/kha-white/manga-ocr/blob/c333b5d36e88d539d6b040b4c4cf90ad5ecd4f69/README.md) / 制作カタログ: [manga-ocr](../../categories/localization.md#manga-ocr)）
  - 2,791★、v0.1.16(2026-07-19)。多数の翻訳ツールが採用
- [muscgab/JMangaBench_Mixed](https://github.com/muscgab/JMangaBench_Mixed) — 日本語漫画OCRの再現可能ベンチ(3,286サンプル)（★1 / GPL-3.0 / 最終push 2026-07-28 / 確認コミット [`9b8396a6`](https://github.com/muscgab/JMangaBench_Mixed/blob/9b8396a6191597c4ed58e05d35bf9f116a1e2d81/README.md)）
  - 第三者作。Manga109-s画像は各自取得。★1と小さいが複数モデルカードが引用

### 画像→テキスト(オノマトペ・効果音SFXのOCR)

<a id="image-to-text--onomatopoeia-ocr"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [JustANormalTinkerer/hayai-ocr-v2.5-nova](https://huggingface.co/JustANormalTinkerer/hayai-ocr-v2.5-nova/tree/e34d7755ed11e626c5ba39544af5d66f20ee57cc)（revision `e34d7755` / 作成 2026-09-20 / 更新 2026-09-21）
- **利用条件**: apache-2.0。メタデータは apache-2.0。カードの datasets に hal-utokyo/Manga109-s が列挙されている。Manga109-s は学習結果の商用利用を許すが、事前学習済みモデルを公開する際に Manga109-s の利用を明記すること等の条件がある(manga109 公式サイトの License 節)。ほかに学習へ使った非公開の約1Mサンプル OCR コーパス、約1.82k 枚の手選別漫画クロップ、Wikipedia・青空文庫・独自の Japanese-Dialogue-Dataset(デコーダ用)の権利関係はカードに記載がなく未確認。視覚エンコーダ siglip2-base-patch16-naflex のライセンスは本調査で未確認。商用可とは断定しない。 SFXデータとして使われうる COO(ku21fan/COO-Comic-Onomatopoeia)は Manga109 画像を要するため、COOを含むモデルは Manga109 利用条件の影響を受ける(本モデルのCOO使用有無は未確認)。
- **選定根拠**: 【事実】SFX(擬音・手書き風デザイン文字)は台詞より難しく、汎用/標準モデルが崩れる。第三者 sorryhyun の評価(HF議論)では、Manga109-s∩COO test のSFX exact が manga-ocr 26.2%・PaddleOCR-VL-1.6 30.2%・Hayai v2.1 74.2%(v2.1.5は54.7%)、同人誌OOD 619行では manga-ocr 6・PaddleOCR-VL 14・Hayai v2.1 177・v2.1.5 309 と Hayai が大差で上。Kellenok の表でもSFX加重CER は Hayai Nova(p512)17.01% で、PP-OCRv6_manga v0.2 26.14%、公式PP-OCRv6 medium 73.21% を上回る(自己報告)。SFX特化の sorryhyun/paddleocr-vl-1.6-manga-lora は COO 台詞・SFX exact 83.9%/88.1%、OOD 305/617 と自己報告で最高だがDL473・likes0・ベース(PaddleOCR-VL-1.6)と878MBの視覚タワーの両方が必要で、Novaとの直接比較はない(作者が Nova-preview の評価を依頼中)。【評価】Hayai Nova を暫定best。SFXは♡などの記号の扱い・長さ7字以上で崩れやすく、COO(ECCV2022)の公式ベースラインは exact 81.2% なので、精度が要る工程では専用ファインチューンが必要。検出側は Koharu Layout の onomatopoeia クラスだが COO の box AP は 0.4431 と弱い。
- **指標（確認日時点）**: DL累計 1,125 / 直近30日 1,125 / likes 0 / Spaces 1
- **概要**: Hayai OCR v2.5 Nova(切り抜きOCR、約150M)。日本語・中国語・韓国語・英語のSFX/手書き風文字を含む切り抜きを読む。SFX(COO)に強い点は第三者評価・別作者の表で確認されている。
- **入力**: SFXを含むテキスト領域の切り抜き(検出は別モデルが必要)。
- **出力**: 認識文字列。
- **必要環境**: manga-dialogue-ocr と同じ(trust_remote_code、siglip2 naflex プロセッサ)。未測定。
- **制約**: ♡など装飾記号の脱落(sorryhyun: Hayai v2.1 で130行)、長いSFXで精度低下。Nova のSFX単独の第三者評価は未公開。訓練データ非公開。
- **使う版・派生**: manga-dialogue-ocr エントリと同一リポジトリ・同一revision。SFX特化の代替: sorryhyun/paddleocr-vl-1.6-manga-lora(LoRA+視覚タワー)。
- **根拠**: [アーキテクチャ・訓練手順・既知制約(自己報告)](https://huggingface.co/JustANormalTinkerer/hayai-ocr-v2.5-nova/blob/e34d7755ed11e626c5ba39544af5d66f20ee57cc/README.md) / [Manga109-s∩COO と同人誌OODでの manga-ocr/PaddleOCR-VL/Hayai の SFX exact(第三者、自前評価セット)](https://huggingface.co/sorryhyun/paddleocr-vl-1.6-manga-lora/discussions/1) / [表2のSFX加重CER: hayai nova(p512) 17.01 / PP-OCRv6_manga v0.2 26.14 / v0.1 45.03(自己報告)](https://huggingface.co/Kellenok/PP-OCRv6_manga/blob/ba1d479e8a61a20e8318c9758c73fbbbd290b98d/README.md) / [SFX特化LoRAの自己報告値(COO SFX exact 83.9%、OOD 305/617)](https://huggingface.co/sorryhyun/paddleocr-vl-1.6-manga-lora/blob/26292839d1469c14212a12a1e01b5b1fe01bff15/README.md)
- **次点**: `sorryhyun/paddleocr-vl-1.6-manga-lora`（SFX特化で自己報告値は最高(COO SFX exact 83.9%)だが、DL累計473・likes0、LoRA+878MB視覚タワーの2ファイル構成、暴走対策は利用側実装。Novaとの直接比較が無く、COO公式分割の訓練データを含むためManga109条件の影響あり。） / `PaddlePaddle/PaddleOCR-VL-1.6`（汎用。stockのSFX exactは30.2%、暴走91件(sorryhyun評価)。Koharuの既定OCRだがSFXには不向き。） / `kha-white/manga-ocr-base`（SFX exact 26.2%、同人誌OODで6/619(sorryhyun評価)と、標準モデルはSFXに弱い。台詞用途では実績最大。）

関連リポジトリ:

- [koharu-rs/koharu](https://github.com/koharu-rs/koharu) — SFXを onomatopoeia クラスで検出しOCR・消去まで繋ぐ（★5,693 / Apache-2.0 / 最終push 2026-09-30 / release 0.83.5 (2026-09-22) / 確認コミット [`45b4cae1`](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md)）
  - Layoutモデルが text/onomatopoeia/bubble/panel を出力し、OCR→inpaintまで同一パイプライン
- [ku21fan/COO-Comic-Onomatopoeia](https://github.com/ku21fan/COO-Comic-Onomatopoeia) — COO(Comic Onomatopoeia)データセットと公式ベースライン(ECCV2022)（★95 / ライセンス未表示 / 最終push 2025-02-18 / 確認コミット [`d8028f01`](https://github.com/ku21fan/COO-Comic-Onomatopoeia/blob/d8028f015b8ce99a4dd798427342f97087529357/README.md)）
  - SFXの標準データ。Manga109画像は別取得。ライセンス表記なし(メタデータ上null)
- [NopeNopeGuy/hayai-ocr](https://github.com/NopeNopeGuy/hayai-ocr) — Hayai OCR ヘルパー（★8 / Apache-2.0 / 最終push 2026-09-21 / release v2.3.0 (2026-09-21) / 確認コミット [`54c2771e`](https://github.com/NopeNopeGuy/hayai-ocr/blob/54c2771e11424f2c732cf32be22d616220ad8c4c/README.md)）
  - Nova実行に使う公式ラッパー

### 画像→テキスト(ギャルゲー/VN・ゲーム画面の日本語OCR)

<a id="image-to-text--game-vn-screen-ocr"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [rtr46/meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0/tree/a28cf5874dc2438ebb1c86336be26bcec51e3375)（revision `a28cf587` / 作成 2025-11-03 / 更新 2026-02-24）
- **利用条件**: lgpl-3.0。HFメタデータは lgpl-3.0、GitHub(rtr46/meikiocr)のライセンス表示は Apache-2.0 と食い違う。どちらが重みに適用されるか作者未明示。学習データ(日本語ゲームの画面)の権利関係はカードに記載なし。商用可とは断定しない。
- **選定根拠**: 【事実】rtr46/meiki.txt.recognition.v0 は日本語ビデオゲーム(カード例はVN風画面)の画面テキストで学習した文字認識モデル(D-FINE+MobileNetV4、文字を物体検出として出力)。HF DL累計675,671・30日97,882・likes7。検出側 meiki.text.detect.v0 も30日49,706。owocr の README は meikiocr を『Recommended / OneOCR に匹敵する精度とCPU遅延』と記載(README上 Recommended が付くオープン重みのローカルOCRは meikiocr のみで、他の Recommended は OneOCR・Chrome Screen AI・Apple Live Text・Google Lens)。対抗は oshizo/donut-base-japanese-visual-novel(2023-05、VN風合成データ、1920x1080のみ、30日DL53・likes8)で、更新も採用も停滞。漫画用 manga-ocr は『印刷日本語OCRとしても使える』とカードにあり owocr が併載するが、VN画面の定量比較は確認できない。【評価】ゲーム/VN画面は meiki を選ぶ。ただし精度ベンチはカード内の画像(パレートグラフ)のみで数値表なし・自己報告、横書きのみ・1行48文字・検出64ボックス上限(v0.1)という制約がある。ライセンス表記もHF(LGPL-3.0)とGitHub(Apache-2.0)で食い違う。漫画の縦書きには使えない。
- **指標（確認日時点）**: DL累計 675,671 / 直近30日 97,882 / likes 7 / Spaces 1
- **概要**: 日本語ビデオゲーム画面のテキスト行認識モデル。『文字認識を文字検出に置き換える』D-FINE系のファインチューン(MobileNetV4バックボーン)。960x32に整形した行画像から最大48文字を文字+bbox+信頼度で出力。検出モデル meiki.text.detect(tiny=VN向け低遅延、small=行数が多い画面向け)と組で meikiocr パッケージになる。
- **入力**: 960x32へリサイズ・パディングした横書き1行の画像(検出は meiki.text.detect)。
- **出力**: 文字・bbox・信頼度のリスト(推奨後処理は inference.py、ONNX)。
- **必要環境**: ONNX Runtime(CPU可、NVIDIA GPUは onnxruntime-gpu 推奨とGitHub README記載)。CPU遅延はカード内の図のみ。本調査では未測定。
- **制約**: 横書きのみ・最大48文字/行。ゲーム画面で学習しており範囲外では性能が変わるとカード明記。検出v0.1は64ボックス上限で漫画検出には不向き(カード)。学習に用いたゲーム画像の出所・権利はカードに記載なし。数値ベンチはグラフのみで自己報告。
- **使う版・派生**: 同じ recognition 内に 960x32 横書き版と vertical.32x480 版のONNX。検出は rtr46/meiki.text.detect.v0(v0.1の320x192/960x544版を含む)。パイプラインは meikiocr(PyPI、GitHub rtr46/meikiocr)。2026-02-21に新チェックポイントへ更新(旧revision ddd06176… も指定可)。
- **根拠**: [用途・制約(横書き、48文字、ゲーム学習)、2026-02-21の更新、パレート主張(自己報告)](https://huggingface.co/rtr46/meiki.txt.recognition.v0/blob/a28cf5874dc2438ebb1c86336be26bcec51e3375/README.md) / [owocr が meikiocr を Recommended(OneOCR相当の精度、64行・48文字制限)として掲載](https://github.com/AuroraWright/owocr/blob/0339f3412bf68c2385e88b59f4c59e4e1c2fe946/README.md) / [meikiocr: 日本語ビデオゲーム向け、PaddleOCR/EasyOCR を上回ると主張(自己報告、グラフのみ)](https://github.com/rtr46/meikiocr/blob/52aa607ecdc1038c7bf390f37cd9a8b306e8a08a/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `PaddlePaddle/PaddleOCR-VL-1.6` — 汎用多言語OCRの有力候補(likes509)。ゲーム画面での比較は未確認。owocr は非オープン重みのOneOCR/Chrome Screen AI/Google Lensも推奨している。
- **次点**: `oshizo/donut-base-japanese-visual-novel`（VN風の合成画面(1920x1080)専用のDonut。names/messages/optionsをJSONで出力できる点は独自だが、2023-05から更新なし、30日DL53・累計1,982・likes8。縦横比が違うと精度低下、ルビ非対応。） / `kha-white/manga-ocr-base`（印刷日本語OCRとしても使えるとカードに記載、owocrが併載。ただしVN画面での定量比較が無く、テキスト検出を別途要する。漫画・縦書き向き。）

関連リポジトリ:

- [rtr46/meikiocr](https://github.com/rtr46/meikiocr) — meiki検出+認識のPythonパイプライン(CLI/ライブラリ)（★97 / Apache-2.0 / 最終push 2026-09-25 / 確認コミット [`52aa607e`](https://github.com/rtr46/meikiocr/blob/52aa607ecdc1038c7bf390f37cd9a8b306e8a08a/README.md)）
  - 97★、Apache-2.0表示、2026-09-25更新。VN/ゲーム用OCRとして owocr が推奨
- [AuroraWright/owocr](https://github.com/AuroraWright/owocr) — 画面キャプチャ→OCRの多エンジン常駐ツール(manga-ocr/meikiocr/OneOCR等)（★301 / GPL-3.0 / 最終push 2026-06-03 / release 1.26.8 (2026-03-28) / 確認コミット [`0339f341`](https://github.com/AuroraWright/owocr/blob/0339f3412bf68c2385e88b59f4c59e4e1c2fe946/README.md)）
  - 301★、GPL-3.0、v1.26.8(2026-03-28)。manga-ocr・meikiocr・OneOCR など多エンジンを切替えられる常駐OCRツール
- [HIllya51/LunaTranslator](https://github.com/HIllya51/LunaTranslator) — VN翻訳ツール(フック+OCR+翻訳)（★13,488 / GPL-3.0 / 最終push 2026-09-30 / release v10.17.1.12 (2026-09-26) / 確認コミット [`363de635`](https://github.com/HIllya51/LunaTranslator/blob/363de6354ef9d085403f78f325cff5d69b97eda8/README.md)）
  - 13,485★(本調査の検索結果中でVN翻訳系最大)、GPL-3.0、2026-09-26リリース
- [bpwhelan/GameSentenceMiner](https://github.com/bpwhelan/GameSentenceMiner) — ゲーム/VNからの言語学習用センテンスマイニング(owocr連携)（★859 / GPL-3.0 / 最終push 2026-09-29 / release v2026.9.4 (2026-09-26) / 確認コミット [`7dac58bc`](https://github.com/bpwhelan/GameSentenceMiner/blob/7dac58bc1a54b2f2b953787f36d587a2aedeb176/README.md)）
  - 859★、GPL-3.0、v2026.9.4(2026-09-26)。owocr を統合

### 画像→テキスト(アニメ・イラストのキャプション/booruタグ生成)

<a id="image-to-text--illustration-captioning"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [fancyfeast/llama-joycaption-beta-one-hf-llava](https://huggingface.co/fancyfeast/llama-joycaption-beta-one-hf-llava/tree/ebf414ea497a020da0f82df3913e5b6cb8e9663a)（revision `ebf414ea` / 作成 2025-05-11 / 更新 2025-05-16）
- **利用条件**: 未記載。HFメタデータにlicense欄なし(本調査の取得値はnull)。ベースが meta-llama/Llama-3.1-8B-Instruct のためLlama 3.1 Community Licenseの条件が及ぶ可能性が高い(推測、要確認)。GitHub の joycaption コードは Apache-2.0。カードは『no restrictions』と述べるが商用可とは断定しない。
- **選定根拠**: 【事実】アニメ特化の自然文キャプションモデルは実用水準のものが見つからない: Andres77872/SmolVLM-500M-anime-caption-v0.2(Apache-2.0、LLM生成の合成キャプション40万件=SFW/NSFW各20万で学習、30日DL85・累計5,584・likes8、ベンチなし)、damoncao/Anime_Image2Prompt(30日DL15)、GilbertKrantz/blip-image-captioning-base-anime(DL0)。一方 fancyfeast/llama-joycaption-beta-one-hf-llava は拡散モデル学習用キャプション用VLMで、HF DL累計1,782,131・30日103,006・likes399・spaces100、GitHub fpgaminer/joycaption 1,268★。プロンプトモードに『Danbooru tag list』『Stable Diffusion Prompt(自然文+booru風タグ)』等(GitHub README確認分)があり、アニメ/イラストの学習データ整備で最も使われるキャプショナ。アニメ専用ではなく写真・デジタルアート・アニメを同等に扱う(カード)ため general_only。booru形式タグ出力の sorryhyun/anima-tagger(Anima学習形式のタグ列)は30日DL291・累計884・likes15で、実体は animetimm の GPL-3.0・ゲート付き分類器+小さな追加ヘッド。タグ付け(分類器)の首位比較は別スライス(image-classification)に委ねる。【評価】検証済みの比較ベンチは見当たらず、採用実績で JoyCaption Beta One を選ぶ。成人向け専用モデル(Qwen3-VL-8B-NSFW-Caption 系)は best 対象外として reviewed_not_included に記録。
- **指標（確認日時点）**: DL累計 1,782,131 / 直近30日 103,006 / likes 399 / Spaces 100
- **概要**: Llama-3.1-8B-Instruct+SigLIP2(so400m-patch14-384)ベースの画像キャプションVLM。拡散モデル学習用に『自由・無検閲・多様』を掲げ、写真・デジタルアート・アニメ等を同等に扱う。GitHub README によれば Danbooru/e621/Rule34 タグ列や Stable Diffusion プロンプト風など複数のプロンプトモードを持つ。
- **入力**: 画像+プロンプト(モード指定文)。LlavaForConditionalGeneration、チャットテンプレートの組み立てに注意(カードが警告)。
- **出力**: 自然文キャプションまたは Danbooru/e621/Rule34 形式のタグ列。
- **必要環境**: カード記載: bfloat16、device_map=0 の例。VRAM等の数値はカードになし。本調査では未測定。
- **制約**: アニメ専用ではない。NSFWも含む無検閲の学習設計(成人向け専用ではなく SFW/NSFW 同等カバレッジ)。Danbooruタグ出力の精度ベンチは確認できず。HFのtransformers v5互換議論が未解決(discussion #18)。
- **使う版・派生**: GGUF: concedo/llama-joycaption-beta-one-hf-llava-mmproj-gguf(30日14,595)、mradermacher/…-GGUF、FP8: NeoChen1024/…-FP8-Dynamic、NF4: John6666/…-nf4。旧版 alpha-two(累計22,230/30d)。
- **根拠**: [用途・設計方針(SFW/NSFW同等、アニメ/デジタルアート含む)、使用例](https://huggingface.co/fancyfeast/llama-joycaption-beta-one-hf-llava/blob/ebf414ea497a020da0f82df3913e5b6cb8e9663a/README.md) / [プロンプトモード一覧(Danbooru tag list / Stable Diffusion Prompt / e621 / Rule34)](https://github.com/fpgaminer/joycaption/blob/8445b2e55db7856d522e44ae84e7415fcf3413f6/README.md) / [アニメ特化キャプション候補の学習設定(合成40万件、SFW/NSFW各20万、Apache-2.0)](https://huggingface.co/Andres77872/SmolVLM-500M-anime-caption-v0.2/blob/30b5f2f137ed28c7c9ab14b4b95f1367cc3440fc/README.md)
- **次点**: `Andres77872/SmolVLM-500M-anime-caption-v0.2`（アニメ特化(SmolVLM-500M、Apache-2.0)だが、30日DL85・累計5,584・likes8、合成キャプション依存、ベンチなし、作者は『写真・非アニメは対象外』と明記。採用実績の差が大きい。） / `sorryhyun/anima-tagger`（Anima学習形式(rating,count,characters,copyrights,general)のタグ列を出す。MIT表記だが背骨の animetimm/caformer_b36.dbv4-full は GPL-3.0 ゲート付き。30日DL291・累計884。タグ付けの本命比較は image-classification 側。）

関連リポジトリ:

- [fpgaminer/joycaption](https://github.com/fpgaminer/joycaption) — JoyCaption の学習・推論・プロンプトモード集（★1,269 / Apache-2.0 / 最終push 2026-02-24 / 確認コミット [`8445b2e5`](https://github.com/fpgaminer/joycaption/blob/8445b2e55db7856d522e44ae84e7415fcf3413f6/README.md)）
  - 1,268★、Apache-2.0、最終更新2026-02-24。アニメLoRA/ファインチューン用データ作成で広く使われるキャプショナの公式リポジトリ

### 画像+テキスト→テキスト(漫画ページ理解VLM:ページOCR+VQA)

<a id="image-text-to-text--manga-understanding-vlm"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [hal-utokyo/MangaLMM](https://huggingface.co/hal-utokyo/MangaLMM/tree/a556fbc7edc256fbd6d3b4d8d3418dd5d68f7c27)（revision `a556fbc7` / 作成 2025-05-16 / 更新 2025-06-01）
- **利用条件**: mit。HFメタデータは mit。ただし学習データ MangaOCR/MangaVQA は Manga109(109巻)とCOOを統合して作られ、Manga109 本体は『学術目的・非営利機関のみ』、Manga109-s(87巻)のみ商用利用可(manga109 公式 License 節)。MangaLMM がどちらの範囲で学習したかはカード本文に記載なし(論文は109巻を使用と記載)。ベースの Qwen2.5-VL-7B-Instruct のライセンスは本調査で未確認。商用可とは断定しない。
- **選定根拠**: 【事実】論文 MangaVQA and MangaLMM(arXiv 2505.20298、EACL Findings 2026採択、東京大学・Aizawa研)の Table 2(自己ベンチ、Manga109の見開きページ)で、MangaOCR(ページ内の検出+認識、IoU0.5のHmean)は MangaLMM 71.5%、GPT-4o/Gemini 2.5 Flash/Claude Sonnet 4.5 と、Qwen2.5-VL 以外の6オープンモデル(Phi-4-multimodal, Pangea-7B, LLaVA-OV-1.5-8B, Sarashina2-Vision-8B, Gemma-3-12B, Heron-NVILA-Lite-15B)は全て0.0%(Qwen2.5-VL-7B は0.9%)。MangaVQA(526問、Gemini 2.5 FlashをLLM審判、10点満点)は Gemini 2.5 Flash 7.26、MangaLMM 6.68、GPT-4o 6.00、Claude Sonnet 4.5 5.84、Qwen2.5-VL-7B 5.65、Gemma-3-12B 4.13。オープンモデル最高かつGPT-4o超え、Geminiには届かない。HF: DL累計9,331・30日364・likes13・spaces2(公式デモあり)、GitHub manga109/mangalmm 50★(MIT)。【評価】漫画専用VLMとして実績と論文ベンチを持つのはこれのみ。ただしQwen2.5-VL-7Bベース(2025-05)で古く、Qwen3-VL・Gemma 4・Qwen3.5/3.6(Koharuが翻訳LLMに採用)等の新しいVLMとの比較は論文にも他所にも見つからない(未検証)。学習データにManga109を含むため商用利用可否に注意。ページ単位のOCR+座標が要るなら本モデル、商用パイプラインなら Koharu Layout系検出+Hayai等の切り抜きOCRの組合せが現実的。
- **指標（確認日時点）**: DL累計 9,331 / 直近30日 364 / likes 13 / Spaces 2
- **概要**: Qwen2.5-VL-7B-Instruct を MangaOCR(Manga109+COO由来、全体約20.9万インスタンス、うち訓練約17万)と合成VQA(GPT-4oが生成した約4万問)で1エポックのみ共同ファインチューンした漫画特化LMM。ページ単位で『bbox_2d + text_content』のJSONを出力するOCRと、漫画内容についてのVQAの双方を1モデルで扱う。
- **入力**: 漫画ページ画像(Manga109見開き1654x1170で学習、Qwen2.5-VLの画素数しきい値方式で3,136〜2,116,800ピクセル)+指示文(OCR指示/質問)。
- **出力**: OCR: bbox_2d と text_content のJSON列。VQA: 自然文の回答。
- **必要環境**: カード本文に要件の記載なし。論文: 学習は A100×4で約2時間。評価時のMangaOCR推論は単一A100で10時間超(公式README)。推論VRAM等は未測定。
- **制約**: OCRの検出Hmean 78.6%、end-to-end 71.5%(再現率68.5%で約3割の本文が未検出)。ページ番号等の注釈外テキストを誤検出。VQAは文字認識の誤りで失敗する例が論文に示される。学習1エポック、訓練・評価ともManga109中心で同人誌・カラー・縦読みへの一般化は未検証。
- **使う版・派生**: mradermacher/MangaLMM-GGUF・MangaLMM-i1-GGUF(30日DL1,833/780)、alfredplpl/MangaLMM(動作修正fork、重み無し)。公式デモ Space: yuki-imajuku/MangaLMM-Demo。
- **根拠**: [モデル概要、公式デモ・コードへのリンク(カードは短い)](https://huggingface.co/hal-utokyo/MangaLMM/blob/a556fbc7edc256fbd6d3b4d8d3418dd5d68f7c27/README.md) / [MangaVQA/MangaOCR、Table 2(MangaLMM 71.5% / VQA 6.68、他モデルのOCRは0%台)、EACL Findings 2026](https://arxiv.org/abs/2505.20298) / [プロジェクトページ: 結果表、データ統計、分割(シリーズ内/著者内/未知著者)](https://manga109.github.io/MangaVQA_LMM/) / [公式実装、学習スクリプト、評価手順(MangaOCR推論に単一A100で10時間超)](https://github.com/manga109/mangalmm/blob/d06fb95af6d91311569d07fec393e339c8ab91d1/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `Qwen/Qwen2.5-VL-7B-Instruct` — MangaLMMのベース。論文ではMangaVQA 5.65・MangaOCR 0.9%。MangaVQAの最高値はプロプライエタリの Gemini 2.5 Flash(7.26)。より新しいオープンVLMの漫画ベンチは未確認。
- **次点**: `ragavsachdeva/magiv3`（Florence-2系の漫画/コミック理解VLM(ICCV2025)。コマ・キャラ・文字・吹き出し尾の検出、OCR、キャラ接地が可能だが、自由質問のVQAではなく定型タスク。非商用ライセンス。30日DL2,235、likes20。） / `psyka-101/GLM-OCR-Manga-LoRA`（GLM-OCR(0.9B)の漫画切り抜きOCR用LoRA(MIT)。CER 111.43%→26.02%(自己報告)。VQAは不可、DL累計483。OCR用途は image-to-text 側で評価済み。）

関連リポジトリ:

- [manga109/MangaLMM](https://github.com/manga109/MangaLMM) — MangaLMM 公式の学習・評価・推論コード（★50 / MIT / 最終push 2025-11-09 / 確認コミット [`d06fb95a`](https://github.com/manga109/MangaLMM/blob/d06fb95af6d91311569d07fec393e339c8ab91d1/README.md)）
  - 50★、MIT、2025-11更新。EACL Findings 2026の公式実装
- [koharu-rs/koharu](https://github.com/koharu-rs/koharu) — VLM/LLMを翻訳工程に使う統合アプリ(OCRは別モデル)（★5,693 / Apache-2.0 / 最終push 2026-09-30 / release 0.83.5 (2026-09-22) / 確認コミット [`45b4cae1`](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md)）
  - Gemma 4/Qwen 3.5-3.8等のGGUFを翻訳に選択可。漫画VLMは未同梱

### 視覚的質問応答(漫画ページの内容理解:MangaVQA)

<a id="visual-question-answering--manga-vqa"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [hal-utokyo/MangaLMM](https://huggingface.co/hal-utokyo/MangaLMM/tree/a556fbc7edc256fbd6d3b4d8d3418dd5d68f7c27)（revision `a556fbc7` / 作成 2025-05-16 / 更新 2025-06-01）
- **利用条件**: mit。HFメタデータは mit。ただし学習データ MangaOCR/MangaVQA は Manga109(109巻)とCOOを統合して作られ、Manga109 本体は『学術目的・非営利機関のみ』、Manga109-s(87巻)のみ商用利用可(manga109 公式 License 節)。MangaLMM がどちらの範囲で学習したかはカード本文に記載なし(論文は109巻を使用と記載)。ベースの Qwen2.5-VL-7B-Instruct のライセンスは本調査で未確認。商用可とは断定しない。 VQA訓練データはGPT-4o(gpt-4o-2024-11-20)出力を含むため、OpenAIの利用条件の影響を受ける可能性がある(推測、要確認)。
- **選定根拠**: 【事実】HFの visual-question-answering タグ配下を anime/manga/comic/illustration/japanese/mangavqa で検索しても該当モデルは0件(ocr/caption語のヒットは pix2struct 等の汎用のみ)。漫画VQAの実体は image-text-to-text タグの hal-utokyo/MangaLMM で、MangaVQA(526問、Gemini 2.5 FlashがLLM審判)のスコアは MangaLMM 6.68、Gemini 2.5 Flash 7.26、GPT-4o 6.00、Claude Sonnet 4.5 5.84、Qwen2.5-VL-7B 5.65、Sarashina2-Vision-8B 4.45、Gemma-3-12B 4.13(論文Table 2、著者自身のベンチ)。合成VQA(GPT-4oがOCR注釈を見て生成した39,837問)で1エポック学習。審判をGPT-4oに替えても MangaLMM 6.57・Gemini 2.5 Flash 7.14 で順位は同じ、Gemini審判と人手評価の相関 r=0.91(論文付録E.2)。VQA専用学習のみ(TVQA)は6.57±0.06、OCR併用で6.68±0.03で、OCR学習がVQAを妨げない。【評価】漫画VQAで公開重み+論文ベンチを持つのは MangaLMM のみ。プロプライエタリ(Gemini 2.5 Flash)には届かず、新世代オープンVLMとの比較は未検証。VQAタグの付与がないためHFのタスク一覧では見つからない点に注意。
- **指標（確認日時点）**: DL累計 9,331 / 直近30日 364 / likes 13 / Spaces 2
- **概要**: manga-understanding-vlm と同一モデル。漫画ページに対する事実質問(誰が・何を・いつ…)と文脈説明に答える。
- **入力**: 漫画ページ画像+質問文。
- **出力**: 自然文の回答。
- **必要環境**: manga-understanding-vlm と同じ(未測定)。公式READMEのVQA評価は審判にGPT-4o(OpenAI API)を使い約40分/A100 1枚(論文本文の審判はGemini 2.5 Flash)。
- **制約**: VQAスコアはGemini 2.5 Flashに劣る。文字の取り違えで誤答する例が論文にある。訓練VQAはGPT-4o生成の合成データで、未知著者の質問でも劣化は小さいと論文は述べるが、Manga109外の漫画は未評価。
- **使う版・派生**: manga-understanding-vlm と同じ(GGUF: mradermacher/MangaLMM-GGUF、デモSpace)。
- **根拠**: [モデル概要(カードは短い)](https://huggingface.co/hal-utokyo/MangaLMM/blob/a556fbc7edc256fbd6d3b4d8d3418dd5d68f7c27/README.md) / [MangaVQA 526問、LLM審判、Table 2、付録Table F(GPT-4o審判 MangaLMM 6.57 / Gemini 7.14)、人手との相関 r=0.91](https://arxiv.org/abs/2505.20298) / [MangaVQA のカテゴリ軸(コマ/ページ、抽出/記述、5W1H、著者既知度)と結果表](https://manga109.github.io/MangaVQA_LMM/)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `Qwen/Qwen2.5-VL-7B-Instruct` — ベースモデル。MangaVQA 5.65(MangaLMM 6.68)。最高はプロプライエタリ Gemini 2.5 Flash の 7.26。
- **次点**: `ragavsachdeva/magiv3`（自由質問VQAではなく、コマ・文字・キャラの検出/接地とキャプションのモデル(PopCaptionsでキャラ接地F1 0.69)。非商用。）

関連リポジトリ:

- [manga109/MangaLMM](https://github.com/manga109/MangaLMM) — MangaVQA評価スクリプト(GPT-4o審判版)と学習コード（★50 / MIT / 最終push 2025-11-09 / 確認コミット [`d06fb95a`](https://github.com/manga109/MangaLMM/blob/d06fb95af6d91311569d07fec393e339c8ab91d1/README.md)）
  - 50★、MIT。公式

### 漫画レイアウト検出(文字・擬音・吹き出し・コマの検出+インスタンスマスク)

<a id="manga-layout-detection--text-bubble-panel-detection"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [mayocream/koharu-layout-rfdetr-seg-2xl-1152](https://huggingface.co/mayocream/koharu-layout-rfdetr-seg-2xl-1152/tree/aed55fdb8ca953c6bec33cf6ed6dd52a9b72bfa2)（revision `aed55fdb` / 作成 2026-07-23 / 更新 2026-07-25）
- **利用条件**: other。HFメタデータは other(カード: RF-DETR部分は Apache-2.0 だが、Manga109 画像でファインチューンしているため custom/other とした)。学習データ mayocream/manga109-segmentation v2.0.0 は Manga109 の109巻すべてを対象とし、Manga109 本体は『学術目的・非営利機関のみ』(Manga109-s の87巻のみ商用可)。Lumina の README もこのモデルを『学術・非商用研究限定』として任意モデル扱い。商用パイプラインでは使えない可能性が高い(要法務確認)。Manga109画像は同梱されない。
- **選定根拠**: 【事実】Koharu Layout RF-DETR Seg 2XL(1152px)は text/onomatopoeia/bubble/panel の4クラスをbox+インスタンスマスクで出す。Manga109 Segmentation v2.0.0 の検証1,001ページ(本の単位で分割、自己報告)で box mAP50-95 0.7969、mAP50 0.8970、F1 0.8392、mask mAP50-95 0.5713。クラス別AP: text 0.8779、bubble 0.9092、panel 0.9574、onomatopoeia 0.4431。Koharu(5,693★、2026-09-22リリース0.83.5)のUIが検出モデルとして採用する唯一のモデル(ただしコードには ogkalu 系・YOLO系の旧検出器も残存)、Lumina は任意枠。HF likes7、DLカウンタ0(safetensorsのみでカウント対象外の可能性)、GitHubコード参照46件。対抗: ogkalu/comic-text-and-bubble-detector(RT-DETRv2、Apache-2.0、約1.1万枚の漫画/Webtoon/コミックで学習、累計605,566DL・30日62,325・likes55、comic-translate・MangaTranslator・Lumina既定が採用)は定量ベンチも panel クラスも無い。tori29umai/rtdetrv4-x-manga109s_v2 は商用許諾済の Manga109-s(87作品)のみで学習し、Manga109-s val 1,212ページで mAP 75.0%・AP50 96.0%(frame/body/text/face、自己報告)だがDL0・likes7。【評価】精度・クラスの網羅はKoharu Layoutが上だが、Manga109全109巻で学習したため商用利用は不可と見るのが安全。商用・公開サービス用途では ogkalu(Apache-2.0)か Manga109-s のみの tori29umai を検討。学習/検証が同一分布(Manga109)で、カラー・Webtoonでの定量結果は無い(カードは目視レビューのみ)。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 7 / Spaces 0
- **概要**: RF-DETR Seg 2XL(rfdetr==1.7.0)を1152pxで漫画ページ用に学習したレイアウト解析器。クラス: 0=text(台詞・キャプション・クレジット等)、1=onomatopoeia、2=bubble、3=panel。教師は Manga109 Segmentation v2.0.0(Zenodoの手描きTextSegマスク、PP-DocLayoutV3提案、koharu-text-sam-ts-lで精緻化)。
- **入力**: 漫画ページ画像(1152x1152で学習・評価)。推奨しきい値: text 0.25 / COO 0.20 / bubble 0.50 / panel 0.50。
- **出力**: クラス別のbbox・インスタンスマスク・信頼度(OCR・読み順・台詞と吹き出しの対応は出さない)。
- **必要環境**: カード記載: CUDA強く推奨、pip install rfdetr==1.7.0 safetensors。学習は H100 80GB×8。推論VRAM・速度は未測定。
- **制約**: COO(擬音)はAP 0.4431と弱い。大きな題字・クレジット・ロゴ・コラージュは苦手、キャラ名札や小アイコンを吹き出しと誤検出し得る。読み順なし。学習は日本の漫画中心。カラー同人誌でのSFXは低しきい値で拾うが精度は目視のみ。
- **使う版・派生**: mayocream/koharu-yolo26s(YOLO26s-seg、other、ShadowB/Manga109-panel-balloon-text-yolov26 ベース)、mayocream/comic-layout-yolo26s(MIT)、ShiniShiho/koharu-layout-rfdetr-seg-2xl-1152-onnx(第三者ONNX)、DevilishDaoSaint/koharu-layout-rfdetr(再配布)。マスク精緻化用 mayocream/koharu-text-sam-ts-l(Hi-SAM派生、Apache-2.0、テキスト画素マスク、DL81)。
- **根拠**: [4クラス、検証指標(1,001ページ)、しきい値、ライセンス・学習データ条件、制約](https://huggingface.co/mayocream/koharu-layout-rfdetr-seg-2xl-1152/blob/aed55fdb8ca953c6bec33cf6ed6dd52a9b72bfa2/README.md) / [学習データ v2.0.0: 109冊・10,098ページ・454,606アノテーション(train 87冊/val 11冊/test 11冊、Manga109画像は非同梱)](https://huggingface.co/datasets/mayocream/manga109-segmentation/blob/main/README.md) / [Lumina README: rfdetr_seg(Koharu Layout)は Manga109 学習のため学術・非商用限定、既定検出器は Apache-2.0 の rtdetr](https://github.com/lumina-tl/lumina/blob/bfbf042aff4c18290198f65c18f31430cd3f5a06/README.md) / [対抗: RT-DETR-v2、約1.1万枚、3クラス(bubble/text_bubble/text_free)、ベンチ記載なし](https://huggingface.co/ogkalu/comic-text-and-bubble-detector/blob/16e8a622f91fabc6b5b65c96d32d1183f8843546/README.md) / [対抗: Manga109-s(87作品)のみ学習、val 1,212ページ mAP 75.0%/AP50 96.0%(自己報告)](https://huggingface.co/tori29umai/rtdetrv4-x-manga109s_v2/blob/864c3bfb837a03ecc62557d5152a5ade5566489b/README.md)
- **次点**: `ogkalu/comic-text-and-bubble-detector`（ライセンスの安全側(Apache-2.0)で採用最大(累計605,566DL、30日62,325、likes55、4 spaces)。ただし panel クラス・マスク・定量ベンチなし、640px、3クラス。商用はこちらが第一候補。） / `tori29umai/rtdetrv4-x-manga109s_v2`（商用許諾済Manga109-sのみで学習(Apache-2.0表記)し、frame/body/text/face を出す。val mAP 75.0%(自己報告)だが、DL0・likes7、2026-05作成、ONNX(1280px固定)のみ、吹き出し/SFXの個別クラスなし。） / `huyvux3005/manga109-segmentation-bubble`（YOLO11n-seg、吹き出し専用(mAP50 99.1%自己報告)。Apache-2.0表記だがカードの学習データに Manga109(対象巻は不明)を含む。manga-translator-ui・MangaTranslator が利用、Koharuには派生の mayocream/manga109-segmentation-bubble が残存。30日DL4,931・likes24。）

関連リポジトリ:

- [koharu-rs/koharu](https://github.com/koharu-rs/koharu) — Koharu Layout を検出段に使う統合アプリ（★5,693 / Apache-2.0 / 最終push 2026-09-30 / release 0.83.5 (2026-09-22) / 確認コミット [`45b4cae1`](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md)）
  - 5,693★、Apache-2.0(アプリ)、0.83.5(2026-09-22)。検出→OCR→消去まで一体
- [roboflow/rf-detr](https://github.com/roboflow/rf-detr) — RF-DETR(検出/インスタンスセグメンテーション)の学習・推論基盤（★9,664 / Apache-2.0 / 最終push 2026-09-30 / release 1.11.1 (2026-09-30) / 確認コミット [`7b9d60c6`](https://github.com/roboflow/rf-detr/blob/7b9d60c61b3188dc871cd54d80257f6b2f483bdd/README.md)）
  - 9,662★、Apache-2.0、1.11.1(2026-09-30)。Koharu Layoutの基盤ライブラリ(rfdetr==1.7.0で学習)
- [ogkalu2/comic-translate](https://github.com/ogkalu2/comic-translate) — ogkalu検出器+manga-ocr+LaMa の翻訳アプリ（★2,960 / Apache-2.0 / 最終push 2026-09-11 / release v2.8.9 (2026-09-11) / 確認コミット [`8977b91a`](https://github.com/ogkalu2/comic-translate/blob/8977b91a4f7a40c3917c5a268e9e7d78e1d818da/README.md)）
  - 2,959★、Apache-2.0、v2.8.9(2026-09-11)。商用安全側のRT-DETR系検出器を実運用
- [dmMaze/BallonsTranslator](https://github.com/dmMaze/BallonsTranslator) — comic-text-detector / YSG等の検出器を選べる翻訳・編集アプリ（★5,171 / GPL-3.0 / 最終push 2026-09-27 / release v1.5.17 (2026-09-27) / 確認コミット [`9c7863c1`](https://github.com/dmMaze/BallonsTranslator/blob/9c7863c1e10c5bd927312eca0a0860177b0e5539/README.md)）
  - 5,171★、GPL-3.0、v1.5.17(2026-09-27)。検出・OCR・インペイントを差し替え可能

### アニメ・イラスト・カラー漫画内テキストブロック検出(枠外文字・題字含む)

<a id="manga-layout-detection--anime-scene-text-detection"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [deepghs/AnimeText_yolo](https://huggingface.co/deepghs/AnimeText_yolo/tree/a180c191bfdb9f0e31b57e7de567e7b6bac50f84)（revision `a180c191` / 作成 2025-05-23 / 更新 2025-10-10）
- **利用条件**: gpl-3.0 / gated。HFメタデータは gpl-3.0 かつ gated=auto(利用条件への同意が必要)。データセット AnimeText のライセンス・元画像の権利はカード抜粋に明記なし(本調査では未確認)。GPL-3.0のためクローズドな組込みは不可。商用可とは断定しない。
- **選定根拠**: 【事実】AnimeText(735,060枚・423万テキストブロック、hard negative付き、論文 arXiv 2510.07951)で学習した YOLO12 系。カード表: yolo12x F1 0.90・mAP50 0.95167・mAP50-95 0.89656(l 0.88587、m 0.87804、s 0.86523、n 0.83449。単一クラス text_block、評価分割は表に明記なし=自己報告)。採用: MangaTranslator が枠外(OSB)文字検出に利用(GH 331★)、sorryhyun が同人誌SFX評価のボックス検出に使用している。likes27、spaces4、GitHubコード参照59件、DLカウンタ0(ゲート付きのため)。漫画ページの4クラス解析(Koharu Layout)は枠内の吹き出し/コマが得意だが、アニメ場面・イラスト・カラー同人誌の装飾文字や枠外題字は AnimeText 系が対象。重なる用途では両者を併用する事例がある(MangaTranslator)。【評価】該当ドメインで同規模の代替がない。ただし最終更新2025-10、GPL-3.0+ゲート(auto承認)で組込みに制約がある。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 28 / Spaces 4
- **概要**: AnimeText データセット(735K枚/4.2Mブロック)で学習した YOLO12 検出器の n/s/m/l/x 5サイズ。クラスは text_block のみ(hard negativeで記号・装飾を区別)。オンラインデモ Space あり(deepghs/AnimeText_yolo)。
- **入力**: アニメ/イラスト/漫画画像(YOLO入力)。F1最大のしきい値はxで0.425、lで0.426、mで0.299、sで0.272、nで0.251(カード表)。
- **出力**: text_blockのbbox。
- **必要環境**: ultralytics(YOLO12)推論。リポジトリはゲート付き(自動承認)でHFトークンが必要。VRAM・速度は未測定(カードにFLOPS/Paramsのみ: x 200G/59.1M、l 89.4G/26.4M)。
- **制約**: 検出のみ(OCR・読み順なし)。単一クラスで吹き出し/SFXの区別なし。F1最大しきい値はサイズ毎に異なる。最終更新2025-10。
- **使う版・派生**: サイズ別 yolo12{n,s,m,l,x}_animetext。mayocream/anime-text-yolo(GPL-3.0、30日DL24)は詳細未確認。
- **根拠**: [YOLO12 n〜x の F1/mAP 表、データセット・論文へのリンク](https://huggingface.co/deepghs/AnimeText_yolo/blob/a180c191bfdb9f0e31b57e7de567e7b6bac50f84/README.md) / [AnimeText: 735K枚・4.2Mブロック、hard negative、既存データセットで学習した検出器より anime 場面で高精度との主張](https://arxiv.org/abs/2510.07951) / [MangaTranslator が枠外テキスト検出に deepghs/AnimeText_yolo を使用(HFトークンとゲート承認が必要と記載)](https://github.com/meangrinch/MangaTranslator/blob/924854a218dda3bc4a22c1a4e65dfe8dc9fa8ac0/README.md) / [sorryhyun のSFX評価で AnimeText_yolo をボックス検出に使用(第三者利用例)](https://huggingface.co/sorryhyun/paddleocr-vl-1.6-manga-lora/discussions/1)
- **次点**: `Kellenok/PP-OCRv6_manga`（漫画/webtoon/イラスト向けの検出(0.9MB)+認識(10MB)の軽量CPUパイプライン。842ページで end-to-end CER 11.34%(v0.2、自己報告)だが30日DL0・likes1、検出単体のAP評価なし。CPU/エッジ用途の有力候補。） / `rtr46/meiki.text.detect.v0`（日本語ゲーム/VN+漫画で学習の低遅延検出器(tiny/small)。30日DL49,706。v0.1はゲーム寄りで64ボックス上限のため漫画には不向きとカード明記。LGPL-3.0。）

関連リポジトリ:

- [meangrinch/MangaTranslator](https://github.com/meangrinch/MangaTranslator) — AnimeText_yolo を枠外文字検出に使う翻訳アプリ(YOLO/SAM検出+FLUX.2 Klein消去)（★331 / Apache-2.0 / 最終push 2026-09-30 / release v1.24.9 (2026-09-30) / 確認コミット [`924854a2`](https://github.com/meangrinch/MangaTranslator/blob/924854a218dda3bc4a22c1a4e65dfe8dc9fa8ac0/README.md)）
  - 331★、Apache-2.0、v1.24.9(2026-09-30)。枠外/枠内を分けて扱う実装例
- [koharu-rs/koharu](https://github.com/koharu-rs/koharu) — 漫画ページ4クラス検出(こちらは枠内中心)との併用設計の参照（★5,693 / Apache-2.0 / 最終push 2026-09-30 / release 0.83.5 (2026-09-22) / 確認コミット [`45b4cae1`](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md)）
  - 5,693★。OCR・消去まで一体

### 漫画の読み順・コマ/文字/キャラ/吹き出し尾の関連付け(台詞の話者推定)

<a id="manga-reading-order"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [ragavsachdeva/magiv3](https://huggingface.co/ragavsachdeva/magiv3/tree/49c73a225122d53adbaa26d53868be81a57706e2)（revision `49c73a22` / 作成 2025-02-27 / 更新 2026-07-21）
- **利用条件**: 未記載。カード本文: 個人・研究・非営利・非営利団体での利用は無制限、それ以外は作者に個別連絡してライセンス契約。HFメタデータにlicense欄なし(取得値null)。商用利用不可と扱う。学習/評価データの PopManga・Manga109 の条件も別途必要。
- **選定根拠**: 【事実】Koharu・ogkalu・Lumina などの実用検出器は読み順を出さない(Koharu Layoutのカードは『OCR・読み順・テキストと吹き出しの関連付けは出力しない』と明記)。読み順に対応する公開モデルは Oxford VGG の Magi 系のみ確認。Magiv3(ICCV 2025、arXiv 2503.23344)は Florence-2 に着想を得た自己回帰VLMで、コマ・キャラ・文字・吹き出し尾を検出し、ボックスを『漫画の読み順(上→下、右→左)』で出力し(論文本文)、OCR・キャラ接地まで1モデルで行う。論文Table 2(関連付け、PopManga/Manga109): Char-Char AMI は Magiv3 0.6884/0.6928/0.6782(PM-S/PM-U/M109)> Magiv2 0.6745/0.6650/0.6456 > Magi 0.6574/0.6527/0.6345、Text-Tail AP は 0.9911/0.9859(v2は0.9838/0.9830)、Text-Char AP は Magiv2 が上(0.7499/0.7512 vs 0.7241/0.7331)。キャラ接地F1 は Magiv3 0.69、Magiv3-cg 0.74、Florence-2 0.28(PopCaptions)。HF: magiv3 DL累計34,562・30日2,235・likes20、magiv2 は累計119,962・30日27,286・likes27(v2のほうが普及)、magi(v1) 累計386,350。【評価】読み順専用の定量評価(順序相関等)は論文・カードで確認できず、ページ順処理の成否は未検証のため低信頼。商用は『個別相談』でNC扱い。トランスクリプト用途なら v2(安定・普及)との併用を検討。GenerationMixin継承の修正を求めるHF議論/PR(#2、7コメント)が open のまま。
- **指標（確認日時点）**: DL累計 34,562 / 直近30日 2,235 / likes 20 / Spaces 1
- **概要**: コミック理解の統合VLM。画像+タスクプロンプトから、コマ・キャラクター・文字・吹き出し尾の検出と関連付け(predict_detections_and_associations)、OCR(predict_ocr)、キャプション中のキャラのコマ内接地(predict_character_grounding)をテキスト出力する。
- **入力**: コミック/漫画ページ画像(グレースケールRGB)。
- **出力**: 読み順に並んだ検出ボックス+関連付け(文字→話者、文字→尾)、OCR文字列、接地座標。
- **必要環境**: カード記載: trust_remote_code=True、torch.float16 で .cuda()。VRAM等は未測定。
- **制約**: ライセンスが非商用。GenerationMixin継承の修正提案(discussion #2)がopen。評価は PopManga と Manga109 で、同人誌・カラー・縦読みでの結果は未確認。読み順の専用精度指標は未確認。
- **使う版・派生**: ragavsachdeva/magiv2(ページ+章単位のキャラ名付き書き起こし、別アーキテクチャ)、magi(v1)、magiv2-crop-embedder。
- **根拠**: [機能一覧、利用法、ライセンス文言(非商用)](https://huggingface.co/ragavsachdeva/magiv3/blob/49c73a225122d53adbaa26d53868be81a57706e2/README.md) / [Magiv3: 読み順出力、Table 1/2(検出・関連付け)、キャラ接地](https://arxiv.org/abs/2503.23344) / [Magiv2 (Tails Tell Tales): チャプター単位の書き起こし、順序付けアルゴリズム、キャラ名付与](https://arxiv.org/abs/2408.00298) / [v1/v2/v3 の使い方とデモ](https://github.com/ragavsachdeva/magi/blob/2a45bf09b43adc80778270a366372aaa148e2291/README.md)
- **次点**: `ragavsachdeva/magiv2`（30日DL27,286・累計119,962と普及しており、Text-Char AP は v3 より高い。チャプター横断のキャラ名付き書き起こしが強みだが、順序付けは後処理アルゴリズム。ライセンスは同様に非商用。）

関連リポジトリ:

- [ragavsachdeva/magi](https://github.com/ragavsachdeva/magi) — Magi v1/v2/v3 公式(論文実装・デモ)（★470 / ライセンス未表示 / 最終push 2025-06-27 / 確認コミット [`2a45bf09`](https://github.com/ragavsachdeva/magi/blob/2a45bf09b43adc80778270a366372aaa148e2291/README.md)）
  - 470★、ライセンス表記なし(GitHub API上null)、2025-06-27更新。コミックの読み順・話者関連付けの唯一の公開実装

### 漫画の文字消去・インペイント(吹き出し/背景のテキスト除去)

<a id="manga-text-inpainting"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [dreMaz/AnimeMangaInpainting](https://huggingface.co/dreMaz/AnimeMangaInpainting/tree/2953a4e935bf01ad1471f6cbfd26ab81abeeb92d)（revision `2953a4e9` / 作成 2023-11-10 / 更新 2023-11-10）
- **利用条件**: mit。HFメタデータは mit。元アーキテクチャ advimman/lama は Apache-2.0(GitHub)。ファインチューンに使った約30万枚の漫画/アニメ画像の出所・権利はカードに記載なく未確認。商用可とは断定しない。
- **選定根拠**: 【事実】dreMaz/AnimeMangaInpainting は Big-LaMa を漫画・アニメ風画像約30万枚でファインチューンした lama_large_512px.ckpt(カード:『older lama_mpe より漫画で大幅に良い』。定量指標なし)。BallonsTranslator のソース(ballontranslator/modules/inpaint/inpaint_default.py)がこのリポジトリを参照(HFユーザー dreMaz と GitHub の dmMaze が同一人物かは未確認)。HF: likes30、spaces8、MIT。DLカウンタは0(.ckptのためカウント対象外)で採用は他指標から推定。採用: BallonsTranslator が『lama*は微調整版』として収録、comic-translate がこのチェックポイントをインペイントに採用(README)、Koharu の既定LaMaはその safetensors 変換(mayocream/lama-manga、カードに『出典: Sanster/models anime-manga-big-lama.pt』、likes11、累計DL503)、Lumina の既定も lama_manga。Koharuのもう一つの直接法 AOT(mayocream/aot-inpainting)は累計DL22,502・spaces10。生成系: Koharu は FLUX.2 Klein 4B(unsloth GGUF: 30日DL304,280・likes227・Apache-2.0、汎用)と RORem Mixed(mayocream GGUF、OpenRAIL++、累計DL36,759)を選択肢にしており、MangaTranslator は FLUX.2 Klein/FLUX.1 Kontext/OpenCVを使う。いずれもアニメ特化ではなく、漫画での定量比較は見つからない。Koharuのガイドは『精密な除去マスクの方が大きなモデルより重要』と記載。【評価】マスク品質に依存する直接法(LaMa)の漫画特化版を標準とし、難所のみ生成系へ切替えるのが現実的。ただし比較ベンチがなく(どのカードにも評価値なし)、IOPaint(旧lama-cleaner、Sanster、重みの元配布元)は2025-04にアーカイブ済み。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 30 / Spaces 8
- **概要**: advimman/lama の Big-LaMa(FFC ResNetジェネレータ)を漫画・アニメ風データ約30万枚でファインチューンした512px用チェックポイント。マスク領域を埋めて文字・ロゴ・局所物体を除去する。
- **入力**: RGB画像+2値マスク(白=再生成領域)。lama-cleaner/IOPaint・BallonsTranslator・comic-translate が読み込める形式(.ckpt)。
- **出力**: マスク領域を埋めたRGB画像。
- **必要環境**: カード本文に記載なし(ファイルは lama_large_512px.ckpt のみ)。VRAM・速度は未測定。Lumina README: lama_manga は CUDA または CPU(DirectML不可)。
- **制約**: カードは評価値・学習データ詳細・ライセンス詳細を記載しない(1〜2行)。模様や線画を『創作』し得る。マスクが粗いと文字残りや吹き出し枠の消失が出る(Koharuガイド)。2023-11から更新なし。discussion #1 に『色や文脈が合わない』課題提起があり未解決。
- **使う版・派生**: mayocream/lama-manga(safetensors変換、MIT、Koharu既定)、Sanster/models GitHub release の anime-manga-big-lama.pt(TorchScript版)。直接法の別案: mayocream/aot-inpainting(AOT GAN)。生成系: unsloth/FLUX.2-klein-4B-GGUF、mayocream/RORem-mixed-GGUF。
- **根拠**: [30万枚で微調整した big lama、lama_mpe より漫画で良いとの自己申告(定量値なし)](https://huggingface.co/dreMaz/AnimeMangaInpainting/blob/2953a4e935bf01ad1471f6cbfd26ab81abeeb92d/README.md) / [Koharu既定のsafetensors変換。出典 anime-manga-big-lama.pt、『評価指標・学習データ成果物は含まない』と明記](https://huggingface.co/mayocream/lama-manga/blob/f91c85b26913b3e83f9877867b4c336da3675238/README.md) / [comic-translate README: インペイントに dreMaz/AnimeMangaInpainting のlamaを採用](https://github.com/ogkalu2/comic-translate/blob/8977b91a4f7a40c3917c5a268e9e7d78e1d818da/README.md) / [Koharuガイド: LaMa/AOTは直接法、FLUX.2 Klein/RORemは生成系で要リソース。マスクの精度が重要](https://koharu.rs/en/guides/cleanup.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `unsloth/FLUX.2-klein-4B-GGUF` — 生成系の汎用インペイント(Apache-2.0、30日DL304,280、likes227)。Koharu/MangaTranslator が背景再構成用に採用。漫画での定量比較は未確認。
- **次点**: `mayocream/lama-manga`（同じ重みのsafetensors変換(MIT、Koharu既定)で派生扱い。累計DL503・likes11。推論実装がKoharu/Luminaに組込済みでRust/ONNX系から使うならこちら。） / `mayocream/aot-inpainting`（AOT GAN(manga-image-translator由来)。累計DL22,502・spaces10で軽量。LaMaより漫画適性の根拠となる評価値なし。） / `mayocream/RORem-mixed-GGUF`（物体除去モデルRORem(SDXLインペイント)のQ4_K GGUF。Koharuが『漫画向け』として選択肢化。ライセンス openrail++、累計DL36,759。SDXL VAE/CLIPが別途必要で、1枚約6.4秒(RTX5090)と重い。）

関連リポジトリ:

- [koharu-rs/koharu](https://github.com/koharu-rs/koharu) — LaMa/AOT/FLUX.2 Klein/RORem を選べる消去工程を持つ統合アプリ（★5,693 / Apache-2.0 / 最終push 2026-09-30 / release 0.83.5 (2026-09-22) / 確認コミット [`45b4cae1`](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md)）
  - 5,693★、0.83.5。直接法と生成法を同一UIで比較できる
- [dmMaze/BallonsTranslator](https://github.com/dmMaze/BallonsTranslator) — lama系微調整/AOT/patchmatch を選べる翻訳・編集アプリ（★5,171 / GPL-3.0 / 最終push 2026-09-27 / release v1.5.17 (2026-09-27) / 確認コミット [`9c7863c1`](https://github.com/dmMaze/BallonsTranslator/blob/9c7863c1e10c5bd927312eca0a0860177b0e5539/README.md)）
  - 5,171★、GPL-3.0、v1.5.17。ソースが dreMaz/AnimeMangaInpainting を参照
- [advimman/lama](https://github.com/advimman/lama) — LaMa本家(学習・推論)（★10,284 / Apache-2.0 / 最終push 2025-02-05 / 確認コミット [`786f5936`](https://github.com/advimman/lama/blob/786f5936b27fb3dacd2b1ad799e4de968ea697e7/README.md)）
  - 10,284★、Apache-2.0、2025-02更新。微調整元のアーキテクチャ
- [zyddnys/manga-image-translator](https://github.com/zyddnys/manga-image-translator) — AOT/lama_large 等のインペイント実装を含む老舗翻訳基盤（★10,457 / GPL-3.0 / 最終push 2026-09-25 / release beta-0.3 (2022-04-23) / 確認コミット [`441d07c5`](https://github.com/zyddnys/manga-image-translator/blob/441d07c59a735c7db3db2e7bb8b07920afd8a9cc/README.md) / 制作カタログ: [manga-image-translator](../../categories/localization.md#manga-image-translator)）
  - 10,457★、GPL-3.0。READMEの「no longer working」はホストデモ。最終リリースbeta-0.3(2022-04)、mainは2026-09-25更新

### 漫画翻訳パイプライン(検出→OCR→消去→翻訳→植字)のアプリ/OSS選定

<a id="manga-translation-pipeline"></a>
- **判定**: モデルなし / 確度 中
- **選定根拠**: 【事実】単一モデルではなくアプリ層の選定。検証した主要OSS(2026-10-01時点): koharu-rs/koharu 5,693★・Apache-2.0・0.83.5(2026-09-22)・Rust製、検出/OCR/消去/翻訳LLMを選択式、PSD出力、エージェント機能; dmMaze/BallonsTranslator 5,171★・GPL-3.0・v1.5.17(2026-09-27); ogkalu2/comic-translate 2,959★・Apache-2.0・v2.8.9(2026-09-11); hgmzhn/manga-translator-ui 2,895★・GPL-3.0・v3.0.4(2026-09-06、manga-image-translator派生); zyddnys/manga-image-translator 10,457★・GPL-3.0(READMEのホスト版は停止、最終リリースbeta-0.3=2022-04、mainは2026-09-25更新); meangrinch/MangaTranslator 331★・Apache-2.0・v1.24.9(2026-09-30); lumina-tl/lumina 19★・MIT・v0.4.0; joyeli/yakuyomi-engine 7★・GPL-3.0(スマホ上NCNN); kha-white/mokuro 1,738★・GPL-3.0(翻訳ではなくオーバーレイ読書)。モデル差し替えの自由度は Koharu(OCR4種・消去4種・検出1種)と BallonsTranslator が高い。Koharuは検出モデルが Manga109 全巻学習で学術・非商用、GPLの翻訳UIは組込み用途で制約になる。X上の言及は Koharu の紹介投稿が中心(tom_doerr 122いいね、Sn0wbrave 234いいね、2026-08)。【評価】本エントリは単一のbestモデルを置かない(none)。開発基盤としては、商用/Apache-2.0重視なら Koharu か comic-translate、カスタマイズ重視なら BallonsTranslator。

関連リポジトリ:

- [koharu-rs/koharu](https://github.com/koharu-rs/koharu) — 最も活発なRust製ローカル漫画翻訳アプリ（★5,693 / Apache-2.0 / 最終push 2026-09-30 / release 0.83.5 (2026-09-22) / 確認コミット [`45b4cae1`](https://github.com/koharu-rs/koharu/blob/45b4cae150dcf280c0ccdf87d750af76f0811c7d/README.md)）
  - 5,693★、Apache-2.0、0.83.5(2026-09-22)。検出/OCR/消去/LLMを設定で差し替え
- [dmMaze/BallonsTranslator](https://github.com/dmMaze/BallonsTranslator) — 編集機能が充実した翻訳ツール(plugin式で検出/OCR/消去を差し替え)（★5,171 / GPL-3.0 / 最終push 2026-09-27 / release v1.5.17 (2026-09-27) / 確認コミット [`9c7863c1`](https://github.com/dmMaze/BallonsTranslator/blob/9c7863c1e10c5bd927312eca0a0860177b0e5539/README.md)）
  - 5,171★、GPL-3.0、v1.5.17(2026-09-27)
- [ogkalu2/comic-translate](https://github.com/ogkalu2/comic-translate) — 漫画/Webtoon/PDF/EPUB対応の翻訳アプリ+ブラウザ拡張（★2,960 / Apache-2.0 / 最終push 2026-09-11 / release v2.8.9 (2026-09-11) / 確認コミット [`8977b91a`](https://github.com/ogkalu2/comic-translate/blob/8977b91a4f7a40c3917c5a268e9e7d78e1d818da/README.md)）
  - 2,959★、Apache-2.0、v2.8.9(2026-09-11)
- [zyddnys/manga-image-translator](https://github.com/zyddnys/manga-image-translator) — 多くの派生(manga-translator-ui 等)の基盤（★10,457 / GPL-3.0 / 最終push 2026-09-25 / release beta-0.3 (2022-04-23) / 確認コミット [`441d07c5`](https://github.com/zyddnys/manga-image-translator/blob/441d07c59a735c7db3db2e7bb8b07920afd8a9cc/README.md) / 制作カタログ: [manga-image-translator](../../categories/localization.md#manga-image-translator)）
  - 10,457★(最大)、GPL-3.0。ただし最終リリース2022-04で、READMEは公式ホスト版の停止を記載
