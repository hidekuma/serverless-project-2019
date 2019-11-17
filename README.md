# Serverless project 2019
서버리스 웹 프로젝트 2019

## 환경
- AWS 계정
- python 3.7.4
- docker
- docker-compose

## AWS 사용 서비스 분포도
![AWS services to use](./i/aws-to-use.png)
- API Gateway
- CloudWatch
- CloudFront
- DynamoDB
- Lambda
- S3
- SNS
- IAM

## 작업내용
### Front-end
[프런트엔드 화면 구성](./front-end)
- 작업완료도에 따라 다름
    1. [화면 작성](./front-end/step1)
    2. [API 연동 완료](./front-end/step2)
    3. [작업본 정리](./front-end/step3)

### Back-end
[백엔드기능 구현](./back-end)
- API
    - GET : [get.py](./back-end/get.py)
    - POST : [post.py](./back-end/post.py)
- Make Image
    - GET : [make.py](./back-end/make.py)
