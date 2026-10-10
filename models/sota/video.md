# 動画のアニメ系SOTA（2026-10-01）

[一覧へ](../anime-task-sota.md) · [リポジトリ全体像](../anime-repositories.md) · [正本JSON](../../sota-catalog.json)

選定基準・注意は[一覧ページ](../anime-task-sota.md)。各項目の「最良」は確度付きの編集判断で、重み取得・推論実行は未実施。

### テキストから動画生成(アニメ)

<a id="text-to-video"></a>
- **判定**: アニメ特化の最良 / 確度 低
- **最良**: [aidealab/AnimeGen-T2V](https://huggingface.co/aidealab/AnimeGen-T2V/tree/ea04305bca418d988e4924a92a1e8ff67cb29a68)（revision `ea04305b` / 作成 2026-06-17 / 更新 2026-06-29）
- **利用条件**: apache-2.0。HFメタデータ・LICENSEファイルともApache-2.0。ただし学習データの出所・権利処理はカードに記載がなく、HF Discussion #1(学習データと既存作品類似出力への質問)は未回答。ベースWan2.2はApache-2.0。商用可の断定は避け、データ由来リスクは利用者判断。
- **選定根拠**: 【事実】オープン重みでアニメ特化のT2VはaidealabのAnimeGen-T2V(Wan2.2 T2V-A14B追加学習、Apache-2.0、2026-06-17公開)のみ確認。HF累計DL 16,517/30日 1,065、likes 61、spaces 1。GitHubコード参照は'AnimeGen-I2V'文字列で36件(I2V/T2V合算の粗い指標)。カードにベンチマークなし。Xでは公開者アカウント(alfredplpl)の告知が1024いいね、第三者の試用記事は少数。【評価】競合となるアニメ特化T2Vが他に無いため選定するが、実力の根拠は薄い。開発者自身がXで『比較対象がWan2.1でWan2.2ではなかった可能性』に言及し、別の投稿者は『最先端モデルに対し品質・一貫性で見劣り』と評価。実務上はMiniMax-H3(汎用)+アニメLoRAがXで多く使われている(下記general_alternative)。学習データ出所はHF Discussion #1で質問が出ているが未回答。
- **指標（確認日時点）**: DL累計 16,962 / 直近30日 1,417 / likes 61 / Spaces 1
- **概要**: AIdeaLab(GENIAC支援)がWan2.2 T2V-A14Bを日本のアニメ表現向けに追加学習したテキスト→動画モデル。high noise/low noiseの2エキスパート(single_file)をDiffusersのWanPipelineで読み込み、lightx2v/Wan2.2-Lightningの4step LoRAと併用する例(8 steps、fps16)がカードにある。
- **入力**: テキストプロンプト(英語推奨。I2V例では先頭に"Japanese anime style, "を付与、negative "3d, cg, photo, stop, wait")
- **出力**: アニメ調の短尺動画(カード例: 832x480または1280x720、16fps、約5秒)
- **必要環境**: カード記載: NVIDIA RTX 4090以上を推奨。Python+PyTorch+Diffusers(peft等)。学習は24×H200(KDDI Kagawaクラスタ)。ローカルでの速度・VRAM実測は未測定。
- **制約**: カード記載: 複雑な動き・手指・目・小物の不安定、同一性ドリフト、フリッカー、長尺や高密度アクションが苦手、実写系は不向き、NSFWは限定的。ベンチマーク記載なし(自己評価も無し)。
- **使う版・派生**: 使用版: リポジトリ直下のhigh_noise.safetensors/low_noise.safetensors(ComfyUI・Diffusers single_file共通)。ベースVAE等は Wan-AI/Wan2.2-T2V-A14B-Diffusers を別途参照。派生: NullpoLab/AnimeGen-T2V-GGUF(30日DL 311)、siouni/AnimeGen-T2V-Quantized(30日DL 71)、mlx-community/AnimeGen-T2V-A14B-Lightning-(bf16|int4)(Apple Silicon)。
- **根拠**: [モデルカード本文(概要・使い方・ライセンス・制約)](https://huggingface.co/aidealab/AnimeGen-T2V/blob/ea04305bca418d988e4924a92a1e8ff67cb29a68/README.md) / [学習データ出所・権利処理に関する未回答の質問(open、コメント1件)](https://huggingface.co/aidealab/AnimeGen-T2V/discussions/1) / [公開告知(2026-07-13、1024いいね)](https://x.com/alfredplpl/status/2076481870003589541) / [公開者アカウントが「Wan2.1 I2Vとの比較でWan2.2との比較が無かった可能性」に言及(19いいね)](https://x.com/alfredplpl/status/2076638766069068034) / [第三者評価: 最先端モデルに比べ品質・キャラ一貫性で見劣りし、学習データ詳細は未確認(7いいね、2026-07-17)](https://x.com/masamune_sakaki/status/2077955548289573242)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `MiniMaxAI/MiniMax-H3` — 汎用だがXで2026-08〜09にアニメ動画用途の報告が最多(HF likes 5,790)。独自ライセンスで米・EU・英・韓は対象外など条件あり。ローカル実行は量子化/4step LoRA前提。
- **次点**: `vrgamedevgirl84/LTX_2.3_Fantasy_Anime_Style_LoRa`（LTX-2.3用のスタイルLoRA(累計6,662DL、likes 11、ライセンス未記載)。完全なモデルではなく、LTXライセンス条件も継承する。） / `Cseti/wan-14b-shinkai-anime-style-lora-v1`（Wan2.1時代の新海誠調LoRA(likes 2、DL計測なし)。Wan2.2世代の単体モデルに劣後。） / `TencentARC/AnimeGamer`（アニメ世界のゲーム状態動画生成用(累計295DL、独自ライセンス animegamer-lisence)。汎用T2Vではない。）

関連リポジトリ:

- [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) — ベースモデルWan2.2の公式推論コード（★17,843 / Apache-2.0 / 最終push 2026-09-21 / 確認コミット [`1ea34ff4`](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/README.md) / 制作カタログ: [wan2.2](../../categories/video.md#wan2.2)）
  - AnimeGenのベース。Apache-2.0、2026-09-21にもpush。
- [modelscope/DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) — AnimeGenの開発ワークフローに使われたと記載のある学習・推論基盤（★13,215 / Apache-2.0 / 最終push 2026-10-09 / release v1.1.9 (2025-11-18) / 確認コミット [`974cfa37`](https://github.com/modelscope/DiffSynth-Studio/blob/974cfa37f27ac55eba3b6d10efa21f876900572d/README.md) / 制作カタログ: [diffsynth-studio](../../categories/workflow.md#diffsynth-studio)）
  - AnimeGenカードが開発基盤として明記。Wan2.2/Wan-Animate-2/LTX-2.5/MiniMax-H3を2026-08〜09に統合済みでApache-2.0。
- [kohya-ss/musubi-tuner](https://github.com/kohya-ss/musubi-tuner) — Wan2.2/MiniMax-H3等のLoRA学習（★2,090 / ライセンス未表示 / 最終push 2026-10-10 / release v0.3.6 (2026-09-27) / 確認コミット [`f8a1b037`](https://github.com/kohya-ss/musubi-tuner/blob/f8a1b03794a49239a3539015075f5123d6c07d66/README.md) / 制作カタログ: [musubi-tuner](../../categories/workflow.md#musubi-tuner)）
  - Wan2.1/2.2・MiniMax-H3をサポート(README)。Xで「musubi-tuner参考の推論ライブラリでAnimeGenを動かした」報告あり。
- [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) — ComfyUIでのWan系推論ノード（★6,728 / Apache-2.0 / 最終push 2026-05-24 / 確認コミット [`088128b2`](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/088128b224242e110d3906c6750e9a3a348a659b/README.md) / 制作カタログ: [comfyui-wanvideowrapper](../../categories/workflow.md#comfyui-wanvideowrapper)）
  - Wan系ComfyUI運用の定番(6.7k stars、Apache-2.0)。ただし最終pushは2026-05-24で、AnimeGen専用の対応記載は未確認。

### 画像から動画生成(アニメ)

<a id="image-to-video"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [IndexTeam/Index-anisora](https://huggingface.co/IndexTeam/Index-anisora/tree/b134a8e677e4b22269827af7d596a4f2d9d3430a)（revision `b134a8e6` / 作成 2025-05-09 / 更新 2025-10-31）
- **利用条件**: apache-2.0。HFメタデータ・GitHubともApache-2.0(V3以降の重みもApache-2.0とREADMEに記載)。ただしHFリポジトリ内にLICENSEファイルは無い(追加PR #4は未マージ)。学習データはbilibili収集の1,000万件超のアニメ映像(論文)で出所・権利処理の詳細は不明。ベンチマークデータは申請フォーム+誓約が必要で非公開。商用可とは断定しない。
- **選定根拠**: 【事実】bilibili公式Index-AniSora(IJCAI'25、Apache-2.0)。HF likes 229・spaces 4、GitHub bilibili/Index-anisora 2,519 stars。GitHubコード参照は'anisora'3,024件・'Index-anisora'274件(粗い指標)に対しAnimeGen-I2Vは36件。アニメ948クリップのAniSora-Benchmarkで自己報告の人手評価 70.13(MiniMax-I2V01 69.63、Vidu-1.5 60.98)、キャラ一貫性 94.54(同89.47)。ただし動きの大きさ(Visual Motion)は47.94で同68.05に劣る。V3.2(Wan2.2系・8step)は2025-09公開で独自ベンチ未公表、HFカードはV1/V2期の記述のまま(更新はGitHub README)。HFのDL計数は累計313で実利用を反映せず(サブフォルダ構成)、GGUF派生 youcef079/Index-Anisora-V3.2-GGUF が累計11,156DL。【評価】次点 aidealab/AnimeGen-I2V は新しく(2026-06)HF累計30,512DLと導入しやすいが、ベンチ無し・開発者が比較対象の不備を疑うツイート・『唇と目しか動かない』報告あり。実測ベンチと採用実績(star・参照数)でAniSoraを上位とするが、V3.2同士の比較は未確認でモデル更新は2025-10-31以降止まっている。
- **指標（確認日時点）**: DL累計 313 / 直近30日 6 / likes 229 / Spaces 4
- **概要**: bilibili Indexチームのアニメ動画生成系。V1はCogVideoX-5B、V2/V3はWan2.1-14B、V3.2(2025-09-23)はWan2.2系(high/low noise、8step)。I2V・先頭/中間/末尾フレーム指定、局所マスク制御(anymask, 2025-10-31)、キャラ360°回転、ビデオスタイル変換、超低解像度SRを機能として記載(GitHub README)。
- **入力**: 画像(+プロンプト)。任意フレームへの画像指定、モーションマスク(anymask)。
- **出力**: アニメ調の短尺動画(尺・解像度はカード未記載)。
- **必要環境**: カード/READMEの記載: V1はRTX 4090で運用可、V3.1の12GB VRAM版がModelScopeにあり(2025-09-25)。HF Discussion #3に「fp8の14BはVRAM16GB+RAM32GBでは厳しい」との利用者報告。実測は未実施。
- **制約**: T2Vの提供なし(README記載はI2V/補間/マスク制御)。V1ベンチでは動きの大きさが弱い。HFのREADMEはV3.x未記載で古い。5B/5B_RLの重みは.pt(pickle)形式のためtorch.load利用時に注意(V3系はsafetensors)。最終モデル更新は2025-10-31で、2026年は保守的更新のみ(GitHub commitは認証情報削除等)。
- **使う版・派生**: 推奨: V3.2/(high_noise_model・low_noise_model、safetensors)。anymask/はマスク制御版。派生: youcef079/Index-Anisora-V3.2-GGUF(累計11,156DL)、woctordho/AniSora-v3-GGUF、shinnpuru/Anisora_comfy_fp8_scaled、Disty0/Index-anisora-5B-diffusers。
- **根拠**: [モデルカード本文(概要・使い方・ライセンス・制約)](https://huggingface.co/IndexTeam/Index-anisora/blob/b134a8e677e4b22269827af7d596a4f2d9d3430a/README.md) / [V3/V3.1/V3.2/anymaskの更新履歴・機能(GitHub README、commit固定)](https://github.com/bilibili/Index-anisora/blob/6cdce3a17548d7ff0f2e05978469f134da25e68e/README.md) / [AniSora論文(IJCAI'25)、948クリップのアニメ評価ベンチマーク](https://arxiv.org/abs/2412.10255) / [LICENSEファイル追加PR(open)。メタデータはApache-2.0](https://huggingface.co/IndexTeam/Index-anisora/discussions/4) / [AnimeGen側の比較根拠: ComfyUIで唇と目しか動かないとの報告(12いいね)](https://x.com/mix_buchi_/status/2076617242482225433)
- **強い汎用モデル（アニメ特化ではない・収録外）**: `MiniMaxAI/MiniMax-H3` — FL2VA(先頭/末尾フレーム)/Ref2VAを持つ汎用オープン重み。Xでアニメ動画用途の報告が多い(ただし高速化LoRAでアニメにゴースト発生との指摘もあり)。独自ライセンスで米・EU・英・韓は対象外。
- **次点**: `aidealab/AnimeGen-I2V`（Wan2.2 I2V-A14B追加学習(2026-06、Apache-2.0、累計30,512DL/30日11,345、likes 41)。Diffusers/ComfyUI/GGUFが整い導入は容易だが、ベンチ無し・参照36件・比較根拠に疑義。AniSoraに実測差を示す証拠が出れば逆転し得る。） / `prithivMLmods/MiniMax-H3-I2V-Anime-Motion-LoRA`（MiniMax-H3向けの実験的LoRA(ループ向けのストップモーション系動き、累計1,674DL、likes 27)。H3独自ライセンス(地域制限)を継承し汎用アニメ動画モデルではない。） / `TencentARC/ToonComposer`（スケッチ+彩色参照からの中割り専用(video-to-videoのsketch-inbetweening-colorization参照)。通常のI2Vではない。）

関連リポジトリ:

- [bilibili/Index-anisora](https://github.com/bilibili/Index-anisora) — AniSora公式(学習・推論・データパイプライン・報酬モデル)（★2,527 / Apache-2.0 / 最終push 2026-07-16 / 確認コミット [`6cdce3a1`](https://github.com/bilibili/Index-anisora/blob/6cdce3a17548d7ff0f2e05978469f134da25e68e/README.md) / 制作カタログ: [index-anisora](../../categories/video.md#index-anisora)）
  - 2,519 stars、Apache-2.0。最終pushは2026-07-16だが内容は認証情報削除。モデル更新は2025-10-31。
- [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) — AniSora V3.2のベース(Wan2.2)推論コード（★17,843 / Apache-2.0 / 最終push 2026-09-21 / 確認コミット [`1ea34ff4`](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/README.md) / 制作カタログ: [wan2.2](../../categories/video.md#wan2.2)）
  - Apache-2.0、2026-09-21 push。
- [kohya-ss/musubi-tuner](https://github.com/kohya-ss/musubi-tuner) — Wan2.1/2.2系I2VのLoRA学習（★2,090 / ライセンス未表示 / 最終push 2026-10-10 / release v0.3.6 (2026-09-27) / 確認コミット [`f8a1b037`](https://github.com/kohya-ss/musubi-tuner/blob/f8a1b03794a49239a3539015075f5123d6c07d66/README.md) / 制作カタログ: [musubi-tuner](../../categories/workflow.md#musubi-tuner)）
  - Wan2.2対応、v0.3.6(2026-09-27)。アニメLoRAを自作する際の標準的ツールの一つ。
- [tdrussell/diffusion-pipe](https://github.com/tdrussell/diffusion-pipe) — Wan2.2等のパイプライン並列学習（★2,029 / GPL-3.0 / 最終push 2026-09-28 / 確認コミット [`334106c2`](https://github.com/tdrussell/diffusion-pipe/blob/334106c2d0e29131b53d504b80e211942dac147e/README.md)）
  - Wan2.2/MiniMax-H3対応、2026-09-28 push(GPL-3.0)。複数GPUでの学習向け。

### 画像+テキストから動画生成(アニメ)

<a id="image-text-to-video"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3/tree/42ed227ee7df40d41602854ae760620d6eb651fe)（revision `42ed227e` / 作成 2026-07-28 / 更新 2026-08-13）
- **利用条件**: other/minimax-h3-community-license-agreement。MiniMax H3 Community License(独自)。対象地域は世界全域だが米国・EU・英国・韓国は除外で、対象地域外での利用・出力の利用は許諾外。年間売上2,000万米ドル超の商用利用は別途許諾、商用UIに「MiniMax H3」表示義務、出力を他AIモデルの改善に使うことは禁止、再配布時は制限を利用者へ承継、提供側は安全対策が必要(LICENSE全文を確認)。商用可と断定しない。
- **選定根拠**: 【事実】HFのimage-text-to-videoタグはMiniMax-H3系が占める(MiniMaxAI/MiniMax-H3: likes 5,790、30日DL 3,612,196、累計9,127,868、2026-07-28公開、FL2VA/Ref2VA、音声同時生成)。アニメ特化のH3向けLoRAは小規模: prithivMLmods/MiniMax-H3-I2V-Anime-Motion-LoRA(累計1,674DL、likes 27、『実験的』とカード自身が明記、ストップモーション系のループ向け)、Inner-Reflections/MiniMax-H3-Looping-Sketch-Anime(likes 77、ライセンス未記載)。Xの2026-08〜09には、H3 Ref2VA+4step LoRAでアニメ動画を作る報告(ai_hakase_ 62〜103いいね、craftcapitallab 207/132いいね: アニメ背景下絵の用途)が多い一方、kiyoshi_shin(30いいね)は高速化LoRAでアニメだとゴースト破綻が出やすいと報告。【評価】アニメ特化LoRAは採用実績が不足のため、汎用ベースのH3をgeneral_onlyで採用し、LoRAは補助とする。ライセンスは地域・収益・用途制限つきで、日本国内利用は対象地域内だが商用可とは断定しない。
- **指標（確認日時点）**: DL累計 10,394,822 / 直近30日 3,596,813 / likes 6,022 / Spaces 100
- **概要**: MiniMax(Nanonoble)のオープン重み音声付き動画生成。FL2VA(先頭/末尾フレーム)とRef2VA(画像9枚・動画3本・音声3本の参照)の2系統、768p生成+2K再生成、日本語を含む11言語の音声。H3-Context-IR(プロンプト整形)は非公開のホスト型で、プロンプトガイドに沿って自前で整形する。
- **入力**: テキスト+画像0〜2枚(FL2VA)、または画像≤9/動画≤3/音声≤3の参照(Ref2VA)。
- **出力**: 24FPSの動画+32kHzステレオ音声、768p(再生成で最大2K)。
- **必要環境**: カード記載の参考構成はsglangで4GPU(--num-gpus 4)。消費者GPU向けは量子化/GGUF/4step LoRA等の派生に依存(Xの自己報告: RTX 4060 Ti 16GBで15秒動画が約10分、2026-09-01 aiaicreate)。実測は未実施。
- **制約**: アニメ特化学習ではない(アニメはXの運用報告ベース)。高速化LoRA併用でアニメにゴースト破綻との報告。複数LoRAの併用が難しいとの報告。疎注意は未公開(初回リリースは全注意のみ)。ポルノ等は自動モデレーション対象と記載。
- **使う版・派生**: 公式: MiniMaxAI/MiniMax-H3。ComfyUI再パッケージ Comfy-Org/MiniMax-H3(30日DL 22,115,336)、加速: lightx2v/Minimax-h3-Turbo(30日DL 1,538,470)、larryvrh/MiniMax-H3-Turbo-Lora、量子化: unsloth/MiniMax-H3-GGUF(30日DL 1,335,287)、MATLOWAI/minimax-h3-fused-turbo-int8-convrot。
- **根拠**: [モデルカード本文(概要・使い方・ライセンス・制約)](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/42ed227ee7df40d41602854ae760620d6eb651fe/README.md) / [独自ライセンス全文(対象地域・収益閾値・出力利用制限)](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/42ed227ee7df40d41602854ae760620d6eb651fe/LICENSE) / [H3 Ref2VAでアニメ動画を4step LoRA+SLAで生成(RTX 3080 Ti 16GB、自己報告、62いいね)](https://x.com/ai_hakase_/status/2097068396181430635) / [アニメ背景下絵制作での利用報告(207いいね)](https://x.com/craftcapitallab/status/2088922901437460942) / [高速化LoRAはアニメでゴースト破綻が出やすいとの報告(30いいね)](https://x.com/kiyoshi_shin/status/2086021782403010800)
- **次点**: `prithivMLmods/MiniMax-H3-I2V-Anime-Motion-LoRA`（アニメ動作LoRA(実験的、ストップモーション系クリップで学習、ループ向け、累計1,674DL)。H3ライセンス継承。採用実績不足。） / `Inner-Reflections/MiniMax-H3-Looping-Sketch-Anime`（ラフスケッチ調ループのスタイルLoRA(likes 77)。ライセンス未記載、DL計数0、用途が限定的。） / `lovis93/studio-1939-old-animation-lora-minimax-h3`（1930年代風の西洋旧アニメLoRA(likes 74、累計5,567DL)。日本アニメ向けではない。）

関連リポジトリ:

- [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) — MiniMax H3公式(推論・プロンプトガイド・スキル)（★9,772 / ライセンス未表示 / 最終push 2026-08-15 / 確認コミット [`d21241f0`](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/README.md)）
  - 9.4k stars。プロンプト作成スキルを同梱(リポジトリ側にライセンスメタデータなし、HF側LICENSEを参照)。
- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) — ComfyUIでのH3実行(Comfy-Org再パッケージ重み)（★136,791 / GPL-3.0 / 最終push 2026-10-10 / release v0.39.0 (2026-10-05) / 確認コミット [`83071e1a`](https://github.com/Comfy-Org/ComfyUI/blob/83071e1aec311d31e773d64d6872181b3bad0fe2/README.md) / 制作カタログ: [comfyui](../../categories/workflow.md#comfyui)）
  - Comfy-Org/MiniMax-H3が最も取得されている配布形態。v0.38.0(2026-09-29)。
- [kohya-ss/musubi-tuner](https://github.com/kohya-ss/musubi-tuner) — H3のLoRA学習(実験的サポート、1フレーム学習ドキュメントあり)（★2,090 / ライセンス未表示 / 最終push 2026-10-10 / release v0.3.6 (2026-09-27) / 確認コミット [`f8a1b037`](https://github.com/kohya-ss/musubi-tuner/blob/f8a1b03794a49239a3539015075f5123d6c07d66/README.md) / 制作カタログ: [musubi-tuner](../../categories/workflow.md#musubi-tuner)）
  - READMEがMiniMax-H3の学習をサポートと明記(2026-09-27 v0.3.6)。
- [ostris/ai-toolkit](https://github.com/ostris/ai-toolkit) — H3(FL2VA/Ref2V)のLoRA学習（★12,260 / MIT / 最終push 2026-10-10 / 確認コミット [`ecee894e`](https://github.com/ostris/ai-toolkit/blob/ecee894ed2b1f3716d9d7326693061ec1a3105bb/README.md)）
  - READMEが対応モデルに記載、MIT、2026-09-27 push。

### 動画(アニメ)のアップスケール・修復(video-to-video)

<a id="video-to-video--upscale-restoration"></a>
- **判定**: モデルなし / 確度 低
- **選定根拠**: 【HF非掲載・重みはGitHub配布】アニメ動画用アップスケーラの実用標準は、HFの公式モデルではなくGitHub配布のONNX/PyTorchモデル群。推奨はthe-database の 2x_AnimeJaNai V3(Real-ESRGAN Compact系、HD/SD向け)で、mpv-AnimeJaNai 752 stars(リリース3.5.0=2026-06-18)、VideoJaNai 280 stars(2.1.0=2026-06-18)。Xでは『Animejanai』投稿が1,363いいね(2026-05-19)。カードやwikiに画質ベンチは無く(wikiのBenchmarksは速度)、画質優位の実測根拠は未確認。ライセンスはmpv-AnimeJaNaiリポジトリのLICENSEがCC BY-NC-SA 4.0で非商用。商用・再配布ならReal-ESRGAN animevideov3(BSD-3-Clause、xinntao/Real-ESRGAN 36.9k stars、最終release 2022-09)、Real-CUGAN(bilibili/ailab 5.9k stars、2023-08以降push無し)等を別途検討。HF側の再パッケージはmlx-community/Real-ESRGAN-animevideov3(累計215DL、非公式)と、Comfy-Org/Real-ESRGAN_repackaged(汎用x4plusのみ、累計563,624DL)で、いずれも公式でなくアニメ動画特化の採用根拠が弱いため採用せず。汎用の動画SR(SeedVR2, FlashVSR)はアニメ特化でない。
- **強い汎用モデル（アニメ特化ではない・収録外）**: `numz/SeedVR2_comfyUI` — 汎用の動画SR(HF累計2,921,839DL、Apache-2.0)。アニメ特化ではなく、線のシャープさ・塗りの忠実さは未検証。
- **次点**: `xinntao/Real-ESRGAN (realesr-animevideov3)`（BSD-3-Clause、GitHub 36.9k stars。ただし2022年のモデルで最終release 2022-09、近年の比較根拠なし。商用・非商用を問わず使いやすい点が利点。） / `bilibili/ailab (Real-CUGAN)`（アニメ特化で軽量だが、リポジトリは2023-08以降更新なし。ncnn版(nihui/realcugan-ncnn-vulkan)は2023-03以降更新なし。） / `Kiteretsu77/APISR`（アニメ制作工程に着想したSR(CVPR-W 2024)、1.1k stars・GPL-3.0、最終push 2025-10。動画向け最適化や採用は限定的。）

関連リポジトリ:

- [the-database/mpv-AnimeJaNai](https://github.com/the-database/mpv-AnimeJaNai) — 2x_AnimeJaNai V3/SD V1モデルとmpvリアルタイム再生環境(TensorRT/DirectML)（★767 / NOASSERTION / 最終push 2026-10-09 / release 3.7.0 (2026-10-07) / 確認コミット [`d9cbaae5`](https://github.com/the-database/mpv-AnimeJaNai/blob/d9cbaae5e92a56e71fdf4da5e063ae3e2611e5f7/README.md)）
  - アニメ向け軽量ONNXモデルの本拠。752 stars、3.5.0(2026-06-18)、2026-09-19 push。LICENSEはCC BY-NC-SA 4.0(GitHubメタデータはNOASSERTION)。
- [the-database/VideoJaNai](https://github.com/the-database/VideoJaNai) — 動画ファイルのバッチ変換GUI(ONNX+TensorRT、RIFE補間対応、旧AnimeJaNaiConverterGui)（★281 / GPL-3.0 / 最終push 2026-06-18 / release 2.1.0 (2026-06-18) / 確認コミット [`68f6060c`](https://github.com/the-database/VideoJaNai/blob/68f6060c3971dfc0f2423b5702f2d259013eca60/README.md)）
  - 280 stars、GPL-3.0、2.1.0(2026-06-18)。
- [NevermindNilas/TheAnimeScripter](https://github.com/NevermindNilas/TheAnimeScripter) — アニメ向けの一括ツールキット(アップスケール・RIFE補間・復元・重複フレーム除去、CLI/AE/Standalone)（★332 / AGPL-3.0 / 最終push 2026-10-07 / release v2.10.0 (2026-09-20) / 確認コミット [`a4913ca9`](https://github.com/NevermindNilas/TheAnimeScripter/blob/a4913ca99e0ef4a8d7253f11f2ee6735752664b4/README.md)）
  - 329 stars、AGPL-3.0、v2.10.0(2026-09-20)。READMEがCUGAN/Adore/SPAN等のモデル搭載を記載。
- [k4yt3x/video2x](https://github.com/k4yt3x/video2x) — Anime4K v4/Real-ESRGAN/Real-CUGAN/RIFEをncnn+Vulkanで動かす汎用フレームワーク（★22,137 / AGPL-3.0 / 最終push 2026-03-07 / release 6.4.0 (2025-01-24) / 確認コミット [`7db9c18d`](https://github.com/k4yt3x/video2x/blob/7db9c18d6278bbad9c3eda0e4e4ae210f9a688eb/README.md)）
  - 21.9k stars だがAGPL-3.0、最終release 6.4.0は2025-01、最終pushは2026-03。

### フレーム補間(アニメの滑らか化)

<a id="video-to-video--frame-interpolation"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [Comfy-Org/frame_interpolation](https://huggingface.co/Comfy-Org/frame_interpolation/tree/219da3c9d8c357ceaf457fc1d5932c6e861b8dee)（revision `219da3c9` / 作成 2026-04-02 / 更新 2026-09-23）
- **利用条件**: other/mit-and-apache-2.0。HFメタデータはlicense=other / mit-and-apache-2.0(RIFE=MIT、FILM=Apache-2.0の混在)。再パッケージ(公式配布元ではない)。カード本文に追加条件の記載なし。
- **選定根拠**: 【事実】アニメ専用の現役補間モデルはHFに無い。アニメ特化のAnimeInterp(CVPR'21、lisiyao21/AnimeInterp)は458 starsで最終push 2024-03、HF重みなし。実務はRIFE(hzwer/Practical-RIFE 1,028 stars MIT、ECCV2022-RIFE 5.6k stars)が標準で、TheAnimeScripterやVideoJaNai、Video2XなどアニメPF系ツールがRIFEを同梱。HFではComfy-Org/frame_interpolation(RIFE v4.25/v4.26 lite/標準/heavy+FILM fp16をComfyUI形式で再パッケージ)が30日DL 72,273・累計148,615・likes 42でComfyUI標準。【評価】アニメ特化の比較ベンチは見つからず、『RIFEがアニメ実務の標準』はツール同梱実績に基づく評価。重複フレーム(3コマ打ち等)の除去は別途必要(TheAnimeScripterが重複除去を同梱)。大きな動きの補間にはToonComposer/ToonCrafter(生成型)やAnimeGen-I2V/Index-AniSoraのキーフレーム補間が別枠。
- **指標（確認日時点）**: DL累計 180,188 / 直近30日 76,630 / likes 47 / Spaces 6
- **概要**: ComfyUI公式(Comfy-Org)による動画フレーム補間モデルの再パッケージ集。RIFE v4.25(lite/標準/heavy)・v4.26(標準/heavy)とFILM fp16。元はhzwer/Practical-RIFEとgoogle-research/frame-interpolation。
- **入力**: 動画フレーム列(ComfyUIのFrame Interpolationワークフロー)。
- **出力**: 2倍等に補間した動画フレーム列。
- **必要環境**: カード記載なし(ComfyUI配置先 models/frame_interpolation/ のみ)。VRAM・速度は未測定。
- **制約**: アニメ特化の学習・検証ではない。ワークフロー画像以外の品質比較記載なし。元の重みはPractical-RIFE配布(Google Drive等)。
- **使う版・派生**: 元: hzwer/Practical-RIFE(GitHub、MIT)、作者名義の hzwer/RIFE(HF、カード記載は最小限)、mlx-community/RIFE-4.25(Apple Silicon、累計1,895DL)、ComfyUIノード Fannovel16/ComfyUI-Frame-Interpolation。
- **根拠**: [モデルカード本文(概要・使い方・ライセンス・制約)](https://huggingface.co/Comfy-Org/frame_interpolation/blob/219da3c9d8c357ceaf457fc1d5932c6e861b8dee/README.md) / [アニメ向けツールキットがRIFE補間を中核機能として同梱](https://github.com/NevermindNilas/TheAnimeScripter/blob/a4913ca99e0ef4a8d7253f11f2ee6735752664b4/README.md) / [アニメ特化補間(CVPR21)の実装。最終push 2024-03で現役ではない](https://github.com/lisiyao21/AnimeInterp/blob/223c5e6f39c525bdfcb51ca8acf9d59d4adeb643/README.md)
- **次点**: `lisiyao21/AnimeInterp`（アニメ特化補間(CVPR21)だがGitHubのみ・458 stars・最終push 2024-03。ComfyUI/ツール統合が乏しい。） / `Doubiiu/ToonCrafter`（2枚のキーフレーム間を生成する生成型補間(約2秒)。フレーム補間の代替ではなく中割り生成枠。） / `mlx-community/RIFE-4.25`（Apple Silicon向け変換(累計1,895DL)。ComfyUI標準のComfy-Org版に劣る。）

関連リポジトリ:

- [hzwer/Practical-RIFE](https://github.com/hzwer/Practical-RIFE) — RIFE実用版(v4.x)の元実装・重み（★1,027 / MIT / 最終push 2026-08-27 / 確認コミット [`bbfd2ea9`](https://github.com/hzwer/Practical-RIFE/blob/bbfd2ea90910789a860ea3e2b32a240cd577b75e/README.md)）
  - MIT、1,028 stars、2026-08-27 push。ComfyUI repackageの元。
- [hzwer/ECCV2022-RIFE](https://github.com/hzwer/ECCV2022-RIFE) — RIFE原論文実装（★5,605 / MIT / 最終push 2025-09-10 / 確認コミット [`5d8adbdd`](https://github.com/hzwer/ECCV2022-RIFE/blob/5d8adbdd40e12c2c8f91930eff838aebe561c086/README.md) / 制作カタログ: [eccv2022-rife](../../categories/animation.md#eccv2022-rife)）
  - MIT、5.6k stars、2025-09 push。
- [Fannovel16/ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation) — ComfyUI向け補間ノード集(RIFE/FILM/GMFSS等)（★1,084 / MIT / 最終push 2026-03-29 / release models (2023-08-10) / 確認コミット [`26545cc2`](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation/blob/26545cc2dd95bc3d27f056016300673bdeee78f5/README.md)）
  - MIT、1.1k stars、最終push 2026-03-29。
- [lisiyao21/AnimeInterp](https://github.com/lisiyao21/AnimeInterp) — アニメ特化補間(CVPR21)（★458 / ライセンス未表示 / 最終push 2024-03-31 / 確認コミット [`223c5e6f`](https://github.com/lisiyao21/AnimeInterp/blob/223c5e6f39c525bdfcb51ca8acf9d59d4adeb643/README.md)）
  - 458 stars。最終push 2024-03で保守停止。参考実装として。

### 線画/スケッチからの中割り・彩色(ToonComposer等)

<a id="video-to-video--sketch-inbetweening-colorization"></a>
- **判定**: アニメ特化の最良 / 確度 中
- **最良**: [TencentARC/ToonComposer](https://huggingface.co/TencentARC/ToonComposer/tree/a166c2c0f0755af6b1876586739e818e92e5c44f)（revision `a166c2c0` / 作成 2025-08-15 / 更新 2026-03-05）
- **利用条件**: mit。HFメタデータ・GitHub LICENSEともMIT(サードパーティ部分は各ライセンス)。基盤Wan2.1 I2V-14B-480PはApache-2.0。学習データの出所はカードに記載なし(未確認)。評価用の映画シーンは許諾の上で評価専用と論文に記載。商用可の断定は避ける。
- **選定根拠**: 【事実】TencentARC/ToonComposer(ICLR 2026、Wan2.1 I2V-14B-480P基盤、MIT)はキーフレームのスケッチ1枚+彩色参照から中割りと彩色を一括生成。論文(arXiv 2508.10881)の自己報告ユーザースタディ(47人、30サンプル、PKBench)で審美/動きの勝率が ToonComposer 70.99%/68.58%、ToonCrafter 17.02%/18.19%、LVCD 7.54%/7.91%、AniDoc 4.45%/5.34%。HF likes 51・spaces 8(DL計数0=カスタム形式)、GitHub 586 stars、コード参照192件。ToonCrafter(Doubiiu、2024-05)は6,030 stars・HF likes 209・spaces 32・参照1,310件と採用実績が桁違いに多い。【評価】比較は提案者の自己報告でToonCrafter/LVCD/AniDocとのみ。採用実績ではToonCrafterが上だが、スケッチ制御と彩色を含む新世代のToonComposerを、実測評価(自己報告)と2025-08公開の鮮度、MITライセンスで選定。欠点はVRAM約57GB(480p、61フレーム、README記載)で、ローカルでは非現実的になりやすい。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 51 / Spaces 8
- **概要**: カートゥーン/アニメ制作の「ポストキーフレーミング」生成。スパーススケッチ注入と空間LoRA(SLRA)でWan2.1をカートゥーン領域へ適応し、少数スケッチ+彩色参照から中割りと彩色を一括処理する。
- **入力**: 彩色済み参照フレーム1枚+キーフレームのスケッチ(1枚〜複数、任意位置)+テキスト。
- **出力**: 480p/608pの彩色アニメーション(61フレーム級)。
- **必要環境**: README記載: 480p・61フレーム生成に約57GB VRAM。デモはHF Space(TencentARC/ToonComposer)。実測は未実施。
- **制約**: ローカル実行は大容量VRAMが必要。自己報告のベンチのみ。アニメ固有のデータ規模・出所は未記載。HF DL計数は0(単一ファイル形式)。
- **使う版・派生**: 重み: 480p/・608p/ 各 tooncomposer.ckpt+config.json。基盤 Wan-AI/Wan2.1-I2V-14B-480P が別途必要。量子化・GGUF派生は確認できず。
- **根拠**: [モデルカード本文(概要・使い方・ライセンス・制約)](https://huggingface.co/TencentARC/ToonComposer/blob/a166c2c0f0755af6b1876586739e818e92e5c44f/README.md) / [論文。PKBench(30サンプル)と47人ユーザースタディで ToonCrafter/LVCD/AniDoc と比較(自己報告)](https://arxiv.org/abs/2508.10881) / [必要VRAM約57GB、重みと基盤モデルの構成](https://github.com/TencentARC/ToonComposer/blob/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c/README.md)
- **次点**: `Doubiiu/ToonCrafter`（2枚のキーフレーム間の生成型補間(SIGGRAPH Asia 2024、GitHub Apache-2.0だがHF license未記載、READMEは「研究探索」と明記)。6,030 stars・HF likes 209と採用は最大だが、スケッチ制御・彩色なし、約2秒・512x320。） / `Yhmeng1106/anidoc`（線画動画の彩色+補間(CVPR'25、MIT、SVD基盤)。ToonComposerの自己報告ユーザースタディで勝率4〜5%。SVDの非商用ライセンス条件を継承する可能性。） / `luckyhzt/lvcd_pretrained_models`（参照ベースの線画動画彩色(SIGGRAPH Asia 2024、SVD基盤)。HF likes 4、ライセンス未記載、同ユーザースタディで勝率約8%。）

関連リポジトリ:

- [TencentARC/ToonComposer](https://github.com/TencentARC/ToonComposer) — ToonComposer公式(Gradioデモ、推論)（★591 / NOASSERTION / 最終push 2025-08-20 / 確認コミット [`53dc3df9`](https://github.com/TencentARC/ToonComposer/blob/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c/README.md) / 制作カタログ: [tooncomposer](../../categories/animation.md#tooncomposer)）
  - 586 stars、ICLR 2026。最終push 2025-08-20、GitHubライセンス判定はNOASSERTION(LICENSEはMIT+第三者条項)。
- [Doubiiu/ToonCrafter](https://github.com/Doubiiu/ToonCrafter) — ToonCrafter公式(生成型補間)（★6,031 / Apache-2.0 / 最終push 2025-03-19 / 確認コミット [`b0c47ff3`](https://github.com/Doubiiu/ToonCrafter/blob/b0c47ff339c5e5ec45b84d0c6587850f242d41ef/README.md) / 制作カタログ: [tooncrafter](../../categories/animation.md#tooncrafter)）
  - 6,030 stars、Apache-2.0、最終push 2025-03-19。kijai/ComfyUI-DynamiCrafterWrapper経由でComfyUIで12GB級で動くとREADME記載。
- [robbyant-research/AniDoc](https://github.com/robbyant-research/AniDoc) — AniDoc公式(線画動画彩色)（★573 / Apache-2.0 / 最終push 2025-04-15 / 確認コミット [`77e0696c`](https://github.com/robbyant-research/AniDoc/blob/77e0696cea9df7bb1cd2c254ba21639d3a6ab8f8/README.md) / 制作カタログ: [anidoc](../../categories/animation.md#anidoc)）
  - 572 stars、Apache-2.0、14GB級VRAM(README)、最終push 2025-04。
- [luckyhzt/LVCD](https://github.com/luckyhzt/LVCD) — LVCD公式(参照ベース線画動画彩色)（★200 / ライセンス未表示 / 最終push 2025-01-06 / 確認コミット [`eb7eced5`](https://github.com/luckyhzt/LVCD/blob/eb7eced5483b6e3a5ec70a007636533c921c6cf2/README.md)）
  - 200 stars、ライセンスなし、最終push 2025-01。

### キャラクター動作転写・キャラ差し替え(Wan-Animate/Viggle系)

<a id="video-to-video--character-animation"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 中
- **最良**: [Wan-AI/Wan2.2-Animate-2-14B](https://huggingface.co/Wan-AI/Wan2.2-Animate-2-14B/tree/6e8f1973bf0abc2aafd517992e8b6d88c3c46e69)（revision `6e8f1973` / 作成 2026-07-14 / 更新 2026-08-09）
- **利用条件**: apache-2.0。HFメタデータ・READMEともApache-2.0。学習データの記載なし。アニメ・2D画像への適用条件に関する追加条件は記載なし。
- **選定根拠**: 【事実】アニメ特化のキャラ動作転写モデルは見つからず、汎用の参照画像+駆動動画方式が標準。最新はWan-AI/Wan2.2-Animate-2-14B(2026-07-14公開、Apache-2.0、likes 271、HF公式ディスカッション9件)。ComfyUI再パッケージ Comfy-Org/Wan-Animate-2 は30日DL 567,925・累計953,947(int8_convrot/蒸留版を含む)。旧版 Wan-AI/Wan2.2-Animate-14B は likes 1,268・累計482,409DL・spaces 100、Diffusers版あり。論文(arXiv 2608.06009)は定性評価とユーザースタディのみで数値ベンチ・アニメ評価なし、カードにanime/cartoon等の語は無い(例は制服の猫キャラ)。HF Discussion #5に『RTX 4090でも720x1280が厳しい』との報告。Xの比較は2人差し替えでWan2.2 Animateが同一人物を2回入れ替えた(4いいね)等、アニメ評価の裏付けは乏しい。【評価】アニメ対応の実証が無いためgeneral_only。新旧の優劣は定量比較が無く、採用規模で新版を採るが、資源要件は新版が重い。Viggle-Animate(drbaph/Viggle-Animate-ComfyUI、H3ベース33B)は30日DL 82,305だがH3ライセンス(地域制限)で、アニメ評価なし。
- **指標（確認日時点）**: DL累計 0 / 直近30日 0 / likes 317 / Spaces 0
- **概要**: Wan2.2系の14Bキャラクター動画アニメーション。駆動動画を中間表現(ポーズ抽出器)なしで直接入力し、参照画像のキャラに動き・表情を転写する。テキストによる視点制御と、10step・CFG無しの蒸留版、リアルタイム向けWan-Animate-2-Liteを論文/カードで言及(リリースノートの公開物はBaseと蒸留版のみ)。
- **入力**: 参照キャラ画像+駆動動画+外見を記述したテキスト(カードは中国語の外見/背景記述をLLMで生成する手順)。
- **出力**: 24fps、最大720p級のキャラクター動画。
- **必要環境**: カード記載: 既定設定は8×A800で720P、480Pは2×A800で検証。Comfy再パッケージにint8_convrot版あり。Discussion #5にRTX 4090で720x1280が厳しいとの利用者報告。自前の実測は未実施。
- **制約**: アニメ・2D絵柄での品質はカード/論文で評価されていない。外見記述に外部LLM(Qwen3.7-Plus例)が必要。RAM/VRAMが大きく、NVFP4等の軽量版要望(Discussion #9)は未対応。HF DL計数は0(videomodel/サブフォルダ構成)のため数値比較不可。
- **使う版・派生**: 使用: wan_animate_2/wan_animate_2_bf16.safetensors、蒸留版 *_distillation.safetensors。ComfyUI: Comfy-Org/Wan-Animate-2(diffusion_models/のbf16・int8_convrot各2種、lightx2v蒸留LoRA)。旧版 Wan-AI/Wan2.2-Animate-14B(+Diffusers、QuantStack/Wan2.2-Animate-14B-GGUF 30日118,193DL)。
- **根拠**: [モデルカード本文(概要・使い方・ライセンス・制約)](https://huggingface.co/Wan-AI/Wan2.2-Animate-2-14B/blob/6e8f1973bf0abc2aafd517992e8b6d88c3c46e69/README.md) / [論文: 中間モーション抽出器なしのDiT、視点制御、Lite版。評価は定性+ユーザースタディ](https://arxiv.org/abs/2608.06009) / [RTX 4090でも720x1280が厳しいとの利用者報告](https://huggingface.co/Wan-AI/Wan2.2-Animate-2-14B/discussions/5) / [ComfyUI再パッケージの構成(30日DL 567,925)](https://huggingface.co/Comfy-Org/Wan-Animate-2/blob/e7181fe1896b7f2ce34120d1a3663413548240d7/README.md)
- **次点**: `Wan-AI/Wan2.2-Animate-14B`（旧版。likes 1,268・累計482,409DLで実績は大きく、Diffusers/GGUF派生も豊富だが、2026-07に後継が出た。アニメ評価は同様に無い。） / `drbaph/Viggle-Animate-ComfyUI`（Viggle-Animate(MiniMax-H3 ref2vaの33B全微調整)のComfy変換(30日DL 82,305、4step)。H3独自ライセンス、専用ノード必要、アニメ評価なし。） / `akatz-ai/MiniMax-H3-Character-Swap-LoRA`（H3向けキャラ差し替えLoRA(実験的、likes 183、30日DL 8,078)。動きのタイミング・表情・カット切替が不安定とカード自身が記載。）

関連リポジトリ:

- [Wan-Video/Wan-Animate-2](https://github.com/Wan-Video/Wan-Animate-2) — Wan-Animate-2公式(推論・Gradio)（★338 / Apache-2.0 / 最終push 2026-08-08 / 確認コミット [`3ad2fef7`](https://github.com/Wan-Video/Wan-Animate-2/blob/3ad2fef7d61d6200c9c653e0fe47be7616b323f3/README.md)）
  - 331 stars、Apache-2.0、2026-08-08。
- [kijai/ComfyUI-WanAnimatePreprocess](https://github.com/kijai/ComfyUI-WanAnimatePreprocess) — Wan-Animate系入力(ポーズ/顔)の前処理ComfyUIノード（★551 / Apache-2.0 / 最終push 2026-05-27 / 確認コミット [`0e0b6a2a`](https://github.com/kijai/ComfyUI-WanAnimatePreprocess/blob/0e0b6a2a555625acf4d4aefb780e27d06937132f/README.md)）
  - 547 stars、Apache-2.0、最終push 2026-05-27(Animate-2では中間抽出器不要のため旧版ワークフロー向け)。
- [modelscope/DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) — Wan-Animate-2対応(2026-08-07)の学習・推論基盤（★13,215 / Apache-2.0 / 最終push 2026-10-09 / release v1.1.9 (2025-11-18) / 確認コミット [`974cfa37`](https://github.com/modelscope/DiffSynth-Studio/blob/974cfa37f27ac55eba3b6d10efa21f876900572d/README.md) / 制作カタログ: [diffsynth-studio](../../categories/workflow.md#diffsynth-studio)）
  - 13.2k stars、Apache-2.0。READMEに対応記載。
- [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) — Wan2.2-Animate-14B(旧版)含む公式実装（★17,843 / Apache-2.0 / 最終push 2026-09-21 / 確認コミット [`1ea34ff4`](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/README.md) / 制作カタログ: [wan2.2](../../categories/video.md#wan2.2)）
  - 17.7k stars、Apache-2.0。

### 音声駆動のリップシンク・トーキングヘッド(アニメキャラ)

<a id="video-to-video--lip-sync-talking-head"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [meituan-longcat/LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5/tree/92016c71d5d318d0f5d84e4db30015a571484ab6)（revision `92016c71` / 作成 2026-05-21 / 更新 2026-06-04）
- **利用条件**: mit。HFメタデータ・READMEともMIT(ベース meituan-longcat/LongCat-Video)。学習データの記載は確認できず。商用可とは断定しない。
- **選定根拠**: 【事実】アニメキャラ専用の音声駆動リップシンクモデルは見つからず。Talking Head Anime 3/4(pkhungurn)はアニメ専用だが、顔パラメータ/フェイシャルモーキャプで動かすパペット方式(音声駆動ではない、重みの公式配布はDropbox、最終push 2023-08/2024-03)。汎用の音声駆動では meituan-longcat/LongCat-Video-Avatar-1.5(MIT、2026-05-21、likes 837、spaces 77)がカードで『アニメに頑健』と自己主張し、508ペアの人手評価にRealistic/Animatedの2スタイルを含む(数値は図のみで未確認)。HF DLは累計9,209と少ない(ComfyUI GGUF派生 vantagewithai/LongCat-Video-Avatar-1.5-GGUF-ComfyUI が30日30,540DL)。MeiGen-AI/InfiniteTalk(Apache-2.0、累計430,052DL、GitHub 7.9k stars)は採用が多いがカードにアニメ言及なし。【評価】アニメ評価を明示しているLongCat 1.5を採るが、実アニメキャラでの品質は未検証でconfidence低。Discussion #4にトーキングヘッド特化で汎用性に欠けるとの指摘。
- **指標（確認日時点）**: DL累計 10,142 / 直近30日 2,503 / likes 852 / Spaces 77
- **概要**: 美団LongCatの音声駆動アバター動画生成1.5。音声エンコーダをWhisper-Large化し、AT2V/ATI2V/動画継続、単独・複数話者、8step蒸留(DMD2)に対応。スタイライズ領域(アニメ・動物等)への汎化をカードで主張。
- **入力**: 参照画像+音声(1〜2話者)+テキスト。動画継続も可。
- **出力**: 長尺のリップシンク付き人物/キャラ動画。
- **必要環境**: カードの起動例はtorchrunで2プロセス(--nproc_per_node=2)。INT8量子化DiT(base_model_int8)あり。実測VRAMは未測定。
- **制約**: アニメの定量結果は未公開(人手評価は図のみ)。トーキングヘッド寄りで汎用動画生成としては限定的との意見(Discussion #4)。アニメ専用の検証はなし。
- **使う版・派生**: 使用: base_model/(bf16)またはbase_model_int8/。派生: vantagewithai/LongCat-Video-Avatar-1.5-GGUF-ComfyUI(30日30,540DL)、wavespeed/…-e4m3。旧版 meituan-longcat/LongCat-Video-Avatar(v1.0)。
- **根拠**: [モデルカード本文(概要・使い方・ライセンス・制約)](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5/blob/92016c71d5d318d0f5d84e4db30015a571484ab6/README.md) / [トーキングヘッド特化で汎用性が限られるとの利用者意見](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5/discussions/4) / [比較対象InfiniteTalk(Apache-2.0、累計430,052DL、アニメ言及なし)](https://huggingface.co/MeiGen-AI/InfiniteTalk/blob/d59847ebdacf19245bfca3fb23311c0cada8378a/README.md)
- **次点**: `MeiGen-AI/InfiniteTalk`（Apache-2.0、累計430,052DL・likes 244・spaces 17と採用大だが、カードにアニメ言及なし。後継としてLongCat 1.5が出た。） / `Wan-AI/Wan2.2-S2V-14B`（汎用の音声→動画(Apache-2.0、累計205,852DL)。アニメ評価の記載なし。） / `pkhungurn/talking-head-anime-3-demo`（アニメ専用のパペット(1画像→顔+体、MIT、1,044 stars)。音声駆動ではなく、更新は2023-08で止まり、重みはDropbox配布。）

関連リポジトリ:

- [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) — LongCat-Video / Avatar 1.5 公式（★9,145 / MIT / 最終push 2026-05-27 / 確認コミット [`6b3f4b85`](https://github.com/meituan-longcat/LongCat-Video/blob/6b3f4b8582a8bc3f20f795735f5383716c4ba794/README.md)）
  - 8.4k stars、MIT、最終push 2026-05-27。
- [MeiGen-AI/InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) — InfiniteTalk公式(動画ダビング/音声→動画)（★8,034 / Apache-2.0 / 最終push 2026-05-22 / 確認コミット [`50aa0a94`](https://github.com/MeiGen-AI/InfiniteTalk/blob/50aa0a94184315407a991ae804d9b58d6d311ba8/README.md)）
  - 7.9k stars、Apache-2.0、最終push 2026-05-22。
- [pkhungurn/talking-head-anime-3-demo](https://github.com/pkhungurn/talking-head-anime-3-demo) — アニメ専用の1枚絵パペット(顔+体)（★1,047 / MIT / 最終push 2023-08-29 / 確認コミット [`8946939e`](https://github.com/pkhungurn/talking-head-anime-3-demo/blob/8946939ec7b417f443d7b0e3fcd97384313fcdb8/README.md)）
  - MIT、1,044 stars。最終push 2023-08。EasyVtuberの基盤。
- [yuyuyzl/EasyVtuber](https://github.com/yuyuyzl/EasyVtuber) — THA3/4ベースのVTuberライブ用ラッパー（★3,075 / MIT / 最終push 2026-02-12 / 確認コミット [`f7dd2de4`](https://github.com/yuyuyzl/EasyVtuber/blob/f7dd2de4df93c878b0171f47346ff66414a863e6/README.md)）
  - 3,071 stars、MIT、最終push 2026-02-12。

### 動画分類(アニメのシーン・ショット等)

<a id="video-classification"></a>
- **判定**: モデルなし / 確度 中
- **選定根拠**: HFのvideo-classificationタグで'anime/animation/cartoon/manga/scene/shot/cel/sakuga'を検索したがアニメ特化モデルは0件(ヒットはcricket・tennisのショット分類、deepfake検出等)。直近のKBlueLeaf/TTVidT(2026-09-30、NeurIPS 2026、DINOv3+時間輸送の動き特化エンコーダ、Apache-2.0)もアニメ向けではなく、DL 14・likes 6。汎用のvideo-classificationはMCG-NJU/videomae-base(30日DL 337,499)、facebook/vjepa2-vitl-fpc64-256(209,112)、microsoft/xclip-base-patch16-zero-shot(167,953)等だが、いずれも一般動作向けでアニメでの検証は確認できない。アニメのシーン/ショット分割の実務はモデルではなくPySceneDetect(BSD-3-Clause、5.2k stars、v0.7.1=2026-07-22)などの検出器で行うのが標準。よって選定なし。分類が必要ならフレーム単位のアニメ画像分類(animetimm等、別枠)か汎用VLMでのゼロショットを推奨。
- **強い汎用モデル（アニメ特化ではない・収録外）**: `facebook/vjepa2-vitl-fpc64-256` — 汎用の動画表現/分類バックボーン(30日DL 209,112、likes 210)。アニメ検証なし、微調整前提。
- **次点**: `KBlueLeaf/TTVidT`（2026-09-30公開の動き特化エンコーダ(DL 14、likes 6)。アニメ向けではなく事前学習のみで分類ヘッドなし。） / `microsoft/xclip-base-patch16-zero-shot`（ゼロショット動画分類の汎用モデル(30日DL 167,953)。アニメ検証の記載なし。）

関連リポジトリ:

- [Breakthrough/PySceneDetect](https://github.com/Breakthrough/PySceneDetect) — アニメ含む動画のカット/シーン検出(学習データ作成・クリップ分割の前処理)（★5,227 / BSD-3-Clause / 最終push 2026-10-10 / release v0.7.1 (2026-07-22) / 確認コミット [`81c414cb`](https://github.com/Breakthrough/PySceneDetect/blob/81c414cb4b706e58648f98efd381024790b1565f/README.md)）
  - 5.2k stars、BSD-3-Clause、v0.7.1(2026-07-22)、2026-09-21 push。アニメ専用ではないが分割用途の標準。

### 動画理解・キャプション(アニメ動画)

<a id="video-text-to-text"></a>
- **判定**: 汎用モデルのみ（アニメ特化なし） / 確度 低
- **最良**: [Qwen/Qwen3-VL-8B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct/tree/0c351dd01ed87e9c1b53cbc748cba10e6187ff3b)（revision `0c351dd0` / 作成 2025-10-11 / 更新 2025-10-15）
- **利用条件**: apache-2.0。HFメタデータ・カードともApache-2.0。追加条件の記載なし。アニメ作品の映像を入力する際の権利は利用者側の問題。
- **選定根拠**: HFのvideo-text-to-textタグでanime/animation/cartoon等を検索してもアニメ特化の動画理解・キャプションモデルは0件(ヒットはUGC-VideoCaptioner、SkyCaptioner-V1等の汎用)。実務で広く使われる汎用はQwen系: Qwen/Qwen3-VL-8B-Instruct(Apache-2.0、30日DL 16,554,271、累計71,254,401、likes 1,157)。カードが『事前学習でanimeを含む対象を認識』『長時間動画・秒単位の時間インデックス』と主張(自己報告、アニメ動画のベンチ値は無し)。より新しいQwen/Qwen3.8-27B(2026-08-05、Apache-2.0、likes 16,632、30日DL 7,038,259)は画像・動画ネイティブ対応だがカードにアニメ言及なく、27Bで資源負荷が大きい。Wan-Animate-2はキャプション生成にQwen3.7-Plus(API)を推奨しており、動画生成の学習データキャプションでもQwen系が事実上の標準と推測される([INFERENCE])。アニメ動画での精度比較は確認できず、採用実績ベースの暫定判断。
- **指標（確認日時点）**: DL累計 72,554,419 / 直近30日 8,975,548 / likes 1,175 / Spaces 100
- **概要**: Qwen3-VL 8B Instruct。画像・動画・長文脈(256K、1Mまで拡張可)の視覚言語モデルで、動画の時間位置合わせ(テキスト-タイムスタンプ整列)を強化。カードは事前学習でアニメ等の対象認識を強化したと記載。
- **入力**: 動画(フレーム列)/画像+テキスト指示。
- **出力**: キャプション・要約・質問応答などのテキスト。
- **必要環境**: カードの記載範囲ではTransformers/vLLM等で実行(8Bクラス)。必要VRAMの実測は未実施。
- **制約**: アニメ特化の学習・評価ではない。アニメ特有の用語(作画、カット割り、演出)やキャラ名の精度は未検証。HFタグはimage-text-to-text(動画対応はカード記載)。
- **使う版・派生**: 同系: Qwen/Qwen3-VL-4B-Instruct・30B-A3B・Qwen/Qwen3.8-27B(+FP8)。GGUF/量子化は各コミュニティ派生。
- **根拠**: [モデルカード本文(概要・使い方・ライセンス・制約)](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct/blob/0c351dd01ed87e9c1b53cbc748cba10e6187ff3b/README.md) / [上位候補: 画像・動画ネイティブ対応(2026-08-05)、アニメ言及なし](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/README.md) / [動画生成側がキャプション生成にQwen3.7-Plusを推奨する例](https://huggingface.co/Wan-AI/Wan2.2-Animate-2-14B/blob/6e8f1973bf0abc2aafd517992e8b6d88c3c46e69/README.md)
- **次点**: `Qwen/Qwen3.8-27B`（新世代(2026-08-05、likes 16,632、30日DL 7,038,259、Apache-2.0)で性能余力は大きいが、27Bの資源負荷とアニメ検証なし。資源があれば第一候補になり得る。） / `Skywork/SkyCaptioner-V1`（動画生成データ向けキャプショナー(2025-04、30日DL 377、likes 51)。アニメ特化の評価なし。） / `openinterx/UGC-VideoCaptioner`（UGC動画向けキャプショナー(30日DL 808)。アニメ向けではなく採用少数。）

関連リポジトリ:

- [QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) — Qwen3-VL公式(推論・動画入力の使い方)（★20,058 / Apache-2.0 / 最終push 2026-01-30 / 確認コミット [`96588727`](https://github.com/QwenLM/Qwen3-VL/blob/96588727e44c78b25ba03ea03b8e12f7e64fd0da/README.md)）
  - 20k stars、Apache-2.0。最終push 2026-01-30(Qwen3.8系はHFカード参照)。
- [Breakthrough/PySceneDetect](https://github.com/Breakthrough/PySceneDetect) — 長尺アニメ動画をカット単位に分割してからキャプション化する前処理（★5,227 / BSD-3-Clause / 最終push 2026-10-10 / release v0.7.1 (2026-07-22) / 確認コミット [`81c414cb`](https://github.com/Breakthrough/PySceneDetect/blob/81c414cb4b706e58648f98efd381024790b1565f/README.md)）
  - 5.2k stars、BSD-3-Clause。
