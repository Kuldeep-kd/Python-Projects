import cv2
import numpy as np

image = cv2.imread("Assets/imagered.jpg",cv2.IMREAD_COLOR)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv_lower = np.array([100,0,0])
hsv_upper = np.array([255,255,255])

mask = cv2.inRange(image, hsv_lower, hsv_upper)
final = cv2.bitwise_and(image,image,mask=mask)


cv2.imshow("image",final)  #image[:,:,0] A new method [?,?,ColorIndex]

cv2.waitKey(0)
cv2.destroyAllWindows()