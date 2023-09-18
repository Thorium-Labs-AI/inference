from pydantic import BaseModel


class DocumentInsertBody(BaseModel):
    content: str
    tenant: str
    chunk_size: int
    sentence_overlap: int


class DocumentInsertResponse(BaseModel):
    id: str
