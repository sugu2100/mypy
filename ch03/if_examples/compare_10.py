# 10을 기준으로 짝수와 홀수 구분

print('수를 입력하세요')
n = int(input())

if n > 10:
    #print("10보다 큰 수입니다.")
    if n % 2 == 0:
        print("10보다 큰 짝수")
    else:
        print("10보다 큰 홀수")
else:
    #print("10이하의 작은 수입니다.")
    if n % 2 == 0:
        print("10이하의 짝수")
    else:
        print("10이하의 홀수")

print("-"*40)

if n > 10 and n % 2 == 0:
    print("10보다 큰 짝수")
elif n > 10 and not n % 2 == 0:
    print("10보다 큰 홀수")
elif n <= 10 and n % 2 == 0:
    print("10이하의 짝수")
elif n <= 10 and not n % 2 == 0:
    print("10이하의 홀수")
