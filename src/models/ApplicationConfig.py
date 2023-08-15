from pydantic import BaseModel


class AppConfig(BaseModel):
    # Redis Config
    redis_host: str
    redis_port: int
    redis_username: str
    redis_password: str

    # AWS Resources
    chatbot_s3_bucket: str
    customer_chatbots_table: str
    document_chunks_table: str
    customer_documents_table: str

    # Vector Database Config
    pinecone_index: str
    pinecone_api_key: str

    # OpenAI config
    embedding_model: str

    # OpenAI Config
    openai_api_key: str
