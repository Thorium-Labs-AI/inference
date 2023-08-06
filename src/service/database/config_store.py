from src.models.InputPayloadModels import ConfigUpsertPayload


def update_config(customer: str, payload: ConfigUpsertPayload):
    pass
    # if payload.dict(exclude_none=True) == {}:
    #     raise ValueError("Changeset is empty.")
    #
    # dynamodb = boto3.resource('dynamodb')
    #
    # table_name = 'configuration'
    # table = dynamodb.Table(table_name)
    #
    # payload_dict = payload.dict(exclude_none=True)
    #
    # update_expression = 'SET '
    # expression_attribute_values = {}
    # for key, value in payload_dict.items():
    #     update_expression += f"{key} = :{key}, "
    #     expression_attribute_values[f":{key}"] = value
    # update_expression = update_expression.rstrip(", ")
    #
    # response = table.update_item(
    #     Key={'customer': customer},
    #     UpdateExpression=update_expression,
    #     ExpressionAttributeValues=expression_attribute_values,
    #     ReturnValues='UPDATED_NEW'
    # )
    #
    # return response
