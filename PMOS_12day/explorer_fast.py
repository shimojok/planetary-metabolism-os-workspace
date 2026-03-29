"""
高速探索エージェント - 500核心ノートを特定
"""

from pathlib import Path
import json
import re

class FastExplorer:
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        
        # ホルダー別スコア倍率（あなたの構成に最適化）
        self.folder_boost = {
            "03_MBT55": 2.0,
            "04_AGRIX": 2.0,
            "07_HealthBook": 2.0,
            "06_PBPE": 2.0,
            "05_AgriWare": 1.5,
            "08_MBT_KampoLibrary": 1.5,
            "09_MBT漢方代謝ライブラリー": 1.5,
            "10_MBT_Probiotics": 1.5,
            "01_Planetary_Problems": 1.0,
            "02_Biological_Systems": 1.0,
            "11_AI_Development": 1.0,
            "21_NotebookLM": 1.0,
            "22_Claude": 1.0,
            "00_inbox": 0.5
        }
        
        # 最重要キーワード（ゲイツ提案に直結）
        self.keywords = {
            'mbt55': 5, 'ghg': 5, 'co2': 5, 'メタン': 5, 'n2o': 5,
            'ゲイツ': 5, 'gates': 5, 'microsoft': 5, 'azure': 5,
            'teleodynamics': 5, 'ハイパーサイクル': 5,
            'シミュレーション': 3, '数式': 3, 'データ': 3,
            '削減量': 3, '収量': 3, 'コスト': 3,
            'agrix': 3, 'healthbook': 3, 'pbpe': 3
        }
    
    def score_note(self, file_path: Path) -> int:
        """ノートの重要度スコアを計算"""
        score = 0
        path_str = str(file_path)
        
        # フォルダによるブースト
        for folder, boost in self.folder_boost.items():
            if folder in path_str:
                score += 10 * boost
                break
        
        # ファイル名でのキーワード
        name_lower = file_path.name.lower()
        for kw, points in self.keywords.items():
            if kw in name_lower:
                score += points
        
        # 内容の先頭でキーワードチェック
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(2000).lower()
                
            for kw, points in self.keywords.items():
                if kw in content:
                    score += points
        except:
            pass
        
        return score
    
    def extract_core_notes(self, limit: int = 500):
        """核心ノートを抽出"""
        all_notes = []
        
        # 全.mdファイルをスキャン
        for md in self.vault_path.rglob("*.md"):
            # 最低サイズ（1KB以上）
            if md.stat().st_size < 1000:
                continue
                
            score = self.score_note(md)
            if score >= 10:  # スコア10以上のみ
                all_notes.append({
                    "path": str(md),
                    "score": score,
                    "size": md.stat().st_size,
                    "name": md.name,
                    "folder": md.parent.name
                })
        
        # スコア順にソート
        all_notes.sort(key=lambda x: x['score'], reverse=True)
        
        # 上位limit件を抽出
        core_notes = all_notes[:limit]
        
        # フォルダ別集計
        folder_stats = {}
        for note in core_notes:
            folder = note['folder']
            folder_stats[folder] = folder_stats.get(folder, 0) + 1
        
        # 保存
        result = {
            "total_scanned": len(all_notes),
            "core_notes": core_notes,
            "folder_distribution": folder_stats,
            "score_range": {
                "min": core_notes[-1]['score'] if core_notes else 0,
                "max": core_notes[0]['score'] if core_notes else 0,
                "avg": sum(n['score'] for n in core_notes) / len(core_notes) if core_notes else 0
            }
        }
        
        # dataフォルダがなければ作成
        Path("data").mkdir(exist_ok=True)
        
        with open('data/core_500.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"\n🎯 核心500ノート抽出完了！")
        print(f"📊 スキャン総数: {len(all_notes)}")
        print(f"📈 スコア範囲: {result['score_range']['min']} - {result['score_range']['max']} (平均 {result['score_range']['avg']:.1f})")
        print("\n📁 フォルダ別内訳:")
        for folder, count in sorted(folder_stats.items(), key=lambda x: x[1], reverse=True):
            print(f"  {folder}: {count}件")
        
        return core_notes

if __name__ == "__main__":
    # あなたのVaultパスに変更してください
    vault_path = r"E:\Documents\BioNexus Holdings\BioNexus_vault"
    
    explorer = FastExplorer(vault_path)
    core_notes = explorer.extract_core_notes(500)