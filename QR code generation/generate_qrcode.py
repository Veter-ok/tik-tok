import qrcode
from PIL import Image

logo = Image.open('logo.jpg')
logo = logo.resize((100, 100), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

QRcode.add_data('https://vm.tiktok.com/ZSJ7W8poo/')
QRcode.make()

QRimg = QRcode.make_image(fill_color="Black", back_color="white").convert("RGB")
pos = ((QRimg.size[0] - logo.size[0]) // 2,
		(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
QRimg.save("QR_code.png")
print("Done!")