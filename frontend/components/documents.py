import streamlit as st
from api import get_documents, delete_document


def render_documents():

    st.subheader("📁 Document Library")

    search = st.text_input(
        "",
        placeholder="🔍 Search document..."
    )

    response = get_documents()

    if response is None:

        st.error("Backend Offline")

        return

    if response.status_code != 200:

        st.error("Unable to fetch documents.")

        return

    documents = response.json()

    if search:

        documents = [
            d for d in documents
            if search.lower() in d["filename"].lower()
        ]

    if not documents:

        st.info("No documents uploaded.")

        return

    st.caption(f"{len(documents)} document(s)")

    for document in documents:

        with st.container(border=True):

            st.markdown(
                f"**📄 {document['filename']}**"
            )

            col1, col2 = st.columns([3,1])

            with col1:

                st.success("Indexed")

            with col2:

                if st.button(
                    "🗑",
                    key=document["filename"],
                    use_container_width=True
                ):

                    response = delete_document(
                        document["filename"]
                    )

                    if response is None:

                        st.error("Backend Offline")

                    elif response.status_code == 200:

                        st.toast("Deleted")

                        st.rerun()

                    else:

                        st.error(response.text)