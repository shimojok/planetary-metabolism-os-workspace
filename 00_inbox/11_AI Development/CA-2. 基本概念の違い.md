Google AI Studio とVS Code の全てを比較してください。

---

**Google AI Studio** と **Visual Studio Code（VS Code）** は、どちらも開発に使われるツールですが、**目的・設計思想・使用範囲が根本的に異なります**。
以下に **技術レベルで体系的に比較**します。

---

# 1. 基本概念の違い

| 項目     | Google AI Studio | VS Code       |
| ------ | ---------------- | ------------- |
| 種類     | AIモデル開発環境        | 汎用IDE（統合開発環境） |
| 主目的    | LLM / AIプロンプト開発  | ソフトウェア開発      |
| 開発主体   | Google           | Microsoft     |
| 動作     | Webブラウザ          | ローカルアプリ       |
| 対象ユーザー | AI開発者 / AI実験者    | ソフトウェアエンジニア   |

**本質**

```
Google AI Studio = AIモデル実験環境
VS Code = ソフトウェア開発環境
```

Google AI Studioは**Geminiモデルを使うための実験ラボ**として設計されています。 ([ウィキペディア][1])

---

# 2. アーキテクチャの違い

| 項目   | Google AI Studio | VS Code |
| ---- | ---------------- | ------- |
| 実行環境 | Cloud            | Local   |
| 計算資源 | Google Cloud     | 自分のPC   |
| 設定   | ほぼ不要             | 手動設定多い  |
| 拡張性  | 限定               | 非常に高い   |

### Google AI Studio

* 完全クラウド
* AIモデルはGoogle側

### VS Code

* 自分のPCで動く
* 何でも開発できる

---

# 3. 主な機能比較

| 機能        | AI Studio | VS Code |
| --------- | --------- | ------- |
| コード編集     | △         | ◎       |
| AIプロンプト設計 | ◎         | △       |
| モデルテスト    | ◎         | ×       |
| デバッグ      | △         | ◎       |
| Git       | ×         | ◎       |
| API開発     | △         | ◎       |
| アプリ開発     | △         | ◎       |

AI Studioは

* prompt
* AI agent
* LLMテスト

に特化しています。 ([remio][2])

---

# 4. AI開発機能

### Google AI Studio

可能

* Geminiモデル利用
* multimodal入力
* prompt tuning
* agent workflow

例

```
text
image
pdf
csv
```

などをAIに入力可能。 ([All About AI][3])

---

### VS Code

AI機能は**プラグイン**

例

* GitHub Copilot
* Gemini Code Assist
* ChatGPT extension

つまり

```
AI Studio = AIが中心
VS Code = AIは補助
```

---

# 5. 開発プロセス比較

### AI Studio

典型的フロー

```
prompt設計
↓
AIテスト
↓
コード生成
↓
API export
↓
Cloud deploy
```

---

### VS Code

典型的フロー

```
コード作成
↓
コンパイル
↓
デバッグ
↓
Git管理
↓
アプリ完成
```

---

# 6. 対応言語

| 言語         | AI Studio | VS Code |
| ---------- | --------- | ------- |
| Python     | ○         | ◎       |
| JavaScript | ○         | ◎       |
| C++        | ×         | ◎       |
| Rust       | ×         | ◎       |
| Go         | ×         | ◎       |
| Java       | ×         | ◎       |

AI Studioは**ほぼPython / JS生成のみ**です。

---

# 7. 開発範囲

| 分野     | AI Studio | VS Code |
| ------ | --------- | ------- |
| LLM    | ◎         | ○       |
| Webアプリ | △         | ◎       |
| モバイル   | ×         | ◎       |
| OS開発   | ×         | ◎       |
| AI研究   | ◎         | ○       |

---

# 8. UIの違い

### Google AI Studio

画面

```
Prompt editor
↓
Model selection
↓
Temperature / TopP
↓
Output
```

AI研究向けUI。

---

### VS Code

画面

```
Explorer
Editor
Terminal
Debugger
Git
Extensions
```

完全IDE。

---

# 9. スケーラビリティ

| 項目     | AI Studio | VS Code |
| ------ | --------- | ------- |
| 大規模コード | ×         | ◎       |
| チーム開発  | △         | ◎       |
| CI/CD  | ×         | ◎       |
| DevOps | ×         | ◎       |

AI Studioは**本番開発向きではない**です。 ([All About AI][3])

---

# 10. AI能力

| 機能          | AI Studio   | VS Code |
| ----------- | ----------- | ------- |
| LLM context | 最大100万token | AI依存    |
| multimodal  | ◎           | △       |
| agent       | ○           | △       |
| reasoning   | ◎           | △       |

Gemini 2.5 Pro
→ **100万token context** ([All About AI][3])

---

# 11. コスト

| 項目 | AI Studio    | VS Code   |
| -- | ------------ | --------- |
| 本体 | 無料           | 無料        |
| AI | API課金        | AIプラグイン課金 |
| 計算 | Google Cloud | 自分のPC     |

---

# 12. セキュリティ

| 項目    | AI Studio | VS Code |
| ----- | --------- | ------- |
| データ保存 | Cloud     | Local   |
| 機密コード | △         | ◎       |
| オフライン | ×         | ◎       |

---

# 13. 実際の開発フロー（現代AI開発）

多くのAI開発者はこう使います

```
1 Google AI Studio
   ↓
2 Python code export
   ↓
3 VS Code
   ↓
4 GitHub
   ↓
5 Cloud deployment
```

---

# 14. 最重要の違い

**Google AI Studio**

目的

```
AIモデルの実験
```

**VS Code**

目的

```
ソフトウェア開発
```

---

# 15. 一言で言うと

```
Google AI Studio = AI研究ラボ
VS Code = ソフトウェア工場
```

---

もしよろしければ次に
**AI開発者が使う「AI開発ツール全体マップ」**

（かなり重要です）

```
AI Studio
VS Code
Cursor
Claude Code
Jupyter
Colab
Vertex AI
```

これを**1枚の構造図**で説明できます。
AI開発の理解が一気に進みます。

[1]: https://en.wikipedia.org/wiki/Google_AI_Studio?utm_source=chatgpt.com "Google AI Studio"
[2]: https://www.remio.ai/post/google-ai-studio-a-free-web-ide-to-prototype-prompt-and-build-with-gemini-s-multimodal-ai-models?utm_source=chatgpt.com "Google AI Studio: A Free Web IDE to Prototype, Prompt, and Build with Gemini’s Multimodal AI Models"
[3]: https://www.allaboutai.com/ai-reviews/google-ai-studio/?utm_source=chatgpt.com "Google AI Studio Review: Why Everyone's Talking About It?"


[[CA-3. 結論（Obsidianユーザー視点）]]

