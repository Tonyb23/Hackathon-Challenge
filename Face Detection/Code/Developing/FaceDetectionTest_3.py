import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/User/Documents/Life/GTB/Tech Academy/Hackathon/Face Detection/Haar Files/haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread('C:/Users/User/Documents/Life/GTB/Tech Academy/Hackathon/Face Detection/Dataset/DatasetImage2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

count_faces=str(len(faces))

if len(faces) == 0:
    print ("No faces found")
 
else:
    print (faces)
    print (faces.shape)
    print ("Number of faces detected: " + str(faces.shape[0]))
 
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
 
    cv2.rectangle(img, ((0,img.shape[0] -25)),(270, img.shape[0]), (255,255,255), -1)
    cv2.putText(img, "Number of faces detected: " + str(faces.shape[0]), (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
 
    cv2.imshow('img with faces',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()