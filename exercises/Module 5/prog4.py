import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img = cv2.imread('/home/pi/book/test_set/lena_color_512.tif',1)

input = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

output = np.zeros(input.shape,np.uint8)
p = 0.2	# probablity of noise
for i in range (input.shape[0]):
	for j in range(input.shape[1]):
		r = random.random()
		if r < p/2:
			output[i][j] = 0,0,0
		elif r < p:
			output[i][j] = 255,255,255
		else:
			output[i][j] = input[i][j]

noise_removed = cv2.medianBlur(output,3)

plt.subplot(121),plt.imshow(output),plt.title('Noisy Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(noise_removed),plt.title('Median Filtering')
plt.xticks([]), plt.yticks([])
plt.show()
