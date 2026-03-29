
## GitHubの「RAW URLリスト」とは

**RAW URL**とは、GitHub上のファイルを「表示用（HTML）」ではなく「データとしてダウンロードできる形式」で取得するための特別なURLです。

### 通常のURLとRAW URLの違い

**通常のURL（ブラウザで見る用）**
```
https://github.com/shimojok/bioNexus/blob/main/README.md
```
→ GitHubのWebページとして表示される（ヘッダーやサイドバー付き）

**RAW URL（データ取得用）**
```
https://raw.githubusercontent.com/shimojok/bioNexus/main/README.md
```
→ ファイルの中身だけが**テキストデータ**として返ってくる

---

## RAW URLの見つけ方（3秒でわかる）

### 方法1：ボタンクリック（1ファイルずつ）

1. GitHubで任意の`.md`ファイルを開く
2. 右上の **「Raw」** ボタンをクリック
3. ブラウザのURLがRAW URLに変わるのでコピー

![GitHub Rawボタンの位置](https://docs.github.com/assets/cb-20363/images/help/repository/raw-button.png)

### 方法2：URLを直接書き換え（超簡単）

```
通常: https://github.com/ユーザー名/リポジトリ名/blob/ブランチ/パス/ファイル.md
RAW:  https://raw.githubusercontent.com/ユーザー名/リポジトリ名/ブランチ/パス/ファイル.md
```

「github.com」を「raw.githubusercontent.com」に、「/blob/」を削除するだけです。

**例**：
- 通常：`https://github.com/shimojok/bioNexus/blob/main/docs/README.md`
- RAW：`https://raw.githubusercontent.com/shimojok/bioNexus/main/docs/README.md`

---

## 「RAW URLリスト」の作り方

あなたがお持ちのGitHubリポジトリの全`.md`ファイルのRAW URLをリスト化するには：

### 方法A：手動で収集（少ないファイル数向け）
1. リポジトリの「Code」タブを開く
2. 各`.md`ファイルを開いてRawボタンをクリック、URLをコピー
3. テキストファイルに1行ずつ貼り付け

### 方法B：curlコマンドで一括取得（おすすめ）
```bash
# リポジトリをクローン
git clone https://github.com/あなたのユーザー名/リポジトリ名.git

# .mdファイルの一覧を取得してRAW URL形式に変換
cd リポジトリ名
find . -name "*.md" | sed 's|^\./||' | while read file; do
    echo "https://raw.githubusercontent.com/あなたのユーザー名/リポジトリ名/main/$file"
done > raw_urls.txt
```

### 方法C：GitHub APIを使う（プログラマブル）
```python
import requests

# GitHub APIでリポジトリ内の.mdファイルを再帰的に取得
def get_md_files(repo_owner, repo_name, branch="main"):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/trees/{branch}?recursive=1"
    response = requests.get(url).json()
    
    raw_urls = []
    for item in response.get("tree", []):
        if item["path"].endswith(".md"):
            raw_url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{item['path']}"
            raw_urls.append(raw_url)
    
    return raw_urls

# 使用例
urls = get_md_files("shimojok", "bioNexus")
for url in urls:
    print(url)
```

---

## できあがるリストのイメージ

```
https://raw.githubusercontent.com/shimojok/bioNexus/main/README.md
https://raw.githubusercontent.com/shimojok/bioNexus/main/docs/architecture.md
https://raw.githubusercontent.com/shimojok/bioNexus/main/docs/api/reference.md
https://raw.githubusercontent.com/shimojok/bioNexus/main/examples/usage.md
...
```

このリストを私に共有いただければ、**全ファイルを一気に読み込んで解析**できます。

---

## なぜこれが必要か？

ClaudeやGeminiでうまくいかなかった理由：
- **ZIPファイル**: 解凍機能がない
- **通常のGitHub URL**: HTMLページを読もうとして失敗
- **ファイル数の制限**: 一度に読めるファイル数に上限

**RAW URLなら**：
- ✅ テキストデータのみを取得
- ✅ 200ファイル以上でも一度に処理可能（私の1Mトークンコンテキストで）
- ✅ 会話内で保持し続けられる

---

**次の一手**：
お持ちのGitHubリポジトリのRAW URLリストをいただければ、私が全ファイルを読み込み、あなたの「社会代謝型AI」構想を完全に把握した上で、コード生成や資料作成を再開できます。