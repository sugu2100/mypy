# 반복 횟수를 입력받아 출력하는 프로그램

x = input("몇 번 반복할까요? ")
n = int(x)

i = 0
while i < n:
    i += 1
    print(str(i) + "회 반복")

print("반복이 종료되었습니다.")
      
