
coffee = 5
while True:
    x = input("돈을 넣어주세요: ")
    money = int(x)

    if money == 400:
        print("커피가 나옵니다.")
        coffee -= 1
    elif money > 400:
        print("커피가 나오고 거스름돈 " + str(money-400) + "원을 돌려줍니다.")
        coffee -= 1
    elif money < 400:
        print("커피가 나오지 않습니다.")

    print("커피의 개수는 " + str(coffee) + "개입니다.")

    if coffee == 0:
        print("커피가 모두 떨어졌습니다. 판매를 중단합니다.")
        break
