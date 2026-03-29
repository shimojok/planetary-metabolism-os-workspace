各コードの構造と、パソコンにインストールするツール、総合的な使い方を教えて下さい。

---

各コードの構造と、インストール方法、総合的な使い方を詳しく説明します。

## 1. コードの構造詳細

### 基本版コード（最初のコード）
```
HealthInferenceEngine
├── __init__()
│   └── データベース初期化
├── _load_databases()
│   ├── disease_db（病気データ）
│   └── phytochemical_db（ファイトケミカルデータ）
├── _create_symptom_mapping()
│   └── 症状と食生活パターンのマッピング作成
├── analyze_questionnaire()
│   └── 問診データ→食生活パターン変換
├── calculate_disease_risk()
│   └── 食生活パターン→病気リスク計算
├── recommend_phytochemicals()
│   └── 病気リスク→ファイトケミカル推奨
├── generate_health_plan()
│   └── 統合的健康分析実行
├── _generate_diet_advice()
│   └── 食事改善アドバイス生成
└── _calculate_overall_risk()
    └── 総合リスク評価

InteractiveQuestionnaire
├── conduct_interview()
│   └── 対話型問診実施
└── display_results()
    └── 結果表示
```

### 拡張版コード（2つ目のコード）
```
AdvancedHealthInferenceEngine (基本版を継承)
├── _load_advanced_databases()
│   ├── symptom_to_disease（詳細な症状-病気マッピング）
│   └── symptom_severity（症状重症度評価）
├── analyze_symptom_patterns()
│   └── 症状パターンの詳細分析
├── generate_personalized_meal_plan()
│   └── 個人に合わせた食事計画生成
├── track_progress()
│   └── 経過追跡と改善評価
└── _generate_follow_up_recommendation()
    └── フォローアップ推奨生成

Flask Web API
├── /analyze_health (POST)
│   └── 健康分析APIエンドポイント
└── /track_progress (POST)
    └── 進捗追跡APIエンドポイント
```

## 2. インストールするツール

### 必須ツール
```bash
# 1. Pythonのインストール（バージョン3.8以上）
# https://www.python.org/downloads/

# 2. 仮想環境の作成（推奨）
python -m venv health_env

# Windowsの場合:
health_env\Scripts\activate

# Mac/Linuxの場合:
source health_env/bin/activate

# 3. 必要なPythonライブラリのインストール
pip install pandas numpy flask openpyxl python-docx

# PDF処理用（オプション）
pip install PyPDF2 pdfplumber
```

### 推奨開発ツール
```bash
# コードエディタ
# - VS Code: https://code.visualstudio.com/
# - PyCharm: https://www.jetbrains.com/pycharm/

# APIテストツール
# - Postman: https://www.postman.com/
# - curl (コマンドライン)
# - VS CodeのREST Client拡張

# バージョン管理
# - Git: https://git-scm.com/
```

## 3. ファイル構成とセットアップ手順

### プロジェクトフォルダ構成
```
health_inference_system/
├── requirements.txt          # 依存パッケージリスト
├── README.md                # プロジェクト説明
├── config/
│   ├── diseases.json        # 病気データ
│   ├── phytochemicals.json  # ファイトケミカルデータ
│   └── symptoms_mapping.json # 症状マッピング
├── src/
│   ├── __init__.py
│   ├── base_engine.py       # 基本エンジン
│   ├── advanced_engine.py   # 拡張エンジン
│   ├── data_loader.py       # データ読み込み
│   ├── api_server.py        # Web API
│   └── cli_interface.py     # コマンドラインインターフェース
├── data/
│   ├── sample_questionnaire.xlsx  # サンプル問診データ
│   └── sample_diet.xlsx     # サンプル食事データ
├── scripts/
│   ├── setup.py             # セットアップスクリプト
│   └── import_data.py       # データインポート
├── tests/
│   ├── test_engine.py       # テストコード
│   └── test_api.py          # APIテスト
└── results/
    └── *.json               # 分析結果出力先
```

### セットアップスクリプト（setup.py）
```python
#!/usr/bin/env python3
"""
健康推論システムセットアップスクリプト
"""

import os
import sys
import json
import shutil
from pathlib import Path

def setup_project():
    """プロジェクトをセットアップ"""
    
    # プロジェクトディレクトリ作成
    directories = [
        'config',
        'src',
        'data',
        'scripts',
        'tests',
        'results',
        'logs'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ ディレクトリ作成: {directory}")
    
    # 設定ファイル作成
    configs = {
        'config/diseases.json': {
            "高血圧": {
                "risk_factors": ["不規則型", "塩分", "野菜少ない"],
                "recommended_phytochemicals": ["カリウム", "マグネシウム", "食物繊維"],
                "severity_levels": {"低": 0.3, "中": 0.6, "高": 0.8}
            },
            "糖尿病": {
                "risk_factors": ["甘物", "間食多い", "運動不足"],
                "recommended_phytochemicals": ["クロム", "亜鉛", "α-リポ酸"],
                "severity_levels": {"低": 0.2, "中": 0.5, "高": 0.7}
            }
        },
        
        'config/phytochemicals.json': {
            "抗酸化作用": {
                "components": ["ビタミンC", "ビタミンE", "β-カロテン"],
                "foods": ["ブルーベリー", "ほうれん草", "ナッツ"],
                "benefits": ["細胞保護", "老化防止", "免疫力向上"]
            },
            "抗炎症作用": {
                "components": ["オメガ3", "クルクミン", "カテキン"],
                "foods": ["青魚", "ターメリック", "緑茶"],
                "benefits": ["炎症抑制", "痛み緩和", "関節保護"]
            }
        }
    }
    
    for filename, content in configs.items():
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        print(f"✓ 設定ファイル作成: {filename}")
    
    # requirements.txt作成
    requirements = [
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "flask>=2.0.0",
        "openpyxl>=3.0.0",
        "python-dotenv>=0.19.0",
        "requests>=2.26.0"
    ]
    
    with open('requirements.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(requirements))
    print("✓ requirements.txt 作成")
    
    # README.md作成
    readme_content = """# 健康推論システム

## 概要
問診データから病気リスクを分析し、ファイトケミカルを推奨するシステム

## セットアップ
```
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

## 使用方法
```
# コマンドラインインターフェース
python src/cli_interface.py

# Web API起動
python src/api_server.py

# サンプルデータインポート
python scripts/import_data.py
```

## データ形式
- 問診データ: JSONまたはExcel形式
- 結果出力: JSON形式
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("✓ README.md 作成")
    
    print("\n✅ セットアップ完了！")
    print("次のコマンドで開始:")
    print("1. pip install -r requirements.txt")
    print("2. python src/cli_interface.py")

if __name__ == "__main__":
    setup_project()
```

## 4. 総合的な使い方

### 方法1: コマンドラインインターフェース（CLI）

```python
# cli_interface.py
import argparse
import json
from src.advanced_engine import AdvancedHealthInferenceEngine

def main():
    parser = argparse.ArgumentParser(description='健康推論システム')
    parser.add_argument('mode', choices=['analyze', 'track', 'report'], 
                       help='実行モード')
    parser.add_argument('--input', '-i', help='入力ファイル')
    parser.add_argument('--output', '-o', default='result.json', 
                       help='出力ファイル')
    parser.add_argument('--format', '-f', choices=['json', 'csv', 'html'], 
                       default='json', help='出力形式')
    
    args = parser.parse_args()
    engine = AdvancedHealthInferenceEngine()
    
    if args.mode == 'analyze':
        if args.input:
            with open(args.input, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            # 対話型入力
            data = interactive_input()
        
        result = engine.generate_health_plan(data)
        save_result(result, args.output, args.format)
        
    elif args.mode == 'track':
        # 進捗追跡
        pass
    
    print(f"分析完了！結果: {args.output}")

if __name__ == "__main__":
    main()
```

**使用方法:**
```bash
# 対話型分析
python cli_interface.py analyze

# ファイルから分析
python cli_interface.py analyze -i questionnaire.json -o result.json

# HTMLレポート生成
python cli_interface.py analyze -i data.json -o report.html -f html
```

### 方法2: Web APIサーバー

```python
# api_server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.advanced_engine import AdvancedHealthInferenceEngine

app = Flask(__name__)
CORS(app)  # CORS対応
engine = AdvancedHealthInferenceEngine()

@app.route('/api/health/analyze', methods=['POST'])
def analyze_health():
    """健康分析API"""
    try:
        data = request.get_json()
        result = engine.generate_health_plan(data['responses'])
        return jsonify({"success": True, "data": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/api/health/track', methods=['POST'])
def track_progress():
    """進捗追跡API"""
    try:
        data = request.get_json()
        result = engine.track_progress(data['initial'], data['current'])
        return jsonify({"success": True, "data": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/api/health/recommendations', methods=['GET'])
def get_recommendations():
    """推奨食品リスト取得API"""
    disease = request.args.get('disease', '')
    severity = request.args.get('severity', 'medium')
    
    recommendations = engine.get_disease_recommendations(disease, severity)
    return jsonify({"success": True, "recommendations": recommendations})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

**使用方法:**
```bash
# サーバー起動
python api_server.py

# 別ターミナルでAPI呼び出し
curl -X POST http://localhost:5000/api/health/analyze \
  -H "Content-Type: application/json" \
  -d '{"responses": {"60歳以上": true, "めまい": true}}'
```

### 方法3: スケジュール実行（定期分析）

```python
# scheduler.py
import schedule
import time
import json
from datetime import datetime
from src.advanced_engine import AdvancedHealthInferenceEngine

def daily_analysis():
    """毎日の自動分析"""
    print(f"[{datetime.now()}] 毎日の健康分析を開始...")
    
    engine = AdvancedHealthInferenceEngine()
    
    # 前回のデータ読み込み
    try:
        with open('data/latest_questionnaire.json', 'r') as f:
            data = json.load(f)
    except:
        print("前回データなし。デフォルト分析を実行")
        return
    
    # 分析実行
    result = engine.generate_health_plan(data)
    
    # 結果保存
    filename = f"results/daily_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"結果を {filename} に保存しました")

def weekly_report():
    """週次レポート生成"""
    print(f"[{datetime.now()}] 週次レポート生成...")
    # 過去7日間のデータを集計
    pass

def monthly_summary():
    """月次サマリー生成"""
    print(f"[{datetime.now()}] 月次サマリー生成...")
    # 過去30日間のデータを分析
    pass

# スケジュール設定
schedule.every().day.at("09:00").do(daily_analysis)
schedule.every().monday.at("10:00").do(weekly_report)
schedule.every().month.at("10:00").do(monthly_summary)

if __name__ == "__main__":
    print("スケジュール実行開始...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # 1分ごとにチェック
```

### 方法4: Jupyter Notebookでの分析

```python
# notebook_analysis.ipynb

# セル1: インポート
import sys
sys.path.append('../src')
from advanced_engine import AdvancedHealthInferenceEngine
import pandas as pd
import matplotlib.pyplot as plt

# セル2: エンジン初期化
engine = AdvancedHealthInferenceEngine()

# セル3: データ読み込み
import json
with open('../data/sample_data.json', 'r', encoding='utf-8') as f:
    questionnaire_data = json.load(f)

# セル4: 分析実行
results = engine.generate_health_plan(questionnaire_data)

# セル5: 可視化
risks = pd.Series(results['disease_risks'])
risks[risks > 0.1].plot(kind='bar', figsize=(10, 6))
plt.title('疾病リスク分析')
plt.ylabel('リスクスコア')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## 5. 完全な実行手順

### ステップ1: 環境構築
```bash
# 1. プロジェクトフォルダ作成
mkdir health_inference_system
cd health_inference_system

# 2. 仮想環境作成
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3. 必須パッケージインストール
pip install pandas numpy flask openpyxl

# 4. プロジェクト構成作成
python setup.py  # 上記のセットアップスクリプトを実行
```

### ステップ2: コード配置
```
# src/base_engine.py に基本エンジンのコードを保存
# src/advanced_engine.py に拡張エンジンのコードを保存
# api_server.py にFlask APIコードを保存
# cli_interface.py にCLIコードを保存
```

### ステップ3: データ準備
```bash
# サンプル問診データ作成
echo '{
  "60歳以上である": true,
  "めまいがする": true,
  "頭が痛い": true,
  "疲れがでてしまう": true
}' > data/questionnaire.json
```

### ステップ4: 実行
```bash
# 方法A: CLIで実行
python cli_interface.py analyze -i data/questionnaire.json

# 方法B: Web APIで実行
python api_server.py
# 別ターミナルで:
curl -X POST http://localhost:5000/api/health/analyze -H "Content-Type: application/json" -d @data/questionnaire.json

# 方法C: Pythonスクリプトから直接実行
python -c "
from src.advanced_engine import AdvancedHealthInferenceEngine
import json
engine = AdvancedHealthInferenceEngine()
with open('data/questionnaire.json') as f:
    data = json.load(f)
result = engine.generate_health_plan(data)
print(json.dumps(result, indent=2, ensure_ascii=False))
"
```

## 6. トラブルシューティング

### よくある問題と解決策

1. **ImportErrorが発生**
```bash
# 仮想環境がアクティベートされているか確認
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# パッケージがインストールされているか確認
pip list | grep -E "pandas|flask|numpy"

# 再インストール
pip install --upgrade pip
pip install -r requirements.txt
```

2. **エンコーディングエラー**
```python
# ファイル読み込み時に明示的にエンコーディング指定
with open('file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```

3. **ポート5000が使用中**
```bash
# 別のポートで起動
python api_server.py --port 5001

# Windowsでポート解放
netstat -ano | findstr :5000
taskkill /PID [PID] /F
```

4. **メモリ不足**
```python
# データを分割して処理
def process_large_data(filename, chunk_size=1000):
    for chunk in pd.read_csv(filename, chunksize=chunk_size):
        process_chunk(chunk)
```

## 7. 実践的な使用例

### 例1: 健康管理アプリとの連携
```python
# app_integration.py
class HealthAppIntegration:
    def __init__(self):
        self.engine = AdvancedHealthInferenceEngine()
    
    def sync_with_health_app(self, user_id):
        """健康管理アプリからデータを取得"""
        # 実際のAPIエンドポイントに置き換え
        response = requests.get(f"https://health-app.com/api/user/{user_id}/data")
        health_data = response.json()
        
        # 問診データに変換
        questionnaire = self.convert_to_questionnaire(health_data)
        
        # 分析実行
        result = self.engine.generate_health_plan(questionnaire)
        
        # 結果をアプリに送信
        self.send_to_app(user_id, result)
        
        return result
```

### 例2: バッチ処理（大量データ）
```bash
# batch_process.sh
#!/bin/bash

# 大量の問診データを一括処理
for file in data/questionnaires/*.json; do
    echo "処理中: $file"
    python cli_interface.py analyze -i "$file" -o "results/$(basename $file)"
done

# 結果を集計
python scripts/aggregate_results.py
```

### 例3: リアルタイム監視
```python
# realtime_monitor.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class QuestionnaireHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith('.json'):
            print(f"新しい問診データ: {event.src_path}")
            # 自動分析実行
            analyze_file(event.src_path)
```

このシステムは、個人の健康管理から医療機関での使用まで、様々な用途に応用できます。必要に応じてデータベース接続やユーザー認証などの機能を追加することも可能です。

[[HB5. HealthBook Platform 統合アーキテクチャ（詳細Prompt）]]

[[5-4. 後半]]
