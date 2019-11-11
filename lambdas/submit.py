import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table('test')

    table.put_item(
        Item=event,
    )

    sns = boto3.client('sns')
    sns.publish(
        TopicArn="arn:aws:sns:ap-northeast-2:085077064225:conferenceTopic",
        Message=event['user_id'],
        Subject=event['type']
    )
    return {
        'statusCode': 200,
        'event': event
    }
