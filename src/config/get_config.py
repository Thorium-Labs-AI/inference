from src.models.ApplicationConfig import AppConfig
from src.utils.shared import from_env

llm_config = {
    "embedding_model": "text-embedding-ada-002"
}

default_config = {
    **llm_config,
    "redis_host": from_env("REDIS_HOST", throw_err=True),
    "redis_username": from_env("REDIS_USERNAME", throw_err=True),
    "redis_password": from_env("REDIS_PASSWORD", throw_err=True),
    "openai_api_key": from_env("OPENAI_KEY", throw_err=True),
    "pinecone_api_key": from_env("PINECONE_KEY", throw_err=True),
    "redis_port": 12119,
}

production_config = {
    **default_config,
    "chatbot_s3_bucket": "chatbot_frontend_configs",
    "customer_chatbots_table": "customer_chatbots",
    "document_chunks_table": "document_chunks",
    "customer_documents_table": "customer_documents",
    "pinecone_index": "embeddings"
}

development_config = {
    **default_config,
    "chatbot_s3_bucket": "chatbot_frontend_configs_dev",
    "customer_chatbots_table": "customer_chatbots_dev",
    "document_chunks_table": "document_chunks_dev",
    "customer_documents_table": "customer_documents_dev",
    "pinecone_index": "embeddings-dev"
}

configs: dict[str, AppConfig] = {
    "production": AppConfig(**production_config),
    "development": AppConfig(**development_config)
}

environment = from_env("ENVIRONMENT", throw_err=True)
config: AppConfig = configs[environment]
