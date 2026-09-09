# モデルに渡す制作リサーチ・コンテキスト

一覧更新日: 2026-09-09。**115件 / 18分野**。各項目の確認日はJSONに記録。

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

## GitHub以外のアニメ画像モデル

- [Anima](https://huggingface.co/circlestone-labs/Anima/blob/f973fc41ec7545364ac9776c2440285f43ff2a30/README.md): Cosmos-Predict2-2Bを基にした2B画像モデル。Qwen系テキストエンコーダとQwen-Image VAEを組み合わせる。 metadataはother、license_nameはcirclestone-labs-non-commercial-license。公開重みを無条件商用可と扱わない。
- [Animagine XL 4.0 / Opt](https://huggingface.co/cagliostrolab/animagine-xl-4.0/blob/2b7c1b397761bf5bd3cc42e5b39ec99314a75a96/README.md): Stable Diffusion XL1.0から学習したアニメ向け画像モデル。 CreativeML Open RAIL++-Mをモデルカードが案内。利用制限と派生モデル条件は原文を参照。
- [Illustrious XL early release v0](https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0/blob/dca0dac303e6dc4b0c31d8001bc685b89b5d0204/README.md): SDXL系のイラスト生成基盤。カードのbase_modelはKohaku XL beta5。 metadataはfair-ai-public-license-1.0-sd。派生モデルが追加条件を持つ場合は別途確認する。
- [NoobAI XL 1.1](https://huggingface.co/Laxhar/noobai-XL-1.1/blob/814a274af2b8097c0828819d561ec74c7d0c6cea/README.md): Illustrious系のアニメ画像モデル。直接のbase_modelはNoobAI XL1.0。 HFメタデータのFAIPL表記に加え、モデルカード本文にモデル・派生・生成物を含む商用禁止と共有条件を記載。本文の追加条件を見落とさない。

## 保留情報

DeepASMR（2026）は論文と音声デモを確認しましたが、対応する公式推論実装・重みは未特定です。実装公開済みとして推薦しないでください。詳細はreviewed-not-included.json。
