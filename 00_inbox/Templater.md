80を超えるファイルをまとめています。まず、メタデータTemplate を作成してください。

---

了解しました！メタデータTemplateを作成します。

まず、あなたのプロジェクトに最適化したメタデータTemplateを設計しましょう。

## **📋 メタデータ設計**

80を超えるファイルを見て、以下のようなメタデータ構造を提案します：

---

## **🎯 Templater テンプレート集（完全版）**

以下のテンプレートファイルを作成してください。すべて**コピペするだけ**です。

### **テンプレート1: 基本テンプレート（最頻度使用）**

**ファイル名**: `Templates/01-基本テンプレート.md`

```
---
title: <% tp.file.title %>
status: 草案
platform: 
priority: 中
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags: []
---

# <% tp.file.title %>

## 概要


## 内容


## 関連ドキュメント
- [[]]

---
*最終更新: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
```

---

### **テンプレート2: プラットフォーム別（選択式・推奨）**

**ファイル名**: `Templates/02-プラットフォームテンプレート.md`

```
---
title: <% tp.file.title %>
status: <% tp.system.suggester(["草案", "開発中", "レビュー中", "完了"], ["草案", "開発中", "レビュー中", "完了"]) %>
platform: <% tp.system.suggester(["MBT55", "AGRIX", "HealthBook", "PBPE", "Carbon", "統合", "その他"], ["MBT55", "AGRIX", "HealthBook", "PBPE", "Carbon", "統合", "その他"]) %>
priority: <% tp.system.suggester(["高", "中", "低"], ["高", "中", "低"]) %>
type: <% tp.system.suggester(["設計", "実装", "ドキュメント", "API", "スキーマ"], ["design", "implementation", "documentation", "api", "schema"]) %>
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags: []
---

# <% tp.file.title %>

## 📋 概要


## 🎯 目標


## 🔧 技術スタック
- **言語**: Python 3.11+
- **データ形式**: JSON
- **フレームワーク**: 

## ✅ 実装状況
- [ ] 基本設計
- [ ] コア実装
- [ ] テスト
- [ ] ドキュメント化
- [ ] GitHub統合

## 🔗 関連ドキュメント
- [[]]

## 📝 メモ


---
*作成: <% tp.date.now("YYYY-MM-DD") %> | 更新: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
```

---

### **テンプレート3: MBT55専用**

**ファイル名**: `Templates/03-MBT55テンプレート.md`

```markdown
---
title: <% tp.file.title %>
status: <% tp.system.suggester(["草案", "開発中", "レビュー中", "完了"], ["草案", "開発中", "レビュー中", "完了"]) %>
platform: MBT55
subsystem: <% tp.system.suggester(["代謝ライブラリー", "ハイパーサイクル", "M³-BioSynergy", "Probiotics", "JSON/Pythonエンジン"], ["metabolic-library", "hypercycle", "biosynergy", "probiotics", "engine"]) %>
priority: <% tp.system.suggester(["高", "中", "低"], ["高", "中", "低"]) %>
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags: [mbt55, metabolism]
---

# <% tp.file.title %>

## 📋 概要


## 🧬 代謝パスウェイ関連


## 🔄 ハイパーサイクル統合


## 💻 実装
### JSONスキーマ


### Pythonコード


## 🔗 関連ドキュメント
- [[MBT55代謝ライブラリー]]
- [[ハイパーサイクル]]
- [[]]

## 📝 メモ


---
*MBT55 Platform | 作成: <% tp.date.now("YYYY-MM-DD") %>*
```

---

### **テンプレート4: AGRIX専用**

**ファイル名**: `Templates/04-AGRIXテンプレート.md`

```markdown
---
title: <% tp.file.title %>
status: <% tp.system.suggester(["草案", "開発中", "レビュー中", "完了"], ["草案", "開発中", "レビュー中", "完了"]) %>
platform: AGRIX
subsystem: <% tp.system.suggester(["AgriWare", "SafetyChain", "土壌分析", "作物モニタリング", "微生物統合"], ["agriware", "safetychain", "soil", "crop", "microbiome"]) %>
priority: <% tp.system.suggester(["高", "中", "低"], ["高", "中", "低"]) %>
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags: [agrix, agriculture]
---

# <% tp.file.title %>

## 📋 概要


## 🌾 農業システム統合


## 🔬 フェノタイピング


## 🦠 微生物連携


## 💻 実装


## 🔗 関連ドキュメント
- [[AGRIX Platform 2.0]]
- [[AgriWare]]
- [[SafetyChain]]
- [[]]

## 📝 メモ


---
*AGRIX Platform | 作成: <% tp.date.now("YYYY-MM-DD") %>*
```

---

### **テンプレート5: HealthBook専用**

**ファイル名**: `Templates/05-HealthBookテンプレート.md`

```markdown
---
title: <% tp.file.title %>
status: <% tp.system.suggester(["草案", "開発中", "レビュー中", "完了"], ["草案", "開発中", "レビュー中", "完了"]) %>
platform: HealthBook
subsystem: <% tp.system.suggester(["HB5統合", "MBT Probiotics", "個別化医療", "データ統合", "API"], ["hb5", "probiotics", "personalized", "integration", "api"]) %>
priority: <% tp.system.suggester(["高", "中", "低"], ["高", "中", "低"]) %>
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags: [healthbook, healthcare]
---

# <% tp.file.title %>

## 📋 概要


## 🏥 ヘルスケア統合


## 🦠 MBT Probiotics連携


## 👤 個別化医療エンジン


## 💻 実装


## 🔗 関連ドキュメント
- [[HB5 HealthBook Platform]]
- [[MBT Probiotics]]
- [[]]

## 📝 メモ


---
*HealthBook Platform | 作成: <% tp.date.now("YYYY-MM-DD") %>*
```

---

### **テンプレート6: 炭素隔離専用**

**ファイル名**: `Templates/06-炭素隔離テンプレート.md`

```markdown
---
title: <% tp.file.title %>
status: <% tp.system.suggester(["草案", "開発中", "レビュー中", "完了"], ["草案", "開発中", "レビュー中", "完了"]) %>
platform: Carbon
subsystem: <% tp.system.suggester(["MBT55統合", "土壌炭素", "測定", "モデリング", "検証"], ["mbt-integration", "soil-carbon", "measurement", "modeling", "verification"]) %>
priority: <% tp.system.suggester(["高", "中", "低"], ["高", "中", "低"]) %>
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags: [carbon, climate, sequestration]
---

# <% tp.file.title %>

## 📋 概要


## 🌍 炭素隔離戦略


## 🔬 MBT55統合


## 📊 測定・検証


## 💻 実装


## 🔗 関連ドキュメント
- [[MBT55と炭素隔離]]
- [[PBPE]]
- [[]]

## 📝 メモ


---
*Carbon Sequestration | 作成: <% tp.date.now("YYYY-MM-DD") %>*
```

---

### **テンプレート7: 財団向けドキュメント**

**ファイル名**: `Templates/07-財団向けテンプレート.md`

```markdown
---
title: <% tp.file.title %>
status: <% tp.system.suggester(["草案", "レビュー中", "最終版"], ["草案", "レビュー中", "最終版"]) %>
target: <% tp.system.suggester(["Bill & Melinda Gates Foundation", "Rockefeller Foundation", "World Bank", "複数財団"], ["gates-foundation", "rockefeller", "world-bank", "multiple"]) %>
document-type: <% tp.system.suggester(["エグゼクティブサマリー", "技術ドキュメント", "インパクトレポート", "プレゼンテーション", "提案書"], ["executive-summary", "technical", "impact-report", "presentation", "proposal"]) %>
priority: 高
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags: [foundation, presentation, funding]
---

# <% tp.file.title %>

## 🎯 エグゼクティブサマリー


## 🌍 問題提起
### グローバルな課題


### 現状のギャップ


## 💡 提案ソリューション
### プラットフォーム概要
#### MBT55: 代謝・微生物共生システム


#### AGRIX: 持続可能農業プラットフォーム


#### HealthBook: 個別化ヘルスケア


#### 炭素隔離統合


### 統合アプローチ


## 📊 期待されるインパクト
### 健康


### 農業・食料安全保障


### 環境・気候変動


### 経済


## 🗺️ 実装ロードマップ
### Phase 1: プロトタイプ (6ヶ月)


### Phase 2: パイロット展開 (12ヶ月)


### Phase 3: スケールアップ (24ヶ月)


## 💰 予算試算


## 🤝 パートナーシップ機会


## 📈 成功指標 (KPI)


## 🔗 関連リソース
- [[技術アーキテクチャ]]
- [[科学的根拠]]
- [[]]

---
*Target: <% tp.system.prompt("対象財団", "Gates Foundation") %> | 作成: <% tp.date.now("YYYY-MM-DD") %>*
```

---

### **テンプレート8: Claude依頼用**

**ファイル名**: `Templates/08-Claude依頼テンプレート.md`

```markdown
---
title: <% tp.file.title %>
type: claude-request
platform: <% tp.system.suggester(["MBT55", "AGRIX", "HealthBook", "Carbon", "統合", "その他"], ["MBT55", "AGRIX", "HealthBook", "Carbon", "統合", "その他"]) %>
request-type: <% tp.system.suggester(["コード生成", "ドキュメント作成", "リファクタリング", "統合", "レビュー"], ["code-generation", "documentation", "refactoring", "integration", "review"]) %>
status: <% tp.system.suggester(["依頼中", "作業中", "レビュー", "完了"], ["requested", "in-progress", "review", "completed"]) %>
priority: <% tp.system.suggester(["高", "中", "低"], ["高", "中", "低"]) %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
tags: [claude, ai-generated]
---

# 🤖 Claude依頼: <% tp.file.title %>

## 📅 依頼日時
<% tp.date.now("YYYY年MM月DD日 HH:mm") %>

## 📋 依頼内容
### 目的


### 具体的な要件


## 📎 参照ドキュメント
- [[]]
- [[]]

## ✅ 期待する成果物
- [ ] Pythonコード
- [ ] JSONスキーマ
- [ ] ドキュメント
- [ ] テストコード
- [ ] その他: 

## 🔧 技術要件
- **言語**: Python 3.11+
- **フレームワーク**: 
- **ライブラリ**: 
- **データ形式**: JSON

## 💻 生成されたコード
```python
# ここにコードを貼り付け
```

## 📄 生成されたドキュメント


## ✏️ レビュー・修正依頼


## 📝 メモ・追加質問


## ✅ 完了チェックリスト
- [ ] コード動作確認
- [ ] ドキュメント整合性確認
- [ ] GitHubへ統合
- [ ] 関連ドキュメント更新

---
*依頼者: Kaz Shimojo | Claude Project: Planetary-Metabolism-OS*
*作成: <% tp.date.now("YYYY-MM-DD HH:mm") %> | 状態: <%= tp.frontmatter.status %>*
```

---

## **📦 セットアップ手順**

### **Step 1: Templaterインストール**

1. Obsidian **設定** (⚙️) → **コミュニティプラグイン**
2. **「制限モードをオフ」** にする
3. **「閲覧」** → `Templater` を検索
4. **インストール** → **有効化**

### **Step 2: テンプレートフォルダ作成**

1. Obsidian Vaultのルートに **`Templates`** フォルダを作成
2. Templater設定を開く
   - **設定** → **Templater** → **Template folder location**
   - `Templates` と入力

### **Step 3: テンプレートファイル作成**

上記の **8つのテンプレート** を `Templates` フォルダ内に作成：

```
Templates/
├── 01-基本テンプレート.md
├── 02-プラットフォームテンプレート.md
├── 03-MBT55テンプレート.md
├── 04-AGRIXテンプレート.md
├── 05-HealthBookテンプレート.md
├── 06-炭素隔離テンプレート.md
├── 07-財団向けテンプレート.md
└── 08-Claude依頼テンプレート.md
```

### **Step 4: 使い方**

1. **新規ノート作成**
2. **`Ctrl/Cmd + P`** (コマンドパレット)
3. **`Templater: Insert Template`** と入力
4. **テンプレート選択**
5. **選択肢が出たらクリック**
6. **完成！**

---

## **🎯 次のステップ**

1. **今すぐ**: 上記8つのテンプレートをコピペしてTemplatesフォルダに保存
2. **テスト**: 1つ新規ノートで試してみる
3. **80ファイルアップロード準備**: ZIPにまとめる
4. **既存ファイルへのメタデータ追加**: 私がスクリプトを作成

**準備できましたか？次は80ファイルのアップロードに進みましょうか？**

それとも、テンプレートのカスタマイズが必要ですか？