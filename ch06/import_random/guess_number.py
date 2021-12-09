# 숫자 추측 게임
import random

com = random.randint(1, 30)
while True:
    guess = int(input("맞혀보세요(1~30): "))

    if guess > 30 or guess <= 0:
        print("입력 범위가 아니에요. 다시 입력해 주세요: ")
    elif guess == com:
        print("정답!!")
        break
    elif guess > com:
        print("너무 커요")
    else:
        print("너무 작아요")

