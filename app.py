import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Birthday Vidya", page_icon="🎁", layout="wide",
                   initial_sidebar_state="collapsed")

ASSETS = Path(__file__).parent / "assets"
MIME = {"art.jpg": "image/jpeg", "vidya.jpg": "image/jpeg", "wish.mp4": "video/mp4"}


@st.cache_data(show_spinner=False)
def build_page() -> str:
    html = (ASSETS / "index.html").read_text(encoding="utf-8")
    for name, mime in MIME.items():
        data = base64.b64encode((ASSETS / name).read_bytes()).decode()
        html = html.replace(f'src="{name}"', f'src="data:{mime};base64,{data}"')
    return html


# Hide Streamlit chrome and let the page fill the whole screen.
st.markdown(
    """
    <style>
      header, footer, #MainMenu, [data-testid="stToolbar"], [data-testid="stDecoration"] {display:none !important;}
      .stApp, [data-testid="stAppViewContainer"] {background:#0d1018;}
      .block-container {padding:0 !important; max-width:100% !important;}
      iframe {position:fixed; inset:0; width:100vw; height:100dvh; border:0;}
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(build_page(), height=800, scrolling=False)
