import cv2 as cv
import numpy as np

frame = cv.imread('Photos/cube.png') #using placehodler for now.

  #mask (no white)
COLOR_INFO = {
  'blue': (np.array([100,150,0]), np.array([140,255,255])),
  'green': (np.array([40,50,50]), np.array([80,255,255])), # or 40,50,50,80,255,255
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

  # significatn colours
  significant_colours = []

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
      significant_colours.append(color_name)
  
  return_value = False
  if colors_found >= 3:
    return_value = True

  return return_value

def is_solved(frame):
  hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
  kernel = np.ones((5,5), np.uint8)
  solved_sides = 0

  for color_name, (lower, upper) in COLOR_INFO.items():
    if color_name == "red":
      mask = is_red(color_name, hsv)
    else:
      mask = cv.inRange(hsv, lower, upper)
    
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    final_mask = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)

    contours, _ = cv.findContours(final_mask, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
      largest = max(contours, key=cv.contourArea)

      if cv.contourArea(largest) > 5000:
        if len(contours) == 1 or cv.contourArea(largest) > 0.85*sum(cv.contourArea(c) for c in contours):
          solved_sides += 1
          print(f'{color_name} face solved')
  
  return solved_sides

result = is_there(frame)
print(result)

result1 = is_solved(frame)
print(result1)

cv.waitKey(0)
cv.destroyAllWindows()



"""
Sources (for future reference):
- https://www.youtube.com/watch?v=oXlwWbU8l2o
- https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
"""