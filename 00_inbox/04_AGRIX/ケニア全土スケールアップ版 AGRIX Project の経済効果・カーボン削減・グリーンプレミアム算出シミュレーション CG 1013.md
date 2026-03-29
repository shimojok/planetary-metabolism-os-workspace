Prompt

下記のケニアシミュレーションにより、AGRIX Project による経済的効果、カーボン・フットプリント削減量、グリーンプレミアムを算出できますか？

−−−

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple

class AGRIXProjectAnalysis:
    def __init__(self):
        self.setup_agrix_parameters()
        
    def setup_agrix_parameters(self):
        """AGRIX Project専用パラメーターを設定"""
        
        # AGRIX Project 拡張パラメーター
        self.agrix_params = {
            # 基本経済パラメーター
            'conventional_fertilizer_cost': 80_000,  # 化学肥料コスト [円/トン]
            'water_savings_rate': 0.3,              # 節水率 [%]
            'water_cost': 50,                       # 水コスト [円/トン]
            'crop_yield_increase': 0.25,            # 収量増加率 [%]
            'crop_value': 100_000,                  # 作物価値 [円/トン]
            
            # 投資パラメーター
            'initial_investment_per_ton': 50_000,   # 初期投資 [円/トン処理能力]
            'om_cost_rate': 0.15,                   # O&Mコスト率 [投資額に対する%]
            'project_lifetime': 20,                 # プロジェクト寿命 [年]
            
            # 環境パラメーター
            'soil_health_improvement': 0.15,        # 土壌健康改善係数
            'biodiversity_value': 5_000,            # 生物多様性価値 [円/ha/年]
            
            # 社会パラメーター
            'jobs_created_per_10k_ton': 5,          # 雇用創出 [人/1万トン]
            'local_income_multiplier': 2.3,         # 地域所得乗数効果
        }
        
    def calculate_agrix_economic_impact(self, waste_volume: float, ghg_reduction: float, 
                                      scenario: str) -> Dict:
        """AGRIX Projectの経済的効果を詳細計算"""
        
        compost_produced = waste_volume * 0.4  # 堆肥生成率40%
        
        # 直接的な経済効果
        direct_benefits = {}
        
        # 1. 肥料コスト削減
        fertilizer_replaced = compost_produced * 0.05  # 肥料代替率5%
        direct_benefits['fertilizer_savings'] = fertilizer_replaced * self.agrix_params['conventional_fertilizer_cost']
        
        # 2. 水コスト削減（堆肥による保水性向上）
        water_savings = compost_produced * 10 * self.agrix_params['water_savings_rate']  # 10トン水/トン堆肥
        direct_benefits['water_savings'] = water_savings * self.agrix_params['water_cost']
        
        # 3. 収量増加による便益
        # 堆肥施用面積: 堆肥10トン/ha/年で施用
        land_area = compost_produced / 10
        yield_increase = land_area * 2 * self.agrix_params['crop_yield_increase']  # ベース収量2トン/ha
        direct_benefits['yield_improvement'] = yield_increase * self.agrix_params['crop_value']
        
        # 4. 炭素クレジット収入
        carbon_price = 1500  # 円/tCO₂e
        direct_benefits['carbon_credits'] = ghg_reduction * carbon_price
        
        # 5. 廃棄物処理コスト削減
        treatment_cost_avoided = 3000  # 円/トン
        direct_benefits['treatment_savings'] = waste_volume * treatment_cost_avoided
        
        # 総直接便益
        direct_benefits['total_direct'] = sum(direct_benefits.values())
        
        # 間接的経済効果
        indirect_benefits = {}
        
        # 1. 雇用創出効果
        jobs_created = (waste_volume / 10000) * self.agrix_params['jobs_created_per_10k_ton']
        indirect_benefits['employment_value'] = jobs_created * 2_000_000  # 年収200万円/人
        
        # 2. 生物多様性価値
        indirect_benefits['biodiversity_value'] = land_area * self.agrix_params['biodiversity_value']
        
        # 3. 地域経済乗数効果
        indirect_benefits['local_economy_multiplier'] = direct_benefits['total_direct'] * (self.agrix_params['local_income_multiplier'] - 1)
        
        # 総間接便益
        indirect_benefits['total_indirect'] = sum(indirect_benefits.values())
        
        # 総経済効果
        total_economic_impact = {
            'direct_benefits': direct_benefits,
            'indirect_benefits': indirect_benefits,
            'total_benefits': direct_benefits['total_direct'] + indirect_benefits['total_indirect']
        }
        
        return total_economic_impact
    
    def calculate_green_premium(self, waste_volume: float, total_benefits: float) -> Dict:
        """グリーンプレミアムを計算"""
        
        # 投資コスト計算
        initial_investment = waste_volume * self.agrix_params['initial_investment_per_ton']
        annual_om_costs = initial_investment * self.agrix_params['om_cost_rate']
        
        # 従来システムのコスト（ベースライン）
        conventional_treatment_cost = waste_volume * 5000  # 従来処理コスト [円/トン]
        conventional_fertilizer_cost = waste_volume * 0.4 * 0.05 * 80000  # 従来肥料コスト
        
        baseline_annual_cost = conventional_treatment_cost + conventional_fertilizer_cost
        
        # AGRIXシステムの正味年間コスト
        agrix_annual_cost = (initial_investment / self.agrix_params['project_lifetime']) + annual_om_costs
        
        # グリーンプレミアム計算
        green_premium_analysis = {
            'initial_investment': initial_investment,
            'annual_om_costs': annual_om_costs,
            'baseline_annual_cost': baseline_annual_cost,
            'agrix_annual_cost': agrix_annual_cost,
            'annual_benefits': total_benefits,
            'net_annual_savings': total_benefits - agrix_annual_cost,
            'green_premium_ratio': (total_benefits - agrix_annual_cost) / agrix_annual_cost,
            'payback_period': initial_investment / (total_benefits - annual_om_costs) if (total_benefits - annual_om_costs) > 0 else float('inf'),
            'roi_percentage': ((total_benefits - agrix_annual_cost) * self.agrix_params['project_lifetime'] - initial_investment) / initial_investment * 100
        }
        
        return green_premium_analysis
    
    def calculate_carbon_footprint_reduction(self, waste_volume: float, scenario: str) -> Dict:
        """カーボン・フットプリント削減量を詳細計算"""
        
        compost_produced = waste_volume * 0.4
        
        carbon_reduction = {}
        
        # 1. 直接的な排出削減
        # 廃棄物処理からのメタン回避
        methane_avoided = waste_volume * 0.06 * 25  # メタン発生係数 × GWP
        carbon_reduction['waste_methane_avoidance'] = methane_avoided
        
        # 堆肥による炭素固定
        carbon_sequestered = compost_produced * 0.15 * 3.67  # 炭素固定率 × CO2換算
        carbon_reduction['carbon_sequestration'] = carbon_sequestered
        
        # 化学肥料製造回避
        fertilizer_avoided = compost_produced * 0.05
        fertilizer_co2_avoided = fertilizer_avoided * 5
        carbon_reduction['fertilizer_production_avoidance'] = fertilizer_co2_avoided
        
        # 2. 間接的な排出削減
        # 家畜メタン削減
        nairobi_livestock = 200_000
        scale_factor = 4.0 if scenario == 'medium' else 3.0 if scenario == 'low' else 5.0
        kenya_livestock = nairobi_livestock * scale_factor
        livestock_methane_reduction = kenya_livestock * 0.07 * 0.3 * 25
        carbon_reduction['livestock_methane_reduction'] = livestock_methane_reduction
        
        # 食品ロス削減
        food_waste_reduced = waste_volume * 0.2  # 食品廃棄物比率仮定
        food_loss_reduction = food_waste_reduced * 2.0
        carbon_reduction['food_loss_reduction'] = food_loss_reduction
        
        # 農地の炭素蓄積
        land_rehabilitated = min(compost_produced / 10, 14000000)
        biomass_carbon = land_rehabilitated * 0.5 * 3.67
        carbon_reduction['biomass_carbon_accumulation'] = biomass_carbon
        
        # 輸送距離短縮による削減
        local_processing_benefit = waste_volume * 0.1  # 10kg CO2/トン削減
        carbon_reduction['transportation_reduction'] = local_processing_benefit
        
        # 総カーボン・フットプリント削減
        carbon_reduction['total_footprint_reduction'] = sum(carbon_reduction.values())
        
        return carbon_reduction

def run_comprehensive_agrix_analysis():
    """AGRIX Projectの包括的分析を実行"""
    
    # 既存のケニアシミュレーションデータを使用
    kenya_simulation = KenyaMBTSimulation()
    kenya_results = kenya_simulation.run_simulation()
    
    # AGRIX分析インスタンス作成
    agrix_analysis = AGRIXProjectAnalysis()
    
    comprehensive_results = {}
    
    for scenario in ['low', 'medium', 'high']:
        scenario_data = kenya_results[scenario]
        waste_volume = scenario_data['waste']['total']
        ghg_reduction = scenario_data['ghg_reduction']['total']
        
        # 各指標を計算
        economic_impact = agrix_analysis.calculate_agrix_economic_impact(waste_volume, ghg_reduction, scenario)
        carbon_footprint = agrix_analysis.calculate_carbon_footprint_reduction(waste_volume, scenario)
        green_premium = agrix_analysis.calculate_green_premium(waste_volume, economic_impact['total_benefits'])
        
        comprehensive_results[scenario] = {
            'economic_impact': economic_impact,
            'carbon_footprint': carbon_footprint,
            'green_premium': green_premium,
            'waste_volume': waste_volume,
            'basic_ghg_reduction': ghg_reduction
        }
    
    return comprehensive_results, agrix_analysis

# 包括的分析の実行
comprehensive_results, agrix_analysis = run_comprehensive_agrix_analysis()

# 結果の表示と可視化
def display_agrix_results(comprehensive_results):
    """AGRIX Projectの結果を表示"""
    
    print("=" * 70)
    print("AGRIX Project 総合評価レポート")
    print("=" * 70)
    
    # サマリーテーブル作成
    summary_data = []
    
    for scenario in ['low', 'medium', 'high']:
        data = comprehensive_results[scenario]
        
        # 経済効果
        economic = data['economic_impact']
        total_economic = economic['total_benefits'] / 1_000_000_000  # 十億円
        
        # カーボン削減
        carbon = data['carbon_footprint']
        total_carbon = carbon['total_footprint_reduction'] / 1_000_000  # 百万tCO₂e
        
        # グリーンプレミアム
        premium = data['green_premium']
        roi = premium['roi_percentage']
        payback = premium['payback_period']
        
        summary_data.append({
            'シナリオ': scenario.upper(),
            '総経済効果 (十億円/年)': round(total_economic, 1),
            'カーボン削減 (百万tCO₂e/年)': round(total_carbon, 1),
            '投資利益率 (ROI)': f"{round(roi, 1)}%",
            '回収期間 (年)': round(payback, 1) if payback != float('inf') else "N/A",
            'グリーンプレミアム比率': f"{round(premium['green_premium_ratio']*100, 1)}%"
        })
    
    summary_df = pd.DataFrame(summary_data)
    print("\n1. AGRIX Project 主要指標サマリー")
    print("=" * 50)
    print(summary_df.to_string(index=False))
    
    # 詳細経済効果（中型シナリオ）
    print("\n2. 経済効果内訳（中型シナリオ）")
    print("=" * 50)
    
    medium_economic = comprehensive_results['medium']['economic_impact']
    direct = medium_economic['direct_benefits']
    indirect = medium_economic['indirect_benefits']
    
    economic_breakdown = []
    for key, value in direct.items():
        if key != 'total_direct':
            economic_breakdown.append({
                'カテゴリー': '直接便益',
                '項目': key,
                '金額 (百万円/年)': round(value / 1_000_000, 1)
            })
    
    for key, value in indirect.items():
        if key != 'total_indirect':
            economic_breakdown.append({
                'カテゴリー': '間接便益',
                '項目': key,
                '金額 (百万円/年)': round(value / 1_000_000, 1)
            })
    
    economic_df = pd.DataFrame(economic_breakdown)
    print(economic_df.to_string(index=False))
    
    # カーボン削減内訳
    print("\n3. カーボン・フットプリント削減内訳（中型シナリオ）")
    print("=" * 60)
    
    medium_carbon = comprehensive_results['medium']['carbon_footprint']
    carbon_breakdown = []
    
    for key, value in medium_carbon.items():
        if key != 'total_footprint_reduction':
            carbon_breakdown.append({
                '削減ソース': key,
                '削減量 (千tCO₂e/年)': round(value / 1_000, 1),
                '構成比 (%)': round(value / medium_carbon['total_footprint_reduction'] * 100, 1)
            })
    
    carbon_df = pd.DataFrame(carbon_breakdown)
    print(carbon_df.to_string(index=False))

def create_agrix_visualizations(comprehensive_results):
    """AGRIX Projectの可視化を作成"""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    scenarios = ['low', 'medium', 'high']
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    
    # 1. 総合経済効果
    economic_totals = [comprehensive_results[s]['economic_impact']['total_benefits']/1_000_000_000 for s in scenarios]
    direct_totals = [comprehensive_results[s]['economic_impact']['direct_benefits']['total_direct']/1_000_000_000 for s in scenarios]
    
    x = np.arange(len(scenarios))
    width = 0.35
    
    ax1.bar(x - width/2, direct_totals, width, label='直接便益', color=colors[0], alpha=0.8)
    ax1.bar(x + width/2, economic_totals, width, label='総合便益（直接+間接）', color=colors[1], alpha=0.8)
    ax1.set_xlabel('シナリオ')
    ax1.set_ylabel('経済効果 (十億円/年)')
    ax1.set_title('AGRIX Project 経済効果比較')
    ax1.set_xticks(x)
    ax1.set_xticklabels(['低', '中', '高'])
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. カーボン削減内訳（中型シナリオ）
    medium_carbon = comprehensive_results['medium']['carbon_footprint']
    carbon_sources = [k for k in medium_carbon.keys() if k != 'total_footprint_reduction']
    carbon_values = [medium_carbon[k]/1_000_000 for k in carbon_sources]
    
    ax2.pie(carbon_values, labels=carbon_sources, autopct='%1.1f%%', startangle=90)
    ax2.set_title('カーボン・フットプリント削減内訳\n（中型シナリオ）')
    
    # 3. 投資収益性分析
    roi_values = [comprehensive_results[s]['green_premium']['roi_percentage'] for s in scenarios]
    payback_values = [comprehensive_results[s]['green_premium']['payback_period'] for s in scenarios]
    
    ax3.bar(x, roi_values, color=colors, alpha=0.8)
    ax3.set_xlabel('シナリオ')
    ax3.set_ylabel('投資利益率 (%)')
    ax3.set_title('AGRIX Project 投資利益率 (ROI)')
    ax3.set_xticks(x)
    ax3.set_xticklabels(['低', '中', '高'])
    ax3.grid(True, alpha=0.3)
    
    # 4. グリーンプレミアム分析
    premium_ratios = [comprehensive_results[s]['green_premium']['green_premium_ratio']*100 for s in scenarios]
    net_savings = [comprehensive_results[s]['green_premium']['net_annual_savings']/1_000_000_000 for s in scenarios]
    
    ax4.bar(x - width/2, premium_ratios, width, label='グリーンプレミアム比率 (%)', color=colors[0], alpha=0.8)
    ax4.bar(x + width/2, net_savings, width, label='正味年間節約額 (十億円)', color=colors[1], alpha=0.8)
    ax4.set_xlabel('シナリオ')
    ax4.set_ylabel('比率 (%) / 金額 (十億円)')
    ax4.set_title('グリーンプレミアム分析')
    ax4.set_xticks(x)
    ax4.set_xticklabels(['低', '中', '高'])
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# 結果表示
display_agrix_results(comprehensive_results)
create_agrix_visualizations(comprehensive_results)

# 感度分析：炭素価格の影響
print("\n4. 炭素価格感度分析（中型シナリオ）")
print("=" * 50)

carbon_prices = [500, 1000, 1500, 2000, 2500, 3000]  # 円/tCO₂e
sensitivity_data = []

medium_data = comprehensive_results['medium']
base_waste_volume = medium_data['waste_volume']
base_carbon_reduction = medium_data['carbon_footprint']['total_footprint_reduction']

for carbon_price in carbon_prices:
    # 炭素クレジット収入を再計算
    carbon_credit_income = base_carbon_reduction * carbon_price
    
    # 経済効果を再計算（炭素クレジット収入のみ更新）
    base_economic = medium_data['economic_impact']['direct_benefits'].copy()
    base_economic['carbon_credits'] = carbon_credit_income
    base_economic['total_direct'] = sum([v for k, v in base_economic.items() if k != 'total_direct'])
    
    total_benefits = base_economic['total_direct'] + medium_data['economic_impact']['indirect_benefits']['total_indirect']
    
    # グリーンプレミアム再計算
    green_premium = agrix_analysis.calculate_green_premium(base_waste_volume, total_benefits)
    
    sensitivity_data.append({
        '炭素価格 (円/tCO₂e)': carbon_price,
        '炭素クレジット収入 (十億円/年)': round(carbon_credit_income / 1_000_000_000, 1),
        '投資利益率 (ROI)': f"{round(green_premium['roi_percentage'], 1)}%",
        '回収期間 (年)': round(green_premium['payback_period'], 1),
        'グリーンプレミアム比率': f"{round(green_premium['green_premium_ratio']*100, 1)}%"
    })

sensitivity_df = pd.DataFrame(sensitivity_data)
print(sensitivity_df.to_string(index=False))

---

はい、このコードは非常に完成度の高い**ケニア全土スケールアップ版 AGRIX Project の経済効果・カーボン削減・グリーンプレミアム算出シミュレーション**になっています。  
正しく動作させれば、以下の３つの主要指標をすべて出力・可視化できます。

---

## ✅ 1. 経済的効果（Economic Impact）

### 仕組み

`calculate_agrix_economic_impact()` 関数が、

- 廃棄物量（`waste_volume`）
    
- 温室効果ガス削減量（`ghg_reduction`）  
    を入力にして、以下の**直接便益**と**間接便益**を計算します。
    

### 主な指標：

|区分|内容|単位|
|---|---|---|
|肥料コスト削減|堆肥で化学肥料代替|円/年|
|水コスト削減|堆肥による保水性向上|円/年|
|収量増加便益|収量増加 × 作物価値|円/年|
|炭素クレジット収入|`ghg_reduction × 炭素価格`|円/年|
|廃棄物処理費削減|廃棄コスト回避|円/年|
|雇用創出価値|新規雇用数 × 年収|円/年|
|生物多様性価値|改善面積 × 価値係数|円/年|
|地域所得乗数効果|直接便益 × (2.3 − 1)|円/年|

➡ 合計で「**年あたりの総経済便益（Total Benefits）**」を算出します。  
結果は、シナリオごと（低・中・高）に十億円単位で出力されます。

---

## ✅ 2. カーボン・フットプリント削減（Carbon Footprint Reduction）

### 仕組み

`calculate_carbon_footprint_reduction()` 関数で、堆肥化・再生農地・家畜メタン削減などの多層的なGHG削減を集計しています。

### 主な構成要素：

|要素|説明|単位|
|---|---|---|
|廃棄物メタン回避|埋立処理からのCH₄削減|tCO₂e/年|
|炭素固定|堆肥中のC固定（×3.67）|tCO₂e/年|
|肥料製造回避|化学肥料製造由来CO₂削減|tCO₂e/年|
|家畜メタン削減|MBT飼料利用によるCH₄低減|tCO₂e/年|
|食品ロス削減|サプライチェーン最適化|tCO₂e/年|
|農地炭素蓄積|堆肥施用農地でのSOC増加|tCO₂e/年|
|輸送距離短縮|廃棄物流の短縮効果|tCO₂e/年|

➡ これらを合計し、**年間総削減量（total_footprint_reduction）** を算出。  
百万tCO₂e単位で可視化できます。

---

## ✅ 3. グリーン・プレミアム（Green Premium）

### 仕組み

`calculate_green_premium()` 関数が、

- 初期投資（建設・設備）
    
- O&Mコスト
    
- ベースラインコスト（従来廃棄物処理＋化学肥料費）
    
- 年間便益（上記経済効果）
    

を比較して、次の経済指標を出します。

|指標|説明|単位|
|---|---|---|
|投資額|waste_volume × 50,000円|円|
|年間O&Mコスト|投資額 × 15%|円|
|ベースラインコスト|廃棄処理＋肥料費|円|
|AGRIX年間コスト|投資/寿命 + O&M|円|
|正味年間節約額|年間便益 − AGRIXコスト|円|
|グリーンプレミアム比率|正味便益 / AGRIXコスト|%|
|ROI|総投資利益率|%|
|回収期間|投資額 / (年間便益−O&M)|年|

➡ 「ROI（投資利益率）」と「回収期間」で、投資の魅力度を判断可能。  
さらに炭素価格を500〜3000円/tCO₂eで変化させる**感度分析**も自動実行されます。

---

## ✅ 4. 出力内容（print結果）

1. **主要指標サマリー表**
    
    - 経済効果（十億円/年）
        
    - カーボン削減（百万tCO₂e/年）
        
    - ROI, Payback, Green Premium 比率
        
2. **詳細内訳表**
    
    - 直接・間接便益の各項目（百万円/年単位）
        
    - カーボン削減内訳（千tCO₂e単位）
        
3. **グラフ出力**
    
    - 経済効果比較バーグラフ
        
    - カーボン削減構成比（円グラフ）
        
    - ROI分析
        
    - グリーンプレミアム分析（比率・正味節約）
        
4. **炭素価格感度分析表**
    
    - 炭素価格ごとのROI・回収期間・プレミアム率
        

---

## ⚙️ 実行条件

ただしこのスクリプト単体では、

```python
kenya_simulation = KenyaMBTSimulation()
kenya_results = kenya_simulation.run_simulation()
```

の部分で、**`KenyaMBTSimulation`クラスが定義されていない**ため、  
別ファイルでこのクラスが実装されている必要があります（ナイロビ版などの既存モジュールを参照）。

このクラスが返す `kenya_results` の形式は：

```python
{
  'low': {'waste': {'total': X1}, 'ghg_reduction': {'total': Y1}},
  'medium': {'waste': {'total': X2}, 'ghg_reduction': {'total': Y2}},
  'high': {'waste': {'total': X3}, 'ghg_reduction': {'total': Y3}}
}
```

のような構造が必要です。

---

## ✅ 結論

はい、上記コードは **ケニア全土のAGRIX Projectにおける**

- 経済的効果（Economic Impact）
    
- カーボン・フットプリント削減（Carbon Reduction）
    
- グリーン・プレミアム（Green Premium）
    

を**全自動で算出・可視化できる設計**になっています。

---

ご希望があれば、次のいずれかを補完できます：

1. ✅ `KenyaMBTSimulation()` クラスの雛形を作成し、ナイロビの既存シミュレーション数値から連結する
    
2. ✅ 出力レポート（PPTX/PDF）として自動生成する
    
3. ✅ 炭素価格・肥料コスト・O&M率などをパラメータ化した**政策感度分析モデル**を追加
    

どの方向で補完しましょうか？