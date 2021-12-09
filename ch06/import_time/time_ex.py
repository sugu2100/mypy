import time

print(time.time())      # 현재시간을 초로 반환
print(time.localtime()) # 년,월,일,시,분,초로 반환
print(time.ctime())     # 날짜와 시간 표기 형태

# 년과 일로 환산(1970. 1.1 이후)
year = round(time.time()/(365*24*60*60))
day = round(time.time()/(24*60*60))
print(year)
print(day)

