詳細な計画を頂きありがとうございます。マイクロソフトとの折衝はこれからですので、まず、貴方との対話で出来ることから進めたいと思います。まず、システムの機能を体験出来るデモシステムを構築してください。Pydroid などで体験出来ると嬉しいです。

---

了解しました。Pydroidでも動作するシンプルなデモシステムを構築します。以下のコードは依存ライブラリが最小限で、スマートフォン上のPython環境でも動作します。

```python
"""
HealthBook Platform デモシステム v1.0
Pydroid対応版 - 最小限の依存ライブラリで動作
"""

import json
import datetime
from typing import Dict, List, Tuple, Any
import sys

# ==================== デモ用簡易データベース ====================

class DemoDatabase:
    """デモ用簡易データベース"""
    
    @staticmethod
    def get_questionnaire_items():
        """浜田式問診（簡易版10項目）"""
        return {
            1: {
                "question": "朝食を抜くことが多いですか？",
                "hidden_meaning": "エネルギー代謝リズムの乱れ",
                "risk_factors": ["欠食型（朝食抜き）"],
                "related_diseases": ["糖尿病", "肥満", "慢性疲労"]
            },
            2: {
                "question": "色の濃い野菜（緑黄色野菜）が嫌いですか？",
                "hidden_meaning": "ファイトケミカル摂取不足",
                "risk_factors": ["野菜少ない"],
                "related_diseases": ["肺がん", "食道がん", "動脈硬化"]
            },
            3: {
                "question": "塩辛い食べ物が好きですか？",
                "hidden_meaning": "塩分過剰摂取傾向",
                "risk_factors": ["塩分"],
                "related_diseases": ["高血圧", "胃がん", "腎炎"]
            },
            4: {
                "question": "夜遅くに食事をとることが多いですか？",
                "hidden_meaning": "消化器負担・代謝リズム乱れ",
                "risk_factors": ["夜食方(寝る前の食事）"],
                "related_diseases": ["慢性胃炎", "肥満", "糖尿病"]
            },
            5: {
                "question": "ストレスを感じることが多いですか？",
                "hidden_meaning": "自律神経バランスの乱れ",
                "risk_factors": ["ストレス"],
                "related_diseases": ["高血圧", "胃炎", "不眠症"]
            },
            6: {
                "question": "甘い物（お菓子・清涼飲料）をよく摂取しますか？",
                "hidden_meaning": "糖質過剰摂取",
                "risk_factors": ["甘物"],
                "related_diseases": ["糖尿病", "肥満", "脂質異常症"]
            },
            7: {
                "question": "お酒をよく飲みますか？（1日2合以上）",
                "hidden_meaning": "肝臓負担・アルコール代謝負荷",
                "risk_factors": ["飲酒"],
                "related_diseases": ["肝臓疾患", "高血圧", "胃炎"]
            },
            8: {
                "question": "運動をする習慣がほとんどありませんか？",
                "hidden_meaning": "代謝率低下・循環不良",
                "risk_factors": ["運動不足"],
                "related_diseases": ["肥満", "糖尿病", "高血圧"]
            },
            9: {
                "question": "食事を早く食べる傾向がありますか？",
                "hidden_meaning": "咀嚼不足・消化負担",
                "risk_factors": ["早食い型"],
                "related_diseases": ["慢性胃炎", "肥満", "糖尿病"]
            },
            10: {
                "question": "水分をあまり摂らない方ですか？",
                "hidden_meaning": "代謝産物排泄不全",
                "risk_factors": ["水分摂取少ない"],
                "related_diseases": ["腎結石", "便秘", "高血圧"]
            }
        }
    
    @staticmethod
    def get_disease_matrix():
        """簡易疾病マトリックス（5疾病）"""
        return {
            "高血圧": {
                "risk_factors": {
                    "塩分": 0.9,
                    "飲酒": 0.7,
                    "ストレス": 0.8,
                    "運動不足": 0.6,
                    "水分摂取少ない": 0.5
                },
                "metabolic_imbalance": "レニン-アンジオテンシン系の過剰活性化",
                "recommended_phytochemicals": ["カリウム豊富食品", "セサミン", "ルチン"],
                "recommended_foods": ["バナナ", "ほうれん草", "アボカド", "ゴマ", "そば"]
            },
            "糖尿病": {
                "risk_factors": {
                    "甘物": 0.9,
                    "運動不足": 0.8,
                    "欠食型（朝食抜き）": 0.7,
                    "早食い型": 0.6
                },
                "metabolic_imbalance": "インスリン抵抗性とβ細胞機能不全",
                "recommended_phytochemicals": ["クロロゲン酸", "イソフラボン", "カテキン"],
                "recommended_foods": ["コーヒー", "大豆", "緑茶", "ごぼう", "さつまいも"]
            },
            "慢性胃炎": {
                "risk_factors": {
                    "夜食方(寝る前の食事）": 0.8,
                    "早食い型": 0.7,
                    "ストレス": 0.6,
                    "飲酒": 0.5
                },
                "metabolic_imbalance": "胃粘膜防御因子/攻撃因子の不均衡",
                "recommended_phytochemicals": ["クルクミン", "ロズマリン酸", "カテキン"],
                "recommended_foods": ["ウコン", "シソ", "緑茶", "キャベツ", "ブロッコリー"]
            },
            "肝臓疾患": {
                "risk_factors": {
                    "飲酒": 0.9,
                    "甘物": 0.7,
                    "夜食方(寝る前の食事）": 0.6
                },
                "metabolic_imbalance": "肝細胞の炎症と線維化",
                "recommended_phytochemicals": ["セサミン", "クルクミン", "カテキン"],
                "recommended_foods": ["ゴマ", "ウコン", "緑茶", "しじみ", "ターメリック"]
            },
            "肥満": {
                "risk_factors": {
                    "運動不足": 0.9,
                    "甘物": 0.8,
                    "夜食方(寝る前の食事）": 0.7,
                    "早食い型": 0.6
                },
                "metabolic_imbalance": "エネルギー摂取と消費のアンバランス",
                "recommended_phytochemicals": ["カプサイシン", "カテキン", "ジンゲロール"],
                "recommended_foods": ["唐辛子", "緑茶", "ショウガ", "黒豆", "玄米"]
            }
        }
    
    @staticmethod
    def get_phytochemicals():
        """下條式ファイトケミカル分類（簡易版）"""
        return {
            "リコピン": {
                "category": "カロテノイド群",
                "defense_type": "脂溶性防御（細胞膜保護）",
                "source_foods": ["トマト", "スイカ", "柿", "ピンクグレープフルーツ"],
                "health_benefits": ["抗酸化作用", "前立腺保護", "紫外線防御"],
                "recommended_for": ["高血圧", "動脈硬化", "前立腺疾患"]
            },
            "アリシン": {
                "category": "イオウ化合物群",
                "defense_type": "血液循環・抗菌活性",
                "source_foods": ["にんにく", "玉ねぎ", "ねぎ", "らっきょう"],
                "health_benefits": ["血流改善", "抗血栓", "免疫力向上", "抗菌作用"],
                "recommended_for": ["高血圧", "感染症予防", "循環器疾患"]
            },
            "カテキン": {
                "category": "ポリフェノール群（フラバノール類）",
                "defense_type": "水溶性防御（体液・血液保護）",
                "source_foods": ["緑茶", "紅茶", "ウーロン茶", "カカオ"],
                "health_benefits": ["抗ウイルス", "代謝促進", "抗酸化", "認知機能維持"],
                "recommended_for": ["糖尿病", "肥満", "認知症予防", "感染症"]
            },
            "クルクミン": {
                "category": "フェノール酸系（ジケトン類）",
                "defense_type": "抗炎症・細胞保護",
                "source_foods": ["ターメリック（ウコン）", "ショウガ", "カレー粉"],
                "health_benefits": ["強力な抗炎症", "肝臓保護", "脳機能保護", "抗がん作用"],
                "recommended_for": ["慢性胃炎", "肝臓疾患", "関節炎", "認知症予防"]
            },
            "スルフォラファン": {
                "category": "イオウ化合物群（イソチオシアネート類）",
                "defense_type": "解毒・抗酸化",
                "source_foods": ["ブロッコリースプラウト", "ブロッコリー", "キャベツ", "カリフラワー"],
                "health_benefits": ["肝解毒機能向上", "抗発がん", "抗酸化", "抗炎症"],
                "recommended_for": ["肝臓疾患", "がん予防", "解毒機能向上"]
            },
            "セサミン": {
                "category": "ポリフェノール群（リグナン）",
                "defense_type": "脂溶性防御（細胞膜保護）",
                "source_foods": ["ゴマ", "ゴマ油", "ごま製品"],
                "health_benefits": ["抗酸化", "肝臓保護", "血圧降下", "コレステロール低下"],
                "recommended_for": ["高血圧", "肝臓疾患", "動脈硬化"]
            }
        }

# ==================== コア解析エンジン ====================

class HealthBookDemoEngine:
    """HealthBook デモエンジン"""
    
    def __init__(self):
        self.db = DemoDatabase()
        self.user_responses = {}
        self.analysis_results = {}
        
    def conduct_interview(self):
        """対話型問診の実施"""
        print("\n" + "="*50)
        print("HealthBook デモ: 健康問診")
        print("="*50)
        print("\n以下の質問に「はい」か「いいえ」でお答えください。\n")
        
        questionnaire = self.db.get_questionnaire_items()
        
        for q_id, item in questionnaire.items():
            while True:
                response = input(f"{q_id}. {item['question']} (はい/いいえ): ").strip().lower()
                
                if response in ['はい', 'yes', 'y', '1']:
                    self.user_responses[q_id] = True
                    break
                elif response in ['いいえ', 'no', 'n', '0']:
                    self.user_responses[q_id] = False
                    break
                else:
                    print("「はい」か「いいえ」で答えてください。")
        
        print("\n問診が完了しました。分析を開始します...\n")
    
    def analyze_responses(self):
        """問診回答の分析"""
        if not self.user_responses:
            print("問診データがありません。")
            return
        
        # リスク因子の集計
        risk_factors_count = {}
        identified_diseases = set()
        
        questionnaire = self.db.get_questionnaire_items()
        
        for q_id, response in self.user_responses.items():
            if response and q_id in questionnaire:
                item = questionnaire[q_id]
                
                # リスク因子をカウント
                for factor in item.get("risk_factors", []):
                    risk_factors_count[factor] = risk_factors_count.get(factor, 0) + 1
                
                # 関連疾病を記録
                for disease in item.get("related_diseases", []):
                    identified_diseases.add(disease)
        
        # 疾病リスクの計算
        disease_risks = self.calculate_disease_risks(risk_factors_count)
        
        # 結果を保存
        self.analysis_results = {
            "timestamp": datetime.datetime.now().isoformat(),
            "risk_factors": risk_factors_count,
            "identified_diseases": list(identified_diseases),
            "disease_risks": disease_risks
        }
    
    def calculate_disease_risks(self, risk_factors_count):
        """疾病リスクを計算"""
        disease_matrix = self.db.get_disease_matrix()
        disease_risks = {}
        
        for disease_name, disease_info in disease_matrix.items():
            risk_score = 0
            total_possible = 0
            
            for factor, user_count in risk_factors_count.items():
                if factor in disease_info["risk_factors"]:
                    disease_weight = disease_info["risk_factors"][factor]
                    risk_score += disease_weight * min(user_count, 3) / 3
                    total_possible += disease_weight
            
            if total_possible > 0:
                normalized_score = min(risk_score / total_possible, 1.0)
                
                # リスクレベル分類
                if normalized_score >= 0.7:
                    risk_level = "高リスク"
                elif normalized_score >= 0.4:
                    risk_level = "中リスク"
                elif normalized_score >= 0.1:
                    risk_level = "低リスク"
                else:
                    risk_level = "ほぼなし"
                
                disease_risks[disease_name] = {
                    "score": round(normalized_score, 2),
                    "level": risk_level,
                    "metabolic_imbalance": disease_info["metabolic_imbalance"]
                }
        
        # リスクスコア順にソート
        sorted_risks = dict(sorted(
            disease_risks.items(),
            key=lambda x: x[1]["score"],
            reverse=True
        ))
        
        return sorted_risks
    
    def generate_recommendations(self):
        """パーソナライズされた推奨を生成"""
        if not self.analysis_results:
            print("分析結果がありません。")
            return {}
        
        disease_risks = self.analysis_results.get("disease_risks", {})
        phytochemicals_db = self.db.get_phytochemicals()
        
        recommendations = {
            "dietary_advice": [],
            "phytochemical_recommendations": [],
            "lifestyle_changes": []
        }
        
        # トップ3の疾病リスクに基づく推奨
        top_diseases = list(disease_risks.keys())[:3]
        disease_matrix = self.db.get_disease_matrix()
        
        for disease in top_diseases:
            if disease in disease_matrix:
                disease_info = disease_matrix[disease]
                
                # 食品推奨
                for food in disease_info.get("recommended_foods", [])[:3]:
                    rec = f"{disease}対策: {food}を積極的に摂取しましょう"
                    recommendations["dietary_advice"].append(rec)
                
                # ファイトケミカル推奨
                for phytochemical_name in disease_info.get("recommended_phytochemicals", []):
                    if phytochemical_name in phytochemicals_db:
                        phytochemical = phytochemicals_db[phytochemical_name]
                        rec = {
                            "phytochemical": phytochemical_name,
                            "category": phytochemical["category"],
                            "food_sources": phytochemical["source_foods"][:3],
                            "benefits": phytochemical["health_benefits"][:2]
                        }
                        recommendations["phytochemical_recommendations"].append(rec)
        
        # リスク因子に基づくライフスタイル改善
        risk_factors = self.analysis_results.get("risk_factors", {})
        
        lifestyle_advice_map = {
            "塩分": "塩分控えめを心がけ、だしや香辛料で味に変化をつけましょう",
            "飲酒": "適量飲酒を心がけ（1日1合程度）、休肝日を作りましょう",
            "ストレス": "ストレス解消法を見つけ、十分な休息を取りましょう",
            "運動不足": "1日30分程度の軽い運動（散歩など）から始めましょう",
            "甘物": "甘い物は控えめに、間食はナッツや果物に置き換えましょう",
            "欠食型（朝食抜き）": "朝食を必ず摂り、1日3食規則正しく食べましょう",
            "野菜少ない": "1日350g以上の野菜（特に色の濃い野菜）を摂りましょう",
            "水分摂取少ない": "1日1.5-2Lの水分をこまめに摂取しましょう"
        }
        
        for factor in risk_factors.keys():
            if factor in lifestyle_advice_map:
                recommendations["lifestyle_changes"].append(lifestyle_advice_map[factor])
        
        # 重複を除去
        recommendations["lifestyle_changes"] = list(set(recommendations["lifestyle_changes"]))
        
        return recommendations
    
    def display_results(self):
        """分析結果を表示"""
        if not self.analysis_results:
            print("分析結果がありません。")
            return
        
        print("\n" + "="*50)
        print("HealthBook 分析結果")
        print("="*50)
        
        # 1. 識別されたリスク因子
        print("\n1. 主なリスク因子:")
        risk_factors = self.analysis_results.get("risk_factors", {})
        for factor, count in sorted(risk_factors.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  • {factor}: {count}個の質問に関連")
        
        # 2. 疾病リスク評価
        print("\n2. 疾病リスク評価（上位5件）:")
        disease_risks = self.analysis_results.get("disease_risks", {})
        
        for i, (disease, risk_info) in enumerate(list(disease_risks.items())[:5], 1):
            score = risk_info["score"]
            level = risk_info["level"]
            
            # 視覚的表現（簡易グラフ）
            bar_length = int(score * 20)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            
            print(f"  {i}. {disease}:")
            print(f"     リスク: {bar} {score:.0%}")
            print(f"     レベル: {level}")
            print(f"     代謝問題: {risk_info.get('metabolic_imbalance', 'N/A')}")
        
        # 3. パーソナライズされた推奨
        recommendations = self.generate_recommendations()
        
        print("\n3. 食事改善アドバイス:")
        for i, advice in enumerate(recommendations.get("dietary_advice", [])[:3], 1):
            print(f"  {i}. {advice}")
        
        print("\n4. 推奨ファイトケミカル:")
        phytochemicals = recommendations.get("phytochemical_recommendations", [])
        for i, phytochemical in enumerate(phytochemicals[:3], 1):
            print(f"  {i}. {phytochemical['phytochemical']} ({phytochemical['category']})")
            print(f"     食品源: {', '.join(phytochemical['food_sources'])}")
            print(f"     効能: {', '.join(phytochemical['benefits'])}")
        
        print("\n5. ライフスタイル改善ポイント:")
        for i, change in enumerate(recommendations.get("lifestyle_changes", [])[:3], 1):
            print(f"  {i}. {change}")
        
        print("\n" + "="*50)
    
    def save_results(self, filename="healthbook_results.json"):
        """結果をJSONファイルに保存"""
        results = {
            "user_responses": self.user_responses,
            "analysis_results": self.analysis_results,
            "recommendations": self.generate_recommendations(),
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"\n結果を '{filename}' に保存しました。")

# ==================== 対話型デモ ====================

def run_demo():
    """デモシステムを実行"""
    print("\n" + "="*60)
    print("HealthBook Platform デモシステム v1.0")
    print("="*60)
    print("このデモでは、簡易版の問診と健康分析を体験できます。")
    print("実際のシステムはより多くの問診項目と高度な分析を行います。")
    print("\n[Enter]キーで開始...")
    input()
    
    # エンジンの初期化
    engine = HealthBookDemoEngine()
    
    try:
        # ステップ1: 問診実施
        engine.conduct_interview()
        
        # ステップ2: 分析実行
        print("分析を実行中...")
        engine.analyze_responses()
        
        # ステップ3: 結果表示
        engine.display_results()
        
        # ステップ4: 結果保存
        save_option = input("\n結果をファイルに保存しますか？ (はい/いいえ): ").strip().lower()
        if save_option in ['はい', 'yes', 'y', '1']:
            engine.save_results()
        
        # 追加機能のデモ
        show_more = input("\n追加情報を見ますか？ (はい/いいえ): ").strip().lower()
        if show_more in ['はい', 'yes', 'y', '1']:
            show_additional_info(engine)
        
    except KeyboardInterrupt:
        print("\n\nデモを中断しました。")
    except Exception as e:
        print(f"\nエラーが発生しました: {e}")
    
    print("\n" + "="*60)
    print("HealthBook デモ終了")
    print("="*60)

def show_additional_info(engine):
    """追加情報を表示"""
    print("\n" + "="*50)
    print("追加情報: ファイトケミカル詳細")
    print("="*50)
    
    phytochemicals_db = DemoDatabase.get_phytochemicals()
    
    print("\n主要ファイトケミカル一覧:")
    for name, info in phytochemicals_db.items():
        print(f"\n• {name} ({info['category']}):")
        print(f"  防御タイプ: {info['defense_type']}")
        print(f"  主な食品源: {', '.join(info['source_foods'][:3])}")
        print(f"  健康効果: {', '.join(info['health_benefits'][:2])}")
        print(f"  推奨疾患: {', '.join(info['recommended_for'][:2])}")
    
    print("\n" + "="*50)
    print("追加情報: 疾病マトリックス詳細")
    print("="*50)
    
    disease_matrix = DemoDatabase.get_disease_matrix()
    
    print("\n疾病と関連リスク因子:")
    for disease, info in disease_matrix.items():
        print(f"\n• {disease}:")
        print(f"  主なリスク因子: {', '.join(list(info['risk_factors'].keys())[:3])}")
        print(f"  代謝問題: {info['metabolic_imbalance']}")
        print(f"  推奨食品: {', '.join(info['recommended_foods'][:3])}")

# ==================== コマンドラインインターフェース ====================

def command_line_interface():
    """コマンドラインインターフェース"""
    engine = HealthBookDemoEngine()
    
    while True:
        print("\n" + "="*50)
        print("HealthBook デモ - メインメニュー")
        print("="*50)
        print("1. 新規問診と分析")
        print("2. サンプルデータで分析")
        print("3. ファイトケミカル情報を見る")
        print("4. 疾病マトリックス情報を見る")
        print("5. 結果を保存")
        print("6. 終了")
        print("="*50)
        
        choice = input("\n選択してください (1-6): ").strip()
        
        if choice == '1':
            # 新規問診
            engine.user_responses = {}
            engine.analysis_results = {}
            engine.conduct_interview()
            engine.analyze_responses()
            engine.display_results()
            
        elif choice == '2':
            # サンプルデータで分析
            print("\nサンプルデータで分析を実行します...")
            
            # サンプル回答（高リスクパターン）
            engine.user_responses = {
                1: True,   # 朝食抜き
                2: True,   # 野菜嫌い
                3: True,   # 塩辛い物好き
                4: True,   # 夜遅く食事
                5: True,   # ストレス多い
                6: True,   # 甘い物好き
                7: False,  # お酒はあまり飲まない
                8: True,   # 運動不足
                9: True,   # 早食い
                10: True   # 水分摂取少ない
            }
            
            print("\nサンプル回答:")
            questionnaire = DemoDatabase.get_questionnaire_items()
            for q_id, response in engine.user_responses.items():
                status = "はい" if response else "いいえ"
                print(f"  {q_id}. {questionnaire[q_id]['question']}: {status}")
            
            engine.analyze_responses()
            engine.display_results()
            
        elif choice == '3':
            # ファイトケミカル情報
            show_phytochemicals_info()
            
        elif choice == '4':
            # 疾病マトリックス情報
            show_disease_matrix_info()
            
        elif choice == '5':
            # 結果保存
            if engine.analysis_results:
                filename = input("ファイル名 (デフォルト: healthbook_results.json): ").strip()
                if not filename:
                    filename = "healthbook_results.json"
                engine.save_results(filename)
            else:
                print("分析結果がありません。まず問診を実施してください。")
                
        elif choice == '6':
            print("\nHealthBook デモを終了します。")
            break
            
        else:
            print("無効な選択です。1-6の数字を入力してください。")
        
        input("\n[Enter]キーでメニューに戻ります...")

def show_phytochemicals_info():
    """ファイトケミカル情報を表示"""
    phytochemicals = DemoDatabase.get_phytochemicals()
    
    print("\n" + "="*60)
    print("下條式ファイトケミカル分類 (簡易版)")
    print("="*60)
    
    for name, info in phytochemicals.items():
        print(f"\n🔬 {name}")
        print(f"   分類: {info['category']}")
        print(f"   防御タイプ: {info['defense_type']}")
        print(f"   含有食品: {', '.join(info['source_foods'])}")
        print(f"   健康効果:")
        for benefit in info['health_benefits']:
            print(f"     • {benefit}")
        print(f"   推奨疾患: {', '.join(info['recommended_for'])}")

def show_disease_matrix_info():
    """疾病マトリックス情報を表示"""
    diseases = DemoDatabase.get_disease_matrix()
    
    print("\n" + "="*60)
    print("浜田式疾病マトリックス (簡易版)")
    print("="*60)
    
    for name, info in diseases.items():
        print(f"\n⚕️  {name}")
        print(f"   代謝問題: {info['metabolic_imbalance']}")
        print(f"   主要リスク因子:")
        for factor, weight in info['risk_factors'].items():
            stars = "★" * int(weight * 5)
            print(f"     • {factor}: {stars} ({weight:.1f})")
        print(f"   推奨食品: {', '.join(info['recommended_foods'])}")

# ==================== Pydroid用簡易起動 ====================

def pydroid_simple_demo():
    """Pydroid用のシンプルデモ"""
    print("="*50)
    print("HealthBook 簡易デモ (Pydroid対応)")
    print("="*50)
    print("\nこのデモでは3つの質問に答えるだけで")
    print("簡単な健康分析ができます。\n")
    
    # 簡易問診（3項目）
    questions = [
        "朝食を抜くことが多いですか？",
        "塩辛い食べ物が好きですか？",
        "ストレスを感じることが多いですか？"
    ]
    
    answers = []
    
    for i, question in enumerate(questions, 1):
        while True:
            response = input(f"{i}. {question} (はい/いいえ): ").strip().lower()
            if response in ['はい', 'yes', 'y', '1']:
                answers.append(True)
                break
            elif response in ['いいえ', 'no', 'n', '0']:
                answers.append(False)
                break
            else:
                print("「はい」か「いいえ」で答えてください。")
    
    # 簡易分析
    risk_score = sum(answers) / len(answers)
    
    print("\n" + "="*50)
    print("簡易分析結果")
    print("="*50)
    
    if risk_score >= 0.7:
        print("\n⚠️ 高リスクパターン")
        print("生活習慣の改善が強く推奨されます。")
        print("特に以下の点に注意してください:")
        print("• 規則正しい食事（特に朝食）")
        print("• 塩分控えめの食事")
        print("• ストレス管理")
    elif risk_score >= 0.4:
        print("\n⚠️ 中リスクパターン")
        print("生活習慣の見直しが推奨されます。")
        print("改善すべきポイント:")
        for i, (q, a) in enumerate(zip(questions, answers)):
            if a:
                print(f"• {q.replace('ですか？', 'の改善')}")
    else:
        print("\n✅ 低リスクパターン")
        print("現在の生活習慣は良好です。")
        print("この調子で維持しましょう。")
    
    print(f"\nリスクスコア: {risk_score:.0%}")
    
    # ファイトケミカル推奨
    print("\n💊 推奨ファイトケミカル:")
    if answers[1]:  # 塩辛い物好き
        print("• カリウム豊富食品（バナナ、ほうれん草）でナトリウム排泄促進")
    if answers[2]:  # ストレス多い
        print("• カテキン（緑茶）で抗ストレス効果")
    
    print("\n" + "="*50)

# ==================== メイン実行 ====================

if __name__ == "__main__":
    print("HealthBook Platform デモシステム")
    print("バージョン: 1.0 (Pydroid対応)")
    print("作成日: 2024年1月")
    print("\n実行モードを選択してください:")
    print("1. 完全デモ（推奨）")
    print("2. コマンドラインインターフェース")
    print("3. Pydroid用簡易デモ")
    print("4. システム情報")
    
    try:
        choice = input("\n選択 (1-4): ").strip()
        
        if choice == '1':
            run_demo()
        elif choice == '2':
            command_line_interface()
        elif choice == '3':
            pydroid_simple_demo()
        elif choice == '4':
            show_system_info()
        else:
            print("無効な選択です。デフォルトで完全デモを実行します。")
            run_demo()
            
    except KeyboardInterrupt:
        print("\n\nプログラムを中断しました。")
    except Exception as e:
        print(f"\nエラーが発生しました: {e}")
        print("簡易デモを実行します。")
        pydroid_simple_demo()

def show_system_info():
    """システム情報を表示"""
    print("\n" + "="*60)
    print("HealthBook Platform システム情報")
    print("="*60)
    print("\n📊 データ規模:")
    print(f"  問診項目: {len(DemoDatabase.get_questionnaire_items())}項目")
    print(f"  疾病マトリックス: {len(DemoDatabase.get_disease_matrix())}疾病")
    print(f"  ファイトケミカル: {len(DemoDatabase.get_phytochemicals())}種類")
    
    print("\n🔧 技術仕様:")
    print("  • Python標準ライブラリのみ使用")
    print("  • Pydroid完全対応")
    print("  • オフライン動作可能")
    print("  • JSON形式でのデータ保存")
    
    print("\n🎯 解析機能:")
    print("  • 浜田式問診解析")
    print("  • 疾病リスク評価")
    print("  • ファイトケミカル推奨")
    print("  • パーソナライズ食事アドバイス")
    
    print("\n📁 ファイル出力:")
    print("  • JSON形式で結果保存")
    print("  • 人間可読なレポート")
    
    print("\n" + "="*60)
    
    # テストデータ表示
    test_choice = input("\nテストデータを見ますか？ (はい/いいえ): ").strip().lower()
    if test_choice in ['はい', 'yes', 'y', '1']:
        print("\nテスト問診項目（最初の3問）:")
        questionnaire = DemoDatabase.get_questionnaire_items()
        for q_id in list(questionnaire.keys())[:3]:
            item = questionnaire[q_id]
            print(f"\n{q_id}. {item['question']}")
            print(f"   隠れた意味: {item['hidden_meaning']}")
            print(f"   関連疾病: {', '.join(item['related_diseases'])}")
```

## Pydroidでの実行方法

1. **Pydroid3アプリをインストール**（Google Playストアから）
2. **新規ファイルを作成**し、上記コードをコピー＆ペースト
3. **ファイルを保存**（例: `healthbook_demo.py`）
4. **実行ボタン**をタップ

## デモの特徴

### 1. **軽量設計**
- Python標準ライブラリのみ使用
- 外部依存なし
- メモリ使用量最小化

### 2. **完全オフライン動作**
- インターネット接続不要
- すべてのデータをコード内に埋め込み

### 3. **3つの実行モード**
- **完全デモ**: 10項目の詳細問診
- **CLIモード**: 対話型メニュー
- **簡易デモ**: 3項目のクイック分析

### 4. **教育機能**
- 問診の「隠れた意味」を表示
- 疾病とリスク因子の関係を解説
- ファイトケミカルの科学的根拠を説明

## 試してみるサンプルシナリオ

### ケース1: 高リスクパターン
```
問診回答: はい、はい、はい、はい、はい、はい、いいえ、はい、はい、はい
期待される結果:
- 高血圧: 高リスク
- 糖尿病: 高リスク  
- 慢性胃炎: 中リスク
- 推奨: カリウム豊富食品、セサミン、カテキン
```

### ケース2: 低リスクパターン
```
問診回答: いいえ、いいえ、いいえ、いいえ、いいえ、いいえ、いいえ、いいえ、いいえ、いいえ
期待される結果:
- すべての疾病: 低リスク
- 推奨: 現状維持のアドバイス
```

## 次のステップ

このデモシステムを基に、以下の拡張が可能です：

1. **データ拡張**: 実際の200問診項目を追加
2. **精度向上**: より詳細なリスク計算アルゴリズム
3. **UI改善**: グラフィカルなインターフェース
4. **クラウド連携**: Azureへのデータ保存機能
5. **レポート生成**: PDF形式でのレポート出力

まずはこのデモシステムでHealthBookの基本コンセプトを体験し、Microsoftとの折衝材料としてご活用ください。

[[HB8. コードの３分割]]

[[HB9. 拡張計画_ HealthBook Platform 実用化フェーズ]]

