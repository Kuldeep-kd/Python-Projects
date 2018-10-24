#Separation of Red colored objects from set of Images
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt



images = [ "image ("+str(x)+").jpg" for x in range(7) ] # number is count of image assets

image = [cv2.imread("Assets/"+fileName) for fileName in images]


for itr in range(len(images)):


	hsv_image = cv2.cvtColor(image[itr], cv2.COLOR_BGR2HSV)
	hsv_lower = np.array([0,0,30])							#Darker Red
	hsv_upper = np.array([100,65,255])						#Brighter Red

	mask = cv2.inRange(image[itr], hsv_lower, hsv_upper)
	final = cv2.bitwise_and(image[itr],image[itr],mask=mask)	#Separate the nonRed part of Image

	final = cv2.cvtColor(final, cv2.COLOR_BGR2RGB)				#Convert images back to RGB for display
	image[itr] = cv2.cvtColor(image[itr], cv2.COLOR_BGR2RGB)	

	
	#Plotting Original Images
	plt.subplot(2, len(images), itr+1)							#plt.subplot(row, col, item)
	plt.imshow(image[itr])
	plt.xticks([])												#Hiding the Ticks and Axis
	plt.yticks([])												#Source: StackOverflow

	#Plotting Segmented Images
	plt.subplot(2, len(images), (len(images)+1)+itr)			#(len(images)+1) + itr are items in the second row > itr_max+1
	plt.imshow(final)
	plt.xticks([])
	plt.yticks([])


plt.show()

cv2.waitKey(0)
plt.close('all')
sys.exit(0)