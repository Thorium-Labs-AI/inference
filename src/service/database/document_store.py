import logging

import boto3

from src.models.DocumentMetadataModel import DocumentMetadataModel
from src.utils.context_utils import hash_document_chunk


class DocumentStore:
    def __init__(self):
        self.dynamodb_conn = boto3.resource('dynamodb')
        self.customer_documents_table = self.dynamodb_conn.Table('customer_documents')
        self.document_chunks_table = self.dynamodb_conn.Table('document_chunks')

    def insert_chunks(self, chunks: list[str], meta: DocumentMetadataModel):
        for i, chunk in enumerate(chunks):
            logging.info(f'Inserting chunk {chunk}')
            self.document_chunks_table.put_item(
                Item={
                    'id': hash_document_chunk(chunk_index=i, document=meta.document_name, customer=meta.customer),
                    'metadata': meta,
                    'chunk': ' '.join(chunk)
                }
            )
