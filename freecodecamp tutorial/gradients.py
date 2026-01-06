import cv2 as cv
import numpy as np

img = cv.imread('../Photos/cube.png')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("soblex", sobelx)
cv.imshow("sobley", sobely)
cv.imshow("combined", combined_sobel)

# canny
canny = cv.Canny(gray, 0, 40)
cv.imshow("Canny", canny)

cv.waitKey(0)