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

def demo_alarm():
  print("Demo started")
  play_alarm()

  print("Waiting for cube to be detected..")
  while not is_there(photo()):
    time.sleep(1)
  print("Found!")

  print("Waiting to check if solved")
  while not is_solved(photo()):
    time.sleep(1)

  print("Solved!")
  stop_alarm()

if __name__ == "__main__":
  demo_alarm()
