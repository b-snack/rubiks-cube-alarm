import cv2 as cv
import numpy as np

img = cv.imread('Photos/cube.png')

grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", grayscale)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

ret, thresh = cv.threshold(grayscale, 125, 255, cv.THRESH_BINARY)

cv.imshow("thresh", thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

print(f"{len(contours)} contours found")

cv.waitKey(0)