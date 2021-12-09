# 일정 시간 후에 타이머 종료
import datetime
import threading

def call():
    print(datetime.datetime.now())

print(datetime.datetime.now())
timer = threading.Timer(10, call)
timer.start()