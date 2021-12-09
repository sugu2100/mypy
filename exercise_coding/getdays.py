import datetime

def get_days(yyyy, mm, dd):
    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    x = datetime.date(yyyy, mm, dd).weekday()
    return days[x]

# 특정한 날의 요일
yyyy = 2021
mm = 10
dd = 21
weekday = get_days(yyyy, mm, dd)
print("{0}년 {1}월 {2}일은 {3}입니다.".format(yyyy, mm, dd, weekday))


