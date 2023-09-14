from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.service.chatbots.openai_base import OpenAIBaseChatbot

router = APIRouter()


class ChatHistoryItem(BaseModel):
    isUser: bool
    text: str


class MessageInferencePayload(BaseModel):
    language_model: str
    instructions: str
    context: str
    message: str
    history: list[ChatHistoryItem]


chatbot = OpenAIBaseChatbot()


@router.post("/messages/", tags=["chatbot"])
async def get_chatbot_response(request: MessageInferencePayload):
    response = chatbot.get_answer(request.message, request.history)

    if response is None:
        raise HTTPException(status_code=500, detail="Chatbot could not retrieve a response.")
    return {"response": response}
