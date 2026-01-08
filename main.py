import datetime
import time
import cv2 as cv
import pygame
from detection import is_solved, is_there
from capture import photo
from alarm import play_alarm, stop_alarm

def main():
  running = True
  while running:
    now = datetime.datetime.now()

    if now.hour == 7 and now.minute ==30:
      play_alarm()
      
      while not is_there(photo()):
        time.sleep(2)
      
      while is_solved(photo()) != True:
        time.sleep(2)
      
      stop_alarm()

      time.sleep(61)

    time.sleep(30)

if __name__ == "__main__":
  main()