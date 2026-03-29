"""
MBT漢方代謝ライブラリー 結合スクリプト v2
フェーズ23〜44（102〜211方剤）のみを結合
"""

import json
import os
from typing import Dict

class KampoLibraryMergerPhase2:
    """フェーズ23〜44専用結合クラス"""
    
    def __init__(self):
        self.phases = {}
        self.master_library = {
            "mbt_kampo_library": {
                "version": "2.44.0",
                "last_updated": "2026-02-25",
                "total_formulas": 294,
                "fully_defined": 0,
                "phase_range": "23-44",
                "formula_range": "102-211",
                "classification_source": "Shimojo Phytochemical Classification",
                "mbt55_version": "MBT55-v2.44",
                "formulas": {}
            }
        }
    
    def load_phase_file(self, phase_num: int, filepath: str):
        """フェーズファイルを読み込む"""
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
        """全フェーズを結合"""
        all_formulas = {}
        duplicate_count = 0
        new_count = 0
        
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
                print(f"❌ 処理エラー (フェーズ{phase_num}): {e}")
        
        # F番号でソート
        self.master_library['mbt_kampo_library']['formulas'] = dict(sorted(all_formulas.items()))
        self.master_library['mbt_kampo_library']['fully_defined'] = len(all_formulas)
        
        print(f"\n📊 結合結果:")
        print(f"  新規方剤: {new_count}")
        print(f"  重複方剤: {duplicate_count}")
        print(f"  合計方剤: {len(all_formulas)}")
        
        return self.master_library
    
    def save_master(self, filename: str = "mbt_kampo_library_phase23-44.json"):
        """マスターJSONを保存"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.master_library, f, ensure_ascii=False, indent=2)
        print(f"\n💾 マスターファイル保存完了: {filename}")
        if os.path.exists(filename):
            size = os.path.getsize(filename) / 1024
            print(f"  ファイルサイズ: {size:.1f} KB")
    
    def verify_formulas(self):
        """方剤の範囲を検証"""
        formulas = self.master_library['mbt_kampo_library']['formulas']
        f_numbers = [int(fid.replace('F', '')) for fid in formulas.keys() if fid.startswith('F')]
        
        if f_numbers:
            print(f"\n🔍 方剤番号範囲: {min(f_numbers)} 〜 {max(f_numbers)}")
            print(f"  期待範囲: 102 〜 211")
            
            # 範囲内かチェック
            min_ok = min(f_numbers) >= 102
            max_ok = max(f_numbers) <= 211
            
            if min_ok and max_ok:
                print(f"✅ 方剤番号は期待範囲内です")
            else:
                print(f"⚠️ 方剤番号が期待範囲から外れています")

def main():
    """メイン実行"""
    print("="*60)
    print("MBT漢方代謝ライブラリー 結合ツール v2")
    print("フェーズ23〜44（102〜211方剤）専用")
    print("="*60)
    
    merger = KampoLibraryMergerPhase2()
    
    # フェーズ23〜44のファイルを指定
    phase_files = {
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
    total_formulas = 0
    
    for phase_num, filename in phase_files.items():
        if merger.load_phase_file(phase_num, filename):
            success_count += 1
            # 簡易的な方剤数カウント（実際の数は後で集計）
            total_formulas += 5
    
    print(f"\n📁 読み込み成功: {success_count}/22 フェーズ")
    print(f"  期待される方剤数: 約 {success_count * 5} 方剤")
    
    if success_count == 0:
        print("❌ ファイルが読み込めませんでした。ファイル名を確認してください。")
        return
    
    # 結合実行
    master = merger.merge_all()
    
    # 保存
    merger.save_master()
    
    # 検証
    merger.verify_formulas()
    
    # 最初と最後の5方剤を表示
    formulas = master['mbt_kampo_library']['formulas']
    
    print("\n📋 最初の5方剤:")
    for i, (fid, fdata) in enumerate(list(formulas.items())[:5]):
        print(f"  {fid}: {fdata.get('name', '不明')}")
    
    print("\n📋 最後の5方剤:")
    for fid, fdata in list(formulas.items())[-5:]:
        print(f"  {fid}: {fdata.get('name', '不明')}")
    
    # 統計情報
    print("\n📊 カテゴリ統計:")
    categories = {}
    for fid, fdata in formulas.items():
        cat = fdata.get('category', '未分類')
        categories[cat] = categories.get(cat, 0) + 1
    
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {cat}: {count}方剤")

if __name__ == "__main__":
    main()