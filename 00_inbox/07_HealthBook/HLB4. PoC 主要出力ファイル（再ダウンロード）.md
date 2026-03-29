2) 主要ファイル（ダウンロード）
PoC スコア（サンプル患者）:
Download CSV — PoC scores (binary mapping)
変換済みの重み行列（●→1 / 空白→0）:
Download CSV — weight_matrix_binary_from_marks.csv
サンプル回答（JSON）:
Download JSON — sample_answers.json
元ファイルの中間変換（視認用）:
Download CSV — weight_matrix_parsed.csv

--------

（今回生成した PoC の出力ファイル）
/mnt/data/healthbook_poc/poc_scores_sample_patient_binary.csv — PoC のスコア結果（サンプル患者）。ダウンロードはこちら
/mnt/data/healthbook_poc/weight_matrix_binary_from_marks.csv — 「●」→1 の重み行列（CSV）。ダウンロードはこちら
/mnt/data/healthbook_poc/sample_answers.json — PoC で使ったサンプル回答。ダウンロードはこちら

これらのファイルを再度ダウンロードさせてください。

---

了解しました。以下に **今回生成した PoC 出力ファイルのダウンロードリンクをすべて再掲**します。

---

## PoC 主要出力ファイル（再ダウンロード）

### ① PoC スコア結果（サンプル患者）

**poc_scores_sample_patient_binary.csv**
（137 疾病 × サンプル回答によるリスクスコア）

[ダウンロードはこちら](sandbox:/mnt/data/healthbook_poc/poc_scores_sample_patient_binary.csv)

---

### ② 変換済み重み行列（● → 1 / 空白 → 0）

**weight_matrix_binary_from_marks.csv**
（疾病 × 食生活・生活習慣項目）

[ダウンロードはこちら](sandbox:/mnt/data/healthbook_poc/weight_matrix_binary_from_marks.csv)

---

### ③ サンプル回答（JSON）

**sample_answers.json**
（PoC 実行時に使用した仮想患者の回答データ）

[ダウンロードはこちら](sandbox:/mnt/data/healthbook_poc/sample_answers.json)

---

### ④ 元Excelの中間変換ファイル（視認・検証用）

**weight_matrix_parsed.csv**
（Excel 構造を保持したままCSV化したもの）

[ダウンロードはこちら](sandbox:/mnt/data/healthbook_poc/weight_matrix_parsed.csv)

---

これらはすべて **同一の PoC 実行結果から生成された正式な中間成果物**です。
次の段階（重みの精緻化、＋／−評価、問診ID付与、Azure実装向け構造化）へそのまま接続できます。
