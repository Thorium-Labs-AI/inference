from src.service.embedders.embedder import Embedder
from openai import Embedding

class OpenAIEmbedder(Embedder):
    def __init__(self):
        super().__init__(model="text-embedding-ada-002")

    def get_embedding(self, embedding_input: list[str], user_id: str):
        return Embedding.create(
                input=embedding_input,
                engine=self.model,
                user=user_id
            )
