import subprocess

def play_alarm():
  # subprocess.Popen(["cvlc", "--play-and-exit", "--loop", "media/alarm.mp3"])
  print("beep")

def stop_alarm():
  # subprocess.call(["pkill", "vlc"])
  print("Stopped")