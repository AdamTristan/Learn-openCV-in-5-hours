import cv2 as cv
import numpy as np

img = cv.imread("IMG_01.jpg")

rows, cols = img.shape[:2]  # get inverse parameters
M = np.float32([[1, 0, 100], [0, 1, 50]]) # 1 argument with 2 rows
dst = cv.warpAffine(img, M, (cols, rows))  # write forward parameters

cv.imshow('dst', dst)
cv.waitKey(0)