import numpy as np
import matplotlib.pyplot as plt
import cv2

for x in range(100):
	image = cv2.imread("Assets/Demo.jpg")

	cv2.rectangle(image, (20,20),(100,100), (255,x,100+x),-1)# Negative values of colors are for filling the poly form inside
	cv2.line(image, (x,10), (200,x), (233,233,233), 1)
	cv2.circle(image, (300,300) , x, (233,233,0), 2)
	polypts = np.array( [[10,10],[10,30],[200,70],[60,10],[30,10],[70,100]], np.int32)
	cv2.polylines(image, [polypts], False, (233,233,233),6)

	cv2.imshow("", image)
	# plt.imshow(image)
	# plt.show()
	cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()
