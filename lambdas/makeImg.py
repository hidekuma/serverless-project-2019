import json
import sys
from PIL import Image, ImageDraw, ImageFont
import qrcode
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    s3.meta.client.download_file('fcsw-2019', 'fonts/NotoSansMonoCJKkr-Bold.otf', '/tmp/bold.otf')
    s3.meta.client.download_file('fcsw-2019', 'imgs/logo.en.png', '/tmp/logo.png')

    records = event.get('Records', None)
    if records:
        user_id = records[0]['Sns']['Message']
        type = records[0]['Sns']['Subject']
        dynamo = boto3.resource('dynamodb')
        table = dynamo.Table('test')

        item = table.get_item(
            Key={
                "user_id": user_id,
                "type": type
            },
        )
        if item:
            item = item['Item']

    user_phone = item['user_phone']
    user_name = item['user_name']
    user_id = item['user_id']
    type = item['type']
    company_name = item['company_name']
    ttf = '/tmp/bold.otf'

    W, H = (400, 250)

    # 1) logo img
    logo = Image.open('/tmp/logo.png')

    # 2) qr code img
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=4,
    )

    qr.add_data(user_phone)
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

    key = f'qrcodes/{user_id}/{type}/qrcode.jpg'
    s3.meta.client.upload_file('/tmp/signed.jpg', 'fcsw-2019', key, ExtraArgs={'ContentType': 'image/jpeg'})

    return {
        'statusCode': 200,
        'event': event
    }

