import logging

import boto3


def get_table(table_name: str):
    dynamodb_client = boto3.client("dynamodb")
    try:
        dynamodb_client.describe_table(TableName=table_name)
        dynamodb_resource = boto3.resource("dynamodb")
        return dynamodb_resource.Table(table_name)
    except Exception as e:
        logging.error(e)
        raise RuntimeError(f"Could not retrieve table '{table_name}'")
