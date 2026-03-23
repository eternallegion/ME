import cv2
import time
import random
i=0
while i<10:
i=i+1
#read image
img1 = cv2.imread('/home/pi/testIMAGE/0')

#cv2.resize('/home/pi/testIMAGE/0')
img2 = cv2.imread('/home/pi/testIMAGE/1')
img3 = cv2.imread('/home/pi/testIMAGE/2')
img4 = cv2.imread('/home/pi/testIMAGE/3')
print (i)
x=[img1, img2,img3, img4]
random.shuffle(x)
#show image
resize_img1 = cv2.resize(img1, (300, 300))
resize_img2 = cv2.resize(img2, (300, 300))
resize_img3 = cv2.resize(img3, (300, 300))
resize_img4 = cv2.resize(img4, (300, 300))
y=[resize_img1, resize_img2, resize_img3, resize_img4]
random.shuffle(y)
cv2.imshow('0',random.choice(y))

cv2.imshow('1',img2)
cv2.imshow('2',img3)
cv2.imshow('3',img4)
time.sleep (10)
cv2.waitKey(3000)
cv2.destroyWindow('0') #== i==i: # waits until a key is pressed

break cv2.destroyAllWindows() #destroys the window showing image
print (i)
cv2.destroyAllWindows()
