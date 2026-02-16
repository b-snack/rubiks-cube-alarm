import os
from datetime import datetime
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from capture import photo

frame = photo()

  #mask (no white)
COLOR_INFO = {
  'blue': (np.array([100,150,0]), np.array([140,255,255])),
  'green': (np.array([40,50,50]), np.array([80,255,255])), # or 40,50,50,80,255,255
  'orange': (np.array([12, 150, 100]), np.array([18, 255, 255])),
  'yellow': (np.array([22,100,100]), np.array([38,255,255])),
  'red': (None, None)
}

OPPOSITES = {
  "1": ["blue", "green"],
  "2": ["red", "orange"]
  # no white & yelo b/c it doesnt detect white. 
}

def create_media():
  folders = ['media/original', 'media/mask-combined', 'media/contour']
  for folder in folders:
    os.makedirs(folder, exist_ok = True)

def check_opposites(solved_colors, opposite_colors):
  true_false = True

  for pair in opposite_colors.values():
    if pair[0] in solved_colors and pair[1] in solved_colors:
      true_false = False
  
  return true_false
      

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

def calc_params(p1, p2):
  if p2[1] - p1[1] == 0:
    a = 0.0
    b = -1.0
  elif p2[0] - p1[0] == 0:
    a = -1.0
    b = 0.0
  else:
    a = (p2[1] - p1[1])/ (p2[0] - p1[0])
    b = -1.0
  c = (-a * p1[0] - b * p1[1])
  
  return a, b, c

def find_intersection(params1, params2):
  x=-1
  y=-1
  return_value = (int(x), int(y))
  det = params1[0] * params2[1] - params2[0] * params1[1]
  if (det < 0.5 and det > -0.5):
    return_value = (-1, -1)
  else:
    x = (params2[1] * (-params1[2]) - params1[1] * (-params2[2])) / det
    y = (params1[0] * (-params2[2]) - params2[0] * (-params1[2])) / det
    return_value = (int(x), int(y))
  
  return return_value

def is_quadrilateral(mask_image):
  contours, _ = cv.findContours(mask_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
  returnValue = False

  if len(contours) == 0:
    returnValue = returnValue

  else:
    largest_contour = max(contours, key = cv.contourArea)
    hull = cv.convexHull(largest_contour)

    epsilon = 0.02* cv.arcLength( hull, True )
    approx = cv.approxPolyDP(hull, epsilon, True)

    corners = len(approx)
    print(f"{corners} corners found")

    if corners == 4:
      returnValue = True
  
  return returnValue
    

def is_there(frame):
  img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

  #singificant pixels:
  colors_found = 0
  threshold = 500
  kernel = np.ones((7,7), np.uint8)

  # significatn colours
  significant_colours = []

  # count num of colors present
  for color_name, (lower, upper) in COLOR_INFO.items():

    if color_name == "red":
      mask = is_red(color_name, img)
    else:
      mask = cv.inRange(img, lower, upper)

    masked = cv.bitwise_and(frame, frame, mask=mask)

    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=2)
    final_mask = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel, iterations=2)

    if cv.countNonZero(final_mask) > threshold:
      colors_found += 1
      significant_colours.append(color_name)
  
  return_value = False
  if colors_found >= 3:
    return_value = True

  return return_value

def is_solved(frame, save_debug=True):

  if save_debug:
    create_media()
    timestamp = datetime.now().strftime("%m%d_%H:%M:%S")

  hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
  kernel = np.ones((7,7), np.uint8)
  solved_sides = 0
  solved_colors = []

  combined_mask = np.zeros(frame.shape[:2], dtype=np.uint8)
  contour_image = frame.copy()

  for color_name, (lower, upper) in COLOR_INFO.items():
    if color_name == "red":
      mask = is_red(color_name, hsv)
    else:
      mask = cv.inRange(hsv, lower, upper)
    
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=2)
    final_mask = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel, iterations=2)

    combined_mask = cv.bitwise_or(combined_mask, final_mask)

    contours, _ = cv.findContours(final_mask, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
      largest = max(contours, key=cv.contourArea)

      cv.drawContours(contour_image, [largest], -1, (0,255,0), 3)

      if cv.contourArea(largest) > 5000:
        if is_quadrilateral(final_mask):
          if len(contours) == 1 or cv.contourArea(largest) > 0.85*sum(cv.contourArea(c) for c in contours):
            solved_sides += 1
            print(f'{color_name} face solved')
            solved_colors.append(color_name)
        else:
          print(f"{color_name} isnt a quadriatlerial")

<<<<<<< HEAD
  if save_debug:
    cv.imwrite(f'media/original/{timestamp}.jpg', frame)
    cv.imwrite(f'media/mask-combined/{timestamp}.jpg', combined_mask)
    cv.imwrite(f"media/contour/{timestamp}.jpg", contour_image)

  if check_opposites(solved_colors, OPPOSITES) and len(solved_colors) == 3:
    return_value = True
  
  else: 
    return_value = False
=======
  return_value = check_opposites(solved_colors, OPPOSITES)
  if check_opposites(solved_colors, OPPOSITES) and len(solved_colors) == 3:
    return_value = True
  
  else: 
    return_value = False

  print(f"{solved_sides} solved side(s), {return_value}")
>>>>>>> a7033d14cf73674664c85141e1e2599cc126a4e3

  return return_value

if __name__ == "__main__":
  is_solved(frame)

"""
Sources (for future reference):
- https://www.youtube.com/watch?v=oXlwWbU8l2o
- https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
- https://nhuvan.github.io/blog/005-quadrilateral/
"""