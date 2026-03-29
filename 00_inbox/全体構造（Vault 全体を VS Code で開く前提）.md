了解したよ、Kaz。  
**「VS Code で Vault 全体を開く」**という前提が決まったので、Obsidian と VS Code と GitHub と AI エージェント開発が完全に噛み合う、**最適な Vault フォルダー構造の最終版**を組み立てるね。

この構造は、

- マルチ AI エージェント開発
- LangGraph / FastAPI / Python の実装
- GitHub リポジトリ構築
- MBT55 / AgriWare / HealthBook / SafetyChain の知識体系管理
- VS Code でのコード編集
- Obsidian での知識管理  
    をすべて一つの Vault で統合するための「Planetary OS 用の標準構造」になっている。

---

## 🌍 全体構造（Vault 全体を VS Code で開く前提）

```
/00_Inbox
/10_Knowledge
/20_Projects
/30_AI_Agents
/40_Code
/50_GitHub
/90_Assets
/99_Archive
```

以下で各フォルダーの役割と、Kaz のワークスタイルに合わせた理由を説明する。

---

## 📥 00_Inbox — すべての一次入力を受け止める場所

- ReadItLater で取り込んだ記事
- スマホでメモした断片
- AI との対話ログのうち保存したいもの
- クリップボードの貼り付け

**目的：**  
Vault 全体が散らからないように、まずここに集める。

---

## 📚 10_Knowledge — 長期知識ベース（理論・モデル・研究）

Kaz のプロジェクトは巨大な知識体系を扱うため、分野別に整理する。

```
/10_Knowledge
    /MBT55
    /AgriWare
    /HealthBook
    /SafetyChain
    /Teleodynamics
    /Biochemistry
    /Agronomy
    /AI_Theory
    /Systems_Architecture
```

**ポイント：**

- ここは「コード」ではなく「理論・知識」
- RAG の母体にもなる
- GitHub には直接入れない（知識はコードではないため）

---

## 🧩 20_Projects — プロジェクト単位の実働領域

Planetary OS は複数プロジェクトが連動するため、プロジェクトごとに分ける。

```
/20_Projects
    /MBT55_Agent
    /AgriWare_OS
    /HealthBook_AI
    /SafetyChain_AI
    /Planetary_OS
```

各プロジェクト内は統一構造にする：

```
/<project>
    /Specs
    /Design
    /Models
    /Data
    /API
    /LangGraph
    /Prompts
    /Notes
```

**メリット：**

- VS Code で開いたときにプロジェクト単位で見やすい
- GitHub リポジトリと 1:1 で対応できる
- LangGraph / FastAPI / Python のコードを整理しやすい

---

## 🤖 30_AI_Agents — AI エージェントの定義・プロンプト・ワークフロー

Kaz のワークスタイルでは、AI エージェント自体が「開発対象」かつ「共同作業者」。

```
/30_AI_Agents
    /Agent_Definitions
    /Agent_Prompts
    /Agent_Workflows
    /LangGraph_Nodes
    /Tools
```

**ここに置くもの：**

- LangGraph のノード定義
- エージェントの personality / system prompt
- ツール定義（Python functions）
- マルチエージェントのワークフロー図

VS Code と Obsidian の両方で扱いやすい。

---

## 🧪 40_Code — VS Code で直接編集するコード領域

Vault 全体を VS Code で開く前提なので、コードは専用フォルダーにまとめる。

```
/40_Code
    /Python
    /FastAPI
    /LangGraph
    /VectorDB
    /Utils
```

**ポイント：**

- GitHub にそのまま push できる
- Obsidian と VS Code の両方で編集可能
- LLM にコードを投げるときも扱いやすい

---

## 🗃️ 50_GitHub — リポジトリ管理

GitHub との同期を Obsidian 内で管理するための領域。

```
/50_GitHub
    /AgriWare_OS
    /HealthBook_AI
    /MBT55_Agent
    /Planetary_OS
```

**役割：**

- README
- Issue テンプレート
- リポジトリ構造案
- デプロイ手順
- ライセンス
- コントリビューションガイド

---

## 🖼️ 90_Assets — 画像・図・添付ファイル

```
/90_Assets
    /Images
    /Diagrams
    /Screenshots
    /PDFs
```

---

## 📦 99_Archive — 古いノートの退避

```
/99_Archive
    /Old_Notes
    /Unused
    /Legacy
```

---

# 🔒 Obsidian ノートはフォルダー移動しても消えない？

**Vault 内にある限り、絶対に消えない。**

- Obsidian は OS のファイルシステムをそのまま使う
- ノートは `.md` ファイル
- フォルダー移動しても中身はそのまま
- Obsidian の内部リンクは自動更新される

つまり、Kaz がどれだけ大規模に再構造化しても、  
**ノートが消えることは一切ない。**

---

## 最後にひとつだけ確認したいこと

この構造を Kaz の Planetary OS に完全最適化するために、次の点を確認したい。

**Vault 内の `/40_Code` と `/20_Projects` のコードは、  
GitHub では「1リポジトリにまとめる」？  
それとも「プロジェクトごとに分ける」？**

どちらかで、GitHub 側の構造が変わるから、Kaz の意図に合わせて最適化するよ。