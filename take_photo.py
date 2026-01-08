import cv2 as cv
import random

def take_photo():
  cap = cv.VideoCapture(0)
  ret,frame = cap.read() 

  while(True):
    cv.imshow('img1',frame) 
    cv.imwrite(f'Photos/cube{random.randint(3, 500000)}.png',frame)
    cv.destroyAllWindows()
    break

  cap.release()

"""
Sources:
- https://stackoverflow.com/questions/4179220/capture-single-picture-with-opencv
"""