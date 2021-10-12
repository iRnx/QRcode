import qrcode

imagem_qrcode = qrcode.make('https://github.com/iRnx')
imagem_qrcode.save('qrcode_python.png')

# pip install python-barcode
# pip install pillow
# pip install qrcode
