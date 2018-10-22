import cv2

image = cv2.imread("Assets/Demo.jpg")
logo = cv2.imread("Assets/firefox.jpg")

rows,cols,channels = logo.shape #Get size of Logo Image
roi = image[0:rows, 0:cols]		#Create ROI of Image to size of Logo

logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)	#Convert to Gray for easier separation
ret, mask = cv2.threshold(logo_gray, 210, 255, cv2.THRESH_BINARY_INV)	#Separate colors rated over 210

maskInv = cv2.bitwise_not(mask)	# Inverse Mask for separation of Image area to logo

logoMasked = cv2.bitwise_and(logo, logo, mask=mask)	# Separate background of logo
ImageMasked = cv2.bitwise_and(roi ,roi, mask=maskInv) #Separate Inside of Image to logo design

final = cv2.add(logoMasked, ImageMasked) #Add both the Separated Images to one file

image[0:rows, 0:cols] = final #Set that final change to original Image

cv2.imshow(" ", image)

