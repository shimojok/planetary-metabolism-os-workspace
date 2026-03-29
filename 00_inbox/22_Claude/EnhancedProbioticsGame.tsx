/**
 * MBT Probiotics Screening Game v2.0 - Enhanced Version
 * 105項目問診 + ファイトケミカル詳細表示
 */

import React, { useState, useEffect } from 'react';

// ===== Types =====
interface PhytochemicalDetail {
  name: string;
  japanese_name: string;
  classification: string;
  subcategory: string;
  color: string;
  source_foods: string[];
  clinical_benefits: string[];
  bioavailability: string;
  absorption_mechanism: string;
  daily_intake_mg: string;
  mbt_pathway: string;
}

interface PhytochemicalRecommendation {
  phytochemical: PhytochemicalDetail;
  relevance_score: number;
  mechanism_explanation: string;
  practical_example: string;
}

interface EnhancedDiseaseProfile {
  disease: string;
  risk_score: number;
  risk_level: string;
  matched_factors: string[];
  recommended_phytochemicals: PhytochemicalRecommendation[];
  metabolic_blockages: string[];
  mbt55_pathways_needed: string[];
}

interface PhytochemicalSynergy {
  combination: string;
  effect: string;
}

interface EfficacyPrediction {
  efficacy_score: number;
  pathway_coverage: number;
  synergy_effects: number;
  clinical_potential: string;
  covered_pathways: string[];
  phytochemical_synergies: PhytochemicalSynergy[];
  recommended_next_steps: string[];
  prediction_basis: string;
}

// ===== Main Component =====
export function EnhancedProbioticsGame() {
  const [step, setStep] = useState<'intro' | 'mode' | 'questionnaire' | 'risk' | 'disease_detail' | 'formulas' | 'results'>('intro');
  const [questionnaireMode, setQuestionnaireMode] = useState<'mini' | 'full'>('mini');
  const [questionnaire, setQuestionnaire] = useState<Record<string, any>>({});
  const [answers, setAnswers] = useState<Record<number, boolean>>({});
  const [riskPredictions, setRiskPredictions] = useState<EnhancedDiseaseProfile[]>([]);
  const [selectedDisease, setSelectedDisease] = useState<EnhancedDiseaseProfile | null>(null);
  const [allPhytochemicals, setAllPhytochemicals] = useState<any[]>([]);
  const [formulas, setFormulas] = useState<any[]>([]);
  const [selectedFormulas, setSelectedFormulas] = useState<string[]>([]);
  const [selectedPhytos, setSelectedPhytos] = useState<string[]>([]);
  const [results, setResults] = useState<EfficacyPrediction | null>(null);
  const [loading, setLoading] = useState(false);

  // ===== Load All Phytochemicals =====
  useEffect(() => {
    fetch('/api/phytochemicals')
      .then(res => res.json())
      .then(data => setAllPhytochemicals(data.phytochemicals));
  }, []);

  // ===== Step 1: Intro =====
  if (step === 'intro') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-green-50 to-purple-50 p-8">
        <div className="max-w-5xl mx-auto">
          <div className="bg-white rounded-3xl shadow-2xl p-12">
            <div className="text-center mb-8">
              <h1 className="text-5xl font-bold bg-gradient-to-r from-blue-600 to-green-600 bg-clip-text text-transparent mb-4">
                MBT Probiotics Development Game
              </h1>
              <p className="text-2xl text-gray-600">
                v2.0 Enhanced Edition
              </p>
            </div>
            
            <div className="bg-gradient-to-r from-blue-100 to-green-100 border-l-4 border-blue-600 p-8 mb-8 rounded-lg">
              <h2 className="text-2xl font-semibold text-blue-900 mb-4">
                🚀 新機能（v2.0）
              </h2>
              <div className="grid md:grid-cols-2 gap-4 text-blue-800">
                <div>
                  <h3 className="font-semibold mb-2">✨ 問診システム強化</h3>
                  <ul className="space-y-1 text-sm">
                    <li>• ミニ版: 10項目（30秒）</li>
                    <li>• フル版: 105項目（5-10分）</li>
                    <li>• より精密な疾病リスク予測</li>
                  </ul>
                </div>
                <div>
                  <h3 className="font-semibold mb-2">🧬 ファイトケミカル詳細</h3>
                  <ul className="space-y-1 text-sm">
                    <li>• 12種類の詳細データ</li>
                    <li>• 生物学的利用能解析</li>
                    <li>• 吸収メカニズム説明</li>
                    <li>• シナジー効果予測</li>
                  </ul>
                </div>
              </div>
            </div>
            
            <div className="grid grid-cols-4 gap-4 mb-10">
              <div className="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-xl text-center">
                <div className="text-4xl font-bold text-blue-600">105</div>
                <div className="text-sm text-gray-600 mt-2">問診項目</div>
              </div>
              <div className="bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-xl text-center">
                <div className="text-4xl font-bold text-green-600">12</div>
                <div className="text-sm text-gray-600 mt-2">ファイトケミカル</div>
              </div>
              <div className="bg-gradient-to-br from-purple-50 to-purple-100 p-6 rounded-xl text-center">
                <div className="text-4xl font-bold text-purple-600">93</div>
                <div className="text-sm text-gray-600 mt-2">疾病分析</div>
              </div>
              <div className="bg-gradient-to-br from-orange-50 to-orange-100 p-6 rounded-xl text-center">
                <div className="text-4xl font-bold text-orange-600">30万</div>
                <div className="text-sm text-gray-600 mt-2">実証データ</div>
              </div>
            </div>
            
            <button
              onClick={() => setStep('mode')}
              className="w-full bg-gradient-to-r from-blue-600 via-green-600 to-purple-600 text-white text-xl font-bold py-5 px-8 rounded-2xl hover:shadow-2xl transition transform hover:scale-105"
            >
              🚀 開始する
            </button>
          </div>
        </div>
      </div>
    );
  }

  // ===== Step 2: Mode Selection =====
  if (step === 'mode') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 p-8">
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-10">
            <h2 className="text-4xl font-bold text-gray-900 mb-3 text-center">
              問診モード選択
            </h2>
            <p className="text-gray-600 mb-10 text-center">
              目的に応じて選択してください
            </p>
            
            <div className="grid md:grid-cols-2 gap-6">
              {/* ミニ版 */}
              <div
                onClick={() => {
                  setQuestionnaireMode('mini');
                  setStep('questionnaire');
                }}
                className="border-3 border-blue-300 bg-blue-50 rounded-2xl p-8 cursor-pointer hover:shadow-xl transition transform hover:scale-105"
              >
                <div className="text-center mb-4">
                  <div className="text-6xl mb-3">⚡</div>
                  <h3 className="text-2xl font-bold text-blue-900">ミニ版</h3>
                  <p className="text-blue-700 mt-2">10項目 / 30秒</p>
                </div>
                <ul className="space-y-2 text-sm text-blue-800">
                  <li>✓ 素早く結果が欲しい方</li>
                  <li>✓ 初めての方におすすめ</li>
                  <li>✓ 主要なリスクを把握</li>
                  <li>✓ デモ・体験用</li>
                </ul>
              </div>
              
              {/* フル版 */}
              <div
                onClick={() => {
                  setQuestionnaireMode('full');
                  setStep('questionnaire');
                }}
                className="border-3 border-green-300 bg-green-50 rounded-2xl p-8 cursor-pointer hover:shadow-xl transition transform hover:scale-105"
              >
                <div className="text-center mb-4">
                  <div className="text-6xl mb-3">🔬</div>
                  <h3 className="text-2xl font-bold text-green-900">フル版</h3>
                  <p className="text-green-700 mt-2">105項目 / 5-10分</p>
                </div>
                <ul className="space-y-2 text-sm text-green-800">
                  <li>✓ 詳細な分析が欲しい方</li>
                  <li>✓ 精密な診断を希望</li>
                  <li>✓ 全カテゴリ網羅</li>
                  <li>✓ 本格的な健康管理</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  // ===== Step 3: Questionnaire (既存コードを拡張) =====
  // ... (既存のQuestionnaireコードにモード対応を追加)

  // ===== Step 4: Enhanced Risk Display with Phytochemicals =====
  if (step === 'risk') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50 p-8">
        <div className="max-w-7xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-8">
            <h2 className="text-3xl font-bold text-gray-900 mb-2">
              疾病リスク予測結果
            </h2>
            <p className="text-gray-600 mb-2">
              30万人の実証データ + ファイトケミカル推奨
            </p>
            <p className="text-sm text-gray-500 mb-8">
              モード: {questionnaireMode === 'mini' ? 'ミニ版（10項目）' : 'フル版（105項目）'}
            </p>
            
            <div className="space-y-6">
              {riskPredictions.map((pred, idx) => (
                <div
                  key={idx}
                  onClick={() => {
                    setSelectedDisease(pred);
                    setStep('disease_detail');
                  }}
                  className="border-2 border-gray-200 rounded-xl p-6 hover:shadow-2xl transition cursor-pointer hover:border-blue-400"
                >
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex-1">
                      <h3 className="text-2xl font-bold text-gray-900 mb-2">
                        {idx + 1}. {pred.disease}
                      </h3>
                      <div className="flex items-center gap-4 text-sm">
                        <span className={`px-4 py-1 rounded-full font-medium ${
                          pred.risk_level === 'HIGH' ? 'bg-red-100 text-red-800' :
                          pred.risk_level === 'MEDIUM' ? 'bg-yellow-100 text-yellow-800' :
                          'bg-green-100 text-green-800'
                        }`}>
                          {pred.risk_level} リスク
                        </span>
                        <span className="text-gray-600">
                          スコア: <span className="font-bold">{pred.risk_score}/100</span>
                        </span>
                      </div>
                    </div>
                  </div>
                  
                  {/* 推奨ファイトケミカル（プレビュー） */}
                  {pred.recommended_phytochemicals.length > 0 && (
                    <div className="mt-4 bg-blue-50 rounded-lg p-4">
                      <div className="text-sm font-semibold text-blue-900 mb-2">
                        💊 推奨ファイトケミカル（{pred.recommended_phytochemicals.length}種類）
                      </div>
                      <div className="flex flex-wrap gap-2">
                        {pred.recommended_phytochemicals.slice(0, 3).map((rec, i) => (
                          <span key={i} className="px-3 py-1 bg-white rounded-full text-xs font-medium text-blue-700 border border-blue-200">
                            {rec.phytochemical.japanese_name}
                          </span>
                        ))}
                        {pred.recommended_phytochemicals.length > 3 && (
                          <span className="px-3 py-1 text-xs text-blue-600">
                            +{pred.recommended_phytochemicals.length - 3}種類
                          </span>
                        )}
                      </div>
                    </div>
                  )}
                  
                  <div className="mt-4 text-sm text-gray-600">
                    👉 クリックして詳細を見る
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }

  // ===== Step 5: Disease Detail with Phytochemical Recommendations =====
  if (step === 'disease_detail' && selectedDisease) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-50 to-pink-50 p-8">
        <div className="max-w-6xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-8">
            {/* ヘッダー */}
            <div className="mb-8">
              <button
                onClick={() => setStep('risk')}
                className="text-blue-600 hover:text-blue-800 mb-4"
              >
                ← 戻る
              </button>
              <h2 className="text-4xl font-bold text-gray-900 mb-3">
                {selectedDisease.disease}
              </h2>
              <div className="flex items-center gap-4">
                <span className={`px-4 py-2 rounded-full font-medium text-lg ${
                  selectedDisease.risk_level === 'HIGH' ? 'bg-red-100 text-red-800' :
                  selectedDisease.risk_level === 'MEDIUM' ? 'bg-yellow-100 text-yellow-800' :
                  'bg-green-100 text-green-800'
                }`}>
                  {selectedDisease.risk_level} リスク
                </span>
                <span className="text-2xl font-bold text-gray-700">
                  {selectedDisease.risk_score}/100
                </span>
              </div>
            </div>
            
            {/* 推奨ファイトケミカル詳細 */}
            <div className="mb-8">
              <h3 className="text-2xl font-bold text-gray-900 mb-6">
                💊 推奨ファイトケミカル
              </h3>
              
              <div className="space-y-6">
                {selectedDisease.recommended_phytochemicals.map((rec, idx) => (
                  <div key={idx} className="border-2 border-blue-200 rounded-xl p-6 bg-gradient-to-r from-blue-50 to-purple-50">
                    <div className="flex items-start justify-between mb-4">
                      <div>
                        <h4 className="text-2xl font-bold text-blue-900 mb-1">
                          {rec.phytochemical.japanese_name}
                        </h4>
                        <p className="text-sm text-gray-600">
                          {rec.phytochemical.classification} / {rec.phytochemical.subcategory}
                        </p>
                      </div>
                      <div className="text-right">
                        <div className="text-3xl font-bold text-blue-600">
                          {rec.relevance_score.toFixed(0)}
                        </div>
                        <div className="text-xs text-gray-500">関連性</div>
                      </div>
                    </div>
                    
                    {/* 含有食品 */}
                    <div className="mb-4">
                      <div className="text-sm font-semibold text-gray-700 mb-2">
                        📦 含有食品:
                      </div>
                      <div className="flex flex-wrap gap-2">
                        {rec.phytochemical.source_foods.map((food, i) => (
                          <span key={i} className="px-3 py-1 bg-white rounded-lg text-sm border border-gray-200">
                            {food}
                          </span>
                        ))}
                      </div>
                    </div>
                    
                    {/* 臨床効果 */}
                    <div className="mb-4">
                      <div className="text-sm font-semibold text-gray-700 mb-2">
                        ✨ 臨床効果:
                      </div>
                      <div className="grid grid-cols-2 gap-2">
                        {rec.phytochemical.clinical_benefits.map((benefit, i) => (
                          <div key={i} className="flex items-center gap-2 text-sm text-gray-700">
                            <span className="text-green-500">✓</span>
                            {benefit}
                          </div>
                        ))}
                      </div>
                    </div>
                    
                    {/* メカニズム */}
                    <div className="bg-white rounded-lg p-4 mb-4">
                      <div className="text-sm font-semibold text-gray-700 mb-2">
                        🔬 吸収メカニズム:
                      </div>
                      <p className="text-sm text-gray-600">
                        {rec.phytochemical.absorption_mechanism}
                      </p>
                    </div>
                    
                    {/* 推奨摂取量 */}
                    <div className="grid grid-cols-3 gap-4 text-center">
                      <div className="bg-white rounded-lg p-3">
                        <div className="text-xs text-gray-500 mb-1">推奨摂取量</div>
                        <div className="text-lg font-bold text-blue-600">
                          {rec.phytochemical.daily_intake_mg} mg/日
                        </div>
                      </div>
                      <div className="bg-white rounded-lg p-3">
                        <div className="text-xs text-gray-500 mb-1">生物学的利用能</div>
                        <div className="text-lg font-bold text-green-600">
                          {rec.phytochemical.bioavailability}
                        </div>
                      </div>
                      <div className="bg-white rounded-lg p-3">
                        <div className="text-xs text-gray-500 mb-1">MBT55経路</div>
                        <div className="text-sm font-bold text-purple-600">
                          {rec.phytochemical.mbt_pathway}
                        </div>
                      </div>
                    </div>
                    
                    {/* 実践例 */}
                    <div className="mt-4 bg-yellow-50 border-l-4 border-yellow-400 p-4">
                      <div className="text-sm font-semibold text-yellow-900 mb-1">
                        💡 実践例
                      </div>
                      <p className="text-sm text-yellow-800">
                        {rec.practical_example}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
            
            {/* 次へ進むボタン */}
            <button
              onClick={() => setStep('formulas')}
              className="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white text-lg font-bold py-4 rounded-xl hover:shadow-xl transition"
            >
              漢方処方を選択 →
            </button>
          </div>
        </div>
      </div>
    );
  }

  // ... (残りのステップ: formulas, results)

  return null;
}

export default EnhancedProbioticsGame;
