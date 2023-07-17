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

        for i in range(0, len(data)):
            i_end = min(i + self.batch_size, len(data))
            lines_batch = data[i: i + self.batch_size]
            ids_batch = [str(n) for n in range(i, i_end)]
            res = self._create_embeddings(data)
            embeds = [record['embedding'] for record in res['data']]
            meta = [metadata + {'text': line} for line in lines_batch]
            to_upsert = zip(ids_batch, embeds, meta)

            index.upsert(vectors=list(to_upsert))

        pass

    def _create_embeddings(self, data: str):
        embeddings = openai.Embedding.create(input=data, engine=self.model)
        logging.info(f"Created embedding for '{data}': [{embeddings}]")
        return embeddings
