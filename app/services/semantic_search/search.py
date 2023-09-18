from app.db.vectors import retrieval as vector_retrieval
from app.db.documents import retrieval as document_retrieval
from app.services.semantic_search import embeddings


def query(query_text: str, tenant: str, limit: int) -> list[str]:
    query_embedding = embeddings.create(query_text)

    search_results = vector_retrieval.search(query=query_embedding, tenant=tenant, limit=limit)

    document_chunks = {}

    for result in search_results:
        metadata = result.metadata
        document_id = metadata.document_id
        chunk_id = metadata.chunk_id

        if document_chunks.get(document_id):
            document_chunks[document_id] += chunk_id
        else:
            document_chunks[document_id] = [chunk_id]

    result_chunks = []

    for document in document_chunks.keys():
        result_chunks += document_retrieval.get_document_chunks(document, document_chunks[document])

    return result_chunks
