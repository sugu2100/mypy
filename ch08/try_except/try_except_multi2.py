
try:
    data = [59, 0, 4, 116, 303]
    x = input("정수 입력(0~4까지 입력해주세요)>")
    num = int(x)
    print(data[num])
except ValueError as e:
    print("값에 문제가 있습니다.")
except IndexError as e:
    print("입력범위가 아닙니다. 0~4까지 입력해주세요")


