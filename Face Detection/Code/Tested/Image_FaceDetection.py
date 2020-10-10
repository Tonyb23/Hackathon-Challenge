import cv2

# Loading classifiers
faceCascade = cv2.CascadeClassifier('C:/Users/User/Documents/Life/GTB/Tech Academy/Hackathon/Face Detection/Haar Files/haarcascades/haarcascade_frontalface_default.xml')

# image to be scanned for faces
img = cv2.imread('C:/Users/User/Documents/Life/GTB/Tech Academy/Hackathon/Face Detection/Images/DatasetImage9.jpg')

# Converting image to gray-scale
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecting features in gray-scale 
faces = faceCascade.detectMultiScale(grey_img, 1.11, 5)

# count the number of faces detected
count_faces = str(len(faces))

# colors to show detected faces
colors = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}

if count_faces == 0:
    print ("No faces found")

else:

    # drawing rectangle around the feature and labeling it
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)

        # rectangle on image to indicate number of faces
        cv2.rectangle(img, ((0,img.shape[0] -25)),(270, img.shape[0]), (255,255,255), -1)
        cv2.putText(img, "Number of faces detected: " + str(faces.shape[0]), (0,img.shape[0] -10),
        cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0), 1)

    # print out the number of faces detected
    print ("Number of faces detected: " + count_faces)

    # show the image with the selection
    cv2.imshow('img with faces',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
