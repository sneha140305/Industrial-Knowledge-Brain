import streamlit as st

from components.sidebar import render_sidebar
from components.dashboard import render_dashboard
from components.upload import render_upload
from components.chat import render_chat
from components.documents import render_documents


# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Industrial Knowledge Brain",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Load CSS
# -----------------------------

def load_css():
    with open("styles/style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )


load_css()


# -----------------------------
# Sidebar
# -----------------------------

render_sidebar()


# -----------------------------
# Header
# -----------------------------

st.title("🤖 Industrial Knowledge Brain")

st.caption(
    "AI-powered Retrieval-Augmented Generation (RAG) Assistant for Industrial Documents"
)

st.write(
    "Upload manuals, SOPs, maintenance guides, inspection reports and ask questions using Gemini AI."
)

st.divider()


# -----------------------------
# Dashboard
# -----------------------------

render_dashboard()

st.divider()


# -----------------------------
# Main Layout
# -----------------------------

left, right = st.columns(
    [1, 2.4],
    gap="large"
)


# =============================
# LEFT PANEL
# =============================

with left:

    with st.container(border=True):

        render_upload()

    st.write("")

    with st.container(border=True):

        render_documents()


# =============================
# RIGHT PANEL
# =============================

with right:

    with st.container(border=True):

        render_chat()

st.divider()


# -----------------------------
# Footer
# -----------------------------

st.caption(
    "Industrial Knowledge Brain • Gemini 2.5 Flash • ChromaDB • FastAPI • Streamlit"
)