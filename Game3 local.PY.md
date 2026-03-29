"""
MBT Probiotics Screening API - ローカル動作版
Windows環境対応・パス修正済み

起動方法:
    pip install fastapi uvicorn pydantic
    python game3_local.py

アクセス:
    API: http://localhost:8000
    ドキュメント: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import json
from pathlib import Path

app = FastAPI(
    title="MBT Probiotics Screening API",
    description="30万人実証データに基づくプロバイオティクススクリーニング",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────
# データファイルのパス設定
# このファイルと同じフォルダに以下を置いてください:
#   - healthbook_30m_dataset.json
#   - mbt_kampo_library_final_array.json
# ─────────────────────────────────────────────
BASE_DIR = Path(__file__).parent

HEALTHBOOK_PATH = BASE_DIR / "healthbook_30m_dataset.json"
KAMPO_PATH = BASE_DIR / "mbt_kampo_library_final_array.json"

# ─────────────────────────────────────────────
# データロード
# ─────────────────────────────────────────────
print("=" * 50)
print("  MBT Probiotics Screening API 起動中...")
print("=" * 50)

if not HEALTHBOOK_PATH.exists():
    raise FileNotFoundError(
        f"healthbook_30m_dataset.json が見つかりません。\n"
        f"以下のパスに置いてください: {HEALTHBOOK_PATH}"
    )

if not KAMPO_PATH.exists():
    raise FileNotFoundError(
        f"mbt_kampo_library_final_array.json が見つかりません。\n"
        f"以下のパスに置いてください: {KAMPO_PATH}"
    )

with open(HEALTHBOOK_PATH, "r", encoding="utf-8") as f:
    healthbook_data = json.load(f)

with open(KAMPO_PATH, "r", encoding="utf-8") as f:
    kampo_library = json.load(f)

print(f"  ✅ 疾病データ: {healthbook_data.get('total_diseases', '?')} 件")
print(f"  ✅ 漢方処方: {kampo_library.get('total_formulas', '?')} 件")
print(f"  ✅ API起動完了: http://localhost:8000")
print(f"  📖 ドキュメント: http://localhost:8000/docs")
print("=" * 50)

# ─────────────────────────────────────────────
# 問診データ（10項目ミニ版）
# ─────────────────────────────────────────────
MINI_QUESTIONNAIRE = {
    "1":  {"question": "朝食を抜くことが多いですか？",           "related_factors": ["欠食型（朝食抜き）", "不規則型"]},
    "2":  {"question": "色の濃い野菜が嫌いですか？",             "related_factors": ["偏食型", "野菜少ない"]},
    "3":  {"question": "塩分の多い食事を好みますか？",           "related_factors": ["塩分", "塩辛い物"]},
    "4":  {"question": "甘いものや間食が多いですか？",           "related_factors": ["甘物", "間食多い"]},
    "5":  {"question": "運動不足ですか？",                       "related_factors": ["運動不足"]},
    "6":  {"question": "ストレスが多い生活を送っていますか？",   "related_factors": ["ストレス"]},
    "7":  {"question": "睡眠不足ですか？",                       "related_factors": ["睡眠不足"]},
    "8":  {"question": "お酒を週3回以上飲みますか？",            "related_factors": ["飲酒", "アルコール"]},
    "9":  {"question": "タバコを吸いますか（過去含む）？",       "related_factors": ["喫煙"]},
    "10": {"question": "家族に糖尿病や高血圧の人がいますか？",   "related_factors": ["遺伝"]},
}

# ─────────────────────────────────────────────
# Models
# ─────────────────────────────────────────────
class QuestionnaireAnswers(BaseModel):
    answers: Dict[int, bool]

class FormulaSelection(BaseModel):
    disease_id: str
    selected_formula_ids: List[str]

# ─────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────
def calculate_disease_risk(answers: Dict[int, bool], disease_data: Dict):
    """疾病リスク計算"""
    risk_score = 0.0
    matched_factors = []

    for q_id, answer in answers.items():
        if not answer:
            continue
        q_data = MINI_QUESTIONNAIRE.get(str(q_id), {})
        related_factors = q_data.get("related_factors", [])

        for factor_name, factor_data in disease_data.get("risk_factors", {}).items():
            if factor_name in related_factors and factor_name not in matched_factors:
                risk_score += factor_data.get("weight", 0.5)
                matched_factors.append(factor_name)

    max_weight = sum(
        f.get("weight", 0.5)
        for f in disease_data.get("risk_factors", {}).values()
    )
    normalized = (risk_score / max_weight * 100) if max_weight > 0 else 0.0
    return round(normalized, 1), matched_factors


def get_risk_level(score: float) -> str:
    if score >= 70:   return "HIGH"
    elif score >= 40: return "MEDIUM"
    elif score >= 20: return "LOW"
    return "VERY_LOW"


def get_gates_priority(disease: str) -> str:
    high = ["糖尿病", "高血圧", "栄養失調", "肺炎", "下痢", "結核", "マラリア"]
    return "HIGH" if any(h in disease for h in high) else "MEDIUM"


def get_global_impact(disease: str) -> str:
    impacts = {
        "糖尿病": "5億人", "高血圧": "12億人",
        "がん": "2,000万人/年", "心筋梗塞": "1,800万人/年",
        "脳卒中": "1,500万人/年", "肥満": "8億人",
    }
    for k, v in impacts.items():
        if k in disease:
            return v
    return "推定1,000万人以上"


def predict_formula_efficacy(formulas: List[Dict], disease: str) -> Dict:
    """漢方処方の効果予測"""
    pathway_counts: Dict[str, int] = {}
    covered_pathways = []

    for formula in formulas:
        for herb, details in formula.get("components", {}).items():
            for phyto in details.get("phytochemicals", []):
                pw = phyto.get("metabolic_pathway")
                if pw:
                    pathway_counts[pw] = pathway_counts.get(pw, 0) + 1
                    if pw not in covered_pathways:
                        covered_pathways.append(pw)

    base = len(covered_pathways) * 20
    synergy = sum((c - 1) * 10 for c in pathway_counts.values() if c > 1)
    efficacy_score = min(100, base + synergy)
    pathway_coverage = min(100, len(covered_pathways) * 25)

    if efficacy_score >= 70:
        clinical = "HIGH"
        next_steps = ["Phase 1臨床試験準備", "Gates Foundation助成申請", "アフリカ3カ国パイロット"]
    elif efficacy_score >= 40:
        clinical = "MEDIUM"
        next_steps = ["追加スクリーニング", "in vitro効果検証", "処方最適化"]
    else:
        clinical = "LOW"
        next_steps = ["代替処方の探索", "メカニズム研究の深化"]

    return {
        "efficacy_score": efficacy_score,
        "pathway_coverage": pathway_coverage,
        "synergy_effects": synergy,
        "clinical_potential": clinical,
        "covered_pathways": covered_pathways,
        "recommended_next_steps": next_steps,
        "prediction_basis": "MBT55代謝経路モデル + 293処方データ",
    }

# ─────────────────────────────────────────────
# API Endpoints
# ─────────────────────────────────────────────
@app.get("/")
def root():
    return {
        "message": "MBT Probiotics Screening API",
        "version": "2.0.0",
        "data_source": "30万人実証データ（浜田式）",
        "total_diseases": healthbook_data.get("total_diseases"),
        "total_formulas": kampo_library.get("total_formulas"),
        "docs": "http://localhost:8000/docs",
    }


@app.get("/api/questionnaire")
def get_questionnaire():
    return {
        "questionnaire": MINI_QUESTIONNAIRE,
        "total_questions": len(MINI_QUESTIONNAIRE),
        "estimated_time": "30秒",
    }


@app.post("/api/predict_risk")
def predict_risk(request: QuestionnaireAnswers):
    """30万人実証データに基づく疾病リスク予測"""
    predictions = []
    diseases = healthbook_data.get("diseases", {})

    for name, data in diseases.items():
        score, factors = calculate_disease_risk(request.answers, data)
        if score > 0:
            predictions.append({
                "disease": name,
                "risk_score": score,
                "risk_level": get_risk_level(score),
                "matched_factors": factors,
                "global_impact": get_global_impact(name),
                "gates_priority": get_gates_priority(name),
            })

    predictions.sort(key=lambda x: x["risk_score"], reverse=True)
    return {
        "predictions": predictions[:15],
        "total_diseases_analyzed": len(diseases),
        "data_source": "30万人実証データ（浜田式問診）",
        "confidence": "HIGH",
    }


@app.get("/api/formulas")
def get_formulas(disease: Optional[str] = None, limit: int = 20):
    """漢方処方リスト取得"""
    formulas = kampo_library.get("formulas", [])

    if disease:
        filtered = [
            f for f in formulas
            if disease in f.get("category", "") or
               any(disease in h for h in f.get("main_herbs", []))
        ]
        return {"formulas": filtered[:limit], "total": len(filtered), "filtered_by": disease}

    return {"formulas": formulas[:limit], "total": len(formulas)}


@app.post("/api/predict_efficacy")
def predict_efficacy(request: FormulaSelection):
    """選択した漢方処方の効果予測"""
    formulas = [
        f for f in kampo_library.get("formulas", [])
        if f.get("id") in request.selected_formula_ids
    ]
    if not formulas:
        raise HTTPException(status_code=404, detail="処方が見つかりません")
    return predict_formula_efficacy(formulas, request.disease_id)


@app.get("/api/diseases/priority")
def get_priority_diseases():
    """Gates Foundation優先疾患リスト"""
    return {
        "diseases": [
            {"id": "malnutrition", "name": "栄養不良（微量栄養素欠乏）",
             "global_impact": "8億人", "gates_priority": "HIGH", "market_size": "$20B/year"},
            {"id": "diabetes", "name": "2型糖尿病",
             "global_impact": "5億人", "gates_priority": "MEDIUM", "market_size": "$300B/year"},
            {"id": "hypertension", "name": "高血圧",
             "global_impact": "12億人", "gates_priority": "MEDIUM", "market_size": "$50B/year"},
            {"id": "diarrhea", "name": "感染性下痢症",
             "global_impact": "年50万人死亡（小児）", "gates_priority": "HIGH", "market_size": "$8B/year"},
        ]
    }

# ─────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)