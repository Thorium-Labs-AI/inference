from src.service.database.pinecone import PineconeVectorStore


def insert_embedding(text: str, metadata: dict):
    vector_store = PineconeVectorStore()
    vector_store.insert_data(text, metadata)


def get_knn(query: str):
    vector_store = PineconeVectorStore()
    return vector_store.get_knn(query)
