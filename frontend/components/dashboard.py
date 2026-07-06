import streamlit as st
from api import get_dashboard


def render_dashboard():

    response = get_dashboard()

    if response is None:
        st.error("❌ Unable to connect to backend.")
        return

    if response.status_code != 200:
        st.error("❌ Unable to load dashboard.")
        return

    data = response.json()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📄 Documents",
            data.get("documents", 0)
        )

        st.metric(
            "📑 Chunks Indexed",
            data.get("chunks", 0)
        )

    with col2:
        st.metric(
            "🤖 AI Model",
            data.get("ai_model", "-")
        )

        st.metric(
            "🗄️ Vector DB",
            data.get("vector_db", "-")
        )

    with col3:
        st.metric(
            "⚡ Backend",
            data.get("backend", "-")
        )

        st.metric(
            "📁 Last Upload",
            data.get("last_upload", "-")
        )