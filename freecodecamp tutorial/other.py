import cv2 as cv
import numpy as np

testimg = cv.imread('Photos/cube.png')

# blur = cv.blur(testimg, (20,20), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny = cv.Canny(testimg, 25, 40)
# cv.imshow("Canny Edge", canny)

grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", gray)

ret, thresh = cv.threshold(testimg, 25, 40, cv.THRESH_BINARY)


cannyblur = cv.Canny(blur, 25, 40)
cv.imshow("Canny & Blur", cannyblur)

dilated = cv.dilate(canny, (20,20), iterations=20)
cv.imshow("Dilated", dilated)

erorded = cv.erode(dilated, (3, 3), iterations=1)

cv.waitKey(0)