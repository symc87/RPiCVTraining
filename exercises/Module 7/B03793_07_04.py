import cv2
import numpy as np
import matplotlib.pyplot as plt

Right= cv2.imread('/home/pi/book/test_set/tsukuba-r.tif',0)
Left = cv2.imread('/home/pi/book/test_set/tsukuba-l.tif',0)

stereo_BM_state=cv2.StereoBM(preset=cv2.STEREO_BM_BASIC_PRESET,ndisparities=32,SADWindowSize=27)
output_map=stereo_BM_state.compute(Left,Right)

titles=['Left','Right','Depth Map']
output=[Left,Right,output_map]

for i in xrange(3):
	plt.subplot(1,3,i+1),plt.imshow(output[i],cmap='gray'),plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()
