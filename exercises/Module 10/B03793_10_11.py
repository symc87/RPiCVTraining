from SimpleCV import *
import time

print 'Displaying Candidate Image'
candidate = Image ('/home/pi/book/test_set/mypy.png')
candidate.show()
time.sleep(7)

print 'Displaying Background Image'
lake = Image ('/home/pi/book/test_set/lake.tif')
lake.show()
time.sleep(7)

print 'Apply and display mask'
mask=candidate.hueDistance(color=Color.GREEN).binarize()
mask.show()
time.sleep(7)

print 'Chroma Key Effect'
output=(lake - mask.invert()) + (candidate-mask)
output.show()
time.sleep(7)
