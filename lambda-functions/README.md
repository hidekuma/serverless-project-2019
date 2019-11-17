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

### layers
#### EC2 - Amazonlinux(2)
1. `sudo yum update -y`
2. `sudo yum install python3 -y`
3. `pip3 install --user virtualenv`
    - `--user` : 사용자 디렉토리에 패키지 패키지를 설치 -> sudo처럼 권한 상승 없이 패키지를 설치/사용
4. `mkdir venv & cd venv`
5. `python3 -m virtualenv -p /usr/bin/python3 py37`
6. `source py37/bin/activate`
7. `mkdir ~/python`
8. `pip3 install pillow qrcode -t ~/python/`
9. `rm -rf ~/python/__pycache__`
10. `zip -r ./output.zip ./python/`
11. `scp -i ~/.ssh/test.pem ec2-user@{host}:~/output.zip .`

#### Docker - Amazonlinux
- https://github.com/hidekuma/python-zip-of-aws-lambda-layers
```bash
git clone https://github.com/hidekuma/python-zip-of-aws-lambda-layers.git
mkdir dist
docker-compose up --build
cd dist # and show output.zip
```
### actions
- S3: get item, put item
- SNS: subscribe topic
- Dynamodb: get item
- make output
