AIエージェントは何を使うのでしょうか?

---

BioNexusのように **複数プラットフォーム（AGRIX / HealthBook / MBT55）を統合するAIエージェント**を構築する場合、単一ツールではなく **AIエージェントフレームワーク + LLM + API基盤**の組み合わせになります。
まず結論から整理します。

---

# 1. BioNexusに最も適したAIエージェント構成（結論）

現時点で最も合理的な構成は

```text
LangGraph
 + Python
 + LLM API
 + FastAPI
 + Vector Database
```

です。


☛ [[AIエージェント構成]]

理由
BioNexusは

* マルチエージェント
* 長期状態管理
* データフロー連携
* 科学モデル

が必要だからです。

---

# 2. AIエージェントフレームワーク比較

| フレームワーク           | 特徴              | 適合度   |
| ----------------- | --------------- | ----- |
| LangGraph         | 状態管理・マルチエージェント  | ⭐⭐⭐⭐⭐ |
| CrewAI            | 役割型エージェント       | ⭐⭐⭐⭐  |
| AutoGen           | Microsoft系マルチAI | ⭐⭐⭐   |
| Semantic Kernel   | Azure連携         | ⭐⭐⭐   |
| OpenAI Agents SDK | シンプル            | ⭐⭐    |

---

# 3. 最有力：LangGraph

LangGraphは

```text
AIエージェントのワークフローエンジン
```

です。

特徴

```text
状態管理
マルチエージェント
ツール接続
長期タスク
```

構造

```text
Agent
 ↓
Graph
 ↓
Workflow
```

---

# 4. BioNexusエージェント構造

BioNexusでは **4エージェント構造**が理想です。

```text
                 System Agent
                       │
       ┌───────────────┼───────────────┐
       │               │               │
 AGRIX Agent     HealthBook Agent   MBT Agent
```

---

### AGRIX Agent

機能

```text
土壌分析
作物最適化
炭素固定モデル
```

入力

```text
soil microbiome
climate
crop data
```

---

### HealthBook Agent

機能

```text
疾病リスク評価
栄養解析
フェノタイプ分析
```

入力

```text
phenotype
diet
microbiome
```

---

### MBT Agent

機能

```text
腸内微生物解析
発酵食品分析
プロバイオティクス設計
```

---

### System Agent

機能

```text
全体統合
Planetary metabolism
シミュレーション
```

---

# 5. 技術スタック

推奨構成

```text
Language
Python
```

```text
Agent Framework
LangGraph
```

```text
API
FastAPI
```

```text
Database
PostgreSQL
```

```text
Vector DB
Qdrant
Weaviate
Pinecone
```

---

# 6. AIモデル

エージェントはLLMを使います。

代表

* OpenAI GPT
* Anthropic Claude
* Gemini

多くのAIシステムでは

```text
Reasoning → Claude
Tool use → GPT
Data → Gemini
```

のように併用します。

---

# 7. GitHub構造

AIエージェントをGitHubに作る場合

```text
bionexus-ai
│
├ agents
│   ├ agrix-agent
│   ├ health-agent
│   └ microbiome-agent
│
├ models
│   ├ hypercycle
│   ├ soil-carbon
│   └ disease-risk
│
├ data
│
└ api
```

---

# 8. エージェント動作フロー

BioNexusでは次の循環になります。

```text
Soil data
 ↓
AGRIX agent
 ↓
Food nutrient data
 ↓
MBT agent
 ↓
Human microbiome
 ↓
HealthBook agent
 ↓
Health prediction
 ↓
System agent
 ↓
Agriculture optimization
```

つまり

```text
Soil → Food → Human → Soil
```

という代謝循環です。

---

# 9. Azureとの関係

KazさんのAzure構想なら

```text
Azure OpenAI
Azure Container Apps
Azure Data Lake
```

と接続します。

---

# 10. AIエージェントの完成形

BioNexusの場合、最終的には

```text
Planetary Metabolic AI
```

になります。

統合対象

```text
Soil microbiome
Agriculture
Food
Human microbiome
Health
Climate
```

つまり

**Planetary Digital Twin**です。

---

もしよければですが、
実はBioNexusのような構造では **もう一段重要な設計**があります。

それは

**「AIエージェントのメモリ構造」**☛

です。

これを設計すると

* HealthBook
* MBT55
* AGRIX

が **同じ知識ベースで動くAI**になります。
ここがAIシステムの核心なので、必要なら **具体的な設計図**を作ります。


[[CA-10. AIエージェントフレームワーク]]
