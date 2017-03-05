from SimpleCV import Image
import time
img=Image('/home/pi/book/test_set/1.5.01.tiff')
lines=img.findLines()
lines.draw(width=3)
img.show()
time.sleep(5)
