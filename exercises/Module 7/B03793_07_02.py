import cv2
import numpy as np
import pymeanshift as pms
from matplotlib import pyplot as plt

image = cv2.imread('/home/pi/book/test_set/coins1.png',1)

#changing the colorspace from  BGR->RGB
input = cv2.cvtColor(image, cv2.COLOR_BGR2RGB )

(segmented_image, labels_image, number_regions) = pms.segment(input,spatial_radius=2,range_radius=2,min_density=300)

#print (type (segmented_image))
#print (type (labels_image))
#print (type (number_regions))

plt.subplot(131),plt.imshow(input),plt.title('Input')
plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(segmented_image),plt.title('Segmented Output')
plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.imshow(labels_image),plt.title('Labeled Output')
plt.xticks([]),plt.yticks([])
plt.show()
