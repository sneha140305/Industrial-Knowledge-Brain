import streamlit as st

from api import compare_documents


def render_comparison():

    st.header("📑 AI Document Comparison")

    file1 = st.file_uploader(
        "Document A",
        type=["pdf"],
        key="compare1"
    )

    file2 = st.file_uploader(
        "Document B",
        type=["pdf"],
        key="compare2"
    )

    if file1 and file2:

        if st.button(
            "⚖ Compare Documents",
            use_container_width=True
        ):

            with st.spinner("Comparing..."):

                response = compare_documents(
                    file1,
                    file2
                )

            if response is None:

                st.error("Backend Offline")

                return

            if response.status_code != 200:

                st.error(response.text)

                return

            st.markdown(
                response.json()["comparison"]
            )