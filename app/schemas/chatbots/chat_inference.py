from typing import Optional

from pydantic import BaseModel


class ChatHistoryItem(BaseModel):
    isUser: bool
    text: str


class SemanticSearchBody(BaseModel):
    limit: int
    tenant: str


class ChatInferenceBody(BaseModel):
    language_model: str
    instructions: str
    context: str
    message: str
    semantic_search: Optional[SemanticSearchBody]
    history: list[ChatHistoryItem]


class ChatInferenceResponse(BaseModel):
    response: str
