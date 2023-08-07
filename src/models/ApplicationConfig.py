from pydantic import BaseModel


class AppConfig(BaseModel):
    redis_host: str
    redis_port: int
    redis_username: str
    redis_password: str
    chatbot_s3_bucket: str
    chatbot_config_table: str
    document_chunks_table: str
    customer_documents_table: str
