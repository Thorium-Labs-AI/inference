from src.service.chatbots.openai_base import OpenAIBaseChatbot


def get_config_from_db(chatbot_id: str):
    print(f'Getting config for chatbot {chatbot_id}...')
    return 'Sample config.'


def process_message(message: str):
    print(f'Processing message: {message}...')
    chatbot = OpenAIBaseChatbot()
    return chatbot.get_answer(message)
