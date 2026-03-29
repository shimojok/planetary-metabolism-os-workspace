添付の問診表から、エクセルの疾病リスク表を通じて疾病リスクを紐解くこと。さらに、野菜のファイトケミカル表を繋げ、健康・代謝改善に繋げたいのです。

[[HealthBook/問診表.pdf]]
[[病気と食生活の関係シート.pdf]]
[[ファイトケミカル分類表.pdf]]

---

提供されたファイルを分析し、問診表と病気リスク、ファイトケミカルを統合した推論エンジンを開発します。以下に、Pythonで実装する推論システムの設計とコードを示します。

## 推論エンジン設計

### システム構成
1. **問診データ解析モジュール** - PDFから症状・生活習慣を抽出
2. **病気リスク評価モジュール** - 食生活パターンから病気リスクを計算
3. **ファイトケミカル推奨モジュール** - 必要な栄養素を提案
4. **統合推論エンジン** - 上記を組み合わせた総合システム

## Python実装コード

```python
import pandas as pd
import numpy as np
import json
from typing import Dict, List, Tuple, Set
import re

class HealthInferenceEngine:
    """健康推論エンジン"""
    
    def __init__(self):
        self.disease_db = None
        self.phytochemical_db = None
        self.symptom_mapping = {}
        self._load_databases()
        self._create_symptom_mapping()
    
    def _load_databases(self):
        """データベースをロード"""
        # 病気と食生活の関係データをロード
        disease_data = {
            'アトピー性皮膚炎': {'欠食型（朝食抜き）': 1, '偏食型': 1, '脂肪': 1, '甘物': 1, '肉多い': 1, '青魚を食べない': 1, '洋食好み': 1, '乳製品多い': 1, '乳製品少ない': 1, '果物多い': 1, '水分摂取多い': 1, '淡白な食事を好むようになった': 1},
            '高血圧': {'不規則型': 1, '欠食型（朝食抜き）': 1, '夜食方(寝る前の食事）': 1, '早食い型': 1, '暴飲・暴食型': 1, '塩分': 1, '飲酒': 1, '野菜少ない': 1, '乳製品少ない': 1, '小魚少ない': 1, '水分摂取少ない': 1, '淡白な食事を好むようになった': 1},
            '糖尿病': {'不規則型': 1, '欠食型（朝食抜き）': 1, '夜食方(寝る前の食事）': 1, '暴飲・暴食型': 1, '外食多い型': 1, '脂肪': 1, '飲酒': 1, '飲酒(10年以上の大酒）': 1, '甘物': 1, '肉多い': 1, '洋食好み': 1, '野菜少ない': 1, '乳製品少ない': 1, '果物少ない': 1, '水分摂取少ない': 1, '淡白な食事を好むようになった': 1},
            '胃炎': {'不規則型': 1, '夜食方(寝る前の食事）': 1, '早食い型': 1, '暴飲・暴食型': 1, '飲酒時少食型': 1, '塩分': 1, '刺激物': 1, '焦げ目(肉＆魚）': 1, '熱物': 1, 'カフェイン': 1, '空腹時の清涼飲料水': 1, '肉多い': 1},
            '便秘': {'欠食型（朝食抜き）': 1, '柔・軟食': 1, '野菜少ない': 1, '乳製品少ない': 1, '小魚少ない': 1, '大豆製品少ない': 1, '加工食品やインスタント食品をよく食べる': 1, '水分摂取少ない': 1, '間食多い': 1},
            '肝臓疾患': {'不規則型': 1, '欠食型（朝食抜き）': 1, '夜食方(寝る前の食事）': 1, '早食い型': 1, '暴飲・暴食型': 1, '外食多い型': 1, '飲酒時少食型': 1, '脂肪': 1, '飲酒': 1, '飲酒(10年以上の大酒）': 1, '甘物': 1, '肉多い': 1, '洋食好み': 1, '野菜少ない': 1, '乳製品少ない': 1, '果物少ない': 1},
        }
        
        self.disease_db = pd.DataFrame(disease_data).fillna(0).T
        
        # ファイトケミカルデータをロード
        phytochemical_data = {
            '抗酸化作用': ['アントシアニン', 'ケルセチン', 'ルチン', 'カテキン', 'リコペン', 'ルテイン', 'アスタキサンチン'],
            '抗炎症作用': ['クルクミン', 'カプサイシン', 'ジンゲロール', 'ロズマリン酸', 'イソフラボン'],
            '肝臓保護': ['セサミン', 'クルクミン', 'カテキン', 'タウリン'],
            '血糖調節': ['クロロゲン酸', 'イソフラボン', 'カテキン', 'β-グルカン'],
            '血圧降下': ['カリウム豊富野菜', 'セサミン', 'ルチン', 'タウリン'],
            '消化促進': ['食物繊維豊富野菜', 'ジンゲロール', 'カプサイシン', 'リモネン'],
        }
        
        # ファイトケミカルと食品のマッピング
        self.phytochemical_foods = {
            'アントシアニン': ['ブルーベリー', 'ぶどう', 'ナスの皮', '赤じそ', '紫芋'],
            'ケルセチン': ['玉ねぎ', 'ブロッコリー', 'リンゴ', '緑茶'],
            'ルチン': ['そば', 'アスパラガス', 'ビーツ'],
            'カテキン': ['緑茶', '紅茶', 'ウーロン茶', 'カカオ'],
            'リコペン': ['トマト', 'スイカ', '柿', 'ピンクグレープフルーツ'],
            'ルテイン': ['ほうれん草', 'ケール', 'ブロッコリー', 'とうもろこし'],
            'アスタキサンチン': ['鮭', 'イクラ', 'エビ', 'カニ'],
            'クルクミン': ['ターメリック（ウコン）', 'ショウガ'],
            'カプサイシン': ['唐辛子', '赤ピーマン'],
            'ジンゲロール': ['ショウガ'],
            'ロズマリン酸': ['シソ', 'ローズマリー', 'レモンバーム'],
            'イソフラボン': ['大豆', '豆腐', '納豆', '豆乳'],
            'セサミン': ['ゴマ', 'ゴマ油'],
            'タウリン': ['イカ', 'タコ', '貝類', '魚介類'],
            'クロロゲン酸': ['コーヒー豆', 'ごぼう', 'さつま芋'],
            'β-グルカン': ['きのこ類', 'オーツ麦', '大麦'],
        }
        
        self.phytochemical_db = phytochemical_data
    
    def _create_symptom_mapping(self):
        """問診表の症状と食生活パターンのマッピングを作成"""
        self.symptom_mapping = {
            'めまいがする': ['不規則型', '欠食型（朝食抜き）', '水分摂取少ない'],
            '頭が痛い': ['不規則型', 'カフェイン', '水分摂取少ない'],
            '朝、関節がこわばって痛い': ['不規則型', '偏食型', '野菜少ない'],
            '体重が増える': ['不規則型', '暴飲・暴食型', '甘物', '間食多い'],
            '疲れがでてしまう': ['不規則型', '欠食型（朝食抜き）', '偏食型'],
            '眠れない': ['不規則型', 'カフェイン', '夜食方(寝る前の食事）'],
            '力がつかない': ['偏食型', '肉食べない', '魚介類食べない', '大豆製品少ない'],
            '60歳以上である': ['柔・軟食', '淡白な食事を好むようになった', '偏食型'],
            '身長が低くなりこない': ['カルシウム不足', '小魚少ない', '乳製品少ない'],
            '腹気が悪い腫瘍で痛いこと': ['刺激物', '脂肪', '暴飲・暴食型'],
            '住環境が悪い': ['外食多い型', '加工食品やインスタント食品をよく食べる'],
            '妊娠回数が多い': ['鉄分不足', '肉食べない', '魚介類食べない'],
            '輸血をした': ['たんぱく質不足', '鉄分豊富食品が必要'],
        }
    
    def analyze_questionnaire(self, questionnaire_data: Dict[str, bool]) -> Dict[str, float]:
        """問診表を分析して食生活パターンを特定"""
        
        # 症状から食生活パターンを推測
        diet_patterns = {}
        
        for symptom, present in questionnaire_data.items():
            if present and symptom in self.symptom_mapping:
                patterns = self.symptom_mapping[symptom]
                for pattern in patterns:
                    diet_patterns[pattern] = diet_patterns.get(pattern, 0) + 1
        
        # 重み付けして確率を計算
        total_symptoms = sum(questionnaire_data.values())
        if total_symptoms > 0:
            for pattern in diet_patterns:
                diet_patterns[pattern] = diet_patterns[pattern] / total_symptoms
        
        return diet_patterns
    
    def calculate_disease_risk(self, diet_patterns: Dict[str, float]) -> Dict[str, float]:
        """食生活パターンから病気リスクを計算"""
        
        disease_risks = {}
        
        for disease in self.disease_db.index:
            risk_score = 0
            total_weight = 0
            
            for pattern, user_value in diet_patterns.items():
                if pattern in self.disease_db.columns:
                    disease_value = self.disease_db.loc[disease, pattern]
                    if disease_value > 0:
                        risk_score += user_value * disease_value
                        total_weight += disease_value
            
            if total_weight > 0:
                disease_risks[disease] = min(risk_score / total_weight, 1.0)
            else:
                disease_risks[disease] = 0.0
        
        # リスクが高い順にソート
        disease_risks = dict(sorted(disease_risks.items(), 
                                   key=lambda x: x[1], 
                                   reverse=True))
        
        return disease_risks
    
    def recommend_phytochemicals(self, disease_risks: Dict[str, float], 
                                top_n: int = 5) -> Dict[str, List[str]]:
        """病気リスクに基づいてファイトケミカルを推奨"""
        
        # リスクが高い病気を取得
        high_risk_diseases = list(disease_risks.keys())[:top_n]
        
        recommendations = {}
        
        # 各病気に対する効果的なファイトケミカルをマッピング
        disease_to_phytochemicals = {
            '高血圧': ['抗酸化作用', '血圧降下', '抗炎症作用'],
            '糖尿病': ['血糖調節', '抗酸化作用', '抗炎症作用'],
            '肝臓疾患': ['肝臓保護', '抗酸化作用', '抗炎症作用'],
            '便秘': ['消化促進', '抗酸化作用'],
            '胃炎': ['抗炎症作用', '消化促進'],
            'アトピー性皮膚炎': ['抗炎症作用', '抗酸化作用'],
        }
        
        for disease in high_risk_diseases:
            if disease in disease_to_phytochemicals:
                phytochemical_types = disease_to_phytochemicals[disease]
                
                for p_type in phytochemical_types:
                    if p_type in self.phytochemical_db:
                        chemicals = self.phytochemical_db[p_type]
                        
                        # 各ファイトケミカルを含む食品を取得
                        food_recommendations = []
                        for chemical in chemicals:
                            if chemical in self.phytochemical_foods:
                                foods = self.phytochemical_foods[chemical]
                                food_recommendations.extend(foods)
                        
                        if food_recommendations:
                            key = f"{disease} ({p_type})"
                            recommendations[key] = list(set(food_recommendations))[:5]  # 重複排除して最大5つ
        
        return recommendations
    
    def generate_health_plan(self, questionnaire_data: Dict[str, bool]) -> Dict:
        """健康改善計画を生成"""
        
        # 1. 食生活パターンを分析
        diet_patterns = self.analyze_questionnaire(questionnaire_data)
        
        # 2. 病気リスクを計算
        disease_risks = self.calculate_disease_risk(diet_patterns)
        
        # 3. ファイトケミカルを推奨
        phytochemical_recommendations = self.recommend_phytochemicals(disease_risks)
        
        # 4. 食事改善アドバイスを生成
        diet_advice = self._generate_diet_advice(diet_patterns)
        
        return {
            "identified_diet_patterns": diet_patterns,
            "disease_risks": disease_risks,
            "phytochemical_recommendations": phytochemical_recommendations,
            "diet_improvement_advice": diet_advice,
            "overall_risk_level": self._calculate_overall_risk(disease_risks)
        }
    
    def _generate_diet_advice(self, diet_patterns: Dict[str, float]) -> List[str]:
        """食事改善アドバイスを生成"""
        
        advice = []
        
        advice_mapping = {
            '不規則型': "食事時間を規則正しくしましょう。1日3食を決まった時間に摂取してください。",
            '欠食型（朝食抜き）': "朝食を必ず摂りましょう。簡単なバナナやヨーグルトでもOKです。",
            '夜食方(寝る前の食事）': "寝る3時間前には食事を終えましょう。",
            '早食い型': "一口20回以上噛むことを心がけ、ゆっくり食事を楽しみましょう。",
            '偏食型': "様々な色の野菜を摂るように心がけ、栄養バランスを改善しましょう。",
            '塩分': "塩分控えめを心がけ、だしや香辛料で味に変化をつけましょう。",
            '脂肪': "脂っこい食事を減らし、魚や植物性の油を積極的に摂りましょう。",
            '野菜少ない': "1日350g以上の野菜を目標に、特に緑黄色野菜を積極的に摂りましょう。",
            '水分摂取少ない': "1日1.5-2Lの水分をこまめに摂取しましょう。",
        }
        
        # 最も頻度の高い食生活パターンからアドバイスを生成
        sorted_patterns = sorted(diet_patterns.items(), key=lambda x: x[1], reverse=True)
        
        for pattern, score in sorted_patterns[:3]:  # 上位3つ
            if pattern in advice_mapping and score > 0.3:
                advice.append(advice_mapping[pattern])
        
        return advice
    
    def _calculate_overall_risk(self, disease_risks: Dict[str, float]) -> str:
        """総合リスクレベルを計算"""
        
        high_risks = [risk for risk in disease_risks.values() if risk > 0.7]
        medium_risks = [risk for risk in disease_risks.values() if 0.4 <= risk <= 0.7]
        
        if high_risks:
            return "高リスク - 専門家のアドバイスを求めましょう"
        elif medium_risks:
            return "中リスク - 生活習慣の改善が必要です"
        else:
            return "低リスク - 現在の習慣を維持しましょう"


class InteractiveQuestionnaire:
    """インタラクティブな問診システム"""
    
    def __init__(self, inference_engine: HealthInferenceEngine):
        self.engine = inference_engine
        self.questions = self._load_questions()
    
    def _load_questions(self):
        """問診項目をロード"""
        return {
            '60歳以上である': "60歳以上ですか？",
            'めまいがする': "めまいを感じることがありますか？",
            '頭が痛い': "頭痛に悩まされることがありますか？",
            '朝、関節がこわばって痛い': "朝、関節がこわばったり痛んだりしますか？",
            '体重が増える': "最近、体重が増加傾向にありますか？",
            '疲れがでてしまう': "疲れがなかなか取れませんか？",
            '眠れない': "睡眠に問題がありますか？",
            '力がつかない': "体に力が入らない感じがしますか？",
            '腹気が悪い腫瘍で痛いこと': "お腹の調子が悪いことがありますか？",
            '住環境が悪い': "住環境に不満がありますか？（騒音、日当たりなど）",
            '輸血をした': "過去に輸血を受けたことがありますか？",
        }
    
    def conduct_interview(self):
        """インタラクティブに問診を実施"""
        print("=== 健康状態問診 ===\n")
        print("以下の質問に「はい」か「いいえ」でお答えください。\n")
        
        responses = {}
        
        for key, question in self.questions.items():
            while True:
                answer = input(f"{question} (はい/いいえ): ").strip().lower()
                if answer in ['はい', 'yes', 'y']:
                    responses[key] = True
                    break
                elif answer in ['いいえ', 'no', 'n']:
                    responses[key] = False
                    break
                else:
                    print("「はい」か「いいえ」で答えてください。")
        
        return responses
    
    def display_results(self, health_plan: Dict):
        """結果を表示"""
        print("\n" + "="*50)
        print("推論結果")
        print("="*50)
        
        print("\n1. 識別された食生活パターン:")
        for pattern, score in health_plan['identified_diet_patterns'].items():
            if score > 0.1:
                print(f"  - {pattern}: {score:.1%}")
        
        print("\n2. 病気リスク評価:")
        for disease, risk in list(health_plan['disease_risks'].items())[:5]:
            if risk > 0.2:
                risk_level = "高" if risk > 0.7 else "中" if risk > 0.4 else "低"
                print(f"  - {disease}: {risk:.1%} ({risk_level}リスク)")
        
        print("\n3. 推奨ファイトケミカルと食品:")
        for category, foods in health_plan['phytochemical_recommendations'].items():
            print(f"  - {category}:")
            for food in foods:
                print(f"    • {food}")
        
        print("\n4. 食事改善アドバイス:")
        for i, advice in enumerate(health_plan['diet_improvement_advice'], 1):
            print(f"  {i}. {advice}")
        
        print(f"\n5. 総合リスクレベル: {health_plan['overall_risk_level']}")
        print("\n" + "="*50)


# 使用例
def main():
    # 推論エンジンを初期化
    engine = HealthInferenceEngine()
    
    # インタラクティブ問診システム
    questionnaire = InteractiveQuestionnaire(engine)
    
    # 問診を実施
    responses = questionnaire.conduct_interview()
    
    # 健康改善計画を生成
    health_plan = engine.generate_health_plan(responses)
    
    # 結果を表示
    questionnaire.display_results(health_plan)
    
    # 詳細データをJSONで保存（オプション）
    with open('health_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(health_plan, f, ensure_ascii=False, indent=2)
    
    print("\n詳細分析結果は 'health_analysis.json' に保存されました。")

if __name__ == "__main__":
    main()
```

## 拡張機能の実装

```python
class AdvancedHealthInferenceEngine(HealthInferenceEngine):
    """拡張版健康推論エンジン"""
    
    def __init__(self):
        super().__init__()
        self._load_advanced_databases()
    
    def _load_advanced_databases(self):
        """詳細なデータベースをロード"""
        # 詳細な病気と症状のマッピング
        self.symptom_to_disease = {
            'めまい': ['高血圧', '貧血', '低血圧', 'メニエール病'],
            '頭痛': ['高血圧', '片頭痛', '緊張性頭痛', '脳血管疾患'],
            '関節痛': ['関節リウマチ', '痛風', '変形性関節症'],
            '疲労感': ['貧血', '甲状腺機能低下症', '糖尿病', '慢性疲労症候群'],
            '不眠': ['不安障害', 'うつ病', '睡眠時無呼吸症候群'],
            '体重増加': ['甲状腺機能低下症', '糖尿病', 'メタボリックシンドローム'],
            '腹痛': ['胃炎', '胃潰瘍', '過敏性腸症候群', '胆石症'],
        }
        
        # 症状の重症度評価
        self.symptom_severity = {
            '高': ['激しい痛み', '意識消失', '呼吸困難'],
            '中': ['持続する症状', '日常生活に支障'],
            '低': ['一時的な症状', '軽度の不快感'],
        }
    
    def analyze_symptom_patterns(self, symptoms: Dict[str, Tuple[bool, str]]) -> Dict:
        """症状パターンを詳細分析"""
        # 症状の存在と重症度を考慮
        pattern_analysis = {}
        
        for symptom, (present, severity) in symptoms.items():
            if present:
                # 症状から関連する病気を特定
                if symptom in self.symptom_to_disease:
                    related_diseases = self.symptom_to_disease[symptom]
                    
                    # 重症度に応じて重み付け
                    severity_weight = {'高': 1.0, '中': 0.7, '低': 0.4}.get(severity, 0.5)
                    
                    for disease in related_diseases:
                        pattern_analysis[disease] = pattern_analysis.get(disease, 0) + severity_weight
        
        return pattern_analysis
    
    def generate_personalized_meal_plan(self, health_plan: Dict, 
                                      preferences: List[str] = None) -> Dict:
        """個人に合わせた食事計画を生成"""
        
        base_recommendations = health_plan['phytochemical_recommendations']
        
        # 食事パターンに基づく提案
        meal_plan = {
            '朝食': [],
            '昼食': [],
            '夕食': [],
            '間食': []
        }
        
        # ファイトケミカルを食事に組み込む
        all_foods = []
        for foods in base_recommendations.values():
            all_foods.extend(foods)
        
        # 重複排除
        unique_foods = list(set(all_foods))
        
        # 食事ごとに分配（簡易版）
        if unique_foods:
            meal_plan['朝食'] = unique_foods[:2]
            meal_plan['昼食'] = unique_foods[2:4]
            meal_plan['夕食'] = unique_foods[4:6]
            meal_plan['間食'] = ['ナッツ類', 'ヨーグルト', 'フルーツ']
        
        # 嗜好を考慮
        if preferences:
            for category in meal_plan:
                meal_plan[category] = [food for food in meal_plan[category] 
                                      if not any(pref.lower() in food.lower() 
                                               for pref in preferences if '嫌い' in pref)]
        
        return meal_plan
    
    def track_progress(self, initial_plan: Dict, follow_up_data: Dict) -> Dict:
        """経過を追跡し改善度を評価"""
        
        improvements = {}
        
        # 食生活パターンの改善を評価
        initial_patterns = initial_plan['identified_diet_patterns']
        
        if 'current_patterns' in follow_up_data:
            current_patterns = follow_up_data['current_patterns']
            
            for pattern in initial_patterns:
                if pattern in current_patterns:
                    improvement = initial_patterns[pattern] - current_patterns[pattern]
                    if improvement > 0:
                        improvements[pattern] = improvement
        
        # 症状の改善を評価
        if 'symptom_improvement' in follow_up_data:
            improvements['symptom_relief'] = follow_up_data['symptom_improvement']
        
        # 総合評価
        total_improvement = sum(improvements.values()) / len(improvements) if improvements else 0
        
        return {
            'improvements': improvements,
            'total_improvement_score': total_improvement,
            'recommendation': self._generate_follow_up_recommendation(total_improvement)
        }
    
    def _generate_follow_up_recommendation(self, improvement_score: float) -> str:
        """フォローアップ推奨を生成"""
        if improvement_score > 0.7:
            return "素晴らしい改善です！現在の習慣を維持してください。"
        elif improvement_score > 0.4:
            return "良い改善が見られます。さらに継続しましょう。"
        elif improvement_score > 0.1:
            return "少しずつ改善しています。継続が大切です。"
        else:
            return "改善が見られません。生活習慣を見直してみましょう。"


# Web API用の実装例
from flask import Flask, request, jsonify

app = Flask(__name__)
engine = AdvancedHealthInferenceEngine()

@app.route('/analyze_health', methods=['POST'])
def analyze_health():
    """健康分析API"""
    try:
        data = request.json
        
        if 'questionnaire_responses' not in data:
            return jsonify({'error': '問診データが必要です'}), 400
        
        # 健康分析を実行
        health_plan = engine.generate_health_plan(data['questionnaire_responses'])
        
        # 必要に応じて詳細分析
        if 'detailed_symptoms' in data:
            symptom_analysis = engine.analyze_symptom_patterns(data['detailed_symptoms'])
            health_plan['symptom_analysis'] = symptom_analysis
        
        if 'food_preferences' in data:
            meal_plan = engine.generate_personalized_meal_plan(
                health_plan, 
                data['food_preferences']
            )
            health_plan['personalized_meal_plan'] = meal_plan
        
        return jsonify(health_plan)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/track_progress', methods=['POST'])
def track_progress():
    """進捗追跡API"""
    try:
        data = request.json
        
        if 'initial_plan' not in data or 'follow_up_data' not in data:
            return jsonify({'error': '初期計画と追跡データが必要です'}), 400
        
        progress = engine.track_progress(data['initial_plan'], data['follow_up_data'])
        
        return jsonify(progress)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # コマンドラインインターフェース
    print("健康推論システム")
    print("1. 健康分析を実行")
    print("2. 進捗を追跡")
    print("3. Webサーバーを起動")
    
    choice = input("選択してください (1-3): ")
    
    if choice == '1':
        main()
    elif choice == '2':
        # 進捗追跡の例
        engine = AdvancedHealthInferenceEngine()
        
        # サンプルデータ
        initial_plan = {
            'identified_diet_patterns': {'不規則型': 0.8, '偏食型': 0.6},
            'disease_risks': {'高血圧': 0.7, '糖尿病': 0.5}
        }
        
        follow_up = {
            'current_patterns': {'不規則型': 0.4, '偏食型': 0.3},
            'symptom_improvement': 0.6
        }
        
        progress = engine.track_progress(initial_plan, follow_up)
        print("\n進捗評価:")
        print(json.dumps(progress, ensure_ascii=False, indent=2))
    
    elif choice == '3':
        app.run(debug=True, port=5000)
```

## 実行手順

1. **必要なライブラリのインストール**:
```bash
pip install pandas numpy flask
```

2. **基本的な使用方法**:
```python
# エンジンの初期化
engine = HealthInferenceEngine()

# 問診データの準備（例）
questionnaire_data = {
    '60歳以上である': True,
    'めまいがする': True,
    '頭が痛い': True,
    '朝、関節がこわばって痛い': False,
    '体重が増える': True,
    '疲れがでてしまう': True,
    '眠れない': False,
    '力がつかない': True,
    '腹気が悪い腫瘍で痛いこと': False,
    '住環境が悪い': True,
    '輸血をした': False,
}

# 健康分析の実行
health_plan = engine.generate_health_plan(questionnaire_data)

# 結果の表示
import json
print(json.dumps(health_plan, ensure_ascii=False, indent=2))
```

## システムの特徴

1. **多層的な分析**:
   - 症状→食生活パターン→病気リスク→栄養推奨の流れ

2. **パーソナライズされた推奨**:
   - 個人の症状と生活習慣に基づいた提案

3. **科学的根拠に基づく**:
   - ファイトケミカルの研究データを活用

4. **実用的なアドバイス**:
   - 具体的な食品と食事パターンの提案

5. **拡張性**:
   - 新しいデータの追加が容易
   - API対応でWebサービス化可能

このシステムは、問診データを入力すると、関連する病気リスクを特定し、それに対応するファイトケミカルを含む食品を推奨します。定期的な使用で健康状態の改善を追跡することも可能です。

[[HB3. 基本の使い方]]
