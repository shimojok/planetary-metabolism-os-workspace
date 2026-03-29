"""
PMOS v2.0 — Day 3-4: Classifier Agent
======================================
優先ノートをドメイン・サブカテゴリに分類し、
主要エンティティを抽出する。

特徴:
- GPT-4oでPMOS専用スキーマを自動提案
- 各ノートを構造化JSONとして分類
- エンティティ抽出（KG構築の前準備）

使用方法:
    python agents/classifier.py
"""

import sys
import json
from pathlib import Path
from typing import Dict, List
from tqdm import tqdm

import openai

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import (
    DATA_DIR, GRAPH_DIR, OPENAI_API_KEY, DOMAINS,
    save_json, load_json, load_note_content, get_logger
)

logger = get_logger("ClassifierAgent")


# ========================================
# Classifier Agent
# ========================================

class ClassifierAgent:
    """
    ノートをPMOSスキーマに従って分類する。

    処理フロー:
      1. propose_schema()  : LLMがスキーマを自動提案（初回のみ）
      2. classify_note()   : 各ノートを分類 + エンティティ抽出
    """

    # デフォルトスキーマ（API障害時のフォールバック）
    DEFAULT_SCHEMA = {
        "domains": [
            {
                "name": "MBT55",
                "subcategories": ["理論・メカニズム", "実証データ", "実装・応用", "数理モデル"],
                "keywords": ["teleodynamics", "微生物", "代謝経路", "メタン", "mbt55"]
            },
            {
                "name": "AGRIX",
                "subcategories": ["農業政策", "土壌修復", "炭素固定", "社会実装"],
                "keywords": ["agrix", "agriculture", "土壌", "carbon sequestration", "farming"]
            },
            {
                "name": "HealthBook",
                "subcategories": ["腸内フローラ", "代謝疾患", "予防医療", "臨床データ"],
                "keywords": ["healthbook", "腸内", "health", "microbiome", "疾患"]
            },
            {
                "name": "PBPE",
                "subcategories": ["カーボンクレジット", "経済モデル", "投資戦略", "市場分析"],
                "keywords": ["pbpe", "carbon credit", "finance", "gdp", "投資"]
            },
            {
                "name": "Climate",
                "subcategories": ["GHG削減", "気候変動政策", "再生エネルギー", "適応策"],
                "keywords": ["ghg", "co2", "climate", "気候", "温室効果"]
            },
        ]
    }

    def __init__(self):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
        self.schema = self._load_or_propose_schema()

    # -------- スキーマ管理 --------

    def _load_or_propose_schema(self) -> dict:
        """スキーマをキャッシュから読むか、LLMで新規提案"""
        schema_path = GRAPH_DIR / "schema.json"
        if schema_path.exists():
            logger.info(f"既存スキーマを読み込み: {schema_path}")
            return load_json(schema_path)
        return self.propose_schema()

    def propose_schema(self) -> dict:
        """
        GPT-4oがPMOSドメインの分類スキーマを自動提案する。
        graph/schema.json に保存。
        """
        logger.info("スキーマを提案中...")
        prompt = """
あなたはPlanetary Metabolic OS（PMOS）の知識アーキテクトです。
以下の5ドメインに対して最適な知識分類スキーマを設計してください。

【対象ドメイン】
- MBT55    : 微生物代謝・teleodynamics・GHG削減
- AGRIX    : 農業政策・土壌修復・炭素固定
- HealthBook: 人体代謝・腸内フローラ・予防医療
- PBPE     : カーボンクレジット市場・経済モデル
- Climate  : 気候変動政策・再生エネルギー

各ドメインについて:
- subcategories: 3〜5個の具体的な下位カテゴリ
- keywords: 分類の判断基準となる7〜10個のキーワード（日英混在OK）

JSONのみ出力（他のテキスト不要）:
{
  "domains": [
    {
      "name": "MBT55",
      "subcategories": [...],
      "keywords": [...]
    },
    ...5ドメイン分...
  ]
}
"""
        try:
            resp = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                timeout=30,
            )
            schema = json.loads(resp.choices[0].message.content)
            save_json(schema, GRAPH_DIR / "schema.json")
            logger.info(f"✅ スキーマ提案完了 → graph/schema.json")
            return schema
        except Exception as e:
            logger.warning(f"スキーマ提案失敗: {e} → デフォルトスキーマを使用")
            save_json(self.DEFAULT_SCHEMA, GRAPH_DIR / "schema.json")
            return self.DEFAULT_SCHEMA

    # -------- ノート分類 --------

    def classify_note(self, note_path: str, content: str | None = None) -> Dict:
        """
        1つのノートを分類し、エンティティを抽出する。

        Returns:
            {
              "primary_domain": str,
              "subcategory": str,
              "confidence": float,
              "key_entities": List[str],
              "relations": List[{"from": str, "to": str, "type": str}],
              "summary": str,
              "tags": List[str]
            }
        """
        if content is None:
            content = load_note_content(note_path, max_chars=3000)

        schema_str = json.dumps(self.schema, ensure_ascii=False, indent=2)

        prompt = f"""
あなたはPMOS知識グラフの分類エンジンです。
以下のノートを与えられたスキーマに従って分類し、エンティティと関係を抽出してください。

【PMOSスキーマ】
{schema_str}

【ノート内容】
{content}

【抽出指示】
- key_entities  : 固有名詞・概念・物質名・手法名を最大10個
- relations     : エンティティ間の意味的関係（例: MBT55 -[削減]-> CH4）
- summary       : 100文字以内の要約（日本語）
- tags          : 検索に役立つキーワードタグを最大5個

JSONのみ出力:
{{
  "primary_domain": "MBT55/AGRIX/HealthBook/PBPE/Climate/Other のいずれか",
  "subcategory": "上記スキーマの下位カテゴリ",
  "confidence": 0.0〜1.0の数値,
  "key_entities": ["エンティティ1", "エンティティ2", ...],
  "relations": [
    {{"from": "エンティティA", "to": "エンティティB", "type": "関係タイプ"}}
  ],
  "summary": "100文字以内の要約",
  "tags": ["タグ1", "タグ2", ...]
}}
"""
        try:
            resp = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                timeout=20,
            )
            return json.loads(resp.choices[0].message.content)
        except Exception as e:
            logger.warning(f"分類エラー ({Path(note_path).name}): {e}")
            from config import quick_classify
            domain = quick_classify(content)
            return {
                "primary_domain": domain,
                "subcategory":    "未分類",
                "confidence":     0.3,
                "key_entities":   [],
                "relations":      [],
                "summary":        content[:80],
                "tags":           [domain.lower()],
            }

    # -------- バッチ分類 --------

    def classify_batch(self, notes: List[Dict]) -> List[Dict]:
        """
        優先ノートリストをまとめて分類する。

        Args:
            notes: explorer.pyが出力した priority_notes.json の内容
        Returns:
            分類結果のリスト → data/classifications.json に保存
        """
        results = []
        for note in tqdm(notes, desc="分類中", unit="note"):
            content = note.get("_demo_content")  # デモ用
            result  = self.classify_note(note["path"], content=content)
            results.append({
                "note":           note["path"],
                "filename":       note["filename"],
                "domain_hint":    note.get("domain_hint", "?"),
                "total_score":    note.get("total_score", 0),
                "classification": result,
            })

        output_path = DATA_DIR / "classifications.json"
        save_json(results, output_path)
        logger.info(f"✅ 分類完了: {len(results)} ノート → {output_path}")
        self._print_domain_summary(results)
        return results

    def _print_domain_summary(self, results: List[Dict]):
        """ドメイン分布サマリーを表示"""
        from collections import Counter
        domains = Counter(r["classification"]["primary_domain"] for r in results)
        print("\n📊 ドメイン分布:")
        for domain, count in domains.most_common():
            bar = "█" * count
            print(f"  {domain:<14}: {bar} ({count})")


# ========================================
# CLI エントリポイント
# ========================================

def main():
    print("""
╔══════════════════════════════════════╗
║  PMOS v2.0 — Classifier Agent (Day3)║
╚══════════════════════════════════════╝
""")
    priority_path = DATA_DIR / "priority_notes.json"
    if not priority_path.exists():
        logger.error("data/priority_notes.json が見つかりません。先に explorer.py を実行してください。")
        sys.exit(1)

    notes      = load_json(priority_path)
    classifier = ClassifierAgent()
    results    = classifier.classify_batch(notes)
    print(f"\n完了: {len(results)} ノートを分類 → data/classifications.json")
    print("次のステップ: python agents/critic.py")


if __name__ == "__main__":
    main()
