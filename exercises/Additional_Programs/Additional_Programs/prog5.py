import cv2

# Upscaling and downscaling an image

img = cv2.imread('/home/pi/book/test_set/house.tiff',1)
UpScale = cv2.resize(img,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
DownScale = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

cv2.imshow('UpScale',UpScale)
cv2.waitKey(0)
cv2.imshow('DownScale',DownScale) 
cv2.waitKey(0)
cv2.destroyAllWindows()
