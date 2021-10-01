import qrcode


url = input("insert url here")
img = qrcode.make(url)
img.save("LookAtMeQR.jpg")
