import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("Assets/Demo.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("Window",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(image,cmap='gray',interpolation='bicubic')
plt.plot([10,100],[199,200],'c',linewidth=5)
plt.show()

