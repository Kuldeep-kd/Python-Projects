import cv2
import numpy as np

cp = cv2.VideoCapture("Assets/Demo.mp4")
bg_sub = cv2.createBackgroundSubtractorMOG2()

while 1:

	_, frame = cp.read()
	mask = bg_sub.apply(frame)

	#cv2.imshow("cp",frame)
	frame = cv2.resize(frame, (700,500), cv2.INTER_CUBIC)
	mask = cv2.resize(mask, (700,500), cv2.INTER_CUBIC)


	mask = cv2.bitwise_and(frame, frame , mask=mask)
	cv2.imshow("mask",mask)


	if cv2.waitKey(6) == ord("q") :
		break


cv2.destroyAllWindows()
