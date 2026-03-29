==このモデルによる、アパレル廃棄物の建材化や有機廃棄物のMBT55処理が、炭素隔離・廃棄物回避・肥料代替・収量増加を通じて温室効果ガス削減に直結することを数値化してください。

### Executive quantification of GHG reductions

以下は、アパレル廃棄物の建材化（1トン当たり）と、有機廃棄物のMBT55処理（1トン当たり）について、保守的・中間・楽観の3シナリオで定量化した結果です。仮定値は透明性のために明示し、式は英語版モデルに準拠しています。

---

## Apparel-to-building materials: per tonne textile

#### Key assumptions by scenario
- **Feedstock and product**
  - **Bio fraction:** 保守 0.50 / 中間 0.60 / 楽観 0.70
  - **C% in bio fraction:** 0.50（全シナリオ）
  - **Permanence factor (product life discount):** 保守 0.40 / 中間 0.60 / 楽観 0.80
  - **Displacement mix:** セメント 0.4 t + 木質パネル 0.3 t（保守）, 0.5 t + 0.3 t（中間）, 0.6 t + 0.4 t（楽観）
- **Baselines and process**
  - **BAU disposal shares:** 埋立 40% / 野焼き 60%（保守）, 50% / 50%（中間）, 30% / 70%（楽観）
  - **EFs:** セメント 0.70 tCO2e/t, 木質パネル 0.80 tCO2e/t, 埋立 0.50 tCO2e/t, 野焼き 1.50 tCO2e/t
  - **Process emissions:** 電力・熱・輸送合計 保守 0.20 / 中間 0.15 / 楽観 0.10 tCO2e/t
  - **End-of-life factor:** 保守 0.10 / 中間 0.05 / 楽観 0.00（高循環）

#### Equations
- Avoided virgin:
  \[
  \mathrm{AvoidedVirgin} = m_{\mathrm{cem}} \cdot 0.70 + m_{\mathrm{wood}} \cdot 0.80
  \]
- Avoided waste:
  \[
  \mathrm{AvoidedWaste} = 1.0 \cdot \left(f_{\mathrm{LF}} \cdot 0.50 + f_{\mathrm{OB}} \cdot 1.50\right)
  \]
- Stored carbon:
  \[
  \mathrm{StoredC} = \mathrm{BioFrac} \cdot 0.50 \cdot \frac{44}{12} \cdot \mathrm{Permanence}
  \]
- End-of-life:
  \[
  \mathrm{EOL} = \mathrm{BioFrac} \cdot 0.50 \cdot \frac{44}{12} \cdot \mathrm{EOLFactor}
  \]
- Net:
  \[
  \mathrm{GHG_{net}} = \mathrm{AvoidedVirgin} + \mathrm{AvoidedWaste} + \mathrm{StoredC} - \mathrm{Process} - \mathrm{EOL}
  \]

#### Results per tonne textile
| Scenario | Avoided virgin | Avoided waste | Stored C | Process | EOL | Net GHG reduction (tCO2e/t) |
|---|---:|---:|---:|---:|---:|---:|
| 保守 | 0.64 | 1.06 | 0.37 | 0.20 | 0.09 | 1.79 |
| 中間 | 0.71 | 1.00 | 0.55 | 0.15 | 0.05 | 2.06 |
| 楽観 | 0.88 | 1.20 | 0.86 | 0.10 | 0.00 | 2.84 |

> 計算例（中間のStored C）: \(0.60 \cdot 0.50 \cdot \frac{44}{12} \cdot 0.60 = 0.55\ \mathrm{tCO2e}\)

---

## MBT55: per tonne organic waste applied to soil

#### Key assumptions by scenario
- **Amendment properties**
  - **C%:** 保守 0.40 / 中間 0.45 / 楽観 0.50
  - **Stable fraction (humification):** 保守 0.30 / 中間 0.40 / 楽観 0.50
  - **Permanence discount (20–30年):** 保守 0.70 / 中間 0.80 / 楽観 0.90
- **BAU disposal avoided methane**
  - **EFBAU (stream-weighted):** 保守 0.40 / 中間 0.60 / 楽観 0.80 tCO2e/t
- **Fertilizer displacement (available nutrients per tonne)**
  - **Available N, P2O5, K2O:** 保守 8 / 4 / 6 kg, 中間 10 / 5 / 8 kg, 楽観 12 / 6 / 10 kg
  - **EFs (manufacturing):** N 6, P2O5 1.2, K2O 0.8 kgCO2e/kg
- **N2O reduction via NUE improvement**
  - **Field EF:** \(0.015\ \mathrm{kg\ N_2O\text{-}N/kg\ N}\), **NUE gain:** 保守 0.15 / 中間 0.25 / 楽観 0.35
  - 変換係数: \(\mathrm{N_2O\text{-}N} \to \mathrm{N_2O}\) は分子量比 \(44/28\)
- **Process and leakage**
  - **Process emissions:** 保守 0.08 / 中間 0.06 / 楽観 0.04 tCO2e/t
  - **Leakage (CH4/N2O/NH3):** 保守 0.05 / 中間 0.04 / 楽観 0.03 tCO2e/t

#### Equations
- Soil carbon:
  \[
  \mathrm{SoilC} = 1.0 \cdot \mathrm{C\%} \cdot \mathrm{Stable} \cdot \frac{44}{12} \cdot \mathrm{Permanence}
  \]
- Avoided CH4:
  \[
  \mathrm{AvoidedCH4} = \mathrm{EF_{BAU}}
  \]
- Fertilizer displacement:
  \[
  \mathrm{FD} = N \cdot 0.006 + P \cdot 0.0012 + K \cdot 0.0008\ \mathrm{tCO2e}
  \]
- N2O reduction:
  \[
  \mathrm{N_2O\;red} = N \cdot 0.015 \cdot \frac{44}{28} \cdot \mathrm{NUE\ gain}\ \mathrm{tCO2e}
  \]
- Net:
  \[
  \mathrm{GHG_{net}} = \mathrm{SoilC} + \mathrm{AvoidedCH4} + \mathrm{FD} + \mathrm{N_2O\;red} - \mathrm{Process} - \mathrm{Leakage}
  \]

#### Results per tonne organic waste
| Scenario | Soil C | Avoided CH4 | Fertilizer displacement | N2O reduction | Process | Leakage | Net GHG reduction (tCO2e/t) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 保守 | 0.31 | 0.40 | 0.07 | 0.01 | 0.08 | 0.05 | 0.66 |
| 中間 | 0.53 | 0.60 | 0.10 | 0.02 | 0.06 | 0.04 | 1.15 |
| 楽観 | 0.82 | 0.80 | 0.14 | 0.03 | 0.04 | 0.03 | 1.72 |

> 計算例（中間 Soil C）: \(0.45 \cdot 0.40 \cdot \frac{44}{12} \cdot 0.80 = 0.53\ \mathrm{tCO2e}\)  
> 計算例（中間 N2O）: \(10 \cdot 0.015 \cdot \frac{44}{28} \cdot 0.25 \approx 0.006\ \mathrm{tCO2e}\)

---

## Program-scale illustration

#### Example annual throughput
- **Textile to panels:** 50,000 t/年  
- **Organic waste MBT55:** 200,000 t/年

#### Aggregated reductions
| Stream | Throughput (t/yr) | Net reduction (tCO2e/t, mid) | Annual reduction (ktCO2e/yr) |
|---|---:|---:|---:|
| Textile-to-panel | 50,000 | 2.06 | 103 |
| MBT55 organics | 200,000 | 1.15 | 230 |
| Total | — | — | 333 |

---

## Notes for MRV readiness
- **Parameter localization:** 埋立/野焼き比率、素材EF、電力EF、栄養可給率は国・都市別に更新。  
- **Conservatism:** 永続性割引と寿命末期リスクを反映（上記は明示）。  
- **Instrumentation:** 質量フロー、エネルギー、堆肥ガス（CH4/N2O）計測、製品耐久試験、SOCトラッキング。  
- **Sensitivity bands:** 表の仮定値を地域データで校正し、範囲を再計算。  

---

必要なら、習志野市や千葉県のベースライン（電力排出係数、廃棄物処理比率、肥料投入実態）をいただければ、上記の数値をローカライズして、政策・投資提案用の確定値に仕上げます。