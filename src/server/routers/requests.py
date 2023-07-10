from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from src.service.auth.authentication import authenticated
from src.service.chat_service import process_message

router = APIRouter()


class ChatRequest(BaseModel):
    message: str

@router.post("/message/", tags=["chatbot"])
async def send_message_to_chatbot(request: ChatRequest):
    response = process_message(request.message)
    if response is None:
        raise HTTPException(status_code=404, detail="Chatbot could not retrieve a response.")
    return {"response": response}
