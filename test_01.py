import cv2
print("package imported")

img = cv2.imread("IMG_01.JPG")

cv2.imshow("Output", img)
cv2.waitKey(0)