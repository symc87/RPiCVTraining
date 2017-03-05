#import numpy as np
import cv2

img1 = cv2.imread('/home/pi/book/test_set/4.2.03.tiff',1)
img2 = cv2.imread('/home/pi/book/test_set/4.2.04.tiff',1)
#output=cv2.subtract(img1,img2)
#output = cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('Image1',img1)
cv2.waitKey(0)
cv2.imshow('Image2',img2)
cv2.waitKey(0)
cv2.imshow('Addition',cv2.add(img2,img1))
cv2.waitKey(0)
cv2.imshow('Weighted Addition',cv2.addWeighted(img1,0.5,img2,0.5,0))
cv2.waitKey(0)
cv2.imshow('Image1-Image2',cv2.subtract(img1,img2))
cv2.waitKey(0)
cv2.imshow('Image2-Image1',cv2.subtract(img2,img1))
cv2.waitKey(0)
cv2.destroyAllWindows()					

