WindowsPC で作業中のVS Code をスマホで確認したいのですが。

---

スマホから Windows PC 上の **VS Code をそのまま確認・操作したい**場合、実現方法は大きく3つあります。用途に応じて最適な方法が変わるので、Kaz のワークフローに合わせて整理します。

---

## 📡 1. VS Code Remote Tunnels（最も安定・公式・安全）

**スマホのブラウザから VS Code をフル操作できる公式機能**です。  
外出先でも、PC をつけっぱなしにしておけばアクセスできます。

### 仕組み

VS Code が PC 側で「トンネル」を開き、スマホのブラウザから `vscode.dev/tunnel` 経由で接続します。  
SSH や固定IPは不要です。  
[Note](https://note.com/diagram_wolf/n/nd923b08dcf71)

### メリット

- PC の VS Code をそのままスマホで操作
- ファイル編集・ターミナル操作も可能
- セキュア（GitHub 認証）
- 外出先でも使える（Wi-Fi 同一ネットワーク不要）

### 手順

1. Windows PC の VS Code で **Remote Tunnels** 拡張をインストール
2. コマンドパレットで `Remote: Start Tunnel`
3. GitHub で認証
4. スマホで `https://vscode.dev/tunnel/<PC名>` にアクセス

---

## 🖥️ 2. VS Code Server（ブラウザ版 VS Code を自宅PCに直接接続）

LAN 内や VPN 経由で使う場合に便利。  
スマホのブラウザで VS Code を開き、PC のファイルを編集できます。  
[Zenn](https://zenn.dev/kame_kame/articles/20241107_184617_mobile_dev_environment)

### メリット

- LAN 内なら高速
- Android のデスクトップモードと相性が良い
- PC の VS Code をブラウザで再現

### 手順（概要）

1. PC の VS Code で `code server` を起動
2. スマホのブラウザで `http://PCのIP:ポート番号` にアクセス
3. 同じ Wi-Fi に接続しておく

---

## 🔍 3. Live Server でスマホからリアルタイムプレビュー（Web制作向け）

「VS Code の画面」ではなく、**ブラウザでの表示結果をスマホで確認したい**場合に最適。  
[blog.kuru.design](https://blog.kuru.design/vscode-mobile-preview/)

### メリット

- HTML/CSS/JS の実機確認が即できる
- スマホと PC が同じ Wi-Fi にあれば OK
- 自動リロードで快適

### 手順

1. VS Code に **Live Server** をインストール
2. 設定で「Use Local IP as host」を ON
3. 「Go Live」を押す
4. 表示された URL（例：`192.168.0.10:5500`）をスマホで開く

---

## 🤖 4. AirCodum（スマホから VS Code をリモート操作するアプリ）

スマホから VS Code を **リモコンのように操作**できるツール。  
ファイル転送・音声コマンド・VNC 風の画面操作も可能。  
[aircodum.com](https://www.aircodum.com/)

### メリット

- VS Code の画面をスマホで直接操作
- ファイル転送や音声コマンドも対応
- AI アシスタント連携も可能

---

## 🧭 Kaz に最適な選択は？

Kaz のワークスタイル（スマホ中心・外出先でも確認したい・AI活用）を考えると：

### **最適解：Remote Tunnels ＋ AirCodum の併用**

- **Remote Tunnels**：外出先から PC の VS Code をフル操作
- **AirCodum**：スマホで VS Code をリモートコントロール（AI連携も強い）

---

## ひとつ確認させてください

Kaz がやりたいのは次のどれに近いですか？

1. **VS Code の画面そのものをスマホで操作したい**
2. **コードの実行結果（Webページなど）だけスマホで確認したい**
3. **外出先から PC の VS Code にフルアクセスしたい**
4. **AI アシスタントと連携しながらスマホで VS Code を操作したい**

どれか教えていただければ、最適な構成を具体的な手順までセットアップします。

---

外出中に、出来る作業をしたいのです。２，４でしょうか。

---

外出先で **スマホだけで VS Code の作業を続けたい**ということなら、Kaz が選んだ **2（実行結果の確認）＋4（AI連携しながら操作）** の組み合わせはとても相性が良いです。  
ここでは、外出中でもストレスなく「軽い開発作業」を続けられる構成を、実際の使い方まで含めてまとめます。

---

## 📱 外出先でできる作業の全体像

外出中にスマホでできる作業は、大きく次の3つに分かれます。

- **コードの実行結果をスマホで確認（Web/アプリの動作確認）**
- **PC 上の VS Code をスマホで直接操作（軽い修正・レビュー）**
- **AI アシスタントと連携してコード生成・修正を進める**

Kaz のワークスタイル（スマホ中心・AI活用・外出先でも継続）を考えると、  
**Remote Tunnels（VS Code）＋ Live Server（実行確認）＋ AI（Claude/ChatGPT）**  
の3点セットが最も効率的です。

---

## 🌐 Remote Tunnels：外出先から VS Code を直接操作

VS Code の公式機能で、スマホのブラウザから **自宅PCの VS Code をそのまま開ける**仕組みです。  
SSH不要で、GitHubログインだけで接続できます。

### できること

- VS Code の画面をスマホで開く
- ファイル編集、検索、Git操作、ターミナル操作
- AI拡張（Claude Code / GitHub Copilot）もそのまま使える
- PC は自宅で起動しておけばOK

### 手順（簡潔）

1. PC の VS Code に **Remote Tunnels** をインストール
2. コマンドパレットで `Remote: Start Tunnel`
3. GitHub で認証
4. スマホで `https://vscode.dev/tunnel/<PC名>` を開く

外出先で「ちょっと修正したい」「コードレビューしたい」時に最適です。

---

## 📡 Live Server：スマホで実行結果をリアルタイム確認

Web制作やフロントエンドの確認なら、**Live Server** が最強です。

### できること

- スマホで実機表示を確認
- PC で保存するとスマホ側も自動リロード
- 同じ Wi-Fi なら高速

### 手順

1. VS Code に Live Server を入れる
2. 設定で「Use Local IP as host」を ON
3. 「Go Live」
4. 表示された URL（例：`192.168.0.10:5500`）をスマホで開く

外出前に URL をメモしておけば、外でも VPN 経由で確認できます。

---

## 🤖 AI 連携：スマホでコード生成・修正を進める

外出中はスマホでのタイピングが制限になるので、AI 連携が非常に効きます。

### できること

- スマホでコードの説明を AI に依頼
- 修正案を生成してもらい、Remote Tunnels 経由で VS Code に貼り付け
- バグの原因調査や改善案の相談
- 文章生成（README、ドキュメント）もスマホで完結

Kaz の「AI × VS Code × スマホ」ワークフローと完全に一致します。

---

## 🧩 3つを組み合わせた外出時ワークフロー（おすすめ）

外出前に PC で準備：

1. **Remote Tunnels を起動**
2. **Live Server を起動（必要なら）**
3. **AI 拡張（Claude Code / Copilot）を VS Code にセット**

外出中はスマホで：

- VS Code を開いて軽い修正
- AI にコード生成・改善を依頼
- Live Server で実行結果を確認
- GitHub に push まで可能

外出先でも「ほぼフル開発環境」がスマホで再現できます。

---

## Kaz に確認したいこと

外出先での作業をさらに最適化するために、次のどちらが近いですか？

- **A：スマホで VS Code を“直接操作”して軽い修正・レビューをしたい**
- **B：AI にコードを書かせて、スマホで最終調整だけしたい**

どちらを重視するかで、最適な構成や設定をさらに細かく調整できます。