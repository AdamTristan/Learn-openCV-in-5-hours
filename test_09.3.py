import cv2 as cv
import numpy as np

img = cv.imread("IMG_01.jpg")

rows, cols = img.shape[:2]
M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1) # center angle scale
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('dst', dst)
cv.waitKey(0)