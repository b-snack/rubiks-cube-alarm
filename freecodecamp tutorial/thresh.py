import cv2 as cv
import numpy as np

img = cv.imread('../Photos/cube.png')
cv.imshow('Cube', img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#simple
threshold, thresh = cv.threshold(gray, 190, 255, cv.THRESH_BINARY)
cv.imshow("Threshol", thresh)

# adaptive
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 65, 5)
cv.imshow("adaptive", adaptive_thresh)


cv.waitKey(0)