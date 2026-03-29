import os
import json
from pathlib import Path

# 現在のフォルダ（Vault）をスキャン
VAULT_PATH = Path(".")

def scan_vault():
    print(f"🚀 PMOS AntiGravity スキャナー起動...")
    knowledge_base = []
    
    # 30万人データや漢方ライブラリの存在確認
    important_files = [
        "mbt_kampo_library_final_array.json",
        "questionnaire_full.json.md",
        "game3_api.py"
    ]
    
    for root, dirs, files in os.walk(VAULT_PATH):
        # システムフォルダを除外
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'venv']
        
        for file in files:
            if file.endswith(".md") or file in important_files:
                path = Path(root) / file
                try:
                    # ファイル情報を取得
                    knowledge_base.append({
                        "name": file,
                        "path": str(path.relative_to(VAULT_PATH)),
                        "type": "knowledge_node" if file.endswith(".md") else "core_data"
                    })
                except Exception:
                    continue

    # 知識マップ（JSON）の書き出し
    output_file = "pmos_knowledge_map.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(knowledge_base, f, ensure_ascii=False, indent=2)
    
    print(f"✅ スキャン成功！ {len(knowledge_base)} 個の知能資産をインデックスしました。")
    print(f"📄 成果物: {output_file} が生成されました。")

if __name__ == "__main__":
    scan_vault()