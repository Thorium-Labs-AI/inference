from pydantic import BaseModel


class ChatHistoryItem(BaseModel):
    text: str
    isUser: bool


class ChatRequestPayload(BaseModel):
    message: str
    history: list[ChatHistoryItem]


class EmbeddingInsertionPayload(BaseModel):
    text: str
    meta: dict
