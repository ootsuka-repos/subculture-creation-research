# 動かせる3Dアセット（2件）

[研究一覧の索引](../papers.md) · [機械可読データ](../papers.json)

公式コードと本研究の学習済み重みの両方が公開されている研究。公開は利用条件・商用利用可・動作確認を意味しない。各項目のコミット、モデルのrevision・確認ファイル、根拠URLは papers.json / papers.jsonl。

| 論文 | 会議 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- | --- |
| [PAct: Part-Decomposed Single-View Articulated Object Generation](https://arxiv.org/abs/2602.14965) | SIGGRAPH Asia 2026<br>採択告知あり・開催前（著者README） | 1枚の画像から、部品と関節を持つ3D物体を生成する。扉・家具などの可動小物を、動かせるアセットへ変換する用途。 | [Mobiuslqm/PAct](https://github.com/Mobiuslqm/PAct) · [条件](https://github.com/Mobiuslqm/PAct/blob/1f6fb8a983ad198daf62ebbc6771cc6d784330cb/LICENSE) | [HF](https://huggingface.co/PAct000/PAct) | パーツ構造・関節推定等の5モデルと推論・学習コード。 重みはCC BY-NC-SA 4.0。著者READMEの採択告知に基づく掲載で、SIGGRAPH Asia 2026は開催前。 |
| [Puppeteer: Rig and Animate Your 3D Models](https://arxiv.org/abs/2508.10898)<br>[制作カタログ](../../categories/3d.md#puppeteer) | NeurIPS 2025<br>NeurIPS 2025 Spotlight | 静的な3Dメッシュに骨格とスキニングを付ける。さらに参照動画を使って動きを最適化し、モデルをアニメーション化する。 | [Seed3D/Puppeteer](https://github.com/Seed3D/Puppeteer) · [条件](https://github.com/Seed3D/Puppeteer/blob/1c0f9fc6ad209667a0ec5ceac9b59964938a8b51/LICENSE) | [HF](https://huggingface.co/Seed3D/Puppeteer) | 公開重みは骨格生成・スキニング用。動画からの動作付けは最適化処理。 NeurIPS 2026は確認日時点で採択通知前のため、2025年を採用。 |
