from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.service.chat_service import process_message, get_config_from_db

router = APIRouter()

class Message(BaseModel):
    text: str


@router.get("/")
async def get_chatbot_config(chatbot_id: str):
    chatbot_config = get_config_from_db(chatbot_id)
    if not chatbot_config:
        raise HTTPException(status_code=404, detail="Chatbot config not found.")
    return chatbot_config


@router.post("/message/", tags=["chatbot"])
async def send_message_to_chatbot(message: Message):
    response = process_message(message.text)
    if response is None:
        raise HTTPException(status_code=404, detail="Chatbot could not retrieve a response.")
    return {"response": response}
