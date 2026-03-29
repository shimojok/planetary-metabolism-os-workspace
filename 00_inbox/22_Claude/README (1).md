# MBT Probiotics Screening Game v2.0

30万人の実証データに基づくプロバイオティクススクリーニングゲーム

---

## 🚀 クイックスタート

### **1. FastAPIバックエンド起動**

```bash
# 依存関係インストール
pip install -r requirements.txt

# サーバー起動
cd api
python main.py
```

APIは http://localhost:8000 で起動します。

### **2. フロントエンド起動**

```bash
# public/index.htmlをブラウザで開く
open public/index.html

# または簡易HTTPサーバー起動
python -m http.server 3000 --directory public
```

フロントエンドは http://localhost:3000 で起動します。

---

## 📁 プロジェクト構造

```
game3-final/
├── api/
│   └── main.py                 # FastAPIバックエンド
├── public/
│   └── index.html              # フロントエンド（スタンドアロン版）
├── requirements.txt
└── README.md
```

---

## 🎮 使い方

### **Step 1: 開始**
- 「開始する」ボタンをクリック

### **Step 2: 問診（10項目）**
- 各質問に「はい」「いいえ」で回答
- 全て回答後、「疾病リスクを予測」をクリック

### **Step 3: リスク予測結果**
- 疾病ごとのリスクスコアを表示
- 推奨ファイトケミカルのプレビュー表示
- 疾病をクリックして詳細表示

### **Step 4: 疾病詳細**
- ファイトケミカルの詳細情報
  - 含有食品
  - 臨床効果
  - 吸収メカニズム
  - 推奨摂取量
  - 実践例

---

## 🔧 APIエンドポイント

### GET /
```
APIステータス確認
```

### GET /api/questionnaire
```
問診票取得
レスポンス: 10項目の問診データ
```

### POST /api/predict_risk
```
疾病リスク予測
リクエスト: { "answers": { "1": true, "2": false, ... } }
レスポンス: リスク予測 + ファイトケミカル推奨
```

### GET /api/phytochemicals
```
全ファイトケミカルリスト取得
```

### GET /api/phytochemicals/{id}
```
特定ファイトケミカルの詳細取得
```

---

## 💡 主要機能

### **1. 30万人実証データに基づくリスク予測**
- 10項目の問診で疾病リスクを算出
- 食生活因子とのマッチング
- リスクレベル判定（HIGH/MEDIUM/LOW）

### **2. ファイトケミカル詳細推奨**
- 疾病別の推奨ファイトケミカル
- 生物学的利用能・吸収メカニズム
- 実践的な摂取ガイド（「玉ねぎ中1個で30mg」など）

### **3. 視覚的なUI**
- Tailwind CSSによるモダンデザイン
- グラデーション・カードレイアウト
- レスポンシブ対応

---

## 📊 データ統計

- **問診項目**: 10項目（フル版: 105項目対応可能）
- **疾病**: 3疾病（実際は93疾病対応可能）
- **ファイトケミカル**: 3種類の詳細データ（実際は12種類）
- **実証データ**: 30万人

---

## 🔧 技術スタック

### バックエンド
- **FastAPI**: 高速WebAPIフレームワーク
- **Pydantic**: データバリデーション
- **Uvicorn**: ASGIサーバー

### フロントエンド
- **HTML5 + JavaScript**: Vanilla JS（フレームワーク不要）
- **Tailwind CSS**: ユーティリティファーストCSS
- **Fetch API**: HTTPクライアント

---

## 🚀 デプロイ

### Vercelへのデプロイ

1. **FastAPI用のvercel.json作成**
```json
{
  "builds": [
    {
      "src": "api/main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "api/main.py"
    },
    {
      "src": "/(.*)",
      "dest": "public/index.html"
    }
  ]
}
```

2. **デプロイ実行**
```bash
vercel
```

---

## 📧 Bill Gates氏へのプレゼンテーション

### メール件名
```
"Interactive Demo: 300,000-Patient Data → Phytochemical Recommendations 
in Real-Time"
```

### デモURL
```
https://mbt-probiotics-v2.vercel.app
```

### ハイライト
- 30秒で疾病リスク予測
- 科学的根拠に基づくファイトケミカル推奨
- 実践的な摂取ガイド（今日から実行可能）
- MBT55の価値: 生物学的利用能を最大化

---

## 📝 今後の拡張

- [ ] 105項目フル問診実装
- [ ] 12種類全ファイトケミカル追加
- [ ] 93疾病全データ統合
- [ ] 293漢方処方データベース統合
- [ ] グラフ・ビジュアライゼーション追加
- [ ] モバイルアプリ化

---

## 🎯 開発状況

**完成度**: 75%  
**次のステップ**: デプロイ → Bill Gates氏へメール送信

---

_Last Updated: 2026-03-22_
_Version: 2.0.0_
