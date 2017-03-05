import sys
import cv2
import numpy as np
from scipy.ndimage import label
from matplotlib import pyplot as plt

# Program for Watershed algorithm

image = cv2.imread('/home/pi/book/test_set/coins2.png',1)

# converting image to RGB
input = cv2.cvtColor ( image , cv2.COLOR_BGR2RGB )

# Pre processing
gray = cv2.cvtColor ( input , cv2.COLOR_BGR2GRAY )

ret1 , bin_image = cv2.threshold ( gray , 0 , 255 , cv2.THRESH_OTSU )
bin_image = cv2.morphologyEx ( bin_image , cv2.MORPH_OPEN, np.ones((3,3),dtype=int) )

border = cv2.dilate(bin_image, None, iterations=5 )
border = border - cv2.erode(border, None)

dt = cv2.distanceTransform(bin_image,2,3)
dt = ((dt-dt.min())/(dt.max()-dt.min())*255).astype(np.uint8)
ret2,dt=cv2.threshold(dt,180,255,cv2.THRESH_BINARY)

lbl,ncc = label(dt)
lbl = lbl * (255/ncc)
lbl[border == 255 ] = 255

lbl = lbl.astype(np.int32)
cv2.watershed(input,lbl)

lbl[lbl==-1]=0
lbl=lbl.astype(np.uint8)
output = 255-lbl

output [output!=255]=0
output =cv2.dilate(output,None)

water_shed=input.copy()
water_shed[output==255]=(0,0,255)

plt.subplot(121),plt.imshow(input),plt.title('Input')
plt.subplot(122),plt.imshow(water_shed),plt.title('Watershed')
plt.show()
