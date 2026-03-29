### Prompt; 
昨日アップロードした300ファイル分のURLを数秒でリスト化できるそうですね？隣のスレッドで聞きました。GitHub CLIやターミナルが使える環境であれば、以下のコマンドが最も速いそうです。

昨日の私とのやり取りを思い出し、私のPC のBash環境での操作法を教えて下さい。

以下、頂いたアドバイスの内容

---
### Prompt1; 

GitHub上の.mdファイルの読み込みに関する、RAW URL リストの提供方法を教えてください。

---

### Gemini 1 ;

GitHub上のMarkdown（.md）ファイルを、レンダリングされたHTMLページとしてではなく、プレーンテキストの**RAW形式**で取得・リスト化する方法ですね。

プログラムでの一括処理や、他のドキュメントへの埋め込みに非常に便利です。主な3つの方法を整理しました。

## 1. 手動でURLを取得する（基本）

少数のファイルであれば、GitHubのUIから直接取得するのが最も確実です。

1. GitHubで対象の `.md` ファイルを開く。
    
2. ファイル表示エリアの右上にある **[Raw]** ボタンをクリック。
    
3. ブラウザのURLバーに表示されるURLをコピーする。
    

> **URLの構造例:**
> 
> `https://raw.githubusercontent.com/ユーザー名/リポジトリ名/ブランチ名/パス/ファイル名.md`

## 2. GitHub CLI / Git を使用してリストを生成する

ファイル数が多い場合、コマンドラインで一括抽出してリスト化するのが効率的です。

### ローカルのリポジトリからパスを抽出する場合

ターミナル（BashやZsh）で以下のコマンドを実行すると、RAW URLのリストを生成できます。

Bash

```
# ユーザー名、リポジトリ名、ブランチ名を定義
USER="your-username"
REPO="your-repo"
BRANCH="main"

# .mdファイルのパスを取得し、RAW URLに変換してリスト化
git ls-files | grep '\.md$' | sed "s|^|https://raw.githubusercontent.com/$USER/$REPO/$BRANCH/|" > raw_url_list.txt
```

## 3. GitHub API を使用する（動的な取得）

スクリプトなどで動的にリストを作成したい場合は、GitHub API（Contents API）を利用します。

### APIエンドポイントの例

`https://api.github.com/repos/{owner}/{repo}/contents/{path}`

**Pythonでの実装イメージ:**

Python

```
import requests

def get_raw_urls(owner, repo, path=""):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url)
    files = response.json()
    
    raw_urls = [file['download_url'] for file in files if file['name'].endswith('.md')]
    return raw_urls

# 使用例
urls = get_raw_urls("google", "googletest")
for url in urls:
    print(url)
```

### 注意点

- **プライベートリポジトリ:** プライベートなURLにアクセスするには、`?token=...` という一時的なトークンを付与するか、APIリクエスト時に `Authorization` ヘッダー（Personal Access Token）を含める必要があります。
    
- **レート制限:** APIを使用する場合、認証なしだと1時間あたり60リクエストまでという制限があります。
    
---
### Prompt 2 ;

300もの.mdファイルがあり、生成AIに読ませたいのです。

---

### Gemini 2; 

300ファイルもの膨大なドキュメントを生成AIに読み込ませる場合、手動でのコピー＆ペーストは現実的ではありません。

AI（特にAPIやコンテキストウィンドウの広いモデル）に効率よく流し込むために、**「全ファイルのRAW URLを1つのテキストファイルにまとめる」**、あるいは**「全内容を1つのファイルに結合する」**方法がベストです。

最も効率的な2つのステップを提案します。

## 1. 全ファイルの RAW URL リストを一括作成する

まずは、300ファイル分のURLを数秒でリスト化しましょう。GitHub CLIやターミナルが使える環境であれば、以下のコマンドが最も速いです。

Bash

```
# 設定（ご自身の環境に合わせて書き換えてください）
USER="ユーザー名"
REPO="リポジトリ名"
BRANCH="main"

# .mdファイルを検索し、RAW URLの形式に変換して保存
git ls-files | grep '\.md$' | sed "s|^|https://raw.githubusercontent.com/$USER/$REPO/$BRANCH/|" > ai_input_urls.txt
```

これで `ai_input_urls.txt` に300行のURLが並びます。

## 2. AIに効率よく読み込ませるための工夫

300のURLをAIに渡す際、AI側の「Webブラウジング機能」で1つずつ読みに行かせると、通信エラーや時間切れ（タイムアウト）が起きやすくなります。

より確実な方法として、**「全ファイルを1つのテキストに結合して渡す」**ことを検討してみてください。

### 全ファイルを結合するスクリプト（推奨）

以下のPythonコードを使えば、300ファイルのRAW URLを巡回し、一つの「巨大な参考資料.md」として統合できます。

Python

```
import requests

# URLリストを読み込む
with open('ai_input_urls.txt', 'r') as f:
    urls = [line.strip() for line in f if line.strip()]

with open('combined_docs_for_ai.md', 'w', encoding='utf-8') as outfile:
    for url in urls:
        filename = url.split('/')[-1]
        print(f"Fetching: {filename}")
        
        response = requests.get(url)
        if response.status_code == 200:
            # AIが構造を理解しやすいよう、ファイル名を見出しとして挿入
            outfile.write(f"\n\n--- FILE: {filename} ---\n\n")
            outfile.write(response.text)
        else:
            print(f"Failed to fetch {url}")

print("完了！ combined_docs_for_ai.md をAIにアップロードしてください。")
```

## 運用のアドバイス

- **トークン制限:** 300ファイルだと合計文字数が膨大になる可能性があります。Gemini 1.5 Proなどの長大なコンテキスト（100万〜200万トークン）に対応したモデルであれば、結合したファイルをそのままアップロードして「この資料全体を把握して」と指示するだけで済みます。
    
- **情報の鮮度:** リポジトリが頻繁に更新されるなら、上記スクリプトを定期実行するようにしておけば、常に最新のドキュメントをAIに読み込ませる準備が整います。
    