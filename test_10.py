import cv2 as cv
import numpy as np

img = cv.imread("IMG_01.jpg")

hor = np.hstack((img, img))
ver = np.vstack((img, img))

cv.imshow('Horizontal', hor)
cv.imshow('Vertical', ver)

cv.waitKey(0)