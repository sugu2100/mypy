
n = int(input("수를 입력하세요 : "))

try:
    div = 10 / n
    print(div)
except ZeroDivisionError as e:
    print(e)
    print("0으로 나눌 수 없습니다.")

