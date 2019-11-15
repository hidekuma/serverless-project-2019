# Amazonilnux (2)
1. sudo yum update -y
2. sudo yum install python3 -y
3. pip3 install --user virtualenv
    - --user : 사용자 디렉토리에 패키지 패키지를 설치 -> sudo처럼 권한 상승 없이 패키지를 설치/사용
4. mkdir venv & cd venv
5. python3 -m virtualenv -p /usr/bin/python3 py37
6. source py37/bin/activate
7. mkdir -p ~/dist/python
8. pip3 install pillow qrcode -t ~/dist/python/
9. rm -rf ~/dist/python/__pycache__
10. zip -r output.zip ./dist/python/
11. scp -i ~/.ssh/test.pem ec2-user@{host}:~/output.zip .
