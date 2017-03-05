import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/home/pi/book/test_set/4.1.08.tiff',0)
plt.hist(img.ravel(),256,[0,256])
plt.show()
