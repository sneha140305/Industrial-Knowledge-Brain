import streamlit as st

from api import get_documents, delete_document


def render_documents():

    st.subheader("📁 Uploaded Documents")

    response = get_documents()

    if response is None:
        st.error("❌ Backend is not reachable.")
        return

    if response.status_code != 200:
        st.error("Unable to fetch documents.")
        return

    documents = response.json()

    if not documents:
        st.info("📭 No documents uploaded yet.")
        return

    st.caption(f"Total Documents: {len(documents)}")

    for document in documents:

        filename = document["filename"]

        col1, col2 = st.columns([5, 1])

        with col1:
            st.markdown(f"📄 **{filename}**")

        with col2:

            if st.button(
                "🗑️",
                key=f"delete_{filename}",
                help="Delete Document"
            ):

                delete_response = delete_document(filename)

                if delete_response is None:
                    st.error("Backend unavailable.")
                    return

                if delete_response.status_code == 200:
                    st.success(f"{filename} deleted successfully.")
                    st.rerun()

                else:
                    st.error(delete_response.text)

        st.divider()