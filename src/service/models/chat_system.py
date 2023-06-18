from datetime import datetime


class ChatSystem:
    def __init__(self, chatbot_id, name, description, embedder, created_date=None, is_active=True):
        self.chatbot_id = chatbot_id
        self.name = name
        self.description = description
        self.is_active = is_active
        self.created_date = created_date or datetime.now().strftime("%Y-%m-%d")
        self.embedder = embedder

    def to_item(self):
        """Converts the chatbot object into a DynamoDB item."""
        return {
            "ChatbotId": self.chatbot_id,
            "Name": self.name,
            "Description": self.description,
            "IsActive": self.is_active,
            "CreatedDate": self.created_date,
            "Embedder": self.embedder
        }

    @staticmethod
    def from_item(item):
        """Creates a chatbot object from a DynamoDB item."""
        return ChatSystem(
            chatbot_id=item['ChatbotId'],
            name=item['Name'],
            description=item['Description'],
            is_active=item['IsActive'],
            created_date=item['CreatedDate'],
            embedder=item['Embedder']
        )
