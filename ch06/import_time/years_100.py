# 100세 되는 해의 연도 계산하기
import datetime

today = datetime.date.today()
print(today.year)

age = int(input("나이 입력 : "))

result = today.year + (100 - age)
print("100세 되는 해는 " + str(result) + "년 입니다.")
