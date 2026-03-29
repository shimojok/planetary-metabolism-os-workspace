"""
PMOS v2.0 — Day 1-2: Explorer Agent
====================================
Obsidian Vaultをスキャンし、最も重要なノートを選別する。

特徴:
- 中断しても再開できるチェックポイント機能
- tqdmによるリアルタイム進捗表示
- スコア分布の可視化
- リンク数の解析（Obsidianのwikilink [[...]] を検出）

使用方法:
    python agents/explorer.py --vault /path/to/vault --limit 100
"""

import sys
import re
import json
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict

import openai
from tqdm import tqdm

# 親ディレクトリをパスに追加してconfig.pyをインポート
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import (
    VAULT_PATH, DATA_DIR, OPENAI_API_KEY,
    PRIORITY_NOTE_LIMIT, save_json, load_json,
    load_note_content, quick_classify, get_logger
)

logger = get_logger("ExplorerAgent")

# ========================================
# Explorer Agent
# ========================================

class ExplorerAgent:
    """
    Vault内のノートをスキャンして重要度を評価する。

    評価基準（各10点、合計40点）:
      1. scientific_score  : 科学的メカニズムの深さ
      2. data_score        : 実証データ・数値の含有
      3. target_score      : ゲイツ財団/Microsoftとの関連性
      4. core_score        : MBT55/AGRIX/HealthBook/PBPE中核度
    """

    def __init__(self, vault_path: str | Path = VAULT_PATH):
        self.vault_path = Path(vault_path)
        self.client     = openai.OpenAI(api_key=OPENAI_API_KEY)
        self._cache_path = DATA_DIR / "explorer_cache.json"
        self._cache: Dict[str, dict] = self._load_cache()

        if not self.vault_path.exists():
            logger.warning(f"Vault not found: {self.vault_path}")
            logger.warning("demo モードで実行します（サンプルデータを使用）")

    # -------- キャッシュ --------

    def _load_cache(self) -> dict:
        if self._cache_path.exists():
            return load_json(self._cache_path)
        return {}

    def _save_cache(self):
        save_json(self._cache, self._cache_path)

    def _get_file_hash(self, path: Path) -> str:
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    # -------- Vault スキャン --------

    def scan_vault(self) -> List[Dict]:
        """Vault内の全.mdファイルをスキャンしてメタデータを取得"""
        notes = []

        if not self.vault_path.exists():
            # デモ用サンプルデータ
            logger.info("デモモード: サンプルノートを生成")
            return self._generate_demo_notes()

        all_md = list(self.vault_path.rglob("*.md"))
        logger.info(f"スキャン開始: {len(all_md)} ファイル発見")

        for md in all_md:
            try:
                stat    = md.stat()
                content = md.read_text(encoding="utf-8", errors="replace")

                # wikilinks [[...]] を検出してリンク数を計算
                links = re.findall(r"\[\[([^\]]+)\]\]", content)

                notes.append({
                    "path":      str(md),
                    "filename":  md.name,
                    "stem":      md.stem,
                    "modified":  datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "size_chars": len(content),
                    "link_count": len(links),
                    "hash":      self._get_file_hash(md),
                    "domain_hint": quick_classify(content),  # キーワードベース高速分類
                })
            except Exception as e:
                logger.debug(f"スキップ {md.name}: {e}")

        return notes

    def _generate_demo_notes(self) -> List[Dict]:
        """デモ用サンプルノート（Vaultなしで動作確認可能）"""
        samples = [
            ("MBT55_mechanism.md",   "MBT55", 8,  "# MBT55メカニズム\nteleodynamicsを用いた微生物代謝の説明。CH4削減率5.8tCO2e/ha/year達成。"),
            ("AGRIX_policy.md",       "AGRIX", 5,  "# AGRIX農業政策\n土壌修復における政策フレームワークと実証データ。農業投入コスト70%削減。"),
            ("HealthBook_gut.md",     "HealthBook", 6, "# 腸内フローラとMBT55\nMBT55投与後の腸内microbiome変化。137疾患リスクマトリクス。"),
            ("PBPE_carbon_market.md", "PBPE", 4, "# カーボンクレジット市場\nPBPEモデルによる炭素市場予測。経済インパクト試算。"),
            ("Gates_Foundation.md",   "Other", 7, "# ゲイツ財団との連携\nBill & Melinda Gates Foundation提案書ドラフト。"),
            ("Climate_GHG.md",        "Climate", 6, "# GHG削減目標\n2030年ネットゼロに向けたMBT55/AGRIX統合戦略。"),
        ]
        notes = []
        for i, (name, domain, links, content) in enumerate(samples):
            notes.append({
                "path":       f"demo/{name}",
                "filename":   name,
                "stem":       name.replace(".md", ""),
                "modified":   "2024-01-01T00:00:00",
                "size_chars": len(content),
                "link_count": links,
                "hash":       f"demo_{i:04d}",
                "domain_hint": domain,
                "_demo_content": content,  # デモ用
            })
        return notes

    # -------- 重要度評価 --------

    def assess_importance(self, note: Dict) -> Dict:
        """
        LLMでノートの重要度を評価する。
        キャッシュ済みの場合はスキップ。
        """
        cache_key = note["hash"]

        # キャッシュヒット → スキップ
        if cache_key in self._cache:
            return self._cache[cache_key]

        # コンテンツ取得（デモ or 実ファイル）
        content = note.get("_demo_content") or load_note_content(note["path"], max_chars=2000)

        prompt = f"""
あなたはPMOS（Planetary Metabolic OS）プロジェクトの知識キュレーターです。
以下のObsidianノートの重要度を評価してください。

【評価基準】（各0〜10点）
- scientific_score : 科学的メカニズムの深さ・独自性（実験結果・数式・引用文献があれば高得点）
- data_score       : 実証データ・数値の含有度（具体的な数値があれば高得点）
- target_score     : ゲイツ財団/Microsoftとの関連性（提案・シナジーへの言及で高得点）
- core_score       : MBT55/AGRIX/HealthBook/PBPEの中核知識か（核心技術の説明で高得点）

【追加メタデータ】
- リンク数: {note['link_count']} （Obsidian wikilinks）
- サイズ:   {note['size_chars']} 文字
- ドメインヒント: {note['domain_hint']}

【ノート内容（最大2000文字）】
{content}

JSONで出力してください（他のテキスト不要）:
{{
  "scientific_score": 整数0-10,
  "data_score": 整数0-10,
  "target_score": 整数0-10,
  "core_score": 整数0-10,
  "total_score": 整数0-40,
  "reasoning": "50文字以内の評価理由"
}}
"""
        try:
            resp = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                timeout=15,
            )
            result = json.loads(resp.choices[0].message.content)

            # キャッシュ保存
            self._cache[cache_key] = result
            return result

        except Exception as e:
            logger.warning(f"評価エラー ({note['filename']}): {e}")
            # フォールバック：キーワードスコア
            base = note["link_count"]
            return {
                "scientific_score": min(base, 10),
                "data_score":       min(base, 10),
                "target_score":     min(base // 2, 10),
                "core_score":       min(base, 10),
                "total_score":      min(base * 3, 40),
                "reasoning":        "API評価失敗 - キーワードスコア使用",
            }

    # -------- メイン処理 --------

    def find_priority_notes(self, limit: int = PRIORITY_NOTE_LIMIT) -> List[Dict]:
        """
        Vaultをスキャンして重要ノートを優先順位付け。

        Returns:
            スコア降順にソートされた上位 `limit` 件のノート情報
        """
        # 1. スキャン
        all_notes = self.scan_vault()
        logger.info(f"総ノート数: {len(all_notes)}")

        # 2. 評価対象の絞り込み（サイズ小さすぎるものを除外）
        candidates = [n for n in all_notes if n["size_chars"] > 200]
        eval_limit = min(len(candidates), limit * 3)  # 3倍候補から絞る
        logger.info(f"評価対象: {eval_limit} ノート")

        # 3. 重要度評価（tqdm進捗バー）
        evaluated = []
        for note in tqdm(candidates[:eval_limit], desc="重要度評価", unit="note"):
            importance = self.assess_importance(note)
            merged     = {**note, **importance}
            evaluated.append(merged)

        # キャッシュ保存
        self._save_cache()

        # 4. スコア順ソート
        evaluated.sort(key=lambda x: (x.get("total_score", 0), x.get("link_count", 0)), reverse=True)

        # 5. 上位limitを保存
        priority = evaluated[:limit]
        output_path = DATA_DIR / "priority_notes.json"
        save_json(priority, output_path)

        logger.info(f"✅ 優先ノート {len(priority)} 件 → {output_path}")
        self._print_top_summary(priority)
        return priority

    def _print_top_summary(self, notes: List[Dict], top_n: int = 10):
        """上位ノートのサマリーを表示"""
        print("\n" + "="*60)
        print(f"{'Rank':<5} {'Score':>6} {'Domain':<12} {'Filename'}")
        print("-"*60)
        for i, n in enumerate(notes[:top_n], 1):
            print(f"{i:<5} {n.get('total_score',0):>5.0f}  {n.get('domain_hint','?'):<12} {n['filename'][:40]}")
        print("="*60)


# ========================================
# CLI エントリポイント
# ========================================

def main():
    parser = argparse.ArgumentParser(description="PMOS Explorer Agent")
    parser.add_argument("--vault", type=str, default=str(VAULT_PATH), help="Obsidian Vault パス")
    parser.add_argument("--limit", type=int, default=PRIORITY_NOTE_LIMIT, help="優先ノート取得数")
    args = parser.parse_args()

    print(f"""
╔══════════════════════════════════════╗
║   PMOS v2.0 — Explorer Agent (Day1) ║
╚══════════════════════════════════════╝
Vault: {args.vault}
Limit: {args.limit}
""")

    explorer  = ExplorerAgent(args.vault)
    priority  = explorer.find_priority_notes(args.limit)
    print(f"\n完了: {len(priority)} ノートを選別 → data/priority_notes.json")
    print("次のステップ: python agents/classifier.py")


if __name__ == "__main__":
    main()
