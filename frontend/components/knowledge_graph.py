import streamlit as st
import networkx as nx
from pyvis.network import Network
import tempfile
import streamlit.components.v1 as components

from api import get_documents


def render_knowledge_graph():

    st.subheader("🕸 Knowledge Graph")

    response = get_documents()

    if response is None:
        st.error("Unable to connect to backend.")
        return

    if response.status_code != 200:
        st.error("Unable to fetch documents.")
        return

    docs = response.json()

    if not docs:
        st.info("Upload documents to generate the graph.")
        return

    G = nx.Graph()

    for doc in docs:

        filename = doc["filename"]

        G.add_node(
            filename,
            color="red",
            size=30
        )

        # Placeholder relationships
        entities = [
            "Maintenance",
            "Safety",
            "Inspection",
            "PPE"
        ]

        for entity in entities:

            G.add_node(
                entity,
                color="skyblue",
                size=20
            )

            G.add_edge(
                filename,
                entity
            )

    net = Network(
        height="650px",
        width="100%",
        bgcolor="#ffffff",
        font_color="black"
    )

    net.from_nx(G)

    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".html"
    )

    net.save_graph(tmp.name)

    with open(tmp.name, "r", encoding="utf-8") as f:

        components.html(
            f.read(),
            height=650,
            scrolling=True
        )