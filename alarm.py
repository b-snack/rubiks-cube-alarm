import subprocess

def play_alarm():
  subprocess.Popen(["cvlc", "--play-and-exit", "--loop", "media/alarm.mp3"])

def stop_alarm():
  subprocess.call(["pkill", "vlc"])

# def play_alarm():
#   pygame.mixer.init()
#   pygame.mixer.music.load("media/alarm.mp3")
#   pygame.mixer.music.play(loops=-1)

# def stop_alarm():
#   pygame.mixer.music.stop()

# os.system("cvlc --play-and-exit alarm.mp3 &") for pi
