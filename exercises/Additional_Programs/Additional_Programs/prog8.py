import numpy as np
import cv2
from matplotlib import pyplot as plt

# Program for k-means clustering

X = np.random.randint(25,50,(25,2))
Y = np.random.randint(60,85,(25,2))
Z = np.vstack((X,Y))

Z = np.float32(Z)


# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Apply KMeans
ret,label,center = cv2.kmeans(Z,2,criteria,10,cv2.KMEANS_RANDOM_CENTERS)


A = Z[label.flatten()==0]
B = Z[label.flatten()==1]

# Now plot 'A' in red, 'B' in blue, 'centers' in yellow
plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c='r')
plt.scatter(center[:,0],center[:,1],s=80,c='y',marker='s')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()
