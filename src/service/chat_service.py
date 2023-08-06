from src.models.InputPayloadModels import ChatRequestPayload
from src.service.chatbots.openai_base import OpenAIBaseChatbot


def process_message(request: ChatRequestPayload):
    chatbot = OpenAIBaseChatbot()
    return chatbot.get_answer(request.message, request.history)
