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