import cv2 as cv
import random

def photo():
  cap = cv.VideoCapture(0)
  ret,frame = cap.read() 
  return_value = None

  cap.release()
  
  if ret:
    return_value = frame
  
  return return_value
    

"""
Sources:
- https://stackoverflow.com/questions/4179220/capture-single-picture-with-opencv
"""