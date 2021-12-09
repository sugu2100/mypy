import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree',
         'strawberry', 'grape', 'garlic','onion', 'potato']
n = 1   # 문제 번호

print("[타자 게임]준비되면 엔터!")
input()
start = time.time()         #시작 시간
while n < 11:
    print('-문제', n)
    q = random.choice(word)
    print(q)
    u = input()  # 사용자 입력
    if q == u:
        print('통과!')
        n += 1
    else:
        print('오타! 다시 도전!')

end = time.time()        #종료 시간
et = end - start
print('타자 시간 : %.2f초' % et)
