import pyqrcode
import png

def Qr(content, module_color, background, file_format, scale):
    
    qrcode = pyqrcode.create(content)
    if file_format == 'png':
        qrcode.png('qr2.png', module_color = module_color, background=background,scale=scale)
    elif file_format == 'svg':
        qrcode.svg('qr2.svg', module_color = module_color, background=background,scale=scale)

result = input('Cтрока: ')
Qr(result, (0,255,255), (0,0,0), file_format = 'png', scale = 8)

