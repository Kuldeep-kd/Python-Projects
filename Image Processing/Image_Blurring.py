#Application of Blur
import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("Assets/image (1).jpg")


hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv_lower = np.array([0,0,30])							#Darker Red
hsv_upper = np.array([100,65,255])						#Brighter Red

mask = cv2.inRange(image, hsv_lower, hsv_upper)
final = cv2.bitwise_and(image, image, mask=mask)	#Separate the nonRed part of Image


#Blur
kernel = np.ones( (4,4), np.float32) / 16
smoothImage = cv2.filter2D(final, -1, kernel)

#Gaussian
GaussianBlur = cv2.GaussianBlur(final, (15,15), 0)

#Median Blur (Best)
median = cv2.medianBlur(final, 15)

#bilateral
bilateral = cv2.bilateralFilter(final, 10, 90, 90)

cv2.imshow("Final", final)
cv2.imshow("smoothImage", smoothImage)
cv2.imshow("GaussianBlur", GaussianBlur)
cv2.imshow("median", median)
cv2.imshow("bilateral", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()