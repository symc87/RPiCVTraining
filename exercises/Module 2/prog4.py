import cv2
import numpy as np
import matplotlib.pyplot as plot

#create black background
image = np.zeros((200,200,3), np.uint8)

#Draws a green filled circle
cv2.circle(image,(80,80),10,(0,255,0),-1)

#Draws an eclipse
cv2.ellipse(image,(99,99),(40,20),0,0,360,(128,128,128),-1)

#draw a diagonal red line with thickness of 2
cv2.line(image,(0,199),(199,0),(0,0,255),2)

#Draws a blue rectangle with thickness of border 1
cv2.rectangle(image,(20,20),(60,60),(255,0,0),1)

#Draws a polygon
points = np.array([[100,5],[125,30],[175,20],[185,10]], np.int32)
points = points.reshape((-1,1,2))
cv2.polylines(image,[points],True,(255,255,0))

#Printing the text
cv2.putText(image,'Test',(80,180), cv2.FONT_HERSHEY_DUPLEX , 1, (255,0,255))

#Displays on screen and waits for the keystroke
cv2.imshow('Shapes',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
