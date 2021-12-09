import random
import time

try:
    with open('word.txt', 'r') as f:
        word = f.readline().split()
    n = 1   #문제 번호

    print('[타자 게임] 준비되면 엔터')
    input()
    start = time.time()
    while n < 11:
        print("-문제", n)
        q = random.choice(word)  # 문제
        print(q)
        u = input()  # 사용자 입력
        if q == u:
            print("통과!")
            n += 1
        else:
            print("오타! 다시 도전!")
    end = time.time()
    #print("게임 종료!")
    et = end - start
    print('타자 시간 : %.2f초' % et)
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다.")

