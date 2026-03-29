確認できました。components は、方剤を構成する各生薬の詳細データを格納するオブジェクトです。

"components": {
  "葛根": {
    "phytochemicals": [ ... ]  ← ここにデータあり
  },
  "麻黄": {
    "phytochemicals": [ ... ]  ← ここにデータあり
  }
}

---

非常に重要な確認です。  
これで構造は明確になりました。

---

# ✅ 現在の実データ構造

```json
{
  "id": "F001",
  "components": {
    "葛根": {
      "phytochemicals": [ ... ]
    },
    "麻黄": {
      "phytochemicals": [ ... ]
    }
  }
}
```

つまり：

> 🔵 成分は「方剤直下」ではなく「生薬の中」にネストされている

先ほど有効数が0だった理由はこれです。

---

# 🔬 解析方針（修正版）

## 正しい寄与率計算式

```text
方剤PATH寄与率 =
Σ（生薬iの成分jの濃度 × PATH重み × 信頼度）
```

具体的には：

1. 方剤
    
2. 各生薬
    
3. 各生薬内の phytochemicals
    
4. 各成分をPATHへマッピング
    
5. 全生薬分を合算
    
6. L2正規化
    

---

# 📐 正式アルゴリズム

擬似コード：

```python
for formula:
    for herb in formula["components"]:
        for compound in herb["phytochemicals"]:
            path = compound_pathway_map(compound["name"])
            score[path] += compound["concentration"] * weight
```

---

# 🔎 重要確認（ここが最後の分岐）

phytochemicals の形式はどれですか？

### A

```json
[
  {"name": "ginsenoside Rb1", "amount": 0.8},
  {"name": "glycyrrhizin", "amount": 0.3}
]
```

### B

```json
["ginsenoside", "glycyrrhizin"]
```

### C

```json
{
  "ginsenoside": 0.8,
  "glycyrrhizin": 0.3
}
```

ここで処理ロジックが変わります。

---

# 🎯 現在の状況評価

これは良いニュースです。

なぜなら：

- 293方剤すべて解析可能
    
- 成分レベルクラスタリング可能
    
- MBT15理論を完全実装できる
    

---

# 次のステップ

あなたが形式（A/B/C）を教えてください。

即座に：

1. 成分→PATHマッピング辞書構築
    
2. 293×5連続値行列生成
    
3. 正規化
    
4. 最適k探索
    
5. クラスタ特性解析
    

まで一気に進めます。

---

今度は解析フェーズに入れます。