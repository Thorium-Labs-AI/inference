import logging

import openai

from app.core.utils.environment import from_env
from app.schemas.chatbots.chat_completion import OpenAIChatCompletionResponse, OpenAIChatCompletionInput
from app.schemas.chatbots.chat_inference import ChatInferenceBody, ChatHistoryItem


class ChatCompletion:
    def __init__(self):
        openai.api_key = from_env("OPENAI_KEY", throw_err=True)
        self.temperature = 0.1

    def get_response(self, language_model: str, payload) -> str:
        try:
            response_raw = openai.ChatCompletion.create(
                model=language_model,
                temperature=self.temperature,
                messages=payload
            )

            response = OpenAIChatCompletionResponse(**response_raw)
            content = response.choices[0].message.content
            return content

        except Exception as e:
            logging.error(e)


chat_completion = ChatCompletion()


def run(body: ChatInferenceBody) -> str:
    instructions = get_system_instructions(body.instructions, body.context)
    openai_input = get_openai_input(instructions, body.message, body.history)

    response = chat_completion.get_response(body.language_model, openai_input)

    return response


def get_openai_input(system_input: OpenAIChatCompletionInput, user_message: str,
                     history: list[ChatHistoryItem]) -> list[dict]:
    chat_history = [
        OpenAIChatCompletionInput(role="user" if item.isUser else "assistant", content=item.text).dict()
        for item in history
    ]

    return [system_input.dict()] + chat_history + [OpenAIChatCompletionInput(role="user", content=user_message).dict()]


def get_system_instructions(instructions: str, context: str) -> OpenAIChatCompletionInput:
    # Since System messages are ignored more frequently, the initial instructions are in user mode.
    system_instruction = OpenAIChatCompletionInput(
        role="user",
        content=f"""
            Instructions: {instructions}
            ---
            Context: {context}
            ---
            """
    )

    return system_instruction
