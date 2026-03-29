# Modeling greenhouse gas reductions for MBT55, MBT Sustainable Cycle, and AGRIX Project

## System boundaries and accounting principles

- **Scope definition:**  
  - **Upstream:** collection, preprocessing, transport.  
  - **Core process:** MBT55 conversion, composting/fermentation, engineered product manufacturing.  
  - **Downstream:** use-phase performance and durability, avoided emissions (landfill methane, open burning, virgin materials), end-of-life pathways.

- **Accounting lenses:**  
  - **Avoided emissions:** replacing high-GHG processes or materials.  
  - **Sequestration:** net stable carbon stored in soils or long-lived products.  
  - **Displacement:** reduced use of synthetic fertilizers and associated CO2, N2O, and energy.  
  - **Leakage controls:** transport, parasitic loads, fugitives, N loss from soils, end-of-life.

- **MRV essentials:**  
  - **Baselines:** country- and stream-specific BAU practices.  
  - **Data hierarchy:** primary operational data > representative regional EFs > conservative defaults.  
  - **Conservatism:** apply degradation and permanence discounts.

## Apparel waste to building materials: avoided emissions and stored carbon

### Core logic
Transforming post-consumer textiles (cotton/synthetics mixes) into durable building panels replaces virgin materials (e.g., cement, OSB/plywood, insulation) and avoids landfill/open burning. Emissions impacts come from three channels: avoided virgin production, avoided waste treatment, and net stored carbon in product.

#### Headline equation

$$
\mathrm{GHG_{net}} = \mathrm{AvoidedVirgin} + \mathrm{AvoidedWaste} + \mathrm{StoredC} - \mathrm{ProcessEmissions} - \mathrm{EndOfLifeEmissions}
$$


#### Components
- **Avoided virgin production**
  $$
  \mathrm{AvoidedVirgin} = \sum_i \left( \mathrm{Mass}_i \cdot \mathrm{EF}_{\mathrm{prod},i} \right)
  $$

- **Label:** $$(\mathrm{Mass}_i) is displaced material (i) per panel$$
- **Label:** $$(\mathrm{EF}_{\mathrm{prod},i}) is cradle-to-gate GHG per kg of material (i)$$

- **Avoided waste treatment**

$$
  \mathrm{AvoidedWaste} = \mathrm{Mass_{textile}} \cdot \left( f_{\mathrm{landfill}} \cdot \mathrm{EF}_{\mathrm{LF}} + f_{\mathrm{burn}} \cdot \mathrm{EF}_{\mathrm{OB}} \right)
  $$
- **Label:** $$(f_{\mathrm{landfill}}, f_{\mathrm{burn}}) are BAU shares$$
  - **Label:** 
  $$(\mathrm{EF}_{\mathrm{LF}}, \mathrm{EF}_{\mathrm{OB}}) are landfill/open burning EFs (include methane and incomplete combustion)$$

- **Stored carbon (product)**
  $$
  \mathrm{StoredC} = \mathrm{Mass_{bio\text{-}fraction}} \cdot \mathrm{C\%} \cdot \frac{44}{12} \cdot \mathrm{PermanenceFactor}
  $$
  - **Label:** Permanence factor discounts for product life and end-of-life fate

- **Process emissions**
  $$
  \mathrm{ProcessEmissions} = \mathrm{Electricity} \cdot \mathrm{EF_{grid}} + \mathrm{Thermal} \cdot \mathrm{EF_{fuel}} + \mathrm{Transport} \cdot \mathrm{EF_{t}}
  $$

- **End-of-life**
  $$
  \mathrm{EndOfLifeEmissions} = \mathrm{Mass_{bio\text{-}fraction}} \cdot \mathrm{C\%} \cdot \frac{44}{12} \cdot \left(1 - \mathrm{CircularityRate}\right) \cdot \mathrm{EOLFactor}
  $$

#### Minimal parameter table (set per country/project)

| Parameter | Meaning | Typical range |
|---|---|---|
| EFprod,cem | GHG per kg cement displaced | 0.5–0.9 kg CO2/kg |
| EFprod,wood | GHG per kg wood panel displaced | 0.2–1.2 kg CO2/kg |
| EFLF | Landfill EF for textiles (CH4 + CO2e) | 0.1–2.0 kg CO2e/kg |
| EFOB | Open burning EF | 1–3 kg CO2e/kg |
| C% | Carbon fraction of bio-textiles | 0.45–0.55 |
| PermanenceFactor | Product life × durability discount | 0.3–0.9 |
| EFgrid | Grid EF | 0.2–0.9 kg CO2e/kWh |
| CircularityRate | Share recovered at EOL | 0.2–0.9 |

> Sources: set with local LCA datasets; the table is a placeholder for your MRV library.

## Organic waste to soil carbon via MBT55: sequestration, methane avoidance, and fertilizer displacement

### Core logic
MBT55 converts diverse organic wastes into compost/humic/fermented inputs. Benefits include: soil carbon accrual; avoided methane from BAU disposal; reduced synthetic N/P/K production; suppressed \(\mathrm{N_2O}\) via improved nitrogen-use efficiency; yield lift raising biomass and future residues.

#### Headline equation
$$
\mathrm{GHG_{net}} = \mathrm{SoilC} + \mathrm{AvoidedCH4} + \mathrm{FertilizerDisplacement} + \mathrm{Yield\text{-}DrivenEffects} - \mathrm{ProcessEmissions} - \mathrm{Leakage}
$$

#### Components
- **Soil carbon accrual**
  $$
  \mathrm{SoilC} = \mathrm{Mass_{applied}} \cdot \mathrm{C\%} \cdot \mathrm{StableFraction} \cdot \frac{44}{12} \cdot \mathrm{PermanenceDiscount}
  $$
  - **Label:** StableFraction captures humification; permanence discounts for 20–30 year accounting

- **Avoided methane from BAU disposal**
  $$
  \mathrm{AvoidedCH4} = \sum_s \left( \mathrm{Mass}_s \cdot \mathrm{EF}_{\mathrm{BAU},s} \cdot \mathrm{CaptureDiscount}_s \right)
  $$
  - **Label:** Stream \(s\) (food waste, manure, sludge, marine residues, disaster debris)

- **Fertilizer displacement (manufacturing)**
  $$
  \mathrm{FertilizerDisplacement} = \sum_{x \in \{N,P,K\}} \left( \mathrm{NutrientAvailable}_x \cdot \mathrm{EF}_{\mathrm{prod},x} \right)
  $$
  - **Label:** NutrientAvailable accounts for mineralization and plant uptake

- **N2O suppression from improved NUE**
  $$
  \mathrm{N_2O\;reduction} = \left( \mathrm{N_{synthetic\;avoided}} \cdot \mathrm{EF}_{\mathrm{field\;N_2O}} \right) \cdot \mathrm{NUE\;GainFactor}
  $$

- **Yield-driven effects (biomass loop)**
  $$
  \mathrm{Yield\text{-}DrivenEffects} = \mathrm{YieldLift} \cdot \mathrm{ResidueFraction} \cdot \mathrm{C\%} \cdot \mathrm{StableFraction} \cdot \frac{44}{12}
  $$

- **Process emissions and leakage**
  $$
  \mathrm{ProcessEmissions} = \mathrm{Electricity} \cdot \mathrm{EF_{grid}} + \mathrm{Thermal} \cdot \mathrm{EF_{fuel}} + \mathrm{Transport} \cdot \mathrm{EF_t}
  $$
  $$
  \mathrm{Leakage} = \mathrm{FugitiveCH4\;compost} + \mathrm{NH_3\;loss} + \mathrm{N_2O\;compost}
  $$

#### Minimal parameter table (per stream and region)

| Parameter | Meaning | Typical range |
|---|---|---|
| C% (compost) | Carbon fraction of amendment | 0.35–0.55 |
| StableFraction | Share becoming stable humus | 0.2–0.6 |
| EFBAU,food | BAU disposal EF for food waste | 0.3–1.5 kg CO2e/kg |
| EFprod,N | GHG per kg synthetic N | 3–8 kg CO2e/kg N |
| EFprod,P | GHG per kg P2O5 | 0.5–2 kg CO2e/kg |
| EFprod,K | GHG per kg K2O | 0.5–1.5 kg CO2e/kg |
| EFfield N2O | Emissions per kg N applied | 0.01–0.02 kg N2O-N/kg N |
| NUE Gain | Fractional improvement of NUE | 0.1–0.4 |
| YieldLift | Fractional yield increase | 0.05–0.30 |
| ResidueFraction | Residues per unit yield | 0.4–1.0 |

> Again, plug in local values; these ranges are placeholders for sensitivity analysis.
> 
## Worked example templates you can drop into AGRIX

### Apparel-to-panel example (per tonne textile)
- **Assumptions**
  - **Label:** 1 tonne mixed textiles; 60% bio-based fraction; C% = 0.5; PermanenceFactor = 0.6  
  - **Label:** Displaces 0.5 t cement and 0.3 t OSB  
  - **Label:** BAU: 50% landfill, 50% open burning
- **Calculation**
  - **AvoidedVirgin:**  
    $$
    0.5 \cdot \mathrm{EFprod,cem} + 0.3 \cdot \mathrm{EFprod,wood}
    $$
  - **AvoidedWaste:**  
    $$
    1.0 \cdot \left(0.5 \cdot \mathrm{EFLF} + 0.5 \cdot \mathrm{EFOB}\right)
    $$
  - **StoredC:**  
    $$
    1.0 \cdot 0.6 \cdot 0.5 \cdot \frac{44}{12} \cdot 0.6
    $$
  - **Subtract Process & EOL:** project-specific
- **Output:** sensitivity curve with EF ranges and a conservative net figure.

### MBT55 soil carbon example (per tonne organic waste applied)
- **Assumptions**
  - **Label:** C% = 0.45; StableFraction = 0.4; PermanenceDiscount = 0.8  
  - **Label:** NutrientAvailable: 10 kg N, 5 kg P2O5, 8 kg K2O  
  - **Label:** BAU disposal EF (stream-weighted) = parameter
- **Calculation**
  - **SoilC:**  
    $$
    1.0 \cdot 0.45 \cdot 0.4 \cdot \frac{44}{12} \cdot 0.8
    $$
  - **AvoidedCH4:**  
    $$
    1.0 \cdot \mathrm{EF_{BAU}}
    $$
  - **FertilizerDisplacement:**  
    $$
    10 \cdot \mathrm{EF_{N}} + 5 \cdot \mathrm{EF_{P}} + 8 \cdot \mathrm{EF_{K}}
    $$
  - **N2O reduction:**  
    $$
    10 \cdot \mathrm{EF_{field\;N_2O}} \cdot \mathrm{NUE\;Gain}
    $$
  - **Yield loop:** plug crop-specific values  
  - **Subtract Process & Leakage:** measured

## ROI structure and MRV workflow

### ROI
- **Benefits**
  - **GHG credits:** $(\mathrm{Price_{CO2}} \cdot \mathrm{GHG_{net}})$$
  - **Fertilizer savings:** $(\sum_x \mathrm{NutrientAvailable}_x \cdot \mathrm{MarketPrice}_x)$$
  - **Yield uplift:** $(\mathrm{YieldLift} \cdot \mathrm{FarmGatePrice} \cdot \mathrm{Area})$$
  - **Waste tipping fee avoided:** $(\mathrm{Mass} \cdot \mathrm{Fee_{BAU}})$$
  - **Material displacement margin:** virgin vs. panel cost differential
- **Costs**
  - **Capex:** MBT55 units, preprocessing, panel line
  - **Opex:** energy, labor, maintenance, logistics, QA/MRV
  - **Compliance:** permits, EPR, certifications
- **Financial metric**
  $$
  \mathrm{ROI} = \frac{\mathrm{AnnualNetBenefits} - \mathrm{AnnualizedCosts}}{\mathrm{AnnualizedCosts}}
  $$
  Use IRR and NPV for multi-year projects with degradation and replacement cycles.

### MRV steps
- **Define baselines:** per stream and geography (landfill share, open burning prevalence, fertilizer practices, grid EF).  
- **Instrument data:** mass flows, energy meters, emissions sampling (CH4/N2O), soil carbon plots, product durability tests.  
- **Apply conservatism:** permanence discounts, leakage buffers, uncertainty intervals.  
- **Third-party verification:** protocol alignment (project-specific), traceability docs, serialized batch tracking.  
- **Publishable dashboards:** per-stream net GHG, per-tonne benefits, ROI, uncertainty bands.

## Strategic notes and risk controls

- **Disaster debris integration:** create a “surge mode” to absorb driftwood and sludge post-event with temporary logistics hubs; track distinct EFs and ensure contamination screening.  
- **Textile heterogeneity:** segregate synthetics vs. bio-based; ensure panel fire safety, VOC controls, and recyclability pathways to preserve permanence.  
- **Soil performance:** calibrate StableFraction and NUE gains by soil type and climate; maintain sentinel plots for multi-year SOC monitoring.  
- **Methane leakage:** enforce aerobic composting, forced aeration, and cover systems; quantify fugitives to keep credibility.  
- **Policy leverage:** align with EPR for textiles, municipal organics mandates, and regenerative agriculture programs to secure feedstock certainty and offtake.

---
