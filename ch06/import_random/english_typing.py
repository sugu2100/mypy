import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree',
        'strawberry', 'grape', 'garlic', 'onion', 'potato']

n = 1  #문제
input("[타자 게임] 준비되면 엔터!")
start = time.time()
while n < 11:
    print('문제', n)
    question = random.choice(word)
    print(question)
    answer = input()
    if answer == question:
        print("통과!")
        n += 1
    else:
        print("오타! 다시 도전!")
end = time.time()
print("타자 시간 : %.2f초" % (end-start))