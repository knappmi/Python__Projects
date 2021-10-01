import qrcode


url = input("Insert URL here: ")
img = qrcode.make(url)
img.save("LookAtMeQR.jpg")
