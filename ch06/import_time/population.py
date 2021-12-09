# 2021년 현재 한국 인구 - 50,000,000만
# 입력된 년 수 이후의 인구를 출력하는 프로그램
"""
1. 17초마다 한 명 출생
2. 12초마다 한 명 사망
3. 1분 27초마다 1명 입국 이민
4. 3분 51초마다 1명 출국 이민
"""
import datetime

num = int(input("년 수 입력 : "))

year1_sec = 365*24*60*60
birth = year1_sec/17
death = year1_sec/12
in_korea = year1_sec/87
out_korea = year1_sec/231
result = birth - death + in_korea - out_korea

population = 50000000 + round(result * num) # 계산 결과  * 년수
print(str(num) + "년 후의 인구는 " + format(population, ',d') + "명입니다.")
