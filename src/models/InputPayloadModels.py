from pydantic import BaseModel


class ChatHistoryItem(BaseModel):
    isUser: bool
    text: str


class ChatRequestPayload(BaseModel):
    message: str
    history: list[ChatHistoryItem]
