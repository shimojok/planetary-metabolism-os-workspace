"""
PMOS v2.0 — Day 6-7: Orchestrator
====================================
Explorer → Classifier → Critic の批評ループを統括する。
最大3回の反復で品質基準（quality_score >= 0.85）を満たすまで再分類。

使用方法:
    # デモ（Vault不要）
    python agents/orchestrator.py --demo

    # 本番（Vault指定）
    python agents/orchestrator.py --vault /path/to/vault --batch-size 10
"""

import sys
import json
import time
import argparse
from pathlib import Path
from typing import Dict, List
from datetime import datetime

import openai
from tqdm import tqdm
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import (
    VAULT_PATH, DATA_DIR, OPENAI_API_KEY,
    BATCH_SIZE, MAX_CRITIQUE_ITERATIONS, PRIORITY_NOTE_LIMIT,
    save_json, load_json, load_note_content, get_logger, CheckpointManager
)
from agents.explorer   import ExplorerAgent
from agents.classifier import ClassifierAgent
from agents.critic     import CriticAgent

logger  = get_logger("Orchestrator")
console = Console()

# 承認の品質閾値
APPROVAL_THRESHOLD = 0.85


# ========================================
# Orchestrator
# ========================================

class Orchestrator:
    """
    全エージェントを統括して批評ループを管理する。

    フロー:
      1. ExplorerAgent → 優先ノート選定
      2. ClassifierAgent → 分類 + エンティティ抽出
      3. CriticAgent → 品質評価
         - quality_score >= 0.85 → 承認
         - 未達 → 修正反映して 2 へ戻る（最大 MAX_CRITIQUE_ITERATIONS 回）
      4. 承認済みノートを data/approved_notes.json に保存
    """

    def __init__(self, vault_path: str | Path = VAULT_PATH):
        self.vault_path  = Path(vault_path)
        self.client      = openai.OpenAI(api_key=OPENAI_API_KEY)
        self.explorer    = ExplorerAgent(vault_path)
        self.classifier  = ClassifierAgent()
        self.critic      = CriticAgent()
        self.checkpoint  = CheckpointManager()
        self.approved:   List[Dict] = []
        self.start_time  = time.time()

    # -------- 1ノードの批評ループ --------

    def process_single_note(self, note: Dict) -> Dict | None:
        """
        1ノートを最大MAX_CRITIQUE_ITERATIONS回の批評ループで処理する。

        Returns:
            承認された場合: 承認済みデータ dict
            未承認の場合:   None
        """
        note_path = note["path"]
        content   = note.get("_demo_content") or load_note_content(note_path, max_chars=3000)

        # 既に処理済みなら skiop
        if self.checkpoint.is_processed(note_path):
            logger.debug(f"スキップ（処理済み）: {note['filename']}")
            return None

        classification = None
        last_critique  = None

        for iteration in range(1, MAX_CRITIQUE_ITERATIONS + 1):

            # ---- 分類（初回 or 批評を反映した再分類）----
            if iteration == 1 or classification is None:
                classification = self.classifier.classify_note(note_path, content=content)
            else:
                # 批評の修正案を適用して再分類
                classification = self._reclassify_with_critique(
                    note_path, content, classification, last_critique
                )

            # ---- 批評 ----
            critique = self.critic.critique_classification(note_path, classification, content=content)

            quality_score = critique.get("quality_score", 0)
            is_approved   = critique.get("is_appropriate", False) and quality_score >= APPROVAL_THRESHOLD

            logger.debug(
                f"[{note['filename'][:30]}] "
                f"反復{iteration}/{MAX_CRITIQUE_ITERATIONS} "
                f"スコア={quality_score:.2f} "
                f"{'✅承認' if is_approved else '🔄再試行'}"
            )

            if is_approved:
                result = {
                    "note":           note_path,
                    "filename":       note["filename"],
                    "classification": classification,
                    "critique":       critique,
                    "iterations":     iteration,
                    "quality_score":  quality_score,
                    "approved_at":    datetime.now().isoformat(),
                }
                self.checkpoint.mark_approved(result)
                self.checkpoint.mark_processed(note_path)
                return result

            last_critique = critique

        # 最大反復達しても未承認 → 最後の結果で仮承認（データ損失防止）
        logger.warning(f"最大反復到達: {note['filename']} → 条件付き承認")
        result = {
            "note":           note_path,
            "filename":       note["filename"],
            "classification": classification,
            "critique":       last_critique,
            "iterations":     MAX_CRITIQUE_ITERATIONS,
            "quality_score":  quality_score,
            "approved_at":    datetime.now().isoformat(),
            "conditional":    True,  # 条件付き承認フラグ
        }
        self.checkpoint.mark_approved(result)
        self.checkpoint.mark_processed(note_path)
        return result

    def _reclassify_with_critique(
        self,
        note_path: str,
        content:   str,
        prev_classification: Dict,
        critique: Dict,
    ) -> Dict:
        """批評を踏まえてLLMで再分類する"""

        # まず修正案を自動適用
        updated = self.critic.apply_corrections(prev_classification, critique)

        # それでも問題があれば LLM に再分類させる
        issues = critique.get("issues", [])
        if not issues:
            return updated

        prompt = f"""
あなたはPMOS知識グラフの分類エンジンです。
前回の分類に以下の問題が指摘されました。批評を参考に改善された分類を返してください。

【ノート内容（最大2000文字）】
{content[:2000]}

【前回の分類】
{json.dumps(prev_classification, ensure_ascii=False, indent=2)}

【批評・指摘された問題点】
{json.dumps(issues, ensure_ascii=False, indent=2)}

【修正提案】
{json.dumps(critique.get('suggested_corrections', {}), ensure_ascii=False, indent=2)}

問題点を解決した改善版の分類JSONのみ出力してください（構造は前回と同じ形式）:
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
            logger.warning(f"再分類エラー: {e} → 修正案を手動適用")
            return updated

    # -------- バッチ処理 --------

    def process_batch(self, notes: List[Dict]) -> List[Dict]:
        """ノートリストをバッチ処理する"""
        batch_approved = []
        for note in tqdm(notes, desc=f"バッチ処理", unit="note"):
            result = self.process_single_note(note)
            if result:
                self.approved.append(result)
                batch_approved.append(result)
        return batch_approved

    # -------- メイン実行 --------

    def run(
        self,
        note_limit:    int = PRIORITY_NOTE_LIMIT,
        batch_size:    int = BATCH_SIZE,
        demo_mode:     bool = False,
    ):
        """
        Week 1 の全処理を実行する。

        Args:
            note_limit : 処理するノートの最大数
            batch_size : 1バッチあたりのノート数（チェックポイント間隔）
            demo_mode  : True の場合、Vault不要でデモデータを使用
        """
        console.print(Panel.fit(
            f"[bold]PMOS v2.0 — Orchestrator[/bold]\n"
            f"Vault: {self.vault_path}\n"
            f"Limit: {note_limit} | Batch: {batch_size} | "
            f"Max Iterations: {MAX_CRITIQUE_ITERATIONS}",
            border_style="blue"
        ))

        # Step 1: Explorer
        console.print("\n[bold cyan]▶ Step 1: Vault スキャン & 優先度評価[/bold cyan]")
        priority_notes = self.explorer.find_priority_notes(note_limit)
        total = len(priority_notes)

        # Step 2 & 3: Classify → Critique ループ（バッチ単位）
        console.print(f"\n[bold cyan]▶ Step 2-3: 分類 → 批評ループ ({total} ノート)[/bold cyan]")

        for batch_idx, start in enumerate(range(0, total, batch_size)):
            batch = priority_notes[start : start + batch_size]
            console.print(f"\n  バッチ {batch_idx+1}/{(total-1)//batch_size+1} "
                          f"({start+1}〜{min(start+batch_size, total)} / {total})")
            self.process_batch(batch)
            self._print_progress()

        # Step 4: 結果保存
        output_path = DATA_DIR / "approved_notes.json"
        save_json(self.approved, output_path)

        # 最終レポート
        elapsed    = time.time() - self.start_time
        stats      = self.checkpoint.stats()
        crit_report = self.critic.generate_report()

        self._print_final_report(stats, crit_report, elapsed, output_path)
        return self.approved

    # -------- 表示ヘルパー --------

    def _print_progress(self):
        stats = self.checkpoint.stats()
        console.print(
            f"  [green]承認済み: {stats['approved']}[/green]  "
            f"[yellow]処理済み: {stats['processed']}[/yellow]  "
            f"[red]失敗: {stats['failed']}[/red]"
        )

    def _print_final_report(self, stats, crit_report, elapsed, output_path):
        table = Table(title="Week 1 完了レポート", box=box.ROUNDED)
        table.add_column("項目",      style="cyan")
        table.add_column("結果",      style="green")
        table.add_row("承認済みノート", str(stats["approved"]))
        table.add_row("承認率",       f"{crit_report['approval_rate']*100:.1f}%")
        table.add_row("平均品質スコア", f"{crit_report['avg_quality_score']:.2f}")
        table.add_row("所要時間",      f"{elapsed/60:.1f} 分")
        table.add_row("出力ファイル",   str(output_path))
        console.print(table)
        console.print("\n[bold green]✅ Week 1 完了！次のステップ: Week 2 — Neo4j KG 構築[/bold green]")
        console.print("[dim]  python graph/kg_builder.py[/dim]\n")


# ========================================
# CLI エントリポイント
# ========================================

def main():
    parser = argparse.ArgumentParser(description="PMOS v2.0 Orchestrator — Week 1")
    parser.add_argument("--vault",      type=str, default=str(VAULT_PATH), help="Obsidian Vault パス")
    parser.add_argument("--limit",      type=int, default=PRIORITY_NOTE_LIMIT, help="処理ノート数")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE, help="バッチサイズ")
    parser.add_argument("--demo",       action="store_true",  help="デモモード（Vault不要）")
    args = parser.parse_args()

    vault = args.vault if not args.demo else "./demo_vault"
    orch  = Orchestrator(vault)
    orch.run(
        note_limit = args.limit,
        batch_size = args.batch_size,
        demo_mode  = args.demo,
    )


if __name__ == "__main__":
    main()
