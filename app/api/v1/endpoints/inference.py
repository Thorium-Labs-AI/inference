from fastapi import APIRouter

from app.schemas.chatbots.chat_inference import ChatInferenceBody, ChatInferenceResponse
from app.services.chatbots import inference

router = APIRouter()


@router.post("/messages/")
async def run_chat_inference(body: ChatInferenceBody) -> ChatInferenceResponse:
    chat_message = inference.run(body)
    return ChatInferenceResponse(response=chat_message)
