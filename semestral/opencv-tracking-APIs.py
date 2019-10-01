

import cv2
import sys
import argparse


print(cv2.__version__)
tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']

tracker_type = tracker_types[0]
 

#tracker = cv2.Tracker_create(tracker_type)
 
if tracker_type == tracker_types[0]:
    tracker = cv2.TrackerBoosting_create()
elif tracker_type == tracker_types[1]:
    tracker = cv2.TrackerMIL_create()
elif tracker_type == tracker_types[2]:
    tracker = cv2.TrackerKCF_create()
elif tracker_type == tracker_types[3]:
    tracker = cv2.TrackerTLD_create()
elif tracker_type == tracker_types[4]:
    tracker = cv2.TrackerMedianFlow_create()
elif tracker_type == tracker_types[5]:
    tracker = cv2.TrackerGOTURN_create()


video = cv2.VideoCapture("ibrahim.mp4")


ret, frame = video.read()
if not ret:
    sys.exit()
    


bbox = cv2.selectROI(frame, False)
ok = tracker.init(frame, bbox)


 
while True:
    # Read a new frame
    ret, frame = video.read()
    if not ret:
        break
     
    # Start timer
    timer = cv2.getTickCount()
 

    ok, bbox = tracker.update(frame)
 


    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
    # Display tracker type on frame
    cv2.putText(frame, tracker_type + " Tracker", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,255,0),2);
 

    # Display result
    cv2.imshow("Tracking", frame)
 
    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break
    
    
video.release()
cv2.destroyAllWindows()