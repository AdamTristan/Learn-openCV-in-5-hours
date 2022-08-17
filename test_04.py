import cv2
import numpy as np

img = cv2.imread("IMG_01.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny_1 = cv2.Canny(img, 100, 100)
imgCanny_2 = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny_1, kernel)
imgEroded = cv2.dilate(imgDialation, kernel)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image_1", imgCanny_1)
cv2.imshow("Canny Image_2", imgCanny_2)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)