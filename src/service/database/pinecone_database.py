import pinecone

from src.service.database.database import Database


class PineconeDatabase(Database):
    def __init__(self, key: str, environment: str):
        super().__init__()
        pinecone.init(key, environment=environment)

    def create_index(self, index_name: str, index_dims: int, metric="euclidean"):
        pinecone.create_index(index_name, index_dims, metric=metric)

    def get_index(self, index_name: str):
        return pinecone.Index(index_name)

    def insert_vectors(self,  vectors: list, index_name: str):
        raise NotImplementedError("Please use subclass.")