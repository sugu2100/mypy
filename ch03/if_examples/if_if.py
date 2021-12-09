"""
print("수를 입력하세요 : ")
n = int(input())
if n > 10:
    #print("10보다 큰 수입니다.")
    if n % 2 == 0:
        print("10보다 큰 짝수입니다.")
    else:
        print("10보다 큰 홀수입니다.")
else:
    #print("10보다 작은 수입니다.")
    if n % 2 == 0:
        print("10이하의 짝수입니다.")
    else:
        print("10이하의 홀수입니다.")

if n > 10 and n % 2 == 0:
    print("10보다 큰 짝수입니다.")
elif n > 10 and n % 2 == 1:
    print("10보다 큰 홀수입니다.")
elif n < 10 and n % 2 == 0:
    print("10보다 작은 짝수입니다.")
else:
    print("10보다 작은 홀수입니다.")
"""





















    


