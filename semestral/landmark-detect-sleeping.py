
import numpy as np
import collections
import cv2
import dlib
from scipy.spatial import distance as dist

def shape_to_np(shape, dtype="int"):
	# initialize the list of (x, y)-coordinates
	coords = np.zeros((68, 2), dtype=dtype)
 
	# loop over the 68 facial landmarks and convert them
	# to a 2-tuple of (x, y)-coordinates
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
 
	# return the list of (x, y)-coordinates
	return coords


def eye_ratio(eye):

	w1 = dist.euclidean(eye[1], eye[5])
	w2 = dist.euclidean(eye[2], eye[4])
	w3 = dist.euclidean(eye[1], eye[4])
	w4 = dist.euclidean(eye[2], eye[5])

	length = dist.euclidean(eye[0], eye[3])
 
	# compute the eye aspect ratio
	ratio = (w1 + w2 + w3 + w4) / (4.0 * length)
 
	return ratio
        

THRESHOLD = 0.40
COUNTER = 0

FACIAL_LANDMARKS_IDXS = collections.OrderedDict([
#	("mouth", (48, 68)),
#	("right_eyebrow", (17, 22)),
#	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
#	("nose", (27, 35)),
#	("jaw", (0, 17))
])
    

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0) #("ibrahim.mp4")

while(cap.isOpened()):
             
    ret, frame = cap.read() #read a frame 
    frame = cv2.resize(frame, (640,480)).copy()

    if ret==False:
        print("No Camera found")
        break
         
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    
    faces = detector(gray, 1)

    for (i, rect) in enumerate(faces):
        
#        cv2.rectangle(frame,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(255,0,255),2)
        
        face_length = rect.bottom()-rect.top()
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)
        
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

        startIndex = FACIAL_LANDMARKS_IDXS['left_eye'][0]
        endIndex = FACIAL_LANDMARKS_IDXS['left_eye'][1]
        leftEye = shape[startIndex:endIndex]
        
        startIndex = FACIAL_LANDMARKS_IDXS['right_eye'][0]
        endIndex = FACIAL_LANDMARKS_IDXS['right_eye'][1]
        rightEye = shape[startIndex:endIndex]
        
        leftEAR = eye_ratio(leftEye)
        rightEAR = eye_ratio(rightEye)
            
        ear = (leftEAR + rightEAR) / 2.0
#        print("leftEAR: ", leftEAR)
#        print("rightEAR: ", rightEAR)
#        print("Eye ratio: ", ear)

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        
        if ear < THRESHOLD:
            COUNTER +=1
        else :
            COUNTER = 0
         
        if COUNTER > 5 :
            print("sleeping!!!")
            cv2.putText(frame, "heyy you are sleeping", (10,50), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
	 

#    print(COUNTER)
    cv2.imshow('frame',frame)
    
        #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cv2.destroyAllWindows() #close all openCV windows   
cap.release() #release video file
 
print("System Exit")   