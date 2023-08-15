from fastapi import APIRouter, HTTPException, Depends
from fastapi_limiter.depends import RateLimiter

from src.models.InputPayloadModels import ChatRequestPayload
from src.service.chat_service import process_message

router = APIRouter()


@router.post("/message/", tags=["chatbot"], dependencies=[Depends(RateLimiter(times=50, hours=12))])
async def send_message_to_chatbot(request: ChatRequestPayload):
    response = process_message(request)
    if response is None:
        raise HTTPException(status_code=404, detail="Chatbot could not retrieve a response.")
    return {"response": response}
