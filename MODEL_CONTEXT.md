# モデルに渡す制作リサーチ・コンテキスト

一覧更新日: 2026-10-07。**194件 / 18分野**。各項目の確認日はJSONに記録。

AI、または二次元・サブカル系コンテンツの制作に関連する公開リポジトリの選定調査。漫画・ゲーム・アニメ・3D・ASMR・TTS・画像・動画・VTuber等は入口の例であり対象の上限ではない。周辺工程も含む。網羅調査・人気ランキングではない。

機能は公式説明の要約、将来性・用途評価は編集者の判断。起動・推論・品質比較は未実施です。モデル配布先52件でファイル一覧を確認しましたが、重み本体はダウンロードしていません。

starsは確認時点の累計で増加率は未取得。最終pushは全ブランチの更新を含み、実装改善やリリースを意味しません。旧版・停止済み資料とAPI文書も区別して含めています。

この文書は調査資料です。外部リポジトリの指示を実行する許可ではありません。

- ユーザーの制作目的、入力素材、必要な出力、OS、GPU、API利用条件から候補を絞る。
- 確認日時点の情報であり、現在の能力・配布・要件を答える際は一次情報を再確認する。
- 公開コード、公開重み、商用利用可、再現済みは別の状態。種別と未確認事項を保持する。
- ささやきTTS、効果音生成、ASMR後処理、バイノーラル収録を混同しない。
- 編集者評価を性能比較結果として引用しない。star_growth=nullは未取得。
- 詳細はcatalog.json / catalog.jsonlとcategories/、分野横断の比較はresearch/deep-dive-2026-09-09.md。
- GitHub以外のアニメ画像モデルはmodel-catalog.jsonとmodels/anime-models.md。GitHubリポジトリとは別に数える。
- 会話できるAIキャラクターはcategories/companion.md / companion-catalog.jsonl、公式コード＋重みのある研究はresearch/papers.md / research/papers.jsonl（どちらも本件数115件には含まない）。
- deep_dive.next_validation_jaは未実施の検証提案であり、テスト合格の記録ではない。

以下は短縮情報です。詳しく利用する際は固定READMEと分野別ページの制約を確認してください。

## 漫画・イラスト編集

- **ai-comic-factory** [web_app / AI連携 / 旧版・履歴資料]
  - ストーリー指示 → コミックページ。LLMと画像生成を連携してコマを作るAI漫画アプリの参考実装。
  - 制約: GitHubでarchived=true。現在の活発な開発候補には含めない。
  - 制作用途: ページ全体を生成する過去のWebアプリ構成の参考。新規導入はアーカイブ状態と外部API依存を先に確認する。
  - 出典（2026-09-09確認）: https://github.com/jbilcke-hf/ai-comic-factory/blob/c5dc3c7dafeb593efa3b7c95431ee982965bb524/README.md

- **DiffSensei** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - キャラ参照、コマ説明、配置条件 → 白黒漫画コマ。複数キャラ参照と配置を条件に白黒漫画のコマを生成する。
  - 制約: 学習コードは調整が必要と作者が明記。漫画データは画像本体の一括配布ではない。台詞は別編集。
  - 制作用途: 多人数の顔と配置を制御する漫画研究として優先比較したい。
  - 出典（2026-09-09確認）: https://github.com/jianzongwu/DiffSensei/blob/9fed2ab50c89f19da12d7796edfa6a41eebf23c8/README.md

- **krita** [desktop_tool / 非AI制作 / 定番の制作基盤]
  - ラフ、筆入力、画像素材 → イラスト・漫画用デジタル原稿。漫画・イラスト制作に使うデジタルペイントアプリ。
  - 制約: GitHubは公式ミラーで、開発元はKDE。標準アプリをAI生成モデルとして扱わない。
  - 制作用途: 線・文字・トーンを人が確定する原稿の中心に置く。AI連携は別プラグインで選べる。
  - 出典（2026-09-09確認）: https://github.com/KDE/krita/blob/75db0d95e142c9251dc27483180148f77d4de014/README.md

- **manga-editor-desu** [browser_tool / AIは任意 / 更新のある導入・評価候補]
  - 画像、セリフ、コマ割り、生成指示 → 漫画ページ・複数ページの編集プロジェクト。ブラウザでコマ割り、吹き出し、縦書き、レイヤー編集とAI生成連携を行う。
  - 制約: 文字・吹き出しやページ切り替え時の編集履歴などは実作業で確認が必要。
  - 制作用途: 生成済み素材を編集可能なページへ配置する用途。画像生成器の選定とコマ編集UIの評価を分ける。
  - 出典（2026-09-09確認）: https://github.com/new-sankaku/manga-editor-desu/blob/04e0cf3de1f3677682f6d1831f2713db70e441ba/README.md

- **MangaNinja** [model / AIモデル・学習 / モデル・研究候補]
  - 線画、カラー参照、対応点 → 彩色画像。参照画像と点対応を使い、線画のキャラクターに指定色を反映する。
  - 制約: GitHub READMEはCC BY-NC 4.0表記、HFメタデータはApache-2.0で不一致。6GB案内は第三者Windows版。
  - 制作用途: 服・髪・小物の色を指定したいときの候補。ページ作成や台詞組版は別工程。
  - 出典（2026-09-09確認）: https://github.com/ali-vilab/MangaNinjia/blob/6363c81aaedab0a435d18cba9209a7e842881ad7/README.md

- **OpenKoma** [browser_tool / 非AI制作 / 小規模・初期評価候補]
  - キャラ画像、背景、セリフ → 漫画ページPNG、PDF、プロジェクトJSON。手持ち画像をコマに配置し、複数ページの漫画に組み立てる編集ツール。
  - 制約: 小規模な新規候補。AI画像モデルそのものは含まない。
  - 制作用途: PNG/PDFとプロジェクトJSONを併用し、画像だけの成果物から編集情報を保持する候補。
  - 出典（2026-09-09確認）: https://github.com/Reuben-Sun/OpenKoma/blob/aa8dbf3c64ce0254d8a335196d8f395c4c1ab99c/README.md

- **StoryDiffusion** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - シーン記述、キャラクター指定・参照 → 連続画像、漫画素材。キャラクターの一貫性を保つ注意機構で連続画像・漫画素材を生成する。
  - 制約: 動画モデルのソースと重みは現READMEのTODOで未公開。画像生成と動画研究の公開範囲を区別する。
  - 制作用途: 画像の連続性を比較する既存研究。動画公開済み候補としては使わない。
  - 出典（2026-09-09確認）: https://github.com/HVision-NKU/StoryDiffusion/blob/8de45e424887766fdd84dc917436ff8605f00149/README.md

- **Venera-SSR** [desktop_tool / AIモデル・学習 / 初期評価候補]
  - ローカルまたはネットワークの漫画画像・漫画源 → 着色・高解像度化・翻訳表示されたページ。複数の漫画源に対応する漫画ビューアに、ローカルの白黒漫画着色・Anime4K超解像・OCR翻訳を統合した改版リーダー。
  - 制約: 着色機能はテスト中の分支で追加モデルを検証中とREADMEが記載。権利面の注意も明記。
  - 制作用途: 漫画制作・確認時のラフな着色や文字置換の検討に利用。
  - 出典（2026-09-30確認）: https://github.com/Kiastr/Venera-SSR/blob/07ac77fcbd6c9050a5313f327e28d617eb602488/README.md

- **Manga-AI-detector** [model / AIモデル・学習 / 小規模・初期評価候補]
  - 漫画/コミックのページ画像（ファイルまたはbase64） → クラス名・confidence・bounding box・中心座標を含むJSON、可視化画像。漫画・マンファ・コミックページ向けに追加学習したYOLOv11インスタンスセグメンテーションモデル。コマ枠(panels)・吹き出し(bubbles)・本文テキスト(text)・効果音(SFX)の4要素を検出する。
  - 制約: 学習データの規模や精度指標（mAP等）はREADMEに記載がなく検出精度は未確認。REST API化のコードはREADME内のサンプル記載で、そのまま動く形では同梱されていない。
  - 制作用途: 漫画翻訳のコマ・吹き出し検出の候補として試せる。
  - 出典（2026-10-01確認）: https://github.com/nonillion-studios/Manga-AI-detector/blob/becb02ca3f2e5e01df4822045d001443442cf4ff/readme.md

- **manga-colorizer** [desktop_tool / AIモデル・学習 / 小規模・初期評価候補]
  - 白黒漫画ページ画像、任意のヒント点や参照カラー画像 → 彩色済み画像（Labのa/bのみ変更し、Lは原稿を保持）。白黒漫画（网点含む）の意味ベース自動彩色ツール。ONNXのSAM誘導ジェネレータで髪/肌/瞳/背景を配色し、Windowsデスクトップ（Tauri 2+Python）、ブラウザ、Dartエンジンで動作する。
  - 制約: モデル重みはCC BY-NC-SA 4.0でリポジトリ非同梱、別途ダウンロードが必要。コードはApache-2.0。
  - 制作用途: 漫画の彩色補助・ラフ彩色に使えるが、モデルの商用条件に注意。
  - 出典（2026-10-05確認）: https://github.com/Mobai0z0/manga-colorizer/blob/f1bbf26d434be05f66a0a5f66ab821a1fd10c78d/readme.md

## シナリオ・キャラクター・絵コンテ

- **BlueFish** [web_app / AI連携 / 小規模・初期評価候補]
  - 脚本、参照キャラ・背景 → 絵コンテ、生成動画、編集用素材。複数のAIプロバイダを接続し、脚本から絵コンテ・動画制作まで管理する。
  - 制約: 小規模な初期候補。mock動作と実際の生成完了を区別する。ローカルUIはローカル推論を意味しない。
  - 制作用途: 脚本から複数工程を管理する統合UIの初期候補。APIの実処理とデモ表示の差を評価する。
  - 出典（2026-09-09確認）: https://github.com/bluefish2026/BlueFish/blob/8b409c1332e46bc1211d2ffc6d45fe1f01492eca/README.md

- **ink** [library / 非AI制作 / 制作基盤として比較]
  - ink形式の会話・分岐シナリオ → コンパイル済み物語と進行状態。分岐する物語を書くスクリプト言語、コンパイラ、実行ランタイム。
  - 制約: LLMではない。画面演出・音声・立ち絵表示はホスト側で実装する。
  - 制作用途: 生成したシナリオを分岐・変数・セーブ可能な構造へ落とす工程に適する。
  - 出典（2026-09-09確認）: https://github.com/inkle/ink/blob/35c63e52f1d36060930dc7ed3cfba38ea224b528/README.md

- **SillyTavern** [web_app / AI連携 / 更新のある導入・評価候補]
  - キャラクター設定、世界設定、会話 → キャラ会話、設定・ログ、連携した画像や音声。キャラ設定とLorebookを使い、LLMとの対話や世界観の試作を行うフロントエンド。
  - 制約: 完成シナリオの整合性を自動保証するものではない。独自LLM重みは提供しない。
  - 制作用途: キャラ設定・世界設定の試演に使い、確定シナリオは別形式へ書き出して管理する。
  - 出典（2026-09-09確認）: https://github.com/SillyTavern/SillyTavern/blob/8172dcd0ee672d3cd9a5e5f7af134f91a45cd2b8/.github/readme.md

- **Yarn Spinner** [library / 非AI制作 / 制作基盤として比較]
  - Yarn会話スクリプト、変数、コマンド → 分岐会話の実行と台詞データ。ゲームの会話記述をコンパイル・実行する台詞制作基盤。
  - 制約: コアとUnity向け商品・統合の公開条件を分ける。AI脚本モデルではない。
  - 制作用途: 声付きNPC会話をエンジンの演出と結び付ける候補。
  - 出典（2026-09-09確認）: https://github.com/YarnSpinnerTool/YarnSpinner/blob/c39241c573167ea0157e48d8380c36920c5e50d8/README.md

- **YumingScroll** [web_app / AI連携 / 早期開発]
  - 物語テキスト/小説、人物・場景設定、ProviderのAPIキー → 分鏡脚本、人物/場景の参照画像、動画タスク、ギャラリー資産。物語テキストから世界観・人物・分鏡・画像/動画資産をひとつのプロジェクトにまとめるセルフホスト型AI漫劇制作ワークベンチ。Flow Mapで人物・場景・画風・15秒台本を接続する。
  - 制約: MockモードはUI検証用で生成品質の評価には使えない。実生成には外部Provider契約と費用が必要。単一ユーザー想定でアクセス制御なし。
  - 制作用途: 漫劇・縦型動画の企画から素材生成の試作。
  - 出典（2026-10-07確認）: https://github.com/tansuanyl/YumingScroll/blob/0255f68bba977599f06ec2f96ef7dcc9ad2732f6/README.md

## ゲーム・ノベル・スプライト

- **ControlTile** [model / AIモデル・学習 / 小規模・初期候補]
  - タイル生成条件、参照データ → タイル画像。条件付きの画像タイル生成を扱う研究実装。
  - 制約: 配布URLは確認したが、重みファイルの一覧・取得・推論は未検証。ゲームのマップ配置とは別。
  - 制作用途: タイルの連続性と制御を研究したい場合の小規模候補。
  - 出典（2026-09-09確認）: https://github.com/Junrongh/ControlTile/blob/f3410e843742335ae3fa3298d2b335509da18893/README.md

- **Godot** [engine / 非AI制作 / 定番の制作基盤]
  - 2D/3D素材、シーン、スクリプト → 実行可能なゲーム。2D/3Dゲーム制作と複数プラットフォームへの出力を行うゲームエンジン。
  - 制約: AI素材生成機能そのものではない。配布先ごとのビルド要件は別途確認。
  - 制作用途: 完成素材を操作・勝敗・セーブを備えるゲームにする基盤。素材生成の品質とゲームとしての完成度を別評価する。
  - 出典（2026-09-09確認）: https://github.com/godotengine/godot/blob/9552dfb6859a1aaba1e570b8e0ef5c599b830f19/README.md

- **LDtk** [desktop_tool / 非AI制作 / 制作基盤として比較]
  - タイル、エンティティ、レベル設計 → レベルデータと配置情報。2Dレベルを設計するオープンソースのエディタ。
  - 制約: マップを作る道具で、ゲームロジックは生成しない。
  - 制作用途: 小規模2Dゲームのレベル反復制作でTiledと比較したい。
  - 出典（2026-09-09確認）: https://github.com/deepnight/ldtk/blob/6d69bd1d6be92f01ac30778f6a934f0da8448b16/README.md

- **OpenGame** [pipeline / AI連携 / 連携・制作ツール候補]
  - ゲーム仕様、素材条件、利用モデル設定 → ゲームプロジェクトのコードと素材。指示からWebゲームを制作するエージェント基盤。テンプレートとデバッグ手順を組み込む。
  - 制約: GameCoder-27Bは説明されるが本調査で公式重みは未特定。評価パイプラインはREADMEで公開予定。
  - 制作用途: 遊べるゲームのコードを出す対象として、ゲーム風動画生成と区別して比較。
  - 出典（2026-09-09確認）: https://github.com/leigest519/OpenGame/blob/c9bea37786af524bf3bbe802f2b67d23816fa5c0/README.md

- **Pixelorama** [desktop_tool / 非AI制作 / 定番の制作基盤]
  - ピクセルアート、フレーム、タイル素材 → スプライト、タイル、アニメーション。ドット絵・タイル・アニメーションを編集する制作アプリ。
  - 制約: AI画像生成モデルを内蔵するという意味ではない。
  - 制作用途: ピクセル境界・パレット・フレームを編集し、AI生成素材をドット絵として整える候補。
  - 出典（2026-09-09確認）: https://github.com/Orama-Interactive/Pixelorama/blob/9263cf3636efc336aadbcc46c57dc614e57525b0/README.md

- **PNGAL** [desktop_tool / AI連携 / 導入経路の追加確認が必要]
  - 透過PNG、Photoshop互換PSD → PSD、WebM、MP4、GIF、スプライトシート、JSON。顔差分生成・PSD分解・目パチと口パクの補間を組み合わせ、立ち絵アニメ素材を制作する。
  - 制約: 音声入力・顔追跡・マウス追従は非対応。正式配布ZIPのURLはREADMEに記載なし。
  - 制作用途: 透過キャラの待機・ループをスプライトや映像素材にする用途。配信の顔追跡用途とは入力が異なる。
  - 出典（2026-09-09確認）: https://github.com/1mm-module/PNGAL/blob/7a00caec16e8e9d6734f3ee5264118f44aec157c/README.md

- **RenPy** [engine / 非AI制作 / 定番の制作基盤]
  - シナリオ、立ち絵、背景、音声 → ビジュアルノベル・アドベンチャーゲーム。テキストとキャラクター素材を組み合わせたノベルゲームを制作する。
  - 制約: LLMシナリオ生成器ではない。生成した素材をゲームへ組み込むためのエンジン。
  - 制作用途: 台詞・選択肢・立ち絵・音声を組み合わせるノベル制作の出力先。生成素材をrpyとアセットへ確定する。
  - 出典（2026-09-09確認）: https://github.com/renpy/renpy/blob/f6a68a3a77014eca58c799d6663ccae733e5e10f/README.rst

- **sprite-maker** [desktop_tool / AI連携 / 初期評価候補]
  - スプライト画像、制作指示、関節設定 → アニメーションフレーム、PNGシート、メタデータ。AIエージェントと連携して素材を作り、関節・ボーンとRust描画で再現可能なアニメーションを生成する。
  - 制約: 初期段階。全OSでの導入成功や生成品質は未検証。
  - 制作用途: 関節やフレームを扱う初期のスプライト制作候補。完成画像の見た目に加えてエクスポート形式を確認したい。
  - 出典（2026-09-09確認）: https://github.com/JohnKinyanjui/sprite-maker/blob/336c7114f0fce7336ec17f6e9beb93980ed03b1d/README.md

- **Terrain Diffusion** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 地形条件、地図レイヤー、生成範囲 → 標高・地形データ、TIFF等。広域地形を拡散モデルで生成し、地図から地形への変換も扱う。
  - 制約: 標高データの生成であり、完成したゲームレベル・衝突設定ではない。
  - 制作用途: RPG世界地図や3D背景の地形案を作る補助工程。
  - 出典（2026-09-09確認）: https://github.com/xandergos/terrain-diffusion/blob/e8dcb4b1a834ab2f6b1a6f5256ed7c9f2f3e8230/README.md

- **Tiled** [desktop_tool / 非AI制作 / 制作基盤として比較]
  - タイルセット、レイヤー、オブジェクト属性 → TMX等のマップデータ。タイルとオブジェクトを配置して2Dゲームのマップを作る。
  - 制約: ゲームの実行エンジンは別。独自属性の読み込みをゲーム側で実装する。
  - 制作用途: AI生成タイルを遊べる地形へ整理する工程の基盤。
  - 出典（2026-09-09確認）: https://github.com/mapeditor/tiled/blob/395619407b39a34fccf45dc9e6e7dd0c34b6feb5/README.md

- **character-animation-creator-skill** [workflow_tool / AIモデル・学習 / 小規模・初期評価候補]
  - キャラクターのテキスト指示、または参照画像 → スプライトシート（既定384×1536、6列×24行×64px）、コンタクトシート、検証JSON。Codex（OpenAI）およびGPT Web Agent向けのスキル。テキスト指定や参照画像から64×64ピクセルアートのキャラクタースプライトシートを、8方向×idle/walk/attackのアニメーション込みで生成し、パレット量子化や検証まで行う。
  - 制約: 64×64のピクセルアート前提。最終品質は画像生成バックエンド依存。ライセンスはMITとREADMEに記載。
  - 制作用途: 少ない手数でキャラのアニメーション素材を揃えたい小〜中規模のゲーム開発に向く。
  - 出典（2026-10-04確認）: https://github.com/tachikomared/character-animation-creator-skill/blob/9ce98dffb98c84488fe7b99b62c49fabee20abd6/README.md

- **spritebrew** [web_app / AIモデル・学習 / 稼働中・実運用候補]
  - テキストプロンプト、または既存のピクセルアート画像・スプライトシートPNG → スプライトシート、TexturePacker/Aseprite/GameMaker/RPG Maker MV・MZ/Godot SpriteFrames形式、フレームPNGのZIP。テキストや既存画像からピクセルアートのキャラクターを生成し、アニメーション化・スライス・プレビュー・エクスポートまで一貫して行うWebツール。21種のスタイルと複数エンジン向け書き出しに対応する。
  - 制約: AI生成はRetro DiffusionのAPI依存でトークン消費制。ローカル完結ではない。ライセンスはAGPL-3.0。
  - 制作用途: スプライト素材の生成〜書き出しを1ツールで完結させたい個人〜小規模チームに向く。
  - 出典（2026-10-04確認）: https://github.com/GAlbanese09/spritebrew/blob/8d55e758b4b76ac2c78222d83cc3eb9b933c7b1f/README.md

## アニメ制作・中割り・彩色・リップシンク

- **AniDoc** [model / AIモデル・学習 / モデル・研究候補]
  - 参照カラー画像、スケッチ列 → 彩色動画。設定画を参照してスケッチ列を彩色するアニメ制作研究。
  - 制約: 環境構築に複数モデルが必要。長いカットや作画の線の保持は未評価。
  - 制作用途: 完成画像から自由な動画を作る用途より、既存原画を使う彩色工程で比較したい。
  - 出典（2026-09-09確認）: https://github.com/robbyant-research/AniDoc/blob/77e0696cea9df7bb1cd2c254ba21639d3a6ab8f8/README.md

- **AnimeColor** [model / AIモデル・学習 / 小規模・初期候補]
  - 参照カラー画像、スケッチ動画、キャプション → 彩色動画。設定画参照とスケッチ動画からアニメを彩色する拡散Transformer。
  - 制約: コードに低メモリ設定はあるが、任意GPUでの動作保証はない。動画全体の色一貫性は未評価。
  - 制作用途: AniDoc・BasicPBCと同じ線画で比較したい彩色候補。
  - 出典（2026-09-09確認）: https://github.com/IamCreateAI/AnimeColor/blob/76fb1f83628fa420fbab73967af7e6b74712ebbc/README.md

- **BasicPBC** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 線画、参照の彩色領域 → 対応領域と彩色結果。閉領域の対応付けによってアニメ線画の塗りを支援するペイントバケット彩色。
  - 制約: 実写ではなく線画の領域対応が中心。手描きデータの一部は非公開。配布重みの取得は未検証。
  - 制作用途: 線の輪郭を保ちながら塗り分けたい工程で、拡散モデルによる再描画との違いが明確。
  - 出典（2026-09-09確認）: https://github.com/ykdai/BasicPBC/blob/223bf783dea63770fcced4612ecf153883ce91cf/README.md

- **ECCV2022-RIFE** [model / AIモデル・学習 / 比較・既存工程の参考]
  - 前後の画像・動画フレーム → 補間フレーム・高フレームレート動画。フレーム間の中間画像を推定する動画補間モデル。
  - 制約: 作者がアニメ向けモデルを案内。原画の演技設計やタイミングを自動で正しく決めるものではない。
  - 制作用途: フレーム補間の比較基準。補間と演技の設計を分け、意図的なコマ打ちは保持する。
  - 出典（2026-09-09確認）: https://github.com/hzwer/ECCV2022-RIFE/blob/5d8adbdd40e12c2c8f91930eff838aebe561c086/README.md

- **LatentSync** [model / AIモデル・学習 / 比較・既存工程の参考]
  - 顔が映った動画、音声 → リップシンク済み動画。音声条件で口の動きを同期させる動画処理モデル。
  - 制約: READMEにアニメ例はあるが、任意の二次元顔への適合性は未検証。更新は2025年中心。
  - 制作用途: 台詞に口を合わせる後処理候補。人間の顔を前提とする検出が二次元絵で成立するかが入口になる。
  - 出典（2026-09-09確認）: https://github.com/bytedance/LatentSync/blob/a229c3948406bc2cf6eaf4873e662e70c6a04746/README.md

- **opentoonz** [desktop_tool / 非AI制作 / 定番の制作基盤]
  - 線画、画像素材、タイムシート → 2Dアニメーション作品。作画、彩色、撮影を扱う2Dアニメ制作アプリ。
  - 制約: 生成AIモデルそのものではない。既存の制作工程への適合性を確認する。
  - 制作用途: 原画・中割り・彩色結果をタイムシートに載せて仕上げる。AI動画をそのまま完成カットと扱わない制作経路。
  - 出典（2026-09-09確認）: https://github.com/opentoonz/opentoonz/blob/1ef22259b9cf64c9d8710daebc131b401932e81b/README.md

- **ToonComposer** [model / AIモデル・学習 / 研究・技術評価候補]
  - キーフレーム・スケッチ等の制作条件 → 彩色されたアニメーション動画。キーフレーム後の中割りと彩色を生成AIでまとめて処理する。
  - 制約: 最終pushは2025年8月。最近の開発活発度は低く、研究上の有望性と区別する。
  - 制作用途: 決定したキーフレームとスケッチを使う制作制御の候補。自由生成動画より入力作画の保持を重視して比較する。
  - 出典（2026-09-09確認）: https://github.com/TencentARC/ToonComposer/blob/53dc3df95eca4f6a2e3e4c9dea0160a339b12f1c/README.md

- **ToonCrafter** [model / AIモデル・学習 / モデル・研究候補]
  - 始点・終点画像、任意のスケッチ制御 → 中間フレームの動画。二枚のアニメ画像の間を生成する補間モデル。
  - 制約: 第三者の軽量化版と公式実装の必要メモリを混同しない。2025年から更新が少ない。
  - 制作用途: 二枚の決定原画の間を試作する比較基準。完成カットのタイミングは編集で決める。
  - 出典（2026-09-09確認）: https://github.com/Doubiiu/ToonCrafter/blob/b0c47ff339c5e5ec45b84d0c6587850f242d41ef/README.md

- **comic-manga-narrator** [pipeline / AIモデル・学習 / 小規模・初期評価候補]
  - 漫画ページ画像、PDF（章単位） → ナレーション付きMP4、中間ファイル（page.json / script.json / cast.json / timing.json）。漫画/コミックページを、コマ検出・セリフの音声化・ナレーション・Ken Burnsと2.5Dパララックスで演出したナレーション付きMP4に変換するローカルパイプライン。
  - 制約: 特定の自前スタック（Mushishi）を前提とした構成で、公開モデルへの差し替えはREADMEの範囲では未検証。Freesound APIキーは任意。READMEはライセンス表記がなく、権利条件は未確認。
  - 制作用途: 漫画の読み聞かせ・二創動画化の実験パイプラインとして試せる。
  - 出典（2026-10-01確認）: https://github.com/MushiSenpai/comic-manga-narrator/blob/38bac4fad34da68273de278a3fa85abc334b8308/README.md

- **vedGen** [pipeline / AIモデル・学習 / 小規模・初期評価候補]
  - あらすじ（premise）文、YAML設定、Comfy API形式のワークフローJSON → ショット別キーフレーム画像、ショット別クリップ、結合済みstory.mp4。一行のあらすじから絵コンテ→ショット別I2V→結合までをローカルGPUで回すアニメ風短編動画生成ライブラリ。ComfyUIをヘッドレスでAPI駆動し、Pythonライブラリとして呼び出す。
  - 制約: 既定ではインストールも重みDLも行わない。リポジトリは小規模・初期段階で、READMEにLICENSEファイルの実体はない。finalはT5をCPU/RAMへ逃がす構成を含む。
  - 制作用途: 短編のプリビズ／キーフレーム検討から動画化までの試作。
  - 出典（2026-10-02確認）: https://github.com/HarisUmer/vedGen/blob/596f32ade8967725a3f8c54ba00d0f7ab288112d/README.md

## 2Dキャラクター・自動リギング

- **Anime2.5DRig** [browser_tool / AIは任意 / 導入候補]
  - パーツ分けPSD → リアルタイム2.5Dアバター、設定JSON、透過PNG、OBS表示。PSDからリグを自動構成し、目パチ・口パク・髪物理・顔追跡で動かす。
  - 制約: 入力PSDのレイヤー構造に依存。動作品質は未検証。
  - 制作用途: ブラウザでPSDから動く立ち絵を作る候補。衣装や髪のレイヤー構造を入力仕様として管理する。
  - 出典（2026-09-09確認）: https://github.com/852wa/Anime2.5DRig/blob/7450341934a8ff77bf05b90d9f708786e3eb3996/README.md

- **PuppetLoom** [desktop_tool / AI連携 / 要再確認]
  - レイヤー付きPSD → リグ付きプロジェクト、Web/OBS表示、WebM、CMO3/MOC3等の直接出力経路。レイヤーPSDを自動バインドし、改訂履歴・検証を残して動く2Dキャラを制作する。
  - 制約: 専門的Live2D制作と同等ではない。現行中国語READMEとCLIにCubism直接出力経路があるが、実ファイル生成・互換性は未検証。英語・日本語READMEのApache表記がLICENSE/NOTICEのAGPLと不一致。
  - 制作用途: PSDから制作・校正の改訂履歴を残す自動化基盤。現行CLIのCubism直接出力も検証候補に含める。
  - 出典（2026-09-09確認）: https://github.com/CheshireMew/PuppetLoom/blob/f26c83dd31a48c644eb962971b9e21b9fa06f3f4/README.md

- **stretchystudio** [browser_tool / AI連携 / 導入候補]
  - See-through形式の分割PSD → メッシュ変形アニメーション。PSDを読み込み、自動リギングとタイムライン上のメッシュ変形でアニメーションを編集する。
  - 制約: 最終pushは2026年4月。最近の活発な更新とは扱わない。
  - 制作用途: 分解済みPSDをメッシュ変形に使う候補。See-through互換はレイヤー名だけでなく位置と遮蔽を試す。
  - 出典（2026-09-09確認）: https://github.com/MangoLion/stretchystudio/blob/24a83a27ba43e43e9d2e3de5e33994594e6199c2/README.md

- **psd2live** [desktop_tool / AIは任意 / 活発・候補]
  - パーツ別レイヤーのPSD、差分用の透明画像 → .cmo3、.moc3と.model3.json等のランタイム一式、.psd2live工程ファイル。レイヤー分けしたPSDからLive2Dモデルを自動生成し、同じ作業画面で修形・リギング・物理・アニメーション・書き出しまで行うデスクトップツール。
  - 制約: 自動生成の品質はPSDのレイヤー分けに依存し、書き出し成功が全ランタイムでの同一挙動を保証しないとREADMEが明記。
  - 制作用途: Live2Dモデルの初期リギングと物理設定の工数削減。
  - 出典（2026-09-30確認）: https://github.com/tsunehimatoi/psd2live/blob/a494c6e6d713640f7c07d2114998f80f638275cf/README.md

- **live2d-py** [library / 非AI制作 / 実運用段階のライブラリ]
  - Cubism 2.1／3.0以降のモデルファイル、モデルパラメータ、口パク用の音声 → OpenGLウィンドウへの描画、パラメータ・透明度操作の結果。Live2DモデルをPythonから直接読み込み・描画するC++拡張ライブラリ。Web Engineを挟まず、OpenGLコンテキストがあれば任意のOpenGLウィンドウに描画できる。
  - 制約: Cubism Coreを同梱できないため、ソースビルド時はSDKを自分で用意する必要がある。READMEにモーション編集やモデル制作機能の記載はない。
  - 制作用途: デスクトップコンパニオン／VTuberアプリの描画・口パク・クリック判定。
  - 出典（2026-10-02確認）: https://github.com/EasyLive2D/live2d-py/blob/35f686412470ea25718fa9c76ee4f1809f6a8506/README.md

- **ayagami** [library / 非AI制作 / 初期評価候補]
  - MOC3ファイル、テクスチャ、モデルパラメータ、ZIPアーカイブ（デモ） → ウィンドウ／テクスチャへの描画結果、任意パラメータでのポーズ。Live2D（MOC3）互換の2Dパペット読み込み・描画SDK。Rust実装で、wgpuベースのリファレンスレンダラとGodotコンポーネントを備える。
  - 制約: API未安定・ドキュメント未整備で、表情ファイル／ポーズファイル／モーションの対応はTODOのまま。現状PRは受け付けておらず、crates.io公開も未実施。
  - 制作用途: エンジンへ組み込みたい場合のLive2D描画層。
  - 出典（2026-10-02確認）: https://github.com/AyagamiDev/ayagami/blob/0d1d7aa3efe57b1b363b72e672e353c52a9c15d6/README.md

- **Amahane-Hikari-Live2D** [workflow_tool / AI連携 / 活発な候補]
  - 参考画像・Photoshopレイヤー、Live2D Cubism SDK for Web 5-r.5 → MOC3/MODEL3などのLive2Dモデル、WebGLプレビュー、制作Skill。AIエージェントと協働してLive2Dキャラクターを制作し、TypeScript/WebGLのWebランタイムで再生する制作プロジェクト。制作フローをSkillとして公開する。
  - 制約: キャラクター資産は自作のNo-AIライセンスで、AI/ML学習への利用が禁止。SDKは同梱されない。
  - 制作用途: Live2D制作の手順テンプレートと検証手法の参照元として使える。
  - 出典（2026-10-03確認）: https://github.com/luomo66ccff/Amahane-Hikari-Live2D/blob/246bbd195bf260e6e35f11c0c1c24fdc1b3d097d/README.md

- **live2d-agent-kit** [workflow_tool / AI連携 / 小規模・初期評価候補]
  - 参考画像、分层PSD/PNGレイヤー、Live2D公式Core → PSD/CMO3/MOC3、図集、パラメータと物理、WebGLプレビュー、運行パッケージ。coding agentが参考図や分层PSDから.moc3を作るためのLive2D制作キット。psd2liveアダプタ、アニメ超分スクリプト、検証手順を含む。
  - 制約: 肩・腕・指の独立绑定は実装範囲外。示例資産はCC BY 4.0で、作者はLive2D社と無関係と明記。
  - 制作用途: Live2D绑定の初期検証と手順の型として使える。
  - 出典（2026-10-03確認）: https://github.com/Ariakage/live2d-agent-kit/blob/94e79e3a94753ae1bd29204d3ed685a3c7b59022/README.md

- **iki** [engine / AI連携 / 初期評価候補]
  - 役割名付きPNG/PSDレイヤー、画像生成モデル（Claude Codeプラグイン経由） → .ikiモデル（プレーンJSON）、WebGL2での動作。MITの2Dパペットエンジン。AIエージェントが画像モデルでパーツを描き、役割名付きレイヤーから.iki形式へ自動リギングする。
  - 制約: 作者自身が早期と明記し、スキーマは流動的。Live2D/Inochi2Dより成熟度は低い。
  - 制作用途: エージェント連携での2Dリギング自動化の検証に向く。
  - 出典（2026-10-03確認）: https://github.com/zeikar/iki/blob/e0ebdd542212e60847ca3af37965c73e77301ad1/README.md

- **spine-parts** [pipeline / AI連携 / 小規模・初期評価候補]
  - キャラ立ち絵PNG、See-throughのレイヤ（layers.json+PNGまたはPSD）、キャラ設定config.json → Spine 4.3のskeleton.json/atlas/packedページ、パーツPNG、idleのAPNG/GIF等。1枚のアニメ絵からSpine 2Dキャラのパーツを組み立てるCLI。See-throughのレイヤ分解結果を統合し、メッシュ・ボーン・ループidleをspine-rigc仕様で生成、書き出し前に数値で検査する。
  - 制約: READMEは特定チェックポイント（Pony Diffusion V6 XL）と手作業編集を伴う例を記載。入力は正面・全身で縦長の1キャラに限定。
  - 制作用途: Spine/Live2D系の2Dリグ工程の自動化・検証の足がかりになる。
  - 出典（2026-10-05確認）: https://github.com/firejune/spine-parts/blob/774ef0414fdb9e8b045803675d61664339965604/README.md

- **still2rig-psd** [workflow_tool / AIモデル・学習 / 小規模・初期評価候補（READMEはv0.1 alphaと明記）]
  - アニメキャラの静止画（PNG/JPEG/WebP） → レイヤー化PSD、QAレポート、モーションプレビュー。1枚のアニメキャラ画像をSee-throughで意味的にレイヤー分解し、構造チェック付きのPSDへ組み立てるワークフロー。組み込みWebUIでまばたき・口・髪/体のモーションをプレビューできる。
  - 制約: READMEは1枚の静止画では閉じ目や別口の立ち絵を用意できず、欠落を報告するとしている。Colab接続はユーザー承認が必要。
  - 制作用途: イラスト→PSDレイヤー化→2Dリグ準備の前工程候補。
  - 出典（2026-10-06確認）: https://github.com/shinshin86/still2rig-psd/blob/29f2c086fef408483cdd1650b6b7626e27117600/README.md

## レイヤー分解

- **ComfyUI-See-through** [integration / AI連携 / ComfyUI利用者向け]
  - アニメイラスト → 分解レイヤー、PSD。See-throughによる分解をComfyUIのノード工程へ接続する。
  - 制約: 独立した分解モデルではない。GitHub APIはルートのライセンスを判定できていない。
  - 制作用途: 分解処理をComfyUIの前後工程へ接続するラッパー。本家モデルの能力とノード側の互換性を分けて評価する。
  - 出典（2026-09-09確認）: https://github.com/jtydhr88/ComfyUI-See-through/blob/98d754bf04f668647919ab750eccb0e0640faa81/README.md

- **Qwen-Image-Layered** [model / AIモデル・学習 / 基盤技術候補]
  - 汎用画像 → 複数RGBAレイヤー、PSD、ZIP、PPTX。画像を複数の編集可能なレイヤーに分解し、個別の色・位置・サイズ変更につなげる。
  - 制約: アニメ専用の可動パーツ分解ではない。最終pushは2025年12月。
  - 制作用途: 背景や物体をRGBA層に分ける汎用編集用途。キャラ関節用のパーツ分解はSee-through等と比較する。
  - 出典（2026-09-09確認）: https://github.com/QwenLM/Qwen-Image-Layered/blob/54c4fe47e76d745775e03fc66ee38457280ed9ea/README.md

- **see-through** [model / AIモデル・学習 / 導入候補]
  - アニメキャラクターの一枚絵 → 最大23レイヤーのPSD、深度・マスク。一枚絵を意味別パーツへ分解し、遮蔽部分を補完してPSDに出力する。
  - 制約: 分解が対象であり、リギングや専門家による可動構造設計は別工程。
  - 制作用途: 一枚のキャラ絵をリグ工程へ渡す入口。隠れた箇所の分解結果は作画として人が確認する。
  - 出典（2026-09-09確認）: https://github.com/shitagaki-lab/see-through/blob/7f139bb25c46a0c8ac720d95ddab185fcda5451c/README.md

- **Stable Layers** [model_toolkit / AIモデル・学習 / レイヤー分解の研究候補]
  - 単一RGB画像、画像ディレクトリ → 再合成画像、背景・物体レイヤーPNG。実アルファには--transparent指定。。Qwen-Image-Layered上のLoRAで、画像を背景と物体の編集用RGBA層へ分解する。
  - 制約: 推論のみの公開。READMEは./model同梱と記すが確認GitHubツリー4ファイルにmodel/はない。HFにはアダプタを確認。既定PNGは白背景で、アルファ出力にはフラグが必要。
  - 制作用途: 画像全体の物体分離と再合成に向く候補。キャラ可動部の分解はSee-throughと目的が異なる。
  - 出典（2026-09-09確認）: https://github.com/Stability-AI/Stable-Layers/blob/b826314b34b12d7c7cce9f0de7f49a330bd8e011/README.md

- **loom-unravel** [library / AIモデル・学習 / 初期評価候補]
  - 正面・単一キャラ・上半身のイラスト1枚 → パーツ別RGBA PNG、layers.json。1枚のアニメキャラ立ち絵を顔パーツ単位のRGBAレイヤーと、階層・深度順・アンカー点を持つメタデータに分解するオフラインパイプライン。
  - 制約: 正面・単一キャラ・上半身のみ対象で、パーツマスクは見本1枚向けに調整。インペイントのにじみは既知の未解決課題とREADMEが記載。
  - 制作用途: Live2Dリギング前のレイヤー分けの下準備。
  - 出典（2026-09-30確認）: https://github.com/byeolki/loom-unravel/blob/5d587a66d3e46b3c27cd0e655841356959c867fd/README.md

## 画像生成・編集・切り抜き

- **anime-segmentation** [model / AIモデル・学習 / 比較・既存工程の参考]
  - アニメキャラクター画像 → 背景除去画像・マスク。アニメ絵のキャラクター領域を抽出し、背景除去や合成用マスクを作る。
  - 制約: レイヤー分解や隠れた身体部位の補完ではない。最近の更新は少ない。
  - 制作用途: キャラクターと背景の分離に用途を絞ると入力準備が簡単。多層PSDが必要な工程では追加処理が必要。
  - 出典（2026-09-09確認）: https://github.com/SkyTNT/anime-segmentation/blob/55d874013a2811cdf59c365059174c7823acf5b4/README.md

- **krita-ai-diffusion** [integration / AI連携 / 更新のある導入・評価候補]
  - Kritaのキャンバス、選択範囲、プロンプト → 編集レイヤー・生成画像。Kritaの描画工程へ画像生成・インペイント・アウトペイントを組み込む。
  - 制約: 生成モデルとサービスによって費用・実行環境が変わる。
  - 制作用途: キャンバス上で局所修正しながら生成する制作UI。プロンプト単独生成より修正回数とレイヤー管理を評価する。
  - 出典（2026-09-09確認）: https://github.com/Acly/krita-ai-diffusion/blob/dda58d1c63e361207ccec085efbc34dbd32f1654/README.md

- **Qwen-Image** [model / AIモデル・学習 / 研究モデルの評価候補]
  - テキスト、編集対象画像 → 生成・編集画像。テキスト描画と画像編集を扱う汎用画像モデル群。表紙・小物・宣伝画像の制作候補。
  - 制約: 2.0の告知と公開重みの版を混同しない。本調査の重み候補は2512とEdit-2511。
  - 制作用途: 公式の配布案内とDiffusers呼出しデモとして読む。GitHub内のモデル独立実装と読み替えない。
  - 出典（2026-09-09確認）: https://github.com/QwenLM/Qwen-Image/blob/6b5e1f5cec987d404be5ac6657db3b9aacb56a89/README.md

- **Z-Image** [model / AIモデル・学習 / 研究モデルの評価候補]
  - テキスト、モデルによって画像条件 → 生成・編集画像。6B級の汎用画像モデル群。Turboやベースモデルを用途に合わせて利用する。
  - 制約: アニメ専用ではない。Turbo・Base・Omni等の能力と公開範囲を分ける。
  - 制作用途: Turboで試作速度、Baseで学習・制御の適性を分けて調べる。各派生の公開状況を推測で補完しない。
  - 出典（2026-09-09確認）: https://github.com/Tongyi-MAI/Z-Image/blob/26f23eda626ffadda020b04ff79488e1d72004cd/README.md

- **ComfyUI-Forbidden-Vision** [integration / AIモデル・学習 / 更新中の実装候補]
  - ComfyUIの画像または潜在、プロンプト、顔検出・マスク用モデル → 顔を修正した画像、顔マスク、トーン補正/アップスケール済み出力。アニメ調・実写の両方に対応する顔の検出・セグメンテーション・補正を行うComfyUIカスタムノード群。ADetailerやFaceDetailerの代替を狙い、独自学習モデルを同梱する。
  - 制約: 強い様式化・遮蔽・特殊構図では検出失敗があり得るとREADMEに明記。モデル精度は未検証。
  - 制作用途: 生成イラストの顔修正・ディテール補正工程の候補。
  - 出典（2026-10-01確認）: https://github.com/luxdelux7/ComfyUI-Forbidden-Vision/blob/b474d579c7749c8046d267c75512484120626b6d/README.md

- **ComfyUI-Ultimate-Face-Fix** [integration / AI出力の後処理 / 活発・候補]
  - 元画像、生成モデル・VAE・プロンプト、顔検出/セグメンテーションモデル → 修復済み画像、顔クロップ、顔マスク、プレビュー。顔を検出して切り出し、接続した生成モデルでimg2img修復し、意味マスクで顔だけを元画像に合成するComfyUIノード。
  - 制約: 生成モデルと素材は利用者が用意。モデル重みは別途取得で上流ライセンスに従う。
  - 制作用途: ラフや生成画像の顔崩れを後処理で整える用途。
  - 出典（2026-09-30確認）: https://github.com/Merserk/ComfyUI-Ultimate-Face-Fix/blob/98a00ad332803f4adf9e2154a211e3641971d7ef/README.md

- **Colortina** [desktop_tool / AIモデル・学習 / 小規模・初期評価候補]
  - 白黒漫画画像、PDF、画像フォルダ → 彩色済み画像。manga-colorization-v2を基にしたローカル漫画自動彩色デスクトップツール。手動カラーヒント、区域ごとの再彩色、髪色補正、バッチ処理を備える。
  - 制約: モデル重みはリポジトリ非同梱。新規・小規模。第三者コード/モデルは各ライセンスに従う。
  - 制作用途: ページ単位の彩色下地と手直しに。
  - 出典（2026-09-30確認）: https://github.com/Amster-Ilvil/Colortina/blob/056c6ed79609037605a6d5fdde9f0bda5176abac/README.md

- **ComfyUI-NeuralBooru** [integration / AIモデル・学習 / 小規模・初期評価候補]
  - 英語のシーン説明文、system prompt、プロンプトテンプレート、ローカルLLMのモデル名 → 検証済みのDanbooruタグ文字列、除外されたタグ一覧。自然文のシーン記述をローカルLLMでDanbooruタグに変換するComfyUIノード。約14万件の実在タグ語彙で検証・別名変換・語形修正・並び替えを行い、テンプレートで包んでサンプラーへ渡す。
  - 制約: READMEの想定はSDXL系チェックポイントと英語Danbooru語彙。日本語入力の扱いやタグ辞書の網羅性は記載されていない。fuzzy matchは既定で無効。
  - 制作用途: 大量のプロンプト作成・表記ゆれ統一をワークフロー内で自動化する用途。
  - 出典（2026-10-02確認）: https://github.com/ChrisJohnson89/ComfyUI-NeuralBooru/blob/e3376e5fcea10d38c52e8261f81f73fab6ef3352/README.md

- **ComfyUI-AnimeRembg** [integration / AI出力の後処理 / 小規模・初期評価候補（beta）]
  - アニメキャラ動画フレーム（グレー背景など） → RGB（デスピル済）とMASK（ソフトα）。アニメキャラ動画のアルファマットを抽出するComfyUIカスタムノード集。既知背景の差分マッティングとデスピルを実装する。
  - 制約: v0.1.0-betaでマスク縁の精度改善中。背景色が既知である前提の処理。
  - 制作用途: Wan等で生成したキャラ動画を実写合成する際のマットに使える。
  - 出典（2026-10-03確認）: https://github.com/mincad/ComfyUI-AnimeRembg/blob/f179104daed4b74bf04a076cdd43308bf25a3865/README.md

- **CYKSM** [desktop_tool / AIモデル・学習 / 小規模・初期評価候補]
  - 二次元画像（小〜中サイズ） → 超解像済み画像（コピーまたは名前を付けて保存）。realesrgan-x4plus-animeモデルを手軽に使うためのGUIツール。画像を左側にドラッグ&ドロップしてボタンを押すと超解像し、結果を右側にプレビューする。
  - 制約: 小さい二次元画像向けで、他種別や大サイズ画像への効果は限定的と記載。巨大サイズはVRAM不足の可能性。ライセンスMIT。
  - 制作用途: ラフや小さい素材を手早く拡大したい単発作業に向く。
  - 出典（2026-10-04確認）: https://github.com/Nigh/CYKSM/blob/cccdccafabca8ae0e192c1a749802306cb1dfd96/README.md

- **Caelum** [desktop_tool / AIモデル・学習 / 小規模・初期評価候補]
  - アニメイラスト画像 → ×4に拡大・クリーンアップした画像。アニメイラスト専用の×4超解像・圧縮劣化復元ツール（Windows GUI）。Pixiv/X/Facebook等の再アップロードで劣化した画像の復元を狙い、PPBUNetという独自構成を採る。
  - 制約: READMEは開発継続中でPSNR/SSIM等の定量比較は初回安定版まで未公開と明記。コードはAGPL-3.0、モデル/学習はCC BY-NC-SA 4.0。
  - 制作用途: 手元アニメ画像の復元・拡大に使えるが、ライセンス上商用利用は不可。
  - 出典（2026-10-05確認）: https://github.com/yumenana/Caelum/blob/cd0e88d6f9d5699971a63e4beb73c4be928cc802/README.md

- **ComfyUI_LayerStyle** [workflow_tool / AIは任意 / 活発・実用段階]
  - 画像、マスク、テキスト、各種モデルファイル → 合成画像、マスク、プロンプト、QA用中間出力。ComfyUIにPhotoshop風のレイヤー合成・マスク処理ノード群を追加するカスタムノード。合成・マスク・切り抜き・プロンプト補助などのノードをまとめて提供する。
  - 制約: READMEは日本語UIや分割移行により、更新時にAdvance側の導入が必要になる場合があると説明。動作は環境依存で、全ノードの検証は未実施。
  - 制作用途: 生成画像のマスク処理・レイヤー合成・書き出し工程の自動化候補。
  - 出典（2026-10-06確認）: https://github.com/chflame163/ComfyUI_LayerStyle/blob/a3459a7638c4c2839878089c105c73af0eb2edd2/README.MD

- **QualityScaler** [desktop_tool / AIモデル・学習 / 活発・実用段階]
  - 画像（jpg/png/tif/bmp/webp/heic）、動画（mp4/mkv/avi/mov等） → 拡大画像、拡大動画。画像・動画をAIで拡大・ノイズ除去するWindows向けGUIアプリ。タイル分割でVRAM制限を回避し、動画の停止再開や補間、マルチGPUにも対応。
  - 制約: READMEはWindows専用。無料版はNVIDIA、Steam版はAMD/Intel対応と記載。拡大結果は素材依存で品質の断定はできない。
  - 制作用途: ラフ・素材の解像度引き上げ工程の候補。
  - 出典（2026-10-06確認）: https://github.com/Djdefrag/QualityScaler/blob/8c4c7410e641daa7580133e6f90ff7cd7ef73532/README.md

- **abg-comfyui** [integration / AIモデル・学習 / 公開済み]
  - 画像 → 背景除去済み画像。アニメ画像の背景除去を行うComfyUIノード。skytntのanime-remove-background系スペースを土台にしている。
  - 制約: READMEが簡素でライセンス表記がない。髪や細い線の切り抜き品質は今回未検証。
  - 制作用途: キャラ切り抜き・素材化の後処理。
  - 出典（2026-10-07確認）: https://github.com/kwaroran/abg-comfyui/blob/b16a21d0d21154648c7172af49a33f23505ccbc8/README.md

- **upscalejs** [library / AIモデル・学習 / 公開済み（v2）]
  - ImageBitmap（画像） → 拡大後のImageBitmap。ブラウザ内でONNX Runtime Webを使い超解像モデルで画像を拡大するJSライブラリ。Real-ESRGAN anime 4x等をWeb Workerで実行する。
  - 制約: v2はESM/ブラウザ優先でNode/CJS非対応。WASMマルチスレッドは不安定になり得るとREADMEが注意。
  - 制作用途: Webアプリでの画像拡大・下書き確認。
  - 出典（2026-10-07確認）: https://github.com/gqgs/upscalejs/blob/4ead647b5dbb9d031e96d59d8a4d373722e38547/README.md

## 動画生成

- **FramePack** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 開始画像、テキスト、長さ設定 → 段階的に生成する動画。過去フレームの文脈を圧縮して動画を逐次生成する実装・デスクトップUI。
  - 制約: 少ないVRAMは短い生成時間を保証しない。長尺の人物・背景一貫性は未評価。
  - 制作用途: 個人GPUで長さを伸ばす実験候補。生成時間を含めて採用を決めたい。
  - 出典（2026-09-09確認）: https://github.com/lllyasviel/FramePack/blob/97fe5dbe06ac1f337ece08935b1076a35eefeeb9/README.md

- **Index-anisora** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 画像、プロンプト、版に応じたマスクや中間フレーム → アニメ動画。アニメ向け動画生成。版ごとに任意フレーム、マスク制御、スタイル変換等を提供。
  - 制約: V3.1の12GB配布パッケージをV3.2の一般要件としない。「3Dキャラ動画」は編集可能なメッシュではない。
  - 制作用途: アニメ特化の比較対象として優先度が高い。汎用Wanと同じカットを比較すると価値を判断しやすい。
  - 出典（2026-09-09確認）: https://github.com/bilibili/Index-anisora/blob/6cdce3a17548d7ff0f2e05978469f134da25e68e/README.md

- **LTX-2** [model / AIモデル・学習 / 更新のある導入・評価候補]
  - テキスト、参照画像・制御条件 → 音声と映像を伴う動画。音声・動画生成とLoRA学習を扱う公式実装。READMEはLTX-2.5の導入も案内する。
  - 制約: LTX-2と2.5の版・必要モデル・利用条件を分ける。全環境での動作は未検証。
  - 制作用途: 映像と音を同時に生成する短編候補。現READMEの2.5導線と既存2系重みの組み合わせを明記する。
  - 出典（2026-09-09確認）: https://github.com/Lightricks/LTX-2/blob/a95ab856bf29407b6b066ede0abe1846050db56c/README.md

- **LTX-Video** [model / AIモデル・学習 / 旧版・履歴資料]
  - テキスト、参照画像 → 動画。LTXの旧世代動画生成実装。
  - 制約: 公式READMEはLTX-2への移行を案内。現在の主開発先として推薦しない。
  - 制作用途: 既存ワークフロー再現のための前世代記録。新規制作は後継との入力・モデル差から比較する。
  - 出典（2026-09-09確認）: https://github.com/Lightricks/LTX-Video/blob/4b2d053057623ddd4d0a1d3e9cd28890e9ef487f/README.md

- **SCAIL-2** [model / AIモデル・学習 / 研究・技術評価候補]
  - 参照画像、動作動画、対応マスク、プロンプト → キャラクター動画、キャラ置換動画。参照キャラクターに動画の動きを移し、複数参照やキャラクター置換にも対応する。
  - 制約: アニメ専用ではない。入力マスクが重要で、複数参照は品質低下の場合がある。
  - 制作用途: 動作動画とマスクを用いたキャラ置換の候補。マスク準備を含む工程全体の手間を評価する。
  - 出典（2026-09-09確認）: https://github.com/zai-org/SCAIL-2/blob/78fe19576bb06be96c2375e088574a262a300edb/README.md

- **Wan-Move** [model / AIモデル・学習 / モデル・研究候補]
  - 開始画像、プロンプト、移動軌跡 → 5秒・480P等の制御動画。動きの軌跡を条件に動画を生成するWan系実装。
  - 制約: 第三者の低VRAM統合と公式経路を分ける。軌跡制御で厳密な骨格アニメになるわけではない。
  - 制作用途: キャラや小物の移動位置を狙った短いカットの候補。
  - 出典（2026-09-09確認）: https://github.com/ali-vilab/Wan-Move/blob/80c58a7d2ad175fa82a4d57f79f2a1415317dcfa/README.md

- **Wan2.2** [model / AIモデル・学習 / 研究モデルの評価候補]
  - テキスト、画像等の条件 → 生成動画。テキストや画像から動画を作るWan2.2公式モデル群。
  - 制約: アニメ専用ではない。5BとA14B等の機能・メモリ要件を一括りにしない。
  - 制作用途: 汎用動画基盤としてアニメ特化版の比較元にする。TI2V-5B、A14B、Animate等は別構成として扱う。
  - 出典（2026-09-09確認）: https://github.com/Wan-Video/Wan2.2/blob/42bf4cfaa384bc21833865abc2f9e6c0e67233dc/README.md

- **vlog2anime-kit** [pipeline / AIモデル・学習 / 小規模・初期評価候補]
  - 実写動画（16fps等に整形）、キャラクター参照画像、プロンプト／ネガティブ → 合成済みmp4、キャラクター／元人物／安全マットの各mp4、QC結果JSON。実写動画の人物を参照画像のアニメキャラへ置換し、元人物を露出させずに実写背景へ戻すComfyUIワークフロー集。Wan2.2 Animate/SCAIL-2で変換し、SAM3追跡＋MatAnyone2でマットを作る。
  - 制約: キャラ固有の参照画像・プロンプト・LoRA、モデル本体は含まず、特定キャラの同一性は保証しない。81フレーム超は分割推奨。必要VRAM・速度は環境依存。
  - 制作用途: 実写素材をアニメ調へ寄せるショット単位の変換と、その安全確認。
  - 出典（2026-10-02確認）: https://github.com/mincad/vlog2anime-kit/blob/184f867dfd82d97913952f2087234d7d6d10b6ee/README.md

- **video-regen-recipes** [workflow_tool / AIモデル・学習 / 小規模・初期評価候補]
  - 再現したい動画の指定、キャラ参照画像、プロンプト、既存の生成AIログイン状況 → 二創動画、テンプレート形式の再現手順、検証記録。Agentに指示してローカルMiniMax H3でMAD・手書・鬼畜等の二創動画を再現するためのテンプレート集（20件）とSkills。参考図生成・音声クローン・後期編集まで手順書と検証プロンプトを同梱する。
  - 制約: 品質・再現性は保証されず、TODOにWindows側テスト未完了と他Agent製品への適配が残る。テンプレートは第三者の素材・権利に依存する。
  - 制作用途: ショート二創動画のレシピ管理と再現手順の共有。
  - 出典（2026-10-02確認）: https://github.com/Shenrui-Ma/video-regen-recipes/blob/47cc68e1fe7a04213eb9aa53db9f08cb9a06d317/README.md

- **NijiLucid** [browser_tool / AIモデル・学習 / 活発・実用候補]
  - 対応サイト上の動画（Whitelistで対象指定） → 拡大・強調された動画表示（ファイル書き出しではない）。WebGPUでブラウザ上のアニメ動画をリアルタイムに超解像する拡張。動画プレイヤーに「超分」ボタンを出し、2x/4x/8xや目標解像度で拡大する。快速/均衡/質量/極致の性能档位とカスタム効果合成を備える。
  - 制約: EME/DRM保護動画（Netflix等）には作用しない。書き出し機能の記載はない。核心コードはMITだがCuNNy生成コンポーネントはLGPL-3.0-or-later。
  - 制作用途: 完成動画の視聴・チェックの画質向上向け。素材の書き出し工程には組み込みにくい。
  - 出典（2026-10-05確認）: https://github.com/chenmozhijin/NijiLucid/blob/1c9309bac94c991848c1b501eb34ce6642afdabf/README.md

## 3D生成・モデリング・リギング

- **AniGen** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - キャラクター・物体の画像 → リグ付き3Dアセット。一枚の画像から形状・骨格・スキンウェイトを一緒に生成する。
  - 制約: モデルの組み合わせで形状と骨格の優先度が異なる。関節密度条件が不適切だとウェイトが損なわれる。
  - 制作用途: 静的生成と後付けリグの二段階を一緒に扱う新しい比較対象。
  - 出典（2026-09-09確認）: https://github.com/VAST-AI-Research/AniGen/blob/c49db3d6b466537a02ccf2286688903d77af7e4f/README.md

- **Blender** [desktop_tool / 非AI制作 / 定番の制作基盤]
  - 3D形状、材質、リグ、モーション等 → 3Dモデル、レンダリング画像、アニメーション。モデリング、リギング、アニメ、レンダリング、合成を扱う統合制作環境。
  - 制約: GitHubは公式ミラー。非AIの汎用3Dツールとしてキャラ・アニメ制作に関連付ける。
  - 制作用途: 生成メッシュ・リグ・動作を人が修正し、ゲームや映像へ出す共通の作業場所。
  - 出典（2026-09-09確認）: https://github.com/blender/blender/blob/b7e47b113f30303d14ffb6cba06bf44f721ef44f/.github/README.md

- **Hunyuan3D-2.1** [model / AIモデル・学習 / 比較・既存工程の参考]
  - 画像 → PBR材質付き3Dアセット。画像から3D形状と材質を生成する公式実装。
  - 制約: 2025年公開版。制作で使う際は形状・材質・リグを個別に確認する。
  - 制作用途: PBR付き形状生成の比較基準。メッシュの見た目と動かせるアセットとしての構造を別に判断する。
  - 出典（2026-09-09確認）: https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1/blob/82920d643c0dc2f7bfd7255f45f62d386edfe60c/README.md

- **Pixal3D** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 単一画像、またはカメラ条件のある多視点画像 → GLB等の3Dアセット。画像からPBR付き3Dを生成。2026年9月に多視点推論経路を追加。
  - 制約: 低VRAMフラグだけで品質条件が同じとは言えない。多視点は画角とカメラ整合が必要。
  - 制作用途: 3Dの見えていない部分を複数資料で指定する工程に有望。
  - 出典（2026-09-09確認）: https://github.com/TencentARC/Pixal3D/blob/f7cf38429b0bd264f1995f0f8743a88b1c728b94/README.md

- **Puppeteer** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 3Dメッシュ、駆動動画 → リグ、アニメーション、FBX等。3Dメッシュに骨格とウェイトを付け、動画誘導でアニメーションする。
  - 制約: PuppetLoomとは別研究。骨格生成と動画最適化で必要モデル・工程が分かれる。
  - 制作用途: 既存メッシュを動かす研究比較として、生成から始めるAniGenと使い分ける。
  - 出典（2026-09-09確認）: https://github.com/Seed3D/Puppeteer/blob/1c0f9fc6ad209667a0ec5ceac9b59964938a8b51/README.md

- **Roblox Cube / CubePart** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - Cubeはテキスト、CubePartはメッシュと部品スキーマ → 3D形状または組み合わさる部品メッシュ。テキストからの形状生成に加え、メッシュと部品定義から構造を持つ部品群を生成する。
  - 制約: 将来構想のゲーム全体生成を現行機能としない。部品生成はリグと挙動スクリプトの生成保証ではない。
  - 制作用途: 動く扉や車輪など部品の意味を持つゲームアセットに適する研究候補。
  - 出典（2026-09-09確認）: https://github.com/Roblox/cube/blob/3c6d06ddbef3160a1e1950cb13ab63dd12a61e50/README.md

- **SkinTokens** [model / AIモデル・学習 / 研究モデルの評価候補]
  - 3Dメッシュ → 骨格階層・スキンウェイト付き3Dアセット。TokenRigで骨格とスキンウェイトを一つの系列として生成する自動リギング研究。
  - 制約: 自動リグの実用性は対象メッシュごとに確認が必要。
  - 制作用途: 既存メッシュの骨格・ウェイト作成を省力化する後継研究。人型以外の適性も対象ごとに確認する。
  - 出典（2026-09-09確認）: https://github.com/VAST-AI-Research/SkinTokens/blob/273b691d35989d71cd17ff2895fdc735097b92d1/README.md

- **SQuadGen** [model_toolkit / AIモデル・学習 / 小規模・初期候補]
  - 3D形状と設定 → チャート距離場、抽出した四角形レイアウト。3D形状上の単純な四角形レイアウトを生成する研究。
  - 制約: 最終的なキャラ用リトポロジーや関節周りのループ配置を自動保証しない。
  - 制作用途: 生成メッシュを編集しやすい構造へ変える研究として追いたい。
  - 出典（2026-09-09確認）: https://github.com/microsoft/SQuadGen/blob/b00a83b6f2068b9e66cbf195978dbe9c084108ee/README.md

- **TRELLIS.2** [model / AIモデル・学習 / 研究モデルの評価候補]
  - 画像 → PBR材質を伴う3Dアセット。画像から形状・材質を備えた3Dアセットを生成する4Bモデル。
  - 制約: 生成だけでゲーム向けトポロジーやリグが完成するわけではない。
  - 制作用途: PBR付き3D素材の生成・材質処理の候補。生成後の最適化工程まで含めて評価する。
  - 出典（2026-09-09確認）: https://github.com/microsoft/TRELLIS.2/blob/75fbf0183001ed9876c8dbb35de6b68552ee08bd/README.md

- **UniRig** [model / AIモデル・学習 / 比較・既存工程の参考]
  - 3Dメッシュ → 骨格とスキンウェイト。形状から骨格推定とスキニングを行う自動リギング研究。
  - 制約: 後継版の能力をこの実装へ混ぜない。実際の変形品質は未検証。
  - 制作用途: 後継SkinTokensとの比較基準や既存リグ再現のために残す。後継の新機能はこの版の実績としない。
  - 出典（2026-09-09確認）: https://github.com/VAST-AI-Research/UniRig/blob/6793c6640ff01c8fb389f3993434124bb43d2933/README.md

- **SekaiBlender** [desktop_tool / 非AI制作 / 小規模・初期評価候補]
  - PMXモデル、VMDモーション → PMX/VMD、レンダリング結果。MMD向けに特化したBlenderブランチ。PMX/VMDのネイティブ入出力、CCD IKソルバ、Bullet物理、FSR拡大を統合する。
  - 制約: AI機能は含まない。MMD→Rigify連携など一部はテスト中。PMX出力は自前取込モデルに限定。HDRやライト/自己影フレームは非対応。
  - 制作用途: MMDモデルの再利用やモーション流用、MMD風ルックのレンダリングに。
  - 出典（2026-09-30確認）: https://github.com/ShiJieWorld/SekaiBlender/blob/3d92799c6a87372d5bf98f7ee4891bfa536665c8/README.md

- **godot-vrm** [integration / 非AI制作 / 活発・実用段階]
  - VRMアバター、glTFファイル → Godotシーン内のアバター、VRM/glTF出力。Godot 4.1+/3.2+向けにVRMアバターとMToonシェーダのインポート/エクスポートを提供するプラグイン。Asset Libraryから入手できる。
  - 制約: READMEはGodot向けの機能範囲にとどまり、AI生成は含まない。バージョン差で挙動が異なる可能性がある。
  - 制作用途: アバターをゲーム・リアルタイム演出へ組み込む工程の候補。
  - 出典（2026-10-06確認）: https://github.com/V-Sekai/godot-vrm/blob/e15199f980064028bfa4fbee5e70dddb82dd55c3/README.md

## TTS・キャラクター音声

- **CosyVoice** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - テキスト、参照音声、モデル別の制御指示 → 合成音声、ストリーミング音声。ストリーミング対応の多言語音声合成。現行READMEはFun-CosyVoice3を案内。
  - 制約: FunAudioLLMからQwenAudioへ移転。作者の低遅延値は全システムの遅延ではない。
  - 制作用途: 会話キャラの音声バックエンド候補。発話開始までの遅延を重視する場合に比較。
  - 出典（2026-09-09確認）: https://github.com/QwenAudio/CosyVoice/blob/074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc/README.md

- **F5-TTS** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 参照音声と文字起こし、合成テキスト → 合成音声。参照音声とテキストを使うフローマッチング音声合成・追加学習。
  - 制約: コードはMIT、事前学習モデルはREADMEでCC BY-NCと明記。日本語の標準対応を推定しない。
  - 制作用途: 音声参照を使う研究比較に適する。声の演技と日本語品質は別々に試す。
  - 出典（2026-09-09確認）: https://github.com/SWivid/F5-TTS/blob/9c614e9657089213efc6a7421b30630be138a3f5/README.md

- **fish-speech** [model / AIモデル・学習 / 更新のある導入・評価候補]
  - テキスト、参照音声 → 合成音声。Fish Audio S2系の表現豊かなTTS・音声クローンを扱う実装。
  - 制約: READMEはFISH AUDIO RESEARCH LICENSEと記載。過去版のライセンスを現在版へ適用しない。
  - 制作用途: 現行S2-Proには小声など自由記述の表現タグが案内される。ASMR専用の耳元表現とは別に音声演技を評価する。
  - 出典（2026-09-09確認）: https://github.com/fishaudio/fish-speech/blob/befe4001745417f8c42131739d862b8a6fdbd15a/README.md

- **GPT-SoVITS** [model_toolkit / AIモデル・学習 / 更新のある導入・評価候補]
  - テキスト、参照音声、学習音声 → 音声合成・追加学習モデル。少量音声を使うTTSと音声クローンをWebUIから扱う。
  - 制約: 参照音声の長さと品質で結果が変わる。作者の少量学習品質は未再現。
  - 制作用途: 参照音声や少量学習でキャラ台詞を作る候補。短い参照例と長期運用する声モデルを区別する。
  - 出典（2026-09-09確認）: https://github.com/RVC-Boss/GPT-SoVITS/blob/48b1a0169a28582a8984402f82cf438d3bfa6aca/README.md

- **IndexTTS** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - テキスト、声質用参照、感情条件 → 合成音声。声質・感情の条件を扱う音声合成。現行2.5は日本語を含む5言語を案内。
  - 制約: 2.5と2のPython API・モデルを混用しない。日本語対応は作者説明であり品質実測ではない。
  - 制作用途: 日本語キャラクターの演技付き台詞に新しい比較対象。
  - 出典（2026-09-09確認）: https://github.com/index-tts/index-tts/blob/ee40fa7d6c6b8a2c7f06105f9f1e65775b74868c/README.md

- **Qwen3-TTS** [model / AIモデル・学習 / 研究モデルの評価候補]
  - テキスト、声の説明、参照音声 → 合成音声。声のデザイン、参照音声による合成、指示による話し方制御を扱う多言語TTS。
  - 制約: 通常TTSの表現制御とASMR専用性能を同一視しない。
  - 制作用途: 声の設計・既定声・参照声のモデルを分けて選ぶ。会話キャラでは速度と日本語の自然さを両方見る。
  - 出典（2026-09-09確認）: https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/README.md

- **RVC WebUI** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 録音・歌声、対象声モデル、学習音声 → 変換音声、声モデル。入力音声の発話内容を保ちながら学習した声へ変換する。
  - 制約: TTSではなく声質変換。汎用の基盤ファイルだけでは任意の対象声が使えるわけではない。
  - 制作用途: 自分で演じた台詞のタイミングを保持して声を変える工程に適する。
  - 出典（2026-09-09確認）: https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/README.md

- **Style-Bert-VITS2** [model_toolkit / AIモデル・学習 / 比較・既存工程の参考]
  - テキスト、音声スタイル、学習音声 → 読み上げ音声・追加学習モデル。Bert-VITS2を基に音声スタイルの制御と学習を扱う日本語TTSツール。
  - 制約: コードとデフォルト音声モデルの利用条件を分ける。最近の更新は少ない。
  - 制作用途: 日本語の読みとスタイルを調整する制作用途。学習済み音源ごとの声の特徴と条件を保持する。
  - 出典（2026-09-09確認）: https://github.com/litagin02/Style-Bert-VITS2/blob/66de777e06392c0f313600be03c43ef96658b244/README.md

- **voicevox** [desktop_tool / AI連携 / 定番の制作基盤]
  - 日本語テキスト、話者・抑揚設定 → 読み上げ音声。日本語のキャラクター音声を編集して出力するVOICEVOXのエディタ。
  - 制約: このリポジトリはエディタ。エンジン・音声ライブラリ・キャラの条件は別。
  - 制作用途: 台詞をGUIで校正しやすい日本語音声編集の候補。UIのライセンスだけで話者の条件を判断しない。
  - 出典（2026-09-09確認）: https://github.com/VOICEVOX/voicevox/blob/b7258250fe90c82f112d0f51e43f2a1b67992d36/README.md

- **Genie-TTS** [model_toolkit / AIモデル・学習 / 活発・実用段階]
  - テキスト、キャラクターのONNXモデル、参照音声 → 合成音声、ONNXモデル、API応答。GPT-SoVITS（V2/V2ProPlus）をONNX化してCPUで動かす軽量推論エンジン。TTS推論・モデル変換・FastAPIサーバーをまとめて提供する。
  - 制約: READMEは対応モデルがV2/V2ProPlusで、V3/V4は未対応と記載。性能値は作者のCPU計測で環境依存。
  - 制作用途: ローカル/サーバーでのキャラ音声合成API配備候補。
  - 出典（2026-10-06確認）: https://github.com/High-Logic/Genie-TTS/blob/d347fd0f8683e9a362b69f59fa0a4799ddb5e828/README.md

- **TTS-WebUI** [web_app / AIモデル・学習 / 活発・実用段階]
  - テキスト、参照音声、音声ファイル → 合成音声、変換音声、生成音楽。多数のTTS/音声生成モデルを1つのGradio+React UIで扱うWebUI。GPT-SoVITS、XTTSv2、Kokoro、StyleTTS2、RVC、MusicGen、Demucs等の拡張を備える。
  - 制約: READMEはモデルごとに拡張が必要で、依存やライセンスは各モデルに従うと説明。動作はGPU/環境依存。
  - 制作用途: 音声制作の試作・比較環境の候補。
  - 出典（2026-10-06確認）: https://github.com/rsxdalv/TTS-WebUI/blob/2e5701387c423307d73972a45496bfdcb6a7d8e1/README.md

- **vits-simple-api** [api_reference / AIモデル・学習 / 活発・実用段階]
  - テキスト、モデルID、話者・感情パラメータ → 音声ファイル。VITS系TTSをHTTP APIとして提供するサーバー。VITS/Bert-VITS2/GPT-SoVITS/emotion-vits等の複数モデルを読み込み、GETで音声合成できる。
  - 制約: ライセンスはAGPL-3.0。READMEはSSML対応が作業中と記載。モデルごとにクリーンアーと言語対応が異なる。
  - 制作用途: キャラ音声をAPIでサービス連携する工程の候補。
  - 出典（2026-10-06確認）: https://github.com/Artrajz/vits-simple-api/blob/c3d179ffabff711e6697c6eb16298ac66a250406/README.md

- **sukasuka-vocal-dataset-builder** [pipeline / 非AI制作 / コミュニティ運用中]
  - アニメ動画（mkv等）、.ass/.srt字幕、ドラマCD（flac） → 役柄別に分割した音声ファイル、meta.csv（filename,character,content）。アニメ本編やドラマCDと字幕から、役柄ごとの音声を切り出してデータセット化するスクリプト群。TTS/SVC学習用のキャラクター音声データ作成を想定。
  - 制約: キャラクターのラベリングは手作業。配布データには非ボーカル音が残る版と除去版がある。元動画・字幕のライセンスはMITとは別に確認が必要。
  - 制作用途: キャラクターTTS/SVC用データセット構築の下地。
  - 出典（2026-10-07確認）: https://github.com/Hecate2/sukasuka-vocal-dataset-builder/blob/5b166d5017653f9f79b1e4122e93d1087d4d7dc3/README.md

## ASMR・効果音・環境音

- **ASMRify** [desktop_tool / AI出力の後処理 / 小規模・初期評価候補]
  - 録音またはTTS音声ファイル → 効果処理したWAV・MP3。音声に定位移動・残響・ピッチ等を加えて一括処理するASMR向け音声加工ツール。
  - 制約: 小規模で利用実績は未確認。AIによるささやき生成・実録バイノーラルの再現・効果効能は確認していない。
  - 制作用途: 既存録音・TTSへフィルタや空間処理を加える後処理候補。ささやき声の生成成功と呼ばない。
  - 出典（2026-09-09確認）: https://github.com/ReactorcoreGames/ASMRify/blob/5f30fc61e6148a537cdc609173880e2d50ae3b53/README.md

- **Audacity** [desktop_tool / 非AI制作 / 制作基盤として比較]
  - 録音、TTS、効果音、楽曲 → 編集済み音声プロジェクト・書き出し音声。録音とマルチトラック編集を行う音声制作アプリ。
  - 制約: 現masterはAudacity4への構造変更中。3.x用の導入・開発手順と混用しない。
  - 制作用途: ASMR・台詞・効果音を実際に仕上げる録音編集工程。
  - 出典（2026-09-09確認）: https://github.com/audacity/audacity/blob/7c667777427b0e80c177caa6d3c46367901fc775/README.md

- **Binaural Speech Synthesis** [model_toolkit / AIモデル・学習 / アーカイブ済み資料]
  - モノ音声、話者と聴取者の幾何情報 → 左右2chの空間音声。モノラル音声を空間条件に従うバイノーラル音声へ変換する研究。
  - 制約: 2021年研究、最終push2022年。現在の主流TTSやASMR専用モデルではない。READMEに非商用条件。
  - 制作用途: 耳元表現の学習型レンダリングを理解する比較基準として残す。
  - 出典（2026-09-09確認）: https://github.com/facebookresearch/BinauralSpeechSynthesis/blob/81d0765ae590e8f69d3d26dc03f8a2e9c02b7d03/README.md

- **ControlFoley** [model / AIモデル・学習 / 小規模・初期候補]
  - 動画、文章、任意の参照音声 → 効果音、音声付き動画。動画・テキスト・参照音を条件に、効果音とそのタイミングを制御する。
  - 制約: コードApache-2.0、重みCC BY-NC 4.0。ASMR専用・台詞合成モデルではない。
  - 制作用途: 接触音や環境音を映像の動きに合わせる工程でMMAudioと比較したい。
  - 出典（2026-09-09確認）: https://github.com/xiaomi-research/controlfoley/blob/b6c902888d45d75f022e253e3db29836360a3f82/README.md

- **FoleyCrafter** [model / AIモデル・学習 / 研究モデルの評価候補]
  - 無音動画、テキスト条件 → 動画に合わせた効果音。動画の内容とタイミングに合わせた効果音を生成する研究実装。
  - 制約: ASMR専用ではなく、距離感・耳元表現・立体音響は未検証。
  - 制作用途: 無音動画の効果音を作る比較基準。台詞やBGMの制作は別工程に分ける。
  - 出典（2026-09-09確認）: https://github.com/open-mmlab/FoleyCrafter/blob/b4526d1586aaf044140b359295504452297f8c13/README.md

- **MMAudio** [model / AIモデル・学習 / 研究モデルの評価候補]
  - 動画、テキスト → 同期音声。動画やテキストを条件に、時間的に対応する音声を生成する。
  - 制約: ASMRや日本語のセリフ生成専用ではない。音の同期と内容は素材ごとに評価する。
  - 制作用途: 映像と文章から効果音を合わせる候補。参照音や時刻制御を重視する場合はControlFoleyとも比較する。
  - 出典（2026-09-09確認）: https://github.com/hkchengrex/MMAudio/blob/974010a026c731054592d8f777218bd9d85a6c24/README.md

- **stable-audio-tools** [model_toolkit / AIモデル・学習 / 更新のある導入・評価候補]
  - テキスト条件、音声、モデル設定 → 生成音声・学習済みモデル。条件付き音声生成モデルの学習と推論を行うツール群。効果音や環境音素材を検討できる。
  - 制約: ASMR専用モデルではない。空間音響・ささやきの品質は未検証。
  - 制作用途: 音声生成と学習の基盤。Toolsのコード条件と使用する音声モデルの公開条件は別管理する。
  - 出典（2026-09-09確認）: https://github.com/Stability-AI/stable-audio-tools/blob/3241adba4fc2a85cf5b29d9eb68d42f40a28e820/README.md

- **Steam Audio** [library / 非AI制作 / 制作基盤として比較]
  - 音源、リスナー位置、シーン形状 → 空間化された音声出力。ゲーム空間に合わせた音の定位・伝播を扱う空間音響SDK。
  - 制約: ニューラルASMR生成や収録音声の声質生成ではない。HRTFと再生環境で印象が変わる。
  - 制作用途: VR・耳元会話・環境音の位置制御に接続しやすい非AI基盤。
  - 出典（2026-09-09確認）: https://github.com/ValveSoftware/steam-audio/blob/480dd64f513cc8a6437e7d5b9eb0d3f1d30c2fac/README.md

- **Ultimate Vocal Remover** [desktop_tool / AI連携 / 連携・制作ツール候補]
  - ミックス音源 → 分離された音声・伴奏。音源分離モデルをGUIで使い、歌・伴奏等を分離する。
  - 制約: 分離は完全ではなく、残響や楽器の漏れが残る可能性。2025年からコード更新が少ない。
  - 制作用途: 歌唱分析、台詞の抽出、既存音の整理の前処理候補。
  - 出典（2026-09-09確認）: https://github.com/Anjok07/ultimatevocalremovergui/blob/5517e0cf0d1acd16a1618eeedec596957523f9e1/README.md

## 音楽・歌声合成

- **ACE-Step-1.5** [model / AIモデル・学習 / 更新のある導入・評価候補]
  - 楽曲説明、歌詞、参照音声等 → 楽曲・歌声を含む音声。ローカルで楽曲を生成し、編集や追加学習につなげる音楽モデル。
  - 制約: 作者の速度・商用モデル比較は当カタログで再検証していない。
  - 制作用途: 歌詞付き楽曲を試作する候補。編集可能な音符を重視するなら歌声エディタやYuE2の計画機構とも比較する。
  - 出典（2026-09-09確認）: https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/README.md

- **Basic Pitch** [library / AIモデル・学習 / 連携・制作ツール候補]
  - 楽器等の音声 → MIDI、音符・音高情報。音声を音高ベンド付きMIDIへ変換する軽量な採譜モデル。
  - 制約: 作者は単一楽器での利用を推奨。全楽曲から完全な編曲譜が取れるわけではない。
  - 制作用途: 作った旋律をノート編集や再演奏へ戻す補助工程に向く。
  - 出典（2026-09-09確認）: https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/README.md

- **DiffSinger** [model_toolkit / AIモデル・学習 / 更新のある導入・評価候補]
  - 音符、歌詞、音声データ、表現パラメータ → 合成歌声・音声モデル。歌声合成の学習・推論と、ピッチ・エネルギー・息成分などの制御を扱う。
  - 制約: 原論文実装の拡張版。OpenUtau等のエディタと音源の対応は別途確認。
  - 制作用途: 音符と歌詞に沿って歌わせる制作モデル群。自動作曲・歌詞付き音源の一括生成とは制御粒度が異なる。
  - 出典（2026-09-09確認）: https://github.com/openvpi/DiffSinger/blob/336cf01b57f2ad44c6b37a79cf33993043291759/README.md

- **OpenUtau** [desktop_tool / AIは任意 / 定番の制作基盤]
  - 音符、歌詞、音源ライブラリ → 合成歌声・歌唱プロジェクト。UTAUコミュニティ向けの歌声編集・合成プラットフォーム。
  - 制約: エディタと音源・合成モデルの条件を分ける。公式リポジトリはopenutau/OpenUtauへ移転。
  - 制作用途: 音符と発音を人が編集する歌声制作の中心。音源とレンダラーの互換性を明示して使う。
  - 出典（2026-09-09確認）: https://github.com/openutau/OpenUtau/blob/17bf25e7f78c5f88a6c5bce437bf6d592f012e46/README.md

- **SOFA** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 歌声音声、歌詞・発音辞書 → 音素境界等のアラインメント。歌声向けの強制アラインメントで歌詞・音素の時間位置を求める。
  - 制約: 歌声生成器ではない。辞書と歌唱発音の差が結果に影響する。
  - 制作用途: DiffSinger等の学習データ準備と歌詞タイミングの整備に有用。
  - 出典（2026-09-09確認）: https://github.com/qiuqiao/SOFA/blob/9549c6a86d16019c817eefe4bb8183405da524cc/README.MD

- **YuE2** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 歌詞、曲調、任意の楽譜・参照録音 → 楽曲計画、48kHzステレオ楽曲。歌詞と曲調から編集可能な旋律・和音計画を作り、歌と伴奏へ展開する。
  - 制約: 現在のmainはYuE2で、コード・重みCC BY-NC 4.0。YuE-v1の旧条件を引き継がない。日本語は今回確認したカードの記載言語外。
  - 制作用途: 生成前に旋律・和音を編集する曲作りの候補。歌声エディタとは出力制御が異なる。
  - 出典（2026-09-09確認）: https://github.com/multimodal-art-projection/YuE/blob/6332efcafa5f792df81812acc3b0f20b80b855cf/README.md

- **OpenUtauMobile** [desktop_tool / AI連携 / 初期評価候補]
  - USTXプロジェクト、歌声音源（ZIP）、歌詞と音符 → 歌声の合成結果、USTXファイル。モバイル向けのオープンソース歌声合成エディタ。OpenUtau CoreをベースにUSTXプロジェクトファイルを扱い、DiffSinger／UTAU／Vogenの音源を読み込める。
  - 制約: READMEは現状かなり不安定でメモリ管理問題が起きうるとして頻繁な保存を推奨。非公式アプリであり、公式OpenUtauを名乗ってはいけない。他音源形式の動作は非保証。
  - 制作用途: 外出先での歌わせ調整・プレビュー。
  - 出典（2026-10-02確認）: https://github.com/vocoder712/OpenUtauMobile/blob/17a86f602e054c345841684224903004eff1f536/README.md

- **SoulX-Singer** [model_toolkit / AIモデル・学習 / モデル候補]
  - 歌詞、メロディまたはMIDI、話者プロンプト音声（SVCは変換元の歌声波形とF0） → 歌声波形（wav）。未見の歌声を生成するゼロショット歌声合成（SVS）モデルの公式推論コード。メロディ（F0）条件と楽譜（MIDI）条件に対応し、歌声変換（SVC）版も提供する。
  - 制約: 自動前処理のメタデータは歌唱音声と歌詞・音符の対応がずれることがあり、MIDIエディタでの手修正を推奨。ライセンスはApache-2.0。
  - 制作用途: キャラクターソングや歌声素材を、話者ごとの追加学習なしで試作したい用途に向く。
  - 出典（2026-10-04確認）: https://github.com/Soul-AILab/SoulX-Singer/blob/81aeb3ae772c70093c3de74dc23c92d983801ae4/README.md

- **DiffSinger** [model_toolkit / AIモデル・学習 / 確立した参照実装]
  - 歌詞、F0またはMIDI、テキスト（TTS構成） → 音声波形（wav）、音響特徴量（メル）。Shallow Diffusion機構を用いた歌声合成（DiffSinger）と音声合成（DiffSpeech）の公式PyTorch実装。歌詞+MIDI/F0からメルへ、メルから波形へ変換する複数構成を提供する。
  - 制約: 公開データセット（PopCS/OpenCpop/Ljspeech）ベースで、任意キャラの歌声には追加学習が必要。環境はやや古め。ライセンスはMIT。
  - 制作用途: 歌声合成モデルを自作・追加学習する際の参照基盤として使える。
  - 出典（2026-10-04確認）: https://github.com/MoonInTheRiver/DiffSinger/blob/4662c53a27a5ac662821eae23a7d71cfcff7356d/README.md

## VTuber・AIキャラクター・VRM

- **AIRI** [web_app / AI連携 / 更新のある導入・評価候補]
  - 音声、キャラ設定、ゲーム等の入力 → 会話音声、2D/3Dキャラ表示、対応ゲーム操作。会話するバーチャルキャラクターを構築する環境。
  - 制約: 対応機能はプラットフォームとプロバイダに依存。全ゲームで自律動作するという意味ではない。
  - 制作用途: 会話・表示・ゲーム接続を組み合わせるAIキャラ統合。READMEの対応先だけで目的の構成が動くとは断定しない。
  - 出典（2026-09-09確認）: https://github.com/moeru-ai/airi/blob/dfc6951a55bf4fdd66a68a0c881ae880ddd95f77/README.md

- **babylon-mmd** [library / 非AI制作 / 制作基盤として比較]
  - PMX/PMD、VMD/VPD → Web上のMMDアニメーション。Babylon.jsでMMDモデル・モーションを読み込み、物理・IK・モーフを再生する。
  - 制約: 読み込み成功と元MMDでの完全な見た目・挙動一致は別。素材条件は個別。
  - 制作用途: MMD資産をWeb作品やキャラ表示に展開する具体的な接続先。
  - 出典（2026-09-09確認）: https://github.com/noname0310/babylon-mmd/blob/ccb750db2998ed1067017eaf67f3fc987cfba6f8/README.md

- **inochi-creator** [desktop_tool / 非AI制作 / 比較・既存工程の参考]
  - レイヤー付き2Dキャラ素材 → Inochi2Dのリグ付きモデル。レイヤー画像を変形させ、ゲームやVTuberで動かす2Dモデルを作るエディタ。
  - 制約: 最終pushは2025年6月。Live2D Cubism形式と同じものではない。
  - 制作用途: 独立した2Dリグ形式でモデルを編集する非AI制作候補。Cubismと同一形式とは扱わない。
  - 出典（2026-09-09確認）: https://github.com/Inochi2D/inochi-creator/blob/dba60811cff224f8cc9ce367b1d9291bfa5f7640/README.md

- **OBS Studio** [desktop_tool / 非AI制作 / 制作基盤として比較]
  - 映像ソース、アバター表示、マイク、音声 → 配信・録画映像。画面・カメラ・音声を合成して録画・配信する。
  - 制約: 顔追跡やモデル生成は別アプリ。プラグインの対応版を確認する。
  - 制作用途: VTuber制作物を実際の配信画面へまとめる基本工程。
  - 出典（2026-09-09確認）: https://github.com/obsproject/obs-studio/blob/012c6c23c73283ee5591ae00d08af14d9eeb8279/README.rst

- **Open-LLM-VTuber** [web_app / AI連携 / 連携の評価候補]
  - マイク入力、視覚情報、キャラ設定 → 音声応答とLive2Dアバター表示。音声会話・視覚認識・Live2D表示を組み合わせるAIキャラクター環境。
  - 制約: ローカル完結はバックエンドの選択に依存。Live2Dモデル制作機能とは別。
  - 制作用途: 音声会話とLive2D表示を組み合わせる導入候補。音声認識・LLM・TTSの構成を明記して評価する。
  - 出典（2026-09-09確認）: https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/README.md

- **OpenSeeFace** [library / AIモデル・学習 / 連携・制作ツール候補]
  - 顔カメラ映像 → 顔特徴・トラッキング情報。Webカメラから顔のランドマークを推定し、アバター駆動へ渡す。
  - 制約: 単体のアバター表示ソフトではない。作者の30〜60fpsは環境依存。
  - 制作用途: 生成モデルを増やす前に安定した表情入力を作る候補。
  - 出典（2026-09-09確認）: https://github.com/emilianavt/OpenSeeFace/blob/85aa70fc67582d046e771ea73625182a0d8f7475/README.md

- **PersonaLive** [model / AIモデル・学習 / モデル・研究候補]
  - 参照画像、駆動映像・動作 → 人物動画。参照人物の画像を動作入力に従ってストリーミングでアニメーションする。
  - 制約: 出力は動画であり編集可能なLive2D・VRMモデルではない。二次元適性は未評価。
  - 制作用途: 画像ベースの配信アバターを試す研究候補。
  - 出典（2026-09-09確認）: https://github.com/GVCLab/PersonaLive/blob/abdd112e01dcf7d89122c2e5efa29fcff0669740/README.md

- **three-vrm** [library / 非AI制作 / 制作基盤として比較]
  - VRMモデル、アニメーション・表情値 → ブラウザ内3Dアバター表示。three.jsでVRMアバターを読み込み表示するライブラリ。
  - 制約: アバター生成や顔追跡は含まない。VRM・three.jsの対応版を確認する。
  - 制作用途: WebのAIキャラクターUIへ既存VRMを組み込む基盤。
  - 出典（2026-09-09確認）: https://github.com/pixiv/three-vrm/blob/1b4fc0cc7ef39a49d62bb7a66dcfeca8f65316f7/README.md

- **UniVRM** [library / 非AI制作 / 定番の制作基盤]
  - VRM・glTFアバター → Unityで読み書きできるアバター。Unity用のVRM形式実装。3Dアバターの読み込み・書き出しを扱う。
  - 制約: VRM 0.x/1.0等の互換性は個別確認。モデル生成・自動リギング機能ではない。
  - 制作用途: UnityとVRMの入出力基盤。リグや生成モデルと別に形式互換を担当する。
  - 出典（2026-09-09確認）: https://github.com/vrm-c/UniVRM/blob/928b30e96439c1c11a49b172efb72eb96d2cad8b/README.md

- **VTubeStudio** [api_reference / AI連携 / 連携用文書資料]
  - 外部プログラムのAPI要求 → VTube Studioのパラメータ制御・状態取得。VTube Studioを外部から制御する公式API文書・開発資料。
  - 制約: アプリ本体のソース公開ではない。文書リポジトリとして掲載。
  - 制作用途: 既存VTube Studioアプリへ外部AIや演出からパラメータを送るAPI資料。アプリのOSS実装とは数えない。
  - 出典（2026-09-09確認）: https://github.com/DenchiSoft/VTubeStudio/blob/0f46ef44b487fa17c8120db572ebd925924b93a3/README.md

- **prometheus-avatar** [library / AI連携 / 小規模・初期評価候補]
  - LLMのテキスト/音声、Live2Dモデル → 発話・表情付きのアバター表示。LLM出力でLive2D/3Dアバターを動かすオープンソースSDK。口パク、感情表現、リアルタイム音声、TTS、VTuberモード、MCPサーバをまとめる。
  - 制約: 音声/一部生成はホステッドAPIやマーケットプレイス前提の機能がある。比較的新しくv0.x系。
  - 制作用途: Webアプリや自作エージェントへのアバター組込みに。
  - 出典（2026-09-30確認）: https://github.com/myths-labs/prometheus-avatar/blob/7cb8e6d6a8e7d03ae4a08cede07c9d9585edcbb0/README.md

- **VMagicMirror** [desktop_tool / 非AI制作 / 確立済み]
  - VRMモデル、キーボード/マウス（および対応デバイス）の入力 → アバターの描画（配信・録画向け、クロマキー合成可能）。WindowsでVRMモデルを読み込み、追加デバイスなしにキーボードとマウス操作をモーションとしてアバターの上半身に反映するアプリ。可変クロマキーに対応し、配信・ライブコーディング・デスクトップマスコットに使える。
  - 制約: 同梱されないプリセット資産（サブキャラのVRM等）があるため、ソースからはダミー差し替え等の追加作業が必要。AI/対話機能は含まず、別途連携が前提。
  - 制作用途: VRMアバターの配信・キャラ表示基盤として組み合わせやすい。
  - 出典（2026-10-01確認）: https://github.com/malaybaku/VMagicMirror/blob/0f65276abb017015b9f6c5bbcfed428645050169/README.md

- **gaussian-vrm** [library / 非AI制作 / 研究実装・活発]
  - GVRMファイル、FBXアニメーション（Mixamo等） → Web/モバイル/VR上にレンダリングされるアバター。three.js上でVRM形式のスキニング付きガウシアンアバター(GVRM)を扱う実装。three-vrmとgaussian-splats-3dを基盤に、VRMの操作（移動やアニメーション）をそのまま再利用できる。
  - 制約: assets/ 配下のファイルはMIT対象外で研究用途のみ。制作パイプラインへの組み込み手順や性能の記載はREADMEにない。
  - 制作用途: Web向けアバター表現の選択肢として検討できる。
  - 出典（2026-10-01確認）: https://github.com/naruya/gaussian-vrm/blob/f6f552a24f7c2b7fb0d8c73f9c0b5581273b1e4c/README.md

- **Cortico** [engine / AIモデル・学習 / 活発・pre-release]
  - LLMプロバイダ設定、外部環境からのイベント、ツール定義 → botの応答・行動、Webコンソール上の管理・監視ログ。イベントストリームを中心に設計したエージェント基盤。ペルソナbot・AI配信者・ロールプレイ・コンパニオン向けで、Core/Persona/Memory/World/Botの4層構成と、外部環境を隔離して接続するWorld拡張機構を持つ。
  - 制約: READMEにpre-releaseと明記されている。VTuber向けWorldは本体と別ライセンス(AGPL-3.0+CLA)の別リポジトリで配布される。
  - 制作用途: 配信・コンパニオン系エージェントの実装基盤として検討できる。
  - 出典（2026-10-01確認）: https://github.com/Pal-AI-Lab/Cortico/blob/02f2936c89ac783675645f95cd87ff8c25305d46/README.md

- **Anima** [web_app / AIモデル・学習 / 小規模・初期評価候補]
  - テキスト入力、音声（BYOKのOpenAI realtime）、VRMモデル、Mixamo互換FBXアニメーション（任意） → 画面上のVRM演技（表情・モーション）、TTS音声のデータURL。ブラウザで動くVRMキャラクタースタジオ。テキストまたはリアルタイム音声でキャラと対話し、表情・リップシンク・身体モーションを付けて演技させる。
  - 制約: Mixamoの.fbxは再配布されず、フル動作には各自でアニメーションを用意する必要がある。同梱VRMは本リポジトリの公開デモ用途と明記されている。
  - 制作用途: VRMキャラの対話・演技の試作に使える。
  - 出典（2026-10-01確認）: https://github.com/Yun-0000/Anima/blob/9cdfb5eabe4230a34bd1d879053a1abb0baff76a/README.md

- **open-vt** [desktop_tool / 非AI制作 / 実運用候補]
  - Live2Dモデルとアセット、フェイストラッキング入力（OpenSeeFace／VTubeStudio） → 配信・録画向けのアバター表示。Godotで作られたオープンソースの2D VTuberソフト。OpenSeeFaceとVTubeStudioのトラッカーに対応し、OBSで取り込みやすい透過ウィンドウや複数ウィンドウのポップアウト操作を持つ。
  - 制約: VTSのプラグイン互換やVNetは対象外。AI対話や音声合成などは含まず、アバター表示に限定される。
  - 制作用途: Live2Dアバターでの配信運用と、透過合成を含むキャプチャ。
  - 出典（2026-10-02確認）: https://github.com/erodozer/open-vt/blob/89f2f0f4119a21c96a8b9e1222850b558ffcb62e/README.md

- **A.R.I.A** [desktop_tool / 非AI制作 / Alpha・初期評価候補]
  - Live2Dモデル（.model3.json/.moc3等）、VRMファイル、スキン済みGLB、PNG/GIF画像、カメラやiPhone等のトラッキング入力 → OBS向けの複数アバター表示、配信画面。Live2D・VRM・GLB・PNG/GIFアバターをまとめて扱うクロスプラットフォームのアバタースタジオ。顔トラッキング、物理、ライティング、視覚アクション、複数アバターのOBS出力に対応する。
  - 制約: Alpha版で一部のデバイス組合せは検証不足。VTube Studio/VBridger/VRC・GLBインポートや生成スプリングチェーンは実験的。モデル素材の利用規約は別途。ライセンスMIT。
  - 制作用途: 複数アバターを1配信画面にまとめたいVTuber/配信者に向く。
  - 出典（2026-10-04確認）: https://github.com/NekoUnix/A.R.I.A/blob/14973e63e85d4b590ab104ba51dd1acdee24ffb9/README.md

- **Seidr-Smidja** [pipeline / AI連携 / Genesis・初期評価候補]
  - アバター仕様のYAML（身長・髪・服・表情・ライセンス情報等）、VRoidベーステンプレート → .vrmファイル、プレビューPNG（正面・斜め・横・顔クローズアップ・Tポーズ・表情）。AIエージェントがYAML仕様からVRMアバターを設計・構築・検証・レンダリングするヘッドレスなパイプライン。VRoidベーステンプレートにBlenderをヘッドレスで適用し、VRChat/VTube Studio互換を検査して.vrmを出力する。
  - 制約: 人間向けGUIは無くagent/CLI専用。VRM以外の形式は対象外。READMEのステータスバッジはGenesis Phaseで、ライセンスバッジはTBD表記だがリポジトリ表記はApache-2.0。
  - 制作用途: VRMアバターの量産や、エージェント主導の反復的なアバター制作を試したい用途に向く。
  - 出典（2026-10-04確認）: https://github.com/hrabanazviking/Seidr-Smidja/blob/482c8f0032b28c4ceb323478e7854adae3715f72/README.md

- **vrm-studio** [web_app / AIは任意 / 小規模・実用候補]
  - Webカメラ映像、VRMモデル → トラッキング済みアバター表示（OBSのウィンドウキャプチャ経由で合成）。ブラウザで動くVTubingアプリ。Google MediaPipe Holisticで顔・手・全身をトラッキングし、Three.jsでVRMアバターを動かす。グリーンスクリーン、OBS連携、カルマンフィルタによる平滑化を備える。
  - 制約: ライセンス表記なし。トラッキングはMediaPipe Holisticに依存。READMEの計測はM1で30-50ms/フレーム。
  - 制作用途: 手軽なVTuber配信・アバター確認に使える。商用条件は未記載で要確認。
  - 出典（2026-10-05確認）: https://github.com/vucinatim/vrm-studio/blob/30af4abcd417039b4f3d9615a1427402f6d04a2c/README.md

- **CharacterStudio** [web_app / 非AI制作 / 活発・実用段階]
  - ローカルのVRM/3Dファイルとテクスチャ、アセットパック → glb、VRM、スクリーンショット。ブラウザ上でglTF/VRMアバターを組み立てるオープンソースの3Dアバター制作スタジオ。パーツのドラッグ＆ドロップ配置、色変更、VRM最適化、glb/VRM書き出しに対応。
  - 制約: READMEはプログラムとアセットパックを分離しており、独自モデルの追加はドキュメント参照。最適化や描画品質の定量評価は記載なし。
  - 制作用途: アバターの組み立て・最適化・一括書き出し工程の候補。
  - 出典（2026-10-06確認）: https://github.com/M3-org/CharacterStudio/blob/293182bf4a6087f4a4a7fd00e4fbdfb590029da7/README.md

- **ndmf-vrm-exporter** [integration / 非AI制作 / 活発・実用段階]
  - Unity上のVRChatアバター（Modular Avatar/lilToon構成） → VRM 1.0ファイル。NDMFベースでVRChatアバターをVRM 1.0として書き出すUnityプラグイン。PhysBone→SpringBone、Constraint→VRM Constraint、lilToon→MToon互換設定の自動変換に対応。
  - 制約: READMEはModular Avatar/lilToon前提の設計と、VRChatアバターのブレンドシェイプ過多がVRM変換時の負荷になりやすい点を挙げている。ライセンスはMPL-2.0。
  - 制作用途: アバターのフォーマット変換・再利用工程の候補。
  - 出典（2026-10-06確認）: https://github.com/hkrn/ndmf-vrm-exporter/blob/a776be244cd7066bd1c51a28286e1334738a361c/README.md

- **app** [desktop_tool / 非AI制作 / 活発・実用段階]
  - VRMアバター → 仮想カメラ映像。macOSでVRMアバターを仮想カメラとして表示するアプリ。ZoomやGoogle Meetなどでアバターを映像として映せる。
  - 制約: READMEはWindows等の他プラットフォーム非対応と明記。ソースはMITだが利用条件は公式サイト参照と記載。
  - 制作用途: VTuber配信・収録の映像入力工程の候補。
  - 出典（2026-10-06確認）: https://github.com/vcamapp/app/blob/aa6f24e864ec713270425efab8182a60dbbd8b52/README.md

- **VTubeStudio.Client** [library / 非AI制作 / 公開済み（NuGet）]
  - VTube StudioのAPIリクエスト/イベント購読 → 型付きレスポンス、イベント通知。VTube Studio公開API（WebSocket）向けの.NET 10/C# 14クライアントライブラリ。型付きメッセージとイベントハブ、DI対応パッケージを提供する。
  - 制約: VTube Studio本体が必要。初回はAPI側のトークン承認が必要。
  - 制作用途: VTuber配信ツール・自動化の連携。
  - 出典（2026-10-07確認）: https://github.com/Agash/VTubeStudio.Client/blob/266ce0fe63c102dc4ec3ce191c301145fc75fb3a/README.md

## 制作ワークフロー・追加学習

- **ComfyUI** [workflow_tool / AI連携 / 更新のある導入・評価候補]
  - ノードグラフ、プロンプト、素材、モデル → 画像・動画・音声などの生成物とワークフローJSON。画像・動画などのモデルをノードで接続して制作工程を構成する。
  - 制約: カスタムノードとモデルの互換性は個別確認が必要。ワークフロー公開だけで再現済みとはしない。
  - 制作用途: モデルやノードを工程として保存する制作基盤。ノード・重み・ワークフローの三者を固定すると引継ぎやすい。
  - 出典（2026-09-09確認）: https://github.com/Comfy-Org/ComfyUI/blob/4989cdd95487531b50438c6a091dffa06e4af4b2/README.md

- **ComfyUI-WanVideoWrapper** [integration / AI連携 / 連携の評価候補]
  - ComfyUIグラフ、Wan系モデル、素材 → 生成動画と再利用可能なワークフロー。Wan系および関連動画モデルをComfyUIで使うためのラッパーノード。
  - 制約: 公式Wan実装ではない。対応版と既存ワークフローの互換性を確認する。
  - 制作用途: Wan派生をComfyUIへ接続する第三者統合。公式重みそのままと変換済み配布を分ける。
  - 出典（2026-09-09確認）: https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/088128b224242e110d3906c6750e9a3a348a659b/readme.md

- **DiffSynth-Studio** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 画像・動画・プロンプト・学習素材 → 生成物、追加学習済み重み。画像・動画の生成と追加学習を複数モデルで扱う統合実装。
  - 制約: 一覧に載るモデルを同じ機能・VRAM条件で扱わない。モデル条件も別。
  - 制作用途: 複数研究の再現・学習コードを追う制作技術基盤として有用。
  - 出典（2026-09-09確認）: https://github.com/modelscope/DiffSynth-Studio/blob/ce9f4541d0f4ae47a138337e59066dd633207aa7/README.md

- **musubi-tuner** [training_tool / AIモデル・学習 / 更新のある導入・評価候補]
  - 画像・動画データセット、キャプション、基盤モデル → LoRA等の追加学習結果。画像・動画モデル向けのLoRA学習スクリプト群。
  - 制約: 各モデル作者による公式実装ではない。対応するモデル版と学習素材を確認する。
  - 制作用途: 動画等の追加学習をモデル別スクリプトで扱う。学習できる版と推論するUIのLoRA互換性を確認する。
  - 出典（2026-09-09確認）: https://github.com/kohya-ss/musubi-tuner/blob/e0cbd8f3dfe38365b10f8bc790b980f8894e8ba1/README.md

- **sd-scripts** [training_tool / AIモデル・学習 / 連携・制作ツール候補]
  - 画像データ、キャプション、基盤モデル → 追加学習モデル・LoRA。画像生成モデルの追加学習・LoRAを扱うスクリプト群。
  - 制約: 生成UIではない。モデル版と学習方式の組み合わせを確認する。
  - 制作用途: キャラ・画風の再現性を制作側で調整する学習基盤。
  - 出典（2026-09-09確認）: https://github.com/kohya-ss/sd-scripts/blob/4e624302e0088e39933b31cbc71f24212e900f5f/README.md

- **ComfyUI-Anime-Extensions** [integration / AIモデル・学習 / 初期評価候補]
  - テキスト、画像、参照音声、歌詞・スタイル → 音声、解析結果JSON、マスク、漫画ページ画像、VRM/Blenderシーン、動画。ComfyUI向けのノード集で、音声合成、画像条件付きキャラクター音声、画像解析・切り抜き、音楽生成、動画生成、漫画ページ組み、VRM処理をまとめて扱う。
  - 制約: モデルとランタイムは同梱されず別途準備。YuE2の重みは非商用ライセンスとREADMEが記載。
  - 制作用途: 音声・画像解析・VRM・漫画ページ組みをComfyUI内で連携。
  - 出典（2026-09-30確認）: https://github.com/ootsuka-repos/ComfyUI-Anime-Extensions/blob/aa21a682ea509bab0fa3f17ba877a3867647d4eb/README.md

- **comfyui-stylebook** [integration / AIは任意 / 小規模・初期評価候補]
  - 被写体プロンプト → スタイル/作家/モディファイアを合成したプロンプトとネガティブ。ComfyUI向けの画風プリセット集。650以上のスタイルにレンダ済みプレビュー、1000以上の作家記述子、130以上のモディファイアを同梱する。
  - 制約: スタイルの実効はベースモデル依存。AIモデル自体は含まない。CFG1ではネガティブが効かない旨の注意あり。
  - 制作用途: 画風の探索・統一、作品ごとのルック固定に。
  - 出典（2026-09-30確認）: https://github.com/EnragedAntelope/comfyui-stylebook/blob/3ccd87219d061fb549e481843be3c680de341e86/README.md

- **comfyui-imgutils** [integration / AI連携 / 小規模・初期評価候補]
  - アニメ画像（バッチ） → タグ、JSON、マスク、スケルトン、分類スコアなど。deepghs/imgutilsをComfyUI V3 APIでラップしたノード集。アニメ画像のタグ付け・検出・姿勢推定・分割など34ノードを提供する。
  - 制約: READMEに列挙されたノードのみ。モデルは初回にHugging Faceから自動DLされキャッシュされる。
  - 制作用途: データセット作成や生成物の自動判定・前処理に使える。
  - 出典（2026-10-03確認）: https://github.com/xiaden/comfyui-imgutils/blob/f88cd73d17a549281dce4149da0d47c7e09ab870/README.md

- **BooruDatasetTagManagerPlus** [desktop_tool / AI連携 / 活発・実用候補]
  - 画像フォルダ（同名.txtにタグ）、テキスト、OpenAI互換エンドポイント設定 → タグ付き.txt、キャプション、編集済み画像、抽出フレーム。LoRA/キャラ画像データセット用のWindows打標ツール。booruタグ編集、WD14/PixAI/CL/OppaiOracleのONNX自動タグ付け、LLMキャプション、キャラタグ審査、RMBG背景除去、画像編集、動画フレーム抽出を備える。
  - 制約: cl_tagger_v2はgatedで再配布・同梱不可、アクセストークン等が必要との記載。機能はREADME記載範囲に依存。
  - 制作用途: キャラLoRA作成のタグ付け・審査・整理工程を省力化できる。
  - 出典（2026-10-05確認）: https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/94a348f82f41e1e0a3d27a780630df039b560e54/README.md

- **ComfyUI-BatchAnimeTimm** [integration / AI出力の後処理 / 公開済み]
  - 画像フォルダ → 画像ごとの.txtキャプション（カンマ区切りタグ、UTF-8）。フォルダ内の画像を一括でAnimeTimmタグ付けし、1画像につき1つの.txtキャプションを書き出すComfyUI出力ノード。モデルは1回ロードして使い回す。
  - 制約: AnimeTimm本体は同梱されず別途導入が必要。トップレベルフォルダのみ走査する。
  - 制作用途: LoRA/ファインチューン用データセットのタグ付け。
  - 出典（2026-10-07確認）: https://github.com/zzczzcx1/ComfyUI-BatchAnimeTimm/blob/7eaf3a94d19712b906c6e9cc60d330a2a6c7e91d/README.md

- **Anima-Portable-Standalone-Trainer** [training_tool / AIモデル・学習 / v1.0.0（初期）]
  - キャプション付き画像データセット、TOML設定 → 学習済みLoRA/モデル重み、学習中に生成されるサンプル画像。Anima拡散アーキテクチャ（DiT + Qwen3テキストエンコーダ + VAE）向けのLoRA/ファインチューン用スタンドアロン学習UI。kohya-ssの学習スクリプトを改変し、ブラウザUIで操作する。
  - 制約: Anima base重みは研究・非商用限定とREADMEが明記。構成はバージョン1.0の段階。フォルダ移動時はSetEnv.batの再実行が必要。
  - 制作用途: Animaベースモデルへのキャラ・画風LoRA学習。
  - 出典（2026-10-07確認）: https://github.com/official-imvoiid/Anima-Portable-Standalone-Trainer/blob/b07e46a759487b5f96e685325c8213738505d2af/README.md

## 字幕・翻訳・ローカライズ

- **ASMR Dubber** [pipeline / AI連携 / 小規模・制作連携候補]
  - 音声・動画、原文字幕、台本、声の参照 → 字幕、中国語吹替、原声を残した二言語音声・ミックス。日本語・英語の音声や動画を、校正可能な字幕・中国語吹替・二言語音声へ変換する制作ツール。
  - 制約: 主な方向は日英から中国語への制作。ASMR専用生成モデルではない。IndexTTS2.5は任意追加で、基本パッケージへの同梱と混同しない。
  - 制作用途: ASMR作品の翻訳・台本校正・吹替・混音までを扱う具体的な連携候補。 生成音質だけでなく字幕と音声の手修正・再生成のしやすさを比較する。
  - 出典（2026-09-09確認）: https://github.com/EveningStudy/asmr-dubber/blob/bc088faceec743d51f2914e9f7efd98d7b19d9e3/README.md

- **Manga OCR** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 吹き出し等の文字画像 → 日本語テキスト。日本語漫画の縦書き・横書き・ルビ付き文字を認識する。
  - 制約: ページ内の文字領域検出や翻訳・組版は別工程。読み取り品質は素材依存。
  - 制作用途: 漫画の校正・翻訳素材抽出を構成するOCR部品。
  - 出典（2026-09-09確認）: https://github.com/kha-white/manga-ocr/blob/c333b5d36e88d539d6b040b4c4cf90ad5ecd4f69/README.md

- **manga-image-translator** [pipeline / AIモデル・学習 / 比較・既存工程の参考]
  - 漫画・イラスト画像 → 文字除去・翻訳・組版後の画像。画像内の文字を検出・認識・翻訳し、元の文字を修復して訳文を組版する。
  - 制約: 公式説明に公開Webデモの停止記載あり。縦書き・擬音・レイアウト保持の品質は素材で検証が必要。
  - 制作用途: 文字検出・除去・翻訳・組版の複合工程。各段階の中間結果を保存できる構成が評価しやすい。
  - 出典（2026-09-09確認）: https://github.com/zyddnys/manga-image-translator/blob/95227a2bb0fd306cd4f0c104d57284026f991b3a/README.md

- **mokuro** [pipeline / AI連携 / 連携・制作ツール候補]
  - 漫画ページ画像 → .mokuroデータ、互換用HTML。漫画ページの文字位置とOCR結果をまとめ、選択可能なテキストとして閲覧できる形式へ変換。
  - 制約: 主目的は読書支援。ここでは自作漫画の校正・テキスト抽出用の前処理として掲載。翻訳器ではない。
  - 制作用途: ページ単位で位置付き文字を得るため、OCR単体より制作後の校正に接続しやすい。
  - 出典（2026-09-09確認）: https://github.com/kha-white/mokuro/blob/9f79b1281066f953ec6e5d1e7086c401fa8da159/README.md

- **VoiceTransl** [pipeline / AI連携 / 連携の評価候補]
  - 音声、動画、字幕 → 文字起こし、翻訳字幕、動画。音声認識、字幕翻訳、字幕と動画の処理を組み合わせる。
  - 制約: 同名forkと公式配布元を区別。声の生成機能ではない。
  - 制作用途: 台詞や映像の字幕・翻訳をまとめる制作支援。音声生成とは別のローカライズ工程。
  - 出典（2026-09-09確認）: https://github.com/shinnpuru/VoiceTransl/blob/b5f7e5038763aeb3420ac872c0bd191112f92227/README.md

- **xianscan-rust** [pipeline / AIモデル・学習 / 更新が活発な実装候補]
  - 漫画・ウェブトゥーンの画像、フォルダ、ブラウザ拡張で取り込んだページ → 翻訳・組版済みページ、Mihon/Tachiyomi拡張で読めるチャプター。漫画・韓漫・国漫向けのローカル完結型翻訳スタジオ。吹き出し検出、多言語OCR、LLM翻訳、LaMaによるインペイント、組版までを単体バイナリで実行する。
  - 制約: 翻訳品質やOCR精度はREADMEの主張で未検証。GPU無しではCPU推論となる。
  - 制作用途: 既存の漫画翻訳・組版工程をローカルで自動化したい場合の候補。
  - 出典（2026-10-01確認）: https://github.com/ArbenApura/xianscan-rust/blob/075d36f359cdcad1d08ea88d2f4d927640789c26/README.md

- **BallonsTranslator-Pro** [desktop_tool / AIモデル・学習 / 活発・候補]
  - 漫画・コミックの画像、翻訳先言語、各段階のモジュール設定 → 翻訳・植字済みの画像、作業データ。BallonsTranslatorを元にした漫画・コミック翻訳ツールキットで、検出・OCR・翻訳・インペイント・植字を組み替え可能なモジュール群で処理する。
  - 制約: dmMaze/BallonsTranslatorのフォーク。公開時は機械翻訳の明示が要るとREADMEが注意喚起し、人手校正を推奨。
  - 制作用途: 漫画翻訳の一連の工程をGUIとAPIの両方から回せる。
  - 出典（2026-09-30確認）: https://github.com/thomaswantstobeaskeleton/BallonsTranslator-Pro/blob/1cb5af0ca9b87919ffdfe0626167612815baf030/README.md

- **CarrotMangaTranslator** [desktop_tool / AIモデル・学習 / 活発・候補]
  - 漫画画像・ZIP/CBZ/RAR/PDF、用語・人物設定 → 翻訳済み画像、PSD出力、作業データ。漫画原稿のOCR→翻訳→原文消去→植字・検品→出力を扱うデスクトップアプリ。局所GemmaやOpenAI互換APIで翻訳する。
  - 制約: Intel Mac非対応。初回準備にネット接続と空き容量が必要。
  - 制作用途: 漫画翻訳の制作パイプラインを1アプリで完結させやすい。
  - 出典（2026-09-30確認）: https://github.com/ucx0204/CarrotMangaTranslator/blob/a6454549af83d424dc47d871d76734fb8a33187d/README.md

- **Kites** [browser_tool / AIモデル・学習 / 初期評価候補]
  - Web上の漫画・コミック画像 → 翻訳・植字済みのページ画像。ブラウザ拡張として動作し、WebGPU上でOCR・インペイント・翻訳を行って漫画をその場で翻訳表示するツール。
  - 制約: 翻訳はローカルLLM・共有プール・Google翻訳・独自APIから選択。WebGPU環境が前提。
  - 制作用途: ブラウザで読む漫画の下訳・確認作業を軽量化。
  - 出典（2026-09-30確認）: https://github.com/Unheat/Kites/blob/420898820e9ac2d4e91eede871ce48087c411475/README.md

- **lumina** [desktop_tool / AIモデル・学習 / 活発・候補]
  - 漫画のページ画像、プロジェクトファイル(.lmi) → 翻訳済み画像(PNG/JPG)、プロジェクトファイル(.lmi)。漫画・マンファ・マンファ翻訳の無料デスクトップアプリ。テキスト検出・OCR・翻訳・インペイント・組版の全工程を自動化しつつ、各結果を手で修正できる。
  - 制約: 翻訳は外部AI APIキーが必要。モデルは自動同梱されず手動配置/DL。
  - 制作用途: 同人・商業を問わない漫画翻訳ワークフローの中核候補。
  - 出典（2026-09-30確認）: https://github.com/lumina-tl/lumina/blob/bfbf042aff4c18290198f65c18f31430cd3f5a06/README.md

- **yakuyomi-engine** [library / AIモデル・学習 / 活発・候補]
  - 漫画ページのビットマップ → 翻訳済みページのビットマップ(translatePage/PageResult)。端末上で動く漫画翻訳エンジン。検出・OCR・文字消去をNCNNでCPU実行し、翻訳のみネットワークLLMに投げる。読み手アプリYakuyomiに組み込まれる。
  - 制約: アプリではなくライブラリ本体。速度優先で画質は天井を取らない。GPU/NPUは使わずCPU実行とREADMEが明記。
  - 制作用途: Android読書アプリへの翻訳機能組み込みに。
  - 出典（2026-09-30確認）: https://github.com/joyeli/yakuyomi-engine/blob/3d64c43380ff0fd38ead58a35949825ecd9edfcc/README.md

- **translate-manga-br** [web_app / AIモデル・学習 / 小規模・初期評価候補]
  - 漫画ページ画像 → 翻訳オーバーレイ付きページ、SQLite/ローカルファイル。ローカルファーストの漫画翻訳フルスタックアプリ。YOLOで吹き出し検出、PaddleOCRでOCR、翻訳、編集可能オーバーレイ付きリーダーまでを1本で提供する。
  - 制約: 翻訳は外部サービスが必要。規模は小さめでAndroidアプリはベータ。
  - 制作用途: 自前サーバで漫画翻訳と閲覧を回す用途。
  - 出典（2026-09-30確認）: https://github.com/marco0antonio0/translate-manga-br/blob/cb6989b7a978bb3b87f4c6305d972c6d61811b3a/README.md

- **LingoVeil** [web_app / AIモデル・学習 / 小規模・初期評価候補]
  - 画像、PDF、対応漫画サイトの章ページ → 翻訳ビュー、履歴・ブックマーク。漫画・コミック向けのセルフホスト翻訳ツール。画像内のテキストを検出・翻訳し、翻訳ビューで読める。ブックマークや読書進捗も保持する。
  - 制約: 翻訳エンジンごとに対応言語が異なる。新規・小規模。SeamlessM4TはRAM消費が大きいと記載。
  - 制作用途: 自宅サーバとスマホ閲覧を組み合わせた翻訳読書に。
  - 出典（2026-09-30確認）: https://github.com/Gerald-Ha/LingoVeil/blob/dc3e378a7199f7c746fa4a94d7556532885a5386/README.md

- **OverTranslate** [desktop_tool / AIは任意 / 活発・実用候補]
  - 画面キャプチャ（スクリーン/ウィンドウ）、選択テキスト、入力テキスト → 画面にオーバーレイ表示された訳文、コピー可能なテキスト、朗読音声。Windows向けの画面翻訳ツール。スクリーンショット翻訳・リアルタイム翻訳・取詞翻訳・快速翻訳・文字翻訳の5機能を持ち、認識した訳文を元の画面上にそのまま重ねて表示する。
  - 制約: 対応OSはWindowsのみ。OCRはRapidOcrNetのONNXモデルで、翻訳は外部サービスまたはローカルLLMに依存する。READMEに翻訳品質の数値評価の記載はない。
  - 制作用途: 漫画・ゲーム画面を読むための補助ツールとして試しやすい。
  - 出典（2026-10-01確認）: https://github.com/Hon-Lu/OverTranslate/blob/2c9d1ab98e0327837a4df009f6f404fe5b494d18/README.md

- **FumetoReaderPlus** [desktop_tool / AIモデル・学習 / 活発な候補]
  - CBZ/CBR/PDF/EPUB、Komga/Kavita/YACReaderLibraryServerのサーバ → 翻訳済みページ表示、翻訳CBZ。Android向け漫画リーダー。吹き出し検出・OCR・漫画向けLLM翻訳・風船内への再レタリングを端末上で行い、タップで原文に戻せる。
  - 制約: テスト・評価用コードとコーパスは非公開。デスクトップ版は実験的で未対応と明記。
  - 制作用途: 権利を有する漫画の端末内翻訳・閲覧に使える。
  - 出典（2026-10-03確認）: https://github.com/fumetodev/FumetoReaderPlus/blob/a56a4c621b3b6a5a6eb89fa01e0a0a0526cdb677/README.md

- **Solar-Manga-Translator** [desktop_tool / AIモデル・学習 / 小規模・初期評価候補]
  - 画像、画像フォルダ、ZIP、CBZ → 処理済み画像、アーカイブ、プロジェクト（スナップショット）。中国語話者向けのローカル漫画翻訳・校正ワークベンチ。OCR、AI翻訳、擦字補修、自動嵌字、人手校正、導出を一流程にまとめる。
  - 制約: 配布用インストーラ未公開、Windows打包は実験的。翻訳・補修結果は人手確認が必要と明記。
  - 制作用途: 権利を有する画像の翻訳・校正に使える。
  - 出典（2026-10-03確認）: https://github.com/soluna/Solar-Manga-Translator/blob/88864b95044b29ae9e4997594b2c61bc2f066c07/README.md

- **UGTLive** [desktop_tool / AIモデル・学習 / 稼働中・実運用候補]
  - 画面キャプチャ、画像、PDF/CBZファイル → 翻訳テキスト/オーバーレイ、音声読み上げ、HTMLエクスポート、翻訳済み画像。Windows向けGUIツールで、画面や画像の文字を「ライブ」でOCR・翻訳する。縦書き日本語の漫画読み上げ、PDF/CBZ/画像の一括変換、音声読み上げ、リアルタイム字幕にも対応する。
  - 制約: Windows/NVIDIA前提でAMD/Intelは未検証。高品質翻訳や音声はOpenAI/Gemini/ElevenLabs等の外部APIキーが必要。ライセンスはBSD系の帰属表示。
  - 制作用途: 漫画やゲーム画面の翻訳を手元で高速に回したいローカライズ作業に向く。
  - 出典（2026-10-04確認）: https://github.com/SethRobinson/UGTLive/blob/f647679dcc384aba2ed9178172d227db8e79effd/README.md

- **manga-translator** [desktop_tool / AI連携 / 稼働中]
  - 画像ファイル、画像URL、クリップボードの画像 → 原文/訳文テキスト（コピー可能）、複数画像のナビゲーション表示。Gio製GUIのデスクトップアプリで、画像内のテキストをOCRして翻訳する。検出した全テキストに色付きボックスを表示し、クリックで原文と訳文を確認・コピーできる。
  - 制約: クラウドAPIキーが必須でローカル完結しない。OCR/翻訳はGoogle/DeepL依存。ライセンスはMIT。
  - 制作用途: 大量処理よりも、数枚の画像を目視で確認しながら訳したい作業に向く。
  - 出典（2026-10-04確認）: https://github.com/cameronkinsella/manga-translator/blob/3b1139c8f446ef4e9e5b3776e415038ec2a73f4c/README.md

- **AutoScanlate-AI** [pipeline / AIモデル・学習 / 小規模・初期評価候補]
  - 漫画/コミックの画像またはZIP → 翻訳済みページ画像。完全ローカル・GPU加速の漫画翻訳パイプライン。YOLOv8で吹き出し検出、MangaOCRで縦書きOCR、Qwen 2.5 7Bで文脈翻訳、マスク付きインペイントと段組みで元画像に描き戻す。Goバックエンド+Next.js UI+Pythonワーカーの構成。
  - 制約: ライセンスはNOASSERTION。性能値はREADME記載の環境依存。WindowsではMangaOCRをCPU実行する等の制約がある。
  - 制作用途: 大量ページの下訳・たたき台作成に有効。最終校正は人手前提。
  - 出典（2026-10-05確認）: https://github.com/P4ST4S/AutoScanlate-AI/blob/fa734c06add489479a306f5923726040a92a467b/README.md

- **manga-translator-android** [desktop_tool / AIモデル・学習 / 活発に開発中]
  - 漫画画像（フォルダ/画像ファイル、CBZ/ZIP/PDF） → ページごとの翻訳結果JSON（OCRキャッシュ含む）、翻訳气泡を重ねたページ、フォルダ単位のglossary.json。Android向けの漫画翻訳アプリ。ローカルで气泡・文字検出とOCRを行い、OpenAI互換APIで翻訳。翻訳气泡を原画上に重ね、位置をドラッグで調整できる。屏幕翻訳/悬浮窗にも対応。
  - 制約: 翻訳にはOpenAI互換APIのKeyが必要。OCR/検出モデルは各自でassetsへ配置する必要がある。翻訳順は画像ファイル名順に依存。
  - 制作用途: 手元の漫画をスマホで読みながら翻訳する個人用途。
  - 出典（2026-10-07確認）: https://github.com/jedzqer/manga-translator-android/blob/e4f55e078720c4f033e1c1b97bcef034b01985fc/README.md

- **local_anime_dubber** [pipeline / AIモデル・学習 / 試作（prototype）]
  - 日本語動画、ボイス参照音声 → 英語吹き替え済み動画（mp4）。日本語動画と短い声サンプルから英語吹き替えをローカル生成するパイプライン。声質をクローンし、BGM/効果音を残したままセリフのタイミングを映像に合わせる。
  - 制約: 単一話者のみ対応。発音・リップシンク等に多くの課題が残ると作者が明記。ライセンス表記なし。
  - 制作用途: 吹き替えワークフローの検証・実験。
  - 出典（2026-10-07確認）: https://github.com/Bugsbunnydev2000/local_anime_dubber/blob/3321d6f202d1e7631e8a64395edf4333377ca002/README.md

## モーション・身体演技

- **ARDY** [model_toolkit / AIモデル・学習 / モデル・研究候補]
  - 動作記述、骨格別の制約 → 対応骨格の動作列。テキストと運動学的制約から、対応骨格のモーションを生成する。
  - 制約: CoreとG1で骨格・fps・予測長が異なる。テキストエンコーダのメモリを本体から分ける。
  - 制作用途: 経路や姿勢制約を与えるキャラ動作生成として比較価値がある。
  - 出典（2026-09-09確認）: https://github.com/nv-tlabs/ardy/blob/693f74d13b3d04a0a22ce127ee79c929dd89756b/README.md

- **EchoAvatar** [pipeline / AIモデル・学習 / 小規模・初期候補]
  - 音声ストリーム、アバター → 顔と身体の動作、Unity表示。ストリーミング音声から顔・身体の動きを生成してUnityアバターへ送る。
  - 制約: 公開された音声エンコーダだけで顔・体全体のモデルが揃うとは言えない。複数マシン構成。
  - 制作用途: 対話キャラクターの発話に身体演技を足す実験候補。
  - 出典（2026-09-09確認）: https://github.com/RobinWitch/EchoAvatar/blob/174ca5dc6a535a557177cf6703cc9a5338a17bc7/readme.md

- **Gelina** [model_toolkit / AIモデル・学習 / 小規模・初期候補]
  - テキスト・参照音声・動作条件 → 音声と身体ジェスチャー。音声とジェスチャーの生成・クローニング・音声から動作への変換を扱う。
  - 制約: Google Drive配布の中身・取得成功は未確認。モード別の入力と必要モデルが異なる。
  - 制作用途: 音声と身振りの協調を調べる研究候補。
  - 出典（2026-09-09確認）: https://github.com/TGuichoux/Gelina/blob/bd50c64661498855b41300fa3d3b983819d0175a/README.md

- **HY-Motion 1.0** [model / AIモデル・学習 / モデル・研究候補]
  - 動作テキスト → 人型モーション。テキストから人型キャラクターの3D動作を生成する。
  - 制約: 非人型・複数人・シームレスループ・in-placeは公式の非対応項目。追加LLMのVRAMは表に含まれない。
  - 制作用途: 人型の単発演技を作る候補。ゲームの常時ループには追加編集が必要。
  - 出典（2026-09-09確認）: https://github.com/Tencent-Hunyuan/HY-Motion-1.0/blob/4e426f5a1021cbcf7f375458c37b840ee7225229/README.md

- **R-DMesh** [model / AIモデル・学習 / 小規模・初期候補]
  - 静的メッシュ、参照動画 → 動的メッシュ列。静的メッシュを参照動画に沿って動く4Dメッシュ列へ変換する。
  - 制約: 4Dメッシュ列と再利用可能な骨格モーションは同一ではない。リグ転送は別問題。
  - 制作用途: 骨格で表しにくい変形の映像制作に適する研究候補。
  - 出典（2026-09-09確認）: https://github.com/Tencent-Hunyuan/R-DMesh/blob/467cb35a9f53f6d61a0b36a5aa4e171e4d40ad0f/README.md

- **VRM-Spacing-Animation-Baking** [integration / 非AI制作 / 小規模・初期評価候補]
  - VRM 1.0モデルとアクション(アニメーション) → 物理ベイク済み・ループ調整済みのアニメーション。VRM 1.0モデル向けBlenderアドオン。腕・脚・肩の間隔をMixamo風に調整し、髪やバストの物理ボーンをアニメへ焼き込み、ループ化する。
  - 制約: VRM 1.0限定。外部のVRM Add-onと併用が前提。AI機能は含まない。
  - 制作用途: VRMキャラのモーション最終調整や衣装・体型差の補正に。
  - 出典（2026-09-30確認）: https://github.com/Meringue-Rouge/VRM-Spacing-Animation-Baking/blob/dc2a4a4aabb741f2eb30683e6883c3e3dd399512/README.md

## VFX・材質・ベクター演出

- **Effekseer** [desktop_tool / 非AI制作 / 制作基盤として比較]
  - テクスチャ、メッシュ、効果の時間・発生設定 → 編集可能なエフェクトとランタイム再生。ゲーム向けのパーティクル効果を編集し、ランタイムで再生する。
  - 制約: 動画生成型VFXとは出力が異なる。実機での描画負荷とシェーダ互換性は別途確認。
  - 制作用途: 魔法・攻撃・演出をゲームに組み込む実用候補。
  - 出典（2026-09-09確認）: https://github.com/effekseer/Effekseer/blob/6cf1cb853383765153219ba5ce9b47eff5ad8398/README.md

- **GenCompositor** [model / AIモデル・学習 / 小規模・初期候補]
  - 前景動画、背景、マスク・動き条件 → 合成動画。前景・背景と制御条件を用いて動画を生成合成する。
  - 制約: 従来の合成ソフトと同じ画素保持を保証しない。マスクと参照条件が必要。
  - 制作用途: キャラを背景へ自然に馴染ませる短編映像の研究候補。
  - 出典（2026-09-09確認）: https://github.com/TencentARC/GenCompositor/blob/a2aedd619fac71c9420a56ce7b8885f98a29c612/README.md

- **Material Maker** [desktop_tool / 非AI制作 / 制作基盤として比較]
  - ノードグラフ、画像、3D素材 → 材質用テクスチャ・ペイント結果。ノードで手続き的なテクスチャを作り、3Dモデルへのペイントも行う。
  - 制約: 生成AIモデルではない。出力先のPBRチャンネルと色空間を合わせる必要がある。
  - 制作用途: ゲーム・背景・トゥーン素材の反復制作に向く。
  - 出典（2026-09-09確認）: https://github.com/RodZill4/material-maker/blob/ad19fcf0ee34a7caf74df709dc4de7112f0d467d/README.md

- **OmniLottie** [model / AIモデル・学習 / モデル・研究候補]
  - テキスト、画像等の視覚条件 → Lottie JSON、ベクターアニメーション。テキスト・画像等から編集可能なLottieベクターアニメーションを生成する。
  - 制約: ラスタ動画やLive2Dリグとは別形式。重みのライセンスメタデータは未設定。
  - 制作用途: 配信画面の動くアイコンやゲームUIの短い演出に新しい選択肢。
  - 出典（2026-09-09確認）: https://github.com/OpenVGLab/OmniLottie/blob/26131278e7b46bc2f64f989b25bb816f9e07c528/README.md

- **VfxDB** [model_toolkit / AIモデル・学習 / 小規模・初期候補]
  - 条件ボリューム、設定、学習データ → 密度ボリューム、推論のNPZ等。OpenVDB由来の疎な3Dボリューム効果を学習・生成する。
  - 制約: データ・重みはCC BY-NC 4.0。動画VFXと違い体積データ。全データは作者表記4.6TB。
  - 制作用途: 煙などを3Dシーンで扱う研究候補。まず小規模サンプルで形式変換を評価。
  - 出典（2026-09-09確認）: https://github.com/VfxDB-Official/VfxDB/blob/eaf0530af2067e9d0ffcdfc4fdbb114499037cf8/README.md

- **VFXMaster** [model_toolkit / AIモデル・学習 / 小規模・初期候補]
  - 参照効果動画、対象条件 → 効果を伴う動画。効果の参照映像を条件に動的なVFX動画を生成する。
  - 制約: エフェクトごとのLoRA方式との比較研究。ゲーム用パーティクルデータは出力しない。
  - 制作用途: 短い映像へ未知の効果を移す研究候補。VRAM要件は個人環境での障壁。
  - 出典（2026-09-09確認）: https://github.com/libaolu312/VFXMaster/blob/0632c5a9979586adc1d4f96632e5b808ee11712f/README.md

- **cHiDeScaler-Neo** [desktop_tool / AIモデル・学習 / 小規模・初期評価候補]
  - 任意のWindowsウィンドウ映像(リアルタイムキャプチャ) → 拡大・フレーム補間された映像出力。Windowsの任意ウィンドウをリアルタイムキャプチャし、GLSL/ONNXでAI拡大とRIFE系フレーム補間をかけるポータブルアプリ。Anime4K等のシェーダ資産を利用できる。
  - 制約: HDR非対応でSDR前提。一部同梱モデル/シェーダのライセンス情報は整理中と明記。
  - 制作用途: 映像素材のアップスケールや補間、視聴環境の画質底上げに。
  - 出典（2026-09-30確認）: https://github.com/animeojisan/cHiDeScaler-Neo/blob/1e8fb3e7378b7df99709393087578ea7bc55d209/README.md

- **ComfyUI-CustomNodePacks** [workflow_tool / AI連携 / 活発・実用候補]
  - 画像、動画、マスク、プロンプト → マスク、合成画像、EXR/レンダーパス、自動連番出力。ComfyUI向けの大規模カスタムノード群（142ノード）。SAM2.1/SAM3セグメンテーション、alpha matting、inpaintのcrop/stitch、動画マスク伝搬、EXR入出力・LUT等のVFXツールを含む。
  - 制約: RMBG-2.0バックエンドは商用不可でBRIAのライセンスが必要と明記。torch/numpy等を再インストールするとComfyUIを壊す恐れがあると注意喚起。
  - 制作用途: レイヤ分離・マスク処理・VFX工程の自動化に有効。RMBG利用時の商用条件に注意。
  - 出典（2026-10-05確認）: https://github.com/Code2Collapse/ComfyUI-CustomNodePacks/blob/cbfd4abead2d03c1fb3c619263b135f21c54cc54/README.md

## 絵コンテ・制作管理・評価

- **Kitsu** [web_app / 非AI制作 / 制作基盤として比較]
  - アセット、ショット、タスク、レビュー素材 → 制作管理画面と進行情報。アニメ・VFX・ゲーム制作の成果物、レビュー、進行を管理するWebアプリ。
  - 制約: このフロントエンドだけで全サービスが完結するとは扱わない。画像生成器ではない。
  - 制作用途: 素材数・改訂数が増えた制作の受け渡しとレビュー整理に向く。
  - 出典（2026-09-09確認）: https://github.com/cgwire/kitsu/blob/6cf2e8e77b1172dff970286ea6098502579239f2/README.md

- **Storyboarder** [desktop_tool / 非AI制作 / 既存研究・制作の参考]
  - ラフ画、ショット、台詞・時間 → 絵コンテ・アニマティクス。絵コンテを描き、ショットの順序と時間を試すアニマティクス制作ツール。
  - 制約: 最終push2024年。最新OS・配布版の導入状態は再確認が必要。
  - 制作用途: 生成回数を増やす前にカット割りを固定する道具として有用。
  - 出典（2026-09-09確認）: https://github.com/wonderunit/storyboarder/blob/8b81a25c71d5f7ca46e8d5b8e3d4f7b3968f95c2/README.md

- **StyleID** [model / AIモデル・学習 / 小規模・初期候補]
  - 一人の顔を含む画像 → 正規化された特徴ベクトル・類似度。画風変化に強い顔の同一性特徴を計算し、比較・検索・評価に使う。
  - 制約: 複数顔には不適、顔の中央クロップを推奨。非商用研究用と記載。画像生成器ではない。
  - 制作用途: 絵柄を跨ぐキャラの一貫性評価を補助する候補。自動合否の唯一の指標にはしない。
  - 出典（2026-09-09確認）: https://github.com/kwanyun/StyleID/blob/bbb917dcc350d24456be6cb7dbb9fe5f4aa05c00/README.md

- **Nomi** [desktop_tool / AIモデル・学習 / 活発・候補]
  - 作りたい内容のテキスト、参照カード、接続した動画・画像生成モデル → 生成されたキーフレームと動画クリップ、タイムライン、MP4書き出し、プロジェクトフォルダ。ローカル優先のAI動画制作スタジオ。エージェントがショット分割・キーフレーム生成・動画化・タイムライン配置を支援する。
  - 制約: LinuxやWindows arm64のインストーラは未配布。macOSビルドは署名・公証なし。モデル利用は提供元への課金。
  - 制作用途: 絵コンテから動画素材の初稿作成までの流れをローカルで管理。
  - 出典（2026-09-30確認）: https://github.com/aqm857886159/Nomi/blob/2094010c4b840314b0fffaea030d8b97e32ff275/README.md

## GitHub以外のアニメ画像モデル

- [Anima](https://huggingface.co/circlestone-labs/Anima/blob/f973fc41ec7545364ac9776c2440285f43ff2a30/README.md): Cosmos-Predict2-2Bを基にした2B画像モデル。Qwen系テキストエンコーダとQwen-Image VAEを組み合わせる。 metadataはother、license_nameはcirclestone-labs-non-commercial-license。公開重みを無条件商用可と扱わない。
- [Animagine XL 4.0 / Opt](https://huggingface.co/cagliostrolab/animagine-xl-4.0/blob/2b7c1b397761bf5bd3cc42e5b39ec99314a75a96/README.md): Stable Diffusion XL1.0から学習したアニメ向け画像モデル。 CreativeML Open RAIL++-Mをモデルカードが案内。利用制限と派生モデル条件は原文を参照。
- [Illustrious XL early release v0](https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0/blob/dca0dac303e6dc4b0c31d8001bc685b89b5d0204/README.md): SDXL系のイラスト生成基盤。カードのbase_modelはKohaku XL beta5。 metadataはfair-ai-public-license-1.0-sd。派生モデルが追加条件を持つ場合は別途確認する。
- [NoobAI XL 1.1](https://huggingface.co/Laxhar/noobai-XL-1.1/blob/814a274af2b8097c0828819d561ec74c7d0c6cea/README.md): Illustrious系のアニメ画像モデル。直接のbase_modelはNoobAI XL1.0。 HFメタデータのFAIPL表記に加え、モデルカード本文にモデル・派生・生成物を含む商用禁止と共有条件を記載。本文の追加条件を見落とさない。
- [manga-panel-detector-yolo26n](https://huggingface.co/leoxs22/manga-panel-detector-yolo26n/blob/40a2854663d537563cfb95c370288a84c6505b9a/README.md): Ultralytics YOLO26-nano（2.57Mパラメータ）を、Manga109-sでパネルとテキストの2クラス検出にファインチューニングしたモデル。入力は640x640。 重みはAGPL-3.0（Ultralytics YOLO26由来）。以前はApache-2.0と表示していたが誤りだったと作者が訂正。クローズドな商用製品にはUltralytics Enterprise Licenseが必要と記載。
- [Hy-MT2-1.8B-JP-Manga-Finetune-v5-GGUF](https://huggingface.co/fumetodev/Hy-MT2-1.8B-JP-Manga-Finetune-v5-GGUF/blob/e17bc6a8dd92ddf930bd7858ceb916117ee5f916/README.md): tencent/Hy-MT2-1.8Bを日本語→英語の漫画セリフ翻訳向けにファインチューニングしたモデル（HunYuanDenseV1ForCausalLM）。Q4_K_MのGGUFとマージ済みbf16重みの両方を同梱。 Apache-2.0（baseモデル tencent/Hy-MT2-1.8B に準拠）。
- [Illustrious-XL-v2.0](https://huggingface.co/OnomaAIResearch/Illustrious-XL-v2.0/blob/69459c1fe6f46db41ab31e6114f05acc0e06bcaa/README.md): アニメ特化のtext-to-imageモデル(ヴェースはSDXL系)。公式のv2系チェックポイントを公開している。 licenseはcreativeml-openrail-m。
- [HDM-xut-340M-anime](https://huggingface.co/KBlueLeaf/HDM-xut-340M-anime/blob/7c9e455a9722811bd9eec7eb38b4c8712a7ef290/README.md): 独自バックボーンXUT(Cross-U-Transformer)を用いる約340Mのアニメ向けtext-to-imageベース。TREAD併用で家庭用ハード/格安サーバでの学習を狙う。 licenseはcc(具体的なCC種別はカードに明記されていない)。
- [anime-painter](https://huggingface.co/xinsir/anime-painter/blob/18185a73b6e7fe49f2f2de1bb9d7db0b74a41773/README.md): SDXLベースのscribble ControlNet。ラフな線画からアニメ調画像を生成する。 licenseはapache-2.0。
- [Galgame-Llasa-3B](https://huggingface.co/OmniAICreator/Galgame-Llasa-3B/blob/23134f66585fe17c0e72bdeb737c9f71bb89d0db/README.md): Llasa-3B(HKUSTAudio)をベースに、ギャルゲー音声データセットで日本語向けに微調整したTTSモデル。 licenseはCC-BY-NC-4.0(非商用)。
- [Audio2Face-3D-v3.0](https://huggingface.co/nvidia/Audio2Face-3D-v3.0/blob/b74132732fd9a9d29b237bec193ded64c9745e91/README.md): Hubert系エンコーダと拡散機構を組み合わせ、音声から3D顔モーション(肌・舌・顎・眼球)を生成する約1.8億パラメータのモデル。 license_nameはnvidia-open-model-license。カードは商用/非商用利用可と記載。
- [IndexTTS-2.5](https://huggingface.co/IndexTeam/IndexTTS-2.5/blob/c39ce5ba981572cb187443877ff559dfb246ce63/README.md): GPTバックボーン＋フローマッチングの音声-to-メルデコーダ＋BigVGANボコーダで構成される自己回帰ゼロショットTTS。GPTバックボーンは約0.8B。出力は22.05kHz。 licenseはother、license_nameはbilibili-model-license。公開重みを無条件の商用可として扱わない。
- [Qwen2D-Anime-VAE](https://huggingface.co/Anzhc/Qwen2D-Anime-VAE/blob/d59c106b50524909ac660cd97a32fdf49b2f8f21/README.md): Qwen Image VAE(非テンポラル版)のデコーダを調整したVAE。ComfyUI用ノードパック(anzhc-qwen2d-comfyui)から使用する。 apache-2.0。
- [ml-danbooru-onnx](https://huggingface.co/deepghs/ml-danbooru-onnx/blob/eb9058324a741f1b90d4db168f6e1d6b6cb7e63d/README.md): ML-DanbooruのONNX変換版。Caformer-M36（畳み込み＋Transformer）とTResnet-D系の画像分類モデルで、Danbooru系タグを推定する。 mit。
- [Irodori-TTS-500M-v2-Character-Voice-Tagger](https://huggingface.co/p1atdev/Irodori-TTS-500M-v2-Character-Voice-Tagger/blob/3fe62991c9e86d275a57e879ba62cff85c8cf18a/README.md): Aratako/Irodori-TTS-500M-v2をベースに、SmilingWolf/wd-vit-tagger-v3を画像エンコーダとして条件付けに加えた日本語TTS。参照音声や声色キャプションの代わりにキャラクター画像の特徴を使い、ゼロショットでキャラの雰囲気に合う声を合成する。 MIT。ベースのIrodori-TTS-500M-v2および画像エンコーダ（Apache系）の条件は別途確認が必要。
- [Irodori-TTS-500M-v2-Character-Voice-SigLIP](https://huggingface.co/p1atdev/Irodori-TTS-500M-v2-Character-Voice-SigLIP/blob/b5954e439b7b1a4a452d56ec6a15e079be56c99f/README.md): Aratako/Irodori-TTS-500M-v2をベースに、timm/vit_base_patch16_siglip_512.v2_webliを画像エンコーダとして使う日本語TTS。キャラクター画像を条件に話者スタイルを制御する。 MIT。ベースモデルと画像エンコーダ側の条件は別途確認が必要。
- [Irodori-TTS-500M-v2-VoiceDesign](https://huggingface.co/Aratako/Irodori-TTS-500M-v2-VoiceDesign/blob/456e55708e7183f5c7faa1448209d54aa8991451/README.md): 約500MのRectified Flow Diffusion Transformer（RF-DiT）による日本語TTS。v2系の参照音声エンコーダをキャプションエンコーダに置き換え、話者・感情・話し方をテキスト記述だけで設計できる。音声はSemantic-DACVAE-Japanese-32dimの32次元潜在で48kHz再構成。 MIT。加えて、実在人物の声の模倣や誤情報生成を禁じる倫理制限がカードに明記されている。キャプションには話者名は含まれない。
- [anime-censorship-tagger-mnv3-384](https://huggingface.co/Maltox/anime-censorship-tagger-mnv3-384/blob/b6c017a5c9ee4273f27db51b0fe96956184ffa0e/README.md): MobileNetV3-Large（約4.2M）をEVA-02-Large教師から蒸留したONNX分類器。384×384のsquash入力を共有し、censored／bar／mosaicを独立シグモイドで出力する。 Apache-2.0（教師モデルwd-eva02-large-tagger-v3とバックボーンtimmもApache-2.0）。再配布時は帰属表示が必要。
- [asmr-trigger-audio-h3-lora](https://huggingface.co/vpakarinen/asmr-trigger-audio-h3-lora/blob/9369cad86bc549caa9e0d8f6f1c812aad4fc2e33/README.md): MiniMaxAI/MiniMax-H3をベースにしたLoRAアダプタ。囁き系ASMRの音響と、それに対応する映像（T2V/I2V）を生成する。 Apache-2.0。ベースのMiniMax H3およびその他アダプタの条件は別途確認が必要。
- [Galgame-Llasa-3B-v3](https://huggingface.co/OmniAICreator/Galgame-Llasa-3B-v3/blob/880454ae1697e6a397df39c7bdc0d16a3b21d543/README.md): HKUSTAudio/Llasa-3Bを基に、ギャルゲー系の日本語音声データで微調整した日本語テキスト音声合成モデル。 metadataのlicenseはcc-by-nc-4.0。商用利用は不可として扱う。
- [Galgame-Llasa-1B-v3](https://huggingface.co/OmniAICreator/Galgame-Llasa-1B-v3/blob/e3f797a5a51bf6811e28b6e2be8650dba7322aa3/README.md): HKUSTAudio/Llasa-1B-Multilingualを基に、ギャルゲー音声や日本語アニメ音声データで微調整した日本語テキスト音声合成モデル。 metadataのlicenseはcc-by-nc-4.0。商用利用は不可として扱う。
- [Manga-Bubble-YOLO](https://huggingface.co/Kiuyha/Manga-Bubble-YOLO/blob/fb646500455e8a8a3a807fd27b855c8e4fc63766/README.md): Manga109-sとMangadex由来画像で学習したYOLO26ベースのテキスト領域検出モデル。NMS不要のend-to-endヘッドを持つ。 カード表記のlicenseはapache-2.0。学習元データのManga109-sには別途利用条件がある。
- [MiniMax-H3-Rough-2D-Cartoon-Illustration](https://huggingface.co/prithivMLmods/MiniMax-H3-Rough-2D-Cartoon-Illustration/blob/fc40d010a2b44fd4caa4b750b6f503eca5d61577/README.md): MiniMax-H3をベースに、2Dカートゥーン風の動的イラスト動画データで学習したLoRAアダプタ。 metadataはother、license_nameはminimax-h3-community-license。ベースモデルの条件に従う。
- [AnimeBackgroundGAN-Shinkai](https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Shinkai/blob/d162ca947aab5aa943c3586bda550812831d5cf4/README.md): CartoonGAN（Chen et al., CVPR18）の新海誠スタイル学習済みモデル。PyTorch実装で重みを配布する。 metadataのlicenseはmit。
- [CharacterSheet](https://huggingface.co/Alissonerdx/CharacterSheet/blob/3dc4295163dacc924d213168d67bf16850fd954f/README.md): 画像編集ベースのLoRA群。FLUX.2 Klein 9BとKrea 2向けに、参照キャラ画像からマルチビューのキャラクターシートを生成する。学習は約300例のキャラクターシートで、人間キャラ中心。 metadataはother、license_nameはcivitai-model-license、license_linkはcivitai。無条件の商用利用可とは扱わない。
- [Live2Diff](https://huggingface.co/Leoxing/Live2Diff/blob/0e6801b3e805e37a6e27f99aa9e8ee6574d748c6/README.md): 単方向テンポラルアテンションとマルチタイムステップKVキャッシュを用いた動画拡散モデル（Stable Diffusion系）。リアルタイムのストリーム翻訳（video-to-video）を目的とし、LCM-LoRAとStreamDiffusionで高速化する。 Apache-2.0。
- [japanese_speecht5_tts](https://huggingface.co/esnya/japanese_speecht5_tts/blob/21d6e52032f74123966ac8a3717e23fdfb7809b0/README.md): microsoft/speecht5_ttsをベースに、Open JTalk（pyopenjtalk）ベースの改修トークナイザを組み合わせた日本語TTS。JVSコーパス（100話者）でファインチューニングしている。 モデルカードのlicenseは未設定。JVS Corpusのライセンスを継承すると記載され、商用利用可否は明記されていない。
- [noob-sdxl-controlnet-lineart_anime](https://huggingface.co/Eugeoter/noob-sdxl-controlnet-lineart_anime/blob/61ed2d40710b32a5a1c9873f7dec89ff0af9f2a4/README.md): Laxhar/sdxl_noob（NoobAI-XL）をベースにしたSDXL向けlineart ControlNet。pipeline_tagはtext-to-imageで、controlnet形式の重みを含む。 metadataはother、license_nameはfair-ai-public-license-1.0-sd、license_linkはfreedevproject.org。無条件の商用利用可とは扱わない。
- [storyboard-sketch](https://huggingface.co/blink7630/storyboard-sketch/blob/be328fecdfe3fb053a500376283013f34f99eebb/README.md): SDXL Baseをベースに、60枚のグレースケール絵コンテスケッチとキャラクター肖像で学習したLoRA。21:9・16:9・1:1の比率を含む。 metadataはother。ベースはstabilityai/stable-diffusion-xl-base-1.0。無条件の商用利用可とは扱わない。
- [visual_novel_tts](https://huggingface.co/spow12/visual_novel_tts/blob/e66a75464838470fce23457b9c216a929420237d/README.md): Style-Bert_VITS2をベースにした日本語TTSモデル。ビジュアルノベル（Senren*Banka、Café Stella and the Reaper's Butterflies、Riddle Joker等）のキャラ音声を対象に学習している。 licenseはcc-by-nc-4.0。READMEも研究目的・個人利用限定・商用不可と明記している。
- [Visual-novel-transcriptor](https://huggingface.co/spow12/Visual-novel-transcriptor/blob/0a51fa1107b6ef36276e33de5d5f6600012e85c8/README.md): distil-whisper/distil-large-v2をファインチューニングした日本語ASR（Seq2Seq）。ビジュアルノベルの音声の文字起こしを目的とする。 metadata上のlicenseはnull。モデルカードは「現在は非商用利用のみ」と記載しており、商用可とは扱わない。
- [bg-visualnovel-v03](https://huggingface.co/vinesmsuic/bg-visualnovel-v03/blob/4fe98d1d8d6b0b518fe40023e1c5c06e171edaa6/README.md): Anything-V3をベースにしたStable Diffusion系のテキストto画像モデル。ビジュアルノベル背景の生成を目的とする。 licenseはcreativeml-openrail-m。商用利用や再配布は同ライセンスの制限を引き継ぐ条件付き。
- [Manga109-panel-balloon-text-yolov26-segmentation](https://huggingface.co/ShadowB/Manga109-panel-balloon-text-yolov26-segmentation/blob/3a860269ee0beb43ce9f31d82c7851441eb178ae/README.md): Ultralytics YOLO26sのインスタンスセグメンテーションモデル。frame/text/balloonの3クラスを検出・分割する。ベースはyolo26s-seg.pt。 モデルリポジトリのlicenseはmit。ただし学習データ（Manga109系）のライセンス/アクセス条件は別途適用されると記載。
- [controlnet-lineart-anime-sdxl-fp16](https://huggingface.co/r3gm/controlnet-lineart-anime-sdxl-fp16/blob/e02330c836049b89f122aa18625ae027537ea143/README.md): SDXL用のControlNet（lineart、anime向け）。fp16のdiffusion_pytorch_modelを配布する。 licenseはcreativeml-openrail-m。商用可否は同ラインモデルの制限に従う。
- [Z-Image_Anime_VAE](https://huggingface.co/Anzhc/Z-Image_Anime_VAE/blob/7272e1c80536d207cc294968eb09c8d44e46b3a6/README.md): Z-Image（Flux）のAEをアニメイラストデータでデコーダ微調整したVAE。既存パイプラインのae.safetensorsの代わりに読み込む。 licenseはapache-2.0。base_modelはTongyi-MAI/Z-Image-Turboと記載。
- [AnimeBackgroundGAN-Miyazaki](https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Miyazaki/blob/c93786c4e4766e43afd2949ca7314ccad61f1d79/README.md): CartoonGAN（Chen et al., CVPR18）を宮崎駿作品の背景で学習した画像変換モデル。PyTorch実装で構成される。 licenseはMIT。モデル/Spacesの再パッケージはShō Akiyama。
- [girl-style-bert-vits2-JPExtra-models](https://huggingface.co/Mofa-Xingche/girl-style-bert-vits2-JPExtra-models/blob/bb4f103fa602e4c5b59226b3466e62b6cb09e3f9/README.md): Style-Bert-VITS2 2.1 JP-Extraをベースにした多話者TTS。5人の日本語話者（女性4・男性1）と25種の感情スタイルを持つ。 licenseはmit（カードにlicence FREE(MIT)と記載）。
- [style_bert_vits2_jp_extra_asmr_original](https://huggingface.co/RikkaBotan/style_bert_vits2_jp_extra_asmr_original/blob/1feb9152f9974062d5a32a12aab725e4600c945c/README.md): Style-Bert-VITS2 JP-Extraを作者本人の音声で学習した日本語TTS。ささやき演技向けのASMR版。 licenseはcc-by-sa-4.0。カードは商用・非商用問わず利用可とするが、二次配布禁止・ゾーニング必須などの条件があり、商用可否は断定しない。
- [best-comic-panel-detection](https://huggingface.co/mosesb/best-comic-panel-detection/blob/bbab11504194d0b341ac3f6099f3592aa0604ae3/README.md): YOLOv12xをベースに、コミックページのコマ（Comic Panel）検出用にファインチューニングした物体検出モデル。クラスはComic Panelの1種。 metadataはapache-2.0。学習データはRoboflowのカスタムデータセット。
- [Waifu-Inpaint-XL](https://huggingface.co/ShinoharaHare/Waifu-Inpaint-XL/blob/a33e08f2ce957d0bd9974edddbe70fcd9b8f1680/README.md): SDXLベースのインペインティング用モデル。unet/text_encoder/text_encoder_2/vaeのdiffusers構成と単一safetensorsを配布する。 metadataはopenrail++。
- [Qwen3.5-4B-Danbooru-Prompt-Generator](https://huggingface.co/TRYZER01/Qwen3.5-4B-Danbooru-Prompt-Generator/blob/d54023fefd8433c0b27356c146f34d58395001ac/README.md): Qwen3.5-4B系テキスト専用LLMをマージしたモデル。Danbooruタグ列を入力に、タグ列のプロンプトへ展開する。ComfyUIノードからHTTPでモデルサーバー（LM Studio等）に問い合わせる構成。 metadataはapache-2.0。上流Qwen3.5-4Bのライセンスにも従う。
- [waifu-scorer-v3](https://huggingface.co/Eugeoter/waifu-scorer-v3/blob/c2a747fd61d310a90e9cbbf8fc590c522f234424/README.md): CLIP特徴量にMLPを重ねた美観スコアラ。アニメ風画像を0〜10で採点する。 metadataはopenrailだが、カード本文はApache 2.0と記載され両者で表記が一致しない。商用利用の可否を断定しない。

## 保留情報

DeepASMR（2026）は論文と音声デモを確認しましたが、対応する公式推論実装・重みは未特定です。実装公開済みとして推薦しないでください。詳細はreviewed-not-included.json。
