import cv2
j=0
for i in dir(cv2):
	if i.startswith('COLOR_'):
		print i
		j=j+1

print 'There are ' + str(j) + ' Colorspace Conversion flags in OpenCV'
