# 숫자 추측 게임
import random

com = random.randint(1, 100)  # 난수
min_v = 1     # 범위 - 최소값
max_v = 100   # 범위 - 최대값
for i in range(0, 10):
    try:  #숫자가 아닌 문자 입력시 에러 처리
        guess = int(input("맞혀보세요([%d회] %d ~ %d) -> " % (i+1, min_v, max_v)))

        if guess > 100 or guess < 1 :
            print("입력 범위가 아니에요. 다시 입력해 주세요: ")
        elif guess == com:
            print("정답!!")
            break
        elif guess > com:
            print("너무 커요!")
            max_v = guess
        else:
            print("너무 작아요!")
            min_v = guess

    except ValueError:
        print("유효한 숫자가 아닙니다. 다시 입력해 주세요")

print("정답 : %d" % guess)
print("점수 : %d점" % ((10 - i) * 10))

