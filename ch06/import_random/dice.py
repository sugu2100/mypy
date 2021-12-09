# 주사위 10번 던지기
import random
import math

for x in range(1, 11):
    dice = random.randint(1, 6)
    print(dice, end=' ')
print()

# 랜덤하게 단어 추출하기
words = ['sky', 'earth', 'moon', 'flower', 'tree',
         'strawberry', 'grape', 'garlic','onion', 'potato']
word = random.choice(words)
print(word)

'''
rand = math.floor(random.random() * 6)
print(rand)
print(words[rand])
'''

# guess_number
com = random.randint(1, 30)
while True:
    x = input("맞혀 보세요(1-30): ")
    guess = int(x)
    if guess == com:
        print("정답!")
        break
    elif guess > com:
        print('너무 커요!')
    else:
        print('너무 작아요!')

        