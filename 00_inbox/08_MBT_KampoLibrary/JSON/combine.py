"""
MBT漢方代謝ライブラリー 結合スクリプト
全フェーズのJSONを結合して完全版を生成
"""

import json
import os
from typing import Dict, List

class KampoLibraryMerger:
    """漢方ライブラリー結合クラス"""
    
    def __init__(self):
        self.phases = {}
        self.master_library = {
            "mbt_kampo_library": {
                "version": "2.22.0",
                "last_updated": "2026-02-24",
                "total_formulas": 294,
                "fully_defined": 0,
                "classification_source": "Shimojo Phytochemical Classification",
                "mbt55_version": "MBT55-v2.22",
                "formulas": {}
            }
        }
        
    def load_phase_file(self, phase_num: int, filepath: str):
        """フェーズファイルを読み込む"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.phases[phase_num] = data
                print(f"✅ フェーズ{phase_num} 読み込み完了: {len(data.get('mbt_kampo_library', {}).get('formulas', {}))}方剤")
        except Exception as e:
            print(f"❌ フェーズ{phase_num} 読み込みエラー: {e}")
    
    def merge_all(self) -> Dict:
        """全フェーズを結合"""
        all_formulas = {}
        duplicate_count = 0
        new_count = 0
        
        # 各フェーズから処方を収集
        for phase_num, phase_data in sorted(self.phases.items()):
            formulas = phase_data.get('mbt_kampo_library', {}).get('formulas', {})
            
            for formula_id, formula_data in formulas.items():
                if formula_id in all_formulas:
                    duplicate_count += 1
                    print(f"⚠️ 重複検出: {formula_id} (フェーズ{phase_num})")
                else:
                    all_formulas[formula_id] = formula_data
                    new_count += 1
        
        # マスターライブラリに格納
        self.master_library['mbt_kampo_library']['formulas'] = dict(sorted(all_formulas.items()))
        self.master_library['mbt_kampo_library']['fully_defined'] = len(all_formulas)
        
        print(f"\n📊 結合結果:")
        print(f"  新規方剤: {new_count}")
        print(f"  重複方剤: {duplicate_count}")
        print(f"  合計方剤: {len(all_formulas)}")
        
        return self.master_library
    
    def save_master(self, filename: str = "mbt_kampo_library_master.json"):
        """マスターJSONを保存"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.master_library, f, ensure_ascii=False, indent=2)
        print(f"\n💾 マスターファイル保存完了: {filename}")
        print(f"  ファイルサイズ: {os.path.getsize(filename) / 1024:.1f} KB")

def create_phase_files():
    """各フェーズのJSONファイルを作成（サンプル）"""
    
    phase_files = {
        1: "phase1_high_priority.json",
        2: "phase2_medium_priority.json",
        3: "phase3_medium_high.json",
        4: "phase4_medium.json",
        5: "phase5_medium_high.json",
        6: "phase6_duplicates.json",
        7: "phase7_new.json",
        8: "phase8_new.json",
        9: "phase9_new.json",
        10: "phase10_new.json",
        11: "phase11_new.json",
        12: "phase12_new.json",
        13: "phase13_new.json",
        14: "phase14_new.json",
        15: "phase15_new.json",
        16: "phase16_new.json",
        17: "phase17_new.json",
        18: "phase18_new.json",
        19: "phase19_new.json",
        20: "phase20_new.json",
        21: "phase21_new.json",
        22: "phase22_duplicates.json"
    }
    
    return phase_files

def main():
    """メイン実行"""
    print("="*60)
    print("MBT漢方代謝ライブラリー 結合ツール")
    print("="*60)
    
    merger = KampoLibraryMerger()
    phase_files = create_phase_files()
    
    # 各フェーズファイルを読み込み
    for phase_num, filename in phase_files.items():
        if os.path.exists(filename):
            merger.load_phase_file(phase_num, filename)
        else:
            print(f"⚠️ ファイルが見つかりません: {filename}")
            # デモ用：空のデータを作成
            demo_data = {
                "mbt_kampo_library": {
                    "formulas": {
                        f"F{phase_num:03d}": {
                            "id": f"F{phase_num:03d}",
                            "name": f"デモ方剤{phase_num}",
                            "category": "デモ"
                        }
                    }
                }
            }
            merger.phases[phase_num] = demo_data
            print(f"  デモデータを作成: フェーズ{phase_num}")
    
    # 結合実行
    master = merger.merge_all()
    
    # 保存
    merger.save_master()
    
    # 統計情報
    print("\n📈 統計情報:")
    formulas = master['mbt_kampo_library']['formulas']
    categories = {}
    for f_id, f_data in formulas.items():
        cat = f_data.get('category', '未分類')
        categories[cat] = categories.get(cat, 0) + 1
    
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {cat}: {count}方剤")

if __name__ == "__main__":
    main()