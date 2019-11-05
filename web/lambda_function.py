import boto3
import uuid
import json
# import os

TABLE = 'runTestDB'
def lambda_handler(event, context):
    # event
    # {
        # "Records": [
            # {
                # "messageId": "7023779c-e080-48f9-b2b7-f646e339980e",
                # "receiptHandle": "AQEB/20FIb7ySoBfUQ+PM5J28Y5wRRjbJuMPNfVqaYcfyIHMYllnzKH1FQcSf3DXxcErB9tzRQvlsk1DyNbp01DGcGF5mJvxlxhM5lcDwBk/xnjG3sxRqhdUk1NrwlGLyxjkKWL7VmR13TYL7fxpIcEOqvIR1QRZBBUqCWEZE8QcHHjE8SEJY8dIQ7/zTcQfXnqGJ+khFBEee5qOglGjIOcV0hV+KWn23Wms4ZHtGxBQQWhfqlxIXO2qBWbLsGoeQfPerSfXnaaCLaVwvarO7msmgRJG71UaBM/C/vY/B4jKj30/1L/U3H4gQsqcToC62YCt5ZJD7mK8tfOUcIkHTQwSylIct/MH23i7TlvOPT00WpOgKt2yTh3GKU1GCnKgF4GB",
                # "body": "welcome",
                # "attributes": {
                    # "ApproximateReceiveCount": "1",
                    # "SentTimestamp": "1571705815262",
                    # "SenderId": "085077064225",
                    # "ApproximateFirstReceiveTimestamp": "1571705815270"
                # },
                # "messageAttributes": {},
                # "md5OfBody": "40be4e59b9a2a2b5dffb918c0e86b3d7",
                # "eventSource": "aws:sqs",
                # "eventSourceARN": "arn:aws:sqs:ap-northeast-2:085077064225:test",
                # "awsRegion": "ap-northeast-2"
            # }
        # ]
    # }
    body = None
    if 'Records' in event:
        body = event['Records'][0]['body']
    # database
    dynamo = boto3.resource('dynamodb')
    # table
    table = dynamo.Table(TABLE)

    data = {}
    if isinstance(body, str):
        try:
            body = json.d(body)
        except:
            pass
        data['body'] = body
    else:
        data = body
    data['id'] = str(uuid.uuid4())


    r = table.put_item(
        Item=data
    )

    return {
        'statusCode': 200,
        'body': body,
        'r': r
    }

