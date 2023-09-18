import pinecone

from app.core.config import config

pinecone.init(
    api_key=config.pinecone_api_key,
    environment="us-west4-gcp-free"
)

if config.pinecone_index not in pinecone.list_indexes():
    pinecone.create_index(config.pinecone_index, dimension=1536)

index = pinecone.Index(config.pinecone_index)
