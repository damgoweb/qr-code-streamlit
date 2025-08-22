# QRコード生成Webアプリ

## 主な構成・機能

### 1. インポートとQRコード生成関数

- `streamlit`, `qrcode`, `PIL.Image`, `io`, `base64` をインポート。
- `create_qr_code` 関数：テキスト・サイズ・色・ボーダー指定でQRコード画像を生成。
- `get_image_download_link` 関数：生成したQRコード画像をダウンロードできるリンク（base64エンコード）を返す。

---

### 2. ページ設定・デザイン

- `st.set_page_config` でタイトル・アイコン・レイアウトを設定。
- CSSでボタンやQRコード表示領域のデザインをカスタマイズ。

---

### 3. サイドバーUI

- プリセット（Google, YouTube, 挨拶, メール）から選択可能。
- サイズ（200～500px）、色（黒・青・紫・緑・赤）、ボーダーサイズ（1～10px）を選択できる。

---

### 4. メインエリア

- 左側：テキスト入力欄（プリセット選択時は初期値が入る）。
- 右側：ヒント（入力例や注意点）。

---

### 5. QRコード生成・表示

- 「QRコードを生成」ボタンで、入力テキスト・設定に基づきQRコード画像を生成。
- 生成結果を中央に表示し、ダウンロードリンクも表示。
- 生成情報（テキスト・サイズ・色・ボーダー・文字数）をexpanderで確認可能。
- エラー時はメッセージ表示。

---

### 6. フッター

- アプリ名と説明を下部に表示。

---

#### 主要な関数・変数リンク

- `create_qr_code`
- `get_image_download_link`

---


##  必要なPython環境:
  - Python 3.7以上
  - Streamlit（Webアプリケーションフレームワーク）
  - qrcode[pil]（QRコード生成ライブラリ）
  - Pillow（画像処理ライブラリ）

## 仮想環境構築手順:

```
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
```

##  実行方法:

```
  pip install -r requirements.txt
  streamlit run qr_code_streamlit.py
```

-  実行するとローカルサーバー（通常は http://localhos
  t:8501）でWebアプリケーションが起動し、ブラウザか
  らアクセスしてQRコード生成ツールを使用できます。