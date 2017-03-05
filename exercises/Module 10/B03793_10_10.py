from SimpleCV import Image
import time
img=Image('/home/pi/book/test_set/7.1.02.tiff')
imgBin=img.binarize()
blobs=imgBin.findBlobs()
blobs.show(width=5)
time.sleep(5)
