from PIL import Image, ImageDraw, ImageFont
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,

)
user_phone = '010-4124-4444'
qr.add_data(user_phone)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

user_name = 'Hidekuma'
company_name = 'TestCompany.inc'

W, H = (500, 300)
img = Image.new('RGB', (W, H), color='#fff')
draw = ImageDraw.Draw(img)

title = 'Fast Campus 2019'
ttf = './SDSwaggerTTF.ttf'
font10 = ImageFont.truetype(ttf, 15)
font20 = ImageFont.truetype(ttf, 20)
font40 = ImageFont.truetype(ttf, 40)

draw.text((40, 10), title, fill='#000', font=font40)
text_size = draw.textsize(title, font=font40)

draw.rectangle((0, text_size[1]+10, img.size[0], text_size[1]+15), fill='#000')
draw.text((40, text_size[1]+25), 'Serverless web project', fill='#000', font=font20)



# w, h = draw.textsize(user_name, font=font40)
# draw.text(((W-w)/2,(H-h)/2), user_name, fill='#000', font=font40)
draw.text((250, 130), user_name, fill='#000', font=font40)
draw.text((260, 180), f'>>> {company_name}', fill='#000', font=font20)
draw.text((260, 210), f'[ FULL CONFERENCE PASS ]', fill='#ed244b', font=font20)
draw.line((0, text_size[1]+50, img.size[0], text_size[1]+50), fill='#000')
draw.line((200, 130, 200, 240), fill='#000')
img.paste(qr_img, (20, 110))

# draw.text((400, 250), 'Sponsored by paper company ', fill='#000', font=font10)

img.show()

