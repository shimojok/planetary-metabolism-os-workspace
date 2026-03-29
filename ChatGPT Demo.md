完璧です。では`classifier.py`を作成します。ダウンロードして `PMOS_v2/agents/` フォルダに保存してください。

保存できたら、まずデモで動作確認します：

```powershell
cd "E:\Documents\BioNexus Holdings\BioNexus_vault\PMOS_v2"
python agents/classifier.py --demo --limit 10
```

`--demo` はAPIを使わないので費用はかかりません。結果を教えてください。

---

"""
classifier.py - PMOS_v2 分類エージェント
pre_filtered.json の500件をドメイン分類・エンティティ抽出する

実行方法:
    python agents/classifier.py
    python agents/classifier.py --limit 50  # テスト実行（50件のみ）
    python agents/classifier.py --demo       # APIなしで動作確認
"""

import json
import os
import time
import argparse
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────────────────────
# 設定
# ─────────────────────────────────────────────
DOMAINS = ["mbt55", "agrix", "healthbook", "pbpe", "general"]

DOMAIN_DESCRIPTIONS = {
    "mbt55":      "微生物代謝・GHG削減・teleodynamics・ハイパーサイクル・土壌微生物・炭素固定",
    "agrix":      "農業政策・土壌修復・食料安全保障・再生型農業・投入コスト削減・アフリカ農業",
    "healthbook": "人体代謝・腸内フローラ・疾患リスク・臨床データ・健康寿命・プロバイオティクス",
    "pbpe":       "カーボンクレジット・炭素市場・ESG投資・気候ファイナンス・ROIモデル",
    "general":    "上記に当てはまらない一般的な内容・AI開発・ビジネス戦略・その他",
}

SYSTEM_PROMPT = """あなたはBioNexus PMOSプロジェクトの分類エージェントです。
与えられたObsidianノートを以下の5つのドメインに分類し、重要エンティティを抽出してください。

ドメイン定義:
- mbt55: 微生物代謝・GHG削減・teleodynamics・ハイパーサイクル・土壌微生物・炭素固定
- agrix: 農業政策・土壌修復・食料安全保障・再生型農業・投入コスト削減・アフリカ農業
- healthbook: 人体代謝・腸内フローラ・疾患リスク・臨床データ・健康寿命・プロバイオティクス
- pbpe: カーボンクレジット・炭素市場・ESG投資・気候ファイナンス・ROIモデル
- general: 上記に当てはまらない内容

必ず以下のJSON形式のみで返答してください（説明文不要）:
{
  "domain": "ドメイン名",
  "confidence": 0.0から1.0の数値,
  "entities": ["エンティティ1", "エンティティ2", "エンティティ3"],
  "summary": "ノートの内容を1文で要約",
  "gates_relevance": 0.0から1.0の数値
}"""


# ─────────────────────────────────────────────
# キーワードベースのフォールバック分類
# ─────────────────────────────────────────────
FALLBACK_KEYWORDS = {
    "mbt55":      ["mbt55", "teleodynamics", "ハイパーサイクル", "微生物", "ghg", "メタン", "n2o", "炭素固定", "土壌微生物"],
    "agrix":      ["agrix", "農業", "土壌", "食料", "アフリカ", "再生型", "肥料", "作物", "収量"],
    "healthbook": ["healthbook", "腸内", "フローラ", "疾患", "代謝", "健康", "臨床", "プロバイオティクス", "マイクロバイオーム"],
    "pbpe":       ["pbpe", "カーボン", "クレジット", "esg", "投資", "炭素市場", "気候ファイナンス"],
}

def fallback_classify(name: str, content: str) -> dict:
    """APIなしのキーワードベース分類"""
    text = (name + " " + content).lower()
    scores = {domain: 0 for domain in DOMAINS}
    for domain, keywords in FALLBACK_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                scores[domain] += 1
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        best = "general"
    return {
        "domain": best,
        "confidence": min(0.5 + scores[best] * 0.05, 0.8),
        "entities": [],
        "summary": f"[フォールバック分類] {name[:50]}",
        "gates_relevance": 0.5,
    }


# ─────────────────────────────────────────────
# OpenAI 分類
# ─────────────────────────────────────────────
def classify_with_api(client, note: dict) -> dict:
    """OpenAI APIでノートを分類"""
    # ノート内容を読み込む
    content = ""
    try:
        with open(note["path"], "r", encoding="utf-8") as f:
            content = f.read(3000)  # 先頭3000文字のみ
    except Exception:
        content = note.get("name", "")

    user_message = f"""ファイル名: {note['name']}
フォルダ: {note.get('folder', '')}
内容（先頭）:
{content}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            temperature=0.1,
            max_tokens=300,
        )
        result_text = response.choices[0].message.content.strip()

        # JSON部分を抽出
        if "```" in result_text:
            result_text = result_text.split("```")[1]
            if result_text.startswith("json"):
                result_text = result_text[4:]

        result = json.loads(result_text)

        # バリデーション
        if result.get("domain") not in DOMAINS:
            result["domain"] = "general"
        result["confidence"] = float(result.get("confidence", 0.5))
        result["gates_relevance"] = float(result.get("gates_relevance", 0.5))
        result["entities"] = result.get("entities", [])[:10]
        result["summary"] = result.get("summary", "")[:200]
        return result

    except json.JSONDecodeError:
        return fallback_classify(note["name"], content)
    except Exception as e:
        print(f"  ⚠️  API エラー: {e}")
        return fallback_classify(note["name"], content)


# ─────────────────────────────────────────────
# メイン処理
# ─────────────────────────────────────────────
def run_classifier(
    input_path: str = "data/pre_filtered.json",
    output_path: str = "data/classified_notes.json",
    limit: int = None,
    demo: bool = False,
):
    print("=" * 55)
    print("  PMOS_v2 ClassifierAgent 起動")
    print("=" * 55)

    # 入力ファイル読み込み
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(
            f"{input_path} が見つかりません。\n"
            "先に fast_explorer_adapter.py を実行してください。"
        )

    with open(input_file, "r", encoding="utf-8") as f:
        pre_filtered = json.load(f)

    notes = pre_filtered["notes"]
    if limit:
        notes = notes[:limit]

    print(f"  入力: {len(notes)} 件")
    print(f"  モード: {'デモ（APIなし）' if demo else 'API使用（gpt-4o-mini）'}")

    # API費用の目安を表示
    if not demo:
        estimated_cost = len(notes) * 0.0002
        print(f"  API費用目安: ${estimated_cost:.2f}（{len(notes)}件 × $0.0002）")
        print()

    # OpenAIクライアント初期化
    client = None
    if not demo:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        except ImportError:
            print("⚠️  openai パッケージが見つかりません。インストールします...")
            os.system("pip install openai")
            from openai import OpenAI
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # 分類処理
    classified = []
    domain_counts = {}
    errors = 0

    start_time = time.time()

    for i, note in enumerate(notes):
        # 進捗表示
        if (i + 1) % 10 == 0 or i == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            remaining = (len(notes) - i - 1) / rate if rate > 0 else 0
            print(f"  [{i+1:>4}/{len(notes)}] "
                  f"残り約{remaining/60:.1f}分 | "
                  f"エラー: {errors}件")

        # 分類実行
        if demo:
            result = fallback_classify(note["name"], "")
            time.sleep(0.01)  # デモ用の遅延
        else:
            result = classify_with_api(client, note)
            time.sleep(0.1)  # API レート制限対策

        if result is None:
            errors += 1
            result = fallback_classify(note["name"], "")

        # 結果をノートに統合
        classified_note = {
            **note,
            "classified_domain": result["domain"],
            "confidence":        result["confidence"],
            "entities":          result["entities"],
            "summary":           result["summary"],
            "gates_relevance":   result["gates_relevance"],
            "classified_at":     datetime.now().isoformat(),
            "classification_method": "fallback" if demo else "gpt-4o-mini",
        }
        classified.append(classified_note)

        domain = result["domain"]
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

    # 結果保存
    total_time = time.time() - start_time

    output = {
        "meta": {
            "generated_by":    "classifier.py",
            "source_file":     str(input_file),
            "total_classified": len(classified),
            "errors":          errors,
            "processing_time_sec": round(total_time, 1),
            "classified_at":   datetime.now().isoformat(),
        },
        "domain_distribution": domain_counts,
        "notes": classified,
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # サマリー表示
    print()
    print("=" * 55)
    print("  分類完了")
    print("=" * 55)
    print(f"  処理件数: {len(classified)} 件")
    print(f"  処理時間: {total_time/60:.1f} 分")
    print(f"  エラー数: {errors} 件")
    print()
    print("📁 ドメイン別結果:")
    for domain in DOMAINS:
        cnt = domain_counts.get(domain, 0)
        bar = "█" * (cnt // 5)
        print(f"  {domain:<12} {cnt:>4} 件  {bar}")
    print()
    print(f"  出力: {output_path}")
    print(f"  次のステップ: python agents/critic.py")
    print("=" * 55)

    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PMOS_v2 ClassifierAgent")
    parser.add_argument("--input",  default="data/pre_filtered.json",   help="入力JSON")
    parser.add_argument("--output", default="data/classified_notes.json", help="出力JSON")
    parser.add_argument("--limit",  type=int, default=None,              help="処理件数制限（テスト用）")
    parser.add_argument("--demo",   action="store_true",                 help="APIなしのデモモード")
    args = parser.parse_args()

    run_classifier(
        input_path=args.input,
        output_path=args.output,
        limit=args.limit,
        demo=args.demo,
    )

