Python

```
import pandas as pd

def run_healthbook_simulation():
    import pandas as pd

def run_healthbook_simulation():
    # --- 1. 浜田先生のナレッジマスター（デモ用抜粋データ） ---
    # 本来はJSONやCSVから読み込みますが、体験用に内部定義します。
    # ●印がある項目を 1.0 (重み) として定義
    matrix_data = {
        "疾患名": ["大腸がん", "狭心症", "糖尿病", "胃がん", "眼精疲労"],
        "早食い型": [1.0, 1.0, 1.0, 1.5, 0.0],  # Q04
        "野菜少ない": [2.0, 1.5, 1.0, 2.0, 2.0], # Q18
        "塩分過多": [1.0, 1.5, 1.0, 2.0, 0.0],  # Q09
        "脂肪過多": [2.0, 2.0, 1.5, 0.0, 0.0],  # Q21
        "夜食型": [1.0, 1.0, 2.0, 1.5, 0.0]     # Q03
    }
    df_matrix = pd.DataFrame(matrix_data).set_index("疾患名")

    # --- 2. ユーザーの問診回答 (ここを書き換えて試せます！) ---
    # 1 = Yes (あてはまる), 0 = No (あてはまらない)
    user_answers = {
        "早食い型": 1,
        "野菜少ない": 1,
        "塩分過多": 1,
        "脂肪過多": 1,
        "夜食型": 1
    }

    # --- 3. 下條・AGRIX・MBT パラメータ (ここを調整して効果を検証！) ---
    agrix_quality_boost = True  # TrueにするとAGRIX産高品質野菜の効果が発動
    mbt_active = True           # Trueにすると腸内代謝が活性化している設定

    # --- 4. 統合推論ロジック ---
    results = []
    for disease in df_matrix.index:
        # A. 浜田式ベースリスク（単純合算）
        base_score = sum(df_matrix.loc[disease][q] * val for q, val in user_answers.items())
        
        # B. 下條式AGRIX補正（高品質な野菜を食べていればリスクを50%軽減）
        mitigation = 0.5 if agrix_quality_boost else 1.0
        
        # C. MBT代謝効率（菌が元気なら有効成分の利用効率が上がり、さらにリスク低減）
        bio_efficiency = 1.2 if mbt_active else 0.8
        
        # 最終スコア計算
        final_score = (base_score * mitigation) / bio_efficiency
        results.append({"疾患": disease, "最終リスクスコア": round(final_score, 2)})

    # 結果を表示
    report = pd.DataFrame(results).sort_values(by="最終リスクスコア", ascending=False)
    
    print("=== BioNexus HealthBook 推論結果 ===")
    print(f"設定: AGRIX品質={agrix_quality_boost}, MBT活性={mbt_active}")
    print("-" * 40)
    print(report)
    print("-" * 40)

# 実行
run_healthbook_simulation()
    print("=== BioNexus HealthBook 推論結果 ===")

run_healthbook_simulation()
```