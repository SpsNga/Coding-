import qrcode
url = input("Enter URL to generate QR code: ").strip()
file_path = "C://Users//yodob//Documents//qrcode.png"
qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image()
img.save(file_path)
print(f"QR code saved to {file_path}")