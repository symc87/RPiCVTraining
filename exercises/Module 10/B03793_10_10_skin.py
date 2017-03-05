from SimpleCV import Image, Camera

cam = Camera()
while 1:
	img=cam.getImage()
	skin =img.findSkintoneBlobs()

	if skin:
		for i in skin:
			print i.centroid()
		skin.draw(), skin.show()
	else:	
		print "No Skin detected"	

		