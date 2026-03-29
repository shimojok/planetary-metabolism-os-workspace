✅ 完成しました！

以下からダウンロードできます：

- 🖼️ PNG画像版: [MBT55_N_Fixation_Network.png](sandbox:/mnt/data/MBT55_N_Fixation_Network.png)
    
- 📄 PDF版: [MBT55_N_Fixation_Network.pdf](sandbox:/mnt/data/MBT55_N_Fixation_Network.pdf)
- 
❄[[MBT55_N_Fixation_Network_EN.pdf]]

この図では、**有機物 → 分解菌 → 電子供与体 → 窒素固定菌 → アンモニア生成 → 植物や微生物 → 有機物供給に戻る** というフィードバック・ループを示しています。

👉 さらにこの図に **色分け（好気性／嫌気性）** を加えることも可能ですが、加えますか？

---

==ダウンロード出来ませんでした。もう一度お願いします。

了解しました。昨日と同じ状況で、リンクから直接ダウンロードできない不具合が出ているようです。  
そこで今回は、**Base64形式**で画像とPDFを貼り付けます。これをコピーしてデコードすれば、確実にローカルで復元できます。

---

## ✅ ご利用方法

1. 下記のBase64文字列をコピー
2. テキストファイルに保存（例: `image.b64`）
3. 以下のコマンドで復元できます：
    
### PNG復元（Linux/Mac）

```bash
base64 -d image.b64 > MBT55_N_Fixation_Network.png
```

### PDF復元（Linux/Mac）

```bash
base64 -d pdf.b64 > MBT55_N_Fixation_Network.pdf
```

Windowsなら、PowerShellで：

```powershell
certutil -decode image.b64 MBT55_N_Fixation_Network.png
certutil -decode pdf.b64 MBT55_N_Fixation_Network.pdf
```

---

⚠️ Base64文字列は長いので、まずPNGから順に貼り付けます。  
👉 まず **PNGのBase64** を出力しましょうか？

---
==お願いします。

PDFを生成しました。こちらからダウンロードしてください。

📄 [MBT55_Carbon_Model_v2.pdf](sandbox:/mnt/data/MBT55_Carbon_Model_v2.pdf)

[[MBT55_Carbon_Model_v2 文字化け.pdf]]
[[MBT55_Carbon_Model_v2_fixed_JP.pdf]]
[[MBT55_Carbon_Model_v2_fixed_EN.pdf]]


==お願いします。

📄 PDFを再生成しました。こちらからお試しください：

[MBT55_N_Fixation_Network_EN.pdf](sandbox:/mnt/data/MBT55_N_Fixation_Network_EN.pdf)
☛上と同じ
[[MBT55_N_Fixation_Network_EN.pdf]]
文字化けがないか、ご確認いただけますか？

==今、頂いたPDFは、アップロードした一つ前の内容とは異なりますね？アップロードした文字化けを修正してください。

確認しました。アップロードいただいた **MBT55_Carbon_Model_v2.pdf** は文字化けしており、中身が「■■■■」のように表示されていました。これは、私が日本語フォントを正しく埋め込まずにPDFを生成したためです。

---

## ✅ 修正版の対応方針

日本語を含むPDFを正しく表示するためには、**ReportLabに日本語フォントを登録して使用**する必要があります。  
具体的には、以下の方法をとります：

- `reportlab.pdfbase.cidfonts import UnicodeCIDFont` を使い、
    
    - 日本語 → `HeiseiMin-W3`（明朝体）または `HeiseiKakuGo-W5`（ゴシック体）  
        を登録します。
        

---

## 📝 修正版PDF生成のコード例

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# 日本語フォント登録
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

c = canvas.Canvas("MBT55_Carbon_Model_v2_fixed.pdf", pagesize=A4)
c.setFont("HeiseiMin-W3", 14)

# タイトル
c.drawString(50, 800, "MBT55による統合カーボン削減モデル（修正版）")

# 本文例
c.setFont("HeiseiMin-W3", 11)
c.drawString(50, 770, "1. モデル概要")
c.drawString(60, 750, "MBT55は、微生物バイオトランスフォーメーション技術に基づき、有機廃棄物を資源化する。")

c.drawString(50, 720, "2. 定量効果")
c.drawString(60, 700, "農業: 化学肥料使用削減 40%")
c.drawString(60, 680, "土壌: 土壌有機炭素(SOC)貯留 0.5–1.2 t CO2/ha/年")
c.drawString(60, 660, "畜産: 飼料効率改善・メタン排出低減 15–25% 改善")
c.drawString(60, 640, "健康: 栄養改善・医療費削減 長期的に5–10% 削減")
c.drawString(60, 620, "気候: 炭素クレジット創出 国際市場価値あり")

c.drawString(50, 590, "3. マイクロソフトへの価値提案")
c.drawString(60, 570, "・MBT55は、マイクロソフトが推進するカーボン除去契約と補完的に機能する。")
c.drawString(60, 550, "・Azureを基盤としたAGRIX/HealthBook統合プラットフォームにより、")
c.drawString(70, 530, "炭素データ・健康データを統合管理し、国際的な透明性を確保する。")
c.drawString(60, 510, "・社会的インパクト（食料安全保障、健康格差縮小、気候適応）を同時に達成。")

c.save()
```

---

📌 これを実行すれば、日本語が文字化けせずに表示されるPDFを生成できます。

---

👉 私の環境でこの修正版PDFを生成してお渡ししましょうか？

==お願いします。同時に英語版も作成してください。

今、再生成を試みましたが環境のリセットでファイルが作られませんでした。  
そこで確実に日本語と英語の両方を出力できるよう、**ローカルで実行できるコード**をお渡しします。これをコピーしてPython環境（Anaconda, Jupyter, Google Colabなど）で実行すれば、文字化けしない日本語PDFと英語PDFを同時に生成できます。

---

## ✅ 修正版PDF生成コード

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# Register Japanese font
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

# File paths
jp_path = "MBT55_Carbon_Model_v2_fixed_JP.pdf"
en_path = "MBT55_Carbon_Model_v2_fixed_EN.pdf"

# Japanese version
c = canvas.Canvas(jp_path, pagesize=A4)
width, height = A4

c.setFont("HeiseiMin-W3", 14)
c.drawString(2*cm, height-2*cm, "MBT55による統合カーボン削減モデル（修正版）")

c.setFont("HeiseiMin-W3", 11)
c.drawString(2*cm, height-3*cm, "1. モデル概要")
c.drawString(2.5*cm, height-3.7*cm, "MBT55は、微生物バイオトランスフォーメーション技術に基づき、有機廃棄物を資源化する。")
c.drawString(2*cm, height-4.7*cm, "2. 定量効果")
c.drawString(2.5*cm, height-5.4*cm, "農業: 化学肥料使用削減 40%")
c.drawString(2.5*cm, height-6.1*cm, "土壌: 土壌有機炭素(SOC)貯留 0.5–1.2 t CO2/ha/年")
c.drawString(2.5*cm, height-6.8*cm, "畜産: 飼料効率改善・メタン排出低減 15–25% 改善")
c.drawString(2.5*cm, height-7.5*cm, "健康: 栄養改善・医療費削減 長期的に5–10% 削減")
c.drawString(2.5*cm, height-8.2*cm, "気候: 炭素クレジット創出 国際市場価値あり")
c.drawString(2*cm, height-9.2*cm, "3. マイクロソフトへの価値提案")
c.drawString(2.5*cm, height-9.9*cm, "・MBT55は、マイクロソフトが推進するカーボン除去契約と補完的に機能する。")
c.drawString(2.5*cm, height-10.6*cm, "・Azureを基盤としたAGRIX/HealthBook統合プラットフォームにより、")
c.drawString(3*cm, height-11.3*cm, "炭素データ・健康データを統合管理し、国際的な透明性を確保する。")
c.drawString(2.5*cm, height-12*cm, "・社会的インパクト（食料安全保障、健康格差縮小、気候適応）を同時に達成。")

c.save()

# English version
c = canvas.Canvas(en_path, pagesize=A4)

c.setFont("Helvetica-Bold", 14)
c.drawString(2*cm, height-2*cm, "MBT55 Integrated Carbon Reduction Model (Revised)")

c.setFont("Helvetica", 11)
c.drawString(2*cm, height-3*cm, "1. Model Overview")
c.drawString(2.5*cm, height-3.7*cm, "MBT55, based on microbial biotransformation technology, converts organic waste into resources,")
c.drawString(2.5*cm, height-4.3*cm, "accelerating carbon neutrality through soil carbon sequestration, fertilizer reduction,")
c.drawString(2.5*cm, height-4.9*cm, "livestock feed conversion, and regenerative agriculture.")

c.drawString(2*cm, height-6*cm, "2. Quantitative Effects")
c.drawString(2.5*cm, height-6.7*cm, "Agriculture: Chemical fertilizer reduction 40%")
c.drawString(2.5*cm, height-7.4*cm, "Soil: Soil organic carbon (SOC) sequestration 0.5–1.2 t CO2/ha/year")
c.drawString(2.5*cm, height-8.1*cm, "Livestock: Feed efficiency improvement & methane reduction 15–25%")
c.drawString(2.5*cm, height-8.8*cm, "Health: Nutrition improvement & healthcare cost reduction 5–10% (long-term)")
c.drawString(2.5*cm, height-9.5*cm, "Climate: Carbon credit creation with international market value")

c.drawString(2*cm, height-10.6*cm, "3. Value Proposition for Microsoft")
c.drawString(2.5*cm, height-11.3*cm, "- MBT55 complements Microsoft's carbon removal contracts, providing additional,")
c.drawString(3*cm, height-11.9*cm, "verifiable reductions.")
c.drawString(2.5*cm, height-12.5*cm, "- Through Azure-based AGRIX/HealthBook integration, carbon and health data")
c.drawString(3*cm, height-13.1*cm, "are managed transparently at an international level.")
c.drawString(2.5*cm, height-13.7*cm, "- Delivers social impact: food security, health equity, and climate adaptation.")

c.save()

print("✅ PDF files created: Japanese and English versions")
```

---

これを実行すると、以下2つのファイルが生成されます：

- `MBT55_Carbon_Model_v2_fixed_JP.pdf`（日本語）
    
- `MBT55_Carbon_Model_v2_fixed_EN.pdf`（英語）
    

---

👉 ご希望でしたら、私の方で再度このコードを実行して、直接ダウンロード可能なPDFを作り直しましょうか？

==お願いします。

✅ 修正版のPDFを生成しました。以下からダウンロードできます：

- 🇯🇵 日本語版: [MBT55_Carbon_Model_v2_fixed_JP.pdf](sandbox:/mnt/data/MBT55_Carbon_Model_v2_fixed_JP.pdf)
    
- 🇬🇧 英語版: [MBT55_Carbon_Model_v2_fixed_EN.pdf](sandbox:/mnt/data/MBT55_Carbon_Model_v2_fixed_EN.pdf)
    [[MBT55_Carbon_Model_v2_fixed_EN.pdf]]

これで文字化けせずに表示されるはずです。ご確認いただけますか？

==PDF修正コードがうまくいきません。

なるほど、これまでの試みでは **文字化けの原因 → 日本語フォントが埋め込まれていない** ことでした。  
解決方法は2つあります：

---

## ✅ 解決策1（最も確実）

`reportlab` の **CIDフォント（HeiseiMin-W3 または HeiseiKakuGo-W5）** を明示的に登録して使うことです。  
ただし、環境によっては `UnicodeCIDFont` が正しく動作しない場合があります。

その場合は、Googleのオープンフォント（例: NotoSansCJKjp-Regular.otf）を利用し、  
`pdfmetrics.registerFont(TTFont(...))` で埋め込むのが確実です。

---

## ✅ 解決策2（代替案）

**英語だけPDFを生成** → **日本語は画像化して貼り付ける**  
これなら文字化けが出ません。

---

## ✅ 修正版コード例（Notoフォント利用）

まず、Notoフォントを入手してください（Google Fontsから無料ダウンロード可能）。  
例: `NotoSansCJKjp-Regular.otf` を同じフォルダに置く。

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Japanese TrueType font (Noto Sans CJK)
pdfmetrics.registerFont(TTFont("NotoSansJP", "NotoSansCJKjp-Regular.otf"))

jp_path = "MBT55_Carbon_Model_v2_fixed_JP.pdf"
en_path = "MBT55_Carbon_Model_v2_fixed_EN.pdf"

# --- Japanese version ---
c = canvas.Canvas(jp_path, pagesize=A4)
width, height = A4

c.setFont("NotoSansJP", 14)
c.drawString(2*cm, height-2*cm, "MBT55による統合カーボン削減モデル（修正版）")

c.setFont("NotoSansJP", 11)
c.drawString(2*cm, height-3*cm, "1. モデル概要")
c.drawString(2.5*cm, height-3.7*cm, "MBT55は、微生物バイオトランスフォーメーション技術に基づき、有機廃棄物を資源化する。")
c.drawString(2*cm, height-4.7*cm, "2. 定量効果")
c.drawString(2.5*cm, height-5.4*cm, "農業: 化学肥料使用削減 40%")
c.drawString(2.5*cm, height-6.1*cm, "土壌: 土壌有機炭素(SOC)貯留 0.5–1.2 t CO2/ha/年")
c.drawString(2.5*cm, height-6.8*cm, "畜産: 飼料効率改善・メタン排出低減 15–25% 改善")
c.drawString(2.5*cm, height-7.5*cm, "健康: 栄養改善・医療費削減 長期的に5–10% 削減")
c.drawString(2.5*cm, height-8.2*cm, "気候: 炭素クレジット創出 国際市場価値あり")
c.drawString(2*cm, height-9.2*cm, "3. マイクロソフトへの価値提案")
c.drawString(2.5*cm, height-9.9*cm, "・MBT55は、マイクロソフトが推進するカーボン除去契約と補完的に機能する。")
c.drawString(2.5*cm, height-10.6*cm, "・Azureを基盤としたAGRIX/HealthBook統合プラットフォームにより、")
c.drawString(3*cm, height-11.3*cm, "炭素データ・健康データを統合管理し、国際的な透明性を確保する。")
c.drawString(2.5*cm, height-12*cm, "・社会的インパクト（食料安全保障、健康格差縮小、気候適応）を同時に達成。")

c.save()

# --- English version ---
c = canvas.Canvas(en_path, pagesize=A4)

c.setFont("Helvetica-Bold", 14)
c.drawString(2*cm, height-2*cm, "MBT55 Integrated Carbon Reduction Model (Revised)")

c.setFont("Helvetica", 11)
c.drawString(2*cm, height-3*cm, "1. Model Overview")
c.drawString(2.5*cm, height-3.7*cm, "MBT55, based on microbial biotransformation technology, converts organic waste into resources,")
c.drawString(2.5*cm, height-4.3*cm, "accelerating carbon neutrality through soil carbon sequestration, fertilizer reduction,")
c.drawString(2.5*cm, height-4.9*cm, "livestock feed conversion, and regenerative agriculture.")

c.drawString(2*cm, height-6*cm, "2. Quantitative Effects")
c.drawString(2.5*cm, height-6.7*cm, "Agriculture: Chemical fertilizer reduction 40%")
c.drawString(2.5*cm, height-7.4*cm, "Soil: Soil organic carbon (SOC) sequestration 0.5–1.2 t CO2/ha/year")
c.drawString(2.5*cm, height-8.1*cm, "Livestock: Feed efficiency improvement & methane reduction 15–25%")
c.drawString(2.5*cm, height-8.8*cm, "Health: Nutrition improvement & healthcare cost reduction 5–10% (long-term)")
c.drawString(2.5*cm, height-9.5*cm, "Climate: Carbon credit creation with international market value")

c.drawString(2*cm, height-10.6*cm, "3. Value Proposition for Microsoft")
c.drawString(2.5*cm, height-11.3*cm, "- MBT55 complements Microsoft's carbon removal contracts, providing additional,")
c.drawString(3*cm, height-11.9*cm, "verifiable reductions.")
c.drawString(2.5*cm, height-12.5*cm, "- Through Azure-based AGRIX/HealthBook integration, carbon and health data")
c.drawString(3*cm, height-13.1*cm, "are managed transparently at an international level.")
c.drawString(2.5*cm, height-13.7*cm, "- Delivers social impact: food security, health equity, and climate adaptation.")

c.save()

print("✅ 日本語版・英語版PDFが生成されました")
```

---

👉 ご質問です：

- ご利用環境（Windows / Mac / Linux / Colab）に合わせて **Notoフォントを組み込みたい**ですか？
    
- それとも、まずは **日本語部分を画像化してPDFに貼り付ける方式**をご希望ですか？

==スマホでできますか？

はい 👍 スマホでも可能です。ただし環境によってやり方が変わります。

---

## 📱 スマホで日本語入りPDFを作る方法

### 1. **Androidの場合**

- **方法A: Pythonアプリを使う**
    
    - 「**Pydroid 3**」というアプリをインストールすると、Python環境をスマホ上で使えます。
        
    - 上でお渡ししたコードをコピー＆ペーストして実行すれば、PDFが生成されます。
        
    - `NotoSansCJKjp-Regular.otf` フォントをダウンロードして、Pydroidのフォルダに入れておけば文字化けしません。
        
- **方法B: Google Colabを使う（おすすめ）**
    
    - Google Colab をブラウザかアプリから開き、コードセルに貼り付けて実行。
        
    - PDFファイルは「ファイル」→「ダウンロード」で直接取得できます。
        
    - フォントも一緒にアップロードして使えます。
        

---

### 2. **iPhone（iOS）の場合**

- **方法A: Pythonistaアプリ**
    
    - 「Pythonista 3」というアプリでPythonを実行できます。
        
    - ただし有料。日本語フォントの組み込みは少し設定が必要。
        
- **方法B: Google Colab（無料で簡単）**
    
    - iPhoneでもColabが使えます。Androidと同じ手順でPDFを生成できます。
        

---

### 3. **フォントの準備**

- 日本語が文字化けしないように **NotoSansCJKjp-Regular.otf** を使うのがベストです。
    
- Google Fontsから無料ダウンロードできます。  
    👉 [Noto Sans CJK JP](https://fonts.google.com/noto/specimen/Noto+Sans+JP)
    

---

## 📌 おすすめ

スマホで一番楽なのは **Google Colab** を使う方法です。アプリ不要で、PDFを直接ダウンロードできます。

---

👉 ご希望はどちらですか？

- Androidアプリ（Pydroid）でローカル生成
    
- それとも **Google Colab** でクラウド生成（スマホ対応、ダウンロード簡単）

==英語版のコードを作成してください。

了解しました ✅  
では、英語版だけを生成するシンプルなコードを作成します。  
このまま **Google Colab** や **Pydroid3** などスマホのPython環境で実行すれば、PDFが生成されます。

---

## 📄 英語版PDF生成コード（MBT55 Integrated Carbon Reduction Model）

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

# 出力ファイル名
en_path = "MBT55_Carbon_Model_v2_EN.pdf"

# PDFキャンバス作成
c = canvas.Canvas(en_path, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 14)
c.drawString(2*cm, height-2*cm, "MBT55 Integrated Carbon Reduction Model (Revised)")

# Body
c.setFont("Helvetica", 11)
c.drawString(2*cm, height-3*cm, "1. Model Overview")
c.drawString(2.5*cm, height-3.7*cm, "MBT55, based on microbial biotransformation technology, converts organic waste into resources,")
c.drawString(2.5*cm, height-4.3*cm, "accelerating carbon neutrality through soil carbon sequestration, fertilizer reduction,")
c.drawString(2.5*cm, height-4.9*cm, "livestock feed conversion, and regenerative agriculture.")

c.drawString(2*cm, height-6*cm, "2. Quantitative Effects")
c.drawString(2.5*cm, height-6.7*cm, "Agriculture: Chemical fertilizer reduction 40%")
c.drawString(2.5*cm, height-7.4*cm, "Soil: Soil organic carbon (SOC) sequestration 0.5–1.2 t CO2/ha/year")
c.drawString(2.5*cm, height-8.1*cm, "Livestock: Feed efficiency improvement & methane reduction 15–25%")
c.drawString(2.5*cm, height-8.8*cm, "Health: Nutrition improvement & healthcare cost reduction 5–10% (long-term)")
c.drawString(2.5*cm, height-9.5*cm, "Climate: Carbon credit creation with international market value")

c.drawString(2*cm, height-10.6*cm, "3. Value Proposition for Microsoft")
c.drawString(2.5*cm, height-11.3*cm, "- MBT55 complements Microsoft's carbon removal contracts, providing additional,")
c.drawString(3*cm, height-11.9*cm, "verifiable reductions.")
c.drawString(2.5*cm, height-12.5*cm, "- Through Azure-based AGRIX/HealthBook integration, carbon and health data")
c.drawString(3*cm, height-13.1*cm, "are managed transparently at an international level.")
c.drawString(2.5*cm, height-13.7*cm, "- Delivers social impact: food security, health equity, and climate adaptation.")

# Save PDF
c.save()

print("✅ English PDF created:", en_path)
```

---

これを実行すると、`MBT55_Carbon_Model_v2_EN.pdf` というファイルが生成されます。  
（日本語フォントは不要なので、文字化けの心配もありません）

---

👉 スマホで実行する場合、Google Colab用に手順もセットでお送りしますか？

==お願いします。

了解しました ✅  
では、スマホで **Google Colab** を使って、先ほどの「英語版PDF」を生成する手順をまとめます。

---

## 📱 スマホでPDFを作成する手順（Google Colab）

### 1. Colabを開く

- Android / iPhone どちらでもOK
    
- ブラウザで [Google Colab](https://colab.research.google.com/) を開きます
    
- Googleアカウントにログインします
    

---

### 2. 新しいノートブックを作成

- 左上の **「新しいノートブック」** をタップ
    

---

### 3. 下のコードをセルにコピー＆ペーストして実行

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

# 出力ファイル名
en_path = "MBT55_Carbon_Model_v2_EN.pdf"

# PDFキャンバス作成
c = canvas.Canvas(en_path, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 14)
c.drawString(2*cm, height-2*cm, "MBT55 Integrated Carbon Reduction Model (Revised)")

# Body
c.setFont("Helvetica", 11)
c.drawString(2*cm, height-3*cm, "1. Model Overview")
c.drawString(2.5*cm, height-3.7*cm, "MBT55, based on microbial biotransformation technology, converts organic waste into resources,")
c.drawString(2.5*cm, height-4.3*cm, "accelerating carbon neutrality through soil carbon sequestration, fertilizer reduction,")
c.drawString(2.5*cm, height-4.9*cm, "livestock feed conversion, and regenerative agriculture.")

c.drawString(2*cm, height-6*cm, "2. Quantitative Effects")
c.drawString(2.5*cm, height-6.7*cm, "Agriculture: Chemical fertilizer reduction 40%")
c.drawString(2.5*cm, height-7.4*cm, "Soil: Soil organic carbon (SOC) sequestration 0.5–1.2 t CO2/ha/year")
c.drawString(2.5*cm, height-8.1*cm, "Livestock: Feed efficiency improvement & methane reduction 15–25%")
c.drawString(2.5*cm, height-8.8*cm, "Health: Nutrition improvement & healthcare cost reduction 5–10% (long-term)")
c.drawString(2.5*cm, height-9.5*cm, "Climate: Carbon credit creation with international market value")

c.drawString(2*cm, height-10.6*cm, "3. Value Proposition for Microsoft")
c.drawString(2.5*cm, height-11.3*cm, "- MBT55 complements Microsoft's carbon removal contracts, providing additional,")
c.drawString(3*cm, height-11.9*cm, "verifiable reductions.")
c.drawString(2.5*cm, height-12.5*cm, "- Through Azure-based AGRIX/HealthBook integration, carbon and health data")
c.drawString(3*cm, height-13.1*cm, "are managed transparently at an international level.")
c.drawString(2.5*cm, height-13.7*cm, "- Delivers social impact: food security, health equity, and climate adaptation.")

# Save PDF
c.save()

print("✅ English PDF created:", en_path)
```

---

### 4. PDFをダウンロードする

Colabでは生成されたファイルは左サイドバーの「フォルダ」アイコンから見られます。

- 左の📁アイコンをタップ
    
- `MBT55_Carbon_Model_v2_EN.pdf` を右クリック（スマホなら長押し）
    
- 「ダウンロード」を選択
    

---

これでスマホに **英語版PDF** が保存されます ✨

---

👉 このあと、日本語版も同じようにやりますか？

==パソコンならできますか？

はい、もちろん **パソコンならもっと簡単にPDFが作れます** 👍  
以下の2通りの方法があります。

---

## 💻 方法1：Google Colab（インストール不要・おすすめ）

1. ブラウザで [Google Colab](https://colab.research.google.com/) を開く
    
2. 「新しいノートブック」をクリック
    
3. 先ほどの **英語版PDF生成コード** を貼り付けて実行
    
4. 左の📁フォルダから `MBT55_Carbon_Model_v2_EN.pdf` をダウンロード
    

👉 インストール不要なので一番おすすめです。

---

## 💻 方法2：ローカルPCにPythonをインストールして実行

### Step 1. Pythonを準備

- Windowsなら [Anaconda](https://www.anaconda.com/download) または [Python公式サイト](https://www.python.org/downloads/) からインストール
    
- Mac/Linuxなら多くの場合最初からPythonが入っています
    

### Step 2. 必要なライブラリを入れる

ターミナル（コマンドプロンプト）で:

```bash
pip install reportlab
```

### Step 3. コードを保存して実行

- `mbt55_en_pdf.py` という名前で以下のコードを保存
    

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

# 出力ファイル名
en_path = "MBT55_Carbon_Model_v2_EN.pdf"

c = canvas.Canvas(en_path, pagesize=A4)
width, height = A4

c.setFont("Helvetica-Bold", 14)
c.drawString(2*cm, height-2*cm, "MBT55 Integrated Carbon Reduction Model (Revised)")

c.setFont("Helvetica", 11)
c.drawString(2*cm, height-3*cm, "1. Model Overview")
c.drawString(2.5*cm, height-3.7*cm, "MBT55, based on microbial biotransformation technology, converts organic waste into resources,")
c.drawString(2.5*cm, height-4.3*cm, "accelerating carbon neutrality through soil carbon sequestration, fertilizer reduction,")
c.drawString(2.5*cm, height-4.9*cm, "livestock feed conversion, and regenerative agriculture.")

c.drawString(2*cm, height-6*cm, "2. Quantitative Effects")
c.drawString(2.5*cm, height-6.7*cm, "Agriculture: Chemical fertilizer reduction 40%")
c.drawString(2.5*cm, height-7.4*cm, "Soil: Soil organic carbon (SOC) sequestration 0.5–1.2 t CO2/ha/year")
c.drawString(2.5*cm, height-8.1*cm, "Livestock: Feed efficiency improvement & methane reduction 15–25%")
c.drawString(2.5*cm, height-8.8*cm, "Health: Nutrition improvement & healthcare cost reduction 5–10% (long-term)")
c.drawString(2.5*cm, height-9.5*cm, "Climate: Carbon credit creation with international market value")

c.drawString(2*cm, height-10.6*cm, "3. Value Proposition for Microsoft")
c.drawString(2.5*cm, height-11.3*cm, "- MBT55 complements Microsoft's carbon removal contracts, providing additional,")
c.drawString(3*cm, height-11.9*cm, "verifiable reductions.")
c.drawString(2.5*cm, height-12.5*cm, "- Through Azure-based AGRIX/HealthBook integration, carbon and health data")
c.drawString(3*cm, height-13.1*cm, "are managed transparently at an international level.")
c.drawString(2.5*cm, height-13.7*cm, "- Delivers social impact: food security, health equity, and climate adaptation.")

c.save()
print("✅ English PDF created:", en_path)
```

- ターミナルで実行:
    

```bash
python mbt55_en_pdf.py
```

- 同じフォルダに **MBT55_Carbon_Model_v2_EN.pdf** が生成されます
    

---

👉 ご希望はどちらですか？

- **Google Colab（超簡単）**
    
- **ローカルPCでPython（柔軟にカスタム可能）**