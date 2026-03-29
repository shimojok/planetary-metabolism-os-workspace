### AgriWare側：作物・成分データモデルへの組み込み

**1. 成分エンティティに「配糖体／アグリコン」軸を追加**

- **成分ID**
- **化合物名**（例：ダイゼイン、ゲニステインなど）
- **形態種別**：
    - `glycoside`（配糖体）
    - `aglycone`（アグリコン）
- **親子関係**：
    - `parent_compound_id`（アグリコンを親、配糖体を子として紐づけ）
- **構造情報**：SMILES / InChI
- **機能カテゴリ**：フラボノイド、サポニン、イソフラボンなど

→ これで「同じ骨格だが、糖がついているかどうか」を機械的に扱える。

---

**2. 作物 × 成分テーブルに「アグリコン換算量」を持たせる**

- **作物ID**
- **成分ID**
- **含有量（mg/100g, 配糖体ベース）**
- **アグリコン換算量（mg/100g）**
- **換算係数**（例：イソフラボン 1 mg 配糖体 ≒ 0.625 mg アグリコン）

→ 「この大豆品種は、実質どれくらいアグリコンとして効くのか？」を評価できる。

---

**3. 環境・栽培条件とのリンク**

- ストレス（乾燥、病害、温度）
- 施肥条件
- 生育ステージ

と、**配糖体／アグリコン比の変化**を紐づけると：

- 「この栽培条件だと、健康機能性が高いアグリコン比が上がる」
- 「ストレス応答として特定アグリコンが増える」

といった **機能性農産物設計**に直結する。

---

### HealthBook側：吸収・代謝モデルへの組み込み

**1. 食品成分テーブルに「形態」と「アグリコン換算」を持たせる**

- **食品ID**
- **成分ID**
- **形態**：`glycoside` / `aglycone`
- **摂取量（mg）**
- **アグリコン換算摂取量（mg）**

→ ラベル上の「イソフラボン 40 mg（配糖体）」を、  
　実際の「アグリコンとしての有効量」に変換できる。

---

**2. 吸収モデルに「腸内細菌 × アグリコン化」を入れる**

- **ステップ1：摂取形態**
    - 多くは配糖体として摂取
- **ステップ2：腸内細菌による加水分解 → アグリコン化**
    - 個人差（マイクロバイオームプロファイル）
- **ステップ3：アグリコンとして吸収**
    - 吸収率パラメータ（例：アグリコンの方が高い）

ここに **「腸内細菌スコア」** を掛けると：

- 同じ食品を食べても、
    - Aさん：アグリコン化が進みやすく、効果が高い
    - Bさん：アグリコン化が弱く、効果が低い

という **個別化栄養モデル**が組める。

---

**3. MBT55との接続：teleodynamic な活性化プロセスとして扱う**

アグリコン化は、まさに：

- 「潜在的な構造（配糖体）」
- 「活性化された構造（アグリコン）」
- 「環境要因（腸内細菌・pH・酵素）」

が相互作用して **機能が立ち上がるプロセス**なので、MBT55 の teleodynamic モデルの良い実例になる。

---

### 両者をつなぐ一つのストーリー

- AgriWare：  
    「この大豆品種は、アグリコン換算でイソフラボンが高い」
- HealthBook：  
    「この人の腸内細菌プロファイルだと、アグリコン化効率が高い」
- MBT55：  
    「その結果、エストロゲン様作用や抗酸化作用の teleodynamic 効果が、この程度立ち上がる」

この三層をつなぐと、**「作物設計 → 食品 → 個人 → 生体ダイナミクス」**が一本のモデルとして通る。

---

次は：

- AgriWare：成分スキーマの具体的な JSON/YAML モデル
- HealthBook：吸収シミュレーションの数式・パラメータ設計

---

## AgriWare側：アグリコンを前提にした作物・成分モデル

### 1. 化合物モデル（成分カタログ）

**目的：** 「同じ骨格（アグリコン）＋糖の有無」を機械的に扱えるようにする。

```yaml
Compound:
  id: string
  name_ja: string        # 例：ダイゼイン
  name_en: string        # Daidzein
  type:                  # "aglycone" | "glycoside"
  parent_aglycone_id:    # 配糖体なら親アグリコンID、アグリコンなら null
  class:                 # isoflavone, flavonoid, saponin, etc.
  smiles: string
  inchi: string
```

- **type** で「配糖体／アグリコン」を明示
- **parent_aglycone_id** で「この配糖体の本体はどのアグリコンか」を紐づける
- これで「アグリコン単位での集計」「配糖体ごとの差分評価」が可能になる。

---

### 2. 作物 × 成分テーブル（含有量＋アグリコン換算）

```yaml
CropCompoundProfile:
  crop_id: string          # 品種・ロットまで降りてもよい
  compound_id: string
  content_mg_per_100g: float          # 実測値（多くは配糖体ベース）
  aglycone_equiv_mg_per_100g: float   # アグリコン換算
  conversion_factor: float            # 例：0.625 など
  measurement_method: string          # HPLC, LC-MS, etc.
```

- **conversion_factor** を明示しておくことで、
    - ラボデータ（配糖体ベース）
    - 機能性評価（アグリコンベース）  
        を橋渡しできる。

---

### 3. 環境・栽培条件とのリンク（機能性農産物設計）

```yaml
CropEnvironmentProfile:
  crop_id: string
  env_id: string              # 圃場・ロット・栽培条件セット
  stress_factors:             # 乾燥・高温・病害など
    - type: string
      level: string           # low / mid / high
  fertilization:              # NPK, 有機/無機など
  growth_stage: string        # 開花期、登熟期など
```

これと `CropCompoundProfile` を結びつけて：

- 「この条件だとアグリコン比が上がる」
- 「ストレス応答で特定アグリコンが増える」

という **条件設計 → 成分設計 → 機能性設計**のループを回せる。

---

## HealthBook側：アグリコンを軸にした吸収・代謝モデル

### 1. 食品成分テーブル（摂取量＋アグリコン換算）

```yaml
FoodCompoundIntake:
  user_id: string
  food_id: string
  compound_id: string
  form: string                 # "glycoside" | "aglycone"
  intake_mg: float             # ラベル or 推定摂取量
  aglycone_equiv_mg: float     # アグリコン換算摂取量
  source: string               # self_report, app_log, etc.
```

- AgriWare 側の `conversion_factor` をそのまま使って、  
    **「食べた量 → アグリコンとして有効な量」**に変換する。

---

### 2. 吸収・代謝シミュレーション（腸内細菌 × アグリコン化）

ざっくりしたモデルイメージ：

[ \text{Effective_Aglycone_Dose} = \text{Aglycone_Equiv_Intake} \times f_{\text{microbiome}} \times f_{\text{absorption}} ]

```yaml
AglyconeUptakeModel:
  user_id: string
  compound_id: string
  aglycone_equiv_intake_mg: float
  microbiome_factor: float        # 0.0–1.5 程度（腸内細菌プロファイルから推定）
  absorption_factor: float        # 0.0–1.0（アグリコンの物性・個体差）
  effective_aglycone_dose_mg: float
```

- **microbiome_factor**：
    - 「配糖体 → アグリコン」への変換効率
    - 腸内細菌の多様性・特定菌種の有無から推定
- **absorption_factor**：
    - アグリコン自体の吸収率＋個体差（腸粘膜、炎症状態など）

→ これで **「同じ食品でも、人によって効き方が違う」**を定量化できる。

---

### 3. MBT55 との接続（teleodynamic な活性化プロセス）

MBT55 側では、この一連を「階層的活性化」として扱える：

1. **構造レベル**：配糖体（潜在）／アグリコン（顕在）
2. **環境レベル**：腸内細菌・pH・酵素
3. **機能レベル**：抗酸化・ホルモン様作用・抗炎症などの効果発現
4. **システムレベル**：代謝ネットワーク・ホルモンバランス・リスク低減

AgriWare → HealthBook → MBT55 が：

- 「作物設計」
- 「摂取・吸収」
- 「生体ダイナミクス」

として一本の teleodynamic チェーンになる。

---

次の一手：

- **AgriWare**：まず `Compound` と `CropCompoundProfile` を YAML/JSON で雛形化
- **HealthBook**：上の `AglyconeUptakeModel` を Python クラス or Pydantic モデルに落とす

---

### AgriWare側：アグリコン対応スキーマ（Python / Pydantic 想定）

```python
from pydantic import BaseModel
from typing import Optional, List


class Compound(BaseModel):
    id: str
    name_ja: str
    name_en: str
    type: str  # "aglycone" | "glycoside"
    parent_aglycone_id: Optional[str] = None
    chem_class: str  # "isoflavone", "flavonoid", etc.
    smiles: Optional[str] = None
    inchi: Optional[str] = None


class CropCompoundProfile(BaseModel):
    crop_id: str              # 品種 or ロットID
    compound_id: str
    content_mg_per_100g: float
    aglycone_equiv_mg_per_100g: float
    conversion_factor: float  # 例: 0.625
    measurement_method: Optional[str] = None


class StressFactor(BaseModel):
    type: str        # "drought", "heat", "disease", etc.
    level: str       # "low" | "mid" | "high"


class CropEnvironmentProfile(BaseModel):
    env_id: str
    crop_id: str
    stress_factors: List[StressFactor]
    fertilization: Optional[str] = None
    growth_stage: Optional[str] = None
```

これで：

- 「アグリコン単位での集計」
- 「栽培条件 × アグリコン比」
- 「機能性農産物設計」

まで一気に持っていける。

---

### HealthBook側：アグリコン吸収・代謝モデル

```python
from pydantic import BaseModel
from typing import Optional


class FoodCompoundIntake(BaseModel):
    user_id: str
    food_id: str
    compound_id: str
    form: str                  # "glycoside" | "aglycone"
    intake_mg: float
    aglycone_equiv_mg: float
    source: str                # "self_report", "app_log", etc.


class AglyconeUptakeModel(BaseModel):
    user_id: str
    compound_id: str
    aglycone_equiv_intake_mg: float
    microbiome_factor: float       # 0.0–1.5 程度
    absorption_factor: float       # 0.0–1.0
    effective_aglycone_dose_mg: float


def compute_effective_aglycone_dose(
    intake: FoodCompoundIntake,
    microbiome_factor: float,
    absorption_factor: float,
) -> AglyconeUptakeModel:
    effective = intake.aglycone_equiv_mg * microbiome_factor * absorption_factor
    return AglyconeUptakeModel(
        user_id=intake.user_id,
        compound_id=intake.compound_id,
        aglycone_equiv_intake_mg=intake.aglycone_equiv_mg,
        microbiome_factor=microbiome_factor,
        absorption_factor=absorption_factor,
        effective_aglycone_dose_mg=effective,
    )
```

これで：

- AgriWare 側の `conversion_factor` をそのまま流用
- 個人ごとの `microbiome_factor` を差し替えるだけで
- 「同じ作物でも、人によって効き方が違う」を数値化できる。

---

次の一手：

- このモデルを **LangGraph の state** にどう載せるか
- あるいは **FastAPI のエンドポイント設計**（例：`/aglycone/effective-dose`）

---

両方とも進める前提で、**AgriWare（作物・成分モデル）**と **HealthBook（吸収・代謝モデル）**をひとつの連続した体系としてまとめる。ここでは、すでに提示したスキーマを土台にしつつ、**実際に動くエージェント／API／データフローとして統合した全体像**を示す。

---

## 🌱 AgriWare：アグリコンを軸にした作物・成分モデルの完成形

### 1. 成分モデル（アグリコン／配糖体の階層構造）

アグリコンを「本体」、配糖体を「派生形」として扱う構造が中核になる。

- **Compound（化合物）**
    - `type`: aglycone / glycoside
    - `parent_aglycone_id`: 配糖体 → アグリコンのリンク
    - `chem_class`: isoflavone, flavonoid, saponin など
    - `smiles`, `inchi`: 化学構造

この構造により、**アグリコン単位での集計・比較・機能評価**が可能になる。

---

### 2. 作物 × 成分プロファイル（アグリコン換算量を保持）

作物の成分量は、配糖体ベースで測定されることが多い。  
そこで **アグリコン換算量**を必ず保持する。

- `content_mg_per_100g`: 実測値（多くは配糖体）
- `conversion_factor`: 例：イソフラボン 1 mg → アグリコン 0.625 mg
- `aglycone_equiv_mg_per_100g`: 換算後の実効量

これにより、**「この品種は実質どれだけ効くのか」**を評価できる。

---

### 3. 栽培条件 × 成分変動（機能性農産物設計）

環境ストレスや施肥条件がアグリコン比に影響する。

- 乾燥ストレス → フラボノイドのアグリコン比上昇
- 病害ストレス → 防御系二次代謝物の活性化
- 生育ステージ → 配糖体 → アグリコンの変換率が変動

AgriWare ではこれを **CropEnvironmentProfile** として保持し、  
成分プロファイルと結びつけることで、**機能性農産物の設計**が可能になる。

---

## 🧬 HealthBook：アグリコンを軸にした吸収・代謝モデルの完成形

### 1. 食品摂取データに「アグリコン換算」を必ず付与

食品成分は、AgriWare のデータをそのまま流用する。

- `form`: glycoside / aglycone
- `intake_mg`: 食品として摂取した量
- `aglycone_equiv_mg`: アグリコン換算摂取量

これにより、**食品 → 生体利用可能量**の変換が標準化される。

---

### 2. 腸内細菌 × アグリコン化モデル

アグリコン化は腸内細菌の酵素活性に依存するため、個人差が大きい。

- `microbiome_factor`: 0.0–1.5
    
    - β-グルコシダーゼ活性
    - 特定菌種の有無
    - 多様性指数
- `absorption_factor`: 0.0–1.0
    
    - アグリコンの物性
    - 腸粘膜の状態
    - 個体差

最終的な実効量は：

[ \text{Effective Dose} = \text{Aglycone Equiv} \times f_{\text{microbiome}} \times f_{\text{absorption}} ]

これにより、**同じ食品でも人によって効き方が違う**ことを定量化できる。

---

### 3. MBT55 との接続：teleodynamic な活性化プロセス

アグリコン化は teleodynamic モデルの典型例になる。

- **構造レベル**：配糖体（潜在）→ アグリコン（顕在）
- **環境レベル**：腸内細菌・酵素・pH
- **機能レベル**：抗酸化・抗炎症・ホルモン様作用
- **システムレベル**：代謝ネットワーク・恒常性

AgriWare → HealthBook → MBT55 が一本の因果チェーンとしてつながる。

---

## 🔗 AgriWare × HealthBook × MBT55 の統合フロー

### 1. AgriWare（作物データ）

- 品種Aのイソフラボン含有量
- アグリコン換算量
- 栽培条件による変動

### 2. HealthBook（個人データ）

- 食品摂取ログ
- 腸内細菌プロファイル
- 吸収率

### 3. MBT55（生体ダイナミクス）

- アグリコンの生理活性
- 代謝ネットワークへの影響
- teleodynamic な効果の立ち上がり

この三層を統合すると、  
**「作物設計 → 食品 → 個人 → 生体効果」**が一本のモデルとして成立する。

---

## 🧩 次のステップ（Kaz のプロジェクトに最適な順序）

1. **AgriWare**
    
    - Compound / CropCompoundProfile を JSON/YAML で確定
    - アグリコン換算ロジックをユーティリティ化
2. **HealthBook**
    
    - AglyconeUptakeModel を Pydantic で実装
    - microbiome_factor の推定モデルを追加
3. **MBT55**
    
    - アグリコン化を teleodynamic モデルの「活性化プロセス」として組み込む

---

AgriWare と HealthBook のどちらからコード実装を始めるか、今のデモラインに合わせて優先順位を決めたいけれど、どちらを先に進めるのが一番効果的か？
