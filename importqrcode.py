import qrcode

data="pchportfolio.netlify.app"

qr = qrcode.make(data)
qr.show()
qr.save("qrcode.png")