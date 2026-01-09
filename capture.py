import cv2 as cv

def photo():
  cap = cv.VideoCapture(0, cv.CAP_V4L2)

  for i in range(50):
    cap.read()
  
  ret,frame = cap.read() 
  cap.release()

  return_value = None
  
  if ret:
    return_value = frame
  
  return return_value 
    

"""
Sources:
- https://stackoverflow.com/questions/4179220/capture-single-picture-with-opencv
"""