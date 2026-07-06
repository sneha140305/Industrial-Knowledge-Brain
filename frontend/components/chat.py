import streamlit as st
from api import ask_question


# =====================================================
# Display Retrieved Sources
# =====================================================

def show_sources(sources):

    if not sources:
        return

    st.markdown("### 📚 Sources")

    for source in sources:

        with st.container(border=True):

            st.markdown(f"#### 📄 {source['filename']}")

            st.write(f"**Chunk:** {source['chunk']}")

            with st.expander("🔍 View Evidence"):

                st.code(
                    source["evidence"],
                    language="text"
                )


# =====================================================
# Ask Backend
# =====================================================

def process_question(question: str):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):

            response = ask_question(question)

        if response is None:

            st.error("Unable to connect to backend.")

            return

        if response.status_code != 200:

            st.error(response.text)

            return

        result = response.json()

        answer = result["answer"]

        st.markdown(answer)

        show_sources(result["sources"])

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": result["sources"]
            }
        )


# =====================================================
# Main Chat UI
# =====================================================

def render_chat():

    st.header("🤖 AI Assistant")

    # =====================================
    # Clear Button
    # =====================================

    col1, col2 = st.columns([6, 1])

    with col2:

        if st.button(
            "🗑 Clear",
            use_container_width=True
        ):

            st.session_state.messages = []

            st.rerun()

    # =====================================
    # Welcome Card
    # =====================================

    if not st.session_state.messages:

        with st.container(border=True):

            st.markdown("""
# 👋 Welcome

Industrial Knowledge Brain is an AI-powered assistant
for industrial manuals, SOPs, maintenance guides,
inspection reports and safety documents.

### 🚀 You can ask

✅ Summarize the document

✅ Explain maintenance procedures

✅ List safety precautions

✅ Generate maintenance checklist

✅ Identify required PPE
""")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "🤖 AI",
                    "Ready"
                )

            with c2:
                st.metric(
                    "📄 Docs",
                    "PDF"
                )

            with c3:
                st.metric(
                    "⚡ Search",
                    "RAG"
                )

    st.write("")

    # =====================================
    # Ask AI Card
    # =====================================

    with st.container(border=True):

        st.subheader("💬 Ask AI")

        question = st.text_input(
            "",
            placeholder="Example: Explain the maintenance procedure...",
            label_visibility="collapsed"
        )

        if st.button(
            "🚀 Ask AI",
            use_container_width=True
        ):

            if question.strip():

                process_question(question)

                st.rerun()

            else:

                st.warning(
                    "Please enter a question."
                )

    st.write("")

    # =====================================
    # QUICK ACTIONS
    # =====================================

    with st.container(border=True):

        st.subheader("⚡ Quick Actions")

        col1, col2 = st.columns(2)

            # ================================
        # Left Column
        # ================================

        with col1:

            if st.button(
                "📄 Summarize Document",
                use_container_width=True
            ):

                process_question(
                    "Summarize the uploaded document."
                )

                st.rerun()

            if st.button(
                "🛠 Maintenance Checklist",
                use_container_width=True
            ):

                process_question(
                    "Generate a maintenance checklist using the uploaded document."
                )

                st.rerun()

        # ================================
        # Right Column
        # ================================

        with col2:

            if st.button(
                "⚠ Safety Analysis",
                use_container_width=True
            ):

                process_question(
                    "List all safety precautions, hazards, warnings and PPE mentioned in the uploaded document."
                )

                st.rerun()

            if st.button(
                "🔍 Explain Procedure",
                use_container_width=True
            ):

                process_question(
                    "Explain the maintenance procedure step by step."
                )

                st.rerun()

    st.write("")

    # =====================================
    # Suggested Questions
    # =====================================

    with st.container(border=True):

        st.subheader("💡 Suggested Questions")

        questions = [
            "What is this document about?",
            "Summarize the uploaded document.",
            "List all safety precautions.",
            "What maintenance steps are mentioned?",
            "Which equipment is discussed?",
            "What PPE is required?"
        ]

        c1, c2 = st.columns(2)

        for i, q in enumerate(questions):

            with (c1 if i % 2 == 0 else c2):

                if st.button(
                    q,
                    key=f"question_{i}",
                    use_container_width=True
                ):

                    process_question(q)

                    st.rerun()

    st.write("")

    # =====================================
    # Conversation
    # =====================================

    with st.container(border=True):

        st.subheader("💬 Conversation")

        if not st.session_state.messages:

            st.info(
                "👋 No conversation yet.\n\nAsk your first question above."
            )

        else:

            for message in st.session_state.messages:

                with st.chat_message(message["role"]):

                    st.markdown(
                        message["content"]
                    )

                    if (
                        message["role"] == "assistant"
                        and "sources" in message
                    ):

                        show_sources(
                            message["sources"]
                        )