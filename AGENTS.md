# このリポジトリで作業するモデルへ

調査を継続する場合はCONTRIBUTING.mdとRESEARCH_NOTES.mdを先に読む。ユーザーの最新の指示を優先し、既存の15カテゴリを対象範囲の上限としない。

正本はcatalog.json。生成ファイルはscripts/export.pyで同期する。事実・作者の説明・編集者の評価・実行検証を区別し、出典・確認日・未確認事項を保持する。変更後はexport.py --check、validate.py、git diff --checkを行う。

モデルへのコンテキストとして読むだけならMODEL_CONTEXT.mdから始め、必要な分野をcategories/またはcatalog.jsonlから取得する。

GitHub以外のアニメ画像モデルの正本はmodel-catalog.json。分野横断の比較はresearch/deep-dive-2026-09-09.md。deep_diveの次の検証項目は未実施の提案であり、合格記録ではない。モデルカード本文の追加条件とメタデータを区別する。
