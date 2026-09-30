# 言語（翻訳・生成・埋め込み）のアニメ系SOTA（2026-10-01）

[一覧へ](../anime-task-sota.md) · [リポジトリ全体像](../anime-repositories.md) · [正本JSON](../../sota-catalog.json)

選定基準・注意は[一覧ページ](../anime-task-sota.md)。各項目の「最良」は確度付きの編集判断で、重み取得・推論実行は未実施。

### 翻訳(日本語→簡体字中国語: ギャルゲー/ラノベ)

<a id="translation--ja-zh-galgame-ln"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [SakuraLLM/Sakura-GalTransl-7B-v3.7](https://huggingface.co/SakuraLLM/Sakura-GalTransl-7B-v3.7/tree/759d76b1745f4428308de6564c5ab710d4358b2e)（revision `759d76b1` / 作成 2024-05-22 / 更新 2025-08-15）
- **利用条件**: cc-by-nc-sa-4.0。メタデータcc-by-nc-sa-4.0。カード本文で商用行為(有償翻訳API・有償配布パッチ・商用翻訳)を明示的に禁止。商用可ではない。学習データの詳細は未公開。
- **選定根拠**: 事実: SakuraLLM系列はGalgame/ラノベ専用の日中翻訳LLMで、GalTransl-7B v3.7はHF累計DL 1,191,861・30日19,418・likes 113、GitHub code参照101件(Sakura-GalTransl-7B検索)。LunaTranslator(13.5k★)・GalTransl(2.3k★)・LinguaGachaなど主要VN翻訳ツールがSakura APIに対応(SakuraLLM README記載)。14B v3.8は累計89,933DLで採用が一桁少ない。評価: 定量ベンチは公開されておらず(READMEはPPLのみ・旧版)、品質優劣は『14Bは7Bより質が高い』というカード記載(自己報告・数値なし)とHF討論(GalTransl-v4 4Bは『7B v3.7と同等程度』と開発者が発言)に留まる。採用実績・6GB VRAMで動く点から7B v3.7を推す。ライセンスはCC-BY-NC-SA 4.0で商用禁止(有償パッチ等も明示禁止)。 汎用LLM(GPT/Claude/DeepSeek等のAPI)との品質比較は確認できず(GalTranslは両方を選べる)。
- **指標（確認日時点）**: DL累計 1,191,861 / 直近30日 19,418 / likes 113 / Spaces 0
- **概要**: ビジュアルノベル(Galgame)翻訳に特化した7Bの日→簡体中国語翻訳LLM(GGUF配布)。行内改行・制御文字・ルビの保持に配慮し、用語表(GPT辞書)と直前の訳文履歴を渡せる。GalTransl/LunaTranslator用に調整。
- **入力**: 日本語の台本テキスト(推奨7〜10文ずつ)＋任意の用語表(src->dst #備考)＋履歴訳文。ChatML形式のsystem/userプロンプト(カード記載のテンプレート)
- **出力**: 簡体字中国語訳(行数・制御記号を保持)
- **必要環境**: カード記載: 空きVRAM 6GB以上で実用(Q6_K=8GB以上推奨、IQ4_XS/Q4_K=6GB)。llama.cpp系/Sakura_Launcher_GUIで起動。推奨温度0.3・top_p 0.8。未測定(当方では実行していない)。
- **制約**: 日→簡中のみ。用語表は一語多訳('a/b')非対応。省略された主語の推論で事実誤り・幻覚が出ることがある(カード既知問題)。HF討論に履歴訳文が出力に混入するバグ報告(GalTransl-v4側)あり。
- **使う版・派生**: 使用ファイル: Sakura-Galtransl-7B-v3.7.gguf(Q6_K)、-IQ4_XS.gguf。同リポジトリは量子化GGUFのみでsafetensorsなし。上位版: SakuraLLM/Sakura-GalTransl-14B-v3.8(GGUF, 累計89,933DL)、軽量版: SakuraLLM/GalTransl-v4-4B-2601(4B, 累計25,519DL)。再アップロード: Nayuta20251106/Sakura-GalTransl-7B-v3.7等(非公式)。
- **根拠**: [用途・更新履歴(v3.7=2025.08 RL改善)・CC-BY-NC-SA・VRAM・プロンプト・既知問題](https://huggingface.co/SakuraLLM/Sakura-GalTransl-7B-v3.7/blob/759d76b1745f4428308de6564c5ab710d4358b2e/README.md) / [Sakura全モデルのCC BY-NC-SA 4.0・商用禁止、LunaTranslator/GalTransl/AiNiee/LinguaGacha/manga-image-translator等の対応ツール一覧、PPL以外の定量評価が無いこと](https://github.com/SakuraLLM/SakuraLLM/blob/main/README.md) / [開発者xd2333: 4Bは7B v3.7と『差不多(同程度)』](https://huggingface.co/SakuraLLM/GalTransl-v4-4B-2601/discussions/1)
- **次点**: `SakuraLLM/Sakura-GalTransl-14B-v3.8`（カードは『7Bより全体品質が良い』とするが数値なし(自己報告)。累計89,933DLと採用が小さく、必要VRAMも大きい。品質優先でVRAMに余裕があるなら有力） / `SakuraLLM/GalTransl-v4-4B-2601`（2026-01更新の最新世代だが4B。開発者は7B v3.7と同程度と述べ、出力形式の不安定報告あり(累計25,519DL)。リアルタイム翻訳向け） / `SakuraLLM/Sakura-14B-Qwen3-v1.5-GGUF`（カードが『非正式版』と明記。ラノベ/漫画/Galgame汎用の14B。VN特化調整は無い）

関連リポジトリ:

- [SakuraLLM/SakuraLLM](https://github.com/SakuraLLM/SakuraLLM) — Sakuraモデルの配布・推論/プロンプト仕様・対応ツール一覧（★4,794 / GPL-3.0 / 最終push 2026-07-23 / release v1.1.0 (2024-05-10) / 確認コミット [`0ff69116`](https://github.com/SakuraLLM/SakuraLLM/blob/0ff69116222ca66c7a15dcff00fd4f9f86b18d5c/README.md)）
  - 公式ハブ。4.8k★。最終push 2026-07-23。GPL-3.0(モデルはCC-BY-NC-SA)。
- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl) — Galgameの自動翻訳・翻訳パッチ作成パイプライン(Sakura/GPT/Claude/DeepSeek対応)（★2,293 / GPL-3.0 / 最終push 2026-09-30 / release 8.1.0 (2026-09-27) / 確認コミット [`ad04d23e`](https://github.com/GalTransl/GalTransl/blob/ad04d23e187dbc37db2de588e99a13b785127a3e/README.md)）
  - 2.3k★、リリース8.1.0(2026-09-27)と活発。GPL-3.0。Sakura-GalTransl専用のAPI/辞書機構を持つ。
- [HIllya51/LunaTranslator](https://github.com/HIllya51/LunaTranslator) — リアルタイムGalgame翻訳(フック/OCR/クリップボード、Sakura API対応)（★13,488 / GPL-3.0 / 最終push 2026-09-30 / release v10.17.1.12 (2026-09-26) / 確認コミット [`363de635`](https://github.com/HIllya51/LunaTranslator/blob/363de6354ef9d085403f78f325cff5d69b97eda8/docs/zh/README.md)）
  - 13.5k★、v10.17.1.12(2026-09-26)。VN翻訳ツールで最大。GPL-3.0。
- [neavo/LinguaGacha](https://github.com/neavo/LinguaGacha) — 小説・ゲーム・字幕のLLM一括翻訳器(Sakura対応とSakura README記載)（★2,519 / ライセンス未表示 / 最終push 2026-09-30 / release MANUAL_BUILD_v0.124.1 (2026-09-30) / 確認コミット [`1669245b`](https://github.com/neavo/LinguaGacha/blob/1669245ba26ecc78861be191f8b52716c520ca8f/README.md)）
  - 2.5k★、2026-09-30更新。ライセンス表示なし(GitHub API null): 利用条件は要確認。

### 翻訳(日本語→英語: ビジュアルノベル)

<a id="translation--ja-en-visual-novel"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [lmg-anon/vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf/tree/ab7c8285d386fab7cd89e951f62e129085df6372)（revision `ab7c8285` / 作成 2025-01-02 / 更新 2025-01-02）
- **利用条件**: llama3。メタデータlicense=llama3(Llama 3 Community License)。ベースrinna/llama-3-youko-8bのライセンスにも従う。学習データVNTL-v5-1kの権利関係はカードに明記なし。商用可と断定できない。
- **選定根拠**: 事実: VNTLはJP→EN VN翻訳に特化したLlama-3系8B QLoRA。同作者のVNTLリーダーボード(256文・埋め込みcosine類似度、自己運営)でvntl-llama3-8b-v2 Q8_0は精度0.695(±0.035)で、Google翻訳0.540・Sugoi 0.609を上回る一方、Qwen2.5-72B Q5_K_M 0.708・GPT-4o 0.750・Claude 3.5 Sonnet 0.744には及ばず、27B版(vntl-gemma2-27b 0.707)より軽量。HF累計DL 6,044,273は異常に大きくGitHub参照は66件のため過大の可能性。評価: JP→EN VN特化の公開モデルは他に見当たらず、リーダーボードは2025-01以降更新なし。失速した古い事実上の標準として推すが、強い汎用LLM(APIや大型ローカル)が精度で勝つ。ライセンスはLlama 3系。
- **指標（確認日時点）**: DL累計 6,044,273 / 直近30日 32,986 / likes 17 / Spaces 0
- **概要**: VN(ビジュアルノベル)台本のJP→EN翻訳用に rinna/llama-3-youko-8b をQLoRA(rank128)で微調整した8Bモデルの量子化GGUF版。キャラ名・性別・別称等のMetadataをプロンプトに与えられ、複数行翻訳に対応。
- **入力**: LLaMA 3形式プロンプト: Metadata(キャラ/用語)＋Japanese: [話者]:「台詞」…＋English: で続ける。temperature 0推奨
- **出力**: 英語訳(話者タグ付き)
- **必要環境**: カード記載なし(8Bのq5_k_m/q8_0 GGUF)。未測定。
- **制約**: 直訳的になる傾向(カード記載)。ベンチは作者自身の256文・埋め込み類似度で、ノイズが大きい(95%CI±0.035)。リーダーボードは2025-01以降更新なし。モデルは2025-01以降更新なし。
- **使う版・派生**: 使用ファイル: vntl-llama3-8b-v2-hf-q5_k_m.gguf / -q8_0.gguf(本リポジトリ=GGUFのみ)。非量子化: lmg-anon/vntl-llama3-8b-v2-hf、LoRA: -qlora。27B版 lmg-anon/vntl-gemma2-27b-gguf(精度0.707、累計DL少)、2B版 vntl-gemma2-2b-gguf。
- **根拠**: [学習方法・プロンプト形式・推奨サンプリング・『より直訳的』との注記](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf/blob/ab7c8285d386fab7cd89e951f62e129085df6372/README.md) / [VNTLリーダーボード(256文・cosine類似度・chrF、自己運営)と既存翻訳ツール比較表(Sugoi 0.6093, Google 0.5395)](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard/blob/main/README.md) / [vntl-llama3-8b-v2 Q8_0 accuracy 0.6952(CI±0.0345)、vntl-gemma2-27b 0.7067、qwen-2.5-72b Q5_K_M 0.7079、gpt-4o-2024-05-13 0.7516](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard/blob/main/leaderboard.jsonl)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `Qwen/Qwen2.5-72B-Instruct` — VNTLリーダーボードでQwen2.5-72B Q5_K_Mが0.708(8B VNTLは0.695)。API系(GPT-4o 0.752/Claude 3.5 Sonnet 0.744)が上位。2026年の新世代モデルは同ボード未掲載で比較不能
- **次点**: `lmg-anon/vntl-gemma2-27b-gguf`（リーダーボード0.707と僅かに高いが27Bで重く、30日DL 144と採用が少ない(2024-07版)） / `pfnet/plamo-2-translate-base`（日英汎用翻訳モデル(アニメ特化でない)。VN評価は未確認）

関連リポジトリ:

- [HIllya51/LunaTranslator](https://github.com/HIllya51/LunaTranslator) — リアルタイムVN翻訳(任意のOpenAI互換LLMを接続可)（★13,488 / GPL-3.0 / 最終push 2026-09-30 / release v10.17.1.12 (2026-09-26) / 確認コミット [`363de635`](https://github.com/HIllya51/LunaTranslator/blob/363de6354ef9d085403f78f325cff5d69b97eda8/docs/zh/README.md)）
  - 13.5k★で最大のVN翻訳ツール。JP→ENも各種エンジン対応。GPL-3.0。
- [lmg-anon/vntl-benchmark](https://github.com/lmg-anon/vntl-benchmark) — VNTLリーダーボードの評価スクリプト（★3 / AGPL-3.0 / 最終push 2024-10-07 / 確認コミット [`325e148a`](https://github.com/lmg-anon/vntl-benchmark/blob/325e148adfeb92207885e5390e32a3f4fb61f6fd/README.md)）
  - JP→EN VN翻訳の評価手段。ただし3★・最終更新2024-10と小規模。AGPL-3.0。
- [ciddwd/overlay-translator](https://github.com/ciddwd/overlay-translator) — Android画面翻訳(オフラインLLM/OCR、VN・漫画向け)（★920 / Apache-2.0 / 最終push 2026-09-19 / release v0.4.7 (2026-09-13) / 確認コミット [`2e4e692f`](https://github.com/ciddwd/overlay-translator/blob/2e4e692f1736fdb6479d761833c508ea3fa208e5/README.md)）
  - 920★、v0.4.7(2026-09-13)。Apache-2.0。

### テキスト生成(タグ/プロンプト拡張: Danbooruタグ→詳細プロンプト)

<a id="text-generation--danbooru-prompt-expansion"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [KBlueLeaf/TIPO-500M-ft](https://huggingface.co/KBlueLeaf/TIPO-500M-ft/tree/386fc21b10c810c0c1c8f182695e28fbbd45597c)（revision `386fc21b` / 作成 2025-01-10 / 更新 2025-01-22）
- **利用条件**: other/kohaku-license-1.0。メタデータlicense=other / license_name=kohaku-license-1.0。カード本文でKohaku License 1.0と記載(条件は外部文書参照、当方未精読のため商用可と断定しない)。学習データDanbooru2023(権利は各作品・作者に依存)を含む。
- **選定根拠**: 事実: TIPO-500M-ftはDanbooru2023+Coyo-HD-11M等で学習した500Mのプロンプト拡張モデル。HF累計DL 436,120・30日59,247・likes 48・spaces 18、拡張z-tipo-extension 637★(webui/Forge/ComfyUI対応)、ICLR 2026採択(OpenReview/arXiv 2411.08127)。論文のシナリオ評価(TIPO-200Mでの実施・自己報告)でFDD 0.2282(最良)、AI Corrupt 0.9195、Aesthetic 6.26(GPT-4o-mini 6.37に次ぐ)と、GPT-4o-mini・Promptis等を上回る。新版TIPO-v2.1-1B-A200M(2026-08-22、30日10,909DL、累計13,087)は評価/品質/人数タグの不具合修正の再学習版だが、ライセンスメタデータがnull・z-tipo-extension READMEに対応記載なし・評価数値なし。評価: 採用・論文裏付けで500M-ftを推すが、新規導入ならv2.1も要検討。ライセンスはKohaku License 1.0(商用可否は未確認)。
- **指標（確認日時点）**: DL累計 436,120 / 直近30日 59,247 / likes 48 / Spaces 18
- **概要**: 短いタグ/自然言語キャプションを、Danbooruタグ様式＋自然文の詳細プロンプトへ拡張するLLaMA系500Mモデル(TIPO)。T2Iに渡す前段のプリサンプリングで多様性を保ちつつ質を上げる。
- **入力**: 品質・レーティング等のメタ情報＋seedタグまたは短キャプション(KGen/z-tipo-extensionが整形)
- **出力**: 拡張されたDanbooruタグ列および/または長い自然言語キャプション
- **必要環境**: カード記載: 500M LLaMA、最大ctx 1024。z-tipo-extension(webui/Forge/ComfyUI)またはtipo-kgenで利用。VRAM等は未測定。
- **制約**: 英語/タグ前提。表の評価はTIPO-200Mで実施(500M-ft自体の数値ではない)かつ自己報告。Anima等の新世代T2Iとの相性は未確認。Danbooru由来の分布にNSFW語彙を含む(rating指定で制御)。
- **使う版・派生**: 使用: model.safetensors(本リポジトリ)。GGUF: TIPO-500M-ft-F16.gguf(同梱)、mradermacher/TIPO-500M-ft-i1-GGUF(非公式)。同系: TIPO-200M-ft2、TIPO-500M(無ft)、新版 KBlueLeaf/TIPO-v2.1-1B-A200M(1B-A200M MoE, 4096ctx, 2026-08-22)。旧系 KBlueLeaf/DanTagGen-delta-rev2(タグ専用、2024-04)。
- **根拠**: [モデル概要・学習データ・評価表(Scenery tag/Short/Truncated Long、TIPO-200M)・Kohaku License](https://huggingface.co/KBlueLeaf/TIPO-500M-ft/blob/386fc21b10c810c0c1c8f182695e28fbbd45597c/README.md) / [v2.1: rating/quality/人数タグの修正と4096ctx・52.4Bトークンでの再学習(評価数値はカードに無し)](https://huggingface.co/KBlueLeaf/TIPO-v2.1-1B-A200M/blob/f5a318524a4ab30cdbbf51816cf406170f454e65/README.md) / [TIPO (ICLR 2026)の実装、DTGとの違い(NL+タグ学習)、z-tipo-extension案内](https://github.com/KohakuBlueleaf/KGen/blob/fecfe05341f021f916f9b23e1c93f23b4c50d9bb/README.md)
- **次点**: `KBlueLeaf/TIPO-v2.1-1B-A200M`（2026-08-22の最新・評価タグ不具合修正版。ただし累計13,087DLと新しく、ライセンスmetadata null、拡張側の対応記載未確認、ベンチ数値なし。自己評価では優位の可能性あり） / `KBlueLeaf/DanTagGen-delta-rev2`（2024-04のタグ専用旧系。累計971,543DLはTIPO-500M-ft(436,120)より多いが30日18,175対59,247で、後継TIPOがNL対応かつ論文評価あり） / `FredZhang7/anime-anything-promptgen-v2`（2023-02のGPT-2系、累計DL 575でTIPOに大差）

関連リポジトリ:

- [KohakuBlueleaf/z-tipo-extension](https://github.com/KohakuBlueleaf/z-tipo-extension) — SD-WebUI/Forge/ComfyUI用のTIPO拡張(プロンプトアップサンプル)（★637 / Apache-2.0 / 最終push 2026-08-23 / 確認コミット [`61328629`](https://github.com/KohakuBlueleaf/z-tipo-extension/blob/6132862978021727284215bc2d5fe5257a872709/README.md)）
  - 637★、最終push 2026-08-23。Apache-2.0。TIPO/DanTagGen系の実運用入口。
- [KohakuBlueleaf/KGen](https://github.com/KohakuBlueleaf/KGen) — TIPOの推論・サンプリング実装(pip install tipo-kgen)（★102 / Apache-2.0 / 最終push 2026-08-22 / 確認コミット [`fecfe053`](https://github.com/KohakuBlueleaf/KGen/blob/fecfe05341f021f916f9b23e1c93f23b4c50d9bb/README.md)）
  - 101★、Apache-2.0、2026-08-22更新。READMEにICLR 2026と明記。
- [DominikDoom/a1111-sd-webui-tagcomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete) — Danbooruタグのオートコンプリート(WebUI)（★2,808 / MIT / 最終push 2026-07-01 / release 3.3.0 (2025-05-08) / 確認コミット [`4170882f`](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete/blob/4170882f90b47be130a0ff9314f663c230b9153d/README.md)）
  - 2.8k★、MIT。タグ語彙補完の定番(TIPOとは別機能)。最終push 2026-07-01。

### テキスト生成(キャラクターロールプレイ/キャラカード対話)

<a id="text-generation--character-roleplay"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [hiwaifu-research/WaifuGemma4-26b-a4b-v1](https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1/tree/540c0f8f2c33683041f227507eaab4f9f6cb17a6)（revision `540c0f8f` / 作成 2026-09-18 / 更新 2026-09-19）
- **利用条件**: apache-2.0。メタデータapache-2.0(ベースgoogle/gemma-4-26B-A4B-itのライセンスに従う点は未確認)。学習データはHiWaifuユーザーの投票ログ(非公開)。アニメ専用ではなく汎用ロールプレイ。
- **選定根拠**: 事実: アニメ特化と確認できるロールプレイ用LLMは見つからなかった(検索でヒットした'waifu'/'anime'名の小モデルは累計DL 数十〜数百で実績なし)。汎用ロールプレイ系では、2026-09-18公開のWaifuGemma4-26B-A4B(Apache-2.0、Gemma 4 MoE、GRPO)が、自社アプリHiWaifuアリーナ1.2M票の報酬で学習し、9,084戦で勝率54.7%・GLM-5.1と49.6%(いずれも自己報告、長文バイアスを補正すると中位とカード自身が記載)。ただしDLは累計1,413・likes 20と12日目で採用実績は未形成、アニメ/日本語の言及なし。採用実績はChun121/Qwen3-4B-RPG-Roleplay-V2(累計168,732DL・MIT・英語4B・ctx2048)が上。評価: 証拠が弱く低信頼。SillyTavern等のフロントで汎用モデルを選ぶのが実態。
- **指標（確認日時点）**: DL累計 1,413 / 直近30日 1,413 / likes 20 / Spaces 0
- **概要**: Gemma 4 26B-A4B(3.8B active MoE)をHiWaifuアリーナの人間投票由来の報酬モデルでGRPO(200step, LoRA r256)した汎用ロールプレイモデル。
- **入力**: キャラカード/ペルソナ＋チャット履歴(8Kトークンで学習、ベースは256Kまで)。非思考モード
- **出力**: キャラクター口調の応答(RL後は長文化、300トークン制限を指示すれば約314トークン)
- **必要環境**: カード記載: bf16、LoRAマージ済み、MoE 25.2B total/3.8B active。必要VRAMは未記載・未測定。
- **制約**: 冗長になる(勝率の一部は長さ由来、カード明記)。アリーナは自社サービスの投票で第三者再現不可。評価言語はスペイン語・ロシア語・英語等で、日本語・アニメ文脈の評価は無い。公開12日で外部の利用報告がほぼ無い。
- **使う版・派生**: 使用: 本リポジトリ(safetensors)。量子化: hiwaifu-research/WaifuGemma4-26b-a4b-v1-GGUF、-i1-GGUF(mradermacher経由含め公式/非公式混在、未確認)。
- **根拠**: [学習手法・アリーナ評価(54.7%/49.6%)・制限(長文化)](https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1/blob/540c0f8f2c33683041f227507eaab4f9f6cb17a6/README.md) / [次点: Qwen3-4B-Base+GRPO LoRA、MIT、データGryphe/Sonnet3.5-Charcard-Roleplay、ctx2048(累計168,732DL)](https://huggingface.co/Chun121/Qwen3-4B-RPG-Roleplay-V2/blob/33b68c5e222267e109fdb7443475ff463b3f0c47/README.md)
- **次点**: `Chun121/Qwen3-4B-RPG-Roleplay-V2`（採用実績は最大(累計168,732DL、likes 77、MIT)だが英語4B・ctx2048・Sonnet3.5合成データで性能上限が低い。アニメ特化でない） / `ClosedCharacter/Peach-2.0-9B-8k-Roleplay`（中国語ロールプレイ特化の9B(Yi-1.5ベース、MIT)。2025-03で更新停止、30日DL 256）

関連リポジトリ:

- [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) — キャラカード/ロールプレイ用LLMフロントエンドの事実上の標準（★33,971 / AGPL-3.0 / 最終push 2026-09-23 / release 1.19.0 (2026-09-14) / 確認コミット [`06bde939`](https://github.com/SillyTavern/SillyTavern/blob/06bde939fb1e9c4c8d8641d810f0a916b5bce127/README.md) / 制作カタログ: [sillytavern](../../categories/story.md#sillytavern)）
  - 34k★、1.19.0(2026-09-14)。AGPL-3.0。
- [jofizcd/Soul-of-Waifu](https://github.com/jofizcd/Soul-of-Waifu) — アニメ系キャラのデスクトップロールプレイ/チャットアプリ（★1,361 / GPL-3.0 / 最終push 2026-08-28 / release v2.5.1 (2026-08-28) / 確認コミット [`747048b3`](https://github.com/jofizcd/Soul-of-Waifu/blob/747048b3b3ad7d321a667630018f7ffc04eb5f6d/README.md)）
  - 1.4k★、v2.5.1(2026-08-28)。GPL-3.0。SillyTavernより小規模だがアニメ寄り。

### 文類似度(日本語埋め込み: アニメ/キャラ検索用途)

<a id="sentence-similarity"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [cl-nagoya/ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m/tree/18b60fb8c2b9df296fb4212bb7d23ef94e579cd3)（revision `18b60fb8` / 作成 2025-04-09 / 更新 2025-04-17）
- **利用条件**: apache-2.0。メタデータ・カードともApache-2.0。学習データの詳細は論文(arXiv 2409.07737)参照、未精読。
- **選定根拠**: 事実: アニメ特化の埋め込みは存在するが実績がない(Lorg0n/hikka-forge2vec: 作品メタデータ用256次元、累計112DL、2026-09-05公開。KiruruP/anime-recommendation-multilingual-mpnet-base-v2-final: 累計278DL)。汎用日本語ではcl-nagoya/ruri-v3-310mがHF累計5,620,247DL・30日544,955・likes 82・spaces 13、GitHub参照444件で突出。JMTEB平均77.24(自己報告)はPLaMo-Embedding-1B 76.10・sarashina-embedding-v1-1b 75.50・multilingual-e5-large 71.65を上回る。Apache-2.0。評価: アニメ語彙での比較は無く、キャラ/作品検索での優位は未検証。汎用SOTAとして採用。
- **指標（確認日時点）**: DL累計 5,620,247 / 直近30日 544,955 / likes 82 / Spaces 13
- **概要**: 日本語汎用テキスト埋め込みモデル(ModernBERT-Ja基盤、768次元、最大8192トークン、語彙100K)。プレフィックス方式('検索クエリ: '等)で用途を切替。
- **入力**: 日本語テキスト。プレフィックス: ''(意味)/'トピック: '/'検索クエリ: '/'検索文書: '
- **出力**: 768次元埋め込みベクトル
- **必要環境**: カード記載: transformers>=4.48、sentence-transformers。FlashAttention2推奨。VRAM等は未測定。
- **制約**: アニメ/マンガ語彙(キャラ名・作品略称・Danbooruタグ・英日混在)への特化評価は無し(JMTEBは汎用ベンチ)。日本語のみで多言語タグ検索には向かない。
- **使う版・派生**: サイズ違い: ruri-v3-30m/70m/130m(JMTEB 74.51〜76.55)。ONNX: sirasagi62/ruri-v3-30m-ONNX。リランカーは cl-nagoya/ruri-v3-reranker-310m。
- **根拠**: [JMTEB平均77.24(310m)、sarashina-embedding-v1-1b 75.50、PLaMo-Embedding-1B 76.10、multilingual-e5-large 71.65との比較表(自己報告)](https://huggingface.co/cl-nagoya/ruri-v3-310m/blob/18b60fb8c2b9df296fb4212bb7d23ef94e579cd3/README.md) / [JMTEB(日本語埋め込み評価ベンチ)の一次情報](https://github.com/sbintuitions/JMTEB/blob/526d5fc00b1682675405ae00fb3594843e53ae5d/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `BAAI/bge-m3` — 多言語(英日混在のDanbooruタグ・キャラ名)検索ならbge-m3(30日DL 35,675,298)やQwen/Qwen3-Embedding-0.6Bが現実的。日本語のみならruri-v3
- **次点**: `pfnet/plamo-embedding-1b`（JMTEB 76.10(Ruri v3カード掲載値)で僅差劣後、1B級で重い(30日DL 122,278)） / `sbintuitions/sarashina-embedding-v2-1b`（1B級で重く、採用はruri-v3に大差(v2は2025-07公開、30日DL 1,944)） / `Lorg0n/hikka-forge2vec`（作品メタデータ(タイトル/ジャンル/ポスター)用のアニメ専用埋め込みだが累計112DL・公開3週間で実績/ベンチなし）

関連リポジトリ:

- [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) — Ruri等の埋め込み/CrossEncoderを動かす標準ライブラリ（★19,137 / Apache-2.0 / 最終push 2026-09-24 / release v6.1.0 (2026-09-18) / 確認コミット [`4a3b5cd6`](https://github.com/huggingface/sentence-transformers/blob/4a3b5cd6ec718e421f57e824a41ed3fd99595df6/README.md)）
  - 19k★、v6.1.0(2026-09-18)、Apache-2.0。Ruriカードの推奨実行環境。
- [sbintuitions/JMTEB](https://github.com/sbintuitions/JMTEB) — 日本語埋め込みの評価ベンチマーク（★93 / CC-BY-SA-4.0 / 最終push 2026-07-31 / release v2.0.0 (2026-03-18) / 確認コミット [`526d5fc0`](https://github.com/sbintuitions/JMTEB/blob/526d5fc00b1682675405ae00fb3594843e53ae5d/README.md)）
  - 93★、v2.0.0(2026-03-18)、CC-BY-SA-4.0。日本語埋め込み比較の基準。

### 特徴抽出(日本語テキスト埋め込み/タグ・キャラ語彙)

<a id="feature-extraction"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [cl-nagoya/ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m/tree/18b60fb8c2b9df296fb4212bb7d23ef94e579cd3)（revision `18b60fb8` / 作成 2025-04-09 / 更新 2025-04-17）
- **利用条件**: apache-2.0。メタデータ・カードともApache-2.0。学習データの詳細は論文(arXiv 2409.07737)参照、未精読。
- **選定根拠**: 事実: HFのfeature-extractionにアニメ特化のテキスト埋め込みで実績のあるものはない(Lorg0n/hikka-forge2vecは累計112DL、deepghs/anime_sites_indicesは0DL)。Danbooruタグ語彙やキャラ名検索を日本語中心で行うなら、sentence-similarityと同じcl-nagoya/ruri-v3-310m(累計5,620,247DL・JMTEB 77.24自己報告)が最有力。評価: 英日混在のタグ・固有名詞ではruriが日本語専用な点が弱点で、多言語モデル(bge-m3, Qwen3-Embedding)との比較は未実施のため低信頼。
- **指標（確認日時点）**: DL累計 5,620,247 / 直近30日 544,955 / likes 82 / Spaces 13
- **概要**: 日本語汎用テキスト埋め込みモデル(ModernBERT-Ja基盤、768次元、最大8192トークン、語彙100K)。プレフィックス方式('検索クエリ: '等)で用途を切替。
- **入力**: 日本語テキスト。プレフィックス: ''(意味)/'トピック: '/'検索クエリ: '/'検索文書: '
- **出力**: 768次元埋め込みベクトル
- **必要環境**: カード記載: transformers>=4.48、sentence-transformers。FlashAttention2推奨。VRAM等は未測定。
- **制約**: アニメ/マンガ語彙(キャラ名・作品略称・Danbooruタグ・英日混在)への特化評価は無し(JMTEBは汎用ベンチ)。日本語のみで多言語タグ検索には向かない。
- **使う版・派生**: サイズ違い: ruri-v3-30m/70m/130m(JMTEB 74.51〜76.55)。ONNX: sirasagi62/ruri-v3-30m-ONNX。リランカーは cl-nagoya/ruri-v3-reranker-310m。
- **根拠**: [JMTEB平均77.24(310m)、sarashina-embedding-v1-1b 75.50、PLaMo-Embedding-1B 76.10、multilingual-e5-large 71.65との比較表(自己報告)](https://huggingface.co/cl-nagoya/ruri-v3-310m/blob/18b60fb8c2b9df296fb4212bb7d23ef94e579cd3/README.md) / [JMTEB(日本語埋め込み評価ベンチ)の一次情報](https://github.com/sbintuitions/JMTEB/blob/526d5fc00b1682675405ae00fb3594843e53ae5d/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `Qwen/Qwen3-Embedding-0.6B` — 多言語(英日タグ混在)用の汎用候補。HF検索値で30日DL 9,744,263。日本語のみならruri-v3を優先
- **次点**: `Lorg0n/hikka-forge2vec`（アニメ/マンガ作品メタデータ+ポスターの統合埋め込み。Apache-2.0だが累計112DL・公開2026-09-05で実績/ベンチなし）

関連リポジトリ:

- [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) — 埋め込み推論の標準ライブラリ（★19,137 / Apache-2.0 / 最終push 2026-09-24 / release v6.1.0 (2026-09-18) / 確認コミット [`4a3b5cd6`](https://github.com/huggingface/sentence-transformers/blob/4a3b5cd6ec718e421f57e824a41ed3fd99595df6/README.md)）
  - 19k★、v6.1.0(2026-09-18)、Apache-2.0。

### リランキング(日本語リランカー: アニメ検索用途)

<a id="text-ranking"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [cl-nagoya/ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m/tree/bb46934ee9ed09f850b9fcff17501b3ef7ddb2b3)（revision `bb46934e` / 作成 2025-04-06 / 更新 2025-04-18）
- **利用条件**: apache-2.0。メタデータ・カードともApache-2.0。
- **選定根拠**: 事実: アニメ特化リランカーは見つからない。汎用日本語でcl-nagoya/ruri-v3-reranker-310mは累計1,439,188DL・30日301,410・likes 15、GitHub参照136件、Apache-2.0。カード自己報告でJQaRA nDCG@10 86.9(BAAI/bge-reranker-v2-m3は67.3、hotchpotch系cross-encoder-large-v1は71.0)。軽量代替hotchpotch/japanese-reranker-xsmall-v2(MIT, 30日124,685DL)はカード上スコア0.8699(別ベンチ・自己報告)で速度約1/5。評価: 一般日本語QA検索の評価であり、アニメ領域での優位は未検証。
- **指標（確認日時点）**: DL累計 1,439,188 / 直近30日 301,410 / likes 15 / Spaces 1
- **概要**: 日本語汎用リランカー(ModernBERT-Ja基盤CrossEncoder、最大8192トークン)。検索結果の再順位付け用。
- **入力**: (クエリ, 文書)ペア
- **出力**: 関連度スコア(0〜1)
- **必要環境**: カード記載: transformers>=4.48、sentence-transformers CrossEncoder。FlashAttention2推奨。未測定。
- **制約**: 汎用日本語向け。アニメ/キャラ領域での評価は無い。
- **使う版・派生**: 小型代替: hotchpotch/japanese-reranker-xsmall-v2(MIT, 30日DL 124,685, カード自己報告スコア0.8699、速度重視)。旧: cl-nagoya/ruri-reranker-large等。
- **根拠**: [JQaRA nDCG@10 86.9 / JaCWIR MAP@10 95.4 / MIRACL Recall@30 97.3(自己報告)。bge-reranker-v2-m3(67.3/93.4/94.9)を上回る](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m/blob/bb46934ee9ed09f850b9fcff17501b3ef7ddb2b3/README.md)
- **次点**: `hotchpotch/japanese-reranker-xsmall-v2`（最小・高速でCPU/低遅延向けに有用(MIT, 累計720,727DL)。精度は上位ではない） / `BAAI/bge-reranker-v2-m3`（多言語の事実上の標準だがRuriカード上の日本語JQaRAで67.3と劣る(自己報告)）

関連リポジトリ:

- [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) — CrossEncoderによるリランキング推論（★19,137 / Apache-2.0 / 最終push 2026-09-24 / release v6.1.0 (2026-09-18) / 確認コミット [`4a3b5cd6`](https://github.com/huggingface/sentence-transformers/blob/4a3b5cd6ec718e421f57e824a41ed3fd99595df6/README.md)）
  - 19k★、v6.1.0(2026-09-18)、Apache-2.0。Ruriリランカーの推奨実行環境。

### 穴埋め(日本語マスクLM)

<a id="fill-mask"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [sbintuitions/modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m/tree/28c180b16463ba6f3fa79b48756fbf21586fe23e)（revision `28c180b1` / 作成 2025-02-06 / 更新 2025-05-01）
- **利用条件**: mit。メタデータMIT。学習は日英Webコーパス4.39Tトークン(詳細コーパスはカード参照)。
- **選定根拠**: 事実: アニメ/マンガ特化のfill-maskモデルは見つからない(検索で該当なし)。汎用日本語ではsbintuitions/modernbert-ja-130mが2025-02公開・累計472,993DL・30日99,401・likes 51・MIT、Ruri v3の基盤にもなっている。老舗のtohoku-nlp/bert-base-japanese-whole-word-masking(30日338,980)の方がDLは多いが2022年世代。評価: fill-maskは事前学習モデルの入口にすぎず、アニメ用途は下流の微調整タスクで決まる。
- **指標（確認日時点）**: DL累計 472,992 / 直近30日 99,401 / likes 51 / Spaces 1
- **概要**: 日本語ModernBERT(130M、語彙102,400、最大8192トークン)。主にファインチューニングの土台として使うエンコーダ。
- **入力**: [MASK]を含む日本語文
- **出力**: マスク位置のトークン候補とスコア
- **必要環境**: カード記載: transformers>=4.48。FlashAttention2推奨。未測定。
- **制約**: アニメ特化ではない。fill-maskは下流微調整(分類/NER等)の前提で、単体でアニメ語彙補完に使う用途は想定外。
- **使う版・派生**: 同系: modernbert-ja-30m/70m/310m(310m: 累計288,779DL)。Ruri v3の基盤。
- **根拠**: [モデル概要・学習段階・用途説明(ファインチューニング前提)](https://huggingface.co/sbintuitions/modernbert-ja-130m/blob/28c180b16463ba6f3fa79b48756fbf21586fe23e/README.md)
- **次点**: `sbintuitions/modernbert-ja-310m`（大型版(累計288,779DL)。精度優先なら選択肢だが単体評価は未確認） / `tohoku-nlp/bert-base-japanese-whole-word-masking`（2022年世代のBERT。30日DLは多いが512トークン制限・形態素解析前処理が必要）

### トークン分類(日本語NER: 作品名/キャラ名/声優名)

<a id="token-classification"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [llm-book/bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset/tree/49ef0cbab94d38498d0c088f73549c22a59def1b)（revision `49ef0cba` / 作成 2023-05-28 / 更新 2023-07-25）
- **利用条件**: apache-2.0。メタデータapache-2.0。学習データllm-book/ner-wikipedia-dataset(Wikipedia由来、CC-BY-SA系の可能性、未確認)。
- **選定根拠**: 事実: アニメ作品名・キャラ名・声優名のNER、および名前の読み(ふりがな)推定を行う公開モデルはHFで確認できなかった(japanese ner/furigana検索: 汎用NER数件、furiganaはWhisper/OCR系のみ)。汎用ではllm-book/bert-base-japanese-v3-ner-wikipedia-dataset(累計1,642,023DL・30日9,534・Apache-2.0)が最も採用され、教科書由来で再現性が高い。評価: Wikipedia人名/地名ラベルでアニメ固有名詞への適合は未検証。現実にはLLMのプロンプト抽出やDB照合の方が妥当。
- **指標（確認日時点）**: DL累計 1,642,023 / 直近30日 9,534 / likes 11 / Spaces 0
- **概要**: cl-tohoku/bert-base-japanese-v3をWikipedia固有表現データで微調整した日本語NER。人名・地名・組織名等を抽出。
- **入力**: 日本語文
- **出力**: 固有表現スパンとラベル(人名/地名/法人名等)
- **必要環境**: カード記載: transformers pipeline(aggregation_strategy=simple)。未測定。
- **制約**: Wikipedia学習のため、アニメ作品名・キャラ名・声優名(作中固有名詞、ひらがな/カタカナ愛称)の抽出精度は未検証。作品名クラスは持たない。
- **使う版・派生**: CRF版: llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset。
- **根拠**: [教科書『大規模言語モデル入門』第6章の固有表現認識モデル、使用例](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset/blob/49ef0cbab94d38498d0c088f73549c22a59def1b/README.md)
- **次点**: `tsmatz/xlm-roberta-ner-japanese`（多言語XLM-R系(2022、累計DL少)。同じく汎用Wikipedia系） / `jurabi/bert-ner-japanese`（2022年の汎用NER、30日3,432DL）

### ゼロショット分類(ジャンル/レーティング/同人ラベル)

<a id="zero-shot-classification"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [MoritzLaurer/bge-m3-zeroshot-v2.0](https://huggingface.co/MoritzLaurer/bge-m3-zeroshot-v2.0/tree/9abf1c8aaeb82a2447809c20753ed0b106b76652)（revision `9abf1c8a` / 作成 2024-04-02 / 更新 2024-04-22）
- **利用条件**: mit。メタデータMIT。ただしカードは『-c』なしモデルは多様なライセンスのデータ(ANLI等)を含むと明記。商用可と断定不可。
- **選定根拠**: 事実: アニメ特化のゼロショット分類モデルは存在しない。汎用の多言語MoritzLaurer/bge-m3-zeroshot-v2.0が累計3,750,217DL・30日118,593・likes 70・MIT、日本語専用のakiFQC/bert-base-japanese-v3_nli-jsnli-jnli-jsickは累計5,761DL。評価: いずれもアニメのジャンル/年齢区分での精度は未検証で、日本語性能の数値は未確認。実務ではLLMにラベルを提示して分類させる方が一般的。
- **指標（確認日時点）**: DL累計 3,750,217 / 直近30日 118,593 / likes 70 / Spaces 2
- **概要**: bge-m3-retromae基盤の多言語ゼロショット分類器(NLI形式、entailment/not_entailment)。任意ラベルで分類できる。
- **入力**: テキストと候補ラベル/仮説
- **出力**: ラベル確率
- **必要環境**: カード記載: transformers zero-shot-classification pipeline、CPU可。未測定。
- **制約**: 日本語性能の数値は確認できていない(カードは多言語を謳うが日本語評価表は未確認)。アニメ特化ではない。
- **使う版・派生**: 同系: MoritzLaurer/deberta-v3-*-zeroshot-v2.0(英語中心)。日本語NLI: akiFQC/bert-base-japanese-v3_nli-jsnli-jnli-jsick(30日1,506DL, CC-BY-SA-4.0)。
- **根拠**: [ゼロショット分類の方式とライセンス注記(-cなしはデータの混在)](https://huggingface.co/MoritzLaurer/bge-m3-zeroshot-v2.0/blob/9abf1c8aaeb82a2447809c20753ed0b106b76652/README.md)
- **次点**: `akiFQC/bert-base-japanese-v3_nli-jsnli-jnli-jsick`（日本語専用NLI(CC-BY-SA-4.0)だが累計5,761DLと採用が小さく2024-04で停止）
