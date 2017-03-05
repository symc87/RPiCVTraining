import cv2
import numpy as np

img = cv2.imread('/home/pi/book/test_set/lena_color_512.tif',cv2.IMREAD_COLOR)
cv2.imshow('Lena',img)
cv2.waitKey(0)
cv2.destroyWindow('Lena')
#cv2.destroyAllWindows()
