import cv2 as cv
import numpy as np

img = cv.imread("IMG_01.jpg")

res_1 = cv.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv.INTER_CUBIC)
height, width = img.shape[:2]
print(height, width)
res_2 = cv.resize(img, ((1)*width, (1)*height), interpolation = cv.INTER_CUBIC) # This one can't deal with float
cv.imshow('res_1', res_1)
cv.imshow('res_2', res_2)
cv.waitKey(0)