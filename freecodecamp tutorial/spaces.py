import cv2 as cv

img = cv.imread('../Photos/cube.png')

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey',grey)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

greyhsv = cv.cvtColor(hsv, cv.COLOR_BGR2GRAY)
cv.imshow('greyhsv',greyhsv) # would probably work best for detecting colors on the cube? or like idk difference? it coudl detect where the cube is but it likely won't be able to tell the colorus apart form each other


cv.waitKey(0)