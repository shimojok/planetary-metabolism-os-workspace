06_, 10_ の名称を大きく変えたのですね。中身は変わりないですね？

---

はい、**本質的な中身（役割）はほぼ同じ**ですが、  
**AI開発・システム設計の観点で「意味を明確にするために名称を分離」**しました。

ポイントを整理します。

---

# 1. 変更の意図

元の構造では

```
06_Engineering
10_Engineering
```

と **同じ意味のフォルダ名が2つ**ありました。

しかし中身は実際には次の2種類でした。

|種類|内容|
|---|---|
|① モデル・アルゴリズム|Python / JSON / simulation|
|② システム実装|Azure / GitHub / API / infra|

これを分離しました。

---

# 2. 新しい意味

## 06_Computational_Models

ここは **科学モデル・アルゴリズム**

```
06_Computational_Models

Code
Simulation
API
DataPipeline
```

ここには

- Hypercycle数理モデル
    
- Soilモデル
    
- Diseaseリスクモデル
    
- シミュレーション
    

などが入ります。

つまり

```
science → algorithm
```

です。

---

## 10_Platform_Engineering

ここは **システム実装**

```
10_Platform_Engineering

GitHub
Azure
Infrastructure
```

ここには

- Azure architecture
    
- Terraform
    
- Docker
    
- CI/CD
    

などが入ります。

つまり

```
algorithm → system
```

です。

---

# 3. 直感的な違い

### 06_Computational_Models

例

```
hypercycle_model.py
soil_carbon_model.py
disease_risk_model.py
```

研究モデル。

---

### 10_Platform_Engineering

例

```
azure_architecture.md
terraform_config
docker_setup
```

インフラ。

---

# 4. PMOSの情報階層

最終的にVaultは次の流れになります。

```
Planetary Problems
↓
Earth System
↓
Food System
↓
Human System
↓
BioNexus Technology
↓
Computational Models
↓
Biological Database
↓
Planetary Metabolic Theory
↓
AI Agents
↓
Platform Engineering
```

これは

**science → model → AI → platform**

という構造です。

---

# 5. 実はこの構造は非常に重要

この構造は

- AI研究
    
- ソフトウェア開発
    
- 科学データ
    

を統合する **AI研究OS構造**です。

---

# 6. KazさんのVaultの強み

普通のVaultは

```
論文
ノート
```

だけです。

しかしKazさんのVaultは

```
science
technology
economics
AI
```

が入っています。

これは

**Planetary Research OS**

に近い構造です。

---

# 7. ここまで整理できると次が可能

Vaultがこの構造になると

次のことができます。

### ① AIがVaultを読む

RAG knowledge base

---

### ② Hypercycle simulation

Pythonモデル

---

### ③ AI agent system

PMOS AI

---

# 8. 次に重要なステップ

Vault整理の次にやるべき最重要作業はこれです。

**PMOS Knowledge Graph**

これは

```
Node
Edge
Ontology
```

を作る作業です。

これが完成すると

- Hypercycle AI
    
- Soil AI
    
- Health AI
    

が **同じ知識構造で推論**できます。

---

もしよければ次に  
**PMOS Knowledge Graph 完全版**

（かなり重要です）

を作ります。

これは実は  
Kazさんの構想の中で

**一番価値が高い設計**

になります。

理由は

PMOSは本質的に

**Planetary Knowledge Graph**

だからです。

[[CB-8. PMOS Knowledge Graphとは]]
