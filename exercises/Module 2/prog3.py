import cv2
import numpy as np
import matplotlib.pyplot as plt

# Program to load a color image in gray scale and to display using matplotlib
img = cv2.imread('/home/pi/book/test_set/lena_color_512.tif',0)
plt.imshow(img,cmap='gray')
plt.title('Lena')
plt.xticks([])
plt.yticks([])
plt.show()
