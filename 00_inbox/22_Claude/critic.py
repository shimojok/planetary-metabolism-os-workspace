"""
PMOS v2.0 — Day 4-5: Critic Agent
===================================
分類結果の品質を検証し、問題点を指摘・修正案を提案する。
Orchestratorと組み合わせて最大3回の批評ループを実行。

使用方法:
    python agents/critic.py
"""

import sys
import json
from pathlib import Path
from typing import Dict, List
from tqdm import tqdm

import openai

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import (
    DATA_DIR, OPENAI_API_KEY,
    save_json, load_json, load_note_content, get_logger
)

logger = get_logger("CriticAgent")


# ========================================
# Critic Agent
# ========================================

class CriticAgent:
    """
    分類結果を批評し、改善を促す「品質保証エージェント」。

    批評観点:
      1. ドメインの適切性（分類のズレを検出）
      2. エンティティの網羅性（見落としを指摘）
      3. 要約の正確性（本質を捉えているか）
      4. 関係の論理的一貫性
    """

    def __init__(self):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
        self.history: List[Dict] = []

    # -------- 分類批評 --------

    def critique_classification(
        self,
        note_path: str,
        classification: Dict,
        content: str | None = None
    ) -> Dict:
        """
        1つの分類結果を批評する。

        Returns:
            {
              "is_appropriate": bool,
              "quality_score": float (0-1),
              "issues": List[str],
              "suggested_corrections": dict,
              "confidence_in_critique": float
            }
        """
        if content is None:
            content = load_note_content(note_path, max_chars=2000)

        prompt = f"""
あなたはPMOS知識グラフの品質保証エージェントです。
以下のノート分類結果を厳密に批評してください。

【ノート内容（最大2000文字）】
{content}

【提案された分類】
{json.dumps(classification, ensure_ascii=False, indent=2)}

【批評の観点】
1. primary_domain の選択は内容と一致しているか？
2. subcategory は適切か？
3. key_entities に重要なエンティティが含まれているか？
4. relationsの論理的整合性（因果・包含・対立関係が正しいか）
5. summary は本質を正確に伝えているか？
6. 全体的な confidence 値は妥当か？

【重要】PMOSにとって重要な以下の概念が見落とされていないか確認:
- teleodynamics（MBT55の核心理論）
- 炭素固定・GHG削減の定量データ
- ゲイツ財団/Microsoftへの提案可能性
- 医療・農業・金融の横断的な関係性

JSONのみ出力:
{{
  "is_appropriate": true または false,
  "quality_score": 0.0〜1.0（0.85以上で承認）,
  "issues": ["問題点1", "問題点2"（問題なければ空リスト）],
  "suggested_corrections": {{
    "primary_domain": "修正案または null",
    "subcategory": "修正案または null",
    "key_entities_to_add": ["追加すべきエンティティ"],
    "summary": "改善された要約または null"
  }},
  "confidence_in_critique": 0.0〜1.0
}}
"""
        try:
            resp = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                timeout=20,
            )
            critique = json.loads(resp.choices[0].message.content)

            # 履歴に記録
            self.history.append({
                "note":         note_path,
                "original":     classification,
                "critique":     critique,
            })
            return critique

        except Exception as e:
            logger.warning(f"批評エラー ({Path(note_path).name}): {e}")
            return {
                "is_appropriate":        True,  # エラー時は承認
                "quality_score":         0.7,
                "issues":               [f"API批評エラー: {e}"],
                "suggested_corrections": {},
                "confidence_in_critique": 0.5,
            }

    # -------- 分類改善 --------

    def apply_corrections(self, classification: Dict, critique: Dict) -> Dict:
        """批評の修正案を分類結果に適用する"""
        corrections = critique.get("suggested_corrections", {})
        updated     = classification.copy()

        if corrections.get("primary_domain"):
            updated["primary_domain"] = corrections["primary_domain"]
        if corrections.get("subcategory"):
            updated["subcategory"] = corrections["subcategory"]
        if corrections.get("summary"):
            updated["summary"] = corrections["summary"]
        if corrections.get("key_entities_to_add"):
            existing = set(updated.get("key_entities", []))
            for e in corrections["key_entities_to_add"]:
                existing.add(e)
            updated["key_entities"] = list(existing)

        return updated

    # -------- レポート生成 --------

    def generate_report(self) -> Dict:
        """批評セッションのサマリーレポートを生成"""
        total     = len(self.history)
        approved  = sum(1 for h in self.history if h["critique"]["is_appropriate"])
        avg_score = (
            sum(h["critique"].get("quality_score", 0) for h in self.history) / total
            if total > 0 else 0
        )

        # よくある問題点を集計
        all_issues: List[str] = []
        for h in self.history:
            all_issues.extend(h["critique"].get("issues", []))

        report = {
            "total_critiqued": total,
            "approved_count":  approved,
            "approval_rate":   round(approved / total, 2) if total else 0,
            "avg_quality_score": round(avg_score, 3),
            "common_issues":   list(set(all_issues))[:10],
            "recommendations": [
                "分類前にwikilinksからコンテキストを拡充する",
                "MBT55ノートは必ずteleodynamicsキーワードを確認",
                "数値データ（tCO2e, %, JPY）は必ずkey_entitiesに含める",
                "ゲイツ財団・Microsoft言及ノートはtarget_scoreを優先",
            ],
        }

        output_path = DATA_DIR / "critique_report.json"
        save_json(report, output_path)
        logger.info(f"✅ 批評レポート → {output_path}")
        return report

    # -------- バッチ批評 --------

    def critique_batch(self, classifications: List[Dict]) -> List[Dict]:
        """分類リストをまとめて批評する（デモ用・単独実行）"""
        results = []
        for item in tqdm(classifications, desc="批評中", unit="note"):
            content = None  # 実ファイルの場合は自動読み込み
            critique = self.critique_classification(
                item["note"],
                item["classification"],
                content=content,
            )
            results.append({**item, "critique": critique})

        output_path = DATA_DIR / "critiqued_classifications.json"
        save_json(results, output_path)

        report = self.generate_report()
        print(f"\n📊 批評サマリー:")
        print(f"  承認率    : {report['approval_rate']*100:.1f}%")
        print(f"  平均品質  : {report['avg_quality_score']:.2f}")
        print(f"  主な問題点: {', '.join(report['common_issues'][:3])}")

        return results


# ========================================
# CLI エントリポイント
# ========================================

def main():
    print("""
╔══════════════════════════════════════╗
║    PMOS v2.0 — Critic Agent (Day4)  ║
╚══════════════════════════════════════╝
""")
    class_path = DATA_DIR / "classifications.json"
    if not class_path.exists():
        logger.error("data/classifications.json が見つかりません。先に classifier.py を実行してください。")
        sys.exit(1)

    classifications = load_json(class_path)
    critic          = CriticAgent()
    results         = critic.critique_batch(classifications)
    print(f"\n完了: {len(results)} 件を批評 → data/critiqued_classifications.json")
    print("次のステップ: python agents/orchestrator.py")


if __name__ == "__main__":
    main()
