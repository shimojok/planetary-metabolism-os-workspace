"""
critic.py - PMOS_v2 批評エージェント（Gemini対応版）
classified_notes.json の分類結果を品質検証する

実行方法:
    python agents/critic.py              # Gemini API使用
    python agents/critic.py --demo       # APIなしで動作確認
    python agents/critic.py --threshold 0.7  # 閾値を変更
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
DEFAULT_THRESHOLD = 0.75  # quality_score の承認閾値

CRITIC_PROMPT = """あなたはBioNexus PMOSプロジェクトの品質検証エージェントです。
以下のノートの分類結果を検証してください。

ドメイン定義:
- mbt55: 微生物代謝・GHG削減・teleodynamics・ハイパーサイクル・土壌微生物・炭素固定
- agrix: 農業政策・土壌修復・食料安全保障・再生型農業・投入コスト削減・アフリカ農業
- healthbook: 人体代謝・腸内フローラ・疾患リスク・臨床データ・健康寿命・プロバイオティクス
- pbpe: カーボンクレジット・炭素市場・ESG投資・気候ファイナンス・ROIモデル
- general: 上記に当てはまらない内容

以下のJSON形式のみで返答してください（説明文不要）:
{"quality_score": 0.0から1.0, "domain_correct": true or false, "corrected_domain": "修正後ドメイン名またはnull", "reason": "判定理由を1文で"}"""


# ─────────────────────────────────────────────
# Gemini クライアント
# ─────────────────────────────────────────────
def get_gemini_client():
    try:
        from google import genai
    except ImportError:
        os.system("pip install google-genai")
        from google import genai
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return client


# ─────────────────────────────────────────────
# フォールバック品質スコア計算
# ─────────────────────────────────────────────
def fallback_quality_score(note: dict) -> dict:
    """APIなしの品質スコア計算"""
    score = 0.5  # ベーススコア

    # confidence が高ければスコアを上げる
    confidence = note.get("confidence", 0.5)
    score += confidence * 0.3

    # フォルダとドメインが一致していればスコアを上げる
    folder = note.get("folder", "").lower()
    domain = note.get("classified_domain", "general")

    folder_domain_map = {
        "03_mbt55": "mbt55",
        "04_agrix": "agrix",
        "07_healthbook": "healthbook",
        "06_pbpe": "pbpe",
        "05_agriware": "agrix",
        "08_mbt_kampolibrary": "mbt55",
        "09_mbt_漢方代謝ライブラリー": "mbt55",
        "10_mbt_probiotics": "mbt55",
    }

    expected_domain = folder_domain_map.get(folder.lower())
    if expected_domain and expected_domain == domain:
        score += 0.2
    elif expected_domain and expected_domain != domain:
        score -= 0.1

    # スコアを0-1に収める
    score = max(0.0, min(1.0, score))

    return {
        "quality_score": round(score, 2),
        "domain_correct": True,
        "corrected_domain": None,
        "reason": "フォールバック評価（キーワード・フォルダ整合性）",
    }


# ─────────────────────────────────────────────
# Gemini 品質検証
# ─────────────────────────────────────────────
def critique_with_gemini(client, note: dict) -> dict:
    content = ""
    try:
        with open(note["path"], "r", encoding="utf-8") as f:
            content = f.read(2000)
    except Exception:
        content = note.get("name", "")

    prompt = f"""{CRITIC_PROMPT}

ファイル名: {note['name']}
フォルダ: {note.get('folder', '')}
分類されたドメイン: {note.get('classified_domain', 'unknown')}
分類時の確信度: {note.get('confidence', 0)}
要約: {note.get('summary', '')}
内容（先頭）:
{content}"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        result_text = response.text.strip()

        # JSON抽出
        if "```" in result_text:
            parts = result_text.split("```")
            for part in parts:
                if "{" in part:
                    result_text = part.strip()
                    if result_text.startswith("json"):
                        result_text = result_text[4:].strip()
                    break

        start = result_text.find("{")
        end = result_text.rfind("}") + 1
        if start >= 0 and end > start:
            result_text = result_text[start:end]

        result = json.loads(result_text)

        # バリデーション
        result["quality_score"] = float(result.get("quality_score", 0.5))
        result["domain_correct"] = bool(result.get("domain_correct", True))
        corrected = result.get("corrected_domain")
        if corrected not in DOMAINS:
            corrected = None
        result["corrected_domain"] = corrected
        result["reason"] = result.get("reason", "")[:200]
        return result

    except json.JSONDecodeError:
        return fallback_quality_score(note)
    except Exception as e:
        print(f"  ⚠️  Gemini エラー（フォールバック使用）")
        return fallback_quality_score(note)


# ─────────────────────────────────────────────
# メイン処理
# ─────────────────────────────────────────────
def run_critic(
    input_path: str = "data/classified_notes.json",
    output_path: str = "data/approved_notes.json",
    threshold: float = DEFAULT_THRESHOLD,
    demo: bool = False,
):
    print("=" * 55)
    print("  PMOS_v2 CriticAgent 起動（Gemini版）")
    print("=" * 55)

    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"{input_path} が見つかりません。")

    with open(input_file, "r", encoding="utf-8") as f:
        classified = json.load(f)

    notes = classified["notes"]
    print(f"  入力: {len(notes)} 件")
    print(f"  承認閾値: quality_score >= {threshold}")
    print(f"  モード: {'デモ（APIなし）' if demo else 'Gemini API'}")
    print()

    # Geminiクライアント
    client = None
    if not demo:
        client = get_gemini_client()
        print("  ✅ Gemini接続OK")
        print()

    # 品質検証
    approved = []
    rejected = []
    corrected_count = 0
    start_time = time.time()

    for i, note in enumerate(notes):
        if (i + 1) % 50 == 0 or i == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            remaining = (len(notes) - i - 1) / rate if rate > 0 else 0
            print(f"  [{i+1:>4}/{len(notes)}] "
                  f"承認: {len(approved)} | "
                  f"却下: {len(rejected)} | "
                  f"残り約{remaining/60:.1f}分")

        if demo:
            result = fallback_quality_score(note)
            time.sleep(0.01)
        else:
            result = critique_with_gemini(client, note)
            time.sleep(1.1)

        # ドメイン修正
        final_domain = note.get("classified_domain")
        if result.get("corrected_domain"):
            final_domain = result["corrected_domain"]
            corrected_count += 1

        reviewed_note = {
            **note,
            "quality_score":    result["quality_score"],
            "domain_correct":   result["domain_correct"],
            "final_domain":     final_domain,
            "critic_reason":    result["reason"],
            "reviewed_at":      datetime.now().isoformat(),
        }

        if result["quality_score"] >= threshold:
            approved.append(reviewed_note)
        else:
            rejected.append(reviewed_note)

    total_time = time.time() - start_time

    # 承認済みノートを保存
    output = {
        "meta": {
            "generated_by":     "critic.py",
            "source_file":      str(input_file),
            "total_input":      len(notes),
            "total_approved":   len(approved),
            "total_rejected":   len(rejected),
            "corrected_domain": corrected_count,
            "threshold":        threshold,
            "processing_time_sec": round(total_time, 1),
            "reviewed_at":      datetime.now().isoformat(),
        },
        "domain_distribution": {},
        "notes": approved,
    }

    # ドメイン別集計
    for note in approved:
        d = note.get("final_domain", "general")
        output["domain_distribution"][d] = output["domain_distribution"].get(d, 0) + 1

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # 却下ノートも保存
    rejected_path = output_path.replace(".json", "_rejected.json")
    with open(rejected_path, "w", encoding="utf-8") as f:
        json.dump({"notes": rejected}, f, indent=2, ensure_ascii=False)

    # サマリー
    approval_rate = len(approved) / len(notes) * 100 if notes else 0

    print()
    print("=" * 55)
    print("  品質検証完了")
    print("=" * 55)
    print(f"  入力:   {len(notes):>4} 件")
    print(f"  承認:   {len(approved):>4} 件 ({approval_rate:.1f}%)")
    print(f"  却下:   {len(rejected):>4} 件")
    print(f"  修正:   {corrected_count:>4} 件（ドメイン修正）")
    print(f"  時間:   {total_time/60:.1f} 分")
    print()
    print("📁 承認済みドメイン別:")
    for domain in DOMAINS:
        cnt = output["domain_distribution"].get(domain, 0)
        bar = "█" * (cnt // 5)
        print(f"  {domain:<12} {cnt:>4} 件  {bar}")
    print()
    print(f"  承認済み出力: {output_path}")
    print(f"  却下ノート:   {rejected_path}")
    print(f"  次のステップ: Week2 Neo4j Knowledge Graph構築")
    print("=" * 55)

    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PMOS_v2 CriticAgent")
    parser.add_argument("--input",     default="data/classified_notes.json", help="入力JSON")
    parser.add_argument("--output",    default="data/approved_notes.json",   help="出力JSON")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD, help="承認閾値（デフォルト0.75）")
    parser.add_argument("--demo",      action="store_true",                   help="APIなしのデモモード")
    args = parser.parse_args()

    run_critic(
        input_path=args.input,
        output_path=args.output,
        threshold=args.threshold,
        demo=args.demo,
    )
