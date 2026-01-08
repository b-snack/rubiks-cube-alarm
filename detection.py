import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

frame = cv.imread('Photos/cube.png')

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
  elif p2[0] - p1[1] == 0:
    a = -1.0
    b = 0.0
  else:
    a = (p2[1] - p1[1])/ (p2[0] - p1[0])
    b = -1.0
  c = (-a * p1[0] - b * p1[1])
  
  return a, b, c

def is_quadrilateral(mask_image):

  contours, _ = cv.findContours(mask_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

  convex_hull_img =np.zeros_like(mask_image)
  
  for contour in contours:
    hull = cv.convexHull(contour)
    cv.drawContours(convex_hull_img, [hull], 0, 255, -1)


  minLineLength = min (mask_image.shape[0],mask_image.shape[1])/3
  lines = cv.HoughLinesP(convex_hull_img,mask_image, rho = 1,theta = 1*np.pi/180,threshold = 50, minLineLength = minLineLength,maxLineGap = 50)

  tmp_img = np.zeros((mask_image.shape[0],mask_image.shape[1]), dtype = np.uint8)
  for i in range(lines.shape[0]):
      x1 = lines[i][0][0]
      y1 = lines[i][0][1]    
      x2 = lines[i][0][2]
      y2 = lines[i][0][3]    
      cv.line(tmp_img,(x1,y1),(x2,y2),(255,0,0),2)
  plt.imshow(tmp_img)



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
  solved_colors = []

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
          solved_colors.append(color_name)
  
  return_value = check_opposites(solved_colors, OPPOSITES)

  print(solved_sides, return_value)

  return return_value


"""
Sources (for future reference):
- https://www.youtube.com/watch?v=oXlwWbU8l2o
- https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
- https://nhuvan.github.io/blog/005-quadrilateral/
"""