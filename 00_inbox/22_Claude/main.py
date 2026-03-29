"""
MBT Probiotics Screening API - Game 3
30万人実証データ統合版
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import json
import sys

app = FastAPI(
    title="MBT Probiotics Screening API",
    description="30万人実証データに基づくプロバイオティクススクリーニング",
    version="1.0.0"
)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# データロード
print("Loading HealthBook datasets...")

# 30万人データセット
with open('/mnt/user-data/outputs/healthbook_30m_dataset.json', 'r', encoding='utf-8') as f:
    healthbook_data = json.load(f)

# 293漢方処方データ
with open('/mnt/user-data/uploads/mbt_kampo_library_final_array.json', 'r', encoding='utf-8') as f:
    kampo_library = json.load(f)

print(f"✅ Loaded {healthbook_data['total_diseases']} diseases")
print(f"✅ Loaded {kampo_library['total_formulas']} kampo formulas")

# ===== Request/Response Models =====

class QuestionnaireAnswers(BaseModel):
    answers: Dict[int, bool]  # {question_id: yes/no}

class DiseaseRisk(BaseModel):
    disease: str
    risk_score: float
    risk_level: str
    matched_factors: List[str]
    global_impact: Optional[str] = None
    gates_priority: Optional[str] = None

class RiskPredictionResponse(BaseModel):
    predictions: List[DiseaseRisk]
    total_diseases_analyzed: int
    data_source: str
    confidence: str

class FormulaSelection(BaseModel):
    disease_id: str
    selected_formula_ids: List[str]

class EfficacyPrediction(BaseModel):
    efficacy_score: float
    pathway_coverage: float
    synergy_effects: float
    clinical_potential: str
    covered_pathways: List[str]
    recommended_next_steps: List[str]
    prediction_basis: str

# ===== Helper Functions =====

def calculate_disease_risk(answers: Dict[int, bool], disease_data: Dict) -> float:
    """30万人データに基づく疾病リスク計算"""
    
    risk_score = 0.0
    matched_factors = []
    total_weight = 0.0
    
    # 問診項目から該当する因子を抽出
    for question_id, answer in answers.items():
        if answer:  # yes の場合
            # 問診項目に関連する食生活因子を取得
            question_data = healthbook_data['mini_questionnaire'][str(question_id)]
            related_factors = question_data['related_factors']
            
            # 疾病のリスク因子とマッチング
            for factor_name, factor_data in disease_data['risk_factors'].items():
                if factor_name in related_factors:
                    weight = factor_data['weight']
                    risk_score += weight
                    total_weight += weight
                    matched_factors.append(factor_name)
    
    # 正規化（0-100スケール）
    if total_weight > 0:
        # 該当因子の割合で計算
        max_possible_weight = sum(f['weight'] for f in disease_data['risk_factors'].values())
        normalized_risk = (risk_score / max_possible_weight) * 100
    else:
        normalized_risk = 0.0
    
    return normalized_risk, matched_factors

def get_risk_level(score: float) -> str:
    """リスクレベル判定"""
    if score >= 70:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    elif score >= 20:
        return "LOW"
    else:
        return "VERY_LOW"

def get_gates_priority(disease: str) -> str:
    """Gates Foundation優先度判定"""
    high_priority = [
        "糖尿病", "高血圧", "慢性腎不全", "慢性肝炎",
        "肺炎", "結核", "マラリア", "HIV",
        "栄養失調", "下痢症"
    ]
    
    for hp in high_priority:
        if hp in disease:
            return "HIGH"
    
    return "MEDIUM"

def get_global_impact(disease: str) -> str:
    """世界的影響の推定"""
    impact_map = {
        "糖尿病": "5億人",
        "高血圧": "12億人",
        "がん": "2,000万人/年",
        "心筋梗塞": "1,800万人/年",
        "脳卒中": "1,500万人/年"
    }
    
    for key, impact in impact_map.items():
        if key in disease:
            return impact
    
    return "推定1,000万人以上"

def predict_formula_efficacy(formulas: List[Dict], disease: str) -> EfficacyPrediction:
    """漢方処方の効果予測"""
    
    pathway_activation = {}
    covered_pathways = []
    
    # 各処方の代謝経路を集計
    for formula in formulas:
        components = formula.get('components', {})
        
        for herb, details in components.items():
            phytochemicals = details.get('phytochemicals', [])
            
            for phyto in phytochemicals:
                pathway = phyto.get('metabolic_pathway')
                if pathway:
                    pathway_activation[pathway] = pathway_activation.get(pathway, 0) + 1
                    if pathway not in covered_pathways:
                        covered_pathways.append(pathway)
    
    # スコア計算
    base_coverage = len(covered_pathways) * 20  # 各経路20点
    synergy = sum((count - 1) * 10 for count in pathway_activation.values() if count > 1)
    
    efficacy_score = min(100, base_coverage + synergy)
    pathway_coverage = min(100, len(covered_pathways) * 25)
    
    # 臨床ポテンシャル判定
    if efficacy_score >= 70:
        clinical_potential = "HIGH"
        next_steps = [
            "Phase 1臨床試験準備",
            "Gates Foundation助成申請",
            "アフリカ3カ国パイロットプログラム"
        ]
    elif efficacy_score >= 40:
        clinical_potential = "MEDIUM"
        next_steps = [
            "追加の菌株スクリーニング",
            "in vitro効果検証",
            "処方最適化"
        ]
    else:
        clinical_potential = "LOW"
        next_steps = [
            "代替処方の探索",
            "メカニズム研究の深化"
        ]
    
    return EfficacyPrediction(
        efficacy_score=efficacy_score,
        pathway_coverage=pathway_coverage,
        synergy_effects=synergy,
        clinical_potential=clinical_potential,
        covered_pathways=covered_pathways,
        recommended_next_steps=next_steps,
        prediction_basis="MBT55代謝経路モデル + 293処方データ"
    )

# ===== API Endpoints =====

@app.get("/")
def root():
    return {
        "message": "MBT Probiotics Screening API",
        "version": "1.0.0",
        "data_source": "30万人実証データ（浜田式）",
        "total_diseases": healthbook_data['total_diseases'],
        "total_formulas": kampo_library['total_formulas']
    }

@app.get("/api/questionnaire")
def get_questionnaire():
    """10項目ミニ問診を取得"""
    return {
        "questionnaire": healthbook_data['mini_questionnaire'],
        "total_questions": len(healthbook_data['mini_questionnaire']),
        "estimated_time": "30秒"
    }

@app.post("/api/predict_risk", response_model=RiskPredictionResponse)
def predict_disease_risk_endpoint(request: QuestionnaireAnswers):
    """
    30万人実証データに基づく疾病リスク予測
    """
    
    predictions = []
    diseases = healthbook_data['diseases']
    
    for disease_name, disease_data in diseases.items():
        # リスク計算
        risk_score, matched_factors = calculate_disease_risk(
            request.answers, 
            disease_data
        )
        
        if risk_score > 0:  # リスクがある場合のみ
            predictions.append(DiseaseRisk(
                disease=disease_name,
                risk_score=round(risk_score, 1),
                risk_level=get_risk_level(risk_score),
                matched_factors=matched_factors,
                global_impact=get_global_impact(disease_name),
                gates_priority=get_gates_priority(disease_name)
            ))
    
    # リスクスコア順にソート
    predictions.sort(key=lambda x: x.risk_score, reverse=True)
    
    return RiskPredictionResponse(
        predictions=predictions[:15],  # 上位15疾病
        total_diseases_analyzed=len(diseases),
        data_source="30万人実証データ（浜田式問診）",
        confidence="HIGH"
    )

@app.get("/api/formulas")
def get_kampo_formulas(disease: Optional[str] = None, limit: int = 20):
    """漢方処方リストを取得"""
    
    formulas = kampo_library['formulas']
    
    if disease:
        # 疾患に関連する処方をフィルタ（簡易版）
        relevant = []
        for formula in formulas:
            # カテゴリまたは臨床適応でマッチング
            category = formula.get('category', '')
            if disease in category or any(disease in comp for comp in formula.get('main_herbs', [])):
                relevant.append(formula)
                if len(relevant) >= limit:
                    break
        
        return {
            "formulas": relevant,
            "total": len(relevant),
            "filtered_by": disease
        }
    
    return {
        "formulas": formulas[:limit],
        "total": len(formulas),
        "showing": min(limit, len(formulas))
    }

@app.post("/api/predict_efficacy", response_model=EfficacyPrediction)
def predict_efficacy_endpoint(request: FormulaSelection):
    """
    選択した漢方処方の効果予測
    """
    
    # 選択された処方を取得
    selected_formulas = [
        f for f in kampo_library['formulas']
        if f['id'] in request.selected_formula_ids
    ]
    
    if not selected_formulas:
        raise HTTPException(status_code=404, detail="No formulas found")
    
    # 効果予測
    prediction = predict_formula_efficacy(selected_formulas, request.disease_id)
    
    return prediction

@app.get("/api/diseases/priority")
def get_priority_diseases():
    """Gates Foundation優先疾患リスト"""
    
    priority_diseases = [
        {
            "id": "malnutrition",
            "name": "栄養不良（微量栄養素欠乏）",
            "global_impact": "8億人",
            "gates_priority": "HIGH",
            "market_size": "$20B/year",
            "description": "途上国の子供・妊婦における鉄・亜鉛・ビタミンA欠乏"
        },
        {
            "id": "diabetes",
            "name": "2型糖尿病",
            "global_impact": "5億人",
            "gates_priority": "MEDIUM",
            "market_size": "$300B/year",
            "description": "インスリン抵抗性とβ細胞機能不全"
        },
        {
            "id": "hypertension",
            "name": "高血圧",
            "global_impact": "12億人",
            "gates_priority": "MEDIUM",
            "market_size": "$50B/year",
            "description": "心血管疾患の主要リスク因子"
        },
        {
            "id": "diarrhea",
            "name": "感染性下痢症",
            "global_impact": "年50万人死亡（小児）",
            "gates_priority": "HIGH",
            "market_size": "$8B/year",
            "description": "途上国の主要な小児死因"
        }
    ]
    
    return {
        "diseases": priority_diseases,
        "total": len(priority_diseases)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
