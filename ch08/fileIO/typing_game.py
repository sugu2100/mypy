import random
import time

try:
    with open("word.txt", 'r') as f:
        word = f.read().split()
        #print(word)

    n = 1   # 문제 번호
    print("[타자 게임]준비되면 엔터!")
    input()
    start = time.time()       # 게임 시작 시간

    while n <= 10:
        print('-문제', n)
        q = random.choice(word)  # 문제 출제
        print(q)
        x = input()  # 사용자 입력
        if q == x:
            print('통과!')
            n += 1
        else:
            print('오타! 다시 도전!')

    end = time.time()    # 게임 종료 시간
    et = end - start
    print('타자 시간 : %.2f초' % et)
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다.")
