## JSONとは

JSON（JavaScript Object Notation）は、データを構造化して表現するための軽量なデータフォーマットです。人間にとって読み書きが容易で、機械にとっても解析・生成が簡単であることが特徴です。

## 基本構文

### データ型
JSONでは以下の6つのデータ型を扱うことができます：

1. **文字列（String）**
```json
"name": "山田太郎"
```

2. **数値（Number）**
```json
"age": 25,
"price": 199.99
```

3. **真偽値（Boolean）**
```json
"isStudent": true,
"hasLicense": false
```

4. **配列（Array）**
```json
"hobbies": ["読書", "映画鑑賞", "水泳"]
```

5. **オブジェクト（Object）**
```json
"address": {
  "city": "東京",
  "zipcode": "100-0001"
}
```

6. **null**
```json
"spouse": null
```

## 実際のJSON例

```json
{
  "id": 1,
  "name": "鈴木一郎",
  "age": 30,
  "email": "ichiro.suzuki@example.com",
  "isEmployed": true,
  "skills": ["Java", "Python", "JavaScript"],
  "address": {
    "postalCode": "150-0001",
    "prefecture": "東京都",
    "city": "渋谷区",
    "street": "神宮前1-1-1"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "03-1234-5678"
    },
    {
      "type": "mobile",
      "number": "090-1234-5678"
    }
  ],
  "birthDate": "1993-05-15",
  "notes": null
}
```

## JSONのルール

### 必須ルール
1. **キーは必ずダブルクォーテーションで囲む**
   - ✅ `"name": "田中"` 
   - ❌ `name: "田中"`

2. **文字列はダブルクォーテーションで囲む**
   - ✅ `"message": "こんにちは"`
   - ❌ `"message": 'こんにちは'`

3. **最後の要素にカンマをつけない**
   ```json
   {
     "name": "山田",  // ← カンマあり
     "age": 25        // ← カンマなし
   }
   ```

## JSONの利用シーン

### 1. Web APIでのデータ交換
```javascript
// APIリクエスト
fetch('https://api.example.com/users/1')
  .then(response => response.json())
  .then(data => console.log(data));
```

### 2. 設定ファイル
```json
{
  "appName": "MyApplication",
  "version": "1.0.0",
  "database": {
    "host": "localhost",
    "port": 5432,
    "name": "myapp_db"
  },
  "logging": {
    "level": "info",
    "file": "app.log"
  }
}
```

### 3. データ保存
```javascript
// ローカルストレージへの保存
const userData = {
  username: "tanaka",
  theme: "dark",
  language: "ja"
};
localStorage.setItem('userPrefs', JSON.stringify(userData));

// 読み込み
const savedPrefs = JSON.parse(localStorage.getItem('userPrefs'));
```

## JSONのメリット

1. **軽量で高速** - XMLなどと比べて記述が少なく、パースが速い
2. **言語非依存** - ほとんどのプログラミング言語でサポート
3. **可読性が高い** - シンプルな構造で理解しやすい
4. **JavaScriptとの親和性** - JavaScriptオブジェクトと相互変換が容易

## JSONと他のフォーマットの比較

| 特徴 | JSON | XML | YAML |
|------|------|-----|------|
| 可読性 | ◎ | ○ | ◎ |
| データサイズ | 小 | 大 | 中 |
| パース速度 | 速い | 遅い | 普通 |
| コメント | × | ○ | ○ |
| スキーマ定義 | △ (JSON Schema) | ○ (XSD) | △ |

## 注意点

1. **コメントが書けない**（公式仕様では）
2. **日付型がない** - 文字列として表現する必要がある
3. **循環参照を扱えない**
4. **数値の精度に制限がある**

## 主要言語でのJSON操作例

### JavaScript
```javascript
// オブジェクト → JSON文字列
const jsonStr = JSON.stringify(obj);

// JSON文字列 → オブジェクト
const obj = JSON.parse(jsonStr);
```

### Python
```python
import json

# 辞書 → JSON文字列
json_str = json.dumps(obj)

# JSON文字列 → 辞書
obj = json.loads(json_str)
```

### Java（Jackson使用）
```java
// オブジェクト → JSON
ObjectMapper mapper = new ObjectMapper();
String json = mapper.writeValueAsString(obj);

// JSON → オブジェクト
MyClass obj = mapper.readValue(json, MyClass.class);
```

JSONはそのシンプルさと汎用性から、現代のWeb開発において事実上の標準データフォーマットとなっています。特にRESTful APIやモバイルアプリケーションとのデータ通信で広く活用されています。