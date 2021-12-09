import datetime

today = datetime.datetime.today()
print(today)
print("{}년 {}월 {}일".format(today.year, today.month, today.day))
print("{}시 {}분 {}초".format(today.hour, today.minute, today.second))

print(today.strftime("%Y. %m. %d %H:%M:%S"))

"""
KST = datetime.timezone(datetime.timedelta(hours=9))
print(KST)
korea = datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=KST)
print(korea)

TW = datetime.timezone(datetime.timedelta(hours=8))
print(TW)
taiwan = datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=TW)
print(taiwan)
"""