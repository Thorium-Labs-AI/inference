import uuid

from boto3.dynamodb.conditions import Key

from ..utils.dynamodb import get_table
from ...core.config import config

table = get_table(config.document_chunks_table)


def insert_document_chunks(chunks: list[str]):
    document_id = uuid.uuid4()

    for chunk_id, chunk in enumerate(chunks):
        table.put_item(
            Item={
                'document_id': document_id,
                'chunk_id': chunk_id,
                'content': chunk,
            }
        )

    return {"document_id": document_id}


def delete_document(document_id: str):
    document_chunks = table.query(
        KeyConditionExpression=Key('document_id').eq(document_id)
    )

    for item in document_chunks['Items']:
        table.delete_item(
            Key={
                'document_id': item['document_id'],
                'sequence_number': item['sequence_number']
            }
        )
