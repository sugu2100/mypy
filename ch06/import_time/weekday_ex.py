import datetime
import calendar

days = ["월", "화", "수", "목", "금", "토", "일"]

# 오늘의 요일
weekday = datetime.datetime.today().weekday()
print(weekday)        #3
print(days[weekday])  #목

# 특정한 날의 요일
theday = datetime.datetime(2021, 10, 26).weekday()
print(days[theday])

# 달력 출력하기
calendar.prmonth(2021, 10)

