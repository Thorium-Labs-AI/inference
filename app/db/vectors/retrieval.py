from app.db.utils.pinecone import index
from app.schemas.vectors.embedding import OpenAIEmbedding, PineconeMatch


def search(query: OpenAIEmbedding, tenant: str, limit: int) -> list[PineconeMatch]:
    vector = query.data[0].embedding

    response = index.query(
        vector=vector,
        filter={
            "tenant": tenant
        },
        top_k=limit,
        include_metadata=True
    )

    for match in response.matches:
        match.metadata['chunk_id'] = int(match.metadata['chunk_id'])

    matches = [PineconeMatch(id=match['id'], score=match['score'], metadata=match['metadata'], values=match['values']) for match in response.matches]

    return matches
