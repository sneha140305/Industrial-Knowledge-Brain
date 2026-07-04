import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="industrial_documents"
)

def store_chunks(chunks, embeddings):

    ids = []

    for i in range(len(chunks)):
        ids.append(str(i))

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )