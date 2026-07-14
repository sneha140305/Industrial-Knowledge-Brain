import streamlit as st
from api import ask_question

if "messages" not in st.session_state:
    st.session_state.messages = []


def show_sources(sources):
    if not sources:
        return
    st.markdown("### 📚 Sources")
    for source in sources:
        with st.container(border=True):
            st.markdown(f"#### 📄 {source.get('filename','Unknown')}")
            st.write(f"**Chunk:** {source.get('chunk','-')}")
            with st.expander("🔍 View Evidence"):
                st.code(source.get("evidence",""), language="text")


def process_question(question: str):
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    response = ask_question(question)

    if response is None:
        answer = "❌ Unable to connect to backend."
        sources = []
    elif response.status_code != 200:
        answer = response.text
        sources = []
    else:
        result = response.json()
        answer = result.get("answer", "No response.")
        sources = result.get("sources", [])

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources,
        }
    )


def render_chat():
    st.header("🤖 AI Assistant")

    _, col = st.columns([6, 1])
    with col:
        if st.button("🗑 Clear", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    if not st.session_state.messages:
        with st.container(border=True):
            st.markdown("""
# 👋 Welcome

Industrial Knowledge Brain helps you analyze:

- 📄 Manuals
- ⚠ Safety Documents
- 🛠 Maintenance Guides
- 📘 SOPs
- 📋 Inspection Reports
""")

    with st.container(border=True):
        st.subheader("💬 Ask AI")
        question = st.text_input(
            "Ask Question",
            placeholder="Example: Summarize this document...",
            key="question_input",
            label_visibility="collapsed",
        )
        if st.button("🚀 Ask AI", use_container_width=True):
            if question.strip():
                process_question(question)
                st.rerun()

    st.write("")

    with st.container(border=True):
        st.subheader("⚡ Quick Actions")

        left, right = st.columns(2)

        actions_left = [
            ("📄 Summarize Document", "Summarize the uploaded document."),
            ("🛠 Maintenance Checklist", "Generate a maintenance checklist using the uploaded document."),
            ("🛡 Compliance Check", "Analyze the uploaded document for compliance, PPE, regulations, emergency procedures and provide a compliance score."),
            ("📋 Inspection Checklist", "Generate an inspection checklist from the uploaded document."),
        ]

        actions_right = [
            ("⚠ Safety Analysis", "List all safety precautions, hazards, warnings and PPE mentioned in the uploaded document."),
            ("🔍 Explain Procedure", "Explain the maintenance procedure step by step."),
            ("🧩 Root Cause Analysis", "Perform root cause analysis and suggest corrective and preventive actions."),
            ("⚡ Risk Assessment", "Perform a risk assessment and provide mitigation recommendations."),
        ]

        with left:
            for i, (label, prompt) in enumerate(actions_left):
                if st.button(label, key=f"left_{i}", use_container_width=True):
                    process_question(prompt)
                    st.rerun()

        with right:
            for i, (label, prompt) in enumerate(actions_right):
                if st.button(label, key=f"right_{i}", use_container_width=True):
                    process_question(prompt)
                    st.rerun()

    st.write("")

    with st.container(border=True):
        st.subheader("💡 Suggested Questions")
        questions = [
            "What is this document about?",
            "Summarize the uploaded document.",
            "List all safety precautions.",
            "Explain the maintenance procedure.",
            "Which equipment is discussed?",
            "What PPE is required?",
        ]
        c1, c2 = st.columns(2)
        for i, q in enumerate(questions):
            with (c1 if i % 2 == 0 else c2):
                if st.button(q, key=f"q_{i}", use_container_width=True):
                    process_question(q)
                    st.rerun()

    st.write("")

    with st.container(border=True):
        st.subheader("💬 Conversation")
        if not st.session_state.messages:
            st.info("No conversation yet. Ask your first question above.")
        else:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
                    if message["role"] == "assistant":
                        show_sources(message.get("sources", []))

    st.markdown("---")
    st.caption("🚀 Industrial Knowledge Brain • Powered by Gemini • ChromaDB • FastAPI • Streamlit")
