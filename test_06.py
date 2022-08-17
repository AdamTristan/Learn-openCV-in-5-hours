import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img[200:300, 100:300] = 255, 0, 0

cv.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0))
cv.rectangle(img, (0,0), (250, 350), (0, 0, 255)) # cv.FILLED to fill the area of rectangle
cv.circle(img, (350,250), 50, (255, 255, 0))
cv.putText(img, 'openCV', (100, 80), cv.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1) # scale and thickness

cv.imshow('Original Image', img)

cv.waitKey(0)