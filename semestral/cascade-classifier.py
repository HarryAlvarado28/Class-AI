
import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture("ibrahim.mp4") #Open video file

while(cap.isOpened()):
             
    ret, frame = cap.read() #read a frame  
    if ret==False:
        print("No Camera found")
        break
         
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)   

    for (x1,y1,w1,h1) in faces:
        cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(255,0,255),2)


    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)   

    for (x1,y1,w1,h1) in eyes:
        cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(255,0,255),2)  
        
    cv2.imshow('frame',frame)
    
        #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release() #release video file
cv2.destroyAllWindows() #close all openCV windows    
print("System Exit")   