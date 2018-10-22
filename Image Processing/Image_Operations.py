import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("Assets/Demo.jpg")

#image[0:100,] = image[0:100, 50:100]

# Car Coords = # Car Coords = 142:220, 80:130
image[0:78, 0:50] =  image[142:220, 80:130]

cv2.imshow("image", image)

# plt.imshow(image)
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
