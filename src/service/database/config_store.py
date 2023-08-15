import boto3

from src.config.get_config import config
from src.models.ChatbotConfig import ChatbotConfig, DynamoDBConfigResponse
from src.utils.aws import get_table


class ConfigStore:
    def __init__(self):
        self.dynamodb_conn = boto3.resource('dynamodb')
        self.customer_chatbots_table = get_table(config.customer_chatbots_table)

    def update_config(self, chatbot_config: ChatbotConfig):
        self.customer_chatbots_table.put_item(
            Item=chatbot_config.dict()
        )

    def get_task_definition(self, customer_id: str = 'HardcodedCustomer', chatbot_id: str = 'my-base-chatbot'):
        dynamodb_res = self.customer_chatbots_table.get_item(
            Key={
                'customer_id': customer_id,
                'chatbot_id': chatbot_id
            },
            AttributesToGet=['task_definition'],
            ConsistentRead=False
        )

        return DynamoDBConfigResponse(**dynamodb_res).Item.task_definition
