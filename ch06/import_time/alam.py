import datetime
import time

now = datetime.datetime.now()
now.minute + 90

if now.minute > 60:
    now.hour += now.minute // 60
    print(now.hour, now.minute, now.second)
else:
    print(now.hour, now.minute, now.second)