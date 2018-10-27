import cv2
import numpy as np


bgr_img = cv2.imread("Assets/rca_main.jpg")
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

template = cv2.imread("Assets/template.jpg",0)
height, width = template.shape[:]


match = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.5
loc = np.where(match >= threshold)

for point in zip(*loc[::-1]):
	cv2.rectangle(bgr_img, point, (point[0]+ width, point[1] + height), (0,200,20), 1)


cv2.imshow("Image",bgr_img)
cv2.waitKey(0)
