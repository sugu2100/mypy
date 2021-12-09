import random

with open("word.txt", 'w') as f:
    word = ['sky', 'happiness', 'human', 'earth', 'horse', 'cow',
            'penguin', 'description', 'egg', 'banana']

    for w in word:
        f.write(w + " ")

# 단어를 랜덤하게 뽑아내기
with open("word.txt", 'r') as f:
    #word = f.readlines()
    word = f.readline().split()
    w = random.choice(word)
    print(w)
