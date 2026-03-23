import cv2
import numpy as np
import os
import random


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0
print (0)

names related to ids: example ==> loze: id=1, etc
names = ['0', '1', '2', '3', '456']
print (1)

#Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

#Define min window size to be recognized as a face
minW = 0.1cam.get(3)
minH = 0.1cam.get(4)

while True:
ret, img =cam.read()
img = cv2.flip(img, 1) # Flip vertically
img1 = cv2.imread('/home/pi/testIMAGE/0')
img2 = cv2.imread('/home/pi/testIMAGE/1')
img3 = cv2.imread('/home/pi/testIMAGE/2')
img4 = cv2.imread('/home/pi/testIMAGE/3')
resize_img1 = cv2.resize(img1, (300, 300))
resize_img2 = cv2.resize(img2, (300, 300))
resize_img3 = cv2.resize(img3, (300, 300))
resize_img4 = cv2.resize(img4, (300, 300))

x=[resize_img1, resize_img2, resize_img3, resize_img4]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print (2)
faces = faceCascade.detectMultiScale( 
    gray,
    scaleFactor = 1.2,
    minNeighbors = 5,
    minSize = (int(minW), int(minH)),
   )

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
    # Check if confidence is less them 100 ==> "0" is perfect match
    if (confidence >= 30):
        id = names[id]
        confidence = "  {0}%".format(round(100 - confidence))
        if (id):
           print ('111111111111111111111')
           A=[resize_img1, resize_img2, resize_img3, resize_img4]
           random.shuffle(A)
           cv2.imshow('test',random.choice(A))
print ('tell')
           cv2.waitKey(10000)
           cv2.destroyWindow('test')
        else:
           print (4444444444444444)
           cv2.waitKey(30000)
           cv2.destroyWindow('test')
           # cv2.destroyAllWindows() # destroys the window showing image

    else:
        id = "unknown"
        confidence = "  {0}%".format(round(100 - confidence))

    cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
    cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  

cv2.imshow('camera',img) 
k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
if k == 27:
    break
#Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
