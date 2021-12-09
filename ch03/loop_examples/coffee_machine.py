# 커피 자동 판매기

coffee = 5

while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 400:
        print("커피가 나옵니다")
        coffee -= 1
    elif money > 400:
        print("커피가 나오고, 거스름돈 %d원을 돌려 받습니다." % (money-400))
        coffee -= 1
    else:
        print("커피가 나오지 않습니다.")
    print("남은 커피의 양은 %d개 입니다." % coffee)
    
    if coffee == 0:
        print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
        break
