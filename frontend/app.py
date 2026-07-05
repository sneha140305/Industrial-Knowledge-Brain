import streamlit as st

from components.sidebar import render_sidebar
from components.dashboard import render_dashboard
from components.upload import render_upload
from components.chat import render_chat
from components.documents import render_documents

def load_css():

    with open("styles/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

if "messages" not in st.session_state:
    st.session_state.messages = []


st.set_page_config(
    page_title="Industrial Knowledge Brain",
    page_icon="🤖",
    layout="wide"
)

load_css()

render_sidebar()

st.markdown(
    """
# 🤖 Industrial Knowledge Brain

### AI-powered Assistant for Industrial Documents

Ask questions across maintenance manuals, SOPs,
inspection reports and safety documents.
"""
)

render_dashboard()

st.divider()

left, right = st.columns(
    [1.2, 2.8],
    gap="large"
)

with left:
    render_upload()

    st.divider()

    render_documents()

with right:
    render_chat()

st.divider()

st.caption(
    "Industrial Knowledge Brain • Powered by Gemini + ChromaDB + FastAPI"
)