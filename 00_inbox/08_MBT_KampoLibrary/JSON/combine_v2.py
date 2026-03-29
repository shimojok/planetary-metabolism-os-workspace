import json
import os
from typing import Dict

class KampoLibraryMerger:
    def __init__(self):
        self.phases = {}
        self.master_library = {
            "mbt_kampo_library": {
                "version": "2.44.0",
                "last_updated": "2026-02-25",
                "total_formulas": 294,
                "fully_defined": 0,
                "classification_source": "Shimojo Phytochemical Classification",
                "mbt55_version": "MBT55-v2.44",
                "formulas": {}
            }
        }
    
    def load_phase_file(self, phase_num: int, filepath: str):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.phases[phase_num] = data
                formulas = data.get('mbt_kampo_library', {}).get('formulas', {})
                print(f"✅ フェーズ{phase_num} 読み込み完了: {len(formulas)}方剤")
                return True
        except FileNotFoundError:
            print(f"❌ ファイルが見つかりません: {filepath}")
            return False
        except json.JSONDecodeError as e:
            print(f"❌ JSONデコードエラー (フェーズ{phase_num}): {e}")
            return False
        except Exception as e:
            print(f"❌ 予期せぬエラー (フェーズ{phase_num}): {e}")
            return False
    
    def merge_all(self) -> Dict:
        all_formulas = {}
        duplicate_count = 0
        new_count = 0
        error_count = 0
        
        for phase_num, phase_data in sorted(self.phases.items()):
            try:
                formulas = phase_data.get('mbt_kampo_library', {}).get('formulas', {})
                for formula_id, formula_data in formulas.items():
                    if formula_id in all_formulas:
                        duplicate_count += 1
                        print(f"⚠️ 重複検出: {formula_id} (フェーズ{phase_num})")
                    else:
                        all_formulas[formula_id] = formula_data
                        new_count += 1
            except Exception as e:
                error_count += 1
                print(f"❌ 処理エラー (フェーズ{phase_num}): {e}")
        
        self.master_library['mbt_kampo_library']['formulas'] = dict(sorted(all_formulas.items()))
        self.master_library['mbt_kampo_library']['fully_defined'] = len(all_formulas)
        
        print(f"\n📊 結合結果:")
        print(f"  新規方剤: {new_count}")
        print(f"  重複方剤: {duplicate_count}")
        print(f"  エラー: {error_count}")
        print(f"  合計方剤: {len(all_formulas)}")
        
        return self.master_library
    
    def save_master(self, filename: str = "mbt_kampo_library_master_v2.44.json"):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.master_library, f, ensure_ascii=False, indent=2)
        print(f"\n💾 マスターファイル保存完了: {filename}")
        if os.path.exists(filename):
            size = os.path.getsize(filename) / 1024
            print(f"  ファイルサイズ: {size:.1f} KB")

def main():
    print("="*60)
    print("MBT漢方代謝ライブラリー 結合ツール v2.44")
    print("="*60)
    
    merger = KampoLibraryMerger()
    
    # フェーズ1〜44のファイルを指定
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
        22: "phase22_duplicates.json",
        23: "phase23_new.json",
        24: "phase24_new.json",
        25: "phase25_new.json",
        26: "phase26_new.json",
        27: "phase27_new.json",
        28: "phase28_new.json",
        29: "phase29_new.json",
        30: "phase30_new.json",
        31: "phase31_new.json",
        32: "phase32_new.json",
        33: "phase33_new.json",
        34: "phase34_new.json",
        35: "phase35_new.json",
        36: "phase36_new.json",
        37: "phase37_new.json",
        38: "phase38_new.json",
        39: "phase39_new.json",
        40: "phase40_new.json",
        41: "phase41_new.json",
        42: "phase42_new.json",
        43: "phase43_new.json",
        44: "phase44_new.json"
    }
    
    # ファイル読み込み
    success_count = 0
    for phase_num, filename in phase_files.items():
        if merger.load_phase_file(phase_num, filename):
            success_count += 25  # 5方剤ずつカウント
        else:
            print(f"⚠️ スキップ: フェーズ{phase_num}")
    
    print(f"\n📁 読み込み成功: {success_count}方剤分")
    
    # 結合実行
    master = merger.merge_all()
    
    # 保存
    merger.save_master()
    
    # 簡単な検証
    print("\n🔍 検証結果:")
    formulas = master['mbt_kampo_library']['formulas']
    expected = 211
    actual = len(formulas)
    
    if actual == expected:
        print(f"✅ 方剤数一致: {actual}/{expected}")
    else:
        print(f"❌ 方剤数不一致: 期待値={expected}, 実際={actual}")
    
    # 最初の5方剤と最後の5方剤を表示
    print("\n📋 最初の5方剤:")
    for i, (fid, fdata) in enumerate(list(formulas.items())[:5]):
        print(f"  {fid}: {fdata.get('name', '不明')}")
    
    print("\n📋 最後の5方剤:")
    for fid, fdata in list(formulas.items())[-5:]:
        print(f"  {fid}: {fdata.get('name', '不明')}")

if __name__ == "__main__":
    main()