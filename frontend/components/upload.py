import streamlit as st
from api import upload_pdf


def render_upload():

    st.subheader("📤 Upload Document")

    st.caption(
        "Upload industrial manuals, SOPs, maintenance guides or safety PDFs."
    )

    uploaded_file = st.file_uploader(
        "",
        type=["pdf"]
    )

    if uploaded_file:

        st.success(f"📄 {uploaded_file.name}")

        size = uploaded_file.size / (1024 * 1024)

        st.caption(f"Size: {size:.2f} MB")

        if st.button(
            "⬆ Upload & Index",
            use_container_width=True
        ):

            with st.spinner("Indexing document..."):

                response = upload_pdf(uploaded_file)

            if response is None:

                st.error("Unable to connect to backend.")

                return

            if response.status_code != 200:

                st.error(response.text)

                return

            result = response.json()

            st.success("✅ Document Indexed Successfully")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Chunks",
                    result["chunks"]
                )

            with col2:

                st.metric(
                    "Status",
                    "Ready"
                )

            st.balloons()