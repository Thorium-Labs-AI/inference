from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.service.chatbots.chatbot import Chatbot

router = APIRouter()


class ChatHistoryItem(BaseModel):
    isUser: bool
    text: str


class MessageInferenceBody(BaseModel):
    language_model: str
    instructions: str
    context: str
    message: str
    history: list[ChatHistoryItem]


def get_system_payload(instructions: str, context: str) -> dict[str]:
    # Since System messages are more frequently ignored, the initial instructions are in user mode.
    sys_message = {
        "role": "user",
        "content": f"""
            Instructions: {instructions}
            ---
            Context: {context: str}
            ---
            """
    }

    return sys_message


inference = Chatbot()


@router.post("/messages/", tags=["chatbot"])
async def get_chatbot_response(body: MessageInferenceBody):
    system_payload = get_system_payload(instructions=body.instructions, context=body.context)
    response = inference.get_response(language_model=body.language_model,
                                      system_payload=system_payload,
                                      user_message=body.message,
                                      history=body.history)

    if response is None:
        raise HTTPException(status_code=500, detail="Chatbot could not retrieve a response.")
    return {"response": response}
