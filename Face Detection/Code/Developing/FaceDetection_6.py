import cv2

# Loading classifiers
faceCascade = cv2.CascadeClassifier('C:/Users/User/Documents/Life/GTB/Tech Academy/Hackathon/Face Detection/Haar Files/haarcascades/haarcascade_frontalface_default.xml')

# image to be scanned for faces
img = cv2.imread('C:\Users\User\Documents\Life\GTB\Tech Academy\Hackathon\Face Detection\Images\DatasetImage4.jpg')

# Converting image to gray-scale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecting features in gray-scale 
faces = faceCascade.detectMultiScale(gray_img, 1.3, 5)

# count the number of faces detected
count_faces = str(len(faces))

# colors to show detected faces
colors = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}

# user to define whether to scan image or use webcam
Option = input("Choose a detection option, 1 for image scanning or 2 for webcam scanning:\n")

# Option 1: Scanning an image
if Option == 1:

    if count_faces == 0:
        print ("No faces found")

    else:

        # drawing rectangle around the feature and labeling it
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.rectangle(img, ((0,img.shape[0] -25)),(270, img.shape[0]), (255,255,255), -1)
            cv2.putText(img, "Number of faces detected: " + str(faces.shape[0]), (0,img.shape[0] -10),
            cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0), 1)

        # print out the number of faces detected
        print ("Number of faces detected: " + count_faces)

        # show the image with the selection
        cv2.imshow('img with faces',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# # Option 2: Running a webcam
# elif Option == 2:

#     video_capture = cv2.VideoCapture(0)

#     while(True):

#         _, frame = video_capture.read()

#         # Converting image to gray-scale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # detecting features in gray-scale 
#         faces = faceCascade.detectMultiScale(gray, 1.2, 5)

#         # drawing rectangle around the feature and labeling it
#         for(x, y, w, h) in faces:
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#             cv2.rectangle(frame, ((0,frame.shape[0] -25)),(270, frame.shape[0]), (255,255,255), -1)
#             cv2.putText(frame, "Number of faces detected: " + str(faces.shape[0]), (0,frame.shape[0] -10),
#             cv2.FONT_HERSHEY_DUPLEX , 0.5, (0,0,0), 1)

#         # count the number of faces detected
#         count_faces = str(len(faces))

#         # print out the number of faces detected
#         print ("Number of faces detected: " + count_faces)

#         # Writing processed image in a new window
#         cv2.imshow("Face", frame)
#         if(cv2.waitKey(1)== ord('q')):
#             break

#     # releasing web-cam
#     video_capture.release()
#     # Destroying output window
#     cv2.destroyAllWindows()

#     # Capturing real time video stream. 0 for built-in web-cams, 0 or -1 for external web-cams
#     video_capture = cv2.VideoCapture(0)

#     # Reading image from video stream
#     _, img = video_capture.read()
#     # Call method we defined above
#     img = detect(img, faceCascade, eyesCascade, noseCascade, mouthCascade)
#     # Writing processed image in a new window
#     cv2.imshow("face detection", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # releasing web-cam
# video_capture.release()
# # Destroying output window
# cv2.destroyAllWindows()
# # Capturing real time video stream. 0 for built-in web-cams, 0 or -1 for external web-cams