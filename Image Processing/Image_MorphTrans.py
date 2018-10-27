import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("Assets/image (1).jpg")

hsv_lower = np.array([0,0,30])
hsv_higher = np.array([100,65,255])

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(image, hsv_lower, hsv_higher)
final = cv2.bitwise_and(image, image , mask=mask)



kernel = np.array([15,15], np.uint8)
erosion = cv2.erode(final, kernel, iterations = 1)
dilation = cv2.dilate(final, kernel, iterations = 1)


MorphOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
MorphClose = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


cv2.imshow("final", final)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("MorphOpen", MorphOpen)
cv2.imshow("MorphClose", MorphClose)

cv2.waitKey(0)
cv2.destroyAllWindows()
