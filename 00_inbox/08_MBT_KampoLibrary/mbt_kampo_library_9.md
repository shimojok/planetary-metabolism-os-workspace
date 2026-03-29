{
  "mbt_kampo_library": {
    "version": "2.8.0",
    "last_updated": "2026-02-24",
    "total_formulas": 294,
    "fully_defined": 41,
    "phase": 9,
    "priority": "medium",
    "formulas": {
      "F035": {
        "id": "F035",
        "name": "桂枝茯苓丸",
        "category": "婦人科・血行改善",
        "main_herbs": ["桂枝", "茯苓", "牡丹皮", "桃仁", "芍薬"],
        "components": {
          "桂枝": {
            "phytochemicals": [
              {
                "name": "桂皮酸",
                "type": "フェニルプロパノイド",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "桂皮酸",
                "mechanism": "血管拡張",
                "clinical_effects": ["冷え改善", "血流促進"],
                "bioavailability": "高"
              }
            ]
          },
          "茯苓": {
            "polysaccharides": {
              "type": "β-グルカン",
              "content_percent": "70-80%",
              "metabolic_pathway": "PATH_05",
              "fermentation_products": ["短鎖脂肪酸"],
              "clinical_effects": ["免疫調整", "利尿"]
            }
          },
          "牡丹皮": {
            "phytochemicals": [
              {
                "name": "パエオノール",
                "type": "フェノール",
                "concentration_mg_per_g": "2.0-4.5",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "パエオノール",
                "mechanism": "血小板凝集抑制",
                "clinical_effects": ["瘀血改善", "月経痛改善"],
                "bioavailability": "高"
              }
            ]
          },
          "桃仁": {
            "phytochemicals": [
              {
                "name": "アミグダリン",
                "type": "シアノゲニック配糖体",
                "concentration_mg_per_g": "3.0-6.0",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "ベンズアルデヒド",
                "mechanism": "血管拡張",
                "clinical_effects": ["血流改善", "月経痛緩和"],
                "bioavailability": "低"
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
                "clinical_effects": ["月経痛改善"],
                "bioavailability": "中"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_01",
          "secondary_pathways": ["PATH_05"],
          "synergy_mechanism": "桂枝・牡丹皮の血流改善＋桃仁の血管拡張＋芍薬の鎮痙で「瘀血」を改善",
          "enhancement_factor": 2.2,
          "key_minerals": ["Fe", "Zn"]
        },
        "indications": {
          "primary": ["月経不順", "月経困難症", "子宮筋腫", "冷え症"],
          "secondary": ["肩こり", "更年期障害", "痔疾"],
          "contraindications": ["妊娠中", "出血性疾患"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001", "MBT55-005"],
          "fermentation_time": "24時間",
          "enhanced_compounds": ["パエオノール", "活性化アミグダリン"],
          "bioavailability_boost": "2-5倍"
        }
      },
      
      "F092": {
        "id": "F092",
        "name": "知柏地黄丸",
        "category": "更年期・ほてり",
        "main_herbs": ["知母", "黄柏", "地黄", "山薬", "山茱萸", "茯苓", "沢瀉", "牡丹皮"],
        "components": {
          "知母": {
            "phytochemicals": [
              {
                "name": "チモサポニン",
                "type": "ステロイドサポニン",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_03",
                "key_microbes": ["放線菌"],
                "active_metabolite": "サルササポゲニン",
                "mechanism": "抗炎症・解熱",
                "clinical_effects": ["ほてり改善", "炎症抑制"],
                "bioavailability": "低"
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
                "active_metabolite": "ジヒドロベルベリン",
                "mechanism": "抗炎症",
                "clinical_effects": ["炎症抑制"],
                "bioavailability": "低"
              }
            ]
          },
          "地黄": {
            "phytochemicals": [
              {
                "name": "カタルポール",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "2.5-5.0",
                "metabolic_pathway": "PATH_02",
                "active_metabolite": "カタルポールアグリコン",
                "mechanism": "ホルモンバランス調整",
                "clinical_effects": ["更年期症状改善"],
                "bioavailability": "低"
              }
            ]
          },
          "山薬": {
            "phytochemicals": [
              {
                "name": "ジオスゲニン",
                "type": "ステロイドサポニン",
                "concentration_mg_per_g": "0.8-1.5",
                "metabolic_pathway": "PATH_03",
                "active_metabolite": "ジオスゲニン",
                "mechanism": "ホルモン前駆体",
                "clinical_effects": ["ホルモンバランス改善"],
                "bioavailability": "中"
              }
            ]
          },
          "山茱萸": {
            "phytochemicals": [
              {
                "name": "モロニサイド",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_02",
                "active_metabolite": "モロニサイドアグリコン",
                "mechanism": "抗酸化",
                "clinical_effects": ["老化抑制"],
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
              "clinical_effects": ["免疫調整"]
            }
          },
          "沢瀉": {
            "phytochemicals": [
              {
                "name": "アリソールB",
                "type": "トリテルペン",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_03",
                "active_metabolite": "アリソールB",
                "mechanism": "利尿",
                "clinical_effects": ["浮腫改善"],
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
                "clinical_effects": ["ほてり改善"],
                "bioavailability": "高"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_02",
          "secondary_pathways": ["PATH_01", "PATH_03"],
          "synergy_mechanism": "知母・黄柏の「陰の熱」を取り、六味丸の基盤で「腎」を補う",
          "enhancement_factor": 2.3,
          "key_minerals": ["Mg", "Fe", "Zn"]
        },
        "indications": {
          "primary": ["更年期障害", "ほてり", "のぼせ", "発汗"],
          "secondary": ["不眠", "イライラ", "頻尿"],
          "contraindications": ["冷え症", "消化不良"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001", "MBT55-002", "MBT55-005"],
          "fermentation_time": "24-36時間",
          "enhanced_compounds": ["サルササポゲニン", "ジヒドロベルベリン", "カタルポールアグリコン"],
          "bioavailability_boost": "3-10倍"
        }
      },
      
      "F136": {
        "id": "F136",
        "name": "明朗散",
        "category": "眼精疲労・視力",
        "main_herbs": ["地黄", "当帰", "芍薬", "川芎", "防風", "羌活", "白芷", "藁本"],
        "components": {
          "地黄": {
            "phytochemicals": [
              {
                "name": "カタルポール",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "2.5-5.0",
                "metabolic_pathway": "PATH_02",
                "active_metabolite": "カタルポールアグリコン",
                "mechanism": "抗酸化",
                "clinical_effects": ["視神経保護"],
                "bioavailability": "低"
              }
            ]
          },
          "当帰": {
            "phytochemicals": [
              {
                "name": "リグスチリド",
                "type": "フタリド",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "リグスチリド",
                "mechanism": "血流改善",
                "clinical_effects": ["眼血流改善"],
                "bioavailability": "中"
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
                "clinical_effects": ["眼精疲労緩和"],
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
                "mechanism": "微小循環改善",
                "clinical_effects": ["眼血流増加"],
                "bioavailability": "高"
              }
            ]
          },
          "防風": {
            "phytochemicals": [
              {
                "name": "クロモン類",
                "type": "クロモン",
                "concentration_mg_per_g": "0.5-1.5",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "クロモン",
                "mechanism": "抗炎症",
                "clinical_effects": ["眼の炎症抑制"],
                "bioavailability": "中"
              }
            ]
          },
          "羌活": {
            "phytochemicals": [
              {
                "name": "ノトプテロール",
                "type": "クマリン",
                "concentration_mg_per_g": "0.3-0.8",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "ノトプテロール",
                "mechanism": "鎮痛",
                "clinical_effects": ["眼痛緩和"],
                "bioavailability": "中"
              }
            ]
          },
          "白芷": {
            "phytochemicals": [
              {
                "name": "ビアクアンゲリコール",
                "type": "クマリン",
                "concentration_mg_per_g": "0.5-1.2",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "ビアクアンゲリコール",
                "mechanism": "鎮痛",
                "clinical_effects": ["眼部不快感改善"],
                "bioavailability": "中"
              }
            ]
          },
          "藁本": {
            "phytochemicals": [
              {
                "name": "テトラヒドロフロクマリン",
                "type": "クマリン",
                "concentration_mg_per_g": "0.3-0.8",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "テトラヒドロフロクマリン",
                "mechanism": "鎮痛",
                "clinical_effects": ["頭痛改善"],
                "bioavailability": "中"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_01",
          "secondary_pathways": ["PATH_02", "PATH_04"],
          "synergy_mechanism": "四物湯で血を補い、防風・羌活・白芷・藁本で頭頸部の循環を改善",
          "enhancement_factor": 1.9,
          "key_minerals": ["Fe", "Zn"]
        },
        "indications": {
          "primary": ["眼精疲労", "かすみ目", "眼痛"],
          "secondary": ["肩こり", "頭痛", "ドライアイ"],
          "contraindications": ["急性炎症"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001", "MBT55-003", "MBT55-004"],
          "fermentation_time": "24時間",
          "enhanced_compounds": ["カタルポールアグリコン", "テトラメチルピラジン", "活性化クマリン"],
          "bioavailability_boost": "2-4倍"
        }
      },
      
      "F198": {
        "id": "F198",
        "name": "抑肝散",
        "category": "神経・精神症状",
        "main_herbs": ["釣藤鈎", "当帰", "川芎", "茯苓", "白朮", "柴胡", "甘草"],
        "components": {
          "釣藤鈎": {
            "phytochemicals": [
              {
                "name": "ゲイソスピジン",
                "type": "インドールアルカロイド",
                "concentration_mg_per_g": "0.3-0.8",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "ゲイソスピジン",
                "mechanism": "GABA受容体作動",
                "clinical_effects": ["抗不安", "鎮静"],
                "bioavailability": "中"
              }
            ]
          },
          "当帰": {
            "phytochemicals": [
              {
                "name": "リグスチリド",
                "type": "フタリド",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "リグスチリド",
                "mechanism": "血流改善",
                "clinical_effects": ["脳血流改善"],
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
                "mechanism": "微小循環改善",
                "clinical_effects": ["脳循環改善"],
                "bioavailability": "高"
              }
            ]
          },
          "茯苓": {
            "polysaccharides": {
              "type": "β-グルカン",
              "content_percent": "70-80%",
              "metabolic_pathway": "PATH_05",
              "fermentation_products": ["短鎖脂肪酸", "GABA"],
              "clinical_effects": ["精神安定", "腸脳相関改善"],
              "bioavailability": "中"
            }
          },
          "白朮": {
            "phytochemicals": [
              {
                "name": "アトラクチレノリド",
                "type": "セスキテルペン",
                "concentration_mg_per_g": "0.5-1.2",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "アトラクチレノリド",
                "mechanism": "消化管運動調整",
                "clinical_effects": ["胃腸症状改善"],
                "bioavailability": "高"
              }
            ]
          },
          "柴胡": {
            "phytochemicals": [
              {
                "name": "サイコサポニンA",
                "type": "トリテルペンサポニン",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "プロサイコゲニン",
                "mechanism": "抗ストレス",
                "clinical_effects": ["ストレス緩和"],
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
                "active_metabolite": "グリチルレチン酸",
                "mechanism": "抗炎症",
                "clinical_effects": ["精神症状緩和"],
                "bioavailability": "中"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_01",
          "secondary_pathways": ["PATH_04", "PATH_05"],
          "synergy_mechanism": "釣藤鈎のGABA作動＋柴胡の抗ストレス＋茯苓の腸脳相関改善",
          "enhancement_factor": 2.5,
          "key_minerals": ["Ca", "Mg"]
        },
        "indications": {
          "primary": ["イライラ", "不安", "不眠", "認知症周辺症状"],
          "secondary": ["夜泣き", "頭痛", "めまい"],
          "contraindications": ["肝機能障害"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001", "MBT55-003", "MBT55-004"],
          "fermentation_time": "24-36時間",
          "enhanced_compounds": ["ゲイソスピジン", "プロサイコゲニン", "GABA"],
          "bioavailability_boost": "3-8倍"
        }
      },
      
      "F210": {
        "id": "F210",
        "name": "苓桂朮甘湯",
        "category": "めまい・立ちくらみ",
        "main_herbs": ["茯苓", "桂枝", "白朮", "甘草"],
        "components": {
          "茯苓": {
            "polysaccharides": {
              "type": "β-グルカン",
              "content_percent": "70-80%",
              "metabolic_pathway": "PATH_05",
              "key_microbes": ["乳酸菌", "ビフィズス菌"],
              "fermentation_products": ["短鎖脂肪酸", "GABA"],
              "clinical_effects": ["水分代謝改善", "精神安定", "めまい改善"],
              "bioavailability": "中"
            }
          },
          "桂枝": {
            "phytochemicals": [
              {
                "name": "桂皮酸",
                "type": "フェニルプロパノイド",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "桂皮酸",
                "mechanism": "血管拡張",
                "clinical_effects": ["脳血流改善", "めまい改善"],
                "bioavailability": "高"
              }
            ]
          },
          "白朮": {
            "phytochemicals": [
              {
                "name": "アトラクチレノリド",
                "type": "セスキテルペン",
                "concentration_mg_per_g": "0.5-1.2",
                "metabolic_pathway": "PATH_04",
                "key_microbes": ["酵母"],
                "active_metabolite": "アトラクチレノリド",
                "mechanism": "水分代謝改善",
                "clinical_effects": ["めまい改善"],
                "bioavailability": "高"
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
                "mechanism": "抗炎症",
                "clinical_effects": ["炎症抑制"],
                "bioavailability": "中"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_04",
          "secondary_pathways": ["PATH_01", "PATH_05"],
          "synergy_mechanism": "茯苓の水分代謝改善＋桂枝の血流改善＋白朮の胃腸調整で「水毒」によるめまいを改善",
          "enhancement_factor": 2.2,
          "key_minerals": ["K", "Ca"]
        },
        "indications": {
          "primary": ["めまい", "立ちくらみ", "頭重"],
          "secondary": ["動悸", "浮腫", "不安"],
          "contraindications": ["脱水症状"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-003", "MBT55-004", "MBT55-001"],
          "fermentation_time": "24-36時間",
          "enhanced_compounds": ["GABA", "短鎖脂肪酸", "桂皮酸"],
          "bioavailability_boost": "2-5倍"
        }
      }
    },
    "metadata": {
      "generated_by": "HealthBook Platform",
      "algorithm_version": "MBT55-v2.8",
      "classification_source": "Shimojo Phytochemical Classification",
      "total_fully_defined": 41,
      "phase1_formulas": ["F038", "F062", "F119", "F151", "F177"],
      "phase2_formulas": ["F035", "F092", "F136", "F198"],
      "phase3_formulas": ["F089", "F123", "F156", "F184", "F201"],
      "phase4_formulas": ["F068", "F156", "F192", "F210", "F228"],
      "phase5_formulas": ["F012", "F025", "F048", "F089", "F123"],
      "phase6_formulas": ["F089", "F123"],
      "phase7_formulas": ["F156", "F184", "F201", "F210", "F228"],
      "phase8_formulas": ["F001", "F025", "F048", "F068", "F089"],
      "phase9_formulas": ["F035", "F092", "F136", "F198", "F210"],
      "next_phase_formulas": ["F038", "F062", "F119", "F151", "F177"]
    }
  }
}