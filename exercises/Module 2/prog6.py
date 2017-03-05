import cv2

# initialize the camera
cam = cv2.VideoCapture(0)   	# 0 -> index of camera
ret, image = cam.read()

if ret:    			# if frame is captured without any errors
    cv2.imshow('SnapshotTest',image)
    cv2.waitKey(0)
    cv2.destroyWindow('SnapshotTest')
    cv2.imwrite('/home/pi/book/output/SnapshotTest.jpg',image) #save image
