import streamlit as st

def render_sidebar():

    with st.sidebar:

        st.markdown("# 🤖")

        st.title("Industrial Knowledge Brain")

        st.divider()

        st.success("🟢 Backend Connected")

        st.markdown("## Features")

        st.markdown("📄 PDF Upload")

        st.markdown("🧠 Gemini AI")

        st.markdown("🔍 Semantic Search")

        st.markdown("📚 ChromaDB")

        st.markdown("💬 AI Chat")

        st.divider()

        st.caption("Version 1.0")