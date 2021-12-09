import random
import time

w = ['sky', 'earth', 'moon', 'flower', 'tree',
         'strawberry', 'grape', 'garlic','onion', 'potato']

print("[타자 게임]준비되면 엔터!")
input()
start = time.time()

q = random.choice(w)
for n in range(1, 11):
    print('-문제', n)
    print(q)
    x = input()  # 사용자 입력
    if q == x:
        print('통과!')
        #n = n + 1
        q = random.choice(w)  # 새 문제 출제 
    else:
        print('오타! 다시 도전!')

end = time.time()       
et = end - start
print('타자 시간 : %.2f초' % et)
