
while True:
    try:
        x = input("숫자를 입력하세요 : ")
        num = int(x)
        print(num)
        break
    except ValueError:
        print("유효한 숫자가 아닙니다. 다시 입력해 주세요.")
