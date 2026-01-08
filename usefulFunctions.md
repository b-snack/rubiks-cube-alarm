## Recording Video & Capturing Images:

```
import cv2 as cv
import sys

capture = cv.VideoCapture(0)

while True:
  isTrue, frame = capture.read()

  frame_resized = rescaleFrame(frame)

  cv.imshow("Video Resized", frame_resized)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()
```

## Drawing a Shapes:

```
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank", blank)

blank[200:300, 300:400] = 0,255,0
cv.imshow("Green", blank)

cv.rectangle(blank, (0,0), (250,250), (0,200,0), 2)
cv.imshow("Rectangle", blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,240,2), thickness=cv.FILLED)
cv.imshow("circle", blank)

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,240,2), thickness=5)
cv.imshow("line", blank)

cv.waitKey(0)
```

## Resizing Frames:

```
def rescaleFrame(frame, scale=0.75):
  # Img, video, live video
  width = int(frame.shape[1] * scale)
  height= int(frame.shape[0] * scale)
  dimensions=(width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
```

## Finding Edges + Blur:

### Will have to adjust based on colour face (I think?)

Edge Cascade:

```
testimg = cv.imread('Photos/test.png')

blur = cv.blur(testimg, (20,20), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

canny = cv.Canny(testimg, 25, 40)
cv.imshow("Canny Edge", canny)

cannyblur = cv.Canny(blur, 25, 40)
cv.imshow("Canny & Blur", cannyblur)

cv.waitKey(0)
```

## Erode & Dilate:

Essentially, thinning & thickening the edges.

```
dilated = cv.dilate(testimg, (kernel, kernel), iterations = n)

eroded = cv.erode(dilated, (kernel, kernel), iterations = k)
```

## Adaptive Thresh - THRESH_MASK will probably be very helpful later on:

```
# adaptive
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 65, 5)
cv.imshow("adaptive", adaptive_thresh)
```
