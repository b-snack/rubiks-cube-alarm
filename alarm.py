import datetime
import os
import time

def alarm():
  running = True
  while running:
    now = datetime.datetime.now()
    if now.hour == 7 and now.minute ==30:
      os.system("start alarm.mp3")
      # os.system("cvlc --play-and-exit alarm.mp3 &") for pi
      time.sleep(61)

    time.sleep(30)
