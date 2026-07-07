import streamlit as st
from api import get_dashboard


def render_dashboard():

    response = get_dashboard()

    if response is None:

        st.error("Backend Offline")

        return

    if response.status_code != 200:

        st.error("Unable to load dashboard.")

        return

    data = response.json()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📄 Documents",
            data["documents"]
        )

        st.metric(
            "📑 Chunks",
            data["chunks"]
        )

        st.metric(
            "⚙ Equipment",
            data["equipment"]
        )

    with col2:

        st.metric(
            "📏 Standards",
            data["standards"]
        )

        st.metric(
            "⚠ Risk Docs",
            data["risk_documents"]
        )

        st.metric(
            "🤖 AI",
            "Gemini"
        )

    with col3:

        st.metric(
            "🗄 Vector DB",
            "ChromaDB"
        )

        st.metric(
            "⚡ Backend",
            "Online"
        )

        st.metric(
            "📄 Last Upload",
            data["last_upload"]
        )