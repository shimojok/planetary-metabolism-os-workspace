"""
fast_explorer_adapter.py
PMOS_12day の explorer_fast.py 出力を PMOS_v2 形式に変換するアダプター

使い方:
    # Step1: explorer_fast.py を実行して data/core_500.json を生成
    # Step2: このアダプターを実行して data/pre_filtered.json を生成
    # Step3: PMOS_v2 の orchestrator.py が pre_filtered.json を読み込む

    python fast_explorer_adapter.py
    python fast_explorer_adapter.py --limit 300  # 絞り込み件数を変更
"""

from pathlib import Path
import json
import argparse
from datetime import datetime


# ─────────────────────────────────────────────
# フォルダ → ドメイン マッピング（PMOS_v2準拠）
# ─────────────────────────────────────────────
FOLDER_TO_DOMAIN = {
    "03_MBT55":                    "mbt55",
    "04_AGRIX":                    "agrix",
    "07_HealthBook":               "healthbook",
    "06_PBPE":                     "pbpe",
    "05_AgriWare":                 "agrix",        # AgriWareはAGRIX配下とみなす
    "08_MBT_KampoLibrary":         "mbt55",
    "09_MBT漢方代謝ライブラリー":    "mbt55",
    "10_MBT_Probiotics":           "mbt55",
    "01_Planetary_Problems":       "general",
    "02_Biological_Systems":       "general",
    "11_AI_Development":           "general",
    "21_NotebookLM":               "general",
    "22_Claude":                   "general",
    "00_inbox":                    "general",
}

# スコア閾値 → 優先度マッピング
def score_to_priority(score: int) -> str:
    # スコア範囲 40-82 に合わせた閾値
    if score >= 70:
        return "critical"
    elif score >= 55:
        return "high"
    elif score >= 45:
        return "medium"
    else:
        return "low"


def convert(input_path: str = "data/core_500.json",
            output_path: str = "data/pre_filtered.json",
            limit: int = 500) -> dict:
    """
    core_500.json → pre_filtered.json（PMOS_v2 Orchestrator 入力フォーマット）
    """
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(
            f"{input_path} が見つかりません。\n"
            "先に explorer_fast.py を実行してください:\n"
            "  python PMOS_12day/explorer_fast.py"
        )

    with open(input_file, "r", encoding="utf-8") as f:
        raw = json.load(f)

    core_notes = raw.get("core_notes", [])[:limit]

    # ── 変換 ──────────────────────────────────
    converted = []
    domain_counts = {}

    for note in core_notes:
        folder = note.get("folder", "")
        domain = FOLDER_TO_DOMAIN.get(folder, "general")
        priority = score_to_priority(note["score"])

        # PMOS_v2 の approved_notes.json と互換のスキーマ
        converted.append({
            "path":       note["path"],
            "name":       note["name"],
            "score":      note["score"],
            "size":       note["size"],
            "domain":     domain,
            "priority":   priority,
            "folder":     folder,
            # ClassifierAgent が上書きするフィールド（初期値）
            "entities":   [],
            "quality_score": None,   # Critic未評価を明示
            "source":     "fast_explorer_prefilter",
            "filtered_at": datetime.now().isoformat(),
        })

        domain_counts[domain] = domain_counts.get(domain, 0) + 1

    # ── 統計 ──────────────────────────────────
    priority_counts = {}
    for n in converted:
        p = n["priority"]
        priority_counts[p] = priority_counts.get(p, 0) + 1

    result = {
        "meta": {
            "generated_by":    "fast_explorer_adapter.py",
            "source_file":     str(input_file),
            "total_input":     len(raw.get("core_notes", [])),
            "total_converted": len(converted),
            "limit_applied":   limit,
            "original_score_range": raw.get("score_range", {}),
            "converted_at":    datetime.now().isoformat(),
        },
        "domain_distribution":    domain_counts,
        "priority_distribution":  priority_counts,
        "notes": converted,
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # ── サマリー表示 ──────────────────────────
    print("=" * 55)
    print("  fast_explorer_adapter 変換完了")
    print("=" * 55)
    print(f"  入力: {input_path}  ({len(raw.get('core_notes', []))} 件)")
    print(f"  出力: {output_path}  ({len(converted)} 件)\n")

    print("📁 ドメイン別:")
    for domain, cnt in sorted(domain_counts.items(), key=lambda x: -x[1]):
        bar = "█" * (cnt // 3)
        print(f"  {domain:<12} {cnt:>4} 件  {bar}")

    print("\n⚡ 優先度別:")
    for level in ["critical", "high", "medium", "low"]:
        cnt = priority_counts.get(level, 0)
        bar = "█" * (cnt // 5)
        print(f"  {level:<10} {cnt:>4} 件  {bar}")

    print(f"\n✅ PMOS_v2 Orchestrator への引き渡し準備完了")
    print(f"   次のステップ: python PMOS_v2/agents/orchestrator.py --prefiltered data/pre_filtered.json")
    print("=" * 55)

    return result


# ─────────────────────────────────────────────
# orchestrator.py 側の読み込みヘルパー（コピペ用）
# ─────────────────────────────────────────────
ORCHESTRATOR_SNIPPET = '''
# ── orchestrator.py に追加するコード ──────────────────
# （argparse に以下を追加）
parser.add_argument("--prefiltered", type=str, default=None,
                    help="fast_explorer_adapter の出力 JSON を使って起動")

# （load_notes() の先頭に追加）
if args.prefiltered:
    with open(args.prefiltered, "r", encoding="utf-8") as f:
        pre = json.load(f)
    notes_to_process = [Path(n["path"]) for n in pre["notes"]]
    print(f"[Prefiltered] {len(notes_to_process)} 件を前段フィルター済みリストから読み込み")
else:
    notes_to_process = list(vault_path.rglob("*.md"))  # 既存ロジック
# ──────────────────────────────────────────────────────
'''


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PMOS_12day → PMOS_v2 アダプター")
    parser.add_argument("--input",  default="data/core_500.json",   help="explorer_fast.py の出力 JSON")
    parser.add_argument("--output", default="data/pre_filtered.json", help="変換後の出力先")
    parser.add_argument("--limit",  type=int, default=500,           help="変換する最大件数")
    parser.add_argument("--snippet", action="store_true",            help="orchestrator.py 組み込みコードを表示")
    args = parser.parse_args()

    if args.snippet:
        print(ORCHESTRATOR_SNIPPET)
    else:
        convert(args.input, args.output, args.limit)