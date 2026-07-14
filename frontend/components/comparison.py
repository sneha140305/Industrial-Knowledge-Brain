import streamlit as st

from api import (
    compare_documents,
    get_documents
)


def render_comparison():

    st.subheader("📑 Compare Documents")

    response = get_documents()

    if response is None:
        st.error("Unable to connect to backend.")
        return

    if response.status_code != 200:
        st.error("Unable to fetch documents.")
        return

    docs = response.json()

    if len(docs) < 2:
        st.info("Upload at least two documents.")
        return

    filenames = [
        doc["filename"]
        for doc in docs
    ]

    col1, col2 = st.columns(2)

    with col1:

        document1 = st.selectbox(
            "Document 1",
            filenames
        )

    with col2:

        remaining = [
            f for f in filenames
            if f != document1
        ]

        document2 = st.selectbox(
            "Document 2",
            remaining
        )

    if st.button(
        "🔍 Compare Documents",
        use_container_width=True
    ):

        with st.spinner(
            "Comparing documents..."
        ):

            response = compare_documents(
                document1,
                document2
            )

        if response is None:

            st.error(
                "Unable to connect to backend."
            )

            return

        if response.status_code != 200:

            st.error(response.text)

            return

        result = response.json()

        st.success(
            "Comparison Complete"
        )

        st.markdown(
            result["summary"]
        )