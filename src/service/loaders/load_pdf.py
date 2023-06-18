from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

class VectorDatabase:
    def __init__(self, api_key, index_name):
        pinecone.init(api_key=api_key)
        self.index_name = index_name

    def create_index(self):
        # Check if index already exists
        if self.index_name not in pinecone.list_indexes():
            pinecone.create_index(name=self.index_name, metric='euclidean')
        self.index = pinecone.Index(index_name=self.index_name)

    def upsert_vectors(self, ids, vectors):
        self.index.upsert(items=zip(ids, vectors))

    def query_vectors(self, query_vector, top_k):
        results = self.index.query(queries=[query_vector], top_k=top_k)
        return results

    def delete_index(self):
        pinecone.deinit()
        pinecone.delete_index(self.index_name)
