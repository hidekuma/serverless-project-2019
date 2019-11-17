import json
from PIL import Image, ImageDraw, ImageFont
import qrcode
import boto3
import os

def lambda_handler(event, context):
    # 1) s3 -> download -> font, img -> tmp
    s3 = boto3.resource('s3')
    s3.Bucket(os.environ['BUCKET_NAME']).download_file('fonts/{font_name}.otf', '/tmp/font.otf')
    s3.Bucket(os.environ['BUCKET_NAME']).download_file('imgs/{logo_name}.png', '/tmp/logo.png')

    # 2) records -> get -> table -> getitem
    records = event['Records']
    if records:
        user_id = records[0]['Sns']['Message']
        conf_type = records[0]['Sns']['Subject']

        # 3) dynamodb get
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.environ['TABLE_NAME'])
        r = table.get_item(
            Key={
                'user_id': user_id,
                'type': conf_type
            }   
        )
        item = r['Item']
        phone_number = item.get('phone_number', '')
        company_name = item.get('company_name', '')
        user_name = item.get('user_name', '')


        # 4) image build
        W, H = (400, 250)

        # 1) logo img
        logo = Image.open('/tmp/logo.png')
        ttf = '/tmp/font.otf'


        # 2) qr code img
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=4,
            border=4,
        )

        qr.add_data(phone_number)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # 3) merge
        img = Image.new('RGB', (W, H), color='#fff')
        img.paste(logo, (15, 15), logo)
        img.paste(qr_img, (15, 100))

        # 4) draw
        font_m = ImageFont.truetype(ttf, 15)
        font_b = ImageFont.truetype(ttf, 20)
        font_B = ImageFont.truetype(ttf, 22)

        draw = ImageDraw.Draw(img)

        draw.text((150, 110), user_name, fill='#000', font=font_b)
        draw.text((150, 140), f'From {company_name}', fill='#000', font=font_m)

        draw.rectangle((145, 170, 375, 205), fill='#f0f0f0')
        draw.text((150, 170), 'FULL CONFERENCE PASS', fill='#ed244b', font=font_B)

        img.save(f'/tmp/signed.jpg', quality=100)

        key = f'qrcodes/{user_id}/{conf_type}/qrcode.jpg'
        s3.meta.client.upload_file('/tmp/signed.jpg', os.environ['BUCKET_NAME'], key, ExtraArgs={'ContentType':'image/jpeg'})


    return {
        'statusCode': 200,
        'event': event
    }

