from SimpleCV import Display, Camera
import time

#Motion Detection using SimpleCV

cap=Camera()

t0=cap.getImage()

disp=Display(t0.size())

while not disp.isDone():
	t1=cap.getImage()
	dist=t1-t0

	mat=dist.getNumpy()
	mean=mat.mean()

	dist.save(disp)

	if mean>=3:
		print 'Something is crawling'

	time.sleep(0.5)
	t0=t1

