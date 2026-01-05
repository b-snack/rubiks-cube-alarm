import cv2 as cv
import numpy as np

img = cv.imread('Photos/red.png')

cv.imshow("image", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)

grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", grayscale)

blur = cv.GaussianBlur(grayscale, (3,3), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

ret, thresh = cv.threshold(grayscale, 20, 255, cv.THRESH_BINARY)

cv.imshow("thresh", thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank, contours, -1, (0,0,255),2)
cv.imshow("Contours Drawn", blank)

print(f"{len(contours)} contours found")

cv.waitKey(0)