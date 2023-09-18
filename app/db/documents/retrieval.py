from app.core.config import config
from app.db.utils.dynamodb import get_table
from boto3.dynamodb.conditions import Key


def get_document_chunks(document_id: str, chunk_ids: list[str]):
    table = get_table(config.document_chunks_table)

    content_list = []

    for chunk_id in chunk_ids:
        response = table.query(
            KeyConditionExpression=Key("document_id").eq(document_id) & Key("chunk_id").eq(chunk_id),
            ProjectionExpression='content',
            ConsistentRead=False
        )

        for item in response.get('Items', []):
            content_list.append(item['content'])

    return content_list
