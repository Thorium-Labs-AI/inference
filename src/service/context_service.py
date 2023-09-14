import logging
from hashlib import sha256

from src.models.ContextModels import Chunk, ChunkIdentifier
from src.models.DocumentMetadataModel import DocumentMetadataModel
from src.service.database.document_store import DocumentStore
from src.service.database.vector_store import VectorStore
from src.utils.text_preprocessing import create_chunk_contents


def hash_document(customer: str, document: str):
    input_string = f'{customer}-{document}'

    hash_object = sha256(input_string.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


class ContextService:
    def __init__(self):
        self.vector_store = VectorStore()
        self.document_store = DocumentStore()

    def insert_embedding(self, document_name: str, customer: str, content: str, metadata: DocumentMetadataModel):
        logging.info(f'Inserting document {document_name} for {customer}')
        clean_text = content
        chunk_contents = create_chunk_contents(clean_text, 15, 10)
        document_hash = hash_document(document=document_name, customer=customer)
        chunks: list[Chunk] = [
            Chunk(**{
                "document_hash": document_hash,
                "sequence_number": i,
                "metadata": metadata.dict(),
                "content": chunk
            }) for i, chunk in enumerate(chunk_contents)]

        self.document_store.insert_document(customer=customer, document_name=document_name, metadata=metadata)
        self.document_store.insert_chunks(document_hash, chunks)
        self.vector_store.insert_chunks(document_hash=document_hash, chunks=chunks)

    def get_knn(self, query: str, k: int = 1) -> list[str]:
        text_chunks: list[str] = []
        embedding_res = self.vector_store.get_knn_documents(query=query, k=k)
        document_chunks = [ChunkIdentifier(**chunk.metadata) for chunk in embedding_res.matches]
        for chunk in document_chunks:
            text_chunks.append(self.document_store.get_document_chunk(chunk))

        return text_chunks
