import cv2 as cv
import numpy as np

frame = cv.imread('Photos/cube2.png') #using placehodler for now.
# actual thing will need to take a photo first.

def is_there(frame):
  img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

  #mask (no white)
  color_info = {
    'blue': (np.array([100,150,0]), np.array([140,255,255])),
    'red': (np.array([0,100,20]), np.array([10,255,255])),
    'green': (np.array([100,25,25]), np.array([80,255,255])),
    'orange': (np.array([10, 100, 20]), np.array([25, 255, 255])),
    'yellow': (np.array([20,100,100]), np.array([40,255,255]))
  }

  #singificant pixels:
  colors_found = 0
  threshold = 500

  # count num of colors present
  for color_name, (lower, upper) in color_info.items():
    mask = cv.inRange(img, lower, upper)
    masked = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow(f"{color_name} mask", mask)
    cv.imshow(f"{color_name} masked", masked)

    if cv.countNonZero(mask) > threshold:
      colors_found += 1
  
  return_value = False
  if colors_found >= 3:
    return_value = True

  return return_value

result = is_there(frame)
print(result)

cv.waitKey(0)
cv.destroyAllWindows()



# archive

## masks
  # blue_mask = cv.inRange(img, [], [])
  # red_mask = cv.inRange(img, [], [])
  # green_mask = cv.inRange(img, [], [])
  # orange_mask = cv.inRange(img, [], [])
  # yellow_mask = cv.inRange(img, [], [])
