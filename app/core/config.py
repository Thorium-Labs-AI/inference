from enum import Enum

from pydantic import BaseModel, ValidationError

from app.core.utils.environment import from_env


class AppConfig(BaseModel):
    document_chunks_table: str
    documents_table: str
    pinecone_index: str
    pinecone_api_key: str
    embedding_model: str
    openai_api_key: str


class Environment(Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"


def get_config_for_env(env: Environment) -> AppConfig:
    base_config = {
        "embedding_model": "text-embedding-ada-002",
        "openai_api_key": from_env("OPENAI_KEY", throw_err=True),
        "pinecone_api_key": from_env("PINECONE_KEY", throw_err=True),
    }

    if env == Environment.PRODUCTION:
        specific_config = {
            "document_chunks_table": "document_chunks",
            "documents_table": "customer_documents",
            "pinecone_index": "embeddings"
        }
    elif env == Environment.DEVELOPMENT:
        specific_config = {
            "document_chunks_table": "document_chunks_dev",
            "documents_table": "customer_documents_dev",
            "pinecone_index": "embeddings-dev"
        }
    else:
        raise ValueError(f"Unsupported environment: {env}")

    return AppConfig(**base_config, **specific_config)


try:
    environment = Environment(from_env("ENVIRONMENT", throw_err=True))
    config = get_config_for_env(environment)
except ValidationError as e:
    raise RuntimeError(f'Cannot set environment to {from_env("ENVIRONMENT", throw_err=True)}')
    pass
