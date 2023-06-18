from src.service.database.database import Database
import chromadb
from chromadb.config import Settings
from langchain.vectorstores import Chroma


class ChromaDatabase(Database):

    def __init__(self, embedder, host: str = "localhost", port: int = 5700):
        super().__init__()
        self.embedder = embedder
        self.client = chromadb.Client(Settings(chroma_api_impl="rest",
                                               chroma_server_host=host,
                                               chroma_server_http_port=port
                                               ))
        self.langchain_store = Chroma(client=self.client)

    def create_index(self, index_name: str, index_dims: int, metric: str):
        db_collection = self.client.get_collection(name=index_name, embedding_function=self.embedder)

        if db_collection is not None:
            self.client.create_collection(name=index_name, embedding_function=self.embedder)

    def delete_index(self, index_name: str):
        try:
            self.client.delete_collection(name=index_name)
        except Exception as err:
            print(err)
            raise err

    def get_index(self, index_name: str):
        return self.client.get_collection(name=index_name)

    def insert_vectors(self, vectors: list, index_name: str):
        pass
