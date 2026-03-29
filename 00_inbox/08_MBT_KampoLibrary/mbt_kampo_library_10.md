{
  "mbt_kampo_library": {
    "version": "2.9.0",
    "last_updated": "2026-02-24",
    "total_formulas": 294,
    "fully_defined": 46,
    "phase": 10,
    "priority": "medium",
    "formulas": {
      "F041": {
        "id": "F041",
        "name": "牛車腎気丸",
        "category": "腰痛・神経痛・頻尿",
        "main_herbs": ["地黄", "山薬", "山茱萸", "沢瀉", "茯苓", "牡丹皮", "桂枝", "附子", "牛膝", "車前子"],
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
                "clinical_effects": ["老化抑制", "頻尿改善"],
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
                "mechanism": "ホルモン調整",
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
                "mechanism": "血流改善",
                "clinical_effects": ["冷え改善"],
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
                "mechanism": "血管拡張",
                "clinical_effects": ["冷え改善"],
                "bioavailability": "高"
              }
            ]
          },
          "附子": {
            "phytochemicals": [
              {
                "name": "アコニチン",
                "type": "ジテルペンアルカロイド",
                "concentration_mg_per_g": "0.05-0.15",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "ベンゾイルアコニン",
                "mechanism": "鎮痛・温熱作用",
                "clinical_effects": ["神経痛改善", "冷え改善"],
                "bioavailability": "低",
                "caution": "毒性成分"
              }
            ]
          },
          "牛膝": {
            "phytochemicals": [
              {
                "name": "エクジステロン",
                "type": "ステロイド",
                "concentration_mg_per_g": "0.3-0.8",
                "metabolic_pathway": "PATH_03",
                "active_metabolite": "エクジステロン",
                "mechanism": "タンパク質合成促進",
                "clinical_effects": ["筋力増強", "抗疲労"],
                "bioavailability": "中"
              }
            ]
          },
          "車前子": {
            "phytochemicals": [
              {
                "name": "オーキュビン",
                "type": "イリドイド配糖体",
                "concentration_mg_per_g": "0.5-1.5",
                "metabolic_pathway": "PATH_02",
                "active_metabolite": "オーキュビン",
                "mechanism": "利尿",
                "clinical_effects": ["排尿改善"],
                "bioavailability": "中"
              }
            ],
            "polysaccharides": {
              "type": "ムチレージ",
              "content_percent": "10-20%",
              "metabolic_pathway": "PATH_05",
              "clinical_effects": ["粘膜保護"]
            }
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_02",
          "secondary_pathways": ["PATH_01", "PATH_03", "PATH_05"],
          "synergy_mechanism": "八味地黄丸に牛膝・車前子を加え、下半身の症状（腰痛・神経痛・頻尿）に特化",
          "enhancement_factor": 2.6,
          "key_minerals": ["Fe", "Zn", "K", "Ca"]
        },
        "indications": {
          "primary": ["腰痛", "坐骨神経痛", "頻尿", "排尿困難"],
          "secondary": ["下肢冷え", "むくみ", "高血圧", "白内障"],
          "contraindications": ["熱証", "急性炎症"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001", "MBT55-002", "MBT55-005"],
          "fermentation_time": "36-48時間",
          "enhanced_compounds": ["カタルポールアグリコン", "ベンゾイルアコニン", "エクジステロン"],
          "bioavailability_boost": "3-8倍"
        }
      },
      
      "F056": {
        "id": "F056",
        "name": "滋陰降火湯",
        "category": "陰虚・ほてり・不眠",
        "main_herbs": ["当帰", "地黄", "芍薬", "川芎", "黄柏", "知母", "麦門冬", "五味子"],
        "components": {
          "当帰": {
            "phytochemicals": [
              {
                "name": "リグスチリド",
                "type": "フタリド",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "リグスチリド",
                "mechanism": "造血促進",
                "clinical_effects": ["貧血改善"],
                "bioavailability": "中"
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
                "mechanism": "抗酸化",
                "clinical_effects": ["抗老化"],
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
                "clinical_effects": ["疼痛緩和"],
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
                "mechanism": "血流改善",
                "clinical_effects": ["冷え改善"],
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
                "active_metabolite": "ジヒドロベルベリン",
                "mechanism": "抗炎症",
                "clinical_effects": ["炎症抑制"],
                "bioavailability": "低"
              }
            ]
          },
          "知母": {
            "phytochemicals": [
              {
                "name": "チモサポニン",
                "type": "ステロイドサポニン",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_03",
                "active_metabolite": "サルササポゲニン",
                "mechanism": "抗炎症",
                "clinical_effects": ["ほてり改善"],
                "bioavailability": "低"
              }
            ]
          },
          "麦門冬": {
            "phytochemicals": [
              {
                "name": "オフィオポゴニン",
                "type": "ステロイドサポニン",
                "concentration_mg_per_g": "0.5-1.5",
                "metabolic_pathway": "PATH_03",
                "active_metabolite": "オフィオポゴニン",
                "mechanism": "抗不整脈",
                "clinical_effects": ["動悸改善"],
                "bioavailability": "低"
              }
            ],
            "polysaccharides": {
              "type": "ムチン様多糖",
              "content_percent": "20-30%",
              "metabolic_pathway": "PATH_05",
              "clinical_effects": ["粘膜保護"]
            }
          },
          "五味子": {
            "phytochemicals": [
              {
                "name": "シサンドリン",
                "type": "リグナン",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "シサンドリン",
                "mechanism": "抗酸化・鎮静",
                "clinical_effects": ["不眠改善", "抗ストレス"],
                "bioavailability": "中"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_02",
          "secondary_pathways": ["PATH_01", "PATH_03"],
          "synergy_mechanism": "四物湯で血を補い、知母・黄柏で「陰の熱」を取り、麦門冬・五味子で潤いを補う",
          "enhancement_factor": 2.4,
          "key_minerals": ["Fe", "Zn", "Mg"]
        },
        "indications": {
          "primary": ["更年期障害", "不眠", "ほてり", "寝汗"],
          "secondary": ["口渇", "乾燥肌", "動悸", "イライラ"],
          "contraindications": ["冷え症", "下痢傾向"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001", "MBT55-002", "MBT55-005"],
          "fermentation_time": "24-36時間",
          "enhanced_compounds": ["カタルポールアグリコン", "ジヒドロベルベリン", "サルササポゲニン", "シサンドリン"],
          "bioavailability_boost": "3-8倍"
        }
      },
      
      "F078": {
        "id": "F078",
        "name": "抑肝散加陳皮半夏",
        "category": "神経性胃炎・不安",
        "main_herbs": ["釣藤鈎", "当帰", "川芎", "茯苓", "白朮", "柴胡", "甘草", "陳皮", "半夏"],
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
                "clinical_effects": ["胃炎改善"],
                "bioavailability": "中"
              }
            ]
          },
          "陳皮": {
            "phytochemicals": [
              {
                "name": "ヘスペリジン",
                "type": "フラバノン配糖体",
                "concentration_mg_per_g": "5.0-10.0",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "ヘスペレチン",
                "mechanism": "消化促進",
                "clinical_effects": ["食欲増進"],
                "bioavailability": "中"
              },
              {
                "name": "リモネン",
                "type": "モノテルペン",
                "concentration_mg_per_g": "2.0-5.0",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "リモネン",
                "mechanism": "消化促進",
                "clinical_effects": ["胃もたれ改善"],
                "bioavailability": "高"
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
                "clinical_effects": ["吐き気改善"],
                "bioavailability": "高"
              }
            ]
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_01",
          "secondary_pathways": ["PATH_04", "PATH_05"],
          "synergy_mechanism": "抑肝散の精神安定作用に陳皮・半夏の消化促進作用を加え、神経性胃炎に対応",
          "enhancement_factor": 2.6,
          "key_minerals": ["Ca", "Mg", "K"]
        },
        "indications": {
          "primary": ["神経性胃炎", "不安", "不眠", "ストレス"],
          "secondary": ["胃もたれ", "吐き気", "食欲不振", "頭痛"],
          "contraindications": ["胃酸過多", "急性胃炎"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001", "MBT55-003", "MBT55-004"],
          "fermentation_time": "24-36時間",
          "enhanced_compounds": ["ゲイソスピジン", "GABA", "ヘスペレチン", "リモネン"],
          "bioavailability_boost": "3-7倍"
        }
      },
      
      "F115": {
        "id": "F115",
        "name": "麦門冬湯",
        "category": "乾性咳嗽・気管支炎",
        "main_herbs": ["麦門冬", "半夏", "人参", "甘草", "大棗", "粳米"],
        "components": {
          "麦門冬": {
            "phytochemicals": [
              {
                "name": "オフィオポゴニン",
                "type": "ステロイドサポニン",
                "concentration_mg_per_g": "0.5-1.5",
                "metabolic_pathway": "PATH_03",
                "active_metabolite": "オフィオポゴニン",
                "mechanism": "粘膜保護・抗炎症",
                "clinical_effects": ["咳止め", "気道保護"],
                "bioavailability": "低"
              }
            ],
            "polysaccharides": {
              "type": "ムチン様多糖",
              "content_percent": "20-30%",
              "metabolic_pathway": "PATH_05",
              "fermentation_products": ["短鎖脂肪酸"],
              "clinical_effects": ["粘膜保護", "免疫調整"],
              "bioavailability": "中"
            }
          },
          "半夏": {
            "phytochemicals": [
              {
                "name": "ホモゲンチジン酸",
                "type": "フェノール酸",
                "concentration_mg_per_g": "1.0-2.5",
                "metabolic_pathway": "PATH_04",
                "active_metabolite": "ホモゲンチジン酸",
                "mechanism": "制吐・去痰",
                "clinical_effects": ["痰の排出"],
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
                "active_metabolite": "コンパウンドK",
                "mechanism": "抗炎症・免疫調整",
                "clinical_effects": ["体力回復", "感染予防"],
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
                "mechanism": "抗炎症・鎮咳",
                "clinical_effects": ["咳止め", "炎症抑制"],
                "bioavailability": "中"
              }
            ]
          },
          "大棗": {
            "polysaccharides": {
              "type": "ペクチン",
              "content_percent": "3-5%",
              "metabolic_pathway": "PATH_05",
              "fermentation_products": ["短鎖脂肪酸"],
              "clinical_effects": ["整腸作用", "免疫調整"]
            }
          },
          "粳米": {
            "polysaccharides": {
              "type": "デンプン",
              "content_percent": "70-80%",
              "metabolic_pathway": "PATH_05",
              "fermentation_products": ["短鎖脂肪酸"],
              "clinical_effects": ["胃腸保護", "エネルギー補給"]
            }
          }
        },
        "formula_synergy": {
          "primary_pathway": "PATH_03",
          "secondary_pathways": ["PATH_04", "PATH_05"],
          "synergy_mechanism": "麦門冬の粘膜保護＋半夏の去痰＋人参・甘草の抗炎症で乾性咳嗽を改善",
          "enhancement_factor": 2.3,
          "key_minerals": ["K", "Ca", "Mg"]
        },
        "indications": {
          "primary": ["乾性咳嗽", "気管支炎", "咽頭炎", "声枯れ"],
          "secondary": ["口渇", "乾燥肌", "糖尿病の口渇"],
          "contraindications": ["痰の多い咳", "湿性咳嗽"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001", "MBT55-004", "MBT55-005"],
          "fermentation_time": "24時間",
          "enhanced_compounds": ["オフィオポゴニン", "グリチルレチン酸", "短鎖脂肪酸"],
          "bioavailability_boost": "2-5倍"
        }
      },
      
      "F144": {
        "id": "F144",
        "name": "酸棗仁湯",
        "category": "不眠・神経症",
        "main_herbs": ["酸棗仁", "茯苓", "知母", "川芎", "甘草"],
        "components": {
          "酸棗仁": {
            "phytochemicals": [
              {
                "name": "サポニン類",
                "type": "トリテルペンサポニン",
                "concentration_mg_per_g": "2.0-4.0",
                "metabolic_pathway": "PATH_01",
                "key_microbes": ["放線菌"],
                "active_metabolite": "酸棗仁サポニン",
                "mechanism": "GABA受容体作動",
                "clinical_effects": ["睡眠改善", "抗不安"],
                "bioavailability": "低"
              },
              {
                "name": "スピナシン",
                "type": "フラボノイド",
                "concentration_mg_per_g": "0.5-1.2",
                "metabolic_pathway": "PATH_01",
                "active_metabolite": "スピナシン",
                "mechanism": "鎮静",
                "clinical_effects": ["睡眠導入"],
                "bioavailability": "中"
              }
            ],
            "oils": {
              "type": "脂肪酸",
              "content_percent": "30-40%",
              "metabolic_pathway": "PATH_03",
              "clinical_effects": ["神経保護"]
            }
          },
          "茯苓": {
            "polysaccharides": {
              "type": "β-グルカン",
              "content_percent": "70-80%",
              "metabolic_pathway": "PATH_05",
              "fermentation_products": ["短鎖脂肪酸", "GABA"],
              "clinical_effects": ["精神安定", "睡眠改善"],
              "bioavailability": "中"
            }
          },
          "知母": {
            "phytochemicals": [
              {
                "name": "チモサポニン",
                "type": "ステロイドサポニン",
                "concentration_mg_per_g": "1.5-3.0",
                "metabolic_pathway": "PATH_03",
                "active_metabolite": "サルササポゲニン",
                "mechanism": "抗炎症・解熱",
                "clinical_effects": ["ほてり改善", "イライラ改善"],
                "bioavailability": "低"
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
                "mechanism": "血流改善",
                "clinical_effects": ["頭痛改善"],
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
          "primary_pathway": "PATH_01",
          "secondary_pathways": ["PATH_03", "PATH_05"],
          "synergy_mechanism": "酸棗仁のGABA作用＋茯苓のGABA産生＋知母の抗炎症で不眠を改善",
          "enhancement_factor": 2.5,
          "key_minerals": ["Ca", "Mg", "Zn"]
        },
        "indications": {
          "primary": ["不眠症", "神経症", "イライラ"],
          "secondary": ["動悸", "不安", "頭痛", "めまい"],
          "contraindications": ["痰湿", "消化不良"]
        },
        "mbt55_optimization": {
          "recommended_strains": ["MBT55-001", "MBT55-004", "MBT55-005"],
          "fermentation_time": "24-36時間",
          "enhanced_compounds": ["酸棗仁サポニン", "GABA", "サルササポゲニン", "短鎖脂肪酸"],
          "bioavailability_boost": "2-6倍"
        }
      }
    },
    "metadata": {
      "generated_by": "HealthBook Platform",
      "algorithm_version": "MBT55-v2.9",
      "classification_source": "Shimojo Phytochemical Classification",
      "total_fully_defined": 46,
      "phase1_formulas": ["F038", "F062", "F119", "F151", "F177"],
      "phase2_formulas": ["F035", "F092", "F136", "F198"],
      "phase3_formulas": ["F089", "F123", "F156", "F184", "F201"],
      "phase4_formulas": ["F068", "F156", "F192", "F210", "F228"],
      "phase5_formulas": ["F012", "F025", "F048", "F089", "F123"],
      "phase6_formulas": ["F089", "F123"],
      "phase7_formulas": ["F156", "F184", "F201", "F210", "F228"],
      "phase8_formulas": ["F001", "F025", "F048", "F068", "F089"],
      "phase9_formulas": ["F035", "F092", "F136", "F198", "F210"],
      "phase10_formulas": ["F041", "F056", "F078", "F115", "F144"],
      "next_phase_formulas": ["F012", "F025", "F048", "F068", "F089"]
    }
  }
}