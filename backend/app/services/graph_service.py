from neo4j import GraphDatabase


class GraphService:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            "bolt://localhost:7687",
            auth=("neo4j", "password123")
        )

    def close(self):
        self.driver.close()

    def add_document_entities(
        self,
        filename,
        entities
    ):

        with self.driver.session() as session:

            session.run(
                """
                MERGE (d:Document {name:$filename})
                """,
                filename=filename
            )

            for entity in entities:

                session.run(
                    """
                    MATCH (d:Document {name:$filename})

                    MERGE (e:Entity {name:$entity})

                    MERGE (d)-[:CONTAINS]->(e)
                    """,
                    filename=filename,
                    entity=entity
                )


graph_service = GraphService()