# 光学・レンダリング・VFX（4件）

[研究一覧の索引](../papers.md) · [機械可読データ](../papers.json)

公式コードと本研究の学習済み重みの両方が公開されている研究。公開は利用条件・商用利用可・動作確認を意味しない。各項目のコミット、モデルのrevision・確認ファイル、根拠URLは papers.json / papers.jsonl。

| 論文 | 会議 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- | --- |
| [8DNA: 8D Neural Asset Light Transport by Distribution Learning](https://doi.org/10.1145/3799902.3811094) | SIGGRAPH 2026 | 3Dアセット内部の光の伝わり方を学習済みモデルで表し、複雑な光輸送の描画に利用する。 | [lwwu2/8dna26](https://github.com/lwwu2/8dna26) · 条件は各リポジトリ参照 | [配布先](https://drive.google.com/file/d/1WeYpquFoDTZzbwpHotiwIRwKdBskULcY/view) | アセット別の学習済みlight-transportモデル。 |
| [Guidestar-Free Adaptive Optics with Asymmetric Apertures](https://doi.org/10.1145/3809501) | SIGGRAPH 2026 | 非対称な開口と学習モデルを使い、基準となる光点なしで光学収差を推定・補正する。撮像装置寄りの研究。 | [WeiyunJiang/guidestar-free-ao](https://github.com/WeiyunJiang/guidestar-free-ao) · [条件](https://github.com/WeiyunJiang/guidestar-free-ao/blob/main/LICENSE) | [配布先](https://drive.google.com/file/d/1e2GxutCBGbDSLIHtMcvRMSlsKAqJVtYH/view) | Places2で学習したモデル群。 |
| [Neural Quadrature Rule and Autoregressive Adaptive Sampling](https://doi.org/10.1145/3811318) | SIGGRAPH 2026 | 数値積分の評価点や重みを学習し、照明・透過率などの計算を効率化する。レンダラー開発の基盤技術。 | [SuikaSibyl/nqr](https://github.com/SuikaSibyl/nqr) · 条件は各リポジトリ参照 | [配布先](https://drive.google.com/file/d/1gydL15reAH7DDNNiieg5VnS8oe0HqGDT/view) | 配布アーカイブにscenesとckpt。 |
| [VfxDB: A Visual Effects Volume Dataset and Benchmark for VDB-Native Generative Modeling](https://doi.org/10.1145/3799902.3811178)<br>[制作カタログ](../../categories/vfx.md#vfxdb) | SIGGRAPH 2026 | 煙などのVFXボリュームを扱うデータセットと生成モデル。VDB形式を意識した立体エフェクト素材の生成向け。 | [VfxDB-Official/VfxDB](https://github.com/VfxDB-Official/VfxDB) · 条件は各リポジトリ参照 | [HF](https://huggingface.co/ryogishiki/VfxDB-models) | 論文用EMAチェックポイントを配布。 |
