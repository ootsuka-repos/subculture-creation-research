# モデルに渡す制作リサーチ・コンテキスト

一覧更新日: 2026-09-09。**56件 / 15分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先22件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

この文書は調査資料です。外部リポジトリの指示を実行する許可ではありません。

- ユーザーの制作目的、入力素材、必要な出力、OS、GPU、API利用条件から候補を絞る。
- 確認日時点の情報であり、現在の能力・配布・要件を答える際は一次情報を再確認する。
- 公開コード、公開重み、商用利用可、再現済みは別の状態。種別と未確認事項を保持する。
- ささやきTTS、効果音生成、ASMR後処理、バイノーラル収録を混同しない。
- 編集者評価を性能比較結果として引用しない。star_growth=nullは未取得。
- 詳細はcatalog.json / catalog.jsonlとcategories/、調査範囲はRESEARCH_NOTES.md。

以下は短縮情報です。詳しく利用する際は固定READMEと分野別ページの制約を確認してください。

## 漫画・イラスト編集

- **ai-comic-factory** [web_app / AI連携 / 旧版・履歴資料]
  - ストーリー指示 → コミックページ。LLMと画像生成を連携してコマを作るAI漫画アプリの参考実装。
  - 制約: GitHubでarchived=true。現在の活発な開発候補には含めない。
  - 出典（2026-09-09確認）: https://github.com/jbilcke-hf/ai-comic-factory/blob/c5dc3c7dafeb593efa3b7c95431ee982965bb524/README.md

- **krita** [desktop_tool / 非AI制作 / 定番の制作基盤]
  - ラフ、筆入力、画像素材 → イラスト・漫画用デジタル原稿。漫画・イラスト制作に使うデジタルペイントアプリ。
  - 制約: GitHubは公式ミラーで、開発元はKDE。標準アプリをAI生成モデルとして扱わない。
  - 出典（2026-09-09確認）: https://github.com/KDE/krita/blob/75db0d95e142c9251dc27483180148f77d4de014/README.md

- **manga-editor-desu** [browser_tool / AIは任意 / 更新のある導入・評価候補]
  - 画像、セリフ、コマ割り、生成指示 → 漫画ページ・複数ページの編集プロジェクト。ブラウザでコマ割り、吹き出し、縦書き、レイヤー編集とAI生成連携を行う。
  - 制約: 文字・吹き出しやページ切り替え時の編集履歴などは実作業で確認が必要。
  - 出典（2026-09-09確認）: https://github.com/new-sankaku/manga-editor-desu/blob/04e0cf3de1f3677682f6d1831f2713db70e441ba/README.md

- **OpenKoma** [browser_tool / 非AI制作 / 小規模・初期評価候補]
  - キャラ画像、背景、セリフ → 漫画ページPNG、PDF、プロジェクトJSON。手持ち画像をコマに配置し、複数ページの漫画に組み立てる編集ツール。
  - 制約: 小規模な新規候補。AI画像モデルそのものは含まない。
  - 出典（2026-09-09確認）: https://github.com/Reuben-Sun/OpenKoma/blob/aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c/README.md

## シナリオ・キャラクター・絵コンテ

- **BlueFish** [web_app / AI連携 / 小規模・初期評価候補]
  - 脚本、参照キャラ・背景 → 絵コンテ、生成動画、編集用素材。複数のAIプロバイダを接続し、脚本から絵コンテ・動画制作まで管理する。
  - 制約: 小規模な初期候補。mock動作と実際の生成完了を区別する。ローカルUIはローカル推論を意味しない。
  - 出典（2026-09-09確認）: https://github.com/bluefish2026/BlueFish/blob/8b409c1332e46bc1211d2ffc6d45fe1f01492eca/README.md

- **SillyTavern** [web_app / AI連携 / 更新のある導入・評価候補]
  - キャラクター設定、世界設定、会話 → キャラ会話、設定・ログ、連携した画像や音声。キャラ設定とLorebookを使い、LLMとの対話や世界観の試作を行うフロントエンド。
  - 制約: 完成シナリオの整合性を自動保証するものではない。独自LLM重みは提供しない。
  - 出典（2026-09-09確認）: https://github.com/SillyTavern/SillyTavern/blob/8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8/.github/readme.md

## ゲーム・ノベル・スプライト

- **Godot** [engine / 非AI制作 / 定番の制作基盤]
  - 2D/3D素材、シーン、スクリプト → 実行可能なゲーム。2D/3Dゲーム制作と複数プラットフォームへの出力を行うゲームエンジン。
  - 制約: AI素材生成機能そのものではない。配布先ごとのビルド要件は別途確認。
  - 出典（2026-09-09確認）: https://github.com/godotengine/godot/blob/9552dfb6859a1aaba1e570b8e0ef5c599b830f19/README.md

- **Pixelorama** [desktop_tool / 非AI制作 / 定番の制作基盤]
  - ピクセルアート、フレーム、タイル素材 → スプライト、タイル、アニメーション。ドット絵・タイル・アニメーションを編集する制作アプリ。
  - 制約: AI画像生成モデルを内蔵するという意味ではない。
  - 出典（2026-09-09確認）: https://github.com/Orama-Interactive/Pixelorama/blob/9263cf3636efc336aadbcc46c57dc614e57525b0/README.md

- **PNGAL** [desktop_tool / AI連携 / 導入経路の追加確認が必要]
  - 透過PNG、Photoshop互換PSD → PSD、WebM、MP4、GIF、スプライトシート、JSON。顔差分生成・PSD分解・目パチと口パクの補間を組み合わせ、立ち絵アニメ素材を制作する。
  - 制約: 音声入力・顔追跡・マウス追従は非対応。正式配布ZIPのURLはREADMEに記載なし。
  - 出典（2026-09-09確認）: https://github.com/1mm-module/PNGAL/blob/7a00caec16e8e9d6734f3ee5264118f44aec157c/README.md

- **RenPy** [engine / 非AI制作 / 定番の制作基盤]
  - シナリオ、立ち絵、背景、音声 → ビジュアルノベル・アドベンチャーゲーム。テキストとキャラクター素材を組み合わせたノベルゲームを制作する。
  - 制約: LLMシナリオ生成器ではない。生成した素材をゲームへ組み込むためのエンジン。
  - 出典（2026-09-09確認）: https://github.com/renpy/renpy/blob/f6a68a3a77014eca58c799d6663ccae733e5e10f/README.rst

- **sprite-maker** [desktop_tool / AI連携 / 初期評価候補]
  - スプライト画像、制作指示、関節設定 → アニメーションフレーム、PNGシート、メタデータ。AIエージェントと連携して素材を作り、関節・ボーンとRust描画で再現可能なアニメーションを生成する。
  - 制約: 初期段階。全OSでの導入成功や生成品質は未検証。
  - 出典（2026-09-09確認）: https://github.com/JohnKinyanjui/sprite-maker/blob/336c7114f0fce7336ec17f6e9beb93980ed03b1d/README.md

## アニメ制作・中割り・彩色・リップシンク

- **ECCV2022-RIFE** [model / AIモデル・学習 / 比較・既存工程の参考]
  - 前後の画像・動画フレーム → 補間フレーム・高フレームレート動画。フレーム間の中間画像を推定する動画補間モデル。
  - 制約: 作者がアニメ向けモデルを案内。原画の演技設計やタイミングを自動で正しく決めるものではない。
  - 出典（2026-09-09確認）: https://github.com/hzwer/ECCV2022-RIFE/blob/5d8adbdd40e12c2c8f91930eff838aebe561c086/README.md

- **LatentSync** [model / AIモデル・学習 / 比較・既存工程の参考]
  - 顔が映った動画、音声 → リップシンク済み動画。音声条件で口の動きを同期させる動画処理モデル。
  - 制約: READMEにアニメ例はあるが、任意の二次元顔への適合性は未検証。更新は2025年中心。
  - 出典（2026-09-09確認）: https://github.com/bytedance/LatentSync/blob/a229c3948406bc2cf6eaf4873e662e70c6a04746/README.md

- **opentoonz** [desktop_tool / 非AI制作 / 定番の制作基盤]
  - 線画、画像素材、タイムシート → 2Dアニメーション作品。作画、彩色、撮影を扱う2Dアニメ制作アプリ。
  - 制約: 生成AIモデルそのものではない。既存の制作工程への適合性を確認する。
  - 出典（2026-09-09確認）: https://github.com/opentoonz/opentoonz/blob/1ef22259b9cf64c9d8710daebc131b401932e81b/README.md

- **ToonComposer** [model / AIモデル・学習 / 研究・技術評価候補]
  - キーフレーム・スケッチ等の制作条件 → 彩色されたアニメーション動画。キーフレーム後の中割りと彩色を生成AIでまとめて処理する。
  - 制約: 最終pushは2025年8月。最近の開発活発度は低く、研究上の有望性と区別する。
  - 出典（2026-09-09確認）: https://github.com/TencentARC/ToonComposer/blob/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c/README.md

## 2Dキャラクター・自動リギング

- **Anime2.5DRig** [browser_tool / AIは任意 / 導入候補]
  - パーツ分けPSD → リアルタイム2.5Dアバター、設定JSON、透過PNG、OBS表示。PSDからリグを自動構成し、目パチ・口パク・髪物理・顔追跡で動かす。
  - 制約: 入力PSDのレイヤー構造に依存。動作品質は未検証。
  - 出典（2026-09-09確認）: https://github.com/852wa/Anime2.5DRig/blob/7450341934a8ff77bf05b90d9f708786e3eb3996/README.md

- **PuppetLoom** [desktop_tool / AI連携 / 要再確認]
  - レイヤー付きPSD → リグ付きプロジェクト、Web/OBS用出力、WebM。PSDから初期リグを作成し、外部エージェントとCLIで検証・調整しながら動く2Dキャラクターを制作する。
  - 制約: 専門的Live2D制作と同等ではない。moc3はCubism Editorでの出力が必要。READMEのApache-2.0表記とGitHub APIのAGPL-3.0判定が不一致のため利用条件は要再確認。
  - 出典（2026-09-09確認）: https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/README.md

- **stretchystudio** [browser_tool / AI連携 / 導入候補]
  - See-through形式の分割PSD → メッシュ変形アニメーション。PSDを読み込み、自動リギングとタイムライン上のメッシュ変形でアニメーションを編集する。
  - 制約: 最終pushは2026年4月。最近の活発な更新とは扱わない。
  - 出典（2026-09-09確認）: https://github.com/MangoLion/stretchystudio/blob/24a83a27ba43e43e9d2e3de5e33994594e6199c2/README.md

## レイヤー分解

- **ComfyUI-See-through** [integration / AI連携 / ComfyUI利用者向け]
  - アニメイラスト → 分解レイヤー、PSD。See-throughによる分解をComfyUIのノード工程へ接続する。
  - 制約: 独立した分解モデルではない。GitHub APIはルートのライセンスを判定できていない。
  - 出典（2026-09-09確認）: https://github.com/jtydhr88/ComfyUI-See-through/blob/98d754bf04f668647919ab750eccb0e0640faa81/README.md

- **Qwen-Image-Layered** [model / AIモデル・学習 / 基盤技術候補]
  - 汎用画像 → 複数RGBAレイヤー、PSD、ZIP、PPTX。画像を複数の編集可能なレイヤーに分解し、個別の色・位置・サイズ変更につなげる。
  - 制約: アニメ専用の可動パーツ分解ではない。最終pushは2025年12月。
  - 出典（2026-09-09確認）: https://github.com/QwenLM/Qwen-Image-Layered/blob/54c4fe47e76d745775e03fc66ee38457280ed9ea/README.md

- **see-through** [model / AIモデル・学習 / 導入候補]
  - アニメキャラクターの一枚絵 → 最大23レイヤーのPSD、深度・マスク。一枚絵を意味別パーツへ分解し、遮蔽部分を補完してPSDに出力する。
  - 制約: 分解が対象であり、リギングや専門家による可動構造設計は別工程。
  - 出典（2026-09-09確認）: https://github.com/shitagaki-lab/see-through/blob/7f139bb25c46a0c8ac720d95ddab185fcda5451c/README.md

## 画像生成・編集・切り抜き

- **anime-segmentation** [model / AIモデル・学習 / 比較・既存工程の参考]
  - アニメキャラクター画像 → 背景除去画像・マスク。アニメ絵のキャラクター領域を抽出し、背景除去や合成用マスクを作る。
  - 制約: レイヤー分解や隠れた身体部位の補完ではない。最近の更新は少ない。
  - 出典（2026-09-09確認）: https://github.com/SkyTNT/anime-segmentation/blob/55d874013a2811cdf59c365059174c7823acf5b4/README.md

- **krita-ai-diffusion** [integration / AI連携 / 更新のある導入・評価候補]
  - Kritaのキャンバス、選択範囲、プロンプト → 編集レイヤー・生成画像。Kritaの描画工程へ画像生成・インペイント・アウトペイントを組み込む。
  - 制約: 生成モデルとサービスによって費用・実行環境が変わる。
  - 出典（2026-09-09確認）: https://github.com/Acly/krita-ai-diffusion/blob/dda58d1c63e361207ccec085efbc34dbd32f1654/README.md

- **Qwen-Image** [model / AIモデル・学習 / 研究モデルの評価候補]
  - テキスト、編集対象画像 → 生成・編集画像。テキスト描画と画像編集を扱う汎用画像モデル群。表紙・小物・宣伝画像の制作候補。
  - 制約: 2.0の告知と公開重みの版を混同しない。本調査の重み候補は2512とEdit-2511。
  - 出典（2026-09-09確認）: https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/README.md

- **Z-Image** [model / AIモデル・学習 / 研究モデルの評価候補]
  - テキスト、モデルによって画像条件 → 生成・編集画像。6B級の汎用画像モデル群。Turboやベースモデルを用途に合わせて利用する。
  - 制約: アニメ専用ではない。Turbo・Base・Omni等の能力と公開範囲を分ける。
  - 出典（2026-09-09確認）: https://github.com/Tongyi-MAI/Z-Image/blob/26f23eda626ffadda020b04ff79488e1d72004cd/README.md

## 動画生成

- **LTX-2** [model / AIモデル・学習 / 更新のある導入・評価候補]
  - テキスト、参照画像・制御条件 → 音声と映像を伴う動画。音声・動画生成とLoRA学習を扱う公式実装。READMEはLTX-2.5の導入も案内する。
  - 制約: LTX-2と2.5の版・必要モデル・利用条件を分ける。全環境での動作は未検証。
  - 出典（2026-09-09確認）: https://github.com/Lightricks/LTX-2/blob/a95ab856bf29407b6b066ede0abe1846050db56c/README.md

- **LTX-Video** [model / AIモデル・学習 / 旧版・履歴資料]
  - テキスト、参照画像 → 動画。LTXの旧世代動画生成実装。
  - 制約: 公式READMEはLTX-2への移行を案内。現在の主開発先として推薦しない。
  - 出典（2026-09-09確認）: https://github.com/Lightricks/LTX-Video/blob/4b2d053057623ddd4d0a1d3e9cd28890e9ef487f/README.md

- **SCAIL-2** [model / AIモデル・学習 / 研究・技術評価候補]
  - 参照画像、動作動画、対応マスク、プロンプト → キャラクター動画、キャラ置換動画。参照キャラクターに動画の動きを移し、複数参照やキャラクター置換にも対応する。
  - 制約: アニメ専用ではない。入力マスクが重要で、複数参照は品質低下の場合がある。
  - 出典（2026-09-09確認）: https://github.com/zai-org/SCAIL-2/blob/78fe19576bb06be96c2375e088574a262a300edb/README.md

- **Wan2.2** [model / AIモデル・学習 / 研究モデルの評価候補]
  - テキスト、画像等の条件 → 生成動画。テキストや画像から動画を作るWan2.2公式モデル群。
  - 制約: アニメ専用ではない。5BとA14B等の機能・メモリ要件を一括りにしない。
  - 出典（2026-09-09確認）: https://github.com/Wan-Video/Wan2.2/blob/42bf4cfaa384bc21833865abc2f9e6c0e67233dc/README.md

## 3D生成・モデリング・リギング

- **Blender** [desktop_tool / 非AI制作 / 定番の制作基盤]
  - 3D形状、材質、リグ、モーション等 → 3Dモデル、レンダリング画像、アニメーション。モデリング、リギング、アニメ、レンダリング、合成を扱う統合制作環境。
  - 制約: GitHubは公式ミラー。非AIの汎用3Dツールとしてキャラ・アニメ制作に関連付ける。
  - 出典（2026-09-09確認）: https://github.com/blender/blender/blob/d0d7c4c861463ae8823a545c022db869c0858f66/.github/README.md

- **Hunyuan3D-2.1** [model / AIモデル・学習 / 比較・既存工程の参考]
  - 画像 → PBR材質付き3Dアセット。画像から3D形状と材質を生成する公式実装。
  - 制約: 2025年公開版。制作で使う際は形状・材質・リグを個別に確認する。
  - 出典（2026-09-09確認）: https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1/blob/82920d643c0dc2f7bfd7255f45f62d386edfe60c/README.md

- **SkinTokens** [model / AIモデル・学習 / 研究モデルの評価候補]
  - 3Dメッシュ → 骨格階層・スキンウェイト付き3Dアセット。TokenRigで骨格とスキンウェイトを一つの系列として生成する自動リギング研究。
  - 制約: 自動リグの実用性は対象メッシュごとに確認が必要。
  - 出典（2026-09-09確認）: https://github.com/VAST-AI-Research/SkinTokens/blob/273b691d35989d71cd17ff2895fdc735097b92d1/README.md

- **TRELLIS.2** [model / AIモデル・学習 / 研究モデルの評価候補]
  - 画像 → PBR材質を伴う3Dアセット。画像から形状・材質を備えた3Dアセットを生成する4Bモデル。
  - 制約: 生成だけでゲーム向けトポロジーやリグが完成するわけではない。
  - 出典（2026-09-09確認）: https://github.com/microsoft/TRELLIS.2/blob/75fbf0183001ed9876c8dbb35de6b68552ee08bd/README.md

- **UniRig** [model / AIモデル・学習 / 比較・既存工程の参考]
  - 3Dメッシュ → 骨格とスキンウェイト。形状から骨格推定とスキニングを行う自動リギング研究。
  - 制約: 後継版の能力をこの実装へ混ぜない。実際の変形品質は未検証。
  - 出典（2026-09-09確認）: https://github.com/VAST-AI-Research/UniRig/blob/6793c6640ff01c8fb389f3993434124bb43d2933/README.md

## TTS・キャラクター音声

- **fish-speech** [model / AIモデル・学習 / 更新のある導入・評価候補]
  - テキスト、参照音声 → 合成音声。Fish Audio S2系の表現豊かなTTS・音声クローンを扱う実装。
  - 制約: READMEはFISH AUDIO RESEARCH LICENSEと記載。過去版のライセンスを現在版へ適用しない。
  - 出典（2026-09-09確認）: https://github.com/fishaudio/fish-speech/blob/befe4001745417f8c42131739d862b8a6fdbd15a/README.md

- **GPT-SoVITS** [model_toolkit / AIモデル・学習 / 更新のある導入・評価候補]
  - テキスト、参照音声、学習音声 → 音声合成・追加学習モデル。少量音声を使うTTSと音声クローンをWebUIから扱う。
  - 制約: 参照音声の長さと品質で結果が変わる。作者の少量学習品質は未再現。
  - 出典（2026-09-09確認）: https://github.com/RVC-Boss/GPT-SoVITS/blob/48b1a0169a28582a8984402f82cf438d3bfa6aca/README.md

- **Qwen3-TTS** [model / AIモデル・学習 / 研究モデルの評価候補]
  - テキスト、声の説明、参照音声 → 合成音声。声のデザイン、参照音声による合成、指示による話し方制御を扱う多言語TTS。
  - 制約: 通常TTSの表現制御とASMR専用性能を同一視しない。
  - 出典（2026-09-09確認）: https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/README.md

- **Style-Bert-VITS2** [model_toolkit / AIモデル・学習 / 比較・既存工程の参考]
  - テキスト、音声スタイル、学習音声 → 読み上げ音声・追加学習モデル。Bert-VITS2を基に音声スタイルの制御と学習を扱う日本語TTSツール。
  - 制約: コードとデフォルト音声モデルの利用条件を分ける。最近の更新は少ない。
  - 出典（2026-09-09確認）: https://github.com/litagin02/Style-Bert-VITS2/blob/66de777e06392c0f313600be03c43ef96658b244/README.md

- **voicevox** [desktop_tool / AI連携 / 定番の制作基盤]
  - 日本語テキスト、話者・抑揚設定 → 読み上げ音声。日本語のキャラクター音声を編集して出力するVOICEVOXのエディタ。
  - 制約: このリポジトリはエディタ。エンジン・音声ライブラリ・キャラの条件は別。
  - 出典（2026-09-09確認）: https://github.com/VOICEVOX/voicevox/blob/b7258250fe90c82f112d0f51e43f2a1b67992d36/README.md

## ASMR・効果音・環境音

- **ASMRify** [desktop_tool / AI出力の後処理 / 小規模・初期評価候補]
  - 録音またはTTS音声ファイル → 効果処理したWAV・MP3。音声に定位移動・残響・ピッチ等を加えて一括処理するASMR向け音声加工ツール。
  - 制約: 小規模で利用実績は未確認。AIによるささやき生成・実録バイノーラルの再現・効果効能は確認していない。
  - 出典（2026-09-09確認）: https://github.com/ReactorcoreGames/ASMRify/blob/5f30fc61e6148a537cdc609173880e2d50ae3b53/README.md

- **FoleyCrafter** [model / AIモデル・学習 / 研究モデルの評価候補]
  - 無音動画、テキスト条件 → 動画に合わせた効果音。動画の内容とタイミングに合わせた効果音を生成する研究実装。
  - 制約: ASMR専用ではなく、距離感・耳元表現・立体音響は未検証。
  - 出典（2026-09-09確認）: https://github.com/open-mmlab/FoleyCrafter/blob/b4526d1586aaf044140b359295504452297f8c13/README.md

- **MMAudio** [model / AIモデル・学習 / 研究モデルの評価候補]
  - 動画、テキスト → 同期音声。動画やテキストを条件に、時間的に対応する音声を生成する。
  - 制約: ASMRや日本語のセリフ生成専用ではない。音の同期と内容は素材ごとに評価する。
  - 出典（2026-09-09確認）: https://github.com/hkchengrex/MMAudio/blob/974010a026c731054592d8f777218bd9d85a6c24/README.md

- **stable-audio-tools** [model_toolkit / AIモデル・学習 / 更新のある導入・評価候補]
  - テキスト条件、音声、モデル設定 → 生成音声・学習済みモデル。条件付き音声生成モデルの学習と推論を行うツール群。効果音や環境音素材を検討できる。
  - 制約: ASMR専用モデルではない。空間音響・ささやきの品質は未検証。
  - 出典（2026-09-09確認）: https://github.com/Stability-AI/stable-audio-tools/blob/3241adba4fc2a85cf5b29d9eb68d42f40a28e820/README.md

## 音楽・歌声合成

- **ACE-Step-1.5** [model / AIモデル・学習 / 更新のある導入・評価候補]
  - 楽曲説明、歌詞、参照音声等 → 楽曲・歌声を含む音声。ローカルで楽曲を生成し、編集や追加学習につなげる音楽モデル。
  - 制約: 作者の速度・商用モデル比較は当カタログで再検証していない。
  - 出典（2026-09-09確認）: https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/README.md

- **DiffSinger** [model_toolkit / AIモデル・学習 / 更新のある導入・評価候補]
  - 音符、歌詞、音声データ、表現パラメータ → 合成歌声・音声モデル。歌声合成の学習・推論と、ピッチ・エネルギー・息成分などの制御を扱う。
  - 制約: 原論文実装の拡張版。OpenUtau等のエディタと音源の対応は別途確認。
  - 出典（2026-09-09確認）: https://github.com/openvpi/DiffSinger/blob/336cf01b57f2ad44c6b37a79cf33993043291759/README.md

- **OpenUtau** [desktop_tool / AIは任意 / 定番の制作基盤]
  - 音符、歌詞、音源ライブラリ → 合成歌声・歌唱プロジェクト。UTAUコミュニティ向けの歌声編集・合成プラットフォーム。
  - 制約: エディタと音源・合成モデルの条件を分ける。公式リポジトリはopenutau/OpenUtauへ移転。
  - 出典（2026-09-09確認）: https://github.com/openutau/OpenUtau/blob/17bf25e7f78c5f88a6c5bce437bf6d592f012e46/README.md

## VTuber・AIキャラクター・VRM

- **AIRI** [web_app / AI連携 / 更新のある導入・評価候補]
  - 音声、キャラ設定、ゲーム等の入力 → 会話音声、2D/3Dキャラ表示、対応ゲーム操作。会話するバーチャルキャラクターを構築する環境。
  - 制約: 対応機能はプラットフォームとプロバイダに依存。全ゲームで自律動作するという意味ではない。
  - 出典（2026-09-09確認）: https://github.com/moeru-ai/airi/blob/dfc6951a55bf4fdd66a68a0c881ae880ddd95f77/README.md

- **inochi-creator** [desktop_tool / 非AI制作 / 比較・既存工程の参考]
  - レイヤー付き2Dキャラ素材 → Inochi2Dのリグ付きモデル。レイヤー画像を変形させ、ゲームやVTuberで動かす2Dモデルを作るエディタ。
  - 制約: 最終pushは2025年6月。Live2D Cubism形式と同じものではない。
  - 出典（2026-09-09確認）: https://github.com/Inochi2D/inochi-creator/blob/dba60811cff224f8cc9ce367b1d9291bfa5f7640/README.md

- **Open-LLM-VTuber** [web_app / AI連携 / 連携の評価候補]
  - マイク入力、視覚情報、キャラ設定 → 音声応答とLive2Dアバター表示。音声会話・視覚認識・Live2D表示を組み合わせるAIキャラクター環境。
  - 制約: ローカル完結はバックエンドの選択に依存。Live2Dモデル制作機能とは別。
  - 出典（2026-09-09確認）: https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/README.md

- **UniVRM** [library / 非AI制作 / 定番の制作基盤]
  - VRM・glTFアバター → Unityで読み書きできるアバター。Unity用のVRM形式実装。3Dアバターの読み込み・書き出しを扱う。
  - 制約: VRM 0.x/1.0等の互換性は個別確認。モデル生成・自動リギング機能ではない。
  - 出典（2026-09-09確認）: https://github.com/vrm-c/UniVRM/blob/928b30e96439c1c11a49b172efb72eb96d2cad8b/README.md

- **VTubeStudio** [api_reference / AI連携 / 連携用文書資料]
  - 外部プログラムのAPI要求 → VTube Studioのパラメータ制御・状態取得。VTube Studioを外部から制御する公式API文書・開発資料。
  - 制約: アプリ本体のソース公開ではない。文書リポジトリとして掲載。
  - 出典（2026-09-09確認）: https://github.com/DenchiSoft/VTubeStudio/blob/0f46ef44b487fa17c8120db572ebd925924b93a3/README.md

## 制作ワークフロー・追加学習

- **ComfyUI** [workflow_tool / AI連携 / 更新のある導入・評価候補]
  - ノードグラフ、プロンプト、素材、モデル → 画像・動画・音声などの生成物とワークフローJSON。画像・動画などのモデルをノードで接続して制作工程を構成する。
  - 制約: カスタムノードとモデルの互換性は個別確認が必要。ワークフロー公開だけで再現済みとはしない。
  - 出典（2026-09-09確認）: https://github.com/Comfy-Org/ComfyUI/blob/4989cdd95487531b50438c6a091dffa06e4af4b2/README.md

- **ComfyUI-WanVideoWrapper** [integration / AI連携 / 連携の評価候補]
  - ComfyUIグラフ、Wan系モデル、素材 → 生成動画と再利用可能なワークフロー。Wan系および関連動画モデルをComfyUIで使うためのラッパーノード。
  - 制約: 公式Wan実装ではない。対応版と既存ワークフローの互換性を確認する。
  - 出典（2026-09-09確認）: https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/088128b224242e110d3906c6750e9a3a348a659b/readme.md

- **musubi-tuner** [training_tool / AIモデル・学習 / 更新のある導入・評価候補]
  - 画像・動画データセット、キャプション、基盤モデル → LoRA等の追加学習結果。画像・動画モデル向けのLoRA学習スクリプト群。
  - 制約: 各モデル作者による公式実装ではない。対応するモデル版と学習素材を確認する。
  - 出典（2026-09-09確認）: https://github.com/kohya-ss/musubi-tuner/blob/e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1/README.md

## 字幕・翻訳・ローカライズ

- **manga-image-translator** [pipeline / AIモデル・学習 / 比較・既存工程の参考]
  - 漫画・イラスト画像 → 文字除去・翻訳・組版後の画像。画像内の文字を検出・認識・翻訳し、元の文字を修復して訳文を組版する。
  - 制約: 公式説明に公開Webデモの停止記載あり。縦書き・擬音・レイアウト保持の品質は素材で検証が必要。
  - 出典（2026-09-09確認）: https://github.com/zyddnys/manga-image-translator/blob/95227a2bb0fd306cd4f0c104d57284026f991b3a/README.md

- **VoiceTransl** [pipeline / AI連携 / 連携の評価候補]
  - 音声、動画、字幕 → 文字起こし、翻訳字幕、動画。音声認識、字幕翻訳、字幕と動画の処理を組み合わせる。
  - 制約: 同名forkと公式配布元を区別。声の生成機能ではない。
  - 出典（2026-09-09確認）: https://github.com/shinnpuru/VoiceTransl/blob/b5f7e5038763aeb3420ac872c0bd191112f92227/README.md

## 保留情報

DeepASMR（2026）は論文と音声デモを確認しましたが、対応する公式推論実装・重みは未特定です。実装公開済みとして推薦しないでください。詳細はreviewed-not-included.json。
