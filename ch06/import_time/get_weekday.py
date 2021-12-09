import datetime

def get_weekday(yyyy, mm, dd):
    days = ["월", "화", "수", "목", "금", "토", "일"]
    theday = datetime.date(yyyy, mm, dd).weekday()
    return days[theday]

yyyy = 2021
mm = 11
dd = 24
weekday = get_weekday(2021, 11, 26)
print("{}년 {}월 {}일은 {}요일입니다.".format(yyyy, mm, dd, weekday))
