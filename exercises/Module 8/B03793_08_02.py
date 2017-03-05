import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/pi/book/test_set/4.2.03.tiff',1)
#color = ('b','g','r')

#for i,col in enumerate(color):
#    histr = cv2.calcHist([img],[i],None,[256],[0,256])
#    plt.plot(histr,color = col)
#    plt.xlim([0,256])
#plt.show()

input=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
histr_RED = cv2.calcHist([input],[0],None,[256],[0,256])
histr_GREEN = cv2.calcHist([input],[1],None,[256],[0,256])
histr_BLUE = cv2.calcHist([input],[2],None,[256],[0,256])

plt.subplot(221),plt.imshow(input),plt.title('Original Image'),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.plot(histr_RED,color='r'), plt.title('Red'), plt.xlim([0,256]), plt.yticks([])
plt.subplot(223),plt.plot(histr_GREEN,color='g'), plt.title('Green'), plt.xlim([0,256]), plt.yticks([])
plt.subplot(224),plt.plot(histr_BLUE,color='b'), plt.title('Blue'), plt.xlim([0,256]), plt.yticks([])
plt.show()
