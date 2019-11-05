from PIL import Image, ImageDraw, ImageFont
import qrcode
type = 'Serverless web project'
user_phone = '010-4124-4444'
user_name = '히데쿠마'
user_id = 'hidekuma'
company_name = 'TestCompany.inc'
ttf = './web/fonts/NotoSansMonoCJKkr-Bold.otf'

W, H = (400, 250)

# 1) logo img
logo = Image.open('./web/imgs/logo.en.resized.png')

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

pass_type = 'FULL CONFERENCE PASS'
draw.text((150, 110), user_name, fill='#000', font=font_b)
draw.text((150, 140), f'From {company_name}', fill='#000', font=font_m)

draw.rectangle((145, 170, 375, 205), fill='#f0f0f0')

draw.text((150, 170), pass_type, fill='#ed244b', font=font_B)
img.save(f'/tmp/signed.jpg', quality=100)
# img.save(f'./signed.jpg', quality=100)
# img.show()

