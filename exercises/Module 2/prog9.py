import cv2
import numpy as np

cam = cv2.VideoCapture('/home/pi/book/output/VideoStream.avi')

while(cam.isOpened()):
    ret, frame = cam.read()
    cv2.imshow('VideoPlay',frame)
    if cv2.waitKey(25) == 27 :
        break

cam.release()
cv2.destroyAllWindows()
