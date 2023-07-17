from sqlalchemy.testing.plugin.plugin_base import logging

from src.service.chatbots.openai_base import OpenAIBaseChatbot
from src.service.database.pinecone import PineconeVectorStore
from src.service.models.InputPayloadModels import ChatRequestPayload


def get_config_from_db(chatbot_id: str):
    logging.info(f'Getting config for chatbot {chatbot_id}...')
    return 'Sample config.'


def process_message(request: ChatRequestPayload):
    chatbot = OpenAIBaseChatbot()
    return chatbot.get_answer(request.message, request.history)


def insert_embedding(text: str, metadata: dict):
    vector_store = PineconeVectorStore()
    vector_store.insert_data()