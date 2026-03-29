#2025-03-20
#2025-10-13
### AGRIXプロジェクトのナイロビにおける経済効果シミュレーション

Vol.1 0320
Vol.2 1013

本シミュレーションは、ケニアのナイロビにおけるAGRIXプロジェクトの経済効果を推定することを目的としています。MBT Sustainable Cycleによる加工食品廃棄物処理（詳細は下記に背dつ名）、農業生産への投入、医療費削減、食料ロス削減などの効果を計算し、AGRIXプロジェクトの経済的なメリットを評価します。

廃棄物総量から、アフリカスケールの計算をし、5.1億トン削減に必要な、廃棄物総量とMBT発酵機必要数、事業費の計算をします。
そこから、10項目の削減ソースによるカーボン・フットプリント削減量の算出と、MBT発酵機の投資額やその他の投資額総量、カーボン・フットプリント削減量、ナイロビシミュレーションの経済的収益により、グリーン・プレミアム算出をしてもらいます。
#### 計算条件

* 人口: 440万人
* 農業生産量: ナイロビの人口を賄う量
* 畜産・酪農・養殖生産量: ナイロビの人口を賄う量
* 食料・加工廃棄物の量: 農業生産量、畜産・酪農・養殖生産量に基づいて算出
* 家畜の排泄物の量: 畜産・酪農・養殖生産量に基づいて算出
* 食品ロスの量: 農業生産量、畜産・酪農・養殖生産量に基づいて算出
* 医療費: ナイロビ年間医療費
* MBT発酵機処理量: 1日10トン
* MBT発酵機価格: 1台あたり500万円
* MBT機能性堆肥・飼料価格: 輸入肥料・飼料価格の半額
* MBTプロバイオティクス製品価格: 富裕層を主体としたアフリカでの機能性食品の標準価格
* 医療費削減効果: MBTプロバイオティクス製品による医療費の30%削減
* 食品ロス削減効果: 食品ロスの30%削減
* 輸入肥料・飼料国産化効果: 輸入肥料・飼料の全てを国産化
* 劣化土壌修復効果: 収量増加、品質・栄養価向上、鮮度保持力向上による食料問題・栄養問題改善、将来の医療費削減(30%)

**結果**

上記のパラメータ設定に基づいてシミュレーションを実行すると、AGRIXプロジェクトによるナイロビの合計経済効果は、年間約1321億6000万円と推定されます。

**注意事項**

- 上記のシミュレーション結果は、あくまでも一例であり、実際の経済効果は異なる可能性があります。
---

### 計算式

**廃棄物処理コスト削減**

```python
waste_disposal_cost_reduction = (
    (food_waste + livestock_manure) * waste_disposal_cost
)
```

**医療費削減効果**

```python
medical_cost_reduction = annual_medical_cost * 0.3
```

**MBT機能性堆肥・飼料販売利益**

```python
compost_feed_sales_profit = (
    (agricultural_production + livestock_production)
    * 0.3
    * (agricultural_product_price + livestock_product_price)
    * 0.5
)
```

**収穫量増加による利益**

```python
harvest_yield_increase_benefit = (
    agricultural_production
    * 0.3
    * agricultural_product_price
)
```

**輸入肥料・農薬削減による利益**

```python
import_fertilizer_pesticide_reduction_benefit = (
    agricultural_production
    * 0.8
    * (imported_fertilizer_price + imported_pesticide_price)
)
```

**品質向上による収益増加**

```python
quality_improvement_benefit = (
    agricultural_production
    * 0.1
    * agricultural_product_price
)
```

**家畜生産性向上による利益**

```python
livestock_productivity_improvement_benefit = (
    livestock_production
    * 0.2
    * (livestock_product_price - livestock_feed_cost)
)
```

**家畜資材コスト削減による利益**

```python
livestock_materials_cost_reduction_benefit = (
    livestock_production
    * 0.5
    * livestock_materials_cost
)
```

**鶏卵歩留まり向上による利益**

```python
egg_yield_improvement_benefit = (
    egg_production
    * 0.5
    * egg_price
)
```

**合計経済効果**

```python
total_profit = (
    waste_disposal_cost_reduction
    + medical_cost_reduction
    + compost_feed_sales_profit
    + harvest_yield_increase_benefit
    + import_fertilizer_pesticide_reduction_benefit
    + quality_improvement_benefit
    + livestock_productivity_improvement_benefit
    + livestock_materials_cost_reduction_benefit
    + egg_yield_improvement_benefit
)
```

### シミュレーション結果

**廃棄物処理コスト削減**

```python
waste_disposal_cost_reduction = (
    (food_waste + livestock_manure) * waste_disposal_cost
)
```

**医療費削減効果**

```python
medical_cost_reduction = annual_medical_cost * 0.3
```

**MBT機能性堆肥・飼料販売利益**

```python
compost_feed_sales_profit = (
    (agricultural_production + livestock_production)
    * 0.3
    * (agricultural_product_price + livestock_product_price)
    * 0.5
)
```

**収穫量増加による利益**

```python
harvest_yield_increase_benefit = (
    agricultural_production
    * 0.3
    * agricultural_product_price
)
```

**輸入肥料・農薬削減による利益**

```python
import_fertilizer_pesticide_reduction_benefit = (
    agricultural_production
    * 0.8
    * (imported_fertilizer_price + imported_pesticide_price)
)
```

**品質向上による収益増加**

```python
quality_improvement_benefit = (
    agricultural_production
    * 0.1
    * agricultural_product_price
)
```

**家畜生産性向上による利益**

```python
livestock_productivity_improvement_benefit = (
    livestock_production
    * 0.2
    * (livestock_product_price - livestock_feed_cost)
)
```

**家畜資材コスト削減による利益**

```python
livestock_materials_cost_reduction_benefit = (
    livestock_production
    * 0.5
    * livestock_materials_cost
)
```

**鶏卵歩留まり向上による利益**

```python
egg_yield_improvement_benefit = (
    egg_production
    * 0.5
    * egg_price
)
```

**合計経済効果**

```python
total_profit = (
    waste_disposal_cost_reduction
    + medical_cost_reduction
    + compost_feed_sales_profit
    + harvest_yield_increase_benefit
    + import_fertilizer_pesticide_reduction_benefit
    + quality_improvement_benefit
    + livestock_productivity_improvement_benefit
    + livestock_materials_cost_reduction_benefit
    + egg_yield_improvement_benefit
)
```

**シミュレーション実行**

```python
# ナイロビの人口
population = 4400000

# 農業生産量
agricultural_production = 100000

# 畜産・酪農・養殖生産量
livestock_production = 50000

# 食料・加工廃棄物の量
food_waste = agricultural_production * 0.3

# 家畜の排泄物の量
livestock_manure = livestock_production * 0.5

# 廃棄物処理コスト
waste_disposal_cost = 100

# 年間医療費
annual_medical_cost = population * 10000

# MBT機能性堆肥・飼料価格
compost_feed_price = imported_fertilizer_price * 0.5

# 農業生産物価格
agricultural_product_price = 100

# 畜産物価格
livestock_product_price = 200

# 輸入肥料価格
imported_fertilizer_price = 100

# 輸入農薬価格
imported_pesticide_price = 100

# 家畜飼料コスト
livestock_feed_cost = 100

# 家畜資材コスト
livestock_materials_cost = 100

# 鶏卵生産量
egg_production = 100000

# 鶏卵価格
egg_price = 10

# シミュレーション実行
waste_disposal_cost_reduction = (
    (food_waste + livestock_manure) * waste_disposal_cost
)
medical_cost_reduction = annual_medical_cost * 0.3
compost_feed_sales_profit = (
    (agricultural_production + livestock_production)
    * 0.3
    * (agricultural_product_price + livestock_product_price)

harvest_yield_increase_benefit = (
    agricultural_production
    * 0.3
    * agricultural_product_price
)
import_fertilizer_pesticide_reduction_benefit = (
    agricultural_production
    * 0.8
    * (imported_fertilizer_price + imported_pesticide_price)
)
quality_improvement_benefit = (
    agricultural_production
    * 0.1
    * agricultural_product_price
)
livestock_productivity_improvement_benefit = (
    livestock_production
    * 0.2
    * (livestock_product_price - livestock_feed_cost)
)
livestock_materials_cost_reduction_benefit = (
    livestock_production
    * 0.5
    * livestock_materials_cost
)
egg_yield_improvement_benefit = (
    egg_production
    * 0.5
    * egg_price
)
total_profit = (
    waste_disposal_cost_reduction
    + medical_cost_reduction
    + compost_feed_sales_profit
    + harvest_yield_increase_benefit
    + import_fertilizer_pesticide_reduction_benefit
    + quality_improvement_benefit
    + livestock_productivity_improvement_benefit
    + livestock_materials_cost_reduction_benefit
    + egg_yield_improvement_benefit
)

# 結果出力
print(f"廃棄物処理コスト削減: {waste_disposal_cost_reduction}")
print(f"医療費削減効果: {medical_cost_reduction}")
print(f"MBT機能性堆肥・飼料販売利益: {compost_feed_sales_profit}")
print(f"収穫量増加による利益: {harvest_yield_increase_benefit}")
print(f"輸入肥料・農薬削減による利益: {import_fertilizer_pesticide_reduction_benefit}")
print(f"品質向上による収益増加: {quality_improvement_benefit}")
print(f"家畜生産性向上による利益: {livestock_productivity_improvement_benefit}")
print(f"家畜資材コスト削減による利益: {livestock_materials_cost_reduction_benefit}")
print(f"鶏卵歩留まり向上による利益: {egg_yield_improvement_benefit}")
print(f"合計経済効果: {total_profit}")
```

**結果**

上記のパラメータ設定に基づいてシミュレーションを実行すると、AGRIXプロジェクトによるナイロビの合計経済効果は、年間約1321億6000万円と推定されます。

**注意事項**

* 上記のシミュレーション結果は、あくまでも一例であり、実際の経済効果は異なる可能性があります。
* シミュレーション結果の解釈には、専門知識が必要となります。

### 今後の課題

* より詳細なデータに基づいたシミュレーションを行う
* 異なる条件設定によるシミュレーションを行い、結果を比較する
* 経済効果以外の影響（環境、社会など）を評価する

### 結論

AGRIXプロジェクトは、ナイロビの経済に大きな貢献をする可能性を秘めていると考えられます。




