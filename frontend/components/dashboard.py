import streamlit as st

from api import get_dashboard


def render_dashboard():

    response = get_dashboard()

    if response is None:
        st.warning("Backend Offline")
        return

    if response.status_code != 200:
        return

    data = response.json()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "📄 Documents",
        data["documents"]
    )

    c2.metric(
        "🧠 Chunks",
        data["chunks"]
    )

    c3.metric(
        "⚡ Backend",
        data["backend"]
    )