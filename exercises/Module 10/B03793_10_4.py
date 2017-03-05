from SimpleCV import Image
import time

#image Segmentation using Color Difference
img1 = Image('/home/pi/book/test_set/4.1.03.tiff')
img1.show()
time.sleep(5)

greendist=img1.colorDistance((108,139,133))

greendistbin=greendist.binarize(30).invert()
greendistbin.show()
time.sleep(5)

onlygreen = img1 - greendistbin
onlygreen.show()
time.sleep(5)
