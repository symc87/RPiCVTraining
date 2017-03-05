from SimpleCV import Image
import time
img=Image('/home/pi/book/test_set/4.2.05.tiff')
img.show()
time.sleep(5)
img.grayscale().show()
time.sleep(5)
