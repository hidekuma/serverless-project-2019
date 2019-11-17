# Lambda functions
APIGateway에 연결하는 최종 Lambda함수

## get.py
### actions
- Dynamodb: get item

## post.py
### actions
- Dynamodb: put item
- SNS: publish topic

## make.py
### required
- PIL (pillow)
- qrcode

### actions
- S3: get item, put item
- SNS: subscribe topic
- Dynamodb: get item
- make output
