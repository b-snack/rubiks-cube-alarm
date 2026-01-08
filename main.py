import datetime
import time
import cv2 as cv
import pygame
from detection import is_solved, is_there
from capture import photo
from alarm import play_alarm, stop_alarm
"""
when 7:30:
  photo()
  def alarm...
    if is this time:
      play sound
        while cube is not there:
          photo()
          time.sleep(3)
        while not solved:
          time sleep (2)
        stop alarm()
      
        

"""

def main():
  running = True
  while running:
    now = datetime.datetime.now()
    img = photo()
    if now.hour == 7 and now.minute ==30:
      play_alarm()
      
      while not is_there(photo()):
        img = photo()
        time.sleep(2)
      
      while not is_solved(photo()):
        img = photo()
        time.sleep(2)
      
      stop_alarm()

      time.sleep(61)

    time.sleep(30)

if __name__ == "__main__":
  main()