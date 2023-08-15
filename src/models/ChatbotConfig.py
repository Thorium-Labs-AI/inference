from typing import Optional

from pydantic import BaseModel


class ChatbotConfig(BaseModel):
    customer_id: Optional[str]
    chatbot_id: Optional[str]
    display_name: Optional[str]
    welcome_message: Optional[str]
    task_definition: Optional[str]
    allowed_domains: Optional[list[str]]


class DynamoDBConfigResponse(BaseModel):
    Item: ChatbotConfig
