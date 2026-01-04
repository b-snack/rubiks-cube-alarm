import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank", blank)

# blank[200:300, 300:400] = 0,255,0
# cv.imshow("Green", blank)

# cv.rectangle(blank, (0,0), (250,250), (0,200,0), 2)
# cv.imshow("Rectangle", blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,240,2), thickness=cv.FILLED)
cv.imshow("circle", blank)

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,240,2), thickness=5)
cv.imshow("line", blank)

cv.waitKey(0)

# capture = cv.VideoCapture(0)

# capturing = True
# while capturing:
#   isTrue, frame = capture.read()
  
#   cv.imshow("Video", frame)

#   if cv.waitKey(20) & 0xFF == ord('d'):
#     capturing = False