"""
PMOS v2.0 共通設定・ユーティリティ
すべてのエージェントがこのモジュールをインポートして使用する
"""

import os
import json
import logging
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# .env 読み込み
load_dotenv()

# ========================================
# 設定定数
# ========================================

VAULT_PATH = Path(os.getenv("VAULT_PATH", "./vault_original"))
DATA_DIR   = Path("data")
GRAPH_DIR  = Path("graph")

OPENAI_API_KEY    = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

NEO4J_URI      = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER     = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

BATCH_SIZE              = int(os.getenv("BATCH_SIZE", 10))
MAX_CRITIQUE_ITERATIONS = int(os.getenv("MAX_CRITIQUE_ITERATIONS", 3))
PRIORITY_NOTE_LIMIT     = int(os.getenv("PRIORITY_NOTE_LIMIT", 100))

# ドメイン定義
DOMAINS = ["MBT55", "AGRIX", "HealthBook", "PBPE", "Climate", "Other"]

DOMAIN_KEYWORDS = {
    "MBT55":      ["mbt55", "微生物", "teleodynamics", "バイオ", "代謝経路", "microbial"],
    "AGRIX":      ["agrix", "農業", "政策", "土壌", "agriculture", "carbon sequestration"],
    "HealthBook": ["healthbook", "健康", "腸内", "health", "metabolic", "病気", "医療"],
    "PBPE":       ["pbpe", "金融", "経済", "finance", "gdp", "投資", "carbon credit"],
    "Climate":    ["気候", "ghg", "co2", "温室", "climate", "carbon", "メタン"],
}

# ========================================
# ディレクトリ初期化
# ========================================

def init_directories():
    """必要なディレクトリを作成"""
    for d in [DATA_DIR, GRAPH_DIR, Path("targets/gates_foundation"), Path("targets/microsoft")]:
        d.mkdir(parents=True, exist_ok=True)

# ========================================
# ロガー設定
# ========================================

def get_logger(name: str) -> logging.Logger:
    """統一フォーマットのロガーを返す"""
    log_level = os.getenv("LOG_LEVEL", "INFO")
    logging.basicConfig(
        level=getattr(logging, log_level),
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        datefmt="%H:%M:%S"
    )
    return logging.getLogger(name)

# ========================================
# ファイルユーティリティ
# ========================================

def save_json(data, path: Path, *, ensure_ascii=False):
    """JSONファイルに保存（日本語対応）"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=ensure_ascii, default=str)

def load_json(path: Path) -> dict | list:
    """JSONファイルを読み込む"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_note_content(path: str, max_chars: int = 3000) -> str:
    """ノートの内容を読み込む（文字数制限あり）"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()[:max_chars]
    except Exception as e:
        return f"[読み込みエラー: {e}]"

# ========================================
# クイック分類（キーワードベース・高速）
# ========================================

def quick_classify(content: str) -> str:
    """キーワードベースの簡易ドメイン分類"""
    content_lower = content.lower()
    scores = {domain: 0 for domain in DOMAIN_KEYWORDS}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        scores[domain] = sum(1 for kw in keywords if kw in content_lower)
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "Other"

# ========================================
# チェックポイント管理
# ========================================

class CheckpointManager:
    """処理の進捗をチェックポイントで管理"""

    def __init__(self, checkpoint_path: str = "data/checkpoint.json"):
        self.path = Path(checkpoint_path)
        self.data = self._load()

    def _load(self) -> dict:
        if self.path.exists():
            return load_json(self.path)
        return {"processed": [], "approved": [], "failed": [], "created_at": datetime.now().isoformat()}

    def save(self):
        save_json(self.data, self.path)

    def mark_processed(self, path: str):
        if path not in self.data["processed"]:
            self.data["processed"].append(path)
            self.save()

    def mark_approved(self, result: dict):
        self.data["approved"].append(result)
        self.save()

    def mark_failed(self, path: str, reason: str):
        self.data["failed"].append({"path": path, "reason": reason})
        self.save()

    def is_processed(self, path: str) -> bool:
        return path in self.data["processed"]

    def stats(self) -> dict:
        return {
            "processed": len(self.data["processed"]),
            "approved":  len(self.data["approved"]),
            "failed":    len(self.data["failed"]),
        }

# モジュール読み込み時に自動実行
init_directories()
