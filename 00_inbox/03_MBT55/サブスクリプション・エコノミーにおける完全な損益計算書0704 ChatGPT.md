サブスクリプション・エコノミーにおける損益計算書（Income Statement）を作成するために、Pythonコードで基本的な構造を作成することができます。損益計算書には、収益、費用、利益などが含まれます。以下は、その例です：

```python
import pandas as pd

# 損益計算書のデータを辞書形式で作成
data = {
    '項目': [
        '収益', 'サブスクリプション収益', 'その他収益',
        '総収益',
        '費用', '運用費用', 'マーケティング費用', '研究開発費用', '管理費用', 'その他費用',
        '総費用',
        '営業利益',
        '税引前利益',
        '法人税',
        '純利益'
    ],
    '金額': [
        '', 500000, 50000, 
        '=B2+B3',
        '', 200000, 50000, 30000, 20000, 10000,
        '=B6+B7+B8+B9+B10',
        '=B4-B11',
        '=B12',
        0.3 * 300000, # 法人税を仮に利益の30%とする
        '=B12-B14'
    ]
}

# DataFrameに変換
df = pd.DataFrame(data)

# 表示
print(df)
```

このコードは基本的な構造を示していますが、具体的な数字は仮定に基づいています。より詳細で現実的な損益計算書を作成するには、実際の収益と費用のデータを提供する必要があります。また、セル内で計算を行う場合には、Excelのようにセル参照を使うことができないため、実際の計算はPythonのコード内で行う必要があります。以下に、計算をPythonで行う完全な例を示します：

```python
import pandas as pd

# サブスクリプションの収益とその他収益
subscription_revenue = 500000
other_revenue = 50000

# 各種費用
operational_expenses = 200000
marketing_expenses = 50000
rnd_expenses = 30000
admin_expenses = 20000
other_expenses = 10000

# 総収益の計算
total_revenue = subscription_revenue + other_revenue

# 総費用の計算
total_expenses = (operational_expenses + marketing_expenses + rnd_expenses +
                  admin_expenses + other_expenses)

# 営業利益の計算
operating_profit = total_revenue - total_expenses

# 法人税率を30%と仮定して税引前利益と法人税、純利益を計算
tax_rate = 0.3
pre_tax_profit = operating_profit
tax = pre_tax_profit * tax_rate
net_profit = pre_tax_profit - tax

# 損益計算書のデータを辞書形式で作成
data = {
    '項目': [
        '収益', 'サブスクリプション収益', 'その他収益', '総収益',
        '費用', '運用費用', 'マーケティング費用', '研究開発費用', '管理費用', 'その他費用', '総費用',
        '営業利益', '税引前利益', '法人税', '純利益'
    ],
    '金額': [
        '', subscription_revenue, other_revenue, total_revenue,
        '', operational_expenses, marketing_expenses, rnd_expenses, admin_expenses, other_expenses, total_expenses,
        operating_profit, pre_tax_profit, tax, net_profit
    ]
}

# DataFrameに変換
df = pd.DataFrame(data)

# 表示
print(df)
```

このコードを実行すると、サブスクリプション・エコノミーにおける損益計算書が出力されます。具体的な数値は仮定に基づいているため、実際のビジネスデータに応じて適宜調整してください。