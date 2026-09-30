# Awesome Anime AI Characters

アニメ・二次元系の**会話できるAIキャラクター**を作る／動かすためのGitHubリポジトリ集。Live2DやVRMの姿を持つデスクトップ伴侶・AI VTuberを中心に、キャラクター対話、人格・会話記憶の制作、アバター実装に直接役立つものを分類して掲載しています。

- [Live2D・2Dキャラクターとの対話](#live2d2dキャラクターとの対話)
- [AI VTuber・配信](#ai-vtuber配信)
- [VRM・3Dキャラクターとの対話](#vrm3dキャラクターとの対話)
- [キャラクター会話・ロールプレイ](#キャラクター会話ロールプレイ)
- [人格・キャラカード・会話記憶の制作](#人格キャラカード会話記憶の制作)
- [アバター表示・アニメーション部品](#アバター表示アニメーション部品)
- [探し方・掲載基準](#探し方掲載基準)

> **注意**: リンク先のコード・モデル・音声・キャラクター素材の権利はそれぞれ別です。掲載は動作・安全性・商用利用の保証ではありません。導入前に各リポジトリのライセンス、同梱素材と外部APIの利用条件を確認してください。版権キャラのモデル・声の再利用や、実在人物の発言・私的な記録を用いた人格作成には権利と同意の確認が必要です。

### 目的から選ぶ

| 目的 | まず見る | 導入前に確認すること |
| --- | --- | --- |
| 自分のLive2Dキャラと音声会話 | [Warashi](https://github.com/inni918/warashi)、[Komorebi](https://github.com/kiskaserver/interactive_assistent) | LLM接続、モデル素材・Cubism Coreの入手条件。Warashiは既存実装の派生版。 |
| 配信コメントにキャラが応答 | [AkaneDen](https://github.com/nadezhdkov/AkaneDen)（Twitch）、[LiveVTuber Stage](https://github.com/KKLL2025/AILiveVTuber-Stage)（Bilibili） | 対象サービスの認証、音声API、VTube StudioまたはLive2Dモデル。 |
| VRMで会話・デスクトップ常駐 | [Aikeya](https://github.com/aikeyaorg/aikeya)、[AniCompanion](https://github.com/catsmice/AniCompanion) | 前者はWebとmacOSベータ、後者はmacOS 15以降で外部エージェントが必要。 |
| テキストでキャラ設定・物語を試す | [SillyTavern](https://github.com/SillyTavern/SillyTavern)、[Serene Pub](https://github.com/doolijb/serene-pub) | LLM接続が必要。後者は複数人セッションとキャラ別の情報管理が特徴。 |
| 発言資料から人格を整理する | [Distilly](https://github.com/titanwings/distilly)、[CharGen](https://github.com/Karmacoke/chargen) | 前者は資料由来のAgent Skill、後者は創作キャラの設定・プロンプト生成。どちらもアバターアプリではない。 |

## Live2D・2Dキャラクターとの対話

- [Project AIRI](https://github.com/moeru-ai/airi) — Live2D/VRMを表示し、音声で会話できるAIキャラクタープロジェクト。Webとデスクトップ向けで、ゲーム連携も扱う。
- [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) — Live2DアバターとLLM・音声認識・音声合成をつなぐ会話アプリ。Web/デスクトップ、ローカルモデル構成やデスクトップペット表示に対応。
- [Soul of Waifu](https://github.com/jofizcd/Soul-of-Waifu) — Live2D/VRMのキャラクターとテキスト・音声で交流するWindows向けアプリ。キャラクター記憶とRPGモードも備える。
- [ChatWaifu Mobile](https://github.com/Voine/ChatWaifu_Mobile) — Android向けの二次元キャラクター会話アプリ。Live2D表示、端末上のVITS音声合成とSherpa音声認識を組み合わせる。付属モデルの商用利用は禁止と明記されている。
- [my-neuro](https://github.com/morettt/my-neuro) — 交換可能なLive2Dモデル、音声・性格を持つAIデスクトップ伴侶の制作ワークベンチ。ローカルLLM、音声会話、配信連携を扱う。
- [Persona Engine](https://github.com/elevenyellow/handcrafted-persona-engine) — マイク入力→LLM→TTS→Live2Dの発話・表情同期を統合。透明デスクトップオーバーレイとOBS向け出力があり、Windows x64とNVIDIA CUDAが必要。
- [Project N.E.K.O.](https://github.com/Project-N-E-K-O/N.E.K.O) — Live2D/VRM/MMDなどのキャラ表示にテキスト・音声・画像入力、持続記憶とエージェント機能を組み合わせる。機能ごとの環境・モデル対応は異なる。
- [EchoBot](https://github.com/KdaiP/EchoBot) — Live2DキャラとのWeb音声対話と、別系統で動くファイル操作などのエージェントを統合。QQ/Telegramにも接続できる。
- [Miru](https://github.com/kiyotakali/Miru) — Live2Dデスクトップペット。許可した画面情報、日誌・長期記憶を使って自発的に話しかける。会話用モデルAPIは利用者が設定する。
- [Waifu Companion](https://github.com/waifuai/waifu-companion) — ブラウザ上でLive2Dキャラを切り替え、人格設定・表情・会話要約と音声入出力を使える。LLMとの通常会話には外部API設定が必要。
- [小凡AI (virtual-person)](https://github.com/ptghb/virtual-person) — Live2Dの表情・動作とLLM対話、TTS、長期記憶を統合。カメラによる手ぶり・視線連動やデスクトップ表示にも対応。
- [Warashi](https://github.com/inni918/warashi) — Open-LLM-VTuber派生のmacOS/Windows向けLive2D伴侶。キャラ別の永続記憶、自発会話、音声割り込みと就寝モードを追加。LLMは利用者が用意し、**同梱フロントエンドと試供モデルの利用条件はコードと別**。
- [Iris](https://github.com/yingwang/iris) — Live2Dの顔追跡と音声割り込み、自発発話を組み合わせたブラウザ伴侶。Claude CLIの認証が必要で、音声合成にはオンラインサービスを使う。
- [Komorebi](https://github.com/kiskaserver/interactive_assistent) — Live2Dのデスクトップ秘書。ローカルのllama.cpp／Whisper.cpp／Piperまたは外部モデルを接続し、許可した画面の参照や会話検索を行う。Cubism Coreとモデルは別途用意。
- [Live2D-LLM-Chat](https://github.com/suzuran0y/Live2D-LLM-Chat) — SenseVoice/FunASRの音声認識、LM Studio等のLLM、CosyVoice合成とLive2Dの口パクをつなぐ対話実装。各音声モデルとLive2Dモデルを別途準備。
- [Anime Companion for VS Code](https://github.com/xShiroeNguyenx/anime-companion-vscode) — VS Code内のLive2Dキャラがコード文脈を踏まえて会話し、エラーやコミットにも反応する試験的拡張。デスクトップに浮かせる機能はWindows限定。
- [Gemma Live2D Assistant](https://github.com/Daniel3282/gemma-live2d-assistant) — Gemmaのオンデバイス音声・画面認識とLive2Dの口パクを組み合わせた実験的なデスクトップ伴侶。モデルの初回取得が必要で、**同梱Live2D素材は非商用条件**。
- [Live2D AI chat](https://github.com/zoollcar/live2d-AI-chat) — ブラウザ内のGGUFモデル、または権限を分けたブラウザ拡張経由の外部モデルでLive2Dと会話。音声・画像やWebページの入力にも対応し、付属素材の利用条件に注意。
- [ai-secretary](https://github.com/ryuno016/ai-secretary) — OpenAI・Whisper・VOICEVOXで話すLive2Dデスクトップ秘書。タスクの登録・確認もできる。**Live2DモデルとCubism Coreは同梱されず**、別途入手が必要。

## AI VTuber・配信

- [Luna AI (AI-Vtuber)](https://github.com/Ikaros-521/AI-Vtuber) — LLM・TTSとLive2Dなどのアバターを接続し、配信コメントへの応答やローカル会話を行う。READMEには商用時の別条件が記載されている。
- [Super Agent Party](https://github.com/heshengtao/super-agent-party) — VRMデスクトップ伴侶、Live2D拡張・VTube Studio連携、キャラクターカードでの複数人会話や配信ボットを備える。
- [z-waif](https://github.com/SugarcaneDefender/z-waif) — ローカルLLMやWhisper/RVCとVTube Studioを連携させるAIキャラ環境。音声会話、ロアブック、過去会話検索を備える。外部ソフトの準備が必要。
- [ChatVRM (Restream連携版)](https://github.com/zoan37/ChatVRM) — pixiv版ChatVRMから派生したVRM会話デモ。Restream経由でX/Twitchの配信コメントを取り込み、OpenRouterとElevenLabsで応答する。配信には各サービスの設定が必要。
- [Yuna AI](https://github.com/MasHasNoLife/yuna-ai) — OllamaとKokoroの音声をVTube StudioのLive2Dへ送り、表情・口パクを動かすローカルAI VTuber。**配信コメント取得は構想段階**で、VTube Studioやモデルを別途用意する。
- [AITuber OnAir](https://github.com/shinshin86/aituber-onair) — Live2D・PNG・Inochi2D・PSD・VRMなどの会話アバター実装例を備えるTypeScript製AI VTuberキット。Live2Dモデル素材とLLM/TTSの設定が必要。
- [AkaneDen](https://github.com/nadezhdkov/AkaneDen) — Twitchコメントやマイク入力にLLMと音声合成で応答し、VTube StudioのLive2D表情・口パクを動かす。Twitch認証とVTube Studio APIの設定が必要。
- [AI-VTUBER-Twitch-Chat-Bot](https://github.com/gaetan-warin/AI-VTUBER-Twitch-Chat-Bot) — Twitchの`!ai`コメントをOllama/Geminiへ送り、ブラウザ音声とLive2Dで返す。**Cubism 2形式のモデル限定**で、Twitch OAuthが必要。
- [LiveVTuber Stage](https://github.com/KKLL2025/AILiveVTuber-Stage) — Bilibiliのコメント・ギフト等を優先キューで処理し、DeepSeek応答をMiMo音声・Live2D表情・字幕に反映。**UIは中国語のみ**。Cubism Coreと使用権のあるモデルは別途準備。
- [ai-streamer](https://github.com/motemen/ai-streamer) — OpenAI・VOICEVOXによる台詞と字幕・表情付きの**静止画2Dアバター**をOBSに表示する。ディレクター入力や自発発話に対応するが、配信コメントの自動収集は記載されていない。

## VRM・3Dキャラクターとの対話

2DのLive2Dとは異なる3Dアバターですが、アニメ調キャラクターの対話実装に役立つため分けて掲載します。

- [ChatdollKit](https://github.com/uezo/ChatdollKit) — Unity/VRMで音声対話できるキャラクターを組み立てるSDK。LLM、音声入出力、表情・モーション・リップシンクを統合。
- [ChatVRM](https://github.com/pixiv/ChatVRM) — ブラウザでVRMキャラクターと音声会話するデモ。音声認識、ChatGPT API、音声合成を利用。**2024年にアーカイブ済み**。
- [LocalChatVRM](https://github.com/pixiv/local-chat-vrm) — ChromeのBuilt-in AIとKokoro.jsでブラウザ内のVRM会話を試す技術デモ。**アーカイブ済み**で、対応するChrome環境が必要。
- [Utsuwa](https://github.com/JuiceBoxxGames/utsuwa) — VRMアバターとの会話に音声、意味検索できる記憶、気分・関係性の変化を組み合わせたブラウザ／デスクトップ伴侶。デスクトップ版はベータ。
- [ChatVRM Agent](https://github.com/badhope/ChatVRM-Agent) — VRMをブラウザに読み込み、マイク入力→LLM→TTSの会話を表情・口パクとともに表示。音声入力はWeb Speech API対応ブラウザに依存。
- [Lobe Vidol](https://github.com/lobehub/lobe-vidol) — VRMキャラの編集・会話、音声入出力、MMDダンスを統合するWeb/PWA。開発中のベータ版。
- [Amica](https://github.com/semperai/amica) — pixiv版ChatVRMから発展したVRM会話アプリ。音声・画像入力、表情表現に対応し、ローカル／クラウドのAIを選べる。
- [Aikeya](https://github.com/aikeyaorg/aikeya) — VRMキャラとの音声・テキスト対話に、関係性の変化と端末内の意味検索記憶を組み合わせる。Web版とmacOSデスクトップ版ベータ。**Live2D対応は未実装**。
- [AniCompanion](https://github.com/catsmice/AniCompanion) — macOS 15以降のVRMデスクトップペット。音声・口パク・表情と、Claude Code／Codexなど利用者側のエージェントを接続する。初回の表示にはネット接続が必要。
- [Companion Space](https://github.com/Johnson-Durui/Companion-Space) — VRM／2D表示を持つローカル優先の学習伴侶。資料を引用する検索付き対話、リアルタイム音声、確認後の記憶保存を扱う。主要な利用経路はデスクトップブラウザ＋ローカル環境。
- [Claw Sama](https://github.com/luckybugqqq/claw-sama) — OpenClawプラグインとして動くmacOS/Windows向けVRMデスクトップペット。音声会話、表情・口パク、人格設定と任意の画面観察を備える。
- [Scowld](https://github.com/apoorvdarshan/scowld) — iOS 17以降のVRM音声伴侶。Amica由来のキャラ表示に、持ち込みAPIキーによる対話・音声入出力と端末内の会話履歴を組み合わせる。
- [xiaoke.ai (小可爱)](https://github.com/liupig/xiaokeai) — Windows向けローカル3D伴侶。VRM/PMX/GLBのキャラと音声対話し、表情・動作・カメラ演出や記憶を扱う。**同梱されないモデル・音声などの素材はコードと利用条件が別**。
- [Yorishiro](https://github.com/sktkkoo/Yorishiro) — macOSのClaude Code／Codex用ターミナルにVRMキャラを同居させる。テキスト・音声対話、表情反応、人格・シーンを変更するパックに対応。

## キャラクター会話・ロールプレイ

アバターがなくても、人格・設定や物語を伴うキャラクター対話を作れる環境です。音声だけの会話実装も含みます。

- [SillyTavern](https://github.com/SillyTavern/SillyTavern) — キャラクターの説明・人格・シナリオや会話例を定義してLLMと対話するフロントエンド。単体でLive2D/VRMを表示するアプリではない。
- [Irori](https://github.com/hikariming/irori) — アニメ調キャラクターカードの人格・記憶を持つデスクトップ作業パートナー。文章作成やコーディングに対応。**音声とLive2Dはロードマップ段階**。
- [Serene Pub](https://github.com/doolijb/serene-pub) — キャラカード、複数人会話、lorebookと長期記憶を扱うセルフホストのテキストRPアプリ。人物ごとの情報可視性と共同セッションに対応。ベータ版。
- [CardGenV2](https://github.com/zebede1980/CardGenV2) — SillyTavern互換のキャラカードを生成・編集してPNG/JSONで出力する環境。複数キャラのテキストRP会話と会話要約・記憶も試せる。LLM接続が必要。
- [Corvus Story Core](https://github.com/JustLateNightAI/Corvus-Story-Core) — テキストRPG向けのGM/NPC会話エンジン。NPCカード、個別記憶、章要約と関係値などの状態を保持する。会話用LLMは別途用意。
- [Project Riko](https://github.com/rayenfeng/riko_project) — アニメ風の人格設定、対話履歴、Faster-WhisperとGPT-SoVITSを組み合わせた音声会話スクリプト。**GUIとVRM表示は未実装**で、外部の音声合成サービスを起動する。

## 人格・キャラカード・会話記憶の制作

**以下は単体でLive2D/VRMキャラと会話するアプリではありません。** 人物資料から人格を整理し、会話用のカードを作り、既存の対話環境に記憶を足すためのツールです。

- [Distilly](https://github.com/titanwings/distilly) — 発言・文書・面談記録・公開資料から、同僚／身近な人／著名人・架空人物の言動や判断の特徴をPerson Profileに整理し、外部エージェント向けSkillとして出力する。**本人の再現を保証せず、独立したアバター／チャットアプリではない**。
- [CharGen](https://github.com/Karmacoke/chargen) — キーワードや世界設定からキャラの心理・経歴・容姿を設計し、別のLLM会話で使えるNPCシステムプロンプトを生成。日本語UIに対応。
- [SillyTavern CharCardStudio](https://github.com/MMKAVERAPPA/SillyTavern-CharCardStudio) — SillyTavern内で人物像・設定資料を草稿化して確認・適用する拡張。SillyTavern本体と設定済みLLMが必要。
- [CharMemory](https://github.com/bal-spec/sillytavern-character-memory) — SillyTavernのキャラ別会話から重要事項を抽出して編集可能な記憶にし、後の会話で検索する拡張。想起にはVector Storageの有効化が必要。
- [AutoMemory for SillyTavern](https://github.com/chuyaowang/sillytavern-auto-memory) — 関係・利用者・世界設定の3層に記憶を分けて保存・検索するセルフホスト拡張。**標準の埋め込みモデルは英語向け**で、日本語には変更が必要。
- [character-card](https://github.com/roleplay-studio/character-card) — SillyTavern形式のPNG/JSONキャラカードを読み書きするPythonライブラリ。人格生成や会話は行わない。

## アバター表示・アニメーション部品

**以下はAI会話アプリではありません。** 上のプロジェクトと組み合わせてアニメ調キャラクターの表示・動きを実装するための部品です。

- [pixi-live2d-display](https://github.com/guansss/pixi-live2d-display) — PixiJS v6からLive2Dモデルを表示・操作するライブラリ。Cubism Coreは別途必要。
- [live2d-widget](https://github.com/stevenjoezhang/live2d-widget) — WebページにLive2D看板娘を表示するウィジェット。モデルは同梱されない。
- [Inochi2D](https://github.com/Inochi2D/inochi2d) — レイヤー分割した2Dイラストをリアルタイムで変形するパペットのSDK・仕様。Live2Dとは別方式。
- [Talking Head Anime 2 Demo](https://github.com/pkhungurn/talking-head-anime-2-demo) — 1枚のアニメキャラ画像から表情・顔向きを操作する研究デモ。音声対話機能はない。
- [AVATAR](https://github.com/ARPAHLS/avatar) — WindowsのVRMデスクトップオーバーレイ。音声に合わせた口パクとVRMA動作、外部エージェント向けMCP操作を備える。**単体のAI会話機能はない**。

## 探し方・掲載基準

調査の入口: [live2d](https://github.com/topics/live2d) · [vtuber](https://github.com/topics/vtuber) · [anime](https://github.com/topics/anime) · [waifu](https://github.com/topics/waifu) · [virtualassistant](https://github.com/topics/virtualassistant) · [ai-companion](https://github.com/topics/ai-companion) · [chatbot](https://github.com/topics/chatbot) · [digital-human](https://github.com/topics/digital-human) のトピック、GitHubの関連語検索、[awesome-ai-vtubers](https://github.com/proj-airi/awesome-ai-vtubers) と [awesome-ai-companion](https://github.com/DasterProkio/awesome-ai-companion)。候補リストやトピックの掲載だけで採用せず、各プロジェクトのREADME・関連ドキュメントで機能と未実装部分を確認しています（2026-09-23）。

- 対象: アニメ調のキャラクターとAIで会話できるアプリ、AI VTuber実装、キャラクター対話環境、およびそれらに直接使う人格・キャラカード・記憶・アバターの部品。単体で会話できないものは専用の節に明示。
- 対象外: 一般的なチャットボット、アニメ作品データベース、画像生成だけのツール、写実的な人物動画専用のデジタルヒューマン。AI非搭載の部品は専用の節に明示。
- 同じプロジェクトは複数トピックにあっても一度だけ掲載。派生版は元との違いが明確な場合に限り区別する。機能は上流の記述に沿った要約であり、ベンチマークや動作検証の結果ではありません。

追加・修正はIssueまたはPull Requestへ。候補のURL、どんなキャラクター対話／アバター機能があるかを示すREADME等の根拠、利用条件の注意点を添えてください。
