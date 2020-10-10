import cv2
import numpy as np
faceDetector = cv2.CascadeClassifier("C:/Users/User/Documents/Life/GTB/Tech Academy/Hackathon/Face Detection/Haar Files/haarcascades/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while(True):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.2, 5)
    for(x, y, w, h) in faces:
      cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    print (len(faces))
    cv2.imshow("Face", frame)
    if(cv2.waitKey(1)== ord('c')):
      break
cap.release()
