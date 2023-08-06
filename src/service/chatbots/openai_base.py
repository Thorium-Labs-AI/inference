import logging
from typing import Optional

import openai
from fastapi import HTTPException
from starlette import status

from src.models.InputPayloadModels import ChatHistoryItem
from src.service.analytics.cost import handle_token_costs
from src.service.chatbots.chatbot import Chatbot
from src.service.context_service import get_system_message
from src.utils.shared import from_env


class OpenAIBaseChatbot(Chatbot):
    def __init__(self, model_name: str = "gpt-3.5-turbo", temperature: float = 0.1):
        super().__init__()

        self.model = model_name
        self.temperature = temperature
        openai.api_key = from_env("OPENAI_KEY", throw_err=True)

    def get_answer(self, question: str, history: list[ChatHistoryItem] = None, context: Optional[str] = None):
        openai_query = {
            "role": "user",
            "content": question
        }

        chat_history: list[dict] = [{"role": "user" if item.isUser else "assistant", "content": item.text} for item in
                                    history]
        messages: list[dict] = [get_system_message(question)] + chat_history + [openai_query]

        logging.info(f'Creating completion for messages: {messages}')

        try:
            res = openai.ChatCompletion.create(
                model=self.model,
                temperature=self.temperature,
                messages=messages
            )
        except Exception as e:
            logging.error(e)
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                detail="Connection to model could not be established.")

        if res.choices and res.choices[0].message:
            chat_response = res.choices[0].message
            handle_token_costs(res.usage['prompt_tokens'], res.usage['completion_tokens'],
                               self.model)
            if not chat_response:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                    detail="Could not process model response.")
            return chat_response.content
