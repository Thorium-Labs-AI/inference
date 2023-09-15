import logging

import boto3

from src.config.get_config import config
from src.models.context_models import DynamoDBChunkResponse, ChunkIdentifier, Chunk
from src.models.document_models import DocumentMetadataModel
from src.utils.aws import get_table


class DocumentStore:
    def __init__(self):
        self.dynamodb_conn = boto3.resource('dynamodb')
        self.customer_documents_table = get_table(config.customer_documents_table)
        self.document_chunks_table = get_table(config.document_chunks_table)

    def insert_document(self, customer: str, document_name: str, metadata: DocumentMetadataModel):
        logging.info(f'Inserting document record into customer documents table...')
        self.customer_documents_table.put_item(
            Item={
                'customer_id': customer,
                'document_id': document_name,
                'metadata': metadata.dict(),
            }
        )

    def insert_chunks(self, document_hash: str, chunks: list[Chunk]):
        logging.info(f'Inserting chunks into document chunks table...')
        for i, chunk in enumerate(chunks):
            self.document_chunks_table.put_item(
                Item={
                    'document_id': document_hash,
                    'sequence_number': chunk.sequence_number,
                    'metadata': chunk.metadata,
                    'chunk': chunk.content
                }
            )

    def get_document_chunk(self, chunk_identifier: ChunkIdentifier) -> str:
        dynamodb_res = self.document_chunks_table.get_item(
            Key={
                'document_id': chunk_identifier.document_hash,
                'sequence_number': chunk_identifier.sequence_number
            },
            AttributesToGet=['chunk'],
            ConsistentRead=False
        )

        return DynamoDBChunkResponse(**dynamodb_res).Item.chunk
