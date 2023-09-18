from app.db.documents import storage as document_storage
from app.db.vectors import storage as vector_storage
from app.schemas.documents.delete import DocumentDeleteBody
from app.schemas.documents.insert import DocumentInsertBody
from app.services.semantic_search import embeddings
from app.services.semantic_search.preprocessing import split_text


def insert_document(body: DocumentInsertBody) -> str:

    chunks = split_text(body.content, chunk_size=body.chunk_size, sentence_overlap=body.sentence_overlap)
    document_id = document_storage.insert_document_chunks(chunks)
    chunk_embeddings = embeddings.batch_create(chunks)

    vector_storage.insert_vectors(document_id=document_id, vectors=chunk_embeddings, tenant=body.tenant)

    return document_id


def delete_document(body: DocumentDeleteBody):
    pass
