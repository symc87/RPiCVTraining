import cv2

img = cv2.imread('/home/pi/book/test_set/4.2.07.tiff')

grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

negative = abs(255-grayscale)

cv2.imshow('Original',img)
cv2.imshow('grayscale',grayscale)
cv2.imshow('Negative',negative)
#cv2.imshow('NOT',cv2.bitwise_not(grayscale))
cv2.waitKey(0)
cv2.destroyAllWindows()					
