import streamlit as st
from api import ask_question


def render_chat():

    st.subheader("💬 AI Assistant")

    # Clear conversation button
    col1, col2 = st.columns([5, 1])

    with col2:
        if st.button("🗑️ Clear"):
            st.session_state.messages = []
            st.rerun()

    # Display previous conversation
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Show sources for assistant messages
            if message["role"] == "assistant" and "sources" in message:
                with st.expander("📚 Sources"):
                    for source in message["sources"]:
                        st.markdown(
                            f"""
**📄 {source['document']}**

Chunk: **{source['chunk']}**
---
"""
                        )

    question = st.chat_input(
        "Ask about your uploaded documents..."
    )

    if not question:
        return

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching documents..."):

            response = ask_question(question)

        if response is None:
            st.error("❌ Unable to connect to backend.")
            return

        if response.status_code != 200:
            st.error(response.text)
            return

        result = response.json()

        answer = result["answer"]

        st.markdown(answer)

        with st.expander("📚 Sources", expanded=True):

            for source in result["sources"]:

                st.markdown(
                    f"""
**📄 {source['document']}**

Chunk: **{source['chunk']}**

---
"""
                )

        # Save assistant response with sources
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": result["sources"]
            }
        )