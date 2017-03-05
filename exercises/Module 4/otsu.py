import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('/home/pi/book/test_set/7.1.08.tiff',0)

#changing the colorspace from  BGR->RGB

ret,output=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('Threshold',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
