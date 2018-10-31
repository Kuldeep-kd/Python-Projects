import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("Assets/Bike1.jpg",1)
img2 = cv2.imread("Assets/Bike2.jpg",1)


orb = cv2.ORB_create()

kp1, desc1 = orb.detectAndCompute(img1,None)
kp2, desc2 = orb.detectAndCompute(img2,None)

bruteF = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bruteF.match(desc1,desc2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:100],None, flags=2)

plt.imshow(img3)
plt.show()