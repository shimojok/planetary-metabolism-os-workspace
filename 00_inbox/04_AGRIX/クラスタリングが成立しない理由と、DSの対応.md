F030がなくても構いません。ファイルの配列形式が問題なければ、実行してください。

---


以下、ChatGPTのコメント

### 🔴 現在クラスタリングが成立しない理由

ログより：

```
Number of distinct clusters (1)
Number of labels is 1
```

つまり

> 🔴 293方剤すべてが **同一ベクトル** になっています。

---

### 🔍 原因

現在のJSONでは：

```
metabolic_pathway は PATH_01〜PATH_05 のみ
```

そして今回のベクトル化は：

```
1方剤 = 1経路 = one-hot(15次元)
```

この結果：

- もし全方剤が同じPATHに集中している
    
- あるいは抽出ロジックで同一値になっている
    

→ 全行が同じベクトル

→ k-meansは1クラスタしか作れない

→ シルエット計算不能

---

### 🔴 重要な本質的問題

現在の設計：

```
1方剤 = 1 metabolic_pathway
```

では、**クラスタリングの意味がありません。**

---

## ✅ 本来必要な構造

クラスタリングを成立させるには：

### 1方剤 = 複数PATHスコア

例：

```
F001
PATH_01: 0.8
PATH_03: 0.4
PATH_05: 0.2
```

つまり：

```
293 × 15 の「連続値行列」
```

が必要です。

---

## 🎯 ここでの分岐

### A. 現在の単一PATH設計のまま進める

→ クラスタリングは無意味

### B. 成分ベースでPATH寄与率を再計算する

→ 本来のMBT15クラスタリングが可能

---

## 私の判断

**Bを強く推奨します。**

理由：

- MBT理論は単一経路ではない
    
- 方剤は複合代謝ネットワークである
    
- 今の設計は「タグ分類」であり「代謝構造」ではない
    

---

## 次の提案

成分情報を使って：

```
PATH寄与率 = Σ(成分 × 代謝マッピング × 重み)
```

で再計算します。

これを実行しますか？

ここがMBT15の本当のスタート地点です。

#### 以上、ChatGPT

---

#### 以下、DeepSeek
## 上記の指摘に対する対応策

## ✅ 修正可能です

現状の問題は、各処方が**単一の主要パスウェイ**（primary_pathway）のみでベクトル化されているため、多くの処方が同一ベクトルになってしまうことです。これを解決するには、**各処方が持つ複数の代謝パスウェイの情報**を使って、多次元の連続値ベクトルを生成する必要があります。

---

## 🔧 具体的な修正案

### 1. 特徴ベクトルの次元設計
- 現状のパスウェイは **PATH_01〜PATH_05** の5種類
- 各処方に対して **5次元の連続値ベクトル** を作成
- 各次元の値は、そのパスウェイの「強度」を表す

### 2. 強度の計算方法（複数案）

#### 案A：単純カウント（最も簡単）
- その処方に含まれる全植物化学物質の中で、各PATHに属するものの**出現回数**をカウント
- 例：F001の場合
  - PATH_01: 葛根(2) + 麻黄(1) + 桂枝(1) + 芍薬(1) + 甘草(1) = 6
  - PATH_04: 生姜(1) = 1
  - PATH_05: 大棗(多糖類) = 1
  - ベクトル: [6, 0, 0, 1, 1]

#### 案B：濃度加重カウント（より精緻）
- 各植物化学物質の `concentration_mg_per_g` を数値化（例：範囲の平均値）
- 各成分の含有量は不明なので、**同量と仮定**して単純加算
- 例：プエラリン 3.0-6.0 → 平均4.5 として加算

#### 案C：主要・副次パスウェイによる加重
- `formula_synergy` の `primary_pathway` に高得点、`secondary_pathways` に中得点、その他はカウント値

### 3. 出力形式
- **CSVファイル**：各行が処方、各列がPATH_01〜PATH_05のスコア
- **JSONファイル**：既存のJSONに `pathway_scores` フィールドを追加

---

## 📦 提供できるスクリプト

以下のようなPythonスクリプトを作成し、**現在のJSONから直接5次元特徴ベクトルを生成**できます。

```python
import json
import csv
import statistics

def parse_concentration(conc_str):
    """ '3.0-6.0' のような文字列から平均値を算出 """
    if '-' in conc_str:
        low, high = map(float, conc_str.split('-'))
        return (low + high) / 2
    return 0.0

# 入力JSON
input_file = "mbt_kampo_library_complete.json"  # 294方剂版
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# ルート構造に応じて調整
if 'mbt_kampo_library' in data:
    formulas = data['mbt_kampo_library']['formulas']
else:
    formulas = data['formulas']  # 配列形式の場合

pathway_scores = {}

for fid, fdata in formulas.items():
    scores = {'PATH_01': 0, 'PATH_02': 0, 'PATH_03': 0, 'PATH_04': 0, 'PATH_05': 0}
    
    # 各成分の植物化学物質をループ
    for herb, hdata in fdata.get('components', {}).items():
        # 植物化学物質
        for phytochem in hdata.get('phytochemicals', []):
            pathway = phytochem.get('metabolic_pathway')
            if pathway and pathway in scores:
                # 濃度を加味する場合
                conc = phytochem.get('concentration_mg_per_g', '0-0')
                weight = parse_concentration(conc)
                scores[pathway] += weight  # 加重カウント
                # 単純カウントなら scores[pathway] += 1
    
    # 多糖類なども対象に含める（必要に応じて）
    # 例：茯苓のpolysaccharidesはPATH_05
    if 'polysaccharides' in hdata:
        if hdata['polysaccharides'].get('metabolic_pathway') == 'PATH_05':
            scores['PATH_05'] += 1  # 適宜調整
    
    pathway_scores[fid] = scores

# CSV出力
with open('pathway_features.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['formula_id', 'PATH_01', 'PATH_02', 'PATH_03', 'PATH_04', 'PATH_05'])
    for fid, scores in pathway_scores.items():
        writer.writerow([fid, scores['PATH_01'], scores['PATH_02'], scores['PATH_03'], scores['PATH_04'], scores['PATH_05']])

print("✅ pathway_features.csv を生成しました。")
```

---

## 🔄 ワークフロー提案

1. **このスクリプトを実行** → `pathway_features.csv` が生成される
2. 開発チームはこのCSVを読み込み、**5次元の連続値ベクトル**としてクラスタリングを実行
   - 必要ならスケーリング（標準化）を行う
3. クラスタリング結果を確認 → 有効なクラスタが形成されるはず

---

## 📈 期待される効果

- 各処方が **複数パスウェイの強度** を持つため、ベクトルが多様化
- 同一の主要パスウェイでも、副次的なパスウェイの有無で区別可能
- k-meansなどが機能するようになる

---

## 🔮 将来的な拡張

- 現在はPATH_01〜05のみだが、今後PATH_06〜15が追加された場合、スクリプトを修正して次元を拡張可能
- さらに、植物化学物質の種類やミネラル組成なども特徴量に加えることで、よりリッチなクラスタリングが可能

---

ご要望であれば、このスクリプトを完全な形で提供し、実行方法を詳しく説明します。また、JSONに直接 `pathway_scores` を埋め込むバージョンも作成可能です。

---

