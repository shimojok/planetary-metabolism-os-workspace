import os

# 書き込み対象のフォルダパス
BASE_DIR = r"E:\PM-OS"

# コンテンツの定義（ファイル名の一部をキーにして、書き込む中身を指定）
# ここに、我々が対話してきた「最強のロジック」を詰め込みます。
contents = {
    "10. 状態推論（診断）": """# 状態推論（診断）：今の土壌は何を求めているか？

## 1. 概要
本ドキュメントでは、MBT55-HyperCycleを用いた土壌フェノタイピングによる「状態推論」のアルゴリズムを定義する。

## 2. 推論ロジック
- **入力データ**: 土壌微生物叢、炭素窒素比(C/N)、代謝産物プロファイル。
- **推論エンジン**: Azure AIによる因果推論モデル。
- **出力**: 最適な施肥処方箋および、N2O排出抑制のためのバイパス経路の特定。

## 3. M³モデルとの連携
$M^3 = \text{Microbe} \times \text{Metabolism} \times \text{Management}$
この数理モデルに基づき、土壌の「健康スコア」をリアルタイムで算出する。
""",

    "GP2-1. Green Premium Reverser": """# Green Premium Reverser 設計案
## 脱炭素肥料の経済的合理性の証明

### 1. 課題：グリーンプレミアム
ビル・ゲイツ氏が提唱するように、脱炭素製品は既存の化学肥料（グレー製品）よりも高価である。

### 2. 解決策：反転のメカニズム
PMOS（Planetary Metabolism OS）は、以下の3点でコストを反転させる：
1. **炭素クレジットの即時化**: 土壌への炭素貯留をリアルタイムで証券化。
2. **収穫量（QOL）の向上**: 微生物制御による栄養価の最大化。
3. **医療費削減のインセンティブ**: 健康的な土壌から生まれた作物による社会保障費の削減分を農家に還元。

### 3. 数理的証明
$$C_{total} = (C_{production} + C_{carbon\_tax}) - (V_{credit} + V_{health\_benefit})$$
$V_{health\_benefit}$ が十分に大きくなることで、グリーンプレミアムは消失する。
""",
    
    "README.md": """# Planetary Metabolism OS (PMOS) - BioNexus 3
## Addressing the 51 Billion Ton Climate Challenge

Planetary Metabolism OS is a comprehensive framework for managing Earth's biological and economic cycles. 

### Core Pillars:
1. **AGRIX**: Soil Phenotyping & Regenerative Agriculture.
2. **HealthBook**: Human Metabolic Data Integration.
3. **Climate**: Reversing the Green Premium through Metabolic Credits.
"""
}

def restore_soul():
    print("--- 魂の復元プロセスを開始します ---")
    
    # workspace_all_urls_encoded.txt を読み込んでファイルパスを特定
    url_file = os.path.join(BASE_DIR, "workspace_all_urls_encoded.txt")
    if not os.path.exists(url_file):
        print(f"エラー: {url_file} が見つかりません。")
        return

    with open(url_file, "r", encoding="utf-8") as f:
        urls = f.readlines()

    success_count = 0
    for url in urls:
        url = url.strip()
        # URLからファイル名を取得し、デコードする
        import urllib.parse
        filename = urllib.parse.unquote(url.split("/")[-1])
        
        # フォルダ構造を考慮（AGRIX/, Climate/ 等）
        # 簡単のため、カレントディレクトリ以下の各フォルダ内を探す
        for root, dirs, files in os.walk(BASE_DIR):
            if filename in files:
                filepath = os.path.join(root, filename)
                
                # コンテンツの特定
                content_to_write = ""
                for key, content in contents.items():
                    if key in filename:
                        content_to_write = content
                        break
                
                if content_to_write:
                    with open(filepath, "w", encoding="utf-8") as wf:
                        wf.write(content_to_write)
                    print(f"復元完了: {filename}")
                    success_count += 1

    print(f"\n--- プロセス終了: {success_count} ファイルに魂を注入しました ---")

if __name__ == "__main__":
    restore_soul()