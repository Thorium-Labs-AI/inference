import logging

import boto3

from src.config.get_config import config
from src.models.DocumentMetadataModel import DocumentMetadataModel
from src.utils.aws import get_table


class DocumentStore:
    def __init__(self):
        self.dynamodb_conn = boto3.resource('dynamodb')
        self.customer_documents_table = get_table(config.customer_documents_table)
        self.document_chunks_table = get_table(config.document_chunks_table)

    def insert_document(self, document_name: str, meta: DocumentMetadataModel):
        logging.info(f'Inserting document record into customer documents table...')
        self.customer_documents_table.put_item(
            Item={
                'customerID': meta.customer,
                'documentID': document_name,
                'metadata': meta.dict(),
            }
        )

    def insert_chunks(self, document_id: str, chunks: list[str], meta: DocumentMetadataModel):
        logging.info(f'Inserting chunks into document chunks table...')
        for i, chunk in enumerate(chunks):
            self.document_chunks_table.put_item(
                Item={
                    'documentID': document_id,
                    'chunkID': i,
                    'metadata': meta.dict(),
                    'chunk': chunk
                }
            )
