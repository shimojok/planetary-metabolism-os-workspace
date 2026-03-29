
**F001（例：葛根湯）の“最低限かつ十分”なJSON構造**を、正確に1件だけ示します。

```json
{
  "id": "F001",
  "name": "葛根湯",
  "metabolic_pathway": "PATH_01",
  "components": {
    "葛根": {
      "role": "君",
      "phytochemicals": ["プエラリン", "ダイゼイン", "ゲニステイン"],
      "action_tags": ["解表", "抗炎症", "血流改善"]
    },
    "麻黄": {
      "role": "臣",
      "phytochemicals": ["エフェドリン", "プソイドエフェドリン"],
      "action_tags": ["気管支拡張", "交感神経刺激"]
    },
    "桂枝": {
      "role": "臣",
      "phytochemicals": ["シンナムアルデヒド"],
      "action_tags": ["発汗", "血流改善"]
    },
    "芍薬": {
      "role": "佐",
      "phytochemicals": ["ペオニフロリン"],
      "action_tags": ["鎮痙", "抗炎症"]
    },
    "甘草": {
      "role": "佐",
      "phytochemicals": ["グリチルリチン"],
      "action_tags": ["抗炎症", "免疫調節"]
    },
    "生姜": {
      "role": "使",
      "phytochemicals": ["ジンゲロール"],
      "action_tags": ["消化促進", "芳香性刺激"]
    },
    "大棗": {
      "role": "使",
      "phytochemicals": ["多糖類"],
      "action_tags": ["腸内環境改善", "免疫調整"]
    }
  }
}
```

### これで十分な理由（最小要件）

- `id`：識別
    
- `metabolic_pathway`：MBT15射影の基底
    
- `components`：
    
    - `role`：重み付け（君=1.0 / 臣=0.7 / 佐=0.4 / 使=0.3 など）
        
    - `action_tags`：機能差を生む主因子
        
    - `phytochemicals`：将来の精緻化用（現段階では必須ではないが推奨）
        

この形式で**211件をトップレベル配列 `[...]` に格納**すれば、即クラスタリング可能です。