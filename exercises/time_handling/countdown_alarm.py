import subprocess
import subprocess, time

countdown = 10

while countdown > 0:
    time.sleep(1)
    print(countdown)
    countdown -= 1

subprocess.run(['start', 'gen_files\\alarm.wav'], shell=True)