import numpy as np
import cv2

image=cv2.imread('/home/pi/book/test_set/test5.png',1)
input = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hor_der = cv2.Sobel(input, ddepth = -1 , dx = 1, dy = 0, ksize = 5)
ver_der = cv2.Sobel(input, ddepth = -1 , dx = 0, dy = 1, ksize = 5)

diff = cv2.subtract(hor_der, ver_der)
diff = cv2.convertScaleAbs(diff)

cv2.imshow('Difference', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()

blur = cv2.GaussianBlur(diff, (3, 3),0)

cv2.imshow('Blurred', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, th = cv2.threshold(blur, 225, 255, cv2.THRESH_BINARY)

cv2.imshow('Thresholded', th)
cv2.waitKey(0)
cv2.destroyAllWindows()

dilated = cv2.dilate(th, None, iterations = 10)

cv2.imshow('Dialation', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()

eroded = cv2.erode(dilated, None, iterations = 15)

cv2.imshow('Erosion', eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()

(contours, hierarchy) = cv2.findContours(eroded, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

areas = [cv2.contourArea(temp) for temp in contours]
max_index = np.argmax(areas)
largest_contour=contours[max_index]

x,y,width,height = cv2.boundingRect(largest_contour)
cv2.rectangle(image,(x,y),(x+width,y+height),(0,255,0),2)

cv2.imshow('Detected Barcode',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
