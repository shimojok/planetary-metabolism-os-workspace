# MBT漢方体系図（Master Map）

---

## 1. 全体構造（6層モデル）

[Layer 1] 生薬（38）
      ↓
[Layer 2] MBT55代謝経路（7）
      ↓
[Layer 3] 生成代謝物クラスター（14）
      ↓
[Layer 4] 薬理作用（代謝物ベース）
      ↓
[Layer 5] 証（補気・活血・清熱・利水・補血・温陽）
      ↓
[Layer 6] 症状・社会的適応（12）


---

## 2. 代謝物 × 証 × 症状（Mermaid）

```mermaid
graph LR
    SCFA[SCFA<br/>短鎖脂肪酸]
    Vaso[血管拡張代謝物]
    AntiInflam[抗炎症フラボノイド]
    AntiAllergy[抗アレルギー代謝物]
    Mucosa[粘膜修復代謝物]
    DiureticM[利水関連代謝物]
    WarmM[温陽関連代謝物]

    HoKi[補気]
    Kakketsu[活血]
    Seinetu[清熱]
    Risui[利水]
    Onyo[温陽]
    Wakai[和解]

    Fatigue[疲労]
    Maternal[母子健康]
    MetS[生活習慣病]
    Coldness[冷え]
    Dysmen[月経痛]
    Infection[感染症]
    Allergy[アレルギー]
    GI[胃腸障害]
    Edema[むくみ]
    Neuro[自律神経]

    SCFA --> HoKi
    Vaso --> Kakketsu
    AntiInflam --> Seinetu
    AntiAllergy --> Seinetu
    Mucosa --> Wakai
    DiureticM --> Risui
    WarmM --> Onyo

    HoKi --> Fatigue
    HoKi --> Maternal
    HoKi --> MetS

    Kakketsu --> Coldness
    Kakketsu --> Dysmen
    Kakketsu --> MetS

    Seinetu --> Infection
    Seinetu --> Allergy
    Seinetu --> MetS

    Wakai --> GI
    Wakai --> Neuro

    Risui --> Edema
    Risui --> MetS

    Onyo --> Coldness
    Onyo --> Neuro
```