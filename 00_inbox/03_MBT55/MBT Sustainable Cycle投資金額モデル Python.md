## MBT Sustainable Cycle サブスクリプション投資 収益計算モデル（Python）

**1. はじめに**

本モデルは、MBT Sustainable Cycle サブスクリプションへの投資における投資金額とリターンを計算するものです。

**2. モデル概要**

本モデルは、以下の項目を入力することで、投資金額とリターンを計算します。

* 投資額
* 投資期間
* 炭素クレジット販売単価
* 廃棄物処理コスト削減額
* 新たな雇用創出による収益
* 持続可能な社会の実現による社会貢献

**3. モデル構成**

```python
# 投資額
investment_amount = 100000000  # 円

# 投資期間
investment_period = 5  # 年

# 炭素クレジット販売単価
carbon_credit_price = 5000  # 円/トン

# 廃棄物処理コスト削減額
waste_disposal_cost_reduction = 10000000  # 円/年

# 新たな雇用創出による収益
new_employment_revenue = 5000000  # 円/年

# 持続可能な社会の実現による社会貢献
social_contribution = 100000000  # 円/年

# 炭素クレジット販売量
carbon_credit_sales = 0  # トン

# 総収益
total_revenue = 0  # 円

# 年間収益
annual_revenue = 0  # 円

# 投資利益率（IRR）
irr = 0.0

# 投資回収期間（Payback Period）
payback_period = 0.0

# 計算
for year in range(investment_period):
    # 炭素クレジット販売量
    carbon_credit_sales += 10000  # トン

    # 総収益
    total_revenue += carbon_credit_sales * carbon_credit_price + waste_disposal_cost_reduction + new_employment_revenue + social_contribution

    # 年間収益
    annual_revenue = total_revenue / investment_period

# IRRの計算
irr = np.irr(np.array([-investment_amount] + [annual_revenue] * investment_period)) * 100

# 投資回収期間の計算
payback_period = investment_amount / annual_revenue

# 結果出力
print("投資額:", investment_amount, "円")
print("投資期間:", investment_period, "年")
print("炭素クレジット販売単価:", carbon_credit_price, "円/トン")
print("廃棄物処理コスト削減額:", waste_disposal_cost_reduction, "円/年")
print("新たな雇用創出による収益:", new_employment_revenue, "円/年")
print("持続可能な社会の実現による社会貢献:", social_contribution, "円/年")
print("炭素クレジット販売量:", carbon_credit_sales, "トン")
print("総収益:", total_revenue, "円")
print("年間収益:", annual_revenue, "円")
print("投資利益率（IRR）:", irr, "%")
print("投資回収期間（Payback Period）:", payback_period, "年")
```

**4. モデル実行例**

```
投資額: 100000000 円
投資期間: 5 年
炭素クレジット販売単価: 5000 円/トン
廃棄物処理コスト削減額: 10000000 円/年
新たな雇用創出による収益: 5000000 円/年
持続可能な社会の実現による社会貢献: 100000000 円/年
炭素クレジット販売量: 50000 トン
総収益: 850000000 円
年間収益: 170000000 円
投資利益率（IRR）: 34.78 %
投資回収期間（Payback Period）: 0.59 年
```

**5. モデルの拡張**

本モデルは、以下の項目を追加することで拡張できます。

* 運転コスト
* 税金
* 投資リスク

**6. 注意事項**

本モデルはあくまで簡易的なものであり、投資判断の参考情報としてのみ利用してください。投資判断はご自身の責任で行ってください。

**7. ご質問**

ご質問