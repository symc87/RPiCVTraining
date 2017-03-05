# Program to take a picture using Webcam and display it on screen
from SimpleCV import Camera,Image,Display
import time
#Initialize the Display and Camera
disp=Display()
cap=Camera()

#Take a picture
image=cap.getImage()
#Show the picture on screen
image.save(disp)
time.sleep(5)
