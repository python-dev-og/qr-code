import qrcode

image = qrcode.make("https://github.com/python-dev-og")
image.save("qr.png")