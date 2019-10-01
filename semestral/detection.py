# import the necessary packages
from imutils import paths
import imutils
import cv2
import numpy as np 
cam = cv2.VideoCapture(0) 
kernel = np.ones((4,4),np.uint8)




#---------------

def find_marker(image):
	# convert the image to grayscale, blur it, and detect edges
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)

	# find the contours in the edged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv2.contourArea)

	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)


def distance_to_camera(knownWidth, focalLength, perWidth):
    # compute and return the distance from the maker to the camera
	dc = (knownWidth * focalLength) / perWidth
	print("DC-",dc," = (knownWidth -",knownWidth,"* focalLength -",focalLength, ") / perWidth-",perWidth)

	return dc

# initialize the known distance from the camera to the object, which
# in this case is 24 inches
KNOWN_DISTANCE = 24.0
 
# initialize the known object width, which in this case, the piece of
# paper is 12 inches wide
KNOWN_WIDTH = 11.0

# def focalLength(frame):
# 	marker = find_marker(frame)
# 	focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
# 	print("focalLength:: ",focalLength,"= (marker[1][0] -", marker[1][0], "* KNOWN_DISTANCE -", KNOWN_DISTANCE, " ) / KNOWN_WIDTH -", KNOWN_WIDTH)
# 	# print(focalLength)
# 	return focalLength
    	

#---------------



while (True):
	ret,frame = cam.read()
	## Como verde
	### La paleta de colore es: BGR:[Blue,Green,Red]
	# rangomax = np.array([50,255,50]) 
	# rangomin = np.array([0,51,0])
	## Como Rojo
	# rangomax = np.array([244,66,50])
	# rangomin = np.array([51,0,0])
	## Como Azul
	# rangomax = np.array([84,234,205])
	# rangomin = np.array([47,135,118])
	# mascara = cv2.inRange(frame, rangomin, rangomax)
	# opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
	# x,y,w,h = cv2.boundingRect(opening)
	# # print("Adelante")
	# cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
	# cv2.circle(frame,(x+int(w/2),y+int(h/2)),6,(0,0,100),-1)
	# image_np = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# print(image_np)
	image = frame

	
	# print("marker[1][0] -> ",marker[1][0])
	# print("focalLength  -> ",focalLength)
	
	marker = find_marker(image)
	# print("focalLength(image) -> ",focalLength(image))
	
	# marker = find_marker(frame)
	focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

	inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])

	print("inches -> ",inches)
 
	# draw a bounding box around the image and display it
	box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
	box = np.int0(box)
	# print("box -> ",box)
	cv2.drawContours(image, [box], -1, (100, 255, 0), 2)
	# print("image -> ", image)
	cv2.putText(image, "%.2fft" % (inches / 12),(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 255), 3)
	cv2.imshow("image", image)
	# cv2.waitKey(0)

	# cv2.imshow('camara' ,image)
	cv2.waitKey(1)
	# k = cv2.waitKey(1) & 0xFF
	# print (k)
	# if k==28:
	# 	print("Dentro del IIFFIFIFIFIFIF")
	# 	break