# textutilsjp

![PyPI](https://img.shields.io/pypi/v/textutilsjp)
![License](https://img.shields.io/github/license/Kongou173/textutilsjp)
![Python](https://img.shields.io/pypi/pyversions/textutilsjp)

日本語テキストの整形・抽出・要約・解析に役立つPythonライブラリです。 
---

## 特徴 / Features

- **全角⇔半角変換**：日本語文書の文字種統一
- **ひらがな⇔カタカナ変換**：表記ゆれ対策
- **メールアドレス・URL抽出**：情報抽出・データクレンジング
- **テキストクリーニング**：改行・空白統一、不要文字除去
- **シンプルな要約**：日本語文章の一行要約
- **キーワード抽出・頻度解析**：自然言語処理タスクの前処理

---

## インストール / Installation

```bash
pip install textutilsjp
```

---

## 使い方 / Usage

### 基本的な使い方

```python
from textutilsjp import (
    to_hankaku, to_zenkaku,
    hira_to_kata, kata_to_hira,
    extract_emails, extract_urls,
    clean_text, summarize,
    extract_keywords, word_count
)

text = "ＡＢＣ　１２３ test@example.com https://example.com"

print(to_hankaku(text))  # ABC 123 test@example.com https://example.com
print(to_zenkaku("ABC 123"))  # ＡＢＣ　１２３
print(hira_to_kata("こんにちは"))  # コンニチハ
print(kata_to_hira("テスト"))  # てすと

print(extract_emails("連絡先: info@example.com, test@sample.jp"))
# ['info@example.com', 'test@sample.jp']

print(extract_urls("公式: https://example.com/info 参考: http://ex.jp"))
# ['https://example.com/info', 'http://ex.jp']

print(clean_text("  こんにちは。\n\n世界！\t  "))
# こんにちは。\n世界！

print(summarize("今日は晴れです。明日は雨でしょう。"))
# 今日は晴れです

print(extract_keywords("テスト テスト python python コード", topn=2))
# ['テスト', 'python']

print(word_count("テスト テスト python コード コード"))
# {'テスト': 2, 'python': 1, 'コード': 2}
```

---

## 関数一覧 / Function List

| 関数                 | 説明                                                         |
|----------------------|--------------------------------------------------------------|
| `to_hankaku`         | 全角→半角変換                                               |
| `to_zenkaku`         | 半角→全角変換                                               |
| `hira_to_kata`       | ひらがな→カタカナ                                           |
| `kata_to_hira`       | カタカナ→ひらがな                                           |
| `extract_emails`     | テキストからメールアドレス抽出                               |
| `extract_urls`       | テキストからURL抽出                                          |
| `clean_text`         | 不要な空白・改行・記号除去                                   |
| `summarize`          | 文章の先頭一文要約                                          |
| `extract_keywords`   | 単語頻度上位キーワード抽出                                  |
| `word_count`         | 単語ごとの出現回数辞書生成                                  |

---

## 応用例 / Advanced Usage

### ファイルからの一括処理

```python
with open("sample.txt", encoding="utf-8") as f:
    data = f.read()
cleaned = clean_text(data)
keywords = extract_keywords(cleaned, topn=5)
print(keywords)
```

### pandasと組み合わせる

```python
import pandas as pd
from textutilsjp import clean_text, extract_keywords

df = pd.read_csv("data.csv")
df["cleaned"] = df["text"].apply(clean_text)
df["keywords"] = df["cleaned"].apply(lambda x: extract_keywords(x, topn=3))
```

---

## よくある用途 / Typical Use Cases

- 日本語データセットの前処理
- スクレイピングした日本語文章のクレンジング
- メール/URLリスト化
- キーワード抽出によるカテゴリ分類
- 業務日報やレポートの要約
- テキストマイニングの下準備

---

## 開発・テスト

### ソースコードのクローン

```bash
git clone https://github.com/Kongou173/textutilsjp.git
cd textutilsjp
pip install -e .
```

### テストの実行

```bash
pytest tests/
```

---

## 貢献・フィードバック / Contribution & Feedback

- プルリクエスト・Issue歓迎！
- 新しい関数・改善案・バグ報告など何でもお願いします。
- 日本語・英語どちらでもOKです。

---

## ライセンス / License

MIT License

---

## 英語版README / English README

See [README_en.md](./README_en.md) for English documentation.

---

## 更新履歴 / Changelog

- v0.0.0 最初のバージョンのリリース開始。2025/7/17(木曜日)

---

## 連絡 / Contact

- GitHub: [yourname](https://github.com/Kongou173)
- Email: jifengtongsheng@gmail.com

---

## 参考 / References

- [日本語テキスト処理の基礎](https://nlp100.github.io/)
- [Python 公式ドキュメント](https://docs.python.org/ja/3/)
