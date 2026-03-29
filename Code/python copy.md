import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple

class KenyaMBTSimulation:
    def __init__(self):
        # 基本パラメーターの設定
        self.setup_parameters()
        
    def setup_parameters(self):
        """シミュレーションで使用するパラメーターを設定"""
        
        # A. ベースライン・人口統計パラメーター
        self.params = {
            # 人口関連
            'nairobi_population': 4_400_000,  # ナイロビ人口
            'kenya_population': 56_000_000,   # ケニア全土人口
            'scale_factor_pop': 56/4.4,       # 人口スケール係数
            
            # 経済パラメーター
            'mbt_machine_cost': 5_000_000,    # MBT発酵機単価 [円/台]
            'treatment_cost_avoided': 3_000,  # 処理費回避単価 [円/トン]
            'compost_sale_price': 5_000,      # 堆肥販売単価 [円/トン]
            'carbon_credit_price': 1_500,     # 炭素クレジット単価 [円/tCO₂e]
            
            # 農業パラメーター
            'degraded_land_area': 14_000_000, # 劣化農地面積 [ha]
            
            # MBT性能パラメーター
            'compost_production_rate': 0.4,   # 堆肥生成率 [%]
            'methane_emission_factor': 0.06,  # メタン発生係数 [t CH₄/t廃棄物]
            'gwp_100': 25,                    # 地球温暖化係数 (100年)
            'carbon_sequestration_rate': 0.15, # 炭素固定率 [tC/t堆肥]
            'co2_conversion_factor': 3.67,    # CO2換算係数
            'fertilizer_replacement_rate': 0.05, # 肥料代替率 [t肥料/t堆肥]
            'fertilizer_production_co2': 5,   # 化学肥料製造CO2 [t CO₂/t肥料]
            'livestock_methane_reduction': 0.3, # 家畜メタン削減率 [%]
            'livestock_methane_emission': 0.07, # 家畜メタン排出量 [t CH₄/頭/年]
            'food_loss_avoidance_factor': 2.0, # 食品ロス回避排出係数 [t CO₂e/tロス]
            'biomass_increase_rate': 0.5,     # 修復農地バイオマス増加 [tC/ha/年]
        }
        
        # ナイロビ廃棄物量ベースライン [トン/年]
        self.nairobi_waste = {
            'food_waste': 365_000,
            'livestock_waste': 320_000,
            'agricultural_residue': 210_000,
            'sewage_sludge': 182_500,
            'processing_waste': 335_000,
            'total': 365_000 + 320_000 + 210_000 + 182_500 + 335_000
        }
        
        # ケニア全土スケールファクター（低・中・高シナリオ）
        self.scale_factors = {
            'low': {
                'food_waste': 10.0,      # 人口比より控えめ
                'livestock_waste': 3.0,
                'agricultural_residue': 10.0,
                'sewage_sludge': 6.0,
                'processing_waste': 4.0
            },
            'medium': {
                'food_waste': 12.7,      # 人口比
                'livestock_waste': 4.0,
                'agricultural_residue': 15.0,
                'sewage_sludge': 8.0,
                'processing_waste': 6.0
            },
            'high': {
                'food_waste': 15.0,      # 都市化進展想定
                'livestock_waste': 5.0,
                'agricultural_residue': 20.0,
                'sewage_sludge': 10.0,
                'processing_waste': 8.0
            }
        }
    
    def calculate_kenya_waste(self, scenario: str = 'medium') -> Dict:
        """ケニア全土の廃棄物量を計算"""
        factors = self.scale_factors[scenario]
        
        kenya_waste = {}
        for waste_type, nairobi_value in self.nairobi_waste.items():
            if waste_type == 'total':
                continue
            factor = factors[waste_type]
            kenya_waste[waste_type] = nairobi_value * factor
        
        kenya_waste['total'] = sum(kenya_waste.values())
        
        return kenya_waste
    
    def calculate_ghg_reduction(self, kenya_waste: Dict, scenario: str) -> Dict:
        """GHG削減効果を計算"""
        
        total_waste = kenya_waste['total']
        compost_produced = total_waste * self.params['compost_production_rate']
        
        # 各削減項目の計算
        reduction = {}
        
        # 1. 廃棄物処理回避によるメタン発生削減
        methane_avoided = total_waste * self.params['methane_emission_factor']
        reduction['waste_methane_avoidance'] = methane_avoided * self.params['gwp_100']
        
        # 2. 堆肥による炭素固定
        carbon_sequestered = compost_produced * self.params['carbon_sequestration_rate']
        reduction['carbon_sequestration'] = carbon_sequestered * self.params['co2_conversion_factor']
        
        # 3. 化学肥料削減
        fertilizer_replaced = compost_produced * self.params['fertilizer_replacement_rate']
        reduction['fertilizer_reduction'] = fertilizer_replaced * self.params['fertilizer_production_co2']
        
        # 4. 家畜メタン削減（家畜頭数はスケールファクターから推定）
        nairobi_livestock = 200_000  # ナイロビ推定20万頭
        scale_factor_livestock = self.scale_factors[scenario]['livestock_waste']
        kenya_livestock = nairobi_livestock * scale_factor_livestock
        
        livestock_methane_reduced = (kenya_livestock * 
                                   self.params['livestock_methane_emission'] * 
                                   self.params['livestock_methane_reduction'])
        reduction['livestock_methane_reduction'] = livestock_methane_reduced * self.params['gwp_100']
        
        # 5. 食品ロス削減効果
        food_waste_reduced = kenya_waste['food_waste'] * 0.5  # 50%削減想定
        reduction['food_loss_reduction'] = food_waste_reduced * self.params['food_loss_avoidance_factor']
        
        # 6. 農地修復によるバイオマス増加
        # 堆肥施用による農地修復面積を推定（堆肥10トン/ha/年で施用想定）
        land_rehabilitated = min(compost_produced / 10, self.params['degraded_land_area'])
        reduction['biomass_carbon'] = land_rehabilitated * self.params['biomass_increase_rate'] * self.params['co2_conversion_factor']
        
        # 総削減量
        reduction['total'] = sum(reduction.values())
        
        return reduction
    
    def calculate_economic_benefits(self, kenya_waste: Dict, ghg_reduction: Dict) -> Dict:
        """経済的便益を計算"""
        
        total_waste = kenya_waste['total']
        compost_produced = total_waste * self.params['compost_production_rate']
        
        benefits = {}
        
        # 収益項目
        benefits['treatment_cost_savings'] = total_waste * self.params['treatment_cost_avoided']
        benefits['compost_sales'] = compost_produced * self.params['compost_sale_price']
        benefits['carbon_credits'] = ghg_reduction['total'] * self.params['carbon_credit_price']
        
        # 総収益
        benefits['total_revenue'] = sum(benefits.values())
        
        # 投資コスト（MBT機導入台数）
        # 1台あたり処理能力：10,000トン/年想定
        mbt_units_needed = total_waste / 10_000
        benefits['investment_cost'] = mbt_units_needed * self.params['mbt_machine_cost']
        
        # 年間純利益
        benefits['annual_net_benefit'] = benefits['total_revenue'] - (benefits['investment_cost'] / 10)  # 10年償却
        
        return benefits
    
    def run_simulation(self):
        """全シナリオのシミュレーションを実行"""
        
        results = {}
        
        for scenario in ['low', 'medium', 'high']:
            # 廃棄物量計算
            kenya_waste = self.calculate_kenya_waste(scenario)
            
            # GHG削減効果計算
            ghg_reduction = self.calculate_ghg_reduction(kenya_waste, scenario)
            
            # 経済的便益計算
            economic_benefits = self.calculate_economic_benefits(kenya_waste, ghg_reduction)
            
            results[scenario] = {
                'waste': kenya_waste,
                'ghg_reduction': ghg_reduction,
                'economic_benefits': economic_benefits
            }
        
        self.results = results
        return results
    
    def generate_report(self):
        """詳細レポートを生成"""
        
        if not hasattr(self, 'results'):
            self.run_simulation()
        
        report = {}
        
        # 基本統計
        report['summary'] = self._create_summary_table()
        report['detailed_analysis'] = self._create_detailed_analysis()
        
        return report
    
    def _create_summary_table(self):
        """サマリーテーブル作成"""
        summary_data = []
        
        for scenario in ['low', 'medium', 'high']:
            result = self.results[scenario]
            waste_total = result['waste']['total'] / 1_000_000  # 百万トン
            ghg_total = result['ghg_reduction']['total'] / 1_000_000  # 百万tCO₂e
            revenue = result['economic_benefits']['total_revenue'] / 1_000_000_000  # 十億円
            net_benefit = result['economic_benefits']['annual_net_benefit'] / 1_000_000_000  # 十億円
            
            summary_data.append({
                'シナリオ': scenario,
                '廃棄物総量 (百万トン/年)': round(waste_total, 2),
                'GHG削減量 (百万tCO₂e/年)': round(ghg_total, 2),
                '総収益 (十億円/年)': round(revenue, 2),
                '年間純利益 (十億円/年)': round(net_benefit, 2)
            })
        
        return pd.DataFrame(summary_data)
    
    def _create_detailed_analysis(self):
        """詳細分析テーブル作成"""
        detailed_data = []
        
        for scenario in ['low', 'medium', 'high']:
            result = self.results[scenario]
            
            # 廃棄物内訳
            for waste_type, amount in result['waste'].items():
                if waste_type != 'total':
                    detailed_data.append({
                        'シナリオ': scenario,
                        'カテゴリー': '廃棄物',
                        '項目': waste_type,
                        '量 (千トン/年)': round(amount / 1_000, 1)
                    })
            
            # GHG削減内訳
            for reduction_type, amount in result['ghg_reduction'].items():
                if reduction_type != 'total':
                    detailed_data.append({
                        'シナリオ': scenario,
                        'カテゴリー': 'GHG削減',
                        '項目': reduction_type,
                        '量 (千tCO₂e/年)': round(amount / 1_000, 1)
                    })
        
        return pd.DataFrame(detailed_data)

# シミュレーションの実行と可視化
def run_comprehensive_simulation():
    """包括的なシミュレーションを実行"""
    
    # シミュレーションインスタンス作成
    simulator = KenyaMBTSimulation()
    
    # シミュレーション実行
    results = simulator.run_simulation()
    
    # レポート生成
    report = simulator.generate_report()
    
    return simulator, results, report

# シミュレーション実行
simulator, results, report = run_comprehensive_simulation()

# 結果の表示
print("=" * 60)
print("ケニア全土 MBT Sustainable Cycle シミュレーション結果")
print("=" * 60)

print("\n1. シナリオ別サマリー")
print("=" * 40)
print(report['summary'].to_string(index=False))

print("\n2. 詳細分析（中型シナリオ）")
print("=" * 40)
medium_details = report['detailed_analysis'][report['detailed_analysis']['シナリオ'] == 'medium']
print(medium_details.to_string(index=False))

# 可視化
def create_visualizations(simulator, results):
    """結果の可視化"""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. 廃棄物構成（中型シナリオ）
    medium_waste = results['medium']['waste']
    waste_types = [k for k in medium_waste.keys() if k != 'total']
    waste_values = [medium_waste[k] / 1_000_000 for k in waste_types]
    
    ax1.pie(waste_values, labels=waste_types, autopct='%1.1f%%', startangle=90)
    ax1.set_title('ケニア全土廃棄物構成（中型シナリオ）\n総量: {:.1f}百万トン/年'.format(medium_waste['total']/1_000_000))
    
    # 2. GHG削減内訳（中型シナリオ）
    medium_ghg = results['medium']['ghg_reduction']
    ghg_types = [k for k in medium_ghg.keys() if k != 'total']
    ghg_values = [medium_ghg[k] / 1_000_000 for k in ghg_types]
    
    ax2.barh(ghg_types, ghg_values)
    ax2.set_xlabel('GHG削減量 (百万tCO₂e/年)')
    ax2.set_title('GHG削減内訳（中型シナリオ）\n総量: {:.1f}百万tCO₂e/年'.format(medium_ghg['total']/1_000_000))
    
    # 3. シナリオ別比較
    scenarios = ['low', 'medium', 'high']
    waste_totals = [results[s]['waste']['total']/1_000_000 for s in scenarios]
    ghg_totals = [results[s]['ghg_reduction']['total']/1_000_000 for s in scenarios]
    
    x = np.arange(len(scenarios))
    width = 0.35
    
    ax3.bar(x - width/2, waste_totals, width, label='廃棄物総量', alpha=0.7)
    ax3.bar(x + width/2, ghg_totals, width, label='GHG削減量', alpha=0.7)
    ax3.set_xlabel('シナリオ')
    ax3.set_ylabel('百万トン / 百万tCO₂e')
    ax3.set_title('シナリオ別比較')
    ax3.set_xticks(x)
    ax3.set_xticklabels(['低', '中', '高'])
    ax3.legend()
    
    # 4. 経済的便益
    revenues = [results[s]['economic_benefits']['total_revenue']/1_000_000_000 for s in scenarios]
    net_benefits = [results[s]['economic_benefits']['annual_net_benefit']/1_000_000_000 for s in scenarios]
    
    ax4.bar(x - width/2, revenues, width, label='総収益', alpha=0.7)
    ax4.bar(x + width/2, net_benefits, width, label='年間純利益', alpha=0.7)
    ax4.set_xlabel('シナリオ')
    ax4.set_ylabel('十億円/年')
    ax4.set_title('経済的便益比較')
    ax4.set_xticks(x)
    ax4.set_xticklabels(['低', '中', '高'])
    ax4.legend()
    
    plt.tight_layout()
    plt.show()

# 可視化の実行
create_visualizations(simulator, results)

# 感度分析
print("\n3. グリーンプレミアム感度分析")
print("=" * 40)

# 炭素クレジット単価を変えたときの影響分析
carbon_prices = [500, 1000, 1500, 2000, 2500]  # 円/tCO₂e
scenario = 'medium'

sensitivity_results = []
for price in carbon_prices:
    # 元の価格を保存
    original_price = simulator.params['carbon_credit_price']
    
    # 新しい価格を設定
    simulator.params['carbon_credit_price'] = price
    
    # 再計算
    kenya_waste = simulator.calculate_kenya_waste(scenario)
    ghg_reduction = simulator.calculate_ghg_reduction(kenya_waste, scenario)
    economic_benefits = simulator.calculate_economic_benefits(kenya_waste, ghg_reduction)
    
    sensitivity_results.append({
        '炭素クレジット単価 (円/tCO₂e)': price,
        '年間純利益 (十億円)': round(economic_benefits['annual_net_benefit'] / 1_000_000_000, 2),
        '投資回収期間 (年)': round(economic_benefits['investment_cost'] / economic_benefits['annual_net_benefit'], 1) if economic_benefits['annual_net_benefit'] > 0 else float('inf')
    })
    
    # 元の価格に戻す
    simulator.params['carbon_credit_price'] = original_price

sensitivity_df = pd.DataFrame(sensitivity_results)
print(sensitivity_df.to_string(index=False))