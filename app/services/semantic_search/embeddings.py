import openai

from app.core.config import config
from app.schemas.vectors.embedding import OpenAIEmbedding


openai.api_key = config.openai_api_key


def batch_create(chunks: list[str]) -> OpenAIEmbedding:
    response = OpenAIEmbedding(**openai.Embedding.create(
        input=chunks,
        engine=config.embedding_model
    ))

    return response


def create(text: str) -> OpenAIEmbedding:
    response = OpenAIEmbedding(**openai.Embedding.create(
        input=[text],
        engine=config.embedding_model
    ))

    return response
