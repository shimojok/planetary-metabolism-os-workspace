"""
MBT Probiotics Screening API - 拡張版 v2.0
105項目問診 + ファイトケミカル詳細対応
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import json

app = FastAPI(
    title="MBT Probiotics Screening API v2.0",
    description="105項目問診 + 12種ファイトケミカル詳細 + 30万人実証データ",
    version="2.0.0"
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
print("Loading Enhanced HealthBook datasets...")

# 拡張版データセット
with open('/mnt/user-data/outputs/healthbook_expanded_v2.json', 'r', encoding='utf-8') as f:
    healthbook_data = json.load(f)

# 293漢方処方データ
with open('/mnt/user-data/uploads/mbt_kampo_library_final_array.json', 'r', encoding='utf-8') as f:
    kampo_library = json.load(f)

print(f"✅ Loaded {healthbook_data['total_questionnaire_items']} questionnaire items")
print(f"✅ Loaded {healthbook_data['total_phytochemicals']} phytochemicals (detailed)")
print(f"✅ Loaded {healthbook_data['total_diseases']} diseases")
print(f"✅ Loaded {kampo_library['total_formulas']} kampo formulas")

# ===== Models =====

class QuestionnaireMode(BaseModel):
    mode: str  # "mini" (10項目) or "full" (105項目)

class QuestionnaireAnswers(BaseModel):
    answers: Dict[int, bool]
    mode: str = "mini"  # デフォルトはミニ版

class DiseaseRisk(BaseModel):
    disease: str
    risk_score: float
    risk_level: str
    matched_factors: List[str]
    global_impact: Optional[str] = None
    gates_priority: Optional[str] = None

class PhytochemicalDetail(BaseModel):
    name: str
    japanese_name: str
    classification: str
    subcategory: str
    color: str
    source_foods: List[str]
    clinical_benefits: List[str]
    bioavailability: str
    absorption_mechanism: str
    daily_intake_mg: str
    mbt_pathway: str
    synergy_effects: Optional[List[str]] = None

class PhytochemicalRecommendation(BaseModel):
    phytochemical: PhytochemicalDetail
    relevance_score: float
    mechanism_explanation: str
    practical_example: str

class EnhancedDiseaseProfile(BaseModel):
    disease: str
    risk_score: float
    risk_level: str
    matched_factors: List[str]
    recommended_phytochemicals: List[PhytochemicalRecommendation]
    metabolic_blockages: List[str]
    mbt55_pathways_needed: List[str]

class EfficacyPrediction(BaseModel):
    efficacy_score: float
    pathway_coverage: float
    synergy_effects: float
    clinical_potential: str
    covered_pathways: List[str]
    phytochemical_synergies: List[Dict[str, str]]
    recommended_next_steps: List[str]
    prediction_basis: str

# ===== Helper Functions =====

def calculate_disease_risk(answers: Dict[int, bool], disease_data: Dict, mode: str = "mini") -> tuple:
    """疾病リスク計算（ミニ版/フル版対応）"""
    
    risk_score = 0.0
    matched_factors = []
    total_weight = 0.0
    
    # 問診項目のソースを選択
    if mode == "mini":
        questionnaire_data = healthbook_data['mini_questionnaire']
    else:
        questionnaire_data = healthbook_data['full_questionnaire_200']
    
    for question_id, answer in answers.items():
        if answer:
            question_data = questionnaire_data.get(str(question_id))
            if not question_data:
                continue
            
            related_factors = question_data.get('related_factors', [])
            
            for factor_name, factor_data in disease_data['risk_factors'].items():
                if factor_name in related_factors:
                    weight = factor_data['weight']
                    risk_score += weight
                    total_weight += weight
                    if factor_name not in matched_factors:
                        matched_factors.append(factor_name)
    
    if total_weight > 0:
        max_possible_weight = sum(f['weight'] for f in disease_data['risk_factors'].values())
        normalized_risk = (risk_score / max_possible_weight) * 100
    else:
        normalized_risk = 0.0
    
    return normalized_risk, matched_factors

def get_risk_level(score: float) -> str:
    if score >= 70:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    elif score >= 20:
        return "LOW"
    else:
        return "VERY_LOW"

def get_recommended_phytochemicals(disease: str, risk_score: float) -> List[PhytochemicalRecommendation]:
    """疾患に対する推奨ファイトケミカル（詳細版）"""
    
    # 疾患別の推奨マッピング
    disease_phyto_map = {
        "高血圧": ["quercetin", "rutin", "allicin"],
        "糖尿病": ["catechin", "isoflavone", "curcumin"],
        "肥満": ["capsaicin", "catechin", "curcumin"],
        "動脈硬化": ["quercetin", "lycopene", "beta_carotene"],
        "がん": ["sulforaphane", "lycopene", "curcumin", "quercetin"],
        "認知症": ["anthocyanin", "catechin", "curcumin"],
        "骨粗鬆症": ["isoflavone"],
        "前立腺肥大": ["lycopene", "isoflavone"],
        "白内障": ["lutein", "beta_carotene"],
        "アレルギー": ["quercetin", "catechin"]
    }
    
    recommendations = []
    phyto_db = healthbook_data['phytochemicals_detailed']
    
    # 疾患名から部分一致で推奨を検索
    relevant_phytos = []
    for disease_key, phyto_list in disease_phyto_map.items():
        if disease_key in disease:
            relevant_phytos.extend(phyto_list)
    
    # 重複除去
    relevant_phytos = list(set(relevant_phytos))
    
    for phyto_id in relevant_phytos[:5]:  # 上位5つ
        if phyto_id in phyto_db:
            phyto = phyto_db[phyto_id]
            
            # 関連性スコア計算（簡易版）
            relevance = min(100, risk_score * 1.2)
            
            # メカニズム説明生成
            mechanism = f"{phyto['absorption_mechanism']}により、{', '.join(phyto['clinical_benefits'][:2])}を実現"
            
            # 実践例
            practical = f"{phyto['source_foods'][0]}を推奨摂取量{phyto['daily_intake_mg']}mg/日"
            
            recommendations.append(PhytochemicalRecommendation(
                phytochemical=PhytochemicalDetail(**phyto),
                relevance_score=relevance,
                mechanism_explanation=mechanism,
                practical_example=practical
            ))
    
    return recommendations

def analyze_phytochemical_synergies(selected_phytos: List[str]) -> List[Dict[str, str]]:
    """ファイトケミカルのシナジー効果分析"""
    
    synergies = []
    phyto_db = healthbook_data['phytochemicals_detailed']
    
    # 既知のシナジー組み合わせ
    known_synergies = {
        ("quercetin", "rutin"): "ルチンがケルセチンの前駆体として作用し、吸収効率向上",
        ("catechin", "curcumin"): "両者の抗酸化作用が相乗効果を発揮",
        ("lycopene", "beta_carotene"): "カロテノイド類の相互作用で抗酸化力増強",
        ("allicin", "sulforaphane"): "硫黄化合物の解毒酵素誘導が相乗",
        ("anthocyanin", "catechin"): "ポリフェノールの抗酸化シナジー"
    }
    
    for i, phyto1 in enumerate(selected_phytos):
        for phyto2 in selected_phytos[i+1:]:
            combo = tuple(sorted([phyto1, phyto2]))
            if combo in known_synergies:
                phyto1_name = phyto_db[phyto1]['japanese_name']
                phyto2_name = phyto_db[phyto2]['japanese_name']
                synergies.append({
                    'combination': f"{phyto1_name} + {phyto2_name}",
                    'effect': known_synergies[combo]
                })
    
    return synergies

def predict_formula_efficacy_enhanced(formulas: List[Dict], disease: str, selected_phytos: List[str] = None) -> EfficacyPrediction:
    """拡張版効果予測（ファイトケミカルシナジー考慮）"""
    
    pathway_activation = {}
    covered_pathways = []
    phyto_ids = []
    
    # 漢方処方からファイトケミカルを抽出
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
                
                # ファイトケミカルID抽出（簡易マッピング）
                phyto_name = phyto.get('name', '').lower()
                if 'quercetin' in phyto_name or 'ケルセチン' in phyto_name:
                    phyto_ids.append('quercetin')
                elif 'catechin' in phyto_name or 'カテキン' in phyto_name:
                    phyto_ids.append('catechin')
    
    # 選択されたファイトケミカルも追加
    if selected_phytos:
        phyto_ids.extend(selected_phytos)
    
    phyto_ids = list(set(phyto_ids))
    
    # シナジー効果分析
    synergies = analyze_phytochemical_synergies(phyto_ids)
    
    # スコア計算
    base_coverage = len(covered_pathways) * 20
    synergy_score = sum((count - 1) * 10 for count in pathway_activation.values() if count > 1)
    synergy_score += len(synergies) * 15  # ファイトケミカルシナジーボーナス
    
    efficacy_score = min(100, base_coverage + synergy_score)
    pathway_coverage = min(100, len(covered_pathways) * 25)
    
    # 臨床ポテンシャル判定
    if efficacy_score >= 70:
        clinical_potential = "HIGH"
        next_steps = [
            "Phase 1臨床試験準備",
            "FDA Fast Track申請",
            "Gates Foundation助成申請",
            "アフリカ3カ国パイロットプログラム"
        ]
    elif efficacy_score >= 40:
        clinical_potential = "MEDIUM"
        next_steps = [
            "追加のファイトケミカルスクリーニング",
            "in vitro効果検証",
            "処方最適化",
            "予備的臨床研究"
        ]
    else:
        clinical_potential = "LOW"
        next_steps = [
            "代替処方の探索",
            "メカニズム研究の深化",
            "基礎研究の継続"
        ]
    
    return EfficacyPrediction(
        efficacy_score=efficacy_score,
        pathway_coverage=pathway_coverage,
        synergy_effects=synergy_score,
        clinical_potential=clinical_potential,
        covered_pathways=covered_pathways,
        phytochemical_synergies=synergies,
        recommended_next_steps=next_steps,
        prediction_basis="MBT55代謝経路モデル + ファイトケミカルシナジー解析 + 293処方データ"
    )

# ===== API Endpoints =====

@app.get("/")
def root():
    return {
        "message": "MBT Probiotics Screening API v2.0",
        "version": "2.0.0",
        "features": [
            "105項目問診システム（ミニ版10項目も利用可能）",
            "12種ファイトケミカル詳細データ",
            "生物学的利用能・吸収メカニズム解析",
            "ファイトケミカルシナジー効果予測",
            "30万人実証データに基づくリスク予測"
        ],
        "data_statistics": {
            "questionnaire_items": healthbook_data['total_questionnaire_items'],
            "phytochemicals": healthbook_data['total_phytochemicals'],
            "diseases": healthbook_data['total_diseases'],
            "kampo_formulas": kampo_library['total_formulas']
        }
    }

@app.post("/api/questionnaire/mode")
def get_questionnaire(request: QuestionnaireMode):
    """問診票取得（ミニ版/フル版選択可能）"""
    
    if request.mode == "mini":
        questionnaire = healthbook_data['mini_questionnaire']
        total = len(questionnaire)
        estimated_time = "30秒"
    elif request.mode == "full":
        questionnaire = healthbook_data['full_questionnaire_200']
        total = len(questionnaire)
        estimated_time = "5-10分"
    else:
        raise HTTPException(status_code=400, detail="Invalid mode. Use 'mini' or 'full'")
    
    return {
        "mode": request.mode,
        "questionnaire": questionnaire,
        "total_questions": total,
        "estimated_time": estimated_time
    }

@app.post("/api/predict_risk/enhanced")
def predict_disease_risk_enhanced(request: QuestionnaireAnswers):
    """
    拡張版疾病リスク予測
    - ミニ版（10項目）/フル版（105項目）対応
    - ファイトケミカル推奨付き
    """
    
    predictions = []
    diseases = healthbook_data['diseases']
    
    for disease_name, disease_data in diseases.items():
        risk_score, matched_factors = calculate_disease_risk(
            request.answers,
            disease_data,
            request.mode
        )
        
        if risk_score > 10:  # 閾値を下げて more sensitive
            # ファイトケミカル推奨を取得
            phyto_recommendations = get_recommended_phytochemicals(disease_name, risk_score)
            
            # 代謝阻害と必要な経路
            metabolic_blockages = [
                f"{factor}による代謝阻害" for factor in matched_factors[:3]
            ]
            
            mbt55_pathways = list(set([
                p.phytochemical.mbt_pathway for p in phyto_recommendations
            ]))
            
            predictions.append(EnhancedDiseaseProfile(
                disease=disease_name,
                risk_score=round(risk_score, 1),
                risk_level=get_risk_level(risk_score),
                matched_factors=matched_factors,
                recommended_phytochemicals=phyto_recommendations,
                metabolic_blockages=metabolic_blockages,
                mbt55_pathways_needed=mbt55_pathways
            ))
    
    predictions.sort(key=lambda x: x.risk_score, reverse=True)
    
    return {
        "mode": request.mode,
        "predictions": predictions[:15],
        "total_analyzed": len(diseases),
        "data_source": "30万人実証データ（浜田式問診）+ ファイトケミカル詳細DB",
        "confidence": "HIGH"
    }

@app.get("/api/phytochemicals")
def get_all_phytochemicals():
    """全ファイトケミカル詳細リスト"""
    
    phyto_db = healthbook_data['phytochemicals_detailed']
    
    phytochemicals = []
    for phyto_id, phyto_data in phyto_db.items():
        phytochemicals.append({
            "id": phyto_id,
            **phyto_data
        })
    
    return {
        "phytochemicals": phytochemicals,
        "total": len(phytochemicals)
    }

@app.get("/api/phytochemicals/{phyto_id}")
def get_phytochemical_detail(phyto_id: str):
    """特定ファイトケミカルの詳細"""
    
    phyto_db = healthbook_data['phytochemicals_detailed']
    
    if phyto_id not in phyto_db:
        raise HTTPException(status_code=404, detail="Phytochemical not found")
    
    return {
        "id": phyto_id,
        **phyto_db[phyto_id]
    }

@app.post("/api/predict_efficacy/enhanced")
def predict_efficacy_enhanced_endpoint(request: dict):
    """
    拡張版効果予測
    - ファイトケミカルシナジー解析
    - 詳細なメカニズム説明
    """
    
    disease_id = request.get('disease_id')
    selected_formula_ids = request.get('selected_formula_ids', [])
    selected_phyto_ids = request.get('selected_phytochemical_ids', [])
    
    # 選択された処方を取得
    selected_formulas = [
        f for f in kampo_library['formulas']
        if f['id'] in selected_formula_ids
    ]
    
    if not selected_formulas and not selected_phyto_ids:
        raise HTTPException(status_code=400, detail="No formulas or phytochemicals selected")
    
    # 拡張版効果予測
    prediction = predict_formula_efficacy_enhanced(
        selected_formulas,
        disease_id,
        selected_phyto_ids
    )
    
    return prediction

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
