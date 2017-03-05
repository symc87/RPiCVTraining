from SimpleCV import Image
import time
img=Image('/home/pi/book/test_set/1.5.01.tiff')
img.grayscale().findCorners().show()
time.sleep(5)
