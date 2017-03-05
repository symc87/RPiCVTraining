#import numpy as np
import cv2

img = cv2.imread('/home/pi/book/test_set/4.2.03.tiff',1)

b,g,r = cv2.split ( img )

cv2.imshow('Blue Channel',b)
cv2.imshow('Green Channel',g)
cv2.imshow('Red Channel',r)

img=cv2.merge((b,g,r))
cv2.imshow('Merged Output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()					
