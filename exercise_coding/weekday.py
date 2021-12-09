import datetime
import calendar

days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

#오늘 날짜 및 시간 출력
today = datetime.datetime.today()
print(today)

# 오늘 요일
weekday = datetime.datetime.today().weekday()
print(weekday)
print(days[weekday])

# 특정한 날의 요일
xday = datetime.date(2021, 10, 22).weekday()
print(xday)
print(days[xday])

# 달력 사용하기
x = calendar.prmonth(2021, 10)
print(x)

