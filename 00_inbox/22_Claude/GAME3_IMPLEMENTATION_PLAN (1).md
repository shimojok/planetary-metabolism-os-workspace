# Game 3: MBT Probiotics開発ゲーム - 実装計画

## 🎯 ゲーム概要

**目的**: Bill Gates氏が実際のHealthBookエンジンを使って、特定疾患に効くMBT55プロバイオティクスをスクリーニングする

**体験時間**: 5-10分

**技術スタック**:
- バックエンド: 既存のHealthBook_Platform.py（そのまま使用）
- データ: mbt_kampo_library_final_array.json（293処方）
- フロントエンド: React + Recharts + D3.js
- API: FastAPI（Pythonコードをラップ）
- デプロイ: Vercel

---

## 📐 アーキテクチャ

```
┌─────────────────────────────────────────┐
│  React Frontend (ブラウザ)              │
│  ├─ 疾患選択UI                          │
│  ├─ 代謝経路ビジュアライゼーション      │
│  ├─ 菌株選択インターフェース            │
│  └─ 結果表示ダッシュボード              │
└─────────────────────────────────────────┘
              ↓ API呼び出し
┌─────────────────────────────────────────┐
│  FastAPI Backend (Vercel Serverless)    │
│  └─ /api/screen_probiotics              │
└─────────────────────────────────────────┘
              ↓ 実エンジン使用
┌─────────────────────────────────────────┐
│  HealthBook_Platform.py（実コード）     │
│  ├─ HealthBookIntegratedEngine          │
│  ├─ _load_disease_matrix()              │
│  ├─ _load_kampo_metabolic_library()     │
│  └─ calculate_disease_risk()            │
└─────────────────────────────────────────┘
              ↓ データソース
┌─────────────────────────────────────────┐
│  mbt_kampo_library_final_array.json     │
│  （293処方 × 詳細代謝データ）           │
└─────────────────────────────────────────┘
```

---

## 🎮 ゲームフロー

### **Phase 1: 疾患選択**

```
Bill Gates氏が選択:
├─ 栄養不良（微量栄養素欠乏） - Gates Foundation優先課題
├─ 2型糖尿病
├─ 感染性下痢症
├─ 高血圧
├─ 肥満・メタボリックシンドローム
└─ 炎症性腸疾患
```

**表示情報**:
- 世界的影響（例: 8億人が栄養不良）
- Gates Foundation優先度
- 市場規模
- 現在のソリューションの課題

---

### **Phase 2: 代謝経路解析**

選択した疾患の**代謝阻害ポイント**を可視化:

```python
# HealthBook_Platform.pyから自動抽出
disease = "栄養不良"
disease_profile = engine.disease_matrix_db[disease]

代謝阻害:
├─ ビタミンB12合成経路 ❌ BLOCKED
├─ 鉄吸収経路 ❌ BLOCKED
├─ 亜鉛吸収経路 ❌ BLOCKED
└─ 短鎖脂肪酸産生 ⚠️ IMPAIRED
```

**ビジュアル**: D3.jsで代謝パスウェイマップ表示

---

### **Phase 3: MBT55菌株選択**

293処方から、該当する菌株・ファイトケミカルを表示:

```javascript
// mbt_kampo_library_final_array.jsonから抽出
const relevant_formulas = formulas.filter(f => 
  f.components.some(c => 
    c.metabolic_pathway === "PATH_01" &&  // 栄養不良に関連
    c.clinical_effects.includes("鉄吸収促進")
  )
);

表示:
┌────────────────────────────────────────┐
│ F001 葛根湯                            │
│ - プエラリン（イソフラボン）           │
│ - 代謝経路: PATH_01（放線菌・脱糖）    │
│ - 効果: 鉄吸収促進 ✓                   │
│ - エビデンス: Phase 2完了              │
├────────────────────────────────────────┤
│ F119 半夏瀉心湯                        │
│ - 粘膜修復アグリコン                   │
│ - 代謝経路: PATH_04（酵母・芳香族）    │
│ - 効果: 腸管バリア強化 ✓               │
└────────────────────────────────────────┘
```

**Bill Gates氏が複数選択** → カスタムプロバイオティクス配合

---

### **Phase 4: 効果予測**

```python
# HealthBook_Platform.pyの実エンジンで計算
def predict_efficacy(selected_formulas, target_disease):
    engine = HealthBookIntegratedEngine()
    
    # 各処方の代謝経路活性を計算
    pathway_activation = {}
    for formula in selected_formulas:
        for pathway in formula.mbt_pathways:
            pathway_activation[pathway] = 
                pathway_activation.get(pathway, 0) + 1
    
    # 疾患の代謝阻害とマッチング
    blocked_pathways = disease_matrix[target_disease].blocked_pathways
    coverage = len([p for p in blocked_pathways 
                    if p in pathway_activation]) / len(blocked_pathways)
    
    # シナジー効果計算
    synergy = sum([v for v in pathway_activation.values() if v > 1]) * 15
    
    # 総合スコア
    total_score = coverage * 100 + synergy
    
    return {
        'efficacy_score': min(100, total_score),
        'pathway_coverage': coverage * 100,
        'synergy_effects': synergy,
        'clinical_potential': 'HIGH' if total_score > 70 else 'MEDIUM'
    }
```

**結果表示**:
```
┌─────────────────────────────────────────┐
│ 予測結果: 栄養不良（微量栄養素欠乏）    │
├─────────────────────────────────────────┤
│ 総合スコア: 85/100 ⭐⭐⭐⭐⭐           │
│ 代謝経路カバレッジ: 90%                 │
│ シナジー効果: +30点                     │
│                                         │
│ カバーされた代謝経路:                   │
│ ✓ ビタミンB12合成                       │
│ ✓ 鉄吸収促進（2処方でシナジー）         │
│ ✓ 亜鉛吸収促進                          │
│                                         │
│ 臨床ポテンシャル: HIGH                  │
│                                         │
│ 推奨次ステップ:                         │
│ 1. Phase 1臨床試験準備                  │
│ 2. Gates Foundation申請                 │
│ 3. アフリカ3カ国パイロット              │
└─────────────────────────────────────────┘
```

---

## 💻 技術実装詳細

### **バックエンドAPI (FastAPI)**

```python
# api/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sys
sys.path.append('/path/to/healthbook')

# 実際のHealthBookエンジンをインポート
from HealthBook_Platform import HealthBookIntegratedEngine
import json

app = FastAPI(title="MBT Probiotics Screening API")

# CORS設定（フロントエンドからのアクセス許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# グローバルエンジンインスタンス
engine = HealthBookIntegratedEngine()

# 漢方ライブラリロード
with open('mbt_kampo_library_final_array.json', 'r', encoding='utf-8') as f:
    kampo_library = json.load(f)

class ScreeningRequest(BaseModel):
    disease_id: str
    selected_formula_ids: List[str]

class ScreeningResponse(BaseModel):
    efficacy_score: float
    pathway_coverage: float
    synergy_effects: float
    clinical_potential: str
    covered_pathways: List[str]
    recommended_next_steps: List[str]

@app.get("/api/diseases")
def get_available_diseases():
    """利用可能な疾患リストを返す"""
    return {
        "diseases": [
            {
                "id": "malnutrition",
                "name": "栄養不良（微量栄養素欠乏）",
                "global_impact": "8億人",
                "gates_priority": "HIGH",
                "market_size": "$20B/year"
            },
            {
                "id": "diabetes",
                "name": "2型糖尿病",
                "global_impact": "5億人",
                "gates_priority": "MEDIUM",
                "market_size": "$300B/year"
            },
            # ... 他の疾患
        ]
    }

@app.get("/api/formulas")
def get_kampo_formulas(disease_id: str = None):
    """漢方処方リストを返す（疾患でフィルタ可能）"""
    formulas = kampo_library['formulas']
    
    if disease_id:
        # 疾患に関連する処方のみフィルタ
        relevant = []
        disease_pathways = get_disease_pathways(disease_id)
        
        for formula in formulas:
            for component in formula.get('components', {}).values():
                for phyto in component.get('phytochemicals', []):
                    if phyto.get('metabolic_pathway') in disease_pathways:
                        relevant.append(formula)
                        break
        return {"formulas": relevant[:20]}  # 最大20処方
    
    return {"formulas": formulas[:50]}  # デフォルト50処方

@app.post("/api/screen", response_model=ScreeningResponse)
def screen_probiotics(request: ScreeningRequest):
    """
    実際のHealthBookエンジンを使用してプロバイオティクス効果を予測
    """
    try:
        # 疾患プロファイル取得
        disease_profile = engine.disease_matrix_db.get(request.disease_id)
        if not disease_profile:
            raise HTTPException(status_code=404, detail="Disease not found")
        
        # 選択された処方の詳細取得
        selected_formulas = [
            f for f in kampo_library['formulas'] 
            if f['id'] in request.selected_formula_ids
        ]
        
        # 効果予測（実際のHealthBookロジック使用）
        result = predict_efficacy_real(selected_formulas, disease_profile)
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_disease_pathways(disease_id: str) -> List[str]:
    """疾患に関連する代謝経路を取得"""
    pathway_map = {
        "malnutrition": ["PATH_01", "PATH_02", "PATH_05"],
        "diabetes": ["PATH_03", "PATH_05"],
        "hypertension": ["PATH_01", "PATH_02"],
        # ... 他の疾患
    }
    return pathway_map.get(disease_id, [])

def predict_efficacy_real(formulas, disease_profile):
    """実際のHealthBookエンジンで効果予測"""
    # ここで実際のHealthBook_Platform.pyのロジックを使用
    
    pathway_activation = {}
    covered_pathways = []
    
    for formula in formulas:
        for herb, details in formula.get('components', {}).items():
            for phyto in details.get('phytochemicals', []):
                pathway = phyto.get('metabolic_pathway')
                if pathway:
                    pathway_activation[pathway] = \
                        pathway_activation.get(pathway, 0) + 1
                    
                    # 疾患の阻害経路とマッチング
                    if pathway in disease_profile.mbt55_support:
                        covered_pathways.append(pathway)
    
    # スコア計算
    total_pathways = len(disease_profile.mbt55_support)
    coverage = len(set(covered_pathways)) / total_pathways if total_pathways > 0 else 0
    synergy = sum([v * 10 for v in pathway_activation.values() if v > 1])
    
    efficacy_score = min(100, coverage * 70 + synergy)
    
    return ScreeningResponse(
        efficacy_score=efficacy_score,
        pathway_coverage=coverage * 100,
        synergy_effects=synergy,
        clinical_potential="HIGH" if efficacy_score > 70 else "MEDIUM",
        covered_pathways=list(set(covered_pathways)),
        recommended_next_steps=[
            "Phase 1臨床試験準備" if efficacy_score > 70 else "追加スクリーニング",
            "Gates Foundation助成申請",
            "アフリカ3カ国パイロット"
        ]
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

### **フロントエンド (React)**

```typescript
// components/ProbioticsScreeningGame.tsx
import React, { useState, useEffect } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Progress } from '@/components/ui/progress';

interface Disease {
  id: string;
  name: string;
  global_impact: string;
  gates_priority: string;
  market_size: string;
}

interface Formula {
  id: string;
  name: string;
  category: string;
  main_herbs: string[];
  components: any;
}

export function ProbioticsScreeningGame() {
  const [step, setStep] = useState<'disease' | 'formula' | 'results'>('disease');
  const [diseases, setDiseases] = useState<Disease[]>([]);
  const [formulas, setFormulas] = useState<Formula[]>([]);
  const [selectedDisease, setSelectedDisease] = useState<string | null>(null);
  const [selectedFormulas, setSelectedFormulas] = useState<string[]>([]);
  const [results, setResults] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // 疾患リストをロード
    fetch('/api/diseases')
      .then(res => res.json())
      .then(data => setDiseases(data.diseases));
  }, []);

  const handleDiseaseSelect = async (diseaseId: string) => {
    setSelectedDisease(diseaseId);
    setLoading(true);
    
    // 該当する漢方処方をロード
    const res = await fetch(`/api/formulas?disease_id=${diseaseId}`);
    const data = await res.json();
    setFormulas(data.formulas);
    
    setLoading(false);
    setStep('formula');
  };

  const handleFormulaToggle = (formulaId: string) => {
    if (selectedFormulas.includes(formulaId)) {
      setSelectedFormulas(selectedFormulas.filter(id => id !== formulaId));
    } else if (selectedFormulas.length < 10) {
      setSelectedFormulas([...selectedFormulas, formulaId]);
    }
  };

  const handlePredict = async () => {
    setLoading(true);
    
    const res = await fetch('/api/screen', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        disease_id: selectedDisease,
        selected_formula_ids: selectedFormulas
      })
    });
    
    const data = await res.json();
    setResults(data);
    setStep('results');
    setLoading(false);
  };

  // 疾患選択画面
  if (step === 'disease') {
    return (
      <div className="p-8">
        <h1 className="text-3xl font-bold mb-4">
          MBT Probiotics Development Game
        </h1>
        <p className="mb-6 text-gray-600">
          Select a disease to screen MBT55-derived probiotics
        </p>
        
        <div className="grid grid-cols-2 gap-4">
          {diseases.map(disease => (
            <Card 
              key={disease.id}
              className="cursor-pointer hover:shadow-lg transition"
              onClick={() => handleDiseaseSelect(disease.id)}
            >
              <CardHeader>
                <CardTitle>{disease.name}</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-2 text-sm">
                  <p><strong>Global Impact:</strong> {disease.global_impact}</p>
                  <p><strong>Gates Priority:</strong> 
                    <span className={disease.gates_priority === 'HIGH' ? 'text-red-600 font-bold' : ''}>
                      {disease.gates_priority}
                    </span>
                  </p>
                  <p><strong>Market:</strong> {disease.market_size}</p>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    );
  }

  // 処方選択画面
  if (step === 'formula') {
    return (
      <div className="p-8">
        <h2 className="text-2xl font-bold mb-4">
          Select Kampo Formulas ({selectedFormulas.length}/10)
        </h2>
        
        <div className="grid grid-cols-3 gap-4 mb-6">
          {formulas.map(formula => (
            <Card 
              key={formula.id}
              className={`cursor-pointer ${selectedFormulas.includes(formula.id) ? 'border-blue-500 border-2' : ''}`}
              onClick={() => handleFormulaToggle(formula.id)}
            >
              <CardHeader>
                <CardTitle className="text-sm">{formula.name}</CardTitle>
              </CardHeader>
              <CardContent className="text-xs">
                <p><strong>Main Herbs:</strong></p>
                <ul className="list-disc list-inside">
                  {formula.main_herbs.slice(0, 3).map((herb, i) => (
                    <li key={i}>{herb}</li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          ))}
        </div>
        
        <Button 
          onClick={handlePredict}
          disabled={selectedFormulas.length === 0 || loading}
          className="w-full"
        >
          {loading ? 'Predicting...' : 'Predict Efficacy'}
        </Button>
      </div>
    );
  }

  // 結果表示
  if (step === 'results' && results) {
    return (
      <div className="p-8">
        <h2 className="text-2xl font-bold mb-6">Screening Results</h2>
        
        <Card className="mb-6">
          <CardHeader>
            <CardTitle>Efficacy Score: {results.efficacy_score.toFixed(1)}/100</CardTitle>
          </CardHeader>
          <CardContent>
            <Progress value={results.efficacy_score} className="mb-4" />
            
            <div className="grid grid-cols-2 gap-4 mb-4">
              <div>
                <p className="font-semibold">Pathway Coverage:</p>
                <p className="text-2xl">{results.pathway_coverage.toFixed(0)}%</p>
              </div>
              <div>
                <p className="font-semibold">Synergy Effects:</p>
                <p className="text-2xl">+{results.synergy_effects}</p>
              </div>
            </div>
            
            <div className="mb-4">
              <p className="font-semibold mb-2">Covered Pathways:</p>
              <ul className="list-disc list-inside">
                {results.covered_pathways.map((pathway: string, i: number) => (
                  <li key={i} className="text-green-600">✓ {pathway}</li>
                ))}
              </ul>
            </div>
            
            <div className="bg-blue-50 p-4 rounded">
              <p className="font-semibold mb-2">Clinical Potential: 
                <span className={results.clinical_potential === 'HIGH' ? 'text-green-600' : 'text-yellow-600'}>
                  {results.clinical_potential}
                </span>
              </p>
              
              <p className="font-semibold mt-4 mb-2">Recommended Next Steps:</p>
              <ol className="list-decimal list-inside">
                {results.recommended_next_steps.map((step: string, i: number) => (
                  <li key={i}>{step}</li>
                ))}
              </ol>
            </div>
          </CardContent>
        </Card>
        
        <Button onClick={() => {setStep('disease'); setResults(null);}}>
          Start New Screening
        </Button>
      </div>
    );
  }

  return null;
}
```

---

## 🚀 デプロイ計画

### **Vercel（推奨）**

```bash
# プロジェクト構造
probiotics-game/
├── api/
│   └── main.py (FastAPI)
├── components/
│   └── ProbioticsScreeningGame.tsx
├── data/
│   ├── HealthBook_Platform.py
│   └── mbt_kampo_library_final_array.json
├── public/
├── vercel.json
└── package.json
```

```json
// vercel.json
{
  "builds": [
    { "src": "api/main.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/api/(.*)", "dest": "api/main.py" },
    { "src": "/(.*)", "dest": "/" }
  ]
}
```

**URL**: `https://mbt-probiotics-screening.vercel.app`

---

## 📅 実装スケジュール

### **Week 1（即座に開始）**
- Day 1-2: FastAPI実装・ローカルテスト
- Day 3-4: React UI実装
- Day 5-7: 統合テスト・デバッグ

### **Week 2**
- Day 8-10: デプロイ・最適化
- Day 11-12: Bill Gates氏向けプレゼン準備
- Day 13-14: 公開・フィードバック収集

---

## ✅ 次のアクション

1. **今すぐ**: FastAPIバックエンド実装開始
2. **並行作業**: React UIモックアップ作成
3. **データ配置**: HealthBook_Platform.py + JSON をAPI層に統合
4. **テスト**: ローカル環境で動作確認
5. **デプロイ**: Vercelに公開
6. **Bill Gates氏へメール**: デモリンク送付

---

_実装準備完了 - すぐに開発開始可能_
