import numpy as np
import cv2

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

bg = cv2.imread('/home/pi/book/test_set/space.jpg',1)

while ( True ):
	ret, frame = cam.read()

#        cv2.imshow('Original',frame)

	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	image_mask=cv2.inRange(hsv,np.array([40,50,50]),np.array([80,255,255]))

#	cv2.imshow('Image Mask',image_mask)

	bg_mask=cv2.bitwise_and(bg,bg,mask=image_mask)

#        cv2.imshow('Background Mask',bg_mask)
			
	fg_mask=cv2.bitwise_and(frame,frame,mask=cv2.bitwise_not(image_mask))

#        cv2.imshow('Foreground Mak',fg_mask)	
	
	cv2.imshow('Output',cv2.add(bg_mask,fg_mask))

	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()
cam.release()
