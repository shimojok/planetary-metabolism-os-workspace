import os

def create_structure(base_path, structure):
    # フォルダが存在しない場合は作成する
    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)
        print(f"Created folder: {base_path}")

    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # 再帰的にフォルダを作成
            create_structure(path, content)
        else:
            # ファイルを書き込む
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
                print(f"Created file: {path}")

# --- コンテンツ定義 ---

portal_readme = """# Planetary-Metabolism-OS (PM-OS)
> **Updated: 2026-02-05**

## 🌍 The Mission: Fixing Planetary Metabolism
[English] We redefine climate action as a **Biological Transformation**. PM-OS is a decentralized infrastructure designed to restore Earth’s carbon/nitrogen cycles using the **MBT55 Microbial Hypercycle**.
[日本語] 私たちは気候変動対策を「生物学的転換」として再定義します。PM-OSは、MBT55微生物ハイパーサイクルを用いて地球の炭素・窒素循環を修復する分散型インフラです。

## ⚡ Answering the "Gates Challenge"
Bill Gates stated: *"There is no equivalent of carbon capture for nitrous oxide (N₂O)."*
**Our Answer:** Don't capture—**Bypass.** MBT55 stabilizes nitrogen into organic humus within 24 hours, preventing N₂O gasification.
[日本語] ビル・ゲイツ氏は「N₂Oには炭素回収に相当するものがない」と言及しましたが、我々は「放出前のバイパス」で応えます。MBT55は24時間以内に窒素を腐植質へ固定し、ガス化そのものを防ぎます。

## 💰 Beyond the Investment Gap (Rockefeller Response)
"Funding shortage is a result, not a starting point." By flipping the **Green Premium** to a negative value through waste upcycling and 30% medical cost reduction, we solve the investment gap at the root.
[日本語] 「資金不足は結果であり、スタートではない」。廃棄物の資源化と医療費3割削減により、グリーン・プレミアムをマイナス（収益）へ転換し、投資ギャップを根本から解決します。
"""

n2o_logic = """import math
class MBT_Nitrogen_Bypass_Model:
    def __init__(self):
        # Data from MBT55 PDF (Sample B)
        self.proteolytic_bacteria = 2.39e7
        self.total_species = 120
    def calculate_efficiency(self):
        # Biological Bypass Logic
        return min(0.95, 0.85 + (math.log10(self.total_species)/10))
"""

# --- 構造定義 ---
structure = {
    "Planetary-Metabolism-OS": {
        "README.md": portal_readme,
        "docs": {
            "strategy": {
                "GATES_RESPONSE.md": "# Detailed Response to Bill Gates\nN2O Bypass implementation details...",
                "ROCKEFELLER_RESPONSE.md": "# Cost Structure Reform\nAddressing the funding gap via MBT ROI..."
            }
        }
    },
    "AGRIX_Regen_Engine": {
        "README.md": "# AGRIX_Regen_Engine\nFocus on GHG Quantification & PBPE Finance.",
        "logic": {
            "mbt_biocontrol_model.py": n2o_logic
        }
    },
    "HealthBook_MI_Core": {
        "README.md": "# HealthBook_MI_Core\nFocus on Metabolic Intelligence & Food Is Medicine."
    }
}

# 実行（現在のフォルダ直下に作成）
create_structure(".", structure)
print("\n--- ALL SUCCESS: 3 Repositories have been updated with 0205 Strategic Logic. ---")