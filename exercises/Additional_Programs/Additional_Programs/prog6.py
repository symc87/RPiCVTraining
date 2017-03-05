import cv2
from time import sleep

# Live Webcam stream Rotation

cam=cv2.VideoCapture(0)
w = 480
h = 320
cam.set(3,w),cam.set(4,h)

angle = 0
while(1):
	ret, image = cam.read()
	if angle == 360:
		angle=0

	M = cv2.getRotationMatrix2D((w/2,h/2),angle,1)
	rotated = cv2.warpAffine(image,M,(w,h))
	cv2.imshow('Rotating Image',rotated)
	angle=angle+1
	sleep(0.2)
	if cv2.waitKey(1) == 27 :
		break

cv2.destroyAllWindows()
