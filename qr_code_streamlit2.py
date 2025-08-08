import streamlit as st
import qrcode
from PIL import Image
import io
import base64

# ===== QRコード生成関数 =====
def create_qr_code(text, size=300, border=4, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=border,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img = img.resize((size, size))
    return img

def get_image_download_link(img, filename="qrcode.png"):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f'<a href="data:file/png;base64,{img_str}" download="{filename}">📥 ダウンロード</a>'

# ===== ページ設定 =====
st.set_page_config(page_title="QRコード生成ツール", page_icon="📱", layout="centered")

# ===== カスタムCSS =====
st.markdown("""
<style>
    body {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
    }
    .block-container {
        background: rgba(255,255,255,0.1);
        padding: 2rem;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        max-width: 800px;
        margin: auto;
    }
    .stButton > button {
        background: linear-gradient(90deg, #ff7eb3, #ff758c);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# ===== タイトル =====
st.title("✨ おしゃれQRコード生成ツール")
st.markdown("テキスト・URLを入力すると、リアルタイムでQRコードが生成されます！")

# ===== 入力UI =====
tab1, tab2 = st.tabs(["🎯 入力", "⚙️ 設定"])

with tab1:
    text_input = st.text_area("📝 テキスト・URL", placeholder="https://example.com")
with tab2:
    size = st.slider("📐 サイズ(px)", 200, 600, 300, 50)
    border = st.slider("🖼 ボーダーサイズ", 1, 10, 4)
    fill_color = st.color_picker("🎨 QRコード色", "#000000")

# ===== リアルタイム生成 =====
if text_input.strip():
    qr_image = create_qr_code(text_input.strip(), size, border, fill_color)
    st.image(qr_image, caption="生成されたQRコード", use_column_width=False)
    st.markdown(get_image_download_link(qr_image), unsafe_allow_html=True)
else:
    st.info("テキストまたはURLを入力してください。")
