import cv2 as cv
import numpy as np

img = cv.imread('Photos/red.png')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow("hsv", hsv)

greyhsv = cv.cvtColor(hsv, cv.COLOR_BGR2GRAY)
cv.imshow("t", greyhsv)

# ================== edge cascades ====================
canny = cv.Canny(greyhsv, 30, 40)
cv.imshow("canny", canny)

dilated = cv.dilate(canny, (4,4), iterations=5)
cv.imshow("dilated", dilated)

# drawing
blank = np.zeros(img.shape, dtype='uint8')

cv.drawContours(blank, contours, -1, (0,0,255),2)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)

# cv.imshow("image", img)

# blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow("Blank", blank)

# grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("grayscale", grayscale)

# blur = cv.GaussianBlur(grayscale, (3,3), cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)

# ret, thresh = cv.threshold(grayscale, 125, 255, cv.THRESH_BINARY)

# cv.imshow("thresh", thresh)
# contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# cv.drawContours(blank, contours, -1, (0,0,255),2)
# cv.imshow("Contours Drawn", blank)

# print(f"{len(contours)} contours found")

