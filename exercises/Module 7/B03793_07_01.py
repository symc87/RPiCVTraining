import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/home/pi/book/test_set/DamagedImage.tiff')
mask = cv2.imread('/home/pi/book/test_set/Mask.tiff',0)

# converting image to RGB
input = cv2.cvtColor ( image , cv2.COLOR_BGR2RGB )

output_TELEA = cv2.inpaint(input,mask,5,cv2.INPAINT_TELEA)
output_NS = cv2.inpaint(input,mask,5,cv2.INPAINT_NS)

plt.subplot(221),plt.imshow(input),plt.title('Damaged Image'),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(mask,cmap='gray'),plt.title('Mask'),plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(output_TELEA),plt.title('Telea Method'),plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(output_NS),plt.title('Navier Stokes Method'),plt.xticks([]),plt.yticks([])
plt.show()
