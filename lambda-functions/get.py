import json
import os
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    user_id = event.get('user_id', None)
    conf_type = event.get('type', None)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])

    if user_id == '*':
        r = table.scan()
    else:
        if conf_type:
            q = Key('user_id').eq(user_id) & Key('type').eq(conf_type)
        else:
            q = Key('user_id').eq(user_id)
        r = table.query(
            KeyConditionExpression=q
        )

    return {
        'statusCode': 200,
        'items': r['Items'],
        'event': event
    }

