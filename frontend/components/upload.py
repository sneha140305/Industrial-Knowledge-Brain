import streamlit as st

from api import upload_pdf


def render_upload():

    st.subheader("📄 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is None:
        return

    # File information
    file_size = uploaded_file.size / 1024

    st.info(
        f"""
**File:** {uploaded_file.name}

**Size:** {file_size:.2f} KB
"""
    )

    if st.button(
        "🚀 Upload & Index",
        use_container_width=True
    ):

        with st.spinner("📚 Reading PDF and creating embeddings..."):

            response = upload_pdf(uploaded_file)

        if response is None:
            st.error("❌ Unable to connect to backend.")
            return

        if response.status_code != 200:
            st.error(response.text)
            return

        result = response.json()

        st.success("✅ Document indexed successfully!")

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Chunks Created",
                result["chunks"]
            )

        with c2:
            st.metric(
                "Status",
                "Indexed"
            )

        st.info(
            f"**Filename:** {result['filename']}"
        )

        st.balloons()

        # Refresh the page so the uploaded
        # documents list updates automatically
        st.rerun()