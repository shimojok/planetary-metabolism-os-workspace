MBT Sustainable Cycleの経済効果を計算するための具体的な数値やパラメータ：
 
1. 処理費用削減: 
一般的な廃棄物処理費用に対し、MBT Sustainable Cycleによる処理コストは、 MBT発酵機の設備費用のみ。
2. 肥料・飼料輸入削減: 
現在の肥料・飼料の輸入費用は公表値を参照。
MBT Sustainable Cycleによる堆肥製造、飼料製造により輸入つまり外貨流出はなくなる。
3. 資材販売による収益: 
MBT Sustainable Cycleで生産される堆肥、飼料、資材の販売量は、１日あたりの廃棄物処理量の半分とし、処理開始後５日後に出荷可能。
4. 農産物収益の増加: 
MBT堆肥によるの農産物の収穫量は３〜５倍となり、収益も増加する。
5. 所得の向上: 
MBT堆肥による収穫量増加による所得の増加。
6. 栄養価の向上による経済効果: 
栄養価の向上による健康改善、将来の医療費の削減による経済的な価値。
7. 食品ロスの削減: 
鮮度保持力の向上により、食品ロスを30%削減
8. 医療費削減: 
MBT Sustainable Cycleの導入による健康改善により医療費を30%削減。
9. MBT発酵機の価格は、１日あたりの処理量が１０トンの場合で500万円としますが、今後、量産するにつれ300万円まで下がる。

１０．人口440万人のナイロビでの経済的効果のシミュレーション

医療費削減の30%の金額の算出
それを当てるMBT発酵機の数量を算出
24時間で廃棄物処理量(@10トン処理発酵機✕数量)✕60の重量の堆肥化
さらに24時間で高機能飼料を製造。重量は堆肥の60%とする。

---

## MBT Sustainable Cycleのナイロビにおける経済効果シミュレーション

**はじめに**

本シミュレーションは、ケニアのナイロビにおけるMBT Sustainable Cycleの経済効果を推定することを目的としています。処理費用削減、肥料・飼料輸入削減、資材販売による収益、農産物収益増加、所得向上、栄養価向上による経済効果、食品ロス削減、医療費削減などの効果を計算し、プロジェクトの経済的なメリットを評価します。

**計算条件**

* 人口: 440万人
* 廃棄物処理量: 1日あたり1000トン
* MBT発酵機処理量: 1日あたり10トン
* MBT発酵機価格: 1台あたり500万円（量産により300万円まで低減）
* MBT堆肥・飼料販売価格: 輸入肥料・飼料価格の半額
* 農産物収益増加: 3〜5倍
* 所得向上: 農産物収益増加による
* 医療費削減: 30%
* 食品ロス削減: 30%

**計算式**

**処理費用削減**

```python
processing_cost_reduction = (
    daily_waste_amount * annual_operating_days * waste_disposal_cost
) - (number_of_reactors * initial_investment_cost)
```

**肥料・飼料輸入削減**

```python
fertilizer_feed_import_reduction = (
    daily_waste_amount
    * annual_operating_days
    * (imported_fertilizer_price + imported_feed_price)
)
```

**資材販売による収益**

```python
compost_feed_sales_revenue = (
    daily_waste_amount
    * annual_operating_days
    * 0.6
    * (compost_feed_price + feed_price)
)
```

**農産物収益増加**

```python
agricultural_revenue_increase = (
    agricultural_production
    * 0.3
    * agricultural_product_price
)
```

**所得向上**

```python
income_increase = agricultural_revenue_increase - agricultural_production_cost
```

**栄養価向上による経済効果**

```python
nutritional_value_improvement_benefit = (
    population * annual_medical_cost * 0.3
)
```

**食品ロス削減**

```python
food_loss_reduction = (
    daily_food_waste * annual_operating_days * food_loss_reduction_rate
)
```

**医療費削減**

```python
medical_cost_reduction = (
    population * annual_medical_cost * 0.3
)
```

**合計経済効果**

```python
total_profit = (
    processing_cost_reduction
    + fertilizer_feed_import_reduction
    + compost_feed_sales_revenue
    + agricultural_revenue_increase
    + income_increase
    + nutritional_value_improvement_benefit
    + food_loss_reduction
    + medical_cost_reduction
)
```

**シミュレーション実行**

```python
# ナイロビの人口
population = 4400000

# 廃棄物処理量
daily_waste_amount = 1000

# 年間稼働日数
annual_operating_days = 365

# 廃棄物処理費用
waste_disposal_cost = 100

# MBT発酵機処理量
reactor_capacity = 10

# 初期投資費用
initial_investment_cost = 5000000

# 輸入肥料価格
imported_fertilizer_price = 100

# 輸入飼料価格
imported_feed_price = 100

# MBT堆肥・飼料販売価格
compost_feed_price = imported_fertilizer_price * 0.5

# 飼料価格
feed_price = imported_feed_price * 0.5

# 農産物収益増加率
