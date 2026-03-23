import cv2

img = cv2.imread("/home/pi/testIMAGE/0")
print("img.shape = {0}".format(img.shape))

resize_img = cv2.resize(img, (300, 300))

resize_img = cv2.resize(img, (300, 300), interpolation=cv2.INTER_AREA)
resize_img = cv2.resize(img, (0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_AREA)
resize_img = cv2.resize(img, (300, 300), fx=0.3, fy=0.7, interpolation=cv2.INTER_AREA)
print("resize_img.shape = {0}".format(resize_img.shape))

cv2.imshow("img", img)
cv2.imshow("resize img", resize_img)
cv2.waitKey()
