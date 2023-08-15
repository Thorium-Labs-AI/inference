from pydantic import BaseModel

from src.models.DocumentMetadataModel import DocumentMetadataModel


class EmbeddingInsertPayload(BaseModel):
    document_name: str
    content: str
    metadata: DocumentMetadataModel


class ChunkIdentifier(BaseModel):
    document_hash: str
    sequence_number: int


class Chunk(ChunkIdentifier):
    metadata: dict
    content: str


class OpenAIEmbeddingResponse(BaseModel):
    class OpenAIEmbeddingPayload(BaseModel):
        object: str
        index: int
        embedding: list

    object: str
    data: list[OpenAIEmbeddingPayload]


class PineconeQueryResponse(BaseModel):
    class PineconeQueryPayload(BaseModel):
        id: str
        metadata: Chunk
        score: int

    matches: list[PineconeQueryPayload]


class DynamoDBChunkResponse(BaseModel):
    class DynamoDBChunkPayload(BaseModel):
        chunk: str

    Item: DynamoDBChunkPayload
