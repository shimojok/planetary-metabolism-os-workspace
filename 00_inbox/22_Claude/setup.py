#!/usr/bin/env python3
"""
PMOS v2.0 — セットアップスクリプト
=====================================
1. Python バージョン確認
2. 仮想環境の案内
3. 必要パッケージのインストール確認
4. .env ファイルのセットアップ案内
5. 動作テスト（デモモード）

使用方法:
    python setup.py
"""

import sys
import os
import subprocess
from pathlib import Path

# ==============================
# カラー出力
# ==============================
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

ok   = lambda s: print(f"{GREEN}✅ {s}{RESET}")
warn = lambda s: print(f"{YELLOW}⚠️  {s}{RESET}")
err  = lambda s: print(f"{RED}❌ {s}{RESET}")
info = lambda s: print(f"{CYAN}ℹ️  {s}{RESET}")
head = lambda s: print(f"\n{BOLD}{s}{RESET}")

# ==============================
# 1. Python バージョン確認
# ==============================
head("=" * 50)
head("  PMOS v2.0 セットアップチェック")
head("=" * 50)

head("【1】Python バージョン確認")
ver = sys.version_info
if ver >= (3, 11):
    ok(f"Python {ver.major}.{ver.minor}.{ver.micro}")
elif ver >= (3, 9):
    warn(f"Python {ver.major}.{ver.minor} — 3.11+ を推奨します")
else:
    err(f"Python {ver.major}.{ver.minor} は非対応です。3.11以上が必要です。")
    sys.exit(1)

# ==============================
# 2. 必須パッケージ確認
# ==============================
head("【2】必須パッケージ確認")

REQUIRED = {
    "openai":              "openai>=1.30.0",
    "dotenv":              "python-dotenv>=1.0.0",
    "tqdm":                "tqdm>=4.66.0",
    "rich":                "rich>=13.7.0",
    "numpy":               "numpy>=1.26.0",
    "matplotlib":          "matplotlib>=3.8.0",
}

OPTIONAL = {
    "neo4j":               "neo4j>=5.19.0       (Week2 KG構築で必要)",
    "chromadb":            "chromadb>=0.5.0     (Week2 ベクトルDB)",
    "langgraph":           "langgraph>=0.1.0    (Week3 エージェント)",
    "sentence_transformers":"sentence-transformers (Week3 埋め込み)",
    "scipy":               "scipy>=1.13.0       (Week4 シミュレーション)",
}

missing_required = []
for module, pkg in REQUIRED.items():
    try:
        __import__(module)
        ok(module)
    except ImportError:
        err(f"{module} が見つかりません → pip install {pkg.split('>')[0]}")
        missing_required.append(pkg)

if missing_required:
    print(f"\n必須パッケージをインストールします...")
    cmd = [sys.executable, "-m", "pip", "install"] + [p.split()[0] for p in missing_required]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        ok("インストール完了")
    else:
        err(f"インストール失敗: {result.stderr[:200]}")
        info("手動で実行してください: pip install -r requirements.txt")

print(f"\n  オプション（後のWeekで必要）:")
for module, pkg in OPTIONAL.items():
    try:
        __import__(module)
        ok(f"  {module}")
    except ImportError:
        warn(f"  {module} — 未インストール: {pkg}")

# ==============================
# 3. .env ファイル確認
# ==============================
head("【3】環境変数 (.env) 確認")

env_path    = Path(".env")
sample_path = Path(".env.example")

if env_path.exists():
    ok(".env ファイルが存在します")

    # API Keyの基本チェック
    content = env_path.read_text()
    if "OPENAI_API_KEY=sk-" in content and "sk-xxxxxxxx" not in content:
        ok("OPENAI_API_KEY が設定されています")
    else:
        err("OPENAI_API_KEY が未設定です")
        info(".env ファイルを開いて OPENAI_API_KEY=sk-your-key-here を設定してください")

    if "VAULT_PATH=" in content:
        vault_line = [l for l in content.split("\n") if l.startswith("VAULT_PATH=")]
        if vault_line:
            vault_path = vault_line[0].split("=", 1)[1].strip()
            if vault_path and Path(vault_path).exists():
                ok(f"VAULT_PATH: {vault_path}")
            elif vault_path:
                warn(f"VAULT_PATH が見つかりません: {vault_path}")
            else:
                warn("VAULT_PATH が空です — Obsidian Vaultのパスを設定してください")
else:
    warn(".env ファイルがありません")
    if sample_path.exists():
        # .env.example から自動コピー
        env_path.write_text(sample_path.read_text())
        ok(".env.example から .env を作成しました")
        info(">>> .env を開いて OPENAI_API_KEY と VAULT_PATH を設定してください <<<")
    else:
        # 最小限の .env を作成
        env_path.write_text(
            "OPENAI_API_KEY=sk-your-openai-api-key-here\n"
            "VAULT_PATH=/path/to/your/obsidian/vault\n"
            "BATCH_SIZE=10\n"
            "MAX_CRITIQUE_ITERATIONS=3\n"
            "PRIORITY_NOTE_LIMIT=100\n"
        )
        ok(".env を新規作成しました — API KeyとVaultパスを設定してください")

# ==============================
# 4. ディレクトリ構造確認
# ==============================
head("【4】ディレクトリ構造確認")

dirs = ["agents", "data", "graph", "memory", "config", "targets/gates_foundation", "targets/microsoft"]
for d in dirs:
    path = Path(d)
    path.mkdir(parents=True, exist_ok=True)
    ok(f"{d}/")

# ==============================
# 5. 実行方法の案内
# ==============================
head("【5】Week 1 実行方法")

print(f"""
{BOLD}デモモード（Vault・APIキー不要）:{RESET}
  cd PMOS_v2
  python agents/orchestrator.py --demo

{BOLD}本番モード（手順）:{RESET}
  1. .env に OPENAI_API_KEY と VAULT_PATH を設定
  2. python agents/explorer.py    # Day 1-2: スキャン＆評価
  3. python agents/classifier.py  # Day 3-4: 分類＋エンティティ抽出
  4. python agents/critic.py      # Day 4-5: 品質検証
  5. python agents/orchestrator.py # Day 6-7: 批評ループ統括

{BOLD}進捗確認:{RESET}
  cat data/checkpoint.json        # チェックポイント確認
  cat data/approved_notes.json    # 承認済みノート確認

{BOLD}Week 2（Neo4j KG構築）は approved_notes.json 完成後:{RESET}
  docker run -d --name neo4j-pmos \\
    -p 7474:7474 -p 7687:7687 \\
    -e NEO4J_AUTH=neo4j/password \\
    neo4j:5-community

  python graph/kg_builder.py
""")

head("=" * 50)
ok("セットアップチェック完了！")
head("=" * 50)
