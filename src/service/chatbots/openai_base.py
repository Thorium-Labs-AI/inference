import logging

import openai
from fastapi import HTTPException
from starlette import status

from src.server.routers.inference import ChatHistoryItem
from src.service.analytics.cost import handle_token_costs
from src.service.context_service import ContextService
from src.utils.shared import from_env


def get_openai_input(system_payload: dict[str], user_message: str, history: list[ChatHistoryItem]):
    chat_history: list[dict] = [{"role": "user" if item.isUser else "assistant", "content": item.text} for item in
                                history]

    query = {
        "role": "user",
        "content": user_message
    }

    openai_input: list[dict] = [system_payload] + chat_history + [query]

    return openai_input


class OpenAIBaseChatbot:
    def __init__(self, temperature: float = 0.1):
        self.temperature = temperature
        self.context_service = ContextService()
        openai.api_key = from_env("OPENAI_KEY", throw_err=True)

    def get_response(self, language_model: str, system_payload: dict[str], user_message: str,
                     history: list[ChatHistoryItem]):
        openai_input = get_openai_input(system_payload, user_message, history)

        try:
            res = openai.ChatCompletion.create(
                model=language_model,
                temperature=self.temperature,
                messages=openai_input
            )
        except Exception as e:
            logging.error(e)
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                detail="OpenAI connection could not be established.")

        if res.choices and res.choices[0].message:
            chat_response = res.choices[0].message
            handle_token_costs(res.usage['prompt_tokens'], res.usage['completion_tokens'],
                               model=language_model)
            if not chat_response:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                    detail="Could not process model response.")
            return chat_response.content
