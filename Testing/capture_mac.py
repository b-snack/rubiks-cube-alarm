import cv2 as cv

def photo(debug=False):
  cap = cv.VideoCapture(0)

  for i in range(50):
    cap.read()
  
  ret,frame = cap.read() 
  cap.release()
  
  if ret and debug:
    cv.imwrite("debug_capture.jpg", frame)
    print("saved debug_capture.jpg")
  
  return frame if ret else None
    

if __name__ == "__main__":
  photo(debug=True)

"""
Sources:
- https://stackoverflow.com/questions/4179220/capture-single-picture-with-opencv
"""

