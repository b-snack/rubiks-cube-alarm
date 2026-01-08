import pygame

def play_alarm():
  pygame.mixer.init()
  pygame.mixer.music.load("media/alarm.mp3")
  pygame.mixer.music.play(loops=-1)

def stop_alarm():
  pygame.mixer.music.stop()

# os.system("cvlc --play-and-exit alarm.mp3 &") for pi