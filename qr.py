#############################################
#Copyright of D A R K _ Mechanic , 2021     #
#https://twitter.com/dark_mechanic          #
#https://www.youtube.com/Dark_mechanic/     #
#############################################

import qrcode
qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=5

	)

data = input('ENTER YOUR CODE : ')

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save('MyQRCode.png')
