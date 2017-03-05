import cv2
import numpy as np

img = cv2.imread('/home/pi/book/test_set/lena_color_512.tif',1)
cv2.imshow('Lena',img)
keyPress = cv2.waitKey(0)
if keyPress == ord('q'):			# If 'q' key is pressed then exit
	cv2.destroyWindow('Lena')					
elif keyPress == ord('s'):			# If 's' key is pressed then save it and exit
	cv2.imwrite('/home/pi/book/output/chapter2_prog2_output.jpg',img)
	cv2.destroyWindow('Lena')
