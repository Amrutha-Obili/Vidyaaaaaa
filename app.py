import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Birthday Vidya",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSETS = Path(__file__).parent / "assets"
FILES = {
    "art.jpg": "image/jpeg",
    "vidya.jpg": "image/jpeg",
    "wish.mp4": "video/mp4",
}


@st.cache_data(show_spinner=False)
def build_page() -> str:
    """Read the page and inline the photos and video so nothing depends on file URLs."""
    html = (ASSETS / "index.html").read_text(encoding="utf-8")
    for name, mime in FILES.items():
        data = base64.b64encode((ASSETS / name).read_bytes()).decode()
        html = html.replace(f'src="{name}"', f'src="data:{mime};base64,{data}"')
    return html


# Remove Streamlit's chrome and make the page frame fill the screen.
st.markdown(
    """
    <style>
      header, footer, #MainMenu,
      [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"] { display: none !important; }
      html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background: #0d1018 !important; overflow: hidden !important;
      }
      .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important; max-width: 100% !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      [data-testid="stElementContainer"]:has(> [data-testid="stMarkdown"] style),
      [data-testid="stElementContainer"]:has(style) { display: none !important; }
      iframe { display: block; width: 100% !important; height: 100vh !important; height: 100dvh !important; border: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(build_page(), height=800, scrolling=True)
