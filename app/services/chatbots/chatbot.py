import logging
from typing import List, Dict

import openai
from fastapi import HTTPException, status
from pydantic import BaseModel

from src.server.inference import ChatHistoryItem
from src.service.analytics.cost import handle_token_costs
from src.service.context_service import ContextService
from src.utils.shared import from_env

logging.basicConfig(level=logging.INFO)

# Type aliases
MessagePayload = Dict[str, str]
ChatInput = List[MessagePayload]


class OpenAIChatCompletionUsage(BaseModel):
    completion_tokens: int
    prompt_tokens: int


class OpenAIResponseMessage(BaseModel):
    content: str


class OpenAIResponseChoice(BaseModel):
    message: OpenAIResponseMessage


class OpenAIChatCompletionResponse(BaseModel):
    choices: List[OpenAIResponseChoice]
    usage: OpenAIChatCompletionUsage


def get_openai_input(system_payload: MessagePayload, user_message: str,
                     history: List[ChatHistoryItem]) -> ChatInput:
    chat_history = [
        {"role": "user" if item.isUser else "assistant", "content": item.text}
        for item in history
    ]
    return [system_payload] + chat_history + [{"role": "user", "content": user_message}]


class Chatbot:
    def __init__(self, temperature: float = 0.1):
        self.temperature = temperature
        self.context_service = ContextService()
        openai.api_key = from_env("OPENAI_KEY", throw_err=True)

    def get_response(self, language_model: str, system_payload: MessagePayload,
                     user_message: str, history: List[ChatHistoryItem]) -> str:

        openai_input = get_openai_input(system_payload, user_message, history)

        try:
            response_raw = openai.ChatCompletion.create(
                model=language_model,
                temperature=self.temperature,
                messages=openai_input
            )
            response = OpenAIChatCompletionResponse(**response_raw)
        except Exception as e:
            logging.error(f"Error connecting to OpenAI: {e}")
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                detail="OpenAI connection could not be established.")

        content = response.choices[0].message.content
        handle_token_costs(response.usage.prompt_tokens, response.usage.completion_tokens,
                           model=language_model)

        if not content:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                detail="Could not process model response.")

        return content
