# 代謝経路モデル図（Metabolic Pathway Model）とAI解析フレーム（Analysis Framework） — HealthBook

> 本ドキュメントは、HealthBookで実行する「全代謝経路解析」と「フェノタイピング連携AI」のための設計図（図解＋実装フレーム）を示します。

---

## 1. 目的
- 腸内マイクロバイオームの機能（代謝経路）を可視化し、個別化介入（食材／MBTコンソーシアム／生活介入）の最適化を行う。
- 代謝経路レベルでの因果モデルを構築し、臨床アウトカム改善につなげるAIを実装する。

---

## 2. 図の構成（推奨レイアウト）
1. **レイヤー表示（左→右）**
   - 入力レイヤー：食事／農産物（AGRIX）／投薬・サプリ／MBT投与／環境データ
   - 微生物レイヤー：種・株プロファイル（メタゲノム）
   - 機能レイヤー：代謝経路（酢酸系、酪酸系、プロピオン酸系、胆汁酸代謝、TMA系など）
   - 代謝物レイヤー：糞便・血中メタボローム（SCFA, BAs, TMAO, 短鎖中間体）
   - 宿主フェノタイプ：臨床指標（体組成、HbA1c、インスリン感受性、炎症マーカー、腸粘膜指標）
   - 出力：診断スコア、推奨介入、予後シミュレーション

2. **ネットワーク表現（下段）**
   - ノード：菌株、酵素（EC番号）、代謝物、臨床指標
   - エッジ：反応（矢印）、代謝流（重み付き）、相互作用（競合/共生）

3. **タイムライン（右下）**
   - 介入前→介入直後→3ヶ月→6ヶ月 などの時系列変化を視覚化

---

## 3. 代謝経路モデル（設計詳細）
- **代謝経路データベース**：MetaCyc / KEGG / BiGG とメタゲノムアノテーション（HUMAnN, eggNOG）をマージ。
- **経路スコア**：各経路ごとに「潜在発現スコア（遺伝子存在）」「活動スコア（トランスクリプトーム/プロテオーム）」「代謝出力スコア（メタボローム）」を計算。
- **例：酢酸系スコア**
  - 遺伝子カバレッジ（acetyl-CoA系、Wood–Ljungdahl系など）
  - トランスクリプトレベルの活性度
  - 糞便／血中の酢酸濃度（補正済み）
  - 合成して総合スコアを出力（0–100）

---

## 4. AI解析フレーム（パイプライン）

### A. データパイプライン
1. **取り込み**：生データ（ショットガンFASTQ、メタトランスクリプトーム、LC-MSメタボローム、臨床CSV、食事ログJSON、AGRIX土壌/作物データ）
2. **前処理**：QC、アダプター除去、ノイズ除去、正規化、バッチ補正
3. **アノテーション**：MetaPhlAn/HUMAnN/DIAMOND→遺伝子/経路マッピング
4. **統合**：マルチオミクス統合フレーム（MOFA2, DIABLO, Deep learning-based fusion）

### B. モデル群（推奨）
1. **因果グラフィカルモデル**（Bayesian Network / Structural Causal Models）
   - 目的：介入効果の推定、反事実シミュレーション
2. **時系列予測モデル**（Transformer-based / RNN）
   - 目的：時系列での代謝物推移・定着予測
3. **表現学習**（Autoencoder / Variational Autoencoder）
   - 目的：個人の“マイクロバイオーム表現”作成（埋め込みベクトル）
4. **応答予測モデル**（XGBoost / LightGBM / Neural Nets）
   - 目的：誰がどの介入に反応するかの予測
5. **生成モデル（合成データ・介入シミュ）**（GAN / Diffusion）
   - 目的：稀なコホートのシミュレーション、ポリシー検証

### C. モデル出力（Clinical Decision Support）
- 酢酸系/酪酸系 等の経路スコア
- 「不足系統の可視化（欠損酵素）」
- 個別化介入案（食材＋MBTコンソーシアム＋行動）
- 期待される効果と不確実性（信頼区間）

---

## 5. データスキーマ（サマリ）
- **participant_id**
- sample_id, timepoint, collection_datetime
- sequencing_fastq_path, metabolomics_file_path
- diet_record (standardized food ontology), agrix_food_id
- clinical_metrics: BMI, HbA1c, CRP, CGM_series_link
- derived: taxonomic_profile (species/strain), pathway_coverage, pathway_activity, metabolite_concentrations

---

## 6. 可視化テンプレート
1. **フロー図**（左：入力→右：出力）— インタラクティブ（ノードクリックで詳細）
2. **ネットワークビュー**（Cytoscape/Graphistry 表示）— ノード色は機能スコア
3. **タイムラインプロット**（各代謝物の時系列）
4. **個別レポート**（PDF自動生成）— 介入提案＋エビデンスチャート

---

## 7. 実装ロードマップ（短期→中期→長期）
- **短期（0–3ヶ月）**：データ棚卸・パイプライン構築（QC→アノテーション→代謝経路マッピング）、酢酸系プロトタイプスコアの作成
- **中期（3–12ヶ月）**：観察コホート解析、小規模介入パイロット、AIモデルの初期学習
- **長期（12–36ヶ月）**：RCT、製剤化パイプライン、Clinical Decision Support の導入

---

## 8. 評価指標（KPI）
- モデル性能：AUC（応答予測）、RMSE（代謝物量予測）
- 臨床：HbA1c差分、体脂肪率、炎症マーカー
- 生物学：経路スコアの再現性、菌株定着率

---

## 9. 負荷・倫理・規制
- 生菌投与やFMT関連の規制遵守、ドナー/製剤スクリーニング、データプライバシー（個人同定防止）

---

## 10. 参考ツール / ライブラリ（実装推奨）
- シーケンス解析：FastQC, Trimmomatic, MetaPhlAn, HUMAnN
- 統合解析：MOFA2, DIABLO (mixOmics), scikit-learn, PyTorch
- 因果推論：DoWhy, CausalNex
- 可視化：Cytoscape, Dash, Plotly

---

### 最後に（アクション提案）
1. 本ドキュメントを基に「図（SVG或いはPNG）」を作成します（ネットワーク図 + レイヤーフロー）。
2. AI解析フレームのコード骨子（Jupyter notebook）を作ります。

どちらを先に作成しましょうか？

