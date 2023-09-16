from pydantic import BaseModel


class ChatHistoryItem(BaseModel):
    isUser: bool
    text: str


class ChatInferenceBody(BaseModel):
    language_model: str
    instructions: str
    context: str
    message: str
    history: list[ChatHistoryItem]


class ChatInferenceResponse(BaseModel):
    response: str
