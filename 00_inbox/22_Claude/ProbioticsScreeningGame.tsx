/**
 * MBT Probiotics Screening Game - Main Component
 * 30万人実証データ統合版
 */

import React, { useState, useEffect } from 'react';

// ===== Types =====
interface Question {
  question: string;
  related_factors: string[];
  category: string;
}

interface DiseaseRisk {
  disease: string;
  risk_score: number;
  risk_level: string;
  matched_factors: string[];
  global_impact?: string;
  gates_priority?: string;
}

interface KampoFormula {
  id: string;
  name: string;
  category: string;
  main_herbs: string[];
}

interface EfficacyPrediction {
  efficacy_score: number;
  pathway_coverage: number;
  synergy_effects: number;
  clinical_potential: string;
  covered_pathways: string[];
  recommended_next_steps: string[];
  prediction_basis: string;
}

// ===== Main Component =====
export function ProbioticsScreeningGame() {
  const [step, setStep] = useState<'intro' | 'questionnaire' | 'risk' | 'formulas' | 'results'>('intro');
  const [questionnaire, setQuestionnaire] = useState<Record<string, Question>>({});
  const [answers, setAnswers] = useState<Record<number, boolean>>({});
  const [riskPredictions, setRiskPredictions] = useState<DiseaseRisk[]>([]);
  const [selectedDisease, setSelectedDisease] = useState<string | null>(null);
  const [formulas, setFormulas] = useState<KampoFormula[]>([]);
  const [selectedFormulas, setSelectedFormulas] = useState<string[]>([]);
  const [results, setResults] = useState<EfficacyPrediction | null>(null);
  const [loading, setLoading] = useState(false);

  // ===== Load Questionnaire =====
  useEffect(() => {
    fetch('/api/questionnaire')
      .then(res => res.json())
      .then(data => setQuestionnaire(data.questionnaire));
  }, []);

  // ===== Handle Questionnaire Submit =====
  const handleQuestionnaireSubmit = async () => {
    setLoading(true);
    
    try {
      const res = await fetch('/api/predict_risk', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ answers })
      });
      
      const data = await res.json();
      setRiskPredictions(data.predictions);
      setStep('risk');
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  // ===== Handle Disease Selection =====
  const handleDiseaseSelect = async (disease: string) => {
    setSelectedDisease(disease);
    setLoading(true);
    
    try {
      const res = await fetch(`/api/formulas?disease=${encodeURIComponent(disease)}&limit=30`);
      const data = await res.json();
      setFormulas(data.formulas);
      setStep('formulas');
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  // ===== Handle Formula Selection =====
  const handleFormulaToggle = (formulaId: string) => {
    if (selectedFormulas.includes(formulaId)) {
      setSelectedFormulas(selectedFormulas.filter(id => id !== formulaId));
    } else if (selectedFormulas.length < 10) {
      setSelectedFormulas([...selectedFormulas, formulaId]);
    }
  };

  // ===== Handle Efficacy Prediction =====
  const handlePredictEfficacy = async () => {
    setLoading(true);
    
    try {
      const res = await fetch('/api/predict_efficacy', {
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
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  // ===== Render Functions =====

  // Step 1: Intro
  if (step === 'intro') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 p-8">
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-10">
            <h1 className="text-4xl font-bold text-gray-900 mb-4">
              MBT Probiotics Development Game
            </h1>
            <p className="text-xl text-gray-600 mb-8">
              30万人の実証データに基づくプロバイオティクススクリーニング
            </p>
            
            <div className="bg-blue-50 border-l-4 border-blue-500 p-6 mb-8">
              <h2 className="text-lg font-semibold text-blue-900 mb-2">
                このゲームでできること
              </h2>
              <ul className="space-y-2 text-blue-800">
                <li>✓ 10個の質問に答えて疾病リスクを予測</li>
                <li>✓ 30万人の実証データに基づく精密診断</li>
                <li>✓ 293漢方処方から最適な組み合わせを選択</li>
                <li>✓ MBT55代謝経路モデルで効果を予測</li>
              </ul>
            </div>
            
            <div className="grid grid-cols-3 gap-4 mb-8">
              <div className="bg-green-50 p-4 rounded-lg">
                <div className="text-3xl font-bold text-green-600">93</div>
                <div className="text-sm text-gray-600">疾病分析</div>
              </div>
              <div className="bg-blue-50 p-4 rounded-lg">
                <div className="text-3xl font-bold text-blue-600">293</div>
                <div className="text-sm text-gray-600">漢方処方</div>
              </div>
              <div className="bg-purple-50 p-4 rounded-lg">
                <div className="text-3xl font-bold text-purple-600">30万</div>
                <div className="text-sm text-gray-600">実証データ</div>
              </div>
            </div>
            
            <button
              onClick={() => setStep('questionnaire')}
              className="w-full bg-gradient-to-r from-blue-600 to-green-600 text-white text-lg font-semibold py-4 px-8 rounded-lg hover:from-blue-700 hover:to-green-700 transition transform hover:scale-105"
            >
              開始する（所要時間: 5分）
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Step 2: Questionnaire
  if (step === 'questionnaire') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 p-8">
        <div className="max-w-3xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-8">
            <h2 className="text-3xl font-bold text-gray-900 mb-6">
              ミニ問診（10項目）
            </h2>
            <p className="text-gray-600 mb-8">
              以下の質問に「はい」または「いいえ」でお答えください
            </p>
            
            <div className="space-y-4 mb-8">
              {Object.entries(questionnaire).map(([id, q]) => (
                <div key={id} className="bg-gray-50 p-5 rounded-lg">
                  <p className="text-lg text-gray-800 mb-3">{q.question}</p>
                  <div className="flex gap-4">
                    <button
                      onClick={() => setAnswers({...answers, [parseInt(id)]: true})}
                      className={`flex-1 py-2 px-4 rounded-lg font-medium transition ${
                        answers[parseInt(id)] === true
                          ? 'bg-blue-600 text-white'
                          : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-100'
                      }`}
                    >
                      はい
                    </button>
                    <button
                      onClick={() => setAnswers({...answers, [parseInt(id)]: false})}
                      className={`flex-1 py-2 px-4 rounded-lg font-medium transition ${
                        answers[parseInt(id)] === false
                          ? 'bg-gray-600 text-white'
                          : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-100'
                      }`}
                    >
                      いいえ
                    </button>
                  </div>
                </div>
              ))}
            </div>
            
            <button
              onClick={handleQuestionnaireSubmit}
              disabled={Object.keys(answers).length < 10 || loading}
              className="w-full bg-gradient-to-r from-blue-600 to-green-600 text-white text-lg font-semibold py-4 px-8 rounded-lg hover:from-blue-700 hover:to-green-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? '分析中...' : '疾病リスクを予測'}
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Step 3: Risk Predictions
  if (step === 'risk') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 p-8">
        <div className="max-w-5xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-8">
            <h2 className="text-3xl font-bold text-gray-900 mb-2">
              疾病リスク予測結果
            </h2>
            <p className="text-gray-600 mb-8">
              30万人の実証データに基づく分析
            </p>
            
            <div className="space-y-4 mb-8">
              {riskPredictions.map((pred, idx) => (
                <div
                  key={idx}
                  onClick={() => handleDiseaseSelect(pred.disease)}
                  className="border border-gray-200 rounded-lg p-5 hover:shadow-lg transition cursor-pointer"
                >
                  <div className="flex items-center justify-between mb-3">
                    <h3 className="text-xl font-semibold text-gray-900">{pred.disease}</h3>
                    <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                      pred.risk_level === 'HIGH' ? 'bg-red-100 text-red-800' :
                      pred.risk_level === 'MEDIUM' ? 'bg-yellow-100 text-yellow-800' :
                      'bg-green-100 text-green-800'
                    }`}>
                      {pred.risk_level}
                    </span>
                  </div>
                  
                  <div className="flex items-center gap-6 text-sm text-gray-600">
                    <div>
                      <span className="font-medium">リスクスコア:</span> {pred.risk_score}/100
                    </div>
                    {pred.global_impact && (
                      <div>
                        <span className="font-medium">世界的影響:</span> {pred.global_impact}
                      </div>
                    )}
                    {pred.gates_priority && (
                      <div>
                        <span className="font-medium">Gates優先度:</span> {pred.gates_priority}
                      </div>
                    )}
                  </div>
                  
                  <div className="mt-3">
                    <span className="text-sm text-gray-500">該当因子:</span>{' '}
                    <span className="text-sm text-gray-700">{pred.matched_factors.join(', ')}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }

  // Step 4: Formula Selection
  if (step === 'formulas') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 p-8">
        <div className="max-w-6xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-8">
            <h2 className="text-3xl font-bold text-gray-900 mb-2">
              漢方処方選択
            </h2>
            <p className="text-gray-600 mb-2">
              対象疾患: <span className="font-semibold text-blue-600">{selectedDisease}</span>
            </p>
            <p className="text-sm text-gray-500 mb-8">
              最大10処方まで選択可能（{selectedFormulas.length}/10）
            </p>
            
            <div className="grid grid-cols-3 gap-4 mb-8">
              {formulas.map(formula => (
                <div
                  key={formula.id}
                  onClick={() => handleFormulaToggle(formula.id)}
                  className={`border-2 rounded-lg p-4 cursor-pointer transition ${
                    selectedFormulas.includes(formula.id)
                      ? 'border-blue-500 bg-blue-50'
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <div className="flex items-start justify-between mb-2">
                    <h3 className="font-semibold text-gray-900">{formula.name}</h3>
                    {selectedFormulas.includes(formula.id) && (
                      <span className="text-blue-600">✓</span>
                    )}
                  </div>
                  <p className="text-xs text-gray-600 mb-2">{formula.id}</p>
                  <div className="text-sm text-gray-700">
                    <span className="font-medium">主要生薬:</span>
                    <div className="mt-1 text-xs">
                      {formula.main_herbs.slice(0, 3).join('、')}
                    </div>
                  </div>
                </div>
              ))}
            </div>
            
            <button
              onClick={handlePredictEfficacy}
              disabled={selectedFormulas.length === 0 || loading}
              className="w-full bg-gradient-to-r from-blue-600 to-green-600 text-white text-lg font-semibold py-4 px-8 rounded-lg hover:from-blue-700 hover:to-green-700 transition disabled:opacity-50"
            >
              {loading ? '効果予測中...' : '効果を予測'}
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Step 5: Results
  if (step === 'results' && results) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 p-8">
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-8">
            <h2 className="text-3xl font-bold text-gray-900 mb-8">
              効果予測結果
            </h2>
            
            <div className="bg-gradient-to-r from-blue-500 to-green-500 rounded-lg p-8 mb-8 text-white">
              <div className="text-center">
                <div className="text-6xl font-bold mb-2">
                  {results.efficacy_score.toFixed(0)}/100
                </div>
                <div className="text-xl">総合スコア</div>
                <div className="mt-4 flex items-center justify-center gap-1">
                  {[...Array(5)].map((_, i) => (
                    <span key={i} className={i < Math.floor(results.efficacy_score / 20) ? 'text-yellow-300' : 'text-white/30'}>
                      ⭐
                    </span>
                  ))}
                </div>
              </div>
            </div>
            
            <div className="grid grid-cols-2 gap-6 mb-8">
              <div className="bg-blue-50 p-6 rounded-lg">
                <div className="text-sm text-gray-600 mb-1">代謝経路カバレッジ</div>
                <div className="text-3xl font-bold text-blue-600">
                  {results.pathway_coverage.toFixed(0)}%
                </div>
              </div>
              <div className="bg-green-50 p-6 rounded-lg">
                <div className="text-sm text-gray-600 mb-1">シナジー効果</div>
                <div className="text-3xl font-bold text-green-600">
                  +{results.synergy_effects}
                </div>
              </div>
            </div>
            
            <div className="mb-8">
              <h3 className="text-lg font-semibold text-gray-900 mb-3">
                カバーされた代謝経路
              </h3>
              <div className="space-y-2">
                {results.covered_pathways.map((pathway, idx) => (
                  <div key={idx} className="flex items-center gap-2 text-green-700">
                    <span>✓</span>
                    <span>{pathway}</span>
                  </div>
                ))}
              </div>
            </div>
            
            <div className="bg-yellow-50 border-l-4 border-yellow-500 p-6 mb-8">
              <h3 className="text-lg font-semibold text-yellow-900 mb-2">
                臨床ポテンシャル: {results.clinical_potential}
              </h3>
              <p className="text-sm text-yellow-800 mb-4">
                予測根拠: {results.prediction_basis}
              </p>
              <div>
                <div className="font-medium text-yellow-900 mb-2">推奨次ステップ:</div>
                <ol className="list-decimal list-inside space-y-1 text-yellow-800">
                  {results.recommended_next_steps.map((step, idx) => (
                    <li key={idx}>{step}</li>
                  ))}
                </ol>
              </div>
            </div>
            
            <button
              onClick={() => {
                setStep('intro');
                setAnswers({});
                setSelectedFormulas([]);
                setResults(null);
              }}
              className="w-full bg-gray-600 text-white text-lg font-semibold py-4 px-8 rounded-lg hover:bg-gray-700 transition"
            >
              新しいスクリーニングを開始
            </button>
          </div>
        </div>
      </div>
    );
  }

  return null;
}

export default ProbioticsScreeningGame;
