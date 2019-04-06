import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("Gens/haarcascade_face.xml")
eye_cascade = cv2.CascadeClassifier("Gens/haarcascade_eye.xml")
img = cv2.imread("Assets/person.jpg")
img_gray = cv2.imread("Assets/person.jpg",0)

faces = face_cascade.detectMultiScale(img_gray, 1.3, 2)

for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
	face = img_gray[y:y+h, x:x+w]
	eyes = eye_cascade.detectMultiScale(face, 1.3, 6)
	for (x1,y1,w1,h1) in eyes:
		cv2.rectangle(img, (x+x1, y+y1), (x+x1+w1, y+y1+h1), (0,255,0), 2)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()