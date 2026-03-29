"""
MBT Probiotics Screening API - 統合完全版（Windows対応）
main.py + main_v2.py を統合・パス修正済み

必要ファイル（このファイルと同じフォルダに置いてください）:
  - healthbook_expanded_v2.json  （93疾病・105問診・12ファイトケミカル）
  - mbt_kampo_library_final_array.json  （293漢方処方）

起動方法:
  pip install fastapi uvicorn pydantic
  python game3_api.py

アクセス:
  API:      http://localhost:8000
  ドキュメント: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import json
from pathlib import Path

# ─────────────────────────────────────────────
# パス設定（このファイルと同じフォルダを参照）
# ─────────────────────────────────────────────
BASE_DIR = Path(__file__).parent

HEALTHBOOK_PATH = BASE_DIR / "healthbook_expanded_v2.json"
KAMPO_PATH      = BASE_DIR / "mbt_kampo_library_final_array.json"

# ─────────────────────────────────────────────
# アプリ初期化
# ─────────────────────────────────────────────
app = FastAPI(
    title="MBT Probiotics Screening API",
    description="30万人実証データ × 93疾病 × 105問診 × 12ファイトケミカル × 293漢方処方",
    version="3.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────
# データロード
# ─────────────────────────────────────────────
print("=" * 55)
print("  MBT Probiotics Screening API v3.0 起動中...")
print("=" * 55)

for path, label in [(HEALTHBOOK_PATH, "HealthBook"), (KAMPO_PATH, "漢方ライブラリー")]:
    if not path.exists():
        raise FileNotFoundError(
            f"\n❌ {label}ファイルが見つかりません。\n"
            f"   場所: {path}\n"
            f"   このPythonファイルと同じフォルダに置いてください。"
        )

with open(HEALTHBOOK_PATH, "r", encoding="utf-8") as f:
    hb = json.load(f)

with open(KAMPO_PATH, "r", encoding="utf-8") as f:
    kampo = json.load(f)

print(f"  ✅ 疾病データ:     {hb.get('total_diseases', '?')} 件")
print(f"  ✅ 問診項目:       {hb.get('total_questionnaire_items', '?')} 項目")
print(f"  ✅ ファイトケミカル: {hb.get('total_phytochemicals', '?')} 種")
print(f"  ✅ 漢方処方:       {kampo.get('total_formulas', '?')} 件")
print(f"  ✅ API起動完了:    http://localhost:8000")
print(f"  📖 ドキュメント:   http://localhost:8000/docs")
print("=" * 55)

# ─────────────────────────────────────────────
# Models
# ─────────────────────────────────────────────
class QuestionnaireMode(BaseModel):
    mode: str = "mini"  # "mini"（10項目）or "full"（105項目）

class QuestionnaireAnswers(BaseModel):
    answers: Dict[int, bool]
    mode: str = "mini"

class FormulaSelection(BaseModel):
    disease_id: str
    selected_formula_ids: List[str]
    selected_phytochemical_ids: Optional[List[str]] = []

# ─────────────────────────────────────────────
# Helper: リスク計算
# ─────────────────────────────────────────────
def calculate_risk(answers: Dict[int, bool], disease_data: Dict, mode: str = "mini"):
    questionnaire = (
        hb.get("mini_questionnaire", {})
        if mode == "mini"
        else hb.get("full_questionnaire_200", {})
    )

    risk_score = 0.0
    matched = []

    for q_id, answer in answers.items():
        if not answer:
            continue
        q_data = questionnaire.get(str(q_id), {})
        for factor, fdata in disease_data.get("risk_factors", {}).items():
            if factor in q_data.get("related_factors", []) and factor not in matched:
                risk_score += fdata.get("weight", 0.5)
                matched.append(factor)

    max_w = sum(f.get("weight", 0.5) for f in disease_data.get("risk_factors", {}).values())
    normalized = round((risk_score / max_w * 100) if max_w > 0 else 0.0, 1)
    return normalized, matched


def risk_level(score: float) -> str:
    if score >= 70:   return "HIGH"
    elif score >= 40: return "MEDIUM"
    elif score >= 20: return "LOW"
    return "VERY_LOW"


def gates_priority(disease: str) -> str:
    high = ["糖尿病", "高血圧", "栄養失調", "肺炎", "下痢", "結核", "マラリア", "感染症"]
    return "HIGH" if any(h in disease for h in high) else "MEDIUM"


def global_impact(disease: str) -> str:
    impacts = {
        "糖尿病": "5億人", "高血圧": "12億人", "がん": "2,000万人/年",
        "心筋梗塞": "1,800万人/年", "脳卒中": "1,500万人/年", "肥満": "8億人",
    }
    for k, v in impacts.items():
        if k in disease:
            return v
    return "推定1,000万人以上"

# ─────────────────────────────────────────────
# Helper: ファイトケミカル推奨
# ─────────────────────────────────────────────
DISEASE_PHYTO_MAP = {
    "高血圧":   ["quercetin", "rutin", "allicin"],
    "糖尿病":   ["catechin", "isoflavone", "curcumin"],
    "肥満":     ["capsaicin", "catechin", "curcumin"],
    "動脈硬化": ["quercetin", "lycopene", "beta_carotene"],
    "がん":     ["sulforaphane", "lycopene", "curcumin", "quercetin"],
    "認知症":   ["anthocyanin", "catechin", "curcumin"],
    "骨粗鬆症": ["isoflavone"],
    "アレルギー": ["quercetin", "catechin"],
    "白内障":   ["lutein", "beta_carotene"],
    "前立腺":   ["lycopene", "isoflavone"],
}

KNOWN_SYNERGIES = {
    ("quercetin", "rutin"):          "ルチンがケルセチンの前駆体として作用し、吸収効率向上",
    ("catechin", "curcumin"):        "両者の抗酸化作用が相乗効果を発揮",
    ("lycopene", "beta_carotene"):   "カロテノイド類の相互作用で抗酸化力増強",
    ("allicin", "sulforaphane"):     "硫黄化合物の解毒酵素誘導が相乗",
    ("anthocyanin", "catechin"):     "ポリフェノールの抗酸化シナジー",
}


def get_phyto_recommendations(disease: str, risk_score: float) -> List[Dict]:
    phyto_db = hb.get("phytochemicals_detailed", {})
    candidates = []
    for key, phytos in DISEASE_PHYTO_MAP.items():
        if key in disease:
            candidates.extend(phytos)
    candidates = list(set(candidates))[:5]

    result = []
    for pid in candidates:
        if pid not in phyto_db:
            continue
        p = phyto_db[pid]
        result.append({
            "id": pid,
            "phytochemical": p,
            "relevance_score": round(min(100, risk_score * 1.2), 1),
            "mechanism_explanation": (
                f"{p.get('absorption_mechanism', '')}により、"
                f"{', '.join(p.get('clinical_benefits', [])[:2])}を実現"
            ),
            "practical_example": (
                f"{p.get('source_foods', [''])[0]}を"
                f"推奨摂取量{p.get('daily_intake_mg', '?')}mg/日"
            ),
        })
    return result


def analyze_synergies(phyto_ids: List[str]) -> List[Dict]:
    phyto_db = hb.get("phytochemicals_detailed", {})
    found = []
    for i, p1 in enumerate(phyto_ids):
        for p2 in phyto_ids[i + 1:]:
            key = tuple(sorted([p1, p2]))
            if key in KNOWN_SYNERGIES:
                found.append({
                    "combination": (
                        f"{phyto_db.get(p1, {}).get('japanese_name', p1)} + "
                        f"{phyto_db.get(p2, {}).get('japanese_name', p2)}"
                    ),
                    "effect": KNOWN_SYNERGIES[key],
                })
    return found


def predict_efficacy(formulas: List[Dict], disease: str, phyto_ids: List[str] = None) -> Dict:
    pathway_counts: Dict[str, int] = {}
    covered = []
    extracted_phytos = []

    for formula in formulas:
        for herb, details in formula.get("components", {}).items():
            for phyto in details.get("phytochemicals", []):
                pw = phyto.get("metabolic_pathway")
                if pw:
                    pathway_counts[pw] = pathway_counts.get(pw, 0) + 1
                    if pw not in covered:
                        covered.append(pw)
                name = phyto.get("name", "").lower()
                if "quercetin" in name or "ケルセチン" in name:
                    extracted_phytos.append("quercetin")
                elif "catechin" in name or "カテキン" in name:
                    extracted_phytos.append("catechin")

    all_phytos = list(set(extracted_phytos + (phyto_ids or [])))
    synergies = analyze_synergies(all_phytos)

    base     = len(covered) * 20
    syn_score = sum((c - 1) * 10 for c in pathway_counts.values() if c > 1)
    syn_score += len(synergies) * 15
    efficacy  = min(100, base + syn_score)
    coverage  = min(100, len(covered) * 25)

    if efficacy >= 70:
        clinical = "HIGH"
        steps = ["Phase 1臨床試験準備", "FDA Fast Track申請",
                 "Gates Foundation助成申請", "アフリカ3カ国パイロット"]
    elif efficacy >= 40:
        clinical = "MEDIUM"
        steps = ["追加スクリーニング", "in vitro検証", "処方最適化", "予備的臨床研究"]
    else:
        clinical = "LOW"
        steps = ["代替処方の探索", "メカニズム研究の深化"]

    return {
        "efficacy_score": efficacy,
        "pathway_coverage": coverage,
        "synergy_effects": syn_score,
        "clinical_potential": clinical,
        "covered_pathways": covered,
        "phytochemical_synergies": synergies,
        "recommended_next_steps": steps,
        "prediction_basis": "MBT55代謝経路モデル + ファイトケミカルシナジー + 293処方データ",
    }

# ─────────────────────────────────────────────
# API Endpoints
# ─────────────────────────────────────────────
@app.get("/")
def root():
    return {
        "message": "MBT Probiotics Screening API v3.0",
        "data_statistics": {
            "diseases":            hb.get("total_diseases"),
            "questionnaire_items": hb.get("total_questionnaire_items"),
            "phytochemicals":      hb.get("total_phytochemicals"),
            "kampo_formulas":      kampo.get("total_formulas"),
        },
        "endpoints": {
            "questionnaire":     "POST /api/questionnaire/mode",
            "predict_risk":      "POST /api/predict_risk",
            "predict_enhanced":  "POST /api/predict_risk/enhanced",
            "phytochemicals":    "GET  /api/phytochemicals",
            "formulas":          "GET  /api/formulas",
            "predict_efficacy":  "POST /api/predict_efficacy",
            "priority_diseases": "GET  /api/diseases/priority",
        },
        "docs": "http://localhost:8000/docs",
    }


@app.post("/api/questionnaire/mode")
def get_questionnaire(request: QuestionnaireMode):
    """問診票取得（ミニ版10項目 / フル版105項目）"""
    if request.mode == "mini":
        q = hb.get("mini_questionnaire", {})
        time_est = "30秒"
    elif request.mode == "full":
        q = hb.get("full_questionnaire_200", {})
        time_est = "5〜10分"
    else:
        raise HTTPException(400, "mode は 'mini' または 'full' を指定してください")
    return {"mode": request.mode, "questionnaire": q,
            "total_questions": len(q), "estimated_time": time_est}


@app.get("/api/questionnaire")
def get_mini_questionnaire():
    """ミニ問診票（10項目）取得"""
    q = hb.get("mini_questionnaire", {})
    return {"questionnaire": q, "total_questions": len(q), "estimated_time": "30秒"}


@app.post("/api/predict_risk")
def predict_risk(request: QuestionnaireAnswers):
    """疾病リスク予測（基本版）"""
    preds = []
    for name, data in hb.get("diseases", {}).items():
        score, factors = calculate_risk(request.answers, data, request.mode)
        if score > 0:
            preds.append({
                "disease": name, "risk_score": score,
                "risk_level": risk_level(score), "matched_factors": factors,
                "global_impact": global_impact(name),
                "gates_priority": gates_priority(name),
            })
    preds.sort(key=lambda x: x["risk_score"], reverse=True)
    return {
        "predictions": preds[:15],
        "total_diseases_analyzed": len(hb.get("diseases", {})),
        "data_source": "30万人実証データ（浜田式問診）",
        "confidence": "HIGH",
    }


@app.post("/api/predict_risk/enhanced")
def predict_risk_enhanced(request: QuestionnaireAnswers):
    """疾病リスク予測（拡張版）- ファイトケミカル推奨付き"""
    preds = []
    for name, data in hb.get("diseases", {}).items():
        score, factors = calculate_risk(request.answers, data, request.mode)
        if score > 10:
            phyto_recs = get_phyto_recommendations(name, score)
            preds.append({
                "disease": name, "risk_score": score,
                "risk_level": risk_level(score), "matched_factors": factors,
                "recommended_phytochemicals": phyto_recs,
                "metabolic_blockages": [f"{f}による代謝阻害" for f in factors[:3]],
                "mbt55_pathways_needed": list(set(
                    r["phytochemical"].get("mbt_pathway", "")
                    for r in phyto_recs
                )),
                "global_impact": global_impact(name),
                "gates_priority": gates_priority(name),
            })
    preds.sort(key=lambda x: x["risk_score"], reverse=True)
    return {
        "mode": request.mode,
        "predictions": preds[:15],
        "total_analyzed": len(hb.get("diseases", {})),
        "data_source": "30万人実証データ + ファイトケミカル詳細DB",
        "confidence": "HIGH",
    }


@app.get("/api/phytochemicals")
def get_phytochemicals():
    """全ファイトケミカル詳細リスト（12種）"""
    db = hb.get("phytochemicals_detailed", {})
    return {"phytochemicals": [{"id": k, **v} for k, v in db.items()], "total": len(db)}


@app.get("/api/phytochemicals/{phyto_id}")
def get_phytochemical(phyto_id: str):
    """特定ファイトケミカルの詳細"""
    db = hb.get("phytochemicals_detailed", {})
    if phyto_id not in db:
        raise HTTPException(404, "ファイトケミカルが見つかりません")
    return {"id": phyto_id, **db[phyto_id]}


@app.get("/api/formulas")
def get_formulas(disease: Optional[str] = None, limit: int = 20):
    """漢方処方リスト（293件）"""
    formulas = kampo.get("formulas", [])
    if disease:
        formulas = [
            f for f in formulas
            if disease in f.get("category", "") or
               any(disease in h for h in f.get("main_herbs", []))
        ]
    return {"formulas": formulas[:limit], "total": len(formulas)}


@app.post("/api/predict_efficacy")
def predict_efficacy_endpoint(request: FormulaSelection):
    """漢方処方の効果予測（シナジー解析付き）"""
    formulas = [
        f for f in kampo.get("formulas", [])
        if f.get("id") in request.selected_formula_ids
    ]
    if not formulas and not request.selected_phytochemical_ids:
        raise HTTPException(400, "処方またはファイトケミカルを選択してください")
    return predict_efficacy(formulas, request.disease_id, request.selected_phytochemical_ids)


@app.get("/api/diseases/priority")
def get_priority_diseases():
    """Gates Foundation優先疾患リスト"""
    return {
        "diseases": [
            {"id": "malnutrition", "name": "栄養不良（微量栄養素欠乏）",
             "global_impact": "8億人", "gates_priority": "HIGH", "market_size": "$20B/year"},
            {"id": "diarrhea", "name": "感染性下痢症",
             "global_impact": "年50万人死亡（小児）", "gates_priority": "HIGH", "market_size": "$8B/year"},
            {"id": "diabetes", "name": "2型糖尿病",
             "global_impact": "5億人", "gates_priority": "MEDIUM", "market_size": "$300B/year"},
            {"id": "hypertension", "name": "高血圧",
             "global_impact": "12億人", "gates_priority": "MEDIUM", "market_size": "$50B/year"},
        ]
    }


# ─────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
