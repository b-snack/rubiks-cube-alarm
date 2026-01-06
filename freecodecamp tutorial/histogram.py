import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../Photos/cube.png')
cv.imshow("cube", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('circle', circle)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('mask', mask)

# gray_hist = cv.calcHist([mask], [0], None, [256], [0,256])



plt.figure()
plt.title('grayscale histogram')
plt.xlabel("bins")
plt.ylabel("# of pixels")

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
  hist = cv.calcHist([img], [i], None, [256], [0,256])
  plt.plot(hist, color=col)
  plt.xlim([0,256])

plt.show()

# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel("bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# hist = cv.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
# plt.imshow(hist,interpolation = 'nearest')
# plt.show()


cv.waitKey(0)