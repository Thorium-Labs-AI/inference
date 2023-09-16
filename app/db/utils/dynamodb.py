import logging

import boto3

dynamodb_client = boto3.client("dynamodb")


def get_table(table_name: str):
    try:
        dynamodb_client.describe_table(TableName=table_name)
        dynamodb_resource = boto3.resource("dynamodb")
        return dynamodb_resource.Table(table_name)
    except Exception as e:
        logging.error(e)
        raise Exception(f"Could not retrieve table '{table_name}'")
