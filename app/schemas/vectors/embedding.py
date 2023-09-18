from pydantic import BaseModel


class OpenAIEmbedding(BaseModel):
    class OpenAIEmbeddingData(BaseModel):
        object: str
        index: int
        embedding: list

    object: str
    data: list[OpenAIEmbeddingData]


class PineconeMatch(BaseModel):

    class PineconeMetadataModel(BaseModel):
        chunk_id: int
        document_id: str
        tenant: str

    id: str
    score: float
    metadata: PineconeMetadataModel
    values: list
