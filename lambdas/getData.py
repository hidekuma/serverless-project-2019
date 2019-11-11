import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table('test')

    if event['user_id'] == '*':
        items = table.scan()
    else:
        fe = Key('user_id').eq(event['user_id']) & Key('type').eq(event['type'])
        items = table.query(
            KeyConditionExpression=fe
        )
    return {
        'statusCode': 200,
        'items': items['Items']
    }

