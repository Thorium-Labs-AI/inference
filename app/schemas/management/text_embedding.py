from pydantic import BaseModel


class OpenAIEmbeddingResponse(BaseModel):
    class OpenAIEmbeddingPayload(BaseModel):
        object: str
        index: int
        embedding: list

    object: str
    data: list[OpenAIEmbeddingPayload]
