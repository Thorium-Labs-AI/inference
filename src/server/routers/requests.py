from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.service.chat_service import process_message
from src.service.models.InputPayloadModels import ChatRequestPayload

router = APIRouter()


@router.post("/message/", tags=["chatbot"])
async def send_message_to_chatbot(request: ChatRequestPayload):
    response = process_message(request)
    if response is None:
        raise HTTPException(status_code=404, detail="Chatbot could not retrieve a response.")
    return {"response": response}
