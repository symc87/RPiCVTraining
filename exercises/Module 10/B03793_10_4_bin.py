from SimpleCV import Image
import time
img = Image('logo')
otsu = img.binarize()
otsu.show()
time.sleep(5)
bin = img.binarize(127)
bin.show()
time.sleep(5)