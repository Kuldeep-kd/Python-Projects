import numpy as np
import matplotlib.pyplot as plt
import cv2

cap = cv2.VideoCapture("./Assets/Demo.jpg")

while cap.isOpened():

	ret,frame = cap.read()
	cv2.imshow("Window",frame)

	# plt.imshow(frame,cmap="gray",interpolation='bicubic')
	# plt.show()
	# This waitkey(millisecs) takes input to wait for delay of millisecs
	if (cv2.waitKey(25) == ord('q')):
		break

cap.release()
cv2.destroyAllWindows()
