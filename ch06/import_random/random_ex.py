
import random
import math

print(random.random()) # 0 <= x < 1

# 주사위
dice = math.floor(random.random() * 6) + 1
print(dice)

dice2 = random.randint(1, 6) # 주사위
print(dice2)

lis = ["강아지", "고양이", "돼지", "말", "소"]

# 리스트에서 무작위로 1개 선택
print(random.choice(lis))

animal = random.choice(lis)
print(animal)

# 리스트의 항목을 무작위로 섞기
random.shuffle(lis)
print(lis)


