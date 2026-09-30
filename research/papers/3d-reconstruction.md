# 3D復元・理解（7件）

[研究一覧の索引](../papers.md) · [機械可読データ](../papers.json)

公式コードと本研究の学習済み重みの両方が公開されている研究。公開は利用条件・商用利用可・動作確認を意味しない。各項目のコミット、モデルのrevision・確認ファイル、根拠URLは papers.json / papers.jsonl。

| 論文 | 会議 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |
| --- | --- | --- | --- | --- | --- |
| [ArtiFixer: Enhancing and Extending 3D Reconstruction with Auto-Regressive Diffusion Models](https://doi.org/10.1145/3799902.3811060) | SIGGRAPH 2026 | 3D復元結果のレンダリングに生じる欠損や破綻を動画拡散モデルで補い、復元の改善や視点範囲の拡張を行う。 | [nv-tlabs/ArtiFixer](https://github.com/nv-tlabs/ArtiFixer) · [条件](https://github.com/nv-tlabs/ArtiFixer/blob/main/LICENSE) | [HF](https://huggingface.co/nvidia/ArtiFixer) | 1.3B・14B。Wanベースモデルが別途必要。 |
| [GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction](https://doi.org/10.1145/3799902.3811222) | SIGGRAPH 2026 | 少数視点から復元した3Dシーンの新視点画像を、参照画像と幾何対応を使って修復する。 | [Xiaoc7/GeoQuery](https://github.com/Xiaoc7/GeoQuery) · [条件](https://github.com/Xiaoc7/GeoQuery/blob/main/LICENSE) | [HF](https://huggingface.co/DIG-UESTC/GeoQuery) | 拡散refinerの重み。 |
| [MegaNorm: Local Patch Embeddings for Efficient and Robust Point Normal Orientation at Super-Large Scale](https://doi.org/10.1145/3799902.3811139) | SIGGRAPH 2026 | 大規模な点群で表面の向きを局所・全体の両方からそろえる。スキャン形状のメッシュ化などの前処理向け。 | [zd-lee/MegaNorm](https://github.com/zd-lee/MegaNorm) · 条件は各リポジトリ参照 | [HF](https://huggingface.co/wlbbbbb/meganorm) | patchnet等の重み。 |
| [Mix3R: Mixing Feed-forward Reconstruction and Generative 3D Priors for Joint Multi-view Aligned 3D Reconstruction and Pose Estimation](https://doi.org/10.1145/3799902.3811152) | SIGGRAPH 2026 | 複数画像から、生成モデルの形状知識を利用して3D形状とカメラ姿勢を同時に推定する。 | [jsnln/mix3r](https://github.com/jsnln/mix3r) · 条件は各リポジトリ参照 | [ModelScope](https://modelscope.cn/models/jsnln00/mix3r) | V1が論文版、V2が会議後の更新版。 |
| [MTPano: Multi-Task Panoramic Scene Understanding via Label-Free Integration of Dense Prediction Priors](https://doi.org/10.1145/3799902.3811193) | SIGGRAPH 2026 | 360度パノラマ画像から、物体・領域の分類、奥行き、表面の向きをまとめて推定する。 | [Evergreen0929/MTPano](https://github.com/Evergreen0929/MTPano) · 条件は各リポジトリ参照 | [HF](https://huggingface.co/jdzhang0929/MTPano) | 140k・408kチェックポイント。 |
| [PointLLM-R: Enhancing 3D Point Cloud Reasoning via Chain-of-Thought](https://doi.org/10.1145/3799902.3811081) | SIGGRAPH 2026 | 3D点群について自然言語で質問し、形状・用途などの説明や分類を得る。3D素材の理解・整理向け。 | [Xqle/PointLLM-R](https://github.com/Xqle/PointLLM-R) · [条件](https://github.com/Xqle/PointLLM-R/blob/master/LICENSE) | [HF](https://huggingface.co/QileXu/PointLLM-R-7B) | 7Bモデル。 |
| [TrajVG: 3D Trajectory-Coupled Visual Geometry Learning](https://doi.org/10.1145/3799902.3811184) | SIGGRAPH 2026 | 動画から点の3D軌跡、フレームごとの形状、カメラ姿勢を整合するように推定する。動的シーンの解析向け。 | [xingy038/TrajVG](https://github.com/xingy038/TrajVG) · [条件](https://github.com/xingy038/TrajVG/blob/main/LICENSE) | [配布先](https://drive.google.com/file/d/1vk27rkLPJrYVUgD7tCFw2ti5NQLYk2PK/view) | 3D軌跡と幾何復元の学習済みモデル。 |
