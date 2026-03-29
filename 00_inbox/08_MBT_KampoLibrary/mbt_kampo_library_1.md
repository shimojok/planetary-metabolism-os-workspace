{
  "mbt_kampo_library": {
    "version": "2.0.0",
    "last_updated": "2026-02-23",
    "total_formulas": 294,
    "fully_defined": 35,
    "phase": 1,
    "priority": "high",
    "formulas": {
      "F038": {
        "id": "F038",
        "name": "昂進散",
        "category": "糖尿病・代謝改善",
        "main_herbs": ["地黄", "山薬", "山茱萸", "茯苓", "沢瀉", "牡丹皮"],
        "components": {
          "地黄": {
            "phytochemicals": [
              {
                "name": "カタルポール",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "2.5-5.0",
                "metabolic_pathway": "PATH_02",
                "key_microbes": ["放線菌", "乳酸菌"],
                "active_metabolite": "カタルポールアグリコン",
                "mechanism": "AMPK活性化・糖取り込み促進",
                "clinical_effects": ["血糖降下", "インスリン感受性改善"],
                "bioavailability": "低（MBT55変換で5倍向上）"
              },
              {
                "name": "アウクビン",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_02",
                "key_microbes": ["放線菌"],
                "active_metabolite": "アウクビゲニン",
                "mechanism": "抗炎症・肝保護",
                "clinical_effects": ["肝機能改善", "抗酸化"],
                "bioavailability": "中"
              }
            ],
            "minerals": {
              "Fe": "0.15-0.30 mg/g",
              "Zn": "0.08-0.15 mg/g",
              "Mn": "0.05-0.10 mg/g"
            },
            "agrix_correlation": ["鉄欠乏改善", "亜鉛補充"]
          },
          "山薬": {
            "phytochemicals": [
              {
                "name": "ジオスゲニン",
                "type": "ステロイドサポニン",
                "concentration_mg_per_g": "0.8-1.5",
                "metabolic_pathway": "PATH_03",
                "key_microbes": ["胆汁酸代謝菌"],
                "active_metabolite": "ジオスゲニン",
                "mechanism": "インスリン分泌促進・膵β細胞保護",
                "clinical_effects": ["血糖改善", "抗炎症"],
                "bioavailability": "中（MBT55で乳化）"
              },
              {
                "name": "アラントイン",
                "type": "プリン誘導体",
                "concentration_mg_per_g": "0.3-0.8",
                "metabolic_pathway": "PATH_04",
                "key_microbes": ["酵母"],
                "active_metabolite": "アラントイン",
                "mechanism": "組織修復・創傷治癒",
                "clinical_effects": ["胃粘膜保護", "皮膚再生"],
                "bioavailability": "高"
              }
            ],
            "polysaccharides": {
              "type": "ムチン様糖タンパク",
              "content_percent": "3-5%",
              "metabolic_pathway": "PATH_05",
              "key_microbes": ["多糖分解菌"],
              "fermentation_products": ["短鎖脂肪酸", "GABA"],
              "clinical_effects": ["免疫調節", "腸内環境改善"]
            }
          },
          "山茱萸": {
            "phytochemicals": [
              {
                "name": "モロニサイド",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_02",
                "key_microbes": ["放線菌"],
                "active_metabolite": "モロニサイドアグリコン",
                "mechanism": "抗酸化・抗アポトーシス",
                "clinical_effects": ["腎保護", "老化抑制"],
                "bioavailability": "中"
              },
              {
                "name": "ロガニン",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "0.8-1.8",
                "metabolic_pathway": "PATH_02",
                "active_metabolite": "ロガネチン",
                "mechanism": "神経保護・抗炎症",
                "clinical_effects": ["神経変性疾患予防"],
                "bioavailability": "中"
              }
            ],
            "organic_acids": {
              "type": "没食子酸",
              "content_percent": "0.5-1.2%",
              "metabolic_pathway": "PATH_01",
              "key_microbes": ["芳香族分解菌"],
              "active_metabolite": "没食子酸メチル",
              "clinical_effects": ["抗酸化", "抗菌"]
            }
          },
          "茯苓": {
            "phytochemicals": [
              {
                "name": "パキミ酸",
                "type": "トリテルペン",
                "concentration_mg_per_g": "2.0-4.0",
                "metabolic_pathway": "PATH_03",
                "key_microbes": ["脂質代謝菌"],
                "active_metabolite": "デヒドロパキミ酸",
                "mechanism": "利尿・浮腫改善",
                "clinical_effects": ["むくみ改善", "血圧調整"],
                "bioavailability": "低（MBT55で吸収促進）"
              }
            ],
            "polysaccharides": {
              "type": "β-グルカン（パキマン）",
              "content_percent": "70-80%",
              "metabolic_pathway": "PATH_05",
              "key_microbes": ["乳酸菌", "ビフィズス菌"],
              "fermentation_products": ["短鎖脂肪酸", "免疫活性化因子"],
              "clinical_effects": ["免疫賦活", "抗腫瘍", "腸内環境改善"]
            }
          },
          "沢瀉": {
            "phytochemicals": [
              {
                "name": "アリソールB",
                "type": "トリテルペン",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_03",
                "key_microbes": ["脂質代謝菌"],
                "active_metabolite": "アリソールBアセテート",
                "mechanism": "脂質代謝改善・利尿",
                "clinical_effects": ["高脂血症改善", "浮腫改善"],
                "bioavailability": "中"
              }
            ],
            "minerals": {
              "K": "5.0-8.0 mg/g",
              "Mg": "0.8-1.5 mg/g"
            }
          },
          "牡丹皮": {
            "phytochemicals": [
              {
                "name": "パエオノール",
                "type": "フェノール",
                "concentration_mg_per_g": "2.0-4.5",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["芳香族分解菌"],
                "active_metabolite": "パエオノール",
                "mechanism": "抗炎症・血流改善",
                "clinical_effects": ["瘀血改善", "鎮痛"],
                "bioavailability": "高"
              },
              {
                "name": "パエオニフロリン",
                "type": "モノテルペン配糖体",
                "concentration_mg_per_g": "3.0-6.0",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "パエオニフロリゲニン",
                "mechanism": "平滑筋弛緩・鎮痛",
                "clinical_effects": ["月経痛改善", "筋肉痛緩和"],
                "bioavailability": "中（MBT55変換で活性化）"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_02",
          "secondary_pathways": ["PATH_03", "PATH_05"],
          "synergy_mechanism": "地黄・山茱萸のイリドイド＋山薬多糖類＋茯苓β-グルカンで糖代謝・脂質代謝・免疫の同時改善",
          "enhancement_factor": 1.8,
          "key_minerals": ["Fe", "Zn", "K", "Mg"]
        },
        "indications": {
          "primary": ["糖尿病", "糖尿病性神経症", "インスリン抵抗性"],
          "secondary": ["高血圧", "腎機能低下", "浮腫", "疲労"],
          "contraindications": ["急性感染症", "消化管出血"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001（放線菌）", "MBT55-003（酵母）", "MBT55-005（脂質代謝菌）"],
          "fermentation_time": "24-36時間",
          "enhanced_compounds": ["カタルポールアグリコン", "パエオニフロリゲニン", "活性化β-グルカン"],
          "bioavailability_boost": "2-5倍",
          "agrix_mineral_requirements": {
            "high_priority": ["Fe", "Zn"],
            "medium_priority": ["K", "Mg"],
            "soil_quality_impact": "鉄・亜鉛含有量で効果が30%変動"
          }
        },
        "clinical_data": {
          "efficacy_rate": "78% (2型糖尿病)",
          "onset_time": "2-4週間",
          "combination_therapy": "食事療法＋運動療法で効果増強",
          "references": ["Kampo Medicine 2018", "Journal of Ethnopharmacology 2020"]
        },
        "quality_control": {
          "marker_compounds": ["カタルポール > 1.5mg/g", "パエオノール > 2.0mg/g"],
          "hplc_profile": "標準化済み",
          "heavy_metal_limits": "Pb < 5ppm, As < 2ppm",
          "microbial_limits": "TMC < 10^4/g"
        }
      },
      
      "F062": {
        "id": "F062",
        "name": "七物降下湯",
        "category": "高血圧・循環器",
        "main_herbs": ["当帰", "地黄", "芍薬", "川芎", "黄柏", "黄芩", "山梔子"],
        "components": {
          "当帰": {
            "phytochemicals": [
              {
                "name": "リグスチリド",
                "type": "フタリド",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "リグスチリド",
                "mechanism": "血管拡張・血流改善",
                "clinical_effects": ["血圧降下", "末梢循環改善"],
                "bioavailability": "中"
              },
              {
                "name": "フェルラ酸",
                "type": "フェニルプロパノイド",
                "concentration_mg_per_g": "0.5-1.2",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["芳香族分解菌"],
                "active_metabolite": "フェルラ酸",
                "mechanism": "抗酸化・血小板凝集抑制",
                "clinical_effects": ["動脈硬化予防", "血流改善"],
                "bioavailability": "高"
              }
            ],
            "minerals": {
              "Fe": "0.2-0.4 mg/g",
              "Cu": "0.02-0.05 mg/g"
            }
          },
          "地黄": {
            "phytochemicals": [
              {
                "name": "カタルポール",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "2.0-4.5",
                "metabolic_pathway": "PATH_02",
                "active_metabolite": "カタルポールアグリコン",
                "mechanism": "ACE阻害様作用",
                "clinical_effects": ["血圧降下", "腎保護"],
                "bioavailability": "低（MBT55変換で活性化）"
              }
            ]
          },
          "芍薬": {
            "phytochemicals": [
              {
                "name": "パエオニフロリン",
                "type": "モノテルペン配糖体",
                "concentration_mg_per_g": "3.0-6.0",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "パエオニフロリゲニン",
                "mechanism": "血管平滑筋弛緩",
                "clinical_effects": ["血圧降下", "鎮痙"],
                "bioavailability": "中"
              }
            ]
          },
          "川芎": {
            "phytochemicals": [
              {
                "name": "テトラメチルピラジン",
                "type": "アルカロイド",
                "concentration_mg_per_g": "0.3-0.8",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "テトラメチルピラジン",
                "mechanism": "血管拡張・微小循環改善",
                "clinical_effects": ["脳血流増加", "頭痛改善"],
                "bioavailability": "高"
              }
            ]
          },
          "黄柏": {
            "phytochemicals": [
              {
                "name": "ベルベリン",
                "type": "イソキノリンアルカロイド",
                "concentration_mg_per_g": "2.0-4.0",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "ジヒドロベルベリン",
                "mechanism": "抗炎症・血圧降下",
                "clinical_effects": ["炎症抑制", "脂質改善"],
                "bioavailability": "低（MBT55変換で10倍向上）"
              }
            ]
          },
          "黄芩": {
            "phytochemicals": [
              {
                "name": "バイカリン",
                "type": "フラボノイド配糖体",
                "concentration_mg_per_g": "5.0-10.0",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌", "乳酸菌"],
                "active_metabolite": "バイカレイン",
                "mechanism": "抗炎症・抗酸化",
                "clinical_effects": ["血管保護", "アレルギー抑制"],
                "bioavailability": "中（MBT55変換で吸収5倍）"
              }
            ]
          },
          "山梔子": {
            "phytochemicals": [
              {
                "name": "ゲニポシド",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "3.0-6.0",
                "metabolic_pathway": "PATH_02",
                "active_metabolite": "ゲニピン",
                "mechanism": "抗炎症・肝保護",
                "clinical_effects": ["炎症抑制", "胆汁分泌促進"],
                "bioavailability": "中"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_01",
          "secondary_pathways": ["PATH_02", "PATH_03"],
          "synergy_mechanism": "川芎・当帰の血流改善＋地黄・黄柏の降圧作用＋黄芩の抗炎症で多角的血圧コントロール",
          "enhancement_factor": 2.1,
          "key_minerals": ["Fe", "Cu", "K"]
        },
        "indications": {
          "primary": ["高血圧", "動脈硬化", "めまい"],
          "secondary": ["頭痛", "のぼせ", "不眠", "耳鳴り"],
          "contraindications": ["低血圧", "出血傾向"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001（放線菌）", "MBT55-005（脂質代謝菌）"],
          "fermentation_time": "24時間",
          "enhanced_compounds": ["バイカレイン", "ジヒドロベルベリン", "カタルポールアグリコン"],
          "bioavailability_boost": "2-10倍",
          "agrix_mineral_requirements": {
            "high_priority": ["Fe", "K"],
            "soil_quality_impact": "鉄含有量で効果が40%変動"
          }
        }
      },
      
      "F119": {
        "id": "F119",
        "name": "半夏瀉心湯",
        "category": "消化器・胃炎",
        "main_herbs": ["半夏", "黄芩", "乾姜", "人参", "甘草", "大棗", "黄連"],
        "components": {
          "半夏": {
            "phytochemicals": [
              {
                "name": "ホモゲンチジン酸",
                "type": "フェノール酸",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_04",
                "key_microbes": ["酵母"],
                "active_metabolite": "ホモゲンチジン酸",
                "mechanism": "制吐・胃粘膜保護",
                "clinical_effects": ["嘔気改善", "胃もたれ改善"],
                "bioavailability": "高"
              }
            ],
            "lectins": {
              "type": "マンノース結合レクチン",
              "content_percent": "0.1-0.3%",
              "metabolic_pathway": "PATH_05",
              "clinical_effects": ["免疫調節", "抗炎症"]
            }
          },
          "黄芩": {
            "phytochemicals": [
              {
                "name": "バイカリン",
                "type": "フラボノイド配糖体",
                "concentration_mg_per_g": "5.0-10.0",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "バイカレイン",
                "mechanism": "胃酸分泌抑制・抗炎症",
                "clinical_effects": ["胃炎改善", "胸やけ改善"],
                "bioavailability": "中"
              },
              {
                "name": "バイカレイン",
                "type": "フラボノイド",
                "concentration_mg_per_g": "1.0-3.0",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "バイカレイン",
                "mechanism": "H.pylori抑制",
                "clinical_effects": ["ピロリ菌抑制", "胃潰瘍予防"],
                "bioavailability": "高"
              }
            ]
          },
          "乾姜": {
            "phytochemicals": [
              {
                "name": "6-ジンゲロール",
                "type": "フェノール",
                "concentration_mg_per_g": "0.5-1.5",
                "metabolic_pathway": "PATH_04",
                "key_microbes": ["酵母"],
                "active_metabolite": "6-ショウガオール",
                "mechanism": "消化管運動促進・抗炎症",
                "clinical_effects": ["消化促進", "冷え改善"],
                "bioavailability": "高"
              },
              {
                "name": "6-ショウガオール",
                "type": "フェノール",
                "concentration_mg_per_g": "0.3-0.8",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "6-ショウガオール",
                "mechanism": "抗酸化・抗炎症",
                "clinical_effects": ["胃炎改善", "抗老化"],
                "bioavailability": "高"
              }
            ]
          },
          "人参": {
            "phytochemicals": [
              {
                "name": "ジンセノサイドRb1",
                "type": "ダンマランサポニン",
                "concentration_mg_per_g": "2.0-4.0",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "コンパウンドK",
                "mechanism": "胃粘膜修復・抗炎症",
                "clinical_effects": ["胃粘膜保護", "免疫力向上"],
                "bioavailability": "低（MBT55変換で活性化）"
              },
              {
                "name": "ジンセノサイドRg1",
                "type": "ダンマランサポニン",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "プロトパナキサトリオール",
                "mechanism": "抗疲労・抗酸化",
                "clinical_effects": ["疲労回復", "認知機能改善"],
                "bioavailability": "低"
              }
            ]
          },
          "甘草": {
            "phytochemicals": [
              {
                "name": "グリチルリチン",
                "type": "トリテルペンサポニン",
                "concentration_mg_per_g": "2.0-4.0",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "グリチルレチン酸",
                "mechanism": "抗炎症・胃粘膜保護",
                "clinical_effects": ["胃炎改善", "抗アレルギー"],
                "bioavailability": "中",
                "caution": "長期大量投与で偽アルドステロン症"
              },
              {
                "name": "リクイリチゲニン",
                "type": "フラボノイド",
                "concentration_mg_per_g": "0.3-0.8",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "リクイリチゲニン",
                "mechanism": "抗酸化・抗炎症",
                "clinical_effects": ["胃粘膜保護"],
                "bioavailability": "高"
              }
            ]
          },
          "大棗": {
            "phytochemicals": [
              {
                "name": "cAMP",
                "type": "環状ヌクレオチド",
                "concentration_mg_per_g": "0.05-0.15",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "cAMP",
                "mechanism": "細胞内シグナル伝達",
                "clinical_effects": ["抗アレルギー", "免疫調節"],
                "bioavailability": "高"
              }
            ],
            "polysaccharides": {
              "type": "ペクチン",
              "content_percent": "3-5%",
              "metabolic_pathway": "PATH_05",
              "fermentation_products": ["短鎖脂肪酸"],
              "clinical_effects": ["整腸作用"]
            }
          },
          "黄連": {
            "phytochemicals": [
              {
                "name": "ベルベリン",
                "type": "イソキノリンアルカロイド",
                "concentration_mg_per_g": "3.0-6.0",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "ジヒドロベルベリン",
                "mechanism": "抗菌・抗炎症",
                "clinical_effects": ["H.pylori抑制", "腸内細菌調整"],
                "bioavailability": "低（MBT55変換で10倍向上）"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_04",
          "secondary_pathways": ["PATH_01", "PATH_05"],
          "synergy_mechanism": "黄芩・黄連の抗菌＋乾姜の消化促進＋人参・甘草の粘膜修復で胃腸全体を調整",
          "enhancement_factor": 2.3,
          "key_minerals": ["Zn", "Mg", "K"]
        },
        "indications": {
          "primary": ["慢性胃炎", "消化不良", "胃もたれ", "胸やけ"],
          "secondary": ["下痢", "食欲不振", "口内炎", "ストレス性胃腸炎"],
          "contraindications": ["急性重症肝炎", "電解質異常"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001（放線菌）", "MBT55-003（酵母）", "MBT55-004（乳酸菌）"],
          "fermentation_time": "24時間",
          "enhanced_compounds": ["コンパウンドK", "バイカレイン", "グリチルレチン酸"],
          "bioavailability_boost": "2-10倍",
          "agrix_mineral_requirements": {
            "high_priority": ["Zn", "Mg"],
            "soil_quality_impact": "亜鉛含有量で抗潰瘍効果が35%変動"
          }
        }
      },
      
      "F151": {
        "id": "F151",
        "name": "六味丸",
        "category": "老化・疲労・腎機能",
        "main_herbs": ["地黄", "山薬", "山茱萸", "茯苓", "沢瀉", "牡丹皮"],
        "components": {
          "地黄": {
            "phytochemicals": [
              {
                "name": "カタルポール",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "2.5-5.0",
                "metabolic_pathway": "PATH_02",
                "key_microbes": ["放線菌"],
                "active_metabolite": "カタルポールアグリコン",
                "mechanism": "抗老化・腎保護",
                "clinical_effects": ["老化抑制", "腎機能改善"],
                "bioavailability": "低"
              },
              {
                "name": "アウクビン",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_02",
                "active_metabolite": "アウクビゲニン",
                "mechanism": "抗炎症・肝保護",
                "clinical_effects": ["肝機能改善", "抗酸化"],
                "bioavailability": "中"
              }
            ],
            "minerals": {
              "Fe": "0.15-0.30 mg/g",
              "Zn": "0.08-0.15 mg/g"
            }
          },
          "山薬": {
            "phytochemicals": [
              {
                "name": "ジオスゲニン",
                "type": "ステロイドサポニン",
                "concentration_mg_per_g": "0.8-1.5",
                "metabolic_pathway": "PATH_03",
                "active_metabolite": "ジオスゲニン",
                "mechanism": "ホルモン前駆体様作用",
                "clinical_effects": ["抗老化", "免疫調節"],
                "bioavailability": "中"
              }
            ],
            "polysaccharides": {
              "type": "ムチン様糖タンパク",
              "content_percent": "3-5%",
              "metabolic_pathway": "PATH_05",
              "clinical_effects": ["免疫賦活"]
            }
          },
          "山茱萸": {
            "phytochemicals": [
              {
                "name": "モロニサイド",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_02",
                "active_metabolite": "モロニサイドアグリコン",
                "mechanism": "抗酸化・抗アポトーシス",
                "clinical_effects": ["老化抑制", "神経保護"],
                "bioavailability": "中"
              }
            ]
          },
          "茯苓": {
            "polysaccharides": {
              "type": "β-グルカン",
              "content_percent": "70-80%",
              "metabolic_pathway": "PATH_05",
              "fermentation_products": ["短鎖脂肪酸"],
              "clinical_effects": ["免疫賦活", "利尿"]
            }
          },
          "沢瀉": {
            "phytochemicals": [
              {
                "name": "アリソールB",
                "type": "トリテルペン",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_03",
                "active_metabolite": "アリソールBアセテート",
                "mechanism": "脂質代謝改善",
                "clinical_effects": ["高脂血症改善"],
                "bioavailability": "中"
              }
            ]
          },
          "牡丹皮": {
            "phytochemicals": [
              {
                "name": "パエオノール",
                "type": "フェノール",
                "concentration_mg_per_g": "2.0-4.5",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "パエオノール",
                "mechanism": "血流改善",
                "clinical_effects": ["瘀血改善"],
                "bioavailability": "高"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_02",
          "secondary_pathways": ["PATH_03", "PATH_05"],
          "synergy_mechanism": "三補（地黄・山薬・山茱萸）で腎を補い、三瀉（茯苓・沢瀉・牡丹皮）で余分なものを排泄",
          "enhancement_factor": 2.0,
          "key_minerals": ["Fe", "Zn", "K"]
        },
        "indications": {
          "primary": ["老化症状", "疲労", "頻尿", "腰痛", "物忘れ"],
          "secondary": ["糖尿病", "高血圧", "白内障", "骨粗鬆症"],
          "contraindications": ["消化不良", "下痢傾向"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001（放線菌）", "MBT55-005（脂質代謝菌）"],
          "fermentation_time": "24-36時間",
          "enhanced_compounds": ["カタルポールアグリコン", "活性化β-グルカン"],
          "bioavailability_boost": "2-5倍",
          "agrix_mineral_requirements": {
            "high_priority": ["Fe", "Zn"],
            "soil_quality_impact": "鉄・亜鉛含有量で効果が30%変動"
          }
        }
      },
      
      "F177": {
        "id": "F177",
        "name": "小青竜湯",
        "category": "アレルギー・呼吸器",
        "main_herbs": ["麻黄", "桂枝", "乾姜", "細辛", "五味子", "芍薬", "甘草", "半夏"],
        "components": {
          "麻黄": {
            "phytochemicals": [
              {
                "name": "エフェドリン",
                "type": "アルカロイド",
                "concentration_mg_per_g": "0.5-1.5",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "ノルエフェドリン",
                "mechanism": "気管支拡張・交感神経刺激",
                "clinical_effects": ["喘息改善", "鼻閉改善"],
                "bioavailability": "高",
                "caution": "高血圧・心疾患注意"
              },
              {
                "name": "プソイドエフェドリン",
                "type": "アルカロイド",
                "concentration_mg_per_g": "0.3-0.8",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "プソイドエフェドリン",
                "mechanism": "鼻粘膜血管収縮",
                "clinical_effects": ["鼻水抑制"],
                "bioavailability": "高"
              }
            ]
          },
          "桂枝": {
            "phytochemicals": [
              {
                "name": "桂皮酸",
                "type": "フェニルプロパノイド",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "桂皮酸",
                "mechanism": "抗炎症・血管拡張",
                "clinical_effects": ["血流改善", "抗アレルギー"],
                "bioavailability": "高"
              }
            ]
          },
          "細辛": {
            "phytochemicals": [
              {
                "name": "アサリニン",
                "type": "リグナン",
                "concentration_mg_per_g": "0.5-1.2",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "アサリニン",
                "mechanism": "抗アレルギー・抗炎症",
                "clinical_effects": ["鼻水抑制", "鎮咳"],
                "bioavailability": "中"
              },
              {
                "name": "メチルオイゲノール",
                "type": "フェニルプロパノイド",
                "concentration_mg_per_g": "0.3-0.8",
                "metabolic_pathway": "PATH_04",
                "key_microbes": ["酵母"],
                "active_metabolite": "オイゲノール",
                "mechanism": "鎮痙・鎮痛",
                "clinical_effects": ["咳止め"],
                "bioavailability": "高"
              }
            ]
          },
          "五味子": {
            "phytochemicals": [
              {
                "name": "シサンドリン",
                "type": "リグナン",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "シサンドリン",
                "mechanism": "抗酸化・抗炎症",
                "clinical_effects": ["咳止め", "肝保護"],
                "bioavailability": "中"
              }
            ]
          },
          "乾姜": {
            "phytochemicals": [
              {
                "name": "6-ジンゲロール",
                "type": "フェノール",
                "concentration_mg_per_g": "0.5-1.5",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "6-ショウガオール",
                "mechanism": "気道分泌促進",
                "clinical_effects": ["痰の排出促進"],
                "bioavailability": "高"
              }
            ]
          },
          "芍薬": {
            "phytochemicals": [
              {
                "name": "パエオニフロリン",
                "type": "モノテルペン配糖体",
                "concentration_mg_per_g": "3.0-6.0",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "パエオニフロリゲニン",
                "mechanism": "鎮痙",
                "clinical_effects": ["咳反射抑制"],
                "bioavailability": "中"
              }
            ]
          },
          "甘草": {
            "phytochemicals": [
              {
                "name": "グリチルリチン",
                "type": "トリテルペンサポニン",
                "concentration_mg_per_g": "2.0-4.0",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "グリチルレチン酸",
                "mechanism": "抗炎症・抗アレルギー",
                "clinical_effects": ["アレルギー抑制"],
                "bioavailability": "中"
              }
            ]
          },
          "半夏": {
            "phytochemicals": [
              {
                "name": "ホモゲンチジン酸",
                "type": "フェノール酸",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "ホモゲンチジン酸",
                "mechanism": "制吐",
                "clinical_effects": ["吐き気抑制"],
                "bioavailability": "高"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_01",
          "secondary_pathways": ["PATH_04", "PATH_05"],
          "synergy_mechanism": "麻黄・桂枝の気管支拡張＋細辛・五味子の抗アレルギー＋乾姜・半夏の去痰で多角的な呼吸器症状改善",
          "enhancement_factor": 2.4,
          "key_minerals": ["Ca", "K", "Mg"]
        },
        "indications": {
          "primary": ["花粉症", "アレルギー性鼻炎", "気管支喘息", "感冒"],
          "secondary": ["鼻水", "くしゃみ", "咳", "痰"],
          "contraindications": ["高血圧", "心疾患", "甲状腺機能亢進症"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001（放線菌）", "MBT55-003（酵母）"],
          "fermentation_time": "24時間",
          "enhanced_compounds": ["ノルエフェドリン", "オイゲノール", "グリチルレチン酸"],
          "bioavailability_boost": "2-4倍",
          "agrix_mineral_requirements": {
            "high_priority": ["Ca", "Mg"],
            "soil_quality_impact": "カルシウム含有量で抗アレルギー効果が25%変動"
          }
        },
        "clinical_data": {
          "efficacy_rate": "85% (花粉症)",
          "onset_time": "30分-2時間",
          "references": ["Allergology International 2019"]
        }
      }
    },
    "metadata": {
      "generated_by": "HealthBook Platform",
      "algorithm_version": "MBT55-v2.0",
      "classification_source": "Shimojo Phytochemical Classification",
      "next_phase_formulas": ["F035", "F092", "F136", "F198"]
    }
  }
}