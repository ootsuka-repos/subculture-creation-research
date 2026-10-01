# 音声のアニメ系SOTA（2026-10-01）

[一覧へ](../anime-task-sota.md) · [リポジトリ全体像](../anime-repositories.md) · [正本JSON](../../sota-catalog.json)

選定基準・注意は[一覧ページ](../anime-task-sota.md)。各項目の「最良」は確度付きの編集判断で、重み取得・推論実行は未実施。

### テキスト音声合成(日本語・アニメ/ゲーム調キャラ音声)

<a id="text-to-speech--anime-character-tts"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [phasefield-audio/Irodori-TTS-v4.1-Anime](https://huggingface.co/phasefield-audio/Irodori-TTS-v4.1-Anime/tree/6b259f5baa5e236b3d14cbd1f8555ca87d92b530)（revision `6b259f5b` / 作成 2026-09-04 / 更新 2026-09-04）
- **利用条件**: mit。カード: MIT。「ベースと同じMITと倫理的制限に従う」とのみ記載(ベース: 無断の声優・著名人のなりすまし/ディープフェイク禁止)。ファインチューン用アニメ音声の出所・権利は未記載で、学習データ由来の権利リスクは不明。商用可とは断定できない。ベース側は生成物に透かし(SilentCipher)を付与する設計。
- **選定根拠**: 【事実】phasefield-audio/Irodori-TTS-v4.1-Anime は Aratako/Irodori-TTS-v4.1-Small(MIT)をアニメ調音声データでfine-tuneした版(カード記載)。HF DLは0だがIrodori系はHF側で未集計(ベースv4.1-Smallも0)で比較不能。likes 128(ベース60)、spaces 2、GitHubコード参照103件、X上の実利用報告が多い(Easy-Irodori-TTS告知788 likes、GPT Astra連携のデモ614 likes、Colab版・ModelScope Studio掲載、Gemini/Fish Audioとの比較動画167 likes)。対抗のNandemoGHS/Anime-Llasa-3Bは学習33,000時間と規模は大きいがCC-BY-NC、DL 24,301/30日335、likes 30、参照66件、多音字(辛い)誤読の報告(Discussion #1)、データの権利処理への懸念ツイートがあり、採用・ライセンス両面で劣後。【評価】日本語アニメ調キャラ音声の実質標準はIrodori系列。MITで48kHz・参照音声クローン・caption/絵文字制御・量子化版が揃う点で実装選定に最も安全。【疑い】微調整データの出所・注釈が非公開(カード自身が「ベースのアノテーション手法は非公開のため独自に注釈」と記載)、投稿者は2026-09-04作成・モデル1件のみの匿名アカウント、ベースとの比較音声/数値がなく(Discussion #2の比較要望は未回答)「アニメ版がベースより良い」ことは未実証。数値ベンチ(Joyo Kanji Yomi/JSUT、自己報告)は公式ベースv4.1-Smallにしか存在しない。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 128 / Spaces 2
- **概要**: Aratako/Irodori-TTS-v4.1-Small(RF-DiT、約766Mパラメータ、48kHz、Semantic-DACVAE-Japanese-32dim)をアニメ調音声でfine-tuneした日本語TTS。参照音声によるゼロショット声質複製、caption(Voice Design)、絵文字による感情・非言語制御を継承(ベースカード記載、本カードは詳細を書かずベース参照)。
- **入力**: 日本語テキスト(+任意で参照音声、caption、絵文字)
- **出力**: 48kHz波形(SilentCipher透かしはベース推論コード側で付与)
- **必要環境**: 推論・導入はAratako/Irodori-TTSのuv sync(cu128/rocm/xpu/cpu)。VRAM・速度はカードに記載なし、未測定。
- **制約**: 日本語のみ(ベースカード)。独自注釈のためcaption/絵文字制御がベースと異なる挙動を示す可能性(本カード)。短い参照1本では話者類似度が下がる(ベースカード:30秒以上推奨)。難読漢字・固有名詞の誤読あり(ベースカード)。ベース比較の客観評価なし。
- **使う版・派生**: ルートのmodel.safetensorsがフル精度。量子化サブディレクトリ: int8-weight-only / int8-dynamic / int4-weight-only / float8-weight-only / float8-dynamic(同一リポジトリ)。同名再アップ sekkit/Irodori-TTS-v4.1-Anime・musafa901/Irodori-TTS-v4.1-Anime(likes 0、非推奨)。GGUF(audio.cpp向け)は要望のみ(Discussion #1)。ベース側MLX版: mlx-community/Irodori-TTS-v4.1-Small-fp16/8bit。
- **根拠**: [MIT・「ベースのアノテーション手法は非公開のため独自に注釈、caption/絵文字制御が異なる可能性」・量子化ディレクトリ一覧](https://huggingface.co/phasefield-audio/Irodori-TTS-v4.1-Anime/blob/6b259f5baa5e236b3d14cbd1f8555ca87d92b530/README.md) / [ベース側のベンチ(Joyo Kanji Yomi Kana-CER 7.29%、JSUT Sentence Kana-CER 3.43%、自己報告)・制約・倫理制限・機能一覧](https://huggingface.co/Aratako/Irodori-TTS-v4.1-Small/blob/2b28324dc263ed5e6638b3cf3dd94c82ead07b4b/README.md) / [比較音声の要望が未回答(2026-09-21)](https://huggingface.co/phasefield-audio/Irodori-TTS-v4.1-Anime/discussions/2) / [Easy-Irodori-TTS(v4.1-Small/v4.1-Anime対応ツール)告知 788 likes](https://x.com/YuuPro_2022/status/2098710827499164073) / [ローカルのIrodori-TTS-v4.1-Animeで雑談配信デモ 614 likes](https://x.com/nachat_dayo/status/2096895393376411927) / [Anime-Llasa-3B関連リポジトリの著作権上の懸念(ツイート主の主張)](https://x.com/mr62n/status/1975887682820792621)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `Aratako/Irodori-TTS-v4.1-Small` — アニメ特化ではない汎用日本語ベース(MIT、likes 60、spaces 7、ベンチあり)。アニメ版の微調整データ出所が気になる場合やベンチ根拠が必要な場合はこちら。
- **次点**: `NandemoGHS/Anime-Llasa-3B`（33,000時間学習でアニメ調に明確に特化するがCC-BY-NC(商用不可)、多音字誤読報告あり、採用指標(DL 30日335、likes 30)が低く、学習データの権利処理に懸念の投稿がある。Llasa-3B+XCodec2の2段構成で重い。） / `Aratako/Irodori-TTS-v4-Large`（3.29Bの大型版(2026-09-27公開、likes 52)。ライセンスはGemma Terms of Use(T5Gemma 2エンコーダ由来)でMITではない。アニメ特化ではない汎用日本語モデル。） / `WariHima/index-tts2-japanese-prosody`（IndexTTS-2の日本語韻律fine-tune(Apache-2.0、likes 6)。アニメ特化ではなく採用実績も乏しい。）

関連リポジトリ:

- [Aratako/Irodori-TTS](https://github.com/Aratako/Irodori-TTS) — Irodori-TTS(v2〜v4.1/v4-Large)の学習・推論・Gradio UI・LoRA・Speaker Inversionコード（★1,373 / MIT / 最終push 2026-09-12 / 確認コミット [`89f9d8fb`](https://github.com/Aratako/Irodori-TTS/blob/89f9d8fbd4d51ea019867ee1197725ede1df13c5/README.md)）
  - 公式実装。MIT、★1363、コード参照788件、2026-09-12更新。anime版もカード上この実装で動かす指定。
- [Aratako/Irodori-TTS-Server](https://github.com/Aratako/Irodori-TTS-Server) — OpenAI互換APIサーバー(Irodori用)（★78 / MIT / 最終push 2026-09-13 / 確認コミット [`61012c76`](https://github.com/Aratako/Irodori-TTS-Server/blob/61012c760f22f7b4a6c21c5c5f8f9e148120b6f9/README.md)）
  - 公式READMEが案内するOpenAI互換推論API。MIT、★77、2026-09-13更新。
- [Aivis-Project/AivisSpeech-Engine](https://github.com/Aivis-Project/AivisSpeech-Engine) — 日本語感情表現TTSエンジン(VOICEVOX互換API+AIVM形式)（★181 / LGPL-3.0 / 最終push 2026-09-18 / release 1.2.0 (2026-04-30) / 確認コミット [`0cf0635d`](https://github.com/Aivis-Project/AivisSpeech-Engine/blob/0cf0635d5f74de4cf07e5fb87b25c4c1d0c8a331/README.md)）
  - 別系統: VOICEVOX ENGINE派生の日本語合成エンジン(LGPL-3.0)。X投稿で利用者10万人突破(@aivis_project)。CPUのみでも動作、AIVM形式のモデルハブあり。

### テキスト音声合成(多言語ゼロショット声質複製・吹き替え/多言語用途)

<a id="text-to-speech--multilingual-zero-shot-cloning"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [Qwen/Qwen3-TTS-12Hz-1.7B-Base](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/tree/fd4b254389122332181a7c3db7f27e918eec64e3)（revision `fd4b2543` / 作成 2026-01-21 / 更新 2026-01-23）
- **利用条件**: apache-2.0。メタデータ・カードともApache-2.0。生成音声の権利・声質複製時の本人同意は利用者責任。商用可とは断定しない(Qwen3-TTS-Tokenizer等の付随条件は未精査)。
- **選定根拠**: 【事実】アニメ特化の多言語ゼロショットTTSは見つからず(日本語アニメ用途はIrodori系が担う)。多言語用途の汎用最有力として Qwen/Qwen3-TTS-12Hz-1.7B-Base を採る。DL 30日3,706,350/累計19,655,002、likes 539、spaces 100、GitHub QwenLM/Qwen3-TTS ★13,597(Apache-2.0)、コード参照5,552件。カード記載: 日本語を含む10言語、3秒の音声で声質複製、fine-tune用ベース。自己報告の多言語WER(CustomVoice 1.7B、日本語4.924%、GPT-4o-AudioPreviewは5.001%)はBaseではなくCustomVoice版の数値。【評価】採用規模・Apache-2.0・公式実装で次点(VoxCPM2、OmniVoice、IndexTTS-2)より選定リスクが低い。【疑い】アニメ演技・キャラ音声での品質や日本語声質複製の比較データは未確認で、日本語アニメ用途ではIrodori系との直接比較がない。IndexTTS-2系はHFメタデータのライセンス未設定でLICENSE.txt個別確認が必要。
- **指標（確認日時点）**: DL累計 19,745,143 / 直近30日 3,679,759 / likes 540 / Spaces 100
- **概要**: Qwen3-TTS(12Hz)のBase 1.7B。日本語含む10言語、3秒程度の参照音声による声質複製、fine-tuneのベースとして利用可(カード記載)。
- **入力**: テキスト+参照音声(+参照テキスト)
- **出力**: 音声波形(ストリーミング低遅延に対応と記載)
- **必要環境**: カードは最低要件を明示せず(Discussion #5に「8GB環境で読み込みエラー」を問う投稿あり)。未測定。
- **制約**: 日本語アニメ/キャラ演技の品質・感情制御は未評価。Discussionに発話速度・ポーズ制御の不足を指摘する投稿あり(#9,#10,#11)。
- **使う版・派生**: 同系列: 0.6B-Base、1.7B/0.6B-CustomVoice、1.7B-VoiceDesign。GGUF: Serveurperso/Qwen3-TTS-GGUF ほか第三者版あり。
- **根拠**: [Apache-2.0、10言語(日本語含む)、Base=3秒声質複製+fine-tune用、多言語WER表(CustomVoice)](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/blob/fd4b254389122332181a7c3db7f27e918eec64e3/README.md) / [公式実装(★13,597)](https://github.com/QwenLM/Qwen3-TTS)
- **次点**: `openbmb/VoxCPM2`（likes 1,650・DL 30日425,152でApache-2.0だが、日本語・キャラ音声の検証材料が未確認。） / `k2-fsa/OmniVoice`（DL 30日1.43M・likes 1,452と大規模だがHFメタデータのライセンス未設定で、日本語品質の根拠も未確認。） / `IndexTeam/IndexTTS-2`（likes 787、感情/長さ制御に強みがあるがライセンスはリポジトリ内LICENSE.txt(メタデータ未設定)、日本語はコミュニティfine-tune(WariHima版)頼み。）

関連リポジトリ:

- [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) — Qwen3-TTS公式推論・fine-tuningコード（★13,607 / Apache-2.0 / 最終push 2026-03-17 / 確認コミット [`022e286b`](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/README.md) / 制作カタログ: [qwen3-tts](../../categories/tts.md#qwen3-tts)）
  - 公式実装、Apache-2.0、★13,597、コード参照はモデルIDで5,552件。
- [index-tts/index-tts](https://github.com/index-tts/index-tts) — IndexTTS-2系ゼロショットTTS(代替)（★24,258 / NOASSERTION / 最終push 2026-09-29 / release v2.5.0 (2026-08-13) / 確認コミット [`d9e41aac`](https://github.com/index-tts/index-tts/blob/d9e41aac89fd00b3d71497fddb287b7f24613712/README.md) / 制作カタログ: [index-tts](../../categories/tts.md#index-tts)）
  - ★24,238、v2.5.0を2026-08-13に公開、2026-09-29更新。ライセンスはGitHub上NOASSERTION(要個別確認)。

### テキスト音声合成(特定キャラの少量データ学習・専用声モデル作成)

<a id="text-to-speech--character-voice-training"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [lj1995/GPT-SoVITS](https://huggingface.co/lj1995/GPT-SoVITS/tree/336b2ec4e8d4ac74740798dd40af44e74659ecaf)（revision `336b2ec4` / 作成 2024-01-16 / 更新 2025-06-04）
- **利用条件**: mit。メタデータMIT。事前学習データの詳細・出典はカードに無い。学習に使う音声(声優・ゲーム音声)の権利は利用者責任。商用可とは断定しない。
- **選定根拠**: 【事実】特定キャラの声を数十秒〜数分のデータで学習する用途ではGPT-SoVITSが最大採用。lj1995/GPT-SoVITS(事前学習重み置き場、MIT)はlikes 425・spaces 74・Discussion 10、HF DLは未集計(0)。GitHub RVC-Boss/GPT-SoVITS ★62,272(MIT)、コード参照822件、2026-08-18更新。READMEの主張: 5秒ゼロショット、1分で few-shot fine-tune、日本語を含む5言語。対抗のStyle-Bert-VITS2(litagin02)は日本語専用設計・JP-Extra対応だが★1,378、AGPL-3.0、最終push 2025-12-07、最新リリース2.7.0(2025-08-24)と鈍化。【評価】汎用だがアニメキャラ音声化の実績が最大で、日本語対応と活発な保守の両立からこれを選ぶ。Irodori系はLoRA/Speaker Inversionで同用途に対応(参照音声のみで足りるなら最新のIrodoriを優先)。【疑い】「アニメ特化」ではない汎用モデル、READMEのfew-shot性能は自己主張で第三者比較は未確認、最終リリース20250606v2proから約16か月、Style-Bert-VITS2は最新事前学習(3.0-base)にカードがない。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 425 / Spaces 74
- **概要**: GPT-SoVITSの事前学習モデル置き場(gsv-v2final-pretrained、gsv-v4-pretrained、chinese-hubert-base、chinese-roberta-wwm-ext-large ほか)。少量データfine-tuneと5秒ゼロショットに使う。
- **入力**: 参照音声(数秒〜1分)+学習用音声と書き起こし(fine-tune時)
- **出力**: 合成音声
- **必要環境**: カードは1行のみ(「GPT-SoVITSで使う事前学習モデル」)。要件はGitHub側READMEに従う。未測定。
- **制約**: アニメ特化ではない。HFリポジトリはモデルカード実質なし。日本語品質・感情制御の客観ベンチなし。
- **使う版・派生**: 重みはHFのlj1995/GPT-SoVITS(gsv-v4-pretrained等)。Style-Bert-VITS2系は litagin/Style-Bert-VITS2-3.0-base(2025-12-07、D/G/WD_0.safetensorsのみ、READMEなし)。
- **根拠**: [カードは1行(事前学習モデル置き場)、MIT](https://huggingface.co/lj1995/GPT-SoVITS/blob/336b2ec4e8d4ac74740798dd40af44e74659ecaf/README.md) / [README: 5秒ゼロショット、1分few-shot、日本語含む5言語(GitHub側の主張)](https://github.com/RVC-Boss/GPT-SoVITS)
- **次点**: `litagin/Style-Bert-VITS2-3.0-base`（日本語特化・感情スタイル制御でVN/ガルゲ界隈向きだが、AGPL-3.0、リポジトリ★1,378で更新が2025-12止まり、HF側にカードなし(likes 7)。） / `Aratako/Irodori-TTS-v4.1-Small`（Irodoriは参照音声ゼロショット+LoRA/Speaker Inversionで同用途に使え日本語品質が高いが、専用声モデルの大量運用エコシステム(AIVM/ボイスモデル交換)はGPT-SoVITS・SBV2・AivisSpeech側が厚い。）

関連リポジトリ:

- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) — 少量データ学習TTS/WebUI(学習・推論・データ整備ツール)（★62,221 / MIT / 最終push 2026-08-18 / release 20250606v2pro (2025-06-06) / 確認コミット [`48b1a016`](https://github.com/RVC-Boss/GPT-SoVITS/blob/48b1a0169a28582a8984402f82cf438d3bfa6aca/README.md) / 制作カタログ: [gpt-sovits](../../categories/tts.md#gpt-sovits)）
  - ★62,272、MIT、コード参照822件、日本語UI・日本語対応。
- [litagin02/Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) — 日本語特化の感情スタイル付きTTS学習/エディタ(SBV2)（★1,379 / AGPL-3.0 / 最終push 2025-12-07 / release 2.7.0 (2025-08-24) / 確認コミット [`66de777e`](https://github.com/litagin02/Style-Bert-VITS2/blob/66de777e06392c0f313600be03c43ef96658b244/README.md) / 制作カタログ: [style-bert-vits2](../../categories/tts.md#style-bert-vits2)）
  - 日本語特化の感情スタイル付きTTS学習/エディタ(SBV2)。READMEはJP-Extra事前学習モデルを案内(リンク先litagin/Style-Bert-VITS2-2.0-base-JP-ExtraはHF APIで404を確認)。AGPL-3.0、★1,378、更新は2025-12。
- [Aivis-Project/AivisSpeech-Engine](https://github.com/Aivis-Project/AivisSpeech-Engine) — AIVM形式モデルを使う日本語TTSエンジン（★181 / LGPL-3.0 / 最終push 2026-09-18 / release 1.2.0 (2026-04-30) / 確認コミット [`0cf0635d`](https://github.com/Aivis-Project/AivisSpeech-Engine/blob/0cf0635d5f74de4cf07e5fb87b25c4c1d0c8a331/README.md)）
  - VOICEVOX互換API、LGPL-3.0、2026-09-18更新、利用者10万人超の告知(X)。

### テキスト音声生成(アニメソング/ボーカル入り楽曲・BGM生成)

<a id="text-to-audio--song-generation"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [ACE-Step/Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5/tree/19671f406d603126926c1b7e2adc169acbcade22)（revision `19671f40` / 作成 2026-01-23 / 更新 2026-02-03）
- **利用条件**: mit。メタデータ・カードともMIT。カードは「ライセンス済み・ロイヤリティフリー・合成データで学習し商用利用可」と自己申告(第三者検証なし)。生成物の権利・類似曲リスクは利用者責任。商用可とは断定しない。
- **選定根拠**: 【事実】アニメ/ボカロ/アニソン特化の公開楽曲生成モデルは見つからず。近いのは ryanontheinside/j_pop-acestep1.5-xl-v1(ACE-Step 1.5 XL用のJ-Pop LoRA、DL累計149、likes 0、ライセンス未設定)のみで採用実績なし。ゲームBGM特化(game music/bgm/chiptune検索)・アニメ特化SFX生成も該当なし。汎用の実用最良として ACE-Step/Ace-Step1.5 を採る: MIT、DL 30日60,818/累計429,095、likes 880、spaces 100、GitHub ace-step/ACE-Step-1.5 ★12,959、コード参照1,250件、LoRA学習が公式機能(カード/README: 8曲・3090で約1時間、約4GB未満VRAMで推論、50以上の言語)。【比較】MiniMaxAI/MiniMax-Music3(2026-08-07、likes 1,418、Gigazine記事で日本語ボーカル対応報道、独自Community License)とm-a-p/YuE2-3B(2026-09-09、likes 1,045、CC-BY-NC、自己報告のWildSongBenchでSuno v5超え、日本語対応の報道)は新しく話題だが、いずれも日本語歌唱品質の第三者比較が無い。【疑い】ACE-StepはXで日本語の漢字読み誤り・歌詞無視が報告されている。実際の日本語歌唱品質でMiniMax-Music3/YuE2が上回る可能性は高く、商用条件(ACEはMIT、MiniMaxは表示義務と年商2,000万USD超は要許諾、YuE2は非商用)で選ぶ暫定判断。
- **指標（確認日時点）**: DL累計 431,547 / 直近30日 61,360 / likes 881 / Spaces 100
- **概要**: 拡散Transformer+LM(計画役)の楽曲生成基盤モデル。歌詞+キャプションから完全な楽曲、カバー、リペイント、ボーカル→BGM変換。50以上の言語、LoRAによる少量曲での個人化に対応(カード記載)。
- **入力**: 歌詞+スタイル記述(キャプション)、参照音声(カバー/編集)
- **出力**: 楽曲音声(最大10分の構成が可能と記載)
- **必要環境**: カード: 4GB未満VRAMで動作、A100で1曲2秒未満、RTX 3090で10秒未満(自己申告)。XL(4B)系は12GB以上(オフロード時)/20GB推奨(GitHub README)。未測定。
- **制約**: アニメ特化ではない。日本語の漢字の読み誤り・歌詞無視がXで報告(@aihonobono2023、XL Turbo使用)。商用可との記述は学習データの由来説明付きだが自己申告。
- **使う版・派生**: 同リポジトリ系: acestep-v15-xl-sft / xl-turbo(MIT、2026-04-02)、acestep-5Hz-lm-0.6B/4B、diffusers版。J-Pop LoRA: ryanontheinside/j_pop-acestep1.5-xl-v1(低採用)。
- **根拠**: [MIT、50+言語、LoRA、商用可の自己申告(学習データの構成)、速度/VRAM自己申告](https://huggingface.co/ACE-Step/Ace-Step1.5/blob/19671f406d603126926c1b7e2adc169acbcade22/README.md) / [公式リポジトリ(XL 4B DiT、LoRA学習、ComfyUI案内)](https://github.com/ace-step/ACE-Step-1.5) / [ACE-Step 1.5 XL Turbo日本語生成の試用報告(漢字読み誤り・歌詞無視の課題)](https://x.com/aihonobono2023/status/2088114314075046358) / [YuE2が日本語ボーカル対応との報道(1,921 likes)](https://x.com/gigazine/status/2098381118147867046)
- **次点**: `MiniMaxAI/MiniMax-Music3`（2026-08-07公開、likes 1,418、DL累計31,510、日本語ボーカル可との報道/試用投稿あり(ComfyUI対応)。8B+2.4Bで重く、独自Community License(表示義務・年商20M USD超は要許諾)。ベンチ/第三者比較なし。日本語品質だけならこちらが上の可能性。） / `m-a-p/YuE2-3B`（2026-09-09公開、likes 1,045、自己報告のWildSongBenchでSuno v5を上回ると主張(best-of-8)。CC-BY-NC-4.0で非商用、24GB GPU推奨、公開3週間で未成熟。） / `HeartMuLa/HeartMuLa-oss-3B`（Apache-2.0、likes 261だがDL累計21,601と採用が小さく日本語の根拠なし。）

関連リポジトリ:

- [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) — ACE-Step 1.5推論・LoRA学習・Gradio/API（★12,984 / MIT / 最終push 2026-10-01 / release v0.1.8 (2026-05-18) / 確認コミット [`ca1e85fe`](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/README.md) / 制作カタログ: [ace-step-1.5](../../categories/music.md#ace-step-1.5)）
  - ★12,959、MIT、v0.1.8(2026-05-18)、2026-09-03更新。
- [MiniMax-AI/MiniMax-Music3](https://github.com/MiniMax-AI/MiniMax-Music3) — MiniMax-Music3 公式推論コード(代替)（★925 / ライセンス未表示 / 最終push 2026-08-14 / 確認コミット [`94565506`](https://github.com/MiniMax-AI/MiniMax-Music3/blob/945655064d59b98004dd70002e7eb5c8c6e11373/README.md)）
  - ★919、2026-08-14更新。ComfyUI公式対応、モデルは独自Community License。
- [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) — YuE/YuE2 公式コード(代替)（★10,687 / Apache-2.0 / 最終push 2026-09-29 / release yue2-v0.1.6 (2026-09-09) / 確認コミット [`18a07bb6`](https://github.com/multimodal-art-projection/YuE/blob/18a07bb628f070c2eede44c3143834818e856a73/README.md) / 制作カタログ: [yue](../../categories/music.md#yue)）
  - ★10,639、Apache-2.0(コード)、yue2-v0.1.6(2026-09-09)。モデル重みはCC-BY-NC。

### 音声認識(アニメ/ゲーム調の演技セリフ・非言語発話の書き起こし)

<a id="automatic-speech-recognition--anime-dialogue-asr"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [litagin/anime-whisper](https://huggingface.co/litagin/anime-whisper/tree/22e2008a8182b357da3922a6308d095008f72973)（revision `22e2008a` / 作成 2024-11-10 / 更新 2024-11-24）
- **利用条件**: mit。メタデータMIT。学習データはガルゲ音声(litagin/Galgame_Speech_ASR_16kHz)で、ゲーム音声の権利は個別。NSFW音声も書き起こせるとカードに明記(汎用モデルとして扱うが利用場面に注意)。商用可とは断定しない。
- **選定根拠**: 【事実】litagin/anime-whisper: kotoba-whisper-v2.0を、約5,300時間・373万ファイルのガルゲ音声(litagin/Galgame_Speech_ASR_16kHz)でfine-tune。DL 30日60,772/累計385,072、likes 163、spaces 9、コード参照125件。自己報告CER(学習外のノベルゲーム5作・約75kファイル、no_repeat_ngram_size=5): anime-whisper 平均13.0%、whisper-large-v3 16.5%、kotoba-whisper-v2.0 18.8%、reazonspeech-nemo-v2 23.6%。第三者(efwkjn、後発モデル作者)のBENCH.md(VNゲーム5作)でも、比較対象に含まれるlitagin/anime-whisperとみられる行「anime」(beam5・n-gram抑制、5作平均CER 13.2%)が後発whisper-ja-anime-v0.3(同設定13.6%)と同水準。※行名「anime」=litagin版は並び順からの推定[INFERENCE]、比較者は競合モデル作者で自己報告。HF Discussionで「非言語発話や擬音の処理は他モデルを大きく上回る」との称賛(2026-03)。【次点】jaykwok/Qwen3-ASR-1.7B-JA-Anime-Galgame(同じデータでQwen3-ASR-1.7Bを全層fine-tune、2026-05-31、DL 30日8,845、likes 1)は自己報告CER 0.1285(base 0.1437、対象4ソース800クリップ)だがanime-whisperとの直接比較が無くライセンスが「other」。【評価】実績・比較評価・MITで最も安全。【疑い】最終更新2024-11-24と古く、タイムスタンプ出力がpipeline標準でなく別途工夫が要る(Discussion #2,#3)。出力正規化の癖(。省略、…1個、半角英数)と、initial_prompt使用で幻覚化する制約。
- **指標（確認日時点）**: DL累計 386,606 / 直近30日 60,093 / likes 163 / Spaces 9
- **概要**: kotoba-whisper-v2.0(whisper-large-v3蒸留)をガルゲ音声・台本5,300時間でfine-tuneした日本語ASR。言い淀み・笑い・叫び・吐息などの非言語発話を忠実に書き起こし、句読点がセリフ台本調になる(カード記載)。
- **入力**: 16kHz日本語音声(30秒チャンク、initial promptなし)
- **出力**: 日本語テキスト(句読点・…つき。タイムスタンプは標準出力なし)
- **必要環境**: transformers pipeline(fp16、batch_size 64例)。VRAM・速度は未測定・カード記載なし。
- **制約**: initial promptを設定すると幻覚・品質劣化(カード警告)。学習データ由来のバイアス: 固有名詞がゲーム内漢字になりやすい、長音/感嘆符/三点リーダーの連続が出力されない、文末「。」がほぼ省略、数字と英字感嘆符が半角、一部卑語に伏せ字「○」。繰り返し幻覚はno_repeat_ngram_size=5〜10で抑制。
- **使う版・派生**: 量子化/変換版: quantumcookie/anime-whisper-ct2(-fp16/-int8)、flyfront/anime-whisper-faster、imeipopo18/anime-whisper-mlx(-q4)、goryodog/anime-whisper-ONNX、NeemaShioSe/Whisper-Anime-ggml。後発のanime系: efwkjn/whisper-ja-anime-v0.3(2025-06-01、2026-09-18更新、ライセンス未設定)。
- **根拠**: [学習データ・CER表(自己報告、5作・75kファイル)・使用注意(initial prompt)・バイアス](https://huggingface.co/litagin/anime-whisper/blob/22e2008a8182b357da3922a6308d095008f72973/README.md) / [第三者ベンチ(litagin/anime-whisperを含む比較、VNゲーム5作)](https://huggingface.co/efwkjn/whisper-ja-anime-v0.3/blob/77edc3f61a06161331b1803252f5987e433dd4a5/BENCH.md) / [ユーザーの評価「非言語・擬音の検出が他を大きく上回る」(2026-03-11)](https://huggingface.co/litagin/anime-whisper/discussions/4) / [後発Qwen3-ASR fine-tuneの自己報告CER(anime-whisperとの比較なし)](https://huggingface.co/jaykwok/Qwen3-ASR-1.7B-JA-Anime-Galgame/blob/6db0efecd56d4a7e0003190a6bd4cac056d0f390/README.md)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `Qwen/Qwen3-ASR-1.7B` — 日本語汎用の最有力(Apache-2.0、DL 30日1,702,288、likes 1,135、歌唱・BGM付き歌も対象)。Xでもwhisperより良いとの投稿多数。演技セリフの非言語発話は未評価。
- **次点**: `jaykwok/Qwen3-ASR-1.7B-JA-Anime-Galgame`（同データでの最新fine-tune(CER 0.1285、base 0.1437、自己報告・800クリップ)。anime-whisperとの比較が無く、DL 30日8,845・likes 1と採用が小さく、ライセンスはmetadata「other」。-hf版(Apache-2.0)は DL 3,001。） / `efwkjn/whisper-ja-anime-v0.3`（turbo+日本語トークナイザのfull fine-tune、長尺に強いとの自己記述。DL累計23,427、likes 11、ライセンス未設定、faster-whisperで語彙差異に注意書き。）

関連リポジトリ:

- [litagin02/anime-whisper](https://github.com/litagin02/anime-whisper) — anime-whisperの評価・観察レポート置き場(READMEは評価コード公開予定と記載)（★49 / ライセンス未表示 / 最終push 2024-11-12 / 確認コミット [`5065987c`](https://github.com/litagin02/anime-whisper/blob/5065987cd1e9d8debad05f452d96aae52f5a92cc/README.md)）
  - ★49、ライセンス未設定、最終push 2024-11-12(停滞)。
- [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) — Whisper系(CTranslate2変換版anime-whisper含む)の高速推論（★25,668 / MIT / 最終push 2026-10-01 / release v1.2.1 (2025-10-31) / 確認コミット [`2ce7f9d7`](https://github.com/SYSTRAN/faster-whisper/blob/2ce7f9d7a9fbe315a5804a33bf7224d42e101174/README.md)）
  - ★25,643、MIT、2026-09-30更新。
- [QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) — Qwen3-ASR推論・fine-tuningツールキット(Qwen3-ASR系anime fine-tuneの実行基盤)（★3,633 / Apache-2.0 / 最終push 2026-06-26 / 確認コミット [`7c6daf77`](https://github.com/QwenLM/Qwen3-ASR/blob/7c6daf77a2421100f5fb066495372c00129d39ff/README.md)）
  - ★3,630、Apache-2.0、Fine Tuning手順付き。
- [m-bain/whisperX](https://github.com/m-bain/whisperX) — Whisper系の単語レベルタイムスタンプ・話者分離パイプライン（★24,332 / BSD-2-Clause / 最終push 2026-09-26 / release v3.8.6 (2026-05-25) / 確認コミット [`771b4a14`](https://github.com/m-bain/whisperX/blob/771b4a14a9486f8fd5aef18ef49e35d639523dd3/README.md)）
  - ★24,318、BSD-2-Clause、2026-09-26更新。anime-whisperはタイムスタンプが標準出力に無いため補助に使う(Discussion #3参照)。

### 音声認識(強制アライメント・字幕タイムスタンプ付与)

<a id="automatic-speech-recognition--forced-alignment-subtitling"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [Qwen/Qwen3-ForcedAligner-0.6B](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B/tree/c7cbfc2048c462b0d63a45797104fc9db3ad62b7)（revision `c7cbfc20` / 作成 2026-01-28 / 更新 2026-01-30）
- **利用条件**: apache-2.0。メタデータ・カードともApache-2.0。商用可とは断定しない(依存データ・トークナイザ条件は未精査)。
- **選定根拠**: 【事実】アニメ特化の強制アライメントモデルは見つからず(日本語phoneme CTCのprj-beatrice/japanese-hubert-base-phoneme-ctc-v4は汎用)。汎用最有力は Qwen/Qwen3-ForcedAligner-0.6B: DL 30日404,713/累計3,151,906、likes 163、spaces 40、Apache-2.0、日本語を含む11言語、最大5分の音声で任意単位のタイムスタンプ(カード記載)。Qwen3-ASRと同梱の推論ツールキットがforced_alignerを標準サポート。MahmoudAshraf/mms-300m-1130-forced-aligner(DL 2.69M、likes 104)は多言語CTC方式の旧来標準。【評価】採用・ライセンス・保守で優位。anime-whisperの出力(タイムスタンプ無し)に後段で時刻付与する用途に向く。【疑い】アニメ演技(叫び、吐息、重なり発話)でのアライメント精度は未検証、カードの精度主張はE2E系との比較で自己報告。
- **指標（確認日時点）**: DL累計 3,165,766 / 直近30日 407,745 / likes 163 / Spaces 40
- **概要**: Qwen3-ASRファミリーの非自己回帰強制アライメントモデル(0.6B)。音声+書き起こしテキストから任意単位(語/文字など)のタイムスタンプを予測、最大5分・11言語。
- **入力**: 音声+書き起こしテキスト
- **出力**: 単位ごとの開始・終了時刻
- **必要環境**: 公式qwen-asrパッケージのforced_aligner引数で利用。vLLM利用時はFlashAttention推奨との記載。VRAM・速度は未測定。
- **制約**: アニメ演技・非言語発話での精度は未評価。最大5分の制約。精度主張はカード自己報告。
- **使う版・派生**: Qwen/Qwen3-ForcedAligner-0.6B-hf(transformers形式、DL 78,813)、GGUF/MLX/4bit変換版多数(OpenASR、cstr、mlx-community、aufklarer)。
- **根拠**: [Apache-2.0、対応11言語(日本語含む)、最大5分、任意単位のタイムスタンプ](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B/blob/c7cbfc2048c462b0d63a45797104fc9db3ad62b7/README.md) / [推論ツールキットでforced_alignerをサポート、Fine Tuning手順](https://github.com/QwenLM/Qwen3-ASR)
- **次点**: `MahmoudAshraf/mms-300m-1130-forced-aligner`（CTC方式の旧来標準(DL 2.69M、likes 104、2024-05)。日本語は表音変換が必要で、新世代のQwen3-ForcedAlignerに対する優位性は未確認。） / `prj-beatrice/japanese-hubert-base-phoneme-ctc-v4`（日本語音素CTC(DL 6,091)。汎用日本語の音素列出力で、単体の字幕用途ではなく前処理向き。）

関連リポジトリ:

- [QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) — Qwen3-ASR/ForcedAligner公式ツールキット（★3,633 / Apache-2.0 / 最終push 2026-06-26 / 確認コミット [`7c6daf77`](https://github.com/QwenLM/Qwen3-ASR/blob/7c6daf77a2421100f5fb066495372c00129d39ff/README.md)）
  - ★3,630、Apache-2.0、forced_aligner統合。
- [MahmoudAshraf97/ctc-forced-aligner](https://github.com/MahmoudAshraf97/ctc-forced-aligner) — CTCベース強制アライメント(代替)（★566 / BSD-2-Clause / 最終push 2026-09-07 / release v0.2 (2024-06-03) / 確認コミット [`64293cc6`](https://github.com/MahmoudAshraf97/ctc-forced-aligner/blob/64293cc6d711e57666c4a8b098e9fd93b381fd88/README.md)）
  - ★566、BSD-2-Clause、2026-09-07更新。
- [m-bain/whisperX](https://github.com/m-bain/whisperX) — Whisper+wav2vec2アライメント+話者分離パイプライン（★24,332 / BSD-2-Clause / 最終push 2026-09-26 / release v3.8.6 (2026-05-25) / 確認コミット [`771b4a14`](https://github.com/m-bain/whisperX/blob/771b4a14a9486f8fd5aef18ef49e35d639523dd3/README.md)）
  - ★24,318、BSD-2-Clause、最新v3.8.6(2026-05-25)。

### 音声変換(キャラ声への変換・歌声変換。RVC/Seed-VC系)

<a id="audio-to-audio--voice-conversion"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [lj1995/VoiceConversionWebUI](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/e6d0c1a17da07c33557852f9dfa2bd44cc75737d)（revision `e6d0c1a1` / 作成 2023-01-12 / 更新 2026-08-01）
- **利用条件**: mit。メタデータMIT。学習に使う声(声優・ゲーム音声)の権利・本人同意は利用者責任。商用可とは断定しない。
- **選定根拠**: 【事実】アニメ特化の汎用声質変換モデルは見つからず(HF上のアニメキャラRVCモデルは個別キャラの重みで、ArkanDash/rvc-genshin-impact likes 246など。基盤は汎用)。汎用最有力はRVC: HFのlj1995/VoiceConversionWebUI likes 1,222・spaces 100・Discussion 138、GitHub RVC-Project ★38,620(MIT)、最新リリース2.3.260718(2026-07-21)、2026-08-04更新と保守継続。対抗のPlachta/Seed-VC(GPL-3.0、HF likes 94・spaces 98、GitHub ★3,892)はゼロショット(1〜30秒参照)・歌声変換対応だが最終push 2025-04-20と停滞。IAHispano/Applio(MIT、★3,773、2026-09-29更新、3.6.5)はRVC系の活発なフォーク。【評価】キャラごとに学習するRVCの資産(ボイスモデル交換文化、ComfyUI/VST等)が最大のため選ぶ。【疑い】lj1995/VoiceConversionWebUIは事前学習モデルと実行バンドル(7z、ffmpeg.exe、bat)の置き場でモデルカードが空、DLは未集計(0)。声質の客観比較データなし。ゼロショット要件ならSeed-VCが適する。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 1,223 / Spaces 100
- **概要**: RVC(Retrieval-based Voice Conversion)WebUIの配布リポジトリ。hubert_base、事前学習重み、Windows向け実行バンドル(RVC20260718Nvidia.7z等)を含む。
- **入力**: 変換元の音声(+対象話者のRVC重み/index)
- **出力**: 対象話者の声に変換した音声
- **必要環境**: カード空。GitHub RVC-Projectのドキュメントに従う。未測定・未確認。
- **制約**: HFリポジトリにモデルカードなし。7z/exe/bat等の実行バンドルを含むため取得・実行には出所確認が必要(本調査では取得せず)。アニメ特化ではない。
- **使う版・派生**: GitHub: RVC-Project/Retrieval-based-Voice-Conversion-WebUI、フォーク: IAHispano/Applio。ゼロショット代替: Plachta/Seed-VC(GPL-3.0)。
- **根拠**: [メタデータMIT、カード本文は空(ファイル構成からバンドル配布を確認)](https://huggingface.co/lj1995/VoiceConversionWebUI/blob/e6d0c1a17da07c33557852f9dfa2bd44cc75737d/README.md) / [実装本体(★38,620、MIT、2.3.260718)](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
- **次点**: `Plachta/Seed-VC`（ゼロショット・歌声変換対応(README)、HF likes 94。GPL-3.0で最終更新2025-04、個別学習のRVC資産が無い。） / `IAHispano/Applio`（RVC系のフォーク(MIT、3.6.5、2026-09-19)。公式実装の代替UIで、アルゴリズム差は未確認。）

関連リポジトリ:

- [RVC-Project/Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) — RVC本体(学習・推論・WebUI)（★38,552 / MIT / 最終push 2026-08-04 / release 2.3.260718 (2026-07-21) / 確認コミット [`81eed5e8`](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/README.md) / 制作カタログ: [retrieval-based-voice-conversion-webui](../../categories/tts.md#retrieval-based-voice-conversion-webui)）
  - ★38,620、MIT、2.3.260718(2026-07-21)。
- [IAHispano/Applio](https://github.com/IAHispano/Applio) — RVC系の活発なフォーク(UI/プラグイン/学習改善)（★3,778 / MIT / 最終push 2026-09-29 / release 3.6.5 (2026-09-19) / 確認コミット [`c7665ac9`](https://github.com/IAHispano/Applio/blob/c7665ac9a305b3683570ed914f1577d53d4b75c4/README.md)）
  - ★3,773、MIT、3.6.5(2026-09-19)、2026-09-29更新。
- [Plachtaa/seed-vc](https://github.com/Plachtaa/seed-vc) — ゼロショット声質変換/歌声変換（★3,892 / GPL-3.0 / 最終push 2025-04-20 / 確認コミット [`51383efd`](https://github.com/Plachtaa/seed-vc/blob/51383efd921027683c89e5348211d93ff12ac2a8/README.md)）
  - ★3,892、GPL-3.0、最終push 2025-04-20(停滞)。READMEは1〜30秒参照のゼロショットと最小1発話のfine-tuneを記載。

### 音声分離(アニメ映像・音源からの台詞/ボーカル抽出、BGM分離)

<a id="audio-to-audio--stem-separation"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [KimberleyJSN/melbandroformer](https://huggingface.co/KimberleyJSN/melbandroformer/tree/ac9b0614ab3cd7f77219e18ba494dfd93956c348)（revision `ac9b0614` / 作成 2024-08-06 / 更新 2026-04-22）
- **利用条件**: mit。メタデータMIT(2026-04-22更新時点)。Discussion #2で作者が2025-06に「自由に使ってよい」と発言後、GPL-3.0を付与し、2026-04にMIT化の要望あり(メタデータは現在mit)。学習データ・商用利用の明示条件はカードになく、Discussion #4/#5の商用利用質問は未解決。商用可と断定しない。
- **選定根拠**: 【事実】アニメ映像の台詞・BGM分離に特化した公開モデルは見つからず。汎用ではMel-Band RoFormer系がボーカル分離の実用標準で、KimberleyJSN/melbandroformer(likes 35、spaces 4)をKijaiがComfyUI向けsafetensors化したKijai/MelBandRoFormer_comfy(DL 30日48,020/累計878,199)が実利用の中心、コード参照"MelBandRoformer"1,912件。ZFTurbo/Music-Source-Separation-Training(★1,566、MIT、v1.0.22 2026-08-27)が学習/推論基盤。demucs(facebookresearch)は2024-04で更新停止・archived。【評価】原著者重みを採る(Kijai版は変換派生)。【疑い】元リポジトリは2025-06にGPL-3.0を追加、2026-04-19にMIT変更の要望が出て、メタデータは2026-04-22更新時点でmit(最初は無ライセンスで、許可発言のみだった)と経緯が不安定。商用利用Discussion(#4,#5)は未解決。SDR等の比較データは本調査で未取得、TV/アニメ音声(BGM+SE+台詞)での性能は未評価。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 34 / Spaces 4
- **概要**: Mel-Band RoFormerのボーカル分離チェックポイント(MelBandRoformer.ckpt)。ボーカル/伴奏の2ステム分離。
- **入力**: 音楽/混合音声
- **出力**: ボーカル+伴奏(インストゥルメンタル)
- **必要環境**: カードはYAML frontmatter(license: mit)のみ。学習/推論はZFTurbo/Music-Source-Separation-Trainingのmel_band_roformer設定。未測定。
- **制約**: 音楽向けに作られた重みで、アニメ音声(台詞+SE+BGM重なり)への適性は未評価。ライセンス経緯が不明瞭(Discussion #1,#2,#4,#5)。
- **使う版・派生**: Kijai/MelBandRoFormer_comfy(fp16/fp32 safetensors、ComfyUI-MelBandRoFormer用、DL累計878,199)。派生: pcunwa/Mel-Band-Roformer-big、becruily/mel-band-roformer-deux(CC-BY-NC)、anvuew/dereverb_mel_band_roformer(GPL-3.0、残響除去)。
- **根拠**: [license: mitのみ(本文なし)](https://huggingface.co/KimberleyJSN/melbandroformer/blob/ac9b0614ab3cd7f77219e18ba494dfd93956c348/README.md) / [ライセンス経緯(許可発言→GPL-3.0→MIT化要望)](https://huggingface.co/KimberleyJSN/melbandroformer/discussions/2) / [ComfyUI向けsafetensors版(元モデルのSafetensors版と記載)](https://huggingface.co/Kijai/MelBandRoFormer_comfy/blob/7dc5fa7824f1f3089a5c4b130d767004ccc1ed12/README.md)
- **次点**: `Kijai/MelBandRoFormer_comfy`（変換派生。ComfyUI実利用は最大(DL累計878,199)だがライセンス未設定・元の経緯を継承。ComfyUI運用ならこちらを使うのが実務的。） / `becruily/mel-band-roformer-deux`（likes 41の派生・改良重みだがCC-BY-NC-4.0で非商用。）

関連リポジトリ:

- [ZFTurbo/Music-Source-Separation-Training](https://github.com/ZFTurbo/Music-Source-Separation-Training) — RoFormer系分離モデルの学習・推論フレームワーク（★1,567 / MIT / 最終push 2026-09-26 / release v1.0.22 (2026-08-27) / 確認コミット [`84b1eac0`](https://github.com/ZFTurbo/Music-Source-Separation-Training/blob/84b1eac0887756b4f1a9d7a1ff49105939749ed2/README.md)）
  - ★1,566、MIT、v1.0.22(2026-08-27)、2026-09-26更新。mel_band_roformer/bs_roformer等に対応。
- [nomadkaraoke/python-audio-separator](https://github.com/nomadkaraoke/python-audio-separator) — 分離モデル(MDX/Roformer等)をCLI/ライブラリで実行（★1,396 / MIT / 最終push 2026-08-27 / release v0.47.0 (2026-08-27) / 確認コミット [`bf1164aa`](https://github.com/nomadkaraoke/python-audio-separator/blob/bf1164aa0f1ee1d1d0ef0f09b315f7659fc06bab/README.md)）
  - ★1,391、MIT、v0.47.0(2026-08-27)。
- [kijai/ComfyUI-MelBandRoFormer](https://github.com/kijai/ComfyUI-MelBandRoFormer) — ComfyUIノード(Mel-Band RoFormer)（★257 / ライセンス未表示 / 最終push 2026-01-30 / 確認コミット [`92c86854`](https://github.com/kijai/ComfyUI-MelBandRoFormer/blob/92c86854e6654f4aacc97484471af95c98ea16d4/README.md)）
  - ★257、ライセンス未設定、2026-01-30停滞。ComfyUI運用の実装基盤。

### 音声変換(ニューラル音声コーデック/デコーダ: Llasa系TTS用・44.1kHz化)

<a id="audio-to-audio--speech-codec"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [NandemoGHS/Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2/tree/58a5080a103abd861052b323279ccabb2333b636)（revision `58a5080a` / 作成 2025-10-27 / 更新 2025-10-28）
- **利用条件**: cc-by-nc-4.0。メタデータ・カードともCC-BY-NC-4.0(非商用)。学習に使った約22,000時間の日本語データの出所・権利はカードに記載なし。商用不可。
- **選定根拠**: 【事実】アニメ/ゲーム調日本語音声向けの公開コーデックとして NandemoGHS/Anime-XCodec2-44.1kHz-v2 がある(約22,000時間の日本語データでデコーダのみfine-tune、エンコーダ/コードブック固定でXCodec2トークン互換、16kHz入力→44.1kHz出力)。DL 30日1,153/累計27,011、likes 14、CC-BY-NC-4.0、2025-10-27。Anime-Llasa-3B系のTTSを44.1kHzで使うための用途特化で、他用途の採用は限定的。【比較】Aratako/MioCodec-25Hz-44.1kHz-v2(MIT、DL 30日486,900/累計746,988、likes 14、2026-02-14)は採用規模で圧倒的(25Hz/341bps、133M、カード記載)だが、カードにアニメ特化の記載はない(Aratako製の汎用コーデック)。Irodori系はSemantic-DACVAE-Japanese-32dim(MIT)を使用。【評価】アニメ特化の選択としてはこれだが、CC-BY-NC・Llasa依存のため、新規開発ではMioCodec/DACVAE系(MIT)が現実的。【疑い】再構成品質の客観指標はカードになし(超解像用途は未評価と明記)、カスタムxcodec2ライブラリ(v0.1.7以上)必須。
- **指標（確認日時点）**: DL累計 27,038 / 直近30日 1,136 / likes 14 / Spaces 2
- **概要**: Anime-XCodec2(XCodec2のアニメ/ゲーム調日本語fine-tune)の44.1kHz版v2。UpSamplerBlockとRMS lossをデコーダに追加し、44.1kHzの日本語音声を再構成。
- **入力**: 16kHz音声(またはXCodec2トークン)
- **出力**: 44.1kHz波形
- **必要環境**: カスタムxcodec2ライブラリ(v0.1.7以上、リポジトリ同梱のtar.gz)必須。標準ライブラリ・0.1.6では動作しない(カード)。VRAM未測定。
- **制約**: デコーダのみ更新でトークンはXCodec2と同一。超解像用途は未評価(カード明記)。再構成指標の記載なし。CC-BY-NC。
- **使う版・派生**: 元: NandemoGHS/Anime-XCodec2(16kHz)、44.1kHz v1: NandemoGHS/Anime-XCodec2-44.1kHz。GGUFデコーダ: telecomadm1145/Anime-XCodec2-44.1kHz-v2-decoder-gguf。
- **根拠**: [44.1kHz v2の内容(デコーダのみfine-tune、トークン互換、約22,000時間、カスタムライブラリ必須、超解像は未評価)](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2/blob/58a5080a103abd861052b323279ccabb2333b636/README.md)
- **次点**: `Aratako/MioCodec-25Hz-44.1kHz-v2`（MIT・DL 30日486,900で採用は桁違い。25Hzトークン/44.1kHz出力で軽量(133M、カード)だがアニメ特化の記載はない。新規開発ではこちらが現実的。） / `Aratako/Semantic-DACVAE-Japanese-32dim`（Irodori系が使うMITの日本語DACVAE(spaces 32)。TTS内蔵で単体のコーデック用途は想定されていない。）

### 音声分類(アニメ/ガルゲ調セリフの感情分類)

<a id="audio-classification--speech-emotion"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [litagin/anime_speech_emotion_classification](https://huggingface.co/litagin/anime_speech_emotion_classification/tree/6b94a022f4ee2aa4d67bfcb9c670cef8b5ac7833)（revision `6b94a022` / 作成 2025-04-01 / 更新 2025-06-28）
- **利用条件**: mit。メタデータMIT。学習データのGalgame_Speech_SER_16kHz(ゲーム音声)の権利はカードに記載なし。商用可と断定しない。
- **選定根拠**: 【事実】litagin/anime_speech_emotion_classification: litagin/Galgame_Speech_SER_16kHzで学習した感情分類(Angry/Disgusted/Embarrassed/Fearful/Happy/Sad/Surprised/Neutral+Sexual1/Sexual2の10クラス)。DL 30日154/累計5,267、likes 6、MIT、2025-04-01。アニメ/ゲーム調の演技音声に対応する公開感情分類は他に見つからない(日本語汎用のBagus/wav2vec2-xlsr-japanese-speech-emotion-recognitionはDL 30日1,997だがアニメ特化でない)。【評価】他に選択肢が無いため採用。【疑い】カードに精度・混同行列・ベンチが無く品質は不明、Sexual1/2クラス(喘ぎ/咀嚼音)を含む。採用規模も小さい。
- **指標（確認日時点）**: DL累計 5,276 / 直近30日 158 / likes 6 / Spaces 0
- **概要**: ガルゲ音声データで学習した音声感情分類モデル(10クラス、カスタムコード使用)。
- **入力**: 16kHz音声
- **出力**: 感情ラベルとスコア(Angry, Disgusted, Embarrassed, Fearful, Happy, Sad, Surprised, Neutral, Sexual1, Sexual2)
- **必要環境**: transformers pipeline(trust_remote_code=True)。VRAM等は未記載・未測定。
- **制約**: 精度指標なし。クラスにNSFW音声(Sexual1=喘ぎ、Sexual2=口淫SE)を含む。学習データはゲーム音声でドメイン外に弱い可能性。
- **使う版・派生**: safetensorsのみ(model.safetensors、modeling.py等)。
- **根拠**: [学習データ、ラベル一覧(Sexual1/Sexual2を含む)、使用方法。精度指標の記載なし](https://huggingface.co/litagin/anime_speech_emotion_classification/blob/6b94a022f4ee2aa4d67bfcb9c670cef8b5ac7833/README.md)
- **次点**: `Bagus/wav2vec2-xlsr-japanese-speech-emotion-recognition`（日本語汎用の感情認識(2022、DL 30日1,997)。アニメ演技音声への適性は未確認。）

### 音声分類(アニメ/ガルゲ声優・キャラ話者埋め込み)

<a id="audio-classification--speaker-embedding"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [litagin/anime_speaker_embedding_ecapa_tdnn_groupnorm](https://huggingface.co/litagin/anime_speaker_embedding_ecapa_tdnn_groupnorm/tree/a2c81c47ee0b9fbfb744ad49849625645867129d)（revision `a2c81c47` / 作成 2025-05-17 / 更新 2025-06-22）
- **利用条件**: mit。メタデータMIT。学習データ(OOPPEENN/VisualNovel_Dataset、ゲーム音声)の権利はカードに明記なし。NSFWな発声が含まれる。商用可と断定しない。
- **選定根拠**: 【事実】litagin/anime_speaker_embedding_ecapa_tdnn_groupnorm(char版。声優版はby_va版): SpeechBrain ECAPA-TDNNのBatchNormをGroupNormに置換しVNデータセット(695万ファイル、7,357キャラ)で学習。VA版は989人の声優、自己報告EER 0.41%(Macro F1 96.80%)。カードはspeechbrain/spkrec-ecapa-voxceleb、pyannote/wespeaker-voxceleb-resnet34-LM、Resemblyzerとのt-SNE比較(学習外の4ゲーム)で「他モデルでは区別できない非言語発話・演技音声を分離できる」と主張(自己報告・定性比較のみ)。MIT、pip install anime_speaker_embedding、GitHub litagin02/anime_speaker_embedding ★23。HFのDLは.pth配布のため0(未集計)、likes 9。アニメ特化の話者埋め込みは他に見つからない。【評価】キャラ/声優クラスタリングや声優別データ分割に有用。【疑い】定量比較(EER等)は自己報告でVA版の内部valid、学習データはOOPPEENN/VisualNovel_Datasetで権利・内容(NSFW含む)が不透明。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 9 / Spaces 0
- **概要**: アニメ/VN向け話者埋め込み(192次元、ECAPA-TDNN+GroupNorm、char版)。同じ声優でもキャラが違えば別話者として学習。VA版は声優単位で埋め込みが集約される。
- **入力**: 日本語アニメ/ゲーム調音声ファイル
- **出力**: 192次元の話者埋め込み(numpy)
- **必要環境**: pip install anime_speaker_embedding(PyTorch)。GPU/CPU。VRAM未測定。
- **制約**: char版は同一話者でもコサイン類似度が低め(カード注意)。学習スクリプトは非公開(公開予定と記載)。fbank前のx*32768スケーリングなど互換性の癖を作者自身が注記。
- **使う版・派生**: VA版: litagin/anime_speaker_embedding_by_va_ecapa_tdnn_groupnorm(likes 4、同日付v0.2.0)。重みはembedding_model.pth。
- **根拠**: [学習データ規模(6,959,970ファイル、7,357キャラ)、VA版EER 0.41%(自己報告)、他モデルとの定性比較](https://huggingface.co/litagin/anime_speaker_embedding_ecapa_tdnn_groupnorm/blob/a2c81c47ee0b9fbfb744ad49849625645867129d/README.md) / [利用ライブラリ(MIT、★23、2025-06-22)](https://github.com/litagin02/anime_speaker_embedding)
- **次点**: `litagin/anime_speaker_embedding_by_va_ecapa_tdnn_groupnorm`（同系の声優単位版(likes 4)。キャラ間の区別より声優の一貫性を重視する用途ではこちらを使う。） / `speechbrain/spkrec-ecapa-voxceleb`（汎用話者埋め込みの標準。アニメ演技・非言語発話は区別できないとカードが比較で主張(自己報告)。）

関連リポジトリ:

- [litagin02/anime_speaker_embedding](https://github.com/litagin02/anime_speaker_embedding) — 話者埋め込み推論ライブラリ(pip)（★23 / MIT / 最終push 2025-06-22 / 確認コミット [`cd3eb24b`](https://github.com/litagin02/anime_speaker_embedding/blob/cd3eb24b6891471372c627d544c07f71a896718c/README.md)）
  - ★23、MIT、2025-06-22。VA/charの2バリアントを提供。

### 音声分類(アニメ調らしさスコア・TTS/声質の評価用)

<a id="audio-classification--anime-likeness-scoring"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [spellbrush/animescore](https://huggingface.co/spellbrush/animescore/tree/eb34860d55a0f696d46ce7383b9b3350f171e504)（revision `eb34860d` / 作成 2026-06-12 / 更新 2026-06-12）
- **利用条件**: mit。メタデータ・カードともMIT。学習に用いた音声データの権利はカードに記載なし。商用可と断定しない。
- **選定根拠**: 【事実】spellbrush/animescore: 音声の「アニメらしさ」を1つのスカラー値で返すスコアラ。論文「AnimeScore: A Preference-Based Dataset and Framework for Evaluating Anime-Like Speech Style」(Interspeech 2026、arXiv 2603.11482)の公式モデル。HuBERT系ヘッド(約9MB)、自己報告でペア比較精度82.4%・AUC 0.908(評価したバックボーンで最良)。MIT、デモSpaceあり、2026-06-12。DL 30日31/累計165、likes 7、spaces 1、GitHub sizigi/animescore ★12と採用は小さいが、アニメ調TTS(Irodori-TTS-Anime等)の出力評価に使える唯一の公開スコアラ。【評価】TTS評価の補助指標として採用価値あり。【疑い】採用はごく小規模、ペア比較データは論文内の自己報告、絶対スコアの閾値は未定義。trust_remote_code=Trueが必要。
- **指標（確認日時点）**: DL累計 165 / 直近30日 31 / likes 7 / Spaces 1
- **概要**: HuBERTベースのアニメ調音声スコアラ(ヘッド重みのみ約9MB)。スコア差の sigmoid でペア比較確率が得られる。
- **入力**: 音声(モノラル、16kHzに再サンプル)
- **出力**: スカラースコア(高いほどアニメ調)
- **必要環境**: PyTorch+transformers(trust_remote_code=True)、requirements.txt同梱。GPU/CPU。未測定。
- **制約**: 評価データ・学習データの詳細は論文参照。絶対値の解釈は不明。採用・検証事例が少ない。
- **使う版・派生**: safetensorsヘッドのみ(model.safetensors)。バックボーンHuBERTは別途ダウンロード。
- **根拠**: [ペア比較精度82.4%・AUC 0.908(自己報告)、使い方、Interspeech 2026引用](https://huggingface.co/spellbrush/animescore/blob/eb34860d55a0f696d46ce7383b9b3350f171e504/README.md) / [論文(AnimeScore、arXiv)](https://arxiv.org/abs/2603.11482)

関連リポジトリ:

- [sizigi/animescore](https://github.com/sizigi/animescore) — AnimeScoreの論文公式コード/推論CLI（★12 / ライセンス未表示 / 最終push 2026-09-27 / 確認コミット [`3e80a3c7`](https://github.com/sizigi/animescore/blob/3e80a3c723b06b4e238c67af2411b5656866a57a/README.md)）
  - ★12、2026-09-27更新、ライセンス未設定(HFカードはMIT)。

### 音声区間検出(アニメ/ガルゲ音声データの切り出し・ASR前処理)

<a id="voice-activity-detection--vad-for-dataset-slicing"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [onnx-community/silero-vad](https://huggingface.co/onnx-community/silero-vad/tree/e71cae966052b992a7eca6b17738916ce0eca4ec)（revision `e71cae96` / 作成 2024-07-02 / 更新 2024-12-15）
- **利用条件**: mit。HFメタデータMIT(ONNX派生・LICENSEファイルあり)、GitHub公式もMIT(READMEで縛りなしと明記)。学習データの詳細はHFカードにない。
- **選定根拠**: 【事実】アニメ特化のVADは見つからず。汎用の実績標準は Silero VAD(GitHub snakers4/silero-vad ★10,332、MIT、v6.2.3を2026-09-23公開、1音声チャンク30ms+を単一CPUスレッド1ms未満、6000言語超で学習と主張)。ガルゲ/VNデータセット作成ツールStyle-Bert-VITS2のslice.pyがsilero-vad(litagin02/silero-vadフォーク)を使うことをコードで確認。HF上の公式リポジトリは無く、onnx-community/silero-vad(MIT、likes 47、spaces 12)をHF代表として掲載(DLは未集計0)。対抗のpyannote/segmentation-3.0は likes 2,041・DL 30日5.4M・累計400M・MITだがgated(auto)で、主用途は話者分離のセグメンテーション。NVIDIAのNemotron-3-Diarization(2026-09-01、likes 549)は新しく話者分離向け。【評価】軽量・permissive・データ切り出し用途の実績でSilero。【疑い】アニメ演技音声の吐息・笑い・ささやきでの欠落率は未検証、BGM重畳時の挙動も未評価。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 46 / Spaces 12
- **概要**: Silero VADのONNX変換(onnx-community、カード本文なし、YAMLメタデータのみ。バージョンは未確認)。音声/非音声を短いチャンク単位で判定する軽量VAD(公式実装はGitHub snakers4/silero-vad)。
- **入力**: 8kHz/16kHz音声
- **出力**: 音声区間確率(フレーム単位)→区間リスト
- **必要環境**: CPU 1スレッド1ms未満/チャンク(公式README自己報告)。未測定。
- **制約**: カード本文なく、元Silero VADのどのバージョンか未確認。アニメ演技音声(吐息・笑い・囁き)での検出漏れは未評価。公式HF重みがなく、HF版はONNX変換派生(onnx-community)。
- **使う版・派生**: onnx/model.onnx(fp32)、model_fp16、model_int8、model_uint8、model_quantized、model_q4、model_q4f16、model_bnb4。公式: GitHub snakers4/silero-vad(PyPI silero-vad、torch.hub)。ほかのHF派生: FluidInference/silero-vad-coreml、aufklarer/Silero-VAD-v5-MLX、istupakov/silero-vad-onnx、deepghs/silero-vad-onnx。
- **根拠**: [メタデータのみ(license: mit、pipeline_tag: voice-activity-detection)でカード本文なし。ONNXファイル一覧(model.onnx、int8/fp16/q4等の量子化版)](https://huggingface.co/onnx-community/silero-vad/blob/e71cae966052b992a7eca6b17738916ce0eca4ec/README.md) / [公式実装(★10,332、MIT、v6.2.3)](https://github.com/snakers4/silero-vad)
- **次点**: `pyannote/segmentation-3.0`（likes 2,041・DL 30日5.4Mと最大採用、MITだがgated(auto)で話者セグメンテーション用途が中心。モデルカードは未閲覧(gated)。） / `FireRedTeam/FireRedVAD`（2026-02-11公開、Apache-2.0、likes 66、DL累計14,329。新しく、日本語アニメでの検証材料が無い。）

関連リポジトリ:

- [snakers4/silero-vad](https://github.com/snakers4/silero-vad) — Silero VAD公式実装(PyTorch/ONNX、PyPI配布)（★10,338 / MIT / 最終push 2026-09-29 / release v6.2.3 (2026-09-23) / 確認コミット [`1e261b03`](https://github.com/snakers4/silero-vad/blob/1e261b036686cd0017d500ee96acd1c4ba572a9d/README.md)）
  - ★10,332、MIT、v6.2.3(2026-09-23)。Style-Bert-VITS2のslice.pyが使用。
- [pyannote/pyannote-audio](https://github.com/pyannote/pyannote-audio) — VAD/話者分離パイプライン(代替)（★10,611 / MIT / 最終push 2026-09-24 / release 4.0.7 (2026-06-30) / 確認コミット [`b749285c`](https://github.com/pyannote/pyannote-audio/blob/b749285c5cdd4636b2edc7f766f1352c8dde9369/README.md)）
  - ★10,607、MIT、4.0.7(2026-06-30)。

### 音声区間検出(話者分離・キャラ別発話割当て)

<a id="voice-activity-detection--speaker-diarization"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [pyannote/speaker-diarization-community-1](https://huggingface.co/pyannote/speaker-diarization-community-1/tree/3533c8cf8e369892e6b79ff1bf80f7b0286a54ee)（revision `3533c8cf` / 作成 2025-04-15 / 更新 2025-09-29）
- **利用条件**: cc-by-4.0 / gated。メタデータ・カードともCC-BY-4.0(帰属表示が必要)。gated(auto)でHF利用条件の承認が必要。学習データ由来の制約はカードに要確認。商用可と断定しない。
- **選定根拠**: 【事実】アニメ特化の話者分離モデルは見つからず。汎用のpyannote/speaker-diarization-community-1(CC-BY-4.0、gated(auto)、DL 30日5,462,903/累計31,718,971、likes 2,329、spaces 49)を採る。カード(公開ミラーpyannote-community/...で閲覧、公式はgated)は自己報告DERでAMI(IHM)17.0%(3.1系は18.8%)、AliMeeting 20.3%(24.5%)、DIHARD 3 20.2%(21.4%)など旧3.1比で改善と記載(会議/通話系データ)。新興の nvidia/Nemotron-3-Diarization(2026-09-01、openmdw-1.1、非gated、likes 549、DL 30日36,386、最大8話者・ストリーミング対応)は有望だが公開1か月で実績少、最大8話者制限あり。【評価】実績・ライセンス・パイプライン完備でpyannote。アニメでは登場人物が多く重なり発話・BGMがあるため、キャラ別の割当てには litagin/anime_speaker_embedding(キャラ/声優の埋め込み)でクラスタリングを併用する方が現実的と推定[INFERENCE]。【疑い】アニメ音声での精度は未評価、最新版のカード本文は公式リポジトリがgatedで直接確認できていない(ミラーで代替)。
- **指標（確認日時点）**: DL累計 31,926,751 / 直近30日 5,503,362 / likes 2,382 / Spaces 49
- **概要**: pyannoteの話者分離パイプライン(community-1)。16kHzモノラルを入力に、話者分離と話者カウントを出力(3.1より改善)。exclusive speaker diarization(ASRタイムスタンプとの突合せ用)を提供。
- **入力**: 音声(モノラル16kHzへ自動変換)
- **出力**: 話者ごとの発話区間(RTTM相当)
- **必要環境**: pyannote.audioをインストールしHF利用条件への同意とトークンが必要(gated)。VRAM・速度は未測定。
- **制約**: HFの利用条件同意が必要(gated)。アニメ音声(BGM、重なり発話、非言語発話)での精度は未評価。DERは会議・通話系ベンチの自己報告。
- **使う版・派生**: 公開ミラー: pyannote-community/speaker-diarization-community-1(非gated、DL 30日136,075)。旧: pyannote/speaker-diarization-3.1(likes 4,013)。有償: precision-2/クラウド。
- **根拠**: [公式リポジトリはgatedのためカード本文は公開ミラー pyannote-community/speaker-diarization-community-1(revision 8a527374977391da736e0daaef26855d949d9685)で確認。DER表は自己報告、使用方法、CC-BY-4.0](https://huggingface.co/pyannote/speaker-diarization-community-1/blob/3533c8cf8e369892e6b79ff1bf80f7b0286a54ee/README.md) / [ミラー側のカード本文(閲覧可能な写し)](https://huggingface.co/pyannote-community/speaker-diarization-community-1/blob/8a527374977391da736e0daaef26855d949d9685/README.md)
- **次点**: `nvidia/Nemotron-3-Diarization`（2026-09-01公開、openmdw-1.1、非gated、likes 549。最大8話者の制限あり、公開1か月で採用実績が少なく、アニメでの評価もない。ストリーミング用途では有力。） / `litagin/anime_speaker_embedding_by_va_ecapa_tdnn_groupnorm`（話者分離パイプラインではなくアニメ向け埋め込み(キャラ/声優クラスタリング用)。併用を推奨(推定)。）

関連リポジトリ:

- [pyannote/pyannote-audio](https://github.com/pyannote/pyannote-audio) — 話者分離/VAD/埋め込みのツールキット（★10,611 / MIT / 最終push 2026-09-24 / release 4.0.7 (2026-06-30) / 確認コミット [`b749285c`](https://github.com/pyannote/pyannote-audio/blob/b749285c5cdd4636b2edc7f766f1352c8dde9369/README.md)）
  - ★10,607、MIT、4.0.7(2026-06-30)、2026-09-24更新。
- [NVIDIA/NeMo-Speech.cpp](https://github.com/NVIDIA/NeMo-Speech.cpp) — Nemotron-3-Diarization向けC++推論ランタイム(代替)（★153 / Apache-2.0 / 最終push 2026-10-01 / release v0.1.0 (2026-08-19) / 確認コミット [`4c101bc7`](https://github.com/NVIDIA/NeMo-Speech.cpp/blob/4c101bc7113f49101a3e11d2c994c519f41939f6/README.md)）
  - ★147、Apache-2.0、v0.1.0(2026-08-19)、2026-09-30更新。

### 音声+テキスト→テキスト(アニメ/ゲーム調セリフの感情・話者特徴キャプション生成、TTS学習用注釈)

<a id="audio-text-to-text--anime-speech-captioning"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [NandemoGHS/Anime-Speech-Japanese-Captioner](https://huggingface.co/NandemoGHS/Anime-Speech-Japanese-Captioner/tree/07433a522b1435b1bd88ff24c2527bc6c715616b)（revision `07433a52` / 作成 2025-11-03 / 更新 2025-11-03）
- **利用条件**: cc-by-nc-4.0。メタデータ・カードともCC-BY-NC-4.0(非商用)。学習データ(Galgame_Gemini_Captions)はGemini 2.5 Pro生成でGeminiと競合する用途の禁止条件があり、元はゲーム音声(日本の著作権法上の学習利用を主張)。商用不可。
- **選定根拠**: 【事実】アニメ/ゲーム調の日本語音声に特化した音声LLMは NandemoGHS/Anime-Speech-Japanese-Captioner(Qwen3-Omni-30B-A3B-Captionerをfine-tune、emotion/profile/mood/speed/prosody/pitch_timbre/style/notes/captionを出力)と同作者のAnime-Speech-Japanese-Refiner(音声+元書き起こし→非言語事象入りの修正書き起こし+記述)のみ。Captioner: DL 30日89/累計223、likes 10、CC-BY-NC-4.0、2025-11-03、FP8版あり。Refiner: DL 累計2,209、likes 12。学習データはGemini 2.5 Proが付けたキャプション(NandemoGHS/Galgame_Gemini_Captions、OOPPEENN VNデータのシャッフル済み部分集合、CC-BY-NC・Gemini競合利用禁止)。【評価】TTS学習用キャプション(Irodori系のcaption条件)作成の自前化手段として唯一の専用モデル。汎用代替はQwen/Qwen3-Omni-30B-A3B-Instruct(DL 30日597,430、likes 1,011、licenseメタデータは「other」)。【疑い/注意】カード掲載の出力例が性的内容(喘ぎ声・性的興奮)でデータにR18ゲーム音声を多く含むことが示唆される(adult特化を目的とは記載していないが、出力が性的になりうる)。採用規模が極小、評価指標なし、vLLM開発コミット指定のビルドが必要、30B級で重い。
- **指標（確認日時点）**: DL累計 226 / 直近30日 92 / likes 10 / Spaces 0
- **概要**: Qwen3-Omni-30B-A3B-Captionerをfine-tuneした、日本語アニメ/ゲーム調音声のキャプション生成モデル。感情、話者像、気分、速度、韻律、ピッチ/音色、スタイルを日本語の構造化テキストで返す。
- **入力**: 音声(1クリップ)
- **出力**: 日本語の構造化キャプション(emotion/profile/mood/speed/prosody/pitch_timbre/style/notes/caption)
- **必要環境**: vLLM(記載のテスト済みコミット18961c5…を要ソースビルド、当時最新安定版0.11.0は未対応)。FP8-DYNAMIC版あり。VRAM未測定(30B-A3B)。
- **制約**: 日本語ゲーム/アニメ調以外(他言語、会議・雑談)は性能が期待できない(カード明記)。出力例は性的内容を含む。評価指標なし。vLLM開発版が必要。
- **使う版・派生**: Anime-Speech-Japanese-Captioner-FP8-DYNAMIC(同作者、DL 37)。関連: NandemoGHS/Anime-Speech-Japanese-Refiner(+FP8)。
- **根拠**: [用途(日本語アニメ/ゲーム調音声)、学習データ、出力フォーマット、vLLM要件、性能の限界(例出力は性的内容を含む)](https://huggingface.co/NandemoGHS/Anime-Speech-Japanese-Captioner/blob/07433a522b1435b1bd88ff24c2527bc6c715616b/README.md) / [学習データ(Gemini 2.5 Pro生成キャプション、CC-BY-NC、競合利用禁止、OOPPEENN部分集合)](https://huggingface.co/datasets/NandemoGHS/Galgame_Gemini_Captions)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `Qwen/Qwen3-Omni-30B-A3B-Instruct` — 汎用の音声理解LLM(DL 30日597,430、累計10,132,444、likes 1,011、license「other」)。アニメ特化ではないが採用・保守が桁違い。
- **次点**: `NandemoGHS/Anime-Speech-Japanese-Refiner`（音声+元書き起こしを入力に、非言語事象入りの修正書き起こしと記述を出す姉妹モデル(likes 12、累計2,209、CC-BY-NC)。キャプション単体ならCaptionerで足りる。）

関連リポジトリ:

- [QwenLM/Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) — Qwen3-Omni公式(Captioner/Refinerのベースモデル)（★4,037 / Apache-2.0 / 最終push 2026-04-23 / 確認コミット [`e4235853`](https://github.com/QwenLM/Qwen3-Omni/blob/e4235853125589c789f06a2dd83e9f4126df5e9d/README.md)）
  - ★4,035、Apache-2.0。
- [modelscope/ms-swift](https://github.com/modelscope/ms-swift) — Captioner/Refinerの学習に使われたfine-tuningフレームワーク(カード記載)（★15,767 / Apache-2.0 / 最終push 2026-10-01 / release v4.5.3 (2026-09-08) / 確認コミット [`02baac98`](https://github.com/modelscope/ms-swift/blob/02baac9832ba12cd24144266ac2ea7020ad0e4b8/README.md)）
  - ★15,761、Apache-2.0、v4.5.3(2026-09-08)、2026-09-30更新。
