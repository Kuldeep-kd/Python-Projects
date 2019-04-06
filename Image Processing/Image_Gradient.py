import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Assets/image (1).jpg")


laplacian = cv2.Laplacian(image, cv2.CV_64F)  #cv2.CV_64F is a DataType
sobelx = cv2.Sobel(image, cv2.CV_64F ,1,0 , ksize=5) #k = Kernel Size
sobely = cv2.Sobel(image, cv2.CV_64F , 0,1 , ksize=5)
Canny = cv2.Canny(image, threshold1=10, threshold2=2)
# laplacian = np.uint8(np.absolute(laplacian))		#Edge Visualisation

cv2.imshow("laplacian",laplacian)
cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)
cv2.imshow("laplacian",laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()