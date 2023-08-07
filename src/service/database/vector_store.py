import logging

import openai
import pinecone

from src.utils.shared import from_env


class VectorStore:
    def __init__(self, batch_size=32):
        self.model = 'text-embedding-ada-002'
        self.batch_size = batch_size

        openai_api_key = from_env("OPENAI_KEY", throw_err=True)
        pinecone_api_key = from_env("PINECONE_KEY", throw_err=True)

        pinecone.init(
            api_key=pinecone_api_key,
            environment="us-west4-gcp-free"
        )

    def insert_chunks(self, chunks: list[str]):
        pass

    def insert_data(self, data: str, metadata: dict):
        if 'demo' not in pinecone.list_indexes():
            pinecone.create_index('demo', dimension=1536)

        index = pinecone.Index('demo')

        embed = self._create_embeddings(data)
        metadata.update({'text': data})
        to_upsert = zip([data], [embed], [metadata])
        index.upsert(vectors=list(to_upsert))

    def _create_embeddings(self, data: str):
        embeddings = openai.Embedding.create(input=[data], engine=self.model)
        logging.info(f"Created embedding for '{data}'")
        return embeddings['data'][0]['embedding']

    def get_knn(self, query: str):
        query_embedding = self._create_embeddings(query)
        index = pinecone.Index('demo')
        res = index.query(query_embedding, top_k=2, include_metadata=True)
        logging.info(f"Retrieved top 2 embeddings for '{query}'")
        logging.info(res)
        return res
