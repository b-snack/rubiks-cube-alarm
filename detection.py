import cv2 as cv
import numpy as np

frame = cv.imread('Photos/cube2.png') #using placehodler for now.

  #mask (no white)
COLOR_INFO = {
  'blue': (np.array([100,150,0]), np.array([140,255,255])),
  'green': (np.array([100,25,25]), np.array([80,255,255])), # or 40,50,50,80,255,255
  'orange': (np.array([12, 150, 100]), np.array([18, 255, 255])),
  'yellow': (np.array([22,100,100]), np.array([38,255,255])),
  'red': (None, None)
}

# actual thing will need to take a photo first.

def is_red(color_name, image):
  if color_name == 'red':
    lower_red1 = np.array([0,50,50])
    upper_red1 = np.array([10,255,255])
    lower_red2 = np.array([170,50,50])
    upper_red2 = np.array([180,255,255])

    mask1 = cv.inRange(image, lower_red1, upper_red1)
    mask2 = cv.inRange(image, lower_red2, upper_red2)
    mask = cv.bitwise_or(mask1, mask2)
  
  return mask

def is_there(frame):
  img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

  #singificant pixels:
  colors_found = 0
  threshold = 500
  kernel = np.ones((5,5), np.uint8)

  # count num of colors present
  for color_name, (lower, upper) in COLOR_INFO.items():

    if color_name == "red":
      mask = is_red(color_name, img)
    else:
      mask = cv.inRange(img, lower, upper)

    masked = cv.bitwise_and(frame, frame, mask=mask)

    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    final_mask = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)

    cv.imshow(f"{color_name} mask", final_mask)
    cv.imshow(f"{color_name} masked", masked)

    if cv.countNonZero(final_mask) > threshold:
      colors_found += 1
  
  return_value = False
  if colors_found >= 3:
    return_value = True

  return return_value

def is_solved(frame):
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  blurred = cv.GaussianBlur(gray, (5,5), 0)
  edges = cv.Canny(gray, 50, 150)

  cv.imshow("Canny edges", edges)
  
  contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

  min_area = 2000
  threshold = 500
  kernel = np.ones((5,5), np.uint8)
  solved_sides = 0

  for contour in contours:
    perimeter = cv.arcLength(contour, 1)
    approx = cv.approxPolyDP(contour, 0.02 * perimeter, True)

    if len(approx) == 4 and cv.contourArea(contour) > min_area:
      blank = np.zeros(frame.shape[:2], dtype='uint8')
      cv.drawContours(blank, [approx], 0,255, -1)

      side_area = cv.bitwise_and(frame, frame, mask=blank)

      for color_name, (lower, upper) in COLOR_INFO.items():

        if color_name == "red":
          mask = is_red(color_name, frame)
        else:
          mask = cv.inRange(frame, lower, upper)

        masked = cv.bitwise_and(frame, frame, mask=mask)

        opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        final_mask = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)

        if cv.countNonZero(final_mask) >= 0.85*cv.countNonZero(side_area):
          solved_sides += 1

    return_value = False
    if solved_sides == 3:
      return_value = True
    
    return return_value

result = is_there(frame)
print(result)

result1 = is_solved(frame)
print(is_solved(frame))

cv.waitKey(0)
cv.destroyAllWindows()



"""
Sources (for future reference):
- https://www.youtube.com/watch?v=oXlwWbU8l2o
- https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
"""