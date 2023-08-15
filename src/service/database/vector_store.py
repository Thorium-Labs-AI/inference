import openai
import pinecone

from src.config.get_config import config
from src.models.ContextModels import OpenAIEmbeddingResponse, Chunk


class VectorStore:
    def __init__(self, batch_size=32):
        self.model = config.embedding_model
        self.batch_size = batch_size

        openai.api_key = config.openai_api_key

        pinecone.init(
            api_key=config.pinecone_api_key,
            environment="us-west4-gcp-free"
        )

    def insert_chunks(self, document_hash: str, chunks: list[Chunk]):
        if config.pinecone_index not in pinecone.list_indexes():
            pinecone.create_index(config.pinecone_index, dimension=1536)

        index = pinecone.Index(config.pinecone_index)
        chunk_embeddings = openai.Embedding.create(input=[chunk.content for chunk in chunks], engine=self.model)
        embedding_vectors = [{
            'id': f'{document_hash}-{i}',
            'values': data['embedding'],
            'metadata': {
                'document_hash': document_hash,
                'sequence_number': i
            }
        } for i, data in
            enumerate(chunk_embeddings.data)]
        index.upsert(vectors=embedding_vectors)

    def get_knn_documents(self, query: str, k: int = 1):
        embedding_response = OpenAIEmbeddingResponse(**openai.Embedding.create(input=[query], engine=self.model))
        embedding_data = embedding_response.data[0].embedding
        index = pinecone.Index(config.pinecone_index)
        res = index.query(embedding_data, top_k=k, include_metadata=True)
        return res
