import cv2 as cv
import numpy as np

img = cv.imread("IMG_01.jpg")

print(img.shape) # 3 for BGR

imgResize = cv.resize(img, (1500, 800))
imgCropped = img[0:1000, 1000:2000] # height comes first

cv.imshow('Original Image', img)
cv.imshow('Resized Image', imgResize)
cv.imshow('Cropped Image', imgCropped)

cv.waitKey(0)