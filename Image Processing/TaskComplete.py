import cv2

vertex = []		#Vertex Data

def mouseClick(event, x,y, flag, param):	#Function for Handling Mouse Events
	if event == cv2.EVENT_LBUTTONDOWN:
		print(f"x = {x} : y = {y}")
		vertex.append((x,y))
		print(vertex)

cascade = cv2.CascadeClassifier("Gens/eye.xml")	#Getting the cascade classifier
capture = cv2.VideoCapture("Assets/FacesVideo.mp4") #Gets the Video Ready

_,img = capture.read()							  #Reads the frame
cv2.imshow("Image",img)

cv2.setMouseCallback("Image", mouseClick, img)

while not len(vertex) == 2:
	cv2.waitKey(50)

x1,y1=vertex[0]
x2,y2=vertex[1]

while 1:
	_,img = capture.read()							  #Reads the frame
	img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  #Convert to gray for faster processing
	img_gray = cv2.blur(img_gray, (30,30))			  #Blurring to remove unwanted artefacts and FalsePositives
	cv2.putText(img,"Fence", (x1,y1-10), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (255,255,255))

	cv2.rectangle(img, vertex[0], vertex[1], (0,255,0), 2)	#The Fence or ROI
	objects = cascade.detectMultiScale(img_gray[x1:x2,y1:y2],1.3,minNeighbors=2,maxSize=(70,70),minSize=(50,50)) #Get the detected objects
	
	for (x,y,w,h) in objects:	#Loop to draw rectangles over detected objects
		cv2.rectangle(img, (x+100,y+100), (x+100+w, y+100+h), (255,0,0), 2)
								#Since objects has been detected in ROI we need to shift it according to the original image

	cv2.imshow("Image",img)
	if cv2.waitKey(25) == ord("q") :	#Wait until q button is pressed with 25ms delay
		break
		
cv2.waitKey(0)
cv2.destroyAllWindows()