最初のコードを試してみました。２つ目のコードをどのように使えばいいですか？

---

２つ目のコード（拡張版）は以下のように使うことができます：

## 基本の使い方

### 1. **拡張エンジン単体で使用する場合**

```python
# AdvancedHealthInferenceEngineクラスをインポート
from your_module import AdvancedHealthInferenceEngine  # ファイル名に置き換えてください

# 拡張エンジンの初期化
advanced_engine = AdvancedHealthInferenceEngine()

# 問診データの準備（症状の詳細情報を含む）
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

# 基本の健康分析（最初のコードと同様）
health_plan = advanced_engine.generate_health_plan(questionnaire_data)

# 症状の詳細分析（追加機能）
detailed_symptoms = {
    'めまい': (True, '中'),  # (存在するか, 重症度: 高/中/低)
    '頭痛': (True, '高'),
    '関節痛': (False, '低'),
    '疲労感': (True, '中'),
    '不眠': (False, '低'),
    '体重増加': (True, '中'),
    '腹痛': (False, '低')
}

symptom_analysis = advanced_engine.analyze_symptom_patterns(detailed_symptoms)
print("症状詳細分析:", symptom_analysis)

# パーソナライズされた食事計画（追加機能）
food_preferences = ['にんにく嫌い', '魚嫌い']  # 嫌いなものを指定
meal_plan = advanced_engine.generate_personalized_meal_plan(health_plan, food_preferences)
print("パーソナライズされた食事計画:", meal_plan)

# 進捗追跡（追加機能）
initial_plan = health_plan
follow_up_data = {
    'current_patterns': {'不規則型': 0.3, '偏食型': 0.2},  # 改善後の食生活パターン
    'symptom_improvement': 0.5  # 症状改善度（0-1）
}

progress = advanced_engine.track_progress(initial_plan, follow_up_data)
print("進捗評価:", progress)
```

### 2. **Web APIとして使用する場合**

```python
# Flaskをインストール
# pip install flask

# 2つ目のコード全体をhealth_api.pyとして保存し、実行
# python health_api.py

# 実行後、コンソールから3を選択してWebサーバーを起動
```

起動後、以下のAPIエンドポイントを使用できます：

#### APIエンドポイント

**健康分析API**:
```bash
curl -X POST http://localhost:5000/analyze_health \
  -H "Content-Type: application/json" \
  -d '{
    "questionnaire_responses": {
      "60歳以上である": true,
      "めまいがする": true,
      "頭が痛い": true,
      "朝、関節がこわばって痛い": false,
      "体重が増える": true,
      "疲れがでてしまう": true,
      "眠れない": false,
      "力がつかない": true,
      "腹気が悪い腫瘍で痛いこと": false,
      "住環境が悪い": true,
      "輸血をした": false
    },
    "detailed_symptoms": {
      "めまい": [true, "中"],
      "頭痛": [true, "高"]
    },
    "food_preferences": ["にんにく嫌い", "魚嫌い"]
  }'
```

**進捗追跡API**:
```bash
curl -X POST http://localhost:5000/track_progress \
  -H "Content-Type: application/json" \
  -d '{
    "initial_plan": {
      "identified_diet_patterns": {"不規則型": 0.8, "偏食型": 0.6},
      "disease_risks": {"高血圧": 0.7, "糖尿病": 0.5}
    },
    "follow_up_data": {
      "current_patterns": {"不規則型": 0.4, "偏食型": 0.3},
      "symptom_improvement": 0.6
    }
  }'
```

### 3. **対話型CLIとして使用する場合**

```python
# 2つ目のコードを実行し、コンソールで選択肢から操作

# 実行時に表示されるメニュー:
# 健康推論システム
# 1. 健康分析を実行
# 2. 進捗を追跡
# 3. Webサーバーを起動

# 1を選択: 最初のコードと同じインタラクティブ問診が実行されます
# 2を選択: 進捗追跡の例が実行されます
# 3を選択: Flaskサーバーが起動します
```

## 完全な使用例

以下は、すべての機能を組み合わせた完全な使用例です：

```python
import json

# AdvancedHealthInferenceEngineクラスをインポート
# 注: 実際にはファイルを分割してimportする必要があります
# from advanced_health_engine import AdvancedHealthInferenceEngine

# 代わりに、2つ目のコード全体をhealth_engine.pyとして保存し、
# from health_engine import AdvancedHealthInferenceEngine でインポート

# 拡張エンジンの作成
engine = AdvancedHealthInferenceEngine()

def complete_example():
    print("=== 完全な健康分析例 ===\n")
    
    # 1. 基本の問診データ
    questionnaire = {
        '60歳以上である': True,
        'めまいがする': True,
        '頭が痛い': True,
        '朝、関節がこわばって痛い': True,
        '体重が増える': True,
        '疲れがでてしまう': True,
        '眠れない': True,
        '力がつかない': True,
        '腹気が悪い腫瘍で痛いこと': False,
        '住環境が悪い': False,
        '輸血をした': False,
    }
    
    # 2. 詳細症状データ
    detailed_symptoms = {
        'めまい': (True, '中'),      # 症状あり、中程度
        '頭痛': (True, '高'),        # 症状あり、重度
        '関節痛': (True, '中'),      # 症状あり、中程度
        '疲労感': (True, '高'),      # 症状あり、重度
        '不眠': (True, '中'),        # 症状あり、中程度
        '体重増加': (True, '中'),    # 症状あり、中程度
        '腹痛': (False, '低'),       # 症状なし
    }
    
    # 3. 食品嗜好
    preferences = [
        'にんにく嫌い',      # にんにくが嫌い
        '乳製品苦手',        # 乳製品が苦手
        '魚好き',            # 魚は好き
        '野菜好き'           # 野菜は好き
    ]
    
    # 4. 基本分析の実行
    print("1. 基本健康分析を実行中...")
    basic_plan = engine.generate_health_plan(questionnaire)
    
    # 5. 症状詳細分析
    print("2. 症状詳細分析を実行中...")
    symptom_analysis = engine.analyze_symptom_patterns(detailed_symptoms)
    
    # 6. パーソナライズされた食事計画
    print("3. パーソナライズされた食事計画を作成中...")
    meal_plan = engine.generate_personalized_meal_plan(basic_plan, preferences)
    
    # 7. 結果の表示
    print("\n" + "="*60)
    print("分析結果まとめ")
    print("="*60)
    
    print("\nA. 識別された食生活パターン:")
    for pattern, score in basic_plan['identified_diet_patterns'].items():
        if score > 0.2:
            print(f"  - {pattern}: {score:.1%}")
    
    print("\nB. 病気リスク（上位5件）:")
    for i, (disease, risk) in enumerate(list(basic_plan['disease_risks'].items())[:5]):
        print(f"  {i+1}. {disease}: {risk:.1%}")
    
    print("\nC. 症状分析結果:")
    for disease, score in sorted(symptom_analysis.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"  - {disease}: 関連度 {score:.2f}")
    
    print("\nD. 推奨食事計画:")
    for time, foods in meal_plan.items():
        if foods:
            print(f"  {time}:")
            for food in foods:
                print(f"    • {food}")
    
    print("\nE. 食事改善アドバイス:")
    for i, advice in enumerate(basic_plan['diet_improvement_advice'], 1):
        print(f"  {i}. {advice}")
    
    print(f"\nF. 総合リスク: {basic_plan['overall_risk_level']}")
    
    # 8. データの保存
    with open('complete_health_analysis.json', 'w', encoding='utf-8') as f:
        result = {
            'basic_analysis': basic_plan,
            'symptom_analysis': symptom_analysis,
            'personalized_meal_plan': meal_plan
        }
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print("\n詳細結果は 'complete_health_analysis.json' に保存されました。")
    
    return basic_plan, symptom_analysis, meal_plan


def follow_up_example(initial_plan):
    """経過追跡の例"""
    print("\n" + "="*60)
    print("3ヶ月後の経過追跡")
    print("="*60)
    
    # フォローアップデータ（3ヶ月後）
    follow_up = {
        'current_patterns': {
            '不規則型': 0.3,      # 改善（0.8 → 0.3）
            '偏食型': 0.4,        # 改善（0.6 → 0.4）
            '水分摂取少ない': 0.2,  # 新たに計測
        },
        'symptom_improvement': 0.7  # 症状が70%改善
    }
    
    # 進捗評価
    progress = engine.track_progress(initial_plan, follow_up)
    
    print("\n進捗評価結果:")
    print(f"総合改善スコア: {progress['total_improvement_score']:.1%}")
    print(f"推奨: {progress['recommendation']}")
    
    print("\n具体的な改善点:")
    for pattern, improvement in progress['improvements'].items():
        print(f"  - {pattern}: {improvement:.1%} 改善")
    
    return progress


if __name__ == "__main__":
    # 完全な分析の実行
    basic_plan, symptom_analysis, meal_plan = complete_example()
    
    # 経過追跡の例を実行
    follow_up_example(basic_plan)
```

## ファイル構成の提案

複数のファイルに分割して管理することをお勧めします：

```
health_system/
├── main.py                    # メイン実行ファイル
├── health_engine.py          # 基本エンジン（最初のコード）
├── advanced_engine.py        # 拡張エンジン（2つ目のコードのクラス部分）
├── api.py                    # Flask API部分
├── data/
│   ├── disease_db.json       # 病気データベース
│   ├── phytochemical_db.json # ファイトケミカルデータ
│   └── symptom_mapping.json  # 症状マッピング
└── results/
    └── *.json                # 分析結果
```

**main.py**:
```python
from advanced_engine import AdvancedHealthInferenceEngine
from api import app  # Flaskアプリ

# CLIインターフェース
def main():
    engine = AdvancedHealthInferenceEngine()
    # ... 対話型コード ...

if __name__ == "__main__":
    # コマンドライン引数で実行モードを選択
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "api":
        app.run(debug=True, port=5000)
    else:
        main()
```

このように構成すると、以下のように実行できます：

```bash
# CLIモードで実行
python main.py

# Web APIモードで実行
python main.py api
```

## 実際に試すための簡易版

2つ目のコードをすぐに試すには：

```python
# 1. 2つ目のコード全体を health_system.py として保存
# 2. 以下を実行

python health_system.py

# コンソールで表示されるメニューから選択：
# 1 → 対話型問診（最初のコードと同じ）
# 2 → 進捗追跡のデモ
# 3 → Webサーバー起動（localhost:5000）

# Webサーバー起動後、ブラウザやcurlでAPIにアクセス可能
```

特に **Web APIとして使用** するのが便利です。ブラウザからは直接POSTできないので、以下のツールを使うことをお勧めします：

1. **Postman** (デスクトップアプリ)
2. **curl** (コマンドラインツール)
3. **Python requestsライブラリ**
4. **VS CodeのREST Client拡張機能**

どの使用法についてもっと詳しく知りたい場合は、具体的な部分を教えてください。

[[HB4. コードの構造詳細]]
