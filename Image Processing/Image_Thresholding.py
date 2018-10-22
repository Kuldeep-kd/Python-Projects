import numpy as np
import cv2

image = cv2.imread("Assets/Bookpage.jpg")

ret, color_thres = cv2.threshold(image, 13, 255, cv2.THRESH_BINARY)
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(ret)

ret, gray_thres = cv2.threshold(grayscale, 12, 255, cv2.THRESH_BINARY)
cv2.imshow("Window", color_thres)

gauss_thres = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19,2)
cv2.imshow("Window", gauss_thres)

cv2.waitKey(0)
cv2.destroyAllWindows()
