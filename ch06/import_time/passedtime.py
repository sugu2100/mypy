import datetime

# date()함수는 날짜만 출력
print("♠ 지금까지 몇 일? ♠")
day1 = datetime.date(2021, 10, 26)
#print(day1)

today = datetime.date.today()
#print(today)
passedtime = today - day1
print("개강 이후 {0}일이 지났습니다.".format(passedtime.days))

