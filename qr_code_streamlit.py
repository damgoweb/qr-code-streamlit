import streamlit as st
import qrcode
from PIL import Image
import io
import base64

def create_qr_code(text, size=300, border=4, fill_color="black", back_color="white"):
    """QRコードを生成する関数"""
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
    """画像のダウンロードリンクを生成"""
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="{filename}">📥 QRコードをダウンロード</a>'
    return href

# ページ設定
st.set_page_config(
    page_title="QRコード生成ツール",
    page_icon="📱",
    layout="centered"
)

# カスタムCSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
    }
    .qr-container {
        text-align: center;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# メインタイトル
st.title("✨ QRコード生成ツール")
st.markdown("テキストやURLを入力してQRコードを生成しましょう！")

# サイドバーでの設定
st.sidebar.header("⚙️ 設定")

# プリセットボタン
st.sidebar.subheader("📋 プリセット")
preset_options = {
    "Google": "https://www.google.com",
    "YouTube": "https://www.youtube.com",
    "挨拶": "こんにちは！",
    "メール": "mailto:example@email.com"
}

selected_preset = st.sidebar.selectbox("プリセットを選択:", ["なし"] + list(preset_options.keys()))

# サイズ選択
size = st.sidebar.selectbox(
    "📐 サイズ:",
    options=[200, 300, 400, 500],
    index=1,
    format_func=lambda x: f"{x}px"
)

# 色選択
color_options = {
    "黒": "#000000",
    "青": "#667eea", 
    "紫": "#764ba2",
    "緑": "#28a745",
    "赤": "#dc3545"
}

selected_color = st.sidebar.selectbox("🎨 色:", list(color_options.keys()))
fill_color = color_options[selected_color]

# ボーダーサイズ
border = st.sidebar.slider("🖼️ ボーダーサイズ:", min_value=1, max_value=10, value=4)

# メインエリア
col1, col2 = st.columns([2, 1])

with col1:
    # テキスト入力
    if selected_preset != "なし":
        default_text = preset_options[selected_preset]
    else:
        default_text = ""
    
    text_input = st.text_area(
        "📝 テキスト・URL:",
        value=default_text,
        height=150,
        placeholder="QRコードにしたいテキストやURLを入力してください..."
    )

with col2:
    st.markdown("### 💡 ヒント")
    st.markdown("""
    - URLは https:// から始めてください
    - メールアドレスは mailto: を付けてください
    - 長いテキストも対応可能です
    - Ctrl+Enter で生成できます
    """)

# 生成ボタン
if st.button("🚀 QRコードを生成", use_container_width=True):
    if text_input.strip():
        try:
            # QRコード生成
            qr_image = create_qr_code(
                text=text_input.strip(),
                size=size,
                border=border,
                fill_color=fill_color,
                back_color="white"
            )
            
            # 結果表示
            st.markdown("---")
            st.success("✅ QRコードが生成されました！")
            
            # QRコード表示
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(qr_image, caption=f"QRコード ({size}x{size}px)")
            
            # ダウンロードリンク
            download_link = get_image_download_link(qr_image)
            st.markdown(download_link, unsafe_allow_html=True)
            
            # 生成情報
            with st.expander("📊 生成情報"):
                st.write(f"**テキスト:** {text_input[:50]}{'...' if len(text_input) > 50 else ''}")
                st.write(f"**サイズ:** {size}x{size}px")
                st.write(f"**色:** {selected_color}")
                st.write(f"**ボーダー:** {border}px")
                st.write(f"**文字数:** {len(text_input)}")
                
        except Exception as e:
            st.error(f"❌ エラーが発生しました: {str(e)}")
    else:
        st.warning("⚠️ テキストまたはURLを入力してください。")

# フッター
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
    💻 Streamlit QRコード生成ツール | 📱 スマートフォンでもQRコードをスキャンできます
</div>
""", unsafe_allow_html=True)