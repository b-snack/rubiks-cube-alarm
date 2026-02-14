import warnings
warnings.filterwarnings("ignore")

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import datetime
import time
import cv2 as cv
from detection import is_solved, is_there
from capture import photo
from alarm import play_alarm, stop_alarm

def main():

  print("Started!")

  running = True
  while running:
    now = datetime.datetime.now()

    if now.hour == 7 and now.minute ==30:
      play_alarm()
      
      while not is_there(photo()):
        time.sleep(5)
      
      while is_solved(photo()) != True:
        time.sleep(5)
      
      stop_alarm()

      time.sleep(61)

    time.sleep(30)

if __name__ == "__main__":
  main()