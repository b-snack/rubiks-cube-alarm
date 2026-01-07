import cv2 as cv
import sys

capture = cv.VideoCapture(0)

while True:
  isTrue, frame = capture.read()

  cv.imshow("Video Resized", frame)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()