"""
MBT55 M³-BioSynergy Model & Element Transmutation Module

Based on: D1. M³-BioSynergy理論と元素転換モジュールの統合.md
"""

import networkx as nx
import numpy as np

class MBT55_Metabolic_Graph:
    """
    MBT55微生物群の代謝ネットワークとGHG削減シミュレーションを行うクラス
    """
    def __init__(self, species_count=120):
        self.G = nx.DiGraph()
        self.species_count = species_count
        
        # 機能群のインデックス定義 (仮定: 均等分布または主要機能群への割り当て)
        # 実際の実装ではメタゲノム解析データ等に基づき設定する
        self.methanotroph_idx = np.arange(0, 15)       # メタン酸化群
        self.denitrifier_idx = np.arange(15, 30)       # 脱窒菌群
        self.humus_forming_idx = np.arange(30, 70)     # 炭素固定群(腐植質生成)
        self.other_idx = np.arange(70, species_count)  # その他(元素転換群、発酵産生群など)
        
        # 相互作用行列の初期化 (ランダムな初期値、対角成分は自己相関)
        # a_ij: 種間相互作用（共生+/競合-）
        self.interaction_matrix = np.random.uniform(-0.05, 0.05, (species_count, species_count))
        np.fill_diagonal(self.interaction_matrix, 1.0)

        # ノード追加: 微生物種 + 代謝物 + 元素プール
        self.add_microbe_nodes()
        self.add_metabolite_nodes(['CO2', 'CH4', 'N2O', 'NH3', 'NO3', 'Humus'])
        self.add_element_pools(['C', 'N', 'P', 'Fe', 'Mn'])
        
        # エッジ: 代謝フローと相互作用
        self.add_metabolic_edges()
        self.add_interaction_edges()
    
    def add_microbe_nodes(self):
        for i in range(self.species_count):
            group = "other"
            if i in self.methanotroph_idx: group = "methanotroph"
            elif i in self.denitrifier_idx: group = "denitrifier"
            elif i in self.humus_forming_idx: group = "humus_former"
            
            self.G.add_node(f"microbe_{i}", type="microbe", group=group)

    def add_metabolite_nodes(self, metabolites):
        for m in metabolites:
            self.G.add_node(m, type="metabolite")

    def add_element_pools(self, elements):
        for e in elements:
            self.G.add_node(f"Pool_{e}", type="element_pool")

    def add_metabolic_edges(self):
        # メタン酸化群: CH4 -> CO2
        for i in self.methanotroph_idx:
            self.G.add_edge("CH4", f"microbe_{i}", type="consumption")
            self.G.add_edge(f"microbe_{i}", "CO2", type="production")
        
        # 脱窒菌群: NO3 -> N2O (還元) -> N2 (完全脱窒促進)
        for i in self.denitrifier_idx:
            self.G.add_edge("NO3", f"microbe_{i}", type="consumption")
            self.G.add_edge("N2O", f"microbe_{i}", type="reduction") # N2Oを消費/還元

        # 炭素固定群: 有機物 -> Humus
        for i in self.humus_forming_idx:
            self.G.add_edge(f"microbe_{i}", "Humus", type="sequestration")

    def add_interaction_edges(self):
        # 相互作用行列に基づいてエッジを追加 (閾値以上の相互作用のみ)
        rows, cols = np.where(np.abs(self.interaction_matrix) > 0.02)
        for r, c in zip(rows, cols):
            if r != c:
                self.G.add_edge(f"microbe_{c}", f"microbe_{r}", weight=self.interaction_matrix[r, c], type="interaction")
    
    def simulate_gas_reduction(self, intervention_vector):
        """
        MBT55介入によるGHG削減をシミュレーション
        intervention_vector: 各菌種への投入量/活性化係数 (numpy array or scalar)
        """
        if np.isscalar(intervention_vector):
            intervention_vector = np.full(self.species_count, intervention_vector)
            
        # 1. 微生物動態更新 (相互作用行列 x 介入ベクトル)
        population_change = self.interaction_matrix @ intervention_vector
        
        # 2. 代謝フロー計算
        co2_seq = self.calc_carbon_sequestration(population_change)
        ch4_oxid = self.calc_methane_oxidation(population_change)
        n2o_reduct = self.calc_n2o_reduction(population_change)
        
        # 3. GHG削減総量 (CO2換算)
        # GWP: CH4=25, N2O=298
        total_co2e = co2_seq + ch4_oxid * 25 + n2o_reduct * 298
        
        return {
            "total_co2e_reduction": total_co2e,
            "co2_sequestration": co2_seq,
            "ch4_oxidation": ch4_oxid,
            "n2o_reduction": n2o_reduct
        }

    def calc_carbon_sequestration(self, pop_vec):
        """炭素固定量の計算（腐植質生成含む）"""
        humification_rate = 0.35  # MBT腐植化係数
        # 負の個体数は0として扱う
        active_pop = np.maximum(0, pop_vec[self.humus_forming_idx])
        return np.sum(active_pop) * humification_rate

    def calc_methane_oxidation(self, pop_vec):
        """メタン酸化量計算"""
        methanotrophs = np.maximum(0, pop_vec[self.methanotroph_idx])
        oxidation_rate = 0.8  # 1菌体あたり酸化能力
        return np.sum(methanotrophs) * oxidation_rate

    def calc_n2o_reduction(self, pop_vec):
        """N₂O還元量計算"""
        denitrifiers = np.maximum(0, pop_vec[self.denitrifier_idx])
        reduction_rate = 0.7  # 脱窒菌によるN₂O→N₂変換効率
        return np.sum(denitrifiers) * reduction_rate * 0.82  # MBT効果係数

def logistic_growth(t, mu_max, K):
    """ロジスティック成長関数"""
    # P(t) = K / (1 + (K/P0 - 1) * exp(-mu_max * t)) の簡易形
    return K / (1.0 + np.exp(-mu_max * (t - 5)))

def ghg_dynamics(t, params):
    """時系列GHG削減シミュレーション"""
    # 微生物群の成長曲線
    growth = logistic_growth(t, params.get('mu_max', 0.5), params.get('K', 1.0))
    
    # 代謝活性曲線
    activity = params.get('alpha', 1.0) * np.exp(-params.get('beta', 0.1) * t)
    
    # GHG削減率の時間変化
    co2_seq_rate = params.get('co2_base', 1.0) * growth * activity
    ch4_oxid_rate = params.get('ch4_base', 1.0) * growth * (1 - np.exp(-t/params.get('tau', 10.0)))
    n2o_reduct_rate = params.get('n2o_base', 1.0) * growth
    
    return co2_seq_rate, ch4_oxid_rate, n2o_reduct_rate
