from src.service.chatbots.openai_base import OpenAIBaseChatbot
from src.service.models.InputPayloadModels import ChatRequestPayload


def process_message(request: ChatRequestPayload):
    chatbot = OpenAIBaseChatbot()
    return chatbot.get_answer(request.message, request.history)
