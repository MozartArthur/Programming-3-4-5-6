import pyqrcode
import png

def Qr(content, file_format, scale):
    
    qrcode = pyqrcode.create(content)
    if file_format == 'png':
        qrcode.png('qr1.png',scale=scale)
    elif file_format == 'svg':
        qrcode.svg('qr1.svg',scale=scale)

result = input('Cтрока: ')
Qr(result, file_format = 'png', scale = 8)