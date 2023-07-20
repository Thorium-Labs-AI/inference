import logging
import os

import openai
import pinecone
from dotenv import load_dotenv


class PineconeVectorStore:
    def __init__(self, batch_size=32):
        load_dotenv()

        self.model = 'text-embedding-ada-002'
        self.batch_size = batch_size

        openai_api_key = os.environ["OPENAI_KEY"]
        pinecone_api_key = os.environ["PINECONE_KEY"]

        if len(openai_api_key) == 0:
            raise ValueError("OPENAI_KEY is not set")
        else:
            openai.api_key = openai_api_key

        if len(pinecone_api_key) == 0:
            raise ValueError("PINECONE_KEY is not set")
        else:
            pinecone.init(
                api_key=pinecone_api_key,
                environment="us-west4-gcp-free"
            )

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
