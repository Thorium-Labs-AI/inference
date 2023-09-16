from app.core.config import config
from app.db.utils.dynamodb import get_table


def get_document_chunks(document_id: str, chunk_ids: list[str]):
    table = get_table(config.document_chunks_table)

    chunks = table.query(
        Key={
            "document_id": document_id,
            "sequence_number": chunk_ids
        },
        AttributesToGet=['content'],
        ConsistentRead=False
    )

    return chunks
