# 시간을 입력하면 초로 환산하는 프로그램
hour = int(input("시간 입력 : "))
minute = int(input("분 입력 : "))
second = int(input("초 입력 : "))
sum_sec = hour * 60 * 60 + minute * 60 + second
print(format(sum_sec, ',d') + "초")