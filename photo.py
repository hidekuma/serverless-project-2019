from PIL import Image, ImageDraw, ImageFont
import qrcode
user_phone = '010-4124-4444'
user_name = 'Hidekuma'
company_name = 'TestCompany.inc'
title = 'Fast Campus 2019'
ttf = './NotoSans-Regular.ttf'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=4,
    border=4,

)
qr.add_data(user_phone)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")


W, H = (300, 210)
font_s = ImageFont.truetype(ttf, 12)
font_m = ImageFont.truetype(ttf, 15)
font_b = ImageFont.truetype(ttf, 20)

img = Image.new('RGB', (W, H), color='#fff')
draw = ImageDraw.Draw(img)

draw.line((0, 0, W, 0), fill='#000')
draw.line((0, 0, 0, H), fill='#000')
draw.line((0, H-1, W, H-1), fill='#000')
draw.line((W-1, 0, W-1, H), fill='#000')

draw.text((20, 10), title, fill='#000', font=font_b)
text_size = draw.textsize(title, font=font_b)
draw.rectangle((0, text_size[1]+10, img.size[0], text_size[1]+15), fill='#000')
draw.text((20, text_size[1]+25), 'Serverless web project', fill='#000', font=font_m)
draw.line((0, text_size[1]+50, img.size[0], text_size[1]+50), fill='#000')

draw.text((130, 110), user_name, fill='#000', font=font_m)
draw.text((130, 130), f':: {company_name}', fill='#000', font=font_m)
draw.text((130, 160), f'[FULL CONFERENCE PASS]', fill='#ed244b', font=font_s)
img.paste(qr_img, (1, text_size[1]+60))

img.save('./signed.jpg')

