import sys

x = input('수를 입력하세요 : ')
n = int(x)

if n == 0:
    print('0으로 나눌 수 없습니다.')
    sys.exit(0)

num = 3 / n

print(num)
