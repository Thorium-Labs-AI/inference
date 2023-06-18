import os
from dotenv import load_dotenv
from typing import Optional

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from src.service.chatbots.chatbot import Chatbot


class OpenAIBaseChatbot(Chatbot):
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        super().__init__()

        load_dotenv()

        api_key = os.environ["OPENAI_KEY"]
        if len(api_key) == 0:
            raise ValueError("OPENAI_KEY is not set")

        self.llm = ChatOpenAI(
            temperature=0,
            openai_api_key=api_key,
            model_name=model_name
        )

        self.conv_chain = ConversationChain(llm=self.llm)

    def get_answer(self, question: str, context: Optional[str] = None):
        return self.conv_chain(question)