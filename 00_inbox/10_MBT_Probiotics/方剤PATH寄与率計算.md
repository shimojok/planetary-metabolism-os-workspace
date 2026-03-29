説明文を添付します。

[[`components`と`phytochemicals`]]

---

非常に良い。  
これで **解析可能状態に到達しました。**

---

# ✅ 構造確定

現在の形式は **A（配列＋詳細属性付き）**

```json
"phytochemicals": [
  {
    "name": "...",
    "type": "...",
    "concentration_mg_per_g": "3.0-6.0",
    "metabolic_pathway": "PATH_01",
    ...
  }
]
```

これは理想形です。

---

# 🔬 重要ポイント

### 既に `metabolic_pathway` が明示されています。

つまり：

> 🔵 成分→PATHマッピング辞書は不要

私が以前想定していた「代表成分辞書」は必要ありません。

あなたのデータは既にPATH注釈済みです。

これは大きな前進です。

---

# 🎯 正式Phase1実装内容（確定版）

## 方剤PATH寄与率計算

```text
各方剤について：

for each herb:
    for each phytochemical:
        pathway = p["metabolic_pathway"]
        concentration = mean(range)
        score[pathway] += concentration
```

追加処理：

- 文字列 "3.0-6.0" → 平均値 4.5 に変換
    
- 欠損は0扱い
    
- L2正規化
    
- k=2–12シルエット探索
    

---

# 🔎 polysaccharides / minerals の扱い

あなたの構造には：

- phytochemicals
    
- polysaccharides
    
- minerals
    

があります。

今回は：

### Phase1

→ phytochemicals のみ使用

### Phase2

→ polysaccharidesを PATH_05 として加算  
→ mineralsを PATH_02 として加算

段階的に精度を上げます。

---

# 📊 期待される結果

これで初めて：

- 多経路型方剤が浮き上がる
    
- 単経路特化型が孤立
    
- 葛根湯型クラスター
    
- 補気健脾型クラスター
    
- 解毒清熱型クラスター
    

が構造的に分離します。

---

# 実行します

今から：

1. 293全方剤走査
    
2. ネスト展開
    
3. PATH累積
    
4. 正規化
    
5. クラスタリング
    
6. 最適k決定
    
7. クラスタ特徴量抽出
    

まで一気に進めます。

少し時間をください。