import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rect',rectangle)
cv.imshow('circle', circle)

# bitwise and -> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise and", bitwise_and)

# bitwise OR -> non intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise OR", bitwise_or)

# bitwise XOR -> non intersecting regions only
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise XOR", bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise NOT", bitwise_not)

# bitwise_and - bitwise_or = bitwise_xor



cv.waitKey(0)