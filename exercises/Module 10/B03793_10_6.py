# Histogram
from SimpleCV import Image
from matplotlib import pyplot as plt

img = Image('/home/pi/book/test_set/4.2.06.tiff')

(r,g,b)=img.splitChannels(False)

plt.subplot(311)
plt.plot(r.histogram(255),color='r')
plt.title('Red Histogram')
plt.xlim([0,256]), plt.yticks([])

plt.subplot(312)
plt.plot(g.histogram(255),color='g')
plt.title('Green Histogram')
plt.xlim([0,256]), plt.yticks([])

plt.subplot(313)
plt.plot(b.histogram(255),color='b')
plt.title('Blue Histogram')
plt.xlim([0,256]), plt.yticks([])

plt.show()